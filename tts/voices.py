# ============================================================
# whalegal 音线映射 —— TTS 合成的角色→音线配置（单一事实来源）
#
# 与 game/script/00_definitions.rpy 的 voice_tag 对齐：
#   主角 ds/cl/gp/u；次要角色 extra_f/extra_m；mystery 剧情＝ds 本体。
#   narrator 不配音（导入工具不为其生成 play_voice 钩子）。
#
# 引擎 = Style-Bert-VITS2（SBV2），服务:
#   conda run -n sbv2 python tts/engine/sbv2/server_fastapi.py   # 端口 5000
# 模型（jvnv 日语语料，许可见 tts/engine/sbv2/LGPL_LICENSE 与模型卡）:
#   jvnv-F1-jp / F2（女声）M1 / M2（男声），7 风格:
#   0:Neutral 1:Angry 2:Disgust 3:Fear 4:Happy 5:Sad 6:Surprise
#   （Neutral 会随文本内容自适应情感）
# ============================================================

BASE_URL = "http://127.0.0.1:5000"

VOICES = {
    ## 元气笨蛋 → F1 + Happy
    "deepseek": {"engine": "sbv2", "lang": "jp",
                 "params": {"model_name": "jvnv-F1-jp", "style": "Happy",
                            "style_weight": 1.1, "url": BASE_URL}},
    ## 傲娇大小姐 → F2 + Neutral（F2 音色偏成熟冷感，情感随文本自适应）
    "claude":   {"engine": "sbv2", "lang": "jp",
                 "params": {"model_name": "jvnv-F2-jp", "style": "Neutral",
                            "style_weight": 1.0, "url": BASE_URL}},
    ## 温柔学姐 → F1 + Neutral 低权重（更平缓柔顺）
    "gpt":      {"engine": "sbv2", "lang": "jp",
                 "params": {"model_name": "jvnv-F1-jp", "style": "Neutral",
                            "style_weight": 0.9, "url": BASE_URL}},
    ## 男主 → M1
    "user":     {"engine": "sbv2", "lang": "jp",
                 "params": {"model_name": "jvnv-M1-jp", "style": "Neutral",
                            "style_weight": 1.0, "url": BASE_URL}},
    ## 次要角色：女性（母亲/图书管理员）→ F2，男性（老师/同学）→ M2
    "extra_f":  {"engine": "sbv2", "lang": "jp",
                 "params": {"model_name": "jvnv-F2-jp", "style": "Neutral",
                            "style_weight": 1.0, "url": BASE_URL}},
    "extra_m":  {"engine": "sbv2", "lang": "jp",
                 "params": {"model_name": "jvnv-M2-jp", "style": "Neutral",
                            "style_weight": 1.0, "url": BASE_URL}},
}

## 剧本 who（story_gen 里的 say 变量名）→ 音线 key
WHO_TO_VOICE = {
    "ds": "deepseek",
    "cl": "claude",
    "gp": "gpt",
    "u": "user",
    "mystery": "deepseek",   # 剧情：？？？即 DeepSeek 本体
    "mother": "extra_f",
    "librarian": "extra_f",
    "teacher": "extra_m",
    "classmate": "extra_m",
}

## 个别台词强制换音线（v_id → 音线 key），一般不用
OVERRIDES = {}
