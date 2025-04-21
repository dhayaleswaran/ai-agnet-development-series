from os import getenv
from agno.memory.v2 import Memory
from agno.memory.db.postgres import PgMemoryDb
from agno.memory.v2.memory import Memory
from dotenv import load_dotenv
from agno.models.ollama import Ollama
from agno.agent import Agent, RunResponse
from fastapi import FastAPI, Request
from typing import Iterator
from fastapi.responses import StreamingResponse
from generate_stream import generate_stream


load_dotenv()

postgres_url = getenv("PGVECTOR_URL", "")

if postgres_url == "":
    raise ValueError("POSTGRES_URL environment variable is not set.")


db = PgMemoryDb(db_url=postgres_url, table_name="memory", schema="public")
memory = Memory(db=db, model=Ollama(id="mistral:latest"))

agent = Agent(
    model=Ollama(id="mistral:latest"),
    memory=memory,
    name="Agentic Memory",
    enable_agentic_memory=True,
    description="You are an agent with memory. You can remember things and recall them later.",
)


app = FastAPI()


@app.get("/health_check")
def health_check():
    result = agent.run("How are you?")
    return {"status": "ok", "response": result.messages[-1].content}


@app.get("/memory")
async def get_memory(name: str):
    memories = memory.get_user_memories(user_id=name)
    return {"memories": memories}


@app.post("/talk")
async def talk(request: Request):
    obj = await request.json()
    memory.create_user_memories(user_id=obj["user"], message=obj["prompt"])

    return StreamingResponse(
        generate_stream(obj["user"], obj["prompt"], agent),
        media_type="text/plain",
    )
