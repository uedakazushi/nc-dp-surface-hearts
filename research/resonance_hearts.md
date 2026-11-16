# Rains resonance と anticanonical heart：研究継続ノート

2026-11-16 / resonance-hearts-v8。最初に `00_research_plan.md` を読む。現行原稿は `papers/nc_del_pezzo_resonance_hearts.tex`、証明はそこからinputされる七つのsectionにある。中心は `resonance_mixed_a2_category.tex` と `resonance_global_heart.tex`。GitHub mainが正本であり、保存成功時はLibraryへ保存しない。一般原則と保存許可は上位方針に記す。

## 1. 現在の到達点と再開の核心

**指定genuine楕円gluingの導来比較は点検済みの入力となった。** 滑らかな可換genuine del Pezzo S、滑らかなE∈|−K_S|、q∈Pic0(E)からのRains gluingに対し、自然なΦ=πRΓ*はDb(Rains heart)≃Db(qgr R)。これは[次数1の反標準モデル原稿](https://github.com/uedakazushi/nc-dp1-moduli/blob/main/papers/dp1_anticanonical_models.tex) の主張であり、今回orbitのInd生成、境界traceの非零性、有限/無限位数双方の環の有限性、source飽和性を一次資料と照合した。独立の外部査読や機械形式化とは区別する。

**全heartの比較**：この範囲で全Rains heart上のΦの振幅は[0,1]。T=ker H1Φ、F=ker H0Φはtorsion pairで、反標準heartを戻すと〈F[1],T〉となる。q非torsionなら境界外Serre部分圏Zにも制限し、T∩Z=ker Ext1(e,−)、F∩Z=ker Hom(e,−)。全任意nc del Pezzo、weak avatar、特異境界や非局所自由gluingに拡張したわけではない。

**任意の混合指数**：隣接根の指数p>0,−n<0の非分裂拡大Pはrank δ=min(p,n)、(h0,h1)=((p−n)+,(n−p)+)。この証明は導来比較に依存しない。二根部分圏の四直既約と全cohomology、両chamberのtorsion pairも決定した。

**指数+2/−1のアフィン作用**：二つの一次元加群W,Uは異なるcharacterを持ち、0→W→V→U→0は非分裂。二次元Vへの作用像は全三角行列代数。逆向き非分裂拡大V'を合わせるとA/Ann(V⊕V')≃Π(A2)という四次元商を得る。二つの新単純の根類はalpha+beta,−betaで、局所Weyl反射に対応する。

**未解決の具体的着手**は、楕円データからA=R/(g−1)の生成元を固定し、この商写像の係数chi_W(a),chi_U(a),eta(a)を求めること。character分離や非分裂性の真偽を再び未解決としない。差分作用素模型または根sheafのHomへの作用から、各生成元の二つのcharacterと両拡大の非対角係数を求める。次の構造課題は全E6境界外圏のアフィン作用、VdB/AS heartとの指定同定、相対familyと退化境界である。

## 2. 規約と符号別Ext

θ=S[-2]、τ=θ^−1、境界triangle θM→M→i_*Li^*M、構造line bundle e、R=⊕Hom(e,τ^n e)、中心正則g∈R1、A=(R[g^−1])0=R/(g−1)を使う。qの向きは `Li^*M=0 ⇒ O_E(alpha)⊗q^m=O_E`、m=chi(e,M)、従ってrho(alpha)=q^(−m)。数値的共鳴だけからsheaf存在を補わず、Rainsのsimple-root effectivity/既約sheaf存在を入力とする。

実在する既約純一次元root sheaf M、alpha²=−2、alpha K=0、Li^*M=0に対し、全nでHom(e,τ^nM)の次元=max(m,0)、Ext1=max(−m,0)、Ext2=0。Mは2-spherical。Φ(M)はm>0でm次元A加群、m<0で(−m)次元A加群[-1]、m=0で零。負指数はRains heartのAZ失敗とpointedなheart非一致を検出する。指定genuine楕円gluingでは導来同値は保たれる。

証明は `resonance_sign_trichotomy.tex`。m≤0はe→Mのimage Iと零次元cokernel Tを使い、Rains Cor10.16のchi(I)≥1とProp7.6のchi(T)≥0でHomを消す。正指数は反変ad双対（Cor5.9,7.26,7.30,7.31、Prop7.16）で指数を反転する。自己ExtはCor7.13とEnd=kから得る。**既約性だけから全射性は従わない**。非torsionかつ境界非交叉の場合の単純性は別の補題である。

