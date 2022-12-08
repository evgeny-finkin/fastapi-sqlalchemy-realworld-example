from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from services import postgres
from sqlalchemy_utils import EmailType

from .mixins import Timestamp


class Artical(Timestamp, postgres.Base):
    __tablename__ = 'articals'

    title = Column(String, nullable=False, primary_key=True)
    description = Column(String, nullable=False)
    body = Column(String, nullable=False)
    tagList = Column(String)
    author_email = Column(EmailType, ForeignKey('users.email'))

    comments = relationship("Comment", back_populates="artical")
    author = relationship("User", back_populates="articals", uselist=False)
    followers = relationship("User", back_populates="followed_articals")
