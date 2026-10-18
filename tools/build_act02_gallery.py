"""Validate the Act 2 background pack and rebuild its offline review page.

Reads original PNGs without editing them; reuses the existing gallery template.
"""
import hashlib
import html
import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from PIL import Image

from build_act01_gallery import TEMPLATE

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "assets_src/act02"
PLAN = ROOT / "docs/art/act02/production-plan.json"
SCENES = [
    ("C2-01", "停滞的电影研究社", "bg_filmclub_dust_day"),
    ("C2-02", "糟糕的成绩单", "bg_classroom_day"),
    ("C2-03", "花坛旁的眼泪", "bg_flowerbed_overcast"),
    ("C2-04", "从课本第一页重新开始", "bg_user_desk_night"),
    ("C2-05", "向老师开口", "bg_corridor_evening"),
    ("C2-06", "第一次看见努力的结果", "bg_corridor_day"),
    ("C2-07", "前排的学姐", "bg_classroom_night"),
    ("C2-08", "不会的地方要说出来", "bg_classroom_evening"),
    ("C2-09", "一点点靠近的课桌", "bg_classroom_evening"),
    ("C2-10", "被推迟的甜品邀约", "bg_classroom_evening"),
    ("C2-11", "没有发出的第二句话", "bg_claude_bedroom_night"),
]


def build():
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    assets, pending = [], []
    for job in plan["jobs"]:
        path = PACK / job["file"]
        if not path.is_file():
            pending.append(job["id"])
            continue
        with Image.open(path) as source:
            source.load()
            width, height = source.size
            alpha = source.getchannel("A").getextrema() if "A" in source.getbands() else (255, 255)
        if abs(width / height - 16 / 9) > 0.01 or alpha != (255, 255):
            raise ValueError(f"Expected opaque 16:9 background: {path}")
        for reference in job["refs"]:
            if not (ROOT / reference).is_file():
                raise FileNotFoundError(reference)
        prompt = ROOT / job["prompt_file"]
        if not prompt.is_file():
            raise FileNotFoundError(prompt)
        refinement = prompt.with_name(prompt.stem + ".refinement.txt")
        assets.append({
            "id": job["id"], "label": job["label"], "path": path.relative_to(ROOT).as_posix(),
            "prompt": job["prompt_file"], "references": job["refs"], "scenes": job["scenes"],
            "refinement_prompt": refinement.relative_to(ROOT).as_posix() if refinement.exists() else None,
            "refinement_reference": f"assets_src/act02/trials/{path.name}" if refinement.exists() else None,
            "width": width, "height": height, "bytes": path.stat().st_size,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "alpha_range": list(alpha),
            "tool": "built-in imagegen", "status": "generated_draft",
        })
    by_id = {a["id"]: a for a in assets}
    shots = [{"id": sid, "title": title, "bg": bg, "sprite": None, "prop": None}
             for sid, title, bg in SCENES if bg in by_id]
    stamp = datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(timespec="seconds")
    manifest = {"schema_version": 1, "updated_at": stamp, "scope": plan["scope"],
                "status": "complete_background_draft_pack" if not pending else "generating",
                "planned_assets": len(plan["jobs"]), "pending_assets": pending,
                "assets": assets, "shots": shots,
                "excluded_trials": [p.relative_to(ROOT).as_posix() for p in sorted((PACK / "trials").glob("*.png"))],
                "notes": "Backgrounds only. Original imagegen PNGs preserved; not integrated into runtime."}
    (PACK / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    viewer_assets = {a["id"]: {"src": str(Path(a["path"]).relative_to("assets_src/act02")).replace("\\", "/"),
                                     "label": a["label"]} for a in assets}
    cards = []
    for asset in assets:
        src = viewer_assets[asset["id"]]["src"]
        label = html.escape(asset["label"])
        prompt = "../../" + asset["prompt"]
        cards.append(f'<article class="card"><a class="art" href="{src}" target="_blank" rel="noopener">'
                     f'<img loading="lazy" src="{src}" alt="{label}"></a><div class="card-copy"><b>{label}</b>'
                     f'<small>{asset["width"]} × {asset["height"]} · PNG</small>'
                     f'<a href="{prompt}">实际提示词</a></div></article>')
    data = json.dumps({"assets": viewer_assets, "shots": shots}, ensure_ascii=False).replace("</", "<\\/")
    page = TEMPLATE.replace("__DATA__", data).replace("__COUNT__", str(len(assets))).replace("__CARDS__", "\n".join(cards))
    page = page.replace("第一幕", "第二幕").replace("从天台到第一次合作", "重新开始")
    page = page.replace("序章 ＋ 第一章", "第二章 · 6 处场地").replace("30 个演出镜头", f"{len(shots)} 个分景背景预览")
    start = page.index('<p class="note">')
    end = page.index("</p>", start) + 4
    page = page[:start] + '<p class="note">本页仅预览第二幕背景，人物、成绩单、草稿、手机、蛋糕等仍为独立资产。相同时段的场地跨分景复用；同场地昼夜差分引用同一底图。方向键切换，空格播放／暂停。</p>' + page[end:]
    page = page.replace("全部资产", "背景原图与时段差分").replace("文件校验与镜头映射", "文件校验与分景映射")
    page = page.replace("../../docs/art/act01/绘图任务单.md", "../../docs/art/act02/绘图任务单.md")
    page = page.replace("角色原型和参考署名随原来源保留。本轮为 AI 生成的第二幕完整美术试稿", "本轮为内置 imagegen 生成的第二幕背景试稿")
    (PACK / "index.html").write_text(page, encoding="utf-8")
    rows = ["# 第二幕背景制作状态", "", f"更新：{stamp}（北京时间）。", "",
            f"已保存并校验 **{len(assets)} / {len(plan['jobs'])}** 张背景；覆盖 **{len(shots)} / {len(SCENES)}** 个分景。", "",
            "六处场地，含教室、书桌和走廊时段差分。仅背景资产包，尚未接入游戏。", "",
            "| 背景 | 文件 |", "| --- | --- |"]
    rows += [f"| {a['label']} | [{Path(a['path']).name}]({viewer_assets[a['id']]['src']}) |" for a in assets]
    if pending:
        rows += ["", "待生成：" + "、".join(pending)]
    rows += ["", "[离线预览](index.html) · [校验清单](manifest.json) · [提示词与参考](../../docs/art/act02/production-plan.json)", ""]
    (PACK / "LIVE_STATUS.md").write_text("\n".join(rows), encoding="utf-8")
    print(json.dumps({"saved": len(assets), "planned": len(plan["jobs"]), "scenes": len(shots), "pending": pending}, ensure_ascii=False))


if __name__ == "__main__":
    build()
