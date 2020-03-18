"""Quote model module."""


from typing import List


class QuoteModel():
    """Quote class."""

    def __init__(self, body: str, author: str):
        """Initialize quote with the body and author."""
        self.body = body
        self.author = author

    @staticmethod
    def clean_quote(body: str, author: str):
        """Clean quote from spaces, new line and double/single quotes."""
        quotes: List[str] = ['"', "'", '”']
        body = body.strip()
        if body[0] in quotes:
            body = body[1:]
        if body[-1] in quotes:
            body = body[:-1]

        author = author.strip()

        return body, author

    def __repr__(self):
        """Return quotes in readable string."""
        return f'"{self.body}" - {self.author}'
