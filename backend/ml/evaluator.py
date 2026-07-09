from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    r2_score,
    mean_squared_error
)


class Evaluator:

    @staticmethod
    def evaluate(task, model, X_test, y_test):

        predictions = model.predict(X_test)

        if task == "classification":

            return {

                "Accuracy": accuracy_score(
                    y_test,
                    predictions
                ),

                "Precision": precision_score(
                    y_test,
                    predictions,
                    average="weighted",
                    zero_division=0
                ),

                "Recall": recall_score(
                    y_test,
                    predictions,
                    average="weighted",
                    zero_division=0
                ),

                "F1": f1_score(
                    y_test,
                    predictions,
                    average="weighted",
                    zero_division=0
                )

            }

        return {

            "R2": r2_score(
                y_test,
                predictions
            ),

            "RMSE": mean_squared_error(
                y_test,
                predictions
            ) ** 0.5

        }