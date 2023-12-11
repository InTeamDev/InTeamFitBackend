import numpy as np
from app.schemas.equipment import Equipment


def sort_index(array: np.array, reverse: bool = True):
    return sorted(range(len(array)), reverse=reverse, key=lambda i: array[i])


class EquipmentService:
    EQUIPMENT_MAPPING = {
        0: "Беговая дорожка",
        1: "Блочный тренажёр",
        2: "Велотренажер",
        3: "Гантели",
        4: "Гимнастический шар",
        5: "Тренажёр для жима ногами",
        6: "Штанга",
        7: "Эллиптический тренажёр"
    }

    @staticmethod
    def create_equipment(prediction_idx, predictions):
        """ Create and return an Equipment object based on prediction index """
        return Equipment(
            name=EquipmentService.EQUIPMENT_MAPPING[prediction_idx],
            description="",  # Consider fetching from a database or a configuration file
            accuracy=predictions[prediction_idx]
        )

    @staticmethod
    async def recognize(image: np.array, model) -> list[Equipment]:
        """ Returns a list of most probable equipments """
        predictions = model.predict(image)
        top_predictions = sort_index(predictions)
        return [
            EquipmentService.create_equipment(idx, predictions)
            for idx in top_predictions[:4]
            if idx in EquipmentService.EQUIPMENT_MAPPING
        ]
