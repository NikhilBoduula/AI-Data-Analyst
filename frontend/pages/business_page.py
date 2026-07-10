import streamlit as st

from backend.agents.business_agent import BusinessAgent


def render_business_page():

    st.title("🧠 Business Insights")

    st.write(
        "AI-generated insights based on your dataset and machine learning results."
    )

    st.divider()

    dataset = st.session_state.get("dataset")

    if dataset is None:

        st.info("Upload a dataset first.")

        return

    automl = st.session_state.get("automl_results")

    shap = st.session_state.get("shap_results")

    insights = BusinessAgent.generate(
        dataset,
        automl,
        shap
    )

    st.session_state["business_insights"] = insights

    for insight in insights:

        with st.container(border=True):

            st.subheader(insight["title"])

            st.write(insight["message"])