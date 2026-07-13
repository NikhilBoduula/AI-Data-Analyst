from fastapi import APIRouter
from pydantic import BaseModel
import pandas as pd

from backend.ml.model_loader import ModelLoader
from backend.explainability.shap_analyzer import SHAPAnalyzer

router = APIRouter()


class SHAPRequest(BaseModel):

    data: list

    model_path: str
    
    target_column: str


@router.post("/shap")
def run_shap(request: SHAPRequest):

    # -----------------------------
    # Reconstruct dataframe
    # -----------------------------

    df = pd.DataFrame(request.data)
    
    X = df.drop(columns=[request.target_column])

    # -----------------------------
    # Load trained model
    # -----------------------------

    model = ModelLoader.load(request.model_path)

    # -----------------------------
    # SHAP
    # -----------------------------

    analyzer = SHAPAnalyzer(
        model,
        X
    )

    results = analyzer.compute()

    return results