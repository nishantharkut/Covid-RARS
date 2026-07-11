#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

if [[ -d ".venv" ]]; then
  # shellcheck disable=SC1091
  source ".venv/bin/activate"
fi

python scripts/53_run_sota_e2e.py "$@"
