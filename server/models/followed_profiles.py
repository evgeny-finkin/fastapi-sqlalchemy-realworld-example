from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import URLType, EmailType

from services import postgres


class FollowedProfile(postgres.Base):
    __tablename__ = 'followed_profiles'

    followed_email = Column(EmailType, primary_key=True)
    follower_email = Column(EmailType, ForeignKey(
        'users.email'), primary_key=True)

    followers = relationship("User", back_populates="followed_profiles")
