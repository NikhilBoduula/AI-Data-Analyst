import streamlit as st

from frontend.ui.hero import hero
from frontend.services.api_client import APIClient


def render_business_page():
    # =====================================================
    # HERO
    # =====================================================
    hero(
        "Business Intelligence",
        "AI Executive Decision Center • Multi-Agent Analysis"
    )

    dataset = st.session_state.get("dataset")
    if dataset is None:
        st.info("📂 Upload a dataset first.")
        return

    automl = st.session_state.get("automl_results")
    shap = st.session_state.get("shap_results")

    if automl is None:
        st.warning("⚠ Please complete AutoML first.")
        return

    if shap is None:
        st.warning("⚠ Please generate SHAP explanations first.")
        return

    # ---------------------------------------
    # Call FastAPI (Business Intelligence)
    # ---------------------------------------
    if st.session_state.get("business_insights") is None:
        with st.spinner("Generating Business Intelligence..."):
            
            insights = APIClient.run_business(
                st.session_state["dataset"],
                automl,
                shap
            )
            
            
           

            if insights is None:
                st.error("Business API returned None.")
                return

            st.session_state["business_insights"] = insights

    insights = st.session_state["business_insights"]
    

    # =====================================================
    # Categorize Insights
    # =====================================================
    executive = None
    reasoning = None
    decisions = None
    execution = None
    intelligence = []

    for insight in insights:
        if not isinstance(insight, dict):
            continue

        title = insight.get("title", "")

        if title == "📋 Executive Summary":
            executive = insight
        elif title == "🧠 AI Reasoning":
            reasoning = insight
        elif title == "🤖 AI Decisions":
            decisions = insight
        elif title == "⚙️ Execution Agent":
            execution = insight
        else:
            intelligence.append(insight)

    # =====================================================
    # EXECUTIVE SUMMARY + AI REASONING
    # =====================================================
    left, right = st.columns(2)

    with left:
        with st.container(border=True):
            st.subheader("📋 Executive Summary")
            if executive and executive.get("message"):
                st.write(executive["message"])
            else:
                st.write("No executive summary available.")

    with right:
        with st.container(border=True):
            st.subheader("🧠 AI Reasoning")
            if reasoning and reasoning.get("message"):
                st.write(reasoning["message"])
            else:
                st.write("No reasoning available.")

    st.divider()

    # =====================================================
    # AI DECISIONS + EXECUTION AGENT
    # =====================================================
    left, right = st.columns(2)

    with left:
        with st.container(border=True):
            st.subheader("🤖 AI Decisions")
            if decisions and isinstance(decisions.get("message"), list):
                for decision in decisions["message"]:
                    st.markdown(f"### {decision.get('step', 'Decision Step')}")

                    c1, c2 = st.columns(2)
                    with c1:
                        st.metric("Decision", decision.get("decision", "N/A"))
                        st.metric("Priority", decision.get("priority", "N/A"))

                    with c2:
                        confidence = decision.get("confidence", 0)
                        st.metric("Confidence", f"{confidence}%")
                        st.progress(confidence / 100)

                    st.info(decision.get("impact", ""))
                    st.success(decision.get("reason", ""))
                    st.divider()
            else:
                st.info("No decisions available.")

    with right:
        with st.container(border=True):
            st.subheader("⚙️ Execution Agent")
            if execution and isinstance(execution.get("actions"), list):
                for action in execution["actions"]:
                    st.markdown(f"### {action.get('task', 'Task')}")
                    st.metric("Status", action.get("status", "N/A"))
                    st.info(action.get("description", ""))
                    st.divider()
            else:
                st.info("No execution plan available.")

    # =====================================================
    # INTELLIGENCE MODULES
    # =====================================================
    if intelligence:
        st.markdown("## 📊 Intelligence Modules")
        cols = st.columns(2)

        for index, module in enumerate(intelligence):
            with cols[index % 2]:
                with st.container(border=True):
                    st.subheader(module.get("title", "Module"))
                    st.write(module.get("message", ""))