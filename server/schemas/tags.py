from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional, List


class Tag(BaseModel):
    tag_name: str

    class Config:
        orm_mode = True
