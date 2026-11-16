# 四つのheartの比較：研究方針

2026-11-16 / hearts-v24。この一式から再開する場合は本書を最初に読む。現行論文は `papers/nc_del_pezzo_hearts.tex`、補足知識は `research/heart_comparison.md`、検証状態は `research/four_hearts_validation.json`。リポジトリ全体の目標は `00_research_plan.md` にあり、本書はheart比較に対象を限定する。

## 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合して研究価値を最大化する。重要な方針変更は理由と元の目標の達成・未達成を簡潔に記し、現在有効な方針へ書き直す。時系列の変更記録を蓄積しない。

証明済み・追加仮定に依存・未完成・予想・計算的観察を分ける。仮定、既知入力、証明の所在、未解決箇所を明記し、原稿に証明があること、今回の点検、有限検算、外部独立査読を区別する。誤りが判明したら依存する本文・要約・方針を更新し、有用な反例や障害をノートに保持する。

公表用原稿は原則日本語LuaLaTeXとし、一次資料の仮定と適用範囲を確認する。未確認の文献内容を補わない。既知成果と本研究の組合せによる結果を区別し、網羅的新規性未確認を明記する。価値ある数学的内容と証明を軽量化のために削らない。

研究継続用bundleは現行方針・ノート・論文・再現に必要な最小限の原稿、PDF、文献情報、コードと小証明書から自己完結的にする。履歴、旧版、バックアップ、外部文献PDF、コンパイル中間物は含めない。必要な知識を会話だけに残さない。

研究区切りの承諾不要Library保存は一般に許可されている。ただし本研究ではユーザーのプロジェクト固有指示により **GitHub mainが正本であり、GitHub保存成功時にはLibraryへ保存しない。失敗時のみ緊急避難に使う**。既存Library資料は無断削除しない。mainへの通常の保存と遠隔確認を行い、force push・不要なPR・GitHub Actionsを使わない。共有mainの他の研究を損なわない。

生成・証明点検・数値検算・組版・保存を別々の状態として報告する。配布前に必要ファイル、参照、組版、計算、ZIP整合性を確認する。

## 最優先の目標：公表価値を支える構造結果と正確性

現在の公表稿は46ページ、主TeXと九つのsectionからなる。最新の中心は `four_hearts_elliptic_coefficients.tex`。自然な比較関手、実際の楕円データ、構造対象を保ったheartの同定を優先し、例・ページ数を増やすこと自体を目標にしない。

## 現在の到達点

右加群規約での辞書L=L1、q=L0/L1と、明示したcohomological shiftを持つmutation列からのactual decupleを保持する。実際の三条件(U+)はO(D123)≠L0、O(D456)≠L1、O(D6)≠L0L1であり、印刷された別規約のtupleをそのまま代入しない。

**全potentialの明示式**：x_b=p_b、y_c=p_(3+c)、X=Σx、Y=Σy、L_iのAbel和をell_iとする。u=X−ell0、t=ell1−Yと置けば、矢基底を選んでw_abc=theta(y_c−x_b+t_a)、(t0,t1,t2)=(u,t,0)。これは全27係数の解析的局所表示であり、基底・liftを変えた時のgaugeを明示する。次数2切断の三つの零点による直接証明を持つ。

**元の六点の復元**：Q_bc=w2bc/w1bcはtheta(y_c−x_b)/theta(y_c−x_b+t)。L1埋込みの最後の三点を座標点にした最初の三点の座標行列PについてP~(entrywise inverse Q)^t。したがって構造頂点を除くcornerはL0に依存せず、一般位置では元の六点の可換三次曲面cornerに一致する。十一条件は新たな補助六点でなく、入力のL1六点の一般位置と同値となる。これはFrobenius公式そのものの新発見ではない。

係数w1の九零条件は一つの前半点と二つの後半点のL1共線条件。Qの九minorは二つの前半点と一つの後半点の共線条件。det(entrywise inverse Q)は前半三点の共線、detQは六点conic。後半三点の共線は(U+)で既に除外される。w0はL0に依存し、零になってもcornerには影響しない。

