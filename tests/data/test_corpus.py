from pathlib import Path

import pytest

from practice_llm.config.data import DataConfig
from practice_llm.data.corpus import (
    CorpusNotFoundError,
    CorpusService,
    EmptyCorpusError,
)


def _config(tmp_path: Path, *, val_fraction: float = 0.5, seed: int = 0) -> DataConfig:
    return DataConfig(
        corpus_path=tmp_path / "corpus.txt", val_fraction=val_fraction, seed=seed
    )


def test_load_reads_configured_path(tmp_path: Path) -> None:
    corpus_path = tmp_path / "corpus.txt"
    corpus_path.write_text("line one\nline two\n", encoding="utf-8")
    service = CorpusService(_config(tmp_path))

    text = service.load()

    assert text == "line one\nline two\n"


def test_load_raises_for_missing_path(tmp_path: Path) -> None:
    service = CorpusService(_config(tmp_path))

    with pytest.raises(CorpusNotFoundError):
        service.load()


def test_split_is_deterministic_for_seed(tmp_path: Path) -> None:
    text = "\n".join(f"line {i}" for i in range(20))
    service_a = CorpusService(_config(tmp_path, seed=42))
    service_b = CorpusService(_config(tmp_path, seed=42))

    split_a = service_a.split(text)
    split_b = service_b.split(text)

    assert split_a == split_b


def test_split_differs_across_seeds(tmp_path: Path) -> None:
    text = "\n".join(f"line {i}" for i in range(20))
    service_a = CorpusService(_config(tmp_path, seed=1))
    service_b = CorpusService(_config(tmp_path, seed=2))

    split_a = service_a.split(text)
    split_b = service_b.split(text)

    assert split_a != split_b


def test_split_respects_val_fraction(tmp_path: Path) -> None:
    text = "\n".join(f"line {i}" for i in range(10))
    service = CorpusService(_config(tmp_path, val_fraction=0.2, seed=0))

    split = service.split(text)

    assert len(split.val_text.splitlines()) == 2
    assert len(split.train_text.splitlines()) == 8


def test_split_raises_for_empty_text(tmp_path: Path) -> None:
    service = CorpusService(_config(tmp_path))

    with pytest.raises(EmptyCorpusError):
        service.split("   \n\n  ")


def test_load_and_split_wires_load_and_split_together(tmp_path: Path) -> None:
    corpus_path = tmp_path / "corpus.txt"
    corpus_path.write_text(
        "\n".join(f"line {i}" for i in range(10)), encoding="utf-8"
    )
    service = CorpusService(_config(tmp_path, val_fraction=0.2, seed=0))

    split = service.load_and_split()

    assert len(split.val_text.splitlines()) == 2
    assert len(split.train_text.splitlines()) == 8
