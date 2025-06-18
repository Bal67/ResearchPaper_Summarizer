import fitz 
import re

def parse_uploaded_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    full_text = ""

    for page in doc:
        full_text += page.get_text()

    return extract_sections(full_text)

def extract_sections(text):
    sections = {}
    
    # Heuristic split based on headings often found in academic papers
    pattern = re.compile(r"\n(?=[A-Z][A-Za-z ]{3,40})\n")  
    chunks = pattern.split(text)

    for chunk in chunks:
        lines = chunk.strip().split("\n")
        if len(lines) >= 2:
            title = lines[0].strip()
            content = "\n".join(lines[1:]).strip()
            if 20 < len(content) < 10000:  
                sections[title] = content

    return type("ParsedPDF", (), {"sections": sections})()  
