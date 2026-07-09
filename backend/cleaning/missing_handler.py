import pandas as pd


class MissingValueHandler:
    """
    Handles missing values in datasets.
    """

    @staticmethod
    def analyze(df: pd.DataFrame):
        """
        Analyze missing values.
        """

        report = pd.DataFrame({
            "Column": df.columns,
            "Missing Count": df.isna().sum().values,
            "Missing Percentage": (
                df.isna().mean() * 100
            ).round(2).values
        })

        return report

    @staticmethod
    def fill(df: pd.DataFrame):
        """
        Automatically fill missing values.
        """

        cleaned_df = df.copy()

        for column in cleaned_df.columns:

            # Try converting numeric-like strings
            converted = pd.to_numeric(cleaned_df[column], errors="coerce")

            # If at least half the non-null values are numeric,
            # treat the column as numeric
            non_null_count = cleaned_df[column].notna().sum()

            if non_null_count > 0 and converted.notna().sum() >= non_null_count / 2:

                median = converted.median()

                cleaned_df[column] = converted.fillna(median)

            else:

                mode = cleaned_df[column].mode()

                if not mode.empty:

                    cleaned_df[column] = cleaned_df[column].fillna(mode.iloc[0])

        return cleaned_df