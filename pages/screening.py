import streamlit as st
from components import navbar, footer
from utils import text_extraction, matcher

# Show navbar
navbar.navbar()

st.markdown("""
<style>
.resume-card {
    background-color: #fff;
    padding: 1.5rem;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    margin-bottom: 2rem;
}
.resume-card h3 {
    color: #007bff;
    margin-bottom: 0.5rem;
}
.score-badge {
    background-color: #007bff;
    color: white;
    padding: 0.4rem 0.8rem;
    border-radius: 5px;
    font-weight: bold;
    display: inline-block;
}
</style>
""", unsafe_allow_html=True)

st.title("📄 Resume Screening")

uploaded_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"], accept_multiple_files=True)

if uploaded_file:
    for file in uploaded_file:
        # Extract text
        resume_text = text_extraction.extract_text(file)
        
        # Keyword matching
        keywords = ["Python", "Machine Learning", "Data Science"]
        score, matched = matcher.match_keywords(resume_text, keywords)
        
        # Display resume in a card
        st.markdown(f"""
        <div class="resume-card">
            <h3>{file.name}</h3>
            <p><strong>Matched Keywords:</strong> {', '.join(matched) if matched else 'None'}</p>
            <p><strong>Score:</strong> <span class="score-badge">{score}/100</span></p>
            <details>
                <summary>View Extracted Text</summary>
                <p>{resume_text.replace('\n','<br>')}</p>
            </details>
        </div>
        """, unsafe_allow_html=True)

# Footer
footer.footer()

