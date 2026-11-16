# 非可換del Pezzo曲面の反標準heartと根圏

2026-11-16 / hearts-strategy-v2。Rains・Van den Bergh・Artin–Schelter・反標準heartを、指定された構造対象と自然関手を保って比較する研究。GitHub mainが正本。

**最初に [研究方針](00_research_plan.md) を読む。** [現状評価・優先順位・一次資料と検証範囲](research/current_assessment.md) に今回の調査をまとめた。

## 中心課題

反標準heartの認識と、実在する境界外根のEuler標数によるheart選択を、公表できる主定理にまとめる。新しい構造目標は全ADE根圏のabel圏同定と、元のアフィン代数A=R/(g−1)の有限次元商である。十一因子が消える古典的退化の壁と、一般位置内の非零指数共鳴を分ける。

## 現行の原稿と研究ノート

- [四つのheart](papers/nc_del_pezzo_hearts.tex)：自然導来比較、全heartのHRS/ADE tilt、規格化AS比較、actual楕円係数、元六点の復元。
- [Rains共鳴](papers/nc_del_pezzo_resonance_hearts.tex)：符号別Ext、混合A2、最大共鳴、四次元アフィン商。
- [Cubic corner](papers/cubic_heart_corner.tex)：四交比、十一条件、六点一般位置、Hilbert関数、有限平坦162次元族と古典根壁。

これらは現行の研究原稿であり、3本の独立した公表論文が完成したことを意味しない。比較とcornerの統合、共鳴別稿の独立性を中心定理に基づいて判断する。

[比較ノート](research/heart_comparison.md) / [共鳴ノート](research/resonance_hearts.md) / [cornerノート](research/cubic_corner.md) / [実施方針](research/four_hearts_plan.md) / [Codex指示](AGENTS.md)

## 確実性と再現

原稿にある証明、今回点検した主要論証、有限計算、未証明目標を区別する。全heartの無条件一致、全potentialのAS性、相対stack降下は主張しない。従来の各validationは個別成果の証明・検算範囲を記したもので、今回の実行範囲は研究評価を参照する。

    python3 -m pip install -r requirements.txt
    python3 computations/verify_four_hearts.py
    python3 computations/verify_resonance_mixed_a2.py
    python3 computations/verify_cubic_corner.py
    latexmk papers/nc_del_pezzo_hearts.tex
    latexmk papers/nc_del_pezzo_resonance_hearts.tex
    latexmk papers/cubic_heart_corner.tex

2026-11-16に全19検算を実行して成功。3主原稿のinput・label/ref・bibitem/citeに静的点検で欠落なし。全文組版はこの環境のLaTeX/LuaTeX-ja欠落で未完了。Python3/SymPyとLuaLaTeX・LuaTeX-ja・latexmkを用い、PDF・Synctex・ログはbuild/へ再生成する。

## 独立して継続する関連研究

[H3分類](https://github.com/uedakazushi/nc-cubic-moduli) /
[次数1モジュライ](https://github.com/uedakazushi/nc-dp1-moduli) /
[nc三次三様体](https://github.com/uedakazushi/nc-cubic-threefold-moduli)

本研究の結果とこれらの研究固有の主張を混同せず、実際に外部結果へ依存する際は固定commitと仮定を示す。
