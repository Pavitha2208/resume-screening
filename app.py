import streamlit as st
import pdfplumber
import pytesseract
from PIL import Image
import pandas as pd
import re

# -----------------------------
# App title
# -----------------------------
st.title("Resume Screening App")
st.write("Upload resumes (PDF or Image) to start screening.")

# -----------------------------
# Configure Tesseract OCR
# -----------------------------
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# -----------------------------
# File uploader (single uploader for PDFs & images)
# -----------------------------
uploaded_files = st.file_uploader(
    "Upload resumes (PDF or Image)",
    type=["pdf", "png", "jpg", "jpeg"],
    accept_multiple_files=True,
    key="resume_uploader_unique"  # MUST be unique
)

# -----------------------------
# Process uploaded resumes
# -----------------------------
if uploaded_files:
    results = []

    for uploaded_file in uploaded_files:
        text = ""

        # Extract text based on file type
        if uploaded_file.type == "application/pdf":
            with pdfplumber.open(uploaded_file) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text
        else:
            image = Image.open(uploaded_file)
            text = pytesseract.image_to_string(image)

        # -----------------------------
        # Extract email and phone
        # -----------------------------
        email = re.findall(r"\S+@\S+", text)
        phone = re.findall(r'\+?\d[\d -]{8,12}\d', text)

        # -----------------------------
        # Extract skills
        # -----------------------------
        skills_list = ["Python", "Java", "SQL", "Excel", "Machine Learning", "Deep Learning", "NLP"]
        found_skills = [skill for skill in skills_list if skill.lower() in text.lower()]

        # -----------------------------
        # Compute resume score
        # -----------------------------
        job_skills = ["Python", "Machine Learning", "SQL"]  # Example job requirements
        score = len(set(found_skills) & set(job_skills)) / len(job_skills) * 100

        # -----------------------------
        # Store results
        # -----------------------------
        results.append({
            "Filename": uploaded_file.name,
            "Email": ", ".join(email) if email else "Not found",
            "Phone": ", ".join(phone) if phone else "Not found",
            "Skills": ", ".join(found_skills) if found_skills else "None",
            "Score (%)": f"{score:.2f}"
        })

    # -----------------------------
    # Display results in a table
    # -----------------------------
    df = pd.DataFrame(results)
    st.subheader("Resume Screening Results")
    st.dataframe(df)

    # -----------------------------
    # CSV Download
    # -----------------------------
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Results as CSV",
        data=csv,
        file_name='resume_screening_results.csv',
        mime='text/csv'
    )

