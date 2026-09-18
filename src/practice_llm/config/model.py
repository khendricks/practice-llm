from pydantic import BaseModel, ConfigDict, Field, model_validator


class ModelConfig(BaseModel):
    """Architecture settings for the decoder-only transformer."""

    model_config = ConfigDict(frozen=True)

    vocab_size: int = Field(gt=0)
    hidden_size: int = Field(gt=0)
    n_heads: int = Field(gt=0)
    n_layers: int = Field(gt=0)
    seq_len: int = Field(gt=0)
    intermediate_size: int = Field(gt=0)
    rope_theta: float = Field(default=10000.0, gt=0.0)
    rms_norm_eps: float = Field(default=1e-5, gt=0.0)
    dropout: float = Field(default=0.0, ge=0.0, lt=1.0)

    @model_validator(mode="after")
    def _check_hidden_size_divisible_by_heads(self) -> "ModelConfig":
        if self.hidden_size % self.n_heads != 0:
            raise ValueError("hidden_size must be divisible by n_heads")
        return self
