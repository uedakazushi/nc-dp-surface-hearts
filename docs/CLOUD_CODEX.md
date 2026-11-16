# Cloud Codex実行環境

2026-11-16。研究方針は `00_research_plan.md`、Codex指示は `AGENTS.md` を最初に読む。GitHub mainが唯一の正本。セットアップはDebian/Ubuntu系のCloud VMを想定する。Mac/ローカルのTeX Liveは変更しない。

## Cloud環境を作成する操作（アカウント側）

ChatGPT/Codexで **Work in > Cloud > Select environment > Create environment** を開き、`uedakazushi/nc-dp-surface-hearts` のmainを選ぶ。GitHub接続が未設定なら接続する。環境の初期設定を作る際、下記を指定する。

- **Install script**: `bash scripts/cloud_setup.sh`
- **Start skill** または開始時のチェック: `bash scripts/check.sh fast`
- Python 3とDebian/Ubuntuのapt/sudoが使えるVMを選ぶ。TeX Liveと日本語フォントの初回導入は大きいため、ビルド環境を再利用する。
- 文献・新規性調査に必要な場合のみWebアクセスを許可する（少なくとも `arxiv.org`, `export.arxiv.org`, `doi.org`, `github.com` など）。アクセスの可否はタスク側でも確認する。
- GitHub mainへの直接push権限は別途確認する。環境の公開（Publish）と必要な個人認可はユーザーがCloud画面で行う。リポジトリのファイル変更だけで環境が自動作成・公開されるわけではない。

Setup検査が完了したら Publish し、新しいCloudタスクで以下を開始する。

> `AGENTS.md` と `00_research_plan.md` を読み、P0→P1を優先して研究を進めてください。まず `bash scripts/check.sh fast` を実行し、既存の主定理の仮定・一次資料・具体例の適用を点検してください。区切りで変更を検算・commitし、権限があればmainにfast-forward pushしてください。PR、GitHub Actions、force pushを使わず、未証明の全ADE有限商を定理扱いしないでください。

## 端末での検証コマンド

```bash
bash scripts/cloud_setup.sh  # 環境作成時の一回
bash scripts/check.sh fast    # 日常的な小さなcheckpoint
bash scripts/check.sh all     # 全19本のPython検算
bash scripts/check.sh tex     # 3つのLuaLaTeX主原稿
bash scripts/check.sh full    # all + tex
```

`scripts/check.sh` は `.venv/bin/python` があれば使い、無ければ `python3` を使う。検算結果とPDFなどは `build/` に置き、Git追跡しない。すべてのPython検算の成功と数学的証明の正しさは別の状態。TeXに異常が出た場合は最初に欠落パッケージとソースのエラーを区別する。

## 作業・保存ルール

各Cloudタスクは独立したcheckoutなので、作業開始時・push前に `git status -sb` と `git fetch origin main` を確認する。先行するmain更新を失わないよう安全に統合し、通常のfast-forward pushのみを行う。15分程度または数学的に切りの良い箇所でcheckpointを作る。権限がなくpushできなければ、保存済みと称さず、コミットと障害を明記する。GitHub Actions・PR・PDF追跡・旧bundleの蓄積は行わない。

この手順書はリポジトリの **設定ファイル** であり、Codex Cloud上の環境作成・apt導入・全文組版・main push権限は、このコミットだけでは検証されていない。
