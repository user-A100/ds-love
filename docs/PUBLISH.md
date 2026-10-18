# whalegal Web 发布教程

> 一条命令把最新游戏发布到 Cloudflare：`./tools/publish_web.sh`
> 本文说明它的原理、首次配置和常见问题。

## 0. 架构一览

```
story/*.md ──import_story.py──▶ game/script/story_gen/ (生成)
                                    │
Ren'Py SDK ──build_web.sh──▶ server/public/ (纯静态产物, gitignored)
                                    │
                        publish_web.sh ──▶ web-dist 分支 (孤儿分支, 存产物)
                                            │
                                    Cloudflare Workers (GitHub App 自动拉取)
                                            │
                                https://whalegal.<子域>.workers.dev
```

- **master** 只放源码（剧本/配置/工具/SDK 外的一切）；
- **web-dist** 只放构建产物（每次发布整体替换），Cloudflare 以它为生产分支，
  Deploy command = `npx wrangler deploy`（读取分支根的 `wrangler.jsonc`，
  把 `public/` 目录作为静态资产上传）。

## 1. 前置条件

- Ren'Py 8.5.3 SDK 位于 `renpy-8.5.3-sdk/`（含 `web/` 支持包），见仓库初始化记录
- python3（构建机自带即可）
- nginx 不参与本流程（那只是本地冒烟用的备用方案）

## 2. 日常发布（90% 的场景）

```bash
./tools/publish_web.sh
```

它依次做四件事：

1. `import_story.py` —— 剧本 md → .rpy（含日文 tl 树）
2. `lint` —— 静态检查，出错即中止
3. Ren'Py `web_build` —— 产出静态文件到 `server/public/`
4. 生成 `_headers` + `wrangler.jsonc` → rsync 进 `web-dist` 工作树 → 提交推送

推送后 Cloudflare 自动部署，约 1 分钟生效。

## 3. 首次配置 Cloudflare（已配置，留档备查）

1. GitHub 仓库 → Settings → GitHub Apps → 安装 Cloudflare Pages/Workers App
2. CF 面板 Workers & Pages → 创建项目 → 连接 whalegal 仓库
3. **生产分支设为 `web-dist`**（不是 master！master 没有产物）
4. 构建配置：
   - Build command：留空
   - Deploy command：`npx wrangler deploy`
   - Preview command：`npx wrangler deploy`
   - Root directory：`/`
5. `wrangler.jsonc` 中 `"name"` 必须与 CF 项目名一致

## 4. 验证部署

- CF 面板 Deployments 看最近一次部署是否为绿色
- 部署日志末行打印访问地址；或直接开 `https://whalegal.<子域>.workers.dev`
- 游戏内验证：主菜单 → 章节 → 对话（名牌/配音）

## 5. 常见问题

| 现象 | 原因 | 处理 |
|------|------|------|
| 页面还是旧版 | PWA service worker 缓存 | 刷新两次；或 DevTools → Application → Service Workers → Unregister，清 Cache Storage（缓存名"未抵达的心意"） |
| `Asset too large` | 单文件 > 25 MiB | 检查 `server/public` 大文件；game.zip 超限通常是资源未走渐进下载（`progressive_download.txt`） |
| 推 master 被 reject | 队友并发推送 | `git pull --rebase origin master` 后再推 |
| 发布分支推不上 | web-dist 被锁 | 检查 CF 是否正占用；稍后重试 `git push -f origin web-dist`（脚本默认非强推） |
| 本地想先看 | — | `./tools/build_web.sh --serve` → http://127.0.0.1:8000（仅本机） |

## 6. 相关文件

| 文件 | 作用 |
|------|------|
| `tools/import_story.py` | 剧本导入器（story/*.md + story/*.json → story_gen） |
| `tools/build_web.sh` | lint + web 构建 + 部署到 server/public |
| `tools/publish_web.sh` | 本教程主角：构建 + 发布 web-dist |
| `tools/gen_ui_assets.py` | 对话框贴图生成（改配色后需重跑） |
| `progressive_download.txt` | 渐进下载规则（音/图片不进 game.zip） |
| `web-presplash.png` | Web 版启动封面（仓库根，web 构建自动识别） |
