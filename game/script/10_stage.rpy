## ============================================================
## L2 舞台层 —— 转场 / 立绘动画 / 场景资产映射
## ============================================================

## ------------------------------------------------------------
## 统一转场（剧本导入工具与手写剧本共用）
## ------------------------------------------------------------

define trans_fade      = Fade(0.5, 0.3, 0.5)          # 黑场过渡（章节/大场景切换）
define trans_dissolve  = Dissolve(0.4)                # 通用叠化（背景/立绘切换）
define trans_flash     = Fade(0.1, 0.0, 0.4, color="#ffffff")  # 闪白（回忆/冲击）
define trans_punch     = hpunch                       # 震屏（撞击/惊吓）

## ------------------------------------------------------------
## 立绘动画
## ------------------------------------------------------------

## 立绘待机：呼吸感上下浮动（show xxx at sprite_idle）
transform sprite_idle:
    yoffset 0
    block:
        ease 2.2 yoffset -8
        ease 2.2 yoffset 0
        repeat

## 立绘入场（左/右）：淡入 + 滑入
transform sprite_enter_left:
    xoffset -40
    alpha 0.0
    easein 0.4 xoffset 0 alpha 1.0

transform sprite_enter_right:
    xoffset 40
    alpha 0.0
    easein 0.4 xoffset 0 alpha 1.0

## ------------------------------------------------------------
## 占位立绘（正式立绘就绪前的剪影）
## 导入工具/美术就绪后用真实 LayeredImage 替换同名定义即可
## ------------------------------------------------------------

init python:

    for _who in ["ds", "cl", "gp"]:
        for _expr in ["normal", "happy", "sad", "angry", "shy"]:
            renpy.image("{} {}".format(_who, _expr), Placeholder("girl"))

## ------------------------------------------------------------
## 场景资产映射表
## 剧本中的「CG-XXX｜描述」→ 背景图文件
## 导入工具按此表生成 scene 语句；图片未就绪时回退黑场
## ------------------------------------------------------------

init python:

    SCENE_BG = {
        "CG-001": "images/bg/cg001_rooftop.png",       # 教学楼天台 · 春日午后
        "CG-002": "images/bg/cg002_flowerbed.png",     # 教学楼前的花坛
        "CG-003": "images/bg/cg003_desk.png",          # 课桌旁
        "CG-004": "images/bg/cg004_aquarium.png",      # 水族馆
        "CG-005": "images/bg/cg005_railcross.png",     # 铁路道口
    }

    def scene_bg(scene_id):
        """按场景卡 ID 切换背景；资产缺失时回退黑场（骨架期安全网）"""
        renpy.hide_screen_all() if False else None
        renpy.scene()
        path = SCENE_BG.get(scene_id)
        if path and renpy.loadable(path):
            renpy.show(path)
        else:
            renpy.show("black")
