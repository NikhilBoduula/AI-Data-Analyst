import streamlit as st


def section(title, icon="📌"):

    st.markdown("")

    st.markdown(f"## {icon} {title}")

    st.divider()