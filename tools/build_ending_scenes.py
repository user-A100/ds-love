"""Map every authored ending beat to original assets and build offline scene preview."""
import html
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT/'assets_src/ending'

def main():
    plan = json.loads((ROOT/'docs/art/ending/production-plan.json').read_text(encoding='utf-8'))
    paths = {j['id']: j['file'] for j in plan['jobs']}
    scenes = [
        ('DS-10','四年里各自成长','bg31_director_studio_day',[
            ('独立导演逐步成长',['cg_ds10_growth_work']),
            ('投稿出版与逐渐拥有读者',['pr27_creative_works']),
            ('节日问候与作品互发',['pr27_creative_works']),
            ('各自承担未来',['cg_ds10_growth_work'])]),
        ('DS-11','名单上熟悉的名字','bg32_adaptation_forum_day',[
            ('工作人员递来名单',['pr28_forum_book_list']),
            ('认出姓名与候鸟简介',['pr28_forum_book_list']),
            ('熟悉声音与转身',['ds_mat_spring_neutral']),
            ('跑近并及时停步',['cg18_forum_reunion']),
            ('笑着说好久不见',['ds_mat_spring_blush'])]),
        ('DS-12','现在的我们再次喜欢','bg33_reunion_park_sunset',[
            ('分享失败与成长',['ds_mat_spring_neutral']),
            ('确认彼此单身',['ds_mat_spring_blush']),
            ('重新回应机场约定',['ds_mat_spring_tender']),
            ('写作也为自己的人生',['ds_mat_spring_teary_smile']),
            ('握手与具体相处需求',['ds_mat_spring_tender']),
            ('主动短吻',['cg19_park_short_kiss'])]),
        ('DS-13A','共同创作仍会争论','bg31_director_studio_day',[
            ('小说进入电影改编',['pr29_adaptation_script','ds_mat_daily_neutral']),
            ('讨论情节与结局',['cg_ds13a_creating_together']),
            ('次日仍一起完成工作',['pr29_adaptation_script','ds_mat_daily_earnest']),
            ('完成片与片名转场',['pr29_adaptation_script'])]),
        ('DS-13B','这本笔记本终于可以归还','bg34_premiere_backstage_evening',[
            ('慌张寻找旧本',['ds_mat_premiere_flustered']),
            ('泛黄纸页与归还约定',['pr01_aged_blue_notebook']),
            ('理解梦想兑现后的拥抱',['cg20_premiere_notebook_embrace']),
            ('工作人员催场与回头邀请',['ds_mat_premiere_neutral']),
            ('回答下一部仍一起拍',['ds_mat_premiere_neutral'])]),
        ('DS-14A','在日常里给彼此留位置','bg31_director_studio_evening',[
            ('忘钥匙与忙到忘吃饭',['cg_ds14a_daily_care']),
            ('轻快带过生活小事',['ds_mat_daily_neutral']),
            ('争论后为彼此留时间',['ds_mat_daily_earnest']),
            ('春日回到母校',['bg01_refurbished_spring_day'])]),
        ('DS-14B','天台上的少女与明天','bg01_refurbished_spring_day',[
            ('翻新的栏杆与并肩回忆',['ds_mat_spring_neutral']),
            ('回忆初遇时的轻松拌嘴',['ds_mat_spring_pout']),
            ('愿意再次相遇并主动牵手',['ds_mat_spring_tender']),
            ('牵手走向楼梯门',['cg21_rooftop_tomorrow']),
            ('明早仍能相见',['ds_mat_spring_happy']),
            ('通关仅解锁实际制作CG',['cg21_rooftop_tomorrow'])])]
    records, cards, missing = [], [], []
    for scene, title, bg, beats in scenes:
        for n,(label, assets) in enumerate(beats,1):
            beat = f'{scene}-B{n:02d}'
            ids = [bg]+assets
            absent = [a for a in ids if not (PACK/paths[a]).is_file()]
            missing.extend(absent)
            records.append(dict(scene=scene,beat=beat,label=label,background=bg,assets=assets,
                                available=not absent,text_layer='Original screenplay dialogue, UI messages, lists, titles, calendar and version numbers are typeset by the game; not baked into artwork.'))
            full = next((a for a in assets if paths[a].startswith(('cg/','backgrounds/'))),None)
            visual = '<img class="bg" src="'+html.escape(paths[full or bg])+'">'
            if not full:
                for a in assets:
                    visual += '<img class="'+('sprite' if paths[a].startswith('characters/') else 'prop')+'" src="'+html.escape(paths[a])+'">'
            cards.append('<article><h2>'+html.escape(beat+' · '+title)+'</h2><div class="frame">'+visual+'</div><p>'+html.escape(label)+'</p><small>'+html.escape(', '.join(ids))+'</small></article>')
    data=dict(scope=plan['scope'],scene_count=len(scenes),beat_count=len(records),covered_beats=sum(r['available'] for r in records),missing_assets=sorted(set(missing)),beats=records)
    (PACK/'scene-coverage.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    plan['completed_scenes']=[scene for scene,_,_,_ in scenes if all(r['available'] for r in records if r['scene']==scene)]
    plan['status']='complete_full_ending_draft_pack' if not missing else 'generating_full_ending'
    (ROOT/'docs/art/ending/production-plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    lines=['# 终章全量绘画覆盖', '', '依据现有分景，范围 DS-10～DS-14B。内置 imagegen 逐资产生成，已有最终天台素材复用。', '', '| 分景 | 名称 | 已覆盖节拍/总节拍 |', '|---|---|---:|']
    for scene,title,_,beats in scenes:
        ready=sum(r['available'] for r in records if r['scene']==scene)
        lines.append(f'| {scene} | {title} | {ready}/{len(beats)} |')
    lines += ['', f"合计：{data['covered_beats']}/{data['beat_count']}节拍；素材执行计划27项（背景6、立绘与表情10、CG7、道具4），原有6项，新增21项。", '',
              '原稿UI、对白、出版物标题、名单、日历、版本号与END由真实文字层完成。普通节拍共享场地和立绘，动作互动CG单独绘制。', '',
              '## 交付与核查', '',
              '- `assets_src/ending/scenes.html`：全部34个节拍的离线画面预览。',
              '- `assets_src/ending/scene-coverage.json`：逐节拍资产映射及缺项。',
              '- `assets_src/ending/manifest.json`：尺寸、字节、SHA-256、alpha及引用关系。',
              '- `docs/art/ending/prompts/`：逐图提示词。',
              '- 三张带人物背景初稿留在 `trials/`，不计入完成数。', '',
              '全部为生成试稿；完成画面覆盖不等于已完成游戏接入、声音演出、逐像素差分配准和正式美术验收。', '',
              '完成后请将原图、提示词、画廊、清单和统计上传到GitHub。']
    (ROOT/'docs/art/ending/全量绘图任务单.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    css='body{background:#101829;color:#e7ecf7;font:16px system-ui;margin:0;padding:28px}main{max-width:1500px;margin:auto;display:grid;grid-template-columns:repeat(auto-fit,minmax(420px,1fr));gap:24px}article{background:#1e2b42;padding:15px;border-radius:12px}h1{max-width:1500px;margin:0 auto 24px}h2{font-size:17px}.frame{position:relative;aspect-ratio:16/9;overflow:hidden;background:#29374a}.bg{width:100%;height:100%;object-fit:cover}.sprite{position:absolute;height:95%;right:8%;bottom:0;max-width:60%;object-fit:contain}.prop{position:absolute;width:40%;height:60%;left:10%;top:20%;object-fit:contain}small{display:block;overflow-wrap:anywhere;color:#aebbd2}'
    (PACK/'scenes.html').write_text('<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>终章全分景预览</title><style>'+css+'</style><h1>终章 · 7分景 / '+str(data['covered_beats'])+'/34节拍已覆盖</h1><main>'+''.join(cards)+'</main></html>',encoding='utf-8')
    print(json.dumps({k:v for k,v in data.items() if k!='beats'},ensure_ascii=False))

if __name__=='__main__':
    main()
