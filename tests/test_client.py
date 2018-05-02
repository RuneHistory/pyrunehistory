import json

from unittest.mock import patch

from pyrunehistory.auth import JwtAuth
from pyrunehistory.client import Client
from pyrunehistory.accounts import Accounts
from tests import IsInstance


def test_hostname(client: Client):
    assert client.hostname == 'http://tests/v1'


def test_accounts(client: Client):
    assert isinstance(client.accounts, Accounts)


def test_call_request_parameters(client: Client):
    method = 'GET'
    url = 'some_url'
    params = {'test_param': 123}
    data = {'test_data': 456}
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    merged_url = '{}/{}'.format(client.hostname, url)
    with patch('requests.request') as request_mock:
        client(method, url, {'test_param': 123}, {'test_data': 456})
        request_mock.assert_called_with(method, merged_url,
                                        auth=IsInstance(JwtAuth),
                                        params=params, data=json.dumps(data),
                                        headers=headers)
