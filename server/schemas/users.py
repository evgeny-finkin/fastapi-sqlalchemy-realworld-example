from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UpdatedUser(BaseModel):
    username: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
    bio: Optional[str]
    image: Optional[HttpUrl]


class NewUser(BaseModel):
    username: str
    email: EmailStr
    password: str
    bio: Optional[str]
    image: Optional[HttpUrl]

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    username: str
    email: EmailStr
    bio: Optional[str]
    image: Optional[HttpUrl]

    class Config:
        orm_mode = True


class AuthenticationUser(BaseModel):
    email: EmailStr
    password: str


class RequestUser(BaseModel):
    email: EmailStr
    password: str
    username: str

    class Config:
        orm_mode = True


class User(BaseModel):
    email: EmailStr
    token: str
    username: str
    bio: str
    image: HttpUrl

    class Config:
        orm_mode = True
