# 《未抵达的心意》体验版 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

执行环境说明：这行来自 writing-plans 模板。当前环境实际提供的是 `executing-plans`；默认在当前会话逐项执行，不以模板文字自动发起子代理或另建聊天。

**Goal:** 在现有 whalegal 工程中完成《未抵达的心意》序章＋第一章的桌面与 Web 可玩体验版。

**Architecture:** 使用现有 Ren'Py 工程、同版本标准 GUI 和原生剧情语句。每场独立 label，主入口顺序 call；原稿、清稿、运行剧本和素材清单职责分开。先验证完整文字流程，再用确定的资产替换场景表示。

**Tech Stack:** Ren'Py 8.5.3 SDK、Ren'Py Script、SDK 内嵌 Python、PowerShell、既有 Bash/rsync/nginx 发布链路。

**Spec:** `docs/story-analysis.md`；原始剧本 `D:/ds-gal/未抵达的心意.md`，SHA-256 见该分析文档。

## Global Constraints

- 首个里程碑仅为序章＋第一章，不实现其余三条无正文路线。
- 中文对白、固定主角名 User；日语 TTS 仅制定接口，不在本里程碑批量生成。
- Ren'Py SDK 保持 `renpy-8.5.3-sdk/` 目录约定；不自动升级。
- 保留现有字体替换、渐进下载、Linux 构建和 nginx 部署能力。
- `start` 全项目唯一；不保留旧测试剧情的第二个入口。
- 不增加外部前端框架、业务服务、数据库、剧情解释器或好感度系统。
- 正式素材使用 1280×720 逻辑画布；角色位置、对话框和菜单在移动端横屏验收。
- 当前 `config.save_directory` 保持 `whalegal-1682947365`，不要随展示名修改。
- 文案编辑、图片生成、配音与对外部署分别执行；本计划没有自动发布或批量生成媒体的步骤。

## File Structure

| 文件 | 操作 | 责任 |
| --- | --- | --- |
| `story/source/未抵达的心意-v1.md` | 创建 | 原稿不变归档 |
| `story/chapters/00_prologue.md`、`01_mistaken_person.md` | 创建 | 首四场清稿 |
| `story/editorial-log.md` | 创建 | 编辑决定，含后期矛盾清单 |
| `story/scene-map.csv` | 创建 | 原稿行号、清稿与 label 对照 |
| `story/asset-manifest.csv` | 创建 | 当前实际素材及使用状态 |
| `game/gui.rpy`、`game/screens.rpy`、`game/gui/` | 创建 | 同版本 SDK 标准 GUI |
| `game/options.rpy` | 修改 | 展示名、关于说明和体验版版本 |
| `game/script/00_definitions.rpy` | 修改 | 新角色定义与自动配音路径 |
| `game/script/01_fonts.rpy` | 保留 | 字体替换 |
| `game/script/02_flow.rpy` | 创建 | 唯一 start、四场顺序、体验版结束 |
| `game/script/03_assets.rpy` | 创建 | 背景、角色和位置名称 |
| `game/script/prologue.rpy` | 创建 | 序章独立场景 |
| `game/script/chapter01.rpy` | 替换 | 正式第一章三场 |
| `tools/build_web.ps1` | 创建 | Windows 构建与同步 |
| `docs/qa/demo-checklist.md` | 创建 | 运行环境、结果、失败记录 |
| `README.md`、`.gitignore` | 修改 | 新入口、环境依赖、归档规则 |

---

### Task 1: 归档剧本并固定首四场

**Files:** 创建 `story/source/未抵达的心意-v1.md`、`story/chapters/00_prologue.md`、`story/chapters/01_mistaken_person.md`、`story/editorial-log.md`、`story/scene-map.csv`。

**Interfaces:** 消费原稿；产出四个清稿场景 `prologue_s01`、`chapter01_s01`、`chapter01_s02`、`chapter01_s03`。清稿字段为“原稿行号、地点/时间、说话人、对白/旁白、演出备注”；不以参考图片 URL 当作实际素材。

- [ ] 在仓库根执行原样复制并核对哈希：

```powershell
New-Item -ItemType Directory -Force story/source, story/chapters | Out-Null
Copy-Item -LiteralPath 'D:/ds-gal/未抵达的心意.md' -Destination 'story/source/未抵达的心意-v1.md'
Get-FileHash -Algorithm SHA256 -LiteralPath 'story/source/未抵达的心意-v1.md'
```

期望哈希为 `94ef1c94d6157e6fda6f8ad1b2b5456fcd9977cdb8b98a7d17f22501775643d3`，不覆盖已有归档的不同内容。

