# 研究方針：非可換del Pezzo曲面の反標準heartと根圏

2026-11-16（日本時間）/ hearts-strategy-v3。本書を再開時に最初に読む。GitHub mainが正本。現状評価・一次資料・今回の検証範囲は [研究評価](research/current_assessment.md) にまとめる。

## 最優先目標と達成基準

**指定された構造対象と反Serre作用から反標準heartを認識し、Rains・VdB・ASの幾何学的な構成が、そのheartと一致する範囲、tiltで結ばれる範囲、収縮を伴う範囲を明示する。** 既存の比較・Euler選択・楕円係数の成果を公表可能な主定理にまとめることを最優先とし、次の新しい構造結果として全ADE根圏と元のアフィン代数の有限商を狙う。

達成の単位は、仮定・指定関手・構造対象・証明・先行研究との差が揃った定理である。原稿数、例数、計算回数、係数表示の長さを成果の尺度にしない。現在は主論文にADE構造結果を集約し、共鳴稿とcorner稿を技術的な補助原稿として維持する。3本の独立論文とはみなさない。

## 恒常的な研究原則と保存許可
数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合して、研究の価値を最大化するよう目標・方針を柔軟に変える。重要な変更では理由、元の目標の達成部分・未解決部分を現行の方針へ統合し、時系列の変更記録を蓄積しない。証明済み、追加仮定付き、未完成、予想、計算的観察を区別し、仮定・依存結果・証明の所在・未解決箇所を明記する。原稿に証明が書かれたこと、今回点検したこと、計算で確認したこと、外部独立査読を区別する。誤りは依存する本文・要約・研究方針へ反映し、有用な反例・障害は研究ノートに整理する。

公表用論文の重要な主張は一次文献で仮定と範囲を照合し、Introductionに既知の内容と寄与を具体的に記す。未確認の書誌を推測で補わない。原稿は原則日本語LuaLaTeXで書き、現在の成果が分かる論理順に構成し、版ごとの追記や履歴を積み上げない。価値ある定理・証明を軽量化のため削除しない。ノートは現在有効な知識、着想、例、計算、障害と文献比較を収め、研究日誌や原稿に重複する全証明を置かない。

研究継続用bundleは研究方針・研究ノート・公表用論文、必要なソース・PDF・書誌・検算コード・証明書・再現手順の最小の自己完結した一式とする。研究区切りでユーザー承諾なくLibraryへ保存することは一般原則として許可済み。ただしこの研究ではGitHub `main`を正本とする個別指示を優先し、GitHubへのpush成功時はLibraryへの重複保存をせず、失敗時にのみ緊急避難に用いる。Libraryの既存ファイルは明示指示なく削除しない。過去版ZIP・旧原稿・バックアップ・変更履歴・中間生成物・キャッシュを現行bundleに残さない。生成・検証・commit・push・remote SHAの確認を別々に報告する。

GitHubへはmainに通常のfast-forward pushを行い、force push・不要なPR・GitHub Actionsを使用しない。共有mainの並行更新を失わないよう内容を確認し、競合は正しく統合する。バックグラウンドの自動再開を保証しない。

## 現在の到達点

以下は「現行原稿に証明があり、今回主要な論理と依存関係を点検した結果」である。外部入力を含む全証明の独立検証・網羅的新規性確認を完了したという意味ではない。

| 内容 | 証明の所在・適用範囲 |
| --- | --- |
| 指定された自然反標準導来切断の同値と全heartのHRS tilt | four_hearts_geometric.tex の thm:derived, thm:globaltilt。滑らかな楕円境界を持つgenuine avatarの指定gluing。 |
| 全heartの差の検出と反標準heartの選択 | four_hearts_root_chambers.tex の thm:globaldefect, prop:numericaltorsion, thm:Eulerchamber, thm:globalADEtilts。非torsionの場合、torsion-free部分は境界非交叉の有限ADE根圏に集中する。t-exact性は全実在単純根の正Euler値で判定できる。 |
| 規格化AS–反標準heartの一致 | four_hearts_elliptic_coefficients.tex の thm:normalized-abelian。指定されたfull very strong周期helixとrolled-up同定を入力とする。全potentialのAS正則性やnoetherian性は主張しない。 |
| actual decupleの27個のtheta係数・元六点の復元 | 同節の thm:theta-potential, thm:original-six-points, cor:elliptic-discriminant。cornerはL0に依存せず、L1で埋め込んだ入力六点の可換cornerに一致する。 |
| corner有限性の十一条件・一様Hilbert関数 | cubic_heart_corner.tex と対応section。標数0で18係数非零のchart。有限性と十一非零条件とC7=0が同値、Hilbert係数は(8,21,33,38,33,21,8)、総次元162。 |
| 同じ最後のraw blow-upからのVdB/Rains/反標準関手の接続 | four_hearts_canonical_comparison.tex の thm:VdBcanonical, cor:fourfunctors。独立に選んだblowdown表示や六回raw反復全体の比較とは区別する。 |
| 混合A2の全対象・rank・四次元アフィン商 | resonance_mixed_a2_category.tex と resonance_global_heart.tex。rank δ=min(p,n)、二根Serre圏はmod Π(A2)。指数+2/−1の指定比較では元のA=R/(g−1)に四次元商がある。 |
| 整数倍点族の単純次元と埋め込まれたheart | four_hearts_root_chambers.tex。例(1,3,2,5,7,11)の単純次元は(6,1,1,2,2,4)、一回のtilt。720個はこの構成からの埋め込まれたheartで、全heart分類や抽象abel圏の720同型類を意味しない。 |

