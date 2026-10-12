// 敷地速刷 外掛：離線功能＋數字卡錯題本（2026-10-12 公司電腦 Claude Code）
// 掛法：index.html 的 </body> 前加一行 <script src="offline_wrongbook.js"></script>
// 不改 generate_app.py 產出的任何函式本體，只包裝 markNumberCard／nextNumberCard／prevNumberCard／updateDashboardStats。
(function () {
  'use strict';

  // ---------- 安全的 localStorage（私密模式或容量滿時不讓功能中斷） ----------
  function lsGet(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function lsSet(k, v) { try { localStorage.setItem(k, v); return true; } catch (e) { return false; } }

  // ---------- 1. 離線：註冊 Service Worker ----------
  if ('serviceWorker' in navigator && location.protocol !== 'file:') {
    window.addEventListener('load', function () {
      navigator.serviceWorker.register('sw.js').catch(function (e) {
        console.warn('[離線] Service Worker 註冊失敗', e);
      });
    });
  }

  // ---------- 2. 錯題本 ----------
  var WB_KEY = 'SITE_PLANNING_WRONGBOOK_V1';
  var CLEAR_AFTER = 2; // 錯題連續答對 2 次才移出錯題本
  var wb = {};
  try { wb = JSON.parse(lsGet(WB_KEY) || '{}') || {}; } catch (e) { wb = {}; }
  var wrongOnly = false;

  function saveWb() { lsSet(WB_KEY, JSON.stringify(wb)); }
  // SITE_DATA 是頁面裡的 const，不掛在 window 上，要用全域名稱直接取
  function nums() { return (typeof SITE_DATA !== 'undefined' && SITE_DATA.numbers) || []; }
  function wrongIdx() {
    var out = [];
    nums().forEach(function (n, i) { if (wb[n.id] && wb[n.id].active) out.push(i); });
    return out;
  }
  function curItem() {
    var a = nums();
    return a.length ? a[appState.numberIndex % a.length] : null;
  }

  function record(id, ok) {
    var r = wb[id] || { wrong: 0, right: 0, streak: 0, active: false, last: 0 };
    r.last = Date.now();
    if (ok) {
      r.right++;
      if (r.active) { r.streak++; if (r.streak >= CLEAR_AFTER) { r.active = false; r.streak = 0; } }
    } else {
      r.wrong++; r.active = true; r.streak = 0;
    }
    wb[id] = r;
    saveWb();
  }

  // 在錯題之間移動；錯題本清空時自動回到一般模式
  function stepWrong(dir) {
    var list = wrongIdx();
    if (!list.length) {
      wrongOnly = false;
      refreshUi();
      if (typeof showToast === 'function') showToast('錯題本已清空，回到全部題目', '🎉', false);
      return false;
    }
    var cur = appState.numberIndex % nums().length;
    var pos = list.indexOf(cur);
    var next;
    if (pos === -1) {
      next = dir > 0 ? (list.find(function (i) { return i > cur; }) ?? list[0])
                     : (list.slice().reverse().find(function (i) { return i < cur; }) ?? list[list.length - 1]);
    } else {
      next = list[(pos + dir + list.length) % list.length];
    }
    appState.numberIndex = next;
    renderNumberCard();
    saveState();
    return true;
  }

  // ---------- 包裝原有函式 ----------
  var origMark = window.markNumberCard;
  var origNext = window.nextNumberCard;
  var origPrev = window.prevNumberCard;
  var origStats = window.updateDashboardStats;

  if (typeof origMark === 'function') {
    window.markNumberCard = function (isMastered) {
      var it = curItem();
      if (it) record(it.id, !!isMastered);
      if (wrongOnly) {
        appState.masteredNumbers[it.id] = isMastered;
        saveState();
        stepWrong(1);
        refreshUi();
        return;
      }
      origMark(isMastered);
      refreshUi();
    };
  }
  if (typeof origNext === 'function') {
    window.nextNumberCard = function () { if (wrongOnly) { stepWrong(1); } else { origNext(); } };
  }
  if (typeof origPrev === 'function') {
    window.prevNumberCard = function () { if (wrongOnly) { stepWrong(-1); } else { origPrev(); } };
  }
  if (typeof origStats === 'function') {
    window.updateDashboardStats = function () { origStats(); refreshUi(); };
  }

  // ---------- 介面：數字卡分類列前加「錯題本」切換鈕 ----------
  function refreshUi() {
    var n = wrongIdx().length;
    var btn = document.getElementById('wb-toggle');
    if (btn) {
      btn.textContent = (wrongOnly ? '✅ 錯題本練習中 ' : '❌ 錯題本 ') + n;
      btn.className = 'px-3 py-1.5 rounded-lg whitespace-nowrap border font-bold transition ' +
        (wrongOnly ? 'bg-rose-600 text-white border-rose-500' : 'bg-rose-950/60 text-rose-300 border-rose-800/60');
      btn.disabled = n === 0 && !wrongOnly;
      btn.style.opacity = btn.disabled ? '0.5' : '1';
    }
    var stat = document.getElementById('stats-num-rate');
    if (stat) stat.title = '錯題本 ' + n + ' 題';
  }

  function mountUi() {
    var tabs = document.getElementById('num-category-tabs');
    if (!tabs || document.getElementById('wb-toggle')) return;
    var btn = document.createElement('button');
    btn.id = 'wb-toggle';
    btn.onclick = function () {
      if (!wrongOnly && !wrongIdx().length) return;
      wrongOnly = !wrongOnly;
      if (wrongOnly) {
        var cur = appState.numberIndex % nums().length;
        if (wrongIdx().indexOf(cur) === -1) stepWrong(1);
        if (typeof showToast === 'function') showToast('錯題本：連續答對 ' + CLEAR_AFTER + ' 次才移出', '❌', false);
      }
      refreshUi();
    };
    tabs.parentNode.insertBefore(btn, tabs);
    var wrap = document.createElement('div');
    wrap.className = 'flex';
    tabs.parentNode.insertBefore(wrap, btn);
    wrap.appendChild(btn);
    refreshUi();
  }

  // 對外：供測試與除錯
  window.WRONGBOOK = {
    data: function () { return JSON.parse(JSON.stringify(wb)); },
    count: function () { return wrongIdx().length; },
    isWrongOnly: function () { return wrongOnly; }
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mountUi);
  } else {
    mountUi();
  }
})();