R/gR=B(E,L,σ)、degL=dと中心正則gからdimR_n=1+d n(n+1)/2。共鳴でHilbert関数は跳ばない。genuine avatarでは零指数根共鳴はなく、weak del Pezzoの(-2)曲線の反標準収縮とは異なる。

## 3. 境界外Serre部分圏と拡大

Z={M | dimM≤1,Li^*M=0}ではτM=M、Ext^j(e,M)はj=0,1だけ。g周期的Extの局所化V^jは有限次元A加群で、短完全列は6項A線型完全列

`0→V0(M1)→V0(M2)→V0(M3)→V1(M1)→V1(M2)→V1(M3)→0`

を誘導する。一般の混合拡大0→M−→M→M+→0でconnecting rankをrとすればh0=m+−r、h1=−m−−r。δ同型なら非零Mが消える。weak del PezzoのEuler列O(−2)→O(−1)^2→Oは古典的完全相殺模型であり、genuine非可換での存在例ではない。

異なる既約根alpha,betaについてHom=Ext2=0、dimExt1=alpha beta。交点負なら同時存在不可、0なら拡大無し、1ならExt1=k。genuine avatarで交点1かつm_alpha+m_beta=0の同時共鳴は、alpha+betaが零指数根になるため不可能。

q非torsionでは境界外sheafの零次元商はない。商Zにi^*Z=0が従い、θZ→Zは同数値類間の全射なのでCor7.7により同型。determinant q^ellと非torsion性からell=0である。従って既約境界外root sheafは全heartで単純。Hnef、H²>0の下、部分商のH次数とθの数値作用からZはSerre部分圏。Prop7.32のfinitely partitive性とnoetherian性で有限長となる。単純対象のD=c1はH⊥の負定値性、偶奇、−D²=2−dimExt1からD²=−2。最大共鳴で全単純根が実在すれば、Zの単純はちょうどr個。

全Zのtorsion pairは現在、指定genuine gluingでは大域比較から得られる。それ以外の境界・avatarについて同じ結論を仮定しない。

## 4. 全次数の最大数値共鳴

滑らかな平面三次Eのflex oを原点、qを非torsionとする。r=9−d、S=Bl_(p_i)P²でrho(ah−Σb_i e_i)=O_E(3ao−Σb_i p_i)。単純根alpha0=h−e1−e2−e3、alpha_i=e_i−e_(i+1)に対する整数m0,…,m_(r−1)から

`3p1=(m0−2m1−m2)q`, `p_i=p1+(Σ_{j<i}m_j)q`

と復元する。p1はE[3]の9通り。全根共鳴は単純根共鳴と同値で、全根指数非零がgenuine条件に等しい。

相異なる正整数N_iの倍点p_i=N_iqでは全根指数が非零。d=6,…,1の根系はA2+A1,A4,D5,E6,E7,E8、根数8,20,40,72,126,240。各E^rでZariski denseであり、N1<N3<N2を課してもdense。全ncモジュライの全成分に対する主張ではない。大小制約の密度は整数行列式−1のE³自己同型(u,v,w)→(u,u+v+w,u+v)から得る。

根の分類はΣb_i=3a、Σb_i²=a²+2による。a=0は差根、a=1は三点、a=2は六点、r=8ではa=3の(2,1,…,1)型もある。Cauchy–Schwarzで|a|≤4、b(b−1)≥0からa=4は不可能。正aの指数は正係数和、差根e_i−e_jの指数はN_j−N_i。滑らかな反標準曲線の存在からHnef・big、非ampleなら有効(-2)曲線がEに制限して自明となり矛盾する。完全証明は `resonance_maximal_a2.tex`、`resonance_maximal_all_degrees.tex`。

具体例N=(1,3,2,5,7,11)、単純根指数(6,2,−1,3,2,4)、alpha=e1−e2は+2、beta=e2−e3は−1、交点1。Rainsの入力により同じheartに両sheafが実在する。全72根の数値共鳴を全72向きの既約sheafの存在と混同しない。有理数例E:y²=x³−x+1、q=(0,1)では2q=(1/4,−7/8)によりNagell–Lutzで非torsion。20個の三点行列式とconic行列式、72根指数の非零性は既存の厳密算術証明書にある。

