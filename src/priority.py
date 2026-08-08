def freshness_points(priority):
    priority = str(priority).lower()

    if "highest" in priority:
        return 30
    elif "very high" in priority:
        return 25
    elif "high" in priority:
        return 20
    elif "medium" in priority:
        return 10
    else:
        return 5


def role_points(role, skills):
    text = f"{role} {skills}".lower()

    tier_1 = [
        "python developer",
        "backend",
        "fastapi",
        "data analyst",
        "business analyst"
    ]

    tier_2 = [
        "data scientist",
        "machine learning",
        "ml engineer",
        "ai engineer",
        "analytics engineer"
    ]

    tier_3 = [
        "data engineer",
        "spark",
        "kafka",
        "etl"
    ]

    if any(word in text for word in tier_1):
        return 25

    if any(word in text for word in tier_2):
        return 20

    if any(word in text for word in tier_3):
        return 15

    return 10


def source_points(source):
    source = str(source).lower()

    if "manual" in source:
        return 20
    elif "cutshort" in source:
        return 18
    elif "wellfound" in source:
        return 18
    elif "remotive" in source:
        return 15
    elif "remoteok" in source:
        return 15
    else:
        return 10


def experience_points(experience):
    text = str(experience).lower()

    if "fresher" in text:
        return 20
    elif "0-1" in text:
        return 20
    elif "0-2" in text:
        return 18
    elif "1-2" in text:
        return 15
    elif "check" in text:
        return 8
    else:
        return 5


def calculate_final_priority_score(
    match_score,
    freshness_priority,
    role,
    skills,
    source,
    experience
):
    try:
        match_score = int(match_score)
    except Exception:
        match_score = 0

    final_score = (
        int(match_score * 0.35)
        + freshness_points(freshness_priority)
        + role_points(role, skills)
        + source_points(source)
        + experience_points(experience)
    )

    if final_score > 100:
        final_score = 100

    if final_score >= 80:
        label = "Apply First"
    elif final_score >= 65:
        label = "High Priority"
    elif final_score >= 50:
        label = "Medium Priority"
    else:
        label = "Low Priority"

    return final_score, label