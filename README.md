[![Lines Of Code](https://tokei.rs/b1/github/Phaust94/qeng_admin_api?category=code)](https://github.com/Phaust94/qeng_admin_api)

This library allows interacting with QEng admin API

The usage is simple.

For uploading NEW levels:
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

For updating EXISTING levels:

A level has to have a `level_order_number` parameter set on LevelMetadata.
If bonuses, hints or sectors are present - these will be completely overwritten.
For level metadata - only the ones passed, will be updated, the rest will stay as they were

```python
from qeng.game import Level, LevelSector, LevelMetadata, Hint, Bonus
from qeng import QengAPI

level = Level(
    level_metadata=LevelMetadata(
        level_order_number=10,
        task_text="QGJHGJHSGDJHS",
    ),
    sectors=[
    ],
    hints=[
        Hint(description="test_hint2", text="Look at me go", penalty=3)
    ],
    bonuses=[
        Bonus(
            answers=["a", "b"],
            delay_appearance_seconds=10,
            text_after_solved="this is after"
        )
    ]
)

GAME_ID = 80
api = QengAPI("USER", 'PASSWORD')
api.update_level(level, GAME_ID)
```