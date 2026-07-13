from fastapi import APIRouter
from pydantic import BaseModel
import pandas as pd

from backend.ml.automl import AutoML

router = APIRouter()


class AutoMLRequest(BaseModel):

    data: list

    target_column: str


@router.post("/automl")
def run_automl(request: AutoMLRequest):

    # ------------------------------------
    # Reconstruct DataFrame
    # ------------------------------------

    df = pd.DataFrame(request.data)

    # ------------------------------------
    # Run AutoML
    # ------------------------------------

    results = AutoML.run(
        df,
        request.target_column
    )

    return results