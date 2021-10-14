"""
Models a QEng game
"""

from pydantic import BaseModel, Field
import typing

from qeng.game.level import Level

__all__ = [
    "Game",
]


class Game(BaseModel):
    game_id: int
    levels: typing.List[Level] = Field(default_factory=list)
