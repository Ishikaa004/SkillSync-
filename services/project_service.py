import re
from pathlib import Path


def extract_projects(resume_text):

    projects = []

    pattern = r'^\s*PROJECTS\s*$([\s\S]*?)(?=^\s*ACHIEVEMENTS|^\s*CERTIFICATIONS|\Z)'

    match = re.search(
        pattern,
        resume_text,
        re.MULTILINE | re.IGNORECASE
    )

    if not match:
        return projects

    project_section = match.group(1)

    lines = project_section.split("\n")

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if line == "PROJECTS":
            continue

        if line.startswith("•"):
            continue

        if len(line) < 4:
            continue

        # Skip technology stack lines
        if any(
            tech in line
            for tech in [
                "Python",
                "FastAPI",
                "Scikit-Learn",
                "NumPy",
                "Pandas",
                "LLM",
                "RAG",
                "REST APIs",
                "JavaScript",
                "HTML",
                "CSS",
                "Generative AI",
                "Full-Stack"
            ]
        ):
            continue

        # Skip description sentences
        if (
            line.startswith("Built")
            or line.startswith("Developed")
            or line.startswith("Engineered")
            or line.startswith("Executed")
            or line.startswith("Integrated")
            or line.startswith("Architected")
            or line.startswith("Implemented")
            or line.startswith("Designed")
        ):
            continue

        projects.append(line)

    return projects


def analyze_projects(projects):

    total_projects = len(projects)

    if total_projects >= 3:
        rating = "Excellent"
    elif total_projects == 2:
        rating = "Good"
    elif total_projects == 1:
        rating = "Average"
    else:
        rating = "Poor"

    return {
        "total_projects": total_projects,
        "projects": projects,
        "rating": rating
    }
