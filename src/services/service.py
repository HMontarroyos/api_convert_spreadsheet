import openpyxl
from io import BytesIO
from model.model import DataModel
from typing import List
from datetime import date

def convert_data_to_json(data: List[DataModel]) -> List[dict]:
    return [item.model_dump() for item in data]

class DataService:
    @staticmethod
    async def compare_data(xlsx_data: bytes):
        required_fields = [
            "description",
            "transactionDate",
            "transactionType",
            "value",
            "recipient",
        ]

        json_transactions = []  

        workbook = openpyxl.load_workbook(BytesIO(xlsx_data), read_only=True)
        sheet = workbook.active

        header = [cell.value for cell in sheet[1]]

        column_indices = {field: header.index(field) if field in header else None for field in required_fields}

        for row in sheet.iter_rows(values_only=True):
            transaction_data = DataModel(
                id=str(row[column_indices["id"]]) if "id" in column_indices and row[column_indices["id"]] else None,
                description=str(row[column_indices["description"]]) if "description" in column_indices and row[column_indices["description"]] else None,
                transactionDate=row[column_indices["transactionDate"]],
                transactionType=str(row[column_indices["transactionType"]]) if "transactionType" in column_indices and row[column_indices["transactionType"]] else None,
                value=row[column_indices["value"]],
                recipient=str(row[column_indices["recipient"]]) if "recipient" in column_indices and row[column_indices["recipient"]] else None
            )
        
            if transaction_data.id is not None and not isinstance(transaction_data.id, str):
                raise ValueError(f"O campo 'id' deve ser uma string ou None, não {type(transaction_data.id).__name__}")

            invalid_keys = [field for field in required_fields if not hasattr(transaction_data, field)]

            if invalid_keys:
                raise ValueError(f"Chaves inválidas encontradas: {', '.join(invalid_keys)}")

            missing_fields = [field for field in required_fields if not hasattr(transaction_data, field)]

            if missing_fields:
                raise ValueError(f"Campos obrigatórios ausentes: {', '.join(missing_fields)}")

            if transaction_data.transactionType not in {'Débito', 'Crédito'}:
                raise ValueError(f"Tipo de transação inválido: {transaction_data.transactionType}")

            if not isinstance(transaction_data.value, (int, float)):
                raise ValueError(f"Valor inválido: {transaction_data.value}")

            transaction = {
                "description": transaction_data.description,
                "transactionDate": transaction_data.transactionDate,
                "transactionType": transaction_data.transactionType,
                "value": transaction_data.value,
                "recipient": transaction_data.recipient or None,
            }

            json_transactions.append(transaction)

        return json_transactions
