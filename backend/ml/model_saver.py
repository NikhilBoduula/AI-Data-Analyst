import os
import joblib


class ModelSaver:

    @staticmethod
    def save(model, filename):

        os.makedirs("models", exist_ok=True)

        path = os.path.join(
            "models",
            filename
        )

        joblib.dump(model, path)

        return path