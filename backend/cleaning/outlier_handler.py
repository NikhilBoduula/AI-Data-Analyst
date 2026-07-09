import pandas as pd


class OutlierHandler:
    """
    Detects and removes outliers using IQR.
    """

    @staticmethod
    def analyze(df: pd.DataFrame):

        report = {}

        numeric_columns = df.select_dtypes(
            include="number"
        ).columns

        for column in numeric_columns:

            Q1 = df[column].quantile(0.25)

            Q3 = df[column].quantile(0.75)

            IQR = Q3 - Q1

            lower = Q1 - 1.5 * IQR

            upper = Q3 + 1.5 * IQR

            count = df[
                (df[column] < lower) |
                (df[column] > upper)
            ].shape[0]

            report[column] = count

        return report

    @staticmethod
    def remove(df: pd.DataFrame):

        cleaned_df = df.copy()

        numeric_columns = cleaned_df.select_dtypes(
            include="number"
        ).columns

        for column in numeric_columns:

            Q1 = cleaned_df[column].quantile(0.25)

            Q3 = cleaned_df[column].quantile(0.75)

            IQR = Q3 - Q1

            lower = Q1 - 1.5 * IQR

            upper = Q3 + 1.5 * IQR

            cleaned_df = cleaned_df[
                (cleaned_df[column] >= lower) &
                (cleaned_df[column] <= upper)
            ]

        return cleaned_df.reset_index(drop=True)