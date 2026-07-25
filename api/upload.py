from fastapi import APIRouter,UploadFile, File,HTTPException
from services.upload_service import save_resume
from services.parser_service import extract_resume_text
from services.extractor_service import extract_resume_details
from services.ats_service import analyze_resume
from services.llm_service import get_ai_feedback
from services.llm_service import get_ai_feedback
from services.ats_service import read_job_description

router= APIRouter(
     prefix="/api/v1/upload",
     tags=["Upload"]
)
ALLOWED_TYPES = [
    "application/pdf",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
]

@router.get("/upload")
def upload():
    return {
        "message":"Upload API is working!"
    }

@router.post("/resume")
async def upload_resume(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are allowed."
        )

    file_path = save_resume(file)

    resume_text = extract_resume_text(file_path)

    details = extract_resume_details(resume_text)

    ats_analysis = analyze_resume(details["skills"])

    job_description = read_job_description()

    ai_feedback = get_ai_feedback(
    resume_text,
    ats_analysis["ats_score"],
    ats_analysis["matched_skills"],
    ats_analysis["missing_skills"],
    job_description
     )


    return {
        "message": "Resume uploaded successfully.",
        "file_path": file_path,
        "resume_text": resume_text,
        "details": details,
        "ats_analysis": ats_analysis,
        "ai_feedback": ai_feedback
    }
    