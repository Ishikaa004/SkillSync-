from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

prompt = ChatPromptTemplate.from_template("""
You are an expert ATS Resume Reviewer and Career Coach.

Below is the candidate's complete resume.

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

Analyze the resume and provide:

# Overall Resume Review

# ATS Compatibility

# Strengths

# Weaknesses

# Missing Skills

# Project Feedback

# Experience Feedback

# Resume Improvement Suggestions

# Career Advice

# Learning Roadmap

Be professional.
Be specific.
Keep each section concise.
""")


def get_ai_feedback(resume,score,matched,missing,job_description):

    chain = prompt | llm

    response = chain.invoke({
        "resume": resume,
        "score": score,
        "matched": matched,
        "missing": missing,
        "job_description": job_description
    })

    return response.content