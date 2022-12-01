from sqlalchemy import Column, Integer, String

from services import postgres


class Profiles(postgres.Base):
    __tablename__ = 'profiles'

    username = Column(Integer, primary_key=True, index=True)
    bio = Column(String, unique=True, index=True, nullable=False)
    image = Column(String, unique=True, index=True, nullable=False)
    following = Column(String, unique=True, index=True, nullable=False)
