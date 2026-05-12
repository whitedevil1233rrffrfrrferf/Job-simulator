import json
import asyncio
from sqlalchemy.orm import Session
from models.resume import Resume
from chains.job_match_chain import job_match_chain
from services.FAISS import get_resume_context
from core.ws_manager import manager

async def match_resume_to_job(resume_id: int, job_description: str, db: Session):

    await manager.send(resume_id, {
        "step": "validating_resume"
    })

    resume = db.query(Resume).filter(Resume.id == resume_id).first()
    if not resume:
        raise ValueError("Resume not found")

    await manager.send(resume_id, {
        "step": "retrieving_context"
    })

    # 🔥 FIX 1: move FAISS to thread
    resume_context = await asyncio.to_thread(
        get_resume_context,
        resume_id,
        job_description
    )

    await manager.send(resume_id, {
        "step": "running_llm"
    })

    # 🔥 FIX 2: move LLM to thread (VERY IMPORTANT)
    result = await asyncio.to_thread(
        job_match_chain.invoke,
        {
            "resume_context": resume_context,
            "job_description": job_description
        }
    )

    await manager.send(resume_id, {
        "step": "completed",
        "result": result
    })

    return result