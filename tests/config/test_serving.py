from pathlib import Path

import pytest
from pydantic import ValidationError

from practice_llm.config.serving import ServingConfig


def _valid_kwargs() -> dict[str, object]:
    return {"checkpoint_path": Path("checkpoints/model.pt"), "device": "cpu"}


def test_serving_config_accepts_valid_fields() -> None:
    config = ServingConfig(**_valid_kwargs())

    assert config.checkpoint_path == Path("checkpoints/model.pt")
    assert config.device == "cpu"


def test_serving_config_defaults_host_and_port() -> None:
    config = ServingConfig(**_valid_kwargs())

    assert config.host == "0.0.0.0"
    assert config.port == 8000


@pytest.mark.parametrize("port", [0, -1, 65536])
def test_serving_config_rejects_port_outside_valid_range(port: int) -> None:
    kwargs = _valid_kwargs()
    kwargs["port"] = port

    with pytest.raises(ValidationError):
        ServingConfig(**kwargs)


def test_serving_config_rejects_invalid_device() -> None:
    kwargs = _valid_kwargs()
    kwargs["device"] = "tpu"

    with pytest.raises(ValidationError):
        ServingConfig(**kwargs)


def test_serving_config_is_frozen() -> None:
    config = ServingConfig(**_valid_kwargs())

    with pytest.raises(ValidationError):
        config.port = 9000  # type: ignore[misc]
