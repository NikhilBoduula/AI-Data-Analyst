from fastapi import APIRouter
from pydantic import BaseModel

import pandas as pd
import numpy as np
import json
import math 

from backend.agents.eda_agent import EDAAgent

router = APIRouter()


class DatasetRequest(BaseModel):
    data: list

def make_json_safe(obj):
    """
    Recursively convert pandas/numpy objects into JSON-safe Python objects.
    """

    if isinstance(obj, dict):
        return {k: make_json_safe(v) for k, v in obj.items()}

    elif isinstance(obj, list):
        return [make_json_safe(v) for v in obj]

    elif isinstance(obj, tuple):
        return [make_json_safe(v) for v in obj]

    elif isinstance(obj, pd.DataFrame):
        return make_json_safe(obj.to_dict(orient="records"))

    elif isinstance(obj, pd.Series):
        return make_json_safe(obj.to_dict())

    elif isinstance(obj, np.ndarray):
        return make_json_safe(obj.tolist())

    elif isinstance(obj, np.integer):
        return int(obj)

    elif isinstance(obj, np.floating):

        value = float(obj)

        if math.isnan(value):
            return None

        return value

    elif isinstance(obj, float):

        if math.isnan(obj):
            return None

        return obj

    return obj

@router.post("/eda")
def run_eda(request: DatasetRequest):
    try:
        # Convert incoming data to DataFrame
        df = pd.DataFrame(request.data)

        if df.empty:
            return {"error": "Received empty dataset"}

        agent = EDAAgent(df)
        results = agent.run()

        # Debug print (optional - remove in production)
        print("\n===== EDA RESULTS =====")
        for key, value in results.items():
            print(f"{key}: {type(value)}")
        print("=======================\n")

        # ------------------------------------------
        # Convert results to JSON-safe format
        # ------------------------------------------
        clean_results = {}

        for key, value in results.items():
            if isinstance(value, pd.DataFrame):
                clean_results[key] = value.to_dict(orient="records")

            elif isinstance(value, pd.Series):
                clean_results[key] = value.to_dict()

            elif isinstance(value, (np.integer, np.int64)):
                clean_results[key] = int(value)

            elif isinstance(value, (np.floating, np.float64)):
                clean_results[key] = float(value)

            elif isinstance(value, np.ndarray):
                clean_results[key] = value.tolist()

            elif isinstance(value, (list, dict)):
                # Try to make sure nested structures are JSON serializable
                try:
                    json.dumps(value)  # Test if it's serializable
                    clean_results[key] = value
                except (TypeError, OverflowError):
                    clean_results[key] = str(value)  # Fallback

            else:
                clean_results[key] = value

        return make_json_safe(clean_results)

    except Exception as e:
        return {
            "error": "Failed to process EDA request",
            "detail": str(e)
        }