from sklearn.model_selection import train_test_split
import pandas as pd

from backend.ml.trainer import Trainer
from backend.ml.evaluator import Evaluator
from backend.ml.model_selector import ModelSelector
from backend.ml.model_saver import ModelSaver


class AutoML:

    @staticmethod
    def detect_task(target):

        if target.dtype == "object":
            return "classification"

        if target.nunique() <= 20:
            return "classification"

        return "regression"

    @staticmethod
    def run(df, target_column):

        # -------------------------
        # Split Features & Target
        # -------------------------

        X = df.drop(columns=[target_column])
        y = df[target_column]

        task = AutoML.detect_task(y)

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        # -------------------------
        # Load Models
        # -------------------------

        if task == "classification":
            models = Trainer.classification_models()
            metric = "Accuracy"
        else:
            models = Trainer.regression_models()
            metric = "R2"

        leaderboard = []

        trained_models = {}

        # -------------------------
        # Train Models
        # -------------------------

        for name, model in models.items():

            try:

                model.fit(X_train, y_train)

                metrics = Evaluator.evaluate(
                    task,
                    model,
                    X_test,
                    y_test
                )

                row = {
                    "Model": name
                }

                row.update(metrics)

                leaderboard.append(row)

                trained_models[name] = model

            except Exception as e:

                print(f"{name} failed : {e}")

        # -------------------------
        # Leaderboard
        # -------------------------

        leaderboard_df = pd.DataFrame(leaderboard)

        leaderboard_df = leaderboard_df.sort_values(
            metric,
            ascending=False
        )

        leaderboard = leaderboard_df.to_dict(
            orient="records"
        )

        # -------------------------
        # Best Model
        # -------------------------

        best = ModelSelector.best(
            leaderboard,
            metric
        )

        best_model = trained_models[
            best["Model"]
        ]

        model_path = ModelSaver.save(
            best_model
        )

        # -------------------------
        # Return
        # -------------------------

        return {

    "task": task,

    "metric": metric,

    "leaderboard": leaderboard,

    "best_model": best,

    "trained_model": best_model,

    "X_train": X_train,

    "X_test": X_test,

    "y_train": y_train,

    "y_test": y_test,

    "feature_names": X.columns.tolist(),

    "model_path": model_path

}