import json

from sqlalchemy.orm import Session
from models.resume import Resume
from chains.job_match_chain import job_match_chain
from services.FAISS import get_resume_context

def match_resume_to_job(resume_id: int, job_description: str, db: Session):
    resume = db.query(Resume).filter(Resume.id == resume_id).first()
    if not resume:
        raise ValueError(f"Resume with ID {resume_id} not found.")
    # STEP 1: RAG retrieval using job description
    resume_context = get_resume_context(resume_id, job_description)
    print("\n===== RESUME CONTEXT RETRIEVED =====")
    print(resume_context)
     # STEP 2: LLM analysis
    result = job_match_chain.invoke({
        "resume_context": resume_context,
        "job_description": job_description
    })
    return result