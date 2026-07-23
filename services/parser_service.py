import fitz
from docx import Document
from pathlib import Path


def extract_text_from_pdf(file_path):

    doc = fitz.open(file_path)

    text = ""

    for page in doc:
        text += page.get_text()

    doc.close()

    return text


def extract_text_from_docx(file_path):

    doc = Document(file_path)

    text = ""

    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"

    return text


def extract_resume_text(file_path):

    file_path = Path(file_path)

    if file_path.suffix.lower() == ".pdf":
        return extract_text_from_pdf(file_path)

    elif file_path.suffix.lower() == ".docx":
        return extract_text_from_docx(file_path)

    else:
        raise ValueError("Unsupported file format.")