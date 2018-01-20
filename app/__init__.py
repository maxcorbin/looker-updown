from flask import Flask, Config
from tinydb import TinyDB

app = Flask(__name__)
app.config.from_object(Config)

from . import routes
