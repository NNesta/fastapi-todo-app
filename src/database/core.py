from fastapi import Depends
from typing import Annotated
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, create_async_engine
import os
from config import settings

engine = create_async_engine(settings.database_url)
async_session_local = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


class Base(DeclarativeBase):
    pass


async def get_db():
    async with async_session_local() as db:
        yield db


DbSession = Annotated[AsyncSession, Depends(get_db)]
