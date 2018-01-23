from requests import get
from feedparser import parse as fparse
from json import loads
import random

class Services(list):
    """This class initializes each service and puts them in an array to iterate over when scheduling jobs. Temporary solution until I work out some persistence.
    """

    def __init__(self):
        self.append(Zendesk())
        self.append(TestService())

class AWS(object):
    """ Docstring TODO
    """

    def __init__(self):
        self.url = 'https://status.aws.amazon.com/rss/ec2-us-east-1.rss'

    def check(self, slack):
        entries = fparse(self.url).entries

class Zendesk(object):
    """This class represents the Zendesk service that is polled for its status.
    It is intended to be a singleton, but not yet implemented as such.
    """

    def __init__(self):
        self.url = 'https://status.zendesk.com/api/internal/incidents.json'

    def check(self, slack):
        response = loads(get(self.url).text)
        incidents = response['current_incidents']
        if len(incidents) > 0:
            slack.api_call('chat.postMessage',
                channel='#general',
                text=('*Zendesk Status Update: *\n<!here> ' + str(incidents[0])))

class GoodResponse(object):
    def __init__(self):
        self.text = 'Service is up'
        self.status_code = 200

    def __bool__(self):
        return self.status_code < 400

class BadResponse(object):
    def __init__(self):
        self.text = 'Service is down'
        self.status_code = 404

    def __bool__(self):
        return self.status_code < 400

class TestService(object):

    def check(self, slack):
        if random.randint(1, 100) == 1:
            status =  BadResponse()
        else:
            status =  GoodResponse()
        if not status:
            slack.api_call('chat.postMessage',
                channel='#general',
                text=('*Test Status Update: *\n<!here> ' + status.text))
