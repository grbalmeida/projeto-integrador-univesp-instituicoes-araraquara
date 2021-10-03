from http_clients.base_http_client import BaseHttpClient

import requests
import json

class ImgHttpClient(BaseHttpClient):

    def __init__(self):
        super().__init__()

    def obter_imgs(self):
        imgs = requests.get(self.api_url + '/imgs').content
        return json.loads(imgs)