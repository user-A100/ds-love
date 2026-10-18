"""Build the offline Act 1 artwork review page from its saved manifest.

Uses the Python standard library only; does not modify any image.
"""

import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "assets_src" / "act01"


def build():
    manifest = json.loads((PACK / "manifest.json").read_text(encoding="utf-8-sig"))
    assets = manifest["assets"]
    by_id = {asset["id"]: asset for asset in assets}
    for asset in assets:
        if not (ROOT / asset["path"]).is_file():
            raise FileNotFoundError(asset["path"])
    for shot in manifest["shots"]:
        for layer in ("bg", "sprite", "prop"):
            if shot.get(layer) and shot[layer] not in by_id:
                raise ValueError(f"Missing {layer} in {shot['id']}: {shot[layer]}")

    viewer_assets = {
        asset["id"]: {
            "src": str(Path(asset["path"]).relative_to("assets_src/act01")).replace("\\", "/"),
            "label": asset["label"],
        }
        for asset in assets
    }
    cards = []
    for asset in assets:
        relative = viewer_assets[asset["id"]]["src"]
        label = html.escape(asset["label"])
        prompt = "../../" + asset["prompt"]
        category = asset["path"].split("/")[2]
        cards.append(
            f'<article class="card" data-category="{category}">'
            f'<a class="art" href="{html.escape(relative)}" target="_blank" '
            f'rel="noopener"><img loading="lazy" src="{html.escape(relative)}" '
            f'alt="{label}"></a><div class="card-copy"><b>{label}</b>'
            f'<small>{asset["width"]} × {asset["height"]} · PNG</small>'
            f'<a href="{html.escape(prompt)}">实际提示词</a></div></article>'
        )

    data = json.dumps({"assets": viewer_assets, "shots": manifest["shots"]}, ensure_ascii=False)
    page = TEMPLATE.replace("__DATA__", data.replace("</", "<\\/"))
    page = page.replace("__COUNT__", str(len(assets))).replace("__CARDS__", "\n".join(cards))
    output = PACK / "index.html"
    output.write_text(page, encoding="utf-8")
    print(f"Built {output}: {len(assets)} assets, {len(manifest['shots'])} shots")


