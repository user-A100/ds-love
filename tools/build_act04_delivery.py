import hashlib
import html
import json
from pathlib import Path
from PIL import Image

root = Path(__file__).resolve().parents[1]
base = root / 'assets_src/act04'
plan = json.loads((root / 'docs/art/act04/production-plan.json').read_text(encoding='utf-8'))
assets, cards = [], []
for job in plan['jobs']:
    path = base / job['file']
    with Image.open(path) as im:
        im.load()
        alpha = im.getchannel('A').getextrema() if 'A' in im.getbands() else None
        if job['transparent']:
            assert alpha and alpha[0] == 0 and alpha[1] > 0, path
        item = dict(id=job['id'], path=path.relative_to(root).as_posix(), width=im.width, height=im.height,
                    sha256=hashlib.sha256(path.read_bytes()).hexdigest(), alpha_range=alpha,
                    status='generated_draft', scenes=job['scenes'], prompt_file=job['prompt_file'])
    assets.append(item)
    cards.append(f'<article><a href="{html.escape(job["file"])}"><img loading="lazy" src="{html.escape(job["file"])}"></a><h2>{html.escape(job["label"])}</h2><p>{html.escape(", ".join(job["scenes"]))} · {item["width"]}×{item["height"]}</p></article>')
(base / 'draft-manifest.json').write_text(json.dumps(dict(status='generated_draft', assets=assets), ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
(base / 'all-assets.html').write_text('<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>第四幕完整试稿</title><style>body{background:#182333;color:#eee;font:16px system-ui;margin:32px}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:24px}article{background:#253448;padding:16px;border-radius:12px}img{width:100%;height:320px;object-fit:contain;background:repeating-conic-gradient(#444 0% 25%,#555 0% 50%) 0/24px 24px}h2{font-size:18px}</style><h1>第四幕：32 / 32 试稿</h1><p>出图完成不等于定稿或游戏接入。已知问题见 REVIEW_NOTES.md。点击图片查看原图。</p><main>'+''.join(cards)+'</main></html>', encoding='utf-8')
(base / 'REVIEW_NOTES.md').write_text('''# 第四幕试稿验收记录

32 / 32 项均已出图，PNG 完整解码与文件哈希已记录；全部要求透明的道具与角色文件均存在透明像素。使用内置 imagegen，提示词见 docs/art/act04/prompts，逐项依赖与分景见 production-plan.json。

## 待修与复核

- 原有角色立绘参考中可见大面积彩色光晕；虽然文件有 alpha，仍需清理背景残留后才能作为正式透明立绘使用。不能仅凭存在 alpha 判断合格。
- cg_c408b_unsent：床的位置与公寓底图不一致，另一只手托腮而非放在乐谱旁；室内连续性与动作需修稿。
- cg_c406a_waiting：头顶呆毛贴近边缘，正式裁切前需留出安全边距。
- cg08_ds_confession：手部抓握偏向裙布而非外套下摆，尾巴未在当前构图中显现；需对照分镜确认或修稿。
- CG 手部、钢琴键与演奏手势仍需正式细查；角色表情差分尚未做像素配准。

所有图片为试稿，未宣告最终验收，尚未接入游戏。本次接续生成 11 项，没有修改其他幕资产。
''', encoding='utf-8')
print(f'Validated {len(assets)} PNGs; manifest and preview saved.')
