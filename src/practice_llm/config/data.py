from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field


class DataConfig(BaseModel):
    """Settings for loading a text corpus and splitting it for training."""

    model_config = ConfigDict(frozen=True)

    corpus_path: Path
    val_fraction: float = Field(default=0.1, gt=0.0, lt=1.0)
    seed: int
