import pandas as pd

from backend.cleaning.column_handler import ColumnHandler
from backend.cleaning.datatype_handler import DatatypeHandler
from backend.cleaning.missing_handler import MissingValueHandler
from backend.cleaning.duplicate_handler import DuplicateHandler
from backend.cleaning.outlier_handler import OutlierHandler


class Cleaner:
    """
    Main cleaning pipeline.
    """

    @staticmethod
    def clean(df: pd.DataFrame):

        cleaned_df = df.copy()

        # Standardize column names
        cleaned_df = ColumnHandler.clean(cleaned_df)

        # Convert data types
        cleaned_df = DatatypeHandler.convert(cleaned_df)

        # Fill missing values
        cleaned_df = MissingValueHandler.fill(cleaned_df)

        # Remove duplicate rows
        cleaned_df = DuplicateHandler.remove(cleaned_df)

        # Remove outliers
        cleaned_df = OutlierHandler.remove(cleaned_df)

        return cleaned_df