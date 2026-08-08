from pathlib import Path
from playwright.sync_api import sync_playwright
from src.profile import APPLICANT_PROFILE


def safe_fill(page, selectors, value):
    for selector in selectors:
        try:
            field = page.locator(selector)

            if field.count() > 0:
                field.first.fill(value)
                return True

        except Exception:
            continue

    return False


def auto_apply(job_url, resume_file):
    """
    Opens a job page, fills common application fields,
    and uploads the recommended resume if upload field exists.
    """

    resume_path = Path("resumes") / resume_file

    if not resume_path.exists():
        return f"Resume file not found: {resume_path}"

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        try:
            page.goto(
                job_url,
                timeout=60000
            )

            page.wait_for_timeout(3000)

            filled_fields = []

            if safe_fill(
                page,
                [
                    "input[name='name']",
                    "input[name='full_name']",
                    "input[name='fullname']",
                    "input[placeholder*='Name']",
                    "input[placeholder*='name']"
                ],
                APPLICANT_PROFILE["full_name"]
            ):
                filled_fields.append("Name")

            if safe_fill(
                page,
                [
                    "input[name='first_name']",
                    "input[name='firstname']",
                    "input[placeholder*='First']"
                ],
                APPLICANT_PROFILE["first_name"]
            ):
                filled_fields.append("First Name")

            if safe_fill(
                page,
                [
                    "input[name='last_name']",
                    "input[name='lastname']",
                    "input[placeholder*='Last']"
                ],
                APPLICANT_PROFILE["last_name"]
            ):
                filled_fields.append("Last Name")

            if safe_fill(
                page,
                [
                    "input[type='email']",
                    "input[name='email']",
                    "input[placeholder*='Email']",
                    "input[placeholder*='email']"
                ],
                APPLICANT_PROFILE["email"]
            ):
                filled_fields.append("Email")

            if APPLICANT_PROFILE["phone"]:
                if safe_fill(
                    page,
                    [
                        "input[type='tel']",
                        "input[name='phone']",
                        "input[name='mobile']",
                        "input[placeholder*='Phone']",
                        "input[placeholder*='Mobile']"
                    ],
                    APPLICANT_PROFILE["phone"]
                ):
                    filled_fields.append("Phone")

            if safe_fill(
                page,
                [
                    "input[name='location']",
                    "input[placeholder*='Location']",
                    "input[placeholder*='location']"
                ],
                APPLICANT_PROFILE["location"]
            ):
                filled_fields.append("Location")

            if APPLICANT_PROFILE["linkedin"]:
                if safe_fill(
                    page,
                    [
                        "input[name='linkedin']",
                        "input[placeholder*='LinkedIn']",
                        "input[placeholder*='linkedin']"
                    ],
                    APPLICANT_PROFILE["linkedin"]
                ):
                    filled_fields.append("LinkedIn")

            if safe_fill(
                page,
                [
                    "input[name='github']",
                    "input[placeholder*='GitHub']",
                    "input[placeholder*='github']"
                ],
                APPLICANT_PROFILE["github"]
            ):
                filled_fields.append("GitHub")

            if APPLICANT_PROFILE["portfolio"]:
                if safe_fill(
                    page,
                    [
                        "input[name='portfolio']",
                        "input[name='website']",
                        "input[placeholder*='Portfolio']",
                        "input[placeholder*='Website']"
                    ],
                    APPLICANT_PROFILE["portfolio"]
                ):
                    filled_fields.append("Portfolio")

            uploaded = False

            file_inputs = page.locator(
                "input[type='file']"
            )

            if file_inputs.count() > 0:
                file_inputs.first.set_input_files(
                    str(resume_path)
                )
                uploaded = True

            filled_text = ", ".join(filled_fields) if filled_fields else "No common fields detected"

            if uploaded:
                return f"Form filled: {filled_text}. Resume uploaded: {resume_file}. Review before submitting."

            return f"Form filled: {filled_text}. No resume upload field found. Review before submitting."

        except Exception as e:
            return f"Auto apply error: {str(e)}"

        finally:
            # Browser closes after execution. Later we can keep it open for manual review.
            browser.close()