from fastapi import APIRouter, HTTPException, status
from typing import Optional,List,Dict

from src.books.book_data import books
from src.books.schemas import Book,BookUpdateModel
#from src.db import get_db_connection
from psycopg2.extras import RealDictCursor


book_router = APIRouter()




# @book_router.get("/",response_model=List[Book])
# async def get_all_books() -> List[Dict]:
#     conn= get_db_connection()
#     cursor = conn.cursor(cursor_factory=RealDictCursor)
#     cursor.execute("SELECT * FROM users")
#     users = cursor.fetchall()  # Fetch all rows
#     return users


@book_router.post("/",status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data:Book) -> dict:
    new_book = book_data.model_dump()

    books.append(new_book)
    return new_book 

@book_router.get("/{book_id}")
async def get_book(book_id:int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(status_code=404,detail="Book not found")

@book_router.patch("/{book_id}")
async def update_books(book_id:int,book_update_data:BookUpdateModel) -> dict:
    for book in books:
        if book["id"] == book_id:
            book["title"] = book_update_data.title
            book["author"] = book_update_data.author
            book["publisher"] = book_update_data.publisher
            book["published_date"] = book_update_data.published_date
            book["page_count"] = book_update_data.page_count
            book["language"] = book_update_data.language 
            return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")

@book_router.delete("/{book_id}")
async def delete_books(book_id:int,status_code=status.HTTP_204_NO_CONTENT) -> dict:
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message":"Book deleted successfully"}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")