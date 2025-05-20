from agno.agent import Agent
from agno.models.ollama import Ollama


def meta_drafter():
    """
    Generates titles and meta descriptions for the given content.
    """
    agent = Agent(
        name="MetaDrafterAgent",
        model=Ollama(id="mistral:latest"),
        goal="Generate a catchy title and meta description for the content.",
        description="Generates titles and meta descriptions for the given content.",
        instructions=(
            "You are a meta drafter agent. Your roles and responsibilities are as follows:\n"
            "- Generate a catchy title for the given content that accurately reflects its main theme.\n"
            "- Create a concise and engaging meta description that summarizes the content and encourages clicks.\n"
            "- Ensure the title and meta description are relevant to the target audience and optimized for search engines.\n"
            "- Maintain a clear and concise writing style, avoiding jargon or overly complex language.\n"
            "- Provide only the title and meta description as output, without additional commentary or explanation.\n"
            "- If the content contains placeholders in the format <>, do not modify or remove them; treat them as immutable placeholders.\n"
        ),
    )

    return agent
