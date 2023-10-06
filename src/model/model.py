from pydantic import BaseModel
from typing import List, Union
from datetime import date

class DataModel(BaseModel):
    id: str
    description: str
    transactionDate: date
    transactionType: Union[str, str]
    value: float
    recipient: str | None

class JSONResponseModel(BaseModel):
    data: List[DataModel]