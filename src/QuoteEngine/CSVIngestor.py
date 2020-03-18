"""CSV file quote ingestor module."""


from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Concrete class that ingests CSV file."""

    allowed_extensions = ['csv']

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

        df = pandas.read_csv(path, header=0)
        quotes = []
        for index, row in df.iterrows():
            body, author = row['body'], row['author']
            body, author = QuoteModel.clean_quote(body, author)
            quote = QuoteModel(body, author)
            quotes.append(quote)

        return quotes
