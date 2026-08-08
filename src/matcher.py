USER_SKILLS = [
    "python",
    "sql",
    "fastapi",
    "machine learning",
    "ml",
    "ai",
    "llm",
    "kafka",
    "spark",
    "docker",
    "pandas",
    "numpy",
    "scikit-learn",
    "data analysis",
    "data science",
    "api",
    "backend",
    "streamlit"
]


def calculate_match_score(job_text):
    job_text = str(job_text).lower()

    matches = 0

    for skill in USER_SKILLS:
        if skill in job_text:
            matches += 1

    score = int((matches / len(USER_SKILLS)) * 100)

    return score