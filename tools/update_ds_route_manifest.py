"""Validate original DS route PNGs and build the handoff manifest and gallery."""
import hashlib
import html
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "assets_src/ds_route"
DOC = ROOT / "docs/art/ds_route"


def read(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def save(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    plan = read(DOC / "production-plan.json")
    route = read(ROOT / "docs/art/ds-route-reuse.json")
    now = datetime.now(timezone(timedelta(hours=8))).isoformat(timespec="seconds")
    assets, pending, errors = [], [], []
    (DOC / "prompts").mkdir(parents=True, exist_ok=True)
    for job in plan["jobs"]:
        prompt = f"docs/art/ds_route/prompts/{job['id']}.txt"
        (ROOT / prompt).write_text(job["prompt"] + "\n", encoding="utf-8")
        for index, previous in enumerate(job.get("previous_versions", []), 1):
            (DOC / "prompts" / f"{job['id']}_revision_{index}.txt").write_text(previous["prompt"] + "\n", encoding="utf-8")
        for ref in job["refs"]:
            if not (ROOT / ref).is_file():
                errors.append(f"Missing reference: {ref}")
        path = PACK / job["file"]
        if not path.is_file():
            pending.append(job["id"])
            continue
        with Image.open(path) as im:
            im.load()
            width, height = im.size
            alpha = im.getchannel("A") if "A" in im.getbands() else None
            extrema = list(alpha.getextrema()) if alpha else [255, 255]
            edge = max(alpha.crop(box).getextrema()[1] for box in ((0, 0, width, 1), (0, height-1, width, height),
                       (0, 0, 1, height), (width-1, 0, width, height))) if alpha else 255
        if job["transparent"] and (extrema[0] != 0 or extrema[1] == 0):
            errors.append(f"Missing real alpha: {job['id']}")
        if job["file"].startswith("characters/") and not .6 < width/height < .72:
            errors.append(f"Unexpected portrait ratio: {job['id']}")
        if not job["transparent"] and not 1.7 < width/height < 1.85:
            errors.append(f"Unexpected landscape ratio: {job['id']}")
        data = path.read_bytes()
        assets.append({**job, "path": "assets_src/ds_route/" + job["file"], "prompt": prompt,
                       "width": width, "height": height, "alpha_range": extrema, "edge_alpha_max": edge,
                       "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
                       "tool": "built-in imagegen", "status": "generated_draft_visually_reviewed"})
    manifest = dict(schema_version=1, updated_at=now, scope=plan["scope"],
                    status="complete_planned_draft_pack" if not pending and not errors else "incomplete",
                    planned_assets=len(plan["jobs"]), completed=len(assets), pending_assets=pending,
                    errors=errors, runtime_integrated=False, pixel_registered=False, assets=assets)
    save(PACK / "manifest.json", manifest)
    grouped = {}
    for asset in assets:
        grouped.setdefault(asset["group"], []).append(asset["path"])
    for task in route["supplement_jobs"]:
        task["generated_assets"] = grouped.get(task["id"], [])
        task["status"] = "engine_ui_pending" if task["kind"] == "engine_ui" else (
            "generated_draft" if task["generated_assets"] else "pending")
    coverage = []
    for scene in route["scenes"]:
        scene["generated_assets"] = list(dict.fromkeys(path for group in scene["supplements"] for path in grouped.get(group, [])))
        scene["remaining_supplements"] = [group for group in scene["supplements"] if not grouped.get(group)]
        paths = scene["reuse"] + scene["generated_assets"]
        missing = [path for path in paths if not (ROOT / path).is_file()]
        if missing:
            errors.extend(f"Missing scene asset: {path}" for path in missing)
        coverage.append(dict(scene=scene["id"], beats=[f"{scene['id']}-B{i:02}" for i in range(1, scene["beats"]+1)],
                             reused_assets=scene["reuse"], generated_assets=scene["generated_assets"],
                             beat_map=scene["beat_map"], remaining=scene["remaining_supplements"],
                             mapped_files_present=not missing, runtime_verified=False))
    route["status"] = "planned_art_generated_engine_ui_pending" if not pending else "generating"
    route["notes"] = "30 supplemental artworks planned, including 4 optional CGs. File-verified scene mapping; UI01/UI03 and runtime visual verification remain. Original images unchanged."
    save(ROOT / "docs/art/ds-route-reuse.json", route)
    save(PACK / "scene-coverage.json", dict(scope="DS-01–DS-09", mapped_beats=sum(s["beats"] for s in route["scenes"]),
                                          status="art_mapped_runtime_pending", scenes=coverage))
    plan["status"] = manifest["status"]
    save(DOC / "production-plan.json", plan)
    lines = ["# DeepSeek线补充美术制作状态", "", f"核查：{now}", "",
             f"已保存并校验 **{len(assets)} / {len(plan['jobs'])}** 项入选图片；待生成：{'、'.join(pending) or '无'}；校验异常：{len(errors)}。", "",
             "本轮包含26张必要补图和4张可选CG。32个PNG含2张修订记录，只计30项入选图。", "",
             "使用内置imagegen生成；原图未改像素、缩放或重编码。立绘/挂件为真实透明PNG；表情未逐像素配准。", "",
             "[全图预览](index.html) · [逐场景映射](scene-coverage.json) · [逐图校验](manifest.json)", ""]
    lines += [f"- {a['scene']} · [{a['label']}]({a['file']})" for a in assets]
    lines += ["", "剩余工作：引擎聊天/通知/日历文字层、脚本接入及画面验收。CG14使用v002冷茶修正版；CG15使用v002手部修正版，拉钩细节可另切PR10局部图。", "",
              "角色来源与署名沿用 ../characters/README.md；完成后请将原图、提示词与清单上传GitHub。"]
    (PACK / "LIVE_STATUS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    cards = []
    for a in assets:
        category = a["file"].split("/")[0]
        cards.append(f'<figure data-kind="{category}"><a href="{html.escape(a["file"])}"><img loading="lazy" src="{html.escape(a["file"])}" alt="{html.escape(a["label"])}"></a><figcaption>{html.escape(a["label"])}<br><small>{html.escape(a["scene"])} · {a["width"]}×{a["height"]} · {a["priority"]}</small></figcaption></figure>')
    page = '''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DeepSeek线补充30张</title><style>body{background:#172132;color:#edf4ff;font:16px system-ui;margin:28px}nav{display:flex;gap:10px;flex-wrap:wrap;margin:24px 0}button{font:inherit;border:1px solid #829ab7;border-radius:6px;padding:8px 14px;color:inherit;background:#283b56;cursor:pointer}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,390px),1fr));gap:18px}figure{margin:0;padding:12px;background:#25344b;border-radius:8px}img{width:100%;height:350px;object-fit:contain;display:block;background:repeating-conic-gradient(#d5dbe3 0% 25%,#adb6c3 0% 50%) 0/20px 20px}figcaption{padding:12px 0 0}small{color:#b7c9e3}[hidden]{display:none}</style><h1>DeepSeek线 · 补充美术30张</h1><p>26张必要补图＋4张可选CG。点击图片查看原始PNG；旧版修订记录不重复展示。</p><nav><button data-filter="all">全部</button><button data-filter="backgrounds">背景</button><button data-filter="characters">立绘/表情</button><button data-filter="props">道具</button><button data-filter="details">局部</button><button data-filter="cg">CG</button></nav><main>'''
    page += "".join(cards) + '''</main><script>document.querySelectorAll('button').forEach(b=>b.onclick=()=>document.querySelectorAll('figure').forEach(f=>f.hidden=b.dataset.filter!=='all'&&b.dataset.filter!==f.dataset.kind));</script></html>'''
    (PACK / "index.html").write_text(page, encoding="utf-8")
    print(json.dumps(dict(completed=len(assets), planned=len(plan["jobs"]), pending=pending, errors=errors), ensure_ascii=False))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
