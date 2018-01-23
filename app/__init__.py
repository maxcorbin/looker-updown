from flask import Flask
from config import Config
import os
from urllib.parse import urlparse
from slackclient import SlackClient
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.redis import RedisJobStore


app = Flask(__name__)
app.config.from_object(Config)

from . import routes
from .models import Services

r = urlparse(app.config['REDIS_URL'])

slack = SlackClient(app.config['SLACK_TOKEN'])

scheduler = BackgroundScheduler(jobstores = {
    'redis': RedisJobStore(host=r.hostname,port=r.port,password=r.password)
})

services = Services()

for service in services:
    scheduler.add_job(service.check, 'interval', seconds=1, args=[slack])

scheduler.start()
