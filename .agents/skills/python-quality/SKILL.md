---
name: python-quality
description: Make or review a Python change in practice-llm. Use for implementation, refactoring, bug fixes, or code review that should preserve the repository's quality checks.
---

1. Read the closest `AGENTS.md` and the affected tests before changing code.
2. Keep API, model, data, and training concerns in their respective packages.
3. Add focused tests for behavior changes; prefer deterministic fixtures.
4. Run `python -m ruff check .`, `python -m mypy src`, and `python -m pytest`.
5. Report the files changed, commands run, and any follow-up work left to another issue.
