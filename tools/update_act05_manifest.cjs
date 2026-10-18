// Index and validate original imagegen PNGs; never modify image pixels.
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const zlib = require('zlib');
const root = path.resolve(__dirname, '..');
const pack = path.join(root, 'assets_src/act05');
const plan = JSON.parse(fs.readFileSync(path.join(root, 'docs/art/act05/production-plan.json'), 'utf8'));
const assets = [], pending = [];
function pngInfo(b) {
  if (b.subarray(0,8).toString('hex') !== '89504e470d0a1a0a') throw Error('Not PNG');
  const w=b.readUInt32BE(16),h=b.readUInt32BE(20),depth=b[24],type=b[25];
  if(depth!==8 || ![2,6].includes(type) || b[28]!==0) throw Error('Unsupported PNG encoding');
  let chunks=[], off=8;
  while(off<b.length){const n=b.readUInt32BE(off),t=b.toString('ascii',off+4,off+8);if(t==='IDAT')chunks.push(b.subarray(off+8,off+8+n));off+=n+12;}
  const raw=zlib.inflateSync(Buffer.concat(chunks)),channels=type===6?4:3,stride=w*channels;
  let prev=Buffer.alloc(stride),pos=0,min=255,max=0,edge=0;
  const paeth=(a,b,c)=>{const p=a+b-c,pa=Math.abs(p-a),pb=Math.abs(p-b),pc=Math.abs(p-c);return pa<=pb&&pa<=pc?a:pb<=pc?b:c;};
  for(let y=0;y<h;y++){const filter=raw[pos++],row=Buffer.from(raw.subarray(pos,pos+stride));pos+=stride;
    for(let x=0;x<stride;x++){const a=x>=channels?row[x-channels]:0,b=prev[x],c=x>=channels?prev[x-channels]:0;row[x]=(row[x]+(filter===0?0:filter===1?a:filter===2?b:filter===3?Math.floor((a+b)/2):paeth(a,b,c)))&255;}
    for(let x=0;x<w;x++){const a=type===6?row[x*channels+3]:255;min=Math.min(min,a);max=Math.max(max,a);if(y===0||y===h-1||x===0||x===w-1)edge=Math.max(edge,a);}prev=row;
  }
  return {width:w,height:h,alpha_range:[min,max],edge_alpha_max:edge};
}
for(const job of plan.jobs){const file=path.join(pack,job.file);if(!fs.existsSync(file)){pending.push(job.id);continue;}
  const prompt='docs/art/act05/prompts/'+job.id+'.txt';if(!fs.existsSync(path.join(root,prompt)))throw Error('Missing prompt '+job.id);
  for(const ref of job.refs||[])if(!fs.existsSync(path.join(root,ref)))throw Error('Missing reference '+ref);
  const b=fs.readFileSync(file),info=pngInfo(b);if(job.transparent&&info.alpha_range[0]!==0)throw Error('Missing alpha '+job.id);
  assets.push({...job,path:'assets_src/act05/'+job.file,prompt,...info,bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex'),tool:'built-in imagegen',status:'generated_draft'});
}
fs.mkdirSync(pack,{recursive:true});
const status=pending.length?'generating':'complete_planned_draft_pack';
fs.writeFileSync(path.join(pack,'manifest.json'),JSON.stringify({schema_version:1,updated_at:new Date().toISOString(),status,scope:plan.scope,planned_assets:plan.jobs.length,pending_assets:pending,assets},null,2)+'\n');
fs.writeFileSync(path.join(pack,'LIVE_STATUS.md'),'# 第五幕美术制作状态\n\n已保存并校验 '+assets.length+' / '+plan.jobs.length+' 项。\n\n'+assets.map(a=>'- '+a.scene+' · ['+a.label+']('+a.file+')').join('\n')+'\n\n待生成：'+(pending.join('、')||'无')+'\n\n原始 PNG 未修改；透明素材验证真实 alpha。当前为生成试制包，尚未接入 Ren’Py，表情差分未逐像素配准。角色原型来源与署名见 ../characters/README.md。\n');
console.log(JSON.stringify({completed:assets.length,planned:plan.jobs.length,pending}));
