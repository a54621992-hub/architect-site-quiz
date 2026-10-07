# 敷地速刷 (Site Planning Blitz) APP 獨立架構與積木抽換指南

> **專案定位**：115 年建築師高考「敷地計畫與都市設計」極速備考 PWA 獨立應用程式。
> **發布站點**：[https://a54621992-hub.github.io/architect-site-quiz/](https://a54621992-hub.github.io/architect-site-quiz/)
> **跨科目對接**：建築法規衝刺 [https://a54621992-hub.github.io/architect-exam-quiz/](https://a54621992-hub.github.io/architect-exam-quiz/)

---

## 一、 積木抽換架構 (Brick Architecture)

本 APP 採用**高內聚、低耦合的「題型積木庫 (Brick Modules)」＋「主控調度核心 (Core Engine)」**架構。
當需要修改某個考科單元、擴充題目或更新 SOP 時，只需抽換對應的資料積木或模組，不會對其他功能產生骨牌式破壞。

```
├── 題型積木庫 (Brick Modules)
│   ├── [積木 1] 作圖 SOP 肌肉記憶積木 (SOP Blitz Brick)
│   │   ├── 11 步驟時間配比清單
│   │   ├── 作圖三鐵律心法卡 (停損/定案/推進)
│   │   ├── 四色筆題幹快篩標記
│   │   └── 下一步反射 4 選 1 盲測題庫
│   │
│   ├── [積木 2] 84 項數字閃卡積木 (Numbers Brick)
│   │   ├── 六大分類 (水保防洪/綠能淨零/容積強度/動線無障礙/防災救災/人口政策)
│   │   ├── 3D 翻牌正面 (題目/情境) 與背面 (標準法規數字/考場一句用法/出處)
│   │   └── 掌握度 LocalStorage 斷點記憶
│   │
│   ├── [積木 3] 72 申論單格快卡積木 (Grids Brick)
│   │   ├── 六功能矩陣篩選 (診/策/制/系/界/時)
│   │   └── 三段式無打字記憶卡 (小標題 → 核心判準/數字 → 3關鍵詞/配圖指引)
│   │
│   ├── [積木 4] 11 張萬用圖卡積木 (Diagrams Brick)
│   │   ├── 向量 SVG 圖像內嵌
│   │   ├── 手勢橫向旋轉與雙指縮放燈箱 (Pinch-to-zoom 1x~4.5x)
│   │   └── 3分鐘手繪法、考場必標元素 Checklist 與失分避坑警示
│   │
│   └── [積木 5] 24 套審題快刀卡積木 (Strategy Cards Brick)
│       ├── 年份標籤滑動條 (115隨堂/115擴大/115模2/115模1/114~95年歷屆)
│       ├── 單頁單題 Pager + 左右手勢滑動換題 (Swipe Navigation)
│       ├── 裁切置中高解析現況圖 (exam_maps/)
│       └── 考題全文展開與自問核心課題/破局黃金決策
│
└── 組合器與主控核心 (Core Engine & Composer)
    ├── ⚡ 3 分鐘隨機微膠囊組合器 (Capsule Composer)：動態自積木 1~4 隨機抽調組合
    ├── 滿版速刷視圖引擎 (Full-screen Scrollable View Engine)
    ├── 離線快取 Service Worker (sw.js v5.1)
    └── 跨站點跳轉機制 (與法規衝刺獨立解耦)
```

---

## 二、 核心題型積木抽換規範

若需擴充或替換題型，依以下資料契約 (Schema) 修改 `site_data.json` 或 Markdown 來源：

### 1. 抽換數字積木 (`SITE_DATA.numbers`)
```json
{
  "id": "num_01",
  "category": "水保防洪",
  "content": "基地出流管制之出流洪峰削減率標準為何？",
  "number": "削減至開發前之 80% 或 100 年洪峰流量",
  "usage": "申論寫於格 4 系統或格 2 策略，標示滯洪池與雨水貯留量化數據",
  "source": "出流管制計畫書審查要點 第 5 點",
  "status": "✓ 115.9"
}
```

### 2. 抽換單格快卡積木 (`SITE_DATA.single_grids`)
```json
{
  "id": "grid_01_01",
  "topic_id": 1,
  "topic_header": "氣候韌性① 極端降雨",
  "func_code": "診",
  "func_name": "診斷",
  "title": "基地微地形高程與洪氾淹水潛勢疊圖",
  "number": "50~100年重現期淹水深度 < 0.3m",
  "keywords": "微地形分析、高程套疊、入流坡降",
  "diagram_ref": "圖卡 05 基地微氣候疊圖"
}
```

### 3. 抽換圖卡積木 (`SITE_DATA.diagrams`)
- 只要在 `diagrams` 陣列置換或追加 `svg_code` 字串，前端即自動產生導航 Chip 與滿版手勢旋轉放大燈箱。

---

## 三、 本地開發與發布工作流

1. **編譯打包**：
   ```powershell
   python build_site_data.py
   python generate_app.py
   python test_verify.py
   ```
2. **推送到獨立 GitHub Pages**：
   - 倉庫：`https://github.com/a54621992-hub/architect-site-quiz`
   - 分支：`main`（直接將 `APP/` 下檔案覆蓋至倉庫根目錄提交）
