import os

from keras.models import load_model


class ModelManager:
    def __init__(self):
        model_path = os.path.join(os.path.dirname(__file__), "xception_model_8_classes")
        self.model = load_model(model_path)
        print(f"Model loaded from {model_path}")

    def get_model(self):
        if self.model is None:
            raise ValueError("Model is not loaded")
        return self.model


model_manager = ModelManager()


def get_model_manager():
    return model_manager
