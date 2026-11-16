# 四つのheartの比較：現行研究ノート

2026-11-16 / hearts-v24。最初に `research/four_hearts_plan.md` を読む。現行原稿は `papers/nc_del_pezzo_hearts.tex` と九つのsection、検証状態は `research/four_hearts_validation.json`。証明が本文にある事項は所在と入力を示し、全文を重複させない。GitHub mainが正本で、保存成功時にはLibraryへ別途アップロードしない。

## 現在の中心結果と再開点

`four_hearts_elliptic_coefficients.tex` でactual normalized decupleの全potential、十一条件の楕円表示、共通領域のnoetherian性と標準heart一致を証明した。以前の「potentialとnoetherian適用域を計算する」という課題はこの範囲では解決済み。次は一般位置外の実在する壁で、どの入力が残り、実際にどの対象・heartが変わるかを確認する。相対heartや全potentialへの拡張を先取りしない。

## 規約と確実性の区別

VdBはraw blow-up heart、Rainsは指定blowdown/gluingのt構造、反標準は指定eとs=S^{-1}[2]のorbit環のqgr、ASは三次元AS正則Z-algebraのqgr。AS helix全体と一頂点のorbit、AS次元3とambient AS4、Z-algebraと一周期graded algebraを分ける。有界heartの存在はrealization Db(heart)→ambientの同値を含意しない。

pointed同値はeとsへの両立を含む。境界、rank、marking、族の降下は別入力。右加群の積はab=s^{deg b}(a)∘b。境界非交叉の有限長Serre圏Zの内在的Db(Z)を、そのcohomologyを持つambient充満三角部分圏D_Zと同一視しない。特にΠ(A2)内部の高次Extの二周期性はambient Ext^{>2}=0と異なる。

## 楕円potentialの明示式と元の六点

基礎体C、E=C/(Z+tau Z)、thetaは奇Jacobi関数。degree d、Abel和lambdaの線束を標準のautomorphy factorで表す。liftの変更は矢と関係の基底の変更になる。x_b=p_b、y_c=p_{3+c}、X=Σx、Y=Σy、L_iのAbel和ell_iとし、u=X−ell0、t=ell1−Y。

actual decupleはA0=O、A1=(L0L1)^−1(Dx+Dy)、A2=L0^−1(Dx)、B_b=O(x_b)、C_c=L0(−y_c)。条件(U+)はu,t,u−tが非零。全potentialは矢・関係の基底を選んで

    w_abc = theta(y_c−x_b+t_a),    (t0,t1,t2)=(u,t,0)

となる（thm:theta-potential）。Hom(A_a,B_b)とHom(B_b,C_c)の切断の積をdegree2 section f_b(z)=theta(z−r_b)theta(z−d+r_b)と書き、係数theta(r_{b+1}−r_{b+2})theta(r_{b+1}+r_{b+2}−d)を掛けて和を取る。r1,r2,r3の三零点から恒等的に零となる。これが全パラメータの証明で、有限個の値の補間ではない。

Q_bc=w2bc/w1bc=theta(y_c−x_b)/theta(y_c−x_b+t)。これは行・列rescaling類としてL0に依存しない。L1の切断h_c(z)=theta(z−y_d)theta(z−y_e)theta(z−y_c−t)は最後の三点を座標点にする基底である。G(z)=∏theta(z−y_j)で割るとh_c(x_b)/G(x_b)=Q_bc^{-1}。従って元のL1六点の座標行列PがP~(Qentrywise-inverse)^tを満たす（thm:original-six-points）。一般位置ではC=B/BpBが同じ六点の可換三次曲面cornerに一致する。一般位置外の幾何的helixを無条件には主張しない。

零条件は以下で尽くされる（cor:elliptic-discriminant）。

