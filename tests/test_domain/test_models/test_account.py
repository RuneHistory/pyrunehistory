from datetime import datetime, timedelta

from pyrunehistory.domain.models.account import Account


def test_account_creation():
    now = datetime.utcnow()
    week_delta = timedelta(weeks=1)
    week_ago = now - week_delta

    account = Account(
        id='5a86be56b0d12d0309c185b9',
        nickname='Account',
        slug='account',
        runs_unchanged=10,
        last_run_at=now,
        run_changed_at=week_ago,
        created_at=week_ago,
        updated_at=now
    )
    assert account.id == '5a86be56b0d12d0309c185b9'
    assert account.nickname == 'Account'
    assert account.slug == 'account'
    assert account.runs_unchanged == 10
    assert account.last_run_at == now
    assert account.run_changed_at == week_ago
    assert account.created_at == week_ago
    assert account.updated_at == now


def test_account_encodable():
    now = datetime.utcnow()
    week_delta = timedelta(weeks=1)
    week_ago = now - week_delta

    account = Account(
        id='5a86be56b0d12d0309c185b9',
        nickname='Account',
        slug='account',
        runs_unchanged=10,
        last_run_at=now,
        run_changed_at=week_ago,
        created_at=week_ago,
        updated_at=now
    )
    assert account.get_encodable() == {
        'id': '5a86be56b0d12d0309c185b9',
        'nickname': 'Account',
        'slug': 'account',
        'runs_unchanged': 10,
        'last_run_at': now.isoformat(),
        'run_changed_at': week_ago.isoformat(),
        'created_at': week_ago.isoformat(),
        'updated_at': now.isoformat(),
    }
