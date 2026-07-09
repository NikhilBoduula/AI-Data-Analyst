import streamlit as st
import pandas as pd

from backend.ml.automl import AutoML


def render_automl_page():

    st.title("🤖 AI AutoML Center")

    # -----------------------------
    # Check Dataset
    # -----------------------------

    if st.session_state.get("engineered_dataset") is not None:

        df = st.session_state["engineered_dataset"]

    elif st.session_state.get("cleaned_dataset") is not None:

        df = st.session_state["cleaned_dataset"]

    elif st.session_state.get("dataset") is not None:

        df = st.session_state["dataset"]

    else:

        st.warning("⚠ Please upload a dataset first.")

        return

    # -----------------------------
    # Dataset Information
    # -----------------------------

    st.subheader("📊 Dataset Information")

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing Values", int(df.isnull().sum().sum()))

    st.divider()

    # -----------------------------
    # Target Selection
    # -----------------------------

    st.subheader("🎯 Select Target Column")

    target_column = st.selectbox(
        "Target Column",
        df.columns
    )

    task = AutoML.detect_task(df[target_column])

    if task == "classification":

        st.success("Detected Task : Classification")

    else:

        st.success("Detected Task : Regression")

    st.divider()

    # -----------------------------
    # Train Models
    # -----------------------------

    if st.button("🚀 Train AI Models", use_container_width=True):

        with st.spinner("Training multiple machine learning models..."):

            results = AutoML.run(
                df,
                target_column
            )

        st.session_state["automl_results"] = results

        st.success("✅ Training Completed!")

    # -----------------------------
    # Results
    # -----------------------------

    if "automl_results" in st.session_state:

        results = st.session_state["automl_results"]

        st.divider()

        st.header("🏆 Leaderboard")

        leaderboard = pd.DataFrame(
            results["leaderboard"]
        )

        st.dataframe(
            leaderboard,
            use_container_width=True
        )

        st.divider()

        st.header("🥇 Best Model")

        best = results["best_model"]

        st.success(
            f"Best Model : {best['Model']}"
        )

        metric = results["metric"]

        st.info(
            f"{metric} : {round(best[metric],4)}"
        )

        st.success(
            f"Saved Model : {results['model_path']}"
        )

        st.divider()

        st.download_button(

            "⬇ Download Leaderboard",

            leaderboard.to_csv(index=False),

            file_name="leaderboard.csv",

            mime="text/csv"

        )