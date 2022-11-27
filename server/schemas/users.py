from pydantic import BaseModel, EmailStr
from typing import Optional


class User(BaseModel):
    isActive: bool
    email: EmailStr
    bio: Optional[str]
