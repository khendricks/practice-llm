from pathlib import Path

from practice_llm.config.data import DataConfig
from practice_llm.config.model import ModelConfig
from practice_llm.config.training import TrainingConfig, TrainingRunConfig


def test_training_run_config_composes_sub_configs() -> None:
    data = DataConfig(corpus_path=Path("corpus.txt"), seed=0)
    model = ModelConfig(
        vocab_size=256,
        hidden_size=64,
        n_heads=4,
        n_layers=2,
        seq_len=128,
        intermediate_size=256,
    )
    training = TrainingConfig(
        seed=0,
        batch_size=32,
        learning_rate=3e-4,
        max_steps=1000,
        warmup_steps=100,
        grad_clip_norm=1.0,
        eval_interval=100,
        checkpoint_interval=500,
        checkpoint_dir=Path("checkpoints"),
        device="cpu",
    )

    run_config = TrainingRunConfig(data=data, model=model, training=training)

    assert run_config.data is data
    assert run_config.model is model
    assert run_config.training is training
