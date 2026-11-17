# 最大共鳴・零指数壁・coherent収縮

2026-11-17 / hearts-v32。研究方針を最初に読む。証明は主論文の `four_hearts_maximal_density.tex`、`four_hearts_zero_walls.tex`、`four_hearts_coherent_contraction.tex`。以下は再開に必要な依存関係と障害であり、本文の全証明を重複しない。

## 最大共鳴の現在の知識

固定した楕円E、flex原点、非torsion q、3≤r≤8で最大共鳴は単純指数の整数表示

    3p1=(m0−2m1−m2)q,  pi=p1+(m1+...+m_(i−1))q

に等しい。相異性等を課す前にE[3]の九選択がある。全根指数非零がgenuine条件。正整数倍点pi=Ni qは全根で非零指数を持ち、任意の厳密な整数順序もunimodular累積和写像によってZariski稠密。既存整列定理と合わせ、指定heartの一致・不一致はともに稠密で非構成可能。これは点ごとの固定楕円chartの主張で、相対t構造や全moduliの代数性の主張ではない。数値根の数8,20,40,72,126,240は実在既約sheafの個数ではなく、Hilbert関数も跳ばない。

## 古典的な零壁と実在対象

十一因子は十の共線根と一つのconic根。弱del Pezzoの反標準収縮f:S→Sbarは(-2)配置をDu Val点へ縮める。K_C=i_*O_C(−1)は2-spherical、全反標準orbitに直交し、Rf_*で消える。特異モデルの剰余体は無限高次Extを持つのでDb(cohS)とDb(cohSbar)は同値でない。Euler列O(−2)→O(−1)^2→Oは同一曲線類の正負相殺であって、genuine非torsionの異なる隣接根の例ではない。

Q0=((1,1,1),(1,2,2),(1,3,4))の有理数六点・反標準三次式・nodeのHessian−2304は主論文に保持。非torsionの例はE=C/(Z+iZ)、q=√2、六点(√3,√5,−√3−√5,√7,√11,√13)、L1=O(3o)、L0=L1q。唯一の共鳴根は±(h−e1−e2−e3)で指数0、前半三点だけ共線。U+と27theta係数非零は残るが成分逆数detQ=0でcornerは無限次元。AS模型と弱gluingの指定比較は未構成。

## 全orbit核とcoherent関手

標準弱楕円gluingDqはB=O_S^perpにeをRHom(M,e)=RHom_E(Li*M,q)で付ける。Fq(e)=O_E、Fq|B=Li*(−)⊗q^−1、theta→id→i_*Fq、Fq s=ΨFqを使う。境界Ψは平行移動と正次数tensor。qの位数は問わない。

既存の `thm:weak-orbit-kernel` は Nq-tail=Nq=iota_q ker Rf_* を全RHom・合成込みで同定する。tail→境界消滅→s周期→Bの対象G、RΓG=Li*G=0→射影公式とSbarのample twist→Rf_*G=0が証明の順序。コンパクト対象内の直交消滅だけからthick生成を推論していない。K_C,q=iota_qK_Cは全qで実在するが、任意のRains heartでの単純sheaf性は未証明。

今回の `thm:weak-coherent-sections` はcoherent有限性を閉じる。eのexceptionalityと正次数境界line bundleのH1消滅から、正orbit間の高次Extを消し、中心正則gとR/g=B(E,Ψ)を得る。平行移動は数値的divisor群に恒等、正次数line bundleはampleなのでKeeler Theorem1.2でBは左右noetherian。固定全次数で有限のg進filtrationからRも左右noetherianとなる。

任意Xについて、n≥1で

    N^j_(n−1) --g--> N^j_n --> C^j(FX)_n --> N^(j+1)_(n−1)

が完全。C^j(V)=⊕H^j(E,Ψ^nV)は有限生成B加群でcohomologicalに有界。従って(N^j/gN^j)の正次数部分はC^jの部分加群として有限生成、degree0を補いgraded NakayamaでN^jを有限生成にできる。XとFXの初期cohomologyの範囲の外ではgは全射でN0=0なので全Nn=0。ここでgが同型とは主張せず全射だけを使う。

正のdg orbit代数がcohomology0だけを持つので、good truncationで通常のRへ移し、module ⊕RHom(e,s^nX)からPhi=πRΓ*を構成する。有限生成性と有界性からDb(qgrR)に入り、kerPhi=Nqを得る。標準弱gluingでは以前の有限性の追加仮定は不要となった。

## 特異gluingとしての収縮先

BKSのTheorem2.14は、射影f、幾何fiber次元≤1、Rf_*O=Oの下でDb(cohS)/kerRf_*≃Db(cohSbar)をdg局所化として与える。弱del PezzoのDu Val収縮はこの仮定を満たす。

