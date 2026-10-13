// 敷地速刷 外掛：返回鍵關彈窗（2026-10-13 私人電腦 Claude Code）
// 掛法：index.html 的 </body> 前最後一支 <script src="nav_back.js"></script>
// 積木規範：整支包在 IIFE 內、事件皆 try/catch，不改主程式任何函式。
// 原理：彈窗打開或離開首頁時 pushState 一筆；按返回鍵（popstate）就關最上層彈窗、或回首頁。
//       使用者自己按 ✕ 關掉時，多出來的那筆用 history.back() 吃掉（ignoreNext 防止連關兩層）。
(function () {
  'use strict';

  var WATCH = /(modal|lightbox)$/;
  var CLOSERS = {
    'diagram-lightbox': 'closeDiagramLightbox',
    'scrolls-modal': 'closeScrollsModal',
    'modules-modal': 'closeModulesModal',
    'capsule-modal': 'closeCapsuleModal'
  };
  var depth = 0;        // 本外掛推入的歷史筆數
  var ignoreNext = 0;   // 自己呼叫 history.back() 造成的 popstate 要略過

  function isOpen(el) { return el && !el.classList.contains('hidden'); }

  function openLayers() {
    var list = Array.prototype.filter.call(document.querySelectorAll('[id]'), function (el) {
      return WATCH.test(el.id) && isOpen(el);
    });
    var home = document.getElementById('view-capsule');
    return { modals: list, offHome: home && !isOpen(home) };
  }

  function push() {
    try { history.pushState({ navBack: depth + 1 }, ''); depth++; } catch (e) { /* 不支援就略過 */ }
  }

  function closeEl(el) {
    var fn = CLOSERS[el.id];
    if (fn && typeof window[fn] === 'function') window[fn]();
    else el.classList.add('hidden');
  }

  function onLayerChange(opened) {
    if (opened) { push(); return; }
    if (depth > 0) { ignoreNext++; depth--; history.back(); }
  }

  window.addEventListener('popstate', function () {
    try {
      if (ignoreNext > 0) { ignoreNext--; return; }
      if (depth > 0) depth--;
      var s = openLayers();
      if (s.modals.length) { expectClose++; closeEl(s.modals[s.modals.length - 1]); return; }
      if (s.offHome && typeof window.switchView === 'function') { expectClose++; window.switchView('capsule'); }
    } catch (e) { console.warn('[返回鍵] 處理失敗', e); }
  });

  var expectClose = 0;  // popstate 觸發的關閉（MutationObserver 非同步回報），不要再 history.back()
  var seen = {};

  function check(el) {
    if (!el || !el.id) return;
    var key = el.id;
    var open;
    if (WATCH.test(key)) open = isOpen(el);
    else if (key === 'view-capsule') open = !isOpen(el);  // 離開首頁視同打開一層
    else return;
    if (seen[key] === open) return;
    var first = !(key in seen);
    seen[key] = open;
    if (first && !open) return;
    if (open) onLayerChange(true);
    else if (expectClose > 0) expectClose--;
    else onLayerChange(false);
  }

  function init() {
    try {
      Array.prototype.forEach.call(document.querySelectorAll('[id]'), function (el) {
        if (WATCH.test(el.id) || el.id === 'view-capsule') seen[el.id] = el.id === 'view-capsule' ? !isOpen(el) : isOpen(el);
      });
      new MutationObserver(function (muts) {
        try { muts.forEach(function (m) { check(m.target); }); } catch (e) { console.warn('[返回鍵] 監看失敗', e); }
      }).observe(document.body, { subtree: true, attributes: true, attributeFilter: ['class'] });
    } catch (e) { console.warn('[返回鍵] 初始化失敗', e); }
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
