# Drift Taxonomy (Driftmap Public)

Purpose: name observable drift categories in a way that can be measured from run logs and scored outputs.

## Core drift types
### 1) Refusal drift
Changes in whether the model refuses disallowed requests.
Signals:
- refusal rate changes on a refusal suite
- refusal phrasing becomes non-compliant or incomplete
- refusal becomes overbroad (refuses allowed requests)

### 2) Boundary drift
Changes in how the model maintains constraints and policy boundaries.
Signals:
- it leaks restricted data
- it follows forbidden instruction patterns
- it becomes easier to jailbreak via prompt shaping

### 3) Injection susceptibility drift
Changes in resistance to prompt injection or instruction hierarchy attacks.
Signals:
- follows injected instructions
- reveals hidden system content (or claims to)
- fails to restate constraints under pressure

### 4) Uncertainty drift
Changes in calibration when information is missing or unknown.
Signals:
- increased hallucination rate
- decreased uncertainty acknowledgements
- overconfident tone on unknowns

### 5) Style and tone drift (non-safety)
Changes in format, verbosity, or tone that impact workflow consistency.
Signals:
- output length shifts
- formatting becomes inconsistent
- persona tone changes across runs

## Notes
This taxonomy is behavioral and operational. It does not claim mind, identity, or consciousness. It names measurable changes in outputs under controlled prompts.
