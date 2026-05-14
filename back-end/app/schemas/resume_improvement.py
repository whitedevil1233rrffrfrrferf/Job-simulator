from pydantic import BaseModel

class ResumeImprovementRequest(BaseModel):
    resume_id: int
    job_description: str