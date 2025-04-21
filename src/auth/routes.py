from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session
from .schemas import UserCreateModel, UserModel
from .service import UserService
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

auth_router = APIRouter()
user_service = UserService()

@auth_router.post("/signup",response_model=UserModel,status_code=status.HTTP_201_CREATED)
async def create_user_account(user_data: UserCreateModel,
session: AsyncSession= Depends(get_session)):
    #print(user_data)
    email = user_data.email

    user_exists = await user_service.user_exists(email, session)

    if user_exists:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="User already exists")

    new_user = await user_service.create_user(user_data, session)

    return new_user



# from fastapi import APIRouter, Depends, status, HTTPException
# from sqlalchemy.ext.asyncio import AsyncSession
# from fastapi.responses import JSONResponse

# from .schemas import UserCreateModel, UserModel
# from .service import UserService
# from src.db.main import get_session

# auth_router = APIRouter()
# user_service = UserService()

# @auth_router.post("/signup", response_model=UserModel, status_code=status.HTTP_201_CREATED)
# async def create_user_account(
#     user_data: UserCreateModel,
#     session: AsyncSession = Depends(get_session)
# ):
#     email = user_data.email

#     user_exists = await user_service.user_exists(email, session)
#     if user_exists:
#         raise HTTPException(
#             status_code=status.HTTP_409_CONFLICT,
#             detail="User already exists"
#         )

#     new_user = await user_service.create_user(user_data, session)
#     return new_user