- [ ] 以原稿 28–143 行生成序章清稿；144–277、278–347、348–435 行生成第一章三个场景。剔除外链图片、网页来源和版本标题，保留全部唯一对白、旁白、碰撞和铃声。
- [ ] `scene-map.csv` 使用以下完整首批映射；行号针对固定哈希原稿：

```csv
scene_id,source_start,source_end,clean_file,renpy_label
prologue_s01,28,143,story/chapters/00_prologue.md,prologue_s01
chapter01_s01,144,277,story/chapters/01_mistaken_person.md,chapter01_s01
chapter01_s02,278,347,story/chapters/01_mistaken_person.md,chapter01_s02
chapter01_s03,348,435,story/chapters/01_mistaken_person.md,chapter01_s03
```

- [ ] 编辑日志写明本批没有新增选项、没有改写误认与告白事件；将分析文档第 4 节逐项纳入后续共同线清稿问题。
- [ ] 人工对照四场，确认“遗失 → 归还 → 阅读故事 → 合作约定 → 电影社建议”连续且无漏段，然后提交本任务文件：`git commit -m "docs: archive story and prepare demo script"`。

### Task 2: 用目标 SDK 验证原工程并合入标准 GUI

**Files:** 创建 `game/gui.rpy`、`game/screens.rpy`、`game/gui/` 和 `docs/qa/demo-checklist.md`；修改 `game/options.rpy`、`README.md`、`.gitignore`。

**Interfaces:** 输入现有工程和 Ren'Py 8.5.3 Windows SDK（需含 Web 支持包）；输出可运行的标准标题、存读档、设置、历史和快速菜单，保持字体映射可用。

- [ ] 将目标 SDK 安装在仓库根的 `renpy-8.5.3-sdk/`；确认 `renpy.exe`、SDK Windows Python 和 `web/` 存在。在改游戏前运行旧测试剧情，记录 SDK 版本、启动情况和错误。
- [ ] 用 SDK Launcher 在仓库之外的临时目录创建一个 1280×720 标准 GUI 项目；只将生成的 `gui.rpy`、`screens.rpy` 和 `gui/` 资产合入当前 `game/`。不复制临时项目的 options、script 或字体定义。
- [ ] 对现有 options 定点修改，保留构建排除规则及存档目录：

```renpy
define config.name = _("未抵达的心意")
define build.name = "whalegal"
define build.version = "0.2.0-demo"
define config.version = "0.2.0-demo"
define gui.about = _p("《未抵达的心意》体验版：序章与第一章。")
```

- [ ] 在生成的 GUI 中将文本、姓名和界面字体配置统一改为已有字体：

```renpy
define gui.text_font = "fonts/NotoSansCJKsc-Regular.otf"
define gui.name_text_font = "fonts/NotoSansCJKsc-Regular.otf"
define gui.interface_text_font = "fonts/NotoSansCJKsc-Regular.otf"
```

复用生成模板的其余默认值，首批只调整字体、蓝/橙强调色和标题背景。不要在未生成模板前引用不存在的 GUI 组件。

- [ ] 从 Windows SDK 执行以下命令，确认 lint 和运行都成功。先检查该 SDK 的实际路径；路径不匹配时按 SDK 目录说明定位，不猜测版本能力：

```powershell
$sdkRoot = Join-Path $PWD 'renpy-8.5.3-sdk'
$sdkPython = Join-Path $sdkRoot 'lib/py3-windows-x86_64/python.exe'
& $sdkPython (Join-Path $sdkRoot 'renpy.py') $PWD.Path lint --error-code
& $sdkPython (Join-Path $sdkRoot 'renpy.py') $PWD.Path run
```

- [ ] 检查标题中文、设置、存读档和历史页面，记录结果；README 写明 Windows 与 Linux 的独立运行方式。将实际下载的 SDK 压缩包、缓存加入忽略项，保留现有跟踪的 `.rpyc` 规则不做无关清理，然后提交：`git commit -m "feat: add standard game UI and demo identity"`。

### Task 3: 建立角色、稳定对白 ID 和四场完整文字流程

**Files:** 修改 `game/script/00_definitions.rpy`；创建 `02_flow.rpy`、`03_assets.rpy`、`prologue.rpy`；替换 `chapter01.rpy`。

**Interfaces:** 使用任务 1 的四场清稿。角色标识为 `u`、`d`、`c`、`g`、`unknown_d`、`classmate`、`librarian`，场景标签精确沿用 `scene-map.csv`。

- [ ] 定义角色并移除已不使用的白鲸、小鲸；旁白使用普通中文阅读样式，不再全局斜体：

