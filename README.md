# pyrunehistory

RuneHistory API client

## Usage
### Client
```
from pyrunehistory.client import Client
rh = Client()
```

#### Arguments
---
Name: host
Type: `str`
Default: `http://api.runehistory.com`
Description: API host that the client will use. You will not need this unless you are working locally. 

Name: version
Type: `int`
Default: `1`
Description: The API version that the client will use. You will not need this unless you are working locally.
---

### Accounts
#### Get accounts
```
from pyrunehistory.client import Client
rh = Client()
accounts = rh.accounts.get_accounts()
```
##### Arguments
---
Name: runs_unchanged_min
Type: `int`
Default: `None`
Description: The minimum amount of times an account has been updated without experience changing.

Name: runs_unchanged_max
Type: `int`
Default: `None`
Description: The maximum amount of times an account has been updated without experience changing.

Name: last_ran_before
Type: `datetime`
Default: `None`
Description: Only show accounts that were last checked before this time.

Name: prioritise
Type: `bool`
Default: `True`
Description: Prioritise the order of return accounts to return accounts to be reported on first.
---

## Running tests
### Install the package with test dependencies
`pip install -e ".[test]"`

### Run tox
`tox`