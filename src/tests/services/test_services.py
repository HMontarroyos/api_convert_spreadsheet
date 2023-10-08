import pytest
from src.services.service import DataService
from datetime import datetime
from decimal import Decimal

@pytest.mark.asyncio
async def test_compare_data():
    with open("src/uploads/TESTE_PLANILHA.xlsx", "rb") as f:
        xlsx_data = f.read()

    json_data = await DataService.compare_data(xlsx_data)
    print(json_data)

    assert isinstance(json_data, list)

    expected_data = [
        {
            "id": None,
            "description": "Nota de peças ",
            "transactionDate": datetime(2023, 9, 1).date(),
            "transactionType": "Débito",
            "value": Decimal("300.12"),
            "recipient": "Claudio Pontes Montarr"
        },
        {
            "id": "1593345a-9e7f-449b-b1ab-c9e33a4fea6a",
            "description": "Compra de Componentes Eletrônicos",
            "transactionDate": datetime(2023, 9, 2).date(),
            "transactionType": "Crédito",
            "value": Decimal("300.12"),
            "recipient": "Adele Fonseca"
        }
    ]

    assert len(json_data) == len(expected_data)

    for i in range(len(json_data)):
        assert json_data[i]["id"] == expected_data[i]["id"] or json_data[i]["id"] == 'nan' 
        assert json_data[i]["description"] == expected_data[i]["description"]
        assert json_data[i]["transactionDate"] == expected_data[i]["transactionDate"]
        assert json_data[i]["transactionType"] == expected_data[i]["transactionType"]
        assert round(float(json_data[i]["value"]), 2) == round(float(expected_data[i]["value"]), 2)  # Arredondando para 2 casas decimais
        assert json_data[i]["recipient"] == expected_data[i]["recipient"]