```renpy
define u = Character("User", color="#d7e3f0")
define d = Character("DeepSeek", color="#4aa3ff", voice_tag="deepseek")
define c = Character("Claude", color="#e6a36a", voice_tag="claude")
define g = Character("GPT", color="#7eae93", voice_tag="gpt")
define unknown_d = Character("？？？", color="#4aa3ff", voice_tag="deepseek")
define classmate = Character("同学")
define librarian = Character("图书管理员")
define narrator = Character(None)
define config.auto_voice = "audio/voice/{id}.ogg"
```

本阶段没有音频文件，自动配音配置不会阻塞文字流程。完整共同线所需母亲、老师等角色在首次使用时增加。

- [ ] `03_assets.rpy` 先声明三个原生背景，保证无需媒体文件也能验证流程：

```renpy
image bg rooftop_spring = Solid("#b7d3e3")
image bg school_ground_evening = Solid("#c9b4a5")
image bg library_afternoon = Solid("#c4c5b5")
```

- [ ] 建立唯一入口；先准备好四场再替换旧入口，避免将半成品当作已交付：

```renpy
label start:
    call prologue_s01
    call chapter01_s01
    call chapter01_s02
    call chapter01_s03
    scene black
    with fade
    centered "《未抵达的心意》体验版结束\n感谢游玩。"
    return
```

- [ ] 按清稿逐场移植全部正文；每个标签自设背景、清除上一场角色并以 `return` 结束。每句加显式唯一 ID，已有 ID 永不因插句重排。序章开头采用原文：

```renpy
label prologue_s01:
    scene bg rooftop_spring
    with fade
    centered "教学楼天台 · 春日午后"
    narrator "那天，我原本只是想找个安静的地方。" id prologue_s01_0001
    narrator "教学楼天台平时很少有人来。尤其是在午休结束前的十几分钟，整个校园都显得格外安静。" id prologue_s01_0002
```

这个代码块只规定开头与格式；本步骤的完成条件是移植原稿 28–143 行的全部有效正文，并以 `return` 结束。第一章的三个标签分别覆盖映射表的原稿范围，不能只放上述示例或剧情摘要。长旁白按语义拆成多条 say，每条独立 ID；原稿引用图片和标题不作为台词播放。

- [ ] 将第一场蓝发少女的对白全部映射 `unknown_d`，后续归还笔记本场改为 `d`；主角独白映射 `narrator`，主角出声映射 `u`。操场之后 DeepSeek 丢笔记本的镜头保留为明确视角切换。
- [ ] 执行任务 2 的 lint；`rg -n '^label start:' game` 应只出现一处。人工核对四场头尾及“同学误认、单杠告白、Claude 答应、笔记本归还、拍电影约定、去电影社”六个事件全部存在。通读直到体验版结束再提交：`git commit -m "feat: add prologue and first chapter"`。

### Task 4: 用体验版素材完成最小演出

**Files:** 修改 `game/script/03_assets.rpy`、`prologue.rpy`、`chapter01.rpy`；创建实际使用的 `game/images/`、`game/audio/bgm/`、`game/audio/sfx/` 文件和 `story/asset-manifest.csv`。

**Interfaces:** 背景名称保持 `bg rooftop_spring`、`bg school_ground_evening`、`bg library_afternoon`；DeepSeek 属性 `normal/smile/panic/sad`，Claude 属性 `normal/angry/blush`。资源准备完成时直接替换同名定义，不改对白 ID。

- [ ] 以分析文档第 6 节的体验版最小素材包选择或制作小样，再固定两名角色与三个背景；若素材尚未定稿，保留任务 3 的可玩文字版，演出阶段标记为未验收。
- [ ] 素材台账字段固定为 `asset_id,type,file,source,permission,status`；每项使用实际路径和实际来源，禁止以原稿参考图 URL 填充成已完成资产。
- [ ] 背景文件准备后将三项定义替换为实际图片，立绘按固定名称声明。位置变换采用原生坐标：

```renpy
transform actor_left:
    xalign 0.25
    yalign 1.0

transform actor_right:
    xalign 0.75
    yalign 1.0
```

- [ ] 逐场安排背景、出入场、表情、碰撞和铃声。先用 dissolve、fade、短停顿即可；每一场结束和下一场开始都核对音乐、角色是否残留。第一场以未知姓名演出，不能提前显示 DeepSeek 姓名。
- [ ] 在实际窗口和移动端横屏检查姓名框、两角色构图、长段文字、自动播放和跳过。确认没有缺失文件错误，再提交所有实际使用资产和引用修改：`git commit -m "feat: stage demo scenes with initial assets"`。

### Task 5: 打通 Windows Web 构建并保留 Linux 发布链路