## 5. 既約根、zigzag、形式変形

最大共鳴で全r単純根sheafが実在するとき、非単純正根gammaにはgamma alpha_i<0となるiがあるためExt1の非負性に反する。負根は有効錐のpointedness（Prop7.19）に反する。同根の指数はq非torsionで一意、Euler値2とCor7.7からsheafも一意。既約sheaf数はd=6,…,1で3,4,5,6,7,8。

T=⊕M_iのgraded ExtはDynkin zigzag Z(Delta)。次数別次元はr,2s,r、全次元は8,14,18,22,26,30。Serre pairingが往復積を非零にし、他の長さ二の積は零。Liu–Wangの既知のintrinsic formality（J. Algebra 677 (2025), Thm1.1, arXiv:2301.06757v3）を使い、固定dg圏のframed変形は辺ごとのx_ij x_ji=0になる。木の葉からの消去でイデアルを同定し、2^s個のs次元分枝。d=6,…,1の分枝数2,8,16,32,64,128。全曲面の相対変形や全モジュライの成分ではない。

形式性だけから自然関手のA∞-module構造は決まらない。現在の最大rankと導来完全忠実性は、形式性とは独立の議論で得ている。係数付きの具体的A∞-module模型はなお有用な未計算情報である。

## 6. 任意正負指数の混合A2

指数p,−n（p,n≥1）の隣接根S+,S−に対するP:0→S−→P→S+→0と逆向きQを取る。非零e→Pは単純性と非分裂性から全射。その核Lはrank1 torsionfree、c1=−gamma。Rains Cor10.12とH(K+gamma)=−dからExt2(e,L)=0、従ってh1(P)=0となる。p>nでは必ず非零e→Pがありδは全射、p≤nでは非零e→Pを仮定するとEuler値に矛盾してδは単射。よってrankδ=min(p,n)。p>nでchi(L,L)=3−2(p−n)なのでLがlineとなるのはp−n=1だけ。

C=〈S+,S−〉_Serre≃mod_fd Π(A2)、直既約S+,S−,P,Q、Hom表は順に

`[[1,0,0,1],[0,1,1,0],[1,0,1,1],[0,1,1,1]]`。

ambient Ext1はS+,S−間の両向きのみ一次元。P⊕QがCのprojective generator。quiverをx:U+→U−、y:U−→U+、xy=yx=0とすると、重複度は(a−rankx−ranky,b−rankx−ranky,rankx,ranky)。r=min(p,n)、t=rankxとして全対象でh0=pa−rt、h1=nb−rt。

p>nでは(T,F)=(add(S+,P),add(S−))、p<nでは(add(S+),add(S−,P))。p≠nなら全非零対象は消えず、p=nの仮想場合では核add(P)となる。genuineではp=nの同時共鳴は不可能。P,Qは同じEuler値p−nを持つが、Qのcohomologyは(p,n)で二次数に残る。

内部Ext_C^(2j)(S+,S+)=kはambient Ext_X^>2=0と異なる。Db(C)→Db(Rains)は完全忠実でない。abel圏の分類をambient三角圏の同定へ読み替えない。

## 7. 導来比較の監査と全heartのtilt

`resonance_global_heart.tex` に完全な論証を置く。監査の要点は以下。

- RainsのgluingはB=O_S^perpにeを付け、RHom(M,e)=RHom_E(Li*M,q)、Fq|B=Li*(−)⊗q^−1、Fq(e)=O_E。S genuineかつE smoothが範囲。
- R=gのRees環は中央正則元と楕円THCR商を持つ。gr_gR=B[g]から整域・左右noetherian。σ無限位数ではRSS Prop2.4がdegL≥1で適用可能。有限位数ではBがPI、YZ Th5.13→5.1(1)→4.5でbalanced dualizing、chi、有限local cdを得る。target全体のsmoothnessは前提にしない。
- 全orbitに右直交するInd対象は境界でも零となりBに入る。古典的実現GはRΓG=0、Li*G=0。S\EがaffineなのでG=0。compact内だけでなくInd全体で直交を消してthick生成を得る。
- sourceとtargetのorbit Extは次数0と2だけで、targetのpairingはRains Cor3.8。非零u∈H1(E,O_E)を実際の境界自己拡大で表し、Φが同じuへ送ることからtraceが非零。Yoneda積との両立性で全orbitのRHomが同型となり、完全忠実性を得る。次元一致だけからA∞構造を推測しない。
- sourceはsmooth properなperfect gluing。Orlovのpseudo-perfect=perfect/表現可能性で右随伴を得て、counit coneをtargetのample orbitとSerre消滅で消す。target smoothnessやthick生成を先取りせず全射性を得る。

