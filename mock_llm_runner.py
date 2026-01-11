#!/usr/bin/env python3
"""
Mock LLM driver that replays known envelopes through the validator
to demonstrate runtime wiring semantics:
- validator.ok == False → output is discarded, only canonical handoff remains
- validator.ok == True → action permission propagates to the language layer
"""

import json
from pathlib import Path
from typing import Iterable, Tuple

from validator import validate_llm_output

SAMPLES_DIR = Path(__file__).parent / "samples"


def load_samples(prefix: str) -> Iterable[Tuple[str, str]]:
    for path in sorted(SAMPLES_DIR.glob(f"{prefix}_*.json")):
        yield path.stem, path.read_text()


def simulate(label: str, raw: str) -> None:
    result = validate_llm_output(raw)
    if result.ok:
        payload = json.loads(raw)
        state = payload["judgment_state"]
        action = state["action_permission"]
        print(
            f"[PASS] {label}: forwarding state (action_permission={action}) "
            "→ Korean mapping layer executes"
        )
    else:
        print(
            f"[DISCARD] {label}: {result.error} | rules={result.violated_rules} "
            "→ emit canonical handoff only"
        )


def main() -> None:
    for group in ("ok", "breach", "error"):
        for label, raw in load_samples(group):
            simulate(label, raw)


if __name__ == "__main__":
    main()
