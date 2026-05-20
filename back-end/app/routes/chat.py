from fastapi import APIRouter, Depends
from schemas.chat import ChatRequest
from services.chat import ask_chat_question


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@router.post("/ask")
async def ask_question(request: ChatRequest):
    return await ask_chat_question(
        request.resume_id,
        request.question
    )