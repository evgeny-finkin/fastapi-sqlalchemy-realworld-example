from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import asyncio

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

# TODO: Fix this shit, you are better than this...


async def init_models():
    async with engine.begin() as session:
        # await session.run_sync(Base.metadata.drop_all)
        await session.run_sync(Base.metadata.create_all)


def init_models_async():
    loop = asyncio.get_event_loop()
    loop.create_task(init_models())


init_models_async()
