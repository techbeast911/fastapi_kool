from fastapi import APIRouter, Depends
from fastapi import FastAPI,status, HTTPException 
from pydantic import BaseModel, Field
from typing import Optional, List
from src.quality.schemas import Record, RecordUpdateModel, RecordCreate
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.main import get_session 
from src.quality.service import get_records
from src.quality.models import quality
from sqlalchemy import select, desc


quality_router = APIRouter()
quality_service = get_records()




@quality_router.get("/quality")
async def get_quality(session: AsyncSession = Depends(get_session)):
    records = await quality_service.get_all_records(session)
    return records


@quality_router.post("/quality", status_code=status.HTTP_201_CREATED)
async def create_quality(record_data: RecordCreate, session: AsyncSession = Depends(get_session)) -> dict:
    new_record = await quality_service.create_record(record_data, session)
    return new_record

@quality_router.patch("/quality/{serial_number}")
async def update_quality(serial_number: str, record_update_data: RecordUpdateModel,
session:AsyncSession = Depends(get_session)) -> dict:
    updated_record = await quality_service.update_record(serial_number, record_update_data, session)
    
    if updated_record:
        return updated_record
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Record not found")

@quality_router.get("/quality/{serial_number}")
async def get_quality_by_serial_number(serial_number: str,session:AsyncSession = Depends(get_session)) -> dict:

    record = await record_service.get_record_by_id(serial_number,session)

    if record:
        return record
    else:
        raise HTTPException(status_code=404, detail="Record not found")

@quality_router.delete("/quality/{serial_number}")
async def delete_quality(serial_number: str):
    record_to_delete = await record_service.delete_record(serial_number,session)

    if record_to_delete:
        return None

    else:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Record Not found")