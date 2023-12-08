import numpy as np


def predict_images(model, images: np.array) -> np.array:
    images /= 255.0
    predictions = model.predict(images)
    predictions.sort()[::-1]
    return predictions[:4]
