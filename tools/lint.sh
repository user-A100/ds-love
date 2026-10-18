#!/usr/bin/env bash
## Ren'Py 脚本静态检查（CI 友好，lint 出错返回非零）
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SDK="${ROOT}/renpy-8.5.3-sdk"

export SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy
cd "${SDK}" && ./renpy.sh "${ROOT}" lint --error-code "$@"
