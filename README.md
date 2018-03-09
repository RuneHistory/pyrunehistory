# pyrunehistory

RuneHistory API client

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

# Running tests
## Install the package with test dependencies
`pip install -e ".[test]"`

## Run tox
`tox`