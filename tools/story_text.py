"""Parse the authored Chinese/Japanese Markdown into ordered story events.

Production notes, reference links and scene directions are not spoken text.
Original files are never changed by this module.
"""
import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Event:
    kind: str
    chapter: str
    text: str
    speaker: str = "narrator"
    source: str = ""
    line: int = 0


ALIASES = {
    "母": "母亲", "Claudeの母": "Claude 母亲", "担任": "班主任",
    "先生": "老师", "クラスメイト": "同学", "図書館員": "图书管理员",
    "図書室の先生": "图书管理员", "図書委員": "图书管理员",
    "スタッフ": "工作人员", "司書": "图书管理员",
}
SPEAKER_NAMES = set(ALIASES) | set(ALIASES.values()) | {
    "User", "DeepSeek", "Claude", "GPT", "？？？", "母亲", "Claude 母亲",
    "班主任", "老师", "同学", "图书管理员", "工作人员",
}
HEADING = re.compile(r"^#{2,3}\s+(.*)$")
DIALOGUE = re.compile(r"^([^：「]{1,24})：「(.*)$")
INLINE = re.compile(r"([^：「\n]{1,24})：「([^」]*)」")
SCENE_CARD = re.compile(r"^((?:CG|BG)-\d+)｜")
END_CUE = re.compile(r"^【(?:第[^】]*(?:完)|DeepSeek True End|通关|クリアCG)")
SELECTION_HEADING = ("最终路线选择", "最終ルート選択")
STAGE_PREFIXES = ("场景 ", "场景：", "シーン ", "場所：", "时间：", "時間：")


def markup(text):
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"(?<!\w)_(.+?)_(?!\w)", r"\1", text)
    return text.strip()


def parse_markdown(path, chapter, chapter_rules=(), start_marker="", body_from_start=False):
    """Each authored paragraph remains a unit; multi-paragraph letters remain speech."""
    path = Path(path)
    events = []
    started = not start_marker
    in_scene = body_from_start
    pending_speaker = None
    pending_text = []
    pending_line = 0

    def say(speaker, text, line):
        text = text.strip()
        if text:
            events.append(Event("say", chapter, text, ALIASES.get(speaker, speaker), str(path), line))

    for lineno, raw in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        stripped = raw.strip()
        line = markup(stripped)
        if not started:
            if line.startswith("# ") and start_marker in line:
                started = True
            continue
        if pending_speaker:
            if not line:
                continue
            # A standalone speaker tag is followed by an opening quote.
            if not pending_text and line.startswith("「"):
                line = line[1:]
            pending_text.append(line.split("」", 1)[0])
            if "」" in line:
                say(pending_speaker, "\n".join(pending_text), pending_line)
                pending_speaker, pending_text = None, []
            continue
        if not line or line.startswith(("![", "- ")) or line == "---" or re.fullmatch(r"\[.*\]\(.*\)", line):
            continue
        if line.startswith("# "):
            in_scene = False
            continue
        match = HEADING.match(line)
        if match:
            heading = match.group(1)
            for rule in chapter_rules:
                if rule["match"] in heading:
                    chapter = rule["chapter"]
                    break
            in_scene = not any(x in heading for x in SELECTION_HEADING)
            if in_scene:
                events.append(Event("heading", chapter, heading, source=str(path), line=lineno))
            continue
        if END_CUE.match(line):
            in_scene = False
            continue
        if not in_scene:
            continue
        match = SCENE_CARD.match(line)
        if match:
            events.append(Event("background", chapter, match.group(1), source=str(path), line=lineno))
            continue
        if line.startswith(STAGE_PREFIXES):
            events.append(Event("direction", chapter, line, source=str(path), line=lineno))
            continue
        if line.startswith(("Next Chapter", "次のシーン：", "下一场景：")):
            continue
        if line.startswith("【"):
            end = line.find("】")
            cue, rest = line[1:end], line[end + 1:].strip()
            events.append(Event("direction", chapter, cue + (" " + rest if rest else ""), source=str(path), line=lineno))
            if cue not in ("旁白", "地の文", "最终独白", "最後の独白"):
                continue
            line = rest
            if not line:
                continue
        match = re.fullmatch(r"([^：「]{1,24})：", line)
        if match and match.group(1).strip() in SPEAKER_NAMES:
            pending_speaker, pending_line = match.group(1).strip(), lineno
            continue
        matches = list(INLINE.finditer(line))
        if matches:
            last, previous = 0, None
            for match in matches:
                if match.start() > last:
                    say("narrator", line[last:match.start()], lineno)
                item = (match.group(1).strip(), match.group(2))
                # The source accidentally repeats the same complete question on one line.
                # Only collapse this exact inline duplication, not repeated lines/scenes.
                if item != previous:
                    say(*item, lineno)
                previous = item
                last = match.end()
            if line[last:].strip():
                say("narrator", line[last:], lineno)
            continue
        match = DIALOGUE.match(line)
        if match:
            pending_speaker, pending_line = match.group(1).strip(), lineno
            pending_text = [match.group(2)] if match.group(2) else []
            continue
        say("narrator", line, lineno)
    if pending_speaker:
        raise ValueError(f"Unclosed dialogue at {path}:{pending_line}")
    return events


