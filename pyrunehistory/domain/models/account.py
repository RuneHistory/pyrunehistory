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
