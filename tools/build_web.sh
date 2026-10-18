#!/usr/bin/env bash
## ============================================================
## whalegal Web(HTML5) 一键打包脚本
## 用法: ./tools/build_web.sh          # 构建并部署到 server/public/
##       ./tools/build_web.sh --serve  # 构建后启动本地冒烟服务器
## 依赖: Ren'Py SDK 位于 renpy-8.5.3-sdk/（含 web 支持包 web/）
## ============================================================
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SDK="${ROOT}/renpy-8.5.3-sdk"
OUT="${ROOT}/server/public"

## Ren'Py 会从项目根目录读取此图，替换浏览器启动时的默认封面。
if [[ ! -s "${ROOT}/web-presplash.png" ]]; then
    echo "缺少项目开屏封面：${ROOT}/web-presplash.png" >&2
    exit 1
fi

## headless 环境保险
export SDL_VIDEODRIVER="${SDL_VIDEODRIVER:-dummy}"
export SDL_AUDIODRIVER="${SDL_AUDIODRIVER:-dummy}"

echo "==> [0/3] 导入剧本 (story/*.md -> game/script/story_gen/)"
python3 "${ROOT}/tools/import_story.py" | tail -3

echo "==> [1/3] Lint 检查"
"${SDK}/renpy.sh" "${ROOT}" lint --error-code >/dev/null

echo "==> [2/3] Web 打包 (Ren'Py launcher web_build)"
BUILD_TMP="$(mktemp -d /tmp/whalegal-web.XXXXXX)"
trap 'rm -rf "${BUILD_TMP}"' EXIT
(cd "${SDK}" && ./renpy.sh launcher web_build "${ROOT}" --destination "${BUILD_TMP}")

## 确认构建已接入定制封面，避免发布默认加载图。
cmp "${ROOT}/web-presplash.png" "${BUILD_TMP}/web-presplash.png"
if ! grep -q 'web-presplash.png' "${BUILD_TMP}/index.html"; then
    echo "Web 构建未引用项目开屏封面，停止发布。" >&2
    exit 1
fi

## Cloudflare Workers 单文件上限为 25 MiB。
python3 - "${BUILD_TMP}" <<'PY'
from pathlib import Path
import sys
oversized = [p for p in Path(sys.argv[1]).rglob('*') if p.is_file() and p.stat().st_size > 25 * 1024 * 1024]
if oversized:
    raise SystemExit('构建文件超过 Cloudflare 25 MiB 上限：' + ', '.join(str(p) for p in oversized))
PY

echo "==> [3/3] 部署到 ${OUT}"
mkdir -p "${OUT}"
rsync -a --delete "${BUILD_TMP}/" "${OUT}/"
rm -f "${OUT}/index.html.symbols"

echo "✔ 完成。产物位于 ${OUT}（$(du -sh "${OUT}" | cut -f1)）"

if [[ "${1:-}" == "--serve" ]]; then
    echo "==> 启动冒烟服务器: http://127.0.0.1:8000/"
    exec python3 "${ROOT}/server/serve.py" --host 127.0.0.1 --port 8000 --root "${OUT}"
fi
