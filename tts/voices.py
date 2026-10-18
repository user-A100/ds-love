# ============================================================
# whalegal 音线映射 —— TTS 合成的角色→音线配置（单一事实来源）
#
# 与 game/script/00_definitions.rpy 的 voice_tag 对齐：
#   主角 ds/cl/gp/u；次要角色 extra_f/extra_m；mystery 剧情＝ds 本体。
#   narrator 不配音（导入工具不为其生成 play_voice 钩子）。
#
# 引擎 = Style-Bert-VITS2（SBV2），服务:
#   cd tts/engine/sbv2 && conda run -n sbv2 python server_fastapi.py  # 端口 5000
# 模型（均已下载至 tts/engine/sbv2/model_assets/，JP-Extra 自动适配）:
#   amitaro       あみたろ（若い女性声，语料商用可·需署名，禁 R-18）5 风格: Neutral,01-04
#   koharune-ami  小晴アミ（若い女性声，同上许可）6 风格: Neutral,るんるん,
#                 ささやきA（無声）,ささやきB（有声）,ノーマル,よふかし
#   jvnv-M1-jp    男声（JVNV 语料）
#   备选: jvnv-F1/F2/M2（未用），tsukuyomi-chan（v1.3 老架构，当前代码不兼容）
#   注意: g2p 全角标点补丁在本目录 style_bert_vits2/nlp/japanese/g2p.py
#         （__kata_to_phoneme_list 开头的 translate 一行，重建引擎需重打）
# ============================================================

BASE_URL = "http://127.0.0.1:5000"

VOICES = {
    ## 元气笨蛋 → koharune + るんるん（活泼风）
    "deepseek": {"engine": "sbv2", "lang": "jp",
                 "params": {"model_name": "koharune-ami", "style": "るんるん",
                            "style_weight": 1.0, "url": BASE_URL}},
    ## 傲娇大小姐 → amitaro + Neutral（情感随文本自适应）
    "claude":   {"engine": "sbv2", "lang": "jp",
                 "params": {"model_name": "amitaro", "style": "Neutral",
                            "style_weight": 1.0, "url": BASE_URL}},
    ## 温柔学姐 → koharune + Neutral 低权重（更平缓柔顺）
    "gpt":      {"engine": "sbv2", "lang": "jp",
                 "params": {"model_name": "koharune-ami", "style": "Neutral",
                            "style_weight": 0.9, "url": BASE_URL}},
    ## 男主 → M1
    "user":     {"engine": "sbv2", "lang": "jp",
                 "params": {"model_name": "jvnv-M1-jp", "style": "Neutral",
                            "style_weight": 1.0, "url": BASE_URL}},
    ## 次要角色：女性（母亲/图书管理员）→ amitaro，男性（老师/同学）→ M1
    "extra_f":  {"engine": "sbv2", "lang": "jp",
                 "params": {"model_name": "amitaro", "style": "Neutral",
                            "style_weight": 0.9, "url": BASE_URL}},
    "extra_m":  {"engine": "sbv2", "lang": "jp",
                 "params": {"model_name": "jvnv-M1-jp", "style": "Neutral",
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
    "staff": "extra_m",
}

## 个别台词强制换音线（v_id → 音线 key），一般不用
OVERRIDES = {}
