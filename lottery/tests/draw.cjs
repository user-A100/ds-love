const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
async function check(writeFails) {
  const elements = new Map();
  function element() { return {textContent:'', disabled:false, children:[], handlers:{}, classList:{add(){},remove(){}}, setAttribute(){}, append(...x){this.children.push(...x)}, replaceChildren(...x){this.children=x}, addEventListener(k,f){this.handlers[k]=f}, showModal(){}, close(){}}; }
  let saved = null;
  const document = {getElementById(id){if(!elements.has(id))elements.set(id,element());return elements.get(id)}, createElement:element, addEventListener(){}};
  vm.runInNewContext(fs.readFileSync(require('node:path').join(__dirname,'../app.js'),'utf8'), {
    document, window:{addEventListener(){}}, navigator:{}, crypto:require('node:crypto').webcrypto,
    localStorage:{getItem(){return saved},setItem(k,v){if(writeFails)throw Error('quota');saved=v}},
    setTimeout(fn){fn()}, Date, Blob, URL
  });
  const seen = new Set();
  for(let i=0;i<100;i++) {
    const pending = elements.get('draw').handlers.click();
    assert(elements.get('draw').disabled, 'button locks immediately during animation');
    await elements.get('draw').handlers.click();
    await pending;
    const number = Number(elements.get('number').textContent);
    assert(number>=1 && number<=100);
    assert(!seen.has(number)); seen.add(number);
    assert.equal(Number(elements.get('remaining').textContent),99-i);
  }
  assert(elements.get('draw').disabled);
  await elements.get('draw').handlers.click();
  assert.equal(Number(elements.get('count').textContent),100);
  await elements.get('confirm-reset').handlers.click();
  assert.equal(Number(elements.get('remaining').textContent),100);
}
(async()=>{await check(false);await check(true);console.log('PASS: 100 unique draws, exhaustion and reset; persistent and storage-denied modes');})().catch(e=>{console.error(e);process.exitCode=1});
