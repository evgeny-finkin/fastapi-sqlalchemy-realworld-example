from sqlalchemy import Column, Integer, String

from services import postgres


class User(postgres.Base):
    __tablename__ = 'users'

    email = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    bio = Column(String, unique=True, index=True, nullable=False)
    image = Column(String, unique=True, index=True, nullable=False)


# User.metadata.create_all(bind=postgres.engine)
