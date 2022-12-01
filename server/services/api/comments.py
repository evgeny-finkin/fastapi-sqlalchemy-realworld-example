from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import EmailStr

from schemas import UpdatedArticle
from models import aricles


async def add_comment(session: AsyncSession, slug: str):
    print('comment added')
# return


async def get_comments(session: AsyncSession, slug: str):
    print('comment returnd')


async def delete_comment(session: AsyncSession, slug: str):
    print('comment deleted')
# return


async def favorite_article(session: AsyncSession, slug: str):
    print('article is now favorite')
# return


async def unfavorite_article(session: AsyncSession, slug: str):
    print('article is now unfavorite')
# return
