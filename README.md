# Meme Generator
Meme generator is an application that can generate meme by combining image and text from users.
This application supports both CLI and web based requests.


## Setup
This code is tested on Python 3.6+.

### Get the Code
```
$ git clone https://github.com/ekaakurniawan/meme-generator-starter-code.git
```

### Create Virtual Environment
Name the virtual environment `meme-generator` or something else. You only need to do this once.
```
$ python3 -m venv [...]/virtualenv/meme-generator
```

### Activate the virtual environment.
```
$ source [...]/virtualenv/meme-generator/bin/activate
```
As the result, make sure your prompt has additional `(meme-generator)`. Run the reset of the commands in the virtual environment.

### Install Required Python Packages
Go to `meme-generator-starter-code` directory and run the following.
```
$ pip install -r requirements.txt
```

### Install Required Linux Packages
```
$ sudo apt-get install -y xpdf
```

### Run Unit Testing
To run unit testing, go to `src` directory.
#### Test Quote Engine
```
$ python -m unittest tests.TestQuoteEngine
```
#### Test Meme Engine
```
$ python -m unittest tests.TestMemeEngine
```

### Exit the Virtual Environment
Use `deactivate` command to exit from virtual environment.
```
$ deactivate
```
You can activate it again using `activate` command shown above.


## Project Organization
All codes are located in `src` directory.
 - `MemeEngine`: Python module to make meme by combining image and quote.
 - `QuoteEngine`: Python module to ingest quote from different file types (CSV, Docx, PDF and Text).
 - `_data`: Directory to store images, quote files and font.
 - `templates`: Directory to store HTML templates.
 - `tests`: Python module for unit testing.
 - `tmp`: Directory to store temporary files and meme result.
 - `app.py`: Web application entry point.
 - `meme.py`: CLI application entry point.
