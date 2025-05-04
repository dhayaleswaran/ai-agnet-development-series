from agno.agent import Agent
from fastapi import FastAPI
from agno.models.ollama import Ollama
from agno.tools.newspaper4k import Newspaper4kTools

agent = Agent(
    model=Ollama(id="mistral:latest"),
    name="Reporter",
    tools=[Newspaper4kTools()],
    show_tool_calls=True,
    description="You are a reporter. You can read the newspaper and summarize it.",
)


app = FastAPI()


@app.get("/summarize")
def summarize(query: str):
    if not query or not isinstance(query, str):
        return {"status": "error", "message": "Invalid query parameter. It must be a non-empty string."}
    
    try:
        response = agent.run(query)
        return {"status": "ok", "response": response.messages[-1].content}
    except Exception as e:
        return {"status": "error", "message": str(e)}
