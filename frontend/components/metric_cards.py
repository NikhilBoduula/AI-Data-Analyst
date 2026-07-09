import streamlit as st


def render_metric_cards(info):

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Rows",
            info["Rows"]
        )

    with col2:

        st.metric(
            "Columns",
            info["Columns"]
        )

    with col3:

        st.metric(
            "Missing",
            info["Missing Values"]
        )

    with col4:

        st.metric(
            "Duplicates",
            info["Duplicate Rows"]
        )