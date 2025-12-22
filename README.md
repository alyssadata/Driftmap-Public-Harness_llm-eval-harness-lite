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


