import streamlit as st
import pandas as pd

from frontend.services.api_client import APIClient


def render_shap_page():
    st.title("🧠 SHAP Explainability")

    # ----------------------------------
    # Check Prerequisites
    # ----------------------------------
    if "automl_results" not in st.session_state:
        st.warning("⚠ Please train a model first from the AutoML page.")
        return

    if "dataset" not in st.session_state:
        st.error("Dataset not found in session state.")
        return

    if "target_column" not in st.session_state:
        st.error("Target column not found in session state.")
        return

    st.success("✅ Model trained successfully!")

    st.divider()

    # ----------------------------------
    # Generate SHAP Values
    # ----------------------------------
    if st.button("🚀 Generate SHAP Values", use_container_width=True, type="primary"):
        with st.spinner("Generating SHAP explanations..."):
            try:
                results = APIClient.run_shap(
                    df=st.session_state["dataset"],
                    model_path=st.session_state["automl_results"]["model_path"],
                    target_column=st.session_state["target_column"]
                )

                st.session_state["shap_results"] = results
                st.success("✅ SHAP values generated successfully!")

            except Exception as e:
                st.error(f"❌ Failed to generate SHAP values: {str(e)}")
                return

    # ----------------------------------
    # Display Results
    # ----------------------------------
    if "shap_results" not in st.session_state:
        st.info("Click the button above to generate SHAP explanations.")
        return

    results = st.session_state["shap_results"]

    # Feature Importance
    st.subheader("📊 Feature Importance")

    if "feature_names" in results and "importance" in results:
        importance_df = pd.DataFrame({
            "Feature": results["feature_names"],
            "Importance": results["importance"]
        })

        importance_df = importance_df.sort_values(
            "Importance", ascending=False
        ).reset_index(drop=True)

        st.dataframe(
            importance_df,
            use_container_width=True,
            hide_index=True
        )
    else:
        st.warning("SHAP results format is unexpected. Missing 'feature_names' or 'importance' keys.")

    # Optional: Add more SHAP visualizations here (e.g., summary plot, force plot, etc.)
    st.divider()
    st.caption("Additional SHAP visualizations (beeswarm, waterfall, etc.) can be added here.")