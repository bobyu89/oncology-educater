# 腫瘤科專師學習手冊

腫瘤科實習用的專科護理師學習系統，兼顧臨床實務與專師甄審。內容分三部分：**藥物篇**講每一類抗癌藥從被發現到用在病人身上的過程；**癌別篇**講四種癌症從發現、診斷、分期到治療與照顧；**共用章節**講劑量計算、急症、支持照護與免疫副作用。

## 怎麼開始

照 [學習路徑](handbook/LEARNING_PATH.md) 的十站順序讀：先看藥物的全貌，再讀化療、標靶、荷爾蒙、免疫治療，接著是支持照護與急症，最後進四個癌別的實戰與總複習。

網頁版把這條路徑做成可以追蹤的學習系統：

| 功能 | 說明 |
|------|------|
| 學習白板 | Heptabase 式的白板：每一站是一個區塊，每個步驟是一張卡片，箭頭是閱讀順序；可拖曳、縮放，點卡片在右側打開內容；另有藥物地圖 |
| 學習路徑 | 十站，每一步連到要讀的段落，顯示預估閱讀時間與完成度 |
| 已讀進度 | 每段結尾可以打勾，總覽頁看得到各章讀了幾段 |
| 測驗 | 各章自我測驗可以直接點選作答、看詳解；測驗中心可以跨章抽題 |
| 錯題本 | 最近一次答錯的題目留在錯題本，重做到答對才離開 |
| 藥物卡 | 藥物篇每個藥一張卡，可以翻卡練習，標記「會了」或「還不熟」 |

學習紀錄存在瀏覽器；用線上網頁並登入時，會另存一份到帳號，換裝置也看得到。

## 章節

### 藥物篇

| 章節 | 內容 |
|------|------|
| [抗癌藥物總論](handbook/05-drugs/01-drug-development.md) | 抗癌藥物簡史、一顆藥從實驗室到病人、怎麼讀臨床試驗、命名規則、病人從發現腫瘤到決定治療的路徑、RECIST |
| [化療藥物](handbook/05-drugs/02-cytotoxic-chemotherapy.md) | 從芥子氣、葉酸拮抗劑、鉑類到天然物：各類化療藥的發現、機轉、毒性與臨床用法 |
| [標靶藥物](handbook/05-drugs/03-targeted-therapy.md) | 小分子 TKI、單株抗體、抗體藥物複合體（ADC）：標的、biomarker、類別毒性與抗藥性 |
| [免疫治療藥物](handbook/05-drugs/04-immunotherapy.md) | 免疫檢查點抑制劑、雙特異性抗體、細胞治療：發現史、機轉、biomarker 與臨床用法 |
| [荷爾蒙治療藥物](handbook/05-drugs/05-endocrine-therapy.md) | Tamoxifen、芳香環酶抑制劑、卵巢抑制、SERD：依停經狀態選藥、毒性與抗藥性 |

### 癌別篇

| 章節 | 內容 |
|------|------|
| [肺癌](handbook/01-lung-cancer.md) | NSCLC 與 SCLC：分期（第 9 版）、標靶與免疫治療、台灣藥證與健保、tarlatamab 病房實務 |
| [胰臟癌](handbook/02-pancreatic-cancer.md) | PDAC：可切除性分類、FOLFIRINOX／NALIRIFOX、UGT1A1 與 DPYD、膽道與胰酵素處置 |
| [乳癌](handbook/03-breast-cancer.md) | 依亞型：HR+／HER2+／TNBC，早期與轉移性、CDK4/6、ADC、心毒性與 ILD 監測 |
| [骨肉瘤與軟組織肉瘤](handbook/04-sarcoma.md) | 骨肉瘤、Ewing、軟骨肉瘤、軟組織肉瘤、GIST；高劑量 methotrexate 與 ifosfamide 病房流程 |

