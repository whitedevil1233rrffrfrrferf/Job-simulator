from fastapi import APIRouter

from schemas.cover_letter import CoverLetterRequest

from services.cover_letter import generate_cover_letter

router = APIRouter( 
    prefix="/cover-letter",
    tags=["Cover Letter"]
    )

@router.post("/generate")
async def generate(
    request: CoverLetterRequest
):
    return await generate_cover_letter(
        request.resume_id,
        request.job_description 
    )
