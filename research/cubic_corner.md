# Cubic corner の有限性と4交比：現行研究ノート

2026-11-15 / hearts-v8 / corner-v7。最初に `00_research_plan.md` を読み、証明は `papers/cubic_heart_corner.tex` の定理 `thm:general-position-iff` とその依存箇所を読む。全次数のheart比較は `research/heart_comparison.md` にある。

## 古典的根壁と anticanonical heart の障害

**証明済み**：11 divisorは10個の共線性根 h-e_i-e_j-e_k とconic根 2h-sum e_i。一般壁の六点blowup Sは弱dP3、対応(-2)曲線 E を反標準射fがA1点へ収縮。F=i_*O_E(-1)は2-sphericalで、全nについてRHom(O_S(n(-K_S)),F)=0、Rf_*F=0。coh Sでは反標準AZ ampleが失敗し、qgr anticanonical ring=coh XだがDb(coh S)とDb(coh X)は導来非同値（特異点の剰余体の非有界Ext）。任意次数の弱dPで(-2)曲線がある場合にも同じ障害が成立する。**これは古典的blowupの結果であり、非可換Rains/VdB/AS heartの壁特殊化の証明ではない。**

**厳密な一壁例**：Q0=[[1,1,1],[1,2,2],[1,3,4]]で9個のminorのうち1個のみ0、detQ=1、det成分逆数Q=1/24。六点は(1:1:1),(2:1:1),(12:4:3)と三座標点で共線3点はp1,p2,p4だけ。反標準三次のnodeは[0:0:1:1]、局所Hessian det=-2304。多項式恒等式を有理数で厳密検証。証明`papers/sections/cubic_corner_root_walls.tex`、再現`computations/verify_cubic_root_wall.py`。

**一次資料**：AOU arXiv:2404.00175v1 §§1,4,8は六点係数を定義。弱dPの反標準収縮はDolgachev, *Classical Algebraic Geometry*, Thm 8.3.2とBlanc–Lamy, Proc. LMS 105(2012), Introduction/§4。幾何学的事実と新規の具体的対応・spherical計算を区別し、新規性の全面調査・独立査読は未実施。

## 現行の完全 Hilbert 関数定理と有限平坦族

**証明済み（標数0・十八係数非零・十一条件）**：道長 graded の商 C=B/BeB は六点配置に依存せず Hilbert 級数
`H_C(t)=8+21t+33t^2+38t^3+33t^4+21t^5+8t^6`、総次元 `162`。前回の下界 `dim C_6>=8` は等号。一般位置 locus で次数 0..6 の次元跳びは存在しない。完全証明は `papers/sections/cubic_corner_hilbert_series.tex`（`papers/cubic_heart_corner.tex` に input）。

AOU(4.9)の可換 cubic の九線束間のHomと、e=A0を経由する積の像を個別に計算した。八頂点間の全Homの次数別次元は(8,21,42,74,105,147,206,252)、経由部分の次元は(0,0,9,36,72,126,198,252)。次数2..5は例外曲線の定義切断とbase-point-free pencil trickで計算。次数6のA_a→A_bに必要な3×3の積写像の単射性は、一方のblowdownで縮約され、他方で滑らかなconicに写る非共線な3曲線への制限で証明する。B_i→B_kとC_j→C_kの2つの経由位置の像の包含もpencil trickで証明する。次元計算はPicard格子のRR（AOU helixのacyclicityを使用）による。

**有限平坦性**：四交比トーラスの十一条件の補開集合 U 上で、universal quotient C_U は道長0..6の階数(8,21,33,38,33,21,8)の局所自由成分の直和で、全体として階数162の有限局所自由 O_U-代数となり、任意の基底変更と可換する。各道長の有限関係行列が全幾何学的fiberで一定階数なので従う。非可換potentialの全27係数のAS性、Rains heart・VdB heartとの比較は主張しない。

