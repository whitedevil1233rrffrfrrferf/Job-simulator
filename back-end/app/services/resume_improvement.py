import asyncio
from services.FAISS import get_resume_context
import json
from chains.resume_improvement_chain import resume_improvement_chain

from core.ws_manager import manager

async def generate_resume_improvements(resume_id: int, job_description: str):

    # Step 1: Get resume context from FAISS
    # STEP 1

    await manager.send(
        resume_id,
        {
            "step": "retrieving_resume_context"
        }
    )

    resume_context = await asyncio.to_thread(get_resume_context, resume_id, job_description)
    print("Resume Context Retrieved:", resume_context)
    # Step 2: LLM Generation
    
    try:
        await manager.send(
            resume_id,
            {
                "step": "running_llm"
            }
        )
        result = await asyncio.to_thread(
            resume_improvement_chain.invoke,
            {
                "resume_context": resume_context,
                "job_description": job_description
            }
        )
    except Exception as e:
        print("Chain error:", e) 
        raise
    await manager.send(
        resume_id,
        {
            "step": "completed",
            "result": result
        }
    )
    
    return result
