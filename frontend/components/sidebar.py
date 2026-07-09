import streamlit as st


def render_sidebar():
    """
    Enterprise Sidebar
    """

    with st.sidebar:

        st.title("🤖 AutoDS AI")

        st.caption("Autonomous AI Data Scientist")

        st.divider()

        selected_page = st.radio(

            "Navigation",

            [

                "🏠 Dashboard",

                "📂 Upload Dataset",

                "🧹 Data Cleaning",

                "📊 EDA",

                "📈 Visualization",

                "🛠 Feature Engineering",

                "🤖 AutoML",

                "📄 Reports",

                "💬 AI Assistant"

            ]

        )

        st.divider()

        st.subheader("Current Dataset")

        if st.session_state["dataset"] is None:

            st.warning("No Dataset Uploaded")

        else:

            st.success(st.session_state["dataset_name"])

            st.write(

                f"Rows : {st.session_state['dataset'].shape[0]}"

            )

            st.write(

                f"Columns : {st.session_state['dataset'].shape[1]}"

            )

        st.divider()

        st.caption("Version 2.0")

    return selected_page