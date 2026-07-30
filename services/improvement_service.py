def generate_resume_improvements(
    ats_analysis,
    experience_analysis,
    education_analysis,
    project_analysis,
    certification_analysis
):

    suggestions = []

    # ATS Suggestions
    if ats_analysis["missing_skills"]:

        for skill in ats_analysis["missing_skills"]:
            suggestions.append(
                f"Learn {skill} and add it to your resume."
            )

    # Experience
    if not experience_analysis["match"]:
        suggestions.append(
            "Gain more relevant work experience through internships or projects."
        )

    # Degree
    if not education_analysis["degree_match"]:
        suggestions.append(
            "Ensure your degree matches the job requirements."
        )

    # Branch
    if not education_analysis["branch_match"]:
        suggestions.append(
            "Highlight relevant Computer Science subjects and projects."
        )

    # Projects
    if project_analysis["total_projects"] < 3:
        suggestions.append(
            "Add more real-world projects to strengthen your portfolio."
        )

    # Certifications
    if certification_analysis["total_certifications"] < 3:
        suggestions.append(
            "Earn more industry-recognized certifications."
        )

    # Resume Quality
    if ats_analysis["ats_score"] >= 90:
        suggestions.append(
            "Excellent resume. Focus on interview preparation."
        )

    elif ats_analysis["ats_score"] >= 75:
        suggestions.append(
            "Good resume. Minor improvements can further increase your ATS score."
        )

    else:
        suggestions.append(
            "Improve missing skills and optimize your resume for ATS."
        )

    return suggestions

