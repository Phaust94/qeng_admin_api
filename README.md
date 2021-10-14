This library allows interacting with QEng admin API

The usage is simple:

```python
from qeng.game import Level, LevelSector, LevelMetadata, Bonus, Hint
from qeng import QengAPI

level = Level(
    level_metadata=LevelMetadata(
        in_game_name="Test1",
        task_text="tst1",
        autopass_time_seconds=100,
        bonus_for_not_autopass=10,
        time_multiplier_in_stats=0.3,
        stats_name="Public name",
        surrender_code="surr",
        task_script="alert(1)",
        answer_format="Word dick",
        answers_limit=19,
        answers_limit_duration_seconds=1000,
        answers_limit_penalty=4,
    ),
    sectors=[
        LevelSector(name="Test sec1", codes=["dick", "vag"])
    ],
    hints=[
        Hint(description="test_hint2", text="Look at me go", penalty=3)
    ],
    bonuses=[
        Bonus(
            answers=["a", "b"],
            delay_appearance_seconds=10,
            bonus_amount=30,
            description="this is bonus",
            text_after_solved="this is after"
        )
    ]
)

GAME_ID = 80
api = QengAPI("LOGIN", 'PASSWORD')
api.upload_level(level, GAME_ID)
```