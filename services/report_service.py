from pathlib import Path
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph
)
from reportlab.lib.styles import getSampleStyleSheet

BASE_DIR = Path(__file__).resolve().parent.parent.parent

REPORT_DIR = BASE_DIR / "reports"

REPORT_DIR.mkdir(
    parents=True,
    exist_ok=True
)


def generate_report(
    filename,
    ats_analysis,
    experience_analysis,
    education_analysis,
    project_analysis,
    certification_analysis,
    resume_improvements,
    learning_roadmap,
    ai_feedback
):

    report_path = REPORT_DIR / filename

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(str(report_path))

    story = []

    story.append(
        Paragraph("<b>SkillSync Resume Analysis Report</b>", styles["Title"])
    )

    story.append(
        Paragraph(
            f"<b>ATS Score:</b> {ats_analysis['ats_score']}%",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Matched Skills:</b> {', '.join(ats_analysis['matched_skills'])}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Missing Skills:</b> {', '.join(ats_analysis['missing_skills'])}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Experience Match:</b> {experience_analysis['match']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Degree Match:</b> {education_analysis['degree_match']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Branch Match:</b> {education_analysis['branch_match']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Total Projects:</b> {project_analysis['total_projects']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Total Certifications:</b> {certification_analysis['total_certifications']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph("<b>Resume Improvements</b>", styles["Heading2"])
    )

    for item in resume_improvements:

        story.append(
            Paragraph(f"• {item}", styles["BodyText"])
        )

    story.append(
        Paragraph("<b>Learning Roadmap</b>", styles["Heading2"])
    )

    for skill in learning_roadmap:

        story.append(
            Paragraph(
                f"{skill['skill']} ({skill['priority']}) - {skill['resource']}",
                styles["BodyText"]
            )
        )

    story.append(
        Paragraph("<b>AI Overall Review</b>", styles["Heading2"])
    )

    story.append(
        Paragraph(
            ai_feedback["overall_review"],
            styles["BodyText"]
        )
    )

    doc.build(story)

    return str(report_path)
if __name__ == "__main__":

    path = generate_report(
        "sample_report.pdf",
        {
            "ats_score": 80,
            "matched_skills": ["Python", "FastAPI"],
            "missing_skills": ["TensorFlow"]
        },
        {"match": True},
        {
            "degree_match": True,
            "branch_match": True
        },
        {"total_projects": 3},
        {"total_certifications": 2},
        [
            "Learn TensorFlow."
        ],
        [
            {
                "skill": "TensorFlow",
                "priority": "High",
                "resource": "Complete TensorFlow course."
            }
        ],
        {
            "overall_review": "Good resume."
        }
    )

    print(path)