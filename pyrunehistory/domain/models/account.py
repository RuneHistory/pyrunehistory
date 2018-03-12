from datetime import datetime


class Account:
    def __init__(self, id: str, nickname: str, slug: str,
                 runs_unchanged: int, last_run_at: datetime,
                 run_changed_at: datetime, created_at: datetime,
                 updated_at: datetime):
        self.id = id
        self.nickname = nickname
        self.slug = slug
        self.runs_unchanged = runs_unchanged
        self.last_run_at = last_run_at
        self.run_changed_at = run_changed_at
        self.created_at = created_at
        self.updated_at = updated_at

    def get_encodable(self):
        return {
            'id': self.id,
            'nickname': self.nickname,
            'slug': self.slug,
            'runs_unchanged': self.runs_unchanged,
            'last_run_at': self.last_run_at.isoformat()
            if self.last_run_at else None,
            'run_changed_at': self.run_changed_at.isoformat()
            if self.run_changed_at else None,
            'created_at': self.created_at.isoformat()
            if self.created_at else None,
            'updated_at': self.updated_at.isoformat()
            if self.updated_at else None,
        }
