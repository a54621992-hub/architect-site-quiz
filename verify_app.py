# -*- coding: utf-8 -*-
"""【專案驗證卡口】敷地APP 與 試題數據無損機械檢驗腳本（Karpathy 驗證標準）"""

import json
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# 若在 repo 根目錄執行，site_data.json 即在同層；若在 AI分析 執行，在 敷地APP 子目錄
APP_DIR = os.path.join(ROOT_DIR, "敷地APP") if os.path.isdir(os.path.join(ROOT_DIR, "敷地APP")) else ROOT_DIR
DATA_PATH = os.path.join(APP_DIR, "site_data.json")
HTML_PATH = os.path.join(APP_DIR, "index.html")
SW_PATH = os.path.join(APP_DIR, "sw.js")


def test_site_data():
    """1. 驗證 site_data.json 結構與數據完整性"""
    if not os.path.isfile(DATA_PATH):
        raise AssertionError("找不到 site_data.json")
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert len(data.get("topics", [])) > 0, "topics 題庫數據為空"
    assert len(data.get("strategy_cards", [])) > 0, "strategy_cards 數據為空"
    assert len(data.get("diagrams", [])) == 11, f"萬用圖卡數量應為 11，但實際為 {len(data.get('diagrams', []))}"
    print(f"  ✓ [1/5] site_data.json 驗證通過（題庫 {len(data['topics'])} 題，策略卡 {len(data['strategy_cards'])} 張，萬用圖卡恰好 11 張）")


def test_generator_execution():
    """2. 執行 generate_app.py 驗證 Exit Code 0"""
    gen_script = os.path.join(ROOT_DIR, "generate_app.py")
    if not os.path.isfile(gen_script):
        raise AssertionError("找不到 generate_app.py")
    res = subprocess.run([sys.executable, gen_script], capture_output=True, text=True, encoding='utf-8', cwd=ROOT_DIR)
    if res.returncode != 0:
        print("generate_app.py 執行報錯：", res.stderr)
        raise AssertionError(f"generate_app.py 執行失敗，Exit Code: {res.returncode}")
    print("  ✓ [2/5] generate_app.py 重新編譯執行通過（Exit Code 0）")


def test_html_output():
    """3. 驗證 index.html 產出完整度與大小"""
    if not os.path.isfile(HTML_PATH):
        raise AssertionError("找不到 敷地APP/index.html")
    size_kb = os.path.getsize(HTML_PATH) / 1024
    assert size_kb > 150, f"index.html 檔案體積異常過小 ({size_kb:.1f} KB)"
    with open(HTML_PATH, "r", encoding="utf-8") as f:
        html = f.read()
    assert "<!DOCTYPE html>" in html, "HTML 缺少 DOCTYPE 宣告"
    assert "SITE_DATA" in html, "HTML 未成功注入試題數據（未找到 SITE_DATA）"
    assert "切換法規" not in html, "HTML 中殘留『切換法規』按鈕，未達成獨立 APP 規範"
    assert "isLightboxRotated = false;" in html, "圖片燈箱預設未設為直式"
    print(f"  ✓ [3/5] index.html 完整性驗證通過（體積 {size_kb:.1f} KB，獨立APP且燈箱直式鎖定）")


def test_desensitization():
    """4. 脫敏檢查：嚴格杜絕敏感字樣"""
    sensitive_words = ["絕" + "機", "騏" + "華"]
    for root, _, files in os.walk(APP_DIR):
        for file in files:
            if file.endswith((".html", ".json", ".js", ".md")):
                fpath = os.path.join(root, file)
                with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                for word in sensitive_words:
                    if word in content:
                        raise AssertionError(f"檔案 {file} 含有機敏字樣：{word}")
    print("  ✓ [4/5] 脫敏驗證通過（全站零敏感字樣殘留）")


def test_service_worker():
    """5. 驗證 sw.js 快取設定"""
    if not os.path.isfile(SW_PATH):
        raise AssertionError("找不到 敷地APP/sw.js")
    with open(SW_PATH, "r", encoding="utf-8") as f:
        sw = f.read()
    assert "CACHE_NAME" in sw, "sw.js 缺少快取名稱宣告"
    print("  ✓ [5/5] sw.js PWA 快取配置驗證通過")


def test_content_consistency():
    """6. 內容一致性：真題卡題名須出現在題文、範卷不得標為官方試題、臨摹圖檔須存在"""
    import re
    import unicodedata
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    past = [c for c in data["strategy_cards"] if re.fullmatch(r"strategy_\d+", c.get("id", ""))]
    for c in past:
        # PDF 抽出的題文含 CJK 相容表意字元（U+F900～FAFF，如「都」FA26），外觀相同但比對不等；
        # NFKC 同時會把全形標點轉半形，所以題文與題名兩側都要正規化
        text = re.sub(r"\s+", "", unicodedata.normalize("NFKC", c.get("full_text", "")))
        core = unicodedata.normalize("NFKC", re.sub(r"（[^）]*）", "", c["title"]))
        for chunk in re.split(r"[、與暨及]", core):
            chunk = re.sub(r"\s+", "", chunk)
            assert len(chunk) < 2 or chunk in text, f"{c['id']} 題名「{c['title']}」的「{chunk}」不在題文中"
    for s in data.get("exam_scrolls", []):
        assert "官方" not in s["year"].replace("非官方", ""), f"{s['id']} 範卷被標成官方試題：{s['year']}"
    for t in data.get("tracing_cards", []):
        assert os.path.isfile(os.path.join(APP_DIR, t["image"])), f"臨摹圖檔不存在：{t['image']}"
    print(f"  ✓ [6/6] 內容一致性通過（真題卡 {len(past)} 張題名皆在題文中，範卷 {len(data.get('exam_scrolls', []))} 份，臨摹 {len(data.get('tracing_cards', []))} 頁）")


if __name__ == "__main__":
    print("【敷地APP 專案機械卡口驗證】")
    try:
        test_site_data()
        test_generator_execution()
        test_html_output()
        test_desensitization()
        test_service_worker()
        test_content_consistency()
        print("\n🎉 [PASS] 所有 6 項機械驗證指標全數通過！")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ [FAIL] 驗證未通過：{e}")
        sys.exit(1)
