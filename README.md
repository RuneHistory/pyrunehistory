# pyrunehistory

[![PyPI version](https://badge.fury.io/py/pyrunehistory.svg)](https://badge.fury.io/py/pyrunehistory)
[![Build Status](https://travis-ci.org/jmwri/pyrunehistory.svg?branch=master)](https://travis-ci.org/jmwri/pyrunehistory)
[![Test Coverage](https://api.codeclimate.com/v1/badges/9aa891c23deb437b1616/test_coverage)](https://codeclimate.com/github/jmwri/pyrunehistory/test_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/9aa891c23deb437b1616/maintainability)](https://codeclimate.com/github/jmwri/pyrunehistory/maintainability)

RuneHistory API client.

# Usage
## Client
```
from pyrunehistory.client import Client
rh = Client()
```

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `host` | `str` | `http://api.runehistory.com` | API host that the client will use. You will not need this unless you are working locally. |
| `version` | `int` | `1` | The API version that the client will use. You will not need this unless you are working locally. |

## Accounts
### Get accounts
```
from pyrunehistory.client import Client
rh = Client()
accounts = rh.accounts.get_accounts()
```

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `runs_unchanged_min` | `int` | `None` | The minimum amount of times an account has been updated without experience changing. |
| `runs_unchanged_max` | `int` | `None` | The maximum amount of times an account has been updated without experience changing. |
| `last_ran_before` | `datetime` | `None` | Only show accounts that were last checked before this time. |
| `prioritise` | `bool` | `True` | Prioritise the order of return accounts to return accounts to be reported on first. |

### Get account
```
from pyrunehistory.client import Client
rh = Client()
accounts = rh.accounts.get_account('nickname')
```

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `slug` | `str` | *N/A* | The slug of the account to fetch. |

### Create account
```
from pyrunehistory.client import Client
rh = Client()
accounts = rh.accounts.create_account('Nickname')
```

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `nickname` | `str` | *N/A* | The nickname of the account to create. |

### Update account
```
from pyrunehistory.client import Client
rh = Client()
accounts = rh.accounts.update_account('old-nickname', 'New Nickname')
```

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `slug` | `str` | *N/A* | The slug of the account to update. |
| `nickname` | `str` | *N/A* | The new nickname of the account. |

## Highscores
All highscores are associated with an account, and you must define the account slug when accessing highscores.
```
from pyrunehistory.client import Client
rh = Client()
accounts = rh.accounts.highscores('nickname')
```

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `slug` | `str` | *N/A* | The slug of the account to perform highscore operations on. |

### Get highscores
```
from pyrunehistory.client import Client
rh = Client()
accounts = rh.accounts.highscores('nickname').get_highscores()
```

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `created_after` | `datetime` | `None` | Only show highscores created on or after this date. |
| `created_before` | `datetime` | `None` | Only show highscores created before this date. |
| `skills` | `list[str]` | `None` | Only retrieve the skills provided in this list. |

### Get highscore
```
from pyrunehistory.client import Client
rh = Client()
accounts = rh.accounts.highscores('nickname').get_highscore('5a9d8e6b95f5e704af4e3d39')
```

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | *N/A* | The ID of the highscore to fetch. |

### Create highscore
The following example will create all skills with the same values to save on space in the example.
```
from pyrunehistory.client import Client
from pyrunehistory.domain.models.highscore import SKILLS, Skill
rh = Client()
skills = {}
for skill in SKILLS:
    skills[skill] = Skill(1, 99, 999999999)
accounts = rh.accounts.highscores('nickname').create_highscore(skills)
```

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `skills` | `dict[str, Skill]` | *N/A* | A dictionary of `Skill` objects that contain the data to build a highscore. |

There is a helper function to create the `Skill` objects for you that takes dictionaries instead.

```
from pyrunehistory.client import Client
from pyrunehistory.domain.models.highscore import SKILLS, to_skills
rh = Client()
skills = {}
for skill in SKILLS:
    skills[skill] = {'rank': 1, 'level': 99, 'experience': 999999999}
skill_objects = to_skills(skills)
accounts = rh.accounts.highscores('nickname').create_highscore(skill_objects)
```

# Running tests
## Install the package with test dependencies
`pip install -e ".[test]"`

## Run tox
`tox`