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
