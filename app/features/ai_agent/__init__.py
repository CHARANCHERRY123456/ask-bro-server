from fastapi import APIRouter
from app.features.ai_agent.llm_chain import query_to_sql_llm

router = APIRouter()

@router.get("/test")
def test_llm(query: str = "Hello, AI!"):
    result = query_to_sql_llm(query)
    return {"result": result}