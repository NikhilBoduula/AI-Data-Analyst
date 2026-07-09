import pandas as pd


class DatasetService:

    @staticmethod
    def get_basic_info(df: pd.DataFrame):

        return {

            "Rows": len(df),

            "Columns": len(df.columns),

            "Missing Values": int(df.isna().sum().sum()),

            "Duplicate Rows": int(df.duplicated().sum()),

            "Column Names": list(df.columns),

            "Data Types": df.dtypes.astype(str).to_dict()

        }