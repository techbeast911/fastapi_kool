from sqlmodel import Field, SQLModel, Relationship, Column
from sqlalchemy.dialects import postgresql as pg
from typing import Optional, List
from datetime import datetime
import uuid

# Define the User model
class User(SQLModel, table=True):
    __tablename__ = "user"
    __schema__ = "public"
    uuid: uuid.UUID = Field(sa_column= Column(
        pg.UUID,nullable= False,primary_key =True,default= uuid.uuid4)
    )
    username: str = Field(index=True, unique=True, nullable=False)
    email: str = Field(index=True, unique=True, nullable=False)
    password: str = Field(nullable=False)
    first_name: str = Field(nullable=False)
    last_name: str = Field(nullable=False)
    is_verified: bool = Field(default=False)
    created_at: datetime = Field(sa_column= Column(
        pg.TIMESTAMP, nullable=False, default=datetime.now))
    updated_at: datetime = Field(sa_column= Column(
        pg.TIMESTAMP, nullable=False, default=datetime.now))


    def __repr__(self):
        return f"<User {self.username}>"