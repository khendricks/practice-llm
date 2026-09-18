from pathlib import Path

import pytest
from pydantic import ValidationError

from practice_llm.config.training import TrainingConfig


def _valid_kwargs() -> dict[str, object]:
    return {
        "seed": 0,
        "batch_size": 32,
        "learning_rate": 3e-4,
        "max_steps": 1000,
        "warmup_steps": 100,
        "grad_clip_norm": 1.0,
        "eval_interval": 100,
        "checkpoint_interval": 500,
        "checkpoint_dir": Path("checkpoints"),
        "device": "cpu",
    }


def test_training_config_accepts_valid_fields() -> None:
    config = TrainingConfig(**_valid_kwargs())

    assert config.seed == 0
    assert config.batch_size == 32
    assert config.learning_rate == 3e-4
    assert config.max_steps == 1000
    assert config.warmup_steps == 100
    assert config.device == "cpu"


def test_training_config_defaults_weight_decay() -> None:
    config = TrainingConfig(**_valid_kwargs())

    assert config.weight_decay == 0.0


@pytest.mark.parametrize(
    "field",
    [
        "batch_size",
        "learning_rate",
        "max_steps",
        "grad_clip_norm",
        "eval_interval",
        "checkpoint_interval",
    ],
)
def test_training_config_rejects_non_positive_fields(field: str) -> None:
    kwargs = _valid_kwargs()
    kwargs[field] = 0

    with pytest.raises(ValidationError):
        TrainingConfig(**kwargs)


def test_training_config_rejects_warmup_steps_exceeding_max_steps() -> None:
    kwargs = _valid_kwargs()
    kwargs["max_steps"] = 100
    kwargs["warmup_steps"] = 200

    with pytest.raises(ValidationError):
        TrainingConfig(**kwargs)


def test_training_config_rejects_invalid_device() -> None:
    kwargs = _valid_kwargs()
    kwargs["device"] = "tpu"

    with pytest.raises(ValidationError):
        TrainingConfig(**kwargs)


def test_training_config_is_frozen() -> None:
    config = TrainingConfig(**_valid_kwargs())

    with pytest.raises(ValidationError):
        config.seed = 1  # type: ignore[misc]
