import pandas as pd


class DatatypeHandler:
    """
    Handles datatype conversions.
    """

    @staticmethod
    def analyze(df: pd.DataFrame):

        return pd.DataFrame({
            "Column": df.columns,
            "Data Type": df.dtypes.astype(str).values
        })

    @staticmethod
    def convert(df: pd.DataFrame):

        cleaned_df = df.copy()

        for column in cleaned_df.columns:

            if cleaned_df[column].dtype == "object":

                try:

                    cleaned_df[column] = pd.to_datetime(
                        cleaned_df[column]
                    )

                except Exception:

                    pass

        return cleaned_df