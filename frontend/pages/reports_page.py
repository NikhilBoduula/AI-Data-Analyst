import streamlit as st

from frontend.services.api_client import APIClient


def render_reports_page():

    st.title("📄 Reports")

    st.write("Generate a complete AI Data Scientist report.")

    st.divider()

    if st.button("🚀 Generate PDF Report", use_container_width=True):

        with st.spinner("Generating report..."):

            result = APIClient.run_reports(
                st.session_state["dataset_path"],
                st.session_state["dataset_name"],
                st.session_state.get("automl_results"),
                st.session_state.get("shap_results")
            )

        st.success("✅ Report Generated Successfully!")

        output_path = result["pdf_path"]

        with open(output_path, "rb") as pdf:

            st.download_button(
                label="⬇ Download PDF",
                data=pdf,
                file_name="AI_Data_Scientist_Report.pdf",
                mime="application/pdf",
                use_container_width=True
            )