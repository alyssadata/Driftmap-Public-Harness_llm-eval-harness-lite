# Run Log Schema (Driftmap Public)

Purpose: standardize what to record every time a suite is run so comparisons are reproducible.

A run log is not the model output itself. It is the metadata and file references that allow a run to be reproduced and compared.

## Required fields (minimum)
- run_id: unique run identifier
- run_utc: timestamp in UTC
- model: model name + version (as available)
- runtime: where it ran (LM Studio, Ollama, OpenAI API, etc.)
- suite_id: which suite was used
- suite_file: path or filename
- settings: temperature, top_p, max_tokens (if applicable)
- scorer: which rubric/scoring method was used
- output_file: results CSV filename
- notes_file: run notes filename (if used)
- receipts: hashes for suite file and output file (SHA-256 recommended)

## Suggested structure (example)
- Suite inputs live in `prompts/`
- Outputs live in `results/`
- Notes live in `sample_results/` (or a dedicated `run_notes/` folder)
- Receipts can be stored as:
  - a `.sha256` file next to the output CSV, or
  - a single append-only receipt log

## Why receipts matter
If an output CSV is edited after the run, the hash changes.
Hashes are the integrity layer that makes drift comparisons trustworthy.
