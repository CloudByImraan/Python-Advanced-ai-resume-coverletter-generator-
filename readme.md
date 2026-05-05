# 🤖 AI Resume & Cover Letter Generator

An AI-powered web application that generates professional resumes and job-specific cover letters using user input and job descriptions.

Built with **Python, Streamlit, and Gemini API**, this project demonstrates real-world AI integration and document automation.

---

## 📌 Overview

This application allows users to:

* Enter personal and professional details
* Paste a job description
* Generate:

  * ✅ Professional Resume
  * ✅ Tailored Cover Letter
* Download both as PDF files

---

## 🚀 Features

* 🤖 AI-powered text generation
* 📄 Resume & Cover Letter creation
* 📥 Download as PDF
* 🧠 Smart prompt-based generation
* 🌐 Interactive web interface (Streamlit)

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Gemini API
* ReportLab
* dotenv

---

## 🧠 How It Works

1. User inputs personal details
2. Job description is provided
3. Data is sent to AI (Gemini API)
4. AI generates:

   * Resume content
   * Cover letter
5. Files are converted to PDF and saved

---

## 🖥️ UI Layout (Simplified View)

```text
+--------------------------------------+
|   AI Resume Generator                |
+--------------------------------------+

[ Full Name        ____________ ]
[ Email            ____________ ]
[ Phone            ____________ ]
[ Skills           ____________ ]

[ Job Description ]
----------------------------------------
| Paste job description here...         |
----------------------------------------

        [ Generate Documents ]

----------------------------------------
| ✅ Resume Generated                  |
| ✅ Cover Letter Generated            |
----------------------------------------

[ Download Resume ]   [ Download Cover Letter ]
```

---

## 📂 Project Structure

```bash
ai-resume-coverletter-generator/
│
├── app.py
├── generator.py
├── utils.py
├── prompts.py
├── requirements.txt
├── .env
├── .gitignore
│
├── generated/
│   ├── resume.pdf
│   ├── cover_letter.pdf
│
└── README.md
```

---

## ▶️ How to Run

```bash
# Clone repository
git clone <your-repo-link>

# Navigate into folder
cd ai-resume-coverletter-generator

# Install dependencies
pip install -r requirements.txt

# Run app
python -m streamlit run app.py
```

---

## 🔑 Setup API Key

1. Get API key from Google AI Studio
2. Create `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

⚠️ Do NOT upload `.env` to GitHub

---

## 🎓 What You Will Learn

* API integration in Python
* Building web apps with Streamlit
* Prompt engineering basics
* Generating PDFs programmatically
* Structuring real-world projects

---

## 🖥️ Sample Output (Terminal)

```bash
Running on http://localhost:8501
```

---

## 🚧 Project Status

✅ Completed ( Mini Advanced Project)

---

## 🔮 Future Improvements

### 🎨 UI/UX Improvements

* Better layout and styling
* Add icons and animations
* Improve user experience

### 🌐 Deployment

* Deploy on:

  * Streamlit Cloud
  * Render
  * Hugging Face Spaces

### 🤖 AI Enhancements

* Custom tone and experience level
* Better formatting output
* Improved prompt engineering

### 📄 Download Options

* Add DOCX format support

### 🔐 Authentication

* User login system
* Save generated documents

---

## 👨‍💻 Author

Imraan Mu'hd Sani

---

## ⭐ Final Note

This project demonstrates:

* Real-world AI integration
* File handling and automation
* Clean modular project structure

👉 A Ministrong portfolio project for showcasing AI + Python skills.

💡 This project demonstrates my current approach and can be further enhanced with more advanced features and optimizations.
📌 Built as part of my early learning phase in machine learning and application development.
