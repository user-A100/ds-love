![未抵达的心意](docs/banner.png)

# 未抵达的心意（ds-love）

沙雕系 galgame，Ren'Py 8.5.3 开发，HTML5 发布，日语 TTS 配音。

日文正文已接入游戏，覆盖序章至第六章和 DeepSeek 真结局。新玩家默认日文，设置中可切换简体中文。章节导航、路线选项及菜单同步本地化；真实日语配音尚未合成。文案生成、验证及配音接入方式见 [日文版接入说明](docs/japanese-integration.md)。

## 快速开始

```bash
# 0. 前置：Ren'Py 8.5.3 SDK 已置于 renpy-8.5.3-sdk/（含 web 支持包 web/）
#    conda 环境: conda activate whalegal  (Python 3.12，与 Ren'Py 8.x 一致)

# 1. 本地测试（lint + web 构建 + 冒烟服务器三合一）
./tools/build_web.sh --serve     # 打开 http://127.0.0.1:8000/

# 2. 仅静态检查
./tools/lint.sh

# 3. 服务器部署（nginx，见下）
```

## 目录结构

```
whalegal/
├── game/                # ★ Ren'Py 游戏主体（仓库根即项目根）
│   ├── script/          #   剧本（按章节拆分 .rpy）
│   ├── audio/{bgm,sfx,voice}/
│   ├── images/ fonts/ gui/
├── story/               # ★ 文案源（master 版沙雕文本）
│   ├── chapters/        #   每章一个文件
│   └── voice_map.json   #   行ID→文本→角色音线（TTS 单一事实来源）
├── tts/                 # ★ TTS 离线流水线（引擎权重 gitignore）
├── server/              # ★ 部署设施
│   ├── public/          #   web 构建产物（gitignored，勿手改）
│   └── deploy/          #   nginx 模板 + 一键部署脚本
├── tools/               #   build_web.sh / lint.sh
├── assets_src/          #   源资产（PSD 等大文件，gitignore）
├── docs/                #   设计文档
└── progressive_download.txt   # web 渐进下载规则（声音/大图按需加载）
```

## Web 打包（HTML5）

现有美术已按正文接入；逐场核对页、素材缺口与维护命令见 [游戏美术接入](docs/art/integration/README.md)。

- Ren'Py 8.5 原生支持 web 导出（WASM），命令行入口：
  `renpy.sh launcher web_build <项目根> --destination <输出目录>`
  （必须在 SDK 目录内执行 CLI，`launcher` 才能被解析。）
- `tools/build_web.sh` 已封装：lint → 打包 → 部署到 `server/public/`。
- 产物为纯静态文件：`index.html` + `game.zip`（游戏数据）+ `renpy.wasm`（引擎）。
- `.wasm` 必须以 `application/wasm` MIME 提供，nginx 模板已配置。

## 部署与发布（Cloudflare）

**日常发布一条命令**：

```bash
./tools/publish_web.sh     # 构建 → 推 web-dist 分支 → CF 自动部署（约 1 分钟生效）
```

线上地址：`https://whalegal.<子域>.workers.dev`（生产分支 = `web-dist`，
产物为纯静态文件，Deploy command = `npx wrangler deploy`）。

完整原理、首次配置步骤与常见问题见 **[docs/PUBLISH.md](docs/PUBLISH.md)**。
自建 nginx 备用方案仍在 `server/deploy/`（校园网内自建服务器有封号风险，仅限校外 VPS）。

## 已知坑（重要）

1. **CLI 相对路径**：`renpy.sh launcher ...` 必须在 SDK 目录内运行，否则
   `launcher` 按 CWD 解析报 "Base directory does not exist"。
2. **中文字体**：Ren'Py common 将默认字体硬编码为 DejaVuSans.ttf（无 CJK）。
   本项目用 `config.font_replacement_map` 全局替换为 Noto Sans CJK SC
   （game/script/01_fonts.rpy）。注意 map 的值必须是 `(font, bold, italic)`
   三元组，写纯字符串会在渲染期抛 `too many values to unpack`。
3. **打包分类**：不要手动排除 `game/**/*.rpyc`，剧本进不了包就是
   `LabelNotFound: 'start'`。遵循默认分类，只写排除规则。
4. **PWA 缓存**：web 版带 service worker（cache 名 `whalegal`），更新后
   看不到新版本时先注销 SW 清 CacheStorage 再刷新。
5. **渐进下载**：`progressive_download.txt` 的 voice 规则对应我们的
   `game/audio/voice/` 目录约定。

## TTS 配音（规划中）

流程：`story/voice_map.json` → `tts/synthesize.py` 批量合成 →
落盘 `game/audio/voice/<行ID>.ogg` → 剧本 `voice` 语句按行ID引用。
模型候选：VOICEVOX（免费、HTTP API、沙雕感强）或 Style-Bert-VITS2
（本地部署、可调情感）。ogg 在 Safari 不走 webaudio，如需兼容
配置 `config.webaudio_required_types = ["audio/mpeg"]` 并改用 mp3。

## 活动抽奖程序

抽奖程序位于 [`lottery/`](lottery/README.md)，与游戏源码放在同一个仓库。下载仓库并解压后，双击 `lottery/index.html` 即可使用，无需安装 Ren’Py。
