from datetime import date
from app.schemas.workout import Workout, WorkoutSlot
from app.repositories.workout import CRUDWorkout


class WorkoutService:
    def __init__(self):
        self.crud = CRUDWorkout()

    async def get_workout(self, workout_date: date) -> Workout:
        workout = await self.crud.get_workout(workout_date)
        if workout is None:
            raise ValueError("Workout for this date not found")
        return workout

    async def get_workout_slots(self) -> list[WorkoutSlot]:
        return await self.crud.get_workout_slots()
