from urllib.parse import quote


def create_gmail_compose_link(to_email, subject, body):
    to_email = str(to_email).strip()
    subject = quote(str(subject))
    body = quote(str(body))

    return (
        f"https://mail.google.com/mail/?view=cm"
        f"&fs=1&to={to_email}&su={subject}&body={body}"
    )