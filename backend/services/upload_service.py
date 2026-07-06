from backend.services.validation_service import ValidationService
from backend.services.file_service import FileService

from config.settings import UPLOAD_FOLDER


class UploadService:

    @staticmethod
    def upload(uploaded_file):

        ValidationService.validate_file(uploaded_file.name)

        path = FileService.save_uploaded_file(
            uploaded_file,
            UPLOAD_FOLDER
        )

        return path