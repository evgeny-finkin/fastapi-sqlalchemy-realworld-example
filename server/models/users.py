from sqlalchemy import Column, Integer, String

from ..services.postgres import Base, engine


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)


User.Base.metadata.create_all(bind=engine)
