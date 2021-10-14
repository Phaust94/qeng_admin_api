"""
QEng API
"""

import requests
from requests.cookies import RequestsCookieJar
from dataclasses import dataclass

from qeng.game import Level

__all__ = [
    "QengAPI",
]

QENG_URL = 'https://qeng.org'


@dataclass
class QengAPI:
    username: str
    password: str
    domain_url: str = QENG_URL

    _cookies: RequestsCookieJar = None

    def __post_init__(self):
        self.authorize()
        return None

    @property
    def authorized(self) -> bool:
        return self._cookies is not None

    def authorize(self) -> None:
        endpoint = "login.php"
        auth = {'user': self.username, 'pass': self.password}
        res = requests.post(
            f"{self.domain_url}/{endpoint}",
            params={"json": 1},
            data=auth,
        )
        res.raise_for_status()
        assert "login_error" not in res.json(), "Invalid login/password"
        cookies = res.cookies
        self._cookies = cookies
        return None

    def upload_level(self, level: Level, game_id: int) -> None:
        endpoint = "import_tasks.php"
        level_json = level.dict(exclude_none=True, by_alias=True)
        upload_res = requests.post(
            f"{self.domain_url}/{endpoint}",
            params={
                "gid": game_id,
                "json": 1,
            },
            json=[level_json],
            cookies=self._cookies,
        )
        upload_res.raise_for_status()
        return None
