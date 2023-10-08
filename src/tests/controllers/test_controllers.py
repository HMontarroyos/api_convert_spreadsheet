import httpx
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_process_xlsx():
    with open("src/uploads/TESTE_PLANILHA.xlsx", "rb") as f:
        files = {"file": ("TESTE_PLANILHA.xlsx", f)}

        response = client.post("/spreadsheet/", files=files)
        assert response.status_code == 200

        json_data = response.json()
        assert "data" in json_data
        assert isinstance(json_data["data"], list)

