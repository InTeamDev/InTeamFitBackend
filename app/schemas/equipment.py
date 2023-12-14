from pydantic import BaseModel


class Equipment(BaseModel):
    name: str
    description: str
    probability: float
