from sqlalchemy import Column, Integer, String

from services import postgres


class Tags(postgres.Base):
    __tablename__ = 'tags'

    tag_name = Column(Integer, primary_key=True, index=True)


# Tags.metadata.create_all(bind=postgres.engine)
