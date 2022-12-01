from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional


class UserBase(BaseModel):
    email: EmailStr


class NewUser(BaseModel):
    username: str
    email: EmailStr
    password: str
    bio: Optional[str]
    image: Optional[HttpUrl]


class AuthenticationUser(BaseModel):
    email: EmailStr
    password: str


class User(BaseModel):
    email: EmailStr
    token: str
    username: str
    bio: str
    image: HttpUrl

    class Config:
        orm_mode = True
