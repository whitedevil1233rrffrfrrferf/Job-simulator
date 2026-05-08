from fastapi import HTTPException, APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session
from db.session import get_db
from services.resume import parse_and_store_resume
from schemas.resume import ResumeResponse, ResumeUploadRequest
from utils.file_parser import extract_text_from_pdf, extract_text_from_docx

router = APIRouter(prefix="/resume", tags=["resume"])

@router.post("/parse", response_model=ResumeResponse)
def parse_resume(request: ResumeUploadRequest, db: Session = Depends(get_db)):
    try:
        resume= parse_and_store_resume(request.resume_text, db=db)
        return resume
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 
    
@router.post("/upload")
def upload_resume(file:UploadFile=File(...), db: Session = Depends(get_db)):
    try:
        if file.filename.endswith('.pdf'):
            resume_text = extract_text_from_pdf(file)    
        elif file.filename.endswith('.docx'):
            resume_text = extract_text_from_docx(file)
        else:
            raise HTTPException(status_code=400, detail="Unsupported file type. Please upload a PDF or DOCX file.")
        return parse_and_store_resume(resume_text, db=db)        
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error processing file: " + str(e))        
    