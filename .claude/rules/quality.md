# Quality bar

- Before considering any change complete, run all three:
  ```bash
  python -m ruff check .
  python -m mypy src
  python -m pytest
  ```
- Add or update focused tests with every behavior change; prefer deterministic
  fixtures over ones that depend on wall-clock time, network access, or
  unseeded randomness.
- Keep functions small and single-purpose. Type all public interfaces
  (`mypy` runs in strict mode — see `pyproject.toml`).
- Use descriptive names over comments; only comment non-obvious model math or
  a workaround for a specific constraint.
- Preserve deterministic behavior wherever a seed is configured — do not add
  code paths that silently reintroduce nondeterminism.
- Do not add error handling, fallbacks, or config flags for situations that
  cannot occur in this codebase.
