from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from schemas import UserCreate
from models import User


async def get_user(session: AsyncSession, user_id: int):
    query = select(User).where(User.id == user_id)
    result = await session.execute(query)
    user = result.scalar_one_or_none()
    return user


def get_users(session: Session, skip: int, limit: int):
    users = session.query(User).offset(skip).limit(limit).all()
    return users


def create_user(session: Session, user: UserCreate):
    db_user = User(email=user.email)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user
