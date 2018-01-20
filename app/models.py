

class Status(dict):
    def __init__(self, service, up):
        self.service = service
        self.up = up
