---
name: llm-experiment
description: Plan, run, or modify a training experiment for practice-llm. Use for corpus processing, tokenization, model training, evaluation, sampling, or checkpoints.
---

1. Record the data source, dataset version or checksum, configuration, seed, and code revision.
2. Keep raw data, tokenized data, metrics, and checkpoints out of Git.
3. Use an explicit train-validation split and evaluate without updating model state.
4. Save checkpoints with enough metadata to reproduce loading and generation.
5. Compare against a small baseline and document limitations instead of claiming model quality from one run.
