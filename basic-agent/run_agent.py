from agno.playground import Playground, serve_playground_app
from agno.agent import Agent
from agno.models.ollama import Ollama


basic_agent = Agent(
    name="Basic Agent",
    model=Ollama(id="mistral:latest"),
    description="You are a basic agent. Help on resolving general queries.",
)

app = Playground(agents=[basic_agent]).get_app()


@app.get("/health_check")
def health_check():
    result = basic_agent.run("How are you?")
    return {"status": "ok", "response": result.messages[-1].content}


if __name__ == "__main__":
    serve_playground_app("run_agent:app", reload=True)
