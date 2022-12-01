from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional, List


class Profile(BaseModel):
    username: str
    bio: str
    image: HttpUrl
    following: List[str]

    class Config:
        orm_mode = True
