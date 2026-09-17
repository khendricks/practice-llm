# Change discipline

- Keep commits scoped to one issue or a closely related fix; do not bundle
  unrelated cleanup into a behavior-change commit.
- Update the README when setup, commands, or user-visible behavior changes.
- Only create commits when the user explicitly asks for one, and never amend
  a commit that has already been pushed.
- Do not use `--no-verify`, force-push, or skip hooks unless the user
  explicitly asks for it.
