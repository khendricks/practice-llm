from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator

from practice_llm.config.data import DataConfig
from practice_llm.config.model import ModelConfig


class TrainingConfig(BaseModel):
    """Optimization and checkpointing settings for a training run."""

    model_config = ConfigDict(frozen=True)

    seed: int
    batch_size: int = Field(gt=0)
    learning_rate: float = Field(gt=0.0)
    weight_decay: float = Field(default=0.0, ge=0.0)
    max_steps: int = Field(gt=0)
    warmup_steps: int = Field(ge=0)
    grad_clip_norm: float = Field(gt=0.0)
    eval_interval: int = Field(gt=0)
    checkpoint_interval: int = Field(gt=0)
    checkpoint_dir: Path
    device: Literal["cpu", "cuda"]

    @model_validator(mode="after")
    def _check_warmup_steps_within_max_steps(self) -> "TrainingConfig":
        if self.warmup_steps > self.max_steps:
            raise ValueError("warmup_steps must not exceed max_steps")
        return self


class TrainingRunConfig(BaseModel):
    """Full configuration needed to reproduce a training run."""

    model_config = ConfigDict(frozen=True)

    data: DataConfig
    model: ModelConfig
    training: TrainingConfig
