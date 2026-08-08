from datetime import datetime, timedelta


def today_date():
    return datetime.now().strftime("%Y-%m-%d")


def followup_date(days=3):
    return (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d")


def generate_followup_message(company, role):
    return f"""
Hi,

I wanted to follow up on my application for the {role} role at {company}.

I am very interested in this opportunity and believe my project experience in Python, FastAPI, AI systems, data workflows, and production-style applications would allow me to contribute effectively.

I would be grateful if you could consider my application.

Best regards,
Harsh Roy
"""