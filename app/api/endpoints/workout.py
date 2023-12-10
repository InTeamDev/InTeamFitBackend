from fastapi import APIRouter, HTTPException, Depends
from datetime import date
workout_router = APIRouter()


@workout_router.get("/workouts/{date}")
async def get_workout(workout_date: date = date.today()):
    return {"date": workout_date}
