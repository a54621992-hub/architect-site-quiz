// 敷地速刷 外掛：手繪臨摹庫（2026-10-12 私人電腦 Claude Code）
// 掛法：index.html 的 </body> 前加一行 <script src="tracing_lib.js"></script>
// 積木規範：整支包在 IIFE 內、事件皆 try/catch、只讀 SITE_DATA.tracing_cards，不改主程式任何函式。
(function () {
  'use strict';

  function getCards() {
    try {
      return (typeof SITE_DATA !== 'undefined' && Array.isArray(SITE_DATA.tracing_cards)) ? SITE_DATA.tracing_cards : [];
    } catch (e) { return []; }
  }

  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  function openImage(src, title) {
    try {
      if (typeof window.openImageLightbox === 'function') window.openImageLightbox(src, title);
      else window.open(src, '_blank');
    } catch (e) { console.warn('[臨摹庫] 開圖失敗', e); }
  }

  function buildModal(cards) {
    var modal = document.createElement('div');
    modal.id = 'tracing-modal';
    modal.className = 'fixed inset-0 z-50 bg-slate-950/90 backdrop-blur-md flex items-center justify-center p-3 hidden';
    modal.innerHTML =
      '<div class="bg-slate-900 border border-slate-700 rounded-3xl max-w-xl w-full p-5 space-y-4 shadow-2xl relative max-h-[92vh] flex flex-col">' +
        '<div class="flex justify-between items-center border-b border-slate-800 pb-3 shrink-0">' +
          '<div class="flex items-center space-x-2"><span class="text-xl">✏️</span><div>' +
            '<h3 class="text-base font-black text-white">手繪臨摹庫</h3>' +
            '<p class="text-[11px] text-violet-300">名師筆記整頁掃描，點圖放大照著畫（共 ' + cards.length + ' 頁）</p>' +
          '</div></div>' +
          '<button data-tr-close class="w-8 h-8 rounded-full bg-slate-800 text-slate-400 hover:text-white flex items-center justify-center text-xs">✕</button>' +
        '</div>' +
        '<div class="overflow-y-auto pr-1 flex-1 grid grid-cols-2 gap-3">' +
          cards.map(function (c, i) {
            return '<div data-tr-idx="' + i + '" class="bg-slate-950/80 p-2 rounded-2xl border border-slate-800 space-y-1.5 cursor-pointer active:scale-95 transition">' +
              '<div class="bg-white rounded-xl overflow-hidden flex items-center justify-center h-40">' +
                '<img loading="lazy" src="' + esc(c.image) + '" alt="' + esc(c.title) + '" class="w-full h-full object-contain">' +
              '</div>' +
              '<div class="flex items-center justify-between gap-1">' +
                '<span class="text-xs font-bold text-white leading-tight">' + esc(c.title) + '</span>' +
                '<span class="text-[10px] px-1.5 py-0.5 rounded-md bg-violet-950 text-violet-300 border border-violet-800/40 whitespace-nowrap">' + esc(c.source_page) + '</span>' +
              '</div>' +
              '<p class="text-[10px] text-slate-400 leading-snug">' + esc(c.desc) + '</p>' +
            '</div>';
          }).join('') +
        '</div>' +
      '</div>';

    modal.addEventListener('click', function (ev) {
      try {
        if (ev.target === modal || ev.target.closest('[data-tr-close]')) { modal.classList.add('hidden'); return; }
        var item = ev.target.closest('[data-tr-idx]');
        if (item) {
          var c = cards[Number(item.getAttribute('data-tr-idx'))];
          if (c) openImage(c.image, c.title + '（' + c.source_page + '）');
        }
      } catch (e) { console.warn('[臨摹庫] 點擊處理失敗', e); }
    });
    // 插在燈箱之前：同為 z-50 時 DOM 在後者疊在上面，燈箱才不會被本彈窗蓋住
    var lightbox = document.getElementById('diagram-lightbox');
    if (lightbox && lightbox.parentNode) lightbox.parentNode.insertBefore(modal, lightbox);
    else document.body.appendChild(modal);
    return modal;
  }

  function buildEntryCard(modal, count) {
    var anchor = document.querySelector('[onclick="openScrollsModal()"]');
    if (!anchor || !anchor.parentNode) return;
    var card = document.createElement('div');
    card.className = 'bg-slate-900/90 p-4 rounded-2xl border border-violet-800/50 active:scale-95 transition cursor-pointer space-y-2 bg-gradient-to-br from-violet-950/30 to-slate-900';
    card.innerHTML =
      '<div class="flex justify-between items-center"><div class="text-2xl">✏️</div>' +
      '<span class="text-[10px] px-1.5 py-0.5 rounded-full bg-violet-500/20 text-violet-300 font-bold border border-violet-500/30">' + count + '頁</span></div>' +
      '<div class="text-sm font-bold text-white">手繪臨摹庫</div>' +
      '<div class="text-[11px] text-slate-400">版面格線＋情境透視，點圖放大臨摹</div>';
    card.addEventListener('click', function () {
      try { modal.classList.remove('hidden'); } catch (e) { console.warn('[臨摹庫] 開啟失敗', e); }
    });
    anchor.parentNode.insertBefore(card, anchor.nextSibling);
  }

  function init() {
    try {
      var cards = getCards();
      if (!cards.length || document.getElementById('tracing-modal')) return;
      buildEntryCard(buildModal(cards), cards.length);
    } catch (e) { console.warn('[臨摹庫] 初始化失敗', e); }
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
