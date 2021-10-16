"""
QEng Game metadata
"""

import enum
import typing

from pydantic import BaseModel, Field

__all__ = [
    "GameScoringType",
    "GameStatisticsState",
]


class GameScoringType(enum.Enum):
    Points = 0
    Time = 1


class GameStatisticsState(enum.Enum):
    AlwaysOpen = 0
    OpenWithoutBonuses = 1
    ClosedDuringGame = 2
    ShortStatsOnly = 4
    AlwaysClosed = 5
    PassedLevelsOnly = 6


class GameMetadata(BaseModel):
    scoring_type: GameScoringType = GameScoringType.Time
    statistics_state: GameStatisticsState = GameStatisticsState.AlwaysClosed
    team_limit: int = 0

    class Config:
        fields = {
            "scoring_type": "type",
            "statistics_state": "stat",
        }
        allow_population_by_field_name = True
        use_enum_values = True
        # arbitrary_types_allowed = True
