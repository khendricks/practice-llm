# Test-driven development

- For every behavior change, write a failing test before writing the
  implementation that makes it pass. Run it to confirm it fails for the
  expected reason, then write the minimum code to pass it.
- Work in small red-green-refactor cycles: one failing test, one passing
  implementation, then refactor with tests green throughout.
- Do not write implementation code that has no failing test driving it.
  Exceptions: pure typed data holders with no behavior (e.g. a dataclass with
  no validators), project scaffolding, and config/dependency wiring.
- Refactors that preserve behavior do not need new tests, but must not reduce
  existing coverage; run the full suite before and after.
- This complements, not replaces, [quality.md](quality.md)'s bar of running
  `ruff`, `mypy`, and `pytest` before considering work complete.
