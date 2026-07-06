from pathlib import Path
import pandas as pd


class LoaderService:
    """
    Loads datasets into a Pandas DataFrame.
    """

    @staticmethod
    def load_dataset(file_path: str) -> pd.DataFrame:
        extension = Path(file_path).suffix.lower()

        if extension == ".csv":
            return pd.read_csv(file_path)

        elif extension == ".xlsx":
            return pd.read_excel(file_path)

        raise ValueError(f"Unsupported file type: {extension}")