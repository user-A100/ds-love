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
define mother = Character(_("母亲"), color="#cc9966")          # User 母亲 / Claude 母亲共用音线
define teacher = Character(_("老师"), color="#888866")         # 班主任 / 任课老师
define classmate = Character(_("同学"), color="#888888")       # 路人同学
define librarian = Character(_("图书管理员"), color="#888866")

define staff = Character(_("工作人员"), color="#888888")

## ------------------------------------------------------------
## 全局配置
## ------------------------------------------------------------

## TTS 配音不在此配置——由 10_stage.rpy 的 play_voice() 钩子实现，
## ID 算法与 tts/synthesize.py 对齐（内容寻址，文案改动不漂移）。

define GAME_TITLE = _("未抵达的心意")
