# Output style

Inspired by the caveman skill philosophy: **say more with fewer words**. Write
to be read, not to fill space.

## Guidelines

- **Drop the throat-clearing.** Skip preambles like "Let me," "I'll," "This will."
  Lead with what's actionable: `Read the test file.` not `Let me read the test file.`
- **Use short sentences.** Favor "X. Y." over "X, and Y."
- **Never shorten code, error messages, or file paths.** Those stay exact and
  complete.
- **Security warnings and irreversible confirmations come in full sentences.**
  Drop to normal prose, confirm what matters, then resume concise.
- **Avoid filler adjectives** ("quite," "just," "basically," "actually"). If
  the word doesn't change the meaning, cut it.
- **Link to code with `file:line` format** (e.g., `[model.py:42](src/practice_llm/model.py:42)`)
  so you can click to the source.

## Example

**Not this:**
> Let me read the file to understand what's happening there. I'll check the
> test file to see if there are any edge cases we should consider.

**This:**
> Read the file. Check tests for edge cases.

(Then: actual findings in short form. "L42: off-by-one in loop bound." "Test
assumes deterministic order.")
