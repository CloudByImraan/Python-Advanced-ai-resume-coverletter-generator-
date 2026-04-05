import streamlit as st
from generator import ResumeGenerator   # Updated import (clean structure)
from utils import Utils, ValidationError

# ---------------------------------------------------------
# PAGE CONFIGURATION
# This sets the title and layout of the Streamlit app
# ---------------------------------------------------------
st.set_page_config(
    page_title="AI Resume Generator",
    layout="centered"
)

# ---------------------------------------------------------
# APP TITLE
# ---------------------------------------------------------
st.title("AI Resume & Cover Letter Generator")

# ---------------------------------------------------------
# SESSION STATE
# Used to store generated results so they persist after refresh
# ---------------------------------------------------------
if "resume" not in st.session_state:
    st.session_state.resume = None

if "cover" not in st.session_state:
    st.session_state.cover = None

# ---------------------------------------------------------
# USER INPUT FIELDS
# Streamlit automatically creates UI components
# ---------------------------------------------------------
name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
skills = st.text_area("Skills (e.g Python, Data Analysis, SQL)")
job_description = st.text_area("Paste Job Description")

# ---------------------------------------------------------
# GENERATE BUTTON LOGIC
# Runs when user clicks the button
# ---------------------------------------------------------
if st.button("Generate Documents"):

    try:
        # -------------------------------
        # INPUT VALIDATION
        # -------------------------------
        Utils.validate_email(email)
        Utils.validate_phone(phone)

        # -------------------------------
        # CALL AI GENERATOR
        # -------------------------------
        generator = ResumeGenerator()

        resume, cover = generator.generate_documents(
            name,
            email,
            phone,
            skills,
            job_description
        )

        # -------------------------------
        # SAVE RESULTS IN SESSION STATE
        # -------------------------------
        st.session_state.resume = resume
        st.session_state.cover = cover

        st.success("Documents generated successfully!")

    except ValidationError as e:
        # Custom validation error (clean error message)
        st.error(str(e))

    except Exception as e:
        # Catch unexpected errors
        st.error(f"System Error: {e}")

# ---------------------------------------------------------
# DOWNLOAD SECTION
# Only shows after documents are generated
# ---------------------------------------------------------
if st.session_state.resume:
    with open("generated/resume.pdf", "rb") as f:
        st.download_button(
            label="Download Resume PDF",
            data=f,
            file_name="Resume.pdf",
            mime="application/pdf"
        )

if st.session_state.cover:
    with open("generated/cover_letter.pdf", "rb") as f:
        st.download_button(
            label="Download Cover Letter PDF",
            data=f,
            file_name="Cover_Letter.pdf",
            mime="application/pdf"
        )