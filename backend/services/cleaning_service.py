import pandas as pd


class CleaningService:
    """
    Performs automatic cleaning.
    """

    @staticmethod
    def remove_duplicates(df: pd.DataFrame):

        return df.drop_duplicates()

    @staticmethod
    def fill_missing(df: pd.DataFrame):

        cleaned = df.copy()

        for column in cleaned.columns:

            if cleaned[column].dtype == "object":

                cleaned[column].fillna(
                    cleaned[column].mode()[0],
                    inplace=True
                )

            else:

                cleaned[column].fillna(
                    cleaned[column].median(),
                    inplace=True
                )

        return cleaned