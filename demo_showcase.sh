#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "=== Canon Demo: validator OK sample ==="
python3 "$ROOT/validator.py" < "$ROOT/samples/ok_high_risk_live_shadow.json"

echo ""
echo "=== Canon Demo: fuzzer (adversarial rejection) ==="
python3 "$ROOT/fuzzer.py"

echo ""
echo "=== Canon Demo: mock LLM runtime wiring ==="
python3 "$ROOT/mock_llm_runner.py"
