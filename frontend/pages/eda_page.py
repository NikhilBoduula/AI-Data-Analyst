import streamlit as st

from backend.agents.eda_agent import EDAAgent
from backend.visualization.plotly_service import PlotlyService


def render_eda_page():

    st.title("📊 AI Exploratory Data Analysis")

    if st.session_state.get("dataset") is None:
        st.warning("⚠ Please upload a dataset first.")
        return

    df = st.session_state["dataset"]

    agent = EDAAgent(df)
    results = agent.run()

    # -----------------------------------------
    # Dataset Overview
    # -----------------------------------------

    st.subheader("📈 Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Rows", results["shape"][0])
    col2.metric("Columns", results["shape"][1])
    col3.metric("Duplicates", results["duplicate_rows"])
    col4.metric("Memory (KB)", results["memory_usage"])

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

    numeric_columns = results["numeric_columns"]
    categorical_columns = results["categorical_columns"]

    # Numeric Charts
    if numeric_columns:

        selected_numeric = st.selectbox(
            "Select Numeric Column",
            numeric_columns,
            key="numeric_column"
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
            key="categorical_column"
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

    corr = results["correlation_matrix"]

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

    st.success(
        f"Dataset contains **{results['shape'][0]} rows** and **{results['shape'][1]} columns**."
    )

    st.success(
        f"Numeric Columns: **{len(results['numeric_columns'])}**"
    )

    st.success(
        f"Categorical Columns: **{len(results['categorical_columns'])}**"
    )

    st.success(
        f"Duplicate Rows: **{results['duplicate_rows']}**"
    )

    if results["duplicate_rows"] > 0:
        st.warning("Duplicate rows detected. Consider cleaning before training models.")

    if results["missing_values"]["Missing Values"].sum() > 0:
        st.warning("Missing values detected in the dataset.")
    else:
        st.success("No missing values detected.")