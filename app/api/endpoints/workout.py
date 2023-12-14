from datetime import date

from fastapi import APIRouter, HTTPException

from app.schemas.workout import Workout, WorkoutSlot
from app.services.workout import WorkoutService

workout_router = APIRouter()


@workout_router.get("/workouts", response_model=Workout)
async def get_workout(workout_date: date = date.today()):
    try:
        return await WorkoutService().get_workout(workout_date)
    except ValueError:
        raise HTTPException(status_code=404, detail="Workout for this date not found")


@workout_router.get("/workouts/slots", response_model=list[WorkoutSlot])
async def get_workout_slots():
    return await WorkoutService().get_workout_slots()
