import streamlit as st


def kpi_card(title, value, icon="📊", help_text=None):

    with st.container(border=True):

        col1, col2 = st.columns([1, 4])

        with col1:
            st.markdown(f"## {icon}")

        with col2:
            st.caption(title)
            st.markdown(f"### {value}")

            if help_text:
                st.caption(help_text)