import os
import requests
from dotenv import load_dotenv

load_dotenv()


def find_direct_apply_jobs(user_prompt, limit=40):
    app_id = os.getenv("ADZUNA_APP_ID")
    app_key = os.getenv("ADZUNA_APP_KEY")

    if not app_id or not app_key:
        return [{
            "source": "DEBUG",
            "company": "Missing API Key",
            "role": "ADZUNA_APP_ID or ADZUNA_APP_KEY not found in .env",
            "location": "Local Setup Issue",
            "posted_time": "Now",
            "job_link": "https://developer.adzuna.com/",
            "experience": "Fix .env",
            "skills": "Your .env file is not loading correctly."
        }]

    url = "https://api.adzuna.com/v1/api/jobs/in/search/1"

    params = {
        "app_id": app_id,
        "app_key": app_key,
        "what": user_prompt,
        "results_per_page": limit,
        "content-type": "application/json",
        "sort_by": "date"
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=30
        )

        print("ADZUNA STATUS:", response.status_code)
        print("ADZUNA RESPONSE:", response.text[:1000])

        if response.status_code != 200:
            return [{
                "source": "DEBUG",
                "company": "Adzuna API Error",
                "role": f"Status Code: {response.status_code}",
                "location": "API Issue",
                "posted_time": "Now",
                "job_link": "https://developer.adzuna.com/",
                "experience": "Check API key",
                "skills": response.text[:500]
            }]

        data = response.json()
        results = data.get("results", [])

        if not results:
            return [{
                "source": "DEBUG",
                "company": "No Results Found",
                "role": f"No jobs found for: {user_prompt}",
                "location": "Try broader prompt",
                "posted_time": "Now",
                "job_link": "https://www.adzuna.in/search",
                "experience": "Try different keyword",
                "skills": "Try: data analyst, python developer, cloud engineer, business analyst"
            }]

        jobs = []

        for item in results:
            company = item.get("company", {}).get("display_name", "Unknown Company")
            role = item.get("title", "Unknown Role")
            location = item.get("location", {}).get("display_name", "India")
            link = item.get("redirect_url", "")
            description = item.get("description", "")
            created = item.get("created", "Check JD")

            jobs.append({
                "source": "Adzuna",
                "company": company,
                "role": role,
                "location": location,
                "posted_time": created,
                "job_link": link,
                "experience": "Check JD",
                "skills": description
            })

        return jobs

    except Exception as e:
        return [{
            "source": "DEBUG",
            "company": "Python Error",
            "role": str(e),
            "location": "Code Error",
            "posted_time": "Now",
            "job_link": "https://developer.adzuna.com/",
            "experience": "Debug needed",
            "skills": str(e)
        }]