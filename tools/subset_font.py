#!/usr/bin/env python3
## ============================================================
## subset_font.py —— 字体子集化（game.zip 瘦身主力）
##
## Noto Sans CJK 全量 15.7MB，游戏实际用字有限。
## 从 剧本(md) + 日文台本 + 游戏脚本(rpy) 收集用字，
## 加安全字符集（拉丁/假名/常用符号），生成 woff2 子集。
##
## 每次构建自动重跑：文案新增字符 → 子集自动扩充 → 无豆腐风险。
## （绕过构建直接 renpy.sh run 的开发者需先手动跑一次本脚本）
##
## 用法: python3 tools/subset_font.py
## 产物: game/fonts/game-regular.woff2（提交入库，供本地开发直接用）
## ============================================================
import glob
import os
import sys

from fontTools import subset
from fontTools.ttLib import TTFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "assets_src", "fonts", "NotoSansCJKsc-Regular.otf")
DST = os.path.join(ROOT, "game", "fonts", "game-regular.woff2")

## 安全字符集：ASCII + 常用中文标点 + 假名 + 注音/符号 + 全角形式
SAFETY = (
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    " .,;:!?()[]{}<>/\\|@#$%^&*-_=+'\"`~"
    "，。、；：！？「」『』【】（）《》〈〉…—～·ー"
    "“”‘’％＋－×÷＝≠±∞℃℉①②③④⑤⑥⑦⑧⑨⑩"
    "♪♫★☆◆◇○●□■△▲▽▼※↑↓←→"
    "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわゐゑをん"
    "がぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽゃゅょっゎゐゑ"
    "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン"
    "ガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポャュョッ"
    "ぁぃぅぇぉゔぇ"
)


def collect_text():
    texts = [SAFETY]
    patterns = [
        os.path.join(ROOT, "story", "chapters", "*.md"),
        os.path.join(ROOT, "story", "ja", "**", "*.md"),
        os.path.join(ROOT, "game", "**", "*.rpy"),
    ]
    for pat in patterns:
        for f in glob.glob(pat, recursive=True):
            with open(f, encoding="utf-8", errors="ignore") as fp:
                texts.append(fp.read())
    return "".join(texts)


def main():
    if not os.path.exists(SRC):
        sys.exit(f"错误: 找不到字体源 {SRC}")

    text = collect_text()
    unicodes = sorted({ord(c) for c in text if not c.isspace() or c == " "})
    print(f"收集用字: {len(unicodes)} 个码位")

    args = subset.Options()
    args.flavor = "woff2"
    args.layout_features = ["*"]          # 保留 OpenType 特性（vert 等）
    args.name_IDs = ["*"]
    args.notdef_outline = True
    args.recalc_bounds = True

    font = subset.load_font(SRC, args)

    ## 只请求源字体实际拥有的字形（emoji 等由 Ren'Py 的 Twemoji 兜底）
    src_cmap = set(font.getBestCmap().keys())
    unicodes = [u for u in unicodes if u in src_cmap]

    subsetter = subset.Subsetter(options=args)
    subsetter.populate(unicodes=unicodes)
    subsetter.subset(font)

    os.makedirs(os.path.dirname(DST), exist_ok=True)
    subset.save_font(font, DST, args)

    ## 覆盖校验：剧本文本中「源字体能显示」的字必须 100% 在子集里
    new_cmap = set(font.getBestCmap().keys())
    missing = [c for c in set(text)
               if ord(c) in src_cmap and ord(c) not in new_cmap
               and not c.isspace()]
    if missing:
        sys.exit(f"错误: 子集缺字 {len(missing)} 个: {''.join(missing[:20])}")

    print("字体子集: %.2f MB -> %s" % (
        os.path.getsize(DST) / 1048576, os.path.relpath(DST, ROOT)))


if __name__ == "__main__":
    main()
