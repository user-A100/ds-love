# 全角色日文配音接入

已同步 GitHub `unsigned123/whalegal` 提交 `93c4141`。全部 1565 条唯一台词音频已按行ID接入现有日文剧本，无缺失。

| 角色 | 已接入音频 |
| --- | ---: |
| DeepSeek（含 mystery） | 500 |
| Claude | 370 |
| GPT | 222 |
| User | 443 |
| 次要女性角色 | 16 |
| 次要男性角色 | 14 |

音频位于 `game/tl/japanese/audio/voice/`，日文剧本通过原生 `voice voice_file("行ID")` 播放。游戏默认日语，旧存档按其语言偏好运行，可在设置切换日语。无需重复插入语音语句。

Claude 使用 `morioki` / `ノーマル`；DeepSeek 使用 `koharune-ami` / `るんるん`；GPT 使用 `amitaro` / `Neutral`，音高比例 0.93。

[完整台词映射](voice-manifest.json) 包含台词、角色、脚本行和音频路径。1565 条行ID校验及全部 Ogg 文件的 FFmpeg 解码检查通过；未逐条人工听音。

Web 包由 `tools/build_web.sh` 重建。日文音频按渐进下载规则随产物提供，后续发布使用 `tools/publish_web.sh` 推送 `web-dist`。

本次 Web 构建已通过 Lint，产物中 1565 条音频均与源文件 SHA-256 一致，`game.zip` 小于 24 MiB。构建产物位于 `server/public/`，本次尚未推送 `web-dist`。
