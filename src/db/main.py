# from sqlmodel import SQLModel, create_engine,text
# from sqlalchemy.ext.asyncio import AsyncEngine

# from src.config import Config
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.orm import sessionmaker
# from contextlib import asynccontextmanager



# engine = AsyncEngine(
#     create_engine(
#     url=Config.DATABASE_URL,
#     echo=True
    
# ))

# async def init_db():
#     async with engine.begin() as conn:
#         from src.books.models import inventory

#         await conn.run_sync(SQLModel.metadata.create_all)

# @asynccontextmanager
# async def get_session() -> AsyncSession:
#     async with async_session_maker() as session:
#         yield session
      

from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from typing import AsyncGenerator
from src.config import Config

# ✅ Correct async engine creation
engine = create_async_engine(Config.DATABASE_URL, echo=True)

# ✅ Correct sessionmaker
async_session_maker = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# ✅ Init DB function
async def init_db():
    async with engine.begin() as conn:
        from src.books.models import inventory  # if needed for metadata
        await conn.run_sync(SQLModel.metadata.create_all)

# ✅ Dependency for FastAPI
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
