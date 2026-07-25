from pathlib import Path
from services.extractor_service import extract_skills


BASE_DIR = Path(__file__).resolve().parent.parent.parent


def read_job_description():

    jd_file = BASE_DIR / "data" / "job_description.txt"

    with open(jd_file, "r") as file:
        job_description = file.read()

    return job_description


def get_job_skills():

    job_description = read_job_description()

    skills = extract_skills(job_description)

    return skills

def compare_skills(resume_skills, job_skills):

    matched_skills = []
    missing_skills = []

    for skill in job_skills:

        if skill in resume_skills:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    return matched_skills, missing_skills

def calculate_ats_score(matched_skills, job_skills):

    if len(job_skills) == 0:
        return 0

    score = (len(matched_skills) / len(job_skills)) * 100

    return round(score, 2)

def analyze_resume(resume_skills):

    job_skills = get_job_skills()

    matched_skills, missing_skills = compare_skills(
        resume_skills,
        job_skills
    )

    ats_score = calculate_ats_score(
        matched_skills,
        job_skills
    )

    strengths = get_strengths(
        matched_skills
    )

    recommendations = get_recommendations(
        missing_skills
    )

    summary = generate_summary(
        ats_score,
        matched_skills,
        missing_skills
    )
    return {
        "ats_score": ats_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "strengths": strengths,
        "recommendations": recommendations,
        "summary": summary
    }

def get_strengths(matched_skills):

    strengths = []

    for skill in matched_skills:
        strengths.append(f"Good knowledge of {skill}")

    return strengths

def get_recommendations(missing_skills):

    recommendations = []

    skill_tips = {
        "Python": "Practice Python programming.",
        "Java": "Improve Java programming skills.",
        "C++": "Strengthen C++ problem-solving skills.",
        "SQL": "Practice SQL for database management.",
        "PostgreSQL": "Learn PostgreSQL database concepts.",
        "FastAPI": "Build REST APIs using FastAPI.",
        "Git": "Practice version control using Git.",
        "GitHub": "Learn GitHub collaboration and workflows.",
        "Docker": "Improve your Docker skills for containerization.",
        "AWS": "Learn AWS for cloud deployment.",
        "Machine Learning": "Study Machine Learning algorithms.",
        "NumPy": "Practice numerical computing with NumPy.",
        "Pandas": "Learn data analysis using Pandas.",
        "Scikit-learn": "Build ML models using Scikit-learn."
    }

    for skill in missing_skills:

        if skill in skill_tips:
            recommendations.append(skill_tips[skill])
        else:
            recommendations.append(f"Learn {skill}")

    return recommendations

def generate_summary(ats_score, matched_skills, missing_skills):

    summary = (
        f"Your resume matches {ats_score}% of the job requirements. "
        f"You matched {len(matched_skills)} skills "
        f"and are missing {len(missing_skills)} skills."
    )

    return summary