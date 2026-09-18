import pytest
from pydantic import ValidationError

from practice_llm.config.model import ModelConfig


def _valid_kwargs() -> dict[str, int | float]:
    return {
        "vocab_size": 256,
        "hidden_size": 64,
        "n_heads": 4,
        "n_layers": 2,
        "seq_len": 128,
        "intermediate_size": 256,
    }


def test_model_config_accepts_valid_fields() -> None:
    config = ModelConfig(**_valid_kwargs())

    assert config.vocab_size == 256
    assert config.hidden_size == 64
    assert config.n_heads == 4
    assert config.n_layers == 2
    assert config.seq_len == 128
    assert config.intermediate_size == 256


def test_model_config_defaults() -> None:
    config = ModelConfig(**_valid_kwargs())

    assert config.rope_theta == 10000.0
    assert config.rms_norm_eps == 1e-5
    assert config.dropout == 0.0


@pytest.mark.parametrize(
    "field",
    [
        "vocab_size",
        "hidden_size",
        "n_heads",
        "n_layers",
        "seq_len",
        "intermediate_size",
    ],
)
def test_model_config_rejects_non_positive_dims(field: str) -> None:
    kwargs = _valid_kwargs()
    kwargs[field] = 0

    with pytest.raises(ValidationError):
        ModelConfig(**kwargs)


def test_model_config_rejects_hidden_size_not_divisible_by_n_heads() -> None:
    kwargs = _valid_kwargs()
    kwargs["hidden_size"] = 65
    kwargs["n_heads"] = 4

    with pytest.raises(ValidationError):
        ModelConfig(**kwargs)


def test_model_config_is_frozen() -> None:
    config = ModelConfig(**_valid_kwargs())

    with pytest.raises(ValidationError):
        config.hidden_size = 128  # type: ignore[misc]
