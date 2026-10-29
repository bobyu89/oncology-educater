# 交班事項

最後更新：2026-10-29（UTC 05:30 前後）。下一個 session 從這份文件開始。

## 一、使用者的決定（不要再問一次）

| 項目 | 決定 |
|------|------|
| 癌別 | 肺癌（樣板）→ 胰臟癌、乳癌、骨肉瘤＋軟組織肉瘤（含 GIST） |
| 用途 | 實習臨床＋專師甄審兼顧 |
| 模組 | 藥物副作用處置、order set 與 SOAP、腫瘤急症與支持照護、個案練習與測驗，全部要 |
| 形式 | Repo（Markdown）＋互動網頁；網頁 UI 依 taste-skill（github.com/leonxlnx/taste-skill）的 app screen 規範 |
| 吉祥物 | Clawd（像素造型），只當吉祥物，不接 AI |
| 健保 | 依使用者提供的原文：`sources/nhi/nhi-drug-rules-1151022.docx`（115/10/22 版） |
| 院內規範 | 沒有，用通用版，需要依院內調整的地方用「院內規範」提示框標註 |
| 語言 | 繁體中文、醫學術語英文、結論先行、比喻教學、每個主張要有指引或文獻 |
| 使用者 | 用量有限，避免不必要的大型工作 |

## 二、已完成

- `handbook/01-lung-cancer.md`：肺癌樣板章，13 段架構完整，87 筆 APA 文獻（PubMed 核對）。**第 9 段健保只有架構，尚未填入。**
- `handbook/00-shared/`：化療劑量、腫瘤急症、支持性照護、irAE 四章。健保內容目前放在「待核對」提示框。
- `tools/build_site.py`＋`tools/site_template.html`：網頁建置（含站內連結檢查）。輸出 `site/index.html`（離線版）與 `site/artifact.html`（發布用，未納入 git）。
- 網頁版已發布：https://claude.ai/artifact/HcoEjbf9RVudFnytExVpHK
- PR：https://github.com/bobyu89/oncology-educater/pull/1（draft，分支 `claude/youthful-lovelace-vwoa5y`）
- 健保原文：`sources/nhi/`（docx 全文＋第 9 節 Markdown）
- 查證資料（下一步直接用，不必重查）：
  - `notes/research/`：肺癌（A、B1、B2）、胰臟癌（pancreas_1–3）、乳癌（breast_1–4）、肉瘤（sarcoma_1–4），每個事實都標 [VERIFIED]/[PARTIAL]/[UNVERIFIED]，附 APA 文獻與 PMID。
  - `notes/nhi/extract_*_verified.md`：健保條文萃取，已由第二個 agent 逐字對照原文校正，含「手冊用總表」可直接放進第 9 段。

## 三、背景工作（皆已完成）

1. **肺癌與共用章節的對抗式查核**：已完成，修正已寫入 `handbook/`，摘要見第五節。腳本在 `notes/workflows/audit-oncology-handbook-*.js`，寫完新章節可沿用，但要把腳本內的暫存路徑改成 `notes/research`。
2. **三個癌別研究的補漏評論**：已完成，補漏內容在 `notes/research/` 各檔案末尾的「## Critic additions」。每份研究的摘要（含重要更正）在 `notes/research/00-research-summaries.txt`，寫章前先讀。重點：
   - 胰臟癌：daraxonrasib（RASolute 302，OS 13.2 對 6.7 個月）已獲美國 FDA 核准（2026-08-26），台灣未上市；TS-1 在台灣沒有術後輔助適應症；Onivyde 第一線 NALIRIFOX 已有台灣適應症；KRAS G12C 只占約 1.6%；PRODIGE 24 用 5 年數據（OS 53.5 對 35.5 個月）。
   - 台灣 UGT1A1*6 頻率約 13%（irinotecan 劑量相關）；5-FU／capecitabine 仿單已加 DPYD 檢測的加框警語（2025-10）。

## 四、下一步（照順序）

