import numpy as np

from app.schemas.equipment import Equipment


class EquipmentService:
    @staticmethod
    async def recognize(image: np.array, model) -> list[Equipment]:
        """ Возвращает список наиболее вероятных оборудований """
        print(image)
        print(image.shape)
        # predictions = model.predict(image)
        # print(predictions)
        # description можно наверное из базы брать? но в таком случае нужно базу с описаниями надыбать
        return [Equipment(name="", description="", accuracy=0.0)]
