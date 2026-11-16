# 最大共鳴と零指数壁：現在の知識

2026-11-17 / hearts-v27。最初に `../00_research_plan.md` を読む。完全な証明は主論文の `four_hearts_maximal_density.tex` と `four_hearts_zero_walls.tex` にあり、ここでは依存関係・障害・次の着手を記す。以前の `current_assessment.md` と個別validationはv26までの実施範囲であり、今回の状態は `resonance_walls_validation.json` を参照する。

## 1. 最大共鳴

固定した滑らかな平面楕円E、flex原点、非torsion q、3≤r≤8で、全根共鳴は単純根指数m_iの整数表示

    3p1=(m0−2m1−m2)q,  pi=p1+(m1+...+m_(i−1))q

と同値。方程式の解は、相異性・genuine性を課す前にはE[3]の九選択となる。相異点の範囲で全根指数非零がgenuine条件に等しい。正整数倍点pi=Ni qは差根と正次数根の明示列挙から全根指数非零。任意の厳密な整数順序を課しても、正整数の累積和を表すunimodular群自己同型からZariski稠密となる。

既存 `thm:sorted-spectrum` を使うと、昇順のRains heartは反標準heartと一致し、N1<N3<N2では負指数単純が実在して一致しない。両集合が稠密なので、固定楕円chartで一致条件も不一致条件も構成可能ではない。相対t構造や一様なkernelを持つ族は構成していない。この点ごとの結論を、そのような追加仮定下の開性と混同しない。

数値共鳴根の個数は8,20,40,72,126,240だが、同じheartの既約root sheaf数ではない。反標準環のHilbert関数の跳びを意味しない。

## 2. 零指数壁の既知模型

十八係数非零chartの十一因子は、十の共線根と一つのconic根。一般壁の可換blow-upでは一つの(-2)曲線Cが反標準収縮でA1点へ縮む。K_C=i_*O_C(−1)は2-spherical、全反標準twistに直交し、Rf_*で消える。任意次数の弱del Pezzoにも同じ障害がある。特異モデルの剰余体の高次Extは無限に残るため、滑らかなSのDbとその反標準qgrのDbは同値ではない。

Q0=((1,1,1),(1,2,2),(1,3,4))の六点・反標準三次式・nodeとHessian−2304を主論文へ収録した。P1のEuler列O(−2)→O(−1)^2→Oも、正負指数の完全相殺を表す。ただしこれは可換同一曲線類の模型で、genuine非torsionの異なる隣接根の対ではない。

## 3. 弱楕円gluingの核定理

Sは滑らかな射影有理弱del Pezzo、Eは滑らかな反標準曲線、d=K_S²>0。B=O_S^perpとし、Rainsの標準dg gluingでeをRHom(M,e)=RHom_E(Li*M,q)によって付ける。Fq(e)=O_E、Fq|B=Li*(−)⊗q^−1、theta→id→i_*Fq、Fq s=Psi Fqを使う。qの位数制限はない。

f:S→Sbarを反標準収縮とすると、

    Nq-tail = Nq = iota_q { G∈Perf(S) : Rf_*G=0 }

を得る（`thm:weak-orbit-kernel`）。ここでNqは全整数のs-orbitに右直交する対象、tailは各cohomological degreeについて十分高い正twistでHomが消える対象。

証明の要点は、tail消滅→境界の正次数orbitによる検出→FqX=0→sX=X→X=iotaG、RΓG=Li*G=0、という順序。古典的Cartier triangleでG(nH)=Gとなり、反標準収縮の射影公式とSbar上のample twistのSerre消滅からRf_*G=0を得る。逆向きは収縮外での同型とEの例外配置からの非交叉による。コンパクト対象内の直交の消滅だけからthick生成を推論していない。

iota_qはdg完全忠実なので、核の全RHomと合成はqによらない。任意の(-2)曲線のK_Cをiota_qで送ることで、全qに実在する零指数2-spherical対象を構成する。任意のRains heartでのsheaf性はこの構成からは従わない。

## 4. 証明済みの帰結と追加仮定