1. **裁決 8 項分歧**：看 `notes/audit/audit-2026-10-29.md`，決定是否修改。
2. **補肺癌第 9 段**：依 `notes/nhi/extract_lung_egfr_verified.md`、`extract_lung_alk_other_verified.md`、`extract_lung_io_verified.md`、`extract_lung_chemo_vegf_verified.md` 寫入，取代現有架構表，並移除 `<!-- status: pending -->`。重點：
   - 每列附條號與最新修訂日期；說明通則十二（生物標記報告的三種合格來源）。
   - 第一線 EGFR TKI 擇一使用、不得互換的規則；osimertinib 第一線自 111/4/1 給付；aumolertinib（9.138）是台灣有給付的第三代 EGFR TKI。
   - 免疫治療 9.69：事前審查、PD-L1 表（P011–P016、P021）、哪些組合不需 PD-L1 報告、療程上限。
   - 原文未收載（無健保給付）：lazertinib、capmatinib、selpercatinib、pralsetinib、sotorasib、adagrasib、lurbinectedin、tarlatamab。
   - 肺癌章開頭的版本表「健保給付」欄改為「藥品給付規定 115/10/22 版」。
3. **共用章節的健保提示框改成正式條號**：依 `notes/nhi/extract_shared_supportive_verified.md`（4.1.2 G-CSF、7.2.1–7.2.3 止吐、5.5.3.2.1 zoledronic acid、5.5.4 denosumab、5.5.6 rasburicase、10.7.3 化療病人 B 肝預防）。
4. **撰寫三章**：`handbook/02-pancreatic-cancer.md`、`handbook/03-breast-cancer.md`、`handbook/04-sarcoma.md`（檔名已登記在 `handbook/chapters.json`）。
   - 以肺癌章為範本，照 `docs/STYLE_GUIDE.md` 的 13 段架構。
   - 資料用 `notes/research/<癌別>_*.md` 與 `notes/nhi/extract_<癌別>*_verified.md`。
   - 肉瘤章涵蓋 osteosarcoma、Ewing sarcoma、chondrosarcoma、軟組織肉瘤、GIST。
   - 寫完每章做查核（可沿用 audit 腳本的找錯＋雙驗證流程，但用量有限時改成每章一個查核 agent）。
   - 完成後更新 `handbook/chapters.json` 的 status 與 `README.md` 的章節表。
5. **發布與交付**：重建網頁 → 截圖檢查 → 更新 artifact（新 session 要用 `url` 參數並先 read）→ commit、push → 更新 PR 說明的待辦清單。

## 五、查核結果摘要

完整紀錄：`notes/audit/audit-2026-10-29.md`。

- 確認並已修正 65 項（critical 2、major 12、minor 51），已寫入 `handbook/`。
  - critical：SIADH 出現抽搐或意識改變時，要先給高張食鹽水；fentanyl 貼片只限已耐受鴉片類藥物的病人。
  - major 包括：戒菸後風險變化、durvalumab 肺炎 G3–4 要永久停藥、SCLC 敏感／抗藥復發的切點改為 90 天（Baize et al., 2020）、sunvozertinib 不列第一線、CTCAE 版本統一、dexrazoxane 每日最大劑量等。
- 修正時新增的引用（Baize 2020、Tindle 2018、Gyawali 2026）已補進參考文獻表；建置通過，沒有壞連結。
- **意見分歧未修改 8 項**：兩位驗證者看法不同，紀錄檔附雙方理由，請下次裁決。
- **內容缺口建議 20 項**：評論者提出，未自動加入，可視用量挑高優先的補上。

## 六、常用指令

```bash
pip install markdown
```

```bash
python3 tools/build_site.py
```

```bash
node notes/workflows/screenshot.js /tmp/shots
```

截圖腳本需要先建好輸出資料夾，並使用環境內建的 Playwright。

## 七、注意事項

- `www.nhi.gov.tw` 與 `www.hpa.gov.tw` 會擋自動抓取；健保以 `sources/nhi/` 原文為準，國健署資料改查衛福部新聞稿。
- taste-skill 的腳本（draw.mjs、inspect.mjs）被權限擋下沒有執行，只套用了它的文字規範（無 emoji、無漸層、表格只用細線、一個強調色等）。
- 提示框用 GitHub alert 語法，第一行寫粗體主題，不用 emoji；建置腳本會自動加上類型標籤。
- 引用格式 APA 7，作者超過 20 位列前 19 位＋省略號＋最後一位，附 DOI 與 PMID。
