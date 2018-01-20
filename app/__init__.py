from flask import Flask
from config import Config
from slackclient import SlackClient
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
app.config.from_object(Config)

from . import routes
from .models import Zendesk, Services

scheduler = BackgroundScheduler()
services = Services()
slack = SlackClient(app.config['SLACK_TOKEN'])

for service in services:
    scheduler.add_job(service.check, 'interval', seconds=5, args=[slack])

scheduler.start()
