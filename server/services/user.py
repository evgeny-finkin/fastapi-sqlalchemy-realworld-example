from sqlalchemy.orm import Session

from schemas import UserCreate
from models import User


def get_user(session: Session, user_id: int):
    user = session.query(User).filter(User.id == user_id).first()
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
