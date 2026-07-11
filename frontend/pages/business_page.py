import streamlit as st
from backend.agents.business_agent import BusinessAgent

def render_business_page():
    st.title("🧠 Business Insights")
    st.write("AI-generated insights based on your dataset and machine learning results.")
    st.divider()

    dataset = st.session_state.get("dataset")
    if dataset is None:
        st.info("Upload a dataset first.")
        return

    automl = st.session_state.get("automl_results")
    shap = st.session_state.get("shap_results")

    # Generate insights
    insights = BusinessAgent.generate(dataset, automl, shap)
    st.session_state["business_insights"] = insights

    # ----------------------------------------------------
    # Display Business Insights
    # ----------------------------------------------------
    for insight in insights:
        # 1. Handle dictionary-based insights (with titles)
        if isinstance(insight, dict) and "title" in insight:
            title = insight["title"]
            
            with st.container(border=True):
                st.subheader(title)

                # AI Decisions Module
                if title == "🤖 AI Decisions":
                    for decision in insight.get("message", []):
                        st.markdown(f"### {decision.get('step', 'Step')}")
                        
                        col1, col2 = st.columns(2)
                        with col1:
                            st.metric("🎯 Decision", decision.get("decision", "N/A"))
                            st.metric("🔥 Priority", decision.get("priority", "N/A"))
                        
                        with col2:
                            conf = decision.get("confidence", 0)
                            st.metric("📊 Confidence", f"{conf}%")
                            st.progress(conf / 100)

                        st.info(f"📈 Expected Impact\n\n{decision.get('impact', 'N/A')}")
                        st.success(f"💡 Reason\n\n{decision.get('reason', 'N/A')}")
                        st.divider()

                # Execution Agent Module
                elif title == "⚙️ Execution Agent":
                    for action in insight.get("actions", []):
                        st.markdown(f"### {action.get('task', 'Task')}")
                        
                        col1, col2 = st.columns(2)
                        with col1:
                            st.metric("📌 Status", action.get("status", "N/A"))
                        
                        with col2:
                            status = action.get("status", "")
                            color = "🟢"
                            if status == "Pending":
                                color = "🟠"
                            elif status == "Suggested":
                                color = "🔵"
                            st.write(f"### {color}")

                        st.info(f"📝 Description\n\n{action.get('description', 'N/A')}")
                        st.divider()
                
                # Default case for other dictionary-based insights
                else:
                    st.write(insight.get("message", insight))
        
        # 2. Handle raw data objects (no title)
        else:
            with st.container(border=True):
                st.write(insight)