def select_resume(job_title, job_description):

    text = f"{job_title} {job_description}".lower()

    if any(
        word in text
        for word in [
            "ai",
            "machine learning",
            "ml",
            "llm"
        ]
    ):
        return "ai_resume.pdf"

    elif any(
        word in text
        for word in [
            "data scientist",
            "data engineer",
            "spark",
            "kafka"
        ]
    ):
        return "data_resume.pdf"

    elif any(
        word in text
        for word in [
            "backend",
            "fastapi",
            "api",
            "python developer"
        ]
    ):
        return "backend_resume.pdf"

    else:
        return "analyst_resume.pdf"