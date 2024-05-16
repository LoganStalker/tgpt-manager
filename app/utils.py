import os

import json
import httpx

from modconfig import Config


class BackendConnector:
    def __init__(self):
        self.cfg = Config(f"app.config")
        if os.path.exists("app/config/local.py"):
            self.cfg.update_from_modules("app.config.local")

        if os.environ.get("ENV") == "tests":
            self.cfg.update_from_modules("app.config.tests")

        self.base_url = f"http://{self.cfg.BACKEND_HOST}:{self.cfg.BACKEND_PORT}"
        self.client = httpx.Client()

    def get_bots_list(self):
        res = self.client.get(f'{self.base_url}/bots', headers={'Accept': 'application/json'})
        # EXAMPLE
        # res = [
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
        #   },
        #   {
        #     'id': 2,
        #     ...
        #   }
        # ]
        return res.json()

    def create_bot(self, data):
        self.client.post(f'{self.base_url}/bots', json=data)

    def delete_bot(self, bot_id):
        self.client.delete(f'{self.base_url}/bots/{bot_id}')

    def start_bot(self, bot_id):
        self.client.post(f'{self.base_url}/bots/start', json={'id': bot_id})

    def stop_bot(self, bot_id):
        # implement the stopping procedure here
        pass
