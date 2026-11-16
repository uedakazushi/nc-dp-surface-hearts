# 非可換del Pezzo曲面の反標準heartと根圏

2026-11-17 / hearts-strategy-v6。GitHub `main` を正本とする。

**研究の再開では最初に [研究方針](00_research_plan.md) を読む。** [研究ノート（比較）](research/heart_comparison.md) / [共鳴](research/resonance_hearts.md) / [corner](research/cubic_corner.md) / [零指数根壁](research/resonance_walls.md)。

## 現行の二論文

- **[第1論文 dp-hearts.tex](papers/dp-hearts.tex)**（hearts-v28）：Rains/VdB/AS/反標準heartのpointedな比較、HRS・ADE単純tilt、規格化theta potentialと六点復元、全ADE根圏と普遍有限商、表現stack、次数1--6の最大共鳴Zariski稠密性、零指数壁の古典的収縮と標準弱gluingのorbit核。
- **[第2論文 dp-hearts2.tex](papers/dp-hearts2.tex)**（hearts2-v1）：第1論文に完全な詳細を収録していない根sheafの符号別Ext・相殺・混合A2の精密計算、ADE zigzag形式変形、cubicの一頂点cornerの十一条件の必要十分性、六点配置との対応、162次元一様Hilbert関数・平坦族、有理数上の計算証明。

第1論文で証明した全次数の最大共鳴と零指数壁について、第2論文は必要な前提だけを簡潔に再掲する。2論文は別々にLuaLaTeXで組版できる構成とし、数学的詳細は両論文からinputされる`papers/sections/`に保持する。過去の3つのdriverは現行論文ではない。

## 数学的な状態

指定genuine smooth elliptic gluingにおける比較と、標準弱楕円gluingの零指数orbit核を区別する。形式変形の32分枝は曲面モジュライの32成分を意味しない。162次元cornerとADE普遍アフィン商は異なる代数。全potentialのAS性・weak gluingのdg商と反標準qgrの同値・曲面族のheart降下は一般に未証明。詳しい仮定と証明所在・次の課題は研究方針を参照する。

## 再現

リポジトリrootで次を実行する。

```sh
bash scripts/cloud_setup.sh
bash scripts/check.sh all
bash scripts/check.sh tex
```

`bash scripts/check.sh tex` は`papers/dp-hearts.tex`、`papers/dp-hearts2.tex` の2本を組版する。`build/`、PDF・同期TeX・auxなどの中間物はGit追跡しない。今回の再編については [検証範囲](research/two_papers_validation.json) を参照。以前の3driverによる組版記録を、新2driverの組版成功として扱わない。

## Cloud Codex

[実行環境手順](docs/CLOUD_CODEX.md) と [Codex指示](AGENTS.md) を参照。一般にmainに直接fast-forward保存し、PR・GitHub Actions・force pushを使わない。
