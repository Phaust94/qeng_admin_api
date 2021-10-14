"""
Models a QEng game
"""

from dataclasses import dataclass
import typing

from qeng.game.level import Level

__all__ = [
    "Game",
]


@dataclass
class Game:
    game_id: int
    levels: typing.List[Level]
