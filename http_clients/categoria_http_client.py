from http_clients.base_http_client import BaseHttpClient

import json
import requests

class CategoriaHttpClient(BaseHttpClient):

    def __init__(self):
        super().__init__()

    def obter_categorias(self):
        categorias = requests.get(self.api_url + '/categorias').content
        return json.loads(categorias)
