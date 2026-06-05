# 📄 AI Resume Analyzer & ATS Optimizer

An AI-powered Resume Analyzer that helps job seekers optimize their resumes for Applicant Tracking Systems (ATS). Upload your resume, compare it against a job description, get an ATS compatibility score, identify missing keywords, and receive AI-powered suggestions to improve your resume.

---

## 🚀 Live Demo

🔗 https://airesumedetector-nzekpvxxnirfqqnj9izyn3.streamlit.app/

---

## 📂 GitHub Repository

🔗 https://github.com/Anshu1109/AI_resume_detector

---

## ✨ Features

### 📊 ATS Score Analysis
- Calculates resume-job description match percentage.
- Helps users understand ATS compatibility.

### 🔍 Keyword Matching
- Extracts important keywords from the job description.
- Identifies missing keywords in the resume.

### 🤖 AI Resume Improvement
- Uses Google Gemini AI to improve resume content.
- Suggests stronger and more impactful bullet points.

### 📄 Resume Parsing
- Extracts text from PDF resumes automatically.
- Supports quick resume analysis.

### 🌐 User-Friendly Interface
- Built with Streamlit.
- Clean and responsive UI.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Core Programming Language |
| Streamlit | Web Application Framework |
| Google Gemini AI | Resume Improvement Suggestions |
| PDFPlumber | PDF Text Extraction |
| Pandas | Data Processing |
| Git & GitHub | Version Control |

---

## 📁 Project Structure

```text
AI_resume_detector/
│
├── app.py                 # Main Streamlit App
├── resume_parser.py       # Resume Text Extraction
├── ats_score.py           # ATS Score Calculation
├── ai_helper.py           # Gemini AI Integration
├── requirements.txt       # Project Dependencies
├── runtime.txt            # Python Runtime Version
└── README.md              # Project Documentation
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/Anshu1109/AI_resume_detector.git
cd AI_resume_detector
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Mac/Linux

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## 🔑 Environment Variables

Create a `.env` file and add your Gemini API Key:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

## 📸 How It Works

1. Upload your Resume (PDF).
2. Paste the Job Description.
3. Click Analyze.
4. View:
   - ATS Score
   - Missing Keywords
   - AI-Powered Resume Suggestions

---

## 🎯 Future Improvements

- DOCX Resume Support
- Resume Download Feature
- Multiple Resume Comparison
- Advanced ATS Scoring
- Job Recommendation System

---

## 👨‍💻 Author

**Anshu Kumar**

B.Tech CSE (AI & ML)

GitHub: https://github.com/Anshu1109

---
## ⭐ Support
If you found this project useful, consider giving it a ⭐ on GitHub.
