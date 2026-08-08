import requests
from datetime import datetime, timezone


TARGET_KEYWORDS = [
    "python",
    "backend",
    "fastapi",
    "data",
    "analyst",
    "scientist",
    "machine learning",
    "ai",
    "ml",
    "engineer"
]


def estimate_posted_time(created_at):

    try:

        posted = datetime.fromisoformat(
            created_at.replace("Z", "+00:00")
        )

        now = datetime.now(timezone.utc)

        diff_hours = (
            now - posted
        ).total_seconds() / 3600

        if diff_hours <= 1:
            return "0-1 hour ago"

        elif diff_hours <= 6:
            return "1-6 hours ago"

        elif diff_hours <= 24:
            return "6-24 hours ago"

        elif diff_hours <= 72:
            return "1-3 days ago"

        else:
            return "3+ days ago"

    except:
        return "3+ days ago"


def relevant_job(title, description):

    text = f"{title} {description}".lower()

    return any(
        keyword in text
        for keyword in TARGET_KEYWORDS
    )


# SOURCE 1
def fetch_remoteok():

    jobs = []

    try:

        response = requests.get(
            "https://remoteok.com/api",
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=20
        )

        data = response.json()

        for item in data[1:]:

            title = item.get("position", "")
            company = item.get("company", "")
            description = item.get("description", "")
            link = item.get("url", "")
            date = item.get("date", "")

            if not relevant_job(title, description):
                continue

            jobs.append({
                "source": "RemoteOK",
                "company": company,
                "role": title,
                "location": "Remote",
                "posted_time": estimate_posted_time(date),
                "job_link": link,
                "experience": "Check JD",
                "skills": description[:1000]
            })

    except:
        pass

    return jobs


# SOURCE 2
def fetch_remotive():

    jobs = []

    try:

        response = requests.get(
            "https://remotive.com/api/remote-jobs",
            timeout=20
        )

        data = response.json()

        for item in data.get("jobs", []):

            title = item.get("title", "")
            company = item.get("company_name", "")
            description = item.get("description", "")
            link = item.get("url", "")
            date = item.get(
                "publication_date",
                ""
            )

            if not relevant_job(title, description):
                continue

            jobs.append({
                "source": "Remotive",
                "company": company,
                "role": title,
                "location": "Remote",
                "posted_time": estimate_posted_time(date),
                "job_link": link,
                "experience": "Check JD",
                "skills": description[:1000]
            })

    except:
        pass

    return jobs


# SOURCE 3
def fetch_wellfound():

    jobs = [
        {
            "source": "Wellfound",
            "company": "Startup Hiring",
            "role": "AI Engineer Startup",
            "location": "Remote / India",
            "posted_time": "0-24 hours ago",
            "job_link": "https://wellfound.com/jobs",
            "experience": "0-2 years",
            "skills": "python ai ml fastapi startup"
        }
    ]

    return jobs


# SOURCE 4
def fetch_cutshort():

    jobs = [
        {
            "source": "Cutshort",
            "company": "India Tech Hiring",
            "role": "Python Backend Developer",
            "location": "India",
            "posted_time": "0-24 hours ago",
            "job_link": "https://cutshort.io/jobs",
            "experience": "0-2 years",
            "skills": "python backend api sql fastapi"
        }
    ]

    return jobs


def fetch_demo_jobs():

    all_jobs = []

    all_jobs.extend(
        fetch_remoteok()
    )

    all_jobs.extend(
        fetch_remotive()
    )

    all_jobs.extend(
        fetch_wellfound()
    )

    all_jobs.extend(
        fetch_cutshort()
    )

    unique_jobs = []

    seen = set()

    for job in all_jobs:

        link = job["job_link"]

        if link not in seen:

            unique_jobs.append(
                job
            )

            seen.add(link)

    return unique_jobs[:100]