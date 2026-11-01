# 腫瘤科專師學習手冊

腫瘤科實習用的專科護理師學習手冊，兼顧臨床實務與專師甄審。每個癌別都照同一套 13 段架構寫：流病、病理、分期、治療、處方、副作用、order set、腫瘤急症、健保給付、個案與測驗。

## 章節

| 章節 | 內容 |
|------|------|
| [肺癌](handbook/01-lung-cancer.md) | NSCLC 與 SCLC：分期（第 9 版）、標靶與免疫治療、台灣藥證與健保、tarlatamab 病房實務 |
| [胰臟癌](handbook/02-pancreatic-cancer.md) | PDAC：可切除性分類、FOLFIRINOX／NALIRIFOX、UGT1A1 與 DPYD、膽道與胰酵素處置 |
| [乳癌](handbook/03-breast-cancer.md) | 依亞型：HR+／HER2+／TNBC，早期與轉移性、CDK4/6、ADC、心毒性與 ILD 監測 |
| [骨肉瘤與軟組織肉瘤](handbook/04-sarcoma.md) | 骨肉瘤、Ewing、軟骨肉瘤、軟組織肉瘤、GIST；高劑量 methotrexate 與 ifosfamide 病房流程 |
| [化療基礎與劑量計算](handbook/00-shared/01-chemo-basics.md) | 劑量計算、藥物分類與解毒劑、藥物基因檢測、導管照護、給藥安全 |
| [腫瘤急症](handbook/00-shared/02-oncologic-emergencies.md) | 發燒性嗜中性球低下、TLS、輸注反應與過敏性休克、腸阻塞、肋膜積水等 |
| [支持性照護](handbook/00-shared/03-supportive-care.md) | 止吐、G-CSF、疼痛、輸血、神經病變、惡病質、感染預防 |
| [免疫治療副作用（irAE）](handbook/00-shared/04-irae.md) | 分級處置、類固醇配套、各器官 irAE、二線免疫抑制 |

每個癌別章節都照同一套 13 段架構：速查卡、流病、病理、分期、治療、處方、副作用、專師實務、腫瘤急症、健保給付、個案、測驗、文獻。

## 怎麼讀

- **在 GitHub 上讀**：直接點上表連結，提示框與摺疊答案都會正常顯示。
- **網頁版（線上）**：<https://claude.ai/artifact/HcoEjbf9RVudFnytExVpHK>（私人頁面，需登入擁有者帳號或經分享才能開啟）。
- **網頁版（離線）**：`site/index.html` 是建置好的單一網頁，有章節導覽、全文搜尋、測驗答案摺疊。下載後用瀏覽器打開即可離線使用，醫院網路擋外站時也能看。

## 目錄結構

```text
handbook/
  chapters.json          章節清單與狀態（網頁導覽依這個產生）
  01-lung-cancer.md      各癌別章節
  00-shared/             跨癌別共用章節
docs/STYLE_GUIDE.md      編寫規範：章節模板、提示框、引用格式
sources/nhi/             健保藥品給付規定原文（見該資料夾說明）
tools/build_site.py      Markdown → 網頁
tools/site_template.html 網頁版面
site/index.html          建置結果（可離線開啟）
```

## 建置網頁版

```bash
pip install markdown
```

```bash
python3 tools/build_site.py
```

建置時會檢查站內連結，指向不存在段落的連結會印出警告。

## 內容依據

- NCCN、ESMO、ASCO 指引（版本標在各章開頭）
- AJCC／IASLC 分期
- 全民健康保險藥品給付規定 第 9 節「抗癌瘤藥物」原文
- 關鍵臨床試驗原始論文，引用以 APA 第 7 版列出並附 DOI、PMID

## 免責聲明

本手冊是學習用整理，不能取代原始指引、藥品仿單、健保公告與院內規範。實際處方以主治醫師判斷與院內流程為準。
