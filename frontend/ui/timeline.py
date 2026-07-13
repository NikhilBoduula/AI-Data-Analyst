import streamlit as st


def workflow_timeline(workflow):

    with st.container(border=True):

        st.markdown("## 🗺 Workflow Timeline")

        for stage in workflow:

            status = stage["status"]
            step = stage["step"]

            if status == "Completed":
                icon = "🟢"
                color = "#16A34A"
                label = "Completed"

            elif status == "Running":
                icon = "🟡"
                color = "#EAB308"
                label = "Running"

            else:
                icon = "⚪"
                color = "#64748B"
                label = "Pending"

            st.markdown(
                f"""
**{icon} {step}**

<small style="color:{color};">{label}</small>
""",
                unsafe_allow_html=True,
            )

            st.divider()