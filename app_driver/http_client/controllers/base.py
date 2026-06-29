import httpx


class BaseController():

    def __init__(self, client: httpx.Client):
        self.client = client