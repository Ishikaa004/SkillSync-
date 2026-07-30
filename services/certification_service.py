import re


def extract_certifications(resume_text):

    certifications = []

    # Find the line containing "Certifications:"
    pattern = r'Certifications\s*:\s*(.*)'

    match = re.search(
        pattern,
        resume_text,
        re.IGNORECASE
    )

    if not match:
        return certifications

    cert_line = match.group(1)

    certifications = [
        cert.strip()
        for cert in cert_line.split(",")
        if cert.strip()
    ]

    return certifications

def analyze_certifications(certifications):

    total = len(certifications)

    if total >= 3:
        rating = "Excellent"
    elif total == 2:
        rating = "Good"
    elif total == 1:
        rating = "Average"
    else:
        rating = "Poor"

    return {
        "total_certifications": total,
        "certifications": certifications,
        "rating": rating
    }

