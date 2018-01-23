from flask import Flask
from config import Config
from slackclient import SlackClient
from redis import StrictRedis


app = Flask(__name__)
app.config.from_object(Config)

slack = SlackClient(app.config['SLACK_TOKEN'])
redis = StrictRedis.from_url(app.config['REDIS_URL'])

from . import routes
from . import models
