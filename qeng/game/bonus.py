"""
Models a QEng bonus
"""

from pydantic import BaseModel, Field
import typing

__all__ = [
    "Bonus",
]


class Bonus(BaseModel):
    number: int = None
    answers: typing.Union[str, typing.List[str]] = Field(default_factory=list)
    delay_appearance_seconds: int = None
    availability_duration_seconds: int = None
    bonus_amount: int = 0
    time_left_conversion_coefficient: float = None
    description: str = None
    text_after_solved: str = None

    class Config:
        fields = {
            "answers": "code",
            "delay_appearance_seconds": "delay",
            "availability_duration_seconds": "duration",
            "bonus_amount": "time",
            "time_left_conversion_coefficient": "duration_k",
            "text_after_solved": "hint",
        }
        allow_population_by_field_name = True
