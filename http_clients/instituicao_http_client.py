from http_clients.base_http_client import BaseHttpClient

import requests
import json

class InstituicaoHttpClient(BaseHttpClient):

    def __init__(self):
        super().__init__()

    def obter_instituicoes(self, nome = None, categoria_id = None):
        params = {}

        if not nome is None:
            params['nome'] = nome

        if not categoria_id is None:
            params['categoria_id'] = categoria_id

        endpoint = f'/instituicoes'
        instituicoes = requests.get(self.api_url + endpoint, params).content
        return json.loads(instituicoes)