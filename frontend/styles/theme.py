from pathlib import Path
import streamlit as st


def load_theme():
    """Load and apply custom CSS theme for the Streamlit app."""
    
    css_path = Path("frontend/styles/components.css")
    
    # Fallback CSS in case the file is missing
    if not css_path.exists():
        st.warning("⚠️ Custom CSS file not found. Using inline styles only.")
        css_content = ""
    else:
        try:
            css_content = css_path.read_text(encoding="utf-8")
        except Exception as e:
            st.error(f"Failed to load CSS: {e}")
            css_content = ""

    # Full theme with custom CSS + Google Font
    full_css = f"""
    <style>
        /* =======================================================
        IMPORT FONT
        ======================================================= */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

        html, body, [class*="css"] {{
            font-family: 'Inter', sans-serif;
        }}

        /* =======================================================
        MAIN APP
        ======================================================= */
        .stApp {{
            background: #0B0F19;
            color: white;
        }}

        /* =======================================================
        SIDEBAR
        ======================================================= */
        [data-testid="stSidebar"] {{
            background: #111827;
            border-right: 1px solid #222B45;
        }}

        [data-testid="stSidebar"] * {{
            color: white;
        }}

        /* =======================================================
        HEADINGS
        ======================================================= */
        h1 {{
            color: white;
            font-weight: 700;
        }}

        h2 {{
            color: #E5E7EB;
        }}

        h3 {{
            color: #CBD5E1;
        }}

        /* =======================================================
        BUTTONS
        ======================================================= */
        .stButton > button {{
            width: 100%;
            border-radius: 12px;
            border: none;
            background: linear-gradient(135deg, #7C3AED, #2563EB);
            color: white;
            font-weight: 600;
            padding: 12px;
            transition: 0.3s;
        }}

        .stButton > button:hover {{
            transform: scale(1.02);
            box-shadow: 0 0 18px rgba(124, 58, 237, 0.55);
        }}

        /* =======================================================
        METRICS
        ======================================================= */
        [data-testid="metric-container"] {{
            background: #141C2F;
            border-radius: 16px;
            padding: 15px;
            border: 1px solid #26324D;
        }}

        /* =======================================================
        DATAFRAME
        ======================================================= */
        .stDataFrame {{
            border-radius: 16px;
            overflow: hidden;
        }}

        /* =======================================================
        ALERTS
        ======================================================= */
        .stSuccess, .stInfo, .stWarning {{
            border-radius: 14px;
        }}

        /* =======================================================
        PROGRESS BAR
        ======================================================= */
        .stProgress > div > div {{
            background: linear-gradient(90deg, #7C3AED, #2563EB);
        }}

        /* =======================================================
        EXPANDER
        ======================================================= */
        .streamlit-expanderHeader {{
            font-size: 18px;
            font-weight: 600;
        }}

        /* =======================================================
        SCROLLBAR
        ======================================================= */
        ::-webkit-scrollbar {{
            width: 10px;
        }}

        ::-webkit-scrollbar-track {{
            background: #0B0F19;
        }}

        ::-webkit-scrollbar-thumb {{
            background: #3B4A68;
            border-radius: 10px;
        }}

        ::-webkit-scrollbar-thumb:hover {{
            background: #7C3AED;
        }}

        /* Custom CSS from file */
        {css_content}
    </style>
    """

    st.markdown(full_css, unsafe_allow_html=True)