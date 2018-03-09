from datetime import datetime

import pytest
from pyrunehistory.domain.models.highscore import HighScore, Skill, SKILLS


def test_skill_creation():
    skill = Skill(50, 30, 123456)
    assert isinstance(skill.rank, int)
    assert skill.rank == 50
    assert isinstance(skill.level, int)
    assert skill.level == 30
    assert isinstance(skill.experience, int)
    assert skill.experience == 123456


def test_skill_types():
    skill = Skill('50', '30', '123456')
    assert isinstance(skill.rank, int)
    assert skill.rank == 50
    assert isinstance(skill.level, int)
    assert skill.level == 30
    assert isinstance(skill.experience, int)
    assert skill.experience == 123456


def test_highscore_creation():
    now = datetime.utcnow()
    skills = {}
    for i, skill in enumerate(SKILLS):
        n = i + 1
        skills[skill] = Skill(n*10, n*5, n*100)
    highscore = HighScore(
        account_id='5a86be56b0d12d0309c185b9',
        id='5a9d8e6b95f5e704af4e3d39',
        created_at=now,
        skills=skills
    )
    assert highscore.account_id == '5a86be56b0d12d0309c185b9'
    assert highscore.id == '5a9d8e6b95f5e704af4e3d39'
    assert highscore.created_at == now
    assert highscore.skills.get('overall').level == 5


def test_highscore_creation_invalid_skill():
    now = datetime.utcnow()
    skills = {
        'not_a_skill': Skill(1, 2, 3)
    }
    with pytest.raises(AttributeError):
        HighScore(
            account_id='5a86be56b0d12d0309c185b9',
            id='5a9d8e6b95f5e704af4e3d39',
            created_at=now,
            skills=skills
        )


def test_highscore_creation_invalid_skill_type():
    now = datetime.utcnow()
    skills = {
        'agility': {
            'rank': 1, 'level': 2, 'experience': 3
        }
    }
    with pytest.raises(AttributeError):
        HighScore(
            account_id='5a86be56b0d12d0309c185b9',
            id='5a9d8e6b95f5e704af4e3d39',
            created_at=now,
            skills=skills
        )

