SKILL_WEIGHTS = {

    "Python": 5,
    "Machine Learning": 5,
    "Deep Learning": 5,

    "FastAPI": 4,
    "SQL": 4,
    "PostgreSQL": 4,
    "Scikit-learn": 4,

    "Docker": 3,
    "AWS": 3,
    "NumPy": 3,
    "Pandas": 3,
    "MongoDB": 3,

    "Git": 2,
    "GitHub": 2,
    "Linux": 2,
    "TensorFlow": 2,
    "PyTorch": 2,

    "HTML": 1,
    "CSS": 1,
    "JavaScript": 1,
    "Excel": 1
}

def get_skill_weight(skill):

    return SKILL_WEIGHTS.get(skill, 1)


def calculate_weighted_score(
    matched_skills,
    job_skills
):

    total_weight = 0
    matched_weight = 0

    for skill in job_skills:
        total_weight += get_skill_weight(skill)

    for skill in matched_skills:
        matched_weight += get_skill_weight(skill)

    if total_weight == 0:
        return 0

    score = (matched_weight / total_weight) * 100

    return round(score, 2)