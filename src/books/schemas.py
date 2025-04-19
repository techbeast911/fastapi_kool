from pydantic import BaseModel
from uuid import UUID, uuid4
from datetime import datetime

class Book(BaseModel):
    
    product_serial_no: int
    date_logged_in: datetime
    product_sku: str
    product_category: str
    client_name: str
    date_logged_out: datetime
    

class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str