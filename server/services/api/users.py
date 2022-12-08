from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import insert, update
from pydantic import EmailStr

from schemas import NewUser, AuthenticationUser, UpdatedUser
from models import User


def test():
    return {'hello': 'world'}


async def get_user(session: AsyncSession, email: EmailStr):
    query = select(
        User.username,
        User.email,
        User.bio,
        User.image,
        User.password
    ).where(User.email == email)
    result = await session.execute(query)
    user = result.first()
    return user


def get_users(session: Session, skip: int, limit: int):
    users = session.query(User).offset(skip).limit(limit).all()
    return users


def authentication(session: Session, authentication_user: AuthenticationUser):
    print('new user created')
    return True


async def create_user(session: AsyncSession, new_user: NewUser):
    query = insert(User).values(
        username=new_user.username,
        email=new_user.email,
        password=new_user.password,
        bio=new_user.bio,
        image=new_user.image
    )
    await session.execute(query)
    await session.commit()


async def update_user(session: AsyncSession, updated_user: UpdatedUser):
    query = update(User).where(User.email == updated_user.email).values(
        username=updated_user.username or User.username,
        email=updated_user.email or User.email,
        password=updated_user.password or User.password,
        bio=updated_user.bio or User.bio,
        image=updated_user.image or User.image
    ).execution_options(synchronize_session=False)
    await session.execute(query)
    await session.commit()