- w2は六点相異性から全て非零。w1bc=0 iff L1=O(x_b+Dy−y_c)：一つの前半点と二つの後半点。
- Qのminor(b,b';c,c')=0 iff L1=O(x_b+x_b'+y_e)、eは残る後半index：二つの前半点と一つの後半点。
- det(Qentrywise-inverse)=0 iff L1=O(Dx)。detQ=0 iff L1²=O(Dx+Dy)。後半三点の共線はt=0であり(U+)で排除。

したがって十八非零と十一条件は入力六点のL1一般位置に等しい。w0bc=0 iff L0=O(Dx−x_b+y_c)で、一般位置でも起こり得るがcornerには影響しない。全27係数のtorus chartに限定する必要はない。elliptic Cauchy/Frobenius恒等式自体は既知であり、新しい点はactual関係係数と入力六点との同定・heart比較への接続である。

## Ampleな構造対象からのnoetherian再構成

命題prop:ample-helix-noetherianの入力はHom有限noetherian heart H、有限homological dimension d、AZ-ampleな(e,s)と全対象への高次Ext tail、eをfoundationに含むfull very strong周期helix。very strong性からHom(e,s^nE_i[k])がk≠0で消え、標的heartの認識により各E_i∈H。T=⊕E_iについてExt^{>0}(T,s^ne)=0も得る。

任意Mへのeの負twistからの全射をd回取り、核K_dまでの有限exact列を作る。高いtwistで各有限個のP_jへのExtを消し、Ext^k(T,s^nM)=Ext^{k+d}(T,s^nK_d)=0とする。e⊂Tなので生成性もあり、(T,s)はAZ-ample。graded右idealの像がnoetherian対象Tの部分対象として安定することを用いた直接のnoetherian証明を本文に収め、AZ再構成からqgr B_T=Hを得る。full strongだけでは足りず、very strongが必要。

規格化Psi+によって標準AS very strong helixをDb(qgrF)へ運ぶ。qgrFはnoetherian、Hom有限、hdim2、標準Oとshiftがample。上記命題の入力はAS標準heartのt-exactnessやnoetherian性を前提にしていない。既存の標準AS実現でorbit algebra=Jacobi B(W+)を同定すると、B(W+)の右noetherian性とqgr A+≃qgr Fを得る。foundationとその全End作用を保存するので、dg Yonedaにより指定Psi+そのものがt-exactである（thm:normalized-abelian）。任意potentialのnoetherian定理ではない。

## 右加群の共通辞書とmutationのshift

VdB (5.4),§10の規約：S+(M)=sigma_*(M tensor L0)、逆はsigma*M tensor L0^−1。L1=sigma*L0なら初期O(−1),O(−2)のrestrictionはL0^−1,(L0L1)^−1。VdB Theorem6.3.1(1),(4)と随伴でLj*Lalpha*=Lbeta*Li*、Proposition9.1.8/(9.11)でLi*Rdelta*=Rdelta_E*Lj*。各境界同型を使って運ぶと最終Orlov tupleは(k_pi,U2,U1,O)となる。

Rains復元：rank u,c1=D,c=chi(e,x)に対しdetFq(x)=rho(D)q^(c−u)。q=P_aなら境界反Serreはt_(a*)(−tensor rho(H))。actual tupleからq=U2U1^−2、L=U1U2^−1。forward RHomと合成を保存する境界関手を使い、Rains (4.11)の三角dg模型を復元する。右規約ではq=L0/L1、L=L1（thm:right-dictionary）。sigma p_iのL0一般位置はp_iのL1一般位置に等しい。境界作用だけからのL=L1 epsilon、epsilon∈E[3]の九候補は、初期twistを固定するとepsilon=Oに決まる。

印刷tuple L0^−2L1、L0^−5L1³は別のS−(M)=L0 tensor sigma*Mの負twistから出る。これをS+の正shiftと同一視するとQ²=Q³=Oという障害がある。本稿は明示したS+構成を採り、原典の全記号の正式な読み替え・著者訂正を確定したとはしない。

左mutationはcone、逆右mutationはcone[−1]。点を線束Mの右へ動かすとM(p)、degree−2線束MをOの右へ動かすとM^−1[−1]となる。R6^-R7^-R8^-の後の末尾三対象へ[1]を明示してsheaf-normalized列を得る。標識Oの位置は9,9,9,6,6,3,1。最後の二つの評価triangleが零になるactual条件(R)はU2(D6)≠O、U1(D123)≠O。

normalized decupleは(O,(L0L1)^−1(D6),L0^−1(D123);O(p1),O(p2),O(p3);L0(−p4),L0(−p5),L0(−p6))。相異なる六点の下でadmissibilityは(U+)の三条件に等しい。これにより(R)も成立し、AOU §7/§9の方法で構成したA+とPsi+はpointedとなる。未変更の印刷decupleからの代数と同一視しない。

逆に(O,A0,B0;K1,K2,K3;C1,C2,C3)からO(pi)=Ki、L0=K1K2K3/B0、O(p3+j)=L0/Cj、L1=O(D6)/(L0A0)、q=L0/L1。translation sigmaを入力に持たない逆復元では、sigma*L0=L1の解はE[3]の九選択となる。初めからsigmaを固定したepsilonの問題とは別。全moduli stackの九対一同型ではない。

## Rains・VdB・反標準比較と共鳴の知識

証明は `four_hearts_geometric.tex`、`four_hearts_canonical_comparison.tex`、`four_hearts_root_chambers.tex`。同じ初期heart・中心・gluing・blowdownを同定したVdB/Rainsはpseudo-canonical認識によりt-exact。VdB最後のRdelta_*は構造対象とSerre作用を保ち、section右随伴omegaとpi Romega=Idを使って自然な反標準導来切断に同定される。環の同定と右作用も固定する。rawと各段階のsection-model置換を混同しない。

genuine smooth classical avatarとsmooth Eの指定gluingでは、全qの自然Phiが導来同値。Indでのorbit生成、境界trace非零、source smooth proper/飽和性の三段階を用いる。無限位数にはRSS Proposition2.4（degree1を含む）、有限位数にはYZのPI・dualizing持上げ・chiの三定理。全Rains heartの振幅[0,1]、T=ker H1Phi、F=ker H0Phi、反標準heartは〈F[1],T〉。

q非torsionでは全F⊂Z。PhiM=U[−1]の両境界restrictionの振幅からi*U=0を得て、中心gの高次全射の次元安定化からg可逆・有限次元局所化となる。従ってt-exactness iff AZ-ample iff全実在Z単純のchi(e,S)>0。数値共鳴だけとの同値ではない。T∩Zは全非零商の正値、F∩Zは全非零部分対象の負値で認識される。総Euler値だけでは足りない。

Z単純はH⊥の負定値性とEuler偶奇から根類を持つ。同根の異なる単純はEuler矛盾、根は有限で、正負係数に分けた関係と有効錐のpointednessから単純根は独立。有限ADEの単純tiltを全heartへ延長でき、各段階の残余Fは境界非交叉にとどまる。負の単純を反射する回数は初期負正根数、終端heartは経路に依存しない。合成自己同値の同型まで主張しない。

実在入力はRains2022 §4 pp34–35の指定blowdown単純根のq冪restrictionによる有効性と、2019稿§11 p141のProposition11.23直前の有効単純根自身に対する存在記述。Proposition11.23のnef仮定を単純根へ誤適用せず、任意の数値共鳴根の実在に拡張しない。

pi=Ni q、相異なる正整数、3≤r≤8では全根指数非零でgenuine。整列nu1<…<nurの後の全simple次元は(nu1+nu2+nu3,nu2−nu1,…,nur−nu_(r−1))、手順回数はinv(N)。同じ無順序点のr!順序heartは埋め込まれたheartとして相異なり、昇順のみ反標準と一致する。抽象abel圏としての非同値や全heart数の分類ではない。

整数倍点をL1=O(3o)、L0=L1q、3b=aのsigma=t_bで実現すると(U+)の三比はq^(N1+N2+N3−1)、q^(N4+N5+N6)、q^(ΣNi−1)。今回の共通領域定理からAS+は反標準heartと一致する。例(1,3,2,5,7,11)ではRainsから一手、simple次元(6,1,1,2,2,4)、一次元二個。作用行列やannihilatorの生成元は未計算。

## 混合A2と別稿の役割

混合A2の非分裂P:0→S−→P→S+→0はrank delta=min(p,n)、cohomology=((p−n)+,(n−p)+)。逆拡大Qは(p,n)。Serre部分圏はmod_fd Pi(A2)で四直既約。指数2,−1では反標準側の異なるcharacter W,Uと非分裂2次元Vを得て、逆拡大V'を合わせA/Ann(V⊕V')=Pi(A2)。この商はhomological epimorphismでない。一般E型の有限次元加群圏をPi(E)と同定していない。

