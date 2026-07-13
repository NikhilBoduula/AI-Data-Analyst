import streamlit as st

from backend.reports.charts import ChartGenerator


class ReportBuilder:

    @staticmethod
    def build(report=None):

        # -------------------------------------------------
        # If no report is supplied, use Streamlit session
        # (keeps the current UI working)
        # -------------------------------------------------

        if report is None:

            dataset = st.session_state.get("dataset")

            report = {

                "dataset": dataset,

                "dataset_name": st.session_state.get("dataset_name"),

                "quality_report": st.session_state.get("quality_report"),

                "eda_results": st.session_state.get("eda_results"),

                "automl_results": st.session_state.get("automl_results"),

                "shap_results": st.session_state.get("shap_results"),

                "charts": []

            }

        # -------------------------------------------------
        # Generate Charts
        # -------------------------------------------------

        dataset = report.get("dataset")

        if dataset is not None:

            report["charts"] = ChartGenerator.save_histograms(dataset)

        return report