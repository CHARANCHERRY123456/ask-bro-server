from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.features.ai_agent.llm_chain import generate_sql_and_answer

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(request: QuestionRequest):
    result = await generate_sql_and_answer(request.question)
    return result