Bbar=O_Sbar^perpについてB/Nf≃Bbar。fは境界近傍で同型なのでLi*G=L i_bar* RfG、gluing moduleはBbar上のRHom_E(L i_bar*(−),q)へ降りる。これにexceptional ebarを付けたDbar_qがQq=(Dq/Nq)^naturalに等しい（`thm:singular-gluing-target`）。q=OではGorenstein双対とCartier triangleによりDb(cohSbar)を回復する。

Sが非genuineなら、特異点xのideal I_xはRΓI_x=0でBbarに入る。Gorenstein次元2と0→I_x→O→k(x)→0からj>2でExt^j(I_x,I_x)=Ext^j(k(x),k(x))。したがってQqには全qで無限高次自己Extがあり、properでなくsourceDqと抽象的にも同値でない。まだ同定していないDb(qgrR_q)の性質として述べてはいけない。

## 古典的特異性圏とDu Val点の高次Ext

`four_hearts_duval_singularity.tex` の `prop:duval-singularity-quotient` では、O_Sbarがexceptionalかつperfectなので、評価triangleによる射影P(G)=Cone(RΓ(G)⊗O→G)がperfectを保つことから、
Bbar/(Bbar∩Perf Sbar)≃D_sg(Sbar) を証明する。全qに共通の充満部分圏だけの部分商であり、Dbar_q全体の特異性圏を同定したわけではない。

Du Val点x_iのideal I_iはRΓ(I_i)=0からBbarに入り、任意のqで像J_i,qを持つ。局所Gorenstein双対性と二つの短完全列から n≥3 で
Ext^n(I_i,I_i)≃Ext^n(k(x_i),k(x_i))、異なる点間はExt^n(I_i,I_j)=0となる。
Du Valの局所環は埋込次元3、余次元1のhypersurfaceで、Tateの最小自由解消による
P_k(t)=(1+t)^3/(1-t²)=1+3t+4t²+4t³+...
から高次次元4δijを得る。これらは局所の既知公式と指定gluingの完全忠実性の帰結で、新規性は別途文献照合が必要。

主要一次資料：Orlov, *Triangulated categories of singularities and D-branes in Landau–Ginzburg models*, Proc. Steklov Inst. Math. 246 (2004), 227–248, arXiv:math/0302304v2。Tate, *Homology of Noetherian rings and local rings*, Illinois J. Math. 1 (1957), 14–27。Tate解消の手順は Stacks Project §23.6 (Tag 09PF) にもある。

## 再発を避けるべき誤った推論

内部次数の下有界性なしにはN/gN有限生成からN有限生成は従わない。例えばk[g,g^−1]はgによる商が零だがk[g]上有限生成でない。新証明のNは非負内部次数である。次数0の境界列の左端を零とみなさず、正次数の単射と有限な補正を使う。g進還元の有限性は固定全次数を保つ同次生成元に対して使う。

核の同定から商同値を結論しない。perfect対象だけで特異標的の全coherent対象を尽くさない。sourceのproper性を商へ移さない。Rのorbitの一致は全非perfect対象間のRHomの一致ではない。

## 反標準orbitの同値と残余特異性

`four_hearts_orbit_core.tex` は全qの標準弱gluingに対し
Tq=thick{s^n e}, Pq=thick{πRq(n)}で Φq|Tq:Tq≃Pq を証明する。
sourceのorbit Extはeのexceptionality・境界triangle・Serre双対性、targetはRains Corollary3.8を使い、traceは境界H¹(O_E)を通じて比較する。genuineのInd生成は不要。
Nqはs不変でTqと左右直交なので、Tqは収縮商Qqにも完全忠実に埋め込まれる。

非genuineではQqに無限高次自己Extの対象がある一方、Tqはproper。
従ってTq⊊Qq、残余Sq=(Qq/Tq)^naturalは非零。
q=O_EではQq=Db(coh Sbar)、Tq=Perf(Sbar)、Sq=D_sg(Sbar)^natural。
これは全qでSqが同じだという定理ではない。また残余商の比較だけでDbar_qとDb(qgr Rq)の全同値が従うとも主張しない。
残るのは非perfect対象とorbitとのgluingを含む、非自明qでの全自然比較。

## A1完備局所環の積まで含む模型