全heartの振幅は、line bundleの有限直和からMへの全射とExt2(e,τ^nM)=Hom(M,θ^(n+1)e)*で示す。後者はn≫0でH次数が負になるline間Homへ単射し零。従ってdegree2の生のExtは有限内部次数にしかなくπで消える。中間t構造のHRS対応から全heartのtorsion pairを得る。境界外ではg周期性でkernelをHom/Ext1で記述できる。任意のMに生のExtの各次数消滅を同一視しない。

## 8. 異なるcharacter、非分裂表現、四次元商

p=2,n=1ではW=ΦP、U=Φ(S−)[1]は一次元、V=ΦS+は二次元。中央局所化のexact完全忠実右随伴とcoherent格子により、有限次元A加群間のambient Ext_Aはqgr側のExtと全次数で一致する。

Hom_A(W,U)=Ext1_X(P,S−)=0からW≄U。非零包含S−→Pは非零Ext1_A(U,W)へ移るので0→W→V→U→0は非分裂。作用像は全下三角代数。行ベクトルではrho(a)=[[chi_W(a),0],[eta(a),chi_U(a)]]、eta(ab)=eta(a)chi_W(b)+chi_U(a)eta(b)。Hom_A(V,U)=k。

W,Uはともにspherical、cross Hom/Ext2は零、cross Ext1は両向きk。逆向き非分裂拡大V'もあり、二characterが生成するSerre部分圏はmod_fd Π(A2)。両表現への作用像は共通対角と両非対角cornerを持つ四次元代数全体なのでA/Ann(V⊕V')≃Π(A2)。これは単なるMorita同値より強い商環の同定である。ただし商写像はhomological epimorphismでない。商の高次Extは二周期、ambient Ext_Aは次数>2で零。

K群ではWの根はalpha+beta、Uの根は−betaで、s_beta(v)=v+(v beta)betaが(2,−1)を(1,1)へ移す。これは二根部分系の局所反射であり、全E6 heartを一つの反射で記述したとは主張しない。実際の楕円生成元に対するchi_W,chi_U,etaおよび商のkernelの生成元は未計算。

## 9. 文献・再現・検証範囲

Rains 2019：arXiv:1907.11301v1、Theorem4.30と§5のgluing/heart、§7の数値・次元、Theorem9.10のline生成、Cor10.12のrank1射、Prop10.13のline等号、§11の根sheaf。Rains 2022：arXiv:2107.13540v2、Cor3.8とtraceの証明、§4 (4.4),(4.7)とnef性、Prop5.1。RSS *Noncommutative Blowups of Elliptic Algebras*, arXiv:1308.2216v2, Prop2.4。YZ *Rings with Auslander Dualizing Complexes*, J.Algebra213 (1999)1–51, arXiv:math/9804005v3, Th4.5,5.1(1),5.13。Orlov *Smooth and proper noncommutative schemes and gluing of DG categories*, arXiv:1402.7364v5, Th3.18,3.25,Cor3.19。これらの関連一次本文を今回照合した。原典web PDF screenshotはCache missで取得できなかったため、画像確認したとはしない。Liu–Wangの既存形式性入力は今回再監査していない。

再現：

    python3 computations/verify_resonance_mixed_a2.py
    latexmk papers/nc_del_pezzo_resonance_hearts.tex

新しい検算は厳密有理数で40,000通り（正指数和17,500、負指数和17,500、balanced仮想場合5,000）、Hom/Euler/Ext、四次元商の行列積、各三角像の次元3、commutant次元4、局所反射を確認した。sheaf存在と導来比較は数学的証明であって計算証明ではない。更新二節の独立driverをLuaLaTeXで9ページに組版し全ページを点検。主原稿全文の組版、旧四スクリプトの再実行、独立査読、網羅的新規性調査は今回未実施。詳細と保存されたsource hashは `research/resonance_hearts_validation.json`。
