---
trigger: always_on
---
# 敷地APP 與 考題分析專案核心規則

本專案為建築師考試「敷地計畫與都市設計」之速刷 PWA 應用與試題分析工作區。

## 1. 開工閘門（防貪婪跳過）
凡涉及修改或生成 Python 產生器（`generate_app.py`、`build_site_data.py` 等）或前端代碼（`敷地APP/index.html`），**第一個動作必須先以 `view_file` 讀取專案技能 `.agents/skills/site-app-workflow/SKILL.md`**，未讀取前嚴禁使用寫檔工具。

## 2. 工程紀律（Karpathy 原則）
嚴格落實全域 `karpathy-guidelines`：先想後寫、微創修改（改動最小行數）、禁止撰寫一次性修補腳本（如 `update_xxx.py`）、嚴禁未經確認的主觀重構。

## 3. 驗收卡口（物理驗證義務）
任何代碼修改完成後，**必須在終端執行 `python verify_app.py`**，確認取得 Exit Code 0 與 `[PASS]` 後方可宣告交付，並在回覆中附上驗證輸出摘要。
