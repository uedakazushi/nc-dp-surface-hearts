# 非可換del Pezzo曲面の反標準heartと根圏

2026-11-17 / hearts-strategy-v13。GitHub mainを正本とする。最初に [研究方針](00_research_plan.md) を読む。

## 現行の二論文

**[dp-hearts.tex](papers/dp-hearts.tex)**（hearts-v35）は主論文。Rains/VdB/AS/反標準heartの指定比較、HRS/Euler選択、全ADE根圏と普遍アフィン有限商、theta係数と六点復元、最大共鳴稠密性を扱う。標準弱楕円gluingでは、零指数orbit核に加え、coherent反標準関手の有限生成性・有界性を証明し、dg商を古典的特異モデル上のgluingとして記述する。

**[dp-hearts2.tex](papers/dp-hearts2.tex)**（hearts2-v1）は補完論文。符号別Ext・混合A2の精密計算・ADE zigzag形式変形、cubic cornerの十一条件、一様Hilbert関数、162次元平坦族と計算証明を保持する。

主論文の新しい収縮先の記述は、一般qについてDb(qgr R_q)との同値まで証明していない。特異gluingには無限高次自己Extが残り、滑らかなsourceのpropernessを商に仮定しない。AS実現、heart、相対降下の入力は別々に扱う。

## 特異性の局所模型

主論文は、共通部分圏 `O_(Sbar)^perp` のperfect商がOrlovの `D_sg(Sbar)` を回復すること、および全Du Val点のideal sheafの高次Extが
`dim Hom(J_i,q,J_j,q[n])=4δ_ij (n>=3)` を満たすことも証明する。非自明qの反標準qgrとの同値は依然として未解決。

## Du Val idealのqgr像・境界と直交性

主論文 `four_hearts_duval_singularity.tex` に以下を証明：
相異なるDu Val点のideal間の`RHom`は`k[-1]`。
`RHom(ebar,J_x)=0`、`RHom(J_x,ebar)=RΓ(E,q)`で、
非自明qなら指定生成対象の部分圏は`Perf(k)⊕thick{J_x}`に分かれる。
さらに`I_x,q=barPhi(J_x,q)∈qgr R_q`は非零のcoherent対象で、
反標準切断加群`M_n=d n(n+1)/2`、`H_R−H_M=1/(1-t)`。
中心元`g`はM上正則で、境界`M/gM`は楕円曲線の`q^{-1}`を回復する。
非自明qでは`Hom_grR(M,R)=0`であり、通常のideal埋込みは存在しない。
## qgrでのHomの跳び（hearts-v35）

`thm:duval-qgr-hom-vanishing`：
非自明`q∈Pic0(E)`に対して、全`r≥0`で
`Hom_qgrR(I_x,q,πR_q(-r))=0`を証明した。
自明`q`では`r≥1`は零、`r=0`では次元1。
`Hom_gr(M,R)=0`をそのまま転用せず、
Serre商のHomのtail表示と、各tailの境界上の線束`q^-1`、
中心元`g`による反復除法を使う。
全比較が完全忠実なら、非自明`q`の
`Ext^j_qgr(I_x,q,πR_q)=0`（`j≥1`）が必要。
この正次数ExtとA1局所Yoneda積は未解決。

## orbit-perfect coreの新結果

弱楕円gluingでも、反標準orbitが生成する完全部分圏では自然関手が同値になる：
`thick_{Dq}{s^ne} ≃ thick_{Db(qgr Rq)}{πRq(n)}`。
ただし零指数壁ではその部分圏は収縮後の全圏を生成しない。
残余商 `(Qq/thick orbit)^natural` は非零で、古典点q=O_EではOrlovの特異性圏に一致する。非自明qの全圏比較は未解決。

## A1根壁の具体的局所模型

主論文はさらに、A1完備局所環の一周期行列因子化を用いて
`D_sg(k[[u,v,w]]/(uv−w²))` 内の特異点idealの安定自己準同型代数を
`M₂(k[η,η⁻¹])`, `deg η=1` と同定する。
前回の「高次Ext次元4」を積と周期性へ強めるもの。ただし非自明qの反標準qgr側の同定は未解決。

## 再開・再現

[零指数壁とcoherent収縮のノート](research/resonance_walls.md) / [現在の評価](research/current_assessment.md) / [実施方針](research/four_hearts_plan.md) / [Codex指示](AGENTS.md)

```sh
bash scripts/cloud_setup.sh
bash scripts/check.sh all
bash scripts/check.sh tex
```

texは2原稿を組版する。生成PDF・Synctex・ログはbuild/に置き、Git追跡しない。以前の確認は改稿4節の20ページ抜粋の組版と画像点検。現行版では主論文・補完論文の静的参照検査を実施し、全文・第2論文の組版と既存21検算の再実行は未実施。[検証状態](research/two_papers_validation.json) を参照する。

[Cloud Codex手順](docs/CLOUD_CODEX.md)。mainへの通常保存、PR・GitHub Actions・force push不使用を基本とし、GitHub mainを正本とし、研究区切りごとにLibraryへも現行checkpointを保存する。個別の成果物の保存状態は検証記録と照合する。研究の有効な内容を削除して軽量化しない。
