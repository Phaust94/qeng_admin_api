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
    game_metadata
    levels: typing.List[Level] = Field(default_factory=list)

    class Config:
        use_enum_values = True
        fields = {
            "game_metadata": "game",
            "levels": "tasks",
        }
        allow_population_by_field_name = True
