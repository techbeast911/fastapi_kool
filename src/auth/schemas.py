from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
import uuid
from typing import Optional, List   
from datetime import datetime



class UserCreateModel(BaseModel):
    username: str = Field(max_length=50, min_length=3)
    email: str = Field(max_length=50)
    password: str = Field(max_length=50, min_length=8)
    first_name: str = Field(max_length=50, min_length=3)
    last_name: str = Field(max_length=50, min_length=3)



class UserModel(BaseModel):
    uid: uuid.UUID 
    username: str 
    email: str 
    password_hash: str = Field(exclude=True)
    first_name: str 
    last_name: str 
    is_verified: bool 
    created_at: datetime 
    updated_at: datetime 