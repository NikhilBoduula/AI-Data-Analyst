from fastapi import APIRouter
from pydantic import BaseModel
import pandas as pd

from backend.agents.business_agent import BusinessAgent

router = APIRouter()


class BusinessRequest(BaseModel):
    data: list
    automl_results: dict
    shap_results: dict


@router.post("/business")
def run_business(request: BusinessRequest):

    # -----------------------------
    # Reconstruct DataFrame
    # -----------------------------

    df = pd.DataFrame(request.data)

    # -----------------------------
    # Generate Business Insights
    # -----------------------------

    results = BusinessAgent.generate(
        dataset=df,
        automl_results=request.automl_results,
        shap_results=request.shap_results
    )

    return results