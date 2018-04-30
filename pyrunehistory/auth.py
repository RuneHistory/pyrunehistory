from requests.auth import HTTPBasicAuth, AuthBase
from requests.models import PreparedRequest

from simplejwt import Jwt


class JwtAuth(AuthBase):
    def __init__(self, token: str):
        self.token = token

    def __call__(self, r: PreparedRequest):
        r.headers.update({'Authorization': 'Bearer {}'.format(self.token)})
        return r


class Auth:
    def __init__(self, client: 'pyrunehistory.client.Client', username: str,
                 password: str, secret: str):
        self.client = client
        self.username = username
        self.password = password
        self.secret = secret
        self.jwt = None  # type: Jwt
        self._token = None  # type: str

    @property
    def token(self) -> str:
        if not self.jwt or not self.jwt.valid():
            self.refresh()
        return self._token

    def refresh(self):
        response = self.client(
            'GET',
            'auth/token',
            auth='basic'
        )
        self.jwt = Jwt.decode(self.secret, response.get('token'))
        self._token = response.get('token')

    def get(self, auth_type: str) -> AuthBase:
        if auth_type == 'basic':
            return HTTPBasicAuth(self.username, self.password)
        if auth_type == 'jwt':
            return JwtAuth(self.token)
        raise ValueError('Invalid authentication type: {}'.format(auth_type))