## 二種類の壁を分ける

1. **非零指数の共鳴：** ρ(α)q^m=O_E、m≠0。genuineな一般位置の内部でも起こる。指定導来比較の下で実在根sheafの像が次数0または1に現れ、既存のHRS/Euler選択定理が働く。固定根圏内のEuler chamberと、楕円パラメータ空間の幾何学的chamberは別概念である。共鳴軌跡の稠密性から有限個の壁の補集合を想像しない。
2. **零指数の古典的根壁：** ρ(α)=O_E。十一因子の消滅は、対応chartで入力六点の共線・conic条件である。ここではgenuine性・一般位置を使う既存定理の仮定を外れる。まずどの入力が壊れるかを決める。既存導来同値の延長や単純なtiltを先取りしない。

規格化共通領域でAS–反標準のt-exactnessと十一因子非消滅は既に結論である。その全入力を保持したまま十一因子が零になる壁を探すことはできない。古典的壁の課題は、weak avatar・収縮・商圏の問題として設定し直す。

## 優先順位と具体的な着手

### P0：中心定理の正確性と新規性を固定する

現在の比較・Euler選択・楕円係数の3つを一つの主定理の論理順にする。Rains 2025の該当本文、AOU §7/§9、OUのvery strong入力について、仮定と右加群規約、構造対象、境界、環の右作用を照合する。対応する一次資料と現時点の照合範囲は研究評価に記載した。

主定理の各適用例では「genuine avatar」「実在する向き付き単純根」「pointedな指定比較」「full very strong helix」「rolled-up環の同定」を個別に確認する。形式的なpointed recognition、AZ再構成、根共鳴の存在・稠密性、Dynkin torsion classのWeyl分類を単独の新規成果に数えない。

**完了条件：** 中心定理ごとに、既知入力と本研究の追加部分をIntroductionで特定し、未確認の外部入力を残した箇所は条件付きと明記する。既に証明のあるEuler chamber選択や、同一最後段階のVdB関手同定を新しい未解決課題に戻さない。

### P1：公表核を完成し、最小例で比較を閉じる

主題を「反標準heartの幾何学的認識と実在根による選択」とする。自然導来切断 → HRS tilt → Euler選択 → 規格化AS比較 → actual theta係数・六点・corner → 具体例、の順に整理する。cornerの十一条件・162次元族・一様消滅次数7は、主論文の技術的中核または一つの補助原稿に集約する。有効な証明はすべて保持する。

既存の整数倍点E6例を主要検証例にし、説明用には一つの指定blowdown単純根だけが非零指数で共鳴するgenuineな配置を一組選ぶ。同じ(E,L0,L1,p_i,q)、potential、比較関手、実在root sheafとその像、HRS torsion pairまで結ぶ。他根の排除は無限個の共鳴条件を有限体計算で確認したことにしない。

**完了条件：** 最小例とE6例において、heartの差を実在対象で検出でき、指定されたAS–反標準同値と両立する。新例は `four_hearts_single_root.tex` の E=C/(Z+iZ)、q=√2、六点(√3,√5,−√3−√5−√2,√7,√11,√13)で閉じた。他根の全整数指数は整数独立性により排除した。新例の大量追加は行わない。既存の強い結果を公表するために、以下P2・P3の全面解決を待つ必要はない。

### P2：ADE根圏とアフィン有限商の本文証明

**本文に証明を追加し、今回論証を点検した範囲。独立査読済みという意味ではない。** `four_hearts_ade_quotient.tex` の lem:formal-ADE-heart → thm:ADE-abelian → lem:finite-fibre-quotient → cor:ADE-affine-quotient が証明の鎖である。

