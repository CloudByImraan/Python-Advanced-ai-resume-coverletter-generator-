# 🤖 AI Resume & Cover Letter Generator

## 📌 Project Overview

This is a beginner-friendly **AI-powered web application** that helps users generate:

* ✅ Professional Resume
* ✅ Job-specific Cover Letter

All you need to do is:

* Enter your personal details
* Paste a job description

👉 The system uses Artificial Intelligence to generate high-quality documents for you.

---

## 🚀 What This Project Does

This application:

* Takes user input (name, email, phone, skills, job description)
* Sends the data to an AI model
* Generates:

  * A professional resume
  * A tailored cover letter
* Converts them into downloadable PDF files

---

## 🧠 Technologies Used

* **Python** → Programming language
* **Streamlit** → Web interface (UI)
* **Gemini API** → AI text generation
* **ReportLab** → PDF generation
* **dotenv** → Secure API key management

---

## 📁 Project Structure

```
ai-resume-coverletter-generator/
│── app.py                  # Main Streamlit app (UI)
│── generator.py            # AI logic
│── utils.py                # Helper functions (validation, PDF)
│── prompts.py              # AI prompt template
│── requirements.txt        # Dependencies
│── .env                    # API key (not uploaded to GitHub)
│── .gitignore              # Ignore unnecessary files
│
├── generated/              # Generated PDF files
│   ├── resume.pdf
│   ├── cover_letter.pdf
│
└── README.md
```

---

## ⚙️ How to Run This Project (Step-by-Step)

### 🟢 Step 1: Clone or Download the Project

```bash
git clone <your-repo-link>
cd ai-resume-coverletter-generator
```

---

### 🟢 Step 2: Install Required Packages

```bash
pip install -r requirements.txt
```

---

### 🟢 Step 3: Get Your API Key

1. Go to: https://aistudio.google.com/app/apikey
2. Click **Create API Key**
3. Copy your key

---

### 🟢 Step 4: Create `.env` File

Create a file named `.env` and add:

```
GEMINI_API_KEY=your_api_key_here
```

---

### 🟢 Step 5: Run the App

```bash
python -m streamlit run app.py
```

---

### 🟢 Step 6: Open in Browser

You will see a link like:

```
http://localhost:8501
```

👉 Open it in your browser.

---

## 🧪 How to Use the App

1. Enter your:

   * Full Name
   * Email
   * Phone Number
   * Skills

2. Paste a Job Description

3. Click **Generate Documents**

4. Download:

   * Resume PDF
   * Cover Letter PDF

---

## ⚠️ Important Notes

* Do NOT upload your `.env` file to GitHub
* Make sure you have internet connection (AI needs it)
* If Streamlit doesn’t run, use:

```bash
python -m streamlit run app.py
```

---

## 💡 Future Improvements (Optional)

* Add interview question generator
* Improve PDF styling
* Add user authentication
* Deploy the app online

---

## 👨‍💻 Author

Built as part of a Python + AI learning project.

---

## ⭐ Final Note

This project is beginner-friendly but also demonstrates:

* API integration
* File handling
* Error handling
* Clean project structure

👉 A solid project for your GitHub portfolio.
