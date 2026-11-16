# 現状評価：反標準heartの認識と次の構造定理

2026-11-16（日本時間）/ hearts-assessment-v1。調査対象は [mainの基準commit a37b2cf](https://github.com/uedakazushi/nc-dp-surface-hearts/tree/a37b2cf23fedb62a24168f4d98633df222b0bf89)。本書は現在の研究判断・確認範囲を記す。方針は [00_research_plan.md](../00_research_plan.md) を優先し、作業履歴は蓄積しない。

## 総合判断

この研究には、公表を狙える構造結果の核がある。特に価値が高いのは、自然反標準導来切断の標的heartを、構造対象と実在根のEuler標数から選び出し、その選択をactual楕円係数と三次曲面の六点配置へ接続する部分である。3本の原稿の独立性や全関連文献に対する新規性はまだ確定していない。

原稿には証明が多数あり、単なる実験結果の集積ではない。一方、既知理論からの帰結、指定AS実現などを入力とする比較、新たな未証明目標が混在し、古いノートでは解決済みの限定版が未解決として残っていた。最優先は、この状態を揃えて中心結果を公表可能な形にすることである。

今回、主要論証の筋道を読み、有限検算を再実行した範囲では、中心結論を直ちに否定する反例や明白な論理的矛盾は見つからなかった。ただし引用された基礎結果の全証明、各特殊族での全仮定、3原稿の全行を独立検証したとは報告しない。

## 1. 中心に置くべき既存の結果

### 1.1 反標準heartの選択原理

現在の指定genuine gluingの自然関手を

\[
 \Phi:D^b(\mathcal A_{\mathrm R})\longrightarrow
       D^b(\mathcal A_{\mathrm{ac}}),\qquad
 \mathcal A_{\mathrm{ac}}=\operatorname{qgr}R(e,s),\quad
 s=\mathbb S^{-1}[2]
\]

とする。現行原稿は導来同値と振幅[0,1]を証明し、

\[
 \mathcal T=\ker H^1\Phi,\qquad
 \mathcal F=\ker H^0\Phi,\qquad
 \Phi^{-1}(\mathcal A_{\mathrm{ac}})
   =\langle\mathcal F[1],\mathcal T\rangle
\]

と記述する。さらに非torsionの範囲で、全heartの差は境界非交叉の有限長Serre圏Zに集中し、

\[
 \Phi\text{ がt-exact}
 \iff (e,s)\text{ がAZ-ample}
 \iff \chi(e,S)>0
       \quad\text{for every actual simple }S\in\mathcal Z
\]

を主張・証明している。全対象MのEuler値の符号だけでは足りない。torsion部分は全非零商の正値、torsion-free部分は全非零部分対象の負値によって認識する。

証明所在は四heart稿のfour_hearts_geometric.texとfour_hearts_root_chambers.tex、特にthm:globaldefect、prop:numericaltorsion。有限ADE型で負指数単純を順次tiltして指定反標準heartへ到達するthm:Eulerchamber、thm:globalADEtiltsも既存結果である。これを新しい未解決課題として再計画しない。

既知のHRS理論やWeyl反射の存在と区別した寄与候補は、「この幾何学的な自然関手が選ぶheartを特定する」点にある。

### 1.2 規格化AS比較・楕円係数・元六点

四heart稿のfour_hearts_elliptic_coefficients.texは、actual normalized decupleのpotentialをtheta関数で書き、係数比Qから入力六点を

\[
 P\sim\bigl(Q^{\langle-1\rangle}\bigr)^{\mathsf t}
\]

として復元する。構造頂点を除いたcornerはL0に依存せず、L1による元六点の可換三次曲面のcornerと一致する。

さらに、ampleな構造対象を含むfull very strong周期helixを入力としてorbit代数をnoetherianに再構成し、規格化されたAS–反標準比較のt-exact性を得ている。ここではfull very strongなAS実現とrolled-up同定が入力である。「ASのnoetherian性を追加仮定しなくてよい」という結論から、「全楕円tupleでAS実現を検証済み」とは推論しない。

### 1.3 cornerの強みと限界

三次曲面のcorner稿には、標数0・18係数非零のchartにおける

\[
 \dim C<\infty
 \iff \Delta_{11}\ne0
 \iff C_7=0,\qquad C=B/BeB,
\]
\[
 H_C(t)=8+21t+33t^2+38t^3+33t^4+21t^5+8t^6
\]

と、階数162の有限局所自由代数族の証明がある。十一条件は九つの2×2 minor、det Q、det Q^{⟨−1⟩}であり、元六点の一般位置に対応する。

良い可換del Pezzoのgeometric helixで頂点除去商が有限次元になること自体は、almost Azumayaなrolled-up algebraに関する既知一般論で説明できる。したがって寄与候補は、正確な境界の十一因子、四パラメータ正規形、L0非依存、Hilbert関数と平坦族、指定heart比較への接続である。対称なHilbert関数だけからselfinjective性を推論しない。

### 1.4 共鳴の蓄積

混合A2では、正負指数p,−nのconnecting mapのrank min(p,n)を、導来完全忠実性に頼らずsheafの論証で得ている。二根Serre圏はmod Π(A2)で四つの直既約を持ち、指数+2/−1のgenuine比較では元のA=R/(g−1)に四次元商がある。

整数倍点のE6例には、全有限次元単純の次元(6,1,1,2,2,4)と一回のtiltがある。720という数は同じpointed導来圏にこの構成で得られる埋め込まれたRains heartsの数である。全有界heartの分類でも、720個の抽象的abel圏の非同値性でもない。

## 2. 計画を修正する数学的理由

### 2.1 古典的な零指数壁と非零共鳴

| 項目 | 零指数の古典根壁 | 非零指数のRains共鳴 |
| --- | --- | --- |
| 式 | ρ(α)=O_E | ρ(α)q^m=O_E、m≠0 |
| 現在の六点模型 | 共線・conic、十一因子消滅 | 一般位置内部にも存在 |
| 既存のgenuine比較 | 仮定を外れる | 適用範囲を確認した上で使用できる |
| 対象の挙動 | 古典的には(-2)対象の収縮・消失 | 根sheafが次数0または1へ移る |
| 最初の課題 | AS実現・helix・導来同値のどの入力が失われるか | 指定関手と実在根・torsion pair・有限表現の同定 |

規格化共通領域では、pointed比較とample構造対象、very strong helix、rolled-up同定が揃うとAS–反標準の一致が従う。全入力を保ったまま十一因子が消えることを期待する計画は成立しない。

共鳴軌跡の稠密性は、固定圏内のEuler chamberをパラメータ空間の有限個の開chamberと同一視できない理由でもある。相対heartは、根データと仮定を管理した底から始める。

### 2.2 解決済みの範囲と残課題

同じ最後のraw blow-up Wと同じRains実現について、VdBのRδ_*を自然反標準導来切断へ同定する結果はthm:VdBcanonicalとcor:fourfunctorsにある。未解決なのは、独立に選んだblowdown表示、各段階のsection-model置換と六回raw反復を混ぜた比較、未変更AOU記号への全体的な翻訳である。

同様に、actual decupleの係数と元六点の復元、Euler chamber選択は既存成果として保持する。特別な共鳴族におけるAS入力の適用確認は、公表前の検証項目として切り離す。

## 3. 次の新規構造目標の評価

**未証明候補：全ADE根圏とアフィン有限商。**

実在単純根の図式Γに対してZ≃mod Π(Γ)を示し、反標準側の有限次元加群圏を支配するAの有限商を得る。これは既存A2結果の自然な拡張であり、根の組合せと実際の楕円アフィン代数を結ぶため、元の生成元の長い係数式を先に増やすより価値が高いと判断する。

具体的な証明入口は、既存のformal zigzag Ext代数のenhancedな生成部分圏で、無shift単純の有限拡大閉包をtwisted complexとして記述すること。次数1のMaurer–Cartan方程式がpreprojective関係となること、次数0射がintertwinerとなること、Dynkinの冪零性により対象が尽くされることを確認する。Ext-quiverの一致だけでは不十分である。

混合共鳴ではΦ|Zは標的の有限次元heart Kへt-exactでない。既存Euler tiltによってKの単純も同じADE spherical配置を持つことを用い、同じ形式性とenhanced拡大閉包の議論をKにも適用してK≃mod Π(Γ)を別に同定する。その後、標的heartの実際の忘却関手をP=⊕P_i^{m_i}で表現し、対応A加群Gのannihilatorを用いてA/Iを認識する。全有限次元A加群がGの有限直和の商であることが鍵で、単なるfaithfulnessから作用像の全射性を推測しない。右加群の規約を固定してMorita代表を記述する。

これはD^b(Z)がambientへ完全忠実に入ることを要求しない。既存A2でheart内部の高次Extがambient Extと異なることは、この区別が不可欠な反例である。162次元corner B/BeBと、Aの境界外有限商は別物である。

## 4. 一次文献の確認と新規性の境界

以下は今回関連箇所を確認した一次資料である。原稿の全参考文献・全証明を網羅した一覧ではない。

| 一次資料 | 確認箇所 | 計画への帰結 |
| --- | --- | --- |
| [VdB, Blowing up of non-commutative smooth surfaces](https://arxiv.org/abs/math/9809116v1) | Definition 11.1.2、Theorem 11.1.3、§11.2 | 六点一般位置は有限条件。raw blow-upとsection-modelの導来比較・境界外対象の基礎は既知入力。 |
| [AOU, Compact moduli of marked noncommutative cubic surfaces](https://arxiv.org/html/2404.00175v1) | §§4,7,9、Theorem 9.4 | qgr Fとqgr Aの導来同値が既知。指定関手のt-exact性を別に証明する意義がある。 |
| [OU, Marked Artin–Schelter surfaces of del Pezzo types](https://arxiv.org/html/2508.04986v1) | Definition 3.1、(3.9)–(3.10)、Lemma 6.2、Theorem 6.4 | very strong性は全forward Ext消滅を与える。一方tupleからの実現には一般性の条件があり、特殊族への自動適用はできない。 |
| [Rains, Filtered deformations of elliptic algebras](https://arxiv.org/pdf/2107.13540v2) | §4 pp.34–35、Proposition 5.1 | 指定simple rootの有効化と共鳴軌跡の稠密性は既知。 |
| [Rains, The (noncommutative) geometry of difference equations](https://arxiv.org/html/2504.16187v1) | 以下の対応箇所、§§11,12,16–18 | 2019稿の基盤を再編した2025 monographも引用・新規性監査の対象とする。 |
| [de Thanhoffer de Völcsey–Van den Bergh, Some new examples of non-degenerate quiver potentials](https://arxiv.org/pdf/1005.0808v3) | §3冒頭、Theorem 4.2.1 | 可換geometric helixの良い点でのcorner有限性は一般論で説明できる。十一因子・具体的族・heartへの接続に寄与を集中する。 |
| [Mizuno, Classifying τ-tilting modules over preprojective algebras of Dynkin type](https://arxiv.org/pdf/1304.0667v3) | Theorems 2.21, 2.30, 3.8, 4.1 | Dynkin preprojectiveのtorsion classesとWeyl群の分類は既知入力。 |
| [Liu–Wang, A∞-deformations of zigzag algebras via Ginzburg dg algebras](https://arxiv.org/pdf/2301.06757v3) | Theorem 1.1、§3、Proposition 4.4 | 標数0のADE形式性とKoszul双対は既知。Etgü–Lekili、Lekili–Uedaの先行結果の帰属を保持する。 |
| [Bousseau, Geometric helices on del Pezzo surfaces from tilting](https://arxiv.org/html/2603.22065v2) | Theorem 1.1、Corollary 1.2、Theorem 5.20 | 可換del Pezzoのgeometric helicesと完成反標準錐のNCCR mutationに既存結果がある。ncの指定heart比較と対象を区別する。v2に固定する。 |

Rainsの2019稿と2025稿の関連番号は、Lemma 4.9→Lemma 11.10、Proposition 4.17→11.19、Proposition 4.24→11.25、Theorem 4.30→11.31、Lemma 5.7→12.7、Theorem 9.10→16.10、Corollary 10.16→17.17。有効simple root自身に対するirreducible sheafの存在は、2019 Proposition 11.23直前と2025 Proposition 18.27直前の記述を用いる。nef条件を課す後続命題そのものを(-2)単純根へ誤適用しない。

全ADEのabel圏と元のAの有限商をこの設定で同時に記述した同一の結果は、今回確認した主要箇所では見つからなかった。これは未発見という状態であり、新規性確定ではない。Rains 2025の409頁全文を取得不能とする以前の記述は更新したが、全文の証明・関連研究の網羅的監査は未完了である。

## 5. 公表の構成

主論文の中心を「反標準heartの認識と根による選択」に置く。cornerの正確な有限性判定・楕円係数・L0非依存は、その具体的な核としてまとめる。162次元族の全証明も保持し、公表先を一つに定める。

共鳴別稿は、全ADE有限商など独立した中心定理が揃う場合に独立論文とする。そうでなければA2例と共鳴結果を主論文へ統合する。現段階で3論文を完成扱いにしない。相対降下・全境界分類・任意potentialのAS性を中心論文の完了条件に加えない。

## 6. 今回の再現確認

基準commitの全70ファイルを取得し、3主原稿と20の依存section、研究ノート、証明書、検算コードを確認した。

- computations/verify_*.pyの全19本をPython3で再実行し、全て終了コード0。
- cornerの有限行列・Hilbert/交点計算、根の有限組合せ、混合A2の線形代数、有限体での楕円関係を含む。これらはsheaf存在・一般t-exact性・複素非torsion条件の証明を代替しない。
- 3主原稿の再帰input/include、labelとref/eqref、bibitemとciteを静的点検し、欠落を検出しなかった。これは組版の確認とは別である。
- latexmkによる3原稿の組版を試したが、この実行環境にlualatex.fmt、lualatex.ini、latex.ltx、ltjsarticle.cls、luatexja.styがなく、TeX本文処理の前に停止した。PDF生成・ページ画像検査は未実施。原稿のコンパイルエラーが判明したという意味ではない。
- 過去のvalidationが記す組版・画像確認は、それぞれの当時の実施記録である。今回成功した組版として扱わない。
- 今回の変更は研究方針・評価・再開用ノートの同期であり、新しい全ADE定理を証明したとは報告しない。

大きなログや再生成可能な出力は現行研究資料へ追加しない。Gitに保持する原稿・コードと短い本評価から再現する。
