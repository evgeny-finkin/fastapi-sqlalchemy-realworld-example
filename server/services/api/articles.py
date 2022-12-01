from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import EmailStr

from schemas import UpdatedArticle
from models import aricles


async def get_articles_by_tegs(
        session: AsyncSession,
        limit: int = 20,
        offset: int = 0,
        tag: str = None,
        author: str = None,
        favorited: str = None):
    print('get articles')
    # return


async def get_article(session: AsyncSession, slug: str):
    print('get article')
    # return


async def get_articles_by_feed(session: AsyncSession, limit: int = 20, offset: int = 0):
    print('get articles')
    # return


async def create_article(session: AsyncSession, username: str):
    print('article created')
# return


async def create_article(session: AsyncSession, slug: str):
    print('article updeted')
# return


async def update_article(session: AsyncSession, slug: str, updated_article: UpdatedArticle):
    print('article upsated')
# return


async def delete_article(session: AsyncSession, slug: str):
    print('article deleted')
# return
