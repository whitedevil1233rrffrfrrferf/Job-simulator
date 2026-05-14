from fastapi import APIRouter, Depends
from schemas.resume_improvement import ResumeImprovementRequest

from services.resume_improvement import generate_resume_improvements

router = APIRouter(
    prefix="/resume-improvement",
    tags=["Resume Improvement"]
)

@router.post("/generate")
async def generate_improvements(request: ResumeImprovementRequest):
    return await generate_resume_improvements(request.resume_id, request.job_description)