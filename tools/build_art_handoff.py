"""Build file-verified art handoff reports without modifying image pixels or game scripts."""
import hashlib
import html
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "docs/art"


def read(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8-sig"))


def write(path, value):
    (ROOT / path).write_text(value, encoding="utf-8")


def main():
    now = datetime.now(timezone(timedelta(hours=8))).isoformat(timespec="seconds")
    route = read("docs/art/ds-route-reuse.json")
    errors, rows, packs = [], [], []
    for pack in ("act01", "act02", "act03", "act04", "act05", "act06", "ending"):
        plan = read(f"docs/art/{pack}/production-plan.json")
        counts = dict(backgrounds=0, characters=0, cg=0, props=0)
        missing = []
        for job in plan["jobs"]:
            rel = f"assets_src/{pack}/{job['file']}"
            path = ROOT / rel
            if not path.exists():
                missing.append(job["id"])
                continue
            data = path.read_bytes()
            with Image.open(path) as im:
                im.load()
                size = list(im.size)
                alpha = list(im.getchannel("A").getextrema()) if "A" in im.getbands() else None
            if job.get("transparent") and (alpha is None or alpha[0] != 0 or alpha[1] == 0):
                errors.append(f"Invalid transparency: {rel}")
            is_scene_plate = job["file"].startswith("backgrounds/") or job["id"].startswith("cg")
            if is_scene_plate and not job.get("transparent") and not 1.7 < size[0] / size[1] < 1.85:
                errors.append(f"Invalid landscape ratio: {rel}")
            counts[job["file"].split("/")[0]] += 1
            rows.append(dict(pack=pack, id=job["id"], path=rel, size=size, alpha_range=alpha,
                             sha256=hashlib.sha256(data).hexdigest(), bytes=len(data)))
        packs.append(dict(pack=pack, completed=sum(counts.values()), planned=len(plan["jobs"]),
                          categories=counts, missing=missing))
    for scene in route["scenes"]:
        for rel in scene["reuse"]:
            if not (ROOT / rel).is_file():
                errors.append(f"Missing reuse: {scene['id']} {rel}")
    job_ids = {job["id"] for job in route["supplement_jobs"]}
    for scene in route["scenes"]:
        for job_id in scene["supplements"]:
            if job_id not in job_ids:
                errors.append(f"Unknown supplement: {job_id}")
    for job in route["supplement_jobs"]:
        for rel in job["refs"]:
            if not (ROOT / rel).is_file():
                errors.append(f"Missing supplement reference: {rel}")
    report = dict(checked_at=now, source="working-tree-production-plans", total=len(rows),
                  planned=sum(p["planned"] for p in packs), unique_image_hashes=len({r["sha256"] for r in rows}),
                  packs=packs, errors=errors, assets=rows)
    write("docs/art/拼接前资产核查.json", json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    lines = ["# 拼接前资产核查", "", f"核查时间：{now}。逐项按当前 production-plan 读取 PNG、验证尺寸/透明通道并计算 SHA-256。", "",
             "| 批次 | 背景 | 立绘 | CG | 道具 | 已落盘/计划 |", "|---|---:|---:|---:|---:|---:|"]
    for p in packs:
        c = p["categories"]
        lines.append(f"| {p['pack']} | {c['backgrounds']} | {c['characters']} | {c['cg']} | {c['props']} | {p['completed']}/{p['planned']} |")
    lines += ["", f"当前批次合计 **{report['total']}/{report['planned']}**；独立文件内容 {report['unique_image_hashes']} 张；校验异常 {len(errors)}。",
              "", "这是生产计划内试稿，不是全剧情完成率。DS-01～09待补任务未计入上述分母。",
              "", "第六章新增：2张互动CG、3张透明道具、5张背景差分/修正。原图未缩放或改绘。提示词见 act06/prompts，逐图来源/尺寸/透明通道/哈希见 assets_src/act06/manifest.json。",
              "", "[DS线复用与补充清单](DS线复用与补充清单.md) · [第六章拼接交接](act06/拼接交接.md) · [新增10张预览](../../assets_src/act06/supplement-gallery.html)",
              "", "游戏拼接可先开展现有章节；DS前半段完整画面仍需补齐清单中的P1项。正式接入后还需逐场验证遮挡、表情切换、存档与分支。完成后将原图、提示词和清单一起上传GitHub。"]
    if errors:
        lines += ["", "校验异常："] + [f"- {e}" for e in errors]
    write("docs/art/拼接前资产核查.md", "\n".join(lines) + "\n")
    lines = ["# DS-01～09复用与补充清单", "", f"核查时间：{now}。覆盖9个分景、{sum(s['beats'] for s in route['scenes'])}个节拍。文件存在校验已执行；复用候选仍需画面与服装验收。", "",
             "本清单为拼接执行依据。P1是正式画面所需任务组，P2是可由普通演出替代的可选CG；任务组不等于图片张数。现有冬装、大学室内服装、大学春装和四年后成熟装分开使用。", ""]
    for scene in route["scenes"]:
        lines += [f"## {scene['id']}｜{scene['title']}", "", "可复用文件：", ""]
        lines += [f"- [{rel.split('/')[-1]}](../../{rel})" for rel in scene["reuse"]]
        lines += ["", "节拍安排：", ""] + [f"- {beat}" for beat in scene["beat_map"]]
        lines += ["", "待补任务：" + "、".join(scene["supplements"]) + "。", "", scene["constraints"], ""]
    lines += ["## 补充任务队列", "", "| ID | 类别 | 优先级 | 制作要求 |", "|---|---|---|---|"]
    lines += [f"| {j['id']} | {j['kind']} | {j['priority']} | {j['need']} |" for j in route["supplement_jobs"]]
    lines += ["", "顺序：先做背景差分与服装基准，再补同服装表情和手部，最后生成CG12/CG17；UI01/UI03用Ren'Py真实文字层实现。完整引用与依赖保存在 [ds-route-reuse.json](ds-route-reuse.json)。",
              "", "拼接前复核：春季天台是否有积雪、PR16热茶是否带蒸汽、大学冬装衣领是否统一、机场出发机位与安检方向是否一致。候选不合格再补差分，避免无条件重画已有场景。"]
    write("docs/art/DS线复用与补充清单.md", "\n".join(lines) + "\n")
    plan = read("docs/art/act06/production-plan.json")
    new_ids = {"cg_c602_final_manuscript_handover", "cg_c603_claude_handhold", "pr08_final_manuscript",
               "pr21_interview_portfolio", "pr09_music_document_case", "bg18_student_room_night_continuity",
               "bg26_filmclub_day_continuity", "bg27_backstage_musiccase", "bg29_crossing_barrier_down",
               "bg29_crossing_train_passing"}
    cards = []
    for j in plan["jobs"]:
        if j["id"] in new_ids:
            cards.append(f'<figure><img loading="lazy" src="{html.escape(j["file"])}"><figcaption>{html.escape(j["label"])}<br>{html.escape(j["id"])}</figcaption></figure>')
    write("assets_src/act06/supplement-gallery.html", '<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>第六章新增10张</title><style>body{background:#182030;color:#eee;font:16px system-ui;margin:32px}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(420px,1fr));gap:20px}figure{margin:0;padding:12px;background:#253147}img{width:100%;display:block;background:repeating-conic-gradient(#ddd 0% 25%,#aaa 0% 50%) 0/20px 20px}figcaption{padding:12px 0}</style><h1>第六章新增10张试稿</h1><p>原始PNG预览；已校验尺寸、透明通道和哈希。尚未接入游戏。</p><main>' + "".join(cards) + '</main></html>\n')
    print(json.dumps(dict(total=report["total"], planned=report["planned"], reuse_scenes=len(route["scenes"]),
                          mapped_beats=sum(s["beats"] for s in route["scenes"]), errors=errors), ensure_ascii=False))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
