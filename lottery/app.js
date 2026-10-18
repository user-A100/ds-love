(() => {
  'use strict';
  const KEY = 'whalegal-lottery-v1';
  const $ = id => document.getElementById(id);
  let records = [], busy = false, storageAvailable = true;
  function load() {
    try {
      const data = JSON.parse(localStorage.getItem(KEY) || '[]');
      if (!Array.isArray(data) || data.length > 100 || data.some(r => !r || !Number.isInteger(r.number) || r.number < 1 || r.number > 100 || !Number.isFinite(r.time)) || new Set(data.map(r => r.number)).size !== data.length) throw new Error('invalid');
      records = data;
    } catch { storageAvailable = false; }
  }
  function save() {
    try { localStorage.setItem(KEY, JSON.stringify(records)); } catch { storageAvailable = false; }
  }
  function remaining() {
    const used = new Set(records.map(r => r.number));
    return Array.from({length:100}, (_, i) => i + 1).filter(n => !used.has(n));
  }
  // Rejection sampling avoids modulo bias, including when the pool shrinks.
  function randomIndex(length) {
    const limit = Math.floor(4294967296 / length) * length;
    const value = new Uint32Array(1);
    do { crypto.getRandomValues(value); } while (value[0] >= limit);
    return value[0] % length;
  }
  function render() {
    const used = new Set(records.map(r => r.number));
    const last = records.at(-1);
    $('remaining').textContent = 100 - records.length;
    $('count').textContent = records.length;
    $('progress').value = 100 - records.length;
    $('number').textContent = last ? last.number : '?';
    $('ticket-foot').textContent = last ? `第 ${records.length} 次相遇 · 已移出奖池` : '轻轻一点，让心意抵达';
    $('grid').replaceChildren(...Array.from({length:100}, (_, i) => {
      const n = i + 1, cell = document.createElement('span');
      cell.className = 'cell' + (used.has(n) ? ' drawn' : '') + (last?.number === n ? ' latest' : '');
      cell.textContent = n;
      cell.setAttribute('aria-label', `${n} 号，${used.has(n) ? '已抽出' : '待抽取'}`);
      return cell;
    }));
    $('history').replaceChildren(...records.slice().reverse().map((r, i) => {
      const li = document.createElement('li');
      const label = document.createElement('span');
      label.textContent = `第 ${records.length - i} 签`;
      const number = document.createElement('b'); number.textContent = `${r.number} 号`;
      const time = document.createElement('time'); time.textContent = new Date(r.time).toLocaleTimeString('zh-CN', {hour12:false});
      li.append(label, number, time); return li;
    }));
    if (!records.length) { const li = document.createElement('li'); li.className = 'empty'; li.textContent = '还没有抽签记录，幸运即将登场。'; $('history').append(li); }
    $('draw').disabled = busy || records.length === 100;
    $('draw').textContent = records.length === 100 ? '本轮幸运已全部送达' : '抽一张幸运签 ✧';
    $('export').disabled = !records.length || busy;
    $('reset').disabled = busy;
    $('save-state').textContent = storageAvailable ? '进度自动保存在当前浏览器' : '无法保存进度，请在关闭前导出记录';
  }
  async function draw() {
    if (busy) return;
    busy = true;
    render();
    const action = () => {
      if (storageAvailable) load();
      const pool = remaining();
      if (!pool.length) return null;
      const record = {number:pool[randomIndex(pool.length)], time:Date.now()};
      records.push(record); save(); return record;
    };
    try {
      const candidates = remaining();
      if (candidates.length && !window.matchMedia?.('(prefers-reduced-motion: reduce)').matches) {
        $('ticket').classList.remove('revealed');
        $('ticket').classList.add('drawing');
        $('ticket').setAttribute('aria-busy', 'true');
        $('draw').textContent = '幸运签正在揭晓…';
        $('message').textContent = '心意流转中，等待你的幸运号码…';
        $('ticket-foot').textContent = '幸运即将抵达';
        // 展示号码不消耗奖池；动画结束后才在锁内抽取并保存真正的结果。
        for (let frame = 0; frame < 22; frame++) {
          $('number').textContent = candidates[randomIndex(candidates.length)];
          await new Promise(resolve => setTimeout(resolve, 35 + 160 * (frame / 21) ** 3));
        }
      }
      $('ticket').classList.remove('drawing');
      $('ticket').setAttribute('aria-busy', 'false');
      const result = navigator.locks ? await navigator.locks.request(KEY, action) : action();
      render();
      if (!result) { $('message').textContent = '100 张签已抽完，重置奖池即可开始新一轮。'; return; }
      $('message').textContent = `幸运抵达！抽中 ${result.number} 号，剩余 ${100-records.length} 张。`;
      $('ticket').classList.remove('revealed');
      void $('ticket').offsetWidth;
      $('ticket').classList.add('revealed');
      await new Promise(resolve => setTimeout(resolve, 500));
    } catch { $('message').textContent = '抽签未完成，请使用支持安全随机数的现代浏览器重试。'; }
    finally {
      $('ticket').classList.remove('drawing');
      $('ticket').setAttribute('aria-busy', 'false');
      busy = false; render();
    }
  }
  $('draw').addEventListener('click', draw);
  $('reset').addEventListener('click', () => $('confirm').showModal());
  $('cancel').addEventListener('click', () => $('confirm').close());
  $('confirm-reset').addEventListener('click', async () => {
    const reset = () => { records = []; save(); };
    if (navigator.locks) await navigator.locks.request(KEY, reset); else reset();
    $('confirm').close(); render(); $('message').textContent = '新一轮已开始，100 张幸运签全部就位。';
  });
  $('export').addEventListener('click', () => {
    const csv = '\ufeff抽取顺序,编号,时间\r\n' + records.map((r,i) => `${i+1},${r.number},${new Date(r.time).toISOString()}`).join('\r\n');
    const url = URL.createObjectURL(new Blob([csv], {type:'text/csv;charset=utf-8'}));
    const link = document.createElement('a'); link.href = url; link.download = '幸运抽签记录.csv'; link.click(); setTimeout(() => URL.revokeObjectURL(url), 1000);
  });
  $('fullscreen').addEventListener('click', async () => {
    try { if (document.fullscreenElement) await document.exitFullscreen(); else await document.documentElement.requestFullscreen(); }
    catch { $('message').textContent = '浏览器未开启全屏，可按 F11 展示。'; }
  });
  document.addEventListener('fullscreenchange', () => { $('fullscreen').textContent = document.fullscreenElement ? '退出全屏' : '全屏展示'; });
  window.addEventListener('storage', e => { if (e.key === KEY) { load(); render(); $('message').textContent = '奖池进度已同步。'; } });
  load(); render();
  if (records.length) $('message').textContent = `已恢复本轮进度：抽出 ${records.length} 张，剩余 ${100-records.length} 张。`;
})();

