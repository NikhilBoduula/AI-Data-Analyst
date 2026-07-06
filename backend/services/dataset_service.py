import pandas as pd


class DatasetService:
    """
    Provides dataset information.
    """

    @staticmethod
    def get_basic_info(df: pd.DataFrame):

        return {

            "Rows": df.shape[0],

            "Columns": df.shape[1],

            "Column Names": list(df.columns)

        }