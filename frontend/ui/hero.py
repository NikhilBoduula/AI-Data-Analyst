import streamlit as st


def hero(title, subtitle):

    st.markdown(
        f"""
<div class="hero">

<div class="hero-title">
🤖 {title}
</div>

<div class="hero-subtitle">
{subtitle}
</div>

</div>
""",
        unsafe_allow_html=True
    )