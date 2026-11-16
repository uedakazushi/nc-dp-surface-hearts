# 四heart比較とcoherent収縮の実施方針

2026-11-17 / hearts-strategy-v8。全体の目標・恒常原則は `../00_research_plan.md`。主論文は `papers/dp-hearts.tex`（hearts-v30）、補完論文は `papers/dp-hearts2.tex`（hearts2-v1）。

## 現在の公表構成

主論文の序論はgenuine領域の自然比較・Euler選択・ADE有限商と、弱領域のcoherent反標準関手・収縮核・特異gluingという二つの定理群を区別する。最大共鳴稠密性と零指数対象の消失も別現象として説明する。基礎的HRS・ample orbit・cornerの証明、actual theta係数、有限次元表現論、明示例を保持する。

## 解決した有限性と残る比較

`four_hearts_coherent_contraction.tex` の境界切断の有限生成→gによる商→下有界graded Nakayama→cohomological有界性により、全標準弱gluingでPhi:Dq→Db(qgrR)を構成した。kerPhiは既存orbit核に一致する。Keelerの定理は有限位数も含む。BKS Theorem2.14を古典的反標準収縮へ適用し、dg商はSbar上のO^perpに境界moduleをglueしたDbar_qとなる。

残るのは一般qのDbar_q→Db(qgrR)の全RHom比較と全射性。A1特異点のideal I_xがO^perpに入り、高次Extが無限に残ることを使って局所模型を作る。genuineのInd-orbit生成の論証を弱領域へそのまま適用せず、核と非perfect対象を明示して扱う。

## 局所特異性の次の具体的検査

`four_hearts_duval_singularity.tex` ではBbarの特異性商と高次Ext次元4δijを証明した。A1壁で反標準qgr側に対応する対象を構成し、Yoneda積・2周期性と商からの全RHom写像を比較する。次元一致は完全忠実性を意味しないため、積と高次構造の一致も検査する。

## 最優先の点検

degree0補正、右R作用、g進filtrationの固定全次数での有限性、dg代数のgood truncationを確認する。BKSの幾何学的仮定を確認する。次に全文を組版し、既存のADE形式性→abel圏復元と特殊共鳴族のAS入力を独立監査する。二論文の証明状態と参照先を揃え、一般qのqgr比較・壁上heart・AS実現・相対化を完成扱いしない。

## 検証と保存

今回のLuaLaTeX確認は改稿4節の20ページ抜粋のみで、全ページのレイアウトを画像確認した。全文・第2論文の組版および21検算の再実行は未実施。詳細は `two_papers_validation.json`。共有mainを確認して通常のfast-forwardで保存し、PDF・ZIP・中間物は追跡しない。
