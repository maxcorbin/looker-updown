from flask import Flask, Config

app = Flask(__name__)
app.config.from_object(Config)

from . import routes
