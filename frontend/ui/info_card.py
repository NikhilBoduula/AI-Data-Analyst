import streamlit as st


def info_card(title, items):

    with st.container(border=True):

        st.subheader(title)

        st.write("")

        for label, value in items:

            left, right = st.columns([1, 1])

            with left:
                st.caption(label)

            with right:
                st.markdown(
                    f"<h3 style='text-align:right'>{value}</h3>",
                    unsafe_allow_html=True
                )

            st.divider()