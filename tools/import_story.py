#!/usr/bin/env python3
## ============================================================
## import_story.py —— 剧本导入器（markdown → Ren'Py 脚本）
##
## 设计原则：
##   1. story/chapters/*.md 是唯一事实来源，game/script/story_gen/
##      下的 .rpy 全部是生成产物（DO NOT EDIT），可随时重建
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
import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORY_DIR = os.path.join(ROOT, "story")
MD_PATH = os.path.join(STORY_DIR, "chapters", "未抵达的心意.md")
GEN_DIR = os.path.join(ROOT, "game", "script", "story_gen")

GENERATED_HEADER = \
"""## ============================================================
## !! 本文件由 tools/import_story.py 生成 —— 请勿手改 !!
## 源: story/chapters/未抵达的心意.md (+ story/*.json)
## 重建: python3 tools/import_story.py
## ============================================================
"""

## 立绘站位：角色变量 → 位置
SPRITE_POS = {"ds": "left", "cl": "center", "gp": "right"}

DIALOGUE_RE = re.compile(r"^(.{1,20}?)：「(.*)$")
HEADING_RE = re.compile(r"^#{2,3}\s+(.*)$")
SCENE_CARD_RE = re.compile(r"^((?:CG|BG)-\d+)｜")
SFX_RE = re.compile(r"^【音效】\s*(.*)$")
INLINE_LINK_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")
INLINE_DLG_RE = re.compile(r"([^：「\n]{1,20})：「([^」]*)」")
STRIP_TAGS = ("BGM", "音效", "场景", "画面", "CG")


