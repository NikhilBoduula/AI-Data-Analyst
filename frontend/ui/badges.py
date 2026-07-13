import streamlit as st


def status_badge(status):

    colors = {
        "Online": "🟢",
        "Completed": "🟢",
        "Running": "🔵",
        "Pending": "🟡",
        "Failed": "🔴",
        "Warning": "🟠"
    }

    icon = colors.get(status, "⚪")

    st.markdown(f"**{icon} {status}**")