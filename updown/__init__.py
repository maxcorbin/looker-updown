from flask import Flask
from celery import Celery
from config import Config
from slackclient import SlackClient


app = Flask(__name__)
app.config.from_object(Config)

slack = SlackClient(app.config['SLACK_TOKEN'])

from . import routes, tasks
from .celery import make_celery

celery = make_celery(app)