每個癌別章節都照同一套 13 段架構：速查卡、流病、病理、分期、治療、處方、副作用、專師實務、腫瘤急症、健保給付、個案、測驗、文獻。

### 共用章節

| 章節 | 內容 |
|------|------|
| [化療基礎與劑量計算](handbook/00-shared/01-chemo-basics.md) | 劑量計算、藥物分類與解毒劑、藥物基因檢測、導管照護、給藥安全 |
| [腫瘤急症](handbook/00-shared/02-oncologic-emergencies.md) | 發燒性嗜中性球低下、TLS、輸注反應與過敏性休克、腸阻塞、肋膜積水等 |
| [支持性照護](handbook/00-shared/03-supportive-care.md) | 止吐、G-CSF、疼痛、輸血、神經病變、惡病質、感染預防 |
| [免疫治療副作用（irAE）](handbook/00-shared/04-irae.md) | 分級處置、類固醇配套、各器官 irAE、二線免疫抑制 |

## 怎麼讀

- **網頁版（GitHub Pages）**：<https://bobyu89.github.io/oncology-educater/>（公開網址；設定方式見下方「發布到 GitHub Pages」）。
- **網頁版（Claude Artifact）**：<https://claude.ai/artifact/HcoEjbf9RVudFnytExVpHK>（私人頁面，需登入擁有者帳號或經分享才能開啟；登入時學習紀錄會存到帳號）。
- **網頁版（離線）**：`site/index.html` 是建置好的單一網頁，下載後用瀏覽器打開即可，醫院網路擋外站時也能用；學習紀錄存在那台裝置的瀏覽器。
- **在 GitHub 上讀**：直接點上表連結，提示框與摺疊答案都會正常顯示；學習路徑見 [handbook/LEARNING_PATH.md](handbook/LEARNING_PATH.md)。

## 目錄結構

```text
handbook/
  chapters.json          章節清單（網頁導覽依這個產生）
  learning-path.json     學習路徑的站別與步驟
  LEARNING_PATH.md       由 learning-path.json 產生的學習路徑（不要手動改）
  01–04-*.md             癌別章節
  05-drugs/              藥物篇
  00-shared/             跨癌別共用章節
docs/STYLE_GUIDE.md      編寫規範：章節模板、提示框、引用格式、藥物卡格式
sources/nhi/             健保藥品給付規定原文（見該資料夾說明）
tools/build_site.py      Markdown → 網頁（學習路徑、測驗、藥物卡都在這裡產生）
tools/lint_chapter.py    章節格式與引用檢查
tools/site_template.html 網頁版面與互動程式
site/index.html          建置結果（可離線開啟）
```

## 建置網頁版

```bash
pip install markdown
```

```bash
python3 tools/build_site.py
```

建置時會檢查站內連結、測驗題格式與藥物卡表格，有問題會印出警告。

## 發布到 GitHub Pages

`.github/workflows/pages.yml` 會在每次推到 `main` 時檢查章節、建置網頁並部署到 GitHub Pages。第一次使用要先開啟 Pages：

1. 到 repo 的 **Settings → Pages**。
2. **Build and deployment → Source** 選 **GitHub Actions**。
3. 推一次到 `main`，或到 **Actions → Deploy handbook to GitHub Pages → Run workflow** 手動執行。

部署完成後的網址是 <https://bobyu89.github.io/oncology-educater/>。GitHub Pages 的網站是公開的；學習紀錄只存在讀者自己的瀏覽器。

## 內容依據

- NCCN、ESMO、ASCO 指引（版本標在各章開頭）
- AJCC／IASLC 分期
- 全民健康保險藥品給付規定 第 9 節「抗癌瘤藥物」原文
- 藥物發現史的原始論文、關鍵臨床試驗與藥品仿單，引用以 APA 第 7 版列出並附 DOI、PMID

## 免責聲明

本手冊是學習用整理，不能取代原始指引、藥品仿單、健保公告與院內規範。實際處方以主治醫師判斷與院內流程為準。
