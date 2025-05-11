from typing import List
from pathlib import Path
from helpers.text_extractor import TextExtractor


def get_document_data(knowledge_data: Path) -> List[str]:
    extracted_data: List[str] = []

    adapter = TextExtractor()
    for data_source_item in knowledge_data.iterdir():
        if data_source_item.is_file():
            extracted_data.append(adapter.extract(data_source_item))

    return extracted_data
