import typing
from datetime import datetime

from pyrunehistory.domain.models.account import Account
from pyrunehistory.highscores import HighScores


class Accounts:
    def __init__(self, client: 'pyrunehistory.client.Client'):
        self.client = client

    def get_accounts(self, runs_unchanged_min: int = None,
                     runs_unchanged_max: int = None,
                     last_ran_before: datetime = None,
                     prioritise: bool = True
                     ) -> typing.List[Account]:
        params = {}
        if runs_unchanged_min is not None:
            params['runs_unchanged_min'] = runs_unchanged_min
        if runs_unchanged_max is not None:
            params['runs_unchanged_max'] = runs_unchanged_max
        if last_ran_before is not None:
            params['last_ran_before'] = last_ran_before.isoformat()
        if prioritise is not None:
            params['prioritise'] = prioritise
        response = self.client(
            'GET',
            'accounts',
            params=params
        )
        accounts = []
        for record in response:
            accounts.append(Account(**record))
        return accounts

    def get_account(self, slug: str) -> Account:
        response = self.client(
            'GET',
            'accounts/{}'.format(slug)
        )
        return Account(**response)

    def create_account(self, nickname: str) -> Account:
        response = self.client(
            'POST',
            'accounts',
            data={
                'nickname': nickname
            }
        )
        return Account(**response)

    def update_account(self, slug: str, nickname: str) -> Account:
        response = self.client(
            'PUT',
            'accounts/{}'.format(slug),
            data={
                'nickname': nickname
            }
        )
        return Account(**response)

    @property
    def highscores(self) -> HighScores:
        return HighScores(self.client)
