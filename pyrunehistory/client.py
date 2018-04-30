import json
import typing

import requests

from pyrunehistory.accounts import Accounts
from pyrunehistory.auth import Auth


class Client(object):
    def __init__(self, username, password, secret,
                 host='http://api.runehistory.com', version: int = 1):
        self.host = host
        self.version = version
        self.auth = Auth(self, username, password, secret)

    @property
    def hostname(self) -> str:
        return '{host:s}/v{version:d}'.format(
            host=self.host, version=self.version
        )

    def __call__(self, method: str, url: str, params: typing.Dict = None,
                 data: typing.Dict = None, auth='jwt') -> dict:
        url = '{host}/{endpoint}'.format(
            host=self.hostname,
            endpoint=url
        )
        encoded_data = json.dumps(data) if data else None
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        response = requests.request(method, url, params=params,
                                    data=encoded_data, headers=headers,
                                    auth=self.auth.get(auth))
        response.raise_for_status()
        return response.json()

    @property
    def accounts(self) -> Accounts:
        return Accounts(self)