def clean_text(text):
    """剥离标记/链接/markdown 噪音，返回纯台词/旁白文本"""
    text = INLINE_LINK_RE.sub(r"\1", text)
    text = re.sub(r"【(?:BGM|音效|场景|画面|CG)[^】]*】", "", text)
    text = re.sub(r"^【旁白】\s*", "", text)
    text = re.sub(r"^【最终独白】\s*", "", text)
    text = re.sub(r"_(.+?)_", r"\1", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def split_inline_dialogue(line):
    """把 '叙述A 角色：「对白」叙述B 角色2：「对白2」' 切成片段列表
    [("n", 叙述A), ("d", 角色, 对白), ("n", 叙述B), ...]"""
    pieces = []
    last = 0
    for m in INLINE_DLG_RE.finditer(line):
        if m.start() > last:
            pieces.append(("n", line[last:m.start()]))
        pieces.append(("d", m.group(1).strip(), m.group(2)))
        last = m.end()
    if last < len(line):
        pieces.append(("n", line[last:]))
    return pieces


def load_json(name):
    with open(os.path.join(STORY_DIR, name), encoding="utf-8") as f:
        return json.load(f)


def esc(text):
    """Ren'Py say 字符串转义: \\ " % [ """
    text = text.replace("\\", "\\\\")
    text = text.replace('"', '\\"')
    text = text.replace("%", "%%")
    text = text.replace("[", "[[")
    return text


def clean_markup(line):
    """去掉轻量 markdown 噪音"""
    line = re.sub(r"\*\*(.+?)\*\*", r"\1", line)
    line = re.sub(r"\*(.+?)\*", r"\1", line)
    return line.strip()


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
        self.unknown_speakers = {}
        self.shown = set()

    # ---------- 章节归属 ----------

    def match_chapter(self, heading):
        for rule in self.structure["chapter_rules"]:
            if rule["match"] in heading:
                return rule["chapter"]
        return None    # 未命中 → 保持当前章节

    # ---------- 语句生成 ----------

    def emit(self, line):
        self.chapters[self.current].append(line)

    def emit_say(self, speaker, text):
        text = text.strip()
        if not text:
            return
        if speaker == "narrator":
            self.emit('narrator "{}"'.format(esc(text)))
            return
        var = self.speakers.get(speaker)
        if var is None:
            ## 未知说话人：并入旁白，加名字前缀，报告警告
            self.unknown_speakers[speaker] = self.unknown_speakers.get(speaker, 0) + 1
            self.emit('narrator "{}：{}"'.format(esc(speaker), esc(text)))
            return
        if var != "narrator":
            self.emit('$ play_voice("{}")'.format(voice_id(speaker, text)))
            ## 自动立绘：主角团在场上且未显示 → 入场
            if var in SPRITE_POS and var not in self.shown:
                self.emit("show {} normal at sprite_pos_{} with trans_dissolve".format(
                    var, SPRITE_POS[var]))
                self.shown.add(var)
        self.emit('{} "{}"'.format(var, esc(text)))

    def emit_scene_reset(self, heading):
        self.emit("")
        self.emit("## ── 场景: {} ──".format(heading))
        for who in sorted(self.shown):
            self.emit("hide {}".format(who))
        self.shown.clear()

    # ---------- 主解析 ----------

    def parse(self):
        start_marker = self.structure.get("start_marker", "")
        started = not start_marker

        with open(MD_PATH, encoding="utf-8") as f:
            lines = f.read().splitlines()

        para_buf = []

        def flush_para():
            if para_buf:
                text = clean_text("".join(para_buf))
                para_buf.clear()
                if text:
                    self.emit_say("narrator", text)

        def emit_plain(stripped):
            """普通文本：行内对白切分后逐段产出"""
            pieces = split_inline_dialogue(clean_text(stripped))
            for p in pieces:
                if p[0] == "d":
                    flush_para()
                    self.emit_say(p[1], p[2])
                elif p[1].strip():
                    self.emit_say("narrator", p[1])

        dlg_speaker = None
        dlg_text = None

        for raw in lines:
            line = raw.rstrip()

            ## ── start_marker 之前的内容（企划书/设定/链接）不进剧本 ──
            if not started:
                if line.startswith("# ") and start_marker in line:
                    started = True
                continue

            ## ── 跨行对白缓冲中 ──
            if dlg_speaker is not None:
                dlg_text += line
                if "」" in line:
                    self.emit_say(dlg_speaker, dlg_text.split("」")[0])
                    dlg_speaker = None
                    dlg_text = None
                continue

            stripped = line.strip()

            ## ── 空行 / H1 / 图片 / 分割线 / 列表项 / 纯链接行 ──
            if (not stripped or stripped.startswith("# ")
                    or stripped.startswith("![")
                    or stripped.startswith("- ")
                    or stripped == "---"
                    or re.fullmatch(r"\[.*\]\(.*\)", stripped)):
                continue

            ## ── 标题（##/###）：章节归属 + 场景边界 ──
            m = HEADING_RE.match(stripped)
            if m:
                flush_para()
                heading = m.group(1).strip()
                new_ch = self.match_chapter(heading)
                if new_ch and new_ch in self.chapters:
                    self.current = new_ch
                self.emit_scene_reset(heading)
                continue

            ## ── 场景卡 CG-XXX/BG-XXX｜描述【旁白】正文… ──
            m = SCENE_CARD_RE.match(stripped)
            if m:
                flush_para()
                self.emit('$ scene_bg("{}")'.format(m.group(1)))
                self.emit("with trans_dissolve")
                rest = stripped[m.end():]
                tail = rest[rest.find("【"):] if "【" in rest else ""
                if tail.strip():
                    emit_plain(tail)
                continue

            ## ── 音效标记 → 注释占位 ──
            m = SFX_RE.match(stripped)
            if m:
                flush_para()
                self.emit("## TODO 音效: {}".format(m.group(1)))
                continue

            ## ── 行首对白（支持跨行）──
            m = DIALOGUE_RE.match(stripped)
            if m and "：" not in m.group(1):
                flush_para()
                speaker = m.group(1).strip()
                rest = m.group(2)
                if "」" in rest:
                    self.emit_say(speaker, rest.split("」")[0])
                else:
                    dlg_speaker, dlg_text = speaker, rest
                continue

            ## ── 普通文本（含行内对白切分）──
            if "：「" in stripped:
                flush_para()
                emit_plain(stripped)
            else:
                para_buf.append(stripped)

        flush_para()

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

        return files

    def report(self):
        print("章节统计:")
        for ch in self.chapter_order:
            print("  {:<10} 语句 {:>5}".format(ch, len(self.chapters[ch])))
        if self.unknown_speakers:
            print("!! 未知说话人（已并入旁白）:")
            for k, v in self.unknown_speakers.items():
                print("   {}: {} 句".format(k, v))


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

    os.makedirs(GEN_DIR, exist_ok=True)
    for old in os.listdir(GEN_DIR):
        if old.endswith(".rpy"):
            os.remove(os.path.join(GEN_DIR, old))
    for name, content in files.items():
        with open(os.path.join(GEN_DIR, name), "w", encoding="utf-8") as f:
            f.write(content)
    print("已生成 {} 个文件 -> {}".format(len(files), os.path.relpath(GEN_DIR, ROOT)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
