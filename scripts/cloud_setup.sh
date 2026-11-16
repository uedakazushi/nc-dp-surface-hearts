#!/usr/bin/env bash
# Debian/Ubuntu-based Codex Cloud setup, run from repository root.
set -Eeuo pipefail
cd "$(dirname "$0")/.."
export DEBIAN_FRONTEND=noninteractive
command -v python3 >/dev/null || { echo 'Python 3 required' >&2; exit 1; }
python3 -m venv .venv
.venv/bin/python -m pip install --disable-pip-version-check -r requirements.txt

if ! command -v lualatex >/dev/null || ! command -v latexmk >/dev/null || ! kpsewhich ltjsarticle.cls >/dev/null 2>&1 || ! kpsewhich luatexja.sty >/dev/null 2>&1; then
  if ! command -v apt-get >/dev/null; then
    echo 'Install LuaLaTeX, LuaTeX-ja, latexmk, tikz-cd and Harano Aji fonts manually' >&2
    exit 1
  fi
  if [ "$(id -u)" -eq 0 ]; then APT=(apt-get)
  elif command -v sudo >/dev/null; then APT=(sudo apt-get)
  else echo 'Need root or sudo for TeX packages' >&2; exit 1; fi
  "${APT[@]}" update
  "${APT[@]}" install -y --no-install-recommends \
    texlive-luatex texlive-lang-japanese texlive-latex-extra \
    texlive-pictures latexmk fonts-haranoaji-mincho fonts-haranoaji-gothic
fi
command -v latexmk
command -v lualatex
kpsewhich ltjsarticle.cls
kpsewhich luatexja.sty
kpsewhich tikz-cd.sty
mkdir -p build
echo 'Setup complete: bash scripts/check.sh fast'
