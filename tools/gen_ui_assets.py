#!/usr/bin/env python3
## ============================================================
## gen_ui_assets.py —— 生成对话 UI 贴图（maid-atelier 风格）
## 配色借鉴 dsh-deep-whale (MIT) by Small-tailqwq:
##   https://github.com/Small-tailqwq/dsh-deep-whale
##   深海军蓝玻璃底 + 蕾丝金描边 + 大圆角
## 仅借鉴配色与造型（MIT 代码），不使用其美术素材（CC BY-NC-SA）
## 产物: game/gui/textbox.png  game/gui/namebox.png
## 用法: python3 tools/gen_ui_assets.py
## ============================================================
import os

from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GUI = os.path.join(ROOT, "game", "gui")

## ---- maid-atelier 色板 ----
NAVY_DEEP = (18, 31, 67)      # 深海军蓝（对话框底）
NAVY_MID = (30, 47, 90)       # 渐变亮端
GOLD = (197, 164, 104)        # 蕾丝金描边
GOLD_SOFT = (226, 207, 170)   # 金柔（名字）

TEXTBOX_W, TEXTBOX_H = 1280, 185
NAMEBOX_W, NAMEBOX_H = 300, 48


def lerp(c1, c2, t):
    return tuple(round(a + (b - a) * t) for a, b in zip(c1, c2))


def rounded_panel(w, h, radius, fill_top, fill_bottom, border, border_alpha=140):
    """垂直微渐变 + 圆角 + 金色描边的玻璃面板（含 1px 抗锯齿余量）"""
    scale = 2                      # 超采样抗锯齿
    W, H = w * scale, h * scale
    r = radius * scale
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    ## 逐行画渐变（限制在圆角矩形内：先画满，再用 mask 裁）
    panel = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    pd = ImageDraw.Draw(panel)
    for y in range(H):
        t = y / max(H - 1, 1)
        pd.line([(0, y), (W, y)], fill=lerp(fill_top, fill_bottom, t))
    mask = Image.new("L", (W, H), 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle([0, 0, W - 1, H - 1], radius=r, fill=255)
    img.paste(panel, (0, 0), mask)

    ## 金色描边
    d.rounded_rectangle(
        [0, 0, W - 1, H - 1], radius=r,
        outline=border + (border_alpha,), width=2 * scale)

    return img.resize((w, h), Image.LANCZOS)


def main():
    os.makedirs(GUI, exist_ok=True)

    ## ---- 对话框：顶角 18px 圆角，底边贴屏幕下缘 ----
    W, H = TEXTBOX_W * 2, TEXTBOX_H * 2
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    panel = rounded_panel(W, H, 18 * 2,
                          NAVY_MID + (232,),       # 顶部略亮
                          NAVY_DEEP + (242,),      # 底部更深更实
                          GOLD, border_alpha=130)
    ## 底部两角改直角：把圆角面板往下贴，底边对齐画布底
    img.paste(panel, (0, 0), panel)
    img = img.crop((0, 0, W, H - 20))   # 裁掉底部圆角区域 → 底边平直
    img = img.resize((TEXTBOX_W, TEXTBOX_H), Image.LANCZOS)
    img.save(os.path.join(GUI, "textbox.png"))
    print("textbox.png", img.size)

    ## ---- 名牌：胶囊形，深蓝底金边 ----
    nb = rounded_panel(NAMEBOX_W, NAMEBOX_H, NAMEBOX_H // 2,
                       (44, 62, 108, 235),
                       NAVY_DEEP + (242,),
                       GOLD, border_alpha=150)
    nb.save(os.path.join(GUI, "namebox.png"))
    print("namebox.png", nb.size)


if __name__ == "__main__":
    main()
