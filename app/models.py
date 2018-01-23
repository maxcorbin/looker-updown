from requests import get
from feedparser import parse
from json import loads
from random import randint


class AWS(object):
    """ Docstring TODO
    """

    def __init__(self):
        self.url = 'https://status.aws.amazon.com/rss/ec2-us-east-1.rss'
        self.cache = 'aws.cache'

    def check(self, post_to):
        entries = parse(self.url).entries


class Zendesk(object):
    """This class represents the Zendesk service that is polled for its status.
    It is intended to be a singleton, but not yet implemented as such.
    """

    def __init__(self):
        self.url = 'https://status.zendesk.com/api/internal/incidents.json'
        self.cache = 'zendesk.cache'

    def check(self, post_to):
        response = get(self.url)

        incidents = loads(response).text['current_incidents']
        if len(incidents) > 0:
            slack.api_call('chat.postMessage',
                channel='#general',
                text=('*Zendesk Status Update: *\n<!here> ' + str(incidents[0])))


class TestService(object):

    def __init__(self):
        self.cache_key = 'testservice.cache'

    def check(self, post_to):
        if randint(1, 24) == 1:
            slack.api_call('chat.postMessage',
                channel='#general',
                text=('*Test Status Update: *\n<!here> ' + 'Service is down!'))
