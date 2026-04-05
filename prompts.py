# prompts.py

def get_prompt(name, email, phone, skills, job_description):
    return f"""
    You are a professional resume writer.

    Generate:
    1. A professional Resume
    2. A professional Cover Letter

    RULES:
    - No markdown
    - No hashtags
    - No asterisks
    - Use clean formatting
    - Make it realistic and job-specific

    USER DETAILS:
    Name: {name}
    Email: {email}
    Phone: {phone}
    Skills: {skills}

    JOB DESCRIPTION:
    {job_description}

    Separate both using:
    "Cover Letter"
    """