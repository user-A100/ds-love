# ============================================================
# whalegal 音线映射 —— TTS 合成的角色→音线配置（单一事实来源）
#
# 与 game/script/00_definitions.rpy 的 voice_tag 对齐：
#   主角 ds/cl/gp/u；次要角色共用 extra；mystery 剧情＝ds 本体。
#   narrator 不配音（导入工具不为其生成 play_voice 钩子）。
#
# 引擎可选值:
#   dummy    本地静音 wav，跑通流水线用，无需服务
#   voicevox VOICEVOX HTTP API（仅日语），params 见下例
#   sbv2     Style-Bert-VITS2 HTTP API（JP/EN/ZH），params 见下例
#
# 接真实引擎时的配置示例（改 engine/params 即可，脚本将翻译为日文后
# 切 voicevox 或 sbv2 的 JP 模型；当前中文稿可切 sbv2 的 ZH 模型）:
#
#   "deepseek": {
#       "engine": "sbv2",
#       "lang": "zh",
#       "params": {"url": "http://127.0.0.1:5000",
#                  "model_id": 0, "style": "Genki", "style_weight": 1.2},
#   },
#   "claude": {
#       "engine": "voicevox",
#       "lang": "jp",
#       "params": {"url": "http://127.0.0.1:50021", "style_id": 8},
#   },
# ============================================================

VOICES = {
    "deepseek": {"engine": "dummy", "lang": "zh", "params": {}},
    "claude":   {"engine": "dummy", "lang": "zh", "params": {}},
    "gpt":      {"engine": "dummy", "lang": "zh", "params": {}},
    "user":     {"engine": "dummy", "lang": "zh", "params": {}},
    "extra":    {"engine": "dummy", "lang": "zh", "params": {}},
}

## 剧本 who（story_gen 里的 say 变量名）→ 音线 key
WHO_TO_VOICE = {
    "ds": "deepseek",
    "cl": "claude",
    "gp": "gpt",
    "u": "user",
    "mystery": "deepseek",   # 剧情：？？？即 DeepSeek 本体
    "mother": "extra",
    "teacher": "extra",
    "classmate": "extra",
    "librarian": "extra",
}

## 个别台词强制换音线（v_id → 音线 key），一般不用
OVERRIDES = {}
