from pytest import fixture

from pyrunehistory.client import Client


@fixture
def client() -> Client:
    return Client('user', 'password', 'secret', 'http://tests')
