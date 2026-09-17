# Experiment reproducibility

Applies to corpus processing, tokenization, model training, evaluation,
sampling, and checkpoints.

- Record the data source, dataset version or checksum, configuration, seed,
  and code revision for every run that produces a checkpoint or reported
  metric.
- Keep raw data, tokenized data, metrics output, and checkpoints out of Git.
- Use an explicit train/validation split; evaluate without mutating model
  state (no gradient updates, no dropout/train-mode side effects).
- Save checkpoints with enough metadata (config, tokenizer version, step) to
  reproducibly reload and generate from them later.
- Compare new results against a small baseline and document limitations
  instead of claiming model quality from a single run.
