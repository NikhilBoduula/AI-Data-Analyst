import streamlit as st

from backend.reports.report_builder import ReportBuilder
from backend.reports.pdf_generator import PDFGenerator


def render_reports_page():

    st.title("📄 Reports")

    st.write(
        "Generate a complete AI Data Scientist report."
    )

    st.divider()

    if st.button("🚀 Generate PDF Report", use_container_width=True):

        with st.spinner("Generating report..."):

            report = ReportBuilder.build()

            output_path = "AI_Data_Scientist_Report.pdf"

            PDFGenerator.generate(
                report,
                output_path
            )

        st.success("✅ Report Generated Successfully!")

        with open(output_path, "rb") as pdf:

            st.download_button(

                label="⬇ Download PDF",

                data=pdf,

                file_name="AI_Data_Scientist_Report.pdf",

                mime="application/pdf",

                use_container_width=True

            )