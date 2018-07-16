import requests
import typing
from datetime import datetime
from pyrunehistory.domain.models.account import Account
from pyrunehistory.domain.models.highscore import HighScore, Skill, SKILLS


def get_raw_highscores(player: str) -> str:
    response = requests.get(
        'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws', {
            'player': player
        })
    response.raise_for_status()
    return response.content.decode('utf-8')


def get_highscore(account: Account) -> HighScore:
    skills = get_plain_highscore(account.nickname)
    highscore = HighScore(account.id, datetime.utcnow(), skills)
    return highscore


def get_plain_highscore(nickname: str) -> dict:
    raw_skills = get_raw_highscores(nickname)
    return parse_response(raw_skills)


def parse_response(data: str) -> typing.Dict[str, Skill]:
    split_skills = data.split('\n')
    skills = {}
    for index, skill_name in enumerate(SKILLS):
        rank, level, experience = split_skills[index].split(',')
        skill = Skill(rank, level, experience)
        skills[skill_name] = skill
    return skills
