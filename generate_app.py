# -*- coding: utf-8 -*-
"""
生成 敷地計畫與都市設計 零散時間極速複習 APP (V5 旗艦版)
- 頂部 24 題標籤專屬辨識化 (115隨堂、115擴大、115模2、115模1、114~95)
- 全量 24 套試題基地圖高精度外科手術裁切 (去雜訊、去大白邊、完美置中)
- 115 年 3 套模考完整題文多模態謄錄注入 (徹底修復「無題目正文」，校正模1題名)
- 全域燈箱雙指捏合手勢縮放 (Pinch-to-zoom 1x~4.5x) 與滑動平移 (Pan/Drag)
- 審題卡單手左右滑動換題 (Swipe Navigation) 與鍵盤方向鍵支援
"""

import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# 若在 repo 根目錄執行，資產在同層；若在 AI分析 執行，在 敷地APP 子目錄
APP_DIR = os.path.join(ROOT_DIR, "敷地APP") if os.path.isdir(os.path.join(ROOT_DIR, "敷地APP")) else ROOT_DIR
JSON_PATH = os.path.join(APP_DIR, "site_data.json")

with open(JSON_PATH, 'r', encoding='utf-8') as f:
    site_data = json.load(f)

json_str = json.dumps(site_data, ensure_ascii=False)

