"""Quote ingestor interface module."""


from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Abstract class for ingestor classes."""

    allowed_extensions: List[str] = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if file extension is supported for ingestion.

        Arguments:
            path {str} -- quote file location.
        Returns:
            bool -- True if the extension is supported and False otherwise.
        """
        ext = path.split('.')[-1].lower()
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes from files and stores them in QuoteModel objects.

        Arguments:
            path {str} -- quote file location.
        Returns:
            List -- list of quote objects.
        """
        pass
