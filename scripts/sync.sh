#!/usr/bin/env bash
# Manually commit the learning folders and push; never force-push.
set -euo pipefail
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

if [[ $# -ne 1 || -z "$1" ]]; then
  printf '%s\n' 'Usage: bash scripts/sync.sh "描述今天的学习进度"' >&2
  exit 2
fi
if ! git remote get-url origin >/dev/null 2>&1; then
  printf '%s\n' '尚未连接 GitHub。请先配置真实的 origin 地址，参见 README。' >&2
  exit 1
fi
branch="$(git symbolic-ref --quiet --short HEAD)" || {
  printf '%s\n' '当前为 detached HEAD，请先切换到学习分支。' >&2
  exit 1
}
git status --short
git add -- README.md ROADMAP.md .gitignore scripts/ progress/ notes/ exercises/ src/
git diff --cached --stat
if ! git diff --cached --quiet; then
  git commit -m "$1"
else
  printf '%s\n' '没有新的修改需要提交，将尝试推送已有提交。'
fi
git push --set-upstream origin "$branch"
printf '%s\n' 'GitHub 推送成功。'
