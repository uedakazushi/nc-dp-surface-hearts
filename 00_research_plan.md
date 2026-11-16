# 研究方針：反標準heart・最大共鳴・零指数根壁

2026-11-17 / hearts-strategy-v5。再開時は本書を最初に読む。現行主論文は `papers/nc_del_pezzo_hearts.tex`（hearts-v27）。GitHub mainが正本であり、リポジトリ全体が再開に必要な現行一式となる。新しい証明と未解決点の案内は `research/resonance_walls.md`、今回の検証範囲は `research/resonance_walls_validation.json`。

## 恒常的な原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合し、研究全体の価値を最大化する。重要な方針変更は理由と元の目標の達成・未達成を現在有効な方針へ統合し、時系列の変更記録を蓄積しない。

証明済み、追加仮定付き、未完成、予想、計算的観察を分ける。仮定・既知入力・証明所在・未解決箇所を明記する。本文に証明があること、今回その証明を点検したこと、有限計算、外部独立査読、形式化を区別する。誤りは依存する主張・要約・方針にも反映し、有用な反例・障害を研究ノートに残す。

公表稿は原則日本語LuaLaTeXとし、現在の成果を理解しやすい論理順で構成する。重要な先行研究の一次資料と適用条件を確認し、Introductionに既知結果と寄与の関係を具体的に書く。未確認の書誌・文献内容を補わず、新規性が未確認なら明記する。原稿の本数やページ数を目的にせず、必要なら統合・分割する。価値ある数学と証明を軽量化のため削除しない。

ノートは現在有効な着想・例・反例・計算・障害・文献比較を整理し、作業日誌にしない。本文の証明を重複転記せず参照先を示す。再開に必要な情報を会話だけに残さない。現行bundleは方針・ノート・論文と最小限のソース・文献情報・計算・証明書・再現手順から自己完結させ、旧版・旧ZIP・バックアップ・変更履歴・外部文献PDF・中間物・キャッシュを収録しない。再取得が難しい入力と必要な証明書は保持する。

研究区切りの承諾不要Library保存は一般原則として許可済み。ただし本研究の個別指示は **GitHub mainを正本とし、保存成功時はLibraryへ重複保存せず、失敗時だけ緊急避難に使う** ことである。既存Libraryファイルは無断削除しない。mainへ通常のfast-forward保存を行い、force push・PR・GitHub Actionsを使わない。並行更新を失わないよう保存前にheadを確認する。PDF・ZIPはGit追跡せず生成する。生成・証明点検・計算・組版・commit・remote確認を別の状態として報告し、背景での自動継続は約束しない。

## 現在の目標と変更理由

中心は、構造対象と反Serre作用が選ぶ反標準heart、実在根のEuler標数によるheartの違い、その有限次元表現論である。最大共鳴のZariski稠密性と既知の零指数根壁を主論文へ統合し、非可換零指数壁の一般論を証明できたところまで含めるという指定に従い、弱楕円gluingの全orbit核を今回の構造目標として進めた。

最大共鳴の稠密性・整数表示・古典的な収縮障害は主論文へ完全な証明付きで移した。さらに、標準弱楕円gluingでは全反標準orbitに直交するdg部分圏が古典的反標準収縮の核と一致することを証明した。これは収縮対象を構成する結果であり、商が反標準qgrの有界導来圏であることまでは解決していない。主論文の中心成果を保ったまま、この境界を明記する。

## 現在の到達点と主張の状態

| 内容 | 状態・証明の所在 |
| --- | --- |
| genuineな楕円gluingの自然導来比較と全heartのHRS tilt | 既存本文の証明を保持。`four_hearts_geometric.tex`。今回全証明を再監査したものではない。 |
| 実在ADE根のEuler標数による反標準heart選択、有限単純tilt、整数倍点の整列 | 既存本文を保持。`four_hearts_root_chambers.tex`。稠密性の新しい系はここを入力とする。 |
| 規格化AS–反標準の一致、actual theta係数、元六点の復元 | 指定AS実現などの入力を含む既存結果を保持。`four_hearts_elliptic_coefficients.tex`。任意potentialへの主張ではない。 |
| 全ADE根圏、普遍有限商、970次元例、Frobenius判定、古典的Repの一致 | 既存本文を保持。`four_hearts_ade_quotient.tex`、`four_hearts_finite_representation_geometry.tex`。独立査読と生成元の具体的作用行列は未完了。 |
| 次数1–6の最大共鳴と任意整数順序のZariski稠密性 | 完全な本文証明を追加・内部点検。`four_hearts_maximal_density.tex`。九価の整数表示とgenuine判定を含む。 |
| 指定heartの一致点・不一致点がともに稠密で、いずれも構成可能でない | 同節の `cor:nonconstructible-texact`。固定楕円chartの点ごとの主張。相対t構造や全モジュライについての主張ではない。 |
| 古典的零根壁の収縮・2-spherical核・導来非同値 | 既知収縮理論の帰結を証明付きで主論文へ統合。`four_hearts_zero_walls.tex`。有理数上の明示的三次方程式とEuler列の相殺例を含む。 |
| 標準弱楕円gluingの全orbit核 | `thm:weak-orbit-kernel`：Nq-tail=Nq=iota_q ker Rf_*。任意q、固定(S,E)。完全な本文証明を追加・内部点検。 |
| 非可換零指数spherical対象・Rを変えないdg商・不可視twist | 同節の対応する系・命題。全qで対象を直接構成するが、指定Rains heartでのsheaf性は未証明。 |
| coherent反標準導来切断の全核 | `prop:weak-coherent-kernel`。有界性と次数付きExtの有限生成性などの追加仮定付き。 |
| dg商とDb(qgr R)の同値、壁上のAS比較、相対収縮 | 未解決。主論文末尾の将来の課題に明記。 |

162次元cornerの一様Hilbert関数・有限平坦族は `cubic_heart_corner.tex` に完全証明を保持する。共鳴補助稿の形式変形・zigzag・混合A2の詳細も保持する。重複の整理のために未移管の有効な内容を削らない。

## 次に着手する課題

### 1. 新しい核同定の独立点検と全文再組版

Rainsの一般有理曲面gluing (4.4)–(4.7)、正次数の境界orbitによる検出、反標準収縮の射影公式を順に点検する。genuine性を用いずに済む箇所と、弱del Pezzo・滑らかな境界・固定gluingを必要とする箇所を明示する。主論文全体を `latexmk -lualatex papers/nc_del_pezzo_hearts.tex` で再組版し、新しい参照と既存節の連結を確認する。今回の組版は追加二節の抜粋に限る。

### 2. coherent収縮へ進むための最初の補題

一つのA1零指数壁で、N^j(X)=⊕Hom(e,s^nX[j])の有限生成性と有界性を、具体的な生成対象に対して証明する。既存genuine比較のInd-orbit生成の証明をそのまま使うことはできない。今回はその生成を妨げる全核が同定されたので、核を除いた商側でどの生成・trace・有限性が必要かを確認する。

完了基準は、自然関手の核の再確認ではなく、商から標的への完全忠実性または本質的全射性を与える新たな補題である。核の同定だけでVerdier局所化を同値と呼ばない。perfect商とcoherent有界導来圏、冪等完備化を区別する。

### 3. 同じ明示的零壁のAS模型とheart

`ex:zero-elliptic-wall` のE=C/(Z+iZ)、q=√2、六点(√3,√5,−√3−√5,√7,√11,√13)を用いる。実在する非可換零指数対象と、admissibleな楕円decuple、無限次元cornerまでは証明済み。次はAS実現、noetherian性、標準helix、指定比較の入力を個別に確かめる。一般位置でのVdB比較を壁へ自動延長しない。

### 4. 後段の相対問題

複数零根の交叉、局所・完成代数、perverse heart、曲面族での底変更・降下は、上記の一壁で比較関手を閉じてから進める。既知の非可換収縮環は与えられた幾何学的収縮を入力とするため、非可換曲面上の収縮射の存在を代用しない。任意のnc del Pezzoの全モジュライ分類は本プロジェクトの完了条件にしない。

## 再開資料と検証

本書 → `research/resonance_walls.md` → 主論文の新二節 → 必要に応じ `research/heart_comparison.md`、`research/resonance_hearts.md`、`research/cubic_corner.md` と既存証明を読む。旧ノート内の未解決状態が現在の主論文と食い違う場合は、本書と本文を優先する。旧bundleや会話の取得を前提にしない。

```sh
python3 -m pip install -r requirements.txt
python3 computations/verify_density_zero_walls.py
bash scripts/check.sh all
latexmk -lualatex papers/nc_del_pezzo_hearts.tex
```

検算コードは新しい一つを加えて21本となる。今回実行したのは新コードで、既存20本は再実行していない。追加二節はLuaLaTeXで10ページの抜粋として組版し全ページを画像点検した。更新後の主論文全体と補助2稿の再組版は未実施。旧validationのv26全文組版記録をv27の成功として扱わない。現行の検証境界は `research/resonance_walls_validation.json` にある。

H3分類・次数1固有モジュライ・nc三次三様体は各別リポジトリの正本で継続し、ここへ再統合しない。必要な外部研究は固定commitと仮定を記して参照する。
