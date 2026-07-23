from fastapi import APIRouter,UploadFile, File,HTTPException
from services.upload_service import save_resume
from services.parser_service import extract_resume_text

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

    return {
        "message": "Resume uploaded successfully.",
        "file_path": file_path,
        "resume_text": resume_text
    }
    