html_template = f'''<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>敷地速刷｜敷地計畫與都市設計極速複習</title>
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="apple-mobile-web-app-title" content="敷地速刷">
  <meta name="theme-color" content="#0f172a">
  <link rel="manifest" href="manifest.json">
  <link rel="apple-touch-icon" href="apple-touch-icon.png">
  <link rel="icon" type="image/png" sizes="192x192" href="icon-192.png">
  <link rel="icon" type="image/png" sizes="512x512" href="icon-512.png">
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          colors: {{
            slate: {{
              750: '#232f48',
              850: '#151e32',
              900: '#0f172a',
              950: '#090d16'
            }},
            emerald: {{
              500: '#10b981',
              600: '#059669'
            }}
          }}
        }}
      }}
    }}
  </script>
  <style>
    * {{
      -webkit-tap-highlight-color: transparent;
      user-select: none;
    }}
    .perspective-1000 {{
      perspective: 1000px;
    }}
    .transform-style-3d {{
      transform-style: preserve-3d;
    }}
    .backface-hidden {{
      backface-visibility: hidden;
      -webkit-backface-visibility: hidden;
    }}
    .rotate-y-180 {{
      transform: rotateY(180deg);
    }}
    .no-scrollbar::-webkit-scrollbar {{
      display: none;
    }}
    .no-scrollbar {{
      -ms-overflow-style: none;
      scrollbar-width: none;
    }}
    @supports (-webkit-touch-callout: none) {{
      .safe-bottom {{
        padding-bottom: env(safe-area-inset-bottom, 20px);
      }}
    }}
  </style>
</head>
<body class="bg-slate-950 text-slate-100 font-sans min-h-screen pb-24 antialiased selection:bg-emerald-500 selection:text-white">

  <!-- 頂部固定狀態列 -->
  <header class="sticky top-0 z-40 bg-slate-900/90 backdrop-blur-md border-b border-slate-800 px-4 py-3 flex justify-between items-center max-w-xl mx-auto shadow-md">
    <div class="flex items-center space-x-2">
      <span class="text-xl">📐</span>
      <div>
        <h1 class="text-base font-black tracking-tight text-white flex items-center space-x-1.5">
          <span>敷地速刷</span>
          <span class="text-[10px] px-1.5 py-0.5 rounded-full bg-emerald-500/20 text-emerald-400 font-bold border border-emerald-500/30">V5.3 旗艦版</span>
        </h1>
        <p class="text-[10px] text-slate-400">專技建築師高考・零散時間極速複習</p>
      </div>
    </div>
    <div class="flex items-center space-x-2">
      <button onclick="cycleFontScale()" class="px-2.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-bold active:scale-95 transition flex items-center space-x-1" title="切換字體大小 (標準 100% / 大字 115% / 特大 130%)">
        <span>🔤</span>
        <span id="header-font-scale-text">字體</span>
      </button>
      <button onclick="toggleSettingsModal()" class="w-8 h-8 rounded-full bg-slate-800 flex items-center justify-center text-slate-300 hover:text-white border border-slate-700 active:scale-95 transition" title="設定與系統資訊">
        ⚙️
      </button>
    </div>
  </header>

  <!-- 主容器 -->
  <main class="max-w-xl mx-auto px-4 pt-3 pb-8 space-y-4">

    <!-- 頂部及格線信心儀表板 (Pass Radar) -->
    <section class="bg-gradient-to-br from-slate-900 via-slate-850 to-slate-900 p-4 rounded-3xl border border-slate-800 shadow-xl relative overflow-hidden">
      <div class="flex justify-between items-center mb-3">
        <span class="text-xs font-bold text-slate-400 tracking-wider">🎯 零散時間備考儀表板</span>
        <span class="text-[11px] font-mono px-2 py-0.5 rounded-full bg-blue-950 text-blue-300 border border-blue-800/50">40天衝刺</span>
      </div>
      <div class="grid grid-cols-3 gap-2 text-center">
        <div class="bg-slate-950/60 p-2.5 rounded-2xl border border-slate-800/80">
          <div class="text-[10px] text-slate-400">審題反射率</div>
          <div class="text-lg font-black text-emerald-400 mt-0.5" id="stats-num-rate">0%</div>
          <div class="text-[9px] text-slate-500">84 組關鍵字反射</div>
        </div>
        <div class="bg-slate-950/60 p-2.5 rounded-2xl border border-slate-800/80">
          <div class="text-[10px] text-slate-400">SOP 反射連勝</div>
          <div class="text-lg font-black text-cyan-400 mt-0.5" id="stats-sop-streak">0 題</div>
          <div class="text-[9px] text-slate-500">11 步驟無腦接</div>
        </div>
        <div class="bg-slate-950/60 p-2.5 rounded-2xl border border-slate-800/80">
          <div class="text-[10px] text-slate-400">六格秒殺卡</div>
          <div class="text-lg font-black text-purple-400 mt-0.5" id="stats-grid-count">0/72</div>
          <div class="text-[9px] text-slate-500">已翻開覆盤</div>
        </div>
      </div>
    </section>

    <!-- 模組 1: 3 分鐘微膠囊 (Daily Capsule) -->
    <section id="view-capsule" class="view-panel space-y-4">
      <div class="bg-slate-900 rounded-3xl border border-slate-800 p-5 shadow-xl space-y-4 text-center">
        <div class="inline-block px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-xs font-bold">
          ⚡ 碎片時間・3 分鐘隨機微膠囊
        </div>
        <h2 class="text-lg font-black text-white">抽空 3 分鐘，建立神經迴路</h2>
        <p class="text-xs text-slate-400 max-w-xs mx-auto leading-relaxed">
          每次隨機抽調：1 組審題反射 ＋ 1 題作圖SOP ＋ 1 格申論骨架 ＋ 1 張萬用圖卡大腦心像
        </p>
        <button onclick="startDailyCapsule()" class="w-full py-3.5 px-4 rounded-2xl bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 hover:to-teal-400 text-slate-950 font-black text-sm shadow-lg shadow-emerald-500/20 active:scale-98 transition flex items-center justify-center space-x-2">
          <span>🚀</span>
          <span>立即開始今日微膠囊 (3 min)</span>
        </button>
      </div>

      <!-- 快速通道卡片 -->
      <div class="grid grid-cols-2 gap-3">
        <div onclick="switchView('sop')" class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 active:scale-95 transition cursor-pointer space-y-2">
          <div class="text-2xl">📐</div>
          <div class="text-sm font-bold text-white">作圖SOP 盲測</div>
          <div class="text-[11px] text-slate-400">11步驟、三鐵律、色筆</div>
        </div>
        <div onclick="switchView('numbers')" class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 active:scale-95 transition cursor-pointer space-y-2">
          <div class="text-2xl">⚡</div>
          <div class="text-sm font-bold text-white">84 組審題關鍵字反射卡</div>
          <div class="text-[11px] text-slate-400">題幹關鍵字 ➔ 3秒下意識反射對策</div>
        </div>
        <div onclick="switchView('grids')" class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 active:scale-95 transition cursor-pointer space-y-2">
          <div class="text-2xl">⚡</div>
          <div class="text-sm font-bold text-white">72 單格快卡</div>
          <div class="text-[11px] text-slate-400">診/策/制/系/界/時</div>
        </div>
        <div onclick="switchView('diagrams')" class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 active:scale-95 transition cursor-pointer space-y-2">
          <div class="text-2xl">🖼️</div>
          <div class="text-sm font-bold text-white">11 張萬用圖卡</div>
          <div class="text-[11px] text-slate-400">向量圖 ＋ 建築師手繪臨摹</div>
        </div>
        <div onclick="openModulesModal()" class="bg-slate-900/90 p-4 rounded-2xl border border-teal-800/50 active:scale-95 transition cursor-pointer space-y-2 bg-gradient-to-br from-teal-950/30 to-slate-900">
          <div class="flex justify-between items-center">
            <div class="text-2xl">📏</div>
            <span class="text-[10px] px-1.5 py-0.5 rounded-full bg-teal-500/20 text-teal-300 font-bold border border-teal-500/30">實戰秒算</span>
          </div>
          <div class="text-sm font-bold text-white">實戰模矩速算</div>
          <div class="text-[11px] text-slate-400">9×9M柱網、坪數、停車救災</div>
        </div>
        <div onclick="openScrollsModal()" class="bg-slate-900/90 p-4 rounded-2xl border border-amber-800/50 active:scale-95 transition cursor-pointer space-y-2 bg-gradient-to-br from-amber-950/30 to-slate-900">
          <div class="flex justify-between items-center">
            <div class="text-2xl">📜</div>
            <span class="text-[10px] px-1.5 py-0.5 rounded-full bg-amber-500/20 text-amber-300 font-bold border border-amber-500/30">8幅手繪</span>
          </div>
          <div class="text-sm font-bold text-white">名師手繪範卷觀摩</div>
          <div class="text-[11px] text-slate-400">4 份範卷正卷與草稿手勢縮放（非官方試題）</div>
        </div>
        <div onclick="switchView('strategy')" class="bg-slate-900/90 p-4 rounded-2xl border border-blue-900/40 col-span-2 active:scale-95 transition cursor-pointer space-y-2 bg-gradient-to-r from-blue-950/40 to-slate-900">
          <div class="flex justify-between items-center">
            <div class="text-2xl">🔪</div>
            <span class="text-[10px] px-2 py-0.5 rounded-full bg-blue-600 text-white font-bold">全量 31 題單頁卡片</span>
          </div>
          <div class="text-sm font-bold text-white">審題快刀卡 (歷屆 20 題 ＋ 模擬考 11 題)</div>
          <div class="text-[11px] text-slate-400">2 分鐘自問課題 ＋ 破局黃金決策 ＋ 高解析基地現況圖</div>
        </div>
      </div>
    </section>

    <!-- 模組 2: 作圖 SOP 肌肉記憶專章 (SOP Blitz) -->
    <section id="view-sop" class="view-panel hidden space-y-4">
      <div class="flex space-x-1.5 p-1 bg-slate-900 rounded-xl border border-slate-800 text-xs font-semibold">
        <button onclick="switchSopTab('blitz')" id="sop-tab-blitz" class="flex-1 py-1.5 rounded-lg bg-emerald-500 text-slate-950 font-bold transition">下一步盲測</button>
        <button onclick="switchSopTab('rules')" id="sop-tab-rules" class="flex-1 py-1.5 rounded-lg text-slate-400 transition">三條鐵律</button>
        <button onclick="switchSopTab('colors')" id="sop-tab-colors" class="flex-1 py-1.5 rounded-lg text-slate-400 transition">色筆標記</button>
        <button onclick="switchSopTab('list')" id="sop-tab-list" class="flex-1 py-1.5 rounded-lg text-slate-400 transition">11 步驟</button>
      </div>

      <!-- SOP 子頁面 1: 下一步盲測 -->
      <div id="sop-sub-blitz" class="space-y-4">
        <div class="bg-slate-900 rounded-3xl border border-slate-800 p-5 shadow-xl space-y-4">
          <div class="flex justify-between items-center text-xs">
            <span class="px-2.5 py-0.5 rounded-full bg-cyan-950 text-cyan-300 font-bold border border-cyan-800/50">肌肉記憶反射測試</span>
            <span class="text-slate-400 font-mono" id="sop-quiz-streak">🔥 連勝: 0 題</span>
          </div>
          <div class="text-base font-bold text-white leading-relaxed" id="sop-quiz-question">
            題目載入中...
          </div>
          <div class="space-y-2 pt-2" id="sop-quiz-options">
            <!-- 動態生成選項 -->
          </div>
          <div id="sop-quiz-feedback" class="hidden p-3.5 rounded-2xl bg-slate-950 border border-slate-800 space-y-2 text-xs">
            <div id="sop-feedback-title" class="font-bold"></div>
            <div id="sop-feedback-text" class="text-slate-300 leading-relaxed"></div>
            <button onclick="loadNextSopQuiz()" class="w-full mt-2 py-2.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs transition">
              下一題反射 →
            </button>
          </div>
        </div>
      </div>

      <!-- SOP 子頁面 2: 三條鐵律 -->
      <div id="sop-sub-rules" class="hidden space-y-3">
        <div id="sop-rules-container" class="space-y-3"></div>
      </div>
      <!-- SOP 子頁面 3: 色筆標記法 -->
      <div id="sop-sub-colors" class="hidden space-y-3">
        <div id="sop-colors-container" class="space-y-3"></div>
      </div>
      <!-- SOP 子頁面 4: 11 步驟總覽 -->
      <div id="sop-sub-list" class="hidden space-y-3">
        <div id="sop-list-container" class="space-y-3"></div>
      </div>
    </section>

    <!-- 模組 3: 84 項審題關鍵字反射卡 (Reflex Blitz) -->
    <section id="view-numbers" class="view-panel hidden space-y-3.5">
      <!-- 分類標籤滑動列 -->
      <div class="flex space-x-1.5 overflow-x-auto no-scrollbar py-0.5 text-xs" id="num-category-tabs"></div>
      
      <!-- 翻牌卡本體 (支援自適應高度與 3D 翻牌) -->
      <div class="perspective-1000 w-full min-h-[320px]">
        <div id="num-card-inner" onclick="flipNumberCard()" class="transform-style-3d relative w-full h-full min-h-[320px] bg-slate-900 rounded-3xl border border-slate-800 p-5 shadow-2xl flex flex-col justify-between cursor-pointer transition-transform duration-500">
          
          <!-- 正面: 審題觸發情境與關鍵字標籤 -->
          <div class="backface-hidden flex flex-col justify-between h-full space-y-3">
            <div class="flex justify-between items-center text-xs">
              <span class="px-2.5 py-0.5 rounded-full bg-cyan-500/15 text-cyan-300 font-bold border border-cyan-500/30" id="num-card-cat">分類</span>
              <span class="text-slate-500 font-mono text-xs" id="num-card-index">01 / 84</span>
            </div>

            <!-- 關鍵字標籤組 (反射模式核心) -->
            <div id="num-card-keywords-wrap" class="space-y-1.5">
              <div class="flex items-center gap-1.5 text-[11px] text-amber-400 font-bold">
                <span>🔑</span><span>核心審題觸發關鍵字：</span>
              </div>
              <div id="num-card-keywords-container" class="flex flex-wrap gap-1.5">
                <!-- 動態注入關鍵字 Chips -->
              </div>
            </div>

            <!-- 題目情境提問 -->
            <div class="my-auto py-2">
              <p class="text-xs text-slate-400 mb-1.5 font-medium" id="num-card-prompt-hint">🎯 考題審題情境反射提問：</p>
              <h3 class="text-base sm:text-lg font-black text-white leading-snug" id="num-card-question">題目內容</h3>
            </div>

            <div class="text-center pt-2 border-t border-slate-800/80 text-[11px] text-cyan-400/80 flex items-center justify-center space-x-1">
              <span id="num-card-front-tap-hint">👆 點擊卡片翻面看 3 秒手繪反射決策 ＆ 黃金數據</span>
            </div>
          </div>

          <!-- 背面: 3秒手繪反射對策 ＆ 黃金數據 ＆ 手繪圖卡一鍵跳轉 -->
          <div class="backface-hidden rotate-y-180 absolute inset-0 bg-slate-900 rounded-3xl border border-emerald-500/40 p-5 flex flex-col justify-between space-y-3 overflow-y-auto no-scrollbar">
            <div class="flex justify-between items-center gap-2 border-b border-slate-800/80 pb-2 shrink-0">
              <span class="text-emerald-400 font-black text-sm shrink-0 whitespace-nowrap flex items-center gap-1" id="num-card-back-title">
                <span>⚡</span><span>3 秒手繪反射決策</span>
              </span>
              <div class="flex items-center gap-2 shrink-0">
                <button onclick="event.stopPropagation(); copyCurrentNumberCard(this)" class="shrink-0 flex items-center gap-1.5 px-3 py-1 rounded-xl font-bold text-xs bg-slate-800 hover:bg-slate-700 text-slate-200 hover:text-white border border-slate-700 active:scale-95 transition shadow-sm whitespace-nowrap" title="複製此卡內容發問 GEM">
                  <span>📋</span><span>複製</span>
                </button>
                <span class="text-[11px] text-slate-400 font-semibold shrink-0 whitespace-nowrap" id="num-card-status">查證標記</span>
              </div>
            </div>

            <!-- 反射對策內容 -->
            <div class="space-y-2.5 my-auto">
              <!-- 3秒手繪決策框 -->
              <div id="num-card-reflex-box" class="bg-slate-950 p-3 rounded-2xl border border-cyan-800/50 text-xs text-cyan-100 text-left leading-relaxed">
                <span class="text-amber-400 block text-[10px] mb-1 font-bold flex items-center gap-1">
                  <span>💡</span><span>空間配置／圖面繪製決策：</span>
                </span>
                <span id="num-card-reflex-text" class="font-medium">反射決策說明</span>
              </div>

              <!-- 黃金數據與法規出處 -->
              <div class="flex items-center justify-between bg-slate-950/80 px-3.5 py-2.5 rounded-xl border border-slate-800">
                <div>
                  <span class="text-[10px] text-slate-400 block font-bold">🎯 黃金量化標準：</span>
                  <div class="text-xl sm:text-2xl font-black text-emerald-400 tracking-wide font-mono" id="num-card-answer">0.2 公頃</div>
                </div>
                <div class="text-right max-w-[50%]">
                  <span class="text-[10px] text-slate-500 block">法規依據：</span>
                  <div class="text-[11px] text-slate-300 font-mono break-words" id="num-card-source">出處條號</div>
                </div>
              </div>

              <!-- 傳統考場一句用法 (兩模式皆可輔助參考) -->
              <div id="num-card-usage-box" class="text-[11px] text-slate-400 text-left bg-slate-950/40 p-2 rounded-xl border border-slate-850">
                <span class="text-slate-500 font-bold">考場一句用法：</span>
                <span id="num-card-usage">用法說明</span>
              </div>

              <!-- 一鍵跳轉對應手繪圖卡臨摹 -->
              <div class="pt-1" id="num-card-jump-box">
                <button onclick="event.stopPropagation(); jumpToCurrentLinkedDiag()" class="w-full py-2.5 px-3 rounded-xl bg-gradient-to-r from-amber-500/20 to-emerald-500/20 hover:from-amber-500/30 hover:to-emerald-500/30 text-amber-300 hover:text-white border border-amber-500/40 text-xs font-bold active:scale-98 transition flex items-center justify-center space-x-1.5 shadow-md">
                  <span>✏️</span><span>一鍵臨摹對應手繪圖：</span><span class="underline font-black" id="num-card-jump-name">圖卡 09｜滯洪剖面 (P31)</span><span>↗</span>
                </button>
              </div>
            </div>

            <div class="text-center pt-2 border-t border-slate-800/80 text-[11px] text-slate-500 flex items-center justify-center space-x-1 shrink-0">
              <span>👆 點擊卡片翻回正面</span>
            </div>
          </div>
        </div>
      </div>

      <!-- 底部切換控制 -->
      <div class="flex items-center justify-between space-x-3 pt-1">
        <button onclick="markNumberCard(false)" class="flex-1 py-3.5 rounded-2xl bg-slate-900 hover:bg-slate-850 text-slate-400 hover:text-white border border-slate-800 font-bold text-xs active:scale-95 transition">
          ✕ 還不熟 (重測)
        </button>
        <button onclick="prevNumberCard()" class="p-3.5 rounded-2xl bg-slate-900 text-slate-300 hover:text-white border border-slate-800 active:scale-95 transition">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
        </button>
        <button onclick="nextNumberCard()" class="p-3.5 rounded-2xl bg-slate-900 text-slate-300 hover:text-white border border-slate-800 active:scale-95 transition">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
        </button>
        <button onclick="markNumberCard(true)" class="flex-1 py-3.5 rounded-2xl bg-emerald-950/50 hover:bg-emerald-900/60 text-emerald-300 border border-emerald-800/40 font-bold text-sm flex items-center justify-center space-x-1 active:scale-95 transition">
          <span>✓ 記住了 (右滑)</span>
        </button>
      </div>
    </section>

    <!-- 模組 4: 72 個單格快卡 (6-Grids Blitz) -->
    <section id="view-grids" class="view-panel hidden space-y-4">
      <div class="flex space-x-1.5 p-1 bg-slate-900 rounded-xl border border-slate-800 text-xs font-semibold overflow-x-auto no-scrollbar">
        <button onclick="filterGridFunc('all')" class="grid-func-btn flex-1 min-w-[45px] py-1.5 rounded-lg bg-purple-600 text-white font-bold" data-func="all">全部</button>
        <button onclick="filterGridFunc('診')" class="grid-func-btn flex-1 min-w-[45px] py-1.5 rounded-lg text-slate-400 hover:text-white" data-func="診">診斷</button>
        <button onclick="filterGridFunc('策')" class="grid-func-btn flex-1 min-w-[45px] py-1.5 rounded-lg text-slate-400 hover:text-white" data-func="策">策略</button>
        <button onclick="filterGridFunc('制')" class="grid-func-btn flex-1 min-w-[45px] py-1.5 rounded-lg text-slate-400 hover:text-white" data-func="制">制度</button>
        <button onclick="filterGridFunc('系')" class="grid-func-btn flex-1 min-w-[45px] py-1.5 rounded-lg text-slate-400 hover:text-white" data-func="系">系統</button>
        <button onclick="filterGridFunc('界')" class="grid-func-btn flex-1 min-w-[45px] py-1.5 rounded-lg text-slate-400 hover:text-white" data-func="界">界面</button>
        <button onclick="filterGridFunc('時')" class="grid-func-btn flex-1 min-w-[45px] py-1.5 rounded-lg text-slate-400 hover:text-white" data-func="時">時間</button>
      </div>
      <div id="grid-cards-container" class="space-y-3"></div>
    </section>

    <!-- 模組 5: 12 張萬用圖卡心智快閃 (Diagrams) -->
    <section id="view-diagrams" class="view-panel hidden space-y-4">
      <div class="flex space-x-2 overflow-x-auto no-scrollbar py-1" id="diag-nav-chips"></div>
      <div class="bg-slate-900 rounded-2xl border border-slate-800 p-4 shadow-xl space-y-4" id="diag-detail-card">
        <div class="flex justify-between items-start gap-2">
          <div class="flex-1">
            <h3 class="text-base font-black text-white" id="diag-title">圖卡 01｜Lynch 五元素轉譯表</h3>
            <p class="text-xs text-amber-400 mt-0.5" id="diag-used-for">跨題用途</p>
          </div>
          <div class="flex items-center gap-2 shrink-0">
            <button onclick="copyCurrentDiagramCard(this)" class="px-2.5 py-1 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold border border-slate-700 active:scale-95 transition flex items-center space-x-1" title="複製圖卡內容">
              <span>📋</span><span>複製</span>
            </button>
            <span class="text-xs px-2 py-0.5 rounded bg-slate-800 text-slate-400" id="diag-id-badge">01/12</span>
          </div>
        </div>

        <!-- 顯示模式切換：向量 SVG vs 手繪臨摹 -->
        <div id="diag-mode-toggle-box" class="flex items-center justify-between gap-2 bg-slate-950 p-1.5 rounded-xl border border-slate-800">
          <button id="diag-btn-svg" onclick="switchDiagMode('svg')" class="flex-1 py-1.5 rounded-lg text-xs font-bold bg-amber-500 text-slate-950 transition">
            🖼️ 原生向量圖解 (SVG)
          </button>
          <button id="diag-btn-sketch" onclick="switchDiagMode('sketch')" class="flex-1 py-1.5 rounded-lg text-xs font-bold text-slate-400 hover:text-white transition">
            ✏️ 建築師手繪臨摹
          </button>
        </div>

        <!-- 圖像展示區 (點擊手勢縮放與滿版臨摹) -->
        <div onclick="window.openCurrentDiagLightbox()" class="bg-white rounded-xl p-2 flex items-center justify-center overflow-hidden border border-slate-700 min-h-[200px] cursor-pointer relative shadow-inner" id="diag-svg-box">
        </div>
        <div class="text-[11px] text-emerald-400 text-center font-medium flex items-center justify-center space-x-1 cursor-pointer" onclick="window.openCurrentDiagLightbox()">
          <span>🔍 點擊圖片進入【手勢縮放 ＆ 滿版臨摹】</span>
        </div>

        <!-- 手繪技法標籤提示 -->
        <div id="diag-techniques-banner" class="hidden bg-emerald-950/40 p-3 rounded-xl border border-emerald-800/40 text-xs space-y-1">
          <span class="font-bold text-emerald-300 flex items-center space-x-1">
            <span>✨</span><span>考場實戰手繪技法與臨摹重點：</span>
          </span>
          <p class="text-emerald-200/90 leading-relaxed text-[11px]" id="diag-techniques-text"></p>
        </div>

        <div class="space-y-3 text-xs">
          <div class="bg-slate-950/60 p-3 rounded-xl border border-slate-800">
            <span class="font-bold text-emerald-400 block mb-1">⏱️ 3 分鐘手繪畫法：</span>
            <p class="text-slate-300 leading-relaxed" id="diag-draw-step"></p>
          </div>
          <div class="bg-slate-950/60 p-3 rounded-xl border border-slate-800">
            <span class="font-bold text-cyan-400 block mb-1.5">✅ 考場必標檢核清單（點擊自檢）：</span>
            <div class="space-y-1.5" id="diag-checklist-box"></div>
          </div>
          <div class="bg-rose-950/30 p-3 rounded-xl border border-rose-900/40 text-rose-300">
            <span class="font-bold block mb-1">⚠️ 常見失分避雷：</span>
            <p class="leading-relaxed" id="diag-pitfall"></p>
          </div>
        </div>
      </div>
    </section>

    <!-- 模組 6: 歷屆+模考審題快刀 (Strategy - 單頁單題 Pager 模式) -->
    <section id="view-strategy" class="view-panel hidden space-y-3.5">
      <!-- 審題快刀試題分類切換 (僅保留「模擬考」與「歷屆試題」) -->
      <div class="flex p-1 bg-slate-900 rounded-2xl border border-slate-800 text-xs font-bold gap-1 shadow-sm">
        <button id="strat-cat-mock" onclick="filterStrategyCategory('mock')" class="flex-1 py-2 rounded-xl text-xs font-black bg-blue-600 text-white transition shadow-sm">
          模擬考
        </button>
        <button id="strat-cat-past" onclick="filterStrategyCategory('past')" class="flex-1 py-2 rounded-xl text-xs font-semibold text-slate-400 hover:text-white transition">
          歷屆試題
        </button>
      </div>

      <!-- 頂部年份快速滑動標籤列 (動態渲染對應分類之年份標籤) -->
      <div class="flex space-x-1.5 overflow-x-auto no-scrollbar py-0.5 text-xs font-semibold" id="strategy-year-tabs">
        <!-- 動態渲染對應分類之年份標籤 -->
      </div>

      <!-- 單題卡片容器 (支援左右手勢滑動換題) -->
      <div id="strategy-single-card" class="bg-slate-900 rounded-3xl border border-slate-800 p-5 shadow-2xl space-y-4 transition-transform duration-200">
        <!-- 動態注入單題卡片 -->
      </div>

      <!-- 底部單手翻頁控制列 -->
      <div class="flex items-center justify-between space-x-3 pt-2">
        <button onclick="prevStrategyQuestion()" class="flex-1 py-3.5 rounded-2xl bg-slate-900 hover:bg-slate-850 text-slate-300 hover:text-white border border-slate-800 font-bold text-xs flex items-center justify-center space-x-1 active:scale-95 transition">
          <span>← 上一題</span>
        </button>
        <div class="text-xs font-mono text-slate-400 px-3" id="strategy-pager-text">
          1 / 24
        </div>
        <button onclick="nextStrategyQuestion()" class="flex-1 py-3.5 rounded-2xl bg-blue-600 hover:bg-blue-500 text-white font-bold text-xs flex items-center justify-center space-x-1 active:scale-95 transition shadow-lg shadow-blue-600/30">
          <span>下一題 →</span>
        </button>
      </div>
    </section>

  </main>

  <!-- 底部固定導航欄 -->
  <nav class="fixed bottom-0 left-0 right-0 z-50 bg-slate-900/95 backdrop-blur-lg border-t border-slate-800/80 px-2 py-1.5 flex justify-around items-center max-w-xl mx-auto shadow-2xl safe-bottom">
    <button onclick="switchView('capsule')" class="nav-btn flex flex-col items-center justify-center py-1 px-2.5 rounded-xl text-emerald-400 transition" data-view="capsule">
      <span class="text-lg">⚡</span>
      <span class="text-[10px] font-bold mt-0.5">微膠囊</span>
    </button>
    <button onclick="switchView('sop')" class="nav-btn flex flex-col items-center justify-center py-1 px-2.5 rounded-xl text-slate-400 hover:text-white transition" data-view="sop">
      <span class="text-lg">📐</span>
      <span class="text-[10px] font-medium mt-0.5">作圖SOP</span>
    </button>
    <button onclick="switchView('numbers')" class="nav-btn flex flex-col items-center justify-center py-1 px-2.5 rounded-xl text-slate-400 hover:text-white transition" data-view="numbers">
      <span class="text-lg">⚡</span>
      <span class="text-[10px] font-medium mt-0.5">關鍵字反射</span>
    </button>
    <button onclick="switchView('grids')" class="nav-btn flex flex-col items-center justify-center py-1 px-2.5 rounded-xl text-slate-400 hover:text-white transition" data-view="grids">
      <span class="text-lg">⚡</span>
      <span class="text-[10px] font-medium mt-0.5">單格快卡</span>
    </button>
    <button onclick="switchView('diagrams')" class="nav-btn flex flex-col items-center justify-center py-1 px-2.5 rounded-xl text-slate-400 hover:text-white transition" data-view="diagrams">
      <span class="text-lg">🖼️</span>
      <span class="text-[10px] font-medium mt-0.5">萬用圖卡</span>
    </button>
    <button onclick="switchView('strategy')" class="nav-btn flex flex-col items-center justify-center py-1 px-2.5 rounded-xl text-slate-400 hover:text-white transition" data-view="strategy">
      <span class="text-lg">🔪</span>
      <span class="text-[10px] font-medium mt-0.5">審題快刀</span>
    </button>
  </nav>

  <!-- 3分鐘隨機微膠囊 (法規速刷滿版大字體風格) -->
  <div id="capsule-modal" class="fixed inset-0 z-50 bg-slate-950 flex flex-col hidden overflow-hidden">
    <!-- 頂部固定狀態列 -->
    <div class="sticky top-0 z-20 bg-slate-900/95 backdrop-blur-md border-b border-slate-800 px-4 py-3 flex justify-between items-center max-w-xl mx-auto w-full shadow-md">
      <div class="flex items-center space-x-2">
        <span class="text-base font-black text-emerald-400">⚡ 3 分鐘微膠囊</span>
        <span class="text-xs px-2.5 py-0.5 rounded-full bg-slate-800 text-slate-300 font-mono font-bold" id="capsule-step-text">1 / 4</span>
      </div>
      <button onclick="closeCapsuleModal()" class="px-3 py-1 rounded-xl bg-slate-800 text-slate-300 hover:text-white text-xs font-bold active:scale-95 transition">
        ✕ 退出
      </button>
    </div>

    <!-- 中間主內容區 (全版面自然上下滾動) -->
    <div class="flex-1 overflow-y-auto px-4 pt-4 pb-32 max-w-xl mx-auto w-full" id="capsule-scroll-area">
      <div id="capsule-body" class="space-y-4"></div>
    </div>

    <!-- 底部固定操作列 -->
    <div class="fixed bottom-0 left-0 right-0 z-20 bg-slate-900/95 backdrop-blur-lg border-t border-slate-800 px-4 py-3 max-w-xl mx-auto flex items-center justify-between space-x-3 shadow-2xl safe-bottom">
      <button onclick="closeCapsuleModal()" class="py-3 px-5 rounded-2xl bg-slate-800 text-slate-300 font-bold text-sm active:scale-95 transition">
        退出
      </button>
      <button onclick="nextCapsuleStep()" id="capsule-next-btn" class="flex-1 py-3.5 px-6 rounded-2xl bg-gradient-to-r from-emerald-500 to-teal-500 text-slate-950 font-black text-base shadow-lg shadow-emerald-500/20 active:scale-95 transition flex items-center justify-center space-x-2">
        <span>下一步 (Next)</span>
        <span>→</span>
      </button>
    </div>
  </div>

  <!-- 系統設定與科目切換彈出視窗 (Settings Modal) -->
  <div id="settings-modal" class="fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-sm flex items-center justify-center p-4 hidden" onclick="if(event.target===this) toggleSettingsModal()">
    <div class="bg-slate-900 border border-slate-700 rounded-3xl max-w-sm w-full p-5 space-y-4 shadow-2xl relative">
      <div class="flex justify-between items-center border-b border-slate-800 pb-3">
        <div class="flex items-center space-x-2">
          <span class="text-xl">⚙️</span>
          <h3 class="text-sm font-black text-white">備考系統與設定</h3>
        </div>
        <button onclick="toggleSettingsModal()" class="w-7 h-7 rounded-full bg-slate-800 text-slate-400 hover:text-white flex items-center justify-center text-xs">
          ✕
        </button>
      </div>

      <!-- APP 版本與題庫資訊 -->
      <div class="bg-slate-950/70 rounded-2xl p-3 border border-slate-800 text-xs space-y-2">
        <div class="flex justify-between items-center">
          <span class="text-slate-400">目前版本</span>
          <span class="text-emerald-400 font-mono font-bold">V5.3 旗艦版（審題反射＆手繪校準）</span>
        </div>
        <div class="flex justify-between items-center">
          <span class="text-slate-400">核心題庫</span>
          <span class="text-slate-200">2.3.0 (84組反射 / 72單格 / 11萬用圖 / 24審題快刀 / 5模矩 / 8大卷)</span>
        </div>
        <div class="flex justify-between items-center">
          <span class="text-slate-400">離線支援</span>
          <span class="text-cyan-400">PWA 離線快取就緒</span>
        </div>
      </div>

      <!-- 全站字體大小調整 -->
      <div class="space-y-2">
        <div class="flex justify-between items-center text-xs text-slate-300 font-bold">
          <span>🔍 全站字體大小調整</span>
          <span id="current-font-label" class="text-emerald-400 font-mono text-xs">標準 (100%)</span>
        </div>
        <div class="grid grid-cols-3 gap-2">
          <button onclick="setFontScale('normal')" id="font-btn-normal" class="py-2.5 px-2 rounded-xl bg-emerald-500 text-slate-950 text-xs font-black transition">
            標準 A (100%)
          </button>
          <button onclick="setFontScale('large')" id="font-btn-large" class="py-2.5 px-2 rounded-xl bg-slate-800 text-slate-300 hover:text-white border border-slate-700 text-xs font-bold transition">
            大字 A+ (115%)
          </button>
          <button onclick="setFontScale('xlarge')" id="font-btn-xlarge" class="py-2.5 px-2 rounded-xl bg-slate-800 text-slate-300 hover:text-white border border-slate-700 text-xs font-bold transition">
            特大 A++ (130%)
          </button>
        </div>
      </div>

      <!-- Gemini GEM 快速連動設定 -->
      <div class="bg-slate-950/70 rounded-2xl p-3.5 border border-slate-800 text-xs space-y-2.5">
        <div class="flex items-center justify-between">
          <span class="text-slate-200 font-bold flex items-center gap-1.5 text-sm">
            <span>✨</span><span>Gemini GEM 快速連動</span>
          </span>
          <span class="text-[10px] text-emerald-400 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40 font-semibold">已支援一鍵複製</span>
        </div>
        <p class="text-slate-400 text-xs leading-relaxed">
          點擊任一小卡「📋 複製」會自動在內容最前方加上「<strong class="text-emerald-400">詳細說明：</strong>」，方便直接貼入您的 Gemini 客製化智能體 (GEM) 查詢知識庫。若填入 GEM 網址，複製時可一鍵直達開啟：
        </p>
        <div class="space-y-2 pt-1">
          <input 
            type="url" 
            id="gem-url-input" 
            placeholder="例如: https://gemini.google.com/gem/..." 
            class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-xs text-slate-100 placeholder-slate-500 focus:outline-none focus:border-cyan-500"
            onchange="saveGemUrl(this.value)"
          />
          <div class="flex justify-between items-center text-xs text-slate-500">
            <span>未填寫時點擊將開啟 Gemini 首頁</span>
            <button onclick="testOpenGem()" class="text-cyan-400 hover:underline font-medium">測試開啟 ↗</button>
          </div>
        </div>
      </div>

      <!-- 進度管理與快取 -->
      <div class="space-y-2 pt-2 border-t border-slate-800">
        <div class="text-[11px] font-bold text-slate-400">資料與快取管理</div>
        <div class="grid grid-cols-2 gap-2">
          <button onclick="resetAllProgress()" class="py-2 px-3 rounded-xl bg-rose-500/15 text-rose-300 border border-rose-500/30 text-xs font-bold hover:bg-rose-500/25 active:scale-95 transition">
            🗑️ 重置進度
          </button>
          <button onclick="forceRefreshCache()" class="py-2 px-3 rounded-xl bg-cyan-500/15 text-cyan-300 border border-cyan-500/30 text-xs font-bold hover:bg-cyan-500/25 active:scale-95 transition">
            🔄 強制更新
          </button>
        </div>
      </div>

      <div class="pt-2">
        <button onclick="toggleSettingsModal()" class="w-full py-2.5 rounded-xl bg-slate-800 text-slate-300 text-xs font-bold hover:bg-slate-700 active:scale-95 transition">
          關閉
        </button>
      </div>
    </div>
  </div>

  <!-- 實戰模矩速算彈窗 (Modules Modal) -->
  <div id="modules-modal" class="fixed inset-0 z-50 bg-slate-950/85 backdrop-blur-md flex items-center justify-center p-3 hidden" onclick="if(event.target===this) closeModulesModal()">
    <div class="bg-slate-900 border border-slate-700 rounded-3xl max-w-lg w-full p-5 space-y-4 shadow-2xl relative max-h-[88vh] flex flex-col">
      <div class="flex justify-between items-center border-b border-slate-800 pb-3 shrink-0">
        <div class="flex items-center space-x-2">
          <span class="text-xl">📏</span>
          <h3 class="text-base font-black text-white">實戰模矩與速算資料庫</h3>
        </div>
        <button onclick="closeModulesModal()" class="w-8 h-8 rounded-full bg-slate-800 text-slate-400 hover:text-white flex items-center justify-center text-xs">
          ✕
        </button>
      </div>
      <div class="overflow-y-auto space-y-3.5 pr-1 flex-1" id="modules-list-container">
        <!-- 動態渲染 5 大模矩項目 -->
      </div>
      <div class="pt-2 border-t border-slate-800 shrink-0">
        <button onclick="closeModulesModal()" class="w-full py-2.5 rounded-xl bg-slate-800 text-slate-300 text-xs font-bold hover:bg-slate-700 transition">
          關閉退出
        </button>
      </div>
    </div>
  </div>

  <!-- 歷屆手繪大卷觀摩彈窗 (Scrolls Modal) -->
  <div id="scrolls-modal" class="fixed inset-0 z-50 bg-slate-950/90 backdrop-blur-md flex items-center justify-center p-3 hidden" onclick="if(event.target===this) closeScrollsModal()">
    <div class="bg-slate-900 border border-slate-700 rounded-3xl max-w-xl w-full p-5 space-y-4 shadow-2xl relative max-h-[92vh] flex flex-col">
      <div class="flex justify-between items-center border-b border-slate-800 pb-3 shrink-0">
        <div class="flex items-center space-x-2">
          <span class="text-xl">📜</span>
          <div>
            <h3 class="text-base font-black text-white">名師手繪範卷 ＆ 構思草稿觀摩</h3>
            <p class="text-[11px] text-amber-400">名師練習卷（非官方試題解答）正卷 ＋ 構思草稿 8 幅（支援手勢縮放）</p>
          </div>
        </div>
        <button onclick="closeScrollsModal()" class="w-8 h-8 rounded-full bg-slate-800 text-slate-400 hover:text-white flex items-center justify-center text-xs">
          ✕
        </button>
      </div>
      <div class="flex space-x-2 border-b border-slate-800 pb-2 overflow-x-auto no-scrollbar shrink-0" id="scrolls-year-tabs">
        <!-- 動態渲染 112~109 年份切換 -->
      </div>
      <div class="overflow-y-auto space-y-4 pr-1 flex-1" id="scrolls-content-box">
        <!-- 動態渲染選定年份之正卷與草稿 -->
      </div>
      <div class="pt-2 border-t border-slate-800 shrink-0">
        <button onclick="closeScrollsModal()" class="w-full py-2.5 rounded-xl bg-slate-800 text-slate-300 text-xs font-bold hover:bg-slate-700 transition">
          關閉退出
        </button>
      </div>
    </div>
  </div>

  <!-- 全螢幕手勢縮放檢視燈箱 (Interactive Zoom/Pan Lightbox) -->
  <div id="diagram-lightbox" class="fixed inset-0 z-50 bg-slate-950/95 backdrop-blur-md flex items-center justify-center p-2 hidden select-none touch-none overflow-hidden" onclick="handleLightboxBackdropClick(event)">
    <!-- 頂部控制工具列 -->
    <div class="absolute top-4 right-4 z-60 flex items-center space-x-2" onclick="event.stopPropagation()">
      <button onclick="zoomInLightbox()" class="w-8 h-8 rounded-full bg-slate-850 hover:bg-slate-750 text-slate-200 border border-slate-700 text-xs font-bold shadow-lg flex items-center justify-center active:scale-90 transition">
        ➕
      </button>
      <button onclick="zoomOutLightbox()" class="w-8 h-8 rounded-full bg-slate-850 hover:bg-slate-750 text-slate-200 border border-slate-700 text-xs font-bold shadow-lg flex items-center justify-center active:scale-90 transition">
        ➖
      </button>
      <button onclick="resetLightboxZoom()" class="px-2.5 h-8 rounded-full bg-slate-850 hover:bg-slate-750 text-slate-200 border border-slate-700 text-[11px] font-bold shadow-lg flex items-center space-x-1 active:scale-90 transition">
        <span>↺ 1x</span>
      </button>
      <button onclick="toggleLightboxRotate()" class="px-2.5 h-8 rounded-full bg-slate-850 hover:bg-slate-750 text-slate-200 border border-slate-700 text-[11px] font-bold shadow-lg flex items-center space-x-1 active:scale-90 transition">
        <span>🔄 橫/直</span>
      </button>
      <button onclick="closeDiagramLightbox()" class="w-8 h-8 rounded-full bg-slate-800 text-slate-200 hover:text-white flex items-center justify-center font-bold text-sm shadow-lg border border-slate-700 active:scale-90 transition">
        ✕
      </button>
    </div>

    <!-- 底部操作提示 -->
    <div class="absolute bottom-3 left-0 right-0 text-center text-[11px] text-slate-400 pointer-events-none flex justify-center items-center space-x-3 bg-slate-950/60 py-1 backdrop-blur-sm">
      <span>🤏 雙指捏合縮放 (Pinch)</span>
      <span>•</span>
      <span>👆 滑動平移 (Drag)</span>
      <span>•</span>
      <span>⚡ 雙擊切換 2.5x</span>
    </div>

    <!-- 縮放視圖容器 -->
    <div id="lightbox-content-box" class="bg-white rounded-2xl p-2 shadow-2xl flex items-center justify-center overflow-hidden max-w-[95vw] max-h-[88vh]" style="transform-origin: center center;" onclick="event.stopPropagation()">
    </div>
  </div>

  <!-- 資料庫核心數據 -->
  <script>
    const SITE_DATA = {json_str};
  </script>

  <!-- APP 邏輯控制腳本 -->
  <script>
    // ==========================================
    // 全域手勢縮放燈箱驅動 (Pinch-to-zoom & Pan)
    // ==========================================
    let isLightboxRotated = false;
    let lbScale = 1.0;
    let lbPosX = 0;
    let lbPosY = 0;
    let lbIsPinching = false;
    let lbIsDragging = false;
    let lbStartDist = 0;
    let lbStartScale = 1.0;
    let lbStartX = 0;
    let lbStartY = 0;
    let lbStartPosX = 0;
    let lbStartPosY = 0;
    let lbLastTapTime = 0;

    function updateLightboxTransform(durationSec = 0) {{
      const box = document.getElementById('lightbox-content-box');
      if (!box) return;
      box.style.transition = durationSec > 0 ? `transform ${{durationSec}}s cubic-bezier(0.2, 0, 0, 1)` : 'none';
      const rot = isLightboxRotated ? 'rotate(90deg) ' : '';
      box.style.transform = `${{rot}}translate(${{lbPosX}}px, ${{lbPosY}}px) scale(${{lbScale}})`;
    }}

    function resetLightboxZoom() {{
      lbScale = 1.0;
      lbPosX = 0;
      lbPosY = 0;
      updateLightboxTransform(0.25);
    }}

    function zoomInLightbox() {{
      lbScale = Math.min(lbScale * 1.3, 4.5);
      updateLightboxTransform(0.2);
    }}

    function zoomOutLightbox() {{
      lbScale = Math.max(lbScale / 1.3, 1.0);
      if (lbScale <= 1.0) {{
        lbPosX = 0;
        lbPosY = 0;
      }}
      updateLightboxTransform(0.2);
    }}

    window.openDiagramLightbox = function(svgCode, title) {{
      const modal = document.getElementById('diagram-lightbox');
      const box = document.getElementById('lightbox-content-box');
      
      box.innerHTML = svgCode;
      const svg = box.querySelector('svg');
      if (svg) {{
        svg.style.width = '100%';
        svg.style.height = '100%';
        svg.style.maxHeight = '100%';
      }}

      modal.classList.remove('hidden');
      isLightboxRotated = false;
      resetLightboxDimensions();
      resetLightboxZoom();
    }};

    window.openImageLightbox = function(imgSrc, title) {{
      const modal = document.getElementById('diagram-lightbox');
      const box = document.getElementById('lightbox-content-box');
      
      box.innerHTML = `<img src="${{imgSrc}}" class="w-full h-full object-contain pointer-events-none" alt="${{title}}">`;
      modal.classList.remove('hidden');
      isLightboxRotated = false;
      resetLightboxDimensions();
      resetLightboxZoom();
    }};

    window.openCurrentDiagLightbox = function() {{
      const diag = SITE_DATA.diagrams[appState.diagramIndex || 0];
      if (!diag) return;
      if (currentDiagMode === 'sketch' && diag.sketch_image) {{
        window.openImageLightbox(diag.sketch_image, diag.header + ' 手繪臨摹原件');
      }} else if (diag.svg_code) {{
        window.openDiagramLightbox(diag.svg_code, diag.header);
      }} else if (diag.sketch_image) {{
        window.openImageLightbox(diag.sketch_image, diag.header + ' 手繪臨摹原件');
      }}
    }};

    function resetLightboxDimensions() {{
      const box = document.getElementById('lightbox-content-box');
      if (!box) return;
      if (isLightboxRotated) {{
        const h = window.innerHeight * 0.90;
        const w = window.innerWidth * 0.92;
        box.style.width = `${{h}}px`;
        box.style.height = `${{w}}px`;
        box.style.maxWidth = 'none';
        box.style.maxHeight = 'none';
      }} else {{
        box.style.width = '95vw';
        box.style.maxWidth = '850px';
        box.style.height = 'auto';
        box.style.maxHeight = '88vh';
      }}
    }}

    window.toggleLightboxRotate = function() {{
      isLightboxRotated = !isLightboxRotated;
      resetLightboxDimensions();
      updateLightboxTransform(0.25);
    }};

    window.closeDiagramLightbox = function() {{
      document.getElementById('diagram-lightbox').classList.add('hidden');
      resetLightboxZoom();
    }};

    function handleLightboxBackdropClick(e) {{
      if (lbScale > 1.1) {{
        resetLightboxZoom();
      }} else {{
        closeDiagramLightbox();
      }}
    }}

    // 綁定燈箱手勢事件 (Touch Pinch & Pan)
    const lbModal = document.getElementById('diagram-lightbox');
    lbModal.addEventListener('touchstart', (e) => {{
      if (e.touches.length === 2) {{
        lbIsPinching = true;
        lbIsDragging = false;
        lbStartDist = Math.hypot(e.touches[0].clientX - e.touches[1].clientX, e.touches[0].clientY - e.touches[1].clientY);
        lbStartScale = lbScale;
      }} else if (e.touches.length === 1) {{
        // 雙擊偵測
        const now = Date.now();
        if (now - lbLastTapTime < 300) {{
          if (lbScale > 1.2) {{
            resetLightboxZoom();
          }} else {{
            lbScale = 2.5;
            updateLightboxTransform(0.25);
          }}
          lbLastTapTime = 0;
          return;
        }}
        lbLastTapTime = now;

        lbIsDragging = true;
        lbIsPinching = false;
        lbStartX = e.touches[0].clientX;
        lbStartY = e.touches[0].clientY;
        lbStartPosX = lbPosX;
        lbStartPosY = lbPosY;
      }}
    }}, {{ passive: false }});

    lbModal.addEventListener('touchmove', (e) => {{
      if (lbIsPinching && e.touches.length === 2) {{
        e.preventDefault();
        const dist = Math.hypot(e.touches[0].clientX - e.touches[1].clientX, e.touches[0].clientY - e.touches[1].clientY);
        lbScale = Math.min(Math.max(lbStartScale * (dist / lbStartDist), 0.8), 4.5);
        updateLightboxTransform(0);
      }} else if (lbIsDragging && e.touches.length === 1 && lbScale > 1.05) {{
        e.preventDefault();
        const dx = e.touches[0].clientX - lbStartX;
        const dy = e.touches[0].clientY - lbStartY;
        if (isLightboxRotated) {{
          lbPosX = lbStartPosX + dy;
          lbPosY = lbStartPosY - dx;
        }} else {{
          lbPosX = lbStartPosX + dx;
          lbPosY = lbStartPosY + dy;
        }}
        updateLightboxTransform(0);
      }}
    }}, {{ passive: false }});

    lbModal.addEventListener('touchend', (e) => {{
      if (lbScale < 1.0) {{
        resetLightboxZoom();
      }} else if (lbScale > 4.0) {{
        lbScale = 4.0;
        updateLightboxTransform(0.2);
      }}
      if (e.touches.length < 2) lbIsPinching = false;
      if (e.touches.length === 0) lbIsDragging = false;
    }});

    // 桌機滾輪支援
    lbModal.addEventListener('wheel', (e) => {{
      e.preventDefault();
      if (e.deltaY < 0) {{
        lbScale = Math.min(lbScale * 1.2, 4.5);
      }} else {{
        lbScale = Math.max(lbScale / 1.2, 1.0);
      }}
      if (lbScale <= 1.0) {{
        lbPosX = 0;
        lbPosY = 0;
      }}
      updateLightboxTransform(0.15);
    }}, {{ passive: false }});

    // ==========================================
    // 全站字體大小動態縮放引擎 (Font Scale Engine)
    // ==========================================
    const FONT_SCALES = {{
      'normal': {{ scale: 100, label: '標準 (100%)', shortLabel: '字體' }},
      'large': {{ scale: 115, label: '大字 (115%)', shortLabel: '大字' }},
      'xlarge': {{ scale: 130, label: '特大 (130%)', shortLabel: '特大' }}
    }};
    let currentFontScale = 'normal';

    function setFontScale(scaleKey) {{
      if (!FONT_SCALES[scaleKey]) scaleKey = 'normal';
      currentFontScale = scaleKey;
      const config = FONT_SCALES[scaleKey];
      
      document.documentElement.style.fontSize = `${{(config.scale / 100) * 16}}px`;
      
      ['normal', 'large', 'xlarge'].forEach(k => {{
        const btn = document.getElementById(`font-btn-${{k}}`);
        if (btn) {{
          if (k === scaleKey) {{
            btn.className = "py-2.5 px-2 rounded-xl bg-emerald-500 text-slate-950 text-xs font-black transition";
          }} else {{
            btn.className = "py-2.5 px-2 rounded-xl bg-slate-800 text-slate-300 hover:text-white border border-slate-700 text-xs font-bold transition";
          }}
        }}
      }});

      const labelEl = document.getElementById('current-font-label');
      if (labelEl) labelEl.innerText = config.label;

      const headerText = document.getElementById('header-font-scale-text');
      if (headerText) headerText.innerText = config.shortLabel;

      localStorage.setItem('APP_FONT_SCALE', scaleKey);
    }}

    function cycleFontScale() {{
      const order = ['normal', 'large', 'xlarge'];
      const nextIdx = (order.indexOf(currentFontScale) + 1) % order.length;
      setFontScale(order[nextIdx]);
    }}

    function initFontScale() {{
      const saved = localStorage.getItem('APP_FONT_SCALE') || 'normal';
      setFontScale(saved);
    }}

    // ==========================================
    // 剪貼簿與 Gemini GEM 連動支援模組
    // ==========================================
    let toastTimer = null;

    function showToast(msg, icon = '📋', showGemBtn = true) {{
      const toast = document.getElementById('global-toast');
      const msgEl = document.getElementById('toast-msg');
      const iconEl = document.getElementById('toast-icon');
      const gemBtn = document.getElementById('toast-gem-btn');
      if (!toast || !msgEl) return;

      msgEl.innerText = msg;
      if (iconEl) iconEl.innerText = icon;

      if (gemBtn) {{
        if (showGemBtn) {{
          gemBtn.classList.remove('hidden');
        }} else {{
          gemBtn.classList.add('hidden');
        }}
      }}

      toast.classList.remove('opacity-0', 'translate-y-4');
      toast.classList.add('opacity-100', 'translate-y-0');

      if (toastTimer) clearTimeout(toastTimer);
      toastTimer = setTimeout(() => {{
        toast.classList.remove('opacity-100', 'translate-y-0');
        toast.classList.add('opacity-0', 'translate-y-4');
      }}, 2500);
    }}

    function copyTextToClipboard(text, successMsg = '已複製！', options = {{}}) {{
      const showGem = options.showGemBtn !== false;
      const onDone = () => {{
        showToast(successMsg, '📋', showGem);
        if (navigator.vibrate) {{
          try {{ navigator.vibrate(40); }} catch(e) {{}}
        }}
      }};

      if (navigator.clipboard && navigator.clipboard.writeText) {{
        navigator.clipboard.writeText(text).then(onDone).catch(() => {{
          fallbackCopyText(text, onDone);
        }});
      }} else {{
        fallbackCopyText(text, onDone);
      }}
    }}

    function fallbackCopyText(text, callback) {{
      const textArea = document.createElement("textarea");
      textArea.value = text;
      textArea.style.position = "fixed";
      textArea.style.left = "-9999px";
      textArea.style.top = "0";
      document.body.appendChild(textArea);
      textArea.focus();
      textArea.select();
      try {{
        document.execCommand('copy');
        if (callback) callback();
      }} catch (err) {{
        alert("複製失敗，請手動選取文字");
      }}
      document.body.removeChild(textArea);
    }}

    function flashCopyBtn(btn) {{
      if (!btn) return;
      const originalHtml = btn.innerHTML;
      btn.innerHTML = `<span>✓</span><span>已複製</span>`;
      btn.classList.add('!bg-emerald-700', '!text-white', '!border-emerald-500');
      setTimeout(() => {{
        btn.innerHTML = originalHtml;
        btn.classList.remove('!bg-emerald-700', '!text-white', '!border-emerald-500');
      }}, 1600);
    }}

    function copyGridCard(id, btnElement) {{
      const g = SITE_DATA.single_grids.find(item => item.id === id);
      if (!g) return;
      const text = `詳細說明：\n${{g.topic_header}} 【${{g.func_abbr}}】格 ${{g.grid_no}}\n${{g.title}}\n▸ 關鍵數字：${{g.number}}\n🔑 關鍵詞：${{g.keywords}}\n▢ 配圖：${{g.diagram}}`;
      copyTextToClipboard(text, '已複製小卡！已加上「詳細說明：」', {{ showGemBtn: true }});
      flashCopyBtn(btnElement);
    }}

    function copyCurrentNumberCard(btnElement) {{
      const nums = SITE_DATA.numbers;
      const idx = appState.numberIndex % nums.length;
      const item = nums[idx];
      if (!item) return;
      const kws = (item.keywords && item.keywords.length > 0) ? item.keywords.join('、') : '';
      const text = `詳細說明：\n【審題關鍵字反射卡】類別：${{item.category}}（第 ${{idx + 1}}/${{nums.length}} 題）\n🔑 審題關鍵字：${{kws}}\n🎯 審題情境：${{item.scenario || item.content}}\n⚡ 3秒手繪反射決策：${{item.reflex || item.usage}}\n▸ 黃金量化標準：${{item.number}}\n📜 法規出處：${{item.source}}\n🖼️ 聯動手繪圖卡：${{item.linked_diag_name || '無'}}`;
      copyTextToClipboard(text, '已複製審題反射卡！已加上「詳細說明：」', {{ showGemBtn: true }});
      flashCopyBtn(btnElement);
    }}

    function copyCurrentStrategyCard(btnElement) {{
      const cards = (typeof getFilteredStrategyCards === 'function') ? getFilteredStrategyCards() : (SITE_DATA.strategy_cards || []);
      const idx = (appState.strategyIndex || 0) % cards.length;
      const card = cards[idx];
      if (!card) return;
      const text = `詳細說明：\n【審題快刀】年份：${{card.year}}｜主題：${{card.theme}}\n題目：${{card.title}}\n破題套路：${{card.expert_decisions ? card.expert_decisions.join('；') : ''}}\n挑戰自問：${{card.challenges ? card.challenges.join('；') : ''}}`;
      copyTextToClipboard(text, '已複製審題卡！已加上「詳細說明：」', {{ showGemBtn: true }});
      flashCopyBtn(btnElement);
    }}

    function copyCurrentDiagramCard(btnElement) {{
      const diag = SITE_DATA.diagrams[appState.diagramIndex || 0];
      if (!diag) return;
      const checkStr = (diag.checklist && diag.checklist.length > 0) ? diag.checklist.join('、') : '無';
      const text = `詳細說明：\n【萬用圖卡】圖名：${{diag.header}}\n跨題用途：${{diag.used_for}}\n作圖步驟：${{diag.draw_step}}\n易犯陷阱：${{diag.pitfall}}\n必備檢核：${{checkStr}}\n手繪技法：${{diag.sketch_techniques || '無'}}`;
      copyTextToClipboard(text, '已複製圖卡！已加上「詳細說明：」', {{ showGemBtn: true }});
      flashCopyBtn(btnElement);
    }}

    function openGemWindow() {{
      const url = localStorage.getItem('USER_GEM_URL') || 'https://gemini.google.com/app';
      window.open(url, '_blank');
    }}

    function loadGemUrl() {{
      const url = localStorage.getItem('USER_GEM_URL') || '';
      const input = document.getElementById('gem-url-input');
      if (input) input.value = url;
    }}

    function saveGemUrl(url) {{
      localStorage.setItem('USER_GEM_URL', url.trim());
      showToast('GEM 網址已儲存！', '💾', false);
    }}

    function testOpenGem() {{
      openGemWindow();
    }}

    // ==========================================
    // 萬用圖卡顯示模式切換 (SVG vs 手繪臨摹)
    // ==========================================
    let currentDiagMode = 'svg';

    function switchDiagMode(mode) {{
      currentDiagMode = mode;
      const btnSvg = document.getElementById('diag-btn-svg');
      const btnSketch = document.getElementById('diag-btn-sketch');
      if (mode === 'svg') {{
        if (btnSvg) btnSvg.className = "flex-1 py-1.5 rounded-lg text-xs font-bold bg-amber-500 text-slate-950 transition";
        if (btnSketch) btnSketch.className = "flex-1 py-1.5 rounded-lg text-xs font-bold text-slate-400 hover:text-white transition";
      }} else {{
        if (btnSvg) btnSvg.className = "flex-1 py-1.5 rounded-lg text-xs font-bold text-slate-400 hover:text-white transition";
        if (btnSketch) btnSketch.className = "flex-1 py-1.5 rounded-lg text-xs font-bold bg-emerald-500 text-slate-950 transition";
      }}
      renderDiagramDetail(appState.diagramIndex || 0);
    }}

    // ==========================================
    // 實戰模矩速算與歷屆大卷彈窗模組
    // ==========================================
    function openModulesModal() {{
      const modal = document.getElementById('modules-modal');
      if (!modal) return;
      modal.classList.remove('hidden');
      renderModulesList();
    }}

    function closeModulesModal() {{
      const modal = document.getElementById('modules-modal');
      if (modal) modal.classList.add('hidden');
    }}

    function renderModulesList() {{
      const container = document.getElementById('modules-list-container');
      if (!container || !SITE_DATA.modules) return;
      container.innerHTML = SITE_DATA.modules.map(m => `
        <div class="bg-slate-950/80 p-4 rounded-2xl border border-slate-800 space-y-2.5">
          <!-- 頂部標題列：分行橫式排版，標題完整舒展，徹底解決手機直排跑版 -->
          <div class="space-y-1.5 border-b border-slate-800/80 pb-2">
            <h4 class="text-base font-black text-white flex items-center gap-2">
              <span class="text-lg">📏</span><span>${{m.title}}</span>
            </h4>
            <div class="flex flex-wrap items-center justify-between gap-1.5">
              <p class="text-xs text-teal-400 font-semibold">${{m.subtitle}}</p>
              <span class="text-xs px-2.5 py-1 rounded-xl bg-teal-950 text-teal-300 font-mono font-bold border border-teal-800/40 shadow-sm">
                ${{m.key_numbers}}
              </span>
            </div>
          </div>
          <div class="text-xs text-slate-200 whitespace-pre-line leading-relaxed bg-slate-900/70 p-3 rounded-xl border border-slate-800/60">
            ${{m.details}}
          </div>
          <div class="text-[11px] text-amber-300 bg-amber-950/30 px-3 py-2 rounded-xl border border-amber-800/30 leading-relaxed">
            💡 考場技巧：${{m.exam_usage}}
          </div>
        </div>
      `).join('');
    }}

    let currentScrollYearIdx = 0;

    function openScrollsModal() {{
      const modal = document.getElementById('scrolls-modal');
      if (!modal) return;
      modal.classList.remove('hidden');
      currentScrollYearIdx = 0;
      renderScrollsTabs();
      renderScrollsContent(0);
    }}

    function closeScrollsModal() {{
      const modal = document.getElementById('scrolls-modal');
      if (modal) modal.classList.add('hidden');
    }}

    function renderScrollsTabs() {{
      const container = document.getElementById('scrolls-year-tabs');
      if (!container || !SITE_DATA.exam_scrolls) return;
      container.innerHTML = SITE_DATA.exam_scrolls.map((s, idx) => `
        <button onclick="switchScrollYear(${{idx}})" class="px-3 py-1.5 rounded-xl text-xs font-bold whitespace-nowrap transition ${{
          idx === currentScrollYearIdx ? 'bg-amber-500 text-slate-950' : 'bg-slate-800 text-slate-300 hover:text-white'
        }}">
          ${{s.year.split(' ')[0]}}
        </button>
      `).join('');
    }}

    function switchScrollYear(idx) {{
      currentScrollYearIdx = idx;
      renderScrollsTabs();
      renderScrollsContent(idx);
    }}

    function renderScrollsContent(idx) {{
      const container = document.getElementById('scrolls-content-box');
      if (!container || !SITE_DATA.exam_scrolls) return;
      const s = SITE_DATA.exam_scrolls[idx];
      if (!s) return;

      container.innerHTML = `
        <div class="space-y-1 pb-1">
          <div class="flex justify-between items-center text-xs">
            <span class="px-2 py-0.5 rounded-md bg-amber-950 text-amber-300 font-bold border border-amber-800/40">${{s.year}}</span>
            <span class="text-slate-400 font-medium">${{s.theme}}</span>
          </div>
          <h4 class="text-sm font-black text-white">${{s.title}}</h4>
        </div>

        <!-- 雙卷並列卡片 (正卷 vs 草稿) -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
          <!-- 正卷 -->
          <div class="bg-slate-950/80 p-3 rounded-2xl border border-slate-800 space-y-2">
            <div class="flex justify-between items-center text-xs">
              <span class="font-bold text-emerald-400 flex items-center gap-1">
                <span>📐</span><span>範卷正卷・手繪全圖</span>
              </span>
              <span class="text-[10px] text-cyan-400 cursor-pointer" onclick="window.openImageLightbox('${{s.final_image}}', '${{s.title}} 正卷全圖')">
                🔍 點擊手勢縮放
              </span>
            </div>
            <div onclick="window.openImageLightbox('${{s.final_image}}', '${{s.title}} 正卷全圖')" class="bg-white rounded-xl p-1.5 flex items-center justify-center overflow-hidden border border-slate-700 min-h-[190px] cursor-pointer relative shadow-inner">
              <img src="${{s.final_image}}" class="w-full max-h-[220px] object-contain rounded" alt="${{s.title}} 正卷全圖" onerror="this.src='apple-touch-icon.png'">
              <div class="absolute bottom-2 right-2 bg-slate-900/85 backdrop-blur-sm text-cyan-300 text-[10px] px-2 py-0.5 rounded-full border border-cyan-500/30">
                🔍 雙指捏合縮放
              </div>
            </div>
          </div>

          <!-- 草稿 -->
          <div class="bg-slate-950/80 p-3 rounded-2xl border border-slate-800 space-y-2">
            <div class="flex justify-between items-center text-xs">
              <span class="font-bold text-amber-400 flex items-center gap-1">
                <span>💡</span><span>構思草稿・概念全圖</span>
              </span>
              <span class="text-[10px] text-cyan-400 cursor-pointer" onclick="window.openImageLightbox('${{s.draft_image}}', '${{s.title}} 草稿全圖')">
                🔍 點擊手勢縮放
              </span>
            </div>
            <div onclick="window.openImageLightbox('${{s.draft_image}}', '${{s.title}} 草稿全圖')" class="bg-white rounded-xl p-1.5 flex items-center justify-center overflow-hidden border border-slate-700 min-h-[190px] cursor-pointer relative shadow-inner">
              <img src="${{s.draft_image}}" class="w-full max-h-[220px] object-contain rounded" alt="${{s.title}} 草稿全圖" onerror="this.src='apple-touch-icon.png'">
              <div class="absolute bottom-2 right-2 bg-slate-900/85 backdrop-blur-sm text-cyan-300 text-[10px] px-2 py-0.5 rounded-full border border-cyan-500/30">
                🔍 雙指捏合縮放
              </div>
            </div>
          </div>
        </div>

        <div class="bg-emerald-950/30 p-3 rounded-xl border border-emerald-800/40 text-xs text-emerald-200 leading-relaxed">
          <span class="font-bold text-emerald-300 block mb-0.5">✨ 卷面臨摹研讀要點：</span>
          ${{s.techniques}}
        </div>
      `;
    }}

    // ==========================================
    // 狀態持久化管理 (LocalStorage)
    // ==========================================
    const STATE_KEY = 'SITE_PLANNING_APP_STATE_V1';
    let appState = {{
      currentView: 'capsule',
      numberIndex: 0,
      numMode: 'reflex',
      masteredNumbers: {{}},
      sopStreak: 0,
      gridRevealed: {{}},
      diagramIndex: 0,
      strategyIndex: 0
    }};

    function loadState() {{
      initFontScale();
      loadGemUrl();
      const saved = localStorage.getItem(STATE_KEY);
      if (saved) {{
        try {{
          appState = Object.assign(appState, JSON.parse(saved));
        }} catch(e) {{}}
      }}
      updateDashboardStats();
    }}

    function saveState() {{
      localStorage.setItem(STATE_KEY, JSON.stringify(appState));
      updateDashboardStats();
    }}

    function updateDashboardStats() {{
      const masteredCount = Object.keys(appState.masteredNumbers || {{}}).filter(k => appState.masteredNumbers[k]).length;
      const totalNums = SITE_DATA.numbers.length;
      const numRate = Math.round((masteredCount / totalNums) * 100);
      document.getElementById('stats-num-rate').innerText = `${{numRate}}%`;
      document.getElementById('stats-sop-streak').innerText = `${{appState.sopStreak || 0}} 題`;
      document.getElementById('stats-grid-count').innerText = `${{Object.keys(appState.gridRevealed || {{}}).length}}/72`;
    }}

    // 視圖切換
    function switchView(viewName) {{
      appState.currentView = viewName;
      document.querySelectorAll('.view-panel').forEach(el => el.classList.add('hidden'));
      const activePanel = document.getElementById(`view-${{viewName}}`);
      if (activePanel) activePanel.classList.remove('hidden');

      document.querySelectorAll('.nav-btn').forEach(btn => {{
        if (btn.getAttribute('data-view') === viewName) {{
          btn.classList.add('text-emerald-400');
          btn.classList.remove('text-slate-400');
        }} else {{
          btn.classList.remove('text-emerald-400');
          btn.classList.add('text-slate-400');
        }}
      }});

      window.scrollTo({{ top: 0, behavior: 'smooth' }});
      saveState();

      if (viewName === 'numbers') renderNumberCard();
      if (viewName === 'sop') initSopQuiz();
      if (viewName === 'grids') renderGridCards();
      if (viewName === 'diagrams') renderDiagramDetail(appState.diagramIndex || 0);
      if (viewName === 'strategy') renderStrategyPager();
    }}

    // ==========================================
    // 模組 2: 作圖 SOP 肌肉記憶
    // ==========================================
    let currentSopQuiz = null;

    function switchSopTab(tabName) {{
      ['blitz', 'rules', 'colors', 'list'].forEach(t => {{
        document.getElementById(`sop-sub-${{t}}`).classList.add('hidden');
        const tabBtn = document.getElementById(`sop-tab-${{t}}`);
        tabBtn.classList.remove('bg-emerald-500', 'text-slate-950', 'font-bold');
        tabBtn.classList.add('text-slate-400');
      }});

      document.getElementById(`sop-sub-${{tabName}}`).classList.remove('hidden');
      const activeBtn = document.getElementById(`sop-tab-${{tabName}}`);
      activeBtn.classList.add('bg-emerald-500', 'text-slate-950', 'font-bold');
      activeBtn.classList.remove('text-slate-400');

      if (tabName === 'rules') renderSopRules();
      if (tabName === 'colors') renderSopColors();
      if (tabName === 'list') renderSopList();
    }}

    function initSopQuiz() {{
      const questions = SITE_DATA.sop.blitz_questions;
      currentSopQuiz = questions[Math.floor(Math.random() * questions.length)];
      
      document.getElementById('sop-quiz-question').innerText = currentSopQuiz.question;
      document.getElementById('sop-quiz-streak').innerText = `🔥 連勝: ${{appState.sopStreak}} 題`;
      document.getElementById('sop-quiz-feedback').classList.add('hidden');

      const options = [currentSopQuiz.correct, ...currentSopQuiz.wrong_options].sort(() => Math.random() - 0.5);
      const container = document.getElementById('sop-quiz-options');
      container.innerHTML = '';

      options.forEach(opt => {{
        const btn = document.createElement('button');
        btn.className = "w-full py-4 px-5 rounded-2xl bg-slate-900 hover:bg-slate-850 active:scale-[0.99] border border-slate-800 text-left text-sm md:text-base font-bold text-slate-200 transition shadow-sm leading-relaxed flex items-center justify-between";
        btn.innerHTML = `<span>${{opt}}</span><span class="text-slate-500">→</span>`;
        btn.onclick = () => handleSopAnswer(opt, btn);
        container.appendChild(btn);
      }});
    }}

    function handleSopAnswer(selected, btnElement) {{
      const isCorrect = (selected === currentSopQuiz.correct);
      const feedbackBox = document.getElementById('sop-quiz-feedback');
      const titleBox = document.getElementById('sop-feedback-title');
      const textBox = document.getElementById('sop-feedback-text');

      document.querySelectorAll('#sop-quiz-options button').forEach(b => b.disabled = true);

      if (isCorrect) {{
        btnElement.classList.add('bg-emerald-950/80', 'border-emerald-500', 'text-emerald-300');
        titleBox.innerHTML = '<span class="text-emerald-400">🎉 答對了！形成肌肉記憶！</span>';
        appState.sopStreak = (appState.sopStreak || 0) + 1;
      }} else {{
        btnElement.classList.add('bg-rose-950/80', 'border-rose-500', 'text-rose-300');
        titleBox.innerHTML = `<span class="text-rose-400">❌ 答錯了！正確應接：${{currentSopQuiz.correct}}</span>`;
        appState.sopStreak = 0;
      }}

      textBox.innerText = currentSopQuiz.explanation;
      feedbackBox.classList.remove('hidden');
      document.getElementById('sop-quiz-streak').innerText = `🔥 連勝: ${{appState.sopStreak}} 題`;
      saveState();
    }}

    function loadNextSopQuiz() {{
      initSopQuiz();
    }}

    function renderSopRules() {{
      const container = document.getElementById('sop-rules-container');
      container.innerHTML = '';
      SITE_DATA.sop.iron_rules.forEach(r => {{
        container.innerHTML += `
          <div class="bg-slate-900 p-5 rounded-2xl border border-slate-800 space-y-3 shadow-lg">
            <span class="text-amber-400 font-black text-base md:text-lg block">🛡️ ${{r.title}}</span>
            <div class="text-sm md:text-base text-white font-bold bg-slate-950 p-3 rounded-xl border border-slate-800">
              👉 ${{r.key_action}}
            </div>
            <p class="text-sm md:text-base text-slate-200 leading-relaxed italic">"${{r.quote}}"</p>
            <p class="text-xs md:text-sm text-slate-400 leading-relaxed pt-1 border-t border-slate-800/80">💡 核心理由：${{r.why}}</p>
          </div>
        `;
      }});
    }}

    function renderSopColors() {{
      const container = document.getElementById('sop-colors-container');
      container.innerHTML = '';
      SITE_DATA.sop.color_markings.forEach(c => {{
        container.innerHTML += `
          <div class="bg-slate-900 p-4 rounded-2xl border border-slate-800 space-y-2.5 shadow-md">
            <div class="flex items-center justify-between">
              <span class="px-3 py-1 rounded-lg text-sm font-black ${{c.css_class}}">${{c.color}}色標記</span>
              <span class="text-sm font-bold text-slate-200">${{c.target}}</span>
            </div>
            <div class="text-xs md:text-sm text-slate-300 space-y-1.5 pt-1 border-t border-slate-800/60">
              ${{c.examples.map(ex => `<div>• ${{ex}}</div>`).join('')}}
            </div>
          </div>
        `;
      }});
    }}

    function renderSopList() {{
      const container = document.getElementById('sop-list-container');
      container.innerHTML = `
        <div class="bg-gradient-to-br from-cyan-950/60 to-slate-900 p-4 rounded-2xl border border-cyan-800/50 space-y-1.5 shadow-md">
          <div class="flex items-center justify-between text-xs font-bold text-cyan-300">
            <span>⏱️ 敷地實戰 3.5 小時大圖作圖時間分配</span>
            <span class="font-mono bg-cyan-900/60 px-2 py-0.5 rounded text-[11px]">總作圖 210 分鐘</span>
          </div>
          <p class="text-xs text-slate-300 leading-relaxed">
            考試 4 小時扣除申論約 30 分鐘，大圖實作鎖定 <b>210 分鐘（3.5 小時）</b>：<br>
            • <b>階段一 審題決策</b>：25% (52.5分) ➔ 審題10%不可壓縮，量體5分定案<br>
            • <b>階段二 正圖60%</b>：35% (73.5分) ➔ 全圖粗線骨架到位，絕不單張畫滿<br>
            • <b>階段三 加深檢核</b>：40% (84.0分) ➔ 全圖加深52.5m ＋ 法規21m ＋ 查漏10.5m
          </p>
        </div>
      `;
      SITE_DATA.sop.steps.forEach(s => {{
        container.innerHTML += `
          <div class="bg-slate-900 p-4 rounded-2xl border border-slate-800 flex items-start space-x-3.5 shadow-sm">
            <div class="w-8 h-8 rounded-xl bg-slate-800 border border-slate-700 flex items-center justify-center font-black text-sm text-cyan-400 flex-shrink-0">
              ${{s.step}}
            </div>
            <div class="flex-1 text-xs md:text-sm">
              <div class="flex justify-between items-center">
                <span class="font-bold text-white text-sm md:text-base">${{s.name}}</span>
                <span class="text-xs text-slate-400 font-mono font-bold">${{s.ratio}}</span>
              </div>
              <div class="text-[11px] text-cyan-300 font-mono font-bold mt-1 bg-slate-950/70 px-2.5 py-1 rounded-lg border border-slate-800 inline-block">
                ⏱️ 建議用時：${{s.minutes_35h || s.ratio}}
              </div>
              <p class="text-slate-200 mt-1.5 leading-relaxed text-xs md:text-sm">${{s.key_points}}</p>
              <p class="text-xs text-slate-400 mt-1 font-mono font-medium">下一動作：${{s.next_step_name}}</p>
            </div>
          </div>
        `;
      }});
    }}

    // ==========================================
    // 模組 3: 84 項審題關鍵字反射卡
    // ==========================================
    let isNumCardFlipped = false;

    function jumpToCurrentLinkedDiag() {{
      const nums = SITE_DATA.numbers;
      const idx = appState.numberIndex % nums.length;
      const item = nums[idx];
      if (!item || !item.linked_diag_id || !SITE_DATA.diagrams) return;
      const diagIdx = SITE_DATA.diagrams.findIndex(d => d.id === item.linked_diag_id);
      if (diagIdx !== -1) {{
        appState.diagramIndex = diagIdx;
        switchView('diagrams');
        switchDiagMode('sketch');
        showToast(`已跳轉至「${{item.linked_diag_name}}」臨摹！`, '✏️', false);
      }}
    }}

    const STATUS_DESC = {{
      '✓': '✓ 本次查證(115.9)',
      '○': '○ 沿用既有查證',
      '△': '△ 設計參考值',
      '⚠': '⚠ 草案/近期修正'
    }};

    function renderNumberCard() {{
      const nums = SITE_DATA.numbers;
      const idx = appState.numberIndex % nums.length;
      const item = nums[idx];
      const isReflex = true;

      isNumCardFlipped = false;
      document.getElementById('num-card-inner').classList.remove('rotate-y-180');

      document.getElementById('num-card-cat').innerText = item.category;
      document.getElementById('num-card-index').innerText = `${{idx + 1}} / ${{nums.length}}`;

      // 正面關鍵字 Chips 與題幹
      const kwWrap = document.getElementById('num-card-keywords-wrap');
      const kwContainer = document.getElementById('num-card-keywords-container');
      const promptHint = document.getElementById('num-card-prompt-hint');
      const frontTapHint = document.getElementById('num-card-front-tap-hint');

      if (item.keywords && item.keywords.length > 0) {{
        kwWrap.classList.remove('hidden');
        kwContainer.innerHTML = item.keywords.map(k => `
          <span class="px-2.5 py-1 rounded-xl bg-cyan-950/80 text-cyan-300 font-bold border border-cyan-700/50 text-xs shadow-sm">
            # ${{k}}
          </span>
        `).join('');
        promptHint.innerText = "🎯 考題審題情境反射提問：";
        document.getElementById('num-card-question').innerText = item.scenario || item.content;
        frontTapHint.innerText = "👆 點擊卡片翻面看 3 秒手繪反射決策 ＆ 黃金數據";
      }} else {{
        kwWrap.classList.add('hidden');
        promptHint.innerText = "請在腦中回想關鍵數字：";
        document.getElementById('num-card-question').innerText = item.content;
        frontTapHint.innerText = "👆 點擊卡片翻面看數字答案";
      }}

      // 背面內容渲染
      const backTitle = document.getElementById('num-card-back-title');
      const reflexBox = document.getElementById('num-card-reflex-box');
      backTitle.innerHTML = '<span>⚡</span><span>3 秒手繪反射決策</span>';
      reflexBox.classList.remove('hidden');
      document.getElementById('num-card-reflex-text').innerText = item.reflex || item.usage;

      document.getElementById('num-card-answer').innerText = item.number;
      document.getElementById('num-card-source').innerText = item.source;
      document.getElementById('num-card-usage').innerText = item.usage;
      document.getElementById('num-card-status').innerText = STATUS_DESC[item.status] || (item.status ? `${{item.status}}` : '最新查證');

      // 聯動手繪圖卡按鈕
      const jumpBox = document.getElementById('num-card-jump-box');
      const jumpNameEl = document.getElementById('num-card-jump-name');
      if (item.linked_diag_name) {{
        jumpBox.classList.remove('hidden');
        jumpNameEl.innerText = item.linked_diag_name;
      }} else {{
        jumpBox.classList.add('hidden');
      }}

      renderNumberTabs();
    }}

    function flipNumberCard() {{
      isNumCardFlipped = !isNumCardFlipped;
      const card = document.getElementById('num-card-inner');
      if (isNumCardFlipped) {{
        card.classList.add('rotate-y-180');
      }} else {{
        card.classList.remove('rotate-y-180');
      }}
    }}

    function nextNumberCard() {{
      appState.numberIndex = (appState.numberIndex + 1) % SITE_DATA.numbers.length;
      renderNumberCard();
      saveState();
    }}

    function prevNumberCard() {{
      appState.numberIndex = (appState.numberIndex - 1 + SITE_DATA.numbers.length) % SITE_DATA.numbers.length;
      renderNumberCard();
      saveState();
    }}

    function markNumberCard(isMastered) {{
      const current = SITE_DATA.numbers[appState.numberIndex % SITE_DATA.numbers.length];
      appState.masteredNumbers[current.id] = isMastered;
      saveState();
      nextNumberCard();
    }}

    function renderNumberTabs() {{
      const container = document.getElementById('num-category-tabs');
      if (container.children.length > 0) return;
      const categories = ['全部', '一、水與基地保水', '二、綠化・節能・淨零', '三、強度・容積・多目標', '四、動線・無障礙・尺度', '五、防災・救災空間', '六、人口・政策'];
      categories.forEach(cat => {{
        const btn = document.createElement('button');
        btn.className = "px-3 py-1.5 rounded-lg whitespace-nowrap bg-slate-900 border border-slate-800 text-slate-300 hover:text-white transition";
        btn.innerText = cat.replace(/[一二三四五六]、/, '');
        btn.onclick = () => {{
          if (cat === '全部') {{
            appState.numberIndex = 0;
          }} else {{
            const targetIdx = SITE_DATA.numbers.findIndex(n => n.category.includes(cat));
            if (targetIdx !== -1) appState.numberIndex = targetIdx;
          }}
          renderNumberCard();
        }};
        container.appendChild(btn);
      }});
    }}

    // ==========================================
    // 模組 4: 72 個單格快卡 (6-Grids Blitz)
    // ==========================================
    let currentGridFilter = 'all';

    function filterGridFunc(func) {{
      currentGridFilter = func;
      document.querySelectorAll('.grid-func-btn').forEach(btn => {{
        if (btn.getAttribute('data-func') === func) {{
          btn.classList.add('bg-purple-600', 'text-white', 'font-bold');
          btn.classList.remove('text-slate-400');
        }} else {{
          btn.classList.remove('bg-purple-600', 'text-white', 'font-bold');
          btn.classList.add('text-slate-400');
        }}
      }});
      renderGridCards();
    }}

    function renderGridCards() {{
      const container = document.getElementById('grid-cards-container');
      container.innerHTML = '';
      
      const filtered = (currentGridFilter === 'all') 
        ? SITE_DATA.single_grids 
        : SITE_DATA.single_grids.filter(g => g.func_abbr === currentGridFilter);

      filtered.forEach(g => {{
        const isRevealed = !!appState.gridRevealed[g.id];
        const card = document.createElement('div');
        card.className = "bg-slate-900 p-4 sm:p-5 rounded-3xl border border-slate-750 hover:border-slate-600 shadow-xl space-y-3 cursor-pointer active:scale-98 transition overflow-hidden";
        card.onclick = () => toggleGridReveal(g.id);

        const cleanNumber = (g.number || '').replace(/^[▸\\s]+/, '');

        card.innerHTML = `
          <!-- 頂部資訊列：左側機能徽章，右側複製按鈕；主題名稱獨立完整呈現 -->
          <div class="border-b border-slate-800/80 pb-2 space-y-1.5">
            <div class="flex items-center justify-between gap-2">
              <span class="shrink-0 px-2.5 py-1 rounded-xl font-black text-xs bg-purple-950 text-purple-300 border border-purple-800/60 whitespace-nowrap shadow-sm">
                【${{g.func_abbr}}】格 ${{g.grid_no}}
              </span>
              <button 
                onclick="event.stopPropagation(); copyGridCard('${{g.id}}', this)"
                class="shrink-0 flex items-center gap-1.5 px-3 py-1 rounded-xl font-bold text-xs bg-slate-800 hover:bg-slate-700 text-slate-200 hover:text-white border border-slate-700 active:scale-95 transition shadow-sm whitespace-nowrap"
                title="複製小卡文字，最前方自動加上『詳細說明：』">
                <span class="text-xs">📋</span><span>複製</span>
              </button>
            </div>
            <!-- 主題分類完整字串 (允許換行，絕無 ... 截斷) -->
            <div class="text-xs sm:text-sm font-bold text-slate-400 leading-snug break-words">
              ${{g.topic_header}}
            </div>
          </div>

          <!-- 卡片核心考點標題 (獨佔一行，完整呈現) -->
          <div class="text-lg sm:text-xl font-black text-white leading-snug tracking-wide pt-0.5 break-words">
            ${{g.title}}
          </div>
          
          <!-- 展開內容區塊 (完整呈現，防止溢出) -->
          <div id="grid-content-${{g.id}}" class="${{isRevealed ? '' : 'hidden'}} pt-3 border-t border-slate-800/80 space-y-2.5 text-sm sm:text-base">
            <div class="text-emerald-400 font-bold leading-relaxed flex items-start gap-2">
              <span class="shrink-0 text-emerald-500 font-black text-base leading-none pt-0.5">▸</span>
              <span class="break-words">關鍵數字：<span class="text-emerald-300 font-mono font-black">${{cleanNumber}}</span></span>
            </div>
            <div class="text-slate-200 leading-relaxed flex items-start gap-2 bg-slate-950/70 p-3 rounded-2xl border border-slate-800/80">
              <span class="shrink-0 text-amber-400 font-black text-sm pt-0.5">🔑</span>
              <div class="break-words font-medium">關鍵詞：<span class="text-white">${{g.keywords}}</span></div>
            </div>
            <div class="text-slate-400 text-xs sm:text-sm font-mono flex items-start gap-2 pt-1">
              <span class="shrink-0">📐</span>
              <span class="break-words">配圖：${{g.diagram}}</span>
            </div>
          </div>
          <div class="text-xs font-bold text-slate-400 text-center pt-1 ${{isRevealed ? 'hidden' : ''}}">
            👆 點擊展開考點核心與關鍵詞
          </div>
        `;
        container.appendChild(card);
      }});
    }}

    function toggleGridReveal(gridId) {{
      appState.gridRevealed[gridId] = !appState.gridRevealed[gridId];
      saveState();
      renderGridCards();
    }}

    // ==========================================
    // 模組 5: 11 張萬用圖卡心智快閃
    // ==========================================
    function renderDiagramDetail(index) {{
      appState.diagramIndex = index;
      const diag = SITE_DATA.diagrams[index];
      if (!diag) return;

      document.getElementById('diag-title').innerText = diag.header;
      document.getElementById('diag-used-for').innerText = `跨題用途：${{diag.used_for}}`;
      document.getElementById('diag-id-badge').innerText = `${{index + 1}} / ${{SITE_DATA.diagrams.length}}`;

      // 檢查此圖卡是否具備精確手繪臨摹稿
      const toggleBox = document.getElementById('diag-mode-toggle-box');
      if (toggleBox) {{
        if (diag.sketch_image) {{
          toggleBox.classList.remove('hidden');
        }} else {{
          toggleBox.classList.add('hidden');
          currentDiagMode = 'svg';
        }}
      }}

      // 更新模式按鈕選中樣式
      const btnSvg = document.getElementById('diag-btn-svg');
      const btnSketch = document.getElementById('diag-btn-sketch');
      if (btnSvg && btnSketch) {{
        if (currentDiagMode === 'svg') {{
          btnSvg.className = "flex-1 py-1.5 rounded-lg text-xs font-bold bg-amber-500 text-slate-950 transition";
          btnSketch.className = "flex-1 py-1.5 rounded-lg text-xs font-bold text-slate-400 hover:text-white transition";
        }} else {{
          btnSvg.className = "flex-1 py-1.5 rounded-lg text-xs font-bold text-slate-400 hover:text-white transition";
          btnSketch.className = "flex-1 py-1.5 rounded-lg text-xs font-bold bg-emerald-500 text-slate-950 transition";
        }}
      }}

      const box = document.getElementById('diag-svg-box');
      if (currentDiagMode === 'sketch' && diag.sketch_image) {{
        box.innerHTML = `
          <div class="w-full flex flex-col items-center">
            <img src="${{diag.sketch_image}}" class="w-full max-h-[360px] object-contain rounded-lg" alt="${{diag.header}} 手繪臨摹" onerror="this.src='apple-touch-icon.png'">
            <div class="w-full mt-2 pt-2 border-t border-slate-200/50 flex justify-between items-center text-[11px] text-slate-600 px-1">
              <span class="font-bold text-emerald-800">📖 《實戰手繪圖解》${{diag.sketch_source_page}}：${{diag.sketch_title}}</span>
              <span class="text-slate-500 font-mono">1:1 手繪臨摹原件</span>
            </div>
          </div>
        `;
      }} else if (diag.svg_code) {{
        box.innerHTML = `
          <div class="w-full flex flex-col items-center">
            ${{diag.svg_code}}
            <div class="w-full mt-2 pt-1 border-t border-slate-100 flex justify-between items-center text-[10px] text-slate-500 px-1">
              <span class="font-bold text-slate-700">📐 數位規範圖解（標準概念幾何圖）</span>
              <span>100% 原生向量 SVG</span>
            </div>
          </div>
        `;
      }} else if (diag.sketch_image) {{
        box.innerHTML = `
          <div class="w-full flex flex-col items-center">
            <img src="${{diag.sketch_image}}" class="w-full max-h-[360px] object-contain rounded-lg" alt="${{diag.header}} 手繪臨摹" onerror="this.src='apple-touch-icon.png'">
            <div class="w-full mt-2 pt-2 border-t border-slate-200/50 flex justify-between items-center text-[11px] text-slate-600 px-1">
              <span class="font-bold text-emerald-800">📖 《實戰手繪圖解》${{diag.sketch_source_page}}：${{diag.sketch_title}}</span>
              <span class="text-slate-500 font-mono">純手繪考場必背</span>
            </div>
          </div>
        `;
      }} else {{
        box.innerHTML = `<div class="text-slate-400 text-xs py-8">暫無圖檔</div>`;
      }}

      // 考場手繪技法提示
      const techBanner = document.getElementById('diag-techniques-banner');
      const techText = document.getElementById('diag-techniques-text');
      if (techBanner && techText) {{
        if (diag.sketch_techniques) {{
          techText.innerText = diag.sketch_techniques;
          techBanner.classList.remove('hidden');
        }} else {{
          techBanner.classList.add('hidden');
        }}
      }}

      document.getElementById('diag-draw-step').innerText = diag.draw_step;
      document.getElementById('diag-pitfall').innerText = diag.pitfall;

      const checkContainer = document.getElementById('diag-checklist-box');
      checkContainer.innerHTML = '';
      (diag.checklist || []).forEach(item => {{
        checkContainer.innerHTML += `
          <label class="flex items-center space-x-2 text-slate-300 cursor-pointer">
            <input type="checkbox" class="rounded bg-slate-800 border-slate-700 text-emerald-500 focus:ring-0">
            <span>${{item}}</span>
          </label>
        `;
      }});

      renderDiagChips();
    }}

    function renderDiagChips() {{
      const container = document.getElementById('diag-nav-chips');
      container.innerHTML = '';
      SITE_DATA.diagrams.forEach((d, i) => {{
        const btn = document.createElement('button');
        const isCurrent = (i === appState.diagramIndex);
        btn.className = `px-3 py-1 rounded-xl text-xs whitespace-nowrap font-bold transition ${{
          isCurrent ? 'bg-amber-500 text-slate-950' : 'bg-slate-900 border border-slate-800 text-slate-400'
        }}`;
        btn.innerText = `圖卡 ${{i+1}}`;
        btn.onclick = () => renderDiagramDetail(i);
        container.appendChild(btn);
      }});
    }}

    // ==========================================
    // 模組 6: 歷屆+模考審題快刀 (單頁一題 Pager 模式)
    // ==========================================
    let strategyCategoryFilter = 'mock';
    let currentStrategyMapIdx = 0;

    function getFilteredStrategyCards() {{
      const allCards = SITE_DATA.strategy_cards || [];
      if (strategyCategoryFilter === 'past') {{
        return allCards.filter(c => c.category === 'past');
      }}
      return allCards.filter(c => c.category === 'mock');
    }}

    function filterStrategyCategory(cat) {{
      strategyCategoryFilter = (cat === 'past') ? 'past' : 'mock';
      appState.strategyIndex = 0;
      currentStrategyMapIdx = 0;
      
      ['mock', 'past'].forEach(k => {{
        const btn = document.getElementById(`strat-cat-${{k}}`);
        if (btn) {{
          if (k === strategyCategoryFilter) {{
            btn.className = "flex-1 py-2 rounded-xl text-xs font-black bg-blue-600 text-white transition shadow-sm";
          }} else {{
            btn.className = "flex-1 py-2 rounded-xl text-xs font-semibold text-slate-400 hover:text-white transition";
          }}
        }}
      }});

      renderStrategyPager();
      saveState();
    }}

    window.switchStrategyMap = function(idx) {{
      currentStrategyMapIdx = idx;
      const cards = getFilteredStrategyCards();
      const card = cards[(appState.strategyIndex || 0) % cards.length];
      if (!card) return;
      const mapList = (card.map_images && card.map_images.length > 0) ? card.map_images : [{{title: '基地圖', src: card.map_image}}];
      const targetMap = mapList[idx] || mapList[0];
      
      const imgElem = document.getElementById('strat-card-map-img');
      if (imgElem) {{
        imgElem.src = targetMap.src;
      }}
      
      mapList.forEach((_, i) => {{
        const tabBtn = document.getElementById(`strat-map-tab-${{i}}`);
        if (tabBtn) {{
          if (i === idx) {{
            tabBtn.className = "px-2.5 py-1 rounded-lg text-xs font-bold bg-emerald-600 text-white shadow-sm transition";
          }} else {{
            tabBtn.className = "px-2.5 py-1 rounded-lg text-xs font-medium bg-slate-800 text-slate-400 hover:text-white transition";
          }}
        }}
      }});
      
      const container = document.getElementById('strat-card-map-container');
      if (container) {{
        container.onclick = () => window.openImageLightbox(targetMap.src, `${{card.title}} - ${{targetMap.title}}`);
      }}
    }};

    function renderStrategyPager() {{
      const cards = getFilteredStrategyCards();
      if (!cards || cards.length === 0) return;
      
      const idx = (appState.strategyIndex || 0) % cards.length;
      const card = cards[idx];
      currentStrategyMapIdx = 0;
      
      // 更新頂部年份標籤
      renderStrategyTabs(idx, cards);
      
      // 更新當前頁碼指示
      document.getElementById('strategy-pager-text').innerText = `${{idx + 1}} / ${{cards.length}}`;

      const catBadge = (card.category === 'mock')
        ? `<span class="px-2.5 py-0.5 rounded-full bg-amber-950/80 text-amber-300 font-bold border border-amber-800/50 shadow-sm">🎯 模擬考・${{card.year}}</span>`
        : `<span class="px-2.5 py-0.5 rounded-full bg-blue-900/40 text-blue-300 font-bold border border-blue-800/40">📜 歷屆真題・${{card.year}}</span>`;

      // 取得圖說陣列
      const mapList = (card.map_images && card.map_images.length > 0) 
        ? card.map_images 
        : [{{title: '基地圖', src: card.map_image}}];
      const currentMap = mapList[0];

      const mapTabsHtml = (mapList.length > 1) ? `
        <div class="flex items-center gap-1.5 overflow-x-auto no-scrollbar py-1">
          ${{mapList.map((m, i) => `
            <button id="strat-map-tab-${{i}}" onclick="switchStrategyMap(${{i}})" class="px-2.5 py-1 rounded-lg text-xs font-bold transition ${{i === 0 ? 'bg-emerald-600 text-white shadow-sm' : 'bg-slate-800 text-slate-400 hover:text-white'}}">
              ${{m.title}}
            </button>
          `).join('')}}
        </div>
      ` : '';

      // 渲染單題卡片
      const container = document.getElementById('strategy-single-card');
      container.innerHTML = `
        <div class="flex justify-between items-center text-xs">
          ${{catBadge}}
          <div class="flex items-center gap-2">
            <button onclick="copyCurrentStrategyCard(this)" class="px-2.5 py-0.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-[11px] font-bold border border-slate-700 active:scale-95 transition flex items-center space-x-1" title="複製此審題卡">
              <span>📋</span><span>複製</span>
            </button>
            <span class="text-slate-400 font-medium">${{card.theme}}</span>
          </div>
        </div>
        
        <h3 class="text-xl md:text-2xl font-black text-white leading-snug break-words">${{card.title}}</h3>

        <!-- 試卷基地圖說 (支援多圖切換與全螢幕手勢放大) -->
        <div class="space-y-1.5">
          <div class="flex justify-between items-center text-xs">
            <span class="text-emerald-400 font-bold flex items-center space-x-1">
              <span>📐</span><span>試卷基地圖說 (${{mapList.length}} 張)</span>
            </span>
            <span class="text-[11px] text-cyan-400 cursor-pointer" onclick="window.openImageLightbox('${{currentMap.src}}', '${{card.title}} - ${{currentMap.title}}')">
              🔍 點擊手勢縮放 (Pinch)
            </span>
          </div>
          ${{mapTabsHtml}}
          <div id="strat-card-map-container" onclick="window.openImageLightbox('${{currentMap.src}}', '${{card.title}} - ${{currentMap.title}}')" class="bg-white rounded-2xl p-2 border border-slate-700 shadow-inner flex items-center justify-center min-h-[220px] max-h-[300px] overflow-hidden cursor-pointer relative group">
            <img id="strat-card-map-img" src="${{currentMap.src}}" class="w-full h-full object-contain max-h-[280px]" alt="${{card.title}} 基地圖" onerror="this.src='apple-touch-icon.png'">
            <div class="absolute bottom-2 right-2 bg-slate-900/85 backdrop-blur-sm text-cyan-300 text-[10px] px-2.5 py-1 rounded-full border border-cyan-500/30 flex items-center space-x-1 shadow-lg font-bold">
              <span>🔍 雙指捏合縮放</span>
            </div>
          </div>
        </div>

        <!-- 2 分鐘大腦自問課題 -->
        <div class="bg-slate-950/80 p-4 rounded-2xl border border-slate-800 text-sm space-y-2">
          <span class="text-amber-400 font-bold block flex items-center space-x-1 text-base">
            <span>⚡</span><span>2 分鐘大腦自問課題：</span>
          </span>
          ${{card.challenges.map(c => `<div class="text-slate-200 leading-relaxed font-medium">• ${{c}}</div>`).join('')}}
        </div>

        <!-- 專家破局黃金決策 -->
        <div class="bg-slate-850 p-4.5 rounded-2xl border border-slate-750 text-sm md:text-base space-y-2.5">
          <span class="text-cyan-400 font-bold block flex items-center space-x-1 text-base">
            <span>💡</span><span>專家破局黃金決策（車道/盲邊/量體/退縮）：</span>
          </span>
          ${{card.expert_decisions.map(d => `<div class="text-slate-100 leading-relaxed font-medium">${{d}}</div>`).join('')}}
        </div>

        <!-- 原汁原味官方題目正文 (可折疊/展開) -->
        <div class="pt-2 border-t border-slate-800/80">
          <button 
            onclick="toggleStrategyFullText()" 
            class="w-full py-3 px-4 text-sm font-bold text-slate-200 hover:text-white flex items-center justify-center gap-2 rounded-2xl bg-slate-850 hover:bg-slate-800 border border-slate-700 active:scale-98 transition shadow-sm"
          >
            <span id="strat-toggle-icon" class="text-xs text-cyan-400 font-mono transition-transform">▼</span>
            <span id="strat-toggle-label">展開歷屆官方題目完整原話</span>
          </button>
          <!-- 官方題目全文展開容器：字級與專家決策一致 (text-sm md:text-base)，高對比不費眼，滑動順暢 -->
          <div 
            id="strat-full-text" 
            class="hidden mt-3 p-4.5 sm:p-5 bg-slate-950/90 rounded-2xl border border-slate-750 text-sm md:text-base text-slate-100 leading-relaxed max-h-[420px] overflow-y-auto whitespace-pre-line shadow-inner select-text"
          >
            ${{card.full_text || '無題目完整原話資料'}}
          </div>
        </div>
      `;
    }}

    function renderStrategyTabs(activeIdx, cards) {{
      const container = document.getElementById('strategy-year-tabs');
      container.innerHTML = '';
      const list = cards || getFilteredStrategyCards();
      list.forEach((c, i) => {{
        const btn = document.createElement('button');
        const isCurrent = (i === activeIdx);
        // 使用明確唯一的標籤 (115擴大、115模2、115模1、115隨堂、114~95)
        const labelText = c.short_tab || (c.year.split(' ')[0].replace('年', ''));
        btn.className = `px-3 py-1 rounded-xl text-xs whitespace-nowrap font-bold transition ${{
          isCurrent ? 'bg-blue-600 text-white shadow-md shadow-blue-900/40' : 'bg-slate-900 border border-slate-800 text-slate-400 hover:text-white'
        }}`;
        btn.innerText = labelText;
        btn.onclick = () => {{
          appState.strategyIndex = i;
          renderStrategyPager();
          saveState();
        }};
        container.appendChild(btn);
      }});
      
      // 自動滾動使選中的 chip 保持在中間視野
      const activeBtn = container.children[activeIdx];
      if (activeBtn) {{
        activeBtn.scrollIntoView({{ behavior: 'smooth', inline: 'center', block: 'nearest' }});
      }}
    }}

    function nextStrategyQuestion() {{
      const cards = getFilteredStrategyCards();
      const total = cards.length;
      if (total === 0) return;
      appState.strategyIndex = ((appState.strategyIndex || 0) + 1) % total;
      renderStrategyPager();
      saveState();
    }}

    function prevStrategyQuestion() {{
      const cards = getFilteredStrategyCards();
      const total = cards.length;
      if (total === 0) return;
      appState.strategyIndex = ((appState.strategyIndex || 0) - 1 + total) % total;
      renderStrategyPager();
      saveState();
    }}

    function toggleStrategyFullText() {{
      const box = document.getElementById('strat-full-text');
      const icon = document.getElementById('strat-toggle-icon');
      const label = document.getElementById('strat-toggle-label');
      if (!box) return;

      const isHidden = box.classList.contains('hidden');
      if (isHidden) {{
        box.classList.remove('hidden');
        if (icon) icon.innerText = '▲';
        if (label) label.innerText = '收起官方原卷題目正文';
      }} else {{
        box.classList.add('hidden');
        if (icon) icon.innerText = '▼';
        if (label) label.innerText = '展開歷屆官方題目完整原話';
      }}
    }}

    // 手機端審題卡左右滑動換題手勢 (Swipe Navigation)
    let cardTouchStartX = 0;
    let cardTouchStartY = 0;
    const cardEl = document.getElementById('strategy-single-card');
    cardEl.addEventListener('touchstart', (e) => {{
      cardTouchStartX = e.touches[0].clientX;
      cardTouchStartY = e.touches[0].clientY;
    }}, {{ passive: true }});
    cardEl.addEventListener('touchend', (e) => {{
      const dx = e.changedTouches[0].clientX - cardTouchStartX;
      const dy = e.changedTouches[0].clientY - cardTouchStartY;
      if (Math.abs(dx) > 55 && Math.abs(dy) < 55) {{
        if (dx < 0) nextStrategyQuestion();
        else prevStrategyQuestion();
      }}
    }}, {{ passive: true }});

    // 鍵盤左右方向鍵支援
    window.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') window.closeDiagramLightbox();
      if (appState.currentView === 'strategy') {{
        if (e.key === 'ArrowRight') nextStrategyQuestion();
        if (e.key === 'ArrowLeft') prevStrategyQuestion();
      }} else if (appState.currentView === 'numbers') {{
        if (e.key === 'ArrowRight') nextNumberCard();
        if (e.key === 'ArrowLeft') prevNumberCard();
        if (e.key === ' ') {{ e.preventDefault(); flipNumberCard(); }}
      }}
    }});

    // ==========================================
    // 3 分鐘隨機微膠囊 (Daily Capsule)
    // ==========================================
    let capsuleStep = 0;
    let capsuleQueue = [];

    function startDailyCapsule() {{
      capsuleStep = 0;
      const rndNum = SITE_DATA.numbers[Math.floor(Math.random() * SITE_DATA.numbers.length)];
      const rndGrid = SITE_DATA.single_grids[Math.floor(Math.random() * SITE_DATA.single_grids.length)];
      const rndDiag = SITE_DATA.diagrams[Math.floor(Math.random() * SITE_DATA.diagrams.length)];
      const rndSop = SITE_DATA.sop.blitz_questions[Math.floor(Math.random() * SITE_DATA.sop.blitz_questions.length)];

      capsuleQueue = [
        {{ type: 'num', data: rndNum }},
        {{ type: 'sop', data: rndSop }},
        {{ type: 'grid', data: rndGrid }},
        {{ type: 'diag', data: rndDiag }}
      ];

      document.getElementById('capsule-modal').classList.remove('hidden');
      renderCapsuleStep();
    }}

    function renderCapsuleStep() {{
      const item = capsuleQueue[capsuleStep];
      const body = document.getElementById('capsule-body');
      const scrollArea = document.getElementById('capsule-scroll-area');
      if (scrollArea) scrollArea.scrollTop = 0;
      document.getElementById('capsule-step-text').innerText = `${{capsuleStep + 1}} / 4`;

      if (item.type === 'num') {{
        const kws = (item.data.keywords && item.data.keywords.length > 0)
          ? `<div class="flex flex-wrap gap-1.5 my-2">` + item.data.keywords.map(k => `<span class="px-2.5 py-1 rounded-xl bg-cyan-950/80 text-cyan-300 font-bold border border-cyan-700/50 text-xs shadow-sm">#${{k}}</span>`).join('') + `</div>`
          : '';
        body.innerHTML = `
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <span class="px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-400 text-xs font-bold border border-emerald-500/30">
                關卡 1/4 ・ 審題關鍵字反射 ＆ 數字速記
              </span>
              <span class="text-xs text-slate-400 font-medium">${{item.data.category}}</span>
            </div>
            <div class="bg-slate-900 p-5 rounded-3xl border border-slate-800 shadow-xl space-y-4">
              ${{kws}}
              <h3 class="text-lg md:text-xl font-bold text-white leading-relaxed">
                ${{item.data.scenario || item.data.content}}
              </h3>
              <div class="p-5 bg-slate-950 rounded-2xl border border-emerald-500/30 text-center space-y-2">
                <span class="text-xs text-slate-400 block font-bold">法規標準數值：</span>
                <div class="text-3xl md:text-4xl font-black text-emerald-400 font-mono tracking-wider">
                  ${{item.data.number}}
                </div>
              </div>
              <div class="bg-slate-950/80 p-4 rounded-2xl border border-slate-800 space-y-1.5 text-sm">
                <span class="text-amber-400 font-bold block text-xs">💡 考場審題反射／用法：</span>
                <p class="text-slate-200 leading-relaxed">${{item.data.reflex || item.data.usage}}</p>
              </div>
              <div class="text-xs text-slate-500 font-mono text-right">
                出處：${{item.data.source}} (${{STATUS_DESC[item.data.status] || item.data.status || '最新查證'}})
              </div>
            </div>
          </div>
        `;
      }} else if (item.type === 'sop') {{
        body.innerHTML = `
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <span class="px-3 py-1 rounded-full bg-cyan-500/20 text-cyan-400 text-xs font-bold border border-cyan-500/30">
                關卡 2/4 ・ 作圖 SOP 肌肉記憶
              </span>
              <span class="text-xs text-cyan-300 font-bold">11 步驟無腦接</span>
            </div>
            <div class="bg-slate-900 p-5 rounded-3xl border border-slate-800 shadow-xl space-y-4">
              <h3 class="text-lg md:text-xl font-bold text-white leading-relaxed">
                ${{item.data.question}}
              </h3>
              <div class="p-5 bg-slate-950 rounded-2xl border border-cyan-500/30 space-y-2">
                <div class="flex items-center space-x-2 text-cyan-400 font-black text-base md:text-lg">
                  <span>👉</span>
                  <span>正確下一步：${{item.data.correct}}</span>
                </div>
                <p class="text-sm md:text-base text-slate-200 leading-relaxed pt-2 border-t border-slate-800/80">
                  ${{item.data.explanation}}
                </p>
              </div>
              <div class="p-3.5 bg-slate-950/70 rounded-2xl border border-slate-800 text-xs text-slate-400 leading-relaxed space-y-1">
                <div class="text-amber-400 font-bold">⚡ 作圖三鐵律心法：</div>
                <div>• <b>停損</b>：卡關超過 3 分鐘立刻換題。</div>
                <div>• <b>定案</b>：構想夠好就定案，限 5 分鐘。</div>
                <div>• <b>推進</b>：由粗到細，全圖先畫到 60% 再加深。</div>
              </div>
            </div>
          </div>
        `;
      }} else if (item.type === 'grid') {{
        body.innerHTML = `
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <span class="px-3 py-1 rounded-full bg-purple-500/20 text-purple-400 text-xs font-bold border border-purple-500/30">
                關卡 3/4 ・ 申論單格秒殺
              </span>
              <span class="text-xs text-purple-300 font-mono font-bold">${{item.data.func_name}}</span>
            </div>
            <div class="bg-slate-900 p-5 rounded-3xl border border-slate-800 shadow-xl space-y-4">
              <div class="text-xs text-slate-400 font-medium">${{item.data.topic_header}}</div>
              <h3 class="text-lg md:text-xl font-bold text-white leading-relaxed">
                ${{item.data.title}}
              </h3>
              <div class="p-5 bg-slate-950 rounded-2xl border border-purple-500/30 space-y-3">
                <div class="flex items-start space-x-2 text-sm md:text-base">
                  <span class="text-emerald-400 font-black flex-shrink-0">▸ 核心判準：</span>
                  <span class="text-emerald-300 font-bold">${{item.data.number}}</span>
                </div>
                <div class="pt-3 border-t border-slate-800/80 text-sm text-slate-200 leading-relaxed">
                  <span class="text-amber-400 font-bold block mb-1.5">🔑 考場 3 關鍵詞：</span>
                  <div class="bg-slate-900 p-3.5 rounded-xl border border-slate-800 text-white font-medium">
                    ${{item.data.keywords}}
                  </div>
                </div>
              </div>
              <div class="text-xs text-slate-400 font-mono">
                📐 搭配圖說：${{item.data.diagram_ref || '萬用圖卡對應圖例'}}
              </div>
            </div>
          </div>
        `;
      }} else if (item.type === 'diag') {{
        body.innerHTML = `
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <span class="px-3 py-1 rounded-full bg-amber-500/20 text-amber-400 text-xs font-bold border border-amber-500/30">
                關卡 4/4 ・ 萬用圖卡大腦心像
              </span>
              <span class="text-xs text-slate-400">大腦心像速覽</span>
            </div>
            <div class="bg-slate-900 p-5 rounded-3xl border border-slate-800 shadow-xl space-y-4">
              <h3 class="text-lg md:text-xl font-bold text-white leading-relaxed">
                ${{item.data.header}}
              </h3>
              <div onclick="window.openDiagramLightbox(capsuleQueue[capsuleStep].data.svg_code, capsuleQueue[capsuleStep].data.header)" class="bg-white rounded-2xl p-3 min-h-[200px] max-h-[320px] overflow-hidden flex items-center justify-center cursor-pointer relative group border border-slate-700 shadow-inner">
                ${{item.data.svg_code}}
                <div class="absolute bottom-2 right-2 bg-slate-900/90 backdrop-blur-sm text-emerald-400 text-xs px-3 py-1 rounded-full border border-emerald-500/30 flex items-center space-x-1.5 shadow-md">
                  <span>🔍</span><span>點擊滿版手勢放大</span>
                </div>
              </div>
              <div class="p-4 bg-slate-950 rounded-2xl border border-slate-800 space-y-1.5 text-sm text-slate-200">
                <span class="text-cyan-400 font-bold block text-xs">✅ 考場必標元素：</span>
                <p class="leading-relaxed">${{item.data.must_mark}}</p>
              </div>
            </div>
          </div>
        `;
      }}
    }}

    function nextCapsuleStep() {{
      capsuleStep++;
      if (capsuleStep < 4) {{
        renderCapsuleStep();
      }} else {{
        alert('🎉 太棒了！今日 3 分鐘微膠囊達成！大腦神經元已建立連結！');
        closeCapsuleModal();
      }}
    }}

    function closeCapsuleModal() {{
      document.getElementById('capsule-modal').classList.add('hidden');
    }}

    function toggleSettingsModal() {{
      const modal = document.getElementById('settings-modal');
      if (modal) modal.classList.toggle('hidden');
    }}

    function resetAllProgress() {{
      if (confirm('確定要重置所有學習進度與標記記錄嗎？（掌握度將歸零重新計算）')) {{
        localStorage.removeItem(STATE_KEY);
        appState = {{
          currentView: 'capsule',
          numberIndex: 0,
          masteredNumbers: {{}},
          sopStreak: 0,
          gridRevealed: {{}},
          diagramIndex: 0,
          strategyIndex: 0
        }};
        saveState();
        switchView('capsule');
        toggleSettingsModal();
        alert('學習進度已成功重置！');
      }}
    }}

    function forceRefreshCache() {{
      if ('caches' in window) {{
        caches.keys().then(names => {{
          names.forEach(name => caches.delete(name));
        }});
      }}
      if ('serviceWorker' in navigator) {{
        navigator.serviceWorker.getRegistrations().then(regs => {{
          regs.forEach(r => r.unregister());
        }});
      }}
      location.reload(true);
    }}

    window.addEventListener('DOMContentLoaded', () => {{
      loadState();
      switchView(appState.currentView || 'capsule');
    }});
  </script>

  <!-- 全域 Toast 提示元件 (支援 Gemini GEM 連動) -->
  <div id="global-toast" class="fixed bottom-20 left-1/2 -translate-x-1/2 z-[150] bg-slate-900/95 backdrop-blur-md text-emerald-300 border border-emerald-500/40 px-4 py-2.5 rounded-2xl shadow-2xl flex items-center gap-2.5 text-xs font-semibold pointer-events-auto transition-all duration-300 opacity-0 translate-y-4 max-w-[92vw]">
    <span id="toast-icon" class="text-base">📋</span>
    <span id="toast-msg" class="break-words leading-tight">已複製！</span>
    <button id="toast-gem-btn" onclick="openGemWindow()" class="hidden ml-1 px-2.5 py-1 rounded-xl bg-gradient-to-r from-emerald-600 to-cyan-600 hover:from-emerald-500 hover:to-cyan-500 text-white font-bold text-xs shadow-md whitespace-nowrap active:scale-95 transition">
      開啟 GEM ↗
    </button>
  </div>
  <script src="offline_wrongbook.js"></script>
  <script src="tracing_lib.js"></script>
</body>
</html>
'''

