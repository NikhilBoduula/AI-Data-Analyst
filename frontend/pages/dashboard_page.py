import streamlit as st


def render_dashboard_page():

    st.title("🏠 Dashboard")

    st.write(
        "Welcome to the Autonomous AI Data Scientist Platform."
    )

    st.divider()

    if st.session_state["dataset"] is None:

        st.info(
            "Upload a dataset from the Upload Dataset page to begin."
        )

        return

    df = st.session_state["dataset"]

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Rows",
        df.shape[0]
    )

    col2.metric(
        "Columns",
        df.shape[1]
    )

    col3.metric(
        "Missing Values",
        int(df.isna().sum().sum())
    )

    st.divider()

    st.subheader("Dataset Preview")

    st.dataframe(
        df.head(),
        use_container_width=True
    )