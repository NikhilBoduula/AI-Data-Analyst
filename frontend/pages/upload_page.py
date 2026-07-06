import streamlit as st

from backend.logger import setup_logger

from backend.services.upload_service import UploadService
from backend.services.loader_service import LoaderService
from backend.services.dataset_service import DatasetService

logger = setup_logger()


def render_upload_page():

    st.header("📂 Upload Dataset")

    uploaded_file = st.file_uploader(
        "Upload CSV or Excel",
        type=["csv", "xlsx"]
    )

    if uploaded_file:

        try:

            file_path = UploadService.upload(uploaded_file)

            logger.info(f"Uploaded: {uploaded_file.name}")

            st.success("Dataset uploaded successfully!")

            df = LoaderService.load_dataset(file_path)

            info = DatasetService.get_basic_info(df)

            st.subheader("Dataset Information")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Rows", info["Rows"])

            with col2:
                st.metric("Columns", info["Columns"])

            st.write("### Columns")

            st.write(info["Column Names"])

            st.write("### Dataset Preview")

            st.dataframe(df.head(10), use_container_width=True)

        except Exception as e:

            logger.error(str(e))

            st.error(str(e))