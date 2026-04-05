import os
import re
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch


# ---------------------------------------------------------
# CUSTOM EXCEPTION
# Used for raising validation-specific errors
# ---------------------------------------------------------
class ValidationError(Exception):
    """Custom exception for validation errors"""
    pass


class Utils:
    """
    Utility class that handles:
    - Input validation (email, phone)
    - Cleaning AI-generated text
    - Saving content as PDF
    """

    # -----------------------------------------------------
    # EMAIL VALIDATION
    # Uses regex to ensure proper email format
    # -----------------------------------------------------
    @staticmethod
    def validate_email(email):
        pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

        if not re.fullmatch(pattern, email):
            raise ValidationError("Invalid email format.")

        return True

    # -----------------------------------------------------
    # PHONE NUMBER VALIDATION
    # Accepts international format (+234..., etc.)
    # -----------------------------------------------------
    @staticmethod
    def validate_phone(phone):
        pattern = r"^\+?\d{7,15}$"

        if not re.fullmatch(pattern, phone):
            raise ValidationError("Invalid phone number format.")

        return True

    # -----------------------------------------------------
    # CLEAN AI TEXT
    # Removes unwanted markdown and extra spacing
    # -----------------------------------------------------
    @staticmethod
    def clean_text(text):
        # Remove markdown symbols like # and *
        text = re.sub(r"[#*]", "", text)

        # Replace excessive newlines with just two
        text = re.sub(r"\n{3,}", "\n\n", text)

        return text.strip()

    # -----------------------------------------------------
    # SAVE CONTENT AS PDF
    # Uses reportlab to generate formatted PDF files
    # -----------------------------------------------------
    @staticmethod
    def save_pdf(file_path, content):

        # Ensure directory exists before saving
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Create PDF document
        doc = SimpleDocTemplate(file_path)

        elements = []  # Holds content blocks
        styles = getSampleStyleSheet()

        # -------------------------------------------------
        # PROCESS TEXT LINE BY LINE
        # Each line becomes a paragraph in the PDF
        # -------------------------------------------------
        for line in content.split("\n"):

            # Skip empty lines to avoid clutter
            if line.strip():
                elements.append(Paragraph(line, styles["Normal"]))
                elements.append(Spacer(1, 0.2 * inch))

        # -------------------------------------------------
        # BUILD PDF DOCUMENT
        # -------------------------------------------------
        doc.build(elements)