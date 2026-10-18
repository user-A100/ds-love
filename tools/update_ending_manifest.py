"""Validate and index original imagegen PNGs without editing pixels."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import hashlib, html, json
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "assets_src/ending"
PLAN = ROOT / "docs/art/ending/production-plan.json"

def update():
    plan = json.loads(PLAN.read_text(encoding="utf-8-sig"))
    assets, pending = [], []
    for job in plan["jobs"]:
        path = PACK / job["file"]
        if not path.is_file():
            pending.append(job["id"])
            continue
        prompt = ROOT / "docs/art/ending/prompts" / (job["id"] + ".txt")
        if not prompt.is_file():
            raise FileNotFoundError(prompt)
        for ref in job.get("refs", []):
            if not (ROOT / ref).is_file():
                raise FileNotFoundError(ref)
        with Image.open(path) as im:
            im.load()
            alpha = im.getchannel("A") if "A" in im.getbands() else None
            extrema = alpha.getextrema() if alpha else (255,255)
            if job["transparent"] and extrema[0] != 0:
                raise ValueError("Missing transparent margins: " + job["file"])
            size = im.size
            edge_max = None
            if alpha:
                edge_max = max(alpha.crop((0,0,im.width,1)).getextrema()[1],
                               alpha.crop((0,im.height-1,im.width,im.height)).getextrema()[1],
                               alpha.crop((0,0,1,im.height)).getextrema()[1],
                               alpha.crop((im.width-1,0,im.width,im.height)).getextrema()[1])
        assets.append({
            "id": job["id"], "label": job["label"], "scene": job["scene"],
            "path": path.relative_to(ROOT).as_posix(),
            "prompt": prompt.relative_to(ROOT).as_posix(),
            "references": job.get("refs", []),
            "width": size[0], "height": size[1], "bytes": path.stat().st_size,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "transparent_requested": job["transparent"], "alpha_range": list(extrema),
            "edge_alpha_max": edge_max,
            "tool": "built-in imagegen", "status": "generated_draft"
        })
    stamp = datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(timespec="seconds")
    manifest = {"schema_version":1, "updated_at":stamp, "order":"reverse_story",
                "status":"generating" if pending else "complete_planned_draft_pack",
                "scope":plan["scope"], "planned_assets":len(plan["jobs"]),
                "pending_assets":pending, "assets":assets,
                "notes":"Original PNG bytes preserved. Reference-based production drafts; not layered Live2D and not runtime integration."}
    (PACK/"manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    lines = ["# 后半段美术实时状态", "", "更新：" + stamp, "",
             f"已保存并校验 {len(assets)} / {len(plan['jobs'])} 项当前计划素材。", "",
             "按剧情倒序制作：DS-14B → DS-14A → DS-13B → DS-13A → DS-12 → DS-11 → DS-10，随后继续向前补缺。",
             "角色脸、蓝眼睛、渐变长发、呆毛、鳍耳、青蓝发结与鲸尾以第一幕队友基准为身份参照；成年便服单独建立基准。",
             "原图、角色来源与上游署名见 ../characters/README.md 及 ../characters/sources/ai-girls/NOTICE.md。生成改编不改写原素材许可。", "",
             "## 已完成", ""]
    lines += [f"- {a['scene']} · {a['label']} — [{Path(a['path']).name}]({Path(a['path']).relative_to('assets_src/ending').as_posix()})" for a in assets]
    if pending:
        lines += ["", "## 已列入计划、尚未完成", ""] + ["- " + p for p in pending]
    lines += ["", "所有 PNG 保留实际生成尺寸；透明图有真实 alpha。草稿需正式美术校正，不代表已完成逐像素差分配准；文件未接入游戏脚本。",
              "未知男主正脸保持不定义；文字与首映物料由游戏文字层排版。", ""]
    (PACK/"LIVE_STATUS.md").write_text("\n".join(lines),encoding="utf-8")
    cards=[]
    for a in assets:
        rel=Path(a["path"]).relative_to("assets_src/ending").as_posix()
        cards.append('<article><a href="'+html.escape(rel)+'" target="_blank"><img loading="lazy" src="'+html.escape(rel)+'" alt="'+html.escape(a["label"])+'"></a><h2>'+html.escape(a["label"])+'</h2><p>'+html.escape(a["scene"])+' · '+str(a["width"])+' × '+str(a["height"])+'</p><code>'+html.escape(a["id"])+'</code></article>')
    page='<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>未抵达的心意 · 后半段美术</title><style>body{margin:0;background:#101829;color:#e7ecf7;font:16px system-ui,sans-serif}header,main{max-width:1450px;margin:auto;padding:28px}header p{color:#aebbd2}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:22px}article{padding:14px;background:#1e2b42;border-radius:12px;overflow:hidden}img{width:100%;height:340px;object-fit:contain;background:repeating-conic-gradient(#39445c 0% 25%,#46526c 0% 50%) 50%/20px 20px}h2{font-size:17px}p,code{font-size:13px}a{color:#8dc9ff}</style><header><h1>未抵达的心意 · 后半段美术</h1><p>剧情倒序 / 原始 PNG / '+str(len(assets))+' 项已完成 / 点击查看原图</p><p>人物时期、同场景布局、旧笔记本形制保持连续；所有版本均为生成试稿。</p><a href="manifest.json">机器可读清单</a> · <a href="LIVE_STATUS.md">制作状态</a></header><main>'+"".join(cards)+'</main></html>'
    (PACK/"index.html").write_text(page,encoding="utf-8")
    print(json.dumps({"completed":len(assets),"planned":len(plan["jobs"]),"pending":pending},ensure_ascii=False))

if __name__ == "__main__":
    update()

