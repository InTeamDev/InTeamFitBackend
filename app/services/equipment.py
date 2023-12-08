import numpy as np

from app.schemas.equipment import Equipment


def sort_index(array: np.array, reverse: bool = True):
    index = range(len(array))
    s = sorted(index, reverse=reverse, key = lambda i: array[i])
    return s


class EquipmentService:
    @staticmethod
    async def recognize(image: np.array, model) -> list[Equipment]:
        """ Возвращает список наиболее вероятных оборудований """
        print(image)
        print(image.shape)
        predictions = model.predict(image)
        top_predictions = sort_index(predictions)
        equipments = []
        # вообще это можно в БД, наверное, вынести
        for prediction_idx in top_predictions[:4]:
            match prediction_idx:
                case 0:
                    equipments.append(Equipment(name="Беговая дорожка",
                                                description="", accuracy=predictions[prediction_idx]))
                case 1:
                    equipments.append(Equipment(name="Блочный тренажёр",
                                                description="", accuracy=predictions[prediction_idx]))
                case 2:
                    equipments.append(Equipment(name="Велотренажер",
                                                description="", accuracy=predictions[prediction_idx]))
                case 3:
                    equipments.append(Equipment(name="Гантели",
                                                description="", accuracy=predictions[prediction_idx]))
                case 4:
                    equipments.append(Equipment(name="Гимнастический шар",
                                                description="", accuracy=predictions[prediction_idx]))
                case 5:
                    equipments.append(Equipment(name="Тренажёр для жима ногами",
                                                description="", accuracy=predictions[prediction_idx]))
                case 6:
                    equipments.append(Equipment(name="Штанга",
                                                description="", accuracy=predictions[prediction_idx]))
                case 7:
                    equipments.append(Equipment(name="Эллиптический тренажёр",
                                                description="", accuracy=predictions[prediction_idx]))

        # print(predictions)
        # description можно наверное из базы брать? но в таком случае нужно базу с описаниями надыбать
        return equipments

