import typing
from datetime import datetime

from pyrunehistory.domain.models.highscore import HighScore, Skill, SKILLS,\
    validate_skills, to_skills


class HighScores:
    def __init__(self, client: 'pyrunehistory.client.Client', slug: str = None):
        self.client = client
        self.slug = slug

    def __call__(self, slug: str):
        self.slug = slug
        return self

    def get_highscores(self, created_after: datetime = None,
                       created_before: datetime = None,
                       skills: typing.List[str] = None
                       ) -> typing.List[HighScore]:
        params = {}
        if created_after is not None:
            params['created_after'] = created_after.isoformat()
        if created_before is not None:
            params['created_before'] = created_before.isoformat()
        if skills is not None:
            params['skills'] = ','.join(skills)
        response = self.client(
            'GET',
            'accounts/{}/highscores'.format(self.slug),
            params=params
        )
        highscores = []
        for record in response:
            record['skills'] = to_skills(record['skills'])
            highscores.append(HighScore(**record))
        return highscores

    def get_highscore(self, id: str) -> HighScore:
        response = self.client(
            'GET',
            'accounts/{}/highscores/{}'.format(self.slug, id)
        )
        response['skills'] = to_skills(response['skills'])
        return HighScore(**response)

    def create_highscore(self, skills: typing.Dict[str, Skill]) -> HighScore:
        missing_skills = set(SKILLS) - set(skills.keys())
        if missing_skills:
            raise ValueError(
                'Missing skills: {}'.format(','.join(missing_skills)))

        validate_skills(skills)
        response = self.client(
            'POST',
            'accounts/{}/highscores'.format(self.slug),
            data={
                'skills': skills
            }
        )
        response['skills'] = to_skills(response['skills'])
        return HighScore(**response)
