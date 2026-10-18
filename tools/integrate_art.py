"""Install referenced original artwork, validate cues, and build a review gallery.

This does not package the game or publish it. Run import_story.py afterwards.
"""
import argparse
import hashlib
import html
import json
from pathlib import Path
import shutil

from import_story import Importer
from art_direction import load_direction

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Validate installed files without writing')
    args = parser.parse_args()
    importer = Importer()
    importer.parse()
    data, _ = load_direction(ROOT, importer.events)
    for asset in data['assets'].values():
        source, target = ROOT / asset['source'], ROOT / 'game' / asset['runtime']
        if args.check:
            if not target.is_file() or hashlib.sha256(source.read_bytes()).digest() != hashlib.sha256(target.read_bytes()).digest():
                raise ValueError('Runtime asset differs or is missing: ' + str(target))
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            if not target.exists() or source.read_bytes() != target.read_bytes():
                shutil.copyfile(source, target)
    report = {'scene_count': len(data['scenes']), 'asset_count': len(data['assets']),
              'cue_count': sum(len(s.get('cues', [])) for s in data['scenes']),
              'chapters': sorted({s['anchor']['chapter'] for s in data['scenes']}),
              'limitations': [{'scene': s['id'], 'notes': s['notes']} for s in data['scenes'] if s['notes']]}
    if not args.check:
        out = ROOT / 'docs/art/integration'
        out.mkdir(exist_ok=True)
        (out / 'coverage.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        cards = []
        def img(key, css):
            asset = data['assets'][key]
            return '<img class="{}" src="../../../{}" alt="{}" loading="lazy">'.format(css, html.escape(asset['source']), html.escape(asset['label']))
        for scene in data['scenes']:
            visual = img(scene['background'], 'bg')
            for who, key in scene['characters'].items():
                visual += img(key, 'sprite ' + who)
            cue_cards = []
            for cue in scene['cues']:
                for kind in ('cg', 'prop', 'background'):
                    if cue.get(kind):
                        cue_cards.append('<figure>{}<figcaption>{}</figcaption></figure>'.format(img(cue[kind], 'thumb'), html.escape(cue['anchor']['text'])))
            cards.append('<article><h2>{} · {}</h2><div class="stage">{}</div><p>{}</p><p>{}</p><div class="cues">{}</div></article>'.format(
                scene['id'], html.escape(scene['title']), visual, html.escape(scene['anchor']['text']),
                html.escape('；'.join(scene['notes'])), ''.join(cue_cards)))
        css = 'body{background:#172335;color:#edf1fa;font:16px system-ui;margin:24px}main{max-width:1400px;margin:auto}article{margin:30px 0;padding:20px;background:#22324a}.stage{position:relative;aspect-ratio:16/9;overflow:hidden}.bg{width:100%;height:100%;object-fit:cover}.sprite{position:absolute;height:97.2%;bottom:0;max-width:60%;object-fit:contain}.ds{left:4%}.cl{left:28%}.gp{right:4%}.cues{display:flex;flex-wrap:wrap;gap:12px}figure{margin:0;width:280px}.thumb{width:100%;height:160px;object-fit:contain;background:#172335}figcaption,p{font-size:13px;line-height:1.7}h2{font-size:19px}'
        page = '<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>游戏美术接入核对</title><style>' + css + '</style><h1>现有美术接入 · ' + str(report['scene_count']) + ' 场</h1><p>场景构图示意与正文触发点；游戏内人物按实际入场对白出现。未打包、未发布。</p><main>' + ''.join(cards) + '</main></html>'
        (out / 'gallery.html').write_text(page, encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
