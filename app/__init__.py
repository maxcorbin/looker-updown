from flask import Flask
from config import Config
from slackclient import SlackClient
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
app.config.from_object(Config)

from . import routes
from .models import Services

r = redis.from_url(os.environ.get('REDIS_URL'))
slack = SlackClient(os.environ.get('SLACK_TOKEN')

scheduler = BackgroundScheduler()
scheduler.add_jobstore('redis',
    jobskey='updown.jobs',
    run_times_key='updown.run_times')
services = Services()

for service in services:
    scheduler.add_job(service.check, 'interval', seconds=1, args=[slack])

scheduler.start()
