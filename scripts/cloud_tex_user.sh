#!/usr/bin/env bash
# Fill missing LuaTeX/Japanese files in a Debian TeX Live 2025/dev environment.
# Uses only build/; requires the already-installed engine and base LaTeX tree.
set -Eeuo pipefail
cd "$(dirname "$0")/.."
command -v luahbtex >/dev/null
command -v latexmk >/dev/null
command -v dpkg-deb >/dev/null
kpsewhich latex.ltx >/dev/null
tex_task_root="$PWD/build/tex-user"
mkdir -p "$tex_task_root/downloads" "$tex_task_root/var/web2c/luahbtex" \
  "$tex_task_root/config" "$tex_task_root/cache"
fetch_tex_deb() {
  local name="$1" group="$2" digest="$3"
  local target="$tex_task_root/downloads/$name.deb"
  if [ ! -f "$target" ]; then
    curl --fail --location --silent --show-error \
      "https://deb.debian.org/debian/pool/main/t/$group/${name}_2024.20250309-1_all.deb" \
      --output "$target"
  fi
  printf '%s  %s\n' "$digest" "$target" | sha256sum --check
  dpkg-deb --extract "$target" "$tex_task_root/system"
}
fetch_tex_deb texlive-luatex texlive-base \
  c6601d6856af0b9cd25c64fcdab4a219a6ce7fd7a37724f532305add28fc72ff
fetch_tex_deb texlive-lang-japanese texlive-lang \
  80dbfdc745a40dc51138e5da05ed4bb409683f333da4f8614e0770f5810d3916
# printf %q keeps repository paths containing whitespace safe to source in Bash.
{
  printf 'export TEXMFHOME=%q\n' "$tex_task_root/system/usr/share/texlive/texmf-dist"
  printf 'export TEXMFVAR=%q\n' "$tex_task_root/var"
  printf 'export TEXMFCONFIG=%q\n' "$tex_task_root/config"
  printf 'export TEXFORMATS=%q\n' "$tex_task_root/var/web2c/luahbtex:"
  # Relative path also works with the engine's restricted file-writing policy.
  printf 'export TEXMFCACHE=%q\n' 'build/tex-user/cache'
} > "$tex_task_root/env.sh"
source "$tex_task_root/env.sh"
luahbtex --ini --interaction=nonstopmode --halt-on-error \
  --output-directory="$TEXMFVAR/web2c/luahbtex" --jobname=lualatex \
  '\input lualatex.ini' > "$tex_task_root/format.log" 2>&1
kpsewhich lualatex.fmt
kpsewhich ltjsarticle.cls
kpsewhich HaranoAjiMincho-Regular.otf
echo 'User-local TeX ready: bash scripts/check.sh tex'
