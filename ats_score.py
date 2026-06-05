import re

def calculate_ats_score(resume_text, job_description):

    resume_words = set(
        re.findall(r'\w+', resume_text.lower())
    )

    jd_words = set(
        re.findall(r'\w+', job_description.lower())
    )

    matched_keywords = resume_words.intersection(jd_words)

    score = (
        len(matched_keywords) /
        max(len(jd_words), 1)
    ) * 100

    return round(score, 2), matched_keywords