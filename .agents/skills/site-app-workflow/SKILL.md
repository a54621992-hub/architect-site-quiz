---
name: site-app-workflow
description: 敷地APP與考題分析系統之積木式架構開發、Python產生器維護與驗證工作流。涉及 generate_app.py、敷地APP/、PWA或試題數據修改時使用。
---

# 敷地速刷 APP 開發與維護工作流

本技能定義本專案之 Python 編譯器維護防線、前端積木架構規範與驗收程序。

## 一、Python 產生器（generate_app.py）維護防線
`generate_app.py` 內嵌超過 1,000 行 HTML/JS 於 Python f-string 中，維護時必須恪遵：
1. **大括號轉義**：內嵌 JS 中的所有字面量大括號 `{}` 必須雙寫為 `{{}}`，否則 Python f-string 會報錯崩潰。
2. **正則與路徑防轉義**：內嵌的正則表達式或反斜線，嚴格確認轉義符號（使用 `\\` 或 raw string 區塊）。
3. **微創修改原則**：嚴禁建立臨時的 `update_generator.py` 跑正則替換；必須使用 `replace_file_content` 直接針對 `generate_app.py` 進行精準行數替換。
4. **只改產生器不改產出 HTML（防沖刷回滾）**：嚴禁直接修改 `敷地APP/index.html`，所有介面與邏輯修改一律在 `generate_app.py` 執行並重新編譯。
5. **數字全數溯源與禁用後備值**：題數、卡片張數與統計數必須 100% 來自 `site_data.json` / `SITE_DATA`，前端禁用 `|| 0` 或 `|| '預設'` 隱藏空值。

## 二、前端積木式架構（Brick Architecture）
單頁 PWA（`敷地APP/index.html`）功能必須具備錯誤隔離能力：
1. **模組獨立封裝**：手勢縮放（Pinch-zoom）、滑動換題（Swipe Navigation）、試題篩選、Service Worker 註冊等各模組各自獨立，避免全域變數污染。
2. **防禦性錯誤隔離**：事件監聽函式內部必須包覆 `try...catch`，單一手勢或組件計算報錯不得造成全站 JS 癱瘓（白屏）。
3. **單向資料流**：試題與策略卡數據由 `site_data.json` 注入，前端組件僅讀取狀態並渲染 DOM，嚴禁在多個模組中分散修改原始數據結構。

## 三、標準工作流與驗收步驟
1. 檢視修改目標，確認改動點在 `generate_app.py` 還是 `site_data.json`。
2. 以外科手術微創方式執行修改。
3. 執行產生器重新編譯：`python generate_app.py`。
4. 執行機械卡口驗收：`python verify_app.py`，確認全部斷言通過。
5. **回報必附承諾對照表**：每次修改回報必須附上對照表（`| 派工／審核項目 | 修改檔案與行號 | 驗收方式與結果 | 是否落實 |`），逐條核銷。
