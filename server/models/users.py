from sqlalchemy import Column, Integer, String

from services import postgres


class User(postgres.Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)


# User.metadata.create_all(bind=postgres.engine)
