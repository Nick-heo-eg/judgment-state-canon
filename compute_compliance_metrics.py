#!/usr/bin/env python3
"""
Aggregates compliance metrics from JSONL logs emitted by the Canon runtime.
Input format matches compliance_report_template.md expectations.
"""

import json
import sys
from collections import Counter
from dataclasses import dataclass
from typing import Dict, Iterable, Tuple


@dataclass
class Counters:
    total: int = 0
    breaches: int = 0
    self_error: int = 0
    enum_violation: int = 0
    tension_omission: int = 0
    extra_key: int = 0
    confidence_violation: int = 0
    handoff_enforced: int = 0
    rule_counts: Counter = None


def load_records(stream: Iterable[str]) -> Iterable[Dict]:
    for line in stream:
        line = line.strip()
        if not line:
            continue
        yield json.loads(line)


def aggregate(records: Iterable[Dict]) -> Tuple[Counters, Dict[str, int]]:
    counts = Counters(rule_counts=Counter())
    for rec in records:
        counts.total += 1
        envelope = rec.get("envelope", {})
        ok = envelope.get("ok", False)
        rules = rec.get("violated_rules", []) or []
        counts.rule_counts.update(rules)

        if not ok:
            counts.breaches += 1
            if envelope.get("error") in {"state_unresolvable", "insufficient_context"}:
                counts.self_error += 1
            if rec.get("action_taken") == "handoff":
                counts.handoff_enforced += 1

        for rule in rules:
            if rule.startswith("schema.enum"):
                counts.enum_violation += 1
            if rule == "high_risk_proceed_guardrail":
                counts.tension_omission += 1
            if rule.startswith("extra:") or "extra" in rule:
                counts.extra_key += 1
            if rule == "confidence_bounds_ordered":
                counts.confidence_violation += 1

    return counts


def main() -> None:
    data = list(load_records(sys.stdin))
    if not data:
        print("No records provided", file=sys.stderr)
        sys.exit(1)
    counts = aggregate(data)

    def rate(value: int) -> float:
        return (value / counts.total) if counts.total else 0.0

    summary = {
        "total": counts.total,
        "breach_rate": rate(counts.breaches),
        "self_declared_error_rate": rate(counts.self_error),
        "enum_violation_rate": rate(counts.enum_violation),
        "tension_omission_rate": rate(counts.tension_omission),
        "extra_key_injection_rate": rate(counts.extra_key),
        "confidence_bounds_violation_rate": rate(counts.confidence_violation),
        "handoff_enforced_count": counts.handoff_enforced,
        "top_rules": counts.rule_counts.most_common(5),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
