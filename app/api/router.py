from fastapi import APIRouter

from .endpoints import equipment_router

api_router = APIRouter()
api_router.include_router(equipment_router, tags=["equipment"])