TEMPLATE = r'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>未抵达的心意 · 第一幕美术</title>
<style>
:root{color-scheme:light;--navy:#243950;--muted:#64788b;--paper:#f4f6f8;--line:#d8e1e8}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--navy);font:15px/1.65 system-ui,'Microsoft YaHei',sans-serif}
main{max-width:1280px;margin:auto;padding:38px 24px 72px}header{display:flex;justify-content:space-between;align-items:end;gap:20px;margin-bottom:24px}
h1{font-size:30px;margin:0;letter-spacing:.04em}p{margin:5px 0;color:var(--muted)}a{color:#356c9c}button,select{font:inherit;border:1px solid var(--line);background:white;color:var(--navy);padding:7px 14px;border-radius:5px;cursor:pointer}button:hover{background:#e7eef4}button:focus-visible,select:focus-visible,a:focus-visible{outline:3px solid #e0a54b;outline-offset:3px}
.stage{position:relative;aspect-ratio:16/9;background:#dce7ed;overflow:hidden;border-radius:7px}.stage>img{position:absolute;display:block;pointer-events:none}.back{width:100%;height:100%;object-fit:cover}.sprite{height:96%;width:59%;object-fit:contain;bottom:-20%;right:0}.prop{height:35%;width:28%;object-fit:contain;bottom:17%;left:19%}.stage .hidden{display:none}.dialogue-safe{position:absolute;bottom:0;width:100%;height:24%;background:linear-gradient(transparent,rgba(15,29,47,.80));color:white;padding:26px 28px 16px;display:flex;flex-direction:column;justify-content:end}.dialogue-safe small{color:#dbe8f3}.dialogue-safe b{font-size:20px;font-weight:500}
.controls{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin:14px 0}.controls span{margin-left:auto;color:var(--muted)}.filmstrip{display:flex;gap:8px;overflow:auto;padding:0 0 14px}.filmstrip button{flex:0 0 155px;text-align:left;padding:9px 10px;font-size:12px}.filmstrip .active{background:var(--navy);color:white}.filmstrip b{display:block;font-size:13px}.note{font-size:13px;margin:12px 0 30px}
h2{font-size:23px;font-weight:600;margin:28px 0 16px}.gallery{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}.card{background:white;border:1px solid var(--line);border-radius:7px;overflow:hidden}.art{height:235px;display:block;background-color:#e7edf1;background-image:linear-gradient(45deg,#dce4e9 25%,transparent 25%),linear-gradient(-45deg,#dce4e9 25%,transparent 25%),linear-gradient(45deg,transparent 75%,#dce4e9 75%),linear-gradient(-45deg,transparent 75%,#dce4e9 75%);background-size:20px 20px;background-position:0 0,0 10px,10px -10px,-10px 0}.art img{width:100%;height:100%;object-fit:contain;display:block}.card-copy{padding:12px 15px;display:flex;flex-wrap:wrap;gap:3px 12px}.card-copy b{width:100%;font-weight:550}.card-copy small{color:var(--muted);margin-right:auto}.card-copy a{font-size:12px}.footer{margin-top:30px;font-size:13px}
@media(max-width:800px){main{padding:22px 12px}.gallery{grid-template-columns:repeat(2,minmax(0,1fr))}.art{height:200px}header{display:block}.dialogue-safe{padding:10px 14px}.dialogue-safe b{font-size:15px}.dialogue-safe small{font-size:10px}}@media(max-width:460px){.gallery{grid-template-columns:1fr}}
</style></head><body><main>
<header><div><p>《未抵达的心意》 · 美术试制 v0.1</p><h1>第一幕，从天台到第一次合作</h1></div><p>序章 ＋ 第一章 · __COUNT__ 项资产 · 30 个演出镜头</p></header>
<section aria-label="连续分镜预览"><div class="stage"><img id="back" class="back" alt=""><img id="sprite" class="sprite hidden" alt=""><img id="prop" class="prop hidden" alt=""><div class="dialogue-safe"><small id="shot-id"></small><b id="shot-title"></b></div></div>
<div class="controls"><button id="prev" type="button">← 上一镜</button><button id="play" type="button">连续播放</button><button id="next" type="button">下一镜 →</button><label for="pace">间隔</label><select id="pace"><option value="4000">4 秒</option><option value="7000">7 秒</option></select><span id="position"></span></div><div id="filmstrip" class="filmstrip" aria-label="镜头选择"></div></section>
<p class="note">这是分镜与资产连续性预览，镜头标题用于辨认演出节拍。立绘、道具在网页中作为独立图层展示，原始 PNG 未合并或改写；图书馆站姿层仅供表情预览，坐姿与接触动作见完整 CG。方向键切镜，空格播放 / 暂停。</p>
<h2>全部资产</h2><div class="gallery">__CARDS__</div>
<p class="footer"><a href="manifest.json">文件校验与镜头映射</a> · <a href="../../docs/art/act01/绘图任务单.md">绘图任务单</a> · 角色原型和参考署名随原来源保留。本轮为 AI 生成的第一幕完整美术试稿，尚未接入正式游戏脚本。</p>
</main><script>
'use strict';
const data=__DATA__;
const shots=data.shots,assets=data.assets;
let index=0,timer=null;
const el=id=>document.getElementById(id);
function layer(id,asset){const image=el(id);image.classList.toggle('hidden',!asset);if(asset){image.src=assets[asset].src;image.alt=assets[asset].label;}else{image.removeAttribute('src');image.alt='';}}
function show(n){index=Math.max(0,Math.min(shots.length-1,n));const shot=shots[index];layer('back',shot.bg);layer('sprite',shot.sprite);layer('prop',shot.prop);el('shot-id').textContent=shot.id;el('shot-title').textContent=shot.title;el('position').textContent=`${index+1} / ${shots.length}`;for(const [i,button] of [...el('filmstrip').children].entries())button.classList.toggle('active',i===index);}
function stop(){if(timer)clearInterval(timer);timer=null;el('play').textContent='连续播放';}
function start(){stop();if(index===shots.length-1)show(0);el('play').textContent='暂停';timer=setInterval(()=>{if(index===shots.length-1)stop();else show(index+1);},Number(el('pace').value));}
shots.forEach((shot,i)=>{const button=document.createElement('button');button.type='button';const label=document.createElement('b');label.textContent=shot.id;button.append(label,document.createTextNode(shot.title));button.addEventListener('click',()=>{stop();show(i);});el('filmstrip').append(button);});
el('prev').addEventListener('click',()=>{stop();show(index-1);});el('next').addEventListener('click',()=>{stop();show(index+1);});el('play').addEventListener('click',()=>timer?stop():start());el('pace').addEventListener('change',()=>{if(timer)start();});
document.addEventListener('keydown',event=>{if(['BUTTON','SELECT','INPUT'].includes(event.target.tagName))return;if(event.code==='ArrowRight'){event.preventDefault();stop();show(index+1);}if(event.code==='ArrowLeft'){event.preventDefault();stop();show(index-1);}if(event.code==='Space'){event.preventDefault();timer?stop():start();}});
show(0);
</script></body></html>'''


if __name__ == "__main__":
    build()
