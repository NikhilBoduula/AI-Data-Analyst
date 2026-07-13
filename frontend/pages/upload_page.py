import os
import streamlit as st
import pandas as pd

from backend.logger import setup_logger
from frontend.services.api_client import APIClient
from backend.services.loader_service import LoaderService
from backend.services.dataset_service import DatasetService
from backend.services.quality_service import QualityService
from backend.services.recommendation_service import RecommendationService

from frontend.components.metric_cards import render_metric_cards
from frontend.components.tabs import create_tabs

logger = setup_logger()


def render_upload_page():
    """
    Upload page for the AI Data Analyst Platform.
    """

    st.header("📂 Upload Dataset")

    uploaded_file = st.file_uploader(
        "Upload CSV or Excel",
        type=["csv", "xlsx"]
    )

    if uploaded_file is None:
        st.info("Please upload a dataset to begin.")
        return

    try:
        # --------------------------------------------------
        # Upload to FastAPI
        # --------------------------------------------------
        api_response = APIClient.upload_dataset(uploaded_file)

        dataset_id = api_response["dataset_id"]
        extension = api_response["extension"]
        file_path = api_response["path"]

        logger.info(f"Uploaded via FastAPI: {uploaded_file.name}")

        # Load dataset from saved location
        df = LoaderService.load_dataset(file_path)

        # =====================================================
        # Store in session state
        # =====================================================
        st.session_state["dataset"] = df
        st.session_state["dataset_name"] = uploaded_file.name
        st.session_state["dataset_path"] = file_path
        st.session_state["dataset_extension"] = extension
        st.session_state["dataset_id"] = dataset_id

        # Get metadata
        info = DatasetService.get_basic_info(df)
        quality = QualityService.analyze(df)
        recommendations = RecommendationService.generate(quality)

        # Store metadata
        st.session_state["dataset_info"] = info
        st.session_state["quality_report"] = quality

        st.success("✅ Dataset uploaded and processed successfully!")

        st.markdown("---")

        st.subheader(f"📁 Dataset: {uploaded_file.name}")

        # KPI Cards
        render_metric_cards(info)

        st.markdown("---")

        # Tabs
        overview_tab, preview_tab, statistics_tab, columns_tab = create_tabs()

        # --------------------------------------------------------
        # Overview Tab
        # --------------------------------------------------------
        with overview_tab:
            st.subheader("Dataset Overview")

            col1, col2 = st.columns(2)

            with col1:
                st.write(f"**File Name:** {uploaded_file.name}")
                st.write(f"**Rows:** {info.get('Rows', 'N/A')}")
                st.write(f"**Columns:** {info.get('Columns', 'N/A')}")

            with col2:
                file_size = os.path.getsize(file_path) / 1024
                st.write(f"**File Size:** {file_size:.2f} KB")
                st.write(f"**Memory Usage:** {quality.get('Memory Usage', 'N/A')} KB")

            st.markdown("---")
            st.subheader("Data Quality")

            quality_df = pd.DataFrame({
                "Metric": ["Missing Values", "Duplicate Rows", "Memory Usage (KB)"],
                "Value": [
                    quality.get("Missing Values", 0),
                    quality.get("Duplicate Rows", 0),
                    quality.get("Memory Usage", 0)
                ]
            })

            st.dataframe(quality_df, use_container_width=True)

            st.markdown("---")
            st.subheader("🤖 AI Recommendations")

            for rec in recommendations:
                st.success(rec)

        # --------------------------------------------------------
        # Preview Tab
        # --------------------------------------------------------
        with preview_tab:
            st.subheader("Dataset Preview")
            st.dataframe(df.head(10), use_container_width=True)

        # --------------------------------------------------------
        # Statistics Tab
        # --------------------------------------------------------
        with statistics_tab:
            st.subheader("Dataset Statistics")
            st.dataframe(
                df.describe(include="all").transpose(),
                use_container_width=True
            )

        # --------------------------------------------------------
        # Columns Tab
        # --------------------------------------------------------
        with columns_tab:
            st.subheader("Column Information")

            column_info = pd.DataFrame({
                "Column Name": df.columns,
                "Data Type": df.dtypes.astype(str).values,
                "Missing Values": df.isna().sum().values,
                "Unique Values": df.nunique().values
            })

            st.dataframe(column_info, use_container_width=True)

    except Exception as e:
        logger.exception(f"Error in upload page: {e}")
        st.error(f"❌ An error occurred: {str(e)}")