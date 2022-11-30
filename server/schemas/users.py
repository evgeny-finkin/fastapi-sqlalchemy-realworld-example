from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    ...


class User(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True
