from vertexai.preview.generative_models import GenerativeModel
from app.features.ai_agent.tools import get_info_from_data, generate_plotly_chart
import os
import httpx
import asyncio
from sqlalchemy import text
from app.db.session import SessionLocal
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + GEMINI_API_KEY

model = GenerativeModel("gemini-1.5-pro")

def query_to_sql_llm(user_input: str) -> str:
    response = model.generate_content(
        user_input,
        generation_config={
            "temperature": 0.8,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 1024
        },
        tools=[get_info_from_data, generate_plotly_chart],
        system_instruction=[
            {
                "role": "system",
                "parts": [{"text": "Respond concisely and playfully in JSON format."}]
            }
        ]
    )
    return response.text

async def generate_sql_and_answer(question: str):
    # 1. Use Gemini to generate SQL
    prompt = f"""
You are an AI that generates SQL queries for a PostgreSQL database. Given a user question, write only the SQL query to answer it. Do not explain, just output the SQL.
Question: {question}
"""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            GEMINI_API_URL,
            json={
                "contents": [{"parts": [{"text": prompt}]}]
            },
            timeout=30
        )
        response.raise_for_status()
        sql = response.json()["candidates"][0]["content"]["parts"][0]["text"].strip()

    # 2. Run SQL on DB
    db = SessionLocal()
    try:
        result = db.execute(text(sql))
        rows = result.fetchall()
        columns = result.keys()
        answer = [dict(zip(columns, row)) for row in rows]
    except Exception as e:
        answer = {"error": str(e), "sql": sql}
    finally:
        db.close()
    return {"sql": sql, "answer": answer}
