from flask import Flask
import os
from dotenv import load_dotenv, find_dotenv

from wit import Wit
from machaao import Machaao

load_dotenv(find_dotenv())
app = Flask(__name__)


wit = Wit(os.environ['WIT_ACCESS_TOKEN'])
machaao = Machaao(os.environ['MESSENGERX_API_TOKEN'], os.environ['MESSENGERX_BASE_URL'])

from main import urls