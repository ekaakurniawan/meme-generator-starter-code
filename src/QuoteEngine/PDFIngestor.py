"""PDF file quote ingestor module."""


import os
import subprocess
import random
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Concrete class that ingests PDF file."""

    allowed_extensions = ['pdf']

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

        tmp_file = f'./tmp/{random.randint(0,9999999999999999)}.txt'
        call = subprocess.call(['pdftotext', path, tmp_file])

        quotes = []
        with open(tmp_file, 'r', encoding='utf-8-sig') as fh:
            lines = fh.readlines()
            for line in lines:
                if '-' in line:
                    body, author = line.strip().split('-')
                    body, author = QuoteModel.clean_quote(body, author)
                    quote = QuoteModel(body, author)
                    quotes.append(quote)

        os.remove(tmp_file)

        return quotes
