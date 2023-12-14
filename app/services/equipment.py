import numpy as np

from app.schemas.equipment import Equipment
from app.repositories.equipment import CRUDEquipment


def sort_index(array: np.array, reverse: bool = True):
    return sorted(range(len(array)), reverse=reverse, key=lambda i: array[i])


class EquipmentService:
    EQUIPMENT_MAPPING = {
        0: {
            "name": "Беговая дорожка",
            "description": "Этот тренажер имитирует бег или ходьбу. Идеален для кардио-тренировок, улучшения выносливости и сжигания калорий.",
        },
        1: {
            "name": "Блочный тренажёр",
            "description": "Предназначен для тренировки различных групп мышц с использованием силовых упражнений. Блоки и тросы позволяют регулировать нагрузку.",
        },
        2: {
            "name": "Велотренажер",
            "description": "Имитирует велосипедную езду. Отлично подходит для кардио, укрепления мышц ног и улучшения общей физической формы.",
        },
        3: {
            "name": "Гантели",
            "description": "Универсальный инструмент для силовых тренировок. Подходят для упражнений на все группы мышц, улучшения баланса и координации.",
        },
        4: {
            "name": "Гимнастический шар",
            "description": "Используется для упражнений на равновесие, растяжку и укрепление мышц кора.",
        },
        5: {
            "name": "Тренажёр для жима ногами",
            "description": "Предназначен для тренировки мышц ног и ягодиц. Позволяет выполнять жим ногами с различным весом.",
        },
        6: {
            "name": "Штанга",
            "description": "Основной инструмент для силовых тренировок. Используется для упражнений на все группы мышц, особенно эффективна для развития силы и массы.",
        },
        7: {
            "name": "Эллиптический тренажёр",
            "description": "Объединяет элементы бега, ходьбы и подъёма по лестнице. Минимизирует нагрузку на суставы, эффективен для кардиотренировок и тренировки всего тела.",
        }
    }

    @staticmethod
    def create_equipment(prediction_idx, predictions):
        """ Create and return an Equipment object based on prediction index """
        return Equipment(
            name=EquipmentService.EQUIPMENT_MAPPING[prediction_idx]['name'],
            description=EquipmentService.EQUIPMENT_MAPPING[prediction_idx]['description'],
            probability=predictions[prediction_idx]
        )

    @staticmethod
    async def recognize(image: np.array, model) -> list[Equipment]:
        """ Returns a list of most probable equipments """
        predictions = model.predict(image)[0]
        top_predictions = sort_index(predictions)
        return [
            EquipmentService.create_equipment(idx, predictions)
            for idx in top_predictions[:4]
            if idx in EquipmentService.EQUIPMENT_MAPPING and predictions[idx] > 0.0001
        ]
