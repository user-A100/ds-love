"""Audit committed art packs across fetched GitHub branches, without merging them."""
import hashlib
import io
import json
import subprocess
from datetime import datetime, timezone, timedelta
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]

def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)

def main():
    sources = [('act01', 'origin/master', 'manifest.json'),
               ('act02', 'origin/master', 'draft-manifest.json'),
               ('act03', 'origin/master', 'draft-manifest.json'),
               ('act05', 'origin/master', 'manifest.json'),
               ('ending', 'origin/master', 'manifest.json')]
    rows, packs, errors = [], [], []
    for pack, ref, filename in sources:
        manifest = json.loads(git('show', f'{ref}:assets_src/{pack}/{filename}'))
        counts = dict(backgrounds=0, characters=0, cg=0, props=0)
        for asset in manifest['assets']:
            path = asset['path']
            data = git('show', f'{ref}:{path}')
            digest = hashlib.sha256(data).hexdigest()
            with Image.open(io.BytesIO(data)) as im:
                im.load()
                size = list(im.size)
                alpha = list(im.getchannel('A').getextrema()) if 'A' in im.getbands() else None
            if asset.get('sha256') and asset['sha256'] != digest:
                errors.append(f'{path}: SHA-256 mismatch')
            if size != [asset['width'], asset['height']]:
                errors.append(f'{path}: dimensions mismatch')
            category = path.split('/')[2]
            counts[category] += 1
            rows.append(dict(pack=pack, id=asset['id'], path=path, ref=ref,
                             sha256=digest, size=size, alpha_range=alpha))
        packs.append(dict(pack=pack, ref=ref, commit=git('rev-parse', ref).decode().strip(),
                          count=sum(counts.values()), categories=counts))
    now = datetime.now(timezone(timedelta(hours=8))).isoformat(timespec='seconds')
    result = dict(checked_at=now, total=len(rows), unique_image_hashes=len({r['sha256'] for r in rows}),
                  packs=packs, errors=errors, assets=rows)
    out = ROOT / 'docs/art'
    (out / 'progress-summary.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    lines = ['# 绘画进度汇总', '', f'核查时间：{now}。依据已抓取的 GitHub 分支逐项读取 PNG、校验尺寸与 SHA-256；未合并分支。', '',
             '| 范围 | 背景 | 立绘/表情 | CG | 道具 | 已出图/当前批次 |', '|---|---:|---:|---:|---:|---:|']
    for p in packs:
        c = p['categories']
        lines.append(f"| {p['pack']} | {c['backgrounds']} | {c['characters']} | {c['cg']} | {c['props']} | {p['count']}/{p['count']} |")
    totals = {k: sum(p['categories'][k] for p in packs) for k in counts}
    lines += [f"| 合计 | {totals['backgrounds']} | {totals['characters']} | {totals['cg']} | {totals['props']} | {len(rows)}/{len(rows)} |", '',
              f"共 {len(rows)} 个入选资产条目，{result['unique_image_hashes']} 个不同 SHA-256 的图片文件。参考图、弃稿、旧版本、游戏内复制文件和重复分支记录不计入新增资产。校验异常：{len(errors)}。", '',
              '## 队友新增作品', '',
              '第五幕新增 Claude 成年冬装·自持、DeepSeek 大学冬装·温柔、GPT 成年工作冬装·微笑，共3项，均为1024×1536，具有真实透明通道。当前3项出图计划完成，不表示第五章全部美术完成。',
              'Claude 原分支：`codex/act05-art-assets`；已由提交 `1544616` 纳入 master，原图与分支版本一致。另两项由 `ed0e054` 纳入 master。第五幕核查提交：`'+packs[3]['commit']+'`，尚未接入游戏。', '',
              '## 全剧情剩余工作', '',
              '- 第四章、第六章：尚无独立完成素材包；已有资产可复用，不等于这些章节完全没有可用素材。',
              '- 第五章：目前新增三位女主的成年冬装基础立绘，其余背景、角色差分、CG和道具仍需按分景补齐。',
              '- DS 线：仅 DS-14B 当前6项素材完成，DS-10～DS-14A及更早路线素材未形成完整交付包。',
              '- 正式验收、差分配准及完整游戏接入尚未完成。当前批次出图率100%，全游戏完成率因完整执行清单尚未建立而不计算。', '',
              '## 记录纠正', '',
              '- 第二幕 README 的10张仅为背景数量，完整试稿包实际21项。',
              '- 第三幕 README 的“制作中”已落后于15/15的进度记录。',
              '- 总资产表“没有完成的绘图”为初始规划状态，不能作为现状。',
              '- 第一幕已有部分背景和立绘进入游戏定义；此前“所有素材尚未接入”说法过于笼统。完整包接入仍未完成。', '',
              '逐项清单与分支提交见 progress-summary.json。完成后请将统计文件上传 GitHub。']
    (out / '绘画进度汇总.md').write_text('\n'.join(lines)+'\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('checked_at', 'total', 'unique_image_hashes', 'packs', 'errors')}, ensure_ascii=False, indent=2))
    if errors:
        raise SystemExit(1)

if __name__ == '__main__':
    main()
