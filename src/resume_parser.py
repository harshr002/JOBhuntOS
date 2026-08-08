from pypdf import PdfReader


KNOWN_SKILLS = [
    "python",
    "sql",
    "power bi",
    "excel",
    "tableau",
    "fastapi",
    "machine learning",
    "deep learning",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "docker",
    "kafka",
    "spark",
    "aws",
    "azure",
    "git",
    "react",
    "java",
    "c++",
    "data analysis",
    "statistics",
    "llm",
    "langchain"
]


def extract_resume_text(pdf_path):
    text = ""

    try:

        reader = PdfReader(
            pdf_path
        )

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    except Exception as e:

        print(
            "Resume parse error:",
            e
        )

    return text.lower()


def extract_resume_skills(resume_text):

    found_skills = []

    for skill in KNOWN_SKILLS:

        if skill.lower() in resume_text:

            found_skills.append(
                skill
            )

    return found_skills


def parse_resume(pdf_path):

    resume_text = extract_resume_text(
        pdf_path
    )

    skills = extract_resume_skills(
        resume_text
    )

    return {
        "raw_text": resume_text,
        "skills": skills
    }
