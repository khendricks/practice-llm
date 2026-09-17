# practice-llm

`practice-llm` is a learning-focused Python project that builds a small
decoder-only language model from scratch and exposes it through a FastAPI chat
application. The implementation prioritizes readable components and
reproducible experiments over production-scale performance.

## Current status

The project foundation is in place: packaging, automated quality checks, Codex
collaboration guidance, and a small FastAPI health endpoint. Model training,
generation, and the chat UI will be added in the tracked GitHub issues.

## Setup

Use Python 3.11 or newer. Create an isolated virtual environment and install
the project with its development tools:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

## Run the API

```bash
python -m uvicorn practice_llm.api.main:app --reload
```

Open <http://127.0.0.1:8000/health> to confirm the server is ready.

## Quality checks

```bash
python -m ruff check .
python -m mypy src
python -m pytest
```

## Data plan

The first training corpus will be Tiny Shakespeare, a small public text corpus
that supports fast iteration. Corpus downloads, deterministic train-validation
splitting, provenance, and checksums will be implemented in the data issue;
generated data and checkpoints are intentionally ignored by Git.

## AI collaboration

Read [`AGENTS.md`](AGENTS.md) before contributing. Repository-specific Codex
skills live in [`.agents/skills`](.agents/skills): `python-quality` applies the
quality workflow, and `llm-experiment` records reproducibility requirements.
