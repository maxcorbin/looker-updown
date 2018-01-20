import requests
import json
import random

class Services(list):
    """This class initializes each service and puts them in an array to iterate over when scheduling jobs. Temporary solution until I work out some persistence.
    """

    def __init__(self):
        self.append(Zendesk())
        self.append(TestService())

class Zendesk(object):
    """This class represents the Zendesk service that is polled for its status.
    It is intended to be a singleton, but not yet implemented as such.
    """

    def __init__(self):
        self.url = 'https://status.zendesk.com/api/internal/incidents.json'

    def check(self, slack):
        response = json.loads(requests.get(self.url).text)
        incidents = response['current_incidents']
        if len(incidents) > 0:
            slack.api_call('chat.postMessage',
                channel='#general',
                text=('*Zendesk Status Update: *\n<!here> ' + str(incidents[0])))

class TestService(object):

    def rotate(l, n):
        return l[n:] + l[:n]

    def __init__(self):
        self.dummies = [None]*1
        self.dummies = self.dummies + ['Test service is down!']

    def check(self, slack):
        status = random.sample(self.dummies, 1)
        if self.dummies[0]:
            slack.api_call('chat.postMessage',
                channel='#general',
                text=('*Test Status Update: *\n<!here> ' + str(status)))