`cubic_heart_corner.tex` は十一条件、一様C7=0、C6非零、Hilbert値(8,21,33,38,33,21,8)、総次元162を保持する。本比較稿は有限性の証明を自立して含むが、一様Hilbert関数の詳細は別稿に残す。道長と反標準cut次数はell=3cut+block(end)−block(start)で区別する。

`nc_del_pezzo_resonance_hearts.tex` は全次数最大数値共鳴、E[3]九選択、zigzag形式性と固定dg圏のframed分枝を保持する。cubicの32個の5次元formal分枝は曲面モジュライ成分ではない。weak(-2)曲線のEuler零の導来的消失は、非零負指数が[−1]に残る現象とは違う。

## 先行研究・検証上の限界

今回の新規入力はAOU (4.7),§7の関係からpotentialへの構成、OU Definition3.1と(3.9)–(3.10)のvery strong標準helix、AZ Theorem4.5とPolishchuk math/0212182v4 Theorem2.4の再構成、Prokofev–Zabrodin 2305.02837v1 (1.7),(2.1)のelliptic Cauchy公式。AOUのprimary HTML、OUとPZの該当PDFページ画像、Polishchukの定理・証明本文を確認した。Polishchuk PDFのscreenshotはCache miss。AZ原典の全文PDFは取得できず、原典書誌、Polishchukと研究論文の定理再掲で照合し、必要なnoetherian部分の証明は本稿に明示した。

Rains2025 monographは今回も全文取得ができず、書誌・概要以上の全面照合を行っていない。外部独立査読、Lean等の形式化、網羅的新規性調査も未実施。今回保持した過去の全数学的証明を改めて独立再監査したという意味ではない。

新コードverify_four_hearts_elliptic.pyはF_1009上のy²=x³−x+1のMiller関数から実際のHom切断を作る。24一般位置六点×3つのL0と四壁を採用し、684個の関係を関数体で交差乗算して検証、L0独立性と射影座標とのgauge一致を確認した。有限体の点はtorsionであり、非torsion条件や複素圏の存在の証拠ではない。六つの旧コードも現行入力で再実行した。生成、全文組版、ページ画像点検、清浄ディレクトリでの再現、GitHub保存はvalidationで別々に報告する。
