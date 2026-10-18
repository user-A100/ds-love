## ============================================================
## L2 舞台层 —— 转场 / 立绘动画 / 配音钩子 / 场景切换
## 注意: SCENE_BG 字典与立绘 image 定义由 story_gen/assets.rpy
## 生成（源: story/scenes.json + story/sprites.json），此处不维护
## ============================================================

## ------------------------------------------------------------
## 统一转场（剧本导入工具与手写剧本共用）
## ------------------------------------------------------------

define trans_fade      = Fade(0.5, 0.3, 0.5)          # 黑场过渡（章节/大场景切换）
define trans_dissolve  = Dissolve(0.4)                # 通用叠化（背景/立绘切换）
define trans_flash     = Fade(0.1, 0.0, 0.4, color="#ffffff")  # 闪白（回忆/冲击）
define trans_punch     = hpunch                       # 震屏（撞击/惊吓）

## ------------------------------------------------------------
## 立绘站位（含呼吸待机动画）
## 生成剧本使用: show ds normal at sprite_pos_left
## ------------------------------------------------------------

transform sprite_pos_left:
    xalign 0.15 yalign 1.0
    block:
        ease 2.2 yoffset -8
        ease 2.2 yoffset 0
        repeat

transform sprite_pos_center:
    xalign 0.5 yalign 1.0
    block:
        ease 2.2 yoffset -8
        ease 2.2 yoffset 0
        repeat

transform sprite_pos_right:
    xalign 0.85 yalign 1.0
    block:
        ease 2.2 yoffset -8
        ease 2.2 yoffset 0
        repeat

## 手动演出用的独立呼吸动画
transform sprite_idle:
    block:
        ease 2.2 yoffset -8
        ease 2.2 yoffset 0
        repeat

## ------------------------------------------------------------
## 配音钩子（TTS 产物按内容寻址 ID 命名，未合成的台词静默跳过）
## tts/synthesize.py 用同一 ID 算法: md5(角色 + \x00 + 台词)[:12]
## ------------------------------------------------------------

init python:

    def voice_file(vid):
        """Native voice statement: missing files stay silent, never use another dub."""
        prefix = "tl/japanese/" if _preferences.language == "japanese" else "<silence 0.01>"
        path = prefix + "audio/voice/{}.ogg".format(vid)
        return path if renpy.loadable(path) else "<silence 0.01>"

    def play_voice(vid):
        # Compatibility for hand-authored scripts using the original hook.
        path = voice_file(vid)
        if path != "<silence 0.01>":
            renpy.music.play(path, channel="voice")
        else:
            renpy.music.stop(channel="voice")

    def scene_bg(scene_key):
        """按场景 key 切换背景；资产未就绪时回退黑场"""
        renpy.scene()
        name = SCENE_BG.get(scene_key)
        if name and renpy.has_image(name):
            renpy.show(name)
        else:
            renpy.show("black")
