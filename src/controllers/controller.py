from fastapi import APIRouter, File, UploadFile, HTTPException
from model.model import DataModel, JSONResponseModel
from services.service import DataService

router = APIRouter()

@router.post("/spreadsheet/")
async def process_xlsx(file: UploadFile = File(...)):
    try:
        xlsx_data = await file.read()

        data = await DataService.compare_data(xlsx_data)

        for item in data:
            if 'id' not in item or not item['id']:
                item['id'] = None

        json_data = JSONResponseModel(data=[DataModel(**item) for item in data])

        return json_data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

