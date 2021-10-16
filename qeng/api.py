"""
QEng API
"""
import json

import requests
from requests.cookies import RequestsCookieJar
from dataclasses import dataclass

from qeng.game import Level, Game

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
        succ = res.json()
        assert "login_error" not in succ, f"Invalid login/password: {succ['login_error']!r}"
        cookies = res.cookies
        self._cookies = cookies
        return None

    def _base_upload_level(self, level: Level, game_id: int) -> None:
        endpoint = "import_tasks.php"

        level_json = level.json(exclude_none=True, by_alias=True, exclude_unset=True)
        level_json = json.loads(level_json)

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
        succ = upload_res.json()
        assert succ.get("success"), f"Failed to upload JSON because of {succ.get('error')!r}"
        return None

    def upload_level(self, level: Level, game_id: int) -> None:
        assert level.level_metadata.level_order_number is None, "Can't upload NEW level with level nuber specified"
        return self._base_upload_level(level, game_id)

    def update_level(self, level: Level, game_id: int) -> None:
        """
        If bonuses, hints or sectors are present - these will be completely overwritten.
        For level metadata - only the ones passed, will be updated, the rest will stay as they were
        :param level: Level class
        :param game_id: id of the game
        :return: None
        """
        assert level.level_metadata.level_order_number is not None, "Can't update level without level number specified"
        return self._base_upload_level(level, game_id)

    def get_game(self, game_id: int) -> Game:
        endpoint = "game_export.php"

        res = requests.get(
            f"{self.domain_url}/{endpoint}",
            params={
                "gid": game_id,
                "json": 1,
            },
            cookies=self._cookies,
        )
        res.raise_for_status()
        game_json = res.json()
        game_inst = Game.parse_obj(game_json)
        return game_inst

    def upload_game(self, game: Game, game_id: int, delete_existing_levels: bool = True) -> None:
        endpoint = "import_tasks.php"

        game_json = game.json(exclude_none=True, by_alias=True, exclude_unset=True)
        game_json = json.loads(game_json)

        params = {
            "gid": game_id,
            "json": 1,
        }

        if delete_existing_levels:
            game_json["delete_all_tasks"] = 1

        res = requests.post(
            f"{self.domain_url}/{endpoint}",
            params=params,
            json=game_json,
            cookies=self._cookies,
        )
        res.raise_for_status()
        return None


