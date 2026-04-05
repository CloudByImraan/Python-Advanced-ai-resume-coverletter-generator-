import os
import google.generativeai as genai
from dotenv import load_dotenv
from utils import Utils
from prompts import get_prompt

# ---------------------------------------------------------
# LOAD ENVIRONMENT VARIABLES
# This loads your API key from the .env file
# ---------------------------------------------------------
load_dotenv()


class ResumeGenerator:
    """
    This class handles:
    - Connecting to Gemini API
    - Generating Resume & Cover Letter
    - Cleaning and saving output
    """

    def __init__(self):
        # -------------------------------------------------
        # GET API KEY FROM .env FILE
        # -------------------------------------------------
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise Exception("Gemini API key not found in .env file")

        # -------------------------------------------------
        # CONFIGURE GEMINI API
        # -------------------------------------------------
        genai.configure(api_key=api_key)

        # Initialize AI model
        self.model = genai.GenerativeModel("models/gemini-2.5-flash")

    def generate_documents(self, name, email, phone, skills, job_description):
        """
        Generates resume and cover letter using AI
        """

        # -------------------------------------------------
        # PROMPT ENGINEERING (VERY IMPORTANT 🔥)
        # This tells the AI exactly what to do
        # -------------------------------------------------
        prompt = get_prompt(name, email, phone, skills, job_description)

        # -------------------------------------------------
        # CALL AI MODEL
        # -------------------------------------------------
        response = self.model.generate_content(prompt)

        # -------------------------------------------------
        # CLEAN AI OUTPUT
        # -------------------------------------------------
        clean_text = Utils.clean_text(response.text)

        # -------------------------------------------------
        # SPLIT INTO RESUME & COVER LETTER
        # -------------------------------------------------
        parts = clean_text.split("Cover Letter")

        resume_text = parts[0].strip()

        if len(parts) > 1:
            cover_letter_text = "Cover Letter\n" + parts[1].strip()
        else:
            cover_letter_text = "Professional cover letter generated."

        # -------------------------------------------------
        # ENSURE OUTPUT FOLDER EXISTS
        # -------------------------------------------------
        os.makedirs("generated", exist_ok=True)

        # -------------------------------------------------
        # SAVE AS PDF
        # -------------------------------------------------
        Utils.save_pdf("generated/resume.pdf", resume_text)
        Utils.save_pdf("generated/cover_letter.pdf", cover_letter_text)

        # -------------------------------------------------
        # RETURN TEXT (USED BY STREAMLIT)
        # -------------------------------------------------
        return resume_text, cover_letter_text