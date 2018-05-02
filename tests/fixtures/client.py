from pytest import fixture
from unittest import mock

from pyrunehistory.client import Client


@fixture
def client() -> Client:
    c = Client('user', 'password', 'secret', 'http://tests')
    c.auth.refresh = mock.create_autospec(c.auth.refresh)
    return c
