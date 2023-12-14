from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import SessionLocal
from app.models import Equipment


class CRUDEquipment:
    @staticmethod
    async def get_equipment_by_name(name: str) -> Equipment:
        async with SessionLocal() as session:
            session: AsyncSession
            query = select(Equipment).filter(Equipment.name == name)
            result = await session.execute(query)
            return result.scalars().first()
