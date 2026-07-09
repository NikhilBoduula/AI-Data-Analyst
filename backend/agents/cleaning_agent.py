import pandas as pd

from backend.cleaning.cleaner import Cleaner
from backend.cleaning.missing_handler import MissingValueHandler
from backend.cleaning.duplicate_handler import DuplicateHandler
from backend.cleaning.outlier_handler import OutlierHandler
from backend.cleaning.datatype_handler import DatatypeHandler


class CleaningAgent:
    """
    AI Cleaning Agent responsible for analyzing and cleaning datasets.
    """

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

    def analyze(self):
        """
        Analyze dataset quality before cleaning.
        """

        return {
            "missing_report": MissingValueHandler.analyze(self.df),
            "duplicate_count": DuplicateHandler.count(self.df),
            "outlier_report": OutlierHandler.analyze(self.df),
            "datatype_report": DatatypeHandler.analyze(self.df),
        }

    def clean(self):
        """
        Execute the complete cleaning pipeline.
        """

        return Cleaner.clean(self.df)