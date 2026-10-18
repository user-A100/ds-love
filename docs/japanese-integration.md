# 日文版游戏接入

日文正文已接入现有 Ren'Py 8.5.3 项目：序章、第一至第六章共同路线、DeepSeek 真结局。新玩家默认使用日文，在设置 → Language 中可切换「日本語 / 简体中文」。原有存档中的语言偏好仍然生效。

章节选择、路线选项、结尾和角色称呼均有日文显示。User、DeepSeek、Claude、GPT 保留原名。Claude、GPT、Normal End 尚无完整原稿，选择后会明确提示本文未收录；不会替作者续写结局。

## 文案与生成链路

- 中文源：`story/chapters/未抵达的心意.md`。
- 日文源：`story/japanese.json` 明确列出的 11 份 Markdown；不自动扫描目录，避免重复导入另一份第四章前篇。
- 中文运行脚本：`game/script/story_gen/`。
- 日文运行脚本：`game/tl/japanese/story_gen/`，通过 Ren'Py 原生 `translate japanese` 和显式台词 ID 对应中文单元。
- 项目菜单翻译：`game/tl/japanese/project.rpy`。`common.rpy`、`screens.rpy` 来自官方 SDK 8.5.3 的 `the_question/game/tl/japanese/`；保留其版权头。

导入器按场景、背景切换及有序角色对话校验对应关系，允许译文自然拆分旁白段落；遇到角色或场景不一致立即报错。当前覆盖 3,950 个中文单元、3,948 个日文段落；多段书信在日文运行时逐段点击。剧本中的制作备注、场景说明不进入对话框。请编辑 Markdown 源后重新生成，勿手改生成脚本。

```bash
python tools/import_story.py
python tools/import_story.py --check
python -m unittest discover -s tests -v
python tts/synthesize.py --language zh --check-only
python tts/synthesize.py --language jp --check-only
```

原生引擎验证（将 SDK 放在仓库根目录）：

```bash
./renpy-8.5.3-sdk/renpy.sh . lint --error-code
./renpy-8.5.3-sdk/renpy.sh . test japanese
```

Windows 使用 SDK 内的 `lib/py3-windows-x86_64/python.exe renpy.py <项目绝对路径>` 执行相同命令。运行测试需要可用的图形渲染环境。

## 日语配音

`tts/synthesize.py --language jp` 读取日文运行台词，音频输出到 `game/tl/japanese/audio/voice/`，缓存使用 `tts/cache-jp.json`。中文仍使用 `game/audio/voice/`，两种语言独立生成、加载、清理。音频 ID 由规范角色名和对应语言台词计算。

本次接入没有合成真实日语配音。默认 dummy 引擎生成的是静音占位；需要先配置 `tts/voices.py` 中的真实引擎再批量合成。缺少当前语言音频时，运行时使用 Ren'Py 的短静音，不会播放其他语言配音。

接入采用 [Ren'Py 原生翻译机制](https://www.renpy.org/doc/html/translation.html) 和 [voice 语句](https://www.renpy.org/doc/html/voice.html)，语言切换与语音重播由引擎管理。
