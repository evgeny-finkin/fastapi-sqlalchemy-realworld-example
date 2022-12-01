from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional, List

from .users import User


class Comment(BaseModel):
    id: int
    body: str
    author: User
