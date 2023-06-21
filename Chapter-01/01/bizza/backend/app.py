from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)


@app.route('/')
def index():
    return ' Welcome to Parth Platform!'


if __name__ == '__main__':

    app.run()
