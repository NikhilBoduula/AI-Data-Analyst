import streamlit as st

from backend.explainability.shap_analyzer import SHAPAnalyzer
from backend.explainability.shap_plots import SHAPPlots
from backend.explainability.shap_utils import SHAPUtils


def render_shap_page():

    st.title("🧠 SHAP Explainability")

    # ----------------------------------
    # Check AutoML Results
    # ----------------------------------

    if "automl_results" not in st.session_state:
        st.warning("⚠ Please train a model first from the AutoML page.")
        return

    results = st.session_state["automl_results"]

    model = results["trained_model"]
    X_train = results["X_train"]

    st.success(f"✅ Best Model: {model.__class__.__name__}")

    st.divider()

    # ----------------------------------
    # Generate SHAP Values
    # ----------------------------------

    if st.button("🚀 Generate SHAP Values", use_container_width=True):

        with st.spinner("Generating SHAP explanations..."):

            analyzer = SHAPAnalyzer(model, X_train)

            st.session_state["shap_results"] = analyzer.compute()

        st.success("✅ SHAP values generated successfully!")

    # ----------------------------------
    # Display Results
    # ----------------------------------

    if "shap_results" not in st.session_state:
        return

    shap_values = st.session_state["shap_results"]["shap_values"]

    # ----------------------------------
    # Feature Importance Chart
    # ----------------------------------

    st.subheader("📊 Feature Importance")

    try:
        fig = SHAPPlots.bar_plot(shap_values)
        st.pyplot(fig, clear_figure=True)

    except Exception as e:
        st.error(f"Bar Plot Error:\n{e}")

    st.divider()

    # ----------------------------------
    # Top Feature Importance Table
    # ----------------------------------

    st.subheader("🏆 Top Feature Importance")

    try:

        importance_df = SHAPUtils.feature_importance(shap_values)

        st.dataframe(
            importance_df,
            use_container_width=True,
            hide_index=True
        )

    except Exception as e:
        st.error(f"Feature Importance Error:\n{e}")

    st.divider()

   