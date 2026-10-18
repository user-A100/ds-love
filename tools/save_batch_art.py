import json
import shutil
import sys
from datetime import datetime
from pathlib import Path
from PIL import Image

root = Path(__file__).resolve().parents[1]
act, name = sys.argv[1:3]
plan = json.loads((root / f'docs/art/{act}/production-plan.json').read_text(encoding='utf-8'))
job = next(j for j in plan['jobs'] if j['id'] == name)
source = max(Path('C:/Users/111222/.codex/generated_images/01a14de3-db63-7e11-8ca3-00ffedad480e').glob('*.png'), key=lambda p: p.stat().st_mtime)
dest = root / f'assets_src/{act}' / job['file']
dest.parent.mkdir(parents=True, exist_ok=True)
if not dest.exists():
    shutil.copy2(source, dest)
assets = []
for j in plan['jobs']:
    f = root / f'assets_src/{act}' / j['file']
    if f.exists():
        with Image.open(f) as im:
            im.load()
            assets.append(dict(id=j['id'], path=f.relative_to(root).as_posix(), width=im.width, height=im.height, alpha_range=im.getchannel('A').getextrema() if 'A' in im.getbands() else None, status='generated_draft'))
n, total = len(assets), len(plan['jobs'])
data = dict(updated_at=datetime.now().astimezone().isoformat(), completed=n, total=total, percent=round(n / total * 100, 1), assets=assets, pending_assets=[j['id'] for j in plan['jobs'] if not (root / f'assets_src/{act}' / j['file']).exists()])
base = root / f'assets_src/{act}'
(base / 'progress.json').write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
(base / 'LIVE_STATUS.md').write_text(f'# {act} 美术制作状态\n\n更新：{data["updated_at"]}\n\n已出图 **{n} / {total}** 项，**{data["percent"]}%**。试稿出图数量，不代表最终验收。\n\n最新保存：{name}\n\n逐项文件及待办见 progress.json。\n', encoding='utf-8')
print(f'{act}: {n}/{total}; saved {dest}')
