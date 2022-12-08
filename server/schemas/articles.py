from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional, List


class Author (BaseModel):
    username: str
    bio: str
    image: Optional[HttpUrl]
    following: List[str]


class Article (BaseModel):
    slug: str
    title: str
    description: str
    body: str
    tagList: List[str]
    favorited: bool
    favoritesCount: int
    author: Author

    class Config:
        orm_mode = True


class UpdatedArticle(BaseModel):
    title: Optional[str]
    description: Optional[str]
    body: Optional[str]
