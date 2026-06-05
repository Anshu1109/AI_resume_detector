import streamlit as st

from resume_parser import extract_text_from_pdf
from ats_score import calculate_ats_score
from ai_helper import improve_resume

st.set_page_config(
    page_title="AI Resume Analyzer",
    layout="wide"
)

st.title("📄 AI Resume Analyzer & ATS Optimizer")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description Here"
)

if uploaded_file and job_description:

    resume_text = extract_text_from_pdf(
        uploaded_file
    )

    score, keywords = calculate_ats_score(
        resume_text,
        job_description
    )

    st.subheader("ATS Score")

    st.metric(
        "Match Score",
        f"{score}%"
    )

    st.subheader("Matched Keywords")

    st.write(list(keywords))

    if st.button("Generate AI Suggestions"):

        with st.spinner(
            "Analyzing Resume..."
        ):

            result = improve_resume(
                resume_text
            )

            st.subheader(
                "AI Recommendations"
            )

            st.write(result)