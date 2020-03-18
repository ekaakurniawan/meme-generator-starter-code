"""Meme engine module."""


import random
from PIL import Image, ImageDraw, ImageFont


class MemeEngine():
    """Meme engine class."""

    def __init__(self, output_directory: str, font_path: str):
        """Initialize meme engine with the location of output directory.

        Arguments:
            output_directory {str} -- output directory.
            font_path {str} -- path to font type.
        """
        self.output_directory = output_directory
        self.font_path = font_path

    def resize_image(self, img: Image, width: int) -> Image:
        """Resize image to maximum width argument while keeping the ratio.

        Arguments:
            img {Image} -- input image.
            width {int} -- maximum width value.
        Returns:
            Image -- resized image.
        """
        img_width = img.size[0]
        if img_width > width:
            ratio = width / float(img.size[0])
            height = int(ratio * float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

        return img

    def make_meme(self, img_path: str, text: str, author: str,
                  width: int = 500) -> str:
        """Make meme using an image and a quote (text and the author).

        Arguments:
            img_path {str} -- file location for the input image.
            text {str} -- quote body.
            author {str} -- quote author.
            width {int} -- maximum width value. Default=500.
        Returns:
            str -- file location for the output image.
        """
        # Load, convert to JPEG and resize image
        img = Image.open(img_path)
        if img.format != 'JPEG':
            img = img.convert('RGB')
        img = self.resize_image(img, width)

        # Load fonts
        text_font = ImageFont.truetype(self.font_path, size=32)
        author_font = ImageFont.truetype(self.font_path, size=25)

        # Draw quote onto image
        draw = ImageDraw.Draw(img)
        y_loc = random.randint(30, img.size[1] - 120)
        draw.text((10, y_loc), f'"{text}"', font=text_font, fill='white')
        draw.text((10, y_loc + 35), f'- {author}', font=author_font,
                  fill='white')

        # Save result
        out_file = f'{random.randint(0, 9999999999999999)}.jpg'
        out_path = f'{self.output_directory}/{out_file}'
        img.save(out_path, "JPEG")

        return out_path
