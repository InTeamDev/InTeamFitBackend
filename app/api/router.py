from fastapi import APIRouter

from .endpoints import equipment_router, workout_router

api_router = APIRouter()
api_router.include_router(equipment_router, tags=["equipment"])
api_router.include_router(workout_router, tags=["workout"])
