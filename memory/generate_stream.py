from agno.agent import Agent, RunResponse
from typing import Iterator


def generator(result: Iterator[RunResponse]):
    for chunk in result:
        yield f"{chunk.content}"


def generate_stream(user: str, prompt: str, agent: Agent):
    result: Iterator[RunResponse] = agent.run(user_id=user, message=prompt, stream=True)
    return generator(result)
