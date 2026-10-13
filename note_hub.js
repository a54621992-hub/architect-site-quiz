// 敷地速刷 外掛：筆記單元主目錄（2026-10-13 私人電腦 Claude Code，使用者裁定 2a）
// 掛法：index.html 的 </body> 前加 <script src="note_hub.js"></script>（放在 reading_lib.js 之後）
// 積木規範：整支包在 IIFE 內、事件皆 try/catch、只讀 SITE_DATA，不改主程式任何函式。
// 每個筆記單元固定 5 個頁籤：讀背 → 臨摹 → 對應六格 → 數字卡 → 真題範卷；對照表在 build_site_data.py 的 NOTE_UNITS。
(function () {
  'use strict';

  function D() { return (typeof SITE_DATA !== 'undefined' && SITE_DATA) ? SITE_DATA : {}; }
  function arr(v) { return Array.isArray(v) ? v : []; }
  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  var TABS = [['read', '📖 讀背'], ['trace', '✏️ 臨摹'], ['grid', '🧩 六格'], ['num', '🔢 數字'], ['exam', '📝 真題']];
  var ON = 'bg-indigo-500 text-white';
  var OFF = 'bg-slate-800 text-slate-300';

  function pagesOf(u) { return arr(D().reading_cards).filter(function (r) { return u.reading.indexOf(r.unit) >= 0; }); }
  function tracesOf(u) {
    var all = arr(D().tracing_cards).concat(arr(D().reading_cards));
    return u.tracing.map(function (n) {
      return all.filter(function (c) { return c.source_page === 'P' + n; })[0];
    }).filter(Boolean);
  }
  function topicsOf(u) { return arr(D().topics).filter(function (t) { return u.topics.indexOf(t.id) >= 0; }); }
  function numsOf(u) { return arr(D().numbers).filter(function (n) { return u.nums.indexOf(n.category) >= 0; }); }
  function cardsOf(u) {
    var all = arr(D().strategy_cards);
    return u.cards.map(function (id) { return all.filter(function (c) { return c.id === id; })[0]; }).filter(Boolean);
  }
  function scrollsOf(u) {
    var all = arr(D().exam_scrolls);
    return u.scrolls.map(function (id) { return all.filter(function (c) { return c.id === id; })[0]; }).filter(Boolean);
  }
  function counts(u) {
    return { read: pagesOf(u).reduce(function (n, p) { return n + p.items.length; }, 0), trace: tracesOf(u).length,
      grid: topicsOf(u).length, num: numsOf(u).length, exam: cardsOf(u).length + scrollsOf(u).length };
  }

  function btn(attrs, cls, html) { return '<button ' + attrs + ' class="' + cls + '">' + html + '</button>'; }

  function renderList(modal, units) {
    modal.querySelector('[data-nh-title]').textContent = '筆記單元';
    modal.querySelector('[data-nh-back]').classList.add('invisible');
    modal.querySelector('[data-nh-tabs]').innerHTML = '';
    modal.querySelector('[data-nh-body]').innerHTML =
      '<p class="text-xs text-slate-400 leading-relaxed">以手繪筆記為主軸：先讀背、再臨摹，最後對照六格、數字卡與真題。標「補充」者為筆記沒有、知識庫整理的高頻考點。</p>' +
      units.map(function (u, i) {
        var c = counts(u);
        var meta = [c.read ? c.read + ' 題讀背' : '', c.trace ? c.trace + ' 頁臨摹' : '', c.grid ? c.grid + ' 組六格' : '',
          c.num ? c.num + ' 張數字' : '', c.exam ? c.exam + ' 題真題' : ''].filter(Boolean).join('・');
        return btn('data-nh-unit="' + i + '"',
          'w-full text-left p-4 rounded-2xl border ' + (u.supplement ? 'border-amber-800/60 bg-amber-950/20' : 'border-slate-800 bg-slate-950/70') + ' active:scale-[0.98] transition',
          '<div class="flex items-center justify-between gap-2"><span class="text-base font-black text-white">' +
            (u.supplement ? '<span class="text-xs px-1.5 py-0.5 mr-1 rounded bg-amber-500/20 text-amber-300">補充</span>' : (i + 1) + '. ') + esc(u.name.replace(/^補充：/, '')) +
          '</span><span class="text-slate-500 text-lg">›</span></div>' +
          '<div class="text-xs text-slate-400 mt-1">' + esc(meta || '—') + '</div>');
      }).join('');
    modal.removeAttribute('data-nh-cur');
  }

  function renderUnit(modal, units, ui, tab) {
    var u = units[ui];
    var c = counts(u);
    modal.setAttribute('data-nh-cur', String(ui));
    modal.querySelector('[data-nh-title]').textContent = u.name;
    modal.querySelector('[data-nh-back]').classList.remove('invisible');
    modal.querySelector('[data-nh-tabs]').innerHTML = TABS.map(function (t) {
      return btn('data-nh-tab="' + t[0] + '"', 'shrink-0 px-3 min-h-[40px] rounded-xl text-sm font-bold whitespace-nowrap ' + (t[0] === tab ? ON : OFF),
        t[1] + ' <span class="opacity-70">' + c[t[0]] + '</span>');
    }).join('');
    var body = modal.querySelector('[data-nh-body]');
    body.innerHTML = ({ read: viewRead, trace: viewTrace, grid: viewGrid, num: viewNum, exam: viewExam })[tab](u);
    body.scrollTop = 0;
  }

  function empty(msg) { return '<p class="text-sm text-slate-500 py-6 text-center">' + esc(msg) + '</p>'; }

  function viewRead(u) {
    var ps = pagesOf(u);
    if (!ps.length) return empty('這個單元是知識庫補充，筆記沒有對應頁；請看六格與數字卡。');
    return btn('data-nh-read=""', 'w-full min-h-[48px] rounded-2xl bg-sky-600 text-white text-sm font-black', '▶ 從第一頁開始讀背（' + ps.length + ' 頁）') +
      ps.map(function (p) {
        return btn('data-nh-read="' + esc(p.source_page.slice(1)) + '"', 'w-full text-left p-3 rounded-2xl border border-slate-800 bg-slate-950/70',
          '<div class="text-xs text-sky-300">' + esc(p.source_page) + '・' + p.items.length + ' 題</div>' +
          '<div class="text-sm font-bold text-white">' + esc(p.title) + '</div>');
      }).join('');
  }

  function viewTrace(u) {
    var ts = tracesOf(u);
    if (!ts.length) return empty('這個單元沒有指定臨摹頁；全部 7 類在首頁「手繪臨摹庫」。');
    return '<div class="grid grid-cols-2 gap-2">' + ts.map(function (t) {
      return btn('data-nh-img="' + esc(t.image) + '" data-nh-cap="' + esc(t.title + '（' + t.source_page + '）') + '"', 'text-left rounded-2xl border border-slate-800 bg-slate-950/70 overflow-hidden',
        '<img src="' + esc(t.image) + '" loading="lazy" alt="" class="w-full h-32 object-cover bg-white">' +
        '<div class="p-2"><div class="text-xs text-violet-300">' + esc(t.source_page) + '</div><div class="text-sm font-bold text-white leading-snug">' + esc(t.title) + '</div></div>');
    }).join('') + '</div>';
  }

  function viewGrid(u) {
    var ts = topicsOf(u);
    if (!ts.length) return empty('筆記這個單元沒有對應的六格申論題。');
    return ts.map(function (t) {
      return '<details class="rounded-2xl border border-slate-800 bg-slate-950/70 p-3" open><summary class="text-sm font-black text-white cursor-pointer">' + esc(t.header) + '</summary>' +
        (t.intro ? '<p class="text-xs text-slate-400 mt-2">' + esc(t.intro) + '</p>' : '') +
        arr(t.grids).map(function (g) {
          return '<div class="mt-2 p-2.5 rounded-xl bg-slate-900 border border-slate-800">' +
            '<div class="text-sm font-bold text-indigo-300">' + g.grid_no + '｜' + esc(g.func_abbr) + '｜' + esc(g.title) + '</div>' +
            '<div class="text-sm text-slate-200 mt-1">' + esc(g.keywords) + '</div>' +
            '<div class="text-xs text-emerald-300 mt-1">' + esc(g.number) + '</div>' +
            '<div class="text-xs text-slate-400">✏️ ' + esc(g.diagram) + '</div></div>';
        }).join('') + '</details>';
    }).join('');
  }

  function viewNum(u) {
    var ns = numsOf(u);
    if (!ns.length) return empty('這個單元沒有對應的數字卡。');
    return ns.map(function (n) {
      return '<div class="p-3 rounded-2xl border border-slate-800 bg-slate-950/70">' +
        '<div class="flex justify-between gap-2"><span class="text-base font-black text-emerald-300">' + esc(n.number) + '</span><span class="text-xs text-slate-500 shrink-0">' + esc(n.status) + '</span></div>' +
        '<div class="text-sm text-slate-100 mt-1">' + esc(n.content) + '</div>' +
        '<div class="text-xs text-slate-400 mt-1">' + esc(n.usage) + '</div>' +
        '<div class="text-xs text-slate-500 mt-1">出處：' + esc(n.source) + '</div></div>';
    }).join('');
  }

  function viewExam(u) {
    var cs = cardsOf(u), ss = scrollsOf(u);
    if (!cs.length && !ss.length) return empty('這個單元沒有對應的真題或範卷。');
    return ss.map(function (s) {
      return btn('data-nh-scroll="' + esc(s.id) + '"', 'w-full text-left p-3 rounded-2xl border border-amber-800/50 bg-amber-950/20',
        '<div class="text-xs text-amber-300">' + esc(s.year) + '</div><div class="text-sm font-bold text-white">📜 ' + esc(s.title) + '</div>');
    }).join('') + cs.map(function (c) {
      return '<div class="p-3 rounded-2xl border border-slate-800 bg-slate-950/70 space-y-1.5">' +
        '<div class="text-xs text-cyan-300">' + esc(c.year) + '</div><div class="text-sm font-black text-white">' + esc(c.title) + '</div>' +
        '<div class="text-xs text-slate-400">' + esc(c.theme) + '</div>' +
        arr(c.challenges).map(function (q) { return '<div class="text-sm text-slate-200">・' + esc(q) + '</div>'; }).join('') +
        btn('data-nh-card="' + esc(c.id) + '"', 'mt-1 px-3 min-h-[40px] rounded-xl bg-slate-800 text-cyan-300 text-sm font-bold', '🔪 到審題快刀看全文') + '</div>';
    }).join('');
  }

  // 跳到審題快刀的指定題（呼叫主程式的全域函式；找不到就只切畫面）
  function gotoCard(id) {
    var card = arr(D().strategy_cards).filter(function (c) { return c.id === id; })[0];
    if (!card) return;
    if (typeof filterStrategyCategory === 'function') filterStrategyCategory(card.category === 'past' ? 'past' : 'mock');
    if (typeof switchView === 'function') switchView('strategy');
    if (typeof getFilteredStrategyCards === 'function' && typeof appState !== 'undefined') {
      var i = getFilteredStrategyCards().map(function (c) { return c.id; }).indexOf(id);
      if (i >= 0) { appState.strategyIndex = i; if (typeof renderStrategyPager === 'function') renderStrategyPager(); }
    }
  }

  function gotoScroll(id) {
    var i = arr(D().exam_scrolls).map(function (s) { return s.id; }).indexOf(id);
    if (typeof openScrollsModal === 'function') openScrollsModal();
    if (i >= 0 && typeof switchScrollYear === 'function') switchScrollYear(i);
  }

  function buildModal(units) {
    var modal = document.createElement('div');
    modal.id = 'note-hub-modal';
    modal.className = 'fixed inset-0 z-50 bg-slate-950 flex flex-col hidden';
    modal.innerHTML =
      '<div class="max-w-xl w-full mx-auto flex flex-col h-full">' +
        '<div class="flex items-center gap-2 px-3 py-2 border-b border-slate-800 shrink-0">' +
          btn('data-nh-back', 'invisible shrink-0 w-11 h-11 rounded-full bg-slate-800 text-slate-200 text-lg', '‹') +
          '<h3 data-nh-title class="flex-1 text-base font-black text-white truncate">筆記單元</h3>' +
          btn('data-nh-close', 'shrink-0 w-11 h-11 rounded-full bg-slate-800 text-slate-300', '✕') +
        '</div>' +
        '<div data-nh-tabs class="flex gap-2 overflow-x-auto no-scrollbar px-3 pt-2 shrink-0"></div>' +
        '<div data-nh-body class="flex-1 overflow-y-auto px-3 py-3 space-y-2.5"></div>' +
      '</div>';

    modal.addEventListener('click', function (ev) {
      try {
        var t = ev.target;
        if (t.closest('[data-nh-close]')) { modal.classList.add('hidden'); return; }
        if (t.closest('[data-nh-back]')) { renderList(modal, units); return; }
        var ui = Number(modal.getAttribute('data-nh-cur'));
        var el;
        if ((el = t.closest('[data-nh-unit]'))) { renderUnit(modal, units, Number(el.getAttribute('data-nh-unit')), 'read'); return; }
        if ((el = t.closest('[data-nh-tab]'))) { renderUnit(modal, units, ui, el.getAttribute('data-nh-tab')); return; }
        if ((el = t.closest('[data-nh-read]'))) {
          if (typeof window.openReadingUnit === 'function') window.openReadingUnit(units[ui].reading, Number(el.getAttribute('data-nh-read')) || 0);
          return;
        }
        if ((el = t.closest('[data-nh-img]'))) {
          if (typeof window.openImageLightbox === 'function') window.openImageLightbox(el.getAttribute('data-nh-img'), el.getAttribute('data-nh-cap'));
          return;
        }
        if ((el = t.closest('[data-nh-card]'))) { modal.classList.add('hidden'); gotoCard(el.getAttribute('data-nh-card')); return; }
        if ((el = t.closest('[data-nh-scroll]'))) { modal.classList.add('hidden'); gotoScroll(el.getAttribute('data-nh-scroll')); return; }
      } catch (e) { console.warn('[筆記單元] 點擊處理失敗', e); }
    });

    // 插在讀背彈窗之前：同為 z-50 時 DOM 在後者疊在上面，讀背與燈箱才會蓋在本頁之上
    var after = document.getElementById('reading-modal') || document.getElementById('diagram-lightbox');
    if (after && after.parentNode) after.parentNode.insertBefore(modal, after);
    else document.body.appendChild(modal);
    renderList(modal, units);
    return modal;
  }

  function buildEntryCard(modal, units) {
    var home = document.getElementById('view-capsule');
    if (!home) return;
    var total = units.reduce(function (n, u) { return n + counts(u).read; }, 0);
    var card = document.createElement('button');
    card.className = 'w-full text-left p-4 rounded-3xl border border-indigo-700/60 bg-gradient-to-br from-indigo-950/60 to-slate-900 active:scale-[0.98] transition space-y-1';
    card.innerHTML =
      '<div class="flex items-center justify-between"><span class="text-base font-black text-white">📚 筆記單元（主目錄）</span><span class="text-indigo-300 text-xl">›</span></div>' +
      '<div class="text-sm text-slate-300">' + units.length + ' 個單元・' + total + ' 題讀背；每單元：讀背→臨摹→六格→數字→真題</div>';
    card.addEventListener('click', function () { try { renderList(modal, units); modal.classList.remove('hidden'); } catch (e) { console.warn('[筆記單元] 開啟失敗', e); } });
    home.insertBefore(card, home.firstChild);
  }

  function init() {
    try {
      var units = arr(D().note_units);
      if (!units.length || document.getElementById('note-hub-modal')) return;
      var modal = buildModal(units);
      buildEntryCard(modal, units);
      window.openNoteHub = function () { renderList(modal, units); modal.classList.remove('hidden'); };
    } catch (e) { console.warn('[筆記單元] 初始化失敗', e); }
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
