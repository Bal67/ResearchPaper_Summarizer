import streamlit as st
from app.auth import login
from app.monitoring import log_event
from app.pdf_parser import parse_uploaded_pdf
from app.bedrock_client import call_claude

login()  # Require login before continuing

st.title("Research Paper Summarizer")

uploaded_file = st.file_uploader("Upload a research paper (PDF)", type="pdf")
if uploaded_file:
    st.info("Parsing PDF...")
    doc = parse_uploaded_pdf(uploaded_file)

    if not doc.sections:
        st.error("No sections found in the document.")
    else:
        st.success("Document parsed successfully.")
        section_list = list(doc.sections.keys())
        selected_section = st.selectbox("Choose a section to summarize", section_list)

        if selected_section and st.button("Summarize Section"):
            text_to_summarize = doc.sections[selected_section][:5000]
            log_event("demo", "Summarize", selected_section)
            prompt = f"""You are an AI assistant. Summarize the '{selected_section}' section of this research paper in plain English. Mention key methods, results, or conclusions:\n\n{text_to_summarize}"""
            response = call_claude(prompt)

            st.subheader("Claude 3.5's Summary")
            st.write(response)