def group_says(events, chapter):
    """Group narration between dialogue anchors, preserving every paragraph."""
    result, narration = [], []
    for e in events:
        if e.chapter != chapter or e.kind != "say":
            continue
        if e.speaker == "narrator":
            narration.append(e)
        else:
            result.append((narration, e))
            narration = []
    return result, narration


def _align_section(chinese, japanese, chapter, speakers):
    """Align by ordered speaker turns, never by fuzzy text similarity.

    Native Ren'Py translation blocks may contain multiple say statements or pass.
    This supports the natural paragraph splits in the supplied Japanese drafts.
    """
    zh, zh_tail = group_says(chinese, chapter)
    ja, ja_tail = group_says(japanese, chapter)
    def role(e):
        if e.speaker not in speakers:
            raise ValueError(f"Unknown speaker {e.speaker!r} at {e.source}:{e.line}")
        return speakers[e.speaker]
    if len(zh) != len(ja):
        raise ValueError(f"{chapter}: dialogue counts differ: Chinese={len(zh)}, Japanese={len(ja)}")
    mapping = {}
    def narrate(before, translated):
        if not before:
            return translated
        mapping[before[0]] = list(translated)
        for event in before[1:]:
            mapping[event] = []
        return []
    for index, ((before, z), (translated, j)) in enumerate(zip(zh, ja)):
        if role(z) != role(j):
            raise ValueError(f"{chapter}: speaker mismatch at turn {index + 1}: {z.source}:{z.line} ({z.speaker}) / {j.source}:{j.line} ({j.speaker})")
        extra = narrate(before, translated)
        mapping[z] = list(extra) + [j]
    extra = narrate(zh_tail, ja_tail)
    if extra:
        if not zh:
            raise ValueError(f"{chapter}: no Chinese units for translation")
        mapping[zh[-1][1]].extend(extra)
    return mapping


def boundary(event):
    if event.kind == "background":
        return "background:" + event.text
    if event.kind == "heading":
        return "heading"
    if event.kind == "direction" and event.text.startswith(
        ("场景切换", "场景：", "シーン転換", "シーン：", "場所：")
    ):
        return "cut"
    return None


def sections(events, chapter):
    result = [("start", [])]
    for event in events:
        if event.chapter != chapter:
            continue
        key = boundary(event)
        if key:
            result.append((key, []))
        elif event.kind == "say":
            result[-1][1].append(event)
    return result


def align_chapter(chinese, japanese, chapter, speakers):
    """Do not move a translated paragraph across a scene/camera boundary."""
    zh, ja = sections(chinese, chapter), sections(japanese, chapter)
    if [key for key, _ in zh] != [key for key, _ in ja]:
        raise ValueError(f"{chapter}: Chinese/Japanese scene boundaries differ")
    mapping = {}
    for index, ((_, z), (_, j)) in enumerate(zip(zh, ja), 1):
        try:
            mapping.update(_align_section(z, j, chapter, speakers))
        except ValueError as error:
            raise ValueError(f"scene section {index}: {error}") from error
    return mapping
