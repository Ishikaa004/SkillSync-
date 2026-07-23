from pathlib import Path
import shutil

UPLOAD_DIR = Path("../data/resumes")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

def save_resume(file):
    file_path = UPLOAD_DIR / file.filename


    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return str(file_path)