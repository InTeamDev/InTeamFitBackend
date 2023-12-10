from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import load_settings

settings = load_settings()

engine = create_async_engine(settings.postgres.get_dsn(async_=True), echo=settings.app.environment == "dev",
                             pool_recycle=1800)
SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()
metadata = MetaData()
