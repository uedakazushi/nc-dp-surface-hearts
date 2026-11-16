# 非可換del Pezzo曲面の反標準heartと根圏

2026-11-16 / hearts-strategy-v3。Rains・Van den Bergh・Artin–Schelter・反標準heartを、指定された構造対象と自然関手を保って比較する研究。GitHub mainが正本。

**最初に [研究方針](00_research_plan.md) を読む。** [現状評価・優先順位・一次資料と検証範囲](research/current_assessment.md) に今回の調査をまとめた。

## 中心課題

反標準heartの認識と、実在する境界外根のEuler標数によるheart選択を、公表できる主定理にまとめる。主論文には全ADE根圏のabel圏同定と、元のアフィン代数A=R/(g−1)の全有限次元表現を支配する商の証明を追加した。十一因子が消える古典的退化の壁と、一般位置内の非零指数共鳴を分ける。

## 現行の原稿と研究ノート

- [四つのheart](papers/nc_del_pezzo_hearts.tex)：自然導来比較、全heartのHRS/ADE tilt、規格化AS比較、actual楕円係数、元六点の復元。
- [Rains共鳴](papers/nc_del_pezzo_resonance_hearts.tex)：符号別Ext、混合A2、最大共鳴、四次元アフィン商。
- [Cubic corner](papers/cubic_heart_corner.tex)：四交比、十一条件、六点一般位置、Hilbert関数、有限平坦162次元族と古典根壁。

主論文は反標準heartの認識・Euler選択・ADE有限商・単根例を集約する。共鳴稿とcorner稿は有効な証明を保持した補助原稿として扱い、3本の独立した完成論文とは数えない。

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

2026-11-16に全20検算を実行して成功。3主原稿をLuaLaTeXで組版し、参照と引用の整合を点検する。今回の確認範囲は研究評価に記載する。Python3/SymPyとLuaLaTeX・LuaTeX-ja・latexmkを用い、PDF・Synctex・ログはbuild/へ再生成する。

## 独立して継続する関連研究

[H3分類](https://github.com/uedakazushi/nc-cubic-moduli) /
[次数1モジュライ](https://github.com/uedakazushi/nc-dp1-moduli) /
[nc三次三様体](https://github.com/uedakazushi/nc-cubic-threefold-moduli)

本研究の結果とこれらの研究固有の主張を混同せず、実際に外部結果へ依存する際は固定commitと仮定を示す。

## Cloud Codex

セットアップ・検算とCodex Cloud環境の登録方法は [Cloud Codex手順](docs/CLOUD_CODEX.md) を参照。研究指示は [AGENTS.md](AGENTS.md)、現在の研究優先順位は [00_research_plan.md](00_research_plan.md) にある。
