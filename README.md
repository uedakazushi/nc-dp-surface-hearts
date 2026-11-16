# 非可換del Pezzo曲面の反標準heartと根圏

2026-11-17 / hearts-strategy-v8。GitHub mainを正本とする。最初に [研究方針](00_research_plan.md) を読む。

## 現行の二論文

**[dp-hearts.tex](papers/dp-hearts.tex)**（hearts-v30）は主論文。Rains/VdB/AS/反標準heartの指定比較、HRS/Euler選択、全ADE根圏と普遍アフィン有限商、theta係数と六点復元、最大共鳴稠密性を扱う。標準弱楕円gluingでは、零指数orbit核に加え、coherent反標準関手の有限生成性・有界性を証明し、dg商を古典的特異モデル上のgluingとして記述する。

**[dp-hearts2.tex](papers/dp-hearts2.tex)**（hearts2-v1）は補完論文。符号別Ext・混合A2の精密計算・ADE zigzag形式変形、cubic cornerの十一条件、一様Hilbert関数、162次元平坦族と計算証明を保持する。

主論文の新しい収縮先の記述は、一般qについてDb(qgr R_q)との同値まで証明していない。特異gluingには無限高次自己Extが残り、滑らかなsourceのpropernessを商に仮定しない。AS実現、heart、相対降下の入力は別々に扱う。

## 特異性の局所模型

主論文は、共通部分圏 `O_(Sbar)^perp` のperfect商がOrlovの `D_sg(Sbar)` を回復すること、および全Du Val点のideal sheafの高次Extが
`dim Hom(J_i,q,J_j,q[n])=4δ_ij (n>=3)` を満たすことも証明する。非自明qの反標準qgrとの同値は依然として未解決。

## 再開・再現

[零指数壁とcoherent収縮のノート](research/resonance_walls.md) / [現在の評価](research/current_assessment.md) / [実施方針](research/four_hearts_plan.md) / [Codex指示](AGENTS.md)

```sh
bash scripts/cloud_setup.sh
bash scripts/check.sh all
bash scripts/check.sh tex
```

texは2原稿を組版する。生成PDF・Synctex・ログはbuild/に置き、Git追跡しない。今回の確認は改稿4節の20ページ抜粋の組版と画像点検で、全文・第2論文の組版と既存21検算の再実行は未実施。[検証状態](research/two_papers_validation.json) を参照する。

[Cloud Codex手順](docs/CLOUD_CODEX.md)。mainへの通常保存、PR・GitHub Actions・force push不使用を基本とし、GitHub保存失敗時のみLibraryへ緊急保存する。研究の有効な内容を削除して軽量化しない。