# 寫入 index.html
OUT_HTML = os.path.join(APP_DIR, "index.html")
with open(OUT_HTML, "w", encoding="utf-8") as f:
    f.write(html_template)
print(f"成功生成 index.html: {OUT_HTML} ({len(html_template)/1024:.1f} KB)")

# 同步 offline_wrongbook.js 外掛檔
import shutil
patch_wb = r"G:\我的雲端硬碟\個人專區\敷地速刷APP\patch\offline_wrongbook.js"
if os.path.isfile(patch_wb):
    shutil.copyfile(patch_wb, os.path.join(APP_DIR, "offline_wrongbook.js"))
    print("成功同步 offline_wrongbook.js 外掛")
patch_tr = r"G:\我的雲端硬碟\個人專區\敷地速刷APP\patch\tracing_lib.js"
if os.path.isfile(patch_tr):
    shutil.copyfile(patch_tr, os.path.join(APP_DIR, "tracing_lib.js"))
    print("成功同步 tracing_lib.js 外掛")

# 更新 sw.js 離線快取版本戳記 (v6.0)
SW_PATH = os.path.join(APP_DIR, "sw.js")
sw_code = '''// Service Worker - 敷地速刷 PWA 離線快取（2026-10-12 改版）
// 改 APP 任何檔案後，把 CACHE_NAME 版號加一，手機才會拿到新版。
const CACHE_NAME = 'site-planning-quiz-v6.3';
const ASSETS = [
  './',
  './index.html',
  './offline_wrongbook.js',
  './tracing_lib.js',
  './manifest.json',
  './icon-192.png',
  './icon-512.png',
  './apple-touch-icon.png'
];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS)));
  self.skipWaiting();
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k)))
    )
  );
  self.clients.claim();
});

function putCache(req, res) {
  // opaque（跨域 CDN，如 Tailwind）也存，離線時版面才不會毀
  if (res && (res.ok || res.type === 'opaque')) {
    const copy = res.clone();
    caches.open(CACHE_NAME).then((c) => c.put(req, copy));
  }
  return res;
}

self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET') return;

  // 頁面本身：網路優先（有網路就拿新版），離線才用快取
  if (req.mode === 'navigate') {
    e.respondWith(
      fetch(req).then((res) => putCache(req, res))
        .catch(() => caches.match(req).then((r) => r || caches.match('./index.html')))
    );
    return;
  }

  // 其他（圖片、JS、CDN）：快取優先，沒有就抓網路並存起來
  e.respondWith(
    caches.match(req).then((hit) => hit || fetch(req).then((res) => putCache(req, res)))
  );
});
'''

with open(SW_PATH, "w", encoding="utf-8") as f:
    f.write(sw_code)
print("成功更新 sw.js (v6.3)")
