from pathlib import Path

from backend.constants import SUPPORTED_EXTENSIONS


class ValidationService:

    @staticmethod
    def validate_file(filename: str):

        extension = Path(filename).suffix.lower()

        if extension not in SUPPORTED_EXTENSIONS:
            raise ValueError(
                f"Unsupported file type: {extension}"
            )

        return True