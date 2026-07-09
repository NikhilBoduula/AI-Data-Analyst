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
            df = pd.read_csv(file_path)

        elif extension == ".xlsx":
            df = pd.read_excel(file_path)

        else:
            raise ValueError(f"Unsupported file type: {extension}")

        # -----------------------------------------
        # Basic preprocessing
        # -----------------------------------------

        df = df.replace("Unrated", pd.NA)
        df = df.replace("", pd.NA)

        # Automatically convert only numeric-like columns
        for column in df.columns:

            converted = pd.to_numeric(
                df[column],
                errors="coerce"
            )

            non_null = df[column].notna().sum()

            if non_null > 0 and converted.notna().sum() >= non_null * 0.8:
                df[column] = converted

        return df