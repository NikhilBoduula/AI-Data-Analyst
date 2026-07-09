import os
import streamlit as st

from backend.logger import setup_logger

from backend.services.upload_service import UploadService
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

    # Sidebar
    

    st.header("📂 Upload Dataset")

    uploaded_file = st.file_uploader(
        "Upload CSV or Excel",
        type=["csv", "xlsx"]
    )

    if uploaded_file is None:
        st.info("Please upload a dataset to begin.")
        return

    try:

        # Upload and save file
        file_path = UploadService.upload(uploaded_file)

        logger.info(f"Uploaded: {uploaded_file.name}")

        # Load dataset
        df = LoaderService.load_dataset(file_path)
        
        # =====================================================
        # Store dataset globally
        # =====================================================

        st.session_state["dataset"] = df
        st.session_state["dataset_name"] = uploaded_file.name
        st.session_state["dataset_path"] = file_path

        # Dataset information
        info = DatasetService.get_basic_info(df)

        # Data quality report
        quality = QualityService.analyze(df)
        
        # =====================================================
        # Store metadata
        # =====================================================

        st.session_state["dataset_info"] = info
        st.session_state["quality_report"] = quality

        # AI recommendations
        recommendations = RecommendationService.generate(quality)

        st.success("✅ Dataset uploaded successfully!")

        st.markdown("---")

        st.subheader(f"📁 Dataset : {uploaded_file.name}")

        # KPI Cards
        render_metric_cards(info)

        st.markdown("---")

        # Tabs
        overview_tab, preview_tab, statistics_tab, columns_tab = create_tabs()

        # --------------------------------------------------------
        # Overview
        # --------------------------------------------------------

        with overview_tab:

            st.subheader("Dataset Overview")

            col1, col2 = st.columns(2)

            with col1:
                st.write(f"**File Name:** {uploaded_file.name}")
                st.write(f"**Rows:** {info['Rows']}")
                st.write(f"**Columns:** {info['Columns']}")

            with col2:
                file_size = os.path.getsize(file_path) / 1024

                st.write(f"**File Size:** {file_size:.2f} KB")
                st.write(f"**Memory Usage:** {quality['Memory Usage']} KB")

            st.markdown("---")

            st.subheader("Data Quality")

            quality_df = {
                "Metric": [
                    "Missing Values",
                    "Duplicate Rows",
                    "Memory Usage (KB)"
                ],
                "Value": [
                    quality["Missing Values"],
                    quality["Duplicate Rows"],
                    quality["Memory Usage"]
                ]
            }

            st.table(quality_df)

            st.markdown("---")

            st.subheader("🤖 AI Recommendations")

            for recommendation in recommendations:
                st.success(recommendation)

        # --------------------------------------------------------
        # Preview
        # --------------------------------------------------------

        with preview_tab:

            st.subheader("Dataset Preview")

            st.dataframe(
                df.head(10),
                use_container_width=True
            )

        # --------------------------------------------------------
        # Statistics
        # --------------------------------------------------------

        with statistics_tab:

            st.subheader("Dataset Statistics")

            st.dataframe(
                df.describe(include="all").transpose(),
                use_container_width=True
            )

        # --------------------------------------------------------
        # Columns
        # --------------------------------------------------------

        with columns_tab:

            st.subheader("Column Information")

            column_info = {
                "Column Name": df.columns,
                "Data Type": df.dtypes.astype(str).values,
                "Missing Values": df.isna().sum().values,
                "Unique Values": df.nunique().values
            }

            st.dataframe(
                column_info,
                use_container_width=True
            )

    except Exception as e:

        logger.exception(e)

        st.error(f"❌ {e}")