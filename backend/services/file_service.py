import os
from pathlib import Path


class FileService:

    @staticmethod
    def save_uploaded_file(uploaded_file, upload_folder):

        os.makedirs(upload_folder, exist_ok=True)

        file_path = Path(upload_folder) / uploaded_file.name

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        return str(file_path)