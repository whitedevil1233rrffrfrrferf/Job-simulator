from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from services.job_match import match_resume_to_job
router = APIRouter(prefix="/match", tags=["match"])

@router.post("/")
def match_job(resume_id: int, job_description: str, db: Session = Depends(get_db)):

    return match_resume_to_job(
        resume_id=resume_id,
        job_description=job_description,
        db=db
    )