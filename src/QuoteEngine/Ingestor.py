"""Quote ingstor module."""


from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .TxtIngestor import TxtIngestor


class Ingestor(IngestorInterface):
    """Class that encapsulate different ingestor file type."""

    ingestors = [CSVIngestor, DocxIngestor, PDFIngestor, TxtIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes from files and stores them in QuoteModel objects.

        Arguments:
            path {str} -- quote file location.
        Returns:
            List -- list of quote objects.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)

        return []
