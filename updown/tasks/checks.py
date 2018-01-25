from requests import get
from feedparser import parse
from json import loads
from random import randint
import celery
from updown import slack


@celery.task()
def check_testservice():
    if randint(1, 24) == 1:
        message = '*Test Status Update: *\n<!here> ' + 'Service is down!'
        slack.api_call(
            'chat.postMessage',
            channel = '#general',
            text = message)

@celery.task()
def check_zendesk():
    url = 'https://status.zendesk.com/api/internal/incidents.json'
    response = get(url)
    if response:
        incidents = loads(response.text)['current_incidents']
        if len(incidents) > 0:
            message = '*Zendesk Status Update: *\n<!here> ' + str(incidents[0])
            slack.api_call(
                'chat.postMessage',
                channel = '#general',
                text = message)
