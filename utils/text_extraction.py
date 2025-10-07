# utils/text_extraction.py

import pdfplumber
from docx import Document

def extract_text(file):
    filename = file.name.lower()
    
    if filename.endswith(".pdf"):
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text.strip()
    
    elif filename.endswith(".docx"):
        doc = Document(file)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text.strip()
    
    else:
        return "Unsupported file format. Please upload PDF or DOCX."
