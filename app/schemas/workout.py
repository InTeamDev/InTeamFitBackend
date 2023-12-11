from pydantic import BaseModel


class Workout(BaseModel):
    id: str
    title: str
    date: str
    notes: str

    exercises: list
