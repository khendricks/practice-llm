# practice-llm contributor guidance

## Project purpose

This repository is a small, learning-focused decoder-only LLM built with PyTorch
and served through FastAPI. Favor readable, explicit implementations over clever
optimizations; explain non-obvious model math close to the code.

## Architecture boundaries

- Keep HTTP concerns in `src/practice_llm/api/` and model/training code outside it.
- Keep data, model, training, and serving settings in typed configuration objects
  once they are introduced; do not add module-level runtime constants.
- Do not couple training code to FastAPI or import the web layer from model code.
- Store generated corpora and checkpoints outside version control.

## Quality bar

- Add or update focused tests with every behavior change.
- Run `python -m pytest`, `python -m ruff check .`, and `python -m mypy src`
  before considering work complete.
- Keep functions small, type public interfaces, and use descriptive names.
- Preserve deterministic behavior where a seed is configured.

## Change discipline

- Keep commits scoped to one issue or a closely related fix.
- Update the README when setup, commands, or user-visible behavior changes.
- Add guidance here only for recurring project-wide decisions; put specialized,
  reusable procedures in `.agents/skills/` instead.
