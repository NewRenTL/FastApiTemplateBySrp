from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database
import os

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(DATABASE_URL)


async_session = sessionmaker(
    bind=engine,
    class_= AsyncSession,
    expire_on_commit=False
)

Base = declarative_base();

database = Database(DATABASE_URL);

async def get_db():
    async with async_session() as session:
        yield session