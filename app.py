import streamlit as st

from backend.logger import setup_logger
from config.settings import APP_NAME, VERSION

from frontend.pages.upload_page import render_upload_page

logger = setup_logger()

logger.info("Application Started")

st.set_page_config(
    page_title=APP_NAME,
    page_icon="📊",
    layout="wide"
)

st.title(APP_NAME)

st.caption("Autonomous AI Data Analyst")

st.write(f"Version: {VERSION}")

st.divider()

render_upload_page()