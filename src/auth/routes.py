from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session
from .schemas import UserCreateModel, UserModel,UserLoginModel
from .service import UserService
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from .utils import create_access_token, decode_token,verify_password
from datetime import timedelta

auth_router = APIRouter()
user_service = UserService()

REFRESH_TOKEN_EXPIRY = 2

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



@auth_router.post('/login')
async def login_users(login_data : UserLoginModel,
session: AsyncSession = Depends(get_session)):
    
    email = login_data.email
    password = login_data.password

    user = await user_service.get_user_by_email(email,session)

    if user is not None:
        password_valid = verify_password(password,user.password_hash)

        if password_valid:
            access_token = create_access_token(
                user_data = {
                    'email':user.email,
                    'user_uid': str(user.uid)
                }
            )

            refresh_token= create_access_token(
                user_data = {
                    'email':user.email,
                    'user_uid': str(user.uid)
                },
                refresh = True,
                expiry = timedelta(days=REFRESH_TOKEN_EXPIRY)
            )

            return JSONResponse(
                content ={
                    "message": "Login Successful",
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "user":{
                        "email":user.email,
                        "uid" : str(user.uid)
                    }
                }
            )

    raise HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Invalid Email Or Password"
    )