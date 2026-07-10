import pandas as pd


class DatasetIntelligence:

    @staticmethod
    def analyze(dataset: pd.DataFrame):

        rows, cols = dataset.shape

        # --------------------------------------------
        # Dataset Size
        # --------------------------------------------

        if rows < 1000:
            dataset_size = "Small Dataset"
            observation = (
                "The dataset is suitable for experimentation and rapid "
                "model development."
            )

        elif rows < 10000:
            dataset_size = "Medium Dataset"
            observation = (
                "The dataset is large enough to train reliable machine "
                "learning models while remaining computationally efficient."
            )

        else:
            dataset_size = "Large Dataset"
            observation = (
                "The dataset is suitable for large-scale machine learning "
                "and production environments."
            )

        # --------------------------------------------
        # Column Types
        # --------------------------------------------

        numeric_columns = dataset.select_dtypes(
            include="number"
        ).columns.tolist()

        categorical_columns = dataset.select_dtypes(
            exclude="number"
        ).columns.tolist()

        # --------------------------------------------
        # Memory Usage
        # --------------------------------------------

        memory = round(
            dataset.memory_usage(deep=True).sum() / 1024,
            2
        )

        # --------------------------------------------
        # Return Intelligence
        # --------------------------------------------

        return {

            "title": "📁 Dataset Intelligence",

            "rows": rows,

            "columns": cols,

            "dataset_size": dataset_size,

            "numeric_columns": len(numeric_columns),

            "categorical_columns": len(categorical_columns),

            "memory_usage": memory,

            "observation": observation,

            "message": (
                f"Rows : {rows:,}\n"
                f"Columns : {cols}\n\n"
                f"Dataset Type : {dataset_size}\n\n"
                f"Numeric Columns : {len(numeric_columns)}\n"
                f"Categorical Columns : {len(categorical_columns)}\n\n"
                f"Memory Usage : {memory} KB\n\n"
                f"Observation\n\n"
                f"{observation}"
            )

        }