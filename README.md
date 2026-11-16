# 非可換del Pezzo曲面のheart比較

2026-11-16。Rains、Van den Bergh、Artin–Schelter、反標準heartの比較と、Rains共鳴・cubic cornerを対象とする独立の研究リポジトリ。**最初に[研究方針](00_research_plan.md)を読む。** GitHub mainが現行の正本。

## 公表用原稿
- [非可換del Pezzo曲面の四つのheart](papers/nc_del_pezzo_hearts.tex) — 指定導来比較、AOUのt-exactness、十一非零条件・楕円係数と壁。
- [Rains共鳴と反標準heart](papers/nc_del_pezzo_resonance_hearts.tex) — 符号別Ext、混合A2、HRS tiltとアフィン商。
- [三次曲面のAS/反標準heartのcorner](papers/cubic_heart_corner.tex) — 四交比、六点一般位置、有限平坦162次元corner、根壁。

[四heart研究ノート](research/heart_comparison.md) ／ [Rains共鳴ノート](research/resonance_hearts.md) ／ [cubic cornerノート](research/cubic_corner.md) ／ [Codex指示](AGENTS.md)。

## 研究の状態
指定の滑らかな楕円gluing・標準noetherian AS三block等、定理ごとに範囲が異なる。すべてのnoncommutative del Pezzo上で無条件なheart一致や相対stack降下を主張しない。最新の状態は `research/four_hearts_validation.json`、`research/resonance_hearts_validation.json`、`research/cubic_corner_validation.json` を参照。

## 再現
```sh
latexmk papers/nc_del_pezzo_hearts.tex
latexmk papers/nc_del_pezzo_resonance_hearts.tex
latexmk papers/cubic_heart_corner.tex
python3 computations/verify_four_hearts.py
python3 computations/verify_resonance_mixed_a2.py
python3 computations/verify_cubic_corner.py
```
Python3（SymPy使用）、LuaLaTeX、latexmk。PDF・Synctex・ログはGitに追跡しない。今回の移管は既存原稿・証明・コードの保全であり、数学的証明の全面再監査ではない。

## 関連する別研究
- [H3分類](https://github.com/uedakazushi/nc-cubic-moduli)
- [次数1 nc del Pezzoモジュライ](https://github.com/uedakazushi/nc-dp1-moduli)
- [nc三次三様体とnc P4](https://github.com/uedakazushi/nc-cubic-threefold-moduli)

必要な外部結果は固定版と仮定を明記して利用する。