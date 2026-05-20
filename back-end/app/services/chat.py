import asyncio
from services.FAISS import get_resume_context
from chains.chat_chain import chat_chain


async def ask_chat_question(
        resume_id: int,
        question: str
):
    # Step 1: get resume content

    resume_context= await asyncio.to_thread(
        get_resume_context, 
        resume_id, 
        question
    )    

    # Step 2: LLM invocation

    result = await asyncio.to_thread(
        chat_chain.invoke,

        {
            "resume_context": resume_context,

            "question": question
        },

        config={
            "configurable": {
                "session_id": str(resume_id)
            }
        }
    )
    
    return {
        "answer": result.content
    }
    