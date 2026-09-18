import random
from dataclasses import dataclass

from practice_llm.config.data import DataConfig


class CorpusNotFoundError(FileNotFoundError):
    """Raised when a configured corpus path does not exist."""


class EmptyCorpusError(ValueError):
    """Raised when a corpus has no non-empty lines to split."""


@dataclass(frozen=True)
class CorpusSplit:
    train_text: str
    val_text: str


class CorpusService:
    """Loads a text corpus and splits it deterministically for training."""

    def __init__(self, config: DataConfig) -> None:
        self._config = config

    def load(self) -> str:
        if not self._config.corpus_path.is_file():
            raise CorpusNotFoundError(
                f"Corpus path not found: {self._config.corpus_path}"
            )
        return self._config.corpus_path.read_text(encoding="utf-8")

    def split(self, text: str) -> CorpusSplit:
        lines = [line for line in text.splitlines() if line.strip()]
        if not lines:
            raise EmptyCorpusError("Corpus has no non-empty lines to split.")

        shuffled = lines.copy()
        random.Random(self._config.seed).shuffle(shuffled)

        val_count = max(1, round(len(shuffled) * self._config.val_fraction))
        val_lines = shuffled[:val_count]
        train_lines = shuffled[val_count:]

        return CorpusSplit(
            train_text="\n".join(train_lines), val_text="\n".join(val_lines)
        )

    def load_and_split(self) -> CorpusSplit:
        return self.split(self.load())
