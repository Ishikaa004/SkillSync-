import re
from pathlib import Path

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
        "phone": extract_phone(text),
        "skills": extract_skills(text)
    }

    return details

def load_skills():

    skills_file = Path("../data/skills.txt")

    with open(skills_file, "r") as file:
        skills = file.read().splitlines()

    return skills

def extract_skills(text):

    skills = load_skills()

    found_skills = []

    text = text.lower()

    for skill in skills:

        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills
