from flask import Flask
import os
from wit import Wit

app = Flask(__name__)

wit = Wit(os.environ['WIT_ACCESS_TOKEN'])

from chatbot import urls

if __name__ == "__main__":
    app.run()