from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import json

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

prompt = ChatPromptTemplate.from_template("""
You are an expert ATS Resume Reviewer.

Analyze this resume.

Resume:
{resume}

ATS Score:
{score}

Matched Skills:
{matched}

Missing Skills:
{missing}

Job Description:
{job_description}

Return ONLY valid JSON.

Do not write Markdown.

Do not use ```.

Return exactly this format:

{{
    "overall_review": "",
    "ats_compatibility": "",
    "strengths": [],
    "weaknesses": [],
    "missing_skills_analysis": "",
    "project_feedback": "",
    "experience_feedback": "",
    "resume_improvement": [],
    "career_advice": "",
    "learning_roadmap": []
}}
""")


def get_ai_feedback(
    resume,
    score,
    matched,
    missing,
    job_description
):

    chain = prompt | llm

    response = chain.invoke({
        "resume": resume,
        "score": score,
        "matched": matched,
        "missing": missing,
        "job_description": job_description
    })

    try:
        feedback = json.loads(response.content)
    except json.JSONDecodeError:
        feedback = {
            "error": "AI returned invalid JSON.",
            "raw_response": response.content
        }

    return feedback