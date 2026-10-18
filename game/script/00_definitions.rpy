## ============================================================
## L1 人物层 —— 《未抵达的心意》角色定义
## 来源: story/chapters/未抵达的心意.md「核心设定」
## voice_tag 与 tts/voices.py 的音线映射对齐（TTS 接入用）
## ============================================================

## ------------------------------------------------------------
## 三位女主角
## ------------------------------------------------------------

## 第一女主：DeepSeek 娘 —— 活泼可爱、天然呆、热情真诚（蓝发）
define ds = Character(
    "DeepSeek",
    color="#4a9eff",
    voice_tag="deepseek",
)

## 傲娇富家大小姐：Claude 娘 —— 嘴硬心软、自尊心强、擅长钢琴
define cl = Character(
    "Claude",
    color="#b07aff",
    voice_tag="claude",
)

## 知性温柔的学姐：GPT 娘 —— 成绩优秀、擅长文学创作、善于倾听
define gp = Character(
    "GPT",
    color="#3ec8a8",
    voice_tag="gpt",
)

## ------------------------------------------------------------
## 主角与叙述者
## ------------------------------------------------------------

## 玩家（第一人称，一般不显示名字，特殊场合用）
define u = Character(
    "User",
    color="#eeeeee",
    voice_tag="user",
)

## 旁白
define narrator = Character(
    what_italic=True,
)

## ------------------------------------------------------------
## 次要角色（台词量少，TTS 可复用主线音线）
## ------------------------------------------------------------

define mystery = Character("？？？", color="#aaaaaa")       # 未揭露身份者
define mother = Character("母亲", color="#cc9966")          # User 母亲 / Claude 母亲共用音线
define teacher = Character("老师", color="#888866")         # 班主任 / 任课老师
define classmate = Character("同学", color="#888888")       # 路人同学
define librarian = Character("图书管理员", color="#888866")

## ------------------------------------------------------------
## 全局配置
## ------------------------------------------------------------

## TTS 自动配音钩子：
## 每句台词按语句 ID 自动找 game/audio/voice/<id>.ogg，
## 文件不存在则静默跳过。tts/synthesize.py 按同一 ID 命名产出。
define config.auto_voice = "audio/voice/{id}.ogg"

define GAME_TITLE = _("未抵达的心意")
