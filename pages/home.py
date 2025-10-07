
import streamlit as st
from components import navbar, footer

# Show navbar
navbar.navbar()

st.markdown("""
<style>
.hero {
    background-color: #007bff;
    color: white;
    padding: 4rem 2rem;
    border-radius: 10px;
    text-align: center;
}
.hero h1 {
    font-size: 3rem;
    margin-bottom: 1rem;
}
.hero p {
    font-size: 1.2rem;
    margin-bottom: 2rem;
}
.features {
    display: flex;
    justify-content: space-between;
    margin-top: 3rem;
}
.feature-card {
    background-color: #fff;
    padding: 2rem;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    flex: 1;
    margin: 0 1rem;
    text-align: center;
}
.feature-card h3 {
    margin-bottom: 1rem;
    color: #007bff;
}
.start-button {
    background-color: white;
    color: #007bff;
    padding: 0.8rem 2rem;
    border-radius: 5px;
    text-decoration: none;
    font-weight: bold;
    display: inline-block;
}
.start-button:hover {
    background-color: #e0e0e0;
}
</style>
""", unsafe_allow_html=True)

# Hero section
st.markdown("""
<div class="hero">
    <h1>Resume Screening Made Easy</h1>
    <p>Upload resumes, extract text, and score them automatically using keyword matching.</p>
    <a href="/pages/screening.py" class="start-button">Start Screening</a>
</div>
""", unsafe_allow_html=True)

# Features section
st.markdown("""
<div class="features">
    <div class="feature-card">
        <h3>Fast Upload</h3>
        <p>Upload multiple resumes in seconds with a simple drag-and-drop interface.</p>
    </div>
    <div class="feature-card">
        <h3>Automatic Extraction</h3>
        <p>Extract text from PDF or DOCX files without manual effort.</p>
    </div>
    <div class="feature-card">
        <h3>Keyword Matching</h3>
        <p>Score resumes automatically based on required skills and keywords.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
footer.footer()
