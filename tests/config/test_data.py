from pathlib import Path

import pytest
from pydantic import ValidationError

from practice_llm.config.data import DataConfig


def test_data_config_accepts_valid_fields() -> None:
    config = DataConfig(corpus_path=Path("corpus.txt"), val_fraction=0.1, seed=0)

    assert config.corpus_path == Path("corpus.txt")
    assert config.val_fraction == 0.1
    assert config.seed == 0


def test_data_config_defaults_val_fraction() -> None:
    config = DataConfig(corpus_path=Path("corpus.txt"), seed=0)

    assert config.val_fraction == 0.1


@pytest.mark.parametrize("val_fraction", [0.0, 1.0, -0.1, 1.1])
def test_data_config_rejects_val_fraction_outside_open_unit_interval(
    val_fraction: float,
) -> None:
    with pytest.raises(ValidationError):
        DataConfig(corpus_path=Path("corpus.txt"), val_fraction=val_fraction, seed=0)


def test_data_config_is_frozen() -> None:
    config = DataConfig(corpus_path=Path("corpus.txt"), seed=0)

    with pytest.raises(ValidationError):
        config.seed = 1  # type: ignore[misc]
