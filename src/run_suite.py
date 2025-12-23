#!/usr/bin/env python3
"""
LM Studio eval runner (lite)

Reads a prompt suite CSV (test_id, prompt, ...),
calls LM Studio's OpenAI-compatible API,
writes a results CSV (test_id, output).

Safe + simple: no scoring, just reproducible runs.
"""

import argparse
import csv
import os
import sys
from datetime import datetime
from typing import Dict, List

import requests


def read_suite(path: str) -> List[Dict[str, str]]:
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    if not rows:
        raise ValueError(f"Suite CSV is empty: {path}")
    if "test_id" not in rows[0] or "prompt" not in rows[0]:
        raise ValueError("Suite CSV must include columns: test_id, prompt")
    return rows


def call_lmstudio(
    base_url: str,
    model: str,
    prompt: str,
    system: str = "",
    temperature: float = 0.8,
    top_p: float = 0.95,
) -> str:
    url = base_url.rstrip("/") + "/chat/completions"
    headers = {"Content-Type": "application/json"}

    messages = []
    if system.strip():
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "top_p": top_p,
    }

    r = requests.post(url, headers=headers, json=payload, timeout=180)
    r.raise_for_status()
    data = r.json()

    # OpenAI-compatible response shape
    return data["choices"][0]["message"]["content"]


def write_results(path: str, rows: List[Dict[str, str]]) -> None:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["test_id", "output"])
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--suite", required=True, help="Path to suite CSV (e.g., prompts/suite_refusal_basic.csv)")
    ap.add_argument("--out", default="", help="Output CSV path (default: sample_results/run_<timestamp>.csv)")
    ap.add_argument("--base-url", default=os.getenv("LMSTUDIO_BASE_URL", "http://localhost:1234/v1"),
                    help="LM Studio server base URL (default: http://localhost:1234/v1)")
    ap.add_argument("--model", default=os.getenv("LMSTUDIO_MODEL", "qwen2.5-32b-instruct"),
                    help="Model name exposed by LM Studio")
    ap.add_argument("--system", default=os.getenv("LMSTUDIO_SYSTEM", ""),
                    help="Optional system message (leave blank to match your 'Blank Model' runs)")
    ap.add_argument("--temperature", type=float, default=0.8)
    ap.add_argument("--top-p", type=float, default=0.95)
    args = ap.parse_args()

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_path = args.out.strip() or f"sample_results/run_{ts}.csv"

    suite_rows = read_suite(args.suite)

    results = []
    for row in suite_rows:
        test_id = row["test_id"].strip()
        prompt = row["prompt"].strip()

        print(f"Running {test_id}...", flush=True)
        output = call_lmstudio(
            base_url=args.base_url,
            model=args.model,
            prompt=prompt,
            system=args.system,
            temperature=args.temperature,
            top_p=args.top_p,
        )
        results.append({"test_id": test_id, "output": output})

    write_results(out_path, results)
    print(f"\nDone. Wrote: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
