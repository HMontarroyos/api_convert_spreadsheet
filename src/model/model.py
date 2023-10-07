from pydantic import BaseModel
from typing import List, Union, Optional
from datetime import date

class DataModel(BaseModel):
    id: Optional[str]
    description: str
    transactionDate: date
    transactionType: str
    value: float
    recipient: str

class JSONResponseModel(BaseModel):
    data: List[DataModel]