import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def improve_resume(resume_text):

    prompt = f"""
    Analyze this resume.

    Resume:
    {resume_text}

    Give:

    1. ATS improvement suggestions
    2. Better bullet points
    3. Missing skills
    4. Resume score out of 100
    """

    response = model.generate_content(prompt)

    return response.text