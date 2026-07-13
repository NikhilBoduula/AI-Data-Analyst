import streamlit as st

from backend.agents.feature_engineering_agent import (
    FeatureEngineeringAgent
)


def render_feature_engineering_page():

    st.title("🛠 AI Feature Engineering")

    if st.session_state.get("dataset") is None:
        st.warning("⚠ Please upload a dataset first.")
        return

    df = st.session_state["dataset"]

    st.subheader("📊 Dataset Information")

    col1, col2 = st.columns(2)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])

    st.divider()

    st.info(
        """
### 🤖 AI Feature Engineering Pipeline

The AI will automatically:

- One-Hot Encode categorical columns
- Remove low variance features
- Standard Scale numeric columns
- Generate ML-ready dataset
"""
    )

    if st.button(
        "🚀 Generate Engineered Features",
        use_container_width=True
    ):

        with st.spinner("Generating features..."):

            agent = FeatureEngineeringAgent(df)

            results = agent.run()

            engineered_df = results["engineered_df"]

            st.session_state[
                "engineered_dataset"
            ] = engineered_df
            
            # Make engineered dataset the active dataset
            st.session_state["dataset"] = engineered_df

        st.success(
            "✅ Feature Engineering completed successfully!"
        )

    if "engineered_dataset" in st.session_state:

        engineered_df = st.session_state[
            "engineered_dataset"
        ]

        st.divider()

        st.subheader("📈 Dataset Comparison")

        col1, col2 = st.columns(2)

        col1.metric(
            "Original Features",
            df.shape[1]
        )

        col2.metric(
            "Engineered Features",
            engineered_df.shape[1]
        )

        st.divider()

        st.subheader("🧠 Engineered Dataset Preview")

        st.dataframe(
            engineered_df.head(10),
            use_container_width=True
        )

        st.divider()

        st.subheader("📋 Engineered Columns")

        st.write(
            engineered_df.columns.tolist()
        )

        st.divider()

        csv = engineered_df.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            "⬇ Download Engineered Dataset",
            data=csv,
            file_name="engineered_dataset.csv",
            mime="text/csv",
            use_container_width=True
        )

        st.divider()

        st.subheader("🤖 AI Recommendations")

        st.success(
            "✔ Categorical variables encoded."
        )

        st.success(
            "✔ Numeric features standardized."
        )

        st.success(
            "✔ Dataset is now ready for Machine Learning."
        )

        st.success(
            "✔ Next step: AutoML."
        )