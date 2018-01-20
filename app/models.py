import requests
import json

class Services(list):
    """This class initializes each service and puts them in an array to iterate over when scheduling jobs. Temporary solution until I work out some persistence.
    """

    def __init__(self):
        self.append(Zendesk())

class Zendesk(object):
    """This class represents the Zendesk service that is polled for its status.
    It is intended to be a singleton, but not yet implemented as such.
    """

    def __init__(self):
        self.url = 'https://status.zendesk.com/api/internal/incidents.json'

    def check(self, slack):
        slack.api_call('chat.postMessage',
            channel='#general',
            text=('*Zendesk Status Update: *' + requests.get(self.url).text)
    	)
