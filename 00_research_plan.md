# 研究方針：反標準heartとcoherent収縮

2026-11-17 / hearts-strategy-v7。再開時は本書を最初に読む。第1論文は `papers/dp-hearts.tex`（hearts-v29）、第2論文は `papers/dp-hearts2.tex`（hearts2-v1）。GitHub mainが正本である。零指数壁の現在の知識は `research/resonance_walls.md`、検証範囲は `research/two_papers_validation.json`。

## 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合して研究全体の価値を最大化する。重要な変更では理由と元の目標の達成部分・残課題を現行方針に統合し、時系列の変更記録を蓄積しない。

証明済み、追加仮定付き、証明未完成、予想、計算的観察を区別する。主張の仮定、既知入力、証明所在、未解決箇所を明記する。本文に証明を書いたこと、今回の内部点検、計算、組版、独立査読、形式化は別の状態である。誤りは依存する本文・要約・方針にも反映し、有用な反例や障害をノートに残す。

公表稿は原則日本語LuaLaTeXで、研究経緯ではなく現在の成果を理解しやすい順序に構成する。重要な先行研究は一次資料で適用条件を確認し、Introductionで既知結果と寄与を具体的に分ける。未確認の内容・書誌は推測で補わず、新規性未確認も明記する。論文本数やページ数を目的にせず、必要なら統合・分割する。有効で公表価値ある成果・証明を軽量化のため削らない。

研究ノートは現在有効な知識・着想・例・反例・計算・失敗した方法の本質的障害を整理し、日誌にしない。再取得困難な情報は簡潔に保持する。論文の全証明を重複させず参照先を示す。再開に必要な情報を会話だけに残さず、現行方針・ノート・原稿・最小限の書誌・コード・証明書・入力・再現手順から自己完結させる。旧版ZIP、バックアップ、作業ログ、重複、中間物、キャッシュを現行一式へ追加しない。必要な検証資産は保持する。

研究区切りの承諾不要Library保存は一般原則として許可済み。ただし本研究の個別指示は **GitHub mainを正本とし、保存成功時はLibraryへ重複保存せず、失敗時だけ緊急避難に用いる** ことである。既存Libraryファイルは明示指示なしに削除しない。mainは通常のfast-forwardで更新し、force push・PR・GitHub Actionsを使わない。並行更新を失わないよう保存前にheadを確認する。PDF・ZIPはGit追跡せず再生成する。生成・検証・commit・push・remote確認を分け、未実行・失敗・制約は正確に報告する。背景での継続は約束しない。

## 二論文の役割

`dp-hearts.tex` は自然heart比較、HRS/Euler選択、AS/VdBの指定比較、actual theta係数と六点復元、ADE普遍有限商と表現族、最大共鳴稠密性、零指数壁の核とcoherent収縮を扱う。`dp-hearts2.tex` は符号別Ext・混合A2・zigzag形式変形とcornerの完全Hilbert関数・162次元平坦族・計算証明を保持する。必要な一般結果は第1論文を引用し、詳細を重複させない。現在の2driverを維持し、旧3driverを復活させない。

## 現在の目標と到達点

公表の中心は「指定反標準関手がheartと根表現をどう認識し、零指数壁では何を収縮するか」である。核の同定だけではcoherent関手や商同値は得られないため、弱領域の有限生成性・有界性と収縮先の記述を優先した。

今回 `four_hearts_coherent_contraction.tex` に次を証明付きで追加した。

1. 標準弱楕円gluingの全q（有限・無限位数とも）でRは左右noetherian。各N^j(X)=⊕Hom(e,s^nX[j])は有限生成で、非零jは有限個。自然Phi:Dq→Db(qgr R)を構成する。追加のcoherent有限性仮定はこの設定では不要となった。
2. 既存のorbit核定理と合わせ、ker Phi=Nq=iota_q ker Rf_*。証明鎖は `lem:graded-boundary-finiteness` → `thm:weak-coherent-sections` → `eq:weak-coherent-kernel-final`。
3. BKS Theorem2.14を古典的反標準収縮に適用し、(Dq/Nq)^naturalを、古典的特異モデルSbar上のO^perpに境界moduleをglueしたDbar_qと同定する。`thm:singular-gluing-target`。q=OではDb(coh Sbar)を回復する。
4. 非genuineならDbar_qは全qで無限高次自己Extを持ち、proper dg圏でない。source Dqと抽象的にも同値でない。`cor:singular-gluing-unbounded`。これを未同定のDb(qgr R_q)へ転用しない。

いずれも新しい本文証明を内部点検した状態であり、独立査読・形式化・網羅的新規性確認ではない。境界切断のnoetherian性はKeeler、古典的局所化はBondal–Kapranov–Schechtmanの既知定理である。既知一般論自体を新規定理としない。

既存のgenuine導来比較・Euler選択・全ADE有限商・表現スキーム・theta係数・最大共鳴稠密性は保持している。今回これらの全証明を再監査したものではない。零指数壁の実在spherical対象・twistの不可視性と有理数および楕円関数の明示例も保持する。

## 未解決の核心

一般の非自明qについて、誘導関手 Dbar_q→Db(qgr R_q) の完全忠実性・本質的全射性は未証明。核を除いたことやorbit上の完全忠実性だけから結論しない。q=Oは古典的局所化で解決するが、非自明qでは特異点に対応する非perfect対象の全高次Extを比較する必要がある。

指定Rains heartにおけるK_C,qのsheaf性・単純性、壁上AS模型とのpointed比較、局所・完成代数、曲面族での底変更・降下も未解決。標準固定(S,E,q)の結果を任意nc del Pezzoや全モジュライの一般論に拡張しない。

## 優先順位と具体的な着手

### P0：公表用の証明・引用・組版を閉じる

新しい有限生成証明で、degree0補正、正次数中心元、内部次数の下有界性、R作用の自然性、dg orbitから通常環への移行を独立点検する。BKSの仮定（射影性、fiber次元≤1、Rf_*O=O）を全弱del Pezzo収縮で確認する。序論はgenuine比較と弱収縮を二つの定理群として整理済み。次は主論文全体の組版・全参照を実行し、既存のADE比較とAS入力を公表前に独立監査する。

### P1：一つのA1壁の非perfect対象を比較する

明示的零壁 `ex:zero-elliptic-wall` を固定し、Sbarの特異点のideal I_x∈O^perpの像をPhiで計算する。単に対象の非消失ではなく、I_xとそれを含む生成対象間の全RHomを比較する。次数付きExtの有限生成性を再び未解決に戻さない。完全忠実性の証明が不足する場合は、最初に一致しないExt次数・積・高次構造を特定する。

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

全文の組版対象はdp-hearts.texとdp-hearts2.texの2本。今回実施したのは改稿した序論・零壁・coherent収縮の抜粋（18ページ）のLuaLaTeX組版と全ページのレイアウト画像確認、抜粋内の参照・文献キー点検である。主論文全文・第2論文の組版と既存21検算の再実行は未実施。本文中の新しい一般定理は計算で証明したものではない。GitHub側のソース更新とローカル抜粋の検証を区別し、詳細は `research/two_papers_validation.json` を読む。
