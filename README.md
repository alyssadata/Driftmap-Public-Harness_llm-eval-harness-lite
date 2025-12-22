# llm-eval-harness-lite
Lightweight, public-safe LLM evaluation harness starter kit: CSV prompt suites + run logs for refusal, boundary integrity, uncertainty, and drift tracking.

## License
- Code: MIT (see `LICENSE.md`)
- Documentation + prompt suites (CSV): CC BY-ND 4.0 (as noted in `LICENSE.md`)

## How to run (manual, no code)
1) Open `prompts/suite_refusal_basic.csv`
2) Copy each prompt into LM Studio (or AnythingLLM if testing with documents)
3) Paste outputs into `results/results_refusal_basic_template.csv`
4) Score using `docs/rubric_refusal_basic.md`
5) Save as a new file: `results/results_refusal_basic_<date>.csv`

## Quickstart (No code)
1) Open a prompt suite in `prompts/`
2) Run each prompt in LM Studio (or another model UI)
3) Paste outputs into a copy of the matching file in `results/`
4) Score each row using `docs/scoring_rubric.md`

## Repository structure
- `prompts/` = public-safe CSV prompt suites
- `results/` = results templates and sample logs
- `docs/` = rubric + methodology notes

## Privacy boundary
This repository contains only generic, public-safe test suites and templates.
Private suites, signature phrasing, and private outputs are intentionally excluded.


