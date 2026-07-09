import pandas as pd


class QualityService:
    """
    Performs dataset quality analysis.
    """

    @staticmethod
    def analyze(df: pd.DataFrame) -> dict:

        memory_usage = (
            df.memory_usage(deep=True).sum()
            / 1024
        )

        report = {

            "Rows": len(df),

            "Columns": len(df.columns),

            "Missing Values": int(df.isna().sum().sum()),

            "Duplicate Rows": int(df.duplicated().sum()),

            "Memory Usage": round(memory_usage, 2),

            "Missing Per Column":
                df.isna().sum().to_dict(),

            "Data Types":
                df.dtypes.astype(str).to_dict()

        }

        return report