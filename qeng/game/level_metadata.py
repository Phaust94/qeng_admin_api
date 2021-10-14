"""
Models a QEng level
"""

from dataclasses import dataclass
import typing

__all__ = [
    "LevelMetadata",
]


@dataclass
class LevelMetadata:
    id: int
    number: int
    # Autopass time in seconds
    max_time: int
    # Bonus for not autopass (seconds/points)
    score: int
    # Time multipler in statistics
    time_k: float
    # Internal name
    working_name: str
    # DIsplay name in stats
    name: typing.Optional[str]
    # Entering this code will give a penalty up to autopass time
    surrender_code: str
    # Task text
    task: str
    # Task script
    script: str
    # Answer format
    answer: str
    # N answers allowed
    answers_limit: int
    # N seconds for which limit is applied
    answers_per_time: int
    # If the limit is exceeded, each code will result in penalty of N seconds
    answers_limit_penalty: int
