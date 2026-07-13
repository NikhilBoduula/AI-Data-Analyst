import streamlit as st


def render_sidebar():
    """
    Premium Sidebar
    """

    with st.sidebar:

        # =====================================================
        # LOGO
        # =====================================================

        st.markdown("# 🤖 AutoDS AI")
        st.caption("Autonomous AI Data Scientist")
        st.caption("AI Operating System")

        st.divider()

        # =====================================================
        # NAVIGATION
        # =====================================================

        st.markdown("### 🚀 Navigation")

        selected_page = st.radio(
            "Navigation",
            [
                "🏠 Dashboard",
                "📂 Upload Dataset",
                "🧹 Data Cleaning",
                "📊 EDA",
                "📈 Visualization",
                "🛠 Feature Engineering",
                "🤖 AutoML",
                "🧠 SHAP Explainability",
                "💼 Business Insights",
                "📄 Reports",
                "💬 AI Assistant",
            ],
            label_visibility="collapsed",
        )

        st.divider()

        # =====================================================
        # DATASET STATUS
        # =====================================================

        st.markdown("### 📁 Dataset Status")

        dataset = st.session_state.get("dataset")

        if dataset is None:

            st.error("🔴 No Dataset Loaded")

        else:

            st.success(
                st.session_state.get(
                    "dataset_name",
                    "Dataset"
                )
            )

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Rows",
                    f"{dataset.shape[0]:,}"
                )

            with col2:
                st.metric(
                    "Columns",
                    dataset.shape[1]
                )

        st.divider()

        # =====================================================
        # SYSTEM STATUS
        # =====================================================

        st.markdown("### 🧠 AI System")

        st.success("🟢 Brain Online")

        progress = 0

        if dataset is not None:
            progress += 15

        if st.session_state.get("eda_results"):
            progress += 20

        if st.session_state.get("automl_results"):
            progress += 35

        if st.session_state.get("shap_results"):
            progress += 30

        st.progress(progress / 100)

        st.caption(f"Pipeline Completion : {progress}%")

        st.divider()

        # =====================================================
        # FOOTER
        # =====================================================

        st.caption("AutoDS AI")
        st.caption("Version 2.0")

    return selected_page