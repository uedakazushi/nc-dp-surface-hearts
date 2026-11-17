# Codex指示：反標準heartとcoherent収縮

2026-11-17 / hearts-strategy-v13。最初に `00_research_plan.md`、`research/resonance_walls.md` を読む。主論文は `papers/dp-hearts.tex`（hearts-v35）、第2論文は `papers/dp-hearts2.tex`（hearts2-v1）。GitHub mainが正本。

## 現在の数学的状態

標準弱楕円gluingの次数付きExtの有限生成性・有界性は `four_hearts_coherent_contraction.tex` に証明がある。Rのnoetherian性、coherent Phiの存在、ker Phi=Nq=iota ker Rf_*までを追加仮定なしで得る（指定弱gluing・滑らかな境界の範囲）。BKS局所化からdg商は古典的特異モデル上のgluing Dbar_qとなる。これらを未解決へ戻さない。

次の核心は一般qの Dbar_q→Db(qgr R_q) の全RHom比較と本質的全射性。まずA1壁の特異点ideal I_xを使う。q=Oでは古典的同値があるが、一般qで同じ結論を仮定しない。非genuineなDbar_qは高次自己Extが無限にありproperでない。sourceのsmooth proper性を商へ移さない。

## Du Val局所核の研究状態

`four_hearts_duval_singularity.tex` に、Bbar/(Bbar∩Perf Sbar)=D_sg(Sbar) と Du Val点のidealの高次Ext次元4δij（全n≥3、全q）の証明がある。TateのPoincare級数 (1+t)^3/(1-t²) を既知入力とする。特異gluing全体の特異性圏や一般qのDb(qgr R_q)との同値は主張していない。次はYoneda積・2周期構造・qgr側の像の検証であり、高次Ext次元計算を未解決に戻さない。

## 現行の新主定理：orbit-perfect core

`four_hearts_orbit_core.tex` の `thm:orbit-core-equivalence` は任意qの標準弱楕円gluingでTq=thick orbitからPq=thick(qgrのfree twists)へのdg同値を示す。Rains Cor.3.8のorbit間Extと境界H¹へのtrace比較が入力であり、genuine時のorbit生成は使わない。
`thm:residual-singularity` は非genuineならTq⊊Qq、残余Sq≠0、q=O_EではSq=D_sg(Sbar)^naturalとする。
非自明qについてQq≅Db(qgr Rq)は依然未解決。完全忠実性をorbit上で示したことと、全圏の同値は混同しない。
次は残余商の像、局所高次Yoneda積、orbitとのgluingをA1壁で比較する。

## 一つのA1壁で解決した局所模型

`four_hearts_a1_stable_model.tex` の一周期matrix B=[[-w,-v],[u,w]]、Ω²_Ak≅N²、underlineEnd_A N=kから、
D_sg(A)内でgraded stable End(m)≅M₂(k[η±1])、degη=1を得た。
通常のExtと完備局所特異性圏への像の安定Endは別物である。
この積模型を非自明qのDb(qgrR_q)で確認したのではない。
次は対応する標的対象・ηの像・gluingを調べる。

## Du Val点のgluingの追加計算

`four_hearts_duval_singularity.tex` に命題 `prop:duval-ideal-boundary-gluing` がある。
Du Val点xのideal sheafの像J_x,qについて
`RHom(ebar,J_x,q)=0`, `RHom(J_x,q,ebar)=RΓ(E,q)`。
非自明qでは両側直交し、q=O_Eでのみ0,1次に各1次元のExt。
指定gluingの定義とE∩{x}=∅から直接証明している。
Dbar_qの全分解やDb(qgr R_q)への同値には延長しない。
これはq不変な局所安定自己Ext代数とは別の情報。
A1壁の残余比較でこの跳びを優先して利用する。

## qgrに生き残る非perfect idealと最初の検証対象

`four_hearts_duval_singularity.tex` に
`prop:duval-offdiagonal-ext`（相異なるidealのRHom=k[-1]）、
`cor:duval-local-splitting`（非自明qでの**生成部分圏のみ**の分解）、
`thm:duval-point-hilbert`（`I_x,q=barPhi(J_x,q)∈qgr R`、
`M_n=d n(n+1)/2`、`H_R−H_M=1/(1-t)`、g正則、
境界`M/gM=q^-1`）、
`prop:duval-no-graded-inclusion`（非自明qで`Hom_grR(M,R)=0`）、
`cor:duval-target-hom-obstruction`（完全忠実なら
`RHom_qgr(pi M,pi R)=0`）が証明付きである。
**`thm:duval-qgr-hom-vanishing` が解決：**
非自明qで全r≥0について `Hom_qgr(πM_x,πR(-r))=0`。
自明qではr=0がk、負twistは零。
`Hom_qgr=colim Hom_gr(M_≥a,R(-r))`を用いて
すべてのtailのg反復除法を証明。graded Homの消滅のみから
推論していない。`cor:duval-target-hom-obstruction`を改訂し、
非自明qで **残る必要条件は正次数Ext^j（j≥1）の消滅** とした。
次のA1壁の研究ではまずExt1を計算する。

## 優先順位

P0は公表に向けた新証明の独立点検、全文組版と参照検査。有限生成証明の正次数部分への単射、degree0補正、下有界graded Nakayama、dg moduleの構成を確認する。P1は一壁の非perfect対象の比較。P2は壁上AS実現とheart内の位置。P3は複数壁・相対化。

既存のgenuine導来比較、Euler選択、全ADE有限商、表現スキーム、theta係数、最大共鳴は保持する。第2論文の符号別Ext・混合拡大・zigzag形式変形・162次元cornerの詳細も削らない。数値共鳴とsheaf存在、abel圏内のExtとambient Ext、162次元cornerと普遍有限商、固定曲面の古典的Repと導来・相対moduliを区別する。

## 執筆・検証・保存

日本語LuaLaTeX。重要な既知入力を一次資料で照合し、一般理論そのものを新規と呼ばない。証明記載・内部点検・計算・組版・独立査読を区別する。今回新しい一般定理の独立査読・機械形式化は未実施。

`bash scripts/check.sh tex` は2本を組版し、`bash scripts/check.sh all` は全verifyコードを実行する。以前の確認は改稿4節の20ページ抜粋。今回v33ではネストinputを含む静的ラベル検査を追加したのみ。主論文全文と第2論文の組版、既存21検算は今回未実施であり、以前の検証を今回の成功としない。詳しくは `research/two_papers_validation.json`。

約15分または数学的区切りでcheckpointを作る。共有mainを確認し安全に統合して通常のfast-forwardで直接保存する。PR・GitHub Actions・force pushを使わない。PDF・ZIP・中間物・cacheは追跡しない。GitHub mainを正本とし、研究区切りごとに現行の研究継続用bundleをLibraryへも保存する。保存実行と読み戻しの状態を正確に記録する。既存Library資料を無断削除しない。生成・保存・remote確認は別々に報告し、背景での自動継続を約束しない。
