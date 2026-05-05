from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI Job Automation API is running"}