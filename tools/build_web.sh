#!/usr/bin/env bash
## ============================================================
## whalegal Web(HTML5) 一键打包脚本
## 用法: ./tools/build_web.sh          # 构建并部署到 server/public/
##       ./tools/build_web.sh --serve  # 构建后启动本地冒烟服务器
## 依赖: Ren'Py SDK 位于 renpy-8.5.3-sdk/（含 web 支持包 web/）
##       fonttools + brotli（字体子集化, pip install fonttools brotli）
## ============================================================
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SDK="${ROOT}/renpy-8.5.3-sdk"
OUT="${ROOT}/server/public"

## headless 环境保险
export SDL_VIDEODRIVER="${SDL_VIDEODRIVER:-dummy}"
export SDL_AUDIODRIVER="${SDL_AUDIODRIVER:-dummy}"

echo "==> [1/4] 导入剧本 (story/*.md -> game/script/story_gen/)"
python3 "${ROOT}/tools/import_story.py" | tail -3

echo "==> [2/4] 字体子集化"
python3 "${ROOT}/tools/subset_font.py"

echo "==> [3/4] Lint 检查"
"${SDK}/renpy.sh" "${ROOT}" lint --error-code >/dev/null

echo "==> [4/4] Web 打包 (Ren'Py launcher web_build)"
BUILD_TMP="$(mktemp -d /tmp/whalegal-web.XXXXXX)"
trap 'rm -rf "${BUILD_TMP}"' EXIT
(cd "${SDK}" && ./renpy.sh launcher web_build "${ROOT}" --destination "${BUILD_TMP}") >/dev/null

## ------------------------------------------------------------
## 体积闸门：CF Workers 单文件上限 25 MiB，留 1 MiB 余量。
## 超限处理：新资源走渐进下载(progressive_download.txt) / 图片量化
## ------------------------------------------------------------
GAMEZIP="$(find "${BUILD_TMP}" -name game.zip | head -1)"
if [[ -n "${GAMEZIP}" ]]; then
    SIZE="$(stat -c%s "${GAMEZIP}")"
    LIMIT=$((24 * 1024 * 1024))
    if (( SIZE > LIMIT )); then
        echo "✘ game.zip = $((SIZE / 1048576)) MiB 超过 24 MiB 闸门（CF 上限 25 MiB）！"
        echo "  排查: unzip -l ${GAMEZIP} | sort -k1 -rn | head"
        exit 1
    fi
    echo "    game.zip: $((SIZE / 1024 / 1024)) MiB ✓ (闸门 24 MiB)"
fi

echo "==> 部署到 ${OUT}"
mkdir -p "${OUT}"
rsync -a --delete "${BUILD_TMP}/" "${OUT}/"
rm -f "${OUT}/index.html.symbols"

echo "✔ 完成。产物位于 ${OUT}（$(du -sh "${OUT}" | cut -f1)）"

if [[ "${1:-}" == "--serve" ]]; then
    echo "==> 启动冒烟服务器: http://127.0.0.1:8000/"
    exec python3 "${ROOT}/server/serve.py" --host 127.0.0.1 --port 8000 --root "${OUT}"
fi
