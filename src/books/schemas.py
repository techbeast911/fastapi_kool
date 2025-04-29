from pydantic import BaseModel
from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional 

class Record(BaseModel):
    
    product_serial_no: int
    date_logged_in: datetime
    product_sku: str
    product_category: str
    client_name: str
    date_logged_out: datetime
    
class RecordCreate(BaseModel):
    product_serial_no: int
    date_logged_in: datetime
    product_sku: str
    product_category: str
    client_name: str
    date_logged_out: datetime

class RecordUpdateModel(BaseModel):
    product_serial_no: Optional[int] = None
    date_logged_in: Optional[datetime] = None
    product_sku: Optional[str] = None
    product_category: Optional[str] = None
    client_name: Optional[str] = None
    date_logged_out: Optional[datetime] = None