**noetherian性と標準heartの一致**：Hom有限noetherian・有限homological dimensionのheartにAZ-ampleなeがあり、eを含むfull very strong周期helixが導来圏内にあるとき、そのfoundation Tはheart内にあり、(T,s)もampleとなる。eのtwistからのd段の全射解消とdimension shiftingで全対象への高次Ext tailを消し、AZ再構成からorbit代数の右noetherian性とabel同値を得る。noetherian性のgraded idealによる証明も収めた。

この命題を、規格化したpointed比較Psi+と既存の標準AS very strong helix実現に適用すると、VdB一般位置・(U+)の共通領域でB(W+)は右noetherianかつqgr A+≃qgr Fとなり、指定Psi+自体がt-exactとなる。したがってこの構成ではnoetherian性とDelta≠0を独立に追加しなくてよい。任意のfull strong collectionをvery strongと読み替えたり、任意potentialへ拡張したりしてはならない。

整数倍点の共鳴族はこの領域に入るため、AS+と反標準heartは一致する。一方、順序付きRains heartは既存の整列定理でそのheartへ移る。例(1,3,2,5,7,11)では一回、全simple次元は(6,1,1,2,2,4)。720の埋め込まれたheartと抽象的abel非同値の分類は区別する。

## 研究方針の更新理由と次の核心

従来の優先課題だった「actual decupleのpotential、十一因子の楕円表示、noetherian適用域」は上の共通領域で解決したので、未解決課題として反復しない。有限係数判定を元の幾何と結び付け、ASと反標準が一致する場所を仮定でなく構成から与えられたことが今回の進展である。

次の優先課題は、一般位置の外でなおactual decupleがadmissibleである壁を選び、純代数的なcornerの無限性と実際の圏の対象・tiltの関係を調べること。ただしVdBの導来比較やvery strong標準実現が失われた点へ定理を無条件に延長しない。まず一つの混合共線壁またはconic壁で、どの入力が残るかを確認する。

もう一つの優先課題は公表稿の再編成と独立点検である。theta関係式、元の六点、ample-helix再構成、共通領域のabel同値を主定理の論理順に置き、規約に関する長い監査部分と一般論の重複を整理する。ただし有効な証明や既存の共鳴結果を削除して軽量化しない。先行研究との比較はAOU §4/7/9、OUのvery strong helix、AZ/Polishchukの再構成を明示し、本研究の追加的な接続と区別する。

未変更の印刷AOU全記号への正式翻訳、Rains2025 monograph全文との網羅的新規性照合、外部独立査読、相対kernel・heart・marked descent、元のアフィン生成元の作用係数は引き続き未完了。

## 再現と実施範囲

    python3 computations/verify_cubic_heart_numerics.py
    python3 computations/verify_four_hearts.py
    python3 computations/verify_four_hearts_corner.py
    python3 computations/verify_four_hearts_chambers.py
    python3 computations/verify_four_hearts_sorted.py
    python3 computations/verify_four_hearts_boundary.py
    python3 computations/verify_four_hearts_elliptic.py
    latexmk -lualatex -outdir=build papers/nc_del_pezzo_hearts.tex

Python標準ライブラリ、LuaLaTeX、LuaTeX-ja、tikz-cd、latexmkを使う。新しいellipticコードはF_1009上のy²=x³−x+1でMiller関数からactual Hom切断を作り、関係を関数体で交差乗算して検査する。24の一般位置配置それぞれ三つのL0、および四種類の強制壁を扱い、計684組の関係式を厳密検算する。有限体の計算を非torsionの存在や複素幾何・noetherian性の証明と呼ばない。

保持した六コードも現行入力で再実行した。全文組版・ページ画像の確認・清浄環境の再現・遠隔保存はvalidationで区別する。過去の全証明の今回の独立再監査や外部査読はしていない。GitHubが正本で、保存成功時にはLibraryへ別途アップロードしない。
