from pydantic import BaseModel

class ChatRequest(BaseModel):
    resume_id: int
    question: str