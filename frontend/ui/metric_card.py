import streamlit as st


def metric_card(title, value, icon="📊", color="#8B5CF6"):

    st.markdown(
        f"""
<div class="metric-card">

<div class="metric-icon">
{icon}
</div>

<div class="metric-title">
{title}
</div>

<div class="metric-value" style="color:{color};">
{value}
</div>

</div>
""",
        unsafe_allow_html=True
    )