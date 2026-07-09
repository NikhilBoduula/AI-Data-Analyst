import pandas as pd


class ColumnHandler:
    """
    Handles column cleaning.
    """

    @staticmethod
    def clean(df: pd.DataFrame):

        cleaned_df = df.copy()

        cleaned_df.columns = (

            cleaned_df.columns

            .str.strip()

            .str.lower()

            .str.replace(" ", "_")

        )

        return cleaned_df