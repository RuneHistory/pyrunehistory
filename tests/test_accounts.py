from datetime import datetime
from copy import deepcopy

from dateutil.parser import parse
from pytest import fixture
from unittest.mock import patch

from pyrunehistory.client import Client
from pyrunehistory.accounts import Accounts


@fixture
def accounts(client: Client) -> Accounts:
    return client.accounts


@fixture
def account_data():
    return deepcopy([
        {
            "created_at": parse("2018-02-16T11:19:50.215000"),
            "id": "5a86be56b0d12d0309c185b9",
            "last_run_at": parse("2018-03-05T18:37:31.470000"),
            "nickname": "Wrighto",
            "run_changed_at": parse("2018-02-26T23:46:44.887000"),
            "runs_unchanged": 27,
            "slug": "wrighto",
            "updated_at": parse("2018-02-16T14:08:28.181000")
        }
    ])


def test_get_accounts(accounts: Accounts, account_data):
    now = datetime.utcnow()
    with patch('pyrunehistory.client.Client.__call__') as call_mock:

        call_mock.return_value = account_data
        res = accounts.get_accounts(1, 2, now)
        call_mock.assert_called_with('GET', 'accounts',
                                        params={
                                            'runs_unchanged_min': 1,
                                            'runs_unchanged_max': 2,
                                            'last_ran_before': now.isoformat(),
                                            'prioritise': True
                                        })
        assert res[0].created_at.isoformat() == '2018-02-16T11:19:50.215000'
        assert res[0].id == '5a86be56b0d12d0309c185b9'
        assert res[0].last_run_at.isoformat() == '2018-03-05T18:37:31.470000'
        assert res[0].nickname == 'Wrighto'
        assert res[0].run_changed_at.isoformat() == '2018-02-26T23:46:44.887000'
        assert res[0].runs_unchanged == 27
        assert res[0].slug == 'wrighto'
        assert res[0].updated_at.isoformat() == '2018-02-16T14:08:28.181000'


def test_get_account(accounts: Accounts, account_data):
    with patch('pyrunehistory.client.Client.__call__') as call_mock:
        call_mock.return_value = account_data[0]
        res = accounts.get_account('wrighto')
        call_mock.assert_called_with('GET', 'accounts/wrighto')
        assert res.created_at.isoformat() == '2018-02-16T11:19:50.215000'
        assert res.id == '5a86be56b0d12d0309c185b9'
        assert res.last_run_at.isoformat() == '2018-03-05T18:37:31.470000'
        assert res.nickname == 'Wrighto'
        assert res.run_changed_at.isoformat() == '2018-02-26T23:46:44.887000'
        assert res.runs_unchanged == 27
        assert res.slug == 'wrighto'
        assert res.updated_at.isoformat() == '2018-02-16T14:08:28.181000'


def test_create_account(accounts: Accounts, account_data):
    with patch('pyrunehistory.client.Client.__call__') as call_mock:
        call_mock.return_value = account_data[0]
        res = accounts.create_account('Wrighto')
        call_mock.assert_called_with('POST', 'accounts', data={
            'nickname': 'Wrighto'
        })
        assert res.created_at.isoformat() == '2018-02-16T11:19:50.215000'
        assert res.id == '5a86be56b0d12d0309c185b9'
        assert res.last_run_at.isoformat() == '2018-03-05T18:37:31.470000'
        assert res.nickname == 'Wrighto'
        assert res.run_changed_at.isoformat() == '2018-02-26T23:46:44.887000'
        assert res.runs_unchanged == 27
        assert res.slug == 'wrighto'
        assert res.updated_at.isoformat() == '2018-02-16T14:08:28.181000'


def test_update_account(accounts: Accounts, account_data):
    with patch('pyrunehistory.client.Client.__call__') as call_mock:
        account_data[0]['slug'] = 'wrighto2'
        account_data[0]['nickname'] = 'Wrighto2'
        call_mock.return_value = account_data[0]
        res = accounts.update_account('wrighto', 'Wrighto2')
        call_mock.assert_called_with('PUT', 'accounts/wrighto', data={
            'nickname': 'Wrighto2'
        })
        assert res.created_at.isoformat() == '2018-02-16T11:19:50.215000'
        assert res.id == '5a86be56b0d12d0309c185b9'
        assert res.last_run_at.isoformat() == '2018-03-05T18:37:31.470000'
        assert res.nickname == 'Wrighto2'
        assert res.run_changed_at.isoformat() == '2018-02-26T23:46:44.887000'
        assert res.runs_unchanged == 27
        assert res.slug == 'wrighto2'
        assert res.updated_at.isoformat() == '2018-02-16T14:08:28.181000'
