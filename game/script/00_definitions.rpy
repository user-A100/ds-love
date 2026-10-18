## ============================================================
## 角色与全局定义
## ============================================================

## 沙雕gal 主角团（占位定义，正式人设待文案导入后细化）

define s = Character(
    "白鲸",
    color="#4aa3ff",
    voice_tag="whale",
)

define k = Character(
    "小鲸",
    color="#ff8ab5",
    voice_tag="ko_whale",
)

define narrator = Character(
    what_italic=True,
)

## ------------------------------------------------------------
## 全局常量
## ------------------------------------------------------------

define WHALEGAL_VERSION = "0.1.0"

## voice 音频目录约定：
## game/audio/voice/<章节>_<行号>.ogg
## 由 tts/synthesize.py 依据 story/voice_map.json 批量生成
define VOICE_DIR = "audio/voice/"
