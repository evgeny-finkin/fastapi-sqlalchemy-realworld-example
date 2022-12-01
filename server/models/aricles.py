from sqlalchemy import Column, Integer, String

from services import postgres


class Articals(postgres.Base):
    __tablename__ = 'articals'

    slug = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, unique=True, index=True, nullable=False)
    body = Column(String, unique=True, index=True, nullable=False)
    tagList = Column(String, unique=True, index=True, nullable=False)
    createdAt = Column(String, unique=True, index=True, nullable=False)
    updatedAt = Column(String, unique=True, index=True, nullable=False)
    favorited = Column(String, unique=True, index=True, nullable=False)
    favoritesCount = Column(String, unique=True, index=True, nullable=False)
    author = Column(String, unique=True, index=True, nullable=False)
