# 四heart比較の実施方針

2026-11-17 / hearts-strategy-v5。恒常原則と研究全体の達成基準は `../00_research_plan.md`。現在の数学本文はhearts-v27。最大共鳴と零指数壁の知識は `resonance_walls.md`、今回の検証は `resonance_walls_validation.json` を参照する。

## 中心結果の構成

自然反標準導来比較 → Euler標数によるheart選択 → 規格化AS比較・actual theta係数と元六点 → 最大共鳴の稠密性と零指数壁 → 混合A2・全ADE有限商・具体例、という主題を保つ。既存の中心結果と有効な証明は削らない。cornerの完全Hilbert関数と共鳴の形式変形は補助原稿に保持する。

## 現在有効な入力

右加群の辞書L=L1、q=L0/L1、sheaf-normalized mutationと(U+)を固定する。標準AS実現のfull very strong性とrolled-up同定を、任意potentialに自動適用しない。全ADEのpreprojective模型・普遍有限商・表現スキームは既存本文に証明があり、今回の零壁研究で再証明したものではない。

## 今回統合したこと

最大共鳴の整数表示と次数1–6の稠密性は `four_hearts_maximal_density.tex` に完全証明を置いた。既存の整列定理との組合せで、指定heartの一致・不一致の両集合が稠密で非構成可能となる。

`four_hearts_zero_walls.tex` では古典的な全次数の収縮障害、有理数上の一壁の方程式、Euler列の相殺を主論文へ統合した。標準弱楕円gluingでは、全orbit核Nqが古典的反標準収縮の核の像に一致し、全qで非零spherical対象が残る。dg商はorbit環を変えず、零指数twistはその環から見えない。

## 次の着手

まず新しい核同定とdg商の証明・文献入力を独立点検し、主論文全体を組版する。次に明示的なA1零壁で次数付きExtの有限生成性・有界性を確認する。coherent Phiの核の同定は条件付きであり、商からqgrへの完全忠実性・全射性を別に証明する。完了基準は単なる核の再計算でなく、実際の収縮比較を閉じる補題である。

零壁の実際の楕円potentialはadmissibleでcornerが無限次元となるが、そのAS模型と弱gluingの指定比較は未構成。ここで壊れる入力を一つずつ確かめる。複数壁、perverse heart、完成局所代数、曲面族の底変更・降下は後段とする。

今回の追加二節は10ページ抜粋として組版済み。全文組版と旧20検算の再実行は未実施。今後の検証で実行した範囲を正確に書き換え、以前のvalidationを現在の成功として引用しない。
