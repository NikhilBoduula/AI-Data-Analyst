import pandas as pd


class DuplicateHandler:
    """
    Handles duplicate rows.
    """

    @staticmethod
    def count(df: pd.DataFrame):

        return int(df.duplicated().sum())

    @staticmethod
    def remove(df: pd.DataFrame):

        return df.drop_duplicates().reset_index(drop=True)