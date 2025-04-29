from fastapi import FastAPI,status, HTTPException 
from pydantic import BaseModel, Field
from typing import Optional, List




class Record(BaseModel):
    date_received: str
    serial_number:int
    product_sku:str
    performance: int
    accessories_checking: str
    status: str
    officer_that_passed_unit: str
    date_passed_to_inventory: str


class RecordCreate(BaseModel):
    date_received: str
    serial_number:int
    product_sku:str
    performance: int
    accessories_checking: str
    status: str
    officer_that_passed_unit: str
    date_passed_to_inventory: str


class RecordUpdateModel(BaseModel):
    date_received: str
    product_sku:str
    performance: int
    accessories_checking: str
    status: str
    officer_that_passed_unit: str
    date_passed_to_inventory: str