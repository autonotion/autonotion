from typing import Any
import requests

from autonotion.models import Database, Page
from autonotion.builder import PageBuilder, DatabaseBuilder

BASE_URL = 'https://api.notion.com/v1/'
VERSION_HEADER = 'Notion-Version'
VERSION_VALUE = '2021-05-13'


class NotionClient:

    def __init__(self, token) -> None:
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({'Authorization': 'Bearer ' + self.token})
        self.session.headers.update({VERSION_HEADER: VERSION_VALUE})
        self.base_url = BASE_URL

    def __getattribute__(self, name: str) -> Any:
        if name in ['get', 'post', 'put', 'patch', 'delete']:
            return self.request(name)
        return super().__getattribute__(name)

    def request(self, method) -> dict:
        def do_request(url, payload={}):
            payload_param = 'json'
            if method == 'get':
                payload_param = 'params'
            response = getattr(self.session, method)(
                self.base_url + url,
                **{payload_param: payload}
            )
            return response.json()
        return do_request


class NotionAPIClient(NotionClient):

    def retrieve_page(self, page_id: str) -> Page:
        return PageBuilder.build(
            self.get('pages/' + page_id)
        )

    def retrieve_database(self, database_id: str) -> Database:
        return DatabaseBuilder.build(
            self.get('databases/' + database_id)
        )
