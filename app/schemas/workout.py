from pydantic import BaseModel
from uuid import UUID
from datetime import date
from app.schemas.exercise import Exercise


class WorkoutExercise(BaseModel):
    exercise: Exercise
    sets: int
    reps: int


class Workout(BaseModel):
    id: UUID
    title: str
    date: date
    notes: str

    exercises: list[WorkoutExercise]


class WorkoutSlot(BaseModel):
    date: date
