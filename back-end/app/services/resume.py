import json
from sqlalchemy.orm import Session
from chains.resume_chain import resume_chain
from repository.resume import createresume


def parse_and_store_resume(resume_text: str, db: Session):

    parsed_data = resume_chain.invoke({
        "resume_text": resume_text
    })

    resume = createresume(
        db=db,
        structured_data=parsed_data,
        raw_text=resume_text
    )

    data = parsed_data
    if isinstance(data, str):
        data = json.loads(data)

    return {
        "id": resume.id,
        "raw_text": resume.raw_text,
        "structured_data": parsed_data
    }