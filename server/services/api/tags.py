from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import EmailStr

from schemas import UpdatedArticle
from models import aricles


async def get_tags(session: AsyncSession):
    print('tages returnd')
# return
