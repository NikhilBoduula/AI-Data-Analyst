import streamlit as st


def control_center(progress, next_step,
                   health="Excellent",
                   brain_status="Online"):

    st.markdown(
        f"""
<div class="glass-card">

<h2>🧠 AI Control Center</h2>

<table style="width:100%;color:white;">

<tr>
<td><b>🤖 Brain Status</b></td>
<td><span class="status-online">🟢 {brain_status}</span></td>
</tr>

<tr>
<td><b>❤️ Pipeline Health</b></td>
<td>{health}</td>
</tr>

<tr>
<td><b>📈 Progress</b></td>
<td>{progress}%</td>
</tr>

<tr>
<td><b>🎯 Next Action</b></td>
<td>{next_step}</td>
</tr>

</table>

</div>
""",
        unsafe_allow_html=True
    )