**数値検算**：`computations/verify_cubic_corner_hilbert.py` は27本の(-1)曲線、4組のblow-down線束、RRによる各次数全Hom、経由部分の次元台帳を整数演算で検査する（積写像の一般的な単射・全射の証明はTeX）。一般位置の別の有理六点配置3組でも既存のJacobian消去を F_1000003 で実行し、同じ次数列を得た。追加部分を日本語LuaLaTeXで3ページ単独組版し、警告・見た目を確認。リポジトリ本稿全体の組版は今回未実施。

## 現行の一様次数定理

**証明済み（標数0・18係数非零）**：四交比の11非零条件と `dim C<∞` と `C_7=0` は同値であり、11条件が成立するとき `dim C_6>=8`。従って `U=U_7={Δ11≠0}`、七が最良の一様消滅次数。証明は `papers/sections/cubic_corner_uniform_cutoff.tex`（現行 `papers/cubic_heart_corner.tex` に `\\input`）。AOU(4.9)の滑らかな可換 cubic の線束モデルを用い、道長7の21ブロックを A_a→B_i（6）、B_i→C_j（9）、C_j→A_a（6）に分け、blow-down線束のconic制限・basepoint-free pencil trick・Kodaira/Kawamata--Viehweg消滅により全て `A0` を経由することを示した。対角道長6の八頂点には各1次元以上の商が残る。これは既存のF7全探索からの推論ではない。有限行列 `M_7` の最大小行列式イデアルの根基は四交比Laurent環で `rad(Δ11)` と一致（scheme構造までは主張しない）。

数値仮定は `computations/verify_cubic_corner_c7_geometry.py` で27本の(-1)曲線との交点、四つのblow-down line class、13個のKV nef/big入力を厳密な整数計算で検査した。これは線束の乗法の代数的証明とは別。LuaLaTeXで新規3ページの単独組版検査を実施したが、リポジトリ全文の再組版は未実施。

## 現行定理（標数0・18係数非零）

AOU型の3×3 cyclic quiver Qtilde と27係数potential W=(w_abc)を取り、B=Jac(Qtilde,W)、e=e_(A0)、C=B/BeBとする。Cはw_0bcに依存しない。w_1bc,w_2bcがすべて非零とし、q_bc=w_2bc/w_1bcを定める。矢の非零rescalingによりqは行・列rescalingを受けるだけで、完全不変量は四つの交比 lambda_ij=q_ij q_00/(q_i0 q_0j) (i,j=1,2)。Q=[[1,1,1],[1,a,b],[1,c,d]]と規格化できる。

**証明済みの必要十分条件**：Cが有限次元 iff Qの9個の2×2小行列式、det Q、det(Qの成分ごとの逆数)がすべて非零。18係数が零なら、先行補題の一閉路表示によりCは無限次元。よって係数トーラスでの悪いlocusは明示的な11 divisorの和集合で尽くされる。

四交比での追加二式は (a-1)(d-1)-(b-1)(c-1) !=0 と bc(1-a)(1-d)-ad(1-b)(1-c) !=0。九小行列式はa,b,c,d !=1、a!=b、c!=d、a!=c、b!=d、ad!=bc。11条件全体の十分性は有限体の推測ではなく、以下の六点復元＋AOUの既知定理＋Serre消滅で証明した。

## 幾何学的再構成と証明の依存関係

P=(Qの成分ごとの逆数)^t の列をp1,p2,p3とし、p4,p5,p6をP2の座標三点とする。Qの各成分非零→可動点1・座標点2の非共線、9小行列式非零→可動点2・座標点1の非共線、det Q^{had-inv}非零→可動点3の非共線、det Q非零→六点がconic上にない。従って六点は一般位置でS=Bl_{p1...p6}P2は滑らかなcubic。

