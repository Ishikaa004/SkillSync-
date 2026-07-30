import re
from datetime import datetime

MONTHS = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12
}


def extract_required_experience(job_description):

    pattern = r'(\d+)\+?\s*(?:years|year|yrs|yr)'

    match = re.search(
        pattern,
        job_description,
        re.IGNORECASE
    )

    if match:
        return int(match.group(1))

    return 0


def extract_date_ranges(resume_text):

    pattern = (
        r'([A-Z][a-z]{2})\s+(\d{4})\s*[–-]\s*'
        r'(?:(Present)|([A-Z][a-z]{2})\s+(\d{4}))'
    )

    return re.findall(pattern, resume_text)


def extract_candidate_experience(resume_text):

    matches = extract_date_ranges(resume_text)

    if not matches:
        return 0

    total_months = 0

    for start_month, start_year, present, end_month, end_year in matches:

        start = datetime(
            int(start_year),
            MONTHS[start_month],
            1
        )

        if present == "Present":

            end = datetime.today()

        else:

            end = datetime(
                int(end_year),
                MONTHS[end_month],
                1
            )

        months = (
            (end.year - start.year) * 12
            + (end.month - start.month)
        )

        total_months += max(months, 0)

    experience_years = round(total_months / 12, 2)

    return experience_years


def compare_experience(
    required_experience,
    candidate_experience
):

    return {
        "required": required_experience,
        "candidate": candidate_experience,
        "match": candidate_experience >= required_experience
    }


