# Architecture boundaries

- Keep HTTP concerns in `src/practice_llm/api/`; keep model, data, and training
  code out of that package and free of FastAPI imports.
- Model code must not import the API layer. Dependencies flow one way:
  `api` -> `chat`/`sampling` -> `model`/`tokenizer`. Never the reverse.
- Put data loading/corpus handling, model/architecture code, training loops,
  and serving code in separate modules under `src/practice_llm/`.
- Use typed configuration objects (e.g. dataclasses or pydantic models) for
  data, model, training, and serving settings once they are introduced.
  Do not add module-level runtime constants for anything configurable.
- Generated corpora and checkpoints are build artifacts: keep them out of
  version control (see `.gitignore`) and never hardcode local paths to them.
- Before introducing a new top-level module or crossing an existing package
  boundary, use the `architecture-reviewer` subagent to sanity-check the
  design against these boundaries.
