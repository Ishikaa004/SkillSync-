def generate_learning_roadmap(missing_skills):

    roadmap = []

    resources = {
        "Python": (
            "High",
            "Complete Python fundamentals and OOP."
        ),
        "SQL": (
            "High",
            "Practice SQL queries and joins."
        ),
        "MongoDB": (
            "High",
            "Build CRUD applications using MongoDB."
        ),
        "Linux": (
            "High",
            "Learn Linux commands and shell scripting."
        ),
        "Git": (
            "Medium",
            "Practice Git branching and version control."
        ),
        "GitHub": (
            "Medium",
            "Learn GitHub collaboration and pull requests."
        ),
        "Docker": (
            "Medium",
            "Containerize FastAPI applications."
        ),
        "AWS": (
            "Medium",
            "Deploy applications on AWS."
        ),
        "Machine Learning": (
            "High",
            "Study supervised and unsupervised learning."
        ),
        "Deep Learning": (
            "High",
            "Learn neural networks and backpropagation."
        ),
        "TensorFlow": (
            "High",
            "Complete TensorFlow beginner projects."
        ),
        "PyTorch": (
            "High",
            "Build deep learning models using PyTorch."
        ),
        "FastAPI": (
            "Medium",
            "Build REST APIs with FastAPI."
        ),
        "Scikit-learn": (
            "Medium",
            "Practice ML models using Scikit-Learn."
        ),
        "NumPy": (
            "Medium",
            "Learn numerical computing using NumPy."
        ),
        "Pandas": (
            "Medium",
            "Practice data analysis using Pandas."
        ),
        "Excel": (
            "Low",
            "Learn Excel formulas and pivot tables."
        )
    }

    for skill in missing_skills:

        if skill in resources:

            priority, resource = resources[skill]

        else:

            priority = "Medium"
            resource = f"Learn {skill} through projects."

        roadmap.append({
            "skill": skill,
            "priority": priority,
            "resource": resource
        })

    return roadmap

