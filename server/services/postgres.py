from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

URL = 'postgresql+psycopg2://user:password@postgres:5432/conduit'
engine = create_engine(
    URL,
    echo=True,
    future=True
)

Session = sessionmaker(
    bind=engine,
    future=True,
    autocommit=False,
    autoflush=False
)

Base = declarative_base()
