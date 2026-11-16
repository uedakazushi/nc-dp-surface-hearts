# Codex指示：反標準heartの認識と根圏

2026-11-16 / hearts-strategy-v2。GitHub mainが正本。最初に00_research_plan.md、research/current_assessment.md、research/four_hearts_plan.mdを読み、必要な研究ノート・3主原稿・sectionへ進む。

## 目標と優先順位

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性から研究全体の価値を最大化する。最優先は、指定構造対象・自然関手による反標準heartの認識と、実在する有限ADE根圏によるheart選択を公表可能な主定理へまとめること。次の新規構造目標は、全ADE根圏のabel圏同定と元のA=R/(g−1)の有限商である。00_research_plan.mdのP0→P1を先行し、P2の構造補題へ進む。零指数壁と相対化は後順位。

既に原稿に証明のあるEuler chamber選択、全heartの有限単純tilt分解、同じ最後のraw blow-upでのVdB関手同定、actual potentialと元六点の復元を未解決として再実行しない。全ADEのmod Π同定と実際のA作用は未証明の目標として扱う。

## 必須の区別

- 十一因子の零指数の古典的壁は一般位置/genuine仮定を外れる。非零指数のRains共鳴と混同しない。壁上へ既存導来同値を自動延長しない。
- 実在単純根と数値的共鳴、指定関手のt-exact性と別の同値、raw blow-upとsection model、全対象のEuler符号と全商/部分対象によるtorsion判定を分ける。
- D^b(境界外Serre圏)をambient部分圏と同一視しない。162次元cornerとAの根表現を支配する有限商を同一視しない。
- 規格化AS比較のfull very strong helixとrolled-up同定は入力である。全potentialのAS性/noetherian性、全heart分類、形式的分枝の大域モジュライ成分性を推測しない。
- Rains 2025の該当本文、AOU/OU、既知のzigzag形式性・Dynkin torsion分類を一次資料で照合する。既知の共鳴稠密性や一般corner有限性を単独の新規成果にしない。

## 執筆・保存・再現

原稿は原則日本語LuaLaTeX。証明記載、今回の証明点検、有限計算、組版、保存、外部査読を分けて報告する。主張の仮定・依存結果・証明所在と未解決箇所を同期する。研究ノートは現行知識を整理し、作業日誌にしない。価値ある数学・証明・再現資産を削除して軽量化しない。3原稿を3公表論文と決めつけず、中心定理で統合・分割を判断する。H3分類・次数1固有モジュライ・nc三次三様体を再取り込みしない。

研究区切りで原稿・ノート・方針・必要な検証資産を自己完結した現行版にする。約15分を保存checkpointの目安に、共有mainの更新を確認して通常のfast-forwardで直接保存し、remote SHAを照合する。PR・GitHub Actions・force pushは使わない。PDF・ZIP・中間物・キャッシュは追跡しない。GitHub保存失敗時のみ、許可済みのLibrary緊急保存を用いる。背景での自動継続は約束しない。

今回の環境では19検算は成功したが、LuaLaTeXのformat・LaTeX本文・LuaTeX-jaが欠落して全文組版を実行できていない。原稿エラーとして扱わず、環境が整った時点で再組版する。

## Cloud Codex の実行方法

Cloud環境の初期化ではリポジトリrootから `bash scripts/cloud_setup.sh` を実行する。Debian/Ubuntuのaptとpipを使う（TeX Live日本語一式の初回導入は容量と時間を要する）。start時は `bash scripts/check.sh fast` で依存関係と研究コードを確認する。詳しくは `docs/CLOUD_CODEX.md`。

- 研究の各区切りは `bash scripts/check.sh fast`、証明や計算を変更した時は該当する `computations/verify_*.py` と必要に応じ `bash scripts/check.sh all` を実行する。公表原稿の更新では `bash scripts/check.sh tex` で3本を組版し、全文検査が必要なら `bash scripts/check.sh full` とする。出力は `build/` に保存しGit追跡しない。
- Codex Cloudのタスクは各々独立したcheckoutであり、`main`へのpush権限やnetworkは環境により異なる。変更をcommitする前に `git status --short` と `git fetch origin main` を確認する。mainが進んでいればその変更を安全に統合し、force pushせず通常のfast-forwardのみ。直接pushできなければcommitを保持し、ブロック理由を報告する。PRやGitHub Actionsへ自動的に切り替えない。
- 一つの数学的補題・証明修正・整った計算チェックを最小作業単位とし、約15分をcheckpointの目安にする。作業を止める質問を増やさず、上位方針のP0→P1→P2へ自律的に進む。ただし未証明主張を完成扱いせず、外部ネットワーク・引用・セットアップ不能を正確に報告する。
