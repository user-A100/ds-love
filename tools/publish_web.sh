#!/usr/bin/env bash
## ============================================================
## publish_web.sh —— 发布 Web 构建产物到 web-dist 孤儿分支
## 供 Cloudflare Pages / GitHub Pages 等静态托管拉取：
##   生产分支 = web-dist，构建命令留空，输出目录 = /
## 用法: ./tools/publish_web.sh
## ============================================================
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BRANCH="web-dist"
WT="$(mktemp -d /tmp/whalegal-publish.XXXXXX)"
trap 'git worktree remove --force "$WT" 2>/dev/null || true' EXIT

cd "${ROOT}"

echo "==> [1/3] 构建 Web 包"
./tools/build_web.sh

echo "==> [2/3] 生成 Cloudflare 配置（_headers + wrangler.jsonc）"
cat > server/public/_headers <<'EOF'
/game.zip
  Cache-Control: no-cache
/service-worker.js
  Cache-Control: no-cache
/manifest.json
  Cache-Control: no-cache
/renpy.wasm
  Cache-Control: public, max-age=3600
/renpy.data
  Cache-Control: public, max-age=3600
EOF

## Workers 静态资产配置：Deploy command = npx wrangler deploy
## 注意 name 必须与 CF 面板里的 Worker/项目名一致
cat > server/public/wrangler.jsonc <<'EOF'
{
  // whalegal —— 纯静态资产 Worker（Ren'Py web 构建）
  // 若 CF 面板中的项目名不是 whalegal，请同步修改此处 name
  "name": "whalegal",
  "compatibility_date": "2025-01-01",
  "assets": {
    "directory": ".",
    "html_handling": "auto-trailing-slash"
  }
}
EOF

echo "==> [3/3] 发布到 ${BRANCH} 分支"
if git show-ref --verify --quiet "refs/remotes/origin/${BRANCH}"; then
    git fetch origin "${BRANCH}"
    git worktree add "${WT}" -b "${BRANCH}" --track "origin/${BRANCH}" 2>/dev/null \
        || git worktree add "${WT}" "${BRANCH}"
else
    git worktree add --orphan -b "${BRANCH}" "${WT}"
fi

rsync -a --delete --exclude '.git' "${ROOT}/server/public/" "${WT}/"

cd "${WT}"
git add -A
if git diff --cached --quiet; then
    echo "无变化，跳过发布"
else
    git commit -m "web: deploy $(date -u +%FT%TZ)"
    git push ${GIT_PUSH_FORCE:+-f} origin "${BRANCH}"
    echo "✔ 已推送 ${BRANCH}，Cloudflare Pages 将自动部署"
fi
