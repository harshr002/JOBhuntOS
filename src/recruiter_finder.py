from urllib.parse import urlparse


COMMON_RECRUITER_PATTERNS = [
    "careers@{domain}",
    "hr@{domain}",
    "jobs@{domain}",
    "recruitment@{domain}",
    "talent@{domain}",
    "hiring@{domain}"
]


def extract_domain(job_url):

    try:

        parsed = urlparse(
            job_url
        )

        domain = parsed.netloc

        domain = domain.replace(
            "www.",
            ""
        )

        if domain:
            return domain

        return None

    except:

        return None


def generate_recruiter_emails(job_url):

    domain = extract_domain(
        job_url
    )

    if not domain:

        return []

    emails = []

    for pattern in COMMON_RECRUITER_PATTERNS:

        email = pattern.format(
            domain=domain
        )

        emails.append(
            email
        )

    return emails