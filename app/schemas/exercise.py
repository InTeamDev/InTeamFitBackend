from uuid import UUID

from pydantic import BaseModel


class Exercise(BaseModel):
    name: str
    description: str
    muscle_group: str
