import streamlit as st

# Load CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles/main.css")

# Default landing page
st.set_page_config(
    page_title="Resume Screening App",
    page_icon="📄",
    layout="wide"
)

st.title("Welcome to the Resume Screening App")
st.write("Use the top menu to navigate between Home and Resume Screening pages.")

