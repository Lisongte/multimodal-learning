#!/usr/bin/env bash
# Browser-based GitHub login using the project-local official CLI.
set -euo pipefail
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"
export GH_CONFIG_DIR="$repo_root/.local/gh-config"
gh_binary="$repo_root/.local/bin/gh"
if [[ ! -x "$gh_binary" ]]; then
  printf '%s\n' '未找到项目本地 GitHub CLI，请先完成工具安装。' >&2
  exit 1
fi
"$gh_binary" auth login --hostname github.com --git-protocol https --web --skip-ssh-key
# Scope authentication to this repository, without changing global Git config.
git config --local --replace-all credential.https://github.com.helper ''
git config --local --add credential.https://github.com.helper "!GH_CONFIG_DIR='$GH_CONFIG_DIR' '$gh_binary' auth git-credential"
"$gh_binary" auth status --hostname github.com
printf '%s\n' '登录完成。现在可执行 bash scripts/sync.sh "学习：当天内容"。'
