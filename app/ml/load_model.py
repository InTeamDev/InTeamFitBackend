import tensorflow as tf
from keras.models import load_model


def preload_model():
    model = load_model("xception_model_8_classes")
    return model