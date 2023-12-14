from datetime import date

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.database import SessionLocal
from app.models import Workout, WorkoutExercise
from app.schemas.workout import WorkoutSlot

from typing import Optional


class CRUDWorkout:
    @staticmethod
    async def get_workout(workout_date: date = date.today()) -> Optional[Workout]:
        async with SessionLocal() as session:
            session: AsyncSession
            result = await session.execute(
                select(Workout)
                .options(joinedload(Workout.exercises).joinedload(WorkoutExercise.exercise))
                .where(Workout.date == workout_date)
            )
            return result.scalars().first()

    @staticmethod
    async def get_workout_slots() -> list[WorkoutSlot]:
        async with SessionLocal() as session:
            session: AsyncSession
            result = await session.execute(
                select(Workout.date).distinct()
            )
            return [WorkoutSlot(date=d) for d in result.scalars().all()]
