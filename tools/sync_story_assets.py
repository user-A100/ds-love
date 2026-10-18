#!/usr/bin/env python3
## ============================================================
## sync_story_assets.py —— 同步剧本引用的美术资产
##
## import_story.py 生成的 assets.rpy 会引用 game/images/story/ 下的
## 图片（映射来自 story/art_direction.json）。美术在 assets_src/ 就绪
## 后，本脚本按「文件名匹配」把缺失文件拷入正确位置。
##
## 找不到源文件的引用保持缺失（Ren'Py 黑场/剪影兜底），仅报告。
## 用法: python3 tools/sync_story_assets.py
## ============================================================
import glob
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_RPY = os.path.join(ROOT, "game", "script", "story_gen", "assets.rpy")
GAME = os.path.join(ROOT, "game")
SRC_ROOT = os.path.join(ROOT, "assets_src")

IMG_REF_RE = re.compile(r'image\s+\S+\s+=\s+(?:Transform\(\s*)?"([^"]+)"')


def main():
    if not os.path.exists(ASSETS_RPY):
        print("assets.rpy 不存在（先跑 import_story.py）")
        return 0

    with open(ASSETS_RPY, encoding="utf-8") as f:
        refs = IMG_REF_RE.findall(f.read())

    ## assets_src 全量索引：basename -> 实际路径（重名取最新 mtime）
    src_index = {}
    for f in glob.glob(os.path.join(SRC_ROOT, "**", "*.*"), recursive=True):
        base = os.path.basename(f)
        if base in src_index:
            if os.path.getmtime(f) > os.path.getmtime(src_index[base]):
                src_index[base] = f
        else:
            src_index[base] = f

    copied, missing = 0, []
    for ref in dict.fromkeys(refs):                 # 去重保序
        dst = os.path.join(GAME, ref)
        if os.path.exists(dst):
            continue
        src = src_index.get(os.path.basename(ref))
        if src:
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
            copied += 1
        else:
            missing.append(ref)

    print(f"资产同步: 新拷 {copied} 个，缺失 {len(missing)} 个")
    for m in missing[:10]:
        print("  缺源:", m)
    return 0


if __name__ == "__main__":
    sys.exit(main())
