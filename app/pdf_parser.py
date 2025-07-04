import fitz  # PyMuPDF

def parse_uploaded_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    full_text = ""

    for page in doc:
        full_text += page.get_text()

    return full_text
