import requests
import streamlit as st
import pandas as pd

from backend.visualization.plotly_service import PlotlyService


def render_eda_page():
    st.title("📊 AI Exploratory Data Analysis")

    if st.session_state.get("dataset") is None:
        st.warning("⚠ Please upload a dataset first.")
        return

    df = st.session_state["dataset"]

    # -----------------------------------------
    # Run EDA via FastAPI (with caching)
    # -----------------------------------------
    if st.session_state.get("eda_results") is None:
        with st.spinner("Running AI Exploratory Data Analysis..."):
            try:
                payload = {
                    "data": df.to_dict(orient="records")
                }

                response = requests.post(
                    "http://127.0.0.1:8000/eda",
                    json=payload,
                    timeout=60
                )

                if response.status_code == 200:
                    results = response.json()
                    st.session_state["eda_results"] = results
                else:
                    st.error(f"FastAPI Error: {response.status_code} - {response.text}")
                    return

            except requests.exceptions.ConnectionError:
                st.error("❌ Could not connect to FastAPI backend. Is it running on http://127.0.0.1:8000?")
                return
            except Exception as e:
                st.error(f"Error during EDA: {str(e)}")
                return
    else:
        results = st.session_state["eda_results"]

    # -----------------------------------------
    # Dataset Overview
    # -----------------------------------------
    st.subheader("📈 Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Rows", results["shape"][0])
    col2.metric("Columns", results["shape"][1])
    col3.metric("Duplicates", results["duplicate_rows"])
    col4.metric("Memory (KB)", round(results.get("memory_usage", 0), 2))

    st.divider()

    # -----------------------------------------
    # Missing Values
    # -----------------------------------------
    st.subheader("🟡 Missing Values")
    st.dataframe(
        results["missing_values"],
        use_container_width=True
    )

    st.divider()

    # -----------------------------------------
    # Summary Statistics
    # -----------------------------------------
    st.subheader("📋 Summary Statistics")
    st.dataframe(
        results["summary_statistics"],
        use_container_width=True
    )

    st.divider()

    # -----------------------------------------
    # Interactive Charts
    # -----------------------------------------
    st.header("📊 Interactive Visualizations")

    numeric_columns = results.get("numeric_columns", [])
    categorical_columns = results.get("categorical_columns", [])

    # Numeric Charts
    if numeric_columns:
        selected_numeric = st.selectbox(
            "Select Numeric Column",
            numeric_columns,
            key="numeric_column_eda"
        )

        col1, col2 = st.columns(2)

        with col1:
            st.plotly_chart(
                PlotlyService.histogram(df, selected_numeric),
                use_container_width=True
            )

        with col2:
            st.plotly_chart(
                PlotlyService.boxplot(df, selected_numeric),
                use_container_width=True
            )
    else:
        st.info("No numeric columns found.")

    st.divider()

    # Categorical Charts
    if categorical_columns:
        selected_category = st.selectbox(
            "Select Categorical Column",
            categorical_columns,
            key="categorical_column_eda"
        )

        col1, col2 = st.columns(2)

        with col1:
            st.plotly_chart(
                PlotlyService.bar_chart(df, selected_category),
                use_container_width=True
            )

        with col2:
            st.plotly_chart(
                PlotlyService.pie_chart(df, selected_category),
                use_container_width=True
            )
    else:
        st.info("No categorical columns found.")

    st.divider()

    # -----------------------------------------
    # Correlation Heatmap
    # -----------------------------------------
    st.header("🔥 Correlation Heatmap")

    corr_data = results.get("correlation_matrix")
    corr = pd.DataFrame(corr_data) if corr_data else pd.DataFrame()

    if not corr.empty and len(corr.columns) > 1:
        st.plotly_chart(
            PlotlyService.correlation_heatmap(corr),
            use_container_width=True
        )
    else:
        st.info("Need at least two numeric columns to display a correlation heatmap.")

    st.divider()

    # -----------------------------------------
    # AI Insights
    # -----------------------------------------
    st.header("🤖 AI Insights")

    st.success(f"Dataset contains **{results['shape'][0]} rows** and **{results['shape'][1]} columns**.")
    st.success(f"Numeric Columns: **{len(results.get('numeric_columns', []))}**")
    st.success(f"Categorical Columns: **{len(results.get('categorical_columns', []))}**")
    st.success(f"Duplicate Rows: **{results.get('duplicate_rows', 0)}**")

    if results.get("duplicate_rows", 0) > 0:
        st.warning("Duplicate rows detected. Consider cleaning before training models.")

    # Missing Values Summary
    missing_df = pd.DataFrame(results.get("missing_values", []))
    missing_total = missing_df["Missing Values"].sum() if not missing_df.empty else 0

    if missing_total > 0:
        st.warning(f"Missing values detected ({missing_total} total).")
    else:
        st.success("No missing values detected.")