AOU arXiv:2404.00175v1, (4.1),(4.7),(4.9),(8.4)-(8.7)で、同じ基底規約なら幾何的potentialの二関係系列がw1_bc=P_cb、w2_bc=1となり、比w2/w1=qを回復する。六点の線束関係で使う conic D_b=(u_{b+1}×u_{b+2})·(X1X2,X2X3,X3X1) と直線 L_{bc}=det[p_{b+1},p_{c+4},X] は、sum_b P_cb D_b L_bc=0 と sum_b M_b L_bc=0 という整数係数の恒等式を満たす。6つの全恒等式は新規の標準ライブラリ検算スクリプトで普遍的に検証した。

AOU(4.9)はJac(Qtilde,Wgeo)=⊕_{v,v',n≥0}Hom_S(Ev,Ev'(nH))を同定する。H=-K_SがampleなのでEv^∨(mH)の大域生成とSerre消滅を用い、n≫0で全Homを Ev→O_S(mH)→Ev'(nH) に分解できる。これがeを通る経路に対応しCの全高次cut成分が零になるため、C有限次元。w0はCに影響しない。したがって四交比の有限corner locusは、ordered six-point general-position moduli Mcubicと正則同型になる。これは全27係数potentialが幾何的であるという主張ではない。

## Heart比較への帰結と留保

AOU型AS helixとのfolding、Serre inverse shift、orbit algebraの飽和、およびnoetherian性が成立する対象では、自然なrestriction qgr B_cut→qgr(eB_cut e)が同値 iff この11条件。右辺は構造対象Oからのanticanonical heart。よってAS heartとanticanonical heartがabel同値となる領域を、指定の自然関手に関して完全に決定した。11条件外で他のabel同値・導来同値が一切ないとは言わない。Rains heart/VdB heartとのpointedness、実際のAOU mutation後E0とπFの同定は未解決。

## 補助定理と検算

必要性：係数零は一閉路、2×2 minor零は2×2支持、det Q零はrank2分解Q=UVと左右核を使い、k[t]上に非冪零三角閉路を持つJacobi表現を構成する。成分逆数行列のdet零はA1/A2を交換して帰着。全文は現在の論文§§3-4、rank2検算 `computations/verify_cubic_corner_rank2.py`。

六点の幾何的同定は `computations/verify_cubic_six_points.py`（標準Pythonのみ）で、9個の自由な座標変数上の6本の普遍的整数多項式恒等式、3つの有理数例、F7の四交比トーラス1296点の全比較（一般位置は80点）を検査した。以前のC7=0の厳密計算（六点witnessでHilbert次元[8,21,33,38,33,21,8,0]、総次元162）、F7の80点すべてでC7=0という有限体観察も保持する。現在は一般位置で一様にC7=0が証明済みであり、以前の有限体結果は独立検算として保持する。

## 次の核心

1. **非可換AS locusと根壁**：古典的な11壁のspherical導来障害を確定した。次は各壁に非可換AS-regularが存在するか、Rains/VdB heartがspecializeするかを確かめる。古典的非同値から非可換全点の非同値を推論しない。
2. **Rains/VdBとの実際の比較**：AOUのmutation後E0≅πFをobject levelで検証し、VdBの最後のδ_*に対するkernelと高次pushforwardを実在対象から計算する。自然同値のt-exactnessと別のderived同値を分離する。
3. **一般次数とmoduli**：全intrinsic cubicを幾何的六点分枝と同一視せず、量子FermatなどOU AS型でない分枝を保持。dP1と他次数のheart比較へ必要十分条件の方法を移植する。

一次資料はAOU §4（4.1,4.9）、§8（8.1,8.4-8.9）と OU arXiv:2508.04986。定理の新規性・初出は未確認。証明記載、整数検算、LuaLaTeX組版は区別する。再現は `python3 computations/verify_cubic_six_points.py`、`python3 computations/verify_cubic_corner_c7_geometry.py`、`python3 computations/verify_cubic_corner_hilbert.py`、`latexmk papers/cubic_heart_corner.tex`。推奨の現行名は Rains heart, VdB heart, AS heart, anticanonical heart。
