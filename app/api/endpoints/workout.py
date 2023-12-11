from datetime import date
from uuid import uuid4

from fastapi import APIRouter

from app.schemas.exercise import Exercise
from app.schemas.workout import Workout

workout_router = APIRouter()


@workout_router.get("/workouts/{date}", response_model=Workout)
async def get_workout(workout_date: date = date.today()):
    return Workout(
        id=str(uuid4()),
        title=f"Workout for {workout_date}",
        date=workout_date,
        notes="Some notes about the workout",
        exercises=[Exercise(id=str(uuid4()), name=f"Exercise {_}") for _ in range(3)],
    )
