# Codex指示：反標準heartと零指数根壁

2026-11-17 / hearts-strategy-v6。最初に `00_research_plan.md`、`research/resonance_walls.md` を読む。第1論文 `papers/dp-hearts.tex`（hearts-v28）、第2論文 `papers/dp-hearts2.tex`（hearts2-v1）と必要なsectionへ進む。GitHub mainが正本。

## 現在の優先順位

価値の最大化を最優先にする。主論文には最大共鳴の稠密性と零指数根壁を追加済み。標準弱楕円gluingの全orbit核を古典的反標準収縮の核に同定した `thm:weak-orbit-kernel` と、orbit環を保存するdg商を独立点検する。その後、一つのA1壁でcoherent導来切断の有限生成性・有界性、商から反標準qgrへの比較を進める。既存のEuler選択・ADE有限商・actual potentialを未解決に戻さない。

## 必須の区別

- 最大共鳴は非零指数のgenuineな点の結果。零指数壁は反標準orbitに見えない対象を持つ。両者を同じHRS tiltの問題にしない。
- Nq-tail=Nq=iota_q ker Rf_*は固定(S,E)の標準弱gluingでのdg核の同定。任意の非可換曲面・全モジュライの相対定理ではない。
- 非可換零指数spherical対象は直接構成したが、任意のRains heartで単純sheafであるとは証明していない。
- ker Phi=Nqには本文のcoherent有限性仮定が必要。dg商とDb(qgr R)の同値、特異点型、壁上AS比較は未証明。
- 数値共鳴とsheaf存在、raw blow-upとsection model、指定関手と任意の同値、有限長heartの内部Extとambient Extを分ける。162次元cornerと普遍アフィン有限商も別物。
- 形式性・preprojective・Morita・収縮・twistの一般理論は既知入力。文献の仮定を一次資料で照合し、網羅的新規性・外部査読を完了したと主張しない。

## 検証・執筆・保存

日本語LuaLaTeXを用い、証明の状態と依存関係を本文・要約・方針で揃える。価値ある証明を削除して軽量化せず、ノートを作業日誌にしない。新しい検算は `python3 computations/verify_density_zero_walls.py`。既存の `bash scripts/check.sh all` は全verifyスクリプトを実行する。`bash scripts/check.sh tex` は2原稿（dp-hearts.tex、dp-hearts2.tex）を組版する。今回の二論文統合では全ラベル・参照・文献キー・input依存の静的点検を行った。新しい2driverの全文組版はまだ実行していない。旧layoutの組版記録を新layoutの検証と混同しない。

Cloud環境の導入は `bash scripts/cloud_setup.sh`、手順は `docs/CLOUD_CODEX.md`。約15分または数学的な区切りを保存checkpointの目安とし、並行mainを確認・安全に統合して通常のfast-forwardで直接保存する。force push・PR・GitHub Actionsを使わない。PDF・ZIP・中間物・環境cacheを追跡しない。保存とremote確認を区別する。

研究区切りのLibrary保存は一般に許可済みだが、本研究ではGitHub保存失敗時のみ緊急避難として用いる。成功時の重複保存、既存Library資料の無断削除、背景での自動継続の約束をしない。権限やネットワークの障害は未完了として報告する。現在の一式から再開できるよう方針・ノート・原稿・再現コードを同期する。

## 二論文の責任分担

`dp-hearts.tex` は圏の幾何学的比較・最大共鳴・零壁・ADE普遍有限商を証明する。`dp-hearts2.tex` は主論文にない符号別Extと混合拡大、固定dg圏の形式変形、cubic cornerの一様Hilbert・計算証明を収める。主論文の数学的帰結を再証明して重複させず、必要な前提は主論文を引用する。未完成の一般化を定理扱いしない。`papers/`に旧3原稿driverを復活させない。2原稿間の参照を別個の組版環境で検証する。将来、中心定理の変化に応じて統合・分割を見直してよい。
