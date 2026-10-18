#!/usr/bin/env bash
## ============================================================
## whalegal 一键部署（nginx 方案）
## 在部署主机上执行: ./server/deploy/deploy.sh [--port N]
## 前置: 仓库已 clone（任意位置）、已安装 nginx、python3（构建用）
## 流程: 构建 Web 包 -> 从模板渲染 nginx 配置 -> 启用 -> reload
## ============================================================
set -euo pipefail

## 仓库根 = 本脚本上两级，不写死绝对路径
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
PORT="80"

while [[ $# -gt 0 ]]; do
    case "$1" in
        --port) PORT="$2"; shift 2 ;;
        *) echo "未知参数: $1"; exit 1 ;;
    esac
done

if ! command -v nginx >/dev/null 2>&1; then
    echo "错误: 未安装 nginx（sudo apt install nginx）" >&2
    exit 1
fi

if [[ $EUID -ne 0 ]]; then
    SUDO="sudo"
else
    SUDO=""
fi

echo "==> [1/3] 构建 Web 包"
cd "${ROOT}"
./tools/build_web.sh

## 确定 include 目录（Debian 系 sites-enabled / RHEL 系 conf.d）
if [[ -d /etc/nginx/sites-enabled ]]; then
    NGINX_DIR="/etc/nginx/sites-available"
    ENABLE_DIR="/etc/nginx/sites-enabled"
elif [[ -d /etc/nginx/conf.d ]]; then
    NGINX_DIR="/etc/nginx/conf.d"
    ENABLE_DIR=""
else
    echo "错误: 找不到 nginx 配置目录" >&2
    exit 1
fi

echo "==> [2/3] 渲染并安装 nginx 配置 (root=${ROOT}, port=${PORT})"
sed -e "s|__ROOT__|${ROOT}|g" -e "s|__PORT__|${PORT}|g" \
    "${ROOT}/server/deploy/nginx.conf.template" \
    | ${SUDO} tee "${NGINX_DIR}/whalegal.conf" > /dev/null

if [[ -n "${ENABLE_DIR}" ]]; then
    ${SUDO} ln -sf "${NGINX_DIR}/whalegal.conf" "${ENABLE_DIR}/whalegal.conf"
    ## 关掉默认站点，避免端口冲突
    ${SUDO} rm -f "${ENABLE_DIR}/default"
fi

echo "==> [3/3] 校验并重载 nginx"
${SUDO} nginx -t
${SUDO} systemctl reload nginx 2>/dev/null || ${SUDO} nginx -s reload

IP="$(hostname -I 2>/dev/null | awk '{print $1}')"
echo "✔ 部署完成: http://${IP}:${PORT}/"
echo "  更新游戏只需: git pull && ./tools/build_web.sh  （静态文件即时生效）"
