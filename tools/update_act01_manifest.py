"""Publish a verifiable snapshot of the images already saved by imagegen.

Reads images for validation only. Never edits or re-encodes PNGs.
"""
import hashlib
import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "assets_src" / "act01"
PLAN = ROOT / "docs" / "art" / "act01" / "production-plan.json"


def update():
    plan = json.loads(PLAN.read_text(encoding="utf-8-sig"))
    assets, pending = [], []
    for job in plan["jobs"]:
        path = PACK / job["file"]
        if not path.is_file():
            pending.append(job["id"])
            continue
        try:
            with Image.open(path) as image:
                image.load()
                width, height = image.size
                alpha = image.getchannel("A").getextrema() if "A" in image.getbands() else (255, 255)
        except OSError:
            pending.append(job["id"])
            continue  # imagegen may still be copying this file
        if job["transparent"] and alpha[0] != 0:
            raise ValueError(f"Expected genuine transparent margins: {path}")
        prompt = ROOT / job["prompt_file"]
        if not prompt.is_file():
            raise FileNotFoundError(prompt)
        assets.append({
            "id": job["id"], "label": job["label"],
            "path": path.relative_to(ROOT).as_posix(),
            "prompt": job["prompt_file"], "references": job["refs"],
            "width": width, "height": height, "bytes": path.stat().st_size,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "transparent_requested": job["transparent"], "alpha_range": list(alpha),
            "tool": "built-in imagegen", "status": "generated_draft",
        })
    ids = {asset["id"] for asset in assets}
    shots = [shot for shot in plan["shots"] if all(not shot.get(key) or shot[key] in ids for key in ("bg", "sprite", "prop"))]
    stamp = datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(timespec="seconds")
    manifest = {
        "schema_version": 1, "updated_at": stamp,
        "status": "complete_draft_pack" if not pending else "generating",
        "scope": plan["scope"], "planned_assets": len(plan["jobs"]),
        "planned_shot_count": len(plan["shots"]), "pending_assets": pending,
        "assets": assets, "shots": shots, "planned_shots": plan["shots"],
        "excluded_trials": ["characters/deepseek/ds_hs_neutral_v001.png"],
        "notes": "Original imagegen PNGs preserved. HTML layers preview separate images; not runtime integration.",
    }
    (PACK / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    rows = ["# 第一幕实时制作状态", "", f"更新：{stamp}（北京时间）。", "", f"已保存并校验 **{len(assets)} / {len(plan['jobs'])}** 项入选资产；覆盖 **{len(shots)} / {len(plan['shots'])}** 个演出镜头。", "", "当前仍在连续生成。以此页和 manifest.json 的实际文件为准；README 的资产数是整批目标。" if pending else "本轮整批美术试稿已完成。", "", "## 队友使用的固定参考", "", "- [DeepSeek 制服基准](characters/deepseek/ds_hs_neutral_v002.png)", "- [Claude 制服基准](characters/claude/claude_hs_neutral_v001.png)", "- [天台场地基准](backgrounds/bg_rooftop_spring_day_v001.png)", "- [图书馆场地基准](backgrounds/bg_library_day_v001.png)", "- [操场场地基准](backgrounds/bg_playground_evening_v001.png)", "- [笔记本基准](props/pr01_blue_notebook_v001.png)", "", "角色的脸、发型、发饰左右、制服细节以以上参考为准；新图必须附对应基准图，不只复制文字提示。光从左上方进入；镜头留出下方约24%的对白区域。参考原图的署名和许可信息继续保留。", "", "## 当前可用文件", "", "| 资产 | 文件 |", "| --- | --- |"]
    rows.extend(f"| {asset['label']} | [{Path(asset['path']).name}]({Path(asset['path']).relative_to('assets_src/act01').as_posix()}) |" for asset in assets)
    if pending:
        rows.extend(["", "## 正在生成 / 待生成", "", *[f"- `{item}`" for item in pending]])
    rows.extend(["", "逐图提示词与参考路径：[production-plan.json](../../docs/art/act01/production-plan.json)；完整校验：[manifest.json](manifest.json)。", ""])
    (PACK / "LIVE_STATUS.md").write_text("\n".join(rows), encoding="utf-8")
    print(json.dumps({"completed": len(assets), "planned": len(plan["jobs"]), "shots": len(shots), "pending": pending}, ensure_ascii=False))


if __name__ == "__main__":
    update()
