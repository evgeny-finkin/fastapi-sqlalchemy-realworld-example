from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from services import postgres
from sqlalchemy_utils import EmailType

from .mixins import Timestamp


class Comment(Timestamp, postgres.Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    artical_title = Column(String, ForeignKey(
        'articals.title'), nullable=False)
    body = Column(String, unique=True, index=True, nullable=False)
    author_email = Column(EmailType, ForeignKey('users.email'))

    author = relationship("User", back_populates="comments", uselist=False)
    artical = relationship("Artical", back_populates="comments", uselist=False)
    followers = relationship("User", back_populates="followed_comments")


# Comment.metadata.create_all(bind=postgres.engine)
