# 研究方針：非可換del Pezzo曲面のheart比較とRains共鳴

2026-11-16 / hearts-migration-v1。本ファイルを研究再開時に最初に読む。GitHub `main` が本プロジェクトの正本である。

## 恒常的な研究原則と保存許可
数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合して、研究の価値を最大化するよう目標・方針を柔軟に変える。重要な変更では理由、元の目標の達成部分・未解決部分を現行の方針へ統合し、時系列の変更記録を蓄積しない。証明済み、追加仮定付き、未完成、予想、計算的観察を区別し、仮定・依存結果・証明の所在・未解決箇所を明記する。原稿に証明が書かれたこと、今回点検したこと、計算で確認したこと、外部独立査読を区別する。誤りは依存する本文・要約・研究方針へ反映し、有用な反例・障害は研究ノートに整理する。

公表用論文の重要な主張は一次文献で仮定と範囲を照合し、Introductionに既知の内容と寄与を具体的に記す。未確認の書誌を推測で補わない。原稿は原則日本語LuaLaTeXで書き、現在の成果が分かる論理順に構成し、版ごとの追記や履歴を積み上げない。価値ある定理・証明を軽量化のため削除しない。ノートは現在有効な知識、着想、例、計算、障害と文献比較を収め、研究日誌や原稿に重複する全証明を置かない。

研究継続用bundleは研究方針・研究ノート・公表用論文、必要なソース・PDF・書誌・検算コード・証明書・再現手順の最小の自己完結した一式とする。研究区切りでユーザー承諾なくLibraryへ保存することは一般原則として許可済み。ただしこの研究ではGitHub `main`を正本とする個別指示を優先し、GitHubへのpush成功時はLibraryへの重複保存をせず、失敗時にのみ緊急避難に用いる。Libraryの既存ファイルは明示指示なく削除しない。過去版ZIP・旧原稿・バックアップ・変更履歴・中間生成物・キャッシュを現行bundleに残さない。生成・検証・commit・push・remote SHAの確認を別々に報告する。

GitHubへはmainに通常のfast-forward pushを行い、force push・不要なPR・GitHub Actionsを使用しない。共有mainの並行更新を失わないよう内容を確認し、競合は正しく統合する。バックグラウンドの自動再開を保証しない。

## 対象と現在の中心目標
非可換del Pezzo曲面に現れるVdB、Rains、AS、anticanonicalの四つのheartを、指定比較関手・構造対象・反Serre自己同値・境界のデータを保って比較する。Rainsの根共鳴によるHRS tilt、混合A2局所模型、AOU/AS cubic cornerの有限性とt-exactness、壁と相対族を解明する。名称が四つあることは四つの相異なるheartを意味しない。raw VdB blow-upとsection-model qgr、導来同値とabelian/t-exact同値を区別する。

## 主要到達点と証明の所在
- `papers/nc_del_pezzo_hearts.tex` とその `papers/sections/four_hearts_*.tex` に、指定Rains/VdB/AS/anticanonical比較、標準AOU三blockの構造対象、有限corner・十一非零条件・t-exactness、楕円係数の明示化を記載する。最新の主張状態は `research/four_hearts_validation.json` と `research/heart_comparison.md` を参照。
- `papers/nc_del_pezzo_resonance_hearts.tex` と七つのresonance節に、根sheafの符号別Ext、正負共鳴の稠密性、混合指数p,-nでのrank min(p,n)、指定genuine gluingの全heart HRS tilt、指数+2/-1での四次元商Π(A2)を記載する。定理の適用範囲と検証は `research/resonance_hearts_validation.json`。
- `papers/cubic_heart_corner.tex` と五つのcorner節に、四交比の十一非零条件と一般位置六点、cornerの有限平坦性、総次元162、一様消滅次数7、古典的根壁を記載する。証明・独立計算の所在は `research/cubic_corner.md` と `research/cubic_corner_validation.json`。

## 未解決の核心と具体的着手
1. 標準楕円AOUデータの実際の壁上で、十一条件の消滅がどの許容AS locusに残り、どの対象・heartが具体的に変わるかを確認する。既に計算された楕円potential係数を使い、1壁ずつheartの検出対象と比較関手を計算する。
2. 同一の楕円gluingで最後のVdB section-model functorと自然なRains functorを、対象・境界・bimoduleを含め厳密に照合する。任意の他のheart同値を無条件に主張しない。
3. 混合A2の `A=R/(g-1)` の元の楕円生成元のcharacter値と非対角cocycle・商kernel生成元を係数式で記述し、さらに全E6境界外圏のアフィン作用を追う。
4. 相対族・底変更・fpqc降下、特異楕円境界・weak avatar・非局所自由gluingへ拡張する。公表論文では一次文献と全主張の依存関係を最終監査する。

## 関連する独立研究
H3（14641非可換三次曲面）完全分類は `uedakazushi/nc-cubic-moduli`、次数1固有のモジュライとweighted sexticは `uedakazushi/nc-dp1-moduli`、非可換三次三様体と非可換P4は `uedakazushi/nc-cubic-threefold-moduli` が正本である。次数1の指定gluing導来比較の原稿は `nc-dp1-moduli/papers/dp1_anticanonical_models.tex` を参照し、その適用範囲を保持する。他の研究の結果は必要な場合に固定commit・仮定を記して参照する。

## 再開と再現
本書 → `research/four_hearts_plan.md` → `research/heart_comparison.md`・`research/resonance_hearts.md`・`research/cubic_corner.md` → 三本の原稿と依存するsection → 各validationファイルを読む。
```sh
latexmk papers/nc_del_pezzo_hearts.tex
latexmk papers/nc_del_pezzo_resonance_hearts.tex
latexmk papers/cubic_heart_corner.tex
python3 computations/verify_four_hearts.py
python3 computations/verify_resonance_mixed_a2.py
python3 computations/verify_cubic_corner.py
```
Python3・SymPy、LuaLaTeX・LuaTeX-ja・latexmkを使用し、PDF・ログは `build/` に再生成する。移管前の検算記録は移管後に再実行したものとして扱わない。