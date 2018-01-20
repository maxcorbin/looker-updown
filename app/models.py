from slackclient import SlackClient

class Status(dict):
    """This class represents status updates from the services that the
    module is monitoring.

    Attributes:
        service: A string containing the name of the service
        up: A boolean indicating whether the service is up
    """
    def __init__(self, service, up):
        self.service = service
        self.up = up
