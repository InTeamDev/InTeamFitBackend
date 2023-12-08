from pydantic import BaseModel


class Equipment(BaseModel):
    # наименование оборудования
    name: str
    # описание оборудования
    description: str
    # точность распознавания
    accuracy: float    # я думаю это лучше переименовать в probability
