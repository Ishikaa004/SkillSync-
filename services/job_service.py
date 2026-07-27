from pathlib import Path
import shutil
from services.parser_service import extract_resume_text

BASE_DIR = Path(__file__).resolve().parent.parent.parent

JD_DIR = BASE_DIR / "data" / "job_descriptions"

JD_DIR.mkdir(parents=True, exist_ok=True)


def save_job_description(file):

    file_path = JD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return str(file_path)



def read_job_description(file_path):

    return extract_resume_text(file_path)

