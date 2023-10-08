from datetime import datetime
import pandas as pd
from io import BytesIO
from model.model import DataModel
from typing import List

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

        df = pd.read_excel(BytesIO(xlsx_data))

        for _, row in df.iterrows():
            id_value = row.get("id")

            transaction_data = DataModel(
                id=str(id_value) if id_value is not None else None,
                description=row["description"],
                transactionDate=datetime(
                    year=row["transactionDate"].year,
                    month=row["transactionDate"].month,
                    day=row["transactionDate"].day
                ).date(),
                transactionType=str(row["transactionType"]),
                value=float(row["value"]),
                recipient=str(row["recipient"])
            )

        
            if transaction_data.id is not None and not isinstance(transaction_data.id, str):
                raise ValueError(f"The 'id' field must be a string, not {type(transaction_data.id).__name__}")

            invalid_keys = [field for field in required_fields if not hasattr(transaction_data, field)]

            if invalid_keys:
                raise ValueError(f"Invalid keys found: {', '.join(invalid_keys)}")

            missing_fields = [field for field in required_fields if not hasattr(transaction_data, field)]

            if missing_fields:
                raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")

            if transaction_data.transactionType not in {'Débito', 'Crédito'}:
                raise ValueError(f"Invalid transaction type: {transaction_data.transactionType} Enter a valid transactionType such as Débito or Crédito")

            if not isinstance(transaction_data.value, (int, float)):
                raise ValueError(f"Invalid value: {transaction_data.value}")

            transaction = {
                "description": transaction_data.description,
                "transactionDate": transaction_data.transactionDate,
                "transactionType": transaction_data.transactionType,
                "value": transaction_data.value,
                "recipient": transaction_data.recipient or None,
            }

            json_transactions.append(transaction)

        return json_transactions
