from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import EmailStr

from schemas import NewUser, AuthenticationUser, UpdatedUser
# from models import Profiles


async def get_profile(session: AsyncSession, username: str):
    print('get profile')
    # return


async def follow(session: AsyncSession, username: str):
    print('add follower')
    # return


async def unfollow(session: AsyncSession, username: str):
    print('removed follower')
# return
