"""Validate chapter-six generated PNGs; preserve original pixels."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import hashlib, json
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / 'assets_src/act06'
PLAN = ROOT / 'docs/art/act06/production-plan.json'

def update():
    plan = json.loads(PLAN.read_text(encoding='utf-8-sig'))
    assets, pending = [], []
    for job in plan['jobs']:
        prompt = ROOT / 'docs/art/act06/prompts' / (job['id'] + '.txt')
        prompt.parent.mkdir(parents=True, exist_ok=True)
        prompt.write_text(job['prompt'] + '\n', encoding='utf-8')
        path = PACK / job['file']
        if not path.is_file():
            pending.append(job['id'])
            continue
        for ref in job['refs']:
            assert (ROOT / ref).is_file(), ref
        with Image.open(path) as im:
            im.load()
            size = im.size
            alpha = im.getchannel('A').getextrema() if 'A' in im.getbands() else (255, 255)
            if job['transparent']:
                assert alpha[0] == 0, f'Missing alpha: {path}'
            else:
                assert 1.7 < size[0] / size[1] < 1.85, f'Invalid landscape ratio: {path}'
        assets.append(dict(id=job['id'], label=job['label'], scene=job['scene'], path=path.relative_to(ROOT).as_posix(), prompt=prompt.relative_to(ROOT).as_posix(), references=job['refs'], width=size[0], height=size[1], alpha_range=list(alpha), bytes=path.stat().st_size, sha256=hashlib.sha256(path.read_bytes()).hexdigest(), tool='built-in imagegen', status='generated_draft'))
    stamp = datetime.now(timezone(timedelta(hours=8))).isoformat(timespec='seconds')
    PACK.mkdir(parents=True, exist_ok=True)
    manifest = dict(schema_version=1, updated_at=stamp, scope='C6-01–C6-06 only', status='in_progress' if pending else 'complete_planned_draft_pack', planned_assets=len(plan['jobs']), pending_assets=pending, assets=assets)
    (PACK / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    lines = ['# 第六章美术资产', '', f'已完成并校验 {len(assets)}/{len(plan["jobs"])} 项。更新：{stamp}', '', '仅覆盖 C6-01～C6-06。沿用 assets_src/act05 的成年冬装三女主；不包含后续路线。', '', '## 本批图片', '']
    lines += [f'- {a["scene"]} · {a["label"]} — [{Path(a["path"]).name}]({Path(a["path"]).relative_to("assets_src/act06").as_posix()})' for a in assets]
    lines += ['', '## 待生成', ''] + (['- ' + p for p in pending] or ['无。'])
    lines += ['', '## 复用与演出', '', '- C6-02：复用 act05 的 DeepSeek 大学冬装；新增认真抱本为独立姿态草稿，并非配准表情差分。', '- C6-03：复用 Claude 成年冬装，后台不穿音乐会礼服。', '- C6-04A/B：复用 GPT 工作冬装，保持白发、龙角、龙翼、长尾和发饰。', '- C6-05/06：共用铁路道口底图；列车和栏杆升降动画需独立图层。', '- 日历 1/20、1/23、1/27、手机联系人、四选项菜单与稿件正文由可编辑文字层显示。', '- 原始 PNG 保持实际尺寸和字节；来源、参考与完整提示词见 manifest.json 和 docs/art/act06。保留上游角色署名。', '- 本批为美术源资产草稿，未接入 Ren’Py 运行脚本。', '']
    (PACK / 'README.md').write_text('\n'.join(lines), encoding='utf-8')
    print(f'Validated {len(assets)}/{len(plan["jobs"])} chapter-six assets; pending: {pending}')

if __name__ == '__main__':
    update()
