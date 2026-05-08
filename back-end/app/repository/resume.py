import json
from sqlalchemy.orm import Session
from models.resume import Resume

def createresume(db:Session, structured_data: dict, raw_text: str):
    resume=Resume(
        raw_text=raw_text,
        structured_data=json.dumps(structured_data)
    )
    db.add(resume)
    db.commit()
    db.refresh(resume)
    return resume

   