from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import EmailStr

from schemas import NewUser, AuthenticationUser
from models import User


async def get_user(session: AsyncSession, email: EmailStr):
    query = select(User).where(User.email == email)
    result = await session.execute(query)
    user = result.scalar_one_or_none()
    return user


def get_users(session: Session, skip: int, limit: int):
    users = session.query(User).offset(skip).limit(limit).all()
    return users


def authentication(session: Session, authentication_user: AuthenticationUser):
    print('user is autanticated')
    return True


def create_user(session: Session, new_user: NewUser):
    print('new user created')
    # return db_user
