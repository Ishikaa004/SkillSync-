import re


def extract_email(text):

    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None

def extract_phone(text):

    pattern = r"\b\d{10}\b"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None

def extract_resume_details(text):

    details = {
        "email": extract_email(text),
        "phone": extract_phone(text)
    }

    return details