from agno.agent import Agent
from agno.models.ollama import Ollama
from textwrap import dedent


def writer(title_and_meta: str, content: str):
    agent = Agent(
        name="WriterAgent",
        description="Generates well-structured articles using the provided title, content, and meta description.",
        goal="Create a medium-ready article in markdown format, integrating the title, content, and meta description.",
        model=Ollama(id="mistral:latest"),
        instructions=dedent(
            """
            You are a writer agent. Your tasks:
            - Compose an article using the supplied title and content.
            - Format the article using standard markdown.
            - Ensure clear structure with appropriate headings and subheadings.
            - Insert the meta description at the beginning.
            - Preserve any placeholders in the format <>.
            - Do not alter or optimize the content; focus on improving structure and readability.
            - Remove unrelated headings and subheadings.
            - Ensure the article is ready for publication on Medium.
            """
        ),
    )

    return agent.run(f"Title and Meta: {title_and_meta}\n\nContent: {content}")
