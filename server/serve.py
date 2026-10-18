#!/usr/bin/env python3
## ============================================================
## whalegal 本地开发/冒烟服务器（纯 stdlib，零依赖）
## 仅用于本机测试！生产部署使用 nginx（见 server/deploy/deploy.sh）
##
## 用法:
##   python3 server/serve.py --port 8000 --root server/public
## ============================================================
import argparse
import functools
import os
import re
import signal
import socket
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

EXTRA_MIME = {
    ".wasm": "application/wasm",
    ".js": "text/javascript",
    ".mjs": "text/javascript",
    ".json": "application/json",
    ".data": "application/octet-stream",
    ".zip": "application/zip",
    ".webp": "image/webp",
    ".pjson": "application/json",
}

RANGE_RE = re.compile(r"bytes=(\d*)-(\d*)\s*$")

## 路径模式 → Cache-Control
CACHE_RULES = [
    (("/game.zip", "/service-worker.js", "/manifest.json", "/index.html"), "no-cache"),
    ((".wasm", ".data"), "public, max-age=3600"),
    ((".png", ".jpg", ".jpeg", ".webp", ".svg", ".ico"), "public, max-age=86400"),
]


def cache_control_for(path):
    for patterns, value in CACHE_RULES:
        for p in patterns:
            if path == p or path.endswith(p):
                return value
    return None


class RenpyHandler(SimpleHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    server_version = "whalegal/0.1"

    def guess_type(self, path):
        ext = os.path.splitext(str(path))[1].lower()
        return EXTRA_MIME.get(ext) or super().guess_type(path)

    def end_headers(self):
        self.send_header("Accept-Ranges", "bytes")
        cc = cache_control_for(self.path)
        if cc:
            self.send_header("Cache-Control", cc)
        super().end_headers()

    # ---------- Range 支持（单区间，静态文件足够） ----------
    def send_head(self):
        rng = self.headers.get("Range", "")
        m = RANGE_RE.match(rng.strip())
        if not m:
            return super().send_head()

        path = self.translate_path(self.path)
        if os.path.isdir(path) or not os.path.isfile(path):
            return super().send_head()

        size = os.path.getsize(path)
        start = int(m.group(1) or 0)
        end = min(int(m.group(2)) if m.group(2) else size - 1, size - 1)
        if start > end or start >= size:
            self.send_response(416)
            self.send_header("Content-Range", f"bytes */{size}")
            self.end_headers()
            return None

        self.send_response(206)
        self.send_header("Content-Type", self.guess_type(path))
        self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
        self.send_header("Content-Length", str(end - start + 1))
        self.send_header("Last-Modified", self.date_time_string(os.path.getmtime(path)))
        self.end_headers()
        f = open(path, "rb")
        f.seek(start)
        self._range_left = end - start + 1
        return f

    def copyfile(self, source, outputfile):
        left = getattr(self, "_range_left", None)
        if left is None:
            return super().copyfile(source, outputfile)
        self._range_left = None
        while left > 0:
            chunk = source.read(min(65536, left))
            if not chunk:
                break
            outputfile.write(chunk)
            left -= len(chunk)

    def log_message(self, fmt, *args):
        if os.environ.get("WHALEGAL_QUIET"):
            return
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))


class RenpyServer(ThreadingHTTPServer):
    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, *args, reuseport=False, **kwargs):
        ## 必须在 super().__init__（触发 server_bind）之前就绪
        self.use_reuseport = reuseport
        super().__init__(*args, **kwargs)

    def server_bind(self):
        ## 多 worker 时让多个进程绑定同一端口，内核做负载均衡
        if self.use_reuseport and hasattr(socket, "SO_REUSEPORT"):
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        super().server_bind()


def serve_one(bind, port, root, reuseport):
    handler = functools.partial(RenpyHandler, directory=root)
    srv = RenpyServer((bind, port), handler, reuseport=reuseport)
    srv.serve_forever()


def main():
    ap = argparse.ArgumentParser(description="whalegal static server")
    ap.add_argument("--host", default="0.0.0.0")
    ap.add_argument("--port", type=int, default=8000)
    ap.add_argument("--root", default="server/public", help="静态根目录（相对仓库根）")
    ap.add_argument("--workers", type=int, default=1, help="进程数（多核时 = CPU 核数）")
    args = ap.parse_args()

    if not os.path.isfile(os.path.join(args.root, "index.html")):
        sys.exit(f"错误: {args.root}/index.html 不存在，请先运行 tools/build_web.sh")

    print(f"whalegal serving {args.root} at http://{args.host}:{args.port}/ "
          f"(workers={args.workers}, pid={os.getpid()})", flush=True)

    if args.workers <= 1:
        serve_one(args.host, args.port, args.root, reuseport=False)
        return

    import multiprocessing as mp
    mp.set_start_method("fork")
    procs = []
    for _ in range(args.workers - 1):
        p = mp.Process(target=serve_one, args=(args.host, args.port, args.root, True),
                       daemon=True)
        p.start()
        procs.append(p)
    try:
        serve_one(args.host, args.port, args.root, reuseport=True)
    finally:
        for p in procs:
            p.terminate()


if __name__ == "__main__":
    main()
