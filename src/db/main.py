from sqlmodel import SQLModel, create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from src.config import Config

# Correct async engine creation
async_engine = create_async_engine(
    url=Config.DATABASE_URL,
    echo=True,
    future=True
)

async def init_db():
    async with async_engine.begin() as conn:
        # Create schemas if they don't exist
        await conn.execute(text("CREATE SCHEMA IF NOT EXISTS quality"))
        await conn.execute(text("CREATE SCHEMA IF NOT EXISTS public"))
        
        # Create all tables
        from src.books.models import inventory
        #await conn.run_sync(inventory.__table__.create)
        from src.quality.models import quality
        #await conn.run_sync(quality.__table__.create)
        await conn.run_sync(SQLModel.metadata.create_all)
        #await conn.run_sync(lambda sync_conn: inventory.__table__.create(sync_conn, checkfirst=True))
        #await conn.run_sync(lambda sync_conn: quality.__table__.create(sync_conn, checkfirst=True))

async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        bind=async_engine,
        expire_on_commit=False,
        class_=AsyncSession
    )
    async with async_session() as session:
        yield session