# 現在の評価と公表準備

2026-11-17 / hearts-v33。主論文 `papers/dp-hearts.tex` と補完論文 `papers/dp-hearts2.tex` の2本を維持する。研究方針は `00_research_plan.md`、零壁の証明依存は `resonance_walls.md`、実行した検証は `two_papers_validation.json` にある。

## 中心的な価値

genuineな領域では、構造対象と自然反標準関手によるheartの認識を、実在ADE根のEuler標数とアフィン代数の普遍有限商へつなぐ点が公表の核である。AS/VdB比較は指定gluing・規格化mutation・very strong helixなどの入力を別々に確認して使う。162次元cornerの一様Hilbert関数と平坦族、zigzag形式変形の詳細は第2論文に保持する。

弱領域では、零指数spherical対象と全orbit核の同定に加え、coherent反標準関手の有限生成性・有界性を証明できた。BKSの古典的局所化を使い、dg商を古典的特異モデル上のgluingとして記述できたことが今回の主要な前進である。

## 証明状態

新節の `thm:weak-coherent-sections` と `thm:singular-gluing-target`、商の無限高次自己Extの系は本文に証明を記載し、内部点検した。Keelerのnoetherian性とBKSのfiber次元1の局所化は既知入力であり、一般定理自体の新規性を主張しない。新しい組合せの網羅的新規性・独立査読・機械形式化は未了。

既存の全ADEのabel同定・普遍商・Frobenius判定・Repスキーム、theta係数・六点復元、最大共鳴非構成可能性は保持する。今回はこれら全ての証明と全引用を再監査したのではない。元の生成元の全作用行列、相対stack降下、任意potentialのAS性は未計算または未証明のままである。

## 今回追加した局所特異性の検出

主論文に独立したDu Val局所節を追加した。共通部分圏Bbarのperfect商はOrlovのD_sg(Sbar)と同値であり、特異点idealの高次Extは全q、n≥3で4δij。前者は評価射による直交射影、後者はTateの既知の最小自由解消による。独立した新規性の完全確認ではない。次元4の計算からADE型の区別や非自明qの反標準qgr同定は従わない。

## 今回の数学的進展：完全部分圏と残余特異性

`papers/sections/four_hearts_orbit_core.tex` に2定理と1補題を追加した。
まず自然coherent反標準関手は、弱gluingの全qでも反標準orbit上で完全忠実で、thick closureに制限すればtargetのorbit-perfect coreとdg同値。
Rains 2022 Corollary 3.8のtarget Extと境界traceの自然性を既知入力とする。
次に非genuineな場合、orbit-perfect coreは収縮dg商全体を生成せず、残余商は必ず非零。
q=O_EではこれがPerf(Sbar)とD_sg(Sbar)を回復する。
結論は非自明qの全Db(qgrR_q)同値ではなく、むしろ不明部分がorbitの外側に残ることを示す。
本文の証明は追加済みで、全行の独立査読・網羅的新規性確認は未実施。

## A1壁の新たな局所到達点

`four_hearts_a1_stable_model.tex` で A1を符号反転不変環として表示し、
一周期行列因子化、第二syzygyのN²分解、rank-one MCMの安定End=kを直接証明した。
局所特異性圏での特異点idealのgraded stable EndはM₂(k[η±1]) (degη=1)。
普通の高次Extの次元列から積と周期性へ進んだが、いずれもqに共通な古典側の局所模型である。
Tate、Eisenbud、Buchweitz–Orlovが既知入力であり、独立査読や全面的な新規性確認は未了。

## 特異点idealとexceptional対象の間のgluingの跳び

`prop:duval-ideal-boundary-gluing` では、滑らかな楕円境界EがDu Val点xを避けることから
`L i^*I_x=O_E` を使い、`RHom(bar e,J_x,q)=0` と
`RHom(J_x,q,bar e)=RΓ(E,q)` を直接計算した。
非自明な次数0線束qでは両側のExtが消え、自明なqでは次数0,1に1次元ずつ残る。
既存の自己Extのq不変性と、exceptional対象へのgluingのq依存性を分ける補強である。
証明は本文に記載し内部点検した。局所gluingから全圏の分解や
非自明qのqgr導来同値を結論していない。新規性の網羅調査・独立査読は未了。

## 今残る核心

一般qの特異gluing Dbar_q と Db(qgrR_q) の自然比較は未完成。coherent関手の存在と全核だけでは完全忠実性・本質的全射性は得られない。非perfect対象の高次Extを扱う必要があり、A1壁の特異点ideal I_xが具体的な着手対象である。q=Oでは古典的局所化に帰着する。

非genuineなDbar_qは全qで無限高次自己Extを持ち、properではない。この事実に合わせて本文のproperness仮定を滑らかなsourceに限定した。商のnoetherian heart、指定Rains heart内の収縮対象、壁上AS比較、相対収縮は別に調べる。

## 公表向けの改稿

要約を短くし、序論をgenuine比較・有限次元表現と弱収縮の二つの定理群に整理した。各仮定と既知入力、解決した有限性、残るqgr比較を対応付けた。基礎のHRS・ample orbit・cornerの証明と、既存の明示例・計算資産は保持した。

## 今回の実行範囲

前段階で改稿した序論・基礎、零指数壁、新しいcoherent収縮の3節を20ページの抜粋として組版し、全20ページのレイアウト画像を確認した。今回のv33ではネストした全inputを含む静的ラベル参照の整合性を確認した。抜粋の内部参照・文献キー・組版に未解決の警告はない。抜粋外の主論文参照は偽の番号を入れず「*」で区別した。全文と第2論文の組版、既存21本の数学的検算は今回は再実行していない。全文のページ数や投稿可能性の最終判定を、この抜粋検証から主張しない。
