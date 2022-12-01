from sqlalchemy import Column, Integer, String

from services import postgres


class comments(postgres.Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, index=True)
    createdAt = Column(String, unique=True, index=True, nullable=False)
    updatedAt = Column(String, unique=True, index=True, nullable=False)
    body = Column(String, unique=True, index=True, nullable=False)
    author = Column(String, unique=True, index=True, nullable=False)
