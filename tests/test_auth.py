from unittest.mock import patch, create_autospec

import pytest
from requests.auth import HTTPBasicAuth
from requests.models import PreparedRequest
from simplejwt import Jwt

from tests import IsInstance
from pyrunehistory.client import Client
from pyrunehistory.auth import Auth, JwtAuth


def test_auth_jwt_with_no_token(auth: Auth):
    jwt = Jwt(auth.secret)
    token = jwt.encode()
    with patch('pyrunehistory.client.Client.__call__',
               autospec=True) as call_mock:
        call_mock.return_value = {
            'token': token
        }
        assert isinstance(auth.get('jwt'), JwtAuth)
        call_mock.assert_called_with(IsInstance(Client), 'GET', 'auth/token', auth='basic')
        assert isinstance(auth.jwt, Jwt)
        assert auth.token == token


def test_auth_basic(auth: Auth):
    assert isinstance(auth.get('basic'), HTTPBasicAuth)


def test_auth_unknown(auth: Auth):
    with pytest.raises(ValueError):
        auth.get('unknown')


def test_jwt_auth_header():
    jwt_auth = JwtAuth('asdf')
    without_header = PreparedRequest()
    with_header = jwt_auth(without_header)
    assert isinstance(with_header, PreparedRequest)
    assert with_header.headers.get('Authorization') == 'Bearer asdf'
