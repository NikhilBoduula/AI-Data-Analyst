from fastapi import APIRouter, UploadFile, File
import shutil
import uuid
from pathlib import Path

router = APIRouter()

DATASET_DIR = Path("storage/datasets")
DATASET_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/upload")
async def upload_dataset(file: UploadFile = File(...)):

    dataset_id = str(uuid.uuid4())

    extension = Path(file.filename).suffix

    stored_filename = f"{dataset_id}{extension}"

    save_path = DATASET_DIR / stored_filename

    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "dataset_id": dataset_id,
        "filename": file.filename,
        "stored_file": stored_filename,
        "extension": extension,
        "path": str(save_path)
    }