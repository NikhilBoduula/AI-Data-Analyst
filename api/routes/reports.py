from fastapi import APIRouter
from pydantic import BaseModel
import pandas as pd

from backend.reports.report_builder import ReportBuilder
from backend.reports.pdf_generator import PDFGenerator

router = APIRouter()


class ReportRequest(BaseModel):

    dataset_path: str

    dataset_name: str

    automl_results: dict | None = None

    shap_results: dict | None = None


@router.post("/reports")
def generate_report(request: ReportRequest):

    # ------------------------------------
    # Load Dataset
    # ------------------------------------

    if request.dataset_path.endswith(".csv"):
        dataset = pd.read_csv(request.dataset_path)
    else:
        dataset = pd.read_excel(request.dataset_path)

    # ------------------------------------
    # Build Report
    # ------------------------------------

    report = {

        "dataset": dataset,

        "dataset_name": request.dataset_name,

        "quality_report": None,

        "eda_results": None,

        "automl_results": request.automl_results,

        "shap_results": request.shap_results,

        "charts": []

    }

    report = ReportBuilder.build(report)

    # ------------------------------------
    # Generate PDF
    # ------------------------------------

    output_path = "AI_Data_Scientist_Report.pdf"

    PDFGenerator.generate(
        report,
        output_path
    )

    return {

        "status": "success",

        "pdf_path": output_path

    }