標数0の実在する有限ADE配置にLiu–Wangの形式性とKellerの無shift twisted extension閉包の復元を適用する。Maurer–Cartanはpreprojective関係、次数0射はintertwiner、負次数射は零で、Dynkinの矢イデアルの冪零性が全表現を尽くす。これによりZ≃mod Π(Γ)を得る。Euler tiltで得たKの単純配置へ同じ議論を**別に**適用し、K≃mod Π(Γ)を得る。Db(Z)のambientへの完全忠実性は使わない。

実際の忘却関手はP=⊕P_i^{m_i}で表現される。GをPに対応する有限次元右A加群とし、I=Ann_A(G)と置く。全有限次元加群がGの有限直和の商になるのでIは全表現の共通annihilatorである。有限な作用像B=A/Iに対するMorita二重中心化から、右加群規約でA/I≃End_Π(P)を得る。単なるfaithfulnessから全射性を推論していない。これが全有限次元商を支配する普遍商である。

次に必要なのは、この結果の全関連文献に対する新規性の追加監査と独立の証明点検である。一般的な形式性・Morita補題を単独の新規定理とはしない。元の楕円生成元の行列表示は未計算であり、普遍商の同型型・実際の作用による構成とは区別する。162次元cornerとも同一視しない。

### P3：零指数の一壁における収縮模型

既存の一壁例Q0=((1,1,1),(1,2,2),(1,3,4))に対応する混合共線壁を第一候補とし、generic pointを調べる。actual decupleのadmissibility、AS正則性、標準helix、noetherian性、反標準環、自然関手のどれが存続するかを順に判定する。

**完了条件：** 一つの実在する非可換族について、失敗する入力とkernel/収縮対象を特定し、古典的i_*O_{(-2)}(−1)の消失と比較する。定理の全入力が壁上で同時に成立しないことを証明できた場合も有効な構造結果である。壁の全列挙や全E6退化の分類へは先に進まない。

### P4：相対化は構造定理が固定された後

まず根図式・Euler次元・比較の仮定が一定の指定された底に限り、kernelの底変更、orbit環、相対torsion pairを調べる。pointwise同値からfpqc降下やmoduli stack同型を推論しない。有限位数q、特異楕円境界、weak avatarの一般理論は、この段階まで保留する。

## 続行・縮小の判断

- P0の主定理集約、P1の単根例、P2の本文証明が現行稿にある。以後はその論証と引用の独立点検を先行する。
- P2で必要なenhancement・有限生成・作用像の全射性が証明できなければ、欠ける仮定と反例候補をノートに書き、既存A2結果と主論文を先に完成する。
- P3はP0/P1を妨げない独立した小範囲の探索にする。数値的壁だけが得られて実在族へ結び付かない場合、結果は計算的観察に留める。
- 出版物の独立性は新しい中心定理で判断する。共鳴別稿は全ADE有限商など独立した結論が揃った場合に分け、既存比較・根理論の重複は一箇所に集約する。

## 研究範囲と再現

H3完全分類は [nc-cubic-moduli](https://github.com/uedakazushi/nc-cubic-moduli)、次数1固有のモジュライは [nc-dp1-moduli](https://github.com/uedakazushi/nc-dp1-moduli)、nc三次三様体は [nc-cubic-threefold-moduli](https://github.com/uedakazushi/nc-cubic-threefold-moduli) が正本。本研究へ再統合しない。外部結果を実際に使う際は固定commitと仮定を記す。

再開順は本書 → [研究評価](research/current_assessment.md) → [四heartの実施方針](research/four_hearts_plan.md) → [比較ノート](research/heart_comparison.md)・[共鳴ノート](research/resonance_hearts.md)・[cornerノート](research/cubic_corner.md) → 主原稿と依存section。詳細な証明を方針へ重複転記しない。

    python3 -m pip install -r requirements.txt
    python3 computations/verify_four_hearts.py
    python3 computations/verify_resonance_mixed_a2.py
    python3 computations/verify_cubic_corner.py
    latexmk papers/nc_del_pezzo_hearts.tex
    latexmk papers/nc_del_pezzo_resonance_hearts.tex
    latexmk papers/cubic_heart_corner.tex

必要時はcomputations/verify_*.py全20本を実行する。Python3/SymPy、LuaLaTeX・LuaTeX-ja・latexmkを使い、生成物はbuild/へ置く。今回の全20本の検算と3稿のLuaLaTeX組版、参照点検の実施範囲は研究評価に記す。計算成功を一般定理や文献照合の代用にしない。
