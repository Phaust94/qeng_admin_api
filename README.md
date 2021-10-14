This library allows interacting with QEng admin API

The usage is simple:

```python
from qeng.game import Level, LevelSector, LevelMetadata
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
)

GAME_ID = 80
api = QengAPI("LOGIN", 'PASSWORD')
api.upload_level(level, GAME_ID)
```