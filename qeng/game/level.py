"""
Models a QEng level
"""
import typing
from pydantic import BaseModel, Field

from qeng.game.level_metadata import LevelMetadata
from qeng.game.level_sector import LevelSector

__all__ = [
    "Level"
]


class Level(BaseModel):
    level_metadata: LevelMetadata
    sectors: typing.List[LevelSector] = Field(default_factory=list)

    class Config:
        allow_population_by_field_name = True
        fields = {"level_metadata": "task", "sectors": "codes"}
    # TODO: hints, bonues