- coherentなPhi=πRΓ*が定義され、各次数付きExtが有限生成・有界でcohomologyを計算するなら、ker Phi=Nq。追加仮定付きの `prop:weak-coherent-kernel`。
- Qq=(Dq/Nq)^naturalは圏論的な収縮候補。orbit対象と核はSerre双対性によって両側直交するため、局所化はorbit間の全Hom・合成を変えず、反標準環Rを保存する。B側の商と降下gluing moduleでも記述できる。
- K_C,qのspherical twistは全orbitで自然に恒等となり、Rへの作用は恒等。Phiが定義されKを消すならPhi T_K=Phi。ADEのbraid関係は既知のspherical twist定理を使う。
- 非genuineなら、標準pairがAZ-ampleで一様な高次Ext消滅を持つ有界heartへのpointed導来同値はない。構造対象を忘れた全抽象的同値の不存在ではない。

核の同定は、商とDb(qgr R)の同値を証明していない。Qqのnoetherian heart・proper性・Serre関手の存在も未証明。これらを本節の成果に含めない。

## 5. 非torsionの明示的零壁

E=C/(Z+iZ)、q=√2、六点(√3,√5,−√3−√5,√7,√11,√13)、L1=O(3o)、L0=L1qを取る。多重二次体のcharacter射影で得られるQ線型独立性から、共鳴する根は±(h−e1−e2−e3)だけで指数0。前半三点だけが共線し、唯一の(-2)曲線がある。

(U+)はu=−q,t=−(√7+√11+√13),u−t≠0から成立。27個のtheta引数はすべて非格子。Qの九minorとdetQは非零だが成分逆数のdetは零で、cornerは無限次元。楕円線束のこの計算はgenuineを必要としない。しかしこのAS模型と弱Dqの指定同値を構成したわけではない。ここが次の一壁の入力監査に適した明示例となる。

## 6. 次の課題と失敗しやすい推論

最優先は一つのA1壁でcoherent反標準関手の有限生成性・有界性を閉じること。その後、商から標的への完全忠実性・本質的全射性を調べる。核が同じというだけで局所化同値は従わない。perfect対象だけの商を、特異標的の非perfectなcoherent複体も含む圏と同一視しない。

K_C,qの指定heart内の位置、perverse heart、局所・完成代数、AS実現の存続は未解決。複数零壁や相対化は後段。固定(S,E)での核のq不変性を、曲面パラメータを動かす降下の証明にしない。

## 7. 一次資料と今回の照合

- Rains, *Filtered deformations of elliptic algebras*, arXiv:2107.13540v2 (2022), §4 (4.4)–(4.7), pp.31–35。一般有理曲面のgluing、境界triangle、effective rootsと稠密性。https://arxiv.org/pdf/2107.13540
- Dolgachev, *Classical Algebraic Geometry: a modern view. II*, author draft, August 10, 2025, Chapter8 Theorem8.3.2, §8.3.2。弱del Pezzoの反標準モデル。https://sites.lsa.umich.edu/idolga/wp-content/uploads/sites/1467/2025/10/CAG-2.pdf
- Drinfeld, *DG quotients of DG categories*, arXiv:math/0210114v7 (2008), §§1.2–1.3,1.6。Homのconeと普遍性。https://arxiv.org/pdf/math/0210114
- Seidel–Thomas, *Braid group actions on derived categories of coherent sheaves*, arXiv:math/0001043v2 (2000), Propositions2.10,2.12–2.13。https://arxiv.org/pdf/math/0001043
- Donovan–Wemyss, *Noncommutative enhancements of contractions*, Adv. Math.344 (2019),99–136, Introduction, §§1.1,6。与えられた幾何学的収縮から始まる理論である。https://www.maths.gla.ac.uk/~mwemyss/DW4.pdf

これらの関連一次本文を今回読んだ。該当PDFのweb screenshotはCache missで失敗したものがあるため、全引用ページの画像確認完了とはしない。既知結果を入力とする今回の組合せの網羅的新規性、外部査読、機械形式化は未実施。Rains2025の全体は今回再監査していない。

## 再現

`python3 computations/verify_density_zero_walls.py` は根列挙、240の整数列、72の順序行列、零壁のQ線型条件、27theta引数、三次恒等式とHessianを厳密計算する。稠密性・sheaf存在・dg同値の証明を計算で代替しない。主論文はリポジトリrootから `latexmk -lualatex papers/nc_del_pezzo_hearts.tex`。今回の抜粋10ページと全文未組版の区別はvalidationに記す。
