import streamlit as st

from backend.agents.eda_agent import EDAAgent


def render_eda_page(df):

    st.title("📊 Exploratory Data Analysis")

    if df is None:

        st.warning("Please upload a dataset first.")

        return

    agent = EDAAgent(df)

    results = agent.run()

    st.subheader("Dataset Shape")

    rows, columns = results["shape"]

    col1, col2 = st.columns(2)

    col1.metric("Rows", rows)
    col2.metric("Columns", columns)

    st.markdown("---")

    st.subheader("Numeric Columns")

    st.write(results["numeric_columns"])

    st.subheader("Categorical Columns")

    st.write(results["categorical_columns"])

    st.markdown("---")

    st.subheader("Missing Values")

    st.dataframe(results["missing_values"])

    st.markdown("---")

    st.subheader("Summary Statistics")

    st.dataframe(
        results["summary_statistics"],
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("Correlation Matrix")

    st.dataframe(
        results["correlation_matrix"],
        use_container_width=True
    )