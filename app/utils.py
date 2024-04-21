import json
import requests

import app.config as config


class BackendConnector:
    def __init__(self):
        self.host = config.BACKEND_HOST
        self.port = config.BACKEND_PORT
        self.base_url = f"http://{self.host}:{self.port}"

    def get_bots_list(self):
        res = requests.get(f'{self.base_url}/bots', headers={'Accept': 'application/json'})
        # [
        #   {
        #     'id': 1,
        #     'bot_name': 'Bot1',
        #     'bot_token': 'as123sdff43',
        #     'bot_api_id': '12345564234',
        #     'bot_api_hash': 'adsdazc123123132',
        #     'openai_api_key': 'rtterterte-trtetertlkmlmk;tr',
        #     'openai_organization': 'xcvxcvxcfdfgdfg',
        #     'openai_assistant_id': 'asdasdasdasdasd',
        #     'active': True
        #   }
        # ]
        return json.loads(res.json())

    def create_bot(self, data):
        requests.post(f'{self.base_url}/bots', json=data)

    def delete_bot(self, bot_id):
        requests.delete(f'{self.base_url}/bots/{bot_id}')

    def start_bot(self, bot_id):
        requests.post(f'{self.base_url}/bots/start', json={'id': bot_id})

    def stop_bot(self, bot_id):
        # implement the stopping procedure here
        pass
