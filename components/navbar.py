import streamlit as st

def navbar():
    st.markdown(
        """
        <nav style="
            background-color: #ffffff;
            padding: 1rem 2rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            border-bottom: 1px solid #e0e0e0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        ">
            <div style="font-weight:700; font-size: 1.2rem; color:#007bff;">Resume Screening App</div>
            <div>
                <a href="/" style="margin-right:1rem; text-decoration:none; color:#333;">Home</a>
                <a href="/pages/screening.py" style="margin-left:1rem; text-decoration:none; color:#333;">Screening</a>
            </div>
        </nav>
        """,
        unsafe_allow_html=True
    )
