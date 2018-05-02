from pytest import fixture

from pyrunehistory.client import Client
from pyrunehistory.auth import Auth


@fixture
def auth() -> Auth:
    c = Client('user', 'password', 'secret', 'http://tests')
    return c.auth
