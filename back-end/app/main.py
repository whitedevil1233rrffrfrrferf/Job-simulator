from fastapi import FastAPI
import uvicorn
from db.session import Base, engine
from models.resume import Resume
from routes.resume import router as resume_router

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(resume_router)

@app.get("/")
def root():
    return {"message": "AI Job Automation API is running"}

if __name__ == "__main__":
    
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)