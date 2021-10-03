import os

class BaseHttpClient:
    def __init__(self):
        self.api_url = os.environ.get('API_URL')