A=k[[u,v,w]]/(uv−w²)=k[[s,t]]^±、N=k[[s,t]]_odd を取る。
B=[[-w,-v],[u,w]] は B²=(w²−uv)I で、coker B=N、ΩN=N。
N≅(u,w)=I はrank-one reflexive、End_A I=A、I^{-1}=I/u、trace II^{-1}=m。
従って underlineEnd_A N=k。
Hilbert–Burchの二列 (-t,0,s),(0,-s,t) は S=k[[s,t]] 上の (s²,t²,st) のsyzygyを生成し、
符号反転の不変部分を取れば Ω²_A k≅N⊕N。
Buchweitz–Orlovにより D_sg(A) で m≅N²、shift1でNに戻る可逆ηを選べる。
次数付き安定End代数は M₂(k[η,η^{-1}]) (degη=1)。
この同型は非標準的だが次数付き積を与える。各n≥3の普通のExt次元4と矛盾せず、
ordinary Extの低次数までLaurent代数だという主張ではない。
非可換gluingの全qに共通する古典側の局所完備化を計算しただけで、qgr側の対象と周期射ηの像はまだ分からない。

一次資料：Eisenbud, *Homological algebra on a complete intersection, with an application to group representations*, Trans. AMS 260 (1980), 35–64;
Buchweitz, *Maximal Cohen–Macaulay Modules and Tate Cohomology*, AMS Mathematical Surveys and Monographs 262; Orlov, arXiv:math/0302304v2。
コード `computations/verify_a1_stable_model.py` はB²、Hilbert–Burchの恒等式とPoincaré級数を検査し、MCM性・Exactnessや安定圏同値の証明は置き換えない。

## 特異点idealに対する境界gluingの跳び

Du Val点xは滑らかな反標準楕円境界Eから離れている。
従ってI_xの導来restrictionはO_Eであり、I_xはRΓ(I_x)=0から
Bbar=O_Sbar^perpに属する。Dbar_qにおける像J_x,qと付加した
exceptional対象ebarについて、指定gluingの定義そのものから
RHom(ebar,J_x,q)=0、RHom(J_x,q,ebar)=RΓ(E,q) が成り立つ。
非自明な次数0線束qでは H^0=H^1=0、自明線束では H^0=H^1=k。
ゆえに非自明qでこの二対象は両側直交し、古典点でだけExtが跳ぶ。
本文の証明は `prop:duval-ideal-boundary-gluing` にある。

これはqによらない同じJ_xの自己Extとは異なる、exceptional側に
結び付くgluingの情報である。I_x一対象に対する両側直交から
Dbar_qの直積分解、全てのBbarに対するgluingの消滅、
非自明qでのDb(qgr R_q)同値を推論してはならない。
先行する一般gluing理論の再適用であり新規性の網羅的確認は未了。
次はA1壁で他のBbar生成対象も含めてこのgluing bimoduleを
調べ、qgr側の像と積を比較する。

## 残課題

一般qのDbar_q→Db(qgrR_q)の完全忠実性・本質的全射性。まずA1壁のI_xと生成対象の間の全Extと積を比較する。coherent有限性は解決したので、それを次の課題として反復しない。指定heartでのK_C,qの位置、壁上AS比較、局所・完成代数、複数壁、曲面族の相対化は別問題として残る。

## 一次資料と検証範囲

- Rains, *Filtered deformations of elliptic algebras*, arXiv:2107.13540v2, §4 (4.4)–(4.7), Proposition5.1と(5.3)。標準gluingと中心元を確認。https://arxiv.org/abs/2107.13540
- Keeler, *Criteria for sigma-ampleness*, arXiv:math/9912051v2, Theorem1.2(1),(2)。有限位数を除外しない左右noetherian性。https://arxiv.org/abs/math/9912051
- Bondal–Kapranov–Schechtman, *Perverse schobers and birational geometry*, arXiv:1801.08286v1, Theorem2.14、§2F。fiber次元≤1の局所化定理。https://arxiv.org/abs/1801.08286
- Dolgachev, *Classical Algebraic Geometry II*, author draft 2025-08-10, Theorem8.3.2と§8.3.2；Drinfeld math/0210114v7, §§1.2–1.3,1.6；Seidel–Thomas math/0001043v2, Propositions2.10,2.12–2.13。既存の零壁入力。
- Donovan–Wemyss, *Noncommutative enhancements of contractions*, Adv.Math.344(2019),99–136。与えられた幾何学的収縮を出発点とする点を区別する。

今回追加した特異点idealとexceptional対象のgluingは定義からの直接計算として本文に証明を記載し内部点検した。以前の新しい証明も内部点検済み。一次資料の関連定理・証明を読んだが、PDF screenshotはCache missで失敗したものがあり、全引用ページの画像確認とはしない。網羅的新規性、独立査読、形式化は未実施。改稿4節を20ページ抜粋としてLuaLaTeX組版し全ページのレイアウトを確認した。全文組版・既存21計算の再実行は今回未実施。再開時の全文検証は `bash scripts/check.sh all` と `bash scripts/check.sh tex`。
