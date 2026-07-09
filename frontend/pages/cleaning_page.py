import streamlit as st

from backend.agents.cleaning_agent import CleaningAgent


def render_cleaning_page():
    """
    AI Data Cleaning Page
    """

    st.title("🧹 AI Data Cleaning Center")

    # Check whether a dataset has been uploaded
    if st.session_state.get("dataset") is None:
        st.warning("⚠️ Please upload a dataset first.")
        return

    df = st.session_state["dataset"]

    agent = CleaningAgent(df)

    report = agent.analyze()

    # =====================================================
    # Dataset Overview
    # =====================================================

    st.subheader("📊 Dataset Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric(
        "Missing Values",
        int(df.isna().sum().sum())
    )

    st.divider()

    # =====================================================
    # Missing Value Report
    # =====================================================

    st.subheader("🟡 Missing Value Report")

    st.dataframe(
        report["missing_report"],
        use_container_width=True
    )

    st.divider()

    # =====================================================
    # Duplicate Report
    # =====================================================

    st.subheader("🔵 Duplicate Rows")

    st.metric(
        "Duplicate Rows",
        report["duplicate_count"]
    )

    st.divider()

    # =====================================================
    # Data Types
    # =====================================================

    st.subheader("🟢 Data Types")

    st.dataframe(
        report["datatype_report"],
        use_container_width=True
    )

    st.divider()

    # =====================================================
    # Outlier Report
    # =====================================================

    st.subheader("🔴 Outlier Report")

    st.json(report["outlier_report"])

    st.divider()

    # =====================================================
    # AI Recommendations
    # =====================================================

    st.subheader("🤖 AI Recommendations")

    st.success("✔ Fill numeric missing values with Median")

    st.success("✔ Fill categorical missing values with Mode")

    st.success("✔ Remove duplicate rows")

    st.success("✔ Convert date columns automatically")

    st.success("✔ Standardize column names")

    st.success("✔ Remove outliers using IQR")

    st.divider()

    # =====================================================
    # Cleaning Button
    # =====================================================

    if st.button("🧹 Apply AI Cleaning"):

        cleaned_df = agent.clean()

        st.session_state["cleaned_dataset"] = cleaned_df

        st.success("✅ Dataset cleaned successfully!")

    # =====================================================
    # Cleaned Dataset Preview
    # =====================================================

    if st.session_state.get("cleaned_dataset") is not None:

        st.divider()

        st.subheader("✅ Cleaned Dataset Preview")

        st.dataframe(
            st.session_state["cleaned_dataset"].head(10),
            use_container_width=True
        )

        csv = st.session_state["cleaned_dataset"].to_csv(index=False)

        st.download_button(
            label="⬇ Download Clean Dataset",
            data=csv,
            file_name="cleaned_dataset.csv",
            mime="text/csv"
        )