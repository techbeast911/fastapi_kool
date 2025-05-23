from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db
from src.auth.routes import auth_router
from fastapi.middleware.cors import CORSMiddleware




@asynccontextmanager
async def life_span(app: FastAPI):
    print(f"server is starting......")
    await init_db()
    yield
    print(f"server is shutting down......")

version = "v1"
app= FastAPI(
    title = "KoolBoks API",
    description = "A simple RESTful API for managing data",
    version=version,lifespan=life_span
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(book_router,prefix=f"/api/{version}/koolboks",tags=["koolboks"])
app.include_router(auth_router,prefix=f"/api/{version}/auth",tags=["auth"])