# 四heart比較の実施方針

2026-11-16 / hearts-strategy-v3。全体方針と恒常原則は [00_research_plan.md](../00_research_plan.md)、根拠と今回の検証は [current_assessment.md](current_assessment.md)。本書は四heart比較の着手順を具体化する。原稿の数学本文はhearts-v25が現行。

## 公表の中心

指定(e,s)と自然反標準導来切断によりheartを認識し、実在する境界外根のEuler標数からRains heartとの差を判定する。規格化AOU比較、actual theta potential、元六点へのcornerの復元を一つの論理として示す。

| 工程 | 出発点 | 完了条件 |
| --- | --- | --- |
| 指定関手の固定 | thm:derived、thm:VdBcanonical、cor:fourfunctors | 同じgluing・構造対象・右環作用・境界を保つことを一つの定理文に集約する。 |
| 全heartの選択 | thm:globaldefect、prop:numericaltorsion、thm:globalADEtilts | 実在単純根によるt-exact判定と有限tiltを主結果へ組み込む。既存の証明を再発見しない。 |
| 規格化AS比較 | thm:normalized-abelian、prop:ample-helix-noetherian | full very strong helix・rolled-up同定を各具体族で確認し、一般的なnoetherian結論と入力を分ける。 |
| 楕円係数と幾何 | thm:theta-potential、thm:original-six-points | actual decuple、L0非依存、元六点、十一因子の関係を主定理の読める順序にする。 |
| 新規性の固定 | Rains 2025、AOU/OU、corner一般論 | Introductionで既知入力と追加的な同定を具体的に分ける。 |

最初の研究区切りでは、この表の仮定と証明依存を揃える。文献規約の正式翻訳は必要な範囲を閉じ、未変更の印刷tupleとの無条件同一視はしない。

## 現在有効な規約と入力

右加群の辞書はL=L1、q=L0/L1。actual sheaf-normalized decupleの構造対象はOで、mutationのconeとcone[−1]、末尾三対象のshiftを区別する。条件(U+)はO(D123)≠L0、O(D456)≠L1、O(D6)≠L0L1。

x_b=p_b、y_c=p_(3+c)、X=Σx、Y=Σy、u=X−ell0、t=ell1−Yと置くと、基底・liftを固定した局所theta係数はw_abc=theta(y_c−x_b+t_a)、(t0,t1,t2)=(u,t,0)。Q=w2/w1からP~(Qの成分逆数)^tとして入力のL1六点を復元する。詳細と証明所在は [heart_comparison.md](heart_comparison.md)。

規格化共通領域では、AS–反標準の一致と十一因子非消滅は結論である。full strongをvery strongと読み替えない。OUの一般tupleに対する結果を特殊共鳴族や壁上へ自動適用しない。

## 具体例の閉じ方

既存の整数倍点例(1,3,2,5,7,11)は単純次元(6,1,1,2,2,4)と一回のtiltを与える。これを同じactual ASデータ・比較関手まで結ぶ依存関係を確認する。説明用の単根例を加える場合は、固定blowdownの実在単純根を一つ指定し、非零指数・genuine条件・他根の排除・像のcohomological degreeを同時に確認する。単なる数値共鳴をsheafの存在とみなさない。

単根の明示例は `four_hearts_single_root.tex` にある。AOU Lemma 7.4とOkawa–Ueda (2020) Theorem 5を使う命題prop:cubic-helix-inputにより、三次曲面型の指定構成ではvery strong入力を照合した。一般tupleの半連続性を特殊族へ自動適用していない。

## 次の点検と目標

1. 全ADEの境界外abel圏と元のA=R/(g−1)の普遍有限商は `four_hearts_ade_quotient.tex` に本文証明を置いた。形式性・無shift拡大閉包・右作用・Morita二重中心化の独立点検を行う。一般的な既知機構を新規成果とはしない。
2. 十一因子の零指数壁では、まずgenuine性・AS実現・very strong性・導来比較のどの仮定が失われるかを特定する。混合共線壁のgeneric pointを一つ選ぶ。既存の非零共鳴HRS tiltとは分ける。
3. 相対kernel・底変更・heart降下は、上のpointwise定理を固定した後、根データが管理された底に限って開始する。

元の生成元の巨大なcharacter/cocycle係数計算や全E6壁の列挙は、これらの構造目標に必要な範囲へ絞る。固定圏のEuler chamberを楕円moduliの開chamberと呼ばない。

## 公表稿と検証

主論文の構成は、自然比較 → heartの選択 → 規格化ASと楕円六点 → corner → 具体例を基本とする。cornerの一様Hilbert関数を含む有効な証明は保持し、重複する一般論と監査説明は整理する。共鳴別稿の独立性は新しい中心定理で判断する。

再現は全体方針のコマンドに従う。今回の20本の検算成功と3稿の全文組版の実施範囲は研究評価に記した。有限体計算を複素非torsion条件やnoetherian性の証明と呼ばない。数学的重要性・正確性を優先し、生成・証明点検・計算・組版・保存を別々に報告する。GitHub mainへの通常保存、PDF非追跡、GitHub Actions不使用、保存失敗時のみLibraryへ緊急避難という恒常原則を守る。
