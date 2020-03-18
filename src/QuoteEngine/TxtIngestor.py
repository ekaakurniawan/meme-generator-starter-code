"""Text file quote ingestor module."""


from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TxtIngestor(IngestorInterface):
    """Concrete class that ingests text file."""

    allowed_extensions = ['txt']

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

        quotes = []
        with open(path, 'r', encoding='utf-8-sig') as fh:
            lines = fh.readlines()
            for line in lines:
                if '-' in line:
                    body, author = line.strip().split('-')
                    body, author = QuoteModel.clean_quote(body, author)
                    quote = QuoteModel(body, author)
                    quotes.append(quote)

        return quotes
