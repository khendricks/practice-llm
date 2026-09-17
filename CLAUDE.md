# CLAUDE.md

Guidance for Claude Code when working in this repository. This is the
Claude-specific counterpart to [`AGENTS.md`](AGENTS.md); keep the two in sync
when project-wide decisions change.

## Project purpose

`practice-llm` is a small, learning-focused decoder-only LLM built with
PyTorch and served through FastAPI. Favor readable, explicit implementations
over clever optimizations; explain non-obvious model math close to the code.

## Rules

@.claude/rules/architecture.md
@.claude/rules/quality.md
@.claude/rules/experiments.md
@.claude/rules/git.md

## Subagents

- `architecture-reviewer` (`.claude/agents/architecture-reviewer.md`): use
  before adding a new top-level module, changing a package boundary, or
  designing a new component (data pipeline, model, training loop, API
  surface). It reviews or proposes designs against this project's
  architecture rules; it does not write code.

## Where to look next

- Repository-specific Codex skills live in [`.agents/skills/`](.agents/skills)
  and describe the same workflows in Codex's format.
- Add guidance here (or to `.claude/rules/`) only for recurring,
  project-wide decisions. One-off task instructions belong in the
  conversation, not in these files.
