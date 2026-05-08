from dotenv import load_dotenv
import os
load_dotenv()

database_url = os.getenv("DATABASE_URL")

LLM_PROVIDER = os.getenv("LLM_PROVIDER")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL")