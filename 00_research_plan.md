# 研究方針：反標準heartとcoherent収縮

2026-11-17 / hearts-strategy-v12。再開時は本書を最初に読む。第1論文は `papers/dp-hearts.tex`（hearts-v34）、第2論文は `papers/dp-hearts2.tex`（hearts2-v1）。GitHub mainが正本である。零指数壁の現在の知識は `research/resonance_walls.md`、検証範囲は `research/two_papers_validation.json`。

## 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合して研究全体の価値を最大化する。重要な変更では理由と元の目標の達成部分・残課題を現行方針に統合し、時系列の変更記録を蓄積しない。

証明済み、追加仮定付き、証明未完成、予想、計算的観察を区別する。主張の仮定、既知入力、証明所在、未解決箇所を明記する。本文に証明を書いたこと、今回の内部点検、計算、組版、独立査読、形式化は別の状態である。誤りは依存する本文・要約・方針にも反映し、有用な反例や障害をノートに残す。

公表稿は原則日本語LuaLaTeXで、研究経緯ではなく現在の成果を理解しやすい順序に構成する。重要な先行研究は一次資料で適用条件を確認し、Introductionで既知結果と寄与を具体的に分ける。未確認の内容・書誌は推測で補わず、新規性未確認も明記する。論文本数やページ数を目的にせず、必要なら統合・分割する。有効で公表価値ある成果・証明を軽量化のため削らない。

研究ノートは現在有効な知識・着想・例・反例・計算・失敗した方法の本質的障害を整理し、日誌にしない。再取得困難な情報は簡潔に保持する。論文の全証明を重複させず参照先を示す。再開に必要な情報を会話だけに残さず、現行方針・ノート・原稿・最小限の書誌・コード・証明書・入力・再現手順から自己完結させる。旧版ZIP、バックアップ、作業ログ、重複、中間物、キャッシュを現行一式へ追加しない。必要な検証資産は保持する。

研究区切りの承諾不要Library保存は一般原則として許可済み。現行の指示に従い、**GitHub mainを正本としながら研究区切りごとにLibraryにも現行の研究継続用bundleを保存する**。保存するbundleには最新版だけを含め、旧版・重複・作業履歴を入れない。GitHub mainへの反映とLibrary保存を別々に検証する。既存Libraryファイルは明示指示なしに削除しない。mainは通常のfast-forwardで更新し、force push・PR・GitHub Actionsを使わない。並行更新を失わないよう保存前にheadを確認する。PDF・ZIPはGit追跡せず再生成する。生成・検証・commit・push・remote確認を分け、未実行・失敗・制約は正確に報告する。背景での継続は約束しない。

## 二論文の役割

`dp-hearts.tex` は自然heart比較、HRS/Euler選択、AS/VdBの指定比較、actual theta係数と六点復元、ADE普遍有限商と表現族、最大共鳴稠密性、零指数壁の核とcoherent収縮を扱う。`dp-hearts2.tex` は符号別Ext・混合A2・zigzag形式変形とcornerの完全Hilbert関数・162次元平坦族・計算証明を保持する。必要な一般結果は第1論文を引用し、詳細を重複させない。現在の2driverを維持し、旧3driverを復活させない。

## 現在の目標と到達点

公表の中心は「指定反標準関手がheartと根表現をどう認識し、零指数壁では何を収縮するか」である。核の同定だけではcoherent関手や商同値は得られないため、弱領域の有限生成性・有界性と収縮先の記述を優先した。

`four_hearts_coherent_contraction.tex` には次の定理群が証明付きである。

1. 標準弱楕円gluingの全q（有限・無限位数とも）でRは左右noetherian。各N^j(X)=⊕Hom(e,s^nX[j])は有限生成で、非零jは有限個。自然Phi:Dq→Db(qgr R)を構成する。追加のcoherent有限性仮定はこの設定では不要となった。
2. 既存のorbit核定理と合わせ、ker Phi=Nq=iota_q ker Rf_*。証明鎖は `lem:graded-boundary-finiteness` → `thm:weak-coherent-sections` → `eq:weak-coherent-kernel-final`。
3. BKS Theorem2.14を古典的反標準収縮に適用し、(Dq/Nq)^naturalを、古典的特異モデルSbar上のO^perpに境界moduleをglueしたDbar_qと同定する。`thm:singular-gluing-target`。q=OではDb(coh Sbar)を回復する。
4. 非genuineならDbar_qは全qで無限高次自己Extを持ち、proper dg圏でない。source Dqと抽象的にも同値でない。`cor:singular-gluing-unbounded`。これを未同定のDb(qgr R_q)へ転用しない。

いずれも新しい本文証明を内部点検した状態であり、独立査読・形式化・網羅的新規性確認ではない。境界切断のnoetherian性はKeeler、古典的局所化はBondal–Kapranov–Schechtmanの既知定理である。既知一般論自体を新規定理としない。

既存のgenuine導来比較・Euler選択・全ADE有限商・表現スキーム・theta係数・最大共鳴稠密性は保持している。これらの全証明を現行の点検で網羅的に独立監査したわけではない。零指数壁の実在spherical対象・twistの不可視性と有理数および楕円関数の明示例も保持する。

## Du Val局所特異性に関する到達点

第1論文の `four_hearts_duval_singularity.tex` では、古典的な特異モデルの共通部分圏 Bbar=O_Sbar^perp に対し
Bbar/(Bbar∩Perf(Sbar)) ≃ D_sg(Sbar) を証明した（`prop:duval-singularity-quotient`）。
Du Val点 x_i のideal sheafの像 J_{i,q} は、どのgluingパラメータ q でも
dim Hom(J_{i,q},J_{j,q}[n])=4δ_ij (n≥3) を満たす（`thm:duval-high-ext`）。
証明は評価triangle、局所Gorenstein双対性とTateの既知のhypersurface最小解消に基づく。

これは構成した特異gluingの共通部分商・高次Extの結果であり、一般qのDb(qgr R_q)を同定する結果ではない。
次の価値ある課題は、A1壁でこの高次ExtのYoneda積・2周期構造と、反標準qgr側の像を比較することである。次元だけではADE型を区別できない。

## 反標準orbitの完全部分圏と残余特異性

第1論文の `four_hearts_orbit_core.tex` で、標準弱楕円gluingの全qについて
Tq=thick{s_q^n e | n∈Z} に制限した自然関手は、Pq=thick{πR_q(n)}へのdg同値であることを証明した。
証明はsourceの境界triangle・Serre双対性とRains Corollary 3.8のtarget orbit Ext公式、
境界H¹(O_E)へのtrace比較に基づき、genuine領域で必要だったInd生成を用いない。
TqはNqと両側直交するため、商Qq=(Dq/Nq)^naturalにも完全忠実に入る。

**零指数壁の決定的障害：** 非genuineなSならQqには無限高次自己Extを持つ対象がある一方、Tqはsmooth proper sourceの部分圏なので全Homが有限である。
従って Tq⊊Qq、残余商 Sq=(Qq/Tq)^natural は全qで非零。
q=O_Eでは Tq=Perf(Sbar)、Sq=D_sg(Sbar)^natural。
自然関手は残余商から Db(qgrR_q)/Pq への比較を誘導するが、一般の非自明qでこの比較が同値という主張はしない。
中心の未解決問題は、この残余部分とorbit部分のgluingを含む全自然比較の検証である。

## 単一A1壁の局所行列因子化と安定自己Ext

第1論文 `papers/sections/four_hearts_a1_stable_model.tex` に、A1完備局所環 A=k[[u,v,w]]/(uv−w²) の奇部分 N=k[[s,t]]_odd と一周期行列 B=[[-w,-v],[u,w]] を明示した。
N≅coker B, B²=(w²−uv)I、Nの安定End環はk。
不変部分を取ったHilbert–Burch表示から Ω²_A k≅N² を直接証明した。
従って局所特異性圏で maximal ideal m≅N² となり、次数付き安定Endは
M₂(k[η,η^{-1}])、deg η=1、非標準同型。
これにより高次Ext次元4を積と一周期性へ精密化したが、これは古典的な完備局所特異性圏の計算であり、q≠O_Eの反標準qgr標的のExt積は未同定。
既知入力はEisenbudのmatrix factorizationとBuchweitz–Orlovの安定MCM同値。これらの既知理論自体は新規成果ではない。
入力と積の区別は `research/resonance_walls.md` も参照。

## Du Val idealのcoherent qgr像と比較の第一障害

第1論文 `papers/sections/four_hearts_duval_singularity.tex` の次の結果は、
`S` が滑らかな有理弱del Pezzo、`E∈|-K_S|` が滑らかな楕円境界、
`x_i` が反標準模型 `Sbar` のDu Val点、`q∈Pic0(E)` が任意という
**指定標準gluing** にのみ適用する。

- `prop:duval-ideal-boundary-gluing`：
  `RHom(ebar,J_x,q)=0`、`RHom(J_x,q,ebar)=RΓ(E,q)`。
  非自明 `q` では両側直交、`q=O_E` でだけ次数0,1に各1次元。
- `prop:duval-offdiagonal-ext`：
  `i≠j` なら `RHom(J_i,q,J_j,q)=k[-1]`。高次数直交であっても
  互いの `Ext1` は非零。局所Gorenstein双対性と `RΓ(I_j)=0` から証明。
- `cor:duval-local-splitting`：
  非自明 `q` で `thick{ebar,J_1,...,J_r}=Perf(k)⊕thick{J_i}`。
  **この有限生成部分圏に限った分解**で、Dbar_q全体を分解しない。
- `thm:duval-point-hilbert`：
  `I_{x,q}=barPhi_q(J_x,q)` は `qgr R_q` の実在する非零coherent対象。
  `M_n=Hom_Q(ebar,sbar^nJ_x,q)` は有限生成で高次cohomologyを持たず、
  `dim M_n=d n(n+1)/2`、`H_R-H_M=1/(1-t)`、`d=K_S²`。
  中心元 `g` は `M` に正則で、
  `(M/gM)_n=H0(E,Psi_q^n q^{-1})`（n≥1）。
  `qgr B(E,Psi_q)≃coh E` で境界は `q^{-1}`。
  `q=O_E` では像は古典的ideal `I_x`。
- `prop:duval-no-graded-inclusion`：
  非自明 `q` では `Hom_grR(M,R)=0`。境界線束間のHom消滅、
  楕円THCR `B` のdomain性、反復 `g` 可除性で証明する。
  Hilbert差がpoint moduleのHilbert級数と一致しても、
  `M` を通常の次数0右idealとしては埋め込めない。
- `cor:duval-target-hom-obstruction`：
  全比較 `barPhi_q` が完全忠実なら、非自明 `q` では
  `RHom_Db(qgrR)(I_x,q,pi R)=0` が必要。**grでのHom消滅は
  qgrでのHom消滅を無条件には意味しない。**
  この標的Homを実際に計算することが現在の最優先の数学的判定問題。

主要な証明依存は境界triangleと `thm:weak-coherent-sections`、
古典的特異gluingの同定 `thm:singular-gluing-target`、
orbitの商への完全忠実性 `prop:zero-dg-quotient`、
楕円曲線のRiemann--Roch、局所Gorenstein双対性、
twisted homogeneous coordinate ringの既知の`qgr`同定である。
本文に証明を書き、その論理を内部点検した状態。
網羅的新規性確認・独立査読・形式化・現行原稿全文組版は未実施。
上の古典的な機構自体を新規成果と呼ばず、指定gluingへの組合せを評価する。

## 未解決の核心

一般の非自明qについて、誘導関手 Dbar_q→Db(qgr R_q) の完全忠実性・本質的全射性は未証明。核を除いたことやorbit上の完全忠実性だけから結論しない。q=Oは古典的局所化で解決するが、非自明qでは特異点に対応する非perfect対象の全高次Extを比較する必要がある。

指定Rains heartにおけるK_C,qのsheaf性・単純性、壁上AS模型とのpointed比較、局所・完成代数、曲面族での底変更・降下も未解決。標準固定(S,E,q)の結果を任意nc del Pezzoや全モジュライの一般論に拡張しない。

## 優先順位と具体的な着手

### P0：公表用の証明・引用・組版を閉じる

新しい有限生成証明で、degree0補正、正次数中心元、内部次数の下有界性、R作用の自然性、dg orbitから通常環への移行を独立点検する。BKSの仮定（射影性、fiber次元≤1、Rf_*O=O）を全弱del Pezzo収縮で確認する。序論はgenuine比較と弱収縮を二つの定理群として整理済み。次は主論文全体の組版・全参照を実行し、既存のADE比較とAS入力を公表前に独立監査する。

### P1：一つのA1壁でqgr側の非perfect比較を閉じる

明示的零壁 `ex:zero-elliptic-wall` を固定する。
`I_x,q∈qgr R_q` の存在、Hilbert級数、境界restriction、
`Hom_grR(M,R)=0` は既に証明したので再度未解決に戻さない。
第一の着手は、有限生成graded `M` の生成元・関係と
`qgr R` におけるsaturation/局所cohomologyを計算して
`Hom_qgr(I_x,q,pi R)` とそれに続く高次`Ext`・Yoneda積を決定すること。
もし非零なら完全忠実性の反例、零なら`RHom`全次数へ進む。
`M/gM` が境界の `q^{-1}` であることは検算条件。
`M`が点idealとしてRに埋まるとの推測を前提にしない。
さらに局所周期元`eta`とorbit生成対象との全`RHom`を比較する。

### P2：壁上のAS実現と指定heart

同じ六点・theta potentialでAS性、noetherian性、very strong性、pointed比較の入力を個別に判定する。genuine領域のVdB比較を自動延長しない。K_C,qが対象として実在することとheartで単純sheafであることを分ける。

### P3：その後の相対問題

複数零壁の交叉、perverse heart、完成局所代数、曲面族の底変更・降下は一壁の比較を閉じた後に進む。全モジュライ分類や全境界の解決を主論文公表の必要条件にしない。H3分類・次数1固有モジュライ・nc三次三様体は別正本で継続する。

## 再現と今回の検証境界

```sh
bash scripts/cloud_setup.sh
bash scripts/check.sh all
bash scripts/check.sh tex
```

全文の組版対象はdp-hearts.texとdp-hearts2.texの2本。前回までに実施したのは改稿した序論・零壁・coherent収縮の抜粋（20ページ）のLuaLaTeX組版と全ページのレイアウト画像確認である。前版ではmain主論文の全てのネストしたinputを含む静的ラベル参照を照合した。現行版の検証状態は `research/two_papers_validation.json` に記録する。静的検査はLuaLaTeX組版や全証明の再検証ではない。主論文全文・第2論文の組版と既存21検算の再実行は未実施。第2論文についてもネストした全12入力を静的検査し、81ラベル・72参照の欠落と重複がないことを確認した。本文中の新しい一般定理は計算で証明したものではない。GitHub側のソース更新とローカル抜粋の検証を区別し、詳細は `research/two_papers_validation.json` を読む。