**Files:** 创建 `tools/build_web.ps1`；修改 `README.md`；按实测需要修改现有渐进下载配置。`tools/build_web.sh`、`server/serve.py`、nginx 模板继续沿用。

**Interfaces:** `./tools/build_web.ps1` 构建至 `server/public/`；`./tools/build_web.ps1 -Serve` 构建后使用既有 `server/serve.py` 在 127.0.0.1:8000 预览。

- [ ] PowerShell 脚本从 `$PSScriptRoot` 求仓库绝对路径，检查目标 SDK、SDK Python 与 Web 支持包；缺失时给出具体路径并非零退出。
- [ ] 顺序执行 lint、在 SDK 目录执行 launcher web_build 到独立临时目录、校验临时目录包含 `index.html` 与引擎/数据文件，全部成功后才同步输出。每次外部程序调用后显式检查 `$LASTEXITCODE`，不能只依赖 `$ErrorActionPreference`。
- [ ] 构建命令采用 SDK CLI；先独立验证该版本命令确实可用，再写入封装：

```powershell
$projectRoot = (Resolve-Path '.').Path
$sdkRoot = Join-Path $projectRoot 'renpy-8.5.3-sdk'
$sdkPython = Join-Path $sdkRoot 'lib/py3-windows-x86_64/python.exe'
$buildOutput = Join-Path ([System.IO.Path]::GetTempPath()) ('whalegal-web-' + [guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $buildOutput | Out-Null
Push-Location $sdkRoot
try {
    & $sdkPython (Join-Path $sdkRoot 'renpy.py') launcher web_build $projectRoot --destination $buildOutput
    if ($LASTEXITCODE -ne 0) { throw 'RenPy Web build failed' }
} finally {
    Pop-Location
}
```

- [ ] 同步前验证目标绝对路径严格为仓库的 `server/public/`，临时目录严格为当前构建创建的 GUID 目录。删除旧产物或清理临时目录时使用同一 PowerShell 的 `Remove-Item -LiteralPath`，不得拼接 cmd 删除命令。校验成功前不覆盖上一份可用产物。
- [ ] `-Serve` 使用可运行的本机 Python 启动已有服务器，参数为 `--host 127.0.0.1 --port 8000 --root` 加 `server/public/` 绝对路径。README 写清 Bash 路径需要 Linux/WSL、rsync 和对应 SDK，PowerShell 路径需要 Windows SDK；不假定两边二进制可互换。
- [ ] 完成一次 Windows 构建和本地浏览器启动，确认不会误触发公网部署；提交脚本和说明：`git commit -m "build: add Windows Web build workflow"`。

### Task 6: 体验版验收与交付

**Files:** 完善 `docs/qa/demo-checklist.md` 和 `README.md`，修复本阶段暴露的具体问题。

**Interfaces:** 输入文字/演出体验版与实际 Web 包；输出可复现验收记录。未能执行的设备或浏览器明确记为未执行，不以 lint 通过代替运行通过。

- [ ] 记录 SDK、操作系统、浏览器版本、构建提交与结果。完成桌面四场全流程，确保结束回到标题，重新开始不带入上次显示的角色/音乐。
- [ ] 在序章、操场、图书馆分别保存并读回；检查对白位置、人物名、画面和音乐；跨场回滚不跳到错误剧情。关闭并重开游戏后验证存档仍可用。
- [ ] Web 至少在当前可用 Chrome/Edge 浏览器完成相同流程，刷新后读档；其余目标浏览器和移动端列为独立实机项。首屏不乱码，按钮可触达，点击交互后背景音乐和音效正常。
- [ ] 在开发者工具记录冷启动传输量和耗时，并模拟慢网核对渐进背景；对 `.wasm` 验证 `application/wasm`；对可 Range 的资源验证 206 和正确 Content-Range。更新构建后核对新文案是否出现，记录 SW/缓存现象。
- [ ] README 标明体验版范围、实际素材/配音状态和启动方式；如 Task 4 未完成则交付名称必须是“文字流程体验版”，不得宣称演出体验版完成。
- [ ] 确认归档/文档/运行源码一致，SDK 和 `server/public/` 未进入暂存区，提交验收与修复：`git commit -m "docs: record demo acceptance results"`。交付时提醒将完成内容推送 GitHub。

## 后续计划边界

本计划完成后按 `docs/story-analysis.md` 的 M2–M6 分别形成小计划：完整文本与最终选择、全线素材/回想、TTS 工具与配音、发布、多路线续写。它们分别依赖清稿、视觉小样、音线试听或独立结局正文；现在不将未决内容伪装成可直接执行的实现。
