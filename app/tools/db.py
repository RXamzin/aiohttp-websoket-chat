from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base

Base = declarative_base()

def get_db_engine(url):
    return create_async_engine(url)

def get_db_session(engine):
    return AsyncSession(engine, expire_on_commit=False)

from app.models.user import User
