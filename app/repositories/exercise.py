from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import SessionLocal
from app.models import Exercise


class CRUDExercise:
    @staticmethod
    async def get_exercises(limit: int = None, offset: int = None) -> list:
        async with SessionLocal() as session:
            session: AsyncSession
            query = select(Exercise)
            if limit:
                query = query.limit(limit)
            if offset:
                query = query.offset(offset)
            result = await session.execute(query)
            return result.scalars().all()
