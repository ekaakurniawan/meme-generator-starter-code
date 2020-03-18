"""Meme Generator Web Application."""


import random
import os
import requests
import sys
from flask import Flask, render_template, abort, request, Response

# @TODO Import your Ingestor and MemeEngine classes
from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine import Ingestor
from MemeEngine import MemeEngine


app = Flask(__name__)

font_path = './_data/fonts/LilitaOne-Regular.ttf'
meme = MemeEngine('./static', font_path)


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"
    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.
    image_url = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author')

    delete_image_flag = False
    if image_url == '':
        img = random.choice(imgs)
    else:
        extension = image_url.split('.')[-1].lower()
        r = requests.get(image_url, allow_redirects=True)
        tmp = f'./tmp/{random.randint(0, 9999999999999999)}.{extension}'
        open(tmp, 'wb').write(r.content)
        delete_image_flag = True
        img = tmp

    if body == '':
        quote = random.choice(quotes)
    else:
        if author == '':
            if delete_image_flag:
                os.remove(img)
            abort(Response('Author Required if Body is Used'))
        quote = QuoteModel(body, author)

    path = meme.make_meme(img, quote.body, quote.author)
    if delete_image_flag:
        os.remove(img)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
