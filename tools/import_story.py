#!/usr/bin/env python3
## ============================================================
## import_story.py —— 剧本导入器（markdown → Ren'Py 脚本）
##
## 设计原则：
##   1. 中文源 story/chapters/*.md 与 story/japanese.json 指定日文稿
##      生成主剧本及 game/tl/japanese/story_gen/，生成文件请勿手改
##   2. 配音 ID = md5(角色+台词)[:12]，内容寻址——插行/删行不
##      错位，台词本身改了 ID 才变（旧配音随之失效，语义正确）
##   3. 所有映射（说话人/章节归属/场景资产/立绘）在 story/*.json
##      配置，本工具不含任何剧情相关的硬编码
##   4. 确定性输出：同一输入永远生成同一文件，git diff 干净
##
## 用法:
##   python3 tools/import_story.py            # 生成
##   python3 tools/import_story.py --check    # 只统计校验，不写盘
## ============================================================
import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import sys

from story_text import parse_markdown, align_chapter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORY_DIR = os.path.join(ROOT, "story")
MD_PATH = os.path.join(STORY_DIR, "chapters", "未抵达的心意.md")
GEN_DIR = os.path.join(ROOT, "game", "script", "story_gen")

GENERATED_HEADER = \
"""## ============================================================
## !! 本文件由 tools/import_story.py 生成 —— 请勿手改 !!
## 源: story/chapters/未抵达的心意.md + story/japanese.json 指定的日文稿
## 重建: python3 tools/import_story.py
## ============================================================
"""

## 立绘站位：角色变量 → 位置
SPRITE_POS = {"ds": "left", "cl": "center", "gp": "right"}

def load_json(name):
    with open(os.path.join(STORY_DIR, name), encoding="utf-8") as f:
        return json.load(f)


def esc(text):
    """Ren'Py say 字符串转义: \\ " % [ """
    text = text.replace("\\", "\\\\")
    text = text.replace("\r\n", "\n").replace("\r", "\n").replace("\n", "\\n")
    text = text.replace('"', '\\"')
    text = text.replace("%", "%%")
    text = text.replace("[", "[[")
    return text


def voice_id(speaker, text):
    h = hashlib.md5((speaker + "\x00" + text.strip()).encode("utf-8")).hexdigest()
    return "v_" + h[:12]


