import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

APP_NAME = "AI Data Analyst"
VERSION = "1.0.0"

DEBUG = True

UPLOAD_FOLDER = "data/uploads"
RAW_DATA_FOLDER = "data/raw"
PROCESSED_DATA_FOLDER = "data/processed"
REPORT_FOLDER = "reports"
MODEL_FOLDER = "models"
LOG_FOLDER = "logs"

SECRET_KEY = os.getenv("SECRET_KEY", "change-me")