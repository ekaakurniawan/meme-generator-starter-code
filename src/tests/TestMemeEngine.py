"""Meme engine tester module."""


import pathlib
import unittest

from MemeEngine import MemeEngine


PROJECT_ROOT = pathlib.Path(__file__).parent.parent


class TestMemeEngine(unittest.TestCase):
    """Collection of meme engine testers."""

    def test_meme_engine__make_meme__pass(self):
        """Test meme engine, make_meme function."""
        output_directory = './tmp'
        font_path = f'{PROJECT_ROOT}/_data/fonts/LilitaOne-Regular.ttf'
        meme = MemeEngine(output_directory, font_path)

        img = f'{PROJECT_ROOT}/_data/photos/dog/xander_1.jpg'
        text = 'when in doubt, run'
        author = 'someone from the internet'
        result = meme.make_meme(img, text, author)
        self.assertEqual(result.split('.')[-1], 'jpg')


if __name__ == '__main__':
    unittest.main()
