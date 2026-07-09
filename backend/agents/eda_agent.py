import pandas as pd
from typing import Dict, Any


class EDAAgent:
    """
    AI Agent responsible for performing Exploratory Data Analysis.
    """

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

    def run(self) -> Dict[str, Any]:
        """
        Execute the complete EDA pipeline.
        """

        return {
            "shape": self.get_shape(),
            "numeric_columns": self.get_numeric_columns(),
            "categorical_columns": self.get_categorical_columns(),
            "missing_values": self.get_missing_values(),
            "summary_statistics": self.get_summary_statistics(),
            "correlation_matrix": self.get_correlation_matrix()
        }

    def get_shape(self):
        return self.df.shape

    def get_numeric_columns(self):
        return self.df.select_dtypes(include="number").columns.tolist()

    def get_categorical_columns(self):
        return self.df.select_dtypes(exclude="number").columns.tolist()

    def get_missing_values(self):
        return self.df.isnull().sum()

    def get_summary_statistics(self):
        return self.df.describe(include="all")

    def get_correlation_matrix(self):
        numeric_df = self.df.select_dtypes(include="number")

        if numeric_df.empty:
            return pd.DataFrame()

        return numeric_df.corr()