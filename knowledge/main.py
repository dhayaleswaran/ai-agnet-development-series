from pathlib import Path
from helpers.get_document_data import get_document_data
from agno.agent import Agent
from dotenv import load_dotenv
from os import getenv
from agno.vectordb.pgvector import PgVector, SearchType
from agno.embedder.ollama import OllamaEmbedder
from agno.document.base import Document
from agno.knowledge.document import DocumentKnowledgeBase
from agno.playground import Playground, serve_playground_app
from agno.models.ollama import Ollama

load_dotenv()

db_url = getenv("PGVECTOR_URL", "")

if db_url == "":
    raise ValueError('Environment variable "PGVECTOR_URL" is not set.')


def main():
    document_data = get_document_data(Path("./data"))
    if len(document_data) == 0:
        print("No data found in the specified directory.")
        return None

    db = PgVector(
        table_name="docs_768d",
        db_url=db_url,
        search_type=SearchType.hybrid,
        embedder=OllamaEmbedder(id="nomic-embed-text", dimensions=768),
        vector_index="HSNW",
    )

    docs = [Document(content=text) for text in document_data]
    print(f"Loaded {len(docs)} documents.")

    kb = DocumentKnowledgeBase(
        documents=docs,
        vector_db=db,
    )
    kb.load(upsert=True)

    agent = Agent(
        model=Ollama(id="mistral:latest"),
        name="Knowledge Agent",
        knowledge=[kb],
        show_tool_calls=True,
        description="You are the representative of #InsightlyAI#"
        "You can answer questions about the company and its products"
        "based on the information provided.",
        instructions=(
            "- For simple greetings like 'hi' or 'hello', respond with 'Hello! How can I help you with information about InsightlyAI today?'\n"
            "- For all other queries, go directly to the answer without any greeting phrase like 'Hello' or 'I'd be happy to help'.\n"
            "- Start your response by directly addressing the query.\n"
            "- Use only the provided documents to answer questions.\n"
            "- Do not share any technical implementation details, internal systems information, or security practices.\n"
            "- Do not share any personal information, customer data, financial information, or other sensitive business information.\n"
            "- If asked about sensitive information, respond with 'I'm not authorized to share that information.'\n"
            "- Ensure responses are accurate, concise, and directly address the query.\n"
            "- If the answer is not found in the documents, respond with 'I don't know.'\n"
            "- Maintain a conversational tone, while being professional and helpful.\n"
            "- Avoid lengthy responses unless explicitly requested."
        ),
        search_knowledge=True,
        markdown=True,
    )

    return Playground(agents=[agent]).get_app()


app = main()


if __name__ == "__main__":
    serve_playground_app("main:app", reload=True)
