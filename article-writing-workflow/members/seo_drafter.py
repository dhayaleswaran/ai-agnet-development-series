from agno.agent import Agent
from agno.models.ollama import Ollama
from textwrap import dedent


def seo_drafter():
    """
    Drafts the given content and improves its SEO.
    """
    agnet = Agent(
        name="SEODrafterAgent",
        model=Ollama(id="mistral:latest"),
        goal="Draft the content and improve its SEO.",
        description="You are an SEO-AI specialized in optimizing the draft article content for search engines.",
        instructions=(
            """ 
            Get the drafted content from ContentEnhancerAgent and follow these instructions:
            1. Keyword Optimization:
                - Enhance the content by incorporating relevant keywords and phrases.
                - The enhancement should be natural and not forced.
                - Ensure that the keywords are relevant to the content and its target audience.
                - This enhancemrent should be done in a way that it does not change the meaning of the content.

            2. SEO Best Practices:
                - Ensure that the content follows SEO best practices.
                - Use proper headings (H1, H2, H3) to structure the content.
                - Include internal and external links where appropriate.
                - Optimize images with alt text and descriptive filenames.
                - Ensure that the content is mobile-friendly and loads quickly.
                - Choose to go with bullets or paragraphs based on the content.
            """
        ),
    )

    return agnet
