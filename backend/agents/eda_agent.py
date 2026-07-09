import pandas as pd
from typing import Dict, Any


class EDAAgent:
    """
    AI Agent responsible for performing Exploratory Data Analysis.
    """

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe.copy()

    def run(self) -> Dict[str, Any]:

        return {

            "shape": self.df.shape,

            "numeric_columns": self.get_numeric_columns(),

            "categorical_columns": self.get_categorical_columns(),

            "missing_values": self.get_missing_values(),

            "summary_statistics": self.get_summary_statistics(),

            "correlation_matrix": self.get_correlation_matrix(),

            "memory_usage": self.get_memory_usage(),

            "duplicate_rows": self.get_duplicate_rows()

        }

    def get_numeric_columns(self):

        return self.df.select_dtypes(include="number").columns.tolist()

    def get_categorical_columns(self):

        return self.df.select_dtypes(exclude="number").columns.tolist()

    def get_missing_values(self):

        return pd.DataFrame({

            "Missing Values": self.df.isnull().sum(),

            "Percentage": (
                self.df.isnull().mean() * 100
            ).round(2)

        })

    def get_summary_statistics(self):

        return self.df.describe(include="all")

    def get_correlation_matrix(self):

        numeric_df = self.df.select_dtypes(include="number")

        if numeric_df.shape[1] < 2:
            return pd.DataFrame()

        return numeric_df.corr()

    def get_memory_usage(self):

        return round(
            self.df.memory_usage(deep=True).sum() / 1024,
            2
        )

    def get_duplicate_rows(self):

        return int(self.df.duplicated().sum())