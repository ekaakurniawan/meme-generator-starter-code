"""Docx file quote ingestor module."""


from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """Concrete class that ingests docx file."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes from file and stores them in QuoteModel objects.

        Arguments:
            path {str} -- quote file location.
        Returns:
            List -- list of quote objects.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        doc = docx.Document(path)
        quotes = []
        for paragraph in doc.paragraphs:
            if '-' in paragraph.text:
                body, author = paragraph.text.strip().split('-')
                body, author = QuoteModel.clean_quote(body, author)
                quote = QuoteModel(body, author)
                quotes.append(quote)

        return quotes
