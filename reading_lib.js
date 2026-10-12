// 敷地速刷 外掛：筆記讀背卡（2026-10-12 私人電腦 Claude Code）
// 掛法：index.html 的 </body> 前加一行 <script src="reading_lib.js"></script>（放在 tracing_lib.js 之後）
// 積木規範：整支包在 IIFE 內、事件皆 try/catch、只讀 SITE_DATA.reading_cards，不改主程式任何函式。
(function () {
  'use strict';

  function getPages() {
    try {
      return (typeof SITE_DATA !== 'undefined' && Array.isArray(SITE_DATA.reading_cards)) ? SITE_DATA.reading_cards : [];
    } catch (e) { return []; }
  }

  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  var TAB_ON = 'bg-sky-500 text-slate-950';
  var TAB_OFF = 'bg-slate-800 text-slate-300';
  var HIDDEN_TEXT = '👆 點一下顯示答案';

  function renderPage(modal, pages, idx) {
    var p = pages[idx];
    modal.querySelectorAll('[data-rd-tab]').forEach(function (btn) {
      var on = Number(btn.getAttribute('data-rd-tab')) === idx;
      (on ? TAB_OFF : TAB_ON).split(' ').forEach(function (k) { btn.classList.remove(k); });
      (on ? TAB_ON : TAB_OFF).split(' ').forEach(function (k) { btn.classList.add(k); });
    });
    modal.querySelector('[data-rd-body]').innerHTML =
      '<div class="flex items-center justify-between gap-2">' +
        '<div><div class="text-[10px] text-sky-300">' + esc(p.unit) + '・' + esc(p.source_page) + '</div>' +
        '<h4 class="text-sm font-black text-white">' + esc(p.title) + '</h4></div>' +
        '<button data-rd-src class="text-[11px] px-2 py-1 rounded-lg bg-slate-800 text-cyan-300 whitespace-nowrap">📄 看原頁</button>' +
      '</div>' +
      '<div class="flex gap-2">' +
        '<button data-rd-all="1" class="flex-1 text-[11px] py-1.5 rounded-lg bg-slate-800 text-slate-300">全部顯示</button>' +
        '<button data-rd-all="0" class="flex-1 text-[11px] py-1.5 rounded-lg bg-slate-800 text-slate-300">全部遮住</button>' +
      '</div>' +
      p.items.map(function (it, i) {
        return '<div data-rd-item="' + i + '" class="bg-slate-950/80 p-3 rounded-2xl border border-slate-800 space-y-2 cursor-pointer">' +
          '<div class="text-xs font-bold text-white">Q' + (i + 1) + '．' + esc(it.q) + '</div>' +
          '<div data-rd-ans class="text-xs text-slate-500 whitespace-pre-line leading-relaxed bg-slate-900/70 p-2.5 rounded-xl border border-slate-800/60">' + HIDDEN_TEXT + '</div>' +
        '</div>';
      }).join('');
    modal.setAttribute('data-rd-cur', String(idx));
  }

  function setAnswer(modal, pages, itemEl, show) {
    var p = pages[Number(modal.getAttribute('data-rd-cur'))];
    var it = p.items[Number(itemEl.getAttribute('data-rd-item'))];
    var ans = itemEl.querySelector('[data-rd-ans]');
    ans.textContent = show ? it.a : HIDDEN_TEXT;
    ans.classList.toggle('text-slate-100', show);
    ans.classList.toggle('text-slate-500', !show);
    itemEl.setAttribute('data-rd-open', show ? '1' : '0');
  }

  function buildModal(pages) {
    var modal = document.createElement('div');
    modal.id = 'reading-modal';
    modal.className = 'fixed inset-0 z-50 bg-slate-950/90 backdrop-blur-md flex items-center justify-center p-3 hidden';
    modal.innerHTML =
      '<div class="bg-slate-900 border border-slate-700 rounded-3xl max-w-xl w-full p-5 space-y-3 shadow-2xl relative max-h-[92vh] flex flex-col">' +
        '<div class="flex justify-between items-center border-b border-slate-800 pb-3 shrink-0">' +
          '<div class="flex items-center space-x-2"><span class="text-xl">📖</span><div>' +
            '<h3 class="text-base font-black text-white">筆記讀背</h3>' +
            '<p class="text-[11px] text-sky-300">名師筆記文字轉錄，先想答案再點開（〔?〕＝原稿字跡不確定）</p>' +
          '</div></div>' +
          '<button data-rd-close class="w-8 h-8 rounded-full bg-slate-800 text-slate-400 hover:text-white flex items-center justify-center text-xs">✕</button>' +
        '</div>' +
        '<div class="flex space-x-2 overflow-x-auto no-scrollbar shrink-0 pb-1">' +
          pages.map(function (p, i) {
            return '<button data-rd-tab="' + i + '" class="px-3 py-1.5 rounded-xl text-xs font-bold whitespace-nowrap transition ' + TAB_OFF + '">' + esc(p.source_page) + '</button>';
          }).join('') +
        '</div>' +
        '<div data-rd-body class="overflow-y-auto pr-1 flex-1 space-y-3"></div>' +
      '</div>';

    modal.addEventListener('click', function (ev) {
      try {
        if (ev.target === modal || ev.target.closest('[data-rd-close]')) { modal.classList.add('hidden'); return; }
        var tab = ev.target.closest('[data-rd-tab]');
        if (tab) { renderPage(modal, pages, Number(tab.getAttribute('data-rd-tab'))); return; }
        var all = ev.target.closest('[data-rd-all]');
        if (all) {
          var show = all.getAttribute('data-rd-all') === '1';
          modal.querySelectorAll('[data-rd-item]').forEach(function (el) { setAnswer(modal, pages, el, show); });
          return;
        }
        if (ev.target.closest('[data-rd-src]')) {
          var p = pages[Number(modal.getAttribute('data-rd-cur'))];
          if (typeof window.openImageLightbox === 'function') window.openImageLightbox(p.image, p.title + '（' + p.source_page + ' 原頁）');
          return;
        }
        var item = ev.target.closest('[data-rd-item]');
        if (item) setAnswer(modal, pages, item, item.getAttribute('data-rd-open') !== '1');
      } catch (e) { console.warn('[讀背] 點擊處理失敗', e); }
    });

    // 插在燈箱之前：同為 z-50 時 DOM 在後者疊在上面，看原頁的燈箱才不會被本彈窗蓋住
    var lightbox = document.getElementById('diagram-lightbox');
    if (lightbox && lightbox.parentNode) lightbox.parentNode.insertBefore(modal, lightbox);
    else document.body.appendChild(modal);
    renderPage(modal, pages, 0);
    return modal;
  }

  function buildEntryCard(modal, pages) {
    var anchor = document.querySelector('[data-tr-entry]') || document.querySelector('[onclick="openScrollsModal()"]');
    if (!anchor || !anchor.parentNode) return;
    var total = pages.reduce(function (n, p) { return n + p.items.length; }, 0);
    var card = document.createElement('div');
    card.className = 'bg-slate-900/90 p-4 rounded-2xl border border-sky-800/50 active:scale-95 transition cursor-pointer space-y-2 bg-gradient-to-br from-sky-950/30 to-slate-900';
    card.innerHTML =
      '<div class="flex justify-between items-center"><div class="text-2xl">📖</div>' +
      '<span class="text-[10px] px-1.5 py-0.5 rounded-full bg-sky-500/20 text-sky-300 font-bold border border-sky-500/30">' + total + '題</span></div>' +
      '<div class="text-sm font-bold text-white">筆記讀背</div>' +
      '<div class="text-[11px] text-slate-400">' + pages.length + ' 頁文字轉錄，遮住答案自測</div>';
    card.addEventListener('click', function () {
      try { modal.classList.remove('hidden'); } catch (e) { console.warn('[讀背] 開啟失敗', e); }
    });
    anchor.parentNode.insertBefore(card, anchor.nextSibling);
  }

  function init() {
    try {
      var pages = getPages();
      if (!pages.length || document.getElementById('reading-modal')) return;
      buildEntryCard(buildModal(pages), pages);
    } catch (e) { console.warn('[讀背] 初始化失敗', e); }
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
