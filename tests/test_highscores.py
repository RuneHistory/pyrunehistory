from datetime import datetime
import json
from copy import deepcopy

from dateutil.parser import parse
import pytest
from pytest import fixture
from unittest.mock import patch

from pyrunehistory.client import Client
from pyrunehistory.highscores import HighScores, to_skills


@fixture
def highscores(client: Client) -> HighScores:
    return client.accounts.highscores('wrighto')


with open('tests/data/highscores.json') as handler:
    test_highscores = json.load(handler)
    for highscore in test_highscores:
        highscore['created_at'] = parse(highscore['created_at'])


@fixture
def highscores_data():
    return deepcopy(test_highscores)


@fixture
def highscores_objects():
    highscores = []
    for highscore in deepcopy(test_highscores):
        highscore['skills'] = to_skills(highscore['skills'])
        highscores.append(highscore)
    return highscores


def test_get_highscores(highscores: HighScores, highscores_data):
    now = datetime.utcnow()
    with patch('pyrunehistory.client.Client.__call__') as call_mock:
        call_mock.return_value = highscores_data
        res = highscores.get_highscores(now, now)
        call_mock.assert_called_with('GET', 'accounts/wrighto/highscores',
                                        params={
                                            'created_after': now.isoformat(),
                                            'created_before': now.isoformat(),
                                        })
        assert res[0].account_id == '5a86be56b0d12d0309c185b9'
        assert res[0].created_at.isoformat() == '2018-03-05T18:37:31.467000'
        assert res[0].id == '5a9d8e6b95f5e704af4e3d39'
        assert res[0].skills.get('agility').experience == 93662
        assert res[0].skills.get('agility').level == 49
        assert res[0].skills.get('agility').rank == 572001


def test_get_highscore(highscores: HighScores, highscores_data):
    with patch('pyrunehistory.client.Client.__call__') as call_mock:
        call_mock.return_value = highscores_data[0]
        res = highscores.get_highscore('5a9d8e6b95f5e704af4e3d39')
        call_mock.assert_called_with('GET', 'accounts/wrighto/highscores/5a9d8e6b95f5e704af4e3d39')
        assert res.account_id == '5a86be56b0d12d0309c185b9'
        assert res.created_at.isoformat() == '2018-03-05T18:37:31.467000'
        assert res.id == '5a9d8e6b95f5e704af4e3d39'
        assert res.skills.get('agility').experience == 93662
        assert res.skills.get('agility').level == 49
        assert res.skills.get('agility').rank == 572001


def test_create_highscore(highscores: HighScores, highscores_data, highscores_objects):
    with patch('pyrunehistory.client.Client.__call__') as call_mock:
        call_mock.return_value = highscores_data[0]
        res = highscores.create_highscore(highscores_objects[0]['skills'])
        call_mock.assert_called_with('POST',
                                     'accounts/wrighto/highscores',
                                     data={
                                         'skills': highscores_objects[0]['skills']
                                     })
        assert res.account_id == '5a86be56b0d12d0309c185b9'
        assert res.created_at.isoformat() == '2018-03-05T18:37:31.467000'
        assert res.id == '5a9d8e6b95f5e704af4e3d39'
        assert res.skills.get('agility').experience == 93662
        assert res.skills.get('agility').level == 49
        assert res.skills.get('agility').rank == 572001


def test_create_highscore_raises_missing_skill(highscores: HighScores, highscores_objects):
    with pytest.raises(ValueError):
        highscores_objects[0]['skills'].pop('agility')
        highscores.create_highscore(highscores_objects[0]['skills'])