class Importer:

    def __init__(self):
        self.speakers = load_json("speakers.json")
        self.structure = load_json("structure.json")
        self.scenes = load_json("scenes.json")
        self.sprites = load_json("sprites.json")
        self.chapter_order = self.structure["chapter_order"]
        self.chapters = {c: [] for c in self.chapter_order}
        self.current = self.chapter_order[0]
        self.shown = set()
        self.events = []
        self.translations = {}
        self.translation_files = {c: [] for c in self.chapter_order}
        self.id_counts = Counter()

    # ---------- 语句生成 ----------

    def emit(self, line):
        self.chapters[self.current].append(line)

    def emit_say(self, speaker, text, event):
        text = text.strip()
        var = "narrator" if speaker == "narrator" else self.speakers.get(speaker)
        if var is None:
            raise ValueError("未知说话人 {} ({}:{})".format(speaker, event.source, event.line))
        if var in SPRITE_POS and var not in self.shown:
            self.emit("show {} normal at sprite_pos_{} with trans_dissolve".format(var, SPRITE_POS[var]))
            self.shown.add(var)
        key = (self.current, speaker, text)
        self.id_counts[key] += 1
        identifier = "story_{}_{}_{}".format(self.current, voice_id(speaker, text)[2:], self.id_counts[key])
        if var != "narrator":
            self.emit('voice voice_file("{}")'.format(voice_id(speaker, text)))
        self.emit('{} "{}" id {}'.format(var, esc(text), identifier))

        translated = self.translations[event]
        block = ["translate japanese {}:".format(identifier)]
        if not translated:
            block.append("    pass")
        for target in translated:
            who = "narrator" if target.speaker == "narrator" else self.speakers[target.speaker]
            # Letters are authored as multi-paragraph speech; show one paragraph per click.
            for paragraph in target.text.split("\n"):
                paragraph = paragraph.strip()
                if not paragraph:
                    continue
                if who != "narrator":
                    block.append('    voice voice_file("{}")'.format(voice_id(target.speaker, paragraph)))
                block.append('    {} "{}"'.format(who, esc(paragraph)))
        self.translation_files[self.current].extend(block + [""])

    def emit_scene_reset(self, heading):
        self.emit("")
        self.emit("## ── 场景: {} ──".format(heading))
        for who in sorted(self.shown):
            self.emit("hide {}".format(who))
        self.shown.clear()

    # ---------- 主解析 ----------

    def parse(self):
        self.events = parse_markdown(
            MD_PATH, self.chapter_order[0], self.structure["chapter_rules"],
            self.structure.get("start_marker", ""))
        japanese = []
        for source in load_json("japanese.json")["sources"]:
            rules = [{"match": "第一章", "chapter": "ch01"}] if source["chapter"] == "ch00" else []
            japanese.extend(parse_markdown(
                Path(STORY_DIR) / source["file"], source["chapter"], rules,
                source.get("start_marker", ""), source.get("body_from_start", False)))
        for chapter in self.chapter_order:
            self.translations.update(align_chapter(self.events, japanese, chapter, self.speakers))
        self.japanese_units = sum(len(v) for v in self.translations.values())
        for event in self.events:
            self.current = event.chapter
            if event.kind == "say":
                self.emit_say(event.speaker, event.text, event)
            elif event.kind == "heading":
                self.emit_scene_reset(event.text)
            elif event.kind == "background":
                self.emit('$ scene_bg("{}")'.format(event.text))
                self.emit("with trans_dissolve")
                self.shown.clear()
            elif event.kind == "direction":
                self.emit("## 演出: " + event.text)

    # ---------- 输出 ----------

    def render(self):
        files = {}

        ## ── assets.rpy: 图片定义 + SCENE_BG ──
        dict_lines = []
        image_lines = []
        for key, conf in self.scenes.items():
            if key.startswith("_"):
                continue
            conf = conf or {}
            img_name = "bg_" + key.lower().replace("-", "_")
            exists = bool(conf.get("file")) and os.path.exists(
                os.path.join(ROOT, "game", conf["file"]))
            if exists:
                dict_lines.append('    "{}": "{}",'.format(key, img_name))
                image_lines.append('image {} = "{}"'.format(img_name, conf["file"]))
            else:
                dict_lines.append('    "{}": None,    ## 资产未就绪: {}'.format(
                    key, conf.get("file", "?")))
        for key, conf in self.sprites.items():
            if key.startswith("_"):
                continue
            conf = conf or {}
            exists = bool(conf.get("file")) and os.path.exists(
                os.path.join(ROOT, "game", conf["file"]))
            if exists:
                image_lines.append('image {} = "{}"'.format(key, conf["file"]))
            else:
                image_lines.append('image {} = Placeholder("girl")'.format(key))

        a = [GENERATED_HEADER, ""]
        a.append("define SCENE_BG = {")
        a.extend(dict_lines)
        a.append("}")
        a.append("")
        a.append("## 立绘（真实资产就绪前用 Placeholder 剪影）")
        a.extend(image_lines)
        files["assets.rpy"] = "\n".join(a) + "\n"

        ## ── 章节文件 ──
        order = self.chapter_order
        for i, ch in enumerate(order):
            body = self.chapters[ch]
            out = [GENERATED_HEADER, "", "label {}:".format(ch)]
            if not body:
                out.append('    narrator "（本章待导入）"')
            else:
                for l in body:
                    out.append("    " + l if l else "")

            ## 章末: 分歧菜单优先，否则顺序链
            branches = self.structure.get("branch_after", {}).get(ch)
            if branches:
                out.append("")
                out.append("    menu:")
                for b in branches:
                    out.append('        "{}":'.format(esc(b["text"])))
                    out.append("            jump {}".format(b["goto"]))
            else:
                nxt = order[i + 1] if i + 1 < len(order) else None
                out.append("")
                out.append("    jump {}".format(nxt if nxt else "ending"))
            files["{}.rpy".format(ch)] = "\n".join(out) + "\n"

        for chapter, body in self.translation_files.items():
            files["tl/japanese/story_gen/{}.rpy".format(chapter)] = GENERATED_HEADER + "\n" + "\n".join(body)
        choices = [GENERATED_HEADER, "translate japanese strings:"]
        for branches in self.structure.get("branch_after", {}).values():
            for branch in branches:
                choices.extend(["", '    old "{}"'.format(esc(branch["text"])),
                                '    new "{}"'.format(esc(branch["japanese"]))])
        files["tl/japanese/story_gen/choices.rpy"] = "\n".join(choices) + "\n"
        return files

    def report(self):
        print("章节统计:")
        for ch in self.chapter_order:
            print("  {:<10} 语句 {:>5}".format(ch, len(self.chapters[ch])))
        print("日文映射: {} 个中文单元 -> {} 个日文段落".format(len(self.translations), self.japanese_units))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="只统计校验，不写盘")
    args = ap.parse_args()

    imp = Importer()
    imp.parse()
    imp.report()

    files = imp.render()
    if args.check:
        print("--check 模式: 未写盘")
        return 0

    for name, content in files.items():
        target = Path(ROOT) / "game" / name if name.startswith("tl/") else Path(GEN_DIR) / name
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("w", encoding="utf-8") as f:
            f.write(content)
    print("已生成 {} 个文件 -> {}".format(len(files), os.path.relpath(GEN_DIR, ROOT)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
