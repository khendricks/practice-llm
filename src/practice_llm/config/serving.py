from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class ServingConfig(BaseModel):
    """Transport and checkpoint settings for the FastAPI server."""

    model_config = ConfigDict(frozen=True)

    host: str = "0.0.0.0"
    port: int = Field(default=8000, gt=0, le=65535)
    checkpoint_path: Path
    device: Literal["cpu", "cuda"]
