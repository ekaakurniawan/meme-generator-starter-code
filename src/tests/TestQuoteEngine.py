"""Quote engine tester module."""


import pathlib
import unittest

from QuoteEngine import CSVIngestor, DocxIngestor, PDFIngestor, TxtIngestor
from QuoteEngine import Ingestor


PROJECT_ROOT = pathlib.Path(__file__).parent.parent


class TestQuoteEngine(unittest.TestCase):
    """Collection of Quote Engine testers."""

    quote_csv_file = f'{PROJECT_ROOT}/_data/DogQuotes/DogQuotesCSV.csv'
    quote_txt_file = f'{PROJECT_ROOT}/_data/DogQuotes/DogQuotesTXT.txt'
    quote_docx_file = f'{PROJECT_ROOT}/_data/DogQuotes/DogQuotesDOCX.docx'
    quote_pdf_file = f'{PROJECT_ROOT}/_data/DogQuotes/DogQuotesPDF.pdf'

    def test_csv_ingestor__can_ingest__true(self):
        """Test CSV file ingestor, can_ingest function."""
        result = CSVIngestor.can_ingest(TestQuoteEngine.quote_csv_file)
        self.assertEqual(result, True)

    def test_csv_ingestor__can_ingest__false(self):
        """Test CSV file ingestor, can_ingest function."""
        result = CSVIngestor.can_ingest(TestQuoteEngine.quote_txt_file)
        self.assertEqual(result, False)

    def test_csv_ingestor__parse__complete(self):
        """Test CSV file ingestor, parse function."""
        result = CSVIngestor.parse(TestQuoteEngine.quote_csv_file)
        self.assertEqual(len(result), 2)
        self.assertEqual(
            result[0].__repr__(),
            '"Chase the mailman" - Skittle')
        self.assertEqual(
            result[1].__repr__(),
            '"When in doubt, go shoe-shopping" - Mr. Paws')

    def test_docx_ingestor__can_ingest__true(self):
        """Test Docx file ingestor, can_ingest function."""
        result = DocxIngestor.can_ingest(TestQuoteEngine.quote_docx_file)
        self.assertEqual(result, True)

    def test_docx_ingestor__can_ingest__false(self):
        """Test Docx file ingestor, can_ingest function."""
        result = DocxIngestor.can_ingest(TestQuoteEngine.quote_csv_file)
        self.assertEqual(result, False)

    def test_docx_ingestor__parse__complete(self):
        """Test Docx file ingestor, parse function."""
        result = DocxIngestor.parse(TestQuoteEngine.quote_docx_file)
        self.assertEqual(len(result), 4)
        self.assertEqual(
            result[0].__repr__(),
            '"Bark like no one’s listening" - Rex')
        self.assertEqual(
            result[1].__repr__(),
            '"RAWRGWAWGGR" - Chewy')
        self.assertEqual(
            result[2].__repr__(),
            '"Life is like peanut butter: crunchy" - Peanut')
        self.assertEqual(
            result[3].__repr__(),
            '"Channel your inner husky" - Tiny')

    def test_pdf_ingestor__can_ingest__true(self):
        """Test PDF file ingestor, can_ingest function."""
        result = PDFIngestor.can_ingest(TestQuoteEngine.quote_pdf_file)
        self.assertEqual(result, True)

    def test_pdf_ingestor__can_ingest__false(self):
        """Test PDF file ingestor, can_ingest function."""
        result = PDFIngestor.can_ingest(TestQuoteEngine.quote_docx_file)
        self.assertEqual(result, False)

    def test_pdf_ingestor__parse__complete(self):
        """Test PDF file ingestor, parse function."""
        result = PDFIngestor.parse(TestQuoteEngine.quote_pdf_file)
        self.assertEqual(len(result), 3)
        self.assertEqual(
            result[0].__repr__(),
            '"Treat yo self" - Fluffles')
        self.assertEqual(result[1].__repr__(),
                         '"Life is like a box of treats" - Forrest Pup')
        self.assertEqual(
            result[2].__repr__(),
            '"It\'s the size of the fight in the dog" - Bark Twain')

    def test_txt_ingestor__can_ingest__true(self):
        """Test Text file ingestor, can_ingest function."""
        result = TxtIngestor.can_ingest(TestQuoteEngine.quote_txt_file)
        self.assertEqual(result, True)

    def test_txt_ingestor__can_ingest__false(self):
        """Test Text file ingestor, can_ingest function."""
        result = TxtIngestor.can_ingest(TestQuoteEngine.quote_pdf_file)
        self.assertEqual(result, False)

    def test_txt_ingestor__parse__complete(self):
        """Test text file ingestor, parse function."""
        result = TxtIngestor.parse(TestQuoteEngine.quote_txt_file)
        self.assertEqual(len(result), 2)
        self.assertEqual(
            result[0].__repr__(),
            '"To bork or not to bork" - Bork')
        self.assertEqual(
            result[1].__repr__(),
            '"He who smelt it..." - Stinky')

    def test_ingestor__parse__csv_complete(self):
        """Test ingestor's parse function for CSV file."""
        result = Ingestor.parse(TestQuoteEngine.quote_csv_file)
        self.assertEqual(len(result), 2)
        self.assertEqual(
            result[0].__repr__(),
            '"Chase the mailman" - Skittle')
        self.assertEqual(
            result[1].__repr__(),
            '"When in doubt, go shoe-shopping" - Mr. Paws')

    def test_ingestor__parse__docx_complete(self):
        """Test ingestor's parse function for Docx file."""
        result = Ingestor.parse(TestQuoteEngine.quote_docx_file)
        self.assertEqual(len(result), 4)
        self.assertEqual(
            result[0].__repr__(),
            '"Bark like no one’s listening" - Rex')
        self.assertEqual(
            result[1].__repr__(),
            '"RAWRGWAWGGR" - Chewy')
        self.assertEqual(
            result[2].__repr__(),
            '"Life is like peanut butter: crunchy" - Peanut')
        self.assertEqual(
            result[3].__repr__(),
            '"Channel your inner husky" - Tiny')

    def test_ingestor__parse__pdf_complete(self):
        """Test ingestor's parse function for PDF file."""
        result = Ingestor.parse(TestQuoteEngine.quote_pdf_file)
        self.assertEqual(len(result), 3)
        self.assertEqual(
            result[0].__repr__(),
            '"Treat yo self" - Fluffles')
        self.assertEqual(
            result[1].__repr__(),
            '"Life is like a box of treats" - Forrest Pup')
        self.assertEqual(
            result[2].__repr__(),
            '"It\'s the size of the fight in the dog" - Bark Twain')

    def test_ingestor__parse__txt_complete(self):
        """Test ingestor's parse function for text file."""
        result = Ingestor.parse(TestQuoteEngine.quote_txt_file)
        self.assertEqual(len(result), 2)
        self.assertEqual(
            result[0].__repr__(),
            '"To bork or not to bork" - Bork')
        self.assertEqual(
            result[1].__repr__(),
            '"He who smelt it..." - Stinky')


if __name__ == '__main__':
    unittest.main()
