from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import URLType, EmailType

from services import postgres


class User(postgres.Base):
    __tablename__ = 'users'

    email = Column(EmailType, primary_key=True, unique=True, index=True)
    username = Column(String, nullable=False)
    bio = Column(String)
    image = Column(URLType)
    password = Column(String, nullable=False)

    articals = relationship("Artical", back_populates="author")
    comments = relationship("Comment", back_populates="author")
    followed_profiles = relationship(
        "FollowedProfile", back_populates="followers")
    followed_articals = relationship("Artical", back_populates="followers")
    followed_comments = relationship("Comment", back_populates="followers")


# User.metadata.create_all(bind=postgres.engine)
