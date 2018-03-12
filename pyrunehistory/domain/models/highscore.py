import typing

from datetime import datetime

SKILLS = ['overall', 'attack', 'defence', 'strength', 'hitpoints',
          'ranged', 'prayer', 'magic', 'cooking', 'woodcutting',
          'fletching', 'fishing', 'firemaking', 'crafting', 'smithing',
          'mining', 'herblore', 'agility', 'theiving', 'slayer',
          'farming', 'hunter']


class Skill:
    def __init__(self, rank: int, level: int, experience: int):
        self.rank = int(rank)
        self.level = int(level)
        self.experience = int(experience)

    def get_encodable(self):
        return {
            'rank': self.rank,
            'level': self.level,
            'experience': self.experience,
        }


class HighScore:
    def __init__(self, account_id: str, id: str,
                 created_at: datetime, skills: typing.Dict[str, Skill]):
        self.account_id = account_id
        self.id = id
        self.created_at = created_at
        self._skills = dict()
        self.skills = skills

    @property
    def skills(self) -> typing.Dict[str, typing.Union[None, Skill]]:
        return {
            skill: self._skills[skill]
            if skill in self._skills else None
            for skill in SKILLS
        }

    @skills.setter
    def skills(self, skills: typing.Dict[str, Skill]):
        validate_skills(skills)
        self._skills = skills

    def get_encodable(self):
        return {
            'account_id': self.account_id,
            'id': self.id,
            'created_at': self.created_at.isoformat()
            if self.created_at else None,
            'skills': from_skills(self.skills),
        }


def validate_skills(skills: typing.Dict[str, Skill]):
    for name, skill in skills.items():
        if name not in SKILLS:
            raise AttributeError('{key} is not a valid skill'.format(
                key=name
            ))
        if not isinstance(skill, Skill):
            raise AttributeError('Skills need to be an instance of {}'.format(
                Skill.__name__
            ))


def to_skills(skills: typing.Dict[str, dict]):
    return {
        name: Skill(**skill)
        for name, skill in skills.items()
    }


def from_skills(skills: typing.Dict[str, Skill]):
    return {name: skill.get_encodable() for name, skill in
            skills.items() if skill is not None}
