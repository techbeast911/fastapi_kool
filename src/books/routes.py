from fastapi import APIRouter, HTTPException, status,Depends
from typing import Optional,List,Dict
from src.db.main import get_session

from src.books.schemas import Record,RecordCreate,RecordUpdateModel
#from src.db import get_db_connection
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from psycopg2.extras import RealDictCursor
from src.books.service import get_records


book_router = APIRouter()
record_service = get_records()



# @book_router.get("/",response_model=List[Book])
# async def get_all_books(session:AsyncSession = Depends(get_session)) -> List[Dict]:
    
#     return books


@book_router.get("/")#,response_model=List[Record])
async def get_all_records(session:AsyncSession = Depends(get_session)):
    records = await record_service.get_all_records(session)
    return records

# @book_router.post("/", status_code=status.HTTP_201_CREATED)
# async def create_a_book(record_data: RecordCreate,
# session:AsyncSession = Depends(get_session)) -> dict:
#     new_record = await record_service.create_record(record_data,session)
    
#     return new_record

@book_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_a_book(record_data: RecordCreate, session: AsyncSession = Depends(get_session)) -> dict:
    new_record = await record_service.create_record(record_data, session)
    return new_record  # ✅ JSON-serializable dictionary


@book_router.get("/{product_serial_no}")
async def get_book(product_serial_no: int,session:AsyncSession = Depends(get_session)) -> dict:
    record = await record_service.get_record_by_id(product_serial_no,session)

    if record:
        return record
    else:
        raise HTTPException(status_code=404, detail="Record not found")

@book_router.patch("/{product_serial_no}")
async def update_books(product_serial_no: int, record_update_data: RecordUpdateModel,
session:AsyncSession = Depends(get_session)) -> dict:
    updated_record = await record.service.update_record(product_serial_no,record_update_data,session)
    
    if updated_record:
        return updated_record
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Record not found")

@book_router.delete("/{product_serial_no}")
async def delete_books(product_serial_no: int):
    record_to_delete = await record_service.delete_record(product_serial_no,session)

    if record_to_delete:
        return None

    else:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Record Not found")