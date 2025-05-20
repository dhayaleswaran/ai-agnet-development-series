from agno.agent import Agent
from agno.models.ollama import Ollama
from textwrap import dedent


def content_enhancer():
    """
    Enhances the given content by checking its grammar, spelling, style
    and readability.
    """

    agent = Agent(
        name="ContentEnhancerAgent",
        model=Ollama(id="mistral:latest"),
        description="Enhances content for grammar, spelling, style, and readability.",
        goal="Enhance the content by checking its grammar, spelling, style, and readability.",
        instructions=dedent(
            """
            You are a content enhancer agent.

            Your job is to take a **poorly written article** and improve it completely while preserving the original meaning.

            **Your tasks:**

            1. **Spelling and Grammar:**
               - Fix all grammar, punctuation, and spelling mistakes.
               - Use correct sentence structures and consistent tenses.
               - Do NOT change the meaning or context.
               - Do NOT change the tone and perspective of the article.

            2. **Style and Readability:**
               - Break long paragraphs into smaller ones.
               - Use Medium-friendly Markdown formatting:
                 - Headings (`##`, `###`)
                 - Bullet points or numbered lists
                 - Bold or italics where appropriate
               - Keep tone consistent and easy to read.
               - Do NOT modify or remove `<placeholders>`; keep them in a single line if found.

            3. **Summary Section:**
               - At the end of the article, add a `## Summary` section.
               - Use bullet points to highlight the key takeaways.

            4. **Thanks for Reading:**
               - Add a `## Thanks for Reading` section.
               - Write a friendly note thanking the reader and inviting feedback.

            **Output only the enhanced article. No comments, no extra explanations.**
            """
        ),
    )

    return agent
