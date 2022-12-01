from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

URL = 'postgresql+asyncpg://postgres:postgres@postgres:5432/conduit'
engine = create_async_engine(
    URL,
    echo=True
)

Session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()


async def get_async_session():
    async with Session() as session:
        yield session
        await session.commit()
