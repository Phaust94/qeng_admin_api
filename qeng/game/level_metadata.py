"""
Models a QEng level
"""

import typing

from pydantic import BaseModel

__all__ = [
    "LevelMetadata",
]


class LevelMetadata(BaseModel):
    level_order_number: int = None
    # Autopass time in seconds
    autopass_time_seconds: int = None
    # Bonus for not autopass (seconds/points)
    bonus_for_not_autopass: int = None
    # Time multipler in statistics
    time_multiplier_in_stats: float = None
    # Internal name
    in_game_name: str = None
    # DIsplay name in stats
    stats_name: typing.Optional[str] = None
    # Entering this code will give a penalty up to autopass time
    surrender_code: str = None
    # Task text
    task_text: str = ""
    # Task script
    task_script: str = None
    # Answer format
    answer_format: str = None
    # N answers allowed
    answers_limit: int = None
    # N seconds for which limit is applied
    answers_limit_duration_seconds: int = None
    # If the limit is exceeded, each code will result in penalty of N seconds
    answers_limit_penalty: int = None

    class Config:
        allow_population_by_field_name = True
        fields = {
            'level_order_number': 'number',
            'autopass_time_seconds': 'max_time',
            "bonus_for_not_autopass": "score",
            "time_multiplier_in_stats": "time_k",
            "in_game_name": "working_name",
            "stats_name": "name",
            "task_text": "task",
            "task_script": "script",
            "answer_format": "answer",
            "answers_limit_duration_seconds": "answers_per_time",
        }

