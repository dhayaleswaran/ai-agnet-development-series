from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional


class DataAdapter(ABC):
    @abstractmethod
    def extract(self, path: str) -> Optional[str]:
        """
        Extract data from the given file path.
        """
        pass

    def file_exists(self, path: str) -> bool:
        return Path(path).is_file()
