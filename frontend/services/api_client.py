import requests
import pandas as pd  # Recommended for type hints / safety


class APIClient:
    BASE_URL = "http://127.0.0.1:8000"

    # ----------------------------------------
    # Upload Dataset
    # ----------------------------------------
    @staticmethod
    def upload_dataset(uploaded_file):
        """Upload dataset to FastAPI backend."""
        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                uploaded_file.type,
            )
        }

        response = requests.post(
            f"{APIClient.BASE_URL}/upload",
            files=files,
        )

        response.raise_for_status()
        return response.json()

    # ----------------------------------------
    # Run EDA
    # ----------------------------------------
    @staticmethod
    def run_eda(df: pd.DataFrame):
        """Send dataset to FastAPI for Exploratory Data Analysis."""
        payload = {
            "data": df.to_dict(orient="records")
        }

        response = requests.post(
            f"{APIClient.BASE_URL}/eda",
            json=payload,
        )

        response.raise_for_status()
        return response.json()

    # ----------------------------------------
    # Run AutoML
    # ----------------------------------------
    @staticmethod
    def run_automl(df: pd.DataFrame, target_column: str):
        """Trigger AutoML training on the backend."""

        payload = {
            "data": df.to_dict(orient="records"),
            "target_column": target_column
        }

        response = requests.post(
            f"{APIClient.BASE_URL}/automl",
            json=payload
        )

        response.raise_for_status()
        return response.json()

    # ----------------------------------------
    # Run SHAP Analysis
    # ----------------------------------------
    @staticmethod
    def run_shap(df: pd.DataFrame, model_path: str, target_column: str = None):
        """Run SHAP analysis."""
        payload = {
            "data": df.to_dict(orient="records"),
            "model_path": model_path
        }
        # Only include target_column if provided (depends on your backend)
        if target_column:
            payload["target_column"] = target_column

        response = requests.post(
            f"{APIClient.BASE_URL}/shap",
            json=payload
        )

        response.raise_for_status()
        return response.json()

    # ----------------------------------------
    # Run Business Intelligence
    # ----------------------------------------
    @staticmethod
    def run_business(df, automl_results, shap_results):

        payload = {

            "data": df.to_dict(orient="records"),

            "automl_results": automl_results,

            "shap_results": shap_results

        }

        response = requests.post(
            f"{APIClient.BASE_URL}/business",
            json=payload
        )

        response.raise_for_status()

        return response.json()

    # ----------------------------------------
    # Generate PDF Report
    # ----------------------------------------
    @staticmethod
    def run_reports(
        dataset_path: str,
        dataset_name: str,
        automl_results: dict,
        shap_results: dict
    ):
        """Generate PDF report."""

        payload = {
            "dataset_path": dataset_path,
            "dataset_name": dataset_name,
            "automl_results": automl_results,
            "shap_results": shap_results
        }

        response = requests.post(
            f"{APIClient.BASE_URL}/reports",
            json=payload
        )

        response.raise_for_status()
        return response.json()