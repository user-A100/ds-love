# Web 开屏封面

项目根目录的 `web-presplash.png` 是网页引擎加载期间使用的封面，采用春日天台、三位女主和蓝色手写标题，底部留出加载状态区域。它与进入游戏后的主菜单背景是两个独立资源。

Ren'Py 8.5.3 的 `launcher/game/web.rpy` 会自动复制项目根目录的图片并替换输出 HTML 中的默认 `web-presplash.jpg` 引用。不需要修改 SDK 或生成的 HTML。

运行 `tools/build_web.sh` 时会检查源图、输出图片内容及 HTML 引用；封面缺失或未正确接入时停止构建。使用 `tools/publish_web.sh` 重新构建并发布后，网站加载画面才会更新。不要直接修改被构建覆盖的 `server/public/`。

当前本机 SDK 缺少 `web/` 支持包，未完成完整 Web 构建验证；访问线上站点返回 HTTP 403，未验证线上页面。发布后应在无痕窗口检查下载、Running 和进入主菜单三个阶段。若旧页面仍在，清理该站点旧的 Service Worker 和缓存后重试。

官方说明：https://www.renpy.org/doc/html/web.html#presplash
