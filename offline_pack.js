// 敷地速刷 外掛：離線圖片包（2026-10-13 私人電腦 Claude Code）
// 掛法：index.html 的 </body> 前加一行 <script src="offline_pack.js"></script>（放在 reading_lib.js 之後）
// 積木規範：整支包在 IIFE 內、事件皆 try/catch、只讀 SITE_DATA，不改主程式任何函式。
// 圖片存進獨立快取 site-planning-img：sw.js 換版時不刪它，改版不必重下載。
(function () {
  'use strict';

  var IMG_CACHE = 'site-planning-img';
  var IMG_RE = /\.(webp|png|jpe?g|svg)$/i;

  // 走遍 SITE_DATA，收集所有相對路徑的圖片
  function collectImages() {
    var found = {};
    (function walk(v) {
      if (typeof v === 'string') {
        if (IMG_RE.test(v) && !/^(https?:|data:)/.test(v)) found[v] = 1;
      } else if (v && typeof v === 'object') {
        for (var k in v) if (Object.prototype.hasOwnProperty.call(v, k)) walk(v[k]);
      }
    })(typeof SITE_DATA !== 'undefined' ? SITE_DATA : null);
    return Object.keys(found);
  }

  function setStatus(card, text) {
    var el = card.querySelector('[data-op-status]');
    if (el) el.textContent = text;
  }

  function countCached(cache, list) {
    return Promise.all(list.map(function (u) { return cache.match(u).then(function (r) { return r ? 1 : 0; }); }))
      .then(function (a) { return a.reduce(function (n, x) { return n + x; }, 0); });
  }

  function refresh(card, list) {
    if (!('caches' in window)) { setStatus(card, '此瀏覽器不支援離線快取'); return; }
    caches.open(IMG_CACHE).then(function (cache) { return countCached(cache, list); })
      .then(function (n) {
        setStatus(card, n >= list.length ? '✅ 已全部離線（' + n + ' 張）' : '已離線 ' + n + '／' + list.length + ' 張，點此下載其餘');
      }).catch(function (e) { console.warn('[離線包] 檢查失敗', e); });
  }

  function download(card, list) {
    if (card.getAttribute('data-op-busy') === '1') return;
    card.setAttribute('data-op-busy', '1');
    var done = 0, fail = 0, bytes = 0, idx = 0;
    caches.open(IMG_CACHE).then(function (cache) {
      function worker() {
        if (idx >= list.length) return Promise.resolve();
        var url = list[idx++];
        return cache.match(url).then(function (hit) {
          if (hit) return;
          return fetch(url, { cache: 'reload' }).then(function (res) {
            if (!res.ok) throw new Error(res.status);
            return res.clone().blob().then(function (b) { bytes += b.size; return cache.put(url, res); });
          });
        }).catch(function () { fail++; })
          .then(function () {
            done++;
            setStatus(card, '下載中 ' + done + '／' + list.length + '（' + (bytes / 1048576).toFixed(1) + ' MB）');
            return worker();
          });
      }
      return Promise.all([worker(), worker(), worker(), worker()]);
    }).then(function () {
      card.setAttribute('data-op-busy', '0');
      if (fail) setStatus(card, '完成，但 ' + fail + ' 張失敗，請連網後再點一次');
      else refresh(card, list);
    }).catch(function (e) {
      card.setAttribute('data-op-busy', '0');
      setStatus(card, '下載失敗：' + e);
    });
  }

  function init() {
    try {
      var list = collectImages();
      if (!list.length || document.getElementById('offline-pack-card')) return;
      var anchor = document.querySelector('[data-tr-entry]') || document.querySelector('[onclick="openScrollsModal()"]');
      if (!anchor || !anchor.parentNode) return;
      var card = document.createElement('div');
      card.id = 'offline-pack-card';
      card.className = 'bg-slate-900/90 p-4 rounded-2xl border border-emerald-800/50 active:scale-95 transition cursor-pointer space-y-2 bg-gradient-to-br from-emerald-950/30 to-slate-900';
      card.innerHTML =
        '<div class="flex justify-between items-center"><div class="text-2xl">📥</div>' +
        '<span class="text-[10px] px-1.5 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 font-bold border border-emerald-500/30">約 55 MB</span></div>' +
        '<div class="text-sm font-bold text-white">離線圖片包</div>' +
        '<div data-op-status class="text-[11px] text-slate-400">建議 Wi-Fi 下載，' + list.length + ' 張圖存進手機</div>';
      card.addEventListener('click', function () {
        try { download(card, list); } catch (e) { console.warn('[離線包] 下載失敗', e); }
      });
      anchor.parentNode.appendChild(card);
      refresh(card, list);
    } catch (e) { console.warn('[離線包] 初始化失敗', e); }
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
