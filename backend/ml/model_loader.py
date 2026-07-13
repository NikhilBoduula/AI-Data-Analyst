import joblib


class ModelLoader:

    @staticmethod
    def load(model_path):

        return joblib.load(model_path)