import streamlit as st

from backend.logger import setup_logger
from config.settings import APP_NAME

from frontend.components.sidebar import render_sidebar

from frontend.pages.dashboard_page import render_dashboard_page
from frontend.pages.upload_page import render_upload_page
from frontend.pages.cleaning_page import render_cleaning_page
from frontend.pages.eda_page import render_eda_page
from frontend.pages.visualization_page import render_visualization_page
from frontend.pages.feature_engineering_page import (
    render_feature_engineering_page
)
from frontend.pages.automl_page import render_automl_page
from frontend.pages.shap_page import render_shap_page
from frontend.pages.business_page import render_business_page
from frontend.pages.reports_page import render_reports_page
from frontend.pages.chat_page import render_chat_page

logger = setup_logger()

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🤖",
    layout="wide"
)

logger.info("Application Started")

# --------------------------------------------------
# Session State Initialization
# --------------------------------------------------

defaults = {
    "dataset": None,
    "dataset_name": None,
    "dataset_path": None,
    "dataset_info": None,
    "quality_report": None,
    "cleaned_dataset": None,
    "eda_results": None,
    "trained_model": None,
    "automl_results": None,
    "shap_results": None,
    "business_insights": None,
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

selected_page = render_sidebar()

# --------------------------------------------------
# Routing
# --------------------------------------------------

if selected_page == "🏠 Dashboard":
    render_dashboard_page()

elif selected_page == "📂 Upload Dataset":
    render_upload_page()

elif selected_page == "🧹 Data Cleaning":
    render_cleaning_page()

elif selected_page == "📊 EDA":
    render_eda_page()

elif selected_page == "📈 Visualization":
    render_visualization_page()

elif selected_page == "🛠 Feature Engineering":
    render_feature_engineering_page()

elif selected_page == "🤖 AutoML":
    render_automl_page()

elif selected_page == "🧠 SHAP Explainability":
    render_shap_page()

elif selected_page == "🧠 Business Insights":
    render_business_page()

elif selected_page == "📄 Reports":
    render_reports_page()

elif selected_page == "💬 AI Assistant":
    render_chat_page()