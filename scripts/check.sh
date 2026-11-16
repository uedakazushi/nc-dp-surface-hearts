#!/usr/bin/env bash
set -Eeuo pipefail
cd "$(dirname "$0")/.."
mode="${1:-fast}"
mkdir -p build
if [ -f build/tex-user/env.sh ]; then source build/tex-user/env.sh; fi
PYTHON=python3
if [ -x .venv/bin/python ]; then PYTHON=.venv/bin/python; fi
case "$mode" in
  fast)
    "$PYTHON" computations/verify_cubic_heart_numerics.py > build/check_cubic_heart.log
    "$PYTHON" computations/verify_four_hearts.py > build/check_four_hearts.log
    "$PYTHON" computations/verify_resonance_mixed_a2.py > build/check_resonance_mixed_a2.log
    ;;
  all)
    for script in computations/verify_*.py; do
      printf 'Checking %s\n' "$script"
      "$PYTHON" "$script" > "build/check_$(basename "$script" .py).log"
    done
    ;;
  tex)
    command -v latexmk >/dev/null || { echo 'latexmk not installed' >&2; exit 1; }
    for paper in papers/nc_del_pezzo_hearts.tex papers/nc_del_pezzo_resonance_hearts.tex papers/cubic_heart_corner.tex; do
      printf 'Typesetting %s\n' "$paper"
      latexmk -lualatex "$paper"
    done
    ;;
  full)
    bash scripts/check.sh all
    bash scripts/check.sh tex
    ;;
  *)
    echo 'Usage: bash scripts/check.sh [fast|all|tex|full]' >&2
    exit 2
    ;;
esac
echo "PASS: $mode"
