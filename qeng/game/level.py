"""
Models a QEng level
"""

from dataclasses import dataclass

from qeng.game.level_metadata import LevelMetadata

__all__ = [
    "Level"
]


@dataclass
class Level:
    level_metadata: LevelMetadata
    # TODO: hints, bonues
