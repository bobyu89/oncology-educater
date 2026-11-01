# 胰臟癌（Pancreatic Cancer）

| 項目 | 本章依據 |
|------|---------|
| 治療指引 | NCCN Guidelines：Pancreatic Adenocarcinoma **Version 4.2026**（Ko et al., 2026）、Neuroendocrine and Adrenal Tumors **Version 2.2026**、Genetic/Familial High-Risk Assessment: Breast, Ovarian, Pancreatic, and Prostate **Version 1.2027**（2026-10-29 於 nccn.org 查詢）；Pan-Asian adapted ESMO 臨床指引（Tai et al., 2025，台灣腫瘤醫學會參與表決）。NCCN 專業版全文未能開啟，條文用語取自 NCCN Guidelines for Patients: Pancreatic Cancer 2026（依專業版 v2.2026）與同儕審查文獻 |
| 分期 | AJCC 第 8 版（外分泌胰臟癌；AJCC 2026 年版分期表仍列第 8 版）；胰臟神經內分泌腫瘤已改用第 9 版（2024）。治療分流看 NCCN 可切除性分類，見 [3.8](#38-nccn-可切除性分類) |
| 副作用分級 | NCI CTCAE v5.0（本手冊一律用 v5.0 分級，因為指引與藥品仿單的處置門檻都以 v5.0 撰寫；NCI 已於 2025-07-22 發布 v6.0，NCI 贊助的進行中試驗仍用 v5.0；理由與差異見[化療基礎](00-shared/01-chemo-basics.md#8-ctcae-分級原則)第 8 節） |
| 健保給付 | 藥品給付規定 115/10/22 版（全民健康保險藥品給付規定第 9 節「抗癌瘤藥物」），見 [第 9 段](#9-健保給付與事前審查) |
| 最後更新 | 2026-11-01 |

**這一章的結論先講：** 胰臟癌的治療不是先看 TNM 分期，而是先看**能不能開刀（resectability）**：可切除、邊緣可切除（borderline）、局部晚期、轉移，四群走不同的路。診斷時只有約 10–15% 屬於可切除，台灣 2023 年長表資料有 51.22% 已是 IV 期，所以「在病人體能還撐得住時，把他送進對的治療」比挑藥更重要。開始任何化療之前，專師要確認四件事：（1）有病理（首選 EUS-FNB）且組織夠做 NGS；（2）**所有** PDAC 都送 germline 檢測，KRAS wild-type 者加做 RNA-based fusion 與 MSI 檢測；（3）影像先做、膽道引流後做、CA19-9 要等膽紅素下降後才算基準值；（4）病人的 ECOG 與器官功能撐不撐得住 FOLFIRINOX 這類三、四藥方案（DPYD、UGT1A1 風險見[化療基礎](00-shared/01-chemo-basics.md#12-藥物基因檢測與特殊族群評估)第 12 節）。

---

## 0. 速查卡

| 主題 | 一句話重點 |
|------|-----------|
| 分型 | PDAC（pancreatic ductal adenocarcinoma, 胰管腺癌）約占胰臟腫瘤的 90%（Park et al., 2021），是本章主題。**台灣癌登的「胰臟癌」不等於 PDAC**：2023 年長表侵襲癌中腺癌 73.45%、NET 7.53%、NEC 0.82%。pNET、壺腹癌、IPMN 要先分開，見下方提示框 |
| 台灣數字 | 2023 年新診斷 **3,427 人，排第 11 名**（依官方前十名截止值推算；ASR 7.66／10 萬）；2025 年死亡 **3,204 人，癌症死因第 7 名**（女性第 5 名）。每年死亡數接近新診斷數（兩者年份不同，僅供對照） |
| 診斷時期別 | 台灣 2023 年長表 IV 期占 51.22%（n = 2,950）；國際資料可切除只有 10–15%、轉移約 50–55%（Park et al., 2021） |
| 可切除性 | NCCN 分四群：resectable、borderline resectable、locally advanced、metastatic。看動脈（CA、SMA、CHA）與靜脈（SMV、PV）被腫瘤接觸的程度，**由 MDT 決定**，見 [3.8](#38-nccn-可切除性分類) |
| CA19-9 | 敏感度 79–81%、特異度 82–90%，**不能篩檢**。Lewis-negative（約 5–10%）幾乎不產生 CA19-9；膽道阻塞使假陽性升到 10–60%，所以**引流、膽紅素下降後再抽基準值**（Ballehaninna & Chamberlain, 2012） |
| 基因檢測 | NCCN：**所有 PDAC 病人都做 germline 檢測**；要用藥的局部晚期／轉移病人做腫瘤 NGS。台灣 527 位病人的外顯子研究，19.7% 帶 germline P/LP variant（Cheng et al., 2024） |
| KRAS | 約 83–89%（大型 NGS 系列）。G12D 43.6%、G12V 30.8%、G12R 15.8%、**G12C 只有 1.6%**。KRAS wild-type（約 11–17%）富含可標靶的 fusion 與 MSI-H，要做 RNA-based 檢測 |
| 術後輔助 | mFOLFIRINOX 24 週，5 年追蹤的中位 OS 53.5 對 35.5 個月（HR 0.68；Conroy et al., 2022）；不適合者 gemcitabine ＋ capecitabine（Neoptolemos et al., 2017） |
| 轉移第一線 | FOLFIRINOX、gemcitabine ＋ nab-paclitaxel、NALIRIFOX 都是 NCCN 偏好方案（PS 0–1）；帶 BRCA1/2 或 PALB2 變異者偏好 cisplatin ＋ gemcitabine 或 FOLFIRINOX |
| 台灣藥證與健保 | **健保（115/10/22 版）轉移性第一線**：FOLFIRINOX（oxaliplatin 9.10、irinotecan 9.12.1，限指定品項）、gemcitabine ＋ albumin-bound paclitaxel（9.4、9.5.2）、NALIRIFOX（Onivyde 9.12.2 第 2 點，需事前審查）。**二線**：Onivyde ＋ 5-FU／leucovorin（9.12.2 第 1 點，需事前審查）。另有 S-1（9.46，局部晚期或轉移）、larotrectinib（9.95，NTRK，需事前審查）。**有藥證但原文未見健保**：olaparib（gBRCA 維持）、pembrolizumab（MSI-H）、entrectinib（NTRK）。capecitabine、erlotinib 無胰臟藥證；daraxonrasib、zenocutuzumab 台灣未上市。細節見[第 9 段](#9-健保給付與事前審查) |
| 預後 | 美國 SEER 5 年相對存活率 13.7%（2016–2022）；台灣癌登 2002–2013 年 5 年存活率 6.6%（腺癌 5.2%），數字偏舊，見 [3.9](#39-預後) |

**各情境的治療主軸**（細節與證據見第 4 段）

| 情境 | 偏好方案（NCCN、Pan-Asian ESMO） | 關鍵試驗 | 台灣狀態 |
|------|------------------------------|---------|---------|
| 可切除，先手術 | 術後 mFOLFIRINOX × 12 次（約 24 週），ECOG 0–1。不適合者 gemcitabine ＋ capecitabine（GemCap）；亞洲指引另列 S-1（Tai et al., 2025，建議 4k、4l） | PRODIGE 24：5 年追蹤的中位 OS 53.5 對 35.5 個月（Conroy et al., 2022）；ESPAC-4：OS 28.0 對 25.5 個月，HR 0.82（Neoptolemos et al., 2017）；JASPAC 01（S-1 對 gemcitabine）：OS HR 0.57（0.44–0.72），5 年 OS 44.1% 對 24.4%（Uesaka et al., 2016） | 輔助方案皆非台灣藥證適應症（off-label）：oxaliplatin、irinotecan 只寫轉移性第一線；S-1 藥證為局部晚期或轉移；capecitabine 無胰臟適應症 |
| 邊緣可切除（可切除者是否術前治療有分歧） | 術前治療：FOLFIRINOX／mFOLFIRINOX（限 PS 0–1）或 gemcitabine ＋ nab-paclitaxel；BRCA／PALB2 者 cisplatin ＋ gemcitabine。最多約 6 個月，在高量醫院進行（NCCN, 2026）。Pan-Asian ESMO 則不常規建議可切除者術前治療，除非在臨床試驗中 [II, D]（Tai et al., 2025，建議 4i） | PREOPANC（可切除與邊緣可切除，gemcitabine 化放療對立即手術）：長期追蹤 OS HR 0.73（0.56–0.96），5 年 OS 20.5% 對 6.5%（Versteijne et al., 2022）；PREOPANC-2：FOLFIRINOX 沒有優於化放療（21.9 對 21.3 個月，HR 0.88，P = .32；Janssen et al., 2025） | 術前方案同樣沒有台灣藥證或健保條文 |
| 局部晚期 | FOLFIRINOX／mFOLFIRINOX 或 gemcitabine ＋ nab-paclitaxel 誘導，最多約 6 個月，MDT 每 2–3 個月重評能否手術（Tai et al., 2025，建議 4u、4w）；化放療不是常規 | LAP07：化放療對化療 OS HR 1.03（0.79–1.34）（Hammel et al., 2016）；CONKO-007：R0 率 25% 對 18%，P = .113（Fietkau et al., 2025） | 局部晚期可用的健保條文是 S-1（9.46）與 gemcitabine（9.4）；oxaliplatin、irinotecan、albumin-bound paclitaxel 的條文只寫轉移性 |
| 轉移，PS 0–1，第一線 | FOLFIRINOX／mFOLFIRINOX、gemcitabine ＋ nab-paclitaxel、NALIRIFOX | PRODIGE 4：OS 11.1 對 6.8 個月，HR 0.57（Conroy et al., 2011）；MPACT：8.5 對 6.7 個月，HR 0.72（Von Hoff et al., 2013）；NAPOLI 3：11.1 對 9.2 個月，HR 0.83（Wainberg et al., 2023） | 三者都有藥證與健保（條號見上方「台灣藥證與健保」列） |
| 轉移，PS 2 或 3 | PS 2 偏好 gemcitabine ＋ nab-paclitaxel、capecitabine、gemcitabine（轉移性另有 CAPEOX、FOLFIRI、FOLFOX）；PS 3 轉移性沒有偏好方案（NCCN, 2026，病人版） | 本手冊未取得 PS 2 專屬的隨機試驗數字；MPACT 收 KPS ≥70、PRODIGE 4 收 ECOG 0–1，不能直接套用到 PS 2 | gemcitabine 有健保（9.4）；capecitabine 無胰臟藥證 |
| 維持治療 | germline BRCA1/2 變異，第一線 platinum 至少 16 週後未惡化：olaparib 300 mg 每日兩次 | POLO：PFS 7.4 對 3.8 個月，HR 0.53（0.35–0.82）；OS 19.0 對 19.2 個月，**未達顯著**（Golan et al., 2019；Kindler et al., 2022） | 有藥證（gBRCA、platinum ≥16 週後），**健保原文未見** |
| 二線以後 | gemcitabine 後：nal-IRI ＋ 5-FU／leucovorin。daraxonrasib 300 mg QD：RASolute 302 二線 OS 13.2 對 6.7 個月，HR 0.40（0.30–0.53），美國 FDA 2026-08-26 核准 | NAPOLI-1：OS 6.1 對 4.2 個月，HR 0.67（Wang-Gillam et al., 2016）；RASolute 302（O'Reilly et al., 2026） | Onivyde 二線有健保（9.12.2 第 1 點，需事前審查）；daraxonrasib 台灣未上市 |
| 有可標靶的變異 | 見 [2.4](#24-可標靶的變異與藥物) | | |

> [!IMPORTANT]
> **必背數字**
> - **PRODIGE 24 要用 5 年數據**：DFS 21.4 對 12.8 個月（HR 0.66，0.54–0.82）；OS 53.5 對 35.5 個月（HR 0.68，0.54–0.85）；5 年 OS 43.2% 對 31.4%（Conroy et al., 2022）。常見的「54.4 對 35.0 個月、HR 0.64」是 2018 年的期中數據（Conroy et al., 2018），別混用。
> - ESPAC-4：GemCap 對 gemcitabine，OS 28.0 對 25.5 個月（HR 0.82，0.68–0.98）；長期追蹤 31.6 對 28.4 個月（HR 0.83，0.71–0.98）（Palmer et al., 2025）。
> - 轉移性第一線三個標準：FOLFIRINOX（11.1 個月）、gemcitabine ＋ nab-paclitaxel（8.5 個月）、NALIRIFOX（11.1 個月，對照組 nab-paclitaxel ＋ gemcitabine 9.2 個月）。
> - POLO：PFS 有效、OS 沒有差別（19.0 對 19.2 個月）。
> - **5-FU bolus 是常見的劑量陷阱**：輔助用 mFOLFIRINOX（PRODIGE 24）與 NALIRIFOX 不加 5-FU bolus；轉移性 FOLFIRINOX（PRODIGE 4）有 400 mg/m² bolus。
> - 可切除性口訣：**動脈接觸 ≤180° 是 borderline、>180° 是 locally advanced；靜脈只要能重建就是 borderline**（細節與例外見 3.8）。
> - 分期錨點：AJCC 第 8 版 T1 ≤2 cm、T2 >2–4 cm、T3 >4 cm；N1 是 1–3 顆、**N2 是 ≥4 顆**；T4 或 N2 都是 III 期。

> [!IMPORTANT]
> **本章講 PDAC；這三種要先分開**
> - **胰臟神經內分泌腫瘤（pNET）**：WHO 2019 依 Ki-67 與分裂象分 NET G1（<3%）、G2（3–20%）、G3（>20%，仍是高分化）與 NEC（低分化）；高分化 NET 的特徵變異是 MEN1、DAXX、ATRX，NEC 則是 TP53、RB1 異常（Nagtegaal et al., 2020）。指引是 NCCN Neuroendocrine and Adrenal Tumors v2.2026，分期用 AJCC 第 9 版，不走 PDAC 的化療路線。晚期標靶：sunitinib（PFS 11.4 對 5.5 個月，HR 0.42；Raymond et al., 2011）、everolimus（RADIANT-3，PFS 11.0 對 4.6 個月，HR 0.35；Yao et al., 2011）；兩者在健保有 pNET 專屬條文（9.31、9.36.1，皆需事前審查，見第 9 段）。
> - **壺腹癌（ampullary adenocarcinoma）**：分 intestinal 與 pancreatobiliary 兩種組織亞型。976 位接受 pancreatoduodenectomy 的病人，整體中位存活 67 個月；輔助 gemcitabine 類化療的好處只見於 pancreatobiliary／mixed 亞型（傾向配對後中位存活未達對 32 個月，P = .020），intestinal 亞型沒有（Moekotte et al., 2020，觀察性資料）。另有研究指出基因分型比組織型更能預測化療效益（Ecker et al., 2025）。處置不在本章範圍。
> - **IPMN**：是 PDAC 的前驅病變之一，不是 PDAC。Kyoto 2024 指引用 high-risk stigmata 與 worrisome features 分流，其中**新發或惡化的糖尿病（過去 1 年內）已列為 worrisome feature**；未切除的 IPMN 即使穩定，另外長出 PDAC 的風險仍約為同齡人口的 3–5 倍（Ohtsuka et al., 2024；判準條列見 2.1）。

---

## 1. 流行病學與危險因子

### 1.1 台灣現況

| 指標 | 數字 | 資料來源與年份 |
|------|------|--------------|
| 新診斷人數 | **3,427 人**（男 1,794、女 1,633），占全部癌症新診斷 138,051 人的 2.48%；**排第 11 名**（官方十大癌症最後一名是子宮體癌 3,690 人；依癌登工作表，其後最多的就是胰臟癌） | 台灣癌症登記中心 2023 年（民國 112 年）發生資料；衛福部 2025-12-30 公布（衛生福利部，2025） |
| 發生率 | 年齡標準化發生率（ASR）7.66／10 萬（男 8.66、女 6.77）；粗發生率 14.68／10 萬 | 同上；2000 年 WHO 世界標準人口 |
| 發生趨勢 | 2013 年 2,124 人（ASR 6.29）→ 2018 年 2,813 人（7.12）→ 2023 年 3,427 人（7.66）。人數增加約 61%，ASR 只緩升，人口老化解釋大部分的增加；登記數會事後修訂，引用要註明報告年 | 同上 |
| 死亡人數 | 3,204 人（男 1,706、女 1,498），**癌症死因第 7 名**（男第 7、女第 5），占癌症死亡 5.84%；標準化死亡率 6.3／10 萬；死亡中位年齡 71 歲（男 70、女 74） | 衛福部 2025 年死因統計（2026-06-22 公布；衛生福利部，2026） |
| 死亡趨勢 | 2024 年 2,970 人（同為第 7 名），2025 年增加 7.9%。衛福部指出十大癌症中只有肺癌、胰臟癌、卵巢癌的標準化死亡率比前一年上升；排名由 2015 年第 8 名升到 2025 年第 7 名 | 同上 |
| 診斷時期別 | IV 期 **51.22%**、III 期 16.68%、II 期 17.56%、I 期 12.64%、0 期 0.92%、不明 0.98%（n = 2,950；整併期別） | 2023 年癌登長表（AJCC 第 8 版；癌症登記中心，2025） |
| 組織型 | 侵襲癌（n = 2,923）：腺癌 73.45%、NET 7.53%、NEC 0.82%、solid pseudopapillary neoplasm 1.47%、acinar cell carcinoma 0.79%、其他 | 同上 |
| 診斷年齡 | <50 歲 8.8%、50–69 歲 46.0%、≥70 歲 45.2% | 同上 |
| 首次治療 | 含手術的治療 32.3%；化療 ± 標靶（未手術）40.47%；化療加免疫治療 0.64%；僅緩和照護 15.05%（≥70 歲 26.3%；醫學中心 10.48%、非醫學中心 28.14%）；未接受首次治療 1.49% | 同上 |

長表只涵蓋 103 家長表申報醫院，包含原位癌與所有組織型，而且胰臟癌自 2022 年（民國 111 年）才納入長表，所以 n = 2,950 不等於官方的 3,427 人。

> [!IMPORTANT]
> **台灣胰臟癌的三個教學重點**
> - **發生率沒進前十，死亡卻進前十**：2023 年新診斷 3,427 人，2025 年死亡 3,204 人（年份不同，僅供對照），代表幾乎是「診斷多少、死亡多少」。
> - **癌登的「胰臟癌」不等於 PDAC**：腺癌只占 73.45%，NET 與 NEC 合計約 8.4%。引用數字時先確認分母。
> - **高齡病人容易被排除在積極治療之外**：≥70 歲占診斷人數 45.2%，其中 26.3% 只接受緩和照護；IV 期病人中，50–69 歲 69.51% 接受化療 ± 標靶、11.42% 僅緩和照護，≥70 歲則分別是 52.75% 與 34.56%。這群人先做老年評估再決定強度（見[化療基礎](00-shared/01-chemo-basics.md#12-藥物基因檢測與特殊族群評估)第 12 節）。

> [!CAUTION]
> **待核對：官方診斷中位年齡與台灣近年存活率**
> 長表年齡分組推算的診斷年齡中位數落在 65–69 歲（含 NET 與原位癌），官方 2023 年胰臟癌診斷中位年齡未能取得（國健署網站無法連線）。台灣癌登的存活率報告只涵蓋十大癌症，沒有胰臟癌，所以本手冊用的是 2002–2013 年的研究數字（見 3.9）。

### 1.2 危險因子

| 類別 | 危險因子 | 風險大小 | 臨床意義 |
|------|---------|---------|---------|
| 吸菸 | 目前吸菸、曾經吸菸 | 82 項研究統合：目前吸菸 RR 1.74（1.61–1.87）、曾吸菸 RR 1.2（1.11–1.29）（Iodice et al., 2008）。PanC4 合併分析：目前吸菸 OR 2.2（1.7–2.8），每日 ≥35 支 OR 3.4（Bosetti et al., 2012） | 戒菸後風險下降，但速度慢：Iodice 估計至少 10 年仍偏高，PanC4 約 20 年才回到從未吸菸者的水準（OR 0.98）。戒菸衛教要做 |
| 代謝 | 長期糖尿病 | 35 個世代研究統合 RR 1.94（1.66–2.27）（Ben et al., 2011）；病程 <4 年 OR 2.1、≥5 年 OR 1.5（Huxley et al., 2005） | 糖尿病既是危險因子，也可能是癌症的早期表現，所以確診後第一年風險最高 |
| 代謝 | **新發糖尿病（≥50 歲）** | 3 年內約 0.85%（18／2,122）被診斷胰臟癌，其中 56% 在符合糖尿病標準後 6 個月內確診（Chari et al., 2005）。ENDPAC 分數 ≥3 者胰臟癌盛行率 3.6%，敏感度 78–80%、特異度 80–85%（Sharma et al., 2018） | 好記的整數是「每 100 人約 1 人」。胰臟癌病人 47% 有糖尿病，其中 74% 是 2 年內新發；胰十二指腸切除後 57%（17／30）糖尿病緩解（Pannala et al., 2008） |
| 代謝 | 肥胖 | 21 項前瞻研究：BMI 每增加 5 kg/m²，RR 1.12（1.06–1.17）（Larsson et al., 2007） | 風險增加幅度小，但盛行率高 |
| 胰臟 | 慢性胰臟炎 | 風險隨診斷後時間下降：2 年內 16.16（12.59–20.73），5 年 lag 7.90（4.26–14.66），≥9 年 lag 3.53（1.69–7.38）（Kirkegård et al., 2017） | 2 年內的高風險多半是反向因果（腫瘤造成胰臟炎）或一開始就誤診，真正的長期風險看 ≥9 年 lag 的 3.53 |
| 家族 | 家族史 | 任一親屬罹病 RR 1.80（1.48–2.12）（Permuth-Wey & Egan, 2009）。家族聚集（familial pancreatic cancer）家族中，依一等親罹病人數，SIR 3.46（1 人）、5.44（2 人）、10.78（≥3 人）（Porter et al., 2022）。兩位一等親罹病者的終生風險約 8%，一般人約 1／64（Goggins et al., 2020） | 一等親罹病且年輕發病（<50 歲）者風險更高。符合條件者轉介遺傳諮詢與監測（見 1.3、1.4） |
| 生活型態 | 吸菸、飲酒、體重 | Pan-Asian ESMO 建議不吸菸、限制飲酒、維持健康體重 [III, A]（Tai et al., 2025） | 沒有可用於降低風險的藥物或篩檢工具 |

> [!IMPORTANT]
> **50 歲以後第一次出現糖尿病**
> 新發糖尿病合併體重下降、上腹或背痛，要把胰臟癌放進鑑別診斷，不要只調降血糖藥。3 年內約每 100 位新發糖尿病的 ≥50 歲病人有 1 位被診斷胰臟癌（0.85%；Chari et al., 2005）。在 IPMN 的追蹤指引中，新發或惡化的糖尿病也被列為 worrisome feature（Ohtsuka et al., 2024）。

### 1.3 遺傳性症候群與 germline 變異

| 基因／症候群 | 胰臟癌風險 | CAPS 2020 監測條件 | 建議起始年齡 |
|-------------|-----------|------------------|------------|
| STK11（Peutz-Jeghers） | 個人層級統合分析 RR 132（95% CL 44–261）（Giardiello et al., 2000） | 不論家族史 | 30–40 歲 |
| CDKN2A（p16；FAMMM） | OR 12.33（5.43–25.61），為檢測基因中最高（C. Hu et al., 2018）；p16-Leiden 家族 75 歲累積風險 17%，平均診斷年齡 58 歲（Vasen et al., 2000） | 不論家族史 | 40 歲 |
| BRCA2 | OR 6.20（4.62–8.17），占病人 1.9%（C. Hu et al., 2018） | ≥1 位一等親罹病，或 ≥2 位任何親等罹病 | 約 50 歲（部分中心 45 歲） |
| BRCA1 | OR 2.58（1.54–4.05），占病人 0.6%（C. Hu et al., 2018） | ≥1 位一等親罹病（此項共識程度較低，同意度 69.6%） | 約 50 歲 |
| PALB2 | RR 2.37（1.24–4.50），80 歲前風險 2–3%（Yang et al., 2020） | ≥1 位一等親罹病 | 約 50 歲 |
| ATM | OR 5.71（4.38–7.33）；RR 6.5（4.5–9.5），累積風險 50 歲 1.1%、70 歲 6.3%、80 歲 9.5%（Hsu et al., 2021） | ≥1 位一等親罹病（2020 年新增） | 約 50 歲 |
| Lynch（MLH1、MSH2、MSH6） | 8.6 倍（4.7–15.7），累積風險 50 歲 1.31%、70 歲 3.68%（Kastrinos et al., 2009） | ≥1 位一等親罹病 | 無正式共識 |
| 遺傳性胰臟炎 | 見 1.2 慢性胰臟炎 | 不論基因狀態都建議監測 | 40 歲，或首次胰臟炎發作後 20 年 |
| 家族聚集、無已知變異 | 見 1.2 家族史 | 三者之一：≥3 位同側親屬且其中 ≥1 位是本人一等親；≥2 位互為一等親的親屬且其中 ≥1 位是本人一等親；≥2 位同側親屬且其中 ≥1 位是本人一等親 | 不早於 50 歲，或比最年輕的罹病親屬早 10 歲 |

「親屬」只算血緣親屬。TP53（Li-Fraumeni）的胰臟癌 OR 為 6.70（C. Hu et al., 2018）。CAPS 對突變帶原者的起始年齡沒有達成正式共識，表中年齡是 CAPS 文中描述的一般做法（Goggins et al., 2020）。

> [!CAUTION]
> **待核對：Peutz-Jeghers syndrome 的胰臟癌終生風險**
> 常見的引用數字（11–36%）無法在本手冊已核對的原文中確認：CAPS 2020 只給監測起始年齡，沒有給終生風險百分比；Giardiello 2000 的摘要給的是相對風險與任何癌症的累積風險（15–64 歲 93%）。因此本手冊只列相對風險，不寫終生風險。

### 1.4 高風險族群的監測與一般人不篩檢

**一般風險族群沒有篩檢。** 台灣公費篩檢只有口腔癌、大腸癌、子宮頸癌、乳癌、肺癌五種（衛生福利部，2025），沒有胰臟癌。CA19-9 用在無症狀人口的陽性預測值只有 0.5–0.9%（Ballehaninna & Chamberlain, 2012），所以不是篩檢工具；CAPS 也不建議以腹部超音波作為首選檢查。

**高風險族群的監測**（CAPS Consortium 2020，modified Delphi，同意度 ≥75% 才算共識，共 55 項共識；Goggins et al., 2020）

| 項目 | 共識內容 |
|------|---------|
| 對象 | 見 1.3 的表；監測應在專家多專科團隊、研究情境下進行 |
| 方式 | 首選 **EUS 與 MRI／MRCP**（兩者如何交替未達共識）；CT 不是第一線（累積輻射），只留給無法做 MRI 或 EUS 者；不建議腹部超音波 |
| 間隔 | 無可疑病灶**每 12 個月**；不確定意義的實質病灶且未轉外科：3 個月內再影像；CDKN2A 帶原者有可疑發現但未手術：3–6 個月再影像。小於 1 cm 的無功能 PanNET 與低風險囊腫同樣每 12 個月 |
| 血液檢查 | 空腹血糖與（或）HbA1c 常規追蹤；CA19-9 **只在影像出現可疑特徵時**抽，不當常規篩檢 |
| 新發糖尿病 | 高風險者新發糖尿病，不論年齡都應啟動監測或立即檢查 |
| 目標 | 找到 stage I（T1N0M0）癌與高度異型增生（high-grade dysplasia，PanIN 或 IPMN） |
| 其他 | 吸菸不改變監測間隔 |

Pan-Asian ESMO 指引採相同方向：高風險者在專家中心監測，通常從 50 歲或比最年輕罹病親屬早 10 歲開始 [III, A]，首選每年 EUS 和（或）胰臟 MRI [IV, B]（Tai et al., 2025）。NCCN Genetic/Familial High-Risk Assessment v1.2027 也有胰臟監測章節，其細部條件本手冊未能開啟核對。

### 1.5 Germline 檢測與台灣資料

**為什麼所有 PDAC 都要做 germline 檢測：** 結果同時影響三件事：（1）第一線要不要用 platinum；（2）有沒有資格用 olaparib 維持治療；（3）家人的 cascade testing 與監測。

- **NCCN**：所有胰臟癌病人都應做基因檢測（血液或唾液），基因包括 ATM、BRCA1、BRCA2、CDKN2A、PALB2、MLH1、MSH2、MSH6、PMS2、STK11、TP53；帶原者或家族史強者轉介遺傳諮詢（NCCN, 2026）。
- **ASCO 2019 provisional clinical opinion**：所有胰臟腺癌病人都應做遺傳風險評估（含家族史）；即使家族史不明顯，germline 檢測也「可以討論」（Stoffel et al., 2019）。
- **CAPS 2020** 對「所有新診斷 PDAC 都做 germline 檢測」**沒有達成共識**，不要寫成所有指引一致（Goggins et al., 2020）。
- **Pan-Asian ESMO**：一般建議做 germline BRCA 檢測 [IV, B]，有家族史與高風險者做遺傳諮詢 [III, A]（Tai et al., 2025）。

| 研究 | 族群 | 檢測範圍 | 結果 |
|------|------|---------|------|
| Cheng et al., 2024 | 台灣 5 家醫學中心，527 位未經篩選的病人，中位年齡 62.5 歲 | 外顯子定序，80 個基因 | **19.7%** 帶 P/LP variant；BRCA2 3.60%、ATR 2.66%、ATM 1.9% |
| C. Hu et al., 2018 | 美國 Mayo，95.6% 為非西班牙裔白人 | 6 個基因 | 5.5%（有家族史 7.9%、無家族史 5.2%） |
| Golan et al., 2019 | POLO 篩檢的轉移性病人 | germline BRCA1/2 | 247／3,315（7.5%） |
| Chung et al., 2023 | 台灣，24 位病人 | 全基因體定序 | 8／24（33.3%）；人數太少，不能當盛行率 |

台灣與美國的數字**不能直接比較**，因為基因 panel 差很多（80 對 6 個基因）。Cheng 2024 另外發現：stage III／IV 且帶有 homologous recombination 基因 germline 變異的病人，第一線用 platinum 的中位 OS 是 26.1 個月，未用 platinum 者 9.6 個月（P = .001）；沒有這類變異者則看不到 platinum 的好處（14.5 對 12.6 個月）（回溯性分析）。

> [!CAUTION]
> **待核對：台灣的基因檢測給付**
> Pan-Asian ESMO 指引中，台灣腫瘤醫學會的敘述是：MSI 的免疫組織化學檢測有健保給付，KRAS PCR 與 BRCA PCR 自費，血液 NGS 的 germline BRCA 檢測部分給付（約 60–70% 的費用）（Tai et al., 2025）。這是指引中的二手敘述，沒有對照健保署公告原文（檢測屬醫療服務給付項目，不在藥品給付規定第 9 節），實際收費與給付以院內公告與最新支付標準為準。

---

## 2. 病理與分子標記

### 2.1 組織型與前驅病變

先分「是不是 PDAC」，再看是不是罕見的變異型。下表的比例是美國 SEER 的資料（159,548 位 PDAC），台灣沒有公開的變異型分布。

| 組織型 | 比例 | 要點 |
|--------|------|------|
| 一般型 PDAC（conventional） | SEER 的 PDAC 中 95.9%（Bengtsson et al., 2024） | 本章幾乎所有的治療證據都來自這一型 |
| Colloid carcinoma | 2.6% | 與 adenosquamous、signet ring、undifferentiated carcinoma with osteoclast-like giant cells 同為多變項模型中 OS 的獨立預測因子（Bengtsson et al., 2024） |
| Adenosquamous carcinoma | 0.8%；占胰臟惡性腫瘤 <5%（Auvray Kuentz et al., 2023） | 預後比一般型差（Xiong et al., 2022）。晚期病人用現代方案（FOLFIRINOX 或 gemcitabine ＋ nab-paclitaxel）的 ORR 39.5% 對 9.7%、PFS 7.8 對 4.7 個月；OS 12.7 對 9.2 個月但未達顯著（P = .35）（回溯性、94 位病人；Auvray Kuentz et al., 2023） |
| Signet ring cell carcinoma | 0.5% | 也是 OS 的獨立預測因子（見 colloid 列） |
| Undifferentiated carcinoma 及其亞型 | undifferentiated 0.1%、osteoclast-like giant cells 型 0.1%、rhabdoid 型 0.003% | rhabdoid 型預後最差，中位存活 2 個月、5 年存活 0%；osteoclast-like giant cells 型也是 OS 的獨立預測因子（Bengtsson et al., 2024） |
| Hepatoid carcinoma、medullary carcinoma | 0.01%、0.006% | medullary 預後最好，中位存活 41 個月、5 年存活 33.3%（Bengtsson et al., 2024） |
| 非 PDAC 的胰臟腫瘤（台灣 2023 年長表侵襲癌） | NET 7.53%、NEC 0.82%、solid pseudopapillary neoplasm 1.47%、acinar cell carcinoma 0.79% | 治療不同，見速查卡的提示框 |

**前驅病變（precursor lesions）**

- 三類：**PanIN**（pancreatic intraepithelial neoplasia）、**IPMN**（intraductal papillary mucinous neoplasm）、**MCN**（mucinous cystic neoplasm）。
- WHO 2019 一律改用**兩級**分級（低度與高度異型增生，取病灶中最高的一級），取代舊的三級 PanIN-1/2/3 系統；不建議再用「carcinoma in situ」，一併歸入高度異型增生。Intraductal oncocytic papillary neoplasm 與 intraductal tubulopapillary neoplasm（ITPN）已與 IPMN 分開（Nagtegaal et al., 2020）。
- AJCC 第 8 版把高度異型增生的 PanIN、IPMN、ITPN、MCN 都放進 Tis（Rhee & Park, 2021）。
- 分子時序：KRAS 突變在低度 PanIN 就出現，進展到較高度時才陸續累積 CDKN2A、TP53、SMAD4 的變異（Park et al., 2021）。

> [!IMPORTANT]
> **PanIN-3 是舊名詞**
> WHO 2019 之後病理報告應寫「高度異型增生（high-grade dysplasia）」，不再有 PanIN-3 或 carcinoma in situ。看到舊報告時要知道它們的對應關係；這是常見的陷阱選項。

**IPMN 的風險分層與追蹤**（Kyoto 2024；判準條列依 Vara-Luiz et al., 2025 的整理）

| 類別 | 內容 |
|------|------|
| High-risk stigmata | 胰頭囊性病灶合併阻塞性黃疸；enhancing mural nodule ≥5 mm 或實質成分；主胰管 ≥10 mm；細胞學可疑或陽性（高度異型增生或腺癌） |
| Worrisome features | 急性胰臟炎；CA19-9 上升；**過去 1 年內新發或惡化的糖尿病**；囊腫 ≥30 mm；enhancing mural nodule <5 mm；囊壁增厚或強化；主胰管 5–9.9 mm；主胰管管徑突然改變伴遠端萎縮；淋巴結腫大；囊腫增大 ≥2.5 mm／年 |
| 未切除 IPMN 的追蹤 | 囊腫 <20 mm：6 個月追蹤一次，穩定則每 18 個月；20 mm 至 <30 mm：6 個月追蹤兩次，之後每 12 個月；≥30 mm 且無其他 worrisome feature：每 6 個月。內容：臨床評估、CA19-9、HbA1c、MRI，MRI 有變化時加做 CT 或 EUS |
| 自然史 | 惰性的分支型 IPMN 進展為高度異型增生或浸潤癌：5 年 0.94–3.3%、10 年 2.3–6.6%、15 年 7.6–15%。另外長出 PDAC 的風險約為同齡人口的 3–5 倍，追蹤 5 年後仍存在 |

> [!CAUTION]
> **待核對：Kyoto 2024 的判準條列**
> Kyoto 2024 指引（Ohtsuka et al., 2024）全文無法開啟，上表的 high-risk stigmata、worrisome features 與追蹤間隔取自 Vara-Luiz 等人（2025）對 Kyoto 2024 的表格整理，尚未對照原文。囊腫大小與主胰管的切點在不同指引間有差異，臨床以院內胰臟外科與消化內科的規範為準。

### 2.2 免疫組織化學染色

PDAC 的免疫染色主要用來排除其他胰臟腫瘤、找 dMMR，並提供預後線索。

| 要回答的問題 | 常用染色 | 結果怎麼讀 | 依據 |
|-------------|---------|-----------|------|
| 是不是神經內分泌分化（NET、NEC） | synaptophysin、chromogranin A、INSM1、CD56；Ki-67 | INSM1 在胰臟神經內分泌腫瘤的陽性率 94.4%（17／18），比傳統標記不敏感但較專一；Ki-67 與分裂象決定 WHO G1–G3 | McHugh et al., 2020；Nagtegaal et al., 2020 |
| 是不是 solid pseudopapillary neoplasm（SPN） | β-catenin、LEF1 | SPN 全部呈 diffuse 核內 β-catenin 與 LEF1 陽性（27 例切除標本、8 例細胞學）；高分化 pNET 為陰性 | Singhi et al., 2014 |
| 有沒有 mismatch repair 缺失 | MLH1、MSH2、MSH6、PMS2 | dMMR 約 0.8%，該系列 7 例全是 Lynch syndrome；沒有做多基因定序時，MSI 與 NTRK 可用標準方法檢測 [IV, B] | Z. I. Hu et al., 2018；Tai et al., 2025 |
| 預後（研究用，非常規） | p53、SMAD4、p16（CDKN2A） | 1,146 例切除 PDAC：SMAD4 表現消失，DFS 較短（HR 1.24，1.09–1.43）、OS 較短（HR 1.27，1.10–1.46）；KRAS、CDKN2A、p53、SMAD4 改變的基因數愈多，OS 愈差（3 個 HR 1.28、4 個 HR 1.47），也愈容易以肝轉移復發 | Masugi et al., 2023 |

### 2.3 分子景觀

| 變異 | 頻率 | 說明與依據 |
|------|------|-----------|
| KRAS 突變（整體） | **約 83–89%** | 88%（n = 3,594；Singhi et al., 2019）、89.3%（n = 2,483；Philip et al., 2022）、83.1%（美國轉移性，n = 2,433；Norton et al., 2025）、86%（n = 318；Lena et al., 2025）。「90% 以上」的寫法來自較早的文獻與指引敘述（Park et al., 2021 寫 90–92%、Tai et al., 2025 寫 90–95%），大型 NGS 系列的數字略低 |
| KRAS 亞型 | G12D 43.6%、G12V 30.8%、G12R 15.8%、其他（G13、Q61、多重）8.2%、**G12C 1.6%**（占 KRAS 突變者） | G12D、G12V 的 OS 比 wild-type 差（HR 1.29 與 1.23）；G12R 在突變型中最好（中位 OS 13.2 個月）（Norton et al., 2025） |
| 四個經典驅動基因 | KRAS、CDKN2A、TP53、SMAD4 | PDAC 反覆出現的體細胞驅動基因（Cancer Genome Atlas Research Network, 2017） |
| DNA 修復缺陷 | BRCA／FANC 變異 14%；BRCA1/2 變異 7.5% | Singhi et al., 2019；Lena et al., 2025 |
| MSI-H／dMMR | 0.8%（7／833），7 例全是 Lynch syndrome；MSI-H 與（或）TMB-H 0.5% | Z. I. Hu et al., 2018；Singhi et al., 2019。KRAS wild-type 中 MSI-H 4.7%、KRAS 突變中 0.7%（Philip et al., 2022） |
| NTRK 融合 | 0.8%（3／400）；KRAS wild-type 中 6.25%（2／32） | DNA-only 定序出現 6 個偽陽性，要用 RNA 驗證（Allen et al., 2023）；以 IHC 篩檢再做 RNA-NGS 的 297 例胰臟癌中 0 例（Demols et al., 2023） |
| NRG1 融合 | 47 例全基因體定序中，3 例 KRAS wild-type 腫瘤全是 NRG1 融合 | 其中 2 位使用 afatinib 的病人有反應（Jones et al., 2019） |

**KRAS wild-type 的 PDAC**（約 11–17%，由各系列的突變率反推）富含可標靶的變異。Philip 等人的 KRAS wild-type 次族群（Philip et al., 2022）：

| 變異 | 比例 | 變異 | 比例 |
|------|------|------|------|
| BRAF 突變 | 13.0% | RET fusion | 1.3% |
| BRAF fusion | 6.6% | NRG1 fusion | 1.3% |
| FGFR2 fusion | 5.2% | ERBB2（HER2）amplification | 2.2% |
| ALK fusion | 2.6% | NTRK amplification（**amplification，不是 fusion**） | 1.8% |
| MET amplification | 1.3% | TMB-high | 4.5% |

> [!TIP]
> **KRAS 像是「卡住的油門」**
> 把 PDAC 想成一輛車：KRAS 突變是油門卡死，在 PanIN 早期就出現；CDKN2A、TP53、SMAD4 是煞車、警示燈與導航陸續壞掉，病灶才從癌前變成癌。約九成的車是油門卡死；剩下一成多的車油門正常，但被裝了一個「外接加速器」（ALK、RET、NRG1、NTRK 的 fusion，或 BRAF 突變）。外接加速器正是標靶藥打得到的地方，所以 KRAS wild-type 不是「沒有突變」，而是「要換個方式找」：做 RNA-based 檢測。G12C 只占 1.6%，肺癌那套 G12C 抑制劑在胰臟幾乎派不上用場。

### 2.4 可標靶的變異與藥物

| 變異 | 約略頻率 | NCCN 列出的藥物 | 胰臟癌證據（本手冊核對到的） | 台灣狀態 |
|------|---------|----------------|--------------------------|---------|
| germline BRCA1/2、PALB2 | gBRCA 約 7.5%（POLO 篩檢人群） | 第一線偏好 cisplatin ＋ gemcitabine 或 FOLFIRINOX／mFOLFIRINOX；維持治療偏好 olaparib，rucaparib 為特定情況（BRCA1/2 或 PALB2，platinum 之後） | POLO：PFS 7.4 對 3.8 個月（HR 0.53，0.35–0.82）；OS 19.0 對 19.2 個月（HR 0.83，P = .3487）；3 年 OS 33.9% 對 17.8%（Golan et al., 2019；Kindler et al., 2022） | olaparib 有藥證（gBRCA，第一線 platinum ≥16 週後未惡化）；健保 9.85 無胰臟適應症，**原文未見**。rucaparib：本手冊未核對 |
| MSI-H／dMMR、TMB-H | MSI-H 約 0.5–0.8% | pembrolizumab、dostarlimab、nivolumab ＋ ipilimumab（病人版列於二線，限未用過免疫治療者） | FDA 仿單（KEYTRUDA，2026-07-10 版；Merck Sharp & Dohme LLC, 2026）的非大腸直腸癌 MSI-H／dMMR 合併分析：胰臟癌 n = 22，ORR 18%（95% CI 5–40）；全癌別 ORR 約 31–34%（Marabelle et al., 2020；Maio et al., 2022）。仿單另指出：本地判定為 MSI-H／dMMR 的腫瘤，中央檢測只有 56.7% 為 MSI-H、62.1% 為 dMMR，免疫治療前要確認 | pembrolizumab 有藥證（不分癌別 MSI-H／dMMR，先前治療後）；健保 9.69 **原文未見**胰臟癌，也未見不分癌別的 MSI-H／dMMR 給付 |
| NTRK1–3 fusion | 0.8%（KRAS wild-type 中 6.25%） | larotrectinib、entrectinib、repotrectinib | 彙整分析中胰臟癌病人極少：larotrectinib 2 位中 1 位有反應（Hong et al., 2020）、entrectinib 3 位中 2 位有反應（Doebele et al., 2020）；全癌別 ORR 分別為 79% 與 57% | larotrectinib 有藥證，且有**健保 9.95**（113/6/1：成人胰臟癌需先前至少一次全身性治療失敗又惡化；需事前審查，每次 12 週）。entrectinib、repotrectinib 有 NTRK 藥證；健保 9.93、9.131 **原文未見** NTRK 或胰臟癌 |
| NRG1 fusion | 約 1.3%（KRAS wild-type 中） | zenocutuzumab（HER2 × HER3 雙特異性抗體） | eNRGy 胰臟癌 cohort：15／36 有反應（42%，95% CI 25–59），DOR 7.4 個月，PFS 9.2 個月；36 位全是 KRAS wild-type（Schram et al., 2025）。FDA 2024-12-04 加速核准 | 台灣未上市 |
| BRAF V600E | BRAF 突變 13.0%（KRAS wild-type 中，含非 V600E） | dabrafenib ＋ trametinib | 本手冊未取得胰臟癌專屬數字 | 台灣藥證未核對；第 9 節無胰臟癌條文 |
| RET fusion | 1.3%（KRAS wild-type 中） | selpercatinib | 同上 | 同上 |
| ALK、ROS1、FGFR2 fusion | ALK 2.6%、FGFR2 5.2%（KRAS wild-type 中）；ROS1 未取得 | ROS1：entrectinib、repotrectinib；FGFR：erdafitinib；ALK 列為檢測目標，病人版未配對特定藥物 | 同上 | 同上 |
| HER2 amplification／overexpression | ERBB2 amplification 2.2%（KRAS wild-type 中） | fam-trastuzumab deruxtecan | 同上 | 同上 |
| KRAS G12C | 1.6% | sotorasib、adagrasib | CodeBreaK 100（sotorasib 960 mg 每日，n = 38）：ORR 21%（10–37），PFS 4.0 個月，OS 6.9 個月（Strickler et al., 2023）；adagrasib 600 mg 每日兩次：胰臟癌 7／21 有反應（33.3%）（Bekaii-Saab et al., 2023） | 兩者有台灣藥證，但**沒有胰臟癌適應症**；健保原文未見 |
| KRAS G12 / G13 / Q61（pan-RAS） | 約 83–89% | daraxonrasib（RAS(ON) 抑制劑）300 mg 每日一次 | RASolute 302（二線，n = 500）：OS 13.2 對 6.7 個月（HR 0.40，0.30–0.53）；PFS 7.2 對 3.6 個月（HR 0.49）；ORR 30% 對 11%（O'Reilly et al., 2026） | 美國 FDA 2026-08-26 核准（適應症比試驗寬，涵蓋已接受至少一線治療或不適合多藥治療者）；**台灣未上市**；第一線數據尚未發表；NCCN 專業版是否收錄未能確認 |
| KRAS G12D | 43.6% | 尚無 G12D 專一的核准藥物 | 專一抑制劑與降解劑都在早期臨床試驗（2026 年發表）；例如 HRS-4642 ＋ nab-paclitaxel／gemcitabine 第一線 ORR 63.3%（n = 30，phase 1b/2；Cui et al., 2026） | 台灣未上市，不屬於常規治療 |

第 9 節原文以「胰」搜尋，只命中 9.4、9.5.2、9.10、9.12.1、9.12.2、9.31、9.36.1、9.46、9.95 九條。表中「健保原文未見」是逐項對照的結果；「未核對」是指本手冊沒有查該藥的 TFDA 藥證。

> [!CAUTION]
> **待核對：藥物清單來源**
> 表中「NCCN 列出的藥物」取自 NCCN Guidelines for Patients: Pancreatic Cancer 2026（依專業版 v2.2026）的生物標記表；專業版 v4.2026 對各藥的使用條件（線別、證據等級）未能開啟核對。NRG1 與 zenocutuzumab 的配對，病人版沒有明寫，是依 FDA 核准與試驗結果配對。daraxonrasib 在 2026-08-26 核准之後，NCCN 是否已納入需查 v4.2026 專業版。

### 2.5 檢測策略：組織 NGS、ctDNA 與 NCCN 建議

| 檢測 | 檢體 | 用途 | 注意 |
|------|------|------|------|
| Germline | 血液或唾液 | **所有 PDAC**（NCCN）；結果影響 platinum 選擇、olaparib 資格與家族 cascade testing | 需遺傳諮詢；不等於腫瘤的變異 |
| 腫瘤 NGS（DNA） | 腫瘤組織（優先） | NCCN：會用藥物治療的胰臟癌都要檢測；一次涵蓋 KRAS、BRCA1/2、PALB2、BRAF、HER2、MSI-H／TMB 等 | 只做 DNA 偵測 fusion 不完整；NTRK 在 DNA-only 出現 6 個偽陽性（Allen et al., 2023） |
| RNA-based fusion 檢測 | 腫瘤組織 | **KRAS wild-type 者建議做**：NTRK、NRG1、RET、ALK、ROS1、FGFR2、BRAF fusion（前六者為 NCCN 生物標記表的 fusion 項目，BRAF fusion 依 Philip et al., 2022 的 KRAS wild-type 分析加入；Tai et al., 2025 建議 2l 為可做延伸分析 [IV, B]，2m 為轉移性 KRAS wild-type 者應評估 MSI、NTRK 與其他罕見 fusion [III, B]；指引未指定平台，本手冊建議用 RNA-based，因為 DNA-only 的 NTRK 有偽陽性） | EUS-FNB 要多穿幾針，檢體量要同時夠診斷與檢測 |
| MSI／MMR | IHC 或 PCR／NGS | 轉移性且 KRAS wild-type 者建議檢測 [III, B]；沒有多基因定序時用標準方法 [IV, B] | 本地與中央判定可能不一致（見 2.4） |
| 血液 ctDNA | 血液 | 只在組織無法檢測時使用（NCCN, 2026） | NCCN 不建議用 ctDNA 做診斷 |

Pan-Asian ESMO 的建議是**不可切除的 PDAC 做體細胞 KRAS 檢測、所有 PDAC 做 germline BRCA 檢測**（Tai et al., 2025，建議 2k）；NCCN 則是所有 PDAC 做 germline 檢測（涵蓋較多基因）、會用藥者做腫瘤 NGS。Pan-Asian ESMO 對 KRAS wild-type 者建議再做延伸檢測（建議 2l 為可做，2m 為轉移性者應評估 MSI、NTRK 與其他罕見 fusion）；NCCN 病人版則未以 KRAS wild-type 作為檢測的啟動條件，而是所有會用藥物治療者都要做生物標記檢測。因為 BRCA／PALB2 影響第一線選擇、維持治療更要接在 platinum 之後，所以**結果要在第一線治療開始前拿到**：確診當天就送 germline 與腫瘤 NGS，不要等第一線失敗才補。

---

## 3. 診斷與分期

### 3.1 臨床表現

| 位置或情境 | 常見表現 | 備註 |
|-----------|---------|------|
| 胰頭、鉤突 | 阻塞性黃疸（皮膚鞏膜變黃、茶色尿、灰白便、搔癢）、體重下降、上腹痛；**Courvoisier sign**：無痛、可觸及的膽囊合併黃疸 | 膽管早早被堵住，常因黃疸提早就醫；膽汁淤積症狀愈多，腫瘤愈局限（Porta et al., 2005） |
| 胰體、尾 | 上腹痛或背痛、體重下降、食慾差，通常沒有黃疸 | 症狀出現時多半已晚期：185 位前瞻性病人中，體尾腫瘤沒有 I 期、>80% 是 IV 期（Porta et al., 2005） |
| 全身症狀的頻率 | 倦怠 86%、食慾不振 85%、**體重下降 85%**、腹痛 79%、茶色尿 59%（n = 185；Porta et al., 2005） | 症狀都不專一，所以需要「想到」才會去照影像 |
| 症狀相對於對照組的 OR | 食慾不振 41、灰白便 31、腹痛 30、**黃疸 20**、體重下降 12、搔癢 5.0（Holly et al., 2004） | 美國舊金山灣區的人口為基礎病例對照研究 |
| 新發糖尿病 | 見 1.2 | ≥50 歲新發糖尿病要想到胰臟癌 |
| 血栓 | 遊走性或不尋常的血栓性靜脈炎可能是隱藏癌症的第一個表現（Trousseau's syndrome；Varki, 2007）。化療試驗的 VTE 合併率 5.9%（13 項試驗、5,694 人），血栓預防試驗的對照組為 16.5%，表示化療試驗低估了風險（Chiasakul et al., 2021）；韓國門診化療病人 6 個月的癌症相關血栓 4.16%（20／481）（Ha et al., 2023） | 預防與處置見[支持性照護](00-shared/03-supportive-care.md#7-癌症相關靜脈血栓vte)第 7 節 |

> [!IMPORTANT]
> **Courvoisier 與 Trousseau：兩個容易混淆的名詞**
> - **Courvoisier sign**：黃疸合併無痛、可觸及的膽囊，提示惡性的遠端膽道阻塞（例如胰頭癌）。Courvoisier 1890 年只是描述 187 例膽道阻塞，觀察到結石引起時膽囊很少擴大，他**從未提出過「定律」**；現代解釋是惡性阻塞造成膽管內長期高壓，而結石常伴纖維化或間歇性阻塞（Fitzgerald et al., 2009）。MRCP 容積測量也支持這個徵象：非結石性膽總管阻塞的膽囊容積較大（P = .03；Murphy et al., 2012）。
> - **Trousseau's syndrome**：癌症相關的血栓傾向（含遊走性血栓性靜脈炎），胰臟癌是經典病因（Varki, 2007）。**不要和 Trousseau's sign 混淆**（低血鈣時血壓計袖帶誘發的手足痙攣）。

> [!CAUTION]
> **待核對：無痛性黃疸與 Courvoisier sign 的出現比例**
> 本手冊未能取得可引用的數字：胰臟癌病人以「無痛性黃疸」表現的比例，以及 Courvoisier sign 的敏感度，在已核對的原文中都沒有。考試或臨床上請把它當成「提示」，不要當成診斷條件。

### 3.2 Work-up 流程

1. **病史與身體評估**：體重變化、黃疸相關症狀（茶色尿、灰白便、搔癢）、上腹或背痛、脂肪便、新發糖尿病、血栓史、家族史、吸菸史；ECOG（見[化療基礎](00-shared/01-chemo-basics.md#1-體能狀態ecog-與-kps)第 1 節）。
2. **抽血**：CBC、肝腎功能（總與直接膽紅素、ALP、AST／ALT）、albumin、INR、血糖與 HbA1c、CA19-9（時機見 3.4）。CA19-9 正常時可加驗 CEA 與 CA-125（NCCN, 2026，病人版）。
3. **影像，先於任何膽道支架**：多期對比增強的胸腹骨盆 CT（即 pancreas-protocol CT），含 late arterial phase 與 portal venous phase [III, A]；**胰頭腫瘤合併黃疸時，影像要在膽道引流或放支架之前做** [IV, A]；影像要在治療開始前 4 週內 [III, A]。CT 不能做或結果不確定時可改用腹部 MRI [IV, C]，此時胸部 CT 為必要 [III, A]；手術前以肝臟 MRI 確認沒有小的肝轉移 [III, B]；PET-CT 不用來診斷原發腫瘤 [III, D]，可用於局部腫瘤的分期，以及遠端轉移不確定時（影像可疑或 CA19-9 很高）[III, B]。局部疾病的影像要在 MDT（含胰臟影像、胰臟外科、腫瘤內科）讀片 [III, A]（Tai et al., 2025，建議 2a–2g、2i）。
4. **取得病理**：EUS 導引的 FNB 為首選（見 3.3）。NCCN 病人版：只要不是先手術，化療前就一定要有活檢（術前治療、局部晚期、轉移都是）；明確可切除而直接手術者，術前是否穿刺依外科與院內流程。
5. **遺傳與分子檢測**：germline 與腫瘤 NGS（見 1.5、2.5），確診當天就送。
6. **膽道阻塞、營養與疼痛**：依 3.5 決定要不要引流；營養與疼痛評估見[支持性照護](00-shared/03-supportive-care.md)。
7. **分期腹腔鏡**：高風險者考慮（見 3.6）。
8. **MDT 決定可切除性**：用 NCCN 解剖學標準，再加生物學與病人條件（見 3.8）。

> [!WARNING]
> **支架之前先照影像**
> 膽道支架的偽影與 ERCP 後胰臟炎會讓 CT 難以判讀血管侵犯，造成分期錯誤（Corallo et al., 2025）。黃疸病人除非有膽管炎或其他引流指徵（見 3.5），**先完成 pancreas-protocol CT，再談引流**（Tai et al., 2025，建議 2b）。

### 3.3 EUS 與取樣

- **NCCN 病人版**：針吸活檢的首選是 **EUS 導引**，檢體較好、風險較低；若同時要做 ERCP 放支架，可先活檢。要多穿幾針，檢體量要同時夠診斷與生物標記檢測。懷疑有轉移時改由超音波或 CT 導引經皮穿刺。**NCCN 不建議用 ctDNA 做診斷**（NCCN, 2026）。
- **FNB 對 FNA**：18 項隨機試驗統合，FNB 診斷準確度 87% 對 80%（P = .02）、取得組織核心的比例 80% 對 62%，且穿刺針數較少（van Riet et al., 2021）。12 項前瞻研究統合在實質性胰臟腫塊的結果相同方向：FNA 準確度較低（risk difference −0.08）、檢體適切率較低，併發症相近（Yao et al., 2024）。
- 局部疾病在化療前應有細胞學或組織學證據，最好經 EUS [III, A]（Tai et al., 2025，建議 2h）。

### 3.4 CA19-9

| 重點 | 內容 | 依據 |
|------|------|------|
| 診斷效能 | 有症狀病人：敏感度 79–81%、特異度 82–90%；切點通常 37 U/mL。用在無症狀人口的陽性預測值只有 0.5–0.9%，**不是篩檢工具**。2,283 位病人的系統性回顧：中位敏感度 79%、特異度 82% | Ballehaninna & Chamberlain, 2012；Goonetilleke & Siriwardena, 2007 |
| Lewis-negative | 5–10% 的人是 Lewis 抗原陰性，幾乎不產生 CA19-9，造成偽陰性。中國 PDAC 世代（FUT3 基因型，n = 682）6.9% 為 Lewis-negative，這群人 CEA（63.8%）與 CA125（51.1%）的敏感度高於 CA19-9（19.1%）。日本 2,418 位切除 PDAC：7.7% 為 CA19-9 不表現者（≤2 U/mL），DUPAN-2 可作替代 | Ballehaninna & Chamberlain, 2012；Liu et al., 2020；Luo et al., 2017；Omiya et al., 2026 |
| 膽道阻塞的偽陽性 | 阻塞性黃疸使偽陽性率升到 10–60%；數值偏高時要**在黃疸解除後重抽** | Ballehaninna & Chamberlain, 2012；Goonetilleke & Siriwardena, 2007 |
| 預後 | 術前 <37 U/mL：中位存活 32–36 個月；>37 U/mL：12–15 個月。>100 U/mL 提示不可切除或已轉移。治療後下降 ≥20–50% 預測存活較長 | Ballehaninna & Chamberlain, 2012 |
| 治療決策 | CA19-9 可用來衡量疾病負荷，並輔助治療決定 [III, B]。IAP 2017 的「生物學邊緣可切除」標準之一是 CA19-9 >500 U/mL | Tai et al., 2025 |
| 預測隱藏轉移 | 術前治療後的病人，腫瘤 ≥3 cm 與基線 CA19-9 >500 U/mL 是隱藏轉移的獨立預測因子（見 3.6） | Rompen et al., 2026 |

> [!TIP]
> **CA19-9 像是一個會誤報也會失靈的煙霧警報器**
> 有些人的警報器天生沒裝電池（Lewis-negative），癌症再大也不響；有些情況下警報器會被「廚房的油煙」誘發（膽道阻塞、膽管炎），沒有火也響。所以 CA19-9 的用法是：**在膽紅素下降後抽基準值，之後看趨勢**；一個孤立的數字，不管高低，都不能單獨下結論。

> [!WARNING]
> **CA19-9 正常不能排除 PDAC**
> Lewis-negative 的病人 CA19-9 可以一直是正常或接近 0，卻已經有轉移。影像高度懷疑時，不要因為「CA19-9 正常」而延後穿刺或轉介；基準值為零的病人，之後追蹤也不能靠 CA19-9，要靠影像與 CEA／CA-125。

### 3.5 膽道阻塞：什麼時候要引流

胰頭癌病人常常是黃疸來就醫，問題是「馬上引流」還是「先手術」。

| 情境 | 建議 | 依據 |
|------|------|------|
| 可切除、可在診斷後約 1 週內手術 | **不要常規術前引流**。隨機試驗（膽紅素 40–250 μmol/L，即 2.3–14.6 mg/dL）：術前引流 4–6 週後再手術，嚴重併發症 74%，直接手術 39%（直接手術組 RR 0.54，0.41–0.71；P < .001）；引流本身的併發症 46% | van der Gaag et al., 2010 |
| 有膽管炎 | **要引流**。Tokyo Guidelines 2018：Grade II（中度）可從早期或緊急引流獲益，Grade III 是伴器官功能障礙的重症；並抽血液培養 | Kiriyama et al., 2018 |
| 膽紅素 >250 μmol/L（約 14.6 mg/dL）且手術會延後超過 2 週 | 內視鏡引流 [I, B] | Tai et al., 2025，建議 4h |
| 嚴重症狀性黃疸（如劇烈搔癢）、手術延後，或黃疸病人要先做術前化療 | 可引流 | Dumonceau et al., 2018（ESGE） |
| 不可切除、預期以非手術處置 | 優先用 **self-expandable metal stent（SEMS）**，阻塞與再介入較少，膽管炎 8% 對 21%；術前引流用 10-mm SEMS | Sawas et al., 2015；Dumonceau et al., 2018 |
| 病理尚未確診 | 用 covered SEMS 或塑膠支架，**不用 uncovered SEMS**。塑膠支架約 3 個月會堵塞，只適合短暫橋接 | Dumonceau et al., 2018 |

化療何時開始與膽紅素有關：FOLFIRINOX 的兩個關鍵試驗都要求膽紅素 ≤1.5 × ULN（PRODIGE 4 允許先引流）；各藥的肝功能調整見第 5、7 段。

> [!WARNING]
> **引流後發燒、冷顫＝先想膽管炎**
> 放過膽道支架的病人若出現發燒、右上腹痛、黃疸加重（Charcot 三聯徵），或再加低血壓與意識改變（Reynolds 五聯徵，已是 Grade III 重症），要當成急症：抽血液培養、依膽管炎處置給抗生素並聯絡消化內科處理引流（Kiriyama et al., 2018）。若同時在化療，還要想到嗜中性球低下的發燒（見[腫瘤急症](00-shared/02-oncologic-emergencies.md#1-發燒性嗜中性球低下)第 1 節）。

> [!NOTE]
> **院內規範：引流時機與支架選擇**
> 術前引流的時機、支架材質（SEMS 或塑膠）與是否與外科共同決定，各院流程不同；上表是文獻原則，實際以院內胰臟外科與消化內科的共識為準。

### 3.6 分期腹腔鏡

CT 看不到的肝臟或腹膜小轉移，會讓病人白白開一次刀（non-therapeutic laparotomy）。分期腹腔鏡（staging laparoscopy, SL）就是在開腹前先看一眼。

**PREOPANC-2 的預先設定分析**（術前治療後接受手術的可切除與邊緣可切除 PDAC；Rompen et al., 2026）：322 位進入手術探查，其中 74.5% 先做 SL。

- 隱藏轉移 39／322（12.1%），是放棄切除的主要原因（90.5%）。
- 無效開腹率：SL 組 4.5%，未做 SL 組 17.1%（P = .002；需治療人數 NNT = 8）。
- 隱藏轉移的獨立預測因子：腫瘤 ≥3 cm、基線 CA19-9 >500 U/mL。

| 風險因子數 | 隱藏轉移比例（95% CI） |
|-----------|---------------------|
| 0（腫瘤 <3 cm 且 CA19-9 ≤500 U/mL） | 2.8%（0.9–8.0） |
| 1 項 | 14.8%（5.9–32.5） |
| 2 項都有 | 28.9%（17.0–44.8） |

結論：SL 應該**依風險因子個別化**，不是每個人都做。Pan-Asian ESMO 在討論局部晚期病人誘導治療後能否手術時指出，診斷性腹腔鏡在亞洲部分機構是常規做法，但沒有納入任何指引（Tai et al., 2025）。NCCN 對 SL 適應症的條文本手冊未能開啟核對。

---

### 3.7 AJCC 第 8 版 TNM

外分泌胰臟癌**仍是 AJCC 第 8 版**（AJCC 2026 年版分期表）；胰臟神經內分泌腫瘤才已改用第 9 版（2024）。Pan-Asian ESMO 同樣建議用 UICC TNM 第 8 版 [III, A]（Tai et al., 2025，建議 3a）。以下定義取自 Allen et al. (2017) 與 Rhee & Park (2021) 對第 8 版的整理（AJCC 手冊原書未開啟核對）。

**T：以腫瘤大小分類**（第 8 版刪除了「胰外侵犯」的定義）

| T | 定義 |
|---|------|
| Tis | 原位癌，含高度異型增生的 PanIN，以及伴高度異型增生的 IPMN、ITPN、MCN |
| T1 | 最大徑 **≤2 cm**；T1a ≤0.5 cm、T1b >0.5 且 <1 cm、T1c 1–2 cm |
| T2 | >2 cm 且 ≤4 cm |
| T3 | >4 cm |
| T4 | 侵犯 celiac axis、SMA 和（或）common hepatic artery（CHA），不論大小 |

**N：以陽性淋巴結顆數分類**

| N | 定義 |
|---|------|
| N0 | 無區域淋巴結轉移 |
| N1 | 1–3 顆區域淋巴結轉移 |
| N2 | **≥4 顆**區域淋巴結轉移 |

M0 為無遠端轉移，M1 為有遠端轉移。

**分期組合**

| 期別 | TNM |
|------|-----|
| 0 | Tis N0 M0 |
| IA | T1 N0 M0 |
| IB | T2 N0 M0 |
| IIA | T3 N0 M0 |
| IIB | T1–3 **N1** M0 |
| III | **任何 T N2** M0，或 **T4 任何 N** M0 |
| IV | 任何 T、任何 N、**M1** |

與第 7 版的差異：T 改成以大小為準；T4 不再寫「不可切除」並納入 CHA；N1 拆成 N1 與 N2；T1–3 N2 由 IIB 移到 III 期；IPMN、ITPN、MCN 的高度異型增生納入 Tis（Rhee & Park, 2021）。

驗證資料：2,318 位 R0 切除病人的遞迴分割分析找到腫瘤大小切點 2.2 與 4.8 cm、淋巴結切點 0、1–3、≥4 顆，支持第 8 版的設計（Allen et al., 2017）。1,525 位病人的 5 年 OS：N0 35.6%、N1 20.8%、N2 10.9%，淋巴結狀態的預後力很強，但在淋巴結陰性的病人中 T 分類沒有預後意義（van Roessel et al., 2018）。

> [!IMPORTANT]
> **邊界值與期別，考試常考**
> - **T1 是「≤2 cm」（含 2 cm），N2 是「≥4 顆」（含 4 顆）**。部分綜說文章誤印成「<2 cm」與「>4 顆」，以 Allen 2017 與 Rhee & Park 2021 的原文定義為準。
> - 只要 **N2 或 T4**，就是 III 期；有 M1 就是 IV 期。
> - 外分泌胰臟癌是第 8 版，**不要寫成第 9 版**（第 9 版是胰臟神經內分泌腫瘤）。

> [!TIP]
> **AJCC 是成績單，NCCN 可切除性是路線圖**
> 病理 TNM 要等腫瘤切下來、淋巴結數完才能打出來，像考試後的成績單，用來估計預後；而開刀前要決定走哪條路，靠的是影像看血管被腫瘤包到什麼程度，也就是 NCCN 的可切除性分類（Rhee & Park, 2021）。所以病歷上「治療決定」寫的是 resectable／borderline／locally advanced，不是「III 期」。

### 3.8 NCCN 可切除性分類

**治療是依可切除性決定，不是依 AJCC 分期。** 分類只看有沒有遠端轉移，以及腫瘤接觸動脈（celiac artery, CA；SMA；CHA）與靜脈（SMV、portal vein, PV）的程度。診斷時約 10–15% 屬可切除，其餘中有一群邊緣可切除（Park et al., 2021；Tai et al., 2025）。

| 分類 | 動脈（CA、SMA、CHA） | 靜脈（SMV、PV） |
|------|--------------------|---------------|
| **Resectable** | 與 CA、SMA、CHA **無腫瘤接觸** | 無接觸；或接觸 **≤180°** 且血管輪廓規則（無 contour irregularity） |
| **Borderline resectable：頭部、鉤突** | CHA 有實質腫瘤接觸、但未延伸到 CA 或肝動脈分叉，能安全完整切除並重建；SMA 實質接觸 **≤180°**；變異動脈（副右肝動脈、替代右肝動脈、替代 CHA 等）有接觸時，要記錄其存在與接觸程度 | SMV／PV 接觸 **>180°**，或 ≤180° 但輪廓不規則或有血栓，且上下游血管適合安全切除與重建；IVC 有實質腫瘤接觸 |
| **Borderline resectable：體尾部** | CA 實質接觸 **≤180°**（另有文獻列：CA >180° 但未侵犯主動脈、GDA 完整，可做 modified Appleby，見下方「待核對」） | 同上 |
| **Locally advanced：頭部、鉤突** | SMA 或 CA 實質接觸 **>180°** | SMV／PV 因腫瘤侵犯或阻塞（腫瘤或單純血栓）而**無法重建** |
| **Locally advanced：體尾部** | SMA 或 CA 接觸 >180°；CA 接觸合併主動脈侵犯 | 同上 |
| **Metastatic** | 任何遠端轉移（含非區域淋巴結） | 不論解剖上能不能切除，都不應先手術 |

術前治療後，腫瘤與血管之間的「實質接觸」可能被血管周圍脂肪的「模糊密度增加或條索狀變化」取代，這種變化也要在報告中描述（Corallo et al., 2025 轉載的 NCCN 註腳）。

> [!CAUTION]
> **待核對：NCCN v4.2026 的體尾部 borderline 條款**
> 上表的度數標準取自兩篇同儕審查文獻轉載的 NCCN 表格（Corallo et al., 2025；Chu & Fishman, 2024）；NCCN 專業版 v4.2026 與 JNCCN 全文都無法開啟，病人版只列分類名稱、沒有度數。兩處文獻在**體尾部**有出入：Søreide & Jamieson (2026) 仍把「CA 接觸 >180° 但未侵犯主動脈、GDA 完整而可做 modified Appleby」列為 borderline；Corallo 等人轉載的「NCCN 2023」表格沒有這一句。臨床上這一類病人是 borderline 還是 locally advanced，以 MDT 與最新版 NCCN 為準。

**生物學與病人條件**：Pan-Asian ESMO 建議同時用 NCCN 的解剖學標準，以及 IAP 共識的生物學與條件因素 [III, B]（Tai et al., 2025，建議 3b）。IAP 2017 定義邊緣可切除時，除解剖外還加了：CA19-9 >500 IU/mL、經切片或 PET-CT 診斷的區域淋巴結轉移、ECOG ≥2（Tai et al., 2025 的描述）。日本肝膽胰外科學會另提出 PET-CT 的 SUVmax、對術前治療的反應、年齡與 Charlson 共病、modified Glasgow Prognostic Score 或嗜中性球／淋巴球比值。

**荷蘭 DPCG 標準不同，不要和 NCCN 混用**：DPCG 的 resectable 是靜脈接觸 ≤90°；borderline 是動脈 ≤90° 或靜脈 >90–270° 但未阻塞；locally advanced 是動脈 >90° 或靜脈 >270°、或阻塞（Chu & Fishman, 2024；Søreide & Jamieson, 2026）。

> [!TIP]
> **動脈像電線，靜脈像水管**
> 動脈被腫瘤包住超過半圈（>180°），就像一條供應腸子與肝臟的主電線被包死，剪斷重接的代價太大，所以 >180° 是 locally advanced；半圈以內（≤180°）還可以處理，是 borderline。靜脈像水管，只要上下游還有好的管子，切掉一段再接起來（reconstruction）就行，所以「靜脈可重建＝borderline，無法重建＝locally advanced」。這是記憶口訣，不是臨床判斷的替代品。

### 3.9 預後

| 指標 | 數字 | 資料來源 |
|------|------|---------|
| 美國 5 年相對存活率（所有期別） | **13.7%**（2016–2022） | NCI SEER Cancer Stat Facts（2026-10-29 查詢） |
| 依診斷時期別 | 局部 43.6%（占 15%）；區域 17.0%（占 28%）；遠端 3.4%（占 51%）；不明 12.5%（占 5%） | 同上（SEER 21） |
| 台灣 5 年存活率 | 全部 **6.6%**（男 5.95%、女 7.47%）；腺癌 5.2%；內分泌腫瘤、NET 與淋巴瘤 41.8–59.1%。1 年 25.52%、3 年 9.22%、10 年 4.71%。診斷時平均年齡 67.3 歲 | 台灣癌登 2002–2013 年，n = 18,320（Chang et al., 2018） |
| 切除後的淋巴結狀態 | 5 年 OS：N0 35.6%、N1 20.8%、N2 10.9% | van Roessel et al., 2018 |
| 術前 CA19-9 | <37 U/mL 中位存活 32–36 個月；>37 U/mL 12–15 個月 | Ballehaninna & Chamberlain, 2012 |
| 試驗中的最佳情況 | 術後 mFOLFIRINOX：5 年 OS 43.2%，中位 53.5 個月 | Conroy et al., 2022 |

美國 SEER 的遠端轉移占 51%，與台灣 2023 年長表的 IV 期 51.22% 幾乎一樣，是很好的對照。

> [!CAUTION]
> **待核對：台灣的存活率數字偏舊**
> 台灣 5 年存活率 6.6% 來自 2002–2013 年診斷的病人，期間早於 FOLFIRINOX、NALIRIFOX 與現行的術前治療策略。官方近年（癌登存活報告）沒有胰臟癌的數字；其 2013 年的 ASR（6.04／10 萬）也與現行癌登工作表（6.29）略有出入，引用時要註明研究期間，不要當成目前的預測。試驗結果（如 5 年 OS 43.2%）則是經過篩選、能接受 mFOLFIRINOX 的病人，不能直接套到一般病人。

> [!IMPORTANT]
> **預後的三個考試重點**
> - 診斷時期別決定存活：美國局部 43.6%、遠端 3.4%（5 年相對存活率）。
> - 切除後 N 狀態比 T 大小更有預後意義（N0／N1／N2 的 5 年 OS 為 35.6%／20.8%／10.9%）。
> - 「台灣癌登的胰臟癌」含 NET，NET 的存活明顯較好（41.8–59.1%），所以腺癌的 5 年存活率（5.2%）才是 PDAC 的數字。

---

## 4. 治療策略（依分期）

胰臟癌的治療有兩條主線：**能不能開刀**決定路線（[3.8](#38-nccn-可切除性分類)的可切除性分類），**體能與器官功能**決定強度（ECOG、膽紅素、神經病變、DPYD 與 UGT1A1）。本段先講手術本身（術式、淋巴結、切緣），再依可切除、邊緣可切除、局部晚期、轉移四群往下走，最後是生物標記導向藥物與台灣的藥證和健保現況。每個建議都標指引與關鍵試驗；台灣沒有藥證或沒有健保給付的，文中直接寫明。

### 4.1 治療分流總覽

進入治療前的六個分流問題（由上往下問，答不出來的先補齊）：

1. **有遠端轉移嗎？** 有 → 轉移性（4.8），手術不是第一步。影像可疑時考慮分期腹腔鏡（[3.6](#36-分期腹腔鏡)）。
2. **血管接觸程度？** 動脈 ≤180° 或靜脈可重建 → resectable 或 borderline；動脈 >180° 或靜脈無法重建 → locally advanced（[3.8](#38-nccn-可切除性分類)）。
3. **生物學風險高嗎？** CA19-9 >500 U/mL（要在膽紅素下降後抽）、PET-CT 或切片證實的區域淋巴結轉移、ECOG ≥2，IAP 2017 把這些列為「生物學邊緣可切除」的條件（Tai et al., 2025）；術前治療後接受手術的病人，腫瘤 ≥3 cm 加基線 CA19-9 >500 U/mL 預測隱藏轉移（Rompen et al., 2026）。
4. **撐得住幾個藥？** ECOG 0–1、膽紅素 ≤1.5 × ULN、沒有既存神經病變，且 UGT1A1、DPYD 風險可接受 → 三、四藥方案；否則雙藥或單藥（見[化療基礎](00-shared/01-chemo-basics.md#12-藥物基因檢測與特殊族群評估)第 12 節）。
5. **分子資料到了嗎？** germline 與腫瘤 NGS（KRAS wild-type 者加 RNA 檢測）要在第一線開始前拿到（[2.5](#25-檢測策略組織-ngsctdna-與-nccn-建議)）。
6. **在哪裡治療？** NCCN 建議術前治療在高量醫院，或在高量醫院的指導下進行，最長約 6 個月（NCCN, 2026，病人版）。

```
診斷（pancreas-protocol CT ＋ EUS-FNB ＋ germline／腫瘤 NGS）→ MDT 分類
 ├─ 遠端轉移 ───→ 4.8 全身治療（依 ECOG）→ 維持／二線（4.9）→ 標靶（4.10）
 ├─ 局部晚期 ───→ 4.7 誘導化療（FOLFIRINOX 或 GnP）→ 每 2–3 個月重評 → 可切除才手術
 ├─ 邊緣可切除 ─→ 4.6 術前治療 → 重評 → 手術 → 術後化療（術前加術後總量約 6 個月）
 └─ 可切除 ─────→ 4.3 先手術 → 4.4 輔助化療（或在高量中心做術前治療，4.5）
```

> [!IMPORTANT]
> **各情境的化療期間（考試常考）**
> - 輔助 mFOLFIRINOX：12 次、約 24 週（PRODIGE 24；Conroy et al., 2018）。輔助化療最好在術後 12 週內開始；若有術前治療，術前加術後總量最多約 6 個月（NCCN, 2026，病人版）。
> - 術前或局部晚期的誘導：最多約 6 個月，MDT 每 2–3 個月重評能否手術（NCCN, 2026，病人版；Tai et al., 2025，建議 4u、4w）。
> - 轉移性第一線：PRODIGE 4 建議有反應者做 6 個月化療（Conroy et al., 2011）；之後視反應與耐受，考慮維持治療或休息。

### 4.2 手術：術式、淋巴結與切緣（R0／R1）

手術是唯一可能治癒的方法，但只開刀不補化療，多數人仍會復發：CONKO-001 的觀察組中位 DFS 6.7 個月、5 年 OS 10.4%（Oettle et al., 2013）；ESPAC-1 沒有接受化療者 5 年存活率 8%（Neoptolemos et al., 2004）。這是輔助化療（4.4）的根據。

| 腫瘤位置 | 常見術式 | 病房端要知道的 |
|---------|---------|--------------|
| 胰頭、鉤突 | pancreatoduodenectomy（Whipple 手術，含保留幽門的變型） | 同時切除胰頭、十二指腸、膽囊與遠端膽管，重建要接胰腸、膽腸與胃（或十二指腸）腸三處；術後瘻管與胃排空問題見下表 |
| 胰體、尾 | distal pancreatectomy，通常合併脾臟切除 | 沒有膽道與胃腸的重建；切緣預後意義的資料比胰頭少（Holm & Verbeke, 2022） |
| 病灶橫跨頸部或需要全胰才能清乾淨切緣 | total pancreatectomy | 內分泌與外分泌功能全失：終生胰島素與胰酵素替代。胰酵素每主餐 40,000–50,000 單位 lipase、點心減半（Dominguez-Muñoz et al., 2025） |
| 靜脈受侵犯但可重建 | 加做 SMV／PV 切除重建 | 這就是「靜脈可重建＝borderline」的意思（[3.8](#38-nccn-可切除性分類)）；動脈切除只在特定情境由 MDT 決定 |

> [!CAUTION]
> **待核對：術式與病灶位置的對應**
> 上表是依解剖原則整理的一般性敘述，本手冊未能開啟 NCCN 專業版的手術原則，也沒有逐項對照外科指引原文。術式選擇（含微創手術、保留幽門、動脈切除）以主刀外科醫師與院內胰臟外科共識為準。

**淋巴結廓清。** ISGPS 建議至少檢出 12–15 顆淋巴結（胰頭癌的站別：5、6、8a、12b1、12b2、12c、13a、13b、14a、14b、17a、17b；胰體尾癌另加 10、11、18）；Pan-Asian ESMO 小組討論後維持「至少 16 顆」，並強調**所有切除的淋巴結都要送檢**，才能做正確的病理分期（Tai et al., 2025，建議 4e）。淋巴結顆數直接決定 N1 或 N2（見 [3.7](#37-ajcc-第-8-版-tnm)）。

**醫院量能。** 美國 Medicare 資料（1994–1999 年）中，胰臟切除術的調整後死亡率在極低量醫院為 16.3%，極高量醫院為 3.8%（Birkmeyer et al., 2002）。這是美國資料，台灣各院的量與結果本手冊沒有取得；但 NCCN 對術前治療的建議也要求在高量醫院進行（NCCN, 2026，病人版）。

**圍術期血栓預防。** 除非有禁忌，接受手術的病人圍術期給 UFH 或 LMWH 預防（Tai et al., 2025，建議 4g）。

**術前膽道引流**：可切除、可在約 1 週內手術者不常規引流；適應症見 [3.5](#35-膽道阻塞什麼時候要引流)。

#### 切緣：R0 不是只有一種定義

病理報告的 R 分類取決於「離切緣多近才算乾淨」：

| 定義 | R0 | R1 | 備註 |
|------|----|----|------|
| 直接接觸標準（0 mm） | 腫瘤沒有碰到墨染切緣 | 腫瘤直接接觸切緣 | 傳統較寬鬆的定義 |
| 1 mm 標準（Leeds 病理協定） | 腫瘤距切緣 >1 mm | 腫瘤距切緣 ≤1 mm（含直接接觸） | 需要標準化取材：多色墨染、軸向切片、廣泛取樣（Verbeke et al., 2006） |

- 定義一改，R0 率就大幅改變：法國前瞻性多中心研究（147 位胰頭癌）中，R0 率由 75%（R1 定義為直接侵犯 0 mm）降到 35%（R1 定義為 <1.0 mm）（Delpero et al., 2017）。英國 Leeds 的標準化病理檢查使胰臟癌的 R1 率達 85%（22／26）（Verbeke et al., 2006）。
- 21 項研究、6,056 位病人的統合分析：R0 且切緣 >1 mm 者，整體存活優於 R1 與切緣 ≤1 mm 的 R0 合併組（合併組 HR 1.36，95% CI 1.23–1.56）（Leonhardt et al., 2022）。
- 術前化療或化放療之後，以 1 mm 為準的傳統 R0 定義不再適用於這些標本（Holm & Verbeke, 2022）。
- 各試驗對 R0／R1 的定義不一致，所以**不同試驗的 R0 率不能直接比較**；法國研究建議未來試驗要註明切緣的毫米數（Delpero et al., 2017）。

> [!IMPORTANT]
> **看病理報告的三個問題**
> 1. 用的是 0 mm 還是 1 mm 標準？同一個標本，R0 率可以差一倍。
> 2. 哪一個切緣有問題？切緣侵犯常是多處，而且以後方切緣最常見（32 例中 21 例；Verbeke et al., 2006）。全胰切除後，SMA 切緣直接被侵犯有獨立預後意義（以 SMA 切緣 ≥0.5 mm 為 R0：中位存活 19 對 10 個月，P = .010，101 位病人）；遠端胰切除的整體切緣狀態則未見影響存活（Aaquist et al., 2024，丹麥全國資料，樣本小）。
> 3. 病人有沒有做過術前治療？術前治療後的切緣判讀要由病理科說明。

> [!TIP]
> **切緣像是挖地瓜**
> 腫瘤像會往四周長根的地瓜。「0 mm 標準」只問：鏟子有沒有鏟到地瓜的根？「1 mm 標準」則問：鏟子周圍有沒有至少留 1 mm 的乾淨泥土？用嚴格的尺，漏掉的根比較少，所以 R1 變多；但 R1 多不代表手術變差，是尺變嚴。看試驗和病理報告時，先問「用哪一把尺」。

**術後併發症（ISGPS 定義）**：這四項是病房端最常聽到的名詞。

| 併發症 | 定義重點 | 備註 |
|--------|---------|------|
| 胰臟瘻管（POPF，ISGPS 2016） | 引流液有可測量的量，且 amylase >3 × 院內血清 amylase 正常上限，並伴臨床相關狀況。原本的 grade A 改稱 biochemical leak，不再算瘻管；B：處置改變，引流 >3 週或需內視鏡／經皮重新放置；C：需再手術、器官衰竭或死亡 | Bassi et al., 2017 |
| 胃排空延遲（DGE，ISGPS 2007） | 術後第 1 週底仍無法回到標準飲食（含延長鼻胃管留置），依臨床衝擊分 A、B、C | Wente et al., 2007a。各級切點本手冊只取得二手整理，未列 |
| 術後出血（PPH，ISGPS 2007） | 依發生時間（≤24 小時為早期、>24 小時為晚期）、部位（腔內或腔外）與嚴重度分級 | Wente et al., 2007b |
| 乳糜漏（chyle leak，ISGPS 2017） | 術後第 3 天起，引流液、引流口或傷口出現乳白色液體，且 triglycerides ≥110 mg/dL（≥1.2 mmol/L）；最多約 10% 的切除術發生。A：只需飲食限制；B：住院延長，需要營養支持、octreotide 或引流；C：更侵入性的處置、加護病房或死亡 | Besselink et al., 2017 |

預防瘻管的隨機試驗（單中心，300 位）：pasireotide 900 µg 皮下注射每日兩次，從手術當天早上開始用 7 天，嚴重度 ≥3 級的瘻管、漏或膿瘍 9% 對 21%（RR 0.44，95% CI 0.24–0.78，P = .006）（Allen et al., 2014）。台灣的相關規定：pasireotide 的藥證只有庫欣氏病（Cushing's disease），用在預防瘻管屬適應症外；octreotide 的藥證適應症則明寫「預防胰臟手術後的併發症」，健保 5.4.3（octreotide 注射劑，102/1/1）第 2 點同樣給付此用途，最長使用七天；5.4.5（somatostatin，89/5/1）第 1 點為最長使用五天。

> [!NOTE]
> **院內規範：術後處置**
> 預防性 octreotide 的使用與否、引流管拔除標準、鼻胃管與早期進食流程，各院胰臟外科做法不同，以院內路徑為準。上表只是定義與文獻證據。

### 4.3 可切除（resectable）：先手術，還是先術前治療

**兩大指引的立場不同，這是目前最大的分歧。**

- **Pan-Asian ESMO**：可切除者以**手術加輔助化療**為標準；不常規建議術前治療，除非在臨床試驗中 [II, D]（Tai et al., 2025，建議 4i）。小組討論時認為，Prep-02/JSAP-05 的結果雖然有說服力，但當時尚未經同儕審查發表，證據等級不能與已發表的試驗同等看待（該試驗之後已發表，見 4.5）。
- **NCCN**：病人版列出術前治療的偏好方案：FOLFIRINOX 或 mFOLFIRINOX（**限 PS 0–1**）、gemcitabine ＋ nab-paclitaxel、帶 BRCA 或 PALB2 變異者 cisplatin ＋ gemcitabine；在高量醫院進行，最長約 6 個月（NCCN, 2026，病人版）。專業版對「明確可切除者是否優先術前治療」的原文本手冊未能開啟。

> [!CAUTION]
> **待核對：NCCN 專業版對可切除者的術前治療條文**
> 本手冊只讀到 NCCN 病人版（依專業版 v2.2026）；專業版 v4.2026 的 Resectable 流程圖（哪些高風險特徵建議先術前治療）未能開啟。臨床上以 MDT 與最新版 NCCN 為準。

**支持術前治療的理由與反證都來自隨機試驗（4.5）：**

| 方向 | 證據 |
|------|------|
| 有利 | PREOPANC：切除者中 R0 率 71% 對 40%，長期追蹤 OS HR 0.73（Versteijne et al., 2020, 2022）。Prep-02/JSAP-05：OS 37.0 對 26.6 個月，HR 0.73，術後 pN1 比例 59.2% 對 81.4%（Unno et al., 2026） |
| 不利或未證實 | NORPACT-1：術前 FOLFIRINOX 的整體存活有輸給立即手術的趨勢（HR 1.52）（Labori et al., 2024）。PREOPANC-2：術前 FOLFIRINOX 沒有贏過術前化放療（Janssen et al., 2025） |
| 還在等 | Alliance A021806（NCT04340141）：第 3 期，**術前加術後 mFOLFIRINOX 對立即手術加術後 mFOLFIRINOX**，主要指標 OS，登錄收案 358 人，ClinicalTrials.gov 狀態為 active, not recruiting；截至 2026-10-29 尚無結果發表。PREOPANC-3 也只有試驗計畫發表 |

**怎麼選（實務原則）：** 影像上明確可切除、CA19-9 不高、沒有淋巴結疑慮、體能好又開刀量能足夠的病人，先手術再 mFOLFIRINOX 是證據最硬的路（4.4）；有生物學高風險特徵（CA19-9 >500 U/mL、腫瘤 ≥3 cm、疑似淋巴結轉移、MASTERPLAN 所列的腫瘤 >4 cm 或胰外侵犯）者，術前治療是合理選項，最好由 MDT 決定或收進試驗。這是依上表證據整理的原則，不是指引逐字條文。

### 4.4 術後輔助治療

**結論：術後 12 週內開始，ECOG 0–1 的病人用 mFOLFIRINOX 12 次；不適合者用 gemcitabine ＋ capecitabine；亞洲指引另列 S-1。** NCCN 偏好 GemCap 與 mFOLFIRINOX，其他可用 5-FU/LV、gemcitabine、5-FU、capecitabine（NCCN, 2026，病人版）。

| 條件 | 方案與劑量（試驗版本） | 關鍵試驗與數字 | 台灣 |
|------|--------------------|--------------|------|
| ECOG 0–1，可耐受 | **mFOLFIRINOX** q2w × 12：oxaliplatin 85、irinotecan 150（原 180，試驗中途改為 150）、leucovorin 400 mg/m²，5-FU 2,400 mg/m² 持續輸注 46 小時，**無 bolus** | PRODIGE 24（n = 493，R0／R1）：DFS 21.4 對 12.8 個月（HR 0.66，0.54–0.82）；OS **53.5 對 35.5 個月（HR 0.68，0.54–0.85）**；5 年 OS 43.2% 對 31.4%；3–4 級不良反應 75.9% 對 52.9%（Conroy et al., 2018, 2022） | oxaliplatin、irinotecan 藥證與健保（9.10、9.12.1）只寫轉移性第一線，**輔助是適應症外、無健保條文** |
| 不適合 mFOLFIRINOX | **GemCap** × 6：gemcitabine 1,000 mg/m² D1,8,15 ＋ capecitabine 830 mg/m² 每日兩次 D1–21，q28d | ESPAC-4（n = 730）：OS 28.0 對 25.5 個月（HR 0.82，0.68–0.98）；長期追蹤 31.6 對 28.4 個月（HR 0.83，0.71–0.98）；3–4 級事件發生於 226／359 位（63%）對 196／366 位（54%）（Neoptolemos et al., 2017；Palmer et al., 2025） | capecitabine 無胰臟藥證，健保 9.17 無胰臟適應症 |
| 亞洲選項 | **S-1** 依 BSA 每日兩次（<1.25 m² 40 mg；1.25 至 <1.5 m² 50 mg；≥1.5 m² 60 mg），D1–28 後休 14 天（6 週週期）× 4 | JASPAC 01（n = 385，日本，非劣性設計）：OS HR 0.57（0.44–0.72），5 年 OS 44.1% 對 24.4%（Uesaka et al., 2016） | TS-1 藥證與健保 9.46（113/2/1）只寫局部晚期或轉移，**輔助是適應症外** |
| 更虛弱或不能用合併方案 | gemcitabine 1,000 mg/m² D1,8,15 q28d × 6，或 5-FU/LV | CONKO-001（對觀察）：DFS 13.4 對 6.7 個月（HR 0.55）；OS HR 0.76（0.61–0.95）（Oettle et al., 2013）。Pan-Asian 建議這群人用 gemcitabine 或 5-FU/LV，證據等級 IV（Tai et al., 2025，建議 4m） | gemcitabine 健保 9.4（115/9/1） |
| **不建議** | gemcitabine ＋ nab-paclitaxel | APACT（n = 866）：獨立審查 DFS 19.4 對 18.8 個月，HR 0.88（0.729–1.063），P = .18，**主要指標未達成**；3 級以上神經病變 15% 對 0%（Tempero et al., 2023） | 不屬輔助標準方案 |

> [!WARNING]
> **輔助 mFOLFIRINOX 與轉移性 FOLFIRINOX 的處方不能互相套用**
> 輔助用（PRODIGE 24）：irinotecan 150、**不加 5-FU bolus**。轉移性 FOLFIRINOX（PRODIGE 4）：irinotecan 180、**加 5-FU 400 mg/m² bolus**。NALIRIFOX 也不加 bolus。開立或核對醫囑時先確認「用在哪個情境」，劑量細節見第 5 段。

> [!IMPORTANT]
> **誰才是「fit for mFOLFIRINOX」？**
> PRODIGE 24 收 18–79 歲、WHO PS 0–1、術後 CA19-9 ≤180、膽紅素 ≤1.5 × ULN，並**排除** Gilbert 症、UGT1A1*28/*28、既存神經病變（UNICANCER, n.d.-a，ClinicalTrials.gov NCT01526135）。所以 53.5 個月的好數字屬於篩選過的族群。ESPAC-4 長期追蹤中，有 26.4% 的病人本來就不符合 PRODIGE 24 的條件，GemCap 在這群人仍有好處（25.9 對 20.7 個月，HR 0.71，0.52–0.98）（Palmer et al., 2025）。DPYD 與 UGT1A1 檢測見[化療基礎](00-shared/01-chemo-basics.md#12-藥物基因檢測與特殊族群評估)第 12 節。

**老年與 PS 2。** ESPAC-4 納入少數 WHO PS 2 的病人（9 與 12 人），GemCap 在 PS 2 沒有看到好處（死亡 HR 0.56，95% CI 0.18–1.78，樣本太小）；ESPAC-3 每組各有 64 位（12%）PS 2 的病人。一項 ≥80 歲的回溯性世代中，接受輔助化療者中位存活 17.2 個月，未接受者 12.7 個月（HR 0.72，0.65–0.79）（皆引自 Tai et al., 2025，原始研究未逐篇核對；回溯性資料）。日本習慣對老年或 PS 2 病人使用 S-1（Tai et al., 2025）。

> [!CAUTION]
> **待核對：JASPAC 01 與台灣輔助治療的藥證邊界**
> （1）JASPAC 01 的中位 OS（46.5 對 25.5 個月）不在 Lancet 摘要，本手冊只在 Pan-Asian ESMO 與日本綜說文章看到；摘要也沒有寫明 R1 切除是否符合納入條件。（2）gemcitabine 的台灣許可證適應症逐字內容本手冊未核對，術後輔助是否落在許可範圍以仿單為準；健保 9.4 原文只說「依藥品許可證登載之適應症範圍內」，沒有限制線別或分期。Pan-Asian ESMO 的台灣段落（台灣腫瘤醫學會參與）寫明輔助情境下現有方案都未獲核准或給付（Tai et al., 2025）。

**輔助化放療：沒有證明能增加存活。**

| 試驗 | 設計與結果 |
|------|-----------|
| ESPAC-1（Neoptolemos et al., 2004） | 289 位，2 × 2 設計；放療為 20 Gy 加 5-FU。5 年存活率：有化放療 10% 對沒有 20%（P = .05）；有化療 21% 對沒有 8%（P = .009）。作者結論：化療有益，化放療對存活有害 |
| RTOG 9704（Regine et al., 2011） | 451 位，全部做 5-FU 化放療（50.4 Gy），前後的化療隨機分為 gemcitabine 或 5-FU。胰頭癌 5 年 OS 22% 對 18%（中位 20.5 對 17.1 個月）；多變項分析 P = .08。首次復發部位：局部 28%，遠端 73% |
| EORTC 40013（Van Laethem et al., 2010） | 第 2 期，90 位，R0 切除的胰頭癌：gemcitabine 對 gemcitabine 後接 50.4 Gy 化放療。以下為化放療組對 gemcitabine 組：中位 OS 兩組都是 24 個月；首次局部復發 11% 對 24%；治療完成率 73.3% 對 86.7% |

這些是 gemcitabine 與 5-FU 時代的試驗；遠端復發才是主要失敗模式（RTOG 9704：73%），所以輔助重點在全身治療。是否對 R1 或淋巴結陽性的個別病人加放療，由 MDT 決定；本手冊未取得 NCCN 專業版對輔助放療的條文。

**術後追蹤。**

- NCCN 病人版：病史與身體檢查、CA19-9、胸部 CT，以及腹部與骨盆的對比增強 CT 或 MRI，「視需要」安排；**未給固定間隔**（NCCN, 2026，病人版）。Pan-Asian ESMO：建議定期追蹤 [III, B]（Tai et al., 2025，建議 6a）。
- 支持定期影像的資料是觀察性的：333 位復發病人中，常規影像追蹤者中位 OS 28 個月，只在症狀出現時檢查者 23 個月（P = .01）；校正後得到復發導向治療的 OR 2.57（1.22–5.41），OS 校正 HR 0.75（0.56–0.99）；無症狀亞群 30 對 21 個月（P = .03）（Andel et al., 2025）。

> [!CAUTION]
> **待核對：追蹤間隔**
> 「每 3–6 個月影像」之類的固定間隔，本手冊沒有取得 NCCN 專業版或 ESMO 的原文，不寫成定論。實際排程以院內路徑與主治醫師為準；基線 CA19-9 為零（Lewis-negative）的病人不能靠 CA19-9 追蹤（見 [3.4](#34-ca19-9)）。

### 4.5 術前（neoadjuvant）與圍術期證據逐一看

| 試驗 | 族群與設計 | 治療 | 主要結果 | 判讀 |
|------|-----------|------|---------|------|
| PREOPANC（Versteijne et al., 2020, 2022） | 第 3 期，荷蘭，可切除或邊緣可切除，n = 246 | 術前 gemcitabine × 3，第 2 個週期同步 36 Gy／15 次 → 手術 → gemcitabine × 4；對照為立即手術 → gemcitabine × 6 | OS HR 0.78（0.58–1.05），P = .096（2020）；長期追蹤 HR **0.73**（0.56–0.96），P = .025，中位 15.7 對 14.3 個月，5 年 OS 20.5% 對 6.5%；R0 71% 對 40%；切除率 61% 對 72% | 初次分析為陰性，長期追蹤轉為陽性，但中位數只差 1.4 個月 |
| PREOPANC-2（Janssen et al., 2025） | 第 3 期，荷蘭，可切除或邊緣可切除，n = 375 | 術前 FOLFIRINOX × 8（全劑量，含 bolus）→ 手術，**術後不再輔助**；對照為術前 gemcitabine 化放療 | OS 21.9 對 21.3 個月，HR 0.88（0.69–1.13），P = .32；腹瀉 3–4 級 23% 對 1%；治療相關死亡 2 對 1 人 | **陰性**：FOLFIRINOX 沒有贏過化放療 |
| NORPACT-1（Labori et al., 2024） | 第 2 期，北歐，可切除胰頭癌，n = 140 | 術前 FOLFIRINOX × 4 → 手術 → 輔助化療；對照為立即手術 → 輔助化療 | 18 個月 OS 60% 對 73%（P = .032）；中位 OS 25.1 對 38.5 個月，**HR 1.52**（1.00–2.33），P = .050；術前組只有 79%（61／77）真的完成術前治療；3 級以上不良反應 58% 對 40% | **陰性，有傾向更差**；第 2 期、樣本小 |
| Prep-02/JSAP-05（Unno et al., 2026） | 第 2／3 期，日本，可切除且無動脈接觸，n = 364 | 術前 gemcitabine 1,000 mg/m² D1, 8 ＋ S-1 40–60 mg 每日兩次 D1–14，q3w × 2 → 手術；兩組都建議術後 S-1 6 個月 | OS **37.0 對 26.6 個月**，HR 0.73（0.56–0.95），P = .018；RFS 14.3 對 11.3 個月；R0 91.1% 對 85.9%；pN1 59.2% 對 81.4% | **陽性**；日本族群與日本式輔助 S-1，外推要小心 |
| Alliance A021501（Katz et al., 2022） | 隨機第 2 期，邊緣可切除，n = 126 | 臂 1：mFOLFIRINOX × 8 → 手術 → mFOLFOX6 × 4；臂 2：mFOLFIRINOX × 7 ＋ SBRT 33–40 Gy／5 次（或 25 Gy／5 次）→ 手術 → mFOLFOX6 | 18 個月 OS 66.7%（56.1–79.4）對 47.3%；中位 OS 29.8 對 17.1 個月；期中 R0 57% 對 33%，臂 2 提前關閉；只有 40%（51／126）接受胰臟切除 | 單用 mFOLFIRINOX 是參考；加放療沒有更好 |
| SWOG S1505（Sohal et al., 2021） | 隨機第 2 期，可切除，符合資格 n = 102 | 術前 12 週加術後 12 週：mFOLFIRINOX 對 gemcitabine ＋ nab-paclitaxel | 2 年 OS 47% 對 48%，**都沒達到預設的 40% 門檻**；中位 OS 23.2 對 23.6 個月；切除率 73% 對 70%；147 位中 29% 在中央影像審查被判不符合資格 | 兩個方案無法分高下；「可切除」的影像判讀本身就不穩 |
| MASTERPLAN（Oar et al., 2026） | 第 2 期，澳紐，高風險局部疾病（腫瘤 >4 cm、胰外侵犯、N+、邊緣可切除或局部晚期），提前結束（74／120 位） | 圍術期化療（mFOLFIRINOX 或 GnP）± SBRT 40 Gy／5 次 | 12 個月局部區域復發 20.2% 對 52.0%（sHR 0.44，0.22–0.88，P = .022）；3 級以上不良反應 70% 對 64% | 只證明**局部控制**，主要指標不是存活；第 2 期 |

> [!TIP]
> **術前治療像是先「試水溫」再下水**
> 先給全身治療，看腫瘤的反應與病人的耐受，再決定要不要開這一刀。優點是微小轉移可能早點被壓制、R0 率與淋巴結降期的證據較好（PREOPANC、Prep-02）；代價是有一部分人在術前就因惡化、併發症或體力下降而失去手術機會（PREOPANC 切除率 61% 對 72%；NORPACT-1 82% 對 89%）。「水溫」可以測，但不是每個人都適合下水。

> [!IMPORTANT]
> **術前試驗的考試重點**
> - **陰性**：PREOPANC-2（FOLFIRINOX 對化放療）、NORPACT-1（趨勢更差，HR 1.52）、S1505（兩臂都沒過 40% 門檻）。**陽性**：PREOPANC（長期追蹤）、Prep-02/JSAP-05。
> - PREOPANC-2 的 FOLFIRINOX 組術後**沒有**輔助治療，NORPACT-1 的術前只有 4 個週期；兩個試驗都不能直接說「術前 mFOLFIRINOX 比術後 mFOLFIRINOX 差或好」，這個問題要等 Alliance A021806。
> - 術前 FOLFIRINOX 或 mFOLFIRINOX 限 **PS 0–1**（NCCN, 2026，病人版）。

### 4.6 邊緣可切除（borderline resectable）

**結論：兩大指引都以全身治療開頭（術前或誘導），重評後再決定手術；放療不是必要的一環。**

- **NCCN**：偏好 FOLFIRINOX 或 mFOLFIRINOX（限 PS 0–1）、gemcitabine ＋ nab-paclitaxel（GnP）；帶 BRCA 或 PALB2 變異者偏好 cisplatin ＋ gemcitabine。最長約 6 個月，在高量醫院進行。病人版另列 consolidation 化放療（化療之後再接），放療搭配的化療藥偏好 capecitabine 或 5-FU，其他建議 gemcitabine（NCCN, 2026，病人版）。
- **Pan-Asian ESMO**：邊緣可切除要同時用解剖與生物學標準定義（見 [3.8](#38-nccn-可切除性分類)）；誘導以 FOLFIRINOX 或 GnP 為主，不適合時可用 gemcitabine ＋ S-1，gemcitabine 加 oxaliplatin 或 capecitabine 是由晚期資料外推的選項；與 S-1 同步的化放療列為選項，證據等級低於誘導化療（Tai et al., 2025，建議 4r、4s）。

**放療加在誘導化療上，沒有看到好處。**

| 試驗 | 結果（引自 Tai et al., 2025 的整理，除非另有標示） |
|------|-------------------------------------------|
| Alliance A021501 | mFOLFIRINOX 加 SBRT 的 R0 率與存活都沒有比較好（4.5 表；Katz et al., 2022） |
| PANDAS／PRODIGE 44（隨機第 2 期） | mFOLFIRINOX × 4 後隨機：再 × 2 對 再 × 2 加 capecitabine 化放療。R0（主要指標）54.1%（20 位）對 58.1%（18 位）；切除率 69% 對 55%；中位 OS 32.8 對 30 個月 |
| GABARNANCE（隨機第 2／3 期，日本，n = 112） | GnP 對 S-1 同步放療（S-1 為全身劑量 80 mg/m²）：R0 60.7% 對 57.1%；中位 OS 23.1 對 31.5 個月（HR 0.758，0.472–1.219，P = .2518） |
| 統合分析（23 項研究，2,930 位，邊緣可切除與局部晚期） | 邊緣可切除的切除率：FOLFIRINOX 53%，gemcitabine 為主的化療 55%；R0 率 75% 對 81%；OS 32.9 對 28.6 個月（P = .285） |

**重評與手術。** 誘導期間依 MDT 安排影像與 CA19-9；術前治療後，腫瘤與血管間的實質接觸可能被血管周圍脂肪的模糊密度取代，這不等於不可切除，要由 MDT 與影像科描述（見 [3.8](#38-nccn-可切除性分類)）。術後依 Alliance A021501 接 mFOLFOX6 × 4，術前加術後的化療總量約 6 個月（NCCN, 2026，病人版）。誘導治療能把一部分原本不可切除的病人帶到手術：111 項研究、4,394 位的統合分析中，原本被判為不可切除（邊緣可切除或局部晚期）者的估計切除機率約 30%，R0 率 79.2%，與原本可切除者（82.1%）相近（引自 Tai et al., 2025）。

> [!NOTE]
> **台灣的健保文字沒有對應邊緣可切除術前方案的條文**
> oxaliplatin（9.10 第 3 點）、irinotecan（9.12.1 第 2 點）、albumin-bound paclitaxel（9.5.2）的給付都限**轉移性**第一線；S-1（9.46）寫的是「局部晚期無法手術切除或轉移性」，邊緣可切除是否等同於「無法手術切除」，原文沒有定義。gemcitabine（9.4）只限「依藥品許可證登載之適應症」。術前或誘導使用 FOLFIRINOX、GnP 前，請與主治醫師、藥師確認自費與申報方式（原文均為 115/10/22 版）。

### 4.7 局部晚期（locally advanced）

**結論：先做約 6 個月的全身誘導治療，每 2–3 個月由 MDT 重評能不能手術；常規加放療沒有證據。**

- **誘導方案**：FOLFIRINOX 或 mFOLFIRINOX、GnP（PS 0–1）。PS 3 的局部晚期，NCCN 病人版偏好單藥 gemcitabine、capecitabine 或 5-FU（NCCN, 2026，病人版）。
- **轉換手術（conversion）**：Pan-Asian ESMO 同意可用標準全身治療做轉換策略，但**轉換後手術是否真有存活好處無法由隨機試驗回答**（不太可能有「誘導後手術對不手術」的試驗），所以證據等級被下調；CA19-9 明顯下降、臨床改善或腫瘤降期的高風險病人才考慮手術，診斷性腹腔鏡在部分亞洲機構是常規，但未納入任何指引（Tai et al., 2025，建議 4w、4x）。
- **LAPACT**（GnP 6 個週期，第 2 期，n = 107）：中位 time to treatment failure 9.0 個月，PFS 10.9 個月，OS 18.8 個月；17 位（16%）接受手術（7 位 R0、9 位 R1）（Philip et al., 2020）。

| 試驗 | 設計 | 結果 | 判讀 |
|------|------|------|------|
| LAP07（Hammel et al., 2016） | 第 3 期，局部晚期；gemcitabine 或加 erlotinib 4 個月，未惡化者（n = 269）再隨機：續化療對 54 Gy 同步 capecitabine 化放療 | 化療 16.5 對化放療 15.2 個月，**HR 1.03**（0.79–1.34），P = .83（期中因無效而停止）；局部惡化 32% 對 46%（P = .03）；erlotinib 組 HR 1.19（0.97–1.45） | 化放療降低局部惡化，卻沒有延長存活；erlotinib 無益 |
| CONKO-007（Fietkau et al., 2025） | 第 3 期，德國；誘導 3 個月（FOLFIRINOX 402 位、gemcitabine 93 位），未惡化的 336 位再隨機：續化療對 50.4 Gy 同步 gemcitabine | 主要指標（因收案慢，由 OS 改為 R0 率）25% 對 18%，**P = .113 未達成**；手術者中 R0 69.4% 對 50.0%（P = .04）；OS HR 0.937（0.747–1.174），P = .57 | 陰性；手術本身與較長存活相關（HR 0.525），但那是非隨機比較 |

> [!CAUTION]
> **待核對：CONKO-007 勘誤與 SBRT 的角色**
> CONKO-007 有勘誤（J Clin Oncol 2026;44:430），本手冊未能讀到更正內容，引用數字前請先查勘誤。SBRT 在局部晚期：本手冊只核對到兩個第 2 期試驗（A021501 的 R0 與存活不佳、MASTERPLAN 的局部區域復發下降但主要指標不是存活），NCCN 專業版對 SBRT 的條文未能開啟，不寫成建議。

> [!IMPORTANT]
> **LAP07 與 CONKO-007 的共同訊息**
> 局部晚期病人死於遠端轉移的比例高，放療能壓低局部惡化（LAP07：32% 對 46%）、提高手術標本的 R0 率（CONKO-007：69.4% 對 50.0%），卻都沒有換到更長的存活。所以放療的位置是「選擇性病人、MDT 決定」，不是常規。

> [!TIP]
> **全身治療是主力部隊，放療是特種部隊**
> 胰臟癌最常見的失敗是「到處開花」（遠端轉移），不是原位復發。把資源先投在全身治療，等主力把戰線壓住、確認沒有新的遠端病灶，再讓特種部隊（SBRT 或化放療）去處理原位那一塊，才有意義。

> [!NOTE]
> **台灣局部晚期可用的健保條文**
> 局部晚期能對應的只有 S-1（9.46，113/2/1）與 gemcitabine（9.4，115/9/1）。FOLFIRINOX 與 GnP 的條文（9.10、9.12.1、9.5.2）只寫轉移性。同 4.6，用在局部晚期的給付與自費方式請先與主治醫師確認。

### 4.8 轉移性：第一線（依體能分層）

**結論：PS 0–1、膽紅素 <1.5 × ULN 的病人，FOLFIRINOX／mFOLFIRINOX、GnP、NALIRIFOX 三者都是 NCCN 偏好方案，也都在 Pan-Asian ESMO 建議之列；選哪一個靠病人條件，不是靠跨試驗比較。**

| 方案 | 劑量（來源試驗） | 存活與反應（對照） | 主要 3 級以上毒性 | 台灣健保（115/10/22 版） |
|------|---------------|-----------------|----------------|----------------------|
| FOLFIRINOX | oxaliplatin 85、irinotecan 180、leucovorin 400 mg/m²；5-FU **bolus 400 ＋ 持續 2,400 mg/m² 輸注 46 小時**；q2w（PRODIGE 4） | OS **11.1 對 6.8 個月**，HR 0.57（0.45–0.73）；PFS 6.4 對 3.3 個月（HR 0.47）；ORR 31.6% 對 9.4%（對 gemcitabine；Conroy et al., 2011） | 嗜中性球低下 45.7%、發燒性嗜中性球低下 5.4%、疲倦 23.6%、嘔吐 14.5%、腹瀉 12.7%、感覺神經病變 9.0%（Tai et al., 2025 引述 PRODIGE 4） | 9.10 第 3 點（本點 111/11/1）＋ 9.12.1 第 2 點（112/2/1，限指定 irinotecan 品項）；原文未訂事前審查 |
| GnP | nab-paclitaxel 125 mg/m² 後接 gemcitabine 1,000 mg/m²，D1, 8, 15，q28d（MPACT） | OS **8.5 對 6.7 個月**，HR 0.72（0.62–0.83）；PFS 5.5 對 3.7 個月；ORR 23% 對 7%（對 gemcitabine；Von Hoff et al., 2013） | 嗜中性球低下 38%、疲倦 17%、**神經病變 17%**、發燒性嗜中性球低下 3%；3 級以上神經病變改善到 1 級以下的中位時間 29 天 | 9.4（115/9/1）＋ 9.5.2（108/11/1，限併用 gemcitabine）；原文未訂事前審查 |
| NALIRIFOX | liposomal irinotecan 50 mg/m²（**以 irinotecan 游離鹼計**，輸注 90 分鐘）、oxaliplatin 60、leucovorin 400 mg/m²，5-FU 2,400 mg/m² 輸注 46 小時；D1, 15，q28d；無 5-FU bolus（NAPOLI 3） | OS **11.1 對 9.2 個月**，HR 0.83（0.70–0.99），P = .036（仿單 HR 0.84）；PFS 7.4 對 5.6 個月（HR 0.69）；ORR 41.8% 對 36.2%，**無顯著差異**（對 GnP；Wainberg et al., 2023） | 腹瀉 20%（GnP 5%）、噁心 12%、低血鉀 15%（4%）、嗜中性球低下 14%（25%）、貧血 11%（17%） | 9.12.2 第 2 點（114/12/1，成人第一線，與 oxaliplatin、5-FU、leucovorin 併用），**需事前審查** |

5-FU 與 leucovorin 在第 9 節沒有獨立條文，只以併用藥身分出現在 9.10、9.12.1、9.12.2。NAPOLI 3 中 80% 有肝轉移，亞洲病人只占 4.9%（Wainberg et al., 2023；Ipsen, 2025）。

**三者的 OS 不能直接排名。** 試驗族群與對照不同（MPACT 的 GnP 對照是單藥 gemcitabine，NAPOLI 3 是 GnP 當對照），而且：

- 日本第 2／3 期 JCOG1611（GENERATE，20–75 歲、PS 0–1，n = 527）在期中分析 426 位時因無效而停止：mFOLFIRINOX 中位 OS 14.0 個月（對 GnP 的 HR 1.31，0.97–1.77）、S-IROX 13.6 個月（HR 1.35，1.00–1.82），GnP 17.1 個月；mFOLFIRINOX 的 3–4 級厭食 23.3%，GnP 5.0%（Ohba et al., 2025）。
- 「modified」沒有統一定義：JCOG1611 的 mFOLFIRINOX 用 oxaliplatin 85、irinotecan 150、5-FU 2,400 mg/m² 輸注 46 小時；韓國 MPACA-3 的 mFOLFIRINOX 用 oxaliplatin 65、irinotecan 135、5-FU 1,000 mg/m² 持續輸注 24 小時（D1–2）（Ohba et al., 2025；Go et al., 2021）。開立時要寫清楚每個藥的劑量。
- 79 項隨機試驗、22,168 位的貝氏網絡統合分析認為 NALIRIFOX 或 FOLFIRINOX 在可耐受時宜優先，GnP 是可行的替代（引自 Tai et al., 2025）。

| 病人條件 | 影響選擇的原因 |
|---------|--------------|
| 膽紅素偏高或尚未引流 | Onivyde 在膽紅素高於正常上限時**沒有建議劑量**（Ipsen, 2025）；nab-paclitaxel 在膽紅素 >1.5 × ULN 時不建議使用（Abraxis, 2022）；irinotecan 在膽紅素 >2 mg/dL 時沒有建議劑量（Pharmacia & Upjohn, 2026）；PRODIGE 4 與 PRODIGE 24 都要求 ≤1.5 × ULN（PRODIGE 4 允許先引流）（UNICANCER, n.d.-a, n.d.-b）。先引流，再談化療 |
| 既存神經病變 | oxaliplatin 與 nab-paclitaxel 都會造成累積性神經病變（MPACT 3 級以上 17%）；PRODIGE 24 排除既存神經病變者 |
| 腸道疾病 | PRODIGE 4 排除發炎性腸道疾病、慢性腹瀉與腸阻塞（UNICANCER, n.d.-b）；Onivyde 仿單：腸阻塞時不可使用（Ipsen, 2025） |
| UGT1A1／DPYD | NALIRIFOX 的 Onivyde 劑量不因 UGT1A1*28 同型合子而降低（50 mg/m²）；二線 NAPOLI-1 方案則要降（4.9）。檢測與東亞資料見[化療基礎](00-shared/01-chemo-basics.md#12-藥物基因檢測與特殊族群評估)第 12 節 |
| 靜脈通路與 46 小時輸液 | FOLFIRINOX 與 NALIRIFOX 要植入式靜脈 port 與攜帶式幫浦（見[化療基礎](00-shared/01-chemo-basics.md#13-中心靜脈導管照護port-apicc隧道式導管)第 13 節）；GnP 可在門診完成 |
| 年齡與 PS | PRODIGE 4 收 18–75 歲、PS 0–1；MPACT 收 KPS ≥70。PS 2 與老年見下方 |

> [!WARNING]
> **膽道還沒通，不要先開含 irinotecan 或 nab-paclitaxel 的處方**
> 胰頭癌病人常常是黃疸來就醫。膽紅素超過仿單的上限時，Onivyde、irinotecan、nab-paclitaxel 都沒有可建議的劑量；引流後的膽管炎還會讓化療期間的發燒難以分辨（見 [3.5](#35-膽道阻塞什麼時候要引流)）。排化療前先確認膽紅素與引流狀態，並跟主治醫師討論。

**PS 2、PS 3 與老年。**

- NCCN 病人版：PS 2 偏好 GnP、capecitabine、gemcitabine，轉移性另有 CAPEOX、FOLFIRI、FOLFOX；PS 3 轉移性**沒有偏好方案**（NCCN, 2026，病人版）。
- 本手冊沒有取得 PS 2 專屬的隨機試驗數字；MPACT 收 KPS ≥70，PRODIGE 4 收 ECOG 0–1，不可直接套用。Pan-Asian 小組也找不到針對 PS 2、膽紅素 >1.5 × ULN 病人的大型前瞻性研究，所以建議用 gemcitabine 或 S-1，證據等級低（Tai et al., 2025，建議 5a-iii）。
- S-1 的依據是日本與台灣合作的 GEST（n = 834，局部晚期與轉移性）：中位 OS gemcitabine 8.8、S-1 9.7、gemcitabine ＋ S-1 10.1 個月；S-1 對 gemcitabine **不劣**（HR 0.96，97.5% CI 0.78–1.18），合併組**未優於** gemcitabine（HR 0.88，0.71–1.08，P = .15）（Ueno et al., 2013）。台灣健保 S-1 條文見 9.46。
- ≥70 歲、PS 0–2 的第 2 期隨機試驗（GIANT，n = 176）：GnP 中位 OS 4.7 個月，5-FU／leucovorin／nal-IRI 4.4 個月（P = .72），沒有差異（引自 Tai et al., 2025）。

**BRCA1/2、PALB2 變異。** NCCN 病人版偏好 cisplatin ＋ gemcitabine 或 FOLFIRINOX／mFOLFIRINOX（NCCN, 2026，病人版）。cisplatin ＋ gemcitabine 的證據是隨機第 2 期試驗中不加 veliparib 的臂（ORR 74.1%、中位 PFS 10.1 個月、中位 OS 15.5 個月；O'Reilly et al., 2020），劑量見 [5.3](#53-以-gemcitabine-為骨幹的處方)；台灣回溯性資料中，stage III／IV 且帶 homologous recombination 基因 germline 變異者，第一線用 platinum 的中位 OS 26.1 個月，未用者 9.6 個月（P = .001；Cheng et al., 2024，回溯性）。維持治療的資格見 4.9。

### 4.9 維持治療與二線以後

#### 維持治療：germline BRCA1/2 與 olaparib

**結論：gBRCA1/2 變異、第一線含 platinum 方案至少 16 週後沒有惡化的轉移性病人，可用 olaparib 300 mg（兩顆 150 mg 錠）每日兩次維持，PFS 延長，整體存活沒有差別。**

- **POLO**（Golan et al., 2019；Kindler et al., 2022）：篩檢 3,315 位，隨機 154 位（3:2）；PFS（獨立審查）**7.4 對 3.8 個月**，HR 0.53（0.35–0.82），P = .004。最終 OS **19.0 對 19.2 個月**，HR 0.83（0.56–1.22），P = .3487，**未達顯著**；3 年 OS 33.9% 對 17.8%。
- 毒性：3 級以上不良反應 40% 對 23%；貧血 3 級以上 11% 對 3%；疲倦、噁心、腹瀉、食慾下降較多；因不良反應停藥 5% 對 2%，生活品質兩組無差別（Golan et al., 2019）。CrCl 31–50 mL/min 時減為 200 mg 每日兩次（AstraZeneca, 2025）。100 mg 錠只用於減量，不可用來湊 300 mg。
- **NCCN**：維持治療在化療穩定或有反應至少約 4–6 個月後考慮；olaparib 為 gBRCA1/2 的偏好維持；rucaparib 列於特定情況（BRCA1/2 或 PALB2，platinum 之後）。其他維持選項：FOLFIRINOX 之後可考慮 capecitabine、FOLFIRI、5-FU/leucovorin 或 FOLFOX，GnP 之後可考慮調整時程的 GnP 或 gemcitabine（NCCN, 2026，病人版；capecitabine 在台灣無胰臟藥證）。
- **台灣**：olaparib 有藥證（衛部藥輸字第027445、027446號，2018-06-05），適應症與 POLO 相符；健保 9.85 有條文但**原文未見胰臟癌適應症**，須自費。rucaparib 的 TFDA 藥證本手冊未核對，第 9 節原文未收載。

> [!TIP]
> **olaparib 靠的是「合成致死」**
> 細胞修補 DNA 雙股斷裂有兩組工人：BRCA 一組、PARP 一組。BRCA 變異的癌細胞等於第一組工人缺席，只靠 PARP 撐場面；olaparib 把第二組也拉走，癌細胞修不好就崩潰，正常細胞還有 BRCA 可用。POLO 因此要求病人先對 platinum 有反應（至少 16 週未惡化）才接維持。PFS 有效、OS 沒有達到顯著差異，兩個終點要一起看。

> [!NOTE]
> **POLO 有勘誤**
> POLO 最終 OS 論文有勘誤（J Clin Oncol 2024;42:2112），本手冊未讀到更正內容；引用 OS 數字前請先查勘誤。

#### 二線以後

| 前線 | 選項 | 證據 | 台灣 |
|------|------|------|------|
| gemcitabine 為主 | **nal-IRI ＋ 5-FU／leucovorin**：nal-IRI 70 mg/m²（游離鹼；= 鹽類 80 mg/m²）、leucovorin 400、5-FU 2,400 mg/m² 輸注 46 小時，q2w | NAPOLI-1（n = 417，KPS ≥70）：OS **6.1 對 4.2 個月**，HR 0.67（0.49–0.92），P = .012；nal-IRI 單藥 4.9 個月（HR 0.99），**無效**；最終分析 6.2 對 4.2 個月，HR 0.75（0.57–0.99）；3–4 級嗜中性球低下 27%、疲倦 14%、腹瀉 13%、嘔吐 11%（Wang-Gillam et al., 2016, 2019） | 9.12.2 第 1 點（107/8/1；條文最新 114/12/1），**需事前審查** |
| gemcitabine 為主 | 含 oxaliplatin 的 5-FU 方案 | CONKO-003（OFF，n = 160）：OS 5.9 對 3.3 個月，HR 0.66（0.48–0.91），P = .010（Oettle et al., 2014）。PANCREOX（mFOLFOX6，n = 108）：OS **6.1 對 9.9 個月（P = .02，反而較差）**，3–4 級不良反應 63% 對 11%（Gill et al., 2016） | oxaliplatin 健保只限轉移性第一線（9.10） |
| gemcitabine 為主 | mFOLFIRINOX 對 S-1（韓國，PS 良好，n = 80） | OS 9.2 對 4.9 個月，adjusted HR 0.4（0.2–0.7），P = .002；PFS 5.2 對 2.2 個月；3–4 級不良反應 56% 對 17%（Go et al., 2021） | 無對應健保條文 |
| FOLFIRINOX 之後 | gemcitabine，或 gemcitabine 加 paclitaxel／nab-paclitaxel（PS 0–2） | 隨機第 3 期 GEMPAX（n = 211）：gemcitabine ＋ paclitaxel 對 gemcitabine，PFS 3.1 對 2.0 個月（HR 0.64），OS 6.4 對 5.9 個月（HR 0.87，0.63–1.20，**無顯著差異**）；韓國第 2 期 GnP（n = 40）：OS 9.9 個月（皆引自 Tai et al., 2025） | gemcitabine 9.4；nab-paclitaxel 9.5.2 只限轉移性第一線併用 gemcitabine |
| RAS 變異 | daraxonrasib | 見 4.10 | 台灣未上市 |

NCCN 病人版的二線原則：之前的方案若結束已超過 6 個月，可以重複使用，否則換方案；gemcitabine 為主之後可選 5-FU／leucovorin／脂質體 irinotecan 等，fluoropyrimidine 為主之後可選 GnP、cisplatin ＋ gemcitabine 等（NCCN, 2026，病人版）。病人版的表格寫 5-FU／leucovorin／irinotecan，內文說明指的是脂質體 irinotecan，且病人不可已用過 irinotecan；這是對病人版文字的解讀，不是專業版原文。

> [!IMPORTANT]
> **nal-IRI 的劑量陷阱（考試與臨床都會遇到）**
> - 二線 NAPOLI-1：70 mg/m²（游離鹼）＝ 80 mg/m²（鹽類）。**UGT1A1*28 同型合子**起始減為 50 mg/m²，耐受再升到 70。
> - 第一線 NALIRIFOX：50 mg/m²，**不因 *28 而減量**。
> - 兩者都不加 5-FU bolus（Ipsen, 2025）。
> - 台灣 Onivyde 仿單只對照 *28，沒有寫東亞常見的 *6（見[化療基礎](00-shared/01-chemo-basics.md#12-藥物基因檢測與特殊族群評估)第 12 節）。

> [!WARNING]
> **Onivyde 不能和一般 irinotecan 互換**
> 脂質體製劑的劑量單位、輸注時間（90 分鐘）、前置藥物（輸注前 30 分鐘給 corticosteroid ＋ 止吐藥）都與 irinotecan 不同；仿單明寫「不可用 Onivyde 取代含 irinotecan 的其他藥品」（Ipsen, 2025）。開立與調劑時看清楚是哪一個品項。

Onivyde 的台灣持證廠商是台灣公司智擎生技製藥；NAPOLI-1 的作者也包括台北榮民總醫院、成大醫院與中國醫藥大學附設醫院的醫師（Wang-Gillam et al., 2016）。

### 4.10 生物標記導向治療與 KRAS 標靶

**結論：KRAS wild-type 約占 11–17%，卻集中了可標靶的變異（見 [2.3](#23-分子景觀)、[2.4](#24-可標靶的變異與藥物)），所以第一線開始前就要拿到 RNA 與 MSI 結果；KRAS 突變的病人，二線已有 daraxonrasib 這個新標準，但台灣尚未上市。** 下表只談「治療位置與證據」，各變異的頻率與檢測方法見第 2 段。

| 變異 | 藥物與劑量 | 胰臟癌證據 | 台灣藥證與健保 |
|------|-----------|-----------|--------------|
| **MSI-H／dMMR** | pembrolizumab 200 mg q3w，最長 2 年（35 個週期）。NCCN 病人版另列 dostarlimab、ipilimumab ＋ nivolumab（未用過免疫治療者，二線） | 美國仿單的非大腸直腸癌 MSI-H／dMMR 合併分析：**胰臟癌 n = 22，ORR 18%（95% CI 5–40）**，反應持續 8.1 至 24.3+ 個月（Merck Sharp & Dohme LLC, 2026）；全癌別 ORR 30.8–34.3%（Marabelle et al., 2020；Maio et al., 2022） | pembrolizumab 有藥證（不分癌別 MSI-H／dMMR，先前治療後無合適替代）；**健保 9.69 原文未見胰臟癌，也未見不分癌別的 MSI-H／dMMR**（只有大腸直腸癌與子宮內膜癌） |
| **NTRK1–3 fusion** | larotrectinib（成人多為 100 mg 每日兩次）、entrectinib（≥600 mg 每日一次）、repotrectinib | 全癌別 ORR：larotrectinib 79%（72–85）、entrectinib 57%（43.2–70.8）；**胰臟癌極少**：larotrectinib 2 位中 1 位有反應，entrectinib 3 位中 2 位（Hong et al., 2020；Doebele et al., 2020） | 三者皆有藥證。**健保只有 larotrectinib（9.95，113/6/1）**，成人胰臟癌需先前至少一次全身性治療失敗且惡化，**事前審查**，每次 12 週；entrectinib（9.93）、repotrectinib（9.131）原文未見 NTRK |
| **NRG1 fusion** | zenocutuzumab（HER2 × HER3 雙特異性抗體）750 mg IV q2w | eNRGy 胰臟癌 cohort（36 位，全是 KRAS wild-type）：15 位有反應（42%，95% CI 25–59），反應持續 7.4 個月，PFS 9.2 個月（Schram et al., 2025）。美國 FDA 2024-12-04 加速核准；**加框警語：胚胎胎兒毒性**，另需注意輸注反應、ILD 與 LVEF | **台灣未上市** |
| **RET fusion** | selpercatinib | 美國 FDA 2022-09-21 加速核准不分癌別的 RET fusion 實體腫瘤：41 位非肺、非甲狀腺腫瘤 ORR 44%（28–60）；有反應的腫瘤包括胰臟腺癌，但胰臟專屬人數與 ORR 本手冊未取得（Duke et al., 2023） | TFDA 藥證本手冊未核對；第 9 節原文未收載 |

> [!CAUTION]
> **待核對：BRAF、HER2、ALK、ROS1、FGFR2 的胰臟癌數字**
> NCCN 病人版（依專業版 v2.2026）列出的藥物包括 dabrafenib ＋ trametinib（BRAF）、fam-trastuzumab deruxtecan（HER2）、erdafitinib（FGFR）、entrectinib 或 repotrectinib（ROS1）等，但本手冊沒有取得這些變異在胰臟癌的專屬療效數字與劑量，也沒有核對這幾個藥的 TFDA 藥證，所以不給劑量與期待值。健保方面，dabrafenib 與 trametinib（9.91）原文只見黑色素瘤與非小細胞肺癌，trastuzumab deruxtecan（9.115）原文未見胰臟癌，erdafitinib 第 9 節原文未收載。KEYNOTE-158 胰臟亞群的 PFS 與 OS 數字只在二手整理中看到，未列。

#### KRAS 突變：daraxonrasib

**RASolute 302**（O'Reilly et al., 2026，*N Engl J Med*）：第 3 期，開放標記，隨機 1:1，**轉移性 PDAC 在一線治療後惡化**（fluoropyrimidine 或 gemcitabine 為主）、ECOG 0–1，n = 500（daraxonrasib 248、化療 252）；91.8% 有 RAS G12 突變，中位年齡 66 歲，亞洲病人 11%，70% 有肝轉移。對照為研究者選擇的化療：mFOLFIRINOX、GnP、FOLFOX 或 nal-IRI ＋ 5-FU／leucovorin。

| 指標 | daraxonrasib 300 mg 每日一次 | 化療 |
|------|---------------------------|------|
| OS（全部病人） | **13.2 個月** | 6.7 個月（HR **0.40**，0.30–0.53，P < .0001） |
| OS（RAS G12 族群，n = 459） | 13.2 個月 | 6.6 個月（HR 0.40，0.30–0.54） |
| PFS（全部／RAS G12） | 7.2／7.3 個月 | 3.6／3.5 個月（HR 0.49／0.45） |
| ORR（全部／RAS G12） | 30%／32% | 11%／11% |
| 3 級以上不良反應 | 61.8% | 69.6% |
| 因治療相關不良反應停藥 | 1.2% | 11.2% |

主要不良反應（任何級別，括號為 3–4 級；daraxonrasib 對化療）：皮疹 87%（13%）對 9%（0%）、腹瀉 67%（7%）對 44%（8%）、**口腔炎 56%（12%）對 19%（3%）**、噁心 52%（3%）對 42%（2%）、疲倦 47%（5%）對 61%（10%）、周邊神經病變 10% 對 29%、指甲周圍炎 17% 對 0%（美國仿單，2026-08-27 版；Revolution Medicines, 2026）。合併安全資料中，皮膚毒性中位約第 13 天出現、口腔炎約第 22 天、腹瀉約第 3 天；消化道穿孔 0.9%（1 例致死）、ILD／肺炎 2.4%（1 例致死）。

前期研究（Wolpin et al., 2026）：劑量 10–400 mg 每日一次，選 300 mg 進入第 3 期；二線 RAS G12 病人（n = 26）ORR 35%（17–56），PFS 8.5 個月，OS 13.1 個月。

**美國 FDA 於 2026-08-26 核准（RASONQUE）**，適應症比試驗寬：已接受至少一線全身治療，**或不適合多藥全身治療**的病人；RASolute 302 本身只收二線。第一線的結果截至 2026-10-29 尚未在同儕審查期刊發表。**台灣沒有藥證**（TFDA 資料 2026-10-27 版查無此藥），第 9 節原文也未收載。

> [!IMPORTANT]
> **RASolute 302 必背**
> 轉移性 PDAC 二線：daraxonrasib 對化療，OS 13.2 對 6.7 個月（HR 0.40）；PFS 7.2 對 3.6 個月；3 級以上不良反應比化療少，停藥率 1.2% 對 11.2%。劑量 300 mg 每日一次；減量 300 → 200 → 150 mg，150 mg 仍不耐受則永久停藥。

> [!WARNING]
> **daraxonrasib：皮膚、口腔、藥物交互作用**
> - **第 1 天就開始預防皮疹**：臉與胸部外用 corticosteroid、保濕劑、SPF ≥30 防曬，並可考慮口服 doxycycline 或 minocycline；口腔炎用含類固醇漱口水（美國仿單，2026-08-27 版）。
> - 它是 CYP3A 與 P-gp 的受質，**也是 P-gp 抑制劑**：P-gp 受質藥物要間隔至少 4 小時；**避免併用 cyclosporine**（兩者都與 cyclophilin A 結合）。
> - 新出現的咳嗽、呼吸困難或劇烈腹痛要通知醫師評估是否為 ILD 或消化道穿孔（仿單：ILD 2.4%、穿孔 0.9%，各有 1 例致死）。
> - 台灣沒有藥證，不要告訴病人「可以處方」。臨床試驗或專案進口的可行性，本手冊沒有核對。

> [!TIP]
> **為什麼一把「鑰匙」能開多種 KRAS 突變**
> G12C 抑制劑像只認得一種鎖孔的鑰匙，只能處理 1.6% 的 G12C。daraxonrasib 更像一個需要輔助夾具（cyclophilin A）才能工作的工具，專門夾住「開機（ON）狀態」的 RAS 蛋白，不挑哪一種 G12、G13 或 Q61 突變，所以涵蓋約 83–89% 的 PDAC。這也解釋了為什麼 cyclosporine 要避免：它跟 daraxonrasib 搶同一個夾具。（機轉敘述為教學簡化，細節以仿單為準。）

> [!CAUTION]
> **待核對：NCCN v4.2026 是否收錄 daraxonrasib**
> 本手冊所讀的 NCCN 病人版（依專業版 v2.2026）早於 2026-08-26 的核准，沒有列這個藥；專業版 v4.2026 的處理未能開啟核對。

**KRAS G12C（約 1.6%）。** sotorasib 960 mg 每日（CodeBreaK 100，n = 38，中位前線數 2 線）：ORR 21%（10–37），PFS 4.0 個月，OS 6.9 個月，3 級不良反應 16%（Strickler et al., 2023）。adagrasib 600 mg 每日兩次：胰臟癌 7／21 位有反應（Bekaii-Saab et al., 2023）。NCCN 病人版二線列出兩者。兩藥在台灣有藥證，但**都沒有胰臟癌適應症**，健保原文未收載。

**KRAS G12D（43.6%）。** 目前沒有核准藥物，下列皆為 2026 年發表的早期臨床試驗，不屬於常規治療：

| 藥物（試驗） | 設定 | 胰臟癌人數 | ORR | PFS／OS（月） |
|-------------|------|-----------|-----|-------------|
| HRS-4642 ＋ nab-paclitaxel／gemcitabine（第 1b／2 期；Cui et al., 2026） | **第一線**，未治療 | 30 | 63.3%（43.9–80.1） | 摘要未列 |
| HRS-4642 ＋ adebrelimab（Shi et al., 2026） | 已治療 | 37 | 43.2%（27.1–60.5） | 5.7／11.5 |
| GFH375（口服；Ai et al., 2026） | 已治療 | 37 位可評估 | 35.1%（13／37） | 5.5／9.9 |
| setidegrasib（KRAS G12D 降解劑，600 mg IV 每週；Park et al., 2026） | 二線或三線 | 21 | 24%（8–47） | 3.0／10.3 |

這些試驗人數少、多為單臂，不能與 RASolute 302 的隨機結果比較；只作為「G12D 專一藥物正在發展」的背景。

### 4.11 新藥在台灣的狀態：藥證、健保與美國核准

指引寫的藥，台灣不一定買得到；買得到也不一定有健保。下表的 TFDA 藥證依 2026-10-27 的開放資料（Taiwan Food and Drug Administration, 2026），健保依 115/10/22 版第 9 節原文（衛生福利部中央健康保險署，2026）；「原文未見」代表該條文存在，但沒有胰臟癌（或對應變異）的適應症；「原文未收載」代表第 9 節搜尋不到該藥。5-FU 與 leucovorin 在第 9 節沒有獨立條文。

| 藥物 | 胰臟癌用途 | 美國 FDA | 台灣藥證（TFDA） | 健保（115/10/22 版） |
|------|-----------|---------|----------------|--------------------|
| gemcitabine | 各期化療骨幹 | 核准 | 有 | 9.4（115/9/1），限許可證適應症範圍，未限線別與分期 |
| oxaliplatin、irinotecan | FOLFIRINOX | 核准 | 有；適應症寫轉移性第一線 FOLFIRINOX | 9.10 第 3 點（111/11/1）、9.12.1 第 2 點（112/2/1，限指定品項）；只限轉移性第一線 |
| albumin-bound paclitaxel（Abraxane） | GnP 第一線 | 核准 | 有（衛部藥輸字第026484號，2015-03-19） | 9.5.2（108/11/1）；限併用 gemcitabine，轉移性第一線 |
| liposomal irinotecan（Onivyde） | NALIRIFOX 第一線；二線 ＋ 5-FU／leucovorin | 核准（仿單 2025-03-03 版） | **有**（衛部藥輸字第026655號，2015-12-07 核發，2026-02-25 最後變更），兩個適應症都有 | 9.12.2 第 1 點（二線，107/8/1）、第 2 點（第一線，114/12/1），**需事前審查** |
| S-1（TS-1） | 局部晚期或轉移 | — | 有；**無輔助適應症** | 9.46（113/2/1）；局部晚期無法手術切除或轉移性 |
| capecitabine | GemCap（輔助） | 仿單（2026-02-05 版）列有輔助 GemCap | 有許可證，**無胰臟適應症**（含 Xeloda） | 9.17 原文未見胰臟癌 |
| erlotinib | gemcitabine ＋ erlotinib | 核准 | **無胰臟適應症** | 9.29 原文未見胰臟癌 |
| olaparib | gBRCA 維持 | 核准 | **有**（gBRCA、platinum ≥16 週後） | 9.85 原文未見胰臟癌，**無健保給付** |
| pembrolizumab | MSI-H／dMMR | 核准（不分癌別） | **有**（不分癌別 MSI-H／dMMR，先前治療後） | 9.69 原文未見胰臟癌，亦未見不分癌別 MSI-H／dMMR，**無健保給付** |
| larotrectinib | NTRK fusion | 核准（不分癌別） | **有** | **有給付**：9.95（113/6/1），事前審查 |
| entrectinib、repotrectinib | NTRK fusion | 核准 | **有**（entrectinib 2020-05-21 核發） | 9.93、9.131 原文未見 NTRK 或胰臟癌 |
| zenocutuzumab | NRG1 fusion | 2024-12-04 加速核准 | **無** | 原文未收載 |
| selpercatinib | RET fusion | 2022-09-21 加速核准（不分癌別） | 本手冊未核對 | 原文未收載 |
| sotorasib、adagrasib | KRAS G12C | 本手冊未核對胰臟適應症 | 有許可證，**無胰臟適應症** | 原文未收載 |
| daraxonrasib（RASONQUE） | RAS 突變二線 | **2026-08-26 核准** | **無** | 原文未收載 |
| dabrafenib ＋ trametinib、trastuzumab deruxtecan、rucaparib | BRAF、HER2、BRCA | 本手冊未核對胰臟適應症 | 本手冊未核對 | 9.91、9.115 原文未見胰臟癌；rucaparib 原文未收載 |

> [!NOTE]
> **藥證、健保、院內處方集是三件事**
> 有藥證代表可以合法使用；健保給付要另外符合第 9 節條件；醫院是否進藥看院內藥事委員會。病人問「這個新藥可以用嗎」，要分三層回答。Pan-Asian ESMO 的台灣段落（Tai et al., 2025）寫到，新藥獲 FDA 或 EMA 核准後，約需 1–2 年才進台灣，再 1–2 年才可能有健保；本表的藥證與健保都會持續更新，引用請註明日期。

---

## 5. 常用處方（Regimen）

> [!NOTE]
> **劑量與輸注時間依院內處方集**
> 以下是試驗與仿單的標準劑量。輸注時間、稀釋液、前置藥與調劑流程各院不同，開立前以單位的化療 protocol 為準。體表面積與劑量計算見[化療基礎與劑量計算](00-shared/01-chemo-basics.md#2-體表面積bsa計算)第 2–4 節，化療前檢核見同章第 5 節。

**這一段的結論先講：** 胰臟癌的處方不難背，難在**三組長得很像的劑量**：（1）輔助 mFOLFIRINOX 與轉移性 FOLFIRINOX，irinotecan 是 150 對 180 mg/m²，5-FU bolus 是無對 400 mg/m²；（2）liposomal irinotecan 的劑量單位，NALIRIFOX 是 50、二線是 70 mg/m²，兩者都以 irinotecan **游離鹼**計，70 mg/m² 游離鹼等於鹽類 80 mg/m²；（3）Onivyde 與一般 irinotecan 不能互換。開處方之前還有三個先決條件：膽紅素與引流狀態（見 [3.5](#35-膽道阻塞什麼時候要引流)）、DPYD 與 UGT1A1（見[化療基礎](00-shared/01-chemo-basics.md#12-藥物基因檢測與特殊族群評估)第 12 節）、靜脈 port 與 46 小時幫浦（同章第 13 節）。各藥的台灣藥證與健保條號依 115/10/22 版，完整表格見[第 9 段](#9-健保給付與事前審查)與 [4.11](#411-新藥在台灣的狀態藥證健保與美國核准)。

### 5.1 FOLFIRINOX 家族：輔助 mFOLFIRINOX 與轉移性 FOLFIRINOX

| 項目 | 輔助 mFOLFIRINOX | 轉移性 FOLFIRINOX |
|------|-----------------|------------------|
| 依據 | PRODIGE 24／CCTG PA.6（Conroy et al., 2018, 2022） | PRODIGE 4／ACCORD 11（Conroy et al., 2011） |
| 週期 | 每 2 週一次，共 12 次（24 週） | 每 2 週一次；PRODIGE 4 建議有反應者做 6 個月化療 |
| oxaliplatin | 85 mg/m² | 85 mg/m² |
| irinotecan | **150 mg/m²**（起始 180，試驗中途依安全性分析改為 150） | **180 mg/m²** |
| leucovorin | 400 mg/m² | 400 mg/m² |
| 5-FU bolus | **無** | **400 mg/m²** |
| 5-FU 持續輸注 | 2,400 mg/m²，46 小時 | 2,400 mg/m²，46 小時 |
| 試驗入選條件 | 18–79 歲、WHO PS 0–1、膽紅素 ≤1.5 × ULN、術後 CA19-9 ≤180；**排除** Gilbert 症、UGT1A1\*28/\*28、既存神經病變（UNICANCER, n.d.-a） | 18–75 歲、WHO PS 0–1、膽紅素 ≤1.5 × ULN（可先引流）、ANC ≥1,500/mm³、血小板 ≥100,000/mm³、肌酸酐 <120 µmol/L；排除發炎性腸道疾病、慢性腹瀉、腸阻塞（UNICANCER, n.d.-b） |
| 3 級以上毒性 | 任一 75.9%（gemcitabine 對照 52.9%）；嗜中性球低下 28.4%、腹瀉 18.6%、疲倦 11.0%、周邊神經病變 9.3%（de Jesus & Riechelmann, 2021，轉載三個輔助試驗的毒性表） | 嗜中性球低下 45.7%、發燒性嗜中性球低下 5.4%、疲倦 23.6%、嘔吐 14.5%、腹瀉 12.7%、感覺神經病變 9.0%（見 [4.8](#48-轉移性第一線依體能分層)） |
| 台灣 | 適應症外，無健保條文（見 [4.4](#44-術後輔助治療)） | 有藥證；健保 9.10 第 3 點（本點 111/11/1；條號最新修訂 115/2/1）加 9.12.1 第 2 點（112/2/1，限指定 irinotecan 品項）；原文未訂事前審查 |

**給藥順序與輸注時間。** PRODIGE 4 的登記資料列出各藥輸注時間：oxaliplatin 2 小時、irinotecan 90 分鐘、leucovorin 2 小時，之後 5-FU bolus 5 分鐘，再接 46 小時持續輸注（UNICANCER, n.d.-b）。Irinotecan 排在 5-FU／leucovorin 之前：Camptosar 仿單指出，先給 irinotecan 再給 5-FU／leucovorin 的順序用於合併療法試驗，並被建議採用（Pharmacia & Upjohn, 2026）。oxaliplatin、irinotecan、leucovorin 之間如何排列（同時或先後），以院內 protocol 為準；PRODIGE 24 的摘要沒有列輸注時間，本手冊不替它補數字。5-FU 的持續輸注要經中心靜脈管路並用輸液幫浦（Fresenius Kabi USA, 2026）；46 小時幫浦的接上、回診拆除與居家問題見[化療基礎](00-shared/01-chemo-basics.md#13-中心靜脈導管照護port-apicc隧道式導管)第 13–14 節。

三個含 oxaliplatin 與 irinotecan 的處方放在一起看，最容易看出差異：

| 處方 | oxaliplatin | irinotecan | 5-FU bolus | 5-FU 輸注 | 週期 |
|------|-------------|-----------|-----------|----------|------|
| 輔助 mFOLFIRINOX | 85 mg/m² | 150 mg/m² | 無 | 2,400 mg/m²／46 小時 | q2w × 12 |
| 轉移性 FOLFIRINOX | 85 mg/m² | 180 mg/m² | 400 mg/m² | 2,400 mg/m²／46 小時 | q2w |
| NALIRIFOX（5.2） | 60 mg/m² | Onivyde 50 mg/m²（游離鹼） | 無 | 2,400 mg/m²／46 小時 | D1, 15，q28d |

三個處方的 leucovorin 都是 400 mg/m²。

> [!WARNING]
> **oxaliplatin 的稀釋液與管路**
> oxaliplatin 只能用 5% dextrose 250 至 500 mL 稀釋，**不可用氯化鈉或任何含氯溶液**；不可與鹼性藥物或鹼性溶液（例如鹼性的 5-FU 溶液）走同一條管路，給其他藥之前先用 5% dextrose 沖管；不可使用含鋁的針頭或輸液套，鋁會使鉑類降解（Meitheal, 2024）。處方、調劑與給藥都要核對稀釋液與管路沖洗液。

> [!WARNING]
> **「modified」不是一個劑量**
> mFOLFIRINOX 在不同試驗裡指不同劑量：PRODIGE 24 是 oxaliplatin 85、irinotecan 150、5-FU 2,400 mg/m² 持續輸注 46 小時、無 bolus；韓國 MPACA-3 是 oxaliplatin 65、irinotecan 135、5-FU 1,000 mg/m² 持續輸注 24 小時（見 [4.8](#48-轉移性第一線依體能分層)）。醫囑上要逐藥寫劑量，不要只寫「mFOLFIRINOX」。

### 5.2 脂質體 irinotecan：NALIRIFOX 與二線 nal-IRI ＋ 5-FU／leucovorin

| 項目 | NALIRIFOX（第一線） | nal-IRI ＋ 5-FU／leucovorin（二線） |
|------|-------------------|---------------------------------|
| 依據 | NAPOLI 3（Wainberg et al., 2023） | NAPOLI-1（Wang-Gillam et al., 2016, 2019） |
| 週期 | D1, 15，q28d（即每 2 週） | 每 2 週 |
| Onivyde（以 irinotecan 游離鹼計） | **50 mg/m²**，輸注 90 分鐘；**不因 UGT1A1\*28 而減量** | **70 mg/m²**（= 鹽類 80 mg/m²），輸注 90 分鐘；UGT1A1\*28 同型合子起始 50 mg/m²，耐受後升到 70 |
| oxaliplatin | 60 mg/m²，輸注 120 分鐘 | 無 |
| leucovorin | 400 mg/m²，輸注 30 分鐘 | 400 mg/m² |
| 5-FU | 2,400 mg/m²，46 小時，**無 bolus** | 2,400 mg/m²，46 小時，**無 bolus** |
| 給藥順序 | Onivyde → oxaliplatin → leucovorin → 5-FU | Onivyde → leucovorin → 5-FU |
| 前置用藥 | 每次 Onivyde 輸注前 30 分鐘給 corticosteroid ＋ 止吐藥 | 同左 |
| 膽紅素 | 高於正常上限，**沒有建議劑量** | 同左 |
| 台灣 | 9.12.2 第 2 點（114/12/1），成人第一線；**需事前審查** | 9.12.2 第 1 點（107/8/1；全條最新修訂 114/12/1）；**需事前審查** |

（劑量、順序、前置與膽紅素規定：Ipsen, 2025。）

**調製與輸注。** Onivyde 每瓶 43 mg／10 mL（4.3 mg/mL，以游離鹼計）；用 500 mL 的 5% dextrose 或 0.9% 氯化鈉稀釋，輕輕倒置混勻，避光；稀釋後室溫 4 小時內、冷藏 24 小時內使用，使用前回溫，不可冷凍；輸注 90 分鐘；屬危害藥品（Ipsen, 2025）。

**劑量計算實例**（BSA 1.70 m²；以下是教學算例，實際 BSA 依院內公式與系統）：

```
NALIRIFOX 的 Onivyde：50 mg/m² × 1.70 m² = 85 mg
  抽取體積 = 85 mg ÷ 4.3 mg/mL ≈ 19.8 mL（需 2 瓶，剩餘丟棄）

二線 nal-IRI（游離鹼）：70 mg/m² × 1.70 m² = 119 mg
  抽取體積 = 119 mg ÷ 4.3 mg/mL ≈ 27.7 mL（需 3 瓶）

錯把鹽類劑量 80 mg/m² 當成處方單位：80 × 1.70 = 136 mg
  136 ÷ 119 ≈ 1.14，即多給約 14%
```

**劑量階梯**（Ipsen, 2025；CTCAE v5.0 用於 NALIRIFOX 表；二線表仿單寫 v4.0）：

| 方案 | 第 1 次 3–4 級不良反應 | 第 2 次 | 第 3 次 | 第 4 次 |
|------|---------------------|--------|--------|--------|
| NALIRIFOX（起始 50） | 40 mg/m² | 32.5 mg/m² | 25 mg/m² | 停用 |
| 二線（起始 70） | 50 mg/m² | 43 mg/m² | 停用 | — |
| 二線，UGT1A1\*28 同型合子且尚未升到 70 | 43 mg/m² | 35 mg/m² | 停用 | — |

NALIRIFOX 每降一階 Onivyde，5-FU 與 oxaliplatin 同步降到原劑量的 80%、65%、50%，第四次停用；leucovorin 維持原劑量；oxaliplatin 耐受不佳時可單獨停掉，Onivyde ＋ 5-FU／leucovorin 繼續。3–4 級不良反應後要等恢復到 ≤1 級，且 ANC ≥2,000/mm³、血小板 ≥100,000/mm³ 才能再給（Ipsen, 2025）。分級行動與永久停藥條件見 [6.2](#62-irinotecan-與脂質體-irinotecan)。

台灣多中心回溯性資料（nal-IRI ＋ 5-FU／leucovorin，9 家醫院，n = 473，ECOG 0–1）：整體中位存活 6.8 個月，3–4 級嗜中性球低下 23.3%、腹瀉 2.7%；降低起始劑量、之後再加量的病人，結果和標準起始劑量相近（中位存活 9.3 對 8.0–8.2 個月）（Su et al., 2022）。這是回溯性分析，不能取代仿單；它提醒的是**劑量強度**（前 6 週累積劑量 >80% 者中位存活 7.9 個月，<60% 者 4.3 個月）與起始劑量要一起看。

> [!WARNING]
> **Onivyde 與 irinotecan 不能互換，劑量單位不能混用**
> 仿單明寫「不可用 Onivyde 取代含 irinotecan HCl 的其他藥品」（Ipsen, 2025）。醫囑、調劑與給藥三關都要確認：品項是 Onivyde 還是 Campto；mg/m² 是游離鹼還是鹽類；是第一線 50 還是二線 70。轉移性第一線的 FOLFIRINOX 用的是一般 irinotecan 180 mg/m²，NALIRIFOX 用的是 Onivyde 50 mg/m²，兩者不是同一個藥的不同劑量。

### 5.3 以 gemcitabine 為骨幹的處方

| 處方 | 劑量與週期 | 依據與備註 | 台灣 |
|------|-----------|-----------|------|
| gemcitabine ＋ nab-paclitaxel（GnP） | nab-paclitaxel 125 mg/m² 輸注 30–40 分鐘，**接著** gemcitabine 1,000 mg/m²；D1, 8, 15，q28d。劑量階梯 125／1,000 → 100／800 → 75／600 → 停用 | MPACT（Von Hoff et al., 2013）；Abraxane 仿單（Abraxis, 2022）。第一線轉移性；輔助不建議（APACT 主要指標未達成，見 [4.4](#44-術後輔助治療)） | 9.4（115/9/1）＋ 9.5.2（108/11/1，限併用 gemcitabine，轉移性第一線）；原文未訂事前審查 |
| gemcitabine 單藥（轉移性，仿單版） | 1,000 mg/m² 輸注 30 分鐘；第 1–8 週每週一次共 7 次，休 1 週，之後每 28 天的 D1, 8, 15 | gemcitabine 仿單（Meitheal, 2025）。輸注超過 60 分鐘或比每週更頻繁，毒性增加（低血壓、類流感症狀、骨髓抑制） | 9.4（115/9/1），限許可證適應症，未限線別與分期 |
| gemcitabine 單藥（輔助或與他藥合併） | 1,000 mg/m² D1, 8, 15，q28d × 6 | CONKO-001（Oettle et al., 2013）；ESPAC-4 與 PRODIGE 24 的對照臂。**起始就是 D1, 8, 15，不是仿單單藥的「每週 × 7」** | 同上 |
| gemcitabine ＋ capecitabine（GemCap，輔助） | gemcitabine 1,000 mg/m² D1, 8, 15；capecitabine **830 mg/m² 每日兩次，D1–21**；q28d，最多 6 個週期 | ESPAC-4（Neoptolemos et al., 2017）；Xeloda 仿單的胰臟癌劑量（H2-Pharma, 2026） | capecitabine 無胰臟藥證，9.17 原文未見胰臟癌；GemCap 屬適應症外 |
| cisplatin ＋ gemcitabine（germline BRCA1/2 或 PALB2，第一線） | cisplatin 25 mg/m² ＋ gemcitabine 600 mg/m²，試驗摘要寫第 3、10 天，每 3 週一次 | 隨機第 2 期，原始設計是加或不加 veliparib（n = 50，ECOG 0–1，未治療的 III–IV 期）：只用 gemcitabine ＋ cisplatin 的臂，ORR 74.1%、PFS 10.1 個月（6.7–11.5）、OS 15.5 個月（12.2–24.3）；3–4 級嗜中性球低下 48%、血小板低下 55%、貧血 52%（O'Reilly et al., 2020）。NCCN 病人版列為偏好方案（NCCN, 2026） | 第 9 節以「胰」搜尋未命中 cisplatin 條文；是否屬藥證適應症本手冊未核對 |

NCCN 病人版另列的其他方案（CAPEOX、FOLFIRI、FOLFOX、OFF、nab-paclitaxel ＋ cisplatin ＋ gemcitabine、GTX、PAXG 等）本手冊沒有整理劑量；OFF 與 mFOLFOX6 在二線的證據互相矛盾，見 [4.9](#49-維持治療與二線以後)。

> [!WARNING]
> **gemcitabine 的輸注時間與 nab-paclitaxel 的名稱**
> gemcitabine 要在 30 分鐘左右輸完，延長到 60 分鐘以上、或比每週更頻繁給，低血壓、類流感症狀與骨髓抑制都會增加（Meitheal, 2025）。nab-paclitaxel（albumin-bound）**不能與其他 paclitaxel 劑型互相替代**，劑量也不同（Abraxis, 2022）；醫囑上要寫「albumin-bound paclitaxel」，不要只寫「paclitaxel」。

### 5.4 口服與維持用藥：S-1、capecitabine、olaparib，以及不建議的 erlotinib

| 藥物 | 劑量 | 服法 | 調整與注意 | 台灣 |
|------|------|------|-----------|------|
| S-1（TS-1，tegafur／gimeracil／oteracil） | 依 BSA 每日兩次：<1.25 m² 40 mg；1.25 至 <1.5 m² 50 mg；≥1.5 m² 60 mg。D1–28 服藥、休 14 天（6 週週期）。JASPAC 01 輔助共 4 個週期；GEST 的晚期方案每 42 天一個週期（S-1 組每日 80／100／120 mg） | 飯後服用 | 與其他 fluoropyrimidine 或 flucytosine 之間至少隔 7 天；與 brivudine、sorivudine 至少隔 4 週；完全 DPD 缺乏、嚴重腎功能不全、嚴重骨髓抑制、嚴重肝功能不全、懷孕為禁忌（TS-1 台灣仿單；Uesaka et al., 2016；Ueno et al., 2013） | 9.46 第 1 點（113/2/1）：局部晚期無法手術切除或轉移性；**輔助屬適應症外** |
| capecitabine（GemCap） | 830 mg/m² 每日兩次，D1–21，q28d，最多 6 個週期 | 餐後 30 分鐘內以水整顆吞，約每 12 小時一次，不可咬碎或切開；劑量四捨五入到最接近的 150 mg；漏服或吐出都不補（H2-Pharma, 2026） | CrCl 30–50 mL/min 減 25%；<30 劑量未建立。加框警語：DPYD、與 vitamin K 拮抗劑（warfarin）併用的出血（H2-Pharma, 2026） | 無胰臟藥證；9.17 原文未見胰臟癌 |
| olaparib | **300 mg（兩顆 150 mg 錠）每日兩次**，連續服用到惡化或毒性 | 空腹或飯後皆可 | 減量 250 mg 每日兩次，再減 200 mg 每日兩次；CrCl 31–50 mL/min 起始 200 mg 每日兩次；併用強效 CYP3A 抑制劑 100 mg 每日兩次、中效 150 mg 每日兩次（停抑制劑 3–5 個半衰期後恢復原劑量）；100 mg 錠只用於減量（AstraZeneca, 2025；見 [4.9](#49-維持治療與二線以後)） | 有藥證（gBRCA，第一線 platinum ≥16 週後未惡化）；9.85 原文未見胰臟癌，**無健保給付** |
| erlotinib（**本手冊不建議常規使用**） | 與 gemcitabine 併用時 100 mg 每日一次（肺癌 150 mg） | 空腹（餐前 1 小時或餐後 2 小時） | 美國仿單提醒：胰臟癌病人的腦血管事故與微血管病變性溶血性貧血風險增加，另有消化道穿孔與水泡性皮膚疾病 | 無胰臟適應症；9.29 原文未見胰臟癌 |

**為什麼不建議 erlotinib。** PA.3 的 gemcitabine ＋ erlotinib 對 gemcitabine，中位 OS 6.24 對 5.91 個月（HR 0.82，0.69–0.99），1 年 OS 23% 對 17%（Moore et al., 2007）：統計上有差異，臨床上只多 0.33 個月，且皮疹與腹瀉明顯增加（美國 erlotinib 仿單所載 PA.3 的 100 mg 組資料：皮疹任何等級 70% 對 30%，腹瀉 48% 對 36%）。局部晚期的 LAP07，加 erlotinib 的 OS 反而是 HR 1.19（0.97–1.45）（Hammel et al., 2016）。台灣沒有胰臟適應症、健保也不給付。要注意的是 NCCN 病人版仍把 gemcitabine ＋ erlotinib 列為「其他建議方案」（NCCN, 2026），所以「本手冊不建議」是依上述證據的教學立場，考試遇到指引題要分清楚。

> [!IMPORTANT]
> **口服藥物的三個台灣差異**
> - **S-1 在台灣的胰臟適應症是局部晚期或轉移，沒有輔助適應症**；日本 JASPAC 01 的輔助用法（OS HR 0.57）在台灣屬適應症外。
> - **capecitabine 在台灣沒有胰臟適應症**，GemCap 輔助用法屬適應症外，也不在 9.17 的給付範圍。
> - **olaparib 有藥證但原文無健保給付**：藥證、健保、院內處方集是三件事（見 [4.11](#411-新藥在台灣的狀態藥證健保與美國核准)）。

### 5.5 前置用藥、止吐與給藥當天的門檻

| 處方 | 止吐與前置用藥 | 給藥當天的血球與腸道門檻 | 其他要記的 |
|------|--------------|----------------------|-----------|
| FOLFIRINOX／mFOLFIRINOX | 5-HT3 拮抗劑 ＋ dexamethasone（oxaliplatin、irinotecan 單藥各屬中致吐，見[支持性照護](00-shared/03-supportive-care.md#11-致吐風險分級)第 1.1–1.2 節）；irinotecan 的早發性膽鹼性症狀可預防性或治療性給 atropine 0.25–1 mg IV 或 SC | 新週期要 ANC ≥1,500/mm³、血小板 ≥100,000/mm³，**且腹瀉已完全恢復、不靠止瀉藥已 ≥24 小時**；延後 1–2 週，2 週仍未恢復就考慮停用（Pharmacia & Upjohn, 2026；這是仿單為大腸直腸癌合併療法訂的重啟條件，FOLFIRINOX 沒有專屬表，見 6.2） | 給藥前確認 loperamide 已交給病人；詢問是否有鴉片類止痛藥與軟便劑（腹瀉時要停，見 6.2） |
| NALIRIFOX／二線 nal-IRI | Onivyde 前 30 分鐘 corticosteroid ＋ 止吐藥；早發性腹瀉不分嚴重度都給 atropine，遲發性腹瀉不分嚴重度都給 loperamide（Ipsen, 2025） | ANC <1,500/mm³ 或發燒性嗜中性球低下就暫停；**每個週期的 D1 與 D8 都驗 CBC**；3–4 級反應後要 ANC ≥2,000/mm³（Ipsen, 2025） | 腸阻塞不可給；仿單建議停用含乳糖產品、低脂飲食、維持水分（Ipsen, 2025） |
| GnP | 沒有常規的過敏前置（與 paclitaxel 不同）；曾有過敏才考慮前置，重度過敏不可再挑戰（Abraxis, 2022）。nab-paclitaxel 與 gemcitabine 屬低致吐，單一止吐藥即可（共用章 1.1） | D1：ANC <1,500/mm³ 或血小板 <100,000/mm³ 就延後；D8、D15 的規則見 6.5 | 膽道阻塞或有膽道支架者，發燒不論 ANC 先給廣效抗生素（6.5） |
| GemCap、gemcitabine | gemcitabine 低致吐；capecitabine 口服 | gemcitabine 單藥：ANC ≥1,000 且血小板 ≥100,000 全劑量，ANC 500–999 或血小板 50,000–99,999 給 75%，更低就暫停（Meitheal, 2025） | capecitabine 的衛教見[化療基礎](00-shared/01-chemo-basics.md#145-口服抗癌藥)第 14.5 節 |
| olaparib | 噁心常見（POLO 任何等級 45% 對 23%），備止吐藥（Golan et al., 2019） | 開始前，前一線化療的血液毒性要恢復到 ≤1 級；CBC 基線，之後每月（AstraZeneca, 2025） | 見 6.6 |

> [!CAUTION]
> **待核對：多藥方案的整體致吐分級與 G-CSF 一級預防**
> oxaliplatin 與 irinotecan 在共用章 1.1 各列為中致吐；FOLFIRINOX、NALIRIFOX 這種多藥方案的整體致吐分級，以及是否達到 G-CSF 一級預防的 FN 風險門檻（約 ≥20%，見[支持性照護](00-shared/03-supportive-care.md#21-什麼時候用)第 2.1 節），本手冊沒有取得指引原文。可引用的數字只有發燒性嗜中性球低下的發生率：PRODIGE 4 為 5.4%，PRODIGE 24 為 3.0%（Tai et al., 2025；de Jesus & Riechelmann, 2021）。實務依院內化療處方系統與主治醫師；G-CSF 的健保規定見共用章 2.4。

### 5.6 胰酵素替代治療（PERT）

**這一段的結論先講：** 胰臟癌病人約 70% 有胰外分泌功能不全（pancreatic exocrine insufficiency, PEI），晚期合併估計約 72%；歐洲指引的起始劑量是**每個主餐 40,000–50,000 單位 lipase、點心減半**，隨餐服用，沒有反應先確認時機與順從性、加量，再加 PPI（Dominguez-Muñoz et al., 2025）。

| 項目 | 內容 |
|------|------|
| 成人劑量 | 主餐 40,000–50,000 單位 lipase；點心 20,000–25,000 單位；用餐與點心時一起服用（Dominguez-Muñoz et al., 2025；與 ESPEN 胰臟炎指引一致，Arvanitakis et al., 2024）。重度 PEI（胰臟癌、胰十二指腸切除、全胰切除）常需要更高劑量；低於 40,000 單位／餐的證據很少 |
| 計量單位 | 看 **lipase 單位**，不是膠囊顆數 |
| 沒有反應時 | 確認有隨餐服用、時間正確、順從性 → 提高劑量 → 加 PPI（胃酸會影響腸溶包衣的溶解）（Dominguez-Muñoz et al., 2025） |
| 證據 | 改善症狀與營養狀態（證據等級 1）；胰臟癌的 PEI 使用 PERT 可能延長存活（證據等級 2）。英國以人口為基礎的觀察性研究，使用 PERT 者校正後中位存活約為 2.6 倍（Roberts et al., 2019），觀察性資料有選擇偏差，不能直接當成因果 |
| 台灣產品 | Creon 25000 與 Creon 40000（卡利消腸溶微粒膠囊）：藥證適應症為囊狀纖維化、慢性胰臟炎、胰臟手術造成的 PEI；Creon 10000 的藥證只有「幫助消化」。藥證字面沒有明寫胰臟癌，癌症相關 PEI 是依胰臟手術與慢性胰臟炎的適應症延伸使用（TFDA 資料 2026-10-27 版） |
| 健保 | 7.3.6（110/1/1）含 amylase＋lipase＋protease 複方製劑（如 Protase、Creon）：胰液分泌不全，含「其他因腫瘤引發之胰管膽管阻塞」；申報時要附病歷與檢驗報告（胰液分泌不全的疾病，以及營養不良或脂肪痢便的記載）；功能性腸胃炎不得使用 |

**劑量計算實例**（病人一天三正餐加兩次點心，用 Creon 25000，每顆 25,000 單位 lipase）：

```
正餐：40,000–50,000 單位 ÷ 25,000 單位／顆 → 2 顆（= 50,000 單位）
點心：20,000–25,000 單位 ÷ 25,000 單位／顆 → 1 顆（= 25,000 單位）
一天：3 × 2 顆 + 2 × 1 顆 = 8 顆 = 200,000 單位 lipase

改用 Creon 40000：正餐 1 顆（40,000 單位）可以，但點心的 20,000–25,000 單位無法用整顆湊出
  → 這位病人用 25000 規格比較好分配
```

> [!WARNING]
> **酵素要在吃東西的時候吃**
> PERT 要和食物一起到達腸道才有效；指引的劑量也是以「隨餐與點心」為前提（Dominguez-Muñoz et al., 2025）。醫囑要寫「隨餐」，並且每個正餐與點心都有一份，不要排進「三餐飯後」的固定給藥時間。病人禁食或管灌時是否給、怎麼給，與營養科和主治醫師確認，不要自行照常給或整天停掉。

> [!TIP]
> **PERT 像是替胰臟「補人手」**
> 胰臟癌或胰臟切除後，原本負責拆解脂肪的胰液不夠，食物裡的脂肪沒被拆開就進了大腸，變成油亮、惡臭、浮水的脂肪痢與體重下降。PERT 是把人手補回來：人手要和工作（食物）同時到場才有用，工作做完才到就沒用。

### 5.7 肝腎功能與膽紅素門檻速查

胰頭癌病人常因膽道阻塞而有高膽紅素，所以開處方前要先對照下表；膽紅素超過門檻的處方，答案是**先引流**（[3.5](#35-膽道阻塞什麼時候要引流)），不是減量硬打。

| 藥物 | 膽紅素與肝功能 | 腎功能 |
|------|--------------|--------|
| Onivyde（NALIRIFOX、二線） | 膽紅素高於正常上限：**沒有建議劑量**（Ipsen, 2025） | 仿單劑量表未訂 |
| irinotecan（FOLFIRINOX） | 膽紅素升高可考慮起始劑量減 1 級；**>2 mg/dL 沒有建議劑量**。臨床試驗未納入膽紅素 >2.0 mg/dL，或轉胺酶 >3 × ULN（有肝轉移者 >5 × ULN）的病人；每週給藥時，膽紅素 1.0–2.0 mg/dL 者 3–4 級嗜中性球低下的機率較高（Pharmacia & Upjohn, 2026） | 使用要小心，**透析病人不可使用**（Pharmacia & Upjohn, 2026） |
| nab-paclitaxel（GnP） | 胰臟癌膽紅素 >1.5 × ULN **不建議使用**；AST >10 × ULN 不建議；胰臟癌臨床試驗未納入膽紅素高於 ULN 的病人（Abraxis, 2022） | 仿單劑量表未訂 |
| gemcitabine | 沒有數字門檻；用藥前與用藥中監測肝功能，嚴重肝毒性要永久停用（Meitheal, 2025） | HUS 或嚴重腎功能不全要永久停用（Meitheal, 2025） |
| oxaliplatin | 基線與每個週期前驗肝功能（Meitheal, 2024） | CrCl <30 mL/min：**65 mg/m²**（Meitheal, 2024） |
| capecitabine | 3–4 級高膽紅素血症：暫停，恢復到 ≤2 級（<3 × ULN）後依 Table 1 比例恢復（H2-Pharma, 2026） | CrCl 30–50 mL/min：減 25%；<30 劑量未建立（H2-Pharma, 2026） |
| S-1 | 嚴重肝功能不全為禁忌（TS-1 台灣仿單） | 嚴重腎功能不全為禁忌（TS-1 台灣仿單） |
| olaparib | 仿單未訂膽紅素門檻 | CrCl 31–50 mL/min：200 mg 每日兩次（AstraZeneca, 2025） |
| 試驗入選門檻 | PRODIGE 4、PRODIGE 24：膽紅素 ≤1.5 × ULN（PRODIGE 4 允許先引流）（UNICANCER, n.d.-a, n.d.-b） | PRODIGE 4：肌酸酐 <120 µmol/L；PRODIGE 24：<130 µmol/L |

> [!IMPORTANT]
> **三個膽紅素數字（考試重點）**
> - **Onivyde：高於 ULN 就沒有建議劑量**；**nab-paclitaxel：>1.5 × ULN 不建議**；**irinotecan：>2 mg/dL 沒有建議劑量**。FOLFIRINOX 的兩個關鍵試驗都要求 ≤1.5 × ULN。
> - 順序是：引流、等膽紅素下降、再排化療；CA19-9 的基準值也要等膽紅素下降後再抽（[3.4](#34-ca19-9)）。

---

## 6. 副作用評估與處置

通用原則：用 CTCAE v5.0 分級（見[化療基礎](00-shared/01-chemo-basics.md#8-ctcae-分級原則)第 8 節）→ 依級數決定**繼續、暫停、減量或永久停藥**。本段只講胰臟癌處方裡各藥的特有毒性與仿單的行動門檻；通用的處置連到共用章節：噁心嘔吐與 G-CSF 見[支持性照護](00-shared/03-supportive-care.md#1-化療引起的噁心嘔吐cinv)第 1–2 節，腹瀉第 5 節，周邊神經病變與手足症候群第 11 節，貧血與輸血第 10 節；發燒性嗜中性球低下與輸注反應、過敏性休克見[腫瘤急症](00-shared/02-oncologic-emergencies.md#1-發燒性嗜中性球低下)第 1、10 節；外滲見[化療基礎](00-shared/01-chemo-basics.md#9-血管外滲extravasation)第 9 節；DPYD、UGT1A1 檢測見同章第 12 節。

**這一段的結論先講：** 胰臟癌處方有四件事要先想到。（1）**irinotecan**：有兩種不同的腹瀉（早發的膽鹼性、遲發的水瀉），工具不同（atropine 與 loperamide），UGT1A1 與膽紅素決定劑量。（2）**oxaliplatin**：急性神經症狀由冷誘發，累積性神經病變決定能打多久，過敏可在**任何一個週期**發生，美國仿單已列加框警語。（3）**5-FU 與 capecitabine**：2025 年 10 月起美國仿單加框警語要求先檢測 DPYD；46 小時輸注期間的胸痛、意識改變、走路不穩都是停藥訊號。（4）**nab-paclitaxel**：累積性神經病變，以及膽道阻塞或有支架者的敗血症風險。本章的特點是這些毒性常疊在膽道問題、胰酵素不足與惡病質上，判讀要多想一層（6.7）。

### 6.1 各方案的 3 級以上毒性一覽

| 方案（試驗） | 嗜中性球低下 | 腹瀉 | 疲倦 | 周邊神經病變 | 其他重點 |
|------------|-------------|------|------|-------------|---------|
| mFOLFIRINOX 輔助（PRODIGE 24） | 28.4%（發燒性 3.0%） | 18.6% | 11.0% | 9.3% | 噁心 5.5%、嘔吐 5.1%、黏膜炎 2.5%；任一 3–4 級 75.9% |
| FOLFIRINOX 轉移性（PRODIGE 4） | 45.7%（發燒性 5.4%） | 12.7% | 23.6% | 9.0% | 嘔吐 14.5%、血小板低下 9.1%、貧血 7.8%、血栓栓塞 6.6%（171 位轉移性病人；Tai et al., 2025 引述） |
| NALIRIFOX（NAPOLI 3） | 14%（論文）；仿單 26% | 20% | 未取得 | 3% | 低血鉀 15%、噁心 12%、嘔吐 7%、貧血 11% |
| GnP（MPACT） | 38%（發燒性 3%） | 未取得 | 17% | 17% | 3–4 級神經病變改善到 ≤1 級的中位時間 29 天 |
| GemCap（ESPAC-4） | 38.2% | 5.3% | 5.6% | 未取得 | 手足症候群 7.2% |
| nal-IRI ＋ 5-FU／leucovorin（NAPOLI-1） | 27%（論文）；仿單 20% | 13%（遲發 9%、早發 3%） | 14% | 未取得 | 嘔吐 11% |
| olaparib（POLO） | 未取得 | 未取得 | 5% | — | 貧血 11%（對照 3%）；任一 3 級以上 40%（對照 23%） |

資料來源：PRODIGE 24 與 PRODIGE 4 引自 Pan-Asian ESMO 指引的整理（Tai et al., 2025），PRODIGE 24 與 ESPAC-4 另對照轉載三個輔助試驗毒性表的網絡統合分析（de Jesus & Riechelmann, 2021）；其餘為各試驗原文（Von Hoff et al., 2013；Wainberg et al., 2023；Wang-Gillam et al., 2016；Golan et al., 2019）與仿單（Ipsen, 2025）。**跨試驗的百分比不能直接比較**：族群、分級版本、給藥強度都不同。NALIRIFOX 與 nal-IRI 的嗜中性球低下，論文與仿單的數字不同，本手冊無法確認原因（可能是名詞歸併方式不同）；兩個數字都要知道，臨床上以 ANC 檢驗值為準。表中「未取得」表示本手冊讀到的來源沒有列出該項，不代表沒有發生。

### 6.2 Irinotecan 與脂質體 irinotecan

#### 兩種腹瀉

| 項目 | 早發性（膽鹼性） | 遲發性 |
|------|----------------|--------|
| 時間 | 輸注中或輸注後 24 小時內 | 輸注後 24 小時以上；Camptosar 仿單：每 3 週給藥中位第 5 天、每週給藥中位第 11 天 |
| 表現 | 流鼻水、流涎、瞳孔縮小、流淚、流汗、潮紅、腸蠕動亢進造成的腹絞痛，也可能心搏過緩 | 水瀉，可延續造成脫水、電解質失衡、敗血症；可併發大腸炎、潰瘍、出血、腸阻塞與感染，另有巨結腸與腸穿孔的報告 |
| 處置工具 | **atropine** 0.25–1 mg IV 或 SC（可預防性或治療性給，除非臨床上禁忌） | **loperamide**：第一次稀便或排便次數增加就開始，首劑 4 mg，之後每 2 小時 2 mg，直到無腹瀉至少 12 小時；夜間可每 4 小時 4 mg；此高劑量**不超過連續 48 小時** |
| 仿單對象 | Camptosar 與 Onivyde 皆列；Onivyde：任何嚴重度的早發性腹瀉都給 atropine | Onivyde：任何嚴重度的遲發性腹瀉都給 loperamide |
| NAPOLI-1 數字 | 3–4 級 3%；26% 的病人用過 atropine | 3–4 級 9%；34% 的病人用過 loperamide |

（Pharmacia & Upjohn, 2026；Ipsen, 2025。）同一個病人可以兩種腹瀉都發生。Camptosar 仿單另寫：出現腹瀉時**避免利尿劑或軟便劑**（Pharmacia & Upjohn, 2026）；Onivyde 仿單建議停用含乳糖產品、低脂飲食、維持水分（Ipsen, 2025）。胰臟癌病人常因鴉片類止痛藥固定吃軟便劑，開始 irinotecan 之前要教他們「一拉肚子就先停軟便劑」。

> [!TIP]
> **兩種腹瀉，兩套工具**
> 這是教學上的簡化比喻：早發性像是身體的「副交感神經按鈕」被按下，所以又流口水、又流汗、又絞痛，用抗膽鹼的 atropine 把按鈕關掉；遲發性是腸道真的被傷到、水分和電解質一直流失，atropine 沒有用，要用 loperamide 把腸子慢下來，並且補水。看到「24 小時以內加流口水流汗」想 atropine，「24 小時以後的水瀉」想 loperamide 加補液。

> [!WARNING]
> **loperamide 高劑量方案：最多 48 小時，而且有心臟風險**
> Camptosar 仿單的方案（首劑 4 mg，之後每 2 小時 2 mg，夜間每 4 小時 4 mg）如果腹瀉一直不停，24 小時累積量可達約 28 mg（自行推算，假設清醒 16 小時：4 + 2 × 8 + 4 × 2）。loperamide 仿單的急性腹瀉每日上限是 16 mg，並有加框警語：超過建議劑量可發生 QT 延長、torsades de pointes、心跳停止與死亡；仿單另指出要避免與其他延長 QT 的藥物（例如 moxifloxacin、抗精神病藥）併用，並避免用於有 QT 風險因子（心律不整病史、老年、電解質異常）的病人（Advagen Pharma, 2026）。所以：高劑量只限 48 小時，超過就是升級的訊號（住院、換 octreotide，見下表），不是繼續加 loperamide；同時腹瀉造成的低血鉀、低血鎂要補，因為電解質異常正是 QT 風險因子。一般化療腹瀉的 loperamide 做法見[支持性照護](00-shared/03-supportive-care.md#52-處置)第 5.2 節，兩者劑量不同，不要混用。

#### 遲發性腹瀉的分級行動

| 分級（CTCAE v5.0） | 病房處置 | 化療處置 |
|-------------------|---------|---------|
| G1：比基線多 <4 次／天 | 口服補水；停乳製品、低脂飲食；開始 loperamide；24 小時內追蹤 | Onivyde：不必暫停（仿單從 G2 起暫停）。Camptosar：下一次給藥等排便恢復到基線，再以相同劑量給（仿單以舊版 CTC 的 G1 為 2–3 次／天） |
| G2：多 4–6 次／天 | 同上；**24–48 小時未改善**，或合併發燒、嚴重嗜中性球低下、血便、脫水、腸阻塞徵象，就升級：加 fluoroquinolone 類抗生素、octreotide、住院（Benson et al., 2004） | Onivyde：**暫停**，恢復到 ≤1 級後以減量階梯重啟（5.2）。Camptosar：暫停，恢復到基線後減 1 個劑量等級 |
| G3：多 ≥7 次／天、需住院、影響自我照顧 | 住院；IV 補液與電解質；糞便檢查（含 *C. difficile*）；octreotide 100–150 µg SC TID（[支持性照護](00-shared/03-supportive-care.md#52-處置)第 5.2 節）；發燒、腸阻塞或嚴重嗜中性球低下給抗生素；Onivyde 仿單：48 小時未改善依院內指引，可加 diphenoxylate ＋ atropine 或 octreotide | 暫停；恢復後減 1 級（Camptosar：減 1 個劑量等級） |
| G4：危及生命 | 加護或緊急處置 | 暫停；Camptosar：恢復後減 2 個劑量等級；是否再繼續由主治醫師決定 |

Camptosar 的劑量等級（大腸直腸癌合併療法）是 180 → 150 → 120 mg/m²；Onivyde 的減量階梯見 5.2。腸阻塞時**不可給**任何一種 irinotecan，要等阻塞解除（Pharmacia & Upjohn, 2026；Ipsen, 2025）。

> [!CAUTION]
> **待核對：FOLFIRINOX 沒有專屬的 irinotecan 劑量調整表**
> 上表「Camptosar」欄取自仿單針對**大腸直腸癌**合併療法的表格，該表以舊版 NCI CTC（v1.0）分級，腹瀉的次數門檻與本手冊用的 v5.0 不完全相同（v1.0 的 G1 為 2–3 次、G3 為 7–9 次、G4 為 ≥10 次）；G2 以上「暫停、恢復後減量」的方向一致。美國仿單沒有胰臟癌 FOLFIRINOX 的劑量調整表，PRODIGE 4 與 PRODIGE 24 的方案內減量細節本手冊未取得。FOLFIRINOX 實際的減量步驟，以院內 protocol 與主治醫師為準。

#### 嗜中性球低下

- **FOLFIRINOX 的 irinotecan**：新週期要 ANC ≥1,500/mm³、血小板 ≥100,000/mm³ 且腹瀉恢復（見 5.5）。Camptosar 的合併療法表：週期中 G3（ANC 500–999）暫停到 ≤G2 後減 1 級，G4（<500）暫停到 ≤G2 後減 2 級，**發燒性嗜中性球低下暫停到恢復後減 2 級**（Pharmacia & Upjohn, 2026）。
- **Onivyde**：ANC <1,500/mm³ 或發燒性嗜中性球低下就暫停；每個週期的 D1 與 D8 驗 CBC；仿單提醒致命的嗜中性球敗血症與發燒性嗜中性球低下都有發生（NAPOLI 3 致命發燒性嗜中性球低下 0.3%；NAPOLI-1 嗜中性球敗血症 3%、致命 0.8%）。**亞洲病人的資料**：NAPOLI-1 的 3–4 級嗜中性球低下，亞洲病人 55%（18／33），白人 18%（13／73）；NAPOLI 3 則是亞洲 30%（6／20）、白人 26%（76／289）（Ipsen, 2025）。亞洲人數很少，只能當作「要更密切追蹤血球」的提醒。
- 發燒性嗜中性球低下的處置見[腫瘤急症](00-shared/02-oncologic-emergencies.md#1-發燒性嗜中性球低下)第 1 節。

#### UGT1A1 與其他 irinotecan 安全事項

| 項目 | 內容 |
|------|------|
| 機轉 | irinotecan 的活性代謝物 SN-38 由 UGT1A1 葡萄糖醛酸化而失活；\*28 與 \*6 等低功能對偶基因使 SN-38 的暴露量升高，嚴重嗜中性球低下與腹瀉的風險上升（Pharmacia & Upjohn, 2026） |
| Camptosar 仿單建議 | 考慮檢測 \*28 與 \*6。已知 \*28/\*28、\*6/\*6 或 \*6/\*28 者，**起始劑量考慮至少降 1 級**，但**精確的減量幅度未知**；異型合子（\*1/\*28、\*1/\*6）是中間代謝型，風險也可能上升。腹瀉的風險在同型合子，以及 irinotecan 劑量 >125 mg/m² 者更大（Pharmacia & Upjohn, 2026）；FOLFIRINOX 的 irinotecan 是 150–180 mg/m² |
| 族群頻率（仿單） | 同型合子 \*28：黑人約 20%、白人約 10%、東亞約 2%；同型合子 \*6：東亞約 2–6%，白人與黑人少見（Pharmacia & Upjohn, 2026） |
| 台灣／亞洲 | 對偶基因頻率 \*28 為 13.9%（白人 33.4%）、**\*6 為 13.0%（白人 0.5%）**，台灣 PEP02 第 1 期試驗引用的亞洲資料；該試驗唯一一例治療相關死亡是 \*6/\*28 複合異型合子（Chang et al., 2015）。在 Hardy-Weinberg 平衡的假設下，\*6 對偶基因頻率 13.0% 約等於 24% 的人帶有至少一個 \*6（1 − 0.87²；其中異型合子約 23%、同型合子約 1.7%，自行推算，非文獻數字） |
| 台灣大腸直腸癌病人 | 128 位，約 20% 帶 \*28；帶因者接受 irinotecan 合併 5-FU／leucovorin，3–4 級嗜中性球低下 53.8% 對 4.9%、腹瀉 26.9% 對 5.9%（Liu et al., 2008） |
| 亞洲統合分析 | \*6 或 \*28 帶因者（異型合子加同型合子）對 \*1/\*1：嗜中性球低下 OR 2.89（1.97–4.23）、腹瀉 OR 2.26（1.71–2.99）；同型合子分別為 OR 6.23（3.11–12.47）與 3.21（2.13–4.85）（Atasilp et al., 2022） |
| Onivyde | NALIRIFOX：50 mg/m²，不分基因型。二線：\*28 同型合子起始 50 mg/m²，耐受再升到 70。台灣 Onivyde 仿單只對照 \*28，沒有寫東亞常見的 \*6（見 [4.9](#49-維持治療與二線以後)） |
| 試驗排除 | PRODIGE 24 排除 UGT1A1\*28/\*28 與 Gilbert 症（UNICANCER, n.d.-a），所以輔助 mFOLFIRINOX 的數字不含這群人 |
| 基因型導向加量（研究） | PURE FIST（大腸癌，FOLFIRI ＋ bevacizumab）：\*1/\*1 與 \*1/\*28 起始 180 mg/m² 並可加量，\*28/\*28 起始 120 mg/m²（Tsai et al., 2020）。這是研究設計，不是仿單劑量 |
| 台灣的檢測供給與給付 | 本手冊無法確認，見[化療基礎](00-shared/01-chemo-basics.md#122-ugt1a1-與-irinotecansacituzumab-govitecan)第 12.2 節的待核對說明 |

- **過敏**：Camptosar 發生 anaphylaxis 就停用（Pharmacia & Upjohn, 2026）；Onivyde 嚴重過敏要永久停用，對 Onivyde 或 irinotecan 有嚴重過敏或 anaphylaxis 病史者禁忌（Ipsen, 2025）。
- **ILD**：Onivyde 對新發或進展的呼吸困難、咳嗽、發燒暫停待評估，確診就停用；危險因子是原有肺疾病、使用有肺毒性的藥、使用 G-CSF、曾接受放療（Ipsen, 2025）。
- **腎功能**：嘔吐與腹瀉造成脫水後，可發生腎功能惡化或急性腎衰竭（Pharmacia & Upjohn, 2026），所以腹瀉時的補液是治療的一部分。
- **NALIRIFOX 不必因這些事減量**：虛弱、掉髮與 3 級厭食不需調整劑量；3 級以上噁心嘔吐只在已給最佳止吐治療仍發生時才減量（Ipsen, 2025）。
- **避孕**：Onivyde 仿單要求有生育可能的女性在治療期間與最後一劑後 7 個月內避孕（Ipsen, 2025）；生育力與避孕諮詢見[化療基礎](00-shared/01-chemo-basics.md#125-生育力保存與避孕諮詢)第 12.5 節。

### 6.3 Oxaliplatin

| 毒性 | 重點 | 處置 |
|------|------|------|
| 急性神經症狀（冷誘發） | 結直腸癌合併 5-FU／leucovorin 的仿單資料：約 56% 的病人出現，單一週期約 30%；輸注後數小時至 2 天內出現，14 天內緩解，下一次給藥常再出現。手、腳、口周與喉嚨的麻、刺、感覺異常；也有下顎痙攣、舌頭感覺異常、構音困難、眼痛、胸悶。**咽喉感覺異常**是主觀的吞嚥困難或呼吸困難，沒有喘鳴或支氣管痙攣；在未治療過的晚期大腸癌病人 1%–2% 為 3–4 級（Meitheal, 2024） | 整個治療期間避冷：不喝冰飲、不碰冰冷物、冷天遮蓋皮膚，**不要用冰塊含漱預防口腔黏膜炎**；咽喉感覺異常先確認沒有喘鳴、血氧正常，再安撫（衛教見[支持性照護](00-shared/03-supportive-care.md#114-oxaliplatin-的急性與累積神經病變)第 11.4 節）。仿單：輸注時間由 2 小時延長到 6 小時，可能減輕急性毒性，例如非危及生命的輸注反應 |
| 累積性（延遲）感覺神經病變 | 持續超過 14 天的麻、刺、感覺減退，可影響本體感覺（寫字、扣釦子、走路）；結直腸癌試驗 48%；可在沒有急性症狀時出現；出現 3 級者 80% 是由 1–2 級進展而來，3 級的中位出現時間是輔助治療 9 個週期、已治療的晚期病人 6 個週期（Meitheal, 2024）。胰臟癌：PRODIGE 24 的 3–4 級 9.3%（另有感覺異常 12.7%）、PRODIGE 4 為 9.0%、NALIRIFOX（oxaliplatin 60 mg/m²）為 3%（Tai et al., 2025；Wainberg et al., 2023） | 每個週期先問症狀與功能，再下醫囑；分級行動見下表 |
| 過敏反應（加框警語） | 嚴重甚至致命的過敏，包括 anaphylaxis，可在給藥後**數分鐘內、任何一個週期**發生；結直腸癌病人 3–4 級 2%–3%；對 oxaliplatin 或其他鉑類有過敏史者禁忌（Meitheal, 2024） | 立即且**永久停藥**並依過敏處置；床邊流程見[腫瘤急症](00-shared/02-oncologic-emergencies.md#10-輸注反應過敏反應與過敏性休克)第 10 節 |
| 骨髓抑制 | 結直腸癌 3–4 級嗜中性球低下 41%–44%、血小板低下 2%–5%；有敗血症與致命個案（Meitheal, 2024） | 每個週期前驗 CBC；ANC 要 ≥1.5 × 10⁹/L 且血小板 ≥75 × 10⁹/L 才給；敗血症或敗血性休克暫停；G4 嗜中性球低下、發燒性嗜中性球低下或 G3–4 血小板低下恢復後減量（結直腸癌仿單的數字：輔助 75 mg/m²、晚期 65 mg/m²） |
| 腎功能不全 | CrCl <30 mL/min（Cockcroft-Gault） | oxaliplatin 減為 65 mg/m²（Meitheal, 2024） |
| 其他仿單警語 | PRES（頭痛、意識改變、癲癇、視力異常）；肺毒性（咳嗽、呼吸困難，肺纖維化 <1%）；肝毒性；QT 延長；橫紋肌溶解；出血 | PRES、確診的 ILD 或肺纖維化、橫紋肌溶解：**永久停藥**。不明原因的呼吸道症狀：暫停到排除 ILD。每個週期前驗肝功能。心衰竭、心搏過緩、電解質異常或併用延長 QT 藥物者做心電圖並矯正電解質。**併用口服抗凝血藥時要更頻繁監測**（出血與 INR 延長的報告）（Meitheal, 2024） |

**神經病變的分級行動**（CTCAE v5.0 感覺神經病變分級見[化療基礎](00-shared/01-chemo-basics.md#83-常用項目v50)第 8.3 節；劑量建議取自仿單的結直腸癌表格，Meitheal, 2024）：

| 分級 | 表現 | 行動 |
|------|------|------|
| G1 | 無症狀 | 繼續；每週期追蹤；衛教避冷與防跌（[支持性照護](00-shared/03-supportive-care.md#115-安全衛教跌倒與燙傷)第 11.5 節） |
| G2 | 中度症狀，影響工具性 ADL | **持續性** G2：考慮減量（結直腸癌仿單：輔助 75 mg/m²、晚期 65 mg/m²）；與主治醫師討論，不要等到 G3 |
| G3 | 嚴重症狀，影響自我照顧 ADL | **持續性** G3：考慮停用 oxaliplatin |
| G4 | 危及生命 | 停用 |

痛的神經病變可用 duloxetine（唯一有證據的藥，針對疼痛不是麻木；健保 1.1.8 不含化療引起的神經病變），細節見[支持性照護](00-shared/03-supportive-care.md#113-治療duloxetine)第 11.3 節。

> [!CAUTION]
> **待核對：胰臟癌 FOLFIRINOX 的 oxaliplatin 減量級距**
> 上表的 75／65 mg/m² 來自美國仿單的結直腸癌 FOLFOX 方案；仿單沒有胰臟癌的 oxaliplatin 劑量調整表。PRODIGE 4 與 PRODIGE 24 的方案內減量細節本手冊未取得，NALIRIFOX 的 oxaliplatin 隨 Onivyde 階梯降到 80%、65%、50%（5.2）。FOLFIRINOX 的實際減量步驟以院內 protocol 與主治醫師為準。

> [!WARNING]
> **oxaliplatin 的過敏不會「先練習幾次」**
> 紫杉醇類的反應多在前 1–2 次暴露，carboplatin 多在用了很多個週期之後，oxaliplatin 則是任何一個週期都可能發生（[腫瘤急症](00-shared/02-oncologic-emergencies.md#10-輸注反應過敏反應與過敏性休克)第 10 節）。仿單的處置是立即且永久停藥；若鉑類仍是最佳選擇，是否減敏、怎麼做，是過敏免疫科與腫瘤科的專科決定，病房不要自行再給。給藥單位要備有過敏與 anaphylaxis 的處置流程，並依院內監測規範觀察病人。

> [!IMPORTANT]
> **oxaliplatin 兩種神經毒性的差別（考試重點）**
> - **急性**：給藥後數小時至 2 天，**冷誘發**，14 天內緩解，下次可能再出現；處置是避冷，不必因此減量。
> - **累積性**：超過 14 天、劑量相關，可影響本體感覺；持續性 G2 考慮減量、G3 考慮停用、G4 停用。
> - 不要用冰塊含漱預防口腔黏膜炎；輸注可由 2 小時延長到 6 小時。

### 6.4 5-FU、capecitabine 與 S-1

#### DPYD 加框警語

- **2025 年 10 月起，美國 5-FU 與 capecitabine 仿單都加了框警語**：開始治療前檢測 DPYD 基因變異，**除非必須立刻治療**；已知帶有會造成完全 DPD 缺乏的特定同型合子或複合異型合子變異者，避免使用；沒有任何劑量被證實對完全 DPD 缺乏者安全；部分缺乏者個別化劑量。仿單同時指出沒有 FDA 核准的 DPYD 檢驗、各檢驗涵蓋的變異不同，而且**沒找到變異仍可能發生嚴重毒性**（Fresenius Kabi USA, 2026；H2-Pharma, 2026）。
- **典型表現**：急性早發的嚴重黏膜炎、腹瀉、嗜中性球低下與神經毒性（Fresenius Kabi USA, 2026），多出現在第一個週期或加量後。細節、CPIC 分數與東亞的限制見[化療基礎](00-shared/01-chemo-basics.md#121-dpyd-與-fluoropyrimidine)第 12.1 節：西方常用的四個變異在東亞人很少見（Yokoi et al., 2020），台灣沒有可靠的 DPYD 族群頻率研究，**陰性的標準檢驗不等於安全**。
- **台灣**：檢測供給與給付本手冊無法確認（見化療基礎 12.1 的待核對說明）；5-FU 的解毒劑 uridine triacetate，TFDA 2026-10-27 的資料查無藥證，專案進口是否可行本手冊未核對。
- **病房端**：第一個週期內主動打電話追蹤口腔潰瘍、腹瀉、發燒與意識變化（時間點依院內流程）；出現早發嚴重毒性就停藥並通知醫師，不要等到下一個週期。

> [!TIP]
> **DPD 是 5-FU 的「清潔工」**
> DPD 酵素分解掉 80% 以上的 fluorouracil（H2-Pharma, 2026）。清潔工罷工，藥就堆在體內，第一個週期就出現嚴重黏膜炎、腹瀉與骨髓抑制。完全缺乏的人沒有安全劑量，部分缺乏的人要個別化劑量，而檢驗沒找到變異，也不代表清潔工一定在上班。

#### 毒性與分級行動

| 毒性 | 重點 | 行動（5-FU 仿單；capecitabine 見下表） |
|------|------|--------------------------------------|
| 腹瀉 | FOLFIRINOX 與 NALIRIFOX 的腹瀉以 irinotecan 為主（6.2） | G3–4：暫停到 ≤G1，再減量（Fresenius Kabi USA, 2026） |
| 黏膜炎、口腔潰瘍 | 5-FU bolus 比持續輸注更常見；46 小時輸注的處方已不含 bolus（NALIRIFOX、輔助 mFOLFIRINOX） | G3–4：暫停到 ≤G1，再減量。合併 irinotecan 時**只減 5-FU，不減 irinotecan**（Pharmacia & Upjohn, 2026）。含 oxaliplatin 的處方不可用冰塊含漱（6.3）。口腔照護見[支持性照護](00-shared/03-supportive-care.md#4-口腔黏膜炎)第 4 節 |
| 手足症候群 | 持續輸注比 bolus 常見，通常在用藥 8–9 週後出現，也可能更早 | G2–3：暫停到恢復或降到 ≤G1，再減量（Fresenius Kabi USA, 2026）。預防與處置見[支持性照護](00-shared/03-supportive-care.md#116-手足症候群hfs與手足皮膚反應hfsr)第 11.6 節 |
| 骨髓抑制 | 嗜中性球最低點通常在給藥後第 9–14 天；每週期前驗 CBC | G4：暫停到恢復，再減量 |
| 心臟毒性 | 心絞痛、心肌梗塞或缺血、心律不整、心衰竭；風險因子是持續輸注（相對於 bolus）與冠狀動脈疾病 | **暫停**；仿單沒有訂恢復後的建議劑量，再給的風險未建立 |
| 高氨性腦病變 | 在沒有肝病的情況下，輸注開始後 72 小時內出現意識改變、混亂、定向力障礙、昏迷或步態不穩，合併血氨升高 | **暫停**並開始降血氨治療；沒有訂恢復後的建議劑量 |
| 急性小腦症候群與其他神經毒性 | 混亂、定向力障礙、步態不穩、視力異常 | **暫停**；沒有訂恢復後的建議劑量 |
| 與 warfarin 併用 | 凝血時間延長；capecitabine 為加框警語（出血，包含死亡） | 密切監測 INR 並調整 warfarin（H2-Pharma, 2026） |

**capecitabine 的手足症候群與其他 G2 以上毒性**（仿單 Table 1，H2-Pharma, 2026）：

| 嚴重度 | 第 1 次 | 第 2 次 | 第 3 次 | 第 4 次 |
|--------|--------|--------|--------|--------|
| G2 | 暫停到 G0–1，以 100% 劑量恢復 | 75% | 50% | 永久停藥 |
| G3 | 暫停到 G0–1，以 75% 劑量恢復 | 50% | 永久停藥 | — |
| G4 | 永久停藥，或暫停到 G0–1 後以 50% 恢復 | — | — | — |

預防用 10% urea 乳霜：capecitabine 方案 6 週內任何等級手足症候群 22.4%，優於含抗氧化劑的新軟膏（39.5%）（Hofheinz et al., 2015）。capecitabine 在 CrCl 30–50 mL/min 減 25%；3–4 級高膽紅素血症，恢復到 ≤2 級（<3 × ULN）後依上表比例恢復（H2-Pharma, 2026）。

> [!WARNING]
> **46 小時幫浦期間的胸痛、意識改變、走路不穩：先停輸注、再打電話**
> 5-FU 仿單把心臟毒性（胸痛、心律不整）、高氨性腦病變（72 小時內的意識改變）與急性小腦症候群（混亂、步態不穩、視力異常）列為要暫停的事件（Fresenius Kabi USA, 2026）。病人帶著幫浦回家的 46 小時，正好落在這個時間窗。出院衛教要寫清楚：出現這幾類症狀，依院內流程停止輸注並立即聯絡醫療團隊或就醫，不要等回診日；病房接到這類電話，不要只是安撫。幫浦與管路的居家問題見[化療基礎](00-shared/01-chemo-basics.md#13-中心靜脈導管照護port-apicc隧道式導管)第 13–14 節。

**S-1 的特有毒性。** S-1 的特色是口腔炎、腹瀉、流淚或淚管阻塞與皮膚色素沉著（TS-1 台灣仿單）；JASPAC 01 中，口腔炎與腹瀉在 S-1 組較常見，3–4 級白血球低下、嗜中性球低下與 AST／ALT 上升則在 gemcitabine 組較常見（Uesaka et al., 2016）。GEST 單藥 S-1 臂的 3 級以上不良反應：嗜中性球低下 8.5%、貧血 7.0%、白血球低下 3.7%、厭食（非血液學）6.3%、腹瀉 4.4%、疲倦 3.7%；與 gemcitabine 併用時嗜中性球低下上升到 61.8%（TS-1 台灣仿單）。S-1 與其他 fluoropyrimidine 之間要隔至少 7 天（5.4）。

### 6.5 nab-paclitaxel 與 gemcitabine（GnP）

**週期內的血球規則**（Abraxane 仿單，胰臟腺癌；Abraxis, 2022）：

| 時間點 | ANC（/mm³）與血小板（/mm³） | 兩藥的行動 |
|--------|--------------------------|-----------|
| D1 | ANC <1,500 或 血小板 <100,000 | 延後給藥，等恢復 |
| D8 | ANC 500 至 <1,000 或 血小板 50,000 至 <75,000 | 降 1 個劑量等級 |
| D8 | ANC <500 或 血小板 <50,000 | 暫停 |
| D15（D8 有給藥） | ANC 500 至 <1,000 或 血小板 50,000 至 <75,000 | 比 D8 再降 1 級 |
| D15（D8 有給藥） | ANC <500 或 血小板 <50,000 | 暫停 |
| D15（D8 被暫停） | ANC ≥1,000 或 血小板 ≥75,000 | 比 D1 降 1 級 |
| D15（D8 被暫停） | ANC 500 至 <1,000 或 血小板 50,000 至 <75,000 | 比 D1 降 2 級 |
| D15（D8 被暫停） | ANC <500 或 血小板 <50,000 | 暫停 |

劑量等級：125／1,000 → 100／800 → 75／600 mg/m²（nab-paclitaxel／gemcitabine）→ 再需要減量就停用。仿單原文以 OR 連接各條件，D15（D8 被暫停）第一列的實際判讀請與藥師確認。

**其他不良反應的行動**（Abraxis, 2022）：

| 不良反應 | nab-paclitaxel | gemcitabine |
|----------|----------------|-------------|
| 發燒性嗜中性球低下 G3–4 | 暫停到退燒且 ANC ≥1,500/mm³，以下一級劑量恢復 | 同左 |
| 周邊神經病變 G3–4 | 暫停到改善至 ≤G1，以**下一級劑量**恢復 | **不減量** |
| 皮膚毒性 G2–3 | 降 1 級；持續就停用 | 降 1 級；持續就停用 |
| 黏膜炎或腹瀉 G3 | 暫停到 ≤G1，降 1 級 | 暫停到 ≤G1，降 1 級 |

- **神經病變**：MPACT 的 3–4 級神經病變 17%（對照 1%），改善到 ≤1 級的中位時間 29 天（Von Hoff et al., 2013）；輔助的 APACT 為 15%（對照 0%），62% 的事件發生在第 4 個週期以後（Tempero et al., 2023），所以是**累積性**的，要每個週期問症狀。處置與衛教見[支持性照護](00-shared/03-supportive-care.md#11-化療相關周邊神經病變與手足症候群)第 11 節。
- **敗血症**：與 gemcitabine 併用時 5%，有或沒有嗜中性球低下都可發生；**膽道阻塞或有膽道支架是嚴重甚至致命敗血症的危險因子**。病人發燒（不論 ANC）就開始廣效抗生素；發燒性嗜中性球低下則兩藥都暫停，退燒且 ANC ≥1,500/mm³ 後減量恢復（Abraxis, 2022）。
- **肺炎**：與 gemcitabine 併用時 4%，含致命個案；疑似時兩藥暫停評估，排除感染後確診就**兩藥都永久停用**（Abraxis, 2022）。
- **過敏**：嚴重過敏（含 anaphylaxis）不可再挑戰；與其他 taxane 之間有交叉過敏的報告（Abraxis, 2022）。
- **肝功能**：胰臟癌膽紅素 >1.5 × ULN 不建議使用；ANC <1,500/mm³ 的基線不可開始（Abraxis, 2022）。
- **給藥**：輸注限制在 30 分鐘左右可降低輸注反應風險；密切觀察輸注部位有無外滲（Abraxis, 2022）。

**gemcitabine 的特有警語**（Meitheal, 2025）：輸注時間過長或過密會增加低血壓、類流感症狀與骨髓抑制；骨髓抑制的單藥規則見 5.5；須**永久停用**的情況是嚴重皮膚不良反應（SCAR）、不明原因的呼吸困難或嚴重肺毒性、溶血性尿毒症候群（HUS）或嚴重腎功能不全、嚴重肝毒性、毛細血管滲漏症候群、PRES（Meitheal, 2025）。放射治療期間或放療後 7 天內給藥，可能使放療毒性嚴重加劇（Meitheal, 2025）。

> [!WARNING]
> **GnP 病人發燒，先想膽道**
> 胰頭癌病人有阻塞性黃疸或膽道支架，發燒可能是膽管炎，不是單純的化療後嗜中性球低下；nab-paclitaxel 仿單把膽道阻塞與支架列為致命敗血症的危險因子，並要求發燒不論 ANC 都開廣效抗生素（Abraxis, 2022）。處理順序：抽血培養、驗 CBC 與膽紅素、立刻通知醫師；膽管炎的診斷與引流時機見 [3.5](#35-膽道阻塞什麼時候要引流)，發燒性嗜中性球低下流程見[腫瘤急症](00-shared/02-oncologic-emergencies.md#1-發燒性嗜中性球低下)第 1 節。

### 6.6 Olaparib

| 毒性 | POLO 的數字（olaparib 對安慰劑） | 行動 |
|------|-----------------------------|------|
| 貧血 | 任何等級 27% 對 17%；**3 級以上 11% 對 3%**（Golan et al., 2019） | CBC 基線與之後每月；血液毒性延長就暫停並每週驗 CBC；**4 週內仍未恢復到 ≤G1**，轉血液科做骨髓檢查與細胞遺傳學（AstraZeneca, 2025）。輸血與 ESA 見[支持性照護](00-shared/03-supportive-care.md#10-化療相關貧血血小板低下與輸血)第 10 節 |
| 疲倦、噁心、腹瀉、食慾下降 | 疲倦 60% 對 35%（3 級以上 5% 對 2%）；噁心 45% 對 23%；腹瀉 29% 對 15%；食慾下降 25% 對 7%（Golan et al., 2019） | 支持性處置；必要時減量 250 → 200 mg 每日兩次（AstraZeneca, 2025）。因不良反應停藥 5% 對 2%，生活品質兩組無差別 |
| MDS／AML | 仿單的合併安全資料約 1.2%（26／2,219），其中 54% 致命；病人都曾接受過鉑類或其他傷害 DNA 的治療 | 確診就停藥。持續的血球低下不要只當成化療後遺症（AstraZeneca, 2025） |
| 肺炎 | 約 1.0%，有致命個案 | 疑似就暫停；確診就停藥 |
| 靜脈血栓栓塞 | 仿單警語（含嚴重或致命的肺栓塞） | 監測血栓症狀；胰臟癌本身已是高風險（[支持性照護](00-shared/03-supportive-care.md#7-癌症相關靜脈血栓vte)第 7 節） |
| 肝毒性 | 仿單警語（含藥物性肝損傷） | 疑似就暫停；確診就停藥 |
| 藥物交互作用 | 強效或中效 CYP3A 抑制劑會提高 olaparib 暴露 | 盡量避免；無法避免時減為 100 mg（強效）或 150 mg（中效）每日兩次，停抑制劑 3–5 個半衰期後恢復（AstraZeneca, 2025） |

（毒性分級與處置：AstraZeneca, 2025；POLO：Golan et al., 2019。）olaparib 的血液毒性與前面的鉑類化療累積有關：仿單要求開始前，前一線化療的血液毒性要恢復到 ≤1 級。

### 6.7 胰臟癌病人特有的判讀情境

這些情境的共同點：同一個症狀有好幾個原因，其中一個是膽道、胰酵素或血栓問題，只看化療毒性會漏掉。

| 情境 | 為什麼容易搞混 | 做法 |
|------|--------------|------|
| 化療期間發燒，尤其有黃疸史或膽道支架 | 膽管炎、嗜中性球低下性發燒、導管感染都可能；nab-paclitaxel 仿單把膽道阻塞與支架列為敗血症的危險因子 | 抽血液培養、CBC、膽紅素，立刻通知醫師；膽管炎要有全身發炎、膽汁淤積與影像證據（Kiriyama et al., 2018）；導管感染見[化療基礎](00-shared/01-chemo-basics.md#135-導管相關血流感染crbsi)第 13.5 節；FN 流程見[腫瘤急症](00-shared/02-oncologic-emergencies.md#1-發燒性嗜中性球低下)第 1 節 |
| 腹瀉 | irinotecan 的遲發性腹瀉、fluoropyrimidine 毒性、**胰外分泌不全的脂肪痢**、感染（如 *C. difficile*）、嗜中性球低下性小腸結腸炎可以同時存在 | 先問糞便性質（水瀉，或油亮、惡臭、浮水）、與化療的時間關係、PERT 有沒有隨餐吃（5.6）；水瀉合併發燒、腹痛或血便當作複雜型；通則見[支持性照護](00-shared/03-supportive-care.md#5-腹瀉)第 5 節，嗜中性球低下性小腸結腸炎見[腫瘤急症](00-shared/02-oncologic-emergencies.md#11-惡性腸阻塞與嗜中性球低下性小腸結腸炎)第 11 節 |
| 腹痛、嘔吐、吃不下 | 腸阻塞、胃出口阻塞、胰臟炎或藥物都可以 | irinotecan 與 Onivyde **腸阻塞時不可給**（Pharmacia & Upjohn, 2026；Ipsen, 2025）；不要只加止吐藥或 loperamide 蓋過去；惡性腸阻塞的評估與處置見[腫瘤急症](00-shared/02-oncologic-emergencies.md#11-惡性腸阻塞與嗜中性球低下性小腸結腸炎)第 11 節 |
| 新發咳嗽、喘、發燒 | gemcitabine 肺毒性、GnP 肺炎（4%）、Onivyde 的 ILD、oxaliplatin 肺毒性、olaparib 肺炎（約 1.0%），另外還有肺栓塞與感染 | 先暫停可疑的藥並安排影像與評估：Onivyde 對新發或進展的呼吸困難、咳嗽、發燒暫停待評估（Ipsen, 2025）；oxaliplatin 暫停到排除 ILD（Meitheal, 2024）；同時評估血栓 |
| 血栓與抗凝血藥 | 胰臟癌的 Khorana 部位項目就占 2 分（[支持性照護](00-shared/03-supportive-care.md#71-風險評估khorana-分數)第 7.1 節）；台灣 4 家醫院、838 位接受姑息化療的胰臟癌病人，VTE 為 8.0%（Chen et al., 2018）；抗凝血藥又與多種化療藥有交互作用 | NCCN 病人版：治療 VTE 以 LMWH 優於 warfarin，腫瘤沒有長進胃或腸腔才可用 DOAC（NCCN, 2026）；capecitabine 與 5-FU 合併 warfarin 要密切監測 INR（H2-Pharma, 2026）；oxaliplatin 合併口服抗凝血藥要更頻繁監測出血（Meitheal, 2024）；olaparib 仿單有 VTE 警語。預防與治療見[支持性照護](00-shared/03-supportive-care.md#7-癌症相關靜脈血栓vte)第 7 節 |
| 血糖 | 新發或胰源性（3c 型）糖尿病在胰臟癌很常見，血糖波動大、低血糖風險高，且常合併胰酵素不足（Hart et al., 2016）；止吐用的 dexamethasone 會使血糖升高（[支持性照護](00-shared/03-supportive-care.md#12-預防處方以第一個療程為準)第 1.2 節） | 化療日與類固醇使用期間監測血糖；PERT 與糖尿病處置要一起評估（5.6） |
| 體重快速下降 | 惡病質、胰酵素不足、吃不下；劑量依體表面積算 | 每個週期量體重，依院內規定重算 BSA（[化療基礎](00-shared/01-chemo-basics.md#2-體表面積bsa計算)第 2 節）；營養與惡病質見[支持性照護](00-shared/03-supportive-care.md#121-惡病質與食慾不振)第 12.1 節 |
| 併用藥物 | irinotecan 經 CYP3A4 與 UGT1A1 代謝 | 強效 CYP3A4 誘導劑（rifampin、phenytoin、carbamazepine、phenobarbital、St. John's wort）會大幅降低 irinotecan 與 SN-38 暴露；強效 CYP3A4 抑制劑（如 ketoconazole、clarithromycin、itraconazole、voriconazole）與 UGT1A1 抑制劑（如 atazanavir、gemfibrozil）可能提高暴露。仿單：除非沒有替代，不要併用；盡量在開始前 2 週改用不誘導酵素的藥，強效抑制劑至少提早 1 週停用（Pharmacia & Upjohn, 2026；Ipsen, 2025）。olaparib 的 CYP3A 抑制劑規則見 6.6 |

### 6.8 暫停與永久停藥條件速查

| 藥物 | 永久停藥（仿單） | 暫停，恢復後再給 |
|------|----------------|----------------|
| irinotecan | 嚴重過敏（含 anaphylaxis）；確診的間質性肺病（Pharmacia & Upjohn, 2026） | G2–4 腹瀉（恢復到基線後減量）；ANC <1,000/mm³ 或發燒性嗜中性球低下；腸阻塞（待阻塞解除） |
| Onivyde | 3–4 級手足症候群、任何級別的神經小腦毒性、≥G2 心臟毒性、ILD、anaphylaxis 或嚴重過敏（NALIRIFOX 表）；二線表為 ILD 與 anaphylaxis；減量階梯用完（NALIRIFOX 第四次、二線第三次）仍需減量時也停用（Ipsen, 2025） | G2–4 腹瀉；ANC <1,500/mm³；發燒性嗜中性球低下；3–4 級不良反應（恢復到 ≤G1 且 ANC ≥2,000/mm³、血小板 ≥100,000/mm³） |
| oxaliplatin | 過敏反應；PRES；確診的 ILD 或肺纖維化；橫紋肌溶解；G4 神經病變（Meitheal, 2024） | ANC <1.5 × 10⁹/L 或血小板 <75 × 10⁹/L（延後）；不明原因呼吸道症狀（待排除 ILD）；敗血症 |
| 5-FU | 仿單沒有永久停藥的條列；心臟毒性、高氨性腦病變、急性小腦症候群與神經毒性發生後，**沒有建議的恢復劑量**，是否再給由主治醫師決定（Fresenius Kabi USA, 2026） | G3–4 腹瀉、G3–4 黏膜炎、G2–3 手足症候群、G4 骨髓抑制（恢復到 ≤G1 後減量） |
| capecitabine | 手足症候群 G2 第 4 次、G3 第 3 次；G4 可永久停藥（H2-Pharma, 2026） | 依 Table 1 暫停到 G0–1，再依比例恢復 |
| nab-paclitaxel | 嚴重過敏不可再挑戰；肺炎確診兩藥都停（Abraxis, 2022） | G3–4 神經病變（≤G1 後降 1 級）；發燒性嗜中性球低下；G3 黏膜炎或腹瀉；G2–3 皮膚毒性要降級 |
| gemcitabine | SCAR；不明原因呼吸困難或嚴重肺毒性；HUS 或嚴重腎功能不全；嚴重肝毒性；毛細血管滲漏症候群；PRES（Meitheal, 2025） | ANC 500–999 或血小板 50,000–99,999：75% 劑量；ANC <500 或血小板 <50,000：暫停 |
| olaparib | 確診的 MDS／AML、肺炎、藥物性肝損傷（AstraZeneca, 2025） | 疑似肺炎或藥物性肝損傷；血液毒性延長（每週驗 CBC，4 週未恢復轉血液科） |

> [!IMPORTANT]
> **胰臟癌處方的副作用必背**
> - **irinotecan 早發性** → atropine 0.25–1 mg IV／SC；**遲發性** → loperamide 首劑 4 mg，之後每 2 小時 2 mg 直到無腹瀉 ≥12 小時，高劑量最多連續 48 小時。
> - **Onivyde**：G2–4 腹瀉、ANC <1,500/mm³、發燒性嗜中性球低下就暫停；腸阻塞不可給；膽紅素高於 ULN 沒有建議劑量；NALIRIFOX 的 50 mg/m² 不因 UGT1A1\*28 減量，二線 70 mg/m² 的 \*28 同型合子從 50 起。
> - **UGT1A1**：\*28／\*28、\*6／\*6、\*6／\*28 → 起始劑量考慮至少降 1 級；亞洲對偶基因頻率約 \*6 13.0%、\*28 13.9%（Chang et al., 2015）。
> - **oxaliplatin**：急性神經症狀冷誘發、避冷、不冰敷；過敏任何週期都可能，立即且永久停藥；CrCl <30 → 65 mg/m²。
> - **5-FU／capecitabine**：先想 DPYD；capecitabine 手足症候群 G2 階梯 100%／75%／50%／停；46 小時輸注期間的胸痛、意識改變、步態不穩要停藥。
> - **nab-paclitaxel**：神經病變 G3–4 暫停到 ≤G1，nab-paclitaxel 降 1 級、gemcitabine **不減量**；有膽道支架或阻塞者發燒，不論 ANC 都開廣效抗生素。
> - **olaparib**：300 mg 每日兩次；每月 CBC；POLO 的 3 級以上貧血 11%（對照 3%），因不良反應停藥 5%。

---

## 7. 專師實務

**這一段的結論先講：** 胰臟癌病人的專師工作，化療處方只占一半，另一半是化療以外的六件事：**膽道有沒有通、胰酵素夠不夠、血糖穩不穩、有沒有血栓、吃得下與體重、痛不痛**，最後是病人與家屬知不知道治療的目標。這些問題會互相冒充（發燒可能是膽管炎、嗜中性球低下或導管感染；腹瀉可能是 irinotecan、脂肪痢或感染），所以每次門診與查房，先用下表七個問題掃一遍，再去看化療的數字。處方劑量與毒性處置見第 5、6 段，急症的第一小時處置見第 8 段。

| 每次都問的問題 | 為什麼問 | 往哪裡看 |
|---------------|---------|---------|
| 眼睛皮膚變黃、茶色尿、灰白便、搔癢、發燒或冷顫嗎？ | 膽道阻塞復發、支架堵塞與膽管炎；膽紅素還決定能不能打 Onivyde、irinotecan 與 nab-paclitaxel | [7.6](#76-膽道支架與膽管炎的日常照護)、[8.1](#81-急性膽管炎acute-cholangitis) |
| 大便是水瀉，還是油亮、惡臭、浮水？胰酵素有沒有隨餐吃？ | irinotecan 的腹瀉與胰外分泌不全的脂肪痢，處置完全不同 | [7.7](#77-胰酵素替代治療的病房流程)、[6.2](#62-irinotecan-與脂質體-irinotecan) |
| 有沒有冒冷汗、發抖、口渴多尿？吃不下的那幾天胰島素怎麼打？ | 胰源性糖尿病容易低血糖；dexamethasone 又會使血糖升高 | [7.9](#79-血糖胰源性3c-型糖尿病與化療期間)、[8.6](#86-低血糖與高血糖危象) |
| 單側腿腫、胸痛、喘、突然的腹痛或腹脹？ | 胰臟癌在 Khorana 分數的部位項目就占 2 分；門靜脈、脾靜脈也會有血栓 | [7.10](#710-血栓預防與處置)、[8.4](#84-門靜脈脾靜脈與腸繫膜靜脈血栓) |
| 一天吃多少？體重幾公斤？ | 體重下降是最常見的表現之一，也決定 BSA 要不要重算 | [7.8](#78-惡病質與營養) |
| 痛幾分？鴉片類用多少？有沒有便祕？ | 胰臟癌的疼痛常需要多層次處置；腹瀉時要停軟便劑 | [7.11](#711-疼痛與-celiac-plexus-neurolysis)、[8.5](#85-無法控制的疼痛) |
| 病人與家屬知道這個治療的目標嗎？ | 早期整合緩和照護是 ASCO 的建議，胰臟癌有隨機試驗支持 | [7.12](#712-緩和照護的整合) |

### 7.1 每次化療前檢核

通用的化療前檢核見[化療基礎](00-shared/01-chemo-basics.md#5-化療前檢核pre-chemo-checklist)第 5 節。下表只列胰臟癌處方要多看的地方，門檻出處見 [5.5](#55-前置用藥止吐與給藥當天的門檻) 與 [5.7](#57-肝腎功能與膽紅素門檻速查)。

| 項目 | 通用門檻 | 胰臟癌要多看的 |
|------|---------|---------------|
| 體能與體重 | ECOG 與上次比較 | 每個週期量體重；超過院內重算 BSA 的比例（常見 ±5% 或 ±10%）就重算；ECOG 變差通知主治醫師，PS 2 以上的方案選擇見 [4.8](#48-轉移性第一線依體能分層) |
| 膽紅素與引流狀態 | 肝功能在可接受範圍 | Onivyde：高於正常上限**沒有建議劑量**；irinotecan：>2 mg/dL 沒有建議劑量；nab-paclitaxel：>1.5 × ULN 不建議（Ipsen, 2025；Pharmacia & Upjohn, 2026；Abraxis, 2022）。同時問黃疸、搔癢、茶色尿、發燒，確認支架是否通暢 |
| 血球 | ANC ≥1,500/µL、PLT ≥100,000/µL | GnP 的 D8、D15 規則見 [6.5](#65-nab-paclitaxel-與-gemcitabinegnp)；Onivyde 每個週期的 D1 與 D8 都驗 CBC；olaparib 每月驗 CBC |
| 腎功能 | 估算 CrCl | oxaliplatin：CrCl <30 mL/min 減為 65 mg/m²；capecitabine：CrCl 30–50 mL/min 減 25%；olaparib：CrCl 31–50 mL/min 起始 200 mg 每日兩次；irinotecan 透析病人不可使用 |
| 腸道 | 前次毒性恢復到 ≤1 級 | 腹瀉已恢復，且不靠止瀉藥已 ≥24 小時，才開下一個含 irinotecan 的週期；腸阻塞時 irinotecan 與 Onivyde 不可給（[5.5](#55-前置用藥止吐與給藥當天的門檻)、[6.2](#62-irinotecan-與脂質體-irinotecan)） |
| 神經 | | oxaliplatin 與 nab-paclitaxel 的神經病變都是累積性；每個週期問「寫字、用手機、走路有沒有變差」，不要等病人主訴（[6.3](#63-oxaliplatin)、[6.5](#65-nab-paclitaxel-與-gemcitabinegnp)） |
| DPYD、UGT1A1 | 見[化療基礎](00-shared/01-chemo-basics.md#12-藥物基因檢測與特殊族群評估)第 12 節 | 開 5-FU、capecitabine 前先想 DPYD；開 irinotecan 前先想 UGT1A1（含台灣常見的 \*6）；PRODIGE 24 排除 UGT1A1\*28/\*28 與 Gilbert 症，檢測陰性不等於安全 |
| 血糖 | | 基線空腹血糖與 HbA1c；dexamethasone 當天與之後幾天追蹤；已用胰島素者先評估低血糖風險（[7.9](#79-血糖胰源性3c-型糖尿病與化療期間)） |
| 血栓與抗凝血藥 | | 問單側腿腫、胸痛、喘；已在用 warfarin 或口服抗凝血藥者，與 capecitabine、5-FU、oxaliplatin 併用要更密切監測（[6.7](#67-胰臟癌病人特有的判讀情境)） |
| 胰酵素與營養 | | 糞便性質、胰酵素劑量與是否隨餐、攝食量與體重（[7.7](#77-胰酵素替代治療的病房流程)、[7.8](#78-惡病質與營養)） |
| 疼痛與便祕 | | 疼痛分數與鴉片類劑量；腹瀉時停軟便劑，第一次稀便就開始 loperamide |
| CA19-9 | | 基準值要在膽紅素下降後抽；Lewis-negative 的病人不能靠 CA19-9 追蹤（[3.4](#34-ca19-9)、[7.14](#714-療效評估與追蹤時程)） |
| 前置用藥 | 確認 premedication | Onivyde 輸注前 30 分鐘給 corticosteroid ＋ 止吐藥；irinotecan 的早發性膽鹼症狀備 atropine；GnP 沒有常規的過敏前置 |
| 通路 | 確認 port 或周邊靜脈 | 46 小時 5-FU 要經中心靜脈並用輸液幫浦，給藥前先確認回血（[化療基礎](00-shared/01-chemo-basics.md#13-中心靜脈導管照護port-apicc隧道式導管)第 13 節） |
| B 肝與生育力 | HBsAg、anti-HBc、anti-HBs；生育力與避孕 | 見[化療基礎](00-shared/01-chemo-basics.md#6-b-型肝炎篩檢與預防性抗病毒)第 6、12.5 節；Onivyde 仿單要求有生育可能的女性避孕至最後一劑後 7 個月 |

> [!WARNING]
> **止瀉藥和軟便劑的方向相反**
> 胰臟癌病人常因鴉片類止痛藥固定吃軟便劑；開始 irinotecan 之後，一拉肚子就要先停軟便劑，同時開始 loperamide（Pharmacia & Upjohn, 2026）。出院前把「哪一顆停、哪一顆開始吃」寫在衛教單上，並請病人覆述一次。

### 7.2 Order set 範例一：輔助 mFOLFIRINOX（第 1 週期第 1 天）

情境：58 歲男性，胰頭 PDAC，Whipple 術後 8 週，pT2N1M0（IIB 期）、R0，ECOG 0。身高 168 cm、體重 64 kg，血清肌酸酐 0.8 mg/dL，ANC 3,200/µL、PLT 210,000/µL、總膽紅素 0.6 mg/dL，術後 CA19-9 22 U/mL，UGT1A1 與 DPYD 結果已由主治醫師評估。依據是 PRODIGE 24（Conroy et al., 2018, 2022）：每 2 週一次、共 12 次（24 週）；NCCN 病人版建議輔助治療最好在術後 12 週內開始（NCCN, 2026）。

**劑量計算**（假設用 Mosteller 公式；實際 BSA 與四捨五入依院內系統。BSA 與 CrCl 的公式見[化療基礎](00-shared/01-chemo-basics.md#2-體表面積bsa計算)第 2、3 節）

```text
BSA  = √(168 × 64 ÷ 3,600) = √2.987 = 1.73 m²
CrCl = (140 − 58) × 64 ÷ (72 × 0.8) = 5,248 ÷ 57.6 ≈ 91 mL/min（Cockcroft-Gault）

oxaliplatin   85 mg/m²    × 1.73 = 147 mg
irinotecan   150 mg/m²    × 1.73 = 259.5 → 約 260 mg
leucovorin   400 mg/m²    × 1.73 = 692 mg
5-FU       2,400 mg/m²    × 1.73 = 4,152 mg，46 小時持續輸注 → 4,152 ÷ 46 ≈ 90.3 mg/h
5-FU bolus   無（輔助 mFOLFIRINOX 不加 bolus）
```

**醫囑範例**

```text
週期 1／12，第 1 天（每 14 天一次）
給藥前：CBC/DC、BUN/Cr、AST/ALT/ALP/T-bil、Na/K/Mg、glucose；確認 port 回血；
        確認 loperamide 已交給病人；確認病人已被告知 46 小時幫浦的注意事項（7.3）
止吐：5-HT3 拮抗劑（例：palonosetron 0.25 mg IV）＋ dexamethasone（劑量依院內止吐規範），
      化療前 30 分鐘
Atropine 0.25–1 mg IV 或 SC，irinotecan 開始前（預防早發性膽鹼症狀；臨床上有禁忌者除外）
  1. Oxaliplatin 147 mg in D5W 250–500 mL，IV 2 小時（不可用 NS 或含氯溶液；管路先用 D5W 沖）
  2. Leucovorin 692 mg，IV 2 小時
  3. Irinotecan 260 mg，在 leucovorin 輸注的最後 90 分鐘同時給，IV 90 分鐘
  4. 5-FU 4,152 mg 持續輸注 46 小時（約 90.3 mg/h），經 port 以攜帶式幫浦；無 bolus
第 3 天（約 46 小時後）：回診拆除幫浦，沖管與封管依院內護理標準
居家：loperamide 備藥（遲發性腹瀉：首劑 4 mg，之後每 2 小時 2 mg，直到無腹瀉至少 12 小時，
      高劑量最多連續 48 小時）；突破性噁心的 PRN 止吐藥；避冷
      發燒 ≥38°C、腹瀉、黃疸、胸痛、意識改變、走路不穩：立即聯絡
下次：第 15 天抽血；ANC ≥1,500/µL、PLT ≥100,000/µL 且腹瀉已恢復，才給第 2 週期
```

給藥順序與輸注時間取自 Pan-Asian ESMO 對 FOLFIRINOX 的描述：oxaliplatin 2 小時，leucovorin 在 oxaliplatin 之後 2 小時，irinotecan 在 leucovorin 的最後 90 分鐘給（Tai et al., 2025）。atropine 與 loperamide 的用法是 irinotecan 仿單的原文（Pharmacia & Upjohn, 2026）；多藥方案的整體致吐分級與 G-CSF 一級預防沒有取得指引原文，見 [5.5](#55-前置用藥止吐與給藥當天的門檻) 的待核對說明。

**同一位病人若是轉移性 FOLFIRINOX（PRODIGE 4），差在哪裡**

| 藥物 | 輔助 mFOLFIRINOX | 轉移性 FOLFIRINOX |
|------|-----------------|------------------|
| oxaliplatin | 85 mg/m² → 147 mg | 85 mg/m² → 147 mg |
| irinotecan | **150 mg/m² → 260 mg** | **180 mg/m² → 311 mg**（180 × 1.73 = 311.4） |
| leucovorin | 400 mg/m² → 692 mg | 400 mg/m² → 692 mg |
| 5-FU bolus | **無** | **400 mg/m² → 692 mg** |
| 5-FU 持續輸注 | 2,400 mg/m² → 4,152 mg（46 小時） | 2,400 mg/m² → 4,152 mg（46 小時） |

> [!WARNING]
> **5-FU bolus 與 irinotecan 劑量：開立前核對三件事**
> 1. 這張醫囑是**輔助**（無 bolus，irinotecan 150）還是**轉移性**（bolus 400 mg/m²，irinotecan 180）？兩者在醫囑上只差兩行，複製舊處方時很容易混淆（[5.1](#51-folfirinox-家族輔助-mfolfirinox-與轉移性-folfirinox)）。
> 2. irinotecan 是一般劑型（如 Campto），**不是 Onivyde**；Onivyde 的劑量單位與輸注時間都不同，不可互換（[5.2](#52-脂質體-irinotecannalirifox-與二線-nal-iri--5-fuleucovorin)）。
> 3. oxaliplatin 的稀釋液是 5% dextrose，管路沖洗液也是 5% dextrose（[5.1](#51-folfirinox-家族輔助-mfolfirinox-與轉移性-folfirinox)）。

> [!NOTE]
> **院內規範要確認的地方**
> 輸注時間、稀釋液與體積、leucovorin 與 irinotecan 是否共用 Y 型接頭、止吐組合與 dexamethasone 劑量、G-CSF 是否一級預防、BSA 公式與四捨五入規則，各院 protocol 不同。上面是格式示範，實際以單位 protocol 為準。健保方面，輔助 mFOLFIRINOX 沒有對應條文：oxaliplatin 的 9.10 第 3 點（本點 111/11/1；全條最新修訂 115/2/1）與 irinotecan 的 9.12.1 第 2 點（112/2/1）都只寫轉移性第一線（[4.4](#44-術後輔助治療)）。

> [!IMPORTANT]
> **輔助 mFOLFIRINOX 的考試重點**
> - 劑量：oxaliplatin 85、irinotecan **150**、leucovorin 400、5-FU 2,400 mg/m² 持續輸注 46 小時，**無 bolus**，共 12 次（24 週）。
> - 療效：5 年追蹤的中位 OS 53.5 對 35.5 個月（HR 0.68，0.54–0.85）；3 級以上毒性 75.9%，嗜中性球低下 28.4%、腹瀉 18.6%（Conroy et al., 2022；Tai et al., 2025）。
> - 試驗排除 UGT1A1\*28/\*28、Gilbert 症與既存神經病變，所以「適合 mFOLFIRINOX」是比「術後病人」更窄的族群。

### 7.3 46 小時幫浦：接上、拆除與居家衛教

5-FU 的持續輸注要經中心靜脈並用輸液幫浦（Fresenius Kabi USA, 2026）。FOLFIRINOX、mFOLFIRINOX、NALIRIFOX 與二線 nal-IRI ＋ 5-FU／leucovorin 都有這 46 小時，而 5-FU 仿單列為要暫停的心臟毒性、高氨性腦病變與急性小腦症候群，正好落在病人回家的這兩天（[6.4](#64-5-fucapecitabine-與-s-1)）。下表依時間點列出醫療端要做的事與要教的事；導管與 port 的操作細節見[化療基礎](00-shared/01-chemo-basics.md#13-中心靜脈導管照護port-apicc隧道式導管)第 13 節，給藥安全標準見同章第 14 節。

| 時間點 | 護理與專師做什麼 | 要教病人與照顧者什麼 |
|--------|----------------|--------------------|
| 接上前（第 1 天） | 確認 port 回血與通暢；5-FU 的劑量、體積與幫浦速率由至少兩位合格人員核對（Neuss et al., 2013）；確認 loperamide 與止吐藥已發給病人 | 先示範再說明：幫浦放在哪裡、管路不要折到或被壓住；請病人用自己的話覆述（teach-back） |
| 接上後、離院前 | 確認幫浦運轉、接點鎖緊、針頭固定、敷料完整；記錄開始時間與預定結束時間；給書面衛教與 24 小時聯絡電話 | 幫浦預定結束的日期與時間；淋浴時用不透水的覆蓋物保護導管與連接處（O'Grady et al., 2011） |
| 居家 46 小時 | 第一個週期主動打電話追蹤（時間點依院內流程）；接到胸痛、意識改變、走路不穩的電話，不要只是安撫（[6.4](#64-5-fucapecitabine-與-s-1)） | **依院內流程停止輸注並立即聯絡**：胸痛或心悸；混亂、嗜睡、走路不穩、視力異常；port 部位灼熱、疼痛、腫脹或漏液；幫浦警示無法排除 |
| 居家，遲發性腹瀉的時間窗 | 確認病人手上有 loperamide，並說得出用法 | 第一次稀便就開始 loperamide：首劑 4 mg，之後每 2 小時 2 mg，直到無腹瀉至少 12 小時；停軟便劑；多喝水；腹瀉合併發燒、明顯脫水（口渴、尿少、頭暈）或持續 48 小時以上不改善，就回診（[6.2](#62-irinotecan-與脂質體-irinotecan)；[支持性照護](00-shared/03-supportive-care.md#52-處置)第 5.2 節） |
| 居家，oxaliplatin 的冷誘發症狀 | | 不喝冰飲、不碰冰冷物、冷天遮蓋皮膚；咽喉緊縮感通常是感覺異常，但喘鳴或血氧下降要立刻就醫；不要用冰塊含漱（[6.3](#63-oxaliplatin)） |
| 發燒 | 依[腫瘤急症](00-shared/02-oncologic-emergencies.md#1-發燒性嗜中性球低下)第 1 節的 FN 流程 | 發燒 ≥38°C 立即回診；有膽道支架者同時想膽管炎（[8.1](#81-急性膽管炎acute-cholangitis)） |
| 管路漏液或脫落 | 5-FU 屬危害藥品，接觸時戴雙層手套，用溢出處理包；通報並記錄（[化療基礎](00-shared/01-chemo-basics.md#10-抗癌藥物的安全操作)第 10 節） | 不要徒手處理，立即聯絡並依院內衛教單處理；家中處理病人排泄物的做法也依院內衛教單（常見為給藥後 48 小時內戴手套） |
| 拆除（約第 3 天） | 核對剩餘藥量與輸注完成時間；沖管與封管依院內標準；檢查 port 部位；評估腹瀉、神經、口腔與血壓；預約下次抽血與回診 | 拆除後仍是遲發性腹瀉的時間窗，loperamide 與症狀日誌繼續到下次回診 |

**出院前的 teach-back 五問**（請病人自己回答，不是點頭）：（1）幫浦哪一天幾點跑完？（2）哪些症狀要停止輸注並馬上打電話？（3）一拉肚子，先吃哪一顆藥、怎麼吃，哪一顆要停？（4）冷的東西可以碰嗎？（5）發燒幾度要回來？

> [!NOTE]
> **幫浦與居家拆除依院內規範**
> 幫浦型號、警示的處理步驟、拆除由誰做（回診由護理人員拆除，或居家護理、經訓練後自行拆除）、化療廢棄物的處理與病人排泄物的注意期間，各院規範不同。本表是衛教項目的架構，具體步驟與電話以單位護理標準為準。

### 7.4 Order set 範例二：gemcitabine ＋ nab-paclitaxel（轉移性第一線，第 1 週期）

情境：66 歲女性，轉移性胰頭 PDAC（肝轉移），ECOG 1。入院時黃疸，已由內視鏡置放金屬支架（SEMS），引流後總膽紅素 0.8 mg/dL（假設正常上限 1.2 mg/dL，1.5 × ULN = 1.8 mg/dL，所以符合 nab-paclitaxel 的使用條件）。身高 156 cm、體重 51 kg，血清肌酸酐 0.7 mg/dL。依據是 MPACT（Von Hoff et al., 2013）與 Abraxane 仿單（Abraxis, 2022）。

**劑量計算**（Mosteller；實際依院內系統）

```text
BSA  = √(156 × 51 ÷ 3,600) = √2.21 = 1.49 m²
CrCl = (140 − 66) × 51 ÷ (72 × 0.7) × 0.85 = 3,774 ÷ 50.4 × 0.85 ≈ 64 mL/min

nab-paclitaxel  125 mg/m² × 1.49 = 186 mg（186.25）
gemcitabine   1,000 mg/m² × 1.49 = 1,490 mg

劑量等級（nab-paclitaxel／gemcitabine，mg/m²）：125／1,000 → 100／800 → 75／600 → 停用
  −1 級：100 × 1.49 = 149 mg ／ 800 × 1.49 = 1,192 mg
  −2 級：75 × 1.49 = 112 mg（111.75）／ 600 × 1.49 = 894 mg
```

**醫囑範例**

```text
週期 1，第 1、8、15 天（每 28 天）
第 1 天給藥前：CBC/DC（ANC ≥1,500/mm³ 且 PLT ≥100,000/mm³ 才給）、BUN/Cr、AST/ALT/ALP/T-bil、
              glucose、CA19-9 基準值（已引流、膽紅素下降後）
止吐：低致吐，單一藥物即可（5-HT3 拮抗劑或 dexamethasone 擇一；有糖尿病者與主治醫師討論）
無常規的過敏前置用藥
  1. Albumin-bound paclitaxel（nab-paclitaxel）186 mg，IV 30–40 分鐘
  2. Gemcitabine 1,490 mg，接在 nab-paclitaxel 之後 IV 30–40 分鐘
第 8、15 天：給藥前 CBC/DC，依下表決定劑量
衛教：發燒（不論 ANC）、黃疸復發、搔癢、茶色尿、手腳麻木、新的咳嗽或喘立即聯絡
```

**第 8 天的決定**（Abraxis, 2022；表上沒有列到的結果，代表照原劑量給藥）

| 第 8 天結果 | 仿單的行動 | 這位病人的劑量 |
|------------|-----------|---------------|
| ANC 800/mm³、PLT 90,000/mm³ | ANC 落在 500 至 <1,000：兩藥降 1 級 | nab-paclitaxel 149 mg、gemcitabine 1,192 mg |
| ANC 1,300/mm³、PLT 62,000/mm³ | PLT 落在 50,000 至 <75,000：兩藥降 1 級 | 同上 |
| ANC 400/mm³ | ANC <500：暫停 | 不給 |
| 手腳麻木影響扣釦子與寫字（3 級） | 暫停到 ≤1 級，**只有 nab-paclitaxel 降 1 級，gemcitabine 不減量** | nab-paclitaxel 149 mg、gemcitabine 1,490 mg |
| 發燒（不論 ANC），膽道有支架 | 先給廣效抗生素；若是發燒性嗜中性球低下，兩藥都暫停 | 見 [8.1](#81-急性膽管炎acute-cholangitis) |

> [!IMPORTANT]
> **GnP 的考試重點**
> - D1：ANC <1,500/mm³ 或 PLT <100,000/mm³ 延後；D8：ANC 500–<1,000 或 PLT 50,000–<75,000 降 1 級，ANC <500 或 PLT <50,000 暫停（Abraxis, 2022）。
> - 劑量階梯 125／1,000 → 100／800 → 75／600；3–4 級神經病變只降 nab-paclitaxel。
> - 黃疸或有膽道支架的病人：nab-paclitaxel 在膽紅素 >1.5 × ULN 時不建議使用；沒有常規過敏前置，但與其他 paclitaxel 劑型不可互換。

> [!WARNING]
> **兩個藥一起降，只有神經病變例外**
> 血球低下造成的降級是 nab-paclitaxel 與 gemcitabine 同步降；神經病變只降 nab-paclitaxel。開立減量醫囑時，兩個藥要各自寫出 mg/m² 與 mg，不要只寫「降一級」。

### 7.5 SOAP 範例：輔助 mFOLFIRINOX 第 4 週期前的門診

**情境：** 7.2 的同一位病人（58 歲男性，胰頭 PDAC 術後，pT2N1M0）。輔助 mFOLFIRINOX 已完成 3 個週期，今天是第 4 週期第 1 天的化療前門診。第 1 週期的體重是 64 kg（BSA 1.73 m²）。

```text
S：C3 之後手指麻木持續超過 2 週，用手機與切菜時握不穩，扣釦子還可以。
   C3 後第 4–6 天水瀉每天 5–6 次（平時 1 次），照指示吃 loperamide，第 7 天恢復，
   已經 3 天不需要止瀉藥。
   大便油亮、浮在水面、味道很重，約 3 週；Creon 25000 每正餐吃 1 顆，點心沒吃。
   食慾尚可，沒有嘔吐。無發燒、黃疸、腹痛或腿腫。疼痛 NRS 1/10（腹部傷口）。
O：BT 36.7°C、HR 78、BP 118/72、SpO2 99%。體重 60.5 kg（C1：64 kg，−5.5%）。
   神經學：雙手指尖針刺覺減退，Romberg 陰性，步態正常。
   Lab：ANC 2,100/µL、PLT 168,000/µL、Hb 11.2 g/dL、T-bil 0.5 mg/dL、ALT 28 U/L、
        Cr 0.8 mg/dL、K 3.6 mmol/L、空腹血糖 118 mg/dL；CA19-9 18 U/mL（術後基準值 22）。
A：1. Oxaliplatin 累積性周邊感覺神經病變，CTCAE v5.0 G2（持續 >14 天，影響工具性日常活動）
   2. Irinotecan 遲發性腹瀉 G2（C3 後），已恢復，且停止痛藥已 ≥24 小時
   3. 疑似胰外分泌不全：油亮浮水便、體重下降；Creon 每餐 25,000 單位，低於建議的 40,000–50,000
   4. 4 週體重下降 5.5%，超過惡病質診斷標準的 5%
   5. 胰頭 PDAC 術後輔助 mFOLFIRINOX C3 完成，無復發跡象
P：1. 與主治醫師討論 oxaliplatin：持續性 G2 考慮減量（FOLFIRINOX 的減量級距依院內 protocol，見 6.3）；
      C4 是否給藥與劑量由主治醫師決定
   2. 體重 −5.5%，若院內以 ±5% 為重算門檻則需重算（±10% 則不需要）：
      BSA = √(168 × 60.5 ÷ 3,600) = 1.68 m²（−2.9%）；
      irinotecan 150 × 1.68 = 252 mg、leucovorin 400 × 1.68 = 672 mg、5-FU 2,400 × 1.68 = 4,032 mg
   3. PERT：Creon 25000 改每正餐 2 顆（50,000 單位）、點心 1 顆（25,000 單位），隨餐中吃；
      下次回診追蹤大便與體重，仍無改善再加 PPI；營養師會診
   4. 衛教：避冷、防跌與防燙傷；下次腹瀉照 loperamide 流程，並停軟便劑
   5. 下次回診第 15 天抽血（ANC、PLT、腹瀉恢復）；CA19-9 追蹤頻率依主治醫師
```

這份紀錄有三個寫法值得學：（1）A 把同一個「拉肚子」拆成不同的問題（irinotecan 腹瀉已恢復，另有疑似脂肪痢），處置才不會混在一起；（2）A3 寫出劑量數字（25,000 對 40,000–50,000 單位），主治醫師與藥師才看得出為什麼要加量（Dominguez-Muñoz et al., 2025）；（3）P2 寫出重算 BSA 的依據與算式，方便藥師核對。

### 7.6 膽道支架與膽管炎的日常照護

**這一小節的結論先講：** 膽道支架是把堵住的水管撐開，不是一勞永逸。塑膠支架大約 3 個月會堵塞，不可切除病人優先用金屬支架（self-expandable metal stent, SEMS），膽管炎比較少（8% 對 21%）（Sawas et al., 2015；Dumonceau et al., 2018）。所以有支架的病人，每次門診都要問黃疸復發、搔癢、茶色尿、發燒；**化療期間的發燒先想膽管炎**，不要只當成嗜中性球低下。

| 支架 | 特性 | 護理上要知道 |
|------|------|-------------|
| 塑膠支架 | 約 3 個月會堵塞，只適合短暫橋接（例如等手術）或病理尚未確診者 | 病歷與病人手上的卡片都要記載置放日期與預定更換時間 |
| 金屬支架（SEMS） | 不可切除、預期非手術處置者的優先選擇，阻塞與再介入較少；術前引流用 10-mm SEMS | 裝了金屬支架仍可能堵塞或發生膽管炎，發燒、黃疸復發時照樣要處理 |
| 病理尚未確診時 | 用有覆膜的 SEMS（covered）或塑膠支架，**不用無覆膜的 SEMS（uncovered）** | 置放前先確認病理狀態與外科計畫（[3.5](#35-膽道阻塞什麼時候要引流)） |

（Dumonceau et al., 2018；Sawas et al., 2015。）

**門診與查房的固定動作**

1. 問黃疸復發、搔癢、茶色尿、灰白便、右上腹痛、發燒與冷顫；抽血看總膽紅素與 ALP 的趨勢，不要只看單次數字。
2. 化療前確認膽紅素在各藥的門檻之內（[5.7](#57-肝腎功能與膽紅素門檻速查)）；膽紅素上升時，先找支架堵塞，不要先怪藥。
3. CA19-9 在膽道阻塞時會偽陽性，數值升高時先確認膽道通不通（[3.4](#34-ca19-9)）。
4. 發燒時：血液培養至少 2 套（含 port），分流後 60 分鐘內給第一劑經驗性抗生素，並同時通知消化內科評估引流（[腫瘤急症](00-shared/02-oncologic-emergencies.md#1-發燒性嗜中性球低下)第 1 節；[8.1](#81-急性膽管炎acute-cholangitis)）。

**化療期間發燒，三種原因怎麼先分**（完整流程見 [6.7](#67-胰臟癌病人特有的判讀情境)）

| 可能原因 | 線索 | 第一步 |
|---------|------|--------|
| 膽管炎 | 發燒加黃疸、右上腹痛；膽紅素或 ALP 上升；有支架或膽道阻塞史 | 血液培養、抗生素、通知消化內科評估引流（Kiriyama et al., 2018） |
| 發燒性嗜中性球低下 | 化療後 7–14 天的 nadir；ANC <500/µL 或預期 48 小時內降到 <500/µL | FN 流程；有膽道阻塞或支架者，發燒不論 ANC 都要開廣效抗生素（Abraxis, 2022） |
| 導管相關血流感染 | port 部位紅腫、沖管後冷顫 | 從 port 與周邊各抽血液培養（[化療基礎](00-shared/01-chemo-basics.md#135-導管相關血流感染crbsi)第 13.5 節） |

三者可以同時存在，所以抽血液培養、給抗生素與通知醫師是同一個動作，不是三選一。

> [!TIP]
> **支架像一條引流水管**
> 膽汁從肝臟經膽管流向十二指腸，胰頭的腫瘤像一塊壓在水管上的石頭。塑膠支架是一根細吸管，容易被濃稠的膽汁和泥沙堵住；金屬支架像可以自己撐開的粗水管，不容易堵，但也不是永遠不堵。水管一堵，積在上游的膽汁就會發炎、感染，這就是膽管炎。（教學簡化，臨床判斷以醫師為準。）

### 7.7 胰酵素替代治療的病房流程

PEI 的機轉、劑量與台灣產品見 [5.6](#56-胰酵素替代治療pert)。這裡只列病房要做的步驟，依據是 2025 年歐洲 PEI 指引（Dominguez-Muñoz et al., 2025）。

| 步驟 | 要做的事 | 備註 |
|------|---------|------|
| 辨識 | 油亮、惡臭、浮水的大便，體重下降，腹脹；先分辨是不是 irinotecan 的水瀉 | 兩者可以同時存在（[6.7](#67-胰臟癌病人特有的判讀情境)） |
| 開立 | 劑量以 **lipase 單位**計：每個主餐 40,000–50,000 單位，點心 20,000–25,000 單位；醫囑寫「隨餐」，每個正餐與點心各一份 | Creon 25000：正餐 2 顆、點心 1 顆；不要排進「三餐飯後」的固定給藥時間 |
| 衛教 | 和食物一起吃；沒吃東西就不必吃；請病人自己說出「哪一餐吃幾顆」 | 酵素和食物要同時到腸道才有效 |
| 評估反應 | 追蹤大便次數與性質、體重、腹脹，與血糖（見 [7.9](#79-血糖胰源性3c-型糖尿病與化療期間)） | 結果寫進病歷，健保申報要用（見下） |
| 沒有反應 | 先確認有隨餐、時間正確、順從性 → 提高劑量 → 加 PPI（胃酸會影響腸溶包衣的溶解） | 重度 PEI（胰臟癌、胰十二指腸切除、全胰切除）常需要更高劑量 |
| 禁食、管灌、全靜脈營養 | 與營養科和主治醫師確認給不給、怎麼給 | 不要自行照常給或整天停掉 |

**健保（7.3.6，110/1/1）：** 適用因疾病造成的胰液分泌不全，原文列有囊狀性纖維化、慢性胰臟炎、**胰臟切除手術**、胃腸繞道手術，以及「其他因腫瘤引發之胰管膽管阻塞」；申報費用時要檢附病歷資料與檢驗（查）報告，內容包括胰液分泌不全的疾病，以及營養不良或脂肪痢便的記載；功能性腸胃炎不得使用。所以 7.5 的 SOAP 把「油亮浮水便、體重下降」寫進 S 與 A，是為了病人的照護，也是為了符合申報條件。

### 7.8 惡病質與營養

胰臟癌確診時，體重下降是最常見的症狀之一（85%；Porta et al., 2005），之後化療又會加一層。體重掉的原因常常不只一個，先分原因，再談營養與藥物。

| 原因 | 線索 | 做法 |
|------|------|------|
| 胰外分泌不全 | 油亮浮水便，食慾還可以但體重掉 | 胰酵素加量（[7.7](#77-胰酵素替代治療的病房流程)） |
| 胃出口阻塞 | 吃了就吐、早飽 | [8.2](#82-胃出口阻塞) |
| 化療副作用 | 噁心、口腔炎、腹瀉、味覺改變 | [支持性照護](00-shared/03-supportive-care.md#1-化療引起的噁心嘔吐cinv)第 1、4、5 節 |
| 疼痛與鴉片類副作用 | 吃飯會痛、便祕、嗜睡 | [7.11](#711-疼痛與-celiac-plexus-neurolysis)；[支持性照護](00-shared/03-supportive-care.md#3-癌症疼痛)第 3、6 節 |
| 血糖失控 | 怕低血糖不敢吃，或高血糖多尿脫水 | [7.9](#79-血糖胰源性3c-型糖尿病與化療期間) |
| 憂鬱與困擾 | 沒胃口、失眠、退縮 | [支持性照護](00-shared/03-supportive-care.md#125-困擾篩檢distress-thermometer)第 12.5 節 |
| 癌症惡病質（全身性發炎造成肌肉流失） | 體重流失 >5%，肌肉量與肌力下降 | 見下 |

**營養與藥物的證據**（定義與診斷見[支持性照護](00-shared/03-supportive-care.md#121-惡病質與食慾不振)第 12.1 節）

- **營養**：ASCO 2020 認為營養諮詢可以提供，但**不應常規使用腸道餵食管與靜脈營養**（Roeland et al., 2020）；ESPEN 2021 涵蓋癌症病人的營養篩檢與營養處置（Muscaritoli et al., 2021）。熱量與蛋白質目標由營養師個別計算。
- **藥物**：沒有任何藥物強到足以列為標準；若試用，ASCO 2020 列 progesterone analog 與短期類固醇（Roeland et al., 2020）。ASCO 2023 rapid update 加入低劑量 olanzapine 2.5 mg 每日一次（Roeland et al., 2023）；基礎試驗（Sandhya 2023，含肝膽胰癌病人）olanzapine 組體重增加 >5% 的比例是 60% 對 9%（Sandhya et al., 2023）。
- **健保**：megestrol 口服液劑是 5.3.6（108/6/1、109/3/1），限用於已排除其他可治療的體重減輕之後、具惡病質的後天免疫缺乏症候群患者及癌症患者；條文定義的惡病質是最近 6 個月內體重流失 >5%，或 BMI <20 且體重流失 >2%。olanzapine 與類固醇用於惡病質的給付，原文未見。
- **anamorelin**：日本 2020 年核准用於非小細胞肺癌、胃癌、胰臟癌與大腸癌的惡病質，美國與歐盟未核准；TFDA 2026-10-27 的資料未見，不要告訴病人「可以處方」（Wakabayashi et al., 2021）。

### 7.9 血糖：胰源性（3c 型）糖尿病與化療期間

**這一小節的結論先講：** 胰臟癌病人 47% 有糖尿病，而且大多是 2 年內新發，胰十二指腸切除後會緩解的比例也很高（Pannala et al., 2008，見 [1.2](#12-危險因子)）；它不是單純的第二型糖尿病，而是 3c 型：胰島素和升糖素**兩個都少**，血糖「忽高忽低」，低血糖風險高，常常還合併胰酵素不足，往往需要胰島素（Hart et al., 2016）。化療這邊再加上 dexamethasone 使血糖升高、噁心嘔吐吃不下使血糖掉下來，所以每個化療週期都要把血糖當成一項生命徵象。

> [!TIP]
> **3c 型糖尿病的「油門」和「剎車」都壞了**
> 胰島素像降血糖的剎車，升糖素像升血糖的油門。第二型糖尿病多半是剎車變鈍；3c 型是剎車和油門一起失靈，所以車速忽快忽慢，吃得少或吃得多都會出問題，低血糖也比較難靠自身反調節救回來。（教學簡化，機轉見 Hart et al., 2016。）

| 情境 | 風險 | 專師做什麼 |
|------|------|-----------|
| 化療日使用 dexamethasone | 血糖升高；corticosteroid 是高血糖高滲透壓狀態（HHS）的常見誘因之一（Umpierrez et al., 2024） | 化療前、當天與之後幾天測血糖；已用胰島素者事先和主治醫師、糖尿病團隊約好調整方式；低致吐方案可與主治醫師討論是否改用非類固醇止吐 |
| 化療後噁心、嘔吐、吃不下 | 胰島素照常打會低血糖；SGLT2 抑制劑會在進食減少時誘發酮酸中毒 | 事先訂「吃不下的日子」計畫：哪些藥停、哪些減、什麼數字要打電話（見下方警示） |
| 胰酵素不足，或沒有隨餐吃 | 吸收不穩，血糖忽高忽低 | 先把 PERT 做好（[7.7](#77-胰酵素替代治療的病房流程)）；PERT 與血糖管理要一起評估（Hart et al., 2016） |
| 胰臟切除術後 | 新發或惡化的糖尿病；常需要胰島素（Hart et al., 2016） | 出院前教血糖自我監測與低血糖處置；會診糖尿病團隊 |
| 口服藥 | metformin 在可行時是合理的選擇（Hart et al., 2016）；口服降血糖藥的效果有限，特別是合併外分泌不全時（Wang & Jiao, 2025） | 是否用 metformin 依腎功能、嘔吐與腹瀉、造影劑使用與主治醫師及藥師評估 |
| 免疫檢查點抑制劑（少數 MSI-H 病人） | 免疫相關糖尿病，可快速進入酮酸中毒 | 見 [irAE](00-shared/04-irae.md#58-免疫治療相關糖尿病)第 5.8 節 |

> [!WARNING]
> **化療期間吃不下時，SGLT2 抑制劑要先停**
> ADA/EASD 等學會的共識指出，SGLT2 抑制劑是現今 euglycemic DKA（血糖低於 200 mg/dL 的酮酸中毒）的主要原因，進食減少與急性疾病都是誘因，可用「病假日規則（sick day rules）」預防；入院時應停用（Umpierrez et al., 2024）。血糖不高，不代表沒有酮酸中毒：吃不下、嘔吐、呼吸深快（Kussmaul 呼吸）的病人，要驗酮體。

> [!CAUTION]
> **待核對：胰臟癌化療病人的血糖目標與用藥**
> 本手冊沒有取得專為胰臟癌化療病人訂定的血糖目標與胰島素調整規則，也沒有核對 ADA 2026 年版標準的全文（本小節的低血糖分級取自 ADA 2024 年版標準的第 6 節，見 [8.6](#86-低血糖與高血糖危象)）。目標值（要鬆還是要緊）要依預期存活、低血糖風險與病人意願，由主治醫師與糖尿病團隊決定。

### 7.10 血栓：預防與處置

**這一小節的結論先講：** 胰臟癌在 Khorana 分數的部位項目就占 2 分，加上任何一個其他項目就達到 3 分（高風險）；但亞洲（含台灣）的資料顯示 VTE 發生率比西方低，Pan-Asian ESMO 因此把常規預防性抗凝血降為「無禁忌時可以考慮」。決定要不要預防，不是看一個分數，而是看血栓風險、出血風險（特別是腫瘤侵犯胃或十二指腸）與藥物交互作用三件事。通用的 Khorana 表與治療見[支持性照護](00-shared/03-supportive-care.md#7-癌症相關靜脈血栓vte)第 7 節。

**算一次 Khorana 分數**：胰臟癌 2 分；血小板 ≥350,000/µL 加 1 分；Hb <10 g/dL 或使用 ESA 加 1 分；白血球 >11,000/µL 加 1 分；BMI ≥35 kg/m² 加 1 分（Khorana et al., 2008）。例：胰臟癌（2）＋ 血小板 380,000/µL（1）＝ 3 分，高風險；胰臟癌（2）＋ Hb 12.5、WBC 8,000、血小板 240,000、BMI 22 ＝ 2 分，達到試驗納入的門檻（≥2）。

| 證據 | 族群與用法 | 結果 |
|------|-----------|------|
| CASSINI（Khorana et al., 2019） | Khorana ≥2 的門診化療病人；rivaroxaban 10 mg 每日一次 | 180 天主要指標未達顯著（6.0% 對 8.8%，HR 0.66，P = .10）；用藥期間 VTE 2.6% 對 6.4%（HR 0.40） |
| CASSINI 胰臟亞群（Vadhan-Raj et al., 2020；n = 273） | 同上 | 180 天主要指標 9.6% 對 13.0%（HR 0.70，0.34–1.43，P = .328），**未達顯著**；用藥期間 3.7% 對 10.1%（HR 0.35，0.13–0.97，P = .034）；主要出血 1.5% 對 2.3%；篩檢時已有 6.6%（24／362）發生 VTE，沒有被隨機分派 |
| AVERT（Carrier et al., 2019） | Khorana ≥2；apixaban 2.5 mg 每日兩次 | VTE 4.2% 對 10.2%（HR 0.41）；主要出血 3.5% 對 1.8%（非胰臟專屬族群） |
| 台灣 4 家醫院（Chen et al., 2018） | 838 位接受姑息化療的胰臟癌病人 | VTE 8.0%（67／838，中位追蹤 7.7 個月）；獨立預測因子是白血球 >11,000/µL 與肝轉移；**化療開始後 1.5 個月內發生的早發 VTE 是不良預後因子** |
| Pan-Asian ESMO 2025（Tai et al., 2025，建議 6b） | 台灣腫瘤醫學會參與表決 | 因亞洲 VTE 發生率較低、預防未顯示存活獲益，降為「無禁忌時可以考慮」[I, C]；日本全國登錄 1,006 位病人中，胰臟癌的出血風險是所有癌別中最高（對大腸癌的 HR 3.88，2.11–7.14） |
| ASCO 2023 指引（Key et al., 2023） | Khorana ≥2 的高風險門診病人 | 評估出血風險後，可考慮 apixaban、rivaroxaban 或 LMWH 預防 |

**實務步驟**

1. 化療前算 Khorana，並**先看基線影像有沒有已經存在的血栓**（CASSINI 的胰臟病人有 6.6% 篩檢時就有 VTE）。
2. 決定預防前先列出出血風險：血小板低下、肝轉移與凝血異常、腫瘤是否侵犯胃或十二指腸、近期出血、預定的侵入性處置（如支架、穿刺）。
3. 治療已發生的 VTE：NCCN 病人版以 LMWH 優於 warfarin；只有在胰臟腫瘤沒有長進胃或腸腔時才可用 DOAC（NCCN, 2026，病人版）；ASCO 2023 將 apixaban 列為治療的有力選項（Key et al., 2023）。
4. 開始前確認交互作用：capecitabine、5-FU 合併 warfarin 要密切監測 INR，oxaliplatin 合併口服抗凝血藥要更頻繁監測出血（[6.7](#67-胰臟癌病人特有的判讀情境)）；olaparib 仿單另有 VTE 警語（[6.6](#66-olaparib)）。
5. 血小板低下時的抗凝血調整見[支持性照護](00-shared/03-supportive-care.md#73-治療)第 7.3 節。

**健保：** DOAC 治療 DVT／PE 的條文是 2.1.4.2 第 3 項（rivaroxaban，本條最新修訂 115/10/1）、2.1.4.3 第 2 項（apixaban，本條最新修訂 111/2/1）、2.1.4.4 第 2 項（edoxaban，本條最新修訂 111/2/1），都須經影像學或血管超音波診斷、沒有癌症專屬條件；依 Khorana 分數的癌症門診預防性抗凝，在這三條原文未見（詳見[支持性照護](00-shared/03-supportive-care.md#74-健保給付doac-治療-dvtpe)第 7.4 節）。

> [!WARNING]
> **抗凝血藥不要加在「還沒查清楚的出血風險」上**
> 胰臟癌病人同時有血小板可能偏低、膽道支架、腫瘤侵犯十二指腸或胃的出血風險；開始 DOAC 或 LMWH 之前，要先看血小板、凝血功能、近期有無黑便或吐血，並由主治醫師決定。已在抗凝血的病人新出現黑便、吐血或引流管出血，立刻通知醫師，並暫停下一劑直到醫師評估（[8.3](#83-消化道出血與假性動脈瘤)）。

### 7.11 疼痛與 celiac plexus neurolysis

胰臟癌的疼痛在 50% 至 70% 的病人很嚴重，而且常難以處理（Arcidiacono et al., 2011）。通用的評估、鴉片類換算、突發痛劑量與副作用處置見[支持性照護](00-shared/03-supportive-care.md#3-癌症疼痛)第 3 節；胰臟癌特別的是三件事。

1. **疼痛的原因不只腫瘤。** 新出現或突然惡化的疼痛要先排除膽管炎、胃出口阻塞、惡性腸阻塞、胰臟炎、出血與穿孔（[第 8 段](#8-腫瘤急症胰臟癌相關)），不要只加鴉片類劑量。
2. **便祕和腹瀉的方向相反，要看藥單。** 鴉片類一定同時開軟便劑；一旦開始 irinotecan 之後拉肚子，要先停軟便劑（[7.1](#71-每次化療前檢核)）。
3. **腹腔神經叢（celiac plexus）阻斷是輔助，不是替代。** 內臟痛在胰臟癌常見，神經溶解術（neurolysis）可降低疼痛；能不能減少鴉片類用量與副作用，各試驗結果不一致（見下表）。

| 證據 | 設計 | 結果 |
|------|------|------|
| Wong et al., 2004 | 無法切除胰臟癌，n = 100，雙盲；經皮 celiac plexus 阻斷（NCPB）對 sham ＋ 最佳化止痛藥 | 前 6 週有中重度疼痛（≥5/10）的病人 14% 對 40%（P = .005）；鴉片類用量（P = .93）、鴉片類副作用、生活品質（P = .46）與存活（P = .26）**沒有差異** |
| Wyse et al., 2011 | 新診斷、有疼痛的無法切除胰臟癌，n = 96；診斷性 EUS 當下做 EUS-CPN 對一般止痛處置 | 3 個月時疼痛改善較多（平均百分比變化差 −60.7，95% CI −86.6 至 −25.5，P = .01）；嗎啡用量 3 個月時有降低趨勢（P = .10）；生活品質與存活無差異 |
| Cochrane（Arcidiacono et al., 2011） | 6 項隨機試驗、358 人（經皮方式） | 4 週時疼痛 VAS 平均差 −0.42（−0.70 至 −0.13）；鴉片類用量顯著較低；作者認為不良反應比鴉片類少是對病人很重要的好處 |

護理重點（臨床提醒）：術後短暫的低血壓與腹瀉可以預期，術後要監測血壓。照會時機是口服與鴉片類最佳化後疼痛仍控制不好，或鴉片類副作用難以忍受時；新診斷、已經有疼痛的病人，也可以考慮在診斷性 EUS 當下就做（Wyse et al., 2011）。生活品質與存活都沒有因為神經溶解而改變，所以要跟病人說清楚：目的是少痛、少吃藥，不是延長壽命。

> [!WARNING]
> **鴉片類的三個陷阱（胰臟癌病人特別常見）**
> 1. 腎功能不全或脫水時，morphine 與 codeine 的活性代謝物會蓄積，優先考慮 fentanyl 等較不依賴腎臟排除的藥物；2. fentanyl 貼片只用於已耐受鴉片類的病人，不可當第一個鴉片類，也不用於需要快速調整的疼痛；3. 開始鴉片類就同時開預防性軟便劑，但 irinotecan 腹瀉時要先停（以上見[支持性照護](00-shared/03-supportive-care.md#34-副作用處置)第 3.4 節與 [6.2](#62-irinotecan-與脂質體-irinotecan)）。

### 7.12 緩和照護的整合

**這一小節的結論先講：** 晚期胰臟癌病人應該在診斷後早期就同時接受緩和照護。隨機試驗（Maltoni et al., 2016）：207 位門診的轉移性或無法切除的局部晚期胰臟癌病人，「系統性早期緩和照護」對「需要時才照會」，12 週時 FACT-Hep 試驗結果指標（TOI）的組間差 3.83 分（95% CI 0.10–7.57，P = .041），肝癌子量表差 2.51 分（0.40–4.61，P = .013），整體存活沒有差異。ASCO 2017 指引建議晚期癌症病人在診斷後早期（建議 8 週內）就合併專業緩和照護（Ferrell et al., 2017）。台灣的法規與共同照護脈絡見[支持性照護](00-shared/03-supportive-care.md#9-早期緩和照護)第 9 節。

| 什麼時候特別要照會或加強 | 為什麼 |
|--------------------------|--------|
| 剛診斷為轉移性或局部晚期 | 與積極治療同步，不是二選一（Ferrell et al., 2017） |
| 疼痛需要多層次處置（鴉片類輪替、神經溶解術） | 見 [7.11](#711-疼痛與-celiac-plexus-neurolysis) |
| 胃出口阻塞、惡性腸阻塞等需要依預後與病人意願選擇處置時 | 症狀處置應由多專科團隊，並及早評估預後與病人意願（Acharya et al., 2026） |
| ECOG 明顯下降、換線後獲益有限 | 需要重新談目標；台灣長表資料中，≥70 歲只做緩和照護的比例是 26.3%（[1.1](#11-台灣現況)） |
| 病人或家屬問 DNR、預立醫療照護諮商或預立醫療決定 | 《安寧緩和醫療條例》與《病人自主權利法》，見共用章 |

> [!NOTE]
> **照會流程依院內規範**
> 緩和共同照護團隊的照會條件、門診是否有緩和療護門診、居家安寧的銜接與健保給付方式，各院不同；本表是時機的提醒，不是照會標準。

### 7.13 胰臟切除術後病房：常見併發症（ISGPS 定義）

輔助化療的病人是從外科病房轉過來的；了解國際胰臟外科研究小組（International Study Group of Pancreatic Surgery, ISGPS）的定義，才聽得懂外科的交班，也才知道什麼徵象要立刻通知。

| 併發症 | 定義與分級 | 護理線索 |
|--------|-----------|---------|
| 術後胰漏（postoperative pancreatic fistula, POPF；ISGPS 2016） | 引流液**任何可測量的量**、amylase **>3 倍**該院血清 amylase 正常上限，**且**有臨床上相關的狀況。舊的 A 級現稱 biochemical leak，不再算胰漏。B 級：術後處置有改變，引流管留置 >3 週，或需內視鏡、經皮重新放置；C 級：需要再手術、單一或多重器官衰竭，或死亡與胰漏有關（Bassi et al., 2017） | 引流液顏色與量依排程記錄，amylase 依外科時程送；發燒、腹痛、引流液混濁要通知 |
| 胃排空延遲（delayed gastric emptying, DGE；ISGPS 2007） | 術後第一週結束時，無法恢復標準飲食，包括鼻胃管留置時間延長；依臨床影響分 A、B、C 級（Wente et al., 2007a） | 噁心、嘔吐、早飽、鼻胃管引流量多；與腫瘤復發造成的胃出口阻塞要分開（[8.2](#82-胃出口阻塞)） |
| 術後出血（post-pancreatectomy hemorrhage, PPH；ISGPS 2007） | 依**發生時間**（早期 ≤24 小時、晚期 >24 小時）、**位置**（腔內、腔外）與**嚴重度**（輕、重）分級（Wente et al., 2007b） | 引流管出現血性液體、嘔血或黑便、心跳加快、血壓下降；**前哨出血（sentinel bleed）**後可能接著大出血（[8.3](#83-消化道出血與假性動脈瘤)） |
| 乳糜漏（chyle leak；ISGPS 2017） | 術後第 3 天或之後，引流液、引流口或傷口出現**乳白色**液體，且三酸甘油酯 **≥110 mg/dL（≥1.2 mmol/L）**；高達 10% 的胰臟切除會發生。A 級：只需口服飲食限制；B 級：住院延長、鼻腸管營養加飲食限制、全靜脈營養、octreotide，或保留或新增引流管；C 級：更侵入性的住院處置、加護病房或死亡（Besselink et al., 2017） | 引流液變乳白色 → 通知外科並送三酸甘油酯 |

**預防胰漏的藥物與台灣狀態：** 單中心隨機試驗（n = 300）在手術當天早上開始給 pasireotide 900 µg 皮下注射每日兩次、共 7 天（14 劑），3 級以上的胰漏、leak 或膿瘍為 9% 對 21%（RR 0.44，0.24–0.78，P = .006）（Allen et al., 2014）。pasireotide（Signifor）在台灣的藥證只有庫欣氏病，用於預防胰漏屬適應症外；octreotide（Sandostatin 及學名藥）的台灣適應症明確包括「預防胰臟手術後的併發症」（TFDA 2026-10-27 資料）。健保：5.4.3 octreotide 注射劑（87/11/1、102/1/1）第 2 點「預防胰臟手術後的併發症，最長使用七天」；5.4.5 somatostatin（87/11/1、89/5/1）第 1 點「預防胰臟手術後的併發症，最長使用五天」。

術後的糖尿病與胰酵素不足也要接著處理：見 [7.9](#79-血糖胰源性3c-型糖尿病與化療期間) 與 [7.7](#77-胰酵素替代治療的病房流程)。

> [!CAUTION]
> **待核對：ISGPS 定義裡只在二手文獻看到的細節**
> 以下只見於二手來源，未在 ISGPS 原文確認：（1）POPF 的「術後第 3 天或之後」時間條件；（2）DGE 各級的天數門檻（A 級為術後第 7 天仍無法吃固體食物、B 級第 14 天、C 級第 21 天的說法，取自 Jiménez-Romero et al., 2025 對 ISGPS 的轉述）；（3）PPH C 級與栓塞、內視鏡或再手術的關係。POPF 的 2016 年定義另有 2024 年更正（*Surgery*, 176(3), 988–989），本手冊未讀到更正內容。臨床分級以外科團隊為準。

### 7.14 療效評估與追蹤時程

**這一小節的結論先講：** 胰臟癌的追蹤分三個階段，用的工具不一樣：（1）**術後輔助期**：每個週期的臨床與抽血評估，不是影像；（2）**轉移性或局部晚期的治療期**：影像（RECIST 1.1）加 CA19-9 趨勢加臨床；（3）**輔助結束後的追蹤**：病史與身體檢查、CA19-9、影像，每 3–6 個月一次的做法來自 NCCN 與 ASCO，但證據等級低、對存活的影響仍有爭議。

| 階段 | 做什麼 | 依據與備註 |
|------|--------|-----------|
| 治療前基線 | 對比增強的胸腹骨盆 CT；CA19-9（膽紅素下降後再抽）；體重、ECOG、神經學、血糖、糞便性質 | 輔助治療前要有胸腹骨盆對比增強 CT 與 CA19-9（NCCN, 2026，病人版）；基準值的時機見 [3.4](#34-ca19-9) |
| 輔助治療期間（mFOLFIRINOX 12 次） | 每個週期前：CBC、肝腎功能、體重、神經、腹瀉、血糖（[7.1](#71-每次化療前檢核)）；CA19-9 的頻率依主治醫師 | 總療程最多 6 個月，包括術前的週期（NCCN, 2026，病人版） |
| 轉移性或局部晚期治療期間 | 臨床評估每個週期；影像用 RECIST 1.1，NAPOLI 3 是基線後每 8 週一次；CA19-9 看趨勢，不看單一數值 | 影像間隔取自試驗的設計（Ipsen, n.d.），不是指引的規定；局部晚期是否可手術每 2–3 個月由 MDT 重評（[4.7](#47-局部晚期locally-advanced)） |
| 維持治療 olaparib | CBC 基線，之後每月 | AstraZeneca, 2025（[6.6](#66-olaparib)） |
| 輔助結束後的追蹤 | 病史與身體檢查、CA19-9、胸部 CT、腹部骨盆對比增強 CT 或 MRI；另追蹤血糖、胰酵素不足與體重 | 前四項是 NCCN 病人版列的項目（間隔見下方待核對說明）；血糖、胰酵素與體重是本手冊依 7.7–7.9 加上的 |

RECIST 1.1 的 CR、PR、SD、PD 定義見[肺癌章 7.6](01-lung-cancer.md#76-療效評估與追蹤)。

**輔助結束後要不要常規影像追蹤，證據兩邊都有。**

- NCCN 與 ASCO 2017 的做法（引自台大醫院 2019 年的描述）：病史與身體檢查、CA19-9 與腹部骨盆 CT，每 3–6 個月一次、共 2 年，之後每年一次；其中 CA19-9 與 CT 是 NCCN 2B 類證據（Wu et al., 2019）。
- 支持者：荷蘭 E-AHPBA 前瞻性橫斷研究（33 個中心，333 位復發病人）：常規影像追蹤組 28 個月，症狀追蹤組 23 個月（P = .01）；調整後 HR 0.75（0.56–0.99），也較常接受針對復發的治療（調整後 OR 2.57，1.22–5.41），但屬觀察性研究（Andel et al., 2025）。Pan-Asian ESMO 因此把「定期追蹤」建議升為 [III, B]（Tai et al., 2025，建議 6a）。
- 保留者：台大醫院 2000–2013 年、181 位有記錄復發的病人，追蹤型態（僅症狀、影像、標記、兩者並用）的中位 OS 分別是 21.4、13.9、20.5、16.5 個月（P = .670），密集追蹤不是 OS 的獨立因子；回溯性且年代較早（Wu et al., 2019）。

> [!CAUTION]
> **待核對：現行 NCCN 的追蹤間隔**
> 上面「每 3–6 個月、共 2 年，之後每年」是 2019 年文獻對 NCCN 與 ASCO 的轉述；NCCN 專業版 v4.2026 無法開啟，間隔與年限可能已改版。NCCN 病人版（2026）只寫追蹤包括病史與身體檢查、CA19-9、胸部 CT、腹部骨盆對比增強 CT 或 MRI「視需要」，未寫間隔。實際排程以主治醫師與院內規範為準。

> [!IMPORTANT]
> **CA19-9 追蹤的四個提醒**
> 1. 基準值要在**膽紅素下降後**抽；黃疸、膽管炎都會讓 CA19-9 偽陽性（[3.4](#34-ca19-9)）。
> 2. 治療後下降 ≥20–50% 預測存活較長（Ballehaninna & Chamberlain, 2012）；但單一數值不能單獨下結論，要看趨勢，並與影像、臨床合讀。
> 3. 數值升高時，先查膽道有沒有堵、有沒有膽管炎，再談是不是進展。
> 4. Lewis-negative 的病人基準值就是零或接近零：追蹤靠影像與 CEA、CA-125，不是 CA19-9。

**長期追蹤另外要顧的**：germline 變異陽性的病人，家人的 cascade testing 與監測（[1.5](#15-germline-檢測與台灣資料)）；術後或化療後的新發糖尿病與胰酵素不足（7.7、7.9）；體重與營養（7.8）；心理困擾與緩和照護（7.12）。

---

## 8. 腫瘤急症（胰臟癌相關）

通用的發燒性嗜中性球低下、輸注反應與過敏性休克、惡性腸阻塞等，見[腫瘤急症章](00-shared/02-oncologic-emergencies.md)（本段 8.7 列出連結與胰臟癌的提醒）。以下是胰臟癌特別常見的六類：多半是**胰頭腫瘤的位置**（緊貼膽管、十二指腸、門靜脈與腸繫膜血管）加上**胰臟本身的內分泌與外分泌功能**所造成。

| 急症 | 為什麼胰臟癌常見 | 辨識 | 第一小時處置 |
|------|----------------|------|-------------|
| 急性膽管炎（[8.1](#81-急性膽管炎acute-cholangitis)） | 胰頭腫瘤堵住遠端膽管；塑膠支架約 3 個月就會堵塞；化療使免疫力下降；nab-paclitaxel 仿單把膽道阻塞與支架列為致命敗血症的危險因子 | 發燒、黃疸、右上腹痛（Charcot 三聯徵）；再加低血壓與意識改變（Reynolds 五聯徵）已是 Grade III；化療或類固醇中的病人可能不發燒 | 生命徵象；**血液培養 ≥2 套（含 port）後立即抗生素**；補液；CBC、肝功能、乳酸、肌酸酐、INR；通知消化內科或介入放射科評估引流；暫停化療；同時是嗜中性球低下就走 FN 流程 |
| 胃出口阻塞（[8.2](#82-胃出口阻塞)） | 十二指腸緊貼胰頭與鉤突，腫瘤壓迫或侵犯；惡性胃出口阻塞主要見於晚期胰臟癌與胃癌 | 吃了就吐、早飽、脫水、體重驟降；與化療噁心、術後胃排空延遲要分開 | 禁食；補液與電解質；急性阻塞又無法立即做內視鏡時，鼻胃管減壓；通知主治醫師；評估是否同時有膽道阻塞；暫停含 irinotecan 的處方待評估 |
| 消化道出血與假性動脈瘤（[8.3](#83-消化道出血與假性動脈瘤)） | 腫瘤侵犯十二指腸、胃或血管；胰臟切除後的胃十二指腸動脈殘端假性動脈瘤（常在胰漏之後）；抗凝血藥與血小板低下；脾靜脈阻塞造成胃靜脈曲張 | 嘔血、黑便、引流管出現血性液體；**前哨出血**；心跳快、血壓降、Hb 掉 | 兩條大管徑靜脈通路、血型交叉、CBC 與凝血；禁食；靜脈 PPI；血流動力學穩定時以 Hb <7 g/dL 為輸血門檻，不穩定時立即通知醫師、依臨床判斷；暫停抗凝血藥；內視鏡 24 小時內；疑似術後出血或假性動脈瘤 → 緊急 CT 血管攝影與介入 |
| 門靜脈、脾靜脈與腸繫膜靜脈血栓（[8.4](#84-門靜脈脾靜脈與腸繫膜靜脈血栓)） | 腫瘤壓迫或侵犯 SMV、門靜脈與脾靜脈；胰臟癌本身是高凝血狀態 | 腹痛、腹脹、腹水，也可能完全無症狀、由影像偶然發現；脾靜脈阻塞可造成胃靜脈曲張出血 | 對比增強 CT 確認；通知主治醫師；先評估出血風險（血小板、凝血、曲張靜脈、腫瘤是否侵犯胃腸），再由主治醫師決定抗凝血 |
| 無法控制的疼痛（[8.5](#85-無法控制的疼痛)） | 腫瘤侵犯腹腔神經叢與後腹腔神經；胰臟癌疼痛在 50% 至 70% 的病人很嚴重 | 疼痛比平時明顯惡化或 NRS ≥7；先想有沒有新的原因（膽管炎、阻塞、穿孔、出血） | 評估與排除新原因；依院內流程快速調整鴉片類（突發痛劑量為每日總量的 10–20%）；輔助藥；會診疼痛或緩和團隊；之後考慮神經溶解術 |
| 低血糖與高血糖危象（[8.6](#86-低血糖與高血糖危象)） | 3c 型糖尿病血糖不穩、低血糖風險高；dexamethasone 使血糖升高；嘔吐吃不下；SGLT2 抑制劑 | 低血糖：冒冷汗、發抖、意識改變。DKA／HHS：噁心嘔吐、腹痛、脫水、呼吸深快、意識改變 | 立刻測指尖血糖；低血糖依分級處置（約 15 g 速效醣類，15 分鐘後再測）；高血糖危象驗酮體、電解質與血氣，補液、補鉀、靜脈胰島素，並找誘因（感染、類固醇、SGLT2 抑制劑） |

> [!IMPORTANT]
> **胰臟癌急症的共同原則**
> 1. 胰頭腫瘤的急症常常**同時發生**：膽管炎合併嗜中性球低下、胃出口阻塞合併膽道阻塞、血栓合併出血風險。第一小時不要只處理一件事。
> 2. 抗生素**不能取代引流**：膽管炎 Grade II 以上需要早期引流（Miura et al., 2018）。
> 3. 暫停化療的原則：嚴重感染、出血、腸阻塞、膽紅素高於仿單門檻時先暫停，恢復後再依 [5.7](#57-肝腎功能與膽紅素門檻速查) 與 [6.8](#68-暫停與永久停藥條件速查) 的條件重啟。

### 8.1 急性膽管炎（acute cholangitis）

**診斷：TG18 三組條件**（Kiriyama et al., 2018）

| 組別 | 內容 |
|------|------|
| A 全身性發炎 | 發燒（>38°C）和（或）寒顫；白血球 <4,000 或 >10,000/mm³，和（或）CRP ≥1 mg/dL |
| B 膽汁淤積 | 黃疸（總膽紅素 ≥2 mg/dL）；ALP、γGT、AST、ALT 任一 >1.5 × ULN |
| C 影像 | 膽管擴張；病因的影像證據（狹窄、結石、支架等） |

三組各至少一項為**確定診斷**。但臨床上懷疑緊急時，TG18 的初始處置是**不等確定診斷就先開始**呼吸循環支持與經驗性治療（Miura et al., 2018）。胰臟癌病人有支架或膽道阻塞史，C 組本來就容易符合，因此發燒加膽紅素或 ALP 上升就要當成膽管炎處理。

**嚴重度與引流時機**（Kiriyama et al., 2018；Miura et al., 2018）

| 分級 | 條件 | 處置 |
|------|------|------|
| Grade I（輕度） | 不符合 II 或 III | 多數只需抗生素等初始治療；對初始治療無反應才考慮引流 |
| Grade II（中度） | 下列任兩項：白血球 >12,000 或 <4,000/µL；發燒 ≥39°C；年齡 ≥75 歲；總膽紅素 ≥5 mg/dL；白蛋白 <正常下限 × 0.7 | **早期**內視鏡或經皮經肝膽道引流 |
| Grade III（重度） | 新發的器官功能障礙，任一系統：心血管（需 dopamine ≥5 µg/kg/min 或任何劑量 norepinephrine）；神經（意識障礙）；呼吸（PaO₂/FiO₂ <300）；腎（少尿、肌酸酐 >2.0 mg/dL）；肝（PT-INR >1.5）；血液（血小板 <100,000/mm³） | 呼吸循環支持；病情穩定後**盡快**引流 |

- **證據**：TG13／TG18 的大型個案系列（日本與台灣）顯示，Grade II 病人接受早期或緊急引流的 30 天死亡率顯著較低，Grade I 與 III 則沒有差異（Kiriyama et al., 2018）。長庚林口的回溯性研究（683 位符合確定診斷者）中，ERCP 在 48 小時內做的 Grade III 病人 30 天死亡率 0 對 6.1%（Huang et al., 2022；回溯性）。
- **抗生素**：TG18 依嚴重度與感染來源（社區或醫療照護相關）列出經驗性用藥，要依培養結果降階，並參考當地抗藥性資料；用藥天數也已系統性回顧（Gomi et al., 2018）。院內有 FN 流程的病人，依院內抗生素政策（[腫瘤急症](00-shared/02-oncologic-emergencies.md#15-專師該開的-order範例)第 1.5 節）。
- **引流方式**：堵塞的支架要更換或另置，由消化內科或介入放射科決定內視鏡或經皮；之後支架的選擇見 [3.5](#35-膽道阻塞什麼時候要引流)。
- **化療**：感染控制、膽紅素回到各藥門檻內（[5.7](#57-肝腎功能與膽紅素門檻速查)）才重啟。

> [!WARNING]
> **沒有發燒也可能是膽管炎**
> 正在使用類固醇（如化療用的 dexamethasone）、高齡或嗜中性球低下的病人，感染時可能只表現為低血壓、意識改變或倦怠（[腫瘤急症](00-shared/02-oncologic-emergencies.md#11-辨識)第 1.1 節）。化療期間出現黃疸復發、右上腹痛、寒顫、血壓偏低或意識變差，即使體溫正常，也先抽血液培養與肝功能，並通知醫師。

### 8.2 胃出口阻塞

**這一小節的結論先講：** 胃出口阻塞（gastric outlet obstruction, GOO）是胰頭腫瘤壓住十二指腸，吃進去的東西過不去；惡性 GOO 主要見於晚期胰臟癌與胃癌，病人常有難以控制的嘔吐與嚴重營養不良，會進一步削弱接受治療的能力（Troncone et al., 2020）。第一小時先「減壓、補水、查電解質」，再找內視鏡或手術的出路。

- **辨識**：吃了就吐、早飽、脫水、體重驟降；要分開的是化療的噁心嘔吐、術後胃排空延遲（[7.13](#713-胰臟切除術後病房常見併發症isgps-定義)）、惡性腸阻塞（[腫瘤急症](00-shared/02-oncologic-emergencies.md#11-惡性腸阻塞與嗜中性球低下性小腸結腸炎)第 11 節）。
- **第一小時**：禁食、靜脈補液並追蹤電解質；急性阻塞且內視鏡一時無法進行時，可用鼻胃管或造瘻管減壓，但**不要長期留置鼻胃管**（Acharya et al., 2026）。評估是否同時有膽道阻塞，並通知主治醫師與消化內科。
- **症狀藥物**：鴉片類、止吐藥與抗分泌藥常用，但在 GOO 的療效證據有限；應由多專科團隊及早評估預後與病人意願，並做營養評估（Acharya et al., 2026）。
- **口服藥吐出來怎麼辦**：capecitabine 漏服或吐出都不補（H2-Pharma, 2026）；需要口服的 S-1 與 olaparib 在無法進食時也要通知主治醫師，不要自行調整。
- **化療**：irinotecan 與 Onivyde 在腸阻塞時不可給（Pharmacia & Upjohn, 2026；Ipsen, 2025）；GOO 時是否適用、何時重啟，由主治醫師決定。

**確定性處置**：

| 選項 | 特性 | 證據 |
|------|------|------|
| 十二指腸金屬支架（SEMS） | 症狀緩解較快，但晚期再阻塞與再介入較多；預期存活 <2 個月較適合 | SUSTENT 隨機試驗：症狀緩解的中位時間，支架 5 天、手術 8 天（Jeurnink et al., 2010） |
| 胃空腸吻合術（手術） | 長期緩解較好；預期存活 ≥2 個月較適合 | 同上 |
| EUS 導引胃腸吻合術（EUS-GE） | 專家中心的選項；6 個月再介入率 4% 對 29%（DRA-GOO，n = 97），不良事件相近 | Teoh et al., 2025；van der Merwe et al., 2022 |

Pan-Asian ESMO 建議金屬支架優於手術處理十二指腸阻塞，並在有專長的中心納入 EUS-GE（Tai et al., 2025，建議 6d）。

> [!TIP]
> **十二指腸像被踩住的水管**
> 胰頭腫瘤像一隻腳踩在連接胃和小腸的水管上，水過不去，所以吃下去的東西往回吐。支架是把水管撐開的彈簧，見效快，但腫瘤長進來又會再堵；胃空腸吻合術與 EUS-GE 是另外接一條旁路，繞過被踩住的地方。（教學簡化。）

### 8.3 消化道出血與假性動脈瘤

**這一小節的結論先講：** 胰臟癌病人的出血有三條路：（1）腫瘤或潰瘍造成的**上消化道出血**；（2）**胰臟切除後的動脈出血**，多半來自胰漏之後的假性動脈瘤（常見於胃十二指腸動脈殘端），大出血前常有一次小量的**前哨出血**；（3）脾靜脈阻塞造成左側門脈高壓、**胃靜脈曲張**出血。三者處置不同，所以第一個問題是：病人有沒有開過刀、腫瘤是否侵犯十二指腸或胃、有沒有脾靜脈阻塞。

| 出血來源 | 數字與特性 | 處置 |
|---------|-----------|------|
| 上消化道出血（腫瘤、潰瘍、藥物） | ACG 2021：住院病人輸血門檻 7 g/dL；內視鏡前可給 erythromycin；內視鏡在到院後 24 小時內；止血後高劑量 PPI 3 天，再改每日兩次口服 PPI 到第 2 週（Laine et al., 2021） | 內視鏡止血失敗時，建議經導管栓塞（Laine et al., 2021）；輸血與血小板見[支持性照護](00-shared/03-supportive-care.md#10-化療相關貧血血小板低下與輸血)第 10 節 |
| 胰臟切除後的假性動脈瘤與動脈出血 | 單中心 1,102 位胰臟手術病人，假性動脈瘤出血 3.2%（35 位），其中 45.7% 先有前哨出血，74.3% 先有胰漏（Ding et al., 2011）；另一個系列：胰十二指腸切除後動脈出血 5.5%，中位發生在術後第 18 天，16 位中 12 位有胰漏、5 位有前哨出血（Kamada et al., 2021） | **血管內治療是第一線**：死亡率 10.0% 對手術 42.9%（Ding et al., 2011）；覆膜支架可同時止血並保留肝動脈血流（Kamada et al., 2021）；台北榮總系列，血管攝影陰性的前哨出血，預防性放置覆膜支架的 30 天死亡率 0（15 位），保守處置 40%（4／10；P = .02）（Lin et al., 2021；回溯性） |
| 胃靜脈曲張（左側門脈高壓） | 脾靜脈阻塞或結紮造成；胰十二指腸切除合併門脈匯流處切除的 118 位病人，6 個月時 37%（44 位）出現胃食道靜脈曲張，其中 5 位（11%）曲張破裂（Tanaka et al., 2019） | 內視鏡與消化內科處置；遠端胰臟癌造成的脾靜脈阻塞可引起左側門脈高壓與曲張靜脈出血（Zhao et al., 2024；病例報告），決定抗凝血前是否先評估曲張，由消化內科與主治醫師決定 |

**第一小時**

1. 評估血流動力學與意識；兩條大管徑靜脈通路；血型與交叉試驗、CBC、凝血功能、肌酸酐。
2. 禁食；靜脈 PPI；暫停抗凝血藥與抗血小板藥，由醫師決定是否逆轉。
3. 血流動力學穩定時 Hb <7 g/dL 才輸血，不穩定時不要等數值，立即通知醫師（[支持性照護](00-shared/03-supportive-care.md#102-紅血球輸血)第 10.2 節）。
4. 內視鏡由消化內科安排（24 小時內）；**術後病人或引流管有血、懷疑假性動脈瘤**，不要等內視鏡，直接聯絡外科與介入放射科做 CT 血管攝影。
5. 暫停化療，並通知主治醫師出血來源與血紅素趨勢。

> [!WARNING]
> **前哨出血：小量、自己停了，也要當急症**
> 胰臟手術後，引流管、嘔吐物或糞便出現少量鮮血、之後自己停止，可能是大出血的預兆；Ding 等人的系列有 45.7% 的假性動脈瘤出血先有前哨出血。台北榮總的回溯性資料中，血管攝影陰性但以保守方式處置的前哨出血，有 5 位日後發生延遲的大出血，2 位在 16 天內死於再出血（Lin et al., 2021）。護理上記錄顏色與量、保持靜脈通路、立刻通知，不要等下一次查房。

### 8.4 門靜脈、脾靜脈與腸繫膜靜脈血栓

**這一小節的結論先講：** 內臟靜脈血栓（splanchnic vein thrombosis, SVT）包括門靜脈、腸繫膜靜脈與脾靜脈血栓，和肝、胰、膽的癌症高度相關；症狀不典型，常被當成腫瘤本身，也可能完全沒有症狀、由分期或追蹤影像偶然發現。它的復發與出血風險都高，沒有隨機試驗，**抗凝血要個別決定**（Cohen et al., 2024）。

| 證據 | 內容 |
|------|------|
| 國際前瞻性登錄（Valeriani et al., 2021） | 132 位癌症合併 SVT 對 132 位一般部位 VTE：SVT 組以肝膽胰癌最多；12 個月復發性血栓 4.7% 對 5.5%，大出血 2.3% 對 4.7%，全因死亡 41.7% 對 39.4%；SVT 病人接受抗凝血的比例較低（68.9% 對 99.2%） |
| RIETE 登錄（Tufano et al., 2018） | 521 位 SVT（309 位偶然發現）：抗凝血期間 20 人症狀性復發、26 人大出血（5 人致命）；偶然發現與有症狀者的復發（調整後 HR 2.04，0.71–5.88）與大出血（HR 1.12，0.47–2.63）都沒有顯著差異；活動性癌症使復發風險上升（HR 3.06，1.14–8.17）；貧血與凝血時間異常使大出血風險上升 |
| 治療選擇 | 指引建議 LMWH 或 DOAC，DOAC 在這個族群的資料有限（Cohen et al., 2024）；NCCN 病人版：只有腫瘤沒有長進胃或腸腔時才可用 DOAC（NCCN, 2026，病人版） |

Tufano 等人（2018）寫道，當時的指引建議有症狀的 SVT 要抗凝血，偶然發現的則不常規抗凝血；但在癌症病人，兩者的復發與出血風險相似，且出血的嚴重度可能超過復發，因此要個別化。

**第一小時與之後**

1. 確認診斷：對比增強 CT（含門脈期）；記錄血栓位置（門靜脈、SMV、脾靜脈）與範圍。
2. 通知主治醫師；先評估出血風險：血小板、凝血功能、近期出血、膽道支架或預定侵入性處置、腫瘤是否侵犯胃或十二指腸，以及脾靜脈阻塞造成的胃靜脈曲張（[8.3](#83-消化道出血與假性動脈瘤)）。
3. 劇烈腹痛、腹脹、嘔吐、血便或乳酸升高時，要考慮腸繫膜缺血，立刻通知外科（臨床提醒）。
4. 抗凝血藥的種類、劑量與療程由主治醫師與血液科決定；一般 VTE 的用法與台灣 DOAC 健保條文見 [7.10](#710-血栓預防與處置)。

> [!NOTE]
> **偶然發現的血栓：誰來負責追蹤**
> 影像報告出現「門靜脈血栓」但病人沒有症狀時，專師的責任是把這份報告送到主治醫師手上、記錄在病歷，並在回診時確認有沒有做出抗凝血與否的決定；不要讓它停在報告系統裡。

### 8.5 無法控制的疼痛

**這一小節的結論先講：** 胰臟癌的疼痛在 50% 至 70% 的病人很嚴重（Arcidiacono et al., 2011），多半來自腫瘤侵犯腹腔神經叢與後腹腔神經。但**突然惡化的疼痛不要先加劑量，先找新的原因**；找完原因，才用鴉片類快速調整、輔助藥與神經溶解術。通用的鴉片類換算與副作用處置見[支持性照護](00-shared/03-supportive-care.md#3-癌症疼痛)第 3 節。

| 伴隨的線索 | 要先想到 | 見 |
|-----------|---------|-----|
| 發燒、黃疸、右上腹痛、寒顫 | 膽管炎、支架堵塞 | [8.1](#81-急性膽管炎acute-cholangitis) |
| 嘔吐、早飽、上腹脹痛 | 胃出口阻塞；惡性腸阻塞 | [8.2](#82-胃出口阻塞)；[腫瘤急症](00-shared/02-oncologic-emergencies.md#11-惡性腸阻塞與嗜中性球低下性小腸結腸炎)第 11 節 |
| 嘔血、黑便、引流管出血、心跳快血壓低 | 出血、假性動脈瘤 | [8.3](#83-消化道出血與假性動脈瘤) |
| 腹脹、腹水、劇烈腹痛合併乳酸升高 | 內臟靜脈血栓、腸繫膜缺血 | [8.4](#84-門靜脈脾靜脈與腸繫膜靜脈血栓) |
| 突然劇烈、腹部僵硬 | 消化道穿孔（臨床提醒） | 立即通知醫師，安排影像 |
| 新的背痛、骨頭痛 | 腫瘤進展、骨轉移 | 影像；骨轉移見[支持性照護](00-shared/03-supportive-care.md#8-骨轉移的骨骼保護劑bone-modifying-agents)第 8 節 |

**處置步驟**（依院內疼痛處置流程調整）

1. 用 NRS 與 OPQRST 評估，量生命徵象，並排除上表的原因；有新原因就先處理原因。
2. 鴉片類：突發痛劑量是每日鴉片類總量的 10–20%；每天需要 3–4 次以上突發痛劑量，就把前一天總量重新計算、提高長效劑量；腎功能不全時避免 morphine 與 codeine（[支持性照護](00-shared/03-supportive-care.md#32-處置原則esmo-2018nccn)第 3.2–3.4 節；Fallon et al., 2018）。
3. 輔助藥：神經病變性疼痛用 gabapentinoid 或 duloxetine；腫瘤壓迫水腫可用類固醇（同上；類固醇要同時顧血糖，見 [7.9](#79-血糖胰源性3c-型糖尿病與化療期間)）。
4. 同時開軟便劑；若正在 irinotecan 的腹瀉期則先停（[7.1](#71-每次化療前檢核)）。
5. 口服與鴉片類最佳化後仍痛，或副作用難忍：會診疼痛或麻醉科，考慮經皮或 EUS 導引的 celiac plexus 神經溶解術（[7.11](#711-疼痛與-celiac-plexus-neurolysis)）。
6. 會診緩和團隊（[7.12](#712-緩和照護的整合)）；紀錄疼痛分數的變化。

> [!WARNING]
> **新的腹痛，不要先用鴉片類把它蓋過去**
> 鴉片類會遮蔽腹部的理學檢查。胰臟癌病人新出現或突然惡化的腹痛，先排除膽管炎、阻塞、出血與穿孔，再調鴉片類；調藥後依院內流程重新評估疼痛與生命徵象，確認不是併發症在惡化。

### 8.6 低血糖與高血糖危象

**這一小節的結論先講：** 胰臟癌病人的血糖急症有兩個方向：吃不下、嘔吐加胰島素造成的**低血糖**，與 dexamethasone、感染、SGLT2 抑制劑與胰島素中斷造成的**高血糖危象**（DKA 與 HHS）。預防與日常監測見 [7.9](#79-血糖胰源性3c-型糖尿病與化療期間)。

**低血糖的分級與處置**（American Diabetes Association Professional Practice Committee, 2024，第 6 節）

| 分級 | 定義 | 處置 |
|------|------|------|
| Level 1 | 血糖 <70 mg/dL 且 ≥54 mg/dL | 意識清楚者吃約 15 g 速效醣類，15 分鐘後再測，仍低就重複 |
| Level 2 | 血糖 <54 mg/dL，出現神經低血糖症狀的門檻 | 立即處置，同上，並找原因 |
| Level 3 | 嚴重事件：意識或身體狀態改變，**需要他人協助**，不論血糖數值 | 不能吞嚥或意識不清時不可經口餵食，依院內低血糖 protocol 給靜脈葡萄糖或升糖素，並通知醫師 |

事件後要檢討原因：吃的量、胰島素劑量、胰酵素有沒有隨餐、化療後嘔吐、體重下降；胰源性糖尿病的升糖素反應受損，低血糖更容易發生，也更難靠自身反調節救回來（Hart et al., 2016）。病人與家屬要學會辨認症狀與處置。

> [!CAUTION]
> **待核對：低血糖分級與處置的出處**
> 上表取自 ADA 2024 年版標準的第 6 節（American Diabetes Association Professional Practice Committee, 2024），本手冊未能開啟該節全文逐條核對（分級與「約 15 g」的規則由同一指引各年版本的摘要確認）；ADA 2026 年版（American Diabetes Association Professional Practice Committee for Diabetes, 2026）的第 6 節已併入高血糖危象，其全文也未核對。實際處置以院內低血糖 protocol 為準。

**高血糖危象：DKA 與 HHS**（ADA/EASD/JBDS/AACE/DTS 2024 共識，Umpierrez et al., 2024）

| 項目 | DKA | HHS |
|------|-----|-----|
| 診斷 | 有糖尿病史或血糖 ≥200 mg/dL；血中 β-hydroxybutyrate（BHB）≥3.0 mmol/L；pH <7.30 和（或）碳酸氫鹽 <18 mmol/L | 明顯高血糖與高滲透壓，**沒有嚴重酮症與酸中毒** |
| 發展速度 | 數小時至數天 | 數天至數週 |
| 胰臟癌病人的誘因 | 感染（膽管炎、導管感染）、胰臟炎、胰島素中斷或吃不下、新發糖尿病、SGLT2 抑制劑 | corticosteroid、感染、胰臟炎 |
| 臨床線索 | 噁心、嘔吐、腹痛（>50%）、脫水、呼吸深快、意識改變 | 腹痛少見；脫水與意識改變為主 |

**第一小時**（依院內 DKA protocol 調整）

1. 指尖血糖，加**直接測血中 BHB**（共識建議），並驗血氣、電解質與陰離子間隙、肌酸酐、乳酸；找誘因，血液培養。
2. 補液：無腎臟或心臟問題時，生理食鹽水或平衡晶體液 500–1,000 mL/h，前 2–4 小時。
3. 血鉀 <5.0 mmol/L 就開始補鉀，維持在 4–5 mmol/L；開始胰島素後 2 小時及之後每 4 小時追蹤血鉀。
4. 胰島素：固定速率靜脈輸注，起始 0.1 U/kg/h；血糖降到 250 mg/dL 以下時加 5–10% 葡萄糖，並降到 0.05 U/kg/h。
5. 碳酸氫鹽不常規給，pH <7.0 才考慮。
6. 停用 SGLT2 抑制劑；依嚴重度決定病房、中度照護或加護病房。

> [!WARNING]
> **血糖不高也可能是酮酸中毒**
> 約 10% 的 DKA 在到院時血糖 <200 mg/dL（euglycemic DKA）；進食減少、酒精、肝衰竭與 SGLT2 抑制劑都是誘因。治療時要把 5–10% 葡萄糖加入靜脈輸液，或與 0.9% 生理食鹽水同時開始（Umpierrez et al., 2024）。化療後吃不下又在用 SGLT2 抑制劑的病人，血糖正常也要驗酮體。

### 8.7 共用章節的急症：胰臟癌病人要多想的地方

| 急症 | 胰臟癌病人的提醒 | 見 |
|------|----------------|-----|
| 發燒性嗜中性球低下 | 有膽道阻塞或支架時，發燒不論 ANC 都開廣效抗生素（Abraxis, 2022）；Onivyde 的致命嗜中性球敗血症與發燒性嗜中性球低下都有報告（Ipsen, 2025） | [腫瘤急症](00-shared/02-oncologic-emergencies.md#1-發燒性嗜中性球低下)第 1 節；[6.2](#62-irinotecan-與脂質體-irinotecan)、[6.5](#65-nab-paclitaxel-與-gemcitabinegnp) |
| 輸注反應與過敏性休克 | oxaliplatin 的過敏在**任何一個週期**都可能發生，仿單處置是立即且永久停藥；Onivyde 嚴重過敏要永久停用 | [腫瘤急症](00-shared/02-oncologic-emergencies.md#10-輸注反應過敏反應與過敏性休克)第 10 節；[6.3](#63-oxaliplatin) |
| 惡性腸阻塞與嗜中性球低下性小腸結腸炎 | 腸阻塞時 irinotecan 與 Onivyde 不可給；化療期間腹痛要先分辨阻塞、結腸炎與脂肪痢 | [腫瘤急症](00-shared/02-oncologic-emergencies.md#11-惡性腸阻塞與嗜中性球低下性小腸結腸炎)第 11 節；[6.7](#67-胰臟癌病人特有的判讀情境) |
| irinotecan 嚴重腹瀉與脫水 | G2 以上就暫停；腹瀉與嘔吐造成脫水可引起急性腎衰竭；高劑量 loperamide 最多連續 48 小時 | [6.2](#62-irinotecan-與脂質體-irinotecan)；[支持性照護](00-shared/03-supportive-care.md#5-腹瀉)第 5 節 |
| 46 小時輸注期間的心臟與神經毒性 | 胸痛、意識改變、走路不穩，依院內流程停止輸注並立即就醫 | [6.4](#64-5-fucapecitabine-與-s-1)、[7.3](#73-46-小時幫浦接上拆除與居家衛教) |
| 導管相關血流感染與導管血栓 | port 與 46 小時幫浦的使用者風險較高；發燒時從 port 與周邊各抽血液培養 | [化療基礎](00-shared/01-chemo-basics.md#135-導管相關血流感染crbsi)第 13.5、13.6 節 |
| 腫瘤溶解症候群、惡性肋膜積水、腦轉移、脊髓壓迫、高血鈣 | 本手冊未整理胰臟癌專屬的處置差異，依通用流程 | [腫瘤急症](00-shared/02-oncologic-emergencies.md#2-腫瘤溶解症候群tls)第 2、4、5、7、12 節 |

> [!IMPORTANT]
> **胰臟癌急症的必背**
> - **膽管炎**：TG18 確定診斷＝A（發炎）＋B（膽汁淤積）＋C（影像）；Grade II 以上要早期引流；Grade III＝新發器官功能障礙（PaO₂/FiO₂ <300、肌酸酐 >2.0 mg/dL、PT-INR >1.5、血小板 <100,000/mm³、意識障礙、需升壓劑）。
> - **胃出口阻塞**：支架見效快、再介入多；胃空腸吻合長期較好；EUS-GE 的 6 個月再介入率 4% 對 29%。
> - **出血**：住院病人的上消化道出血 Hb 7 g/dL 輸血、24 小時內內視鏡；術後前哨出血要當急症；血管內治療是假性動脈瘤出血的第一線。
> - **血栓**：內臟靜脈血栓復發與出血風險都高，抗凝血要個別決定。
> - **血糖**：低血糖 <70 mg/dL；<54 mg/dL 是 Level 2；DKA 的 BHB ≥3.0 mmol/L；SGLT2 抑制劑在吃不下時停用。

---

## 9. 健保給付與事前審查

**這一段的結論先講：** 胰臟癌的健保條文很短，但每一條都有陷阱。（1）轉移性第一線的三種標準方案都有給付：FOLFIRINOX（oxaliplatin 9.10 第 3 點加 irinotecan 9.12.1 第 2 點）、gemcitabine ＋ albumin-bound paclitaxel（9.4 加 9.5.2）、NALIRIFOX（Onivyde 9.12.2 第 2 點）；其中**只有 Onivyde（9.12.2，第一線與二線）規定事前審查**，而且原文沒有訂審查週期。（2）oxaliplatin、irinotecan、albumin-bound paclitaxel 的條文都寫「轉移性第一線」，所以**輔助、術前、局部晚期、轉移性二線**用 FOLFIRINOX 或 GnP，原文沒有對應條文（S-1 的 9.46 與 gemcitabine 的 9.4 是例外）。（3）有藥證不等於有給付：olaparib（gBRCA 維持）、pembrolizumab（MSI-H）、entrectinib（NTRK）在台灣有藥證，但 115/10/22 版第 9 節原文找不到胰臟癌或對應變異的條文；NTRK 只有 larotrectinib（9.95）有胰臟癌給付，而且要先前至少一次全身性治療失敗，需事前審查，每次 12 週。（4）胰臟神經內分泌腫瘤（pNET）的 sunitinib 與 everolimus 有專屬條文（9.31、9.36.1），**PDAC 病人不能用**。

### 9.0 先讀這裡：怎麼讀給付規定

- **依據版本**：全民健康保險藥品給付規定第 9 節「抗癌瘤藥物」，**115/10/22 版**（衛生福利部中央健康保險署，2026；原文存於 `sources/nhi/section9-1151022.md`，附表另見 `sources/nhi/nhi-drug-rules-1151022.docx`）。日期是民國紀年，115 年 ＝ 2026 年。
- **第 9 節與胰臟有關的條文只有九條**：以「胰」全文搜尋命中 9.4、9.5.2、9.10、9.12.1、9.12.2、9.31、9.36.1、9.46、9.95；英文 pancrea 無命中。本段的「原文未見」都是逐條對照的結果。
- **條號欄的日期**是該條最新的修訂日期；括號裡的「本點」日期是該款自己的日期。兩者不同時，兩個都寫。
- **藥證適應症是疊加條件**：9.4 寫「依藥品許可證登載之適應症範圍內給付」，9.10、9.12.1 的標題寫「需符合藥品許可證登載之適應症」，也就是藥要先用在藥證適應症的範圍內，再符合該款的給付條件。gemcitabine 在藥證上的逐字適應症本手冊沒有核對（見 [4.4](#44-術後輔助治療) 的待核對說明）。
- **用字不同不代表意思不同**：9.10、9.12.1 寫「轉移性胰臟癌」，9.5.2、9.12.2 寫「轉移性胰腺癌」，同一種病。
- **ECOG 與 biomarker**：胰臟癌的九條都沒有寫 ECOG；只有 9.95 需要檢附生物標記報告（NTRK），其他條文要的是病理報告與影像。
- **5-FU 與 leucovorin 沒有獨立條文**：第 9 節找不到這兩個藥的條號，只以併用藥身分出現在 9.10、9.12.1、9.12.2。
- **讀每一條的五個欄位**：適應症限制（線別、期別、前線用藥）→ 事前審查 → 療程與續用評估 → 停用條件 → 擇一或不得互換的限制。胰臟癌的條文大多只有第一欄有字。

> [!IMPORTANT]
> **通則十二：生物標記報告要合格**
> 給付規定要求附生物標記檢測報告時（胰臟癌只有 9.95 的 NTRK 基因融合），報告必須符合下列**任一**條件（113/6/1）：
> - （一）符合全民健康保險醫療服務給付項目及支付標準的規定；
> - （二）使用經衛生福利部許可的伴隨式診斷用體外診斷醫療器材（IVD）檢測；
> - （三）由衛生福利部核定之實驗室開發檢測（LDT）施行計畫所列醫療機構的認證實驗室執行，且技術項目符合核定的分析標的。
>
> 9.95 另外寫明「NTRK 1/2/3 檢測需符合通則十二」。送審前先確認手上的報告屬於哪一種，出處與檢測項目要在病歷上看得到。

**事前審查一覽：胰臟癌九條裡哪些要、哪些不要**

| 條文 | 藥品 | 條文是否規定事前審查 | 審查或評估週期 |
|------|------|-------------------|--------------|
| 9.4 | gemcitabine | 否（原文未規定） | 原文未規定 |
| 9.5.2 | albumin-bound paclitaxel | 否 | 原文未規定 |
| 9.10 第 3 點 | oxaliplatin（FOLFIRINOX） | 否 | 原文未規定 |
| 9.12.1 第 2 點 | irinotecan（FOLFIRINOX） | 否 | 原文未規定 |
| 9.12.2 第 1、2 點 | Onivyde（二線、第一線） | **是**（第 3 點，適用全條） | **原文未訂審查週期**、療程上限與續用條件 |
| 9.46 第 1 點 | S-1 | 否（條文中的事前審查只屬第 2 點胃癌術後輔助） | 原文未規定 |
| 9.95 | larotrectinib | **是**（第 4 點） | 每次申請 12 週 |
| 9.31 第 3 點 | sunitinib（pNET） | **是**（事前專案審查） | 每 3 個月評估一次 |
| 9.36.1 第 5 點 | everolimus（pNET） | **是** | 每次申請 3 個月 |

「條文沒有規定事前審查」不等於不用留資料：病歷仍要看得出病理、期別、線別與前線用藥，因為日後可能被審查（見 9.7）。

### 9.1 細胞毒性化療：轉移性第一、二線與局部晚期

| 藥品（商品名） | 條號（最新修訂） | 給付適應症與條件 | 事前審查 | 療程／續用評估 | 停用／互換／併用限制 |
|--------------|---------------|----------------|---------|--------------|------------------|
| gemcitabine（Gemzar） | 9.4（115/9/1；本點 115/6/1、115/9/1） | 胰臟癌（與非小細胞肺癌、膀胱癌、乳癌、卵巢癌、膽道癌並列），限「依藥品許可證登載之適應症範圍內」。原文未限線別、分期、組織型、ECOG、biomarker | 否（原文未規定） | 原文未規定 | 原文未列停用條件，也未訂劑量或數量限制。併用其他標靶治療、免疫檢查點抑制劑時，病人須符合該併用藥品的給付規定 |
| albumin-bound paclitaxel（Abraxane） | 9.5.2（108/11/1；母條 9.5 最新為 115/10/1） | **限併用 gemcitabine**，作為轉移性胰腺癌患者的第一線治療 | 否 | 原文未規定 | 原文未列停用條件。沒有擇一或不得互換條款。胰臟癌給付只見於另立的 9.5.2；9.5.1（paclitaxel 注射劑）各點都沒有胰臟癌適應症 |
| oxaliplatin | 9.10 第 3 點（條 115/2/1；本點 111/11/1） | 與 5-fluorouracil、leucovorin 及 irinotecan 併用（FOLFIRINOX），作為轉移性胰臟癌的第一線治療；條文標題「需符合藥品許可證登載之適應症」 | 否 | 原文未規定 | 原文未列停用條件。第 1 點 (1)「若再加用 irinotecan 則不予給付」**只適用轉移性結腸直腸癌**，不適用胰臟癌 |
| irinotecan（Campto） | 9.12.1 第 2 點（本點 112/2/1；母條 9.12 最新為 114/12/1） | 與 5-fluorouracil、leucovorin 及 oxaliplatin 併用（FOLFIRINOX），作為轉移性胰臟癌的第一線治療；標題「需符合藥品許可證登載之適應症」。**品項限用** Irino、Irinotel、Campto、Irinotecan Injection Concentrate、Irican、Innocan、Irinotecan Injection | 否 | 原文未規定 | 原文未列停用條件。品項限制只寫在第 2 點（胰臟癌）；Onivyde 不在這份名單，另立 9.12.2 |
| irinotecan liposome（Onivyde）：二線 | 9.12.2 第 1 點（本點 107/8/1；全條 114/12/1） | 與 5-FU 及 leucovorin 合併使用於**曾接受過 gemcitabine 治療後復發或惡化**的轉移性胰腺癌。原文未提 ECOG、biomarker | **是**（第 3 點） | 原文未訂審查週期、療程上限、影像頻率 | 原文未列停用條件。限併用 5-FU 及 leucovorin |
| irinotecan liposome（Onivyde）：第一線 | 9.12.2 第 2 點（114/12/1） | 與 oxaliplatin、5-FU 和 leucovorin 併用，作為轉移性胰腺癌**成人**病人第一線治療（原文沒有寫 NALIRIFOX 這個名稱） | **是**（第 3 點） | 同上 | 原文未列停用條件。原文未規定與 9.10／9.12.1 的 FOLFIRINOX 之間有擇一或不得互換的條款 |
| tegafur/gimeracil/oteracil（S-1，TS-1） | 9.46 第 1 點（條 113/2/1；本點未標日期） | 治療**局部晚期無法手術切除或轉移性**胰臟癌病人。原文未限線別、ECOG、biomarker，也沒有規定單用或併用 | 否（事前審查只屬第 2 點胃癌術後輔助） | 原文未規定（「限用 1 年」只屬胃癌術後輔助） | 原文未列停用條件。「不得與標靶治療、其他化療或免疫檢查點抑制劑併用」只屬第 3 點非小細胞肺癌 |

**讀表時最容易踩的地方**

- **FOLFIRINOX 要兩條配成一對**：oxaliplatin（9.10 第 3 點）與 irinotecan（9.12.1 第 2 點）。irinotecan 有**品項限制**，開立與調劑時先對照名單；Onivyde 是另一個藥（9.12.2），兩者不能互換（[5.2](#52-脂質體-irinotecannalirifox-與二線-nal-iri--5-fuleucovorin) 的 WARNING）。
- **「第一線」「二線」寫在條文裡，就是給付範圍**：9.5.2 與 9.10、9.12.1 都是「轉移性第一線」；只有 9.12.2 第 1 點明寫二線（曾接受 gemcitabine 後復發或惡化）。照字面讀，FOLFIRINOX 失敗之後改用 GnP，nab-paclitaxel 沒有對應的二線條文（見 9.4）。
- **局部晚期**：能對應的只有 S-1（9.46，「局部晚期無法手術切除或轉移性」）與 gemcitabine（9.4）；FOLFIRINOX、GnP、NALIRIFOX 的條文寫的是轉移性。
- **Onivyde 的事前審查沒有細節**：9.12.2 只寫「需經事前審查核准後使用」，沒有檢附文件清單、審查週期、續用條件。實際的送審格式與週期，本手冊無法由原文判斷，以健保署分區業務組與院內藥事部門的要求為準。
- **S-1 的藥證與給付範圍一致**：台灣藥證與 9.46 都是局部晚期或轉移性，所以日本 JASPAC 01 的術後輔助用法在台灣屬適應症外，也沒有給付條文（[4.4](#44-術後輔助治療)）。

### 9.2 NTRK 基因融合：larotrectinib（9.95）

| 藥品（商品名） | 條號（最新修訂） | 給付適應症與條件 | 事前審查 | 療程／續用評估 | 停用／互換／併用限制 |
|--------------|---------------|----------------|---------|--------------|------------------|
| larotrectinib（Vitrakvi） | 9.95 第 1、2、3(4)、4 點（條 113/6/1；第 1 至 3 點 112/12/1；第 4 點 111/3/1、111/6/1、113/6/1） | **共通條件（第 1 點）**：有 NTRK 基因融合的實體腫瘤成人和兒童病人，且須同時 (1) 具 NTRK 基因融合，**無已知的後天阻抗性突變**；(2) 為轉移性實體腫瘤，或手術切除極可能造成嚴重病症（severe morbidity）；(3) **沒有合適的替代治療選項（包含免疫檢查點抑制劑）**。**成人（≧18 歲）胰臟癌（第 3 點 (4)）**：先前曾接受過至少一次全身性治療失敗，又有疾病惡化，無法手術切除或轉移性胰臟癌。兒童（未滿 18 歲，第 2 點）：除嬰兒纖維肉瘤外，須曾接受一線治療後無效或復發。原文未提 ECOG | **是**（第 4 點）；初次申請須檢附 NTRK 基因融合檢測報告，NTRK 1/2/3 檢測須符合通則十二 | 每次申請 12 週；再次申請須檢附療效評估資料證實無疾病進展，才可繼續使用。原文未規定影像頻率與總療程上限 | 原文未另列停用條款；未能證實無疾病進展即不得續用。原文沒有擇一或不得互換條款 |

**讀表重點**

- **沒有「第一線」這個給付途徑**：成人胰臟癌的條文要求先前至少一次全身性治療失敗又惡化。未曾治療、剛確診的 NTRK 融合病人，照字面讀沒有對應條文，這和 NCCN 把 NTRK 列為要檢測的標靶並不衝突，只是給付時點較晚。
- **三個條件缺一不可**：沒有後天阻抗性突變、轉移性（或切除會造成嚴重病症）、沒有合適的替代治療（含免疫檢查點抑制劑）。病歷要寫出為什麼沒有其他合適的選項。
- **NTRK 融合在 PDAC 很少**：整體約 0.8%（3／400），KRAS wild-type 中約 6.25%；只做 DNA 定序會有偽陽性（6 個），要用 RNA 驗證（Allen et al., 2023；見 [2.3](#23-分子景觀)、[2.5](#25-檢測策略組織-ngsctdna-與-nccn-建議)）。送審的報告要符合通則十二，驗證方式與報告出處在送審前先確認。
- **同類的另兩個藥沒有胰臟癌給付**：entrectinib（9.93）只給付 ROS-1 陽性的非小細胞肺癌；repotrectinib（9.131）只給付在 crizotinib 或 entrectinib 治療中惡化的 ROS1 陽性非小細胞肺癌。兩個藥在台灣都有 NTRK 藥證（見 9.5）。

### 9.3 胰臟神經內分泌腫瘤（pNET）：sunitinib 與 everolimus

> [!IMPORTANT]
> **pNET 不是 PDAC，條文不能互用**
> 9.31 第 3 點與 9.36.1 第 2 點寫的是「胰臟神經內分泌腫瘤」，條件含 WHO 2010 分類 G1／G2 或分化良好，**不包括 PDAC**。PDAC 病人不符合這兩條。pNET 的分類與治療路線見[速查卡的提示框](#0-速查卡)，指引是 NCCN Neuroendocrine and Adrenal Tumors，不在本章的化療路線內。

| 藥品（商品名） | 條號（最新修訂） | 給付適應症與條件 | 事前審查 | 療程／續用評估 | 停用／互換／併用限制 |
|--------------|---------------|----------------|---------|--------------|------------------|
| sunitinib（Sutent） | 9.31 第 3 點（條 112/3/1；本點 101/5/1，第 (3) 款 102/1/1） | 成人；進展性、無法切除或轉移性、**分化良好**的胰臟神經內分泌腫瘤，須同時符合：(1) WHO 2010 分類 G1 或 G2；(2) 一年內影像檢查證實有明顯惡化；(3) 不可合併使用化學治療或相關標靶藥物 | **是**（經事前專案審查核准）；附表九之五 | 需每 3 個月評估一次；原文未規定每次申請的療程長度與總療程上限 | 原文未規定停用條件。sunitinib 條文沒有互換條款；everolimus 條文規定兩者不得轉換（見下一列）。第 2 點 (4)「耐受性不佳以原藥減量」只屬腎細胞癌 |
| everolimus 5 mg／10 mg（Afinitor） | 9.36.1 第 2、5、6 點（條 114/12/1；第 2 點 102/1/1；第 5 點 104/12/1、108/10/1；第 6 點 108/10/1） | 成人；無法切除或轉移的胰臟內分泌腫瘤，分化程度為良好或中度，或 WHO 2010 年分類為 G1、G2；為進展性腫瘤，即過去 12 個月影像檢查為持續惡化（RECIST 定義為疾病惡化）；不可合併使用化學藥物或其他標靶藥物 | **是**（第 5 點：除晚期腎細胞癌外都需事前審查）；附表九之九 | 每次申請 3 個月；初次須檢送病理報告及影像報告；之後每 3 個月申請一次，再次申請須檢附影像資料及前次治療結果評估資料證實無惡化，才可繼續使用。原文未規定總療程上限 | 未能證實無惡化即不得續用。**除因嚴重不良反應或耐受不良外，本品與 sunitinib 不得轉換使用**（第 2 點 (4)）；**每日最大劑量 10 mg**（第 6 點）。9.36.2（Votubia）無胰臟適應症；9.36.1 第 3 點是胃腸道或肺部來源的非功能性 NET，不屬胰臟來源 |

與 pNET 有關、但不在第 9 節的條文（115/10/22 版，已對照原文）：

- **5.4.3 octreotide 注射劑**（87/11/1、102/1/1）第 4 點：治療患有功能性症狀之胃、腸、胰內分泌腫瘤的患者。
- **5.4.4 octreotide 長效型**（89/7/1、102/1/1、104/4/1）第 2 點：同上；第 4 點需事前審查，每次申請以一年為限；第 5 點用於第 1、2 項時每次 20 mg，間隔四週。
- **5.4.6 lanreotide**（最新修訂 106/8/1）第 3 點：無法切除、分化程度為良好或中度、局部進展或轉移性的胃、腸、胰臟神經內分泌腫瘤（GEP-NETs）；非功能性須附 6 個月內 somatostatin-receptor 陽性報告；每月限 120 mg 長效注射劑一針，間隔 4 週；需事前審查，每次申請以一年為限，期滿須再次申請核准才得續用。

### 9.4 依病人情境對照：哪一段治療有條文

下表把第 4 段的治療情境對到 115/10/22 版原文。**「原文沒有對應」只代表第 9 節找不到條文**，不代表不該用；指引建議的治療（NCCN, 2026；Tai et al., 2025）要和給付分開看。

| 情境 | 原文有對應的條文 | 原文沒有對應，或需要確認的地方 |
|------|---------------|--------------------------|
| 可切除，術後輔助（[4.4](#44-術後輔助治療)） | gemcitabine（9.4，未限分期，限藥證適應症範圍內；術後輔助是否落在許可範圍，見 4.4 的待核對說明） | mFOLFIRINOX：9.10、9.12.1 只寫轉移性第一線。GemCap：capecitabine 9.17 無胰臟適應症。S-1：9.46 只寫局部晚期或轉移，台灣藥證也沒有輔助適應症 |
| 可切除或邊緣可切除的術前治療（[4.5](#45-術前neoadjuvant與圍術期證據逐一看)、[4.6](#46-邊緣可切除borderline-resectable)） | gemcitabine（9.4） | FOLFIRINOX、GnP、NALIRIFOX 的條文限轉移性。S-1 的「局部晚期無法手術切除」包不包含邊緣可切除，原文沒有定義 |
| 局部晚期（[4.7](#47-局部晚期locally-advanced)） | S-1（9.46）；gemcitabine（9.4） | FOLFIRINOX（9.10、9.12.1）、GnP（9.5.2）、NALIRIFOX（9.12.2 第 2 點）都限轉移性 |
| 轉移性第一線（[4.8](#48-轉移性第一線依體能分層)） | FOLFIRINOX（9.10 第 3 點加 9.12.1 第 2 點）；GnP（9.4 加 9.5.2）；NALIRIFOX（9.12.2 第 2 點，**事前審查**）；gemcitabine 單藥（9.4）；S-1（9.46，未限線別） | 三套方案之間原文沒有擇一或不得互換的條款；「第一線」治療中途因毒性換方案算不算同一線，原文沒有定義 |
| 轉移性二線，前線以 gemcitabine 為主（[4.9](#49-維持治療與二線以後)） | Onivyde ＋ 5-FU／leucovorin（9.12.2 第 1 點，**事前審查**）；S-1（9.46） | FOLFIRINOX 作為二線：9.10、9.12.1 限第一線，原文無對應 |
| 轉移性二線，前線是 FOLFIRINOX 或 NALIRIFOX | gemcitabine（9.4，未限線別）；S-1（9.46） | GnP 作為二線：9.5.2 限第一線，nab-paclitaxel 沒有二線條文。Onivyde 二線（9.12.2 第 1 點）條文是「曾接受過 gemcitabine 治療後」，前線沒用過 gemcitabine 的病人是否符合，原文看不出來 |
| germline BRCA1/2 維持治療 | 無 | olaparib 在 9.85 原文未見胰臟癌 |
| MSI-H／dMMR | 無 | pembrolizumab 在 9.69 原文未見胰臟癌，也未見不分癌別的 MSI-H／dMMR |
| NTRK 基因融合 | larotrectinib（9.95，成人需先前至少一次全身性治療失敗又惡化；**事前審查**） | 第一線的 NTRK 融合沒有條文；entrectinib、repotrectinib 原文未見 NTRK |
| 胰臟神經內分泌腫瘤（不是 PDAC） | sunitinib（9.31）；everolimus（9.36.1）；lanreotide、octreotide 長效型（第 5 節） | PDAC 不適用 |

> [!CAUTION]
> **待核對：線別與「第一線」的定義**
> 9.5.2、9.10、9.12.1 與 9.12.2 第 2 點都寫「第一線」，原文沒有定義第一線的範圍。下面三件事，原文沒有答案，本手冊不下結論，開立與送審前請向主治醫師、藥事部門確認，必要時詢問健保署分區業務組：（1）FOLFIRINOX 或 NALIRIFOX 打了一兩個週期因毒性停用，改成 GnP，算不算同一個第一線；（2）FOLFIRINOX 失敗後的 GnP 二線，nab-paclitaxel 有沒有給付；（3）邊緣可切除或局部晚期術前治療用的 FOLFIRINOX 或 GnP，是否因為「轉移性」三個字而不給付。上表是照條文字面對照的結果，院內與審查端的實際做法可能不同。

> [!WARNING]
> **事前審查沒過，不要把 Onivyde 換成「同劑量」的 irinotecan**
> Onivyde 與一般 irinotecan 是不同的藥：劑量單位（游離鹼）、輸注時間（90 分鐘）、前置藥物都不同，仿單明寫不可互相取代（Ipsen, 2025）。Onivyde 未獲核准、或病人只能改走 9.10 加 9.12.1 的 FOLFIRINOX 時，必須由醫師重新開立完整的新處方（含 5-FU bolus 與 irinotecan 劑量的決定，見 [5.1](#51-folfirinox-家族輔助-mfolfirinox-與轉移性-folfirinox)），不是把 Onivyde 的 50 或 70 mg/m² 直接改成另一個品項。

### 9.5 有藥證或指引建議、但原文沒有胰臟條文的藥

下表的藥，在 115/10/22 版第 9 節用學名與商品名逐一搜尋，**沒有胰臟癌（或對應變異）的給付文字**。TFDA 藥證依 2026-10-27 的開放資料。有藥證可以合法處方；沒有給付時，費用怎麼處理（自費或院內其他安排）由主治醫師與院內流程決定。

| 藥品 | 本章出現的位置 | TFDA 藥證（2026-10-27 資料） | 115/10/22 版原文 | 說明 |
|------|--------------|---------------------------|----------------|------|
| olaparib（Lynparza） | [4.9](#49-維持治療與二線以後)、[5.4](#54-口服與維持用藥s-1capecitabineolaparib以及不建議的-erlotinib) | **有**（衛部藥輸字第027445、027446號，2018-06-05）：gBRCA、第一線 platinum 至少 16 週未惡化後維持，與 POLO 相符 | 9.85（PARP 抑制劑）有條文，但適應症是卵巢／輸卵管／原發性腹膜癌、三陰性乳癌、mCRPC、高復發風險早期乳癌，**原文未見胰臟癌** | 無健保給付 |
| pembrolizumab（Keytruda） | [2.4](#24-可標靶的變異與藥物)、[4.10](#410-生物標記導向治療與-kras-標靶) | **有**：不分癌別的 MSI-H／dMMR 實體瘤，先前治療後無合適替代 | 9.69 有條文，**原文未見胰臟癌**，也未見不分癌別的 MSI-H／dMMR。MSI-H／dMMR 只出現在大腸直腸癌（限 pembrolizumab 第一線）與子宮內膜癌（限 dostarlimab 併 carboplatin ＋ paclitaxel） | 無健保給付 |
| entrectinib（Rozlytrek） | [2.4](#24-可標靶的變異與藥物) | **有**（NTRK 融合實體腫瘤；2020-05-21 核發） | 9.93 只給付 ROS-1 陽性非小細胞肺癌，原文未見 NTRK 或胰臟癌 | Pan-Asian ESMO 台灣段落寫「未核准」，與 TFDA 資料不符，以 TFDA 為準（Tai et al., 2025） |
| repotrectinib（Augtyro） | [2.4](#24-可標靶的變異與藥物) | **有**（NTRK 融合實體腫瘤） | 9.131 只給付 ROS1 陽性非小細胞肺癌，原文未見 NTRK 或胰臟癌 | 無健保給付 |
| capecitabine（Xeloda） | [4.4](#44-術後輔助治療)、[5.4](#54-口服與維持用藥s-1capecitabineolaparib以及不建議的-erlotinib) | 有許可證，**無胰臟適應症** | 9.17 有條文（乳癌、結腸直腸癌、胃癌），**原文未見胰臟癌** | GemCap 輔助屬適應症外，也無給付條文 |
| erlotinib（Tarceva） | [5.4](#54-口服與維持用藥s-1capecitabineolaparib以及不建議的-erlotinib) | **無胰臟適應症**（僅非小細胞肺癌） | 9.29 僅非小細胞肺癌，**原文未見胰臟癌** | 本手冊不建議常規使用 |
| sotorasib（Lumakras）、adagrasib（Krazati） | [4.10](#410-生物標記導向治療與-kras-標靶) | 有許可證，**無胰臟適應症** | 原文未收載 | KRAS G12C 只占約 1.6% |
| zenocutuzumab | [4.10](#410-生物標記導向治療與-kras-標靶) | **無** | 原文未收載 | 美國 FDA 2024-12-04 加速核准（NRG1 融合） |
| daraxonrasib（RASONQUE） | [4.10](#410-生物標記導向治療與-kras-標靶) | **無**（2026-10-27 資料查無） | 原文未收載 | 美國 FDA 2026-08-26 核准；台灣尚未上市 |
| selpercatinib、rucaparib、erdafitinib | [2.4](#24-可標靶的變異與藥物)、[4.9](#49-維持治療與二線以後) | 本手冊未核對 | 原文未收載 | 藥證狀態不要告訴病人「可以處方」，先向藥事部門確認 |
| dabrafenib ＋ trametinib、trastuzumab deruxtecan | [2.4](#24-可標靶的變異與藥物) | 本手冊未核對胰臟適應症 | 9.91（黑色素瘤與非小細胞肺癌）與 9.115（乳癌）有條文，**原文未見胰臟癌** | 無健保給付 |

**有條文，但本章用到的胰臟癌用法原文未見**

| 藥品 | 有條文的部分 | 本章的胰臟癌用法（原文未見給付文字） |
|------|------------|--------------------------------|
| oxaliplatin（9.10）、irinotecan（9.12.1） | 轉移性第一線 FOLFIRINOX | 輔助 mFOLFIRINOX（PRODIGE 24）、術前與誘導、局部晚期、二線 |
| albumin-bound paclitaxel（9.5.2） | 轉移性第一線，限併用 gemcitabine | GnP 二線、輔助（APACT 主要指標未達成） |
| Onivyde（9.12.2） | 轉移性第一線與二線 | 術前或局部晚期的 NALIRIFOX |
| S-1（9.46） | 局部晚期無法手術切除或轉移性 | 術後輔助（JASPAC 01） |
| gemcitabine（9.4） | 許可證範圍內，未限分期 | gemcitabine ＋ erlotinib：9.4 規定併用標靶治療時須符合併用藥的給付規定，而 erlotinib 沒有胰臟癌條文。GemCap 的 capecitabine 也沒有胰臟癌條文（9.17） |

> [!TIP]
> **藥證是駕照，健保是油錢補助，處方集是車庫**
> 有藥證，像是這個人有駕照，合法上路；健保給付，是這趟路程的油錢有人補助，要符合條文才補；院內處方集，是車庫裡有沒有這輛車。三件事互相獨立：有駕照沒油錢補助（olaparib）、有油錢補助沒有車（藥事委員會沒進藥）、車在庫裡但路線不對（FOLFIRINOX 用在術前）。（教學簡化。）

> [!NOTE]
> **病人問「這個藥可以用嗎」**
> 先分三層回答：①有沒有台灣藥證（TFDA；見 [4.11](#411-新藥在台灣的狀態藥證健保與美國核准)）；②有沒有健保給付、符不符合條件（本段）；③院內有沒有進藥。原文未見代表 115/10/22 版第 9 節沒有條文，不代表藥物無效或不該用。指引建議、但沒有給付的藥，由主治醫師與病人討論自費或其他途徑，專師的角色是把三層的狀態講清楚，不要說「健保不給付，所以不能用」。Pan-Asian ESMO 的台灣段落提到，新藥獲 FDA 或 EMA 核准後，約需 1–2 年才進台灣，再 1–2 年才可能有健保（Tai et al., 2025）。

### 9.6 不在第 9 節、但胰臟癌病人常碰到的條文

下列條文來自第 9 節以外的章節，條號與日期已對照 115/10/22 版原文。**G-CSF 與止吐劑的完整規定在共用章節**，不在這裡重複。

| 項目 | 條號（最新修訂） | 與胰臟癌有關的重點 | 本手冊位置 |
|------|---------------|-----------------|-----------|
| G-CSF | 4.1.2.1 短效型（101/6/1）；4.1.2.2 長效型（114/9/1） | 其他惡性疾病（含胰臟癌）走 4.1.2.1 第 (4) 款，條件是化療後**曾經發生**白血球 <1,000/cumm 或 ANC <500/cumm；pegfilgrastim 限非骨髓性癌症，同樣要求「曾經發生」。原文沒有「依發燒性嗜中性球低下風險 ≥20% 預防」這一款，所以 FOLFIRINOX、NALIRIFOX 第 1 週期的一級預防是否給付，原文看不出來 | [支持性照護](00-shared/03-supportive-care.md#24-健保給付g-csf)第 2.4 節；[腫瘤急症](00-shared/02-oncologic-emergencies.md#16-健保給付g-csf)第 1.6 節；[5.5](#55-前置用藥止吐與給藥當天的門檻) |
| 止吐劑 | 7.2.1（102/9/1）、7.2.2（102/8/1）、7.2.3（114/8/1） | 靜脈化療的致吐風險依 NCCN 最新版判定；NK1 拮抗劑（7.2.2）只列高致吐，NEPA（7.2.3）中致吐化療只限已用含 5-HT3 處方仍發生症狀者的後續療程。FOLFIRINOX、NALIRIFOX 這類多藥方案的整體分級，本手冊沒有取得指引原文 | [支持性照護](00-shared/03-supportive-care.md#14-健保給付止吐劑)第 1.4 節；[5.5](#55-前置用藥止吐與給藥當天的門檻) |
| denosumab（Xgeva） | 5.5.4（113/10/1） | 限用於多發性骨髓瘤，以及乳癌、前列腺癌、肺癌、結腸直腸癌、膀胱癌、腎癌、子宮頸癌、卵巢癌、食道癌、胃癌及**胰癌**併有蝕骨性骨轉移的病人。zoledronic acid 4 mg（5.5.3.2.1，100/1/1）的骨轉移適應症只列骨髓瘤、乳癌、前列腺癌，不含胰癌 | [支持性照護](00-shared/03-supportive-care.md#83-健保給付骨骼保護劑)第 8.3 節 |
| 胰酵素（Creon 等） | 7.3.6（110/1/1） | 因疾病造成的胰液分泌不全，含胰臟切除手術與「其他因腫瘤引發之胰管膽管阻塞」；申報時檢附病歷與檢驗（查）報告，須有胰液分泌不全疾病、營養不良或脂肪痢便的記載；功能性腸胃炎不得使用 | [5.6](#56-胰酵素替代治療pert)、[7.7](#77-胰酵素替代治療的病房流程) |
| octreotide 注射劑；somatostatin；pasireotide | 5.4.3（87/11/1、102/1/1）第 2 點；5.4.5（87/11/1、89/5/1）第 1 點；5.4.8（103/7/1、106/10/1） | 5.4.3：預防胰臟手術後的併發症，**最長使用七天**；5.4.5：同用途，**最長使用五天**；5.4.8 pasireotide 限庫欣氏病，用於預防胰漏屬適應症外 | [4.2](#42-手術術式淋巴結與切緣r0r1)、[7.13](#713-胰臟切除術後病房常見併發症isgps-定義) |
| megestrol 口服液劑 | 5.3.6（108/6/1、109/3/1） | 限用於已排除其他可治療的體重減輕後、具惡病質的後天免疫缺乏症候群患者及癌症患者；惡病質條件為最近 6 個月內體重流失 >5%，或 BMI <20 且體重流失 >2% | [7.8](#78-惡病質與營養) |
| DOAC（治療 DVT／PE） | 2.1.4.2（rivaroxaban，條 115/10/1）、2.1.4.3（apixaban，條 111/2/1）、2.1.4.4（edoxaban，條 111/2/1） | 治療用途須經影像學或血管超音波診斷，沒有癌症專屬條件；依 Khorana 分數的癌症門診預防性抗凝，在這三條原文未見 | [7.10](#710-血栓預防與處置)；[支持性照護](00-shared/03-supportive-care.md#74-健保給付doac-治療-dvtpe)第 7.4 節 |

### 9.7 專師送事前審查前的檢核

**先講結論：** 事前審查被退件的原因，本手冊沒有原文可查，不推測；能做的是把原文要求的文件一項一項備齊，並把「條文怎麼寫」和「病人怎麼分類」逐字對照。第 9 節與胰臟有關的九條裡，只有四個藥要事前審查（Onivyde、larotrectinib、sunitinib、everolimus），其中 Onivyde 的原文沒有列任何檢附文件。

| 藥品群組 | 初次申請（或病歷留存）要備的文件 | 續用要備的文件 |
|---------|------------------------------|--------------|
| 所有案件的共同底線 | 病理或細胞檢查報告（PDAC 寫腺癌；pNET 另附 WHO 分級）；期別與線別照條文用字寫（「轉移性」「局部晚期無法手術切除」「第一線」「曾接受過 gemcitabine 治療後復發或惡化」）；影像報告；前線方案與日期 | 治療後的相關臨床資料與影像，證實無惡化或無進展 |
| Onivyde（9.12.2） | 原文只寫「需經事前審查核准後使用」，沒有檢附文件清單。病歷上要看得出：轉移性胰腺癌；第一線（成人，併 oxaliplatin、5-FU、leucovorin）或二線（曾接受過 gemcitabine 治療後復發或惡化的紀錄與影像）；處方品項是 Onivyde，不是一般 irinotecan | 原文未訂續用條件與週期，依核准內容與健保署分區業務組的要求 |
| larotrectinib（9.95） | NTRK 基因融合檢測報告（NTRK 1/2/3，符合通則十二）；先前至少一次全身性治療失敗又惡化的紀錄（前線方案、惡化影像）；無法手術切除或轉移性；沒有已知後天阻抗性突變，沒有合適替代治療（含免疫檢查點抑制劑）的說明 | 每 12 週：療效評估資料證實無疾病進展 |
| sunitinib（9.31）：pNET | 病理報告為 pNET，WHO 2010 分類 G1 或 G2；一年內影像證實明顯惡化；沒有合併化學治療或相關標靶藥物；附表九之五（有 pNET 的勾選欄） | 每 3 個月評估一次，附影像 |
| everolimus（9.36.1）：pNET | 病理報告與影像報告；過去 12 個月影像持續惡化（RECIST 疾病惡化）；沒有合併化學藥物或其他標靶藥物；附表九之九；每日不超過 10 mg | 每 3 個月再申請：影像資料及前次治療結果評估證實無惡化；與 sunitinib 不得轉換（除嚴重不良反應或耐受不良） |
| 不需事前審查：gemcitabine、GnP、FOLFIRINOX、S-1 | 病歷留存：胰臟癌病理報告；轉移證據影像（FOLFIRINOX、GnP、NALIRIFOX），或「局部晚期無法手術切除」的 MDT 紀錄（S-1）；第一線的說明；irinotecan 的品項（限指定名單）；albumin-bound paclitaxel 與 gemcitabine 併用 | 原文未規定 |

**送審前的小提醒（都來自原文）**

- **記下每個藥的週期**：larotrectinib 每次申請 12 週；everolimus 每次申請 3 個月；sunitinib 每 3 個月評估一次；Onivyde 原文未訂。
- **確認品項**：FOLFIRINOX 的 irinotecan 限 9.12.1 名單內的七個品項；Onivyde 是另一條；nab-paclitaxel 要寫 albumin-bound paclitaxel，與 paclitaxel 注射劑（9.5.1）是不同的條文。
- **不要把 pNET 條文用到 PDAC**，也不要把 PDAC 的 FOLFIRINOX 條文用到術前或局部晚期而不先確認（見 9.4）。
- **生物標記報告**：larotrectinib 的 NTRK 報告要符合通則十二，先確認報告出處。
- **併用藥各自合格**：9.4 規定 gemcitabine 與標靶治療、免疫檢查點抑制劑併用時，病人須符合併用藥的給付規定。

> [!IMPORTANT]
> **事前審查的後果（附表九之五、九之九的注意事項）**
> 第 9 節原文附有 sunitinib 與 everolimus 的申請表，表尾的注意事項寫明：應事前審查的項目，未依規定事前申請核准者，**不予給付費用**；事前申請核准的個案，日後如經審定病人或醫事機構有不符給付規定者，**亦不予給付費用**；對核定結果有異議，應在收到通知後六十日內循申復及爭議審議途徑處理，不得以新個案重新申請；醫事機構如因事出緊急，得以書面說明電傳保險人報備後先行處理治療，並立即備齊應附文件備查。

> [!CAUTION]
> **待核對：Onivyde 與 larotrectinib 沒有附表，適用同樣的注意事項嗎**
> 上面的注意事項寫在 sunitinib 與 everolimus 的申請表上。9.12.2（Onivyde）與 9.95（larotrectinib）在原文沒有對應的附表，這兩個藥的申請方式、時限、緊急處置與核准後的審查，原文看不出來，本手冊不下結論；實際流程以健保署分區業務組與院內藥事部門為準。條文在 115/10/22 版之後若改版，請重新對照原文的條號與修訂日期。

---

## 10. 個案練習

三個個案分別對應術前決策與黃疸（第 3、4 段）、化療毒性與基因檢測（第 5、6 段）、膽管炎（第 7、8 段）。先自己回答引導問題，再展開參考答案；答案裡的數字與條號都回到前面的段落。

### 個案一：黃疸的邊緣可切除胰頭癌

63 歲男性，2 個月內體重下降 6 kg，茶色尿、皮膚變黃 2 週，3 個月前被診斷糖尿病（空腹血糖 138 mg/dL）。ECOG 1，BMI 22。Pancreas-protocol CT（**在引流之前完成**）：胰頭 3.2 cm 低密度腫塊；SMV 接觸約 200°、輪廓不規則，但上下游血管通暢、評估可重建；SMA 接觸約 90°；celiac axis 與 CHA 無接觸；無肝臟或其他遠端轉移。EUS-FNB：腺癌。總膽紅素 11.8 mg/dL、ALP 520 U/L、ALT 98 U/L，沒有發燒；ANC 4,100/µL、PLT 260,000/µL、肌酸酐 0.8 mg/dL；CA19-9 1,860 U/mL。他說「想趕快開刀」，家屬問「先化療會不會耽誤」。

1. 依 NCCN，這是哪一類？哪些影像發現決定分類？CA19-9 1,860 U/mL 要怎麼解讀？
2. 黃疸要不要引流？化療前膽紅素要降到多少？
3. 術前治療怎麼選？第一個週期之前要先拿到哪些資料？證據是什麼？
4. 健保怎麼看這個術前處方？

<details>
<summary>參考答案</summary>

1. **邊緣可切除（borderline resectable，頭部）。** SMV 接觸 >180° 且輪廓不規則，但上下游適合安全切除與重建；SMA 實質接觸 ≤180°；celiac axis 與 CHA 沒有接觸，沒有遠端轉移，所以不是 locally advanced（SMA 或 CA >180°，或 SMV／PV 無法重建），也不是 metastatic（[3.8](#38-nccn-可切除性分類)；Corallo et al., 2025；Chu & Fishman, 2024）。治療分流看這個分類，不是看 AJCC 分期。CA19-9 是在膽紅素 11.8 mg/dL 時抽的，膽道阻塞使偽陽性升到 10–60%，要在引流、膽紅素下降後重抽，當作基準值（Ballehaninna & Chamberlain, 2012）。如果重抽仍 >500 U/mL，這是 IAP 2017「生物學邊緣可切除」的標準之一（Tai et al., 2025）；再加上腫瘤 ≥3 cm，兩項隱藏轉移的風險因子都有，隱藏轉移比例 28.9%（95% CI 17.0–44.8），要和外科討論分期腹腔鏡（Rompen et al., 2026；[3.6](#36-分期腹腔鏡)）。新發糖尿病加體重下降，是這位病人的另一個線索（[1.2](#12-危險因子)）。
2. **要引流，而且影像已經先做完**（[3.2](#32-work-up-流程)「支架之前先照影像」）。膽紅素 11.8 mg/dL 約 202 µmol/L，低於 250 µmol/L（約 14.6 mg/dL）的內視鏡引流門檻（Tai et al., 2025）；如果可以在診斷後約 1 週內手術，不常規引流（van der Gaag et al., 2010）。但這位病人要先做數個月的術前化療，手術不是 1 週內，ESGE 的原則是黃疸病人要先做術前化療時可以引流；病理已確診，術前引流用 10-mm SEMS（Dumonceau et al., 2018；[3.5](#35-膽道阻塞什麼時候要引流)）。支架材質與時機與消化內科、外科共同決定。化療的膽紅素門檻：PRODIGE 4、PRODIGE 24 要求 ≤1.5 × ULN；Onivyde 高於 ULN 沒有建議劑量；irinotecan >2 mg/dL 沒有建議劑量；nab-paclitaxel >1.5 × ULN 不建議（[5.7](#57-肝腎功能與膽紅素門檻速查)）。順序是：引流 → 等膽紅素下降 → 重抽 CA19-9 基準值 → 排化療。引流後發燒或冷顫，先想膽管炎（[8.1](#81-急性膽管炎acute-cholangitis)）。
3. **選擇。** NCCN 病人版對邊緣可切除的偏好方案：FOLFIRINOX 或 mFOLFIRINOX（限 PS 0–1）、GnP；帶 BRCA 或 PALB2 變異者 cisplatin ＋ gemcitabine；最長約 6 個月，在高量醫院進行（NCCN, 2026，病人版）；放療加在誘導化療上沒有看到好處（[4.6](#46-邊緣可切除borderline-resectable)）。ECOG 1、膽道引流後，FOLFIRINOX 或 GnP 都可以考慮，選擇看膽紅素、既存神經病變、腸道疾病、UGT1A1 與 DPYD（[4.8](#48-轉移性第一線依體能分層)）。**證據：** Alliance A021501（隨機第 2 期，邊緣可切除，n = 126）mFOLFIRINOX × 8 → 手術 → mFOLFOX6 × 4，18 個月 OS 66.7%（56.1–79.4），中位 OS 29.8 個月，但只有 40% 接受胰臟切除；加 SBRT 的臂沒有更好（Katz et al., 2022）。PREOPANC-2 的術前 FOLFIRINOX 沒有贏過術前化放療（OS 21.9 對 21.3 個月，HR 0.88；Janssen et al., 2025）。所以回答家屬：先化療不是耽誤，是邊緣可切除的標準路線，但術前治療後仍可能因惡化或體力下降而失去手術機會（[4.5](#45-術前neoadjuvant與圍術期證據逐一看)）。**第一個週期之前要拿到：** germline 檢測（所有 PDAC；BRCA／PALB2 會改變 platinum 的選擇）與腫瘤 NGS，確診當天就送（[2.5](#25-檢測策略組織-ngsctdna-與-nccn-建議)）；開 irinotecan 前想 UGT1A1、開 5-FU 前想 DPYD（[化療基礎](00-shared/01-chemo-basics.md#12-藥物基因檢測與特殊族群評估)第 12 節）；port 與 46 小時幫浦的準備；PERT、血糖與營養評估（[5.6](#56-胰酵素替代治療pert)、[7.8](#78-惡病質與營養)、[7.9](#79-血糖胰源性3c-型糖尿病與化療期間)）。化療期間由 MDT 安排影像與 CA19-9 重評，再決定手術；術前加術後的化療總量約 6 個月。
4. **原文沒有對應條文。** oxaliplatin（9.10 第 3 點）、irinotecan（9.12.1 第 2 點）、albumin-bound paclitaxel（9.5.2）、Onivyde（9.12.2 第 2 點）都限「轉移性」；gemcitabine（9.4）未限分期；S-1（9.46）寫「局部晚期無法手術切除或轉移性」，邊緣可切除算不算「無法手術切除」，原文沒有定義（[9.4](#94-依病人情境對照哪一段治療有條文)）。專師的角色不是說「健保不給付，所以不能做」，而是把藥證、給付、處方集三層說清楚，再請主治醫師與藥師確認自費或其他申報方式。FOLFIRINOX 與 GnP 的條文沒有事前審查，Onivyde 才有。

</details>

### 個案二：轉移性 mFOLFIRINOX 第 1 週期後的水瀉

56 歲女性，轉移性胰體尾 PDAC（肝轉移），ECOG 1，總膽紅素 0.7 mg/dL。身高 158 cm、體重 52 kg（Mosteller BSA 1.51 m²）。因疼痛固定使用 oxycodone，並每天吃軟便劑（magnesium oxide）。第一線 mFOLFIRINOX：oxaliplatin 85、irinotecan 150、leucovorin 400 mg/m²，5-FU 2,400 mg/m² 持續輸注 46 小時，無 bolus（irinotecan 150 × 1.51 ≈ 227 mg）。病歷**沒有 UGT1A1 與 DPYD 的結果**。第 1 週期給藥後第 6 天，她因水瀉每天 8 次（平時 1 次）來急診，吃了 4 mg loperamide 沒有改善；口腔多處潰瘍，痛到喝水困難；頭暈。T 37.9°C、BP 98/62 mmHg、HR 108；K 3.0 mmol/L、肌酸酐 1.3 mg/dL（基線 0.6）；ANC 700/µL、PLT 150,000/µL。

1. 這是哪一型腹瀉、CTCAE v5.0 幾級？第一小時要做什麼？
2. 她吃的藥有什麼要立刻調整？loperamide 的界線在哪裡？
3. 腹瀉、黏膜炎、嗜中性球低下同時出現，是 irinotecan 還是 5-FU 的問題？UGT1A1 與 DPYD 要怎麼想？
4. 下一個週期怎麼決定？健保上有什麼要注意？

<details>
<summary>參考答案</summary>

1. **遲發性腹瀉**（輸注後 >24 小時；Camptosar 仿單每 3 週給藥的中位時間是第 5 天），比基線多 7 次／天，加上脫水與腎功能惡化需要住院，是 **CTCAE v5.0 G3**；口腔潰瘍痛到無法進食也是 G3 黏膜炎（[6.2](#62-irinotecan-與脂質體-irinotecan)）。第一小時：量生命徵象與直立性變化；IV 補液；補鉀並查鎂；肌酸酐 1.3 是腹瀉脫水造成的腎功能惡化，仿單也有這項警語；糞便檢查含 *C. difficile*；追蹤 CBC；**暫停化療**並通知主治醫師，住院。ANC 700/µL 且預期 48 小時內降到 <500，已符合嗜中性球低下的定義；T 37.9°C 還沒達到發燒標準（單次 ≥38.3°C，或 ≥38.0°C 持續 1 小時），但要密切監測體溫，一旦達標就走 FN 流程，分流後 60 分鐘內給抗生素（[腫瘤急症](00-shared/02-oncologic-emergencies.md#1-發燒性嗜中性球低下)第 1 節）。G2 以上合併嚴重嗜中性球低下、脫水，屬於升級條件：加 fluoroquinolone 類抗生素、octreotide 100–150 µg SC TID、住院（Benson et al., 2004；[支持性照護](00-shared/03-supportive-care.md#52-處置)第 5.2 節）。
2. **立刻停軟便劑**（Camptosar 仿單：腹瀉時避免利尿劑或軟便劑；Pharmacia & Upjohn, 2026）。loperamide：首劑 4 mg，之後每 2 小時 2 mg，直到無腹瀉至少 12 小時，**高劑量最多連續 48 小時**。這個方案持續下去 24 小時累積量可達約 28 mg，超過 loperamide 仿單每日 16 mg 的上限，有 QT 延長與 torsades de pointes 的加框警語（Advagen Pharma, 2026）；她 K 3.0 正是 QT 的風險因子，所以補鉀鎂與評估心電圖不能省。超過 48 小時還在拉，是升級的訊號（octreotide、住院），不是繼續加 loperamide。atropine 只針對輸注當天的早發性膽鹼症狀，她沒有，不需要。口腔照護見[支持性照護](00-shared/03-supportive-care.md#4-口腔黏膜炎)第 4 節，且含 oxaliplatin 的處方不可用冰塊含漱（[6.3](#63-oxaliplatin)）。
3. **兩者都可能，也可以並存，臨床上無法只靠症狀分開。** irinotecan 的活性代謝物 SN-38 由 UGT1A1 失活，\*28/\*28、\*6/\*6 或 \*6/\*28 的病人嚴重嗜中性球低下風險較高（Pharmacia & Upjohn, 2026）；5-FU 的 DPD 缺乏則造成第一個週期早發的嚴重黏膜炎、腹瀉、嗜中性球低下與神經毒性（Fresenius Kabi USA, 2026）。她的口腔潰瘍偏向 5-FU，但 irinotecan 也解釋得通。做法：通知主治醫師，抽 UGT1A1（\*28 與 \*6）與 DPYD 檢測，院內是否可做、是否給付，本手冊無法確認（[化療基礎](00-shared/01-chemo-basics.md#121-dpyd-與-fluoropyrimidine)第 12.1、12.2 節）。**怎麼用結果：** UGT1A1 \*28/\*28、\*6/\*6 或 \*6/\*28，下次 irinotecan 起始劑量考慮至少降 1 級，精確幅度未知；台灣 \*6 的對偶基因頻率約 13.0%（白人 0.5%），\*28 為 13.9%，只測 \*28 會漏掉 \*6（Chang et al., 2015）。DPYD：完全缺乏者避免 fluoropyrimidine，部分缺乏者個別化劑量；但西方常用的四個變異在東亞人很少見（Yokoi et al., 2020），**標準檢驗陰性不等於安全，推翻不了這次已經發生的嚴重毒性**。uridine triacetate 在 TFDA 2026-10-27 的資料查無藥證（[6.4](#64-5-fucapecitabine-與-s-1)）。
4. **重啟條件**（[5.5](#55-前置用藥止吐與給藥當天的門檻)）：ANC ≥1,500/mm³、PLT ≥100,000/mm³，腹瀉完全恢復且不靠止瀉藥已 ≥24 小時，黏膜炎降到 ≤G1；延後 1–2 週，2 週仍未恢復就考慮停用。**劑量：** 仿單對大腸直腸癌合併療法的規則是 G3 腹瀉恢復後減 1 個劑量等級（180 → 150 → 120 mg/m²）、發燒性嗜中性球低下減 2 級、G3–4 黏膜炎**只減 5-FU，不減 irinotecan**；但美國仿單沒有 FOLFIRINOX 專屬的調整表，她用的已是 150 mg/m² 的 mFOLFIRINOX，下一級是多少，由主治醫師與院內 protocol 決定（[6.2](#62-irinotecan-與脂質體-irinotecan) 的待核對說明）。若基因檢測顯示高風險，GnP 是不含 irinotecan 與 5-FU 的另一個第一線選項（[4.8](#48-轉移性第一線依體能分層)）。出院前用 teach-back 確認：一拉肚子先停軟便劑、馬上吃 loperamide、什麼情況要回診（[7.3](#73-46-小時幫浦接上拆除與居家衛教)）。**健保：** mFOLFIRINOX 仍走 9.10 第 3 點加 9.12.1 第 2 點（FOLFIRINOX，轉移性第一線；irinotecan 限指定品項），條文沒有規定劑量，減量不改變條文的適用；改成 GnP 算不算同一個第一線，原文沒有定義（[9.4](#94-依病人情境對照哪一段治療有條文)）。G-CSF 的 4.1.2.1 第 (4) 款要求「曾經發生」ANC <500/cumm，原文沒有界定是先前或本次療程，這次 ANC 若降到 <500，之後週期的 G-CSF 先向藥事確認（[支持性照護](00-shared/03-supportive-care.md#24-健保給付g-csf)第 2.4 節）。

</details>

### 個案三：置放支架的病人，GnP 後發燒

74 歲男性，轉移性胰頭 PDAC（肝轉移），4 個月前因黃疸置放**塑膠膽道支架**。第一線 GnP 第 3 週期，今天是 D8 給藥後第 3 天（週期第 11 天）。寒顫、發燒 39.2°C，右上腹痛，眼睛變黃 2 天。BP 88/52 mmHg，給 1 L 生理食鹽水後回到 100/62 mmHg，HR 112，意識清楚，SpO2 96%（室內空氣）。右胸壁 port 周圍無紅腫。Lab：WBC 2,100/µL、ANC 450/µL、PLT 128,000/µL、總膽紅素 5.8 mg/dL（上週 0.9）、ALP 510 U/L（上週 180）、肌酸酐 1.2 mg/dL、INR 1.3、lactate 2.8 mmol/L。ECOG 本來是 1，今天 2。

1. 這是哪幾個診斷的重疊？TG18 怎麼診斷、嚴重度幾級？
2. 第一小時依序要做什麼？為什麼不能只等 ANC 或只給抗生素？
3. 引流與抗生素各扮演什麼角色？後續的支架怎麼處理？
4. 化療何時、用什麼劑量重啟？還要和病人談什麼？

<details>
<summary>參考答案</summary>

1. **三個診斷重疊，不是三選一**（[7.6](#76-膽道支架與膽管炎的日常照護)）：①急性膽管炎（塑膠支架約 3 個月會堵塞，已 4 個月）；②發燒性嗜中性球低下（ANC 450 <500/µL，發燒 39.2°C）；③導管相關血流感染（有 port，需要從 port 與周邊各抽培養）。**TG18 診斷**（Kiriyama et al., 2018）：A 全身性發炎＝發燒、寒顫，WBC 2,100 <4,000；B 膽汁淤積＝總膽紅素 5.8 ≥2 mg/dL，ALP 510 >1.5 × ULN；C 影像＝膽管擴張或支架狀態，需 CT 或超音波確認；A、B、C 各至少一項為確定診斷，但臨床懷疑時不等影像就先處置。**嚴重度：Grade II。** 符合的條件有 WBC <4,000、發燒 ≥39°C、總膽紅素 ≥5 mg/dL（年齡 74 歲，未達 ≥75）；Grade III 要有新發的器官功能障礙，這位病人血壓輸液後回升且未用升壓劑、意識清楚、肌酸酐 1.2 <2.0、INR 1.3 <1.5、血小板 128,000 >100,000、SpO2 正常，所以不是 Grade III。但初始低血壓與 lactate 2.8 要密切再評估，一旦需要升壓劑或出現器官功能惡化就升為 Grade III（[8.1](#81-急性膽管炎acute-cholangitis)）。
2. **第一小時：** 生命徵象；**血液培養 2 套**（周邊 1 套，port 每個管腔各 1 套；抽不到不要拖延抗生素）；分流後 **60 分鐘內給第一劑經驗性廣效抗生素**，要同時涵蓋 FN 與膽道菌，選藥依 TG18 與院內抗生素政策（Gomi et al., 2018；[腫瘤急症](00-shared/02-oncologic-emergencies.md#12-立即處置第一小時)第 1.2 節）；IV 補液；CBC/DC、肝功能、lactate、肌酸酐、INR；**暫停化療**；立刻通知消化內科或介入放射科評估引流；通知主治醫師。不能只等 ANC：nab-paclitaxel 仿單把膽道阻塞與支架列為致命敗血症的危險因子，並要求發燒不論 ANC 都開廣效抗生素（Abraxis, 2022）。不能只給抗生素：Grade II 以上膽管炎需要早期引流，抗生素不能取代引流（Miura et al., 2018）。
3. **抗生素控制感染，引流解除阻塞，兩者缺一不可。** Grade II 要早期內視鏡（或經皮經肝）引流；ANC 與血小板低下對處置安全性的影響，由消化內科評估。堵塞的塑膠支架更換或另置，不可切除病人優先用 SEMS，膽管炎 8% 對 21%（Sawas et al., 2015；Dumonceau et al., 2018；[3.5](#35-膽道阻塞什麼時候要引流)）。培養結果回來後降階，用藥天數依 TG18（Gomi et al., 2018）。引流前不繼續化療。
4. **重啟條件：** 感染控制、退燒；膽紅素回到各藥門檻內（nab-paclitaxel 在胰臟癌 >1.5 × ULN 不建議使用；[5.7](#57-肝腎功能與膽紅素門檻速查)）。發燒性嗜中性球低下 G3–4：nab-paclitaxel 與 gemcitabine 兩藥都暫停到退燒且 ANC ≥1,500/mm³，再以**下一級劑量**恢復，也就是 100／800 mg/m²（Abraxis, 2022；[6.5](#65-nab-paclitaxel-與-gemcitabinegnp)）。之後的 D8、D15 依血球規則決定。G-CSF 的健保條件見[支持性照護](00-shared/03-supportive-care.md#24-健保給付g-csf)第 2.4 節。**要談的事：** 病人 ECOG 由 1 掉到 2，第 3 週期出現重症感染，這是重新討論治療目標的時機（[7.12](#712-緩和照護的整合)）；支架卡片與居家警訊（發燒 ≥38°C、黃疸復發、搔癢、茶色尿、右上腹痛）用 teach-back 確認；說明下次有症狀要當天回診，不要等下一次門診。

</details>

---

## 11. 自我測驗

**Q1.** 依台灣癌登 2023 年長表（AJCC 第 8 版），胰臟癌診斷時最常見的期別與約略比例為何？

A. I 期，約 40%　B. IV 期，約 51%　C. III 期，約 51%　D. II 期，約 40%

<details>
<summary>答案與詳解</summary>

**答案：B**。2023 年長表（n = 2,950）：IV 期 51.22%、II 期 17.56%、III 期 16.68%、I 期 12.64%，與美國 SEER 遠端轉移占 51% 幾乎一樣（本章 1.1、3.9）。補充：癌登的「胰臟癌」不等於 PDAC，腺癌只占 73.45%，NET 與 NEC 合計約 8.4%，引用數字前先確認分母。

</details>

**Q2.** 胰頭癌病人，pancreas-protocol CT 顯示 SMA 實質腫瘤接觸約 240°，SMV 通暢，沒有遠端轉移。NCCN 可切除性分類為何？

A. Resectable　B. Borderline resectable　C. Metastatic　D. Locally advanced

<details>
<summary>答案與詳解</summary>

**答案：D**。SMA 或 celiac axis 實質接觸 >180° 是 locally advanced；動脈接觸 ≤180° 是 borderline；靜脈只要能安全切除並重建就是 borderline，無法重建才是 locally advanced（本章 3.8；Corallo et al., 2025；Chu & Fishman, 2024）。治療分流看這個分類，不是看 AJCC 分期。

</details>

**Q3.** 胰頭癌病人總膽紅素 14 mg/dL，CA19-9 2,100 U/mL。下列處理何者最正確？

A. 膽道阻塞使 CA19-9 偽陽性，應在引流、膽紅素下降後重抽當基準值　B. CA19-9 超過 1,000 U/mL 即可確診，不需要病理　C. CA19-9 可作為一般成人的篩檢工具　D. Lewis-negative 的病人 CA19-9 會異常偏高

<details>
<summary>答案與詳解</summary>

**答案：A**。阻塞性黃疸使 CA19-9 偽陽性升到 10–60%，要在黃疸解除後重抽（Ballehaninna & Chamberlain, 2012；本章 3.4）。B 錯：化療前一定要有病理，首選 EUS-FNB。C 錯：無症狀人口的陽性預測值只有 0.5–0.9%。D 錯：Lewis-negative（約 5–10%）幾乎不產生 CA19-9，造成偽陰性。

</details>

**Q4.** 58 歲男性，胰頭癌合併黃疸（總膽紅素 12 mg/dL），影像明確可切除，外科預計診斷後約 1 週內手術。依隨機試驗證據，術前膽道引流的原則是？

A. 一律先放塑膠支架，引流 4–6 週後再手術　B. 一律先做經皮經肝膽道引流　C. 不常規術前引流，直接手術　D. 引流可降低手術死亡率，應常規進行

<details>
<summary>答案與詳解</summary>

**答案：C**。隨機試驗（膽紅素 40–250 µmol/L，即 2.3–14.6 mg/dL）：術前引流 4–6 週後再手術的嚴重併發症 74%，直接手術 39%（RR 0.54，0.41–0.71）；引流本身的併發症 46%（van der Gaag et al., 2010；本章 3.5）。例外是膽管炎、膽紅素 >250 µmol/L 且手術會延後超過 2 週、嚴重搔癢，以及要先做術前化療的病人。

</details>

**Q5.** 胰頭癌手術後病理：腫瘤最大徑 3.0 cm，4 顆區域淋巴結轉移，無遠端轉移。依 AJCC 第 8 版，期別為何？

A. IIB　B. III　C. IV　D. IIA

<details>
<summary>答案與詳解</summary>

**答案：B**。T 以大小分：>2 且 ≤4 cm 是 T2；N 以顆數分：1–3 顆是 N1，**≥4 顆是 N2**。任何 T 加 N2（或 T4）都是 III 期；T1–3 N1 才是 IIB（Allen et al., 2017；Rhee & Park, 2021；本章 3.7）。邊界值常考：T1 是 ≤2 cm，N2 是 ≥4 顆；外分泌胰臟癌是第 8 版，不是第 9 版。

</details>

**Q6.** 關於 PRODIGE 24（輔助 mFOLFIRINOX 對 gemcitabine），下列何者正確？

A. 5 年追蹤 OS 為 53.5 對 35.5 個月（HR 0.68），但試驗排除 Gilbert 症、UGT1A1\*28/\*28 與既存神經病變　B. 對照組是 gemcitabine ＋ capecitabine　C. 54.4 對 35.0 個月（HR 0.64）是 5 年的最終分析　D. 納入 UGT1A1\*28/\*28 與 Gilbert 症的病人，證明各基因型都安全

<details>
<summary>答案與詳解</summary>

**答案：A**。5 年數據：DFS 21.4 對 12.8 個月（HR 0.66），OS 53.5 對 35.5 個月（HR 0.68，0.54–0.85），5 年 OS 43.2% 對 31.4%（Conroy et al., 2022）。B 錯：對照組是 gemcitabine（GemCap 是 ESPAC-4 的實驗組）。C 錯：54.4 對 35.0、HR 0.64 是 2018 年的期中數據（Conroy et al., 2018）。D 錯：這些人被排除，所以 53.5 個月屬於篩選過的族群（本章 4.4、7.2）。

</details>

**Q7.** 58 歲男性，胰頭癌 Whipple 術後 8 週，ECOG 0，要開輔助 mFOLFIRINOX（PRODIGE 24 版本）。下列處方何者正確？

A. oxaliplatin 85、irinotecan 180、leucovorin 400 mg/m²，5-FU bolus 400 加 2,400 mg/m² 輸注 46 小時，共 24 次　B. oxaliplatin 60 mg/m²、Onivyde 50 mg/m²、leucovorin 400 mg/m²，5-FU 2,400 mg/m²，D1, 15 每 28 天　C. oxaliplatin 85、irinotecan 150、leucovorin 400 mg/m²，5-FU bolus 400 加 2,400 mg/m² 輸注 46 小時，共 12 次　D. oxaliplatin 85、irinotecan 150、leucovorin 400 mg/m²，5-FU 2,400 mg/m² 持續輸注 46 小時，無 bolus，每 2 週一次共 12 次

<details>
<summary>答案與詳解</summary>

**答案：D**。輔助 mFOLFIRINOX：irinotecan **150**、**無 5-FU bolus**、共 12 次（24 週）（Conroy et al., 2018；本章 5.1）。A 是轉移性 FOLFIRINOX（PRODIGE 4：irinotecan 180、加 bolus 400）的劑量，且週期數錯；B 是 NALIRIFOX（Onivyde 50 mg/m²，Wainberg et al., 2023）；C 多了 bolus。醫囑上要逐藥寫劑量，不要只寫「mFOLFIRINOX」。

</details>

**Q8.** 關於 Onivyde（liposomal irinotecan）的劑量，下列何者正確？

A. NALIRIFOX 的 Onivyde 是 70 mg/m²，UGT1A1\*28 同型合子要減為 50 mg/m²　B. 二線 nal-IRI ＋ 5-FU／leucovorin 的 70 mg/m² 以游離鹼計，相當於鹽類 80 mg/m²；UGT1A1\*28 同型合子起始 50 mg/m²，耐受後升到 70　C. Onivyde 與一般 irinotecan 可以用相同的 mg/m² 互換　D. NALIRIFOX 與二線方案都要加 5-FU bolus 400 mg/m²

<details>
<summary>答案與詳解</summary>

**答案：B**。二線 NAPOLI-1 方案 70 mg/m²（游離鹼）＝ 80 mg/m²（鹽類），\*28 同型合子從 50 起（Ipsen, 2025；本章 5.2）。A 錯：NALIRIFOX 是 50 mg/m² 且不因 UGT1A1\*28 減量。C 錯：仿單明寫不可用 Onivyde 取代含 irinotecan 的其他藥品。D 錯：兩個方案的 5-FU 都是 46 小時輸注、無 bolus。

</details>

**Q9.** 胰頭癌病人總膽紅素 2.5 mg/dL（正常上限 1.2 mg/dL），尚未引流。下列敘述何者正確？

A. nab-paclitaxel 在膽紅素 >3 × ULN 才不建議，此時可以開 GnP　B. FOLFIRINOX 的兩個關鍵試驗允許膽紅素 ≤3 × ULN　C. Onivyde 在膽紅素高於正常上限時沒有建議劑量，nab-paclitaxel（胰臟癌）>1.5 × ULN 不建議，irinotecan >2 mg/dL 沒有建議劑量，所以應先引流再排化療　D. gemcitabine 在膽紅素 >1.5 × ULN 是禁忌，其他藥可以照常

<details>
<summary>答案與詳解</summary>

**答案：C**。2.5 mg/dL 約 2.1 × ULN，同時超過 Onivyde、nab-paclitaxel 與 irinotecan（>2 mg/dL）的仿單門檻（Ipsen, 2025；Abraxis, 2022；Pharmacia & Upjohn, 2026；本章 5.7）。PRODIGE 4 與 PRODIGE 24 都要求 ≤1.5 × ULN（PRODIGE 4 允許先引流），所以 B 錯。順序是：引流、等膽紅素下降、再排化療。

</details>

**Q10.** FOLFIRINOX 的 irinotecan 輸注結束後 3 小時，病人流口水、冒汗、腹絞痛，心跳 52 次／分。最適合的處置是？

A. loperamide 首劑 4 mg　B. octreotide 100 µg 皮下注射　C. 停用軟便劑並補液即可　D. atropine 0.25–1 mg 靜脈或皮下注射

<details>
<summary>答案與詳解</summary>

**答案：D**。輸注中或 24 小時內的早發性（膽鹼性）症狀用 atropine 0.25–1 mg IV 或 SC；24 小時之後的遲發性水瀉才用 loperamide（首劑 4 mg，之後每 2 小時 2 mg，直到無腹瀉 ≥12 小時，高劑量最多連續 48 小時）（Pharmacia & Upjohn, 2026；本章 6.2）。octreotide 是 G2 以上遲發性腹瀉、24–48 小時未改善時的升級選項。

</details>

**Q11.** mFOLFIRINOX 給藥後第 2 天，病人喝冰水後手與喉嚨有刺痛和緊縮感，SpO2 99%、無喘鳴，12 天後緩解。最合適的判讀與衛教是？

A. 冷誘發的急性感覺異常；整個治療期間避冷（不喝冰飲、不碰冰冷物），確認無喘鳴且血氧正常，不必因此減量　B. 這是 anaphylaxis，應立即永久停用 oxaliplatin　C. 這是累積性神經病變 G3，應停用 oxaliplatin　D. 建議含冰塊預防口腔黏膜炎

<details>
<summary>答案與詳解</summary>

**答案：A**。oxaliplatin 的急性神經症狀在給藥後數小時至 2 天出現，冷誘發，14 天內緩解，下次給藥常再出現；咽喉感覺異常是主觀的吞嚥或呼吸困難，沒有喘鳴或支氣管痙攣（Meitheal, 2024；本章 6.3）。累積性神經病變是持續超過 14 天、劑量相關；真正的過敏反應（anaphylaxis）才是立即且永久停藥。含 oxaliplatin 的處方**不可**用冰塊含漱。

</details>

**Q12.** 台灣病人 FOLFIRINOX 第 1 週期後第 5 天出現 G3 腹瀉、G3 口腔黏膜炎、ANC 300/µL。下列何者最正確？

A. 西方常用的四個 DPYD 變異檢測陰性，即可排除 DPD 缺乏　B. 台灣只需檢測 UGT1A1\*28，因為 \*6 在東亞罕見　C. 早發的黏膜炎、腹瀉與嗜中性球低下要同時想到 DPYD（5-FU）與 UGT1A1（irinotecan），標準檢驗陰性不等於安全　D. uridine triacetate 在台灣已有藥證，可作為 5-FU 的解毒劑

<details>
<summary>答案與詳解</summary>

**答案：C**。5-FU 仿單：DPD 缺乏造成第一個週期早發的嚴重黏膜炎、腹瀉、嗜中性球低下與神經毒性（Fresenius Kabi USA, 2026）；irinotecan 的 UGT1A1\*28/\*28、\*6/\*6、\*6/\*28 嚴重嗜中性球低下風險較高（Pharmacia & Upjohn, 2026）。A 錯：西方常用的四個變異在東亞人很少見（Yokoi et al., 2020），陰性不等於安全。B 錯：台灣 \*6 的對偶基因頻率約 13.0%（白人 0.5%），\*28 為 13.9%（Chang et al., 2015）。D 錯：TFDA 2026-10-27 的資料查無此藥證（本章 6.2、6.4）。

</details>

**Q13.** 66 歲女性 GnP 第 1 週期第 8 天（nab-paclitaxel 125、gemcitabine 1,000 mg/m²，無神經病變），ANC 800/mm³、PLT 90,000/mm³。依 Abraxane 仿單，下列何者正確？

A. 兩藥照原劑量給　B. 兩藥各降 1 個劑量等級（nab-paclitaxel 100、gemcitabine 800 mg/m²）　C. 兩藥暫停　D. 只降 nab-paclitaxel，gemcitabine 維持 1,000 mg/m²

<details>
<summary>答案與詳解</summary>

**答案：B**。D8：ANC 500 至 <1,000 或 PLT 50,000 至 <75,000，兩藥降 1 級；ANC <500 或 PLT <50,000 暫停。這位病人 ANC 800 已落在降級範圍（PLT 90,000 本身不觸發）。劑量階梯 125／1,000 → 100／800 → 75／600 → 停用（Abraxis, 2022；本章 6.5、7.4）。D1 的門檻不同：ANC <1,500 或 PLT <100,000 就延後。

</details>

**Q14.** GnP 病人出現 3 級周邊感覺神經病變（影響扣釦子與寫字）。依仿單，處置是？

A. 暫停到 ≤1 級，以下一級劑量恢復 nab-paclitaxel，gemcitabine 不減量　B. 兩藥同步降 1 級　C. 只暫停 gemcitabine　D. 永久停用兩藥

<details>
<summary>答案與詳解</summary>

**答案：A**。血球低下造成的降級是兩藥同步降；**神經病變只降 nab-paclitaxel**，gemcitabine 不減量（Abraxis, 2022；本章 6.5）。MPACT 的 3–4 級神經病變 17%，改善到 ≤1 級的中位時間 29 天（Von Hoff et al., 2013）；輔助 APACT 的神經病變 62% 發生在第 4 個週期之後，是累積性的，每個週期都要問症狀（Tempero et al., 2023）。

</details>

**Q15.** 關於 olaparib 維持治療，下列何者正確？

A. POLO 的 OS 19.0 對 19.2 個月，證實 olaparib 顯著延長存活　B. 健保 9.85 給付胰臟癌 gBRCA 維持治療　C. 所有轉移性 PDAC 第一線化療後都可使用　D. 適用 germline BRCA1/2 變異、第一線含 platinum 方案至少 16 週未惡化者；POLO 的 PFS 7.4 對 3.8 個月（HR 0.53），OS 無顯著差異；台灣有藥證，但第 9 節 9.85 原文未見胰臟癌

<details>
<summary>答案與詳解</summary>

**答案：D**。POLO（篩檢 3,315 位、隨機 154 位）：PFS 7.4 對 3.8 個月，HR 0.53（0.35–0.82）；最終 OS 19.0 對 19.2 個月，HR 0.83（0.56–1.22），P = .3487，未達顯著（Golan et al., 2019；Kindler et al., 2022）。劑量 300 mg 每日兩次。台灣藥證與 POLO 族群相符（衛部藥輸字第027445、027446號），9.85 有條文但適應症不含胰臟癌，所以 A、B 錯；C 錯在需要 gBRCA1/2 與 platinum 反應（本章 4.9、9.5）。

</details>

**Q16.** 關於 daraxonrasib，下列何者正確？

A. 台灣已有藥證，並由 9.69 給付　B. 只對 KRAS G12C 有效，約占 PDAC 的 1.6%　C. RASolute 302（轉移性 PDAC 二線）OS 13.2 對 6.7 個月（HR 0.40）；美國 FDA 於 2026-08-26 核准；台灣沒有藥證，第 9 節原文也未收載　D. 第一線隨機試驗結果已在同儕審查期刊發表

<details>
<summary>答案與詳解</summary>

**答案：C**。RASolute 302：OS 13.2 對 6.7 個月（HR 0.40，0.30–0.53），PFS 7.2 對 3.6 個月，因治療相關不良反應停藥 1.2% 對 11.2%（O'Reilly et al., 2026）；300 mg 每日一次。它是 RAS(ON) 抑制劑，不挑 G12、G13 或 Q61 突變，涵蓋約 83–89% 的 PDAC（KRAS 突變的比例），不是 G12C 專一藥（B 錯）。TFDA 2026-10-27 的資料查無此藥，第一線數據截至 2026-10-29 尚未發表（本章 4.10、9.5）。

</details>

**Q17.** 74 歲男性，轉移性胰頭癌置放塑膠膽道支架 4 個月，GnP 化療期間發燒 39.2°C、寒顫，總膽紅素 5.8 mg/dL，WBC 2,100/µL，血壓輸液後回升、意識清楚、肌酸酐 1.2 mg/dL。依 TG18，嚴重度與處置為何？

A. Grade II，抗生素加早期引流，抗生素不能取代引流　B. Grade I，只給抗生素觀察　C. Grade III，必須先放升壓劑，不需要引流　D. 不符合診斷，等 ANC 回升再評估

<details>
<summary>答案與詳解</summary>

**答案：A**。Grade II 是下列任兩項：WBC >12,000 或 <4,000/µL、發燒 ≥39°C、年齡 ≥75、總膽紅素 ≥5 mg/dL、白蛋白 <正常下限 × 0.7；這位病人有三項。Grade III 要有新發的器官功能障礙（需升壓劑、意識障礙、PaO₂/FiO₂ <300、肌酸酐 >2.0 mg/dL、INR >1.5、血小板 <100,000/mm³），他沒有。Grade II 要早期內視鏡或經皮經肝引流（Kiriyama et al., 2018；Miura et al., 2018；本章 8.1）。同時要走 FN 流程，血液培養含 port，60 分鐘內給抗生素。

</details>

**Q18.** 胰臟癌病人油亮、浮水、惡臭的大便，體重下降，要開 Creon 25000。下列何者正確？

A. 每次 10,000 單位 lipase，三餐飯後固定給　B. 每個主餐 40,000–50,000 單位 lipase，點心減半，隨餐服用；沒有反應先確認時機與順從性，再加量，最後加 PPI　C. 以膠囊顆數計算，不需要看 lipase 單位　D. 禁食或管灌時照常每餐給

<details>
<summary>答案與詳解</summary>

**答案：B**。歐洲 PEI 指引的起始劑量是主餐 40,000–50,000 單位 lipase、點心 20,000–25,000 單位；用 Creon 25000 就是正餐 2 顆、點心 1 顆（Dominguez-Muñoz et al., 2025；本章 5.6）。要看 lipase 單位，不是顆數；醫囑寫「隨餐」，不要排進固定的飯後時間。禁食或管灌時是否給、怎麼給，與營養科和主治醫師確認。健保 7.3.6（110/1/1）申報要檢附胰液分泌不全與營養不良或脂肪痢便的記載。

</details>

**Q19.** 一位轉移性胰臟癌病人，血小板 380,000/µL、Hb 12.5 g/dL、WBC 8,000/µL、BMI 22，準備開始門診化療。其 Khorana 分數是？

A. 3　B. 2　C. 4　D. 1

<details>
<summary>答案與詳解</summary>

**答案：A**。胰臟癌的部位項目 2 分，血小板 ≥350,000/µL 加 1 分，Hb、WBC、BMI 皆未達門檻，共 3 分，屬高風險（Khorana et al., 2008；本章 7.10）。但亞洲（含台灣）的 VTE 發生率較低，Pan-Asian ESMO 把常規預防性抗凝降為「無禁忌時可以考慮」；開始前要先看基線影像有沒有已存在的血栓，並評估出血風險（腫瘤是否侵犯胃或十二指腸、血小板、膽道支架）。

</details>

**Q20.** 黃疸合併無痛、可觸及的膽囊，最能提示下列何者？

A. Trousseau's sign，低血鈣　B. Trousseau's syndrome，癌症相關血栓　C. Courvoisier sign，提示惡性的遠端膽道阻塞，例如胰頭癌　D. Murphy's sign，急性膽囊炎

<details>
<summary>答案與詳解</summary>

**答案：C**。Courvoisier sign 是黃疸加無痛、可觸及的膽囊，提示惡性遠端膽道阻塞；Courvoisier 1890 年只是描述 187 例膽道阻塞，從未提出「定律」（Fitzgerald et al., 2009；本章 3.1）。Trousseau's syndrome 是癌症相關的血栓傾向，胰臟癌是經典病因（Varki, 2007）；Trousseau's sign 是低血鈣時血壓計袖帶誘發的手足痙攣，兩者不要混淆。本手冊未取得 Courvoisier sign 的敏感度，只把它當作提示。

</details>

**Q21.** 依 115/10/22 版藥品給付規定，下列哪一個轉移性胰臟癌用藥的條文**明文**規定「需經事前審查核准後使用」？

A. oxaliplatin（9.10）　B. albumin-bound paclitaxel（9.5.2）　C. S-1（9.46）　D. irinotecan liposome（Onivyde，9.12.2）

<details>
<summary>答案與詳解</summary>

**答案：D**。9.12.2 第 3 點「需經事前審查核准後使用」，適用第一線（第 2 點）與二線（第 1 點）；原文沒有訂審查週期。9.4 gemcitabine、9.5.2、9.10、9.12.1、9.46 對胰臟癌都沒有事前審查規定。胰臟癌相關的四個事前審查藥是 Onivyde、larotrectinib（9.95，每次 12 週）、sunitinib（9.31，pNET）與 everolimus（9.36.1，pNET，每次 3 個月）（本章 9.0、9.1）。

</details>

**Q22.** 轉移性 PDAC 第一線 FOLFIRINOX 惡化，主治醫師想二線改 GnP。照 115/10/22 版 9.5.2 的字面，下列何者正確？

A. 9.5.2 給付轉移性二線，需事前審查　B. 9.5.2 只寫「限併用 gemcitabine，作為轉移性胰腺癌患者之第一線治療」，二線 GnP 的 nab-paclitaxel 原文沒有對應條文；gemcitabine 本身（9.4）未限線別　C. 9.5.2 允許 albumin-bound paclitaxel 單用　D. albumin-bound paclitaxel 與 paclitaxel 注射劑（9.5.1）可以互相替代申報

<details>
<summary>答案與詳解</summary>

**答案：B**。9.5.2（108/11/1）限第一線、限併用 gemcitabine，沒有事前審查，也沒有二線條文；9.5.1 的 paclitaxel 注射劑各點都沒有胰臟癌適應症，兩者是不同條文，劑型也不能互相替代（Abraxis, 2022）。FOLFIRINOX 失敗後改 GnP 的給付，原文看不出來，送審前向藥事部門確認（本章 9.1、9.4）。

</details>

**Q23.** 下列敘述何者符合 9.95 對胰臟癌的給付？

A. 剛確診、尚未治療的 NTRK 融合轉移性病人可作為第一線給付　B. entrectinib 與 larotrectinib 都給付 NTRK 融合胰臟癌　C. 成人 NTRK 基因融合胰臟癌，先前至少一次全身性治療失敗又有疾病惡化，無法手術切除或轉移性；需事前審查，每次 12 週，檢測報告須符合通則十二　D. 不需檢附 NTRK 基因融合檢測報告

<details>
<summary>答案與詳解</summary>

**答案：C**。9.95 第 3 點 (4) 的成人胰臟癌要求先前至少一次全身性治療失敗又惡化（A 錯）；第 1 點另要求無已知後天阻抗性突變、轉移性（或手術切除極可能造成嚴重病症）、沒有合適的替代治療（含免疫檢查點抑制劑）；第 4 點需事前審查，初次申請須附 NTRK 1/2/3 檢測報告並符合通則十二（D 錯），再次申請須附療效評估證實無疾病進展。entrectinib（9.93）與 repotrectinib（9.131）有藥證，但原文未見 NTRK 或胰臟癌（B 錯）（本章 9.2、9.5）。

</details>

**Q24.** 胰臟癌病人併有蝕骨性骨轉移，依 115/10/22 版，下列何者正確？

A. zoledronic acid 4 mg 的骨轉移適應症列有胰癌　B. denosumab 要事前審查，且不含胰癌　C. 骨轉移用藥全部在第 9 節　D. denosumab（Xgeva，5.5.4）的適應症列有胰癌；zoledronic acid 4 mg（5.5.3.2.1）的骨轉移適應症只列多發性骨髓瘤、乳癌、前列腺癌

<details>
<summary>答案與詳解</summary>

**答案：D**。5.5.4（113/10/1）列名的癌別包括胰癌；5.5.3.2.1（100/1/1）的骨轉移適應症只有多發性骨髓瘤、乳癌、前列腺癌，不含胰癌。兩者都不在第 9 節，也都沒有事前審查，條文沒有規定給藥間隔或總療程。pamidronate／clodronate（5.5.3.1）第 2 款不限癌別，但要求使用止痛劑後仍不易控制（本章 9.6；[支持性照護](00-shared/03-supportive-care.md#83-健保給付骨骼保護劑)第 8.3 節）。

</details>

---

## 12. 參考文獻

APA 第 7 版。作者超過 20 位時列前 19 位、省略號與最後一位。期刊文章附 DOI 與 PMID，並於 2026-11-01 以 PubMed 收錄資料逐筆核對 DOI、第一作者與年份。藥品仿單取自 DailyMed／openFDA（2026-10-29 至 2026-11-01 查詢），列出仿單版本與生效日。NCCN 專業版全文未能開啟，本章引用的專業版內容限於已發表的 JNCCN 版本（Ko et al., 2026，僅取得摘要）；病人版另列。台灣官方資料與健保、藥證資料列在最後。

Aaquist, T., Fristrup, C. W., Hasselby, J. P., Hamilton-Dutoit, S., Eld, M., Pfeiffer, P., Mortensen, M. B., & Detlefsen, S. (2024). Prognostic value of margin clearance in total and distal pancreatectomy specimens with pancreatic ductal adenocarcinoma in a Danish population-based nationwide study. *Pathology, Research and Practice, 254*, Article 155077. https://doi.org/10.1016/j.prp.2023.155077（PMID: 38277754）

Abraxis. (2022). *Abraxane (paclitaxel protein-bound particles for injectable suspension) (albumin-bound)* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=24d10449-2936-4cd3-b7db-a7683db721e4（版本日期 2022-10-31）

Acharya, T., Spathis, A., Godfrey, E., Corbett, G., Kuhn, I., & Etkind, S. N. (2026). Palliative management of malignant gastric outlet obstruction: A practice review. *Palliative Medicine, 40*(3), 333–343. https://doi.org/10.1177/02692163251403430（PMID: 41454660）

Advagen Pharma. (2026). *Loperamide hydrochloride capsules* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=03c907d5-87f8-47a6-9544-5a24f5272739（版本日期 2026-01-05）

Ai, X., Song, Z., Wu, L., Zhou, A., Cheng, D., Zong, H., Wu, H., Niu, Z., Sun, Y., Zhu, L., Li, Z., Deng, Y., Yuan, Y., Qu, X., Zhao, H., Du, Y., Li, Z., Wang, Y., Shen, H., . . . Lu, S. (2026). Oral KRAS G12D inhibitor GFH375 for previously treated advanced solid tumors with KRAS G12D mutations: A phase 1 trial. *Nature Medicine, 32*(9), 3302–3312. https://doi.org/10.1038/s41591-026-04559-4（PMID: 42745055）

Allen, M. J., Zhang, A., Bavi, P., Kim, J. C., Jang, G. H., Kelly, D., Perera, S., Denroche, R. E., Notta, F., Wilson, J. M., Dodd, A., Ramotar, S., Hutchinson, S., Fischer, S. E., Grant, R. C., Gallinger, S., Knox, J. J., & O'Kane, G. M. (2023). Molecular characterisation of pancreatic ductal adenocarcinoma with NTRK fusions and review of the literature. *Journal of Clinical Pathology, 76*(3), 158–165. https://doi.org/10.1136/jclinpath-2021-207781（PMID: 34583947）

Allen, P. J., Gönen, M., Brennan, M. F., Bucknor, A. A., Robinson, L. M., Pappas, M. M., Carlucci, K. E., D'Angelica, M. I., DeMatteo, R. P., Kingham, T. P., Fong, Y., & Jarnagin, W. R. (2014). Pasireotide for postoperative pancreatic fistula. *New England Journal of Medicine, 370*(21), 2014–2022. https://doi.org/10.1056/NEJMoa1313688（PMID: 24849084）

Allen, P. J., Kuk, D., Fernández-del Castillo, C., Basturk, O., Wolfgang, C. L., Cameron, J. L., Lillemoe, K. D., Ferrone, C. R., Morales-Oyarvide, V., He, J., Weiss, M. J., Hruban, R. H., Gönen, M., Klimstra, D. S., & Mino-Kenudson, M. (2017). Multi-institutional validation study of the American Joint Commission on Cancer (8th edition) changes for T and N staging in patients with pancreatic adenocarcinoma. *Annals of Surgery, 265*(1), 185–191. https://doi.org/10.1097/SLA.0000000000001763（PMID: 27163957）

American Diabetes Association Professional Practice Committee. (2024). 6. Glycemic goals and hypoglycemia: Standards of care in diabetes—2024. *Diabetes Care, 47*(Suppl. 1), S111–S125. https://doi.org/10.2337/dc24-S006（PMID: 38078586）

American Diabetes Association Professional Practice Committee for Diabetes. (2026). 6. Glycemic goals, hypoglycemia, and hyperglycemic crises: Standards of care in diabetes—2026. *Diabetes Care, 49*(Suppl. 1), S132–S149. https://doi.org/10.2337/dc26-S006（PMID: 41358894）

Andel, P. C. M., van Goor, I. W. J. M., Augustinus, S., Berrevoet, F., Besselink, M. G., Bhojwani, R., Boggi, U., Bouwense, S. A. W., Cirkel, G. A., van Dam, J. L., Djanani, A., Dorcaratto, D., Dreyer, S., den Dulk, M., Frigerio, I., Ghorbani, P., Goetz, M. R., Groot Koerkamp, B., Gryspeerdt, F., . . . van Santvoort, H. C. (2025). Routine imaging or symptomatic follow-up after resection of pancreatic adenocarcinoma. *JAMA Surgery, 160*(1), 74–84. https://doi.org/10.1001/jamasurg.2024.5024（PMID: 39504033）

Arcidiacono, P. G., Calori, G., Carrara, S., McNicol, E. D., & Testoni, P. A. (2011). Celiac plexus block for pancreatic cancer pain in adults. *Cochrane Database of Systematic Reviews, 2011*(3), CD007519. https://doi.org/10.1002/14651858.CD007519.pub2（PMID: 21412903）

Arvanitakis, M., Ockenga, J., Bezmarevic, M., Gianotti, L., Krznarić, Ž., Lobo, D. N., Löser, C., Madl, C., Meier, R., Phillips, M., Rasmussen, H. H., Van Hooft, J. E., & Bischoff, S. C. (2024). ESPEN practical guideline on clinical nutrition in acute and chronic pancreatitis. *Clinical Nutrition, 43*(2), 395–412. https://doi.org/10.1016/j.clnu.2023.12.019（PMID: 38169174）

AstraZeneca. (2025). *Lynparza (olaparib) tablets* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=741ff3e3-dc1a-45a6-84e5-2481b27131aa（版本日期 2025-07-10）

Atasilp, C., Biswas, M., Jinda, P., Nuntharadthanaphong, N., Rachanakul, J., Hongkaew, Y., Vanwong, N., Saokaew, S., & Sukasem, C. (2022). Association of UGT1A1*6, UGT1A1*28, or ABCC2 c.3972C>T genetic polymorphisms with irinotecan-induced toxicity in Asian cancer patients: Meta-analysis. *Clinical and Translational Science, 15*(7), 1613–1633. https://doi.org/10.1111/cts.13277（PMID: 35506159）

Auvray Kuentz, M., Hautefeuille, V., de Mestier, L., Coutzac, C., Lecomte, T., Nardon, V., Artru, P., Turpin, A., Drouillard, A., Malka, D., Tran-Minh, M.-L., Trouilloud, I., Lièvre, A., Williet, N., Pernot, S., Touchefeu, Y., Taieb, J., Hammel, P., & Zaanan, A. (2023). Chemotherapy in advanced pancreatic adenosquamous carcinoma: A retrospective multicenter AGEO study. *International Journal of Cancer, 152*(9), 1894–1902. https://doi.org/10.1002/ijc.34414（PMID: 36562310）

Ballehaninna, U. K., & Chamberlain, R. S. (2012). The clinical utility of serum CA 19-9 in the diagnosis, prognosis and management of pancreatic adenocarcinoma: An evidence based appraisal. *Journal of Gastrointestinal Oncology, 3*(2), 105–119. https://doi.org/10.3978/j.issn.2078-6891.2011.021（PMID: 22811878）

Bassi, C., Marchegiani, G., Dervenis, C., Sarr, M., Abu Hilal, M., Adham, M., Allen, P., Andersson, R., Asbun, H. J., Besselink, M. G., Conlon, K., Del Chiaro, M., Falconi, M., Fernandez-Cruz, L., Fernandez-Del Castillo, C., Fingerhut, A., Friess, H., Gouma, D. J., Hackert, T., . . . Buchler, M. (2017). The 2016 update of the International Study Group (ISGPS) definition and grading of postoperative pancreatic fistula: 11 years after. *Surgery, 161*(3), 584–591. https://doi.org/10.1016/j.surg.2016.11.014（PMID: 28040257）

Bekaii-Saab, T. S., Yaeger, R., Spira, A. I., Pelster, M. S., Sabari, J. K., Hafez, N., Barve, M., Velastegui, K., Yan, X., Shetty, A., Der-Torossian, H., & Pant, S. (2023). Adagrasib in advanced solid tumors harboring a KRAS G12C mutation. *Journal of Clinical Oncology, 41*(25), 4097–4106. https://doi.org/10.1200/JCO.23.00434（PMID: 37099736）

Bengtsson, A., Andersson, R., & Ansari, D. (2024). Histological variants of pancreatic ductal adenocarcinoma: A survival analysis. *Langenbeck's Archives of Surgery, 409*(1), Article 312. https://doi.org/10.1007/s00423-024-03506-6（PMID: 39425752）

Ben, Q., Xu, M., Ning, X., Liu, J., Hong, S., Huang, W., Zhang, H., & Li, Z. (2011). Diabetes mellitus and risk of pancreatic cancer: A meta-analysis of cohort studies. *European Journal of Cancer, 47*(13), 1928–1937. https://doi.org/10.1016/j.ejca.2011.03.003（PMID: 21458985）

Benson, A. B., Ajani, J. A., Catalano, R. B., Engelking, C., Kornblau, S. M., Martenson, J. A., McCallum, R., Mitchell, E. P., O'Dorisio, T. M., Vokes, E. E., & Wadler, S. (2004). Recommended guidelines for the treatment of cancer treatment-induced diarrhea. *Journal of Clinical Oncology, 22*(14), 2918–2926. https://doi.org/10.1200/JCO.2004.04.132（PMID: 15254061）

Besselink, M. G., van Rijssen, L. B., Bassi, C., Dervenis, C., Montorsi, M., Adham, M., Asbun, H. J., Bockhorn, M., Strobel, O., Büchler, M. W., Busch, O. R., Charnley, R. M., Conlon, K. C., Fernández-Cruz, L., Fingerhut, A., Friess, H., Izbicki, J. R., Lillemoe, K. D., Neoptolemos, J. P., . . . Gouma, D. J. (2017). Definition and classification of chyle leak after pancreatic operation: A consensus statement by the International Study Group on Pancreatic Surgery. *Surgery, 161*(2), 365–372. https://doi.org/10.1016/j.surg.2016.06.058（PMID: 27692778）

Birkmeyer, J. D., Siewers, A. E., Finlayson, E. V. A., Stukel, T. A., Lucas, F. L., Batista, I., Welch, H. G., & Wennberg, D. E. (2002). Hospital volume and surgical mortality in the United States. *New England Journal of Medicine, 346*(15), 1128–1137. https://doi.org/10.1056/NEJMsa012337（PMID: 11948273）

Bosetti, C., Lucenteforte, E., Silverman, D. T., Petersen, G., Bracci, P. M., Ji, B. T., Negri, E., Li, D., Risch, H. A., Olson, S. H., Gallinger, S., Miller, A. B., Bueno-de-Mesquita, H. B., Talamini, R., Polesel, J., Ghadirian, P., Baghurst, P. A., Zatonski, W., Fontham, E., . . . La Vecchia, C. (2012). Cigarette smoking and pancreatic cancer: An analysis from the International Pancreatic Cancer Case-Control Consortium (Panc4). *Annals of Oncology, 23*(7), 1880–1888. https://doi.org/10.1093/annonc/mdr541（PMID: 22104574）

Cancer Genome Atlas Research Network. (2017). Integrated genomic characterization of pancreatic ductal adenocarcinoma. *Cancer Cell, 32*(2), 185–203.e13. https://doi.org/10.1016/j.ccell.2017.07.007（PMID: 28810144）

Carrier, M., Abou-Nassar, K., Mallick, R., Tagalakis, V., Shivakumar, S., Schattner, A., Kuruvilla, P., Hill, D., Spadafora, S., Marquis, K., Trinkaus, M., Tomiak, A., Lee, A. Y. Y., Gross, P. L., Lazo-Langner, A., El-Maraghi, R., Goss, G., Le Gal, G., Stewart, D., . . . Wells, P. S. (2019). Apixaban to prevent venous thromboembolism in patients with cancer. *New England Journal of Medicine, 380*(8), 711–719. https://doi.org/10.1056/NEJMoa1814468（PMID: 30511879）

Chang, J. S., Chen, L.-T., Shan, Y.-S., Chu, P.-Y., Tsai, C.-R., & Tsai, H.-J. (2018). The incidence and survival of pancreatic cancer by histology, including rare subtypes: A nation-wide cancer registry-based study from Taiwan. *Cancer Medicine, 7*(11), 5775–5788. https://doi.org/10.1002/cam4.1795（PMID: 30264519）

Chang, T. C., Shiah, H. S., Yang, C. H., Yeh, K. H., Cheng, A. L., Shen, B. N., Wang, Y. W., Yeh, C. G., Chiang, N. J., Chang, J. Y., & Chen, L. T. (2015). Phase I study of nanoliposomal irinotecan (PEP02) in advanced solid tumor patients. *Cancer Chemotherapy and Pharmacology, 75*(3), 579–586. https://doi.org/10.1007/s00280-014-2671-x（PMID: 25577133）

Chari, S. T., Leibson, C. L., Rabe, K. G., Ransom, J., de Andrade, M., & Petersen, G. M. (2005). Probability of pancreatic cancer following diabetes: A population-based study. *Gastroenterology, 129*(2), 504–511. https://doi.org/10.1016/j.gastro.2005.05.007（PMID: 16083707）

Cheng, S. M., Su, Y.-Y., Chiang, N.-J., Wang, C.-J., Chao, Y.-J., Huang, C.-J., Tsai, H.-J., Chen, S.-H., Chang, C.-Y., Tsai, C.-R., Li, Y.-J., Yen, C.-J., Chuang, S.-C., Chang, J. S.-M., Shan, Y.-S., Hwang, D.-Y., & Chen, L.-T. (2024). Germline mutations of homologous recombination genes and clinical outcomes in pancreatic cancer: A multicenter study in Taiwan. *Journal of Biomedical Science, 31*(1), Article 21. https://doi.org/10.1186/s12929-024-01008-7（PMID: 38350919）

Chen, J.-S., Hung, C.-Y., Chang, H., Liu, C.-T., Chen, Y.-Y., Lu, C.-H., Chang, P.-H., Hung, Y.-S., & Chou, W.-C. (2018). Venous thromboembolism in Asian patients with pancreatic cancer following palliative chemotherapy: Low incidence but a negative prognosticator for those with early onset. *Cancers, 10*(12), Article 501. https://doi.org/10.3390/cancers10120501（PMID: 30544670）

Chiasakul, T., Patell, R., Maraveyas, A., Carrier, M., & Zwicker, J. I. (2021). Discordant reporting of VTE in pancreatic cancer: A systematic review and meta-analysis of thromboprophylaxis versus chemotherapeutic trials. *Journal of Thrombosis and Haemostasis, 19*(2), 489–501. https://doi.org/10.1111/jth.15175（PMID: 33174368）

Chu, L. C., & Fishman, E. K. (2024). Pancreatic ductal adenocarcinoma staging: A narrative review of radiologic techniques and advances. *International Journal of Surgery, 110*(10), 6052–6063. https://doi.org/10.1097/JS9.0000000000000899（PMID: 38085802）

Chung, A.-K., Lin, R.-T., Yeh, C.-C., Yang, C.-Y., Wu, C.-J., Chen, P.-L., & Lin, J.-T. (2023). Diagnostic rate of germline pathogenic variants in pancreatic ductal adenocarcinoma patients using whole genome sequencing. *Frontiers in Genetics, 14*, Article 1172365. https://doi.org/10.3389/fgene.2023.1172365（PMID: 37234870）

Cohen, O., Caiano, L. M., & Levy-Mendelovich, S. (2024). Cancer-associated splanchnic vein thrombosis: Clinical implications and management considerations. *Thrombosis Research, 234*, 75–85. https://doi.org/10.1016/j.thromres.2023.12.014（PMID: 38183815）

Conroy, T., Castan, F., Lopez, A., Turpin, A., Ben Abdelghani, M., Wei, A. C., Mitry, E., Biagi, J. J., Evesque, L., Artru, P., Lecomte, T., Assenat, E., Bauguion, L., Ychou, M., Bouché, O., Monard, L., Lambert, A., & Hammel, P. (2022). Five-year outcomes of FOLFIRINOX vs gemcitabine as adjuvant therapy for pancreatic cancer: A randomized clinical trial. *JAMA Oncology, 8*(11), 1571–1578. https://doi.org/10.1001/jamaoncol.2022.3829（PMID: 36048453）

Conroy, T., Desseigne, F., Ychou, M., Bouché, O., Guimbaud, R., Bécouarn, Y., Adenis, A., Raoul, J. L., Gourgou-Bourgade, S., de la Fouchardière, C., Bennouna, J., Bachet, J. B., Khemissa-Akouz, F., Péré-Vergé, D., Delbaldo, C., Assenat, E., Chauffert, B., Michel, P., Montoto-Grillot, C., & Ducreux, M. (2011). FOLFIRINOX versus gemcitabine for metastatic pancreatic cancer. *New England Journal of Medicine, 364*(19), 1817–1825. https://doi.org/10.1056/NEJMoa1011923（PMID: 21561347）

Conroy, T., Hammel, P., Hebbar, M., Ben Abdelghani, M., Wei, A. C., Raoul, J. L., Choné, L., Francois, E., Artru, P., Biagi, J. J., Lecomte, T., Assenat, E., Faroux, R., Ychou, M., Volet, J., Sauvanet, A., Breysacher, G., Di Fiore, F., Cripps, C., . . . Bachet, J. B. (2018). FOLFIRINOX or gemcitabine as adjuvant therapy for pancreatic cancer. *New England Journal of Medicine, 379*(25), 2395–2406. https://doi.org/10.1056/NEJMoa1809775（PMID: 30575490）

Corallo, C., Al-Adhami, A. S., Jamieson, N., Valle, J., Radhakrishna, G., Moir, J., & Albazaz, R. (2025). An update on pancreatic cancer imaging, staging, and use of the PACT-UK radiology template pre- and post-neoadjuvant treatment. *British Journal of Radiology, 98*(1165), 13–26. https://doi.org/10.1093/bjr/tqae217（PMID: 39460945）

Cui, J., Jiang, K., Li, W., Ni, S., Zong, H., Du, J., He, Y., Liu, Z., Kong, G., Zhang, Y., Li, X., Han, H., Yao, F., Chen, Y., Zhou, M., & Wang, L. (2026). KRAS-G12D inhibitor HRS-4642 plus chemotherapy in advanced KRAS G12D-mutant pancreatic cancer: A phase 1b/2 trial. *Nature Medicine, 32*(9), 3294–3301. https://doi.org/10.1038/s41591-026-04538-9（PMID: 42426224）

de Jesus, V. H. F., & Riechelmann, R. P. (2021). Comparative efficacy of modified FOLFIRINOX, gemcitabine plus capecitabine and gemcitabine plus nab-paclitaxel as adjuvant treatment for resected pancreatic cancer: A Bayesian network meta-analysis. *Ecancermedicalscience, 15*, 1276. https://doi.org/10.3332/ecancer.2021.1276（PMID: 34567261）

Delpero, J. R., Jeune, F., Bachellier, P., Regenet, N., Le Treut, Y. P., Paye, F., Carrere, N., Sauvanet, A., Adham, M., Autret, A., Poizat, F., Turrini, O., & Boher, J. M. (2017). Prognostic value of resection margin involvement after pancreaticoduodenectomy for ductal adenocarcinoma: Updates from a french prospective multicenter study. *Annals of Surgery, 266*(5), 787–796. https://doi.org/10.1097/SLA.0000000000002432（PMID: 28953554）

Demols, A., Rocq, L., Perez-Casanova, L., Charry, M., De Nève, N., Ramadhan, A., Van Campenhout, C., De Clercq, S., Maris, C., Closset, J., Lucidi, V., Salmon, I., & D'Haene, N. (2023). A two-step diagnostic approach for NTRK gene fusion detection in biliary tract and pancreatic adenocarcinomas. *The Oncologist, 28*(7), e520–e525. https://doi.org/10.1093/oncolo/oyad075（PMID: 36994874）

Ding, X., Zhu, J., Zhu, M., Li, C., Jian, W., Jiang, J., Wang, Z., Hu, S., & Jiang, X. (2011). Therapeutic management of hemorrhage from visceral artery pseudoaneurysms after pancreatic surgery. *Journal of Gastrointestinal Surgery, 15*(8), 1417–1425. https://doi.org/10.1007/s11605-011-1561-3（PMID: 21584822）

Doebele, R. C., Drilon, A., Paz-Ares, L., Siena, S., Shaw, A. T., Farago, A. F., Blakely, C. M., Seto, T., Cho, B. C., Tosi, D., Besse, B., Chawla, S. P., Bazhenova, L., Krauss, J. C., Chae, Y. K., Barve, M., Garrido-Laguna, I., Liu, S. V., Conkling, P., . . . Demetri, G. D. (2020). Entrectinib in patients with advanced or metastatic NTRK fusion-positive solid tumours: Integrated analysis of three phase 1–2 trials. *The Lancet Oncology, 21*(2), 271–282. https://doi.org/10.1016/S1470-2045(19)30691-6（PMID: 31838007）

Dominguez-Muñoz, J. E., Vujasinovic, M., de la Iglesia, D., Cahen, D., Capurso, G., Gubergrits, N., Hegyi, P., Hungin, P., Ockenga, J., Paiella, S., Perkhofer, L., Rebours, V., Rosendahl, J., Salvia, R., Scheers, I., Szentesi, A., Bonovas, S., Piovani, D., & Löhr, J. M. (2025). European guidelines for the diagnosis and treatment of pancreatic exocrine insufficiency: UEG, EPC, EDS, ESPEN, ESPGHAN, ESDO, and ESPCG evidence-based recommendations. *United European Gastroenterology Journal, 13*(1), 125–172. https://doi.org/10.1002/ueg2.12674（PMID: 39639485）

Duke, E. S., Bradford, D., Marcovitz, M., Amatya, A. K., Mishra-Kalyani, P. S., Nguyen, E., Price, L. S. L., Fourie Zirkelbach, J., Li, Y., Bi, Y., Kraft, J., Dorff, S. E., Scepura, B., Stephenson, M., Ojofeitimi, I., Nair, A., Han, Y., Tezak, Z., Lemery, S. J., . . . Singh, H. (2023). FDA approval summary: Selpercatinib for the treatment of advanced RET fusion-positive solid tumors. *Clinical Cancer Research, 29*(18), 3573–3578. https://doi.org/10.1158/1078-0432.ccr-23-0459（PMID: 37265412）

Dumonceau, J.-M., Tringali, A., Papanikolaou, I. S., Blero, D., Mangiavillano, B., Schmidt, A., Vanbiervliet, G., Costamagna, G., Devière, J., García-Cano, J., Gyökeres, T., Hassan, C., Prat, F., Siersema, P. D., & van Hooft, J. E. (2018). Endoscopic biliary stenting: Indications, choice of stents, and results: European Society of Gastrointestinal Endoscopy (ESGE) Clinical Guideline — updated October 2017. *Endoscopy, 50*(9), 910–930. https://doi.org/10.1055/a-0659-9864（PMID: 30086596）

Ecker, B. L., Seier, K., Choubey, A., Eckhoff, A. M., Tortorello, G. N., Balachandran, V. P., Blackburn, N., D'Angelica, M. I., DeMatteo, R. P., Blazer, D. G., Drebin, J. A., Fisher, W. E., Gill, A. J., Gingras, M.-C., Kingham, T. P., Lee, M. K., Lidsky, M. E., Nussbaum, D. P., Overman, M. J., . . . Jarnagin, W. R. (2025). Histologic- and genomic-directed adjuvant therapy for ampullary adenocarcinoma: A hidden genome-derived analysis. *Journal of the National Comprehensive Cancer Network, 23*(6), 234–240. https://doi.org/10.6004/jnccn.2025.7008（PMID: 40499590）

Fallon, M., Giusti, R., Aielli, F., Hoskin, P., Rolke, R., Sharma, M., & Ripamonti, C. I. (2018). Management of cancer pain in adult patients: ESMO clinical practice guidelines. *Annals of Oncology, 29*(Suppl 4), iv166–iv191. https://doi.org/10.1093/annonc/mdy152（PMID: 30052758）

Ferrell, B. R., Temel, J. S., Temin, S., Alesi, E. R., Balboni, T. A., Basch, E. M., Firn, J. I., Paice, J. A., Peppercorn, J. M., Phillips, T., Stovall, E. L., Zimmermann, C., & Smith, T. J. (2017). Integration of palliative care into standard oncology care: American Society of Clinical Oncology clinical practice guideline update. *Journal of Clinical Oncology, 35*(1), 96–112. https://doi.org/10.1200/JCO.2016.70.1474（PMID: 28034065）

Fietkau, R., Ghadimi, M., Grützmann, R., Wittel, U. A., Jacobasch, L., Uhl, W., Croner, R. S., Bechstein, W. O., Neumann, U. P., Waldschmidt, D., Boeck, S., Moosmann, N., Reinacher-Schick, A. C., Golcher, H., Adler, W., Semrau, S., Lubgan, D., Kallies, A., Hecht, M., . . . Oettle, H. (2025). Benefit of chemoradiotherapy versus chemotherapy after induction therapy for conversion of unresectable into resectable pancreatic cancer: The randomized CONKO-007 trial. *Journal of Clinical Oncology, 43*(30), 3266–3278. https://doi.org/10.1200/JCO-24-01502（PMID: 40802908）

Fitzgerald, J. E. F., White, M. J., & Lobo, D. N. (2009). Courvoisier's gallbladder: Law or sign? *World Journal of Surgery, 33*(4), 886–891. https://doi.org/10.1007/s00268-008-9908-y（PMID: 19190960）

Fresenius Kabi USA. (2026). *Fluorouracil injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=21af1777-87f7-4e40-9917-f1677e7ff1a5（版本日期 2026-06-08）

Giardiello, F. M., Brensinger, J. D., Tersmette, A. C., Goodman, S. N., Petersen, G. M., Booker, S. V., Cruz-Correa, M., & Offerhaus, J. A. (2000). Very high risk of cancer in familial Peutz-Jeghers syndrome. *Gastroenterology, 119*(6), 1447–1453. https://doi.org/10.1053/gast.2000.20228（PMID: 11113065）

Gill, S., Ko, Y.-J., Cripps, C., Beaudoin, A., Dhesy-Thind, S., Zulfiqar, M., Zalewski, P., Do, T., Cano, P., Lam, W. Y. H., Dowden, S., Grassin, H., Stewart, J., & Moore, M. (2016). PANCREOX: A randomized phase III study of fluorouracil/leucovorin with or without oxaliplatin for second-line advanced pancreatic cancer in patients who have received gemcitabine-based chemotherapy. *Journal of Clinical Oncology, 34*(32), 3914–3920. https://doi.org/10.1200/JCO.2016.68.5776（PMID: 27621395）

Goggins, M., Overbeek, K. A., Brand, R., Syngal, S., Del Chiaro, M., Bartsch, D. K., Bassi, C., Carrato, A., Farrell, J., Fishman, E. K., Fockens, P., Gress, T. M., van Hooft, J. E., Hruban, R. H., Kastrinos, F., Klein, A., Lennon, A. M., Lucas, A., Park, W., . . . Bruno, M. (2020). Management of patients with increased risk for familial pancreatic cancer: Updated recommendations from the International Cancer of the Pancreas Screening (CAPS) Consortium. *Gut, 69*(1), 7–17. https://doi.org/10.1136/gutjnl-2019-319352（PMID: 31672839）

Golan, T., Hammel, P., Reni, M., Van Cutsem, E., Macarulla, T., Hall, M. J., Park, J.-O., Hochhauser, D., Arnold, D., Oh, D.-Y., Reinacher-Schick, A., Tortora, G., Algül, H., O'Reilly, E. M., McGuinness, D., Cui, K. Y., Schlienger, K., Locker, G. Y., & Kindler, H. L. (2019). Maintenance olaparib for germline BRCA-mutated metastatic pancreatic cancer. *New England Journal of Medicine, 381*(4), 317–327. https://doi.org/10.1056/NEJMoa1903387（PMID: 31157963）

Gomi, H., Solomkin, J. S., Schlossberg, D., Okamoto, K., Takada, T., Strasberg, S. M., Ukai, T., Endo, I., Iwashita, Y., Hibi, T., Pitt, H. A., Matsunaga, N., Takamori, Y., Umezawa, A., Asai, K., Suzuki, K., Han, H.-S., Hwang, T.-L., Mori, Y., . . . Yamamoto, M. (2018). Tokyo Guidelines 2018: Antimicrobial therapy for acute cholangitis and cholecystitis. *Journal of Hepato-Biliary-Pancreatic Sciences, 25*(1), 3–16. https://doi.org/10.1002/jhbp.518（PMID: 29090866）

Goonetilleke, K. S., & Siriwardena, A. K. (2007). Systematic review of carbohydrate antigen (CA 19-9) as a biochemical marker in the diagnosis of pancreatic cancer. *European Journal of Surgical Oncology, 33*(3), 266–270. https://doi.org/10.1016/j.ejso.2006.10.004（PMID: 17097848）

Go, S.-I., Lee, S.-C., Bae, W. K., Zang, D. Y., Lee, H. W., Jang, J. S., Ji, J. H., Kim, J. H., Park, S., Sym, S. J., Yang, Y., Jeon, S. Y., Hwang, I. G., Oh, S. Y., & Kang, J. H. (2021). Modified FOLFIRINOX versus S-1 as second-line chemotherapy in gemcitabine-failed metastatic pancreatic cancer patients: A randomised controlled trial (MPACA-3). *European Journal of Cancer, 157*, 21–30. https://doi.org/10.1016/j.ejca.2021.08.002（PMID: 34464782）

Ha, H., Ko, Y.-H., Kim, K., Hong, J., Lee, G.-W., Jeong, S. H., Bang, S.-M., & Yoon, S.-S. (2023). Application of the Khorana score for cancer-associated thrombosis prediction in patients of East Asian ethnicity undergoing ambulatory chemotherapy. *Thrombosis Journal, 21*(1), Article 63. https://doi.org/10.1186/s12959-023-00505-3（PMID: 37271814）

Hammel, P., Huguet, F., van Laethem, J. L., Goldstein, D., Glimelius, B., Artru, P., Borbath, I., Bouché, O., Shannon, J., André, T., Mineur, L., Chibaudel, B., Bonnetain, F., & Louvet, C. (2016). Effect of chemoradiotherapy vs chemotherapy on survival in patients with locally advanced pancreatic cancer controlled after 4 months of gemcitabine with or without erlotinib: The LAP07 randomized clinical trial. *JAMA, 315*(17), 1844–1853. https://doi.org/10.1001/jama.2016.4324（PMID: 27139057）

Hart, P. A., Bellin, M. D., Andersen, D. K., Bradley, D., Cruz-Monserrate, Z., Forsmark, C. E., Goodarzi, M. O., Habtezion, A., Korc, M., Kudva, Y. C., Pandol, S. J., Yadav, D., & Chari, S. T. (2016). Type 3c (pancreatogenic) diabetes mellitus secondary to chronic pancreatitis and pancreatic cancer. *The Lancet Gastroenterology & Hepatology, 1*(3), 226–237. https://doi.org/10.1016/S2468-1253(16)30106-6（PMID: 28404095）

Hofheinz, R.-D., Gencer, D., Schulz, H., Stahl, M., Hegewisch-Becker, S., Loeffler, L. M., Kronawitter, U., Bolz, G., Potenberg, J., Tauchert, F., Al-Batran, S.-E., & Schneeweiss, A. (2015). Mapisal versus urea cream as prophylaxis for capecitabine-associated hand-foot syndrome: A randomized phase III trial of the AIO Quality of Life Working Group. *Journal of Clinical Oncology, 33*(22), 2444–2449. https://doi.org/10.1200/JCO.2014.60.4587（PMID: 26124485）

Holly, E. A., Chaliha, I., Bracci, P. M., & Gautam, M. (2004). Signs and symptoms of pancreatic cancer: A population-based case-control study in the San Francisco Bay area. *Clinical Gastroenterology and Hepatology, 2*(6), 510–517. https://doi.org/10.1016/s1542-3565(04)00171-5（PMID: 15181621）

Holm, M. B., & Verbeke, C. S. (2022). Prognostic impact of resection margin status on distal pancreatectomy for ductal adenocarcinoma. *Current Oncology, 29*(9), 6551–6563. https://doi.org/10.3390/curroncol29090515（PMID: 36135084）

Hong, D. S., DuBois, S. G., Kummar, S., Farago, A. F., Albert, C. M., Rohrberg, K. S., van Tilburg, C. M., Nagasubramanian, R., Berlin, J. D., Federman, N., Mascarenhas, L., Geoerger, B., Dowlati, A., Pappo, A. S., Bielack, S., Doz, F., McDermott, R., Patel, J. D., Schilder, R. J., . . . Drilon, A. (2020). Larotrectinib in patients with TRK fusion-positive solid tumours: A pooled analysis of three phase 1/2 clinical trials. *The Lancet Oncology, 21*(4), 531–540. https://doi.org/10.1016/S1470-2045(19)30856-3（PMID: 32105622）

H2-Pharma. (2026). *Xeloda (capecitabine) tablets* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e702d84d-7162-4751-bf37-d724cc7e45a5（版本日期 2026-02-05）

Hsu, F.-C., Roberts, N. J., Childs, E., Porter, N., Rabe, K. G., Borgida, A., Ukaegbu, C., Goggins, M. G., Hruban, R. H., Zogopoulos, G., Syngal, S., Gallinger, S., Petersen, G. M., & Klein, A. P. (2021). Risk of pancreatic cancer among individuals with pathogenic variants in the ATM gene. *JAMA Oncology, 7*(11), 1664–1668. https://doi.org/10.1001/jamaoncol.2021.3701（PMID: 34529012）

Huang, Y.-C., Wu, C.-H., Lee, M. H., Wang, S. F., Tsou, Y.-K., Lin, C.-H., Sung, K.-F., & Liu, N.-J. (2022). Timing of endoscopic retrograde cholangiopancreatography in the treatment of acute cholangitis of different severity. *World Journal of Gastroenterology, 28*(38), 5602–5613. https://doi.org/10.3748/wjg.v28.i38.5602（PMID: 36304084）

Hu, C., Hart, S. N., Polley, E. C., Gnanaolivu, R., Shimelis, H., Lee, K. Y., Lilyquist, J., Na, J., Moore, R., Antwi, S. O., Bamlet, W. R., Chaffee, K. G., DiCarlo, J., Wu, Z., Samara, R., Kasi, P. M., McWilliams, R. R., Petersen, G. M., & Couch, F. J. (2018). Association between inherited germline mutations in cancer predisposition genes and risk of pancreatic cancer. *JAMA, 319*(23), 2401–2409. https://doi.org/10.1001/jama.2018.6228（PMID: 29922827）

Huxley, R., Ansary-Moghaddam, A., Berrington de González, A., Barzi, F., & Woodward, M. (2005). Type-II diabetes and pancreatic cancer: A meta-analysis of 36 studies. *British Journal of Cancer, 92*(11), 2076–2083. https://doi.org/10.1038/sj.bjc.6602619（PMID: 15886696）

Hu, Z. I., Shia, J., Stadler, Z. K., Varghese, A. M., Capanu, M., Salo-Mullen, E., Lowery, M. A., Diaz, L. A., Jr., Mandelker, D., Yu, K. H., Zervoudakis, A., Kelsen, D. P., Iacobuzio-Donahue, C. A., Klimstra, D. S., Saltz, L. B., Sahin, I. H., & O'Reilly, E. M. (2018). Evaluating mismatch repair deficiency in pancreatic adenocarcinoma: Challenges and recommendations. *Clinical Cancer Research, 24*(6), 1326–1336. https://doi.org/10.1158/1078-0432.CCR-17-3099（PMID: 29367431）

Iodice, S., Gandini, S., Maisonneuve, P., & Lowenfels, A. B. (2008). Tobacco and the risk of pancreatic cancer: A review and meta-analysis. *Langenbeck's Archives of Surgery, 393*(4), 535–545. https://doi.org/10.1007/s00423-007-0266-2（PMID: 18193270）

Ipsen. (n.d.). *A study to assess the effectiveness and safety of irinotecan liposome injection, 5-fluorouracil/leucovorin plus oxaliplatin in patients not previously treated for metastatic pancreatic cancer, compared to nab-paclitaxel+gemcitabine treatment* (ClinicalTrials.gov Identifier NCT04083235). Retrieved November 1, 2026, from https://clinicaltrials.gov/study/NCT04083235

Ipsen. (2025). *Onivyde (irinotecan liposome) injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c8b58efa-1820-48a4-b70d-62918fc4abfc（版本日期 2025-03-03）

Janssen, Q. P., van Dam, J. L., van Bekkum, M. L., Bonsing, B. A., Bos, H., Bosscha, K. P., Bouwense, S. A. W., Brouwer-Hol, L., Bruynzeel, A. M. E., Busch, O. R., Coene, P. L. O., van Eijck, C. H. J., de Groot, J. W. B., Haberkorn, B. C. M., de Hingh, I. H. J. T., Karsten, T. M., Kazemier, G., van der Kolk, M. B., Liem, M. S. L., . . . Groot Koerkamp, B. (2025). Neoadjuvant FOLFIRINOX versus neoadjuvant gemcitabine-based chemoradiotherapy in resectable and borderline resectable pancreatic cancer (PREOPANC-2): A multicentre, open-label, phase 3 randomised trial. *The Lancet Oncology, 26*(10), 1346–1356. https://doi.org/10.1016/S1470-2045(25)00363-8（PMID: 40945523）

Jeurnink, S. M., Steyerberg, E. W., van Hooft, J. E., van Eijck, C. H. J., Schwartz, M. P., Vleggaar, F. P., Kuipers, E. J., & Siersema, P. D. (2010). Surgical gastrojejunostomy or endoscopic stent placement for the palliation of malignant gastric outlet obstruction (SUSTENT study): A multicenter randomized trial. *Gastrointestinal Endoscopy, 71*(3), 490–499. https://doi.org/10.1016/j.gie.2009.09.042（PMID: 20003966）

Jiménez-Romero, C., de Juan Lerma, A., Marcacuzco Quinto, A., Caso Maestro, O., Alonso Murillo, L., Rioja Conde, P., & Justo Alonso, I. (2025). Risk factors for delayed gastric emptying after pancreatoduodenectomy: A 10-year retrospective study. *Annals of Medicine, 57*(1), Article 2453076. https://doi.org/10.1080/07853890.2025.2453076（PMID: 39817563）

Jones, M. R., Williamson, L. M., Topham, J. T., Lee, M. K. C., Goytain, A., Ho, J., Denroche, R. E., Jang, G., Pleasance, E., Shen, Y., Karasinska, J. M., McGhie, J. P., Gill, S., Lim, H. J., Moore, M. J., Wong, H.-L., Ng, T., Yip, S., Zhang, W., . . . Renouf, D. J. (2019). NRG1 gene fusions are recurrent, clinically actionable gene rearrangements in KRAS wild-type pancreatic ductal adenocarcinoma. *Clinical Cancer Research, 25*(15), 4674–4681. https://doi.org/10.1158/1078-0432.CCR-19-0191（PMID: 31068372）

Kamada, Y., Hori, T., Yamamoto, H., Harada, H., Yamamoto, M., Yamada, M., Yazawa, T., Sasaki, B., Tani, M., Sato, A., Katsura, H., Tani, R., Aoyama, R., Sasaki, Y., Okada, M., & Zaima, M. (2021). Fatal arterial hemorrhage after pancreaticoduodenectomy: How do we simultaneously accomplish complete hemostasis and hepatic arterial flow? *World Journal of Hepatology, 13*(4), 483–503. https://doi.org/10.4254/wjh.v13.i4.483（PMID: 33959229）

Kastrinos, F., Mukherjee, B., Tayob, N., Wang, F., Sparr, J., Raymond, V. M., Bandipalliam, P., Stoffel, E. M., Gruber, S. B., & Syngal, S. (2009). Risk of pancreatic cancer in families with Lynch syndrome. *JAMA, 302*(16), 1790–1795. https://doi.org/10.1001/jama.2009.1529（PMID: 19861671）

Katz, M. H. G., Shi, Q., Meyers, J., Herman, J. M., Chuong, M., Wolpin, B. M., Ahmad, S., Marsh, R., Schwartz, L., Behr, S., Frankel, W. L., Collisson, E., Leenstra, J., Williams, T. M., Vaccaro, G., Venook, A., Meyerhardt, J. A., & O'Reilly, E. M. (2022). Efficacy of preoperative mFOLFIRINOX vs mFOLFIRINOX plus hypofractionated radiotherapy for borderline resectable adenocarcinoma of the pancreas: The A021501 phase 2 randomized clinical trial. *JAMA Oncology, 8*(9), 1263–1270. https://doi.org/10.1001/jamaoncol.2022.2319（PMID: 35834226）

Key, N. S., Khorana, A. A., Kuderer, N. M., Bohlke, K., Lee, A. Y. Y., Arcelus, J. I., Wong, S. L., Balaban, E. P., Flowers, C. R., Gates, L. E., Kakkar, A. K., Tempero, M. A., Gupta, S., Lyman, G. H., & Falanga, A. (2023). Venous thromboembolism prophylaxis and treatment in patients with cancer: ASCO guideline update. *Journal of Clinical Oncology, 41*(16), 3063–3071. https://doi.org/10.1200/JCO.23.00294（PMID: 37075273）

Khorana, A. A., Kuderer, N. M., Culakova, E., Lyman, G. H., & Francis, C. W. (2008). Development and validation of a predictive model for chemotherapy-associated thrombosis. *Blood, 111*(10), 4902–4907. https://doi.org/10.1182/blood-2007-10-116327（PMID: 18216292）

Khorana, A. A., Soff, G. A., Kakkar, A. K., Vadhan-Raj, S., Riess, H., Wun, T., Streiff, M. B., Garcia, D. A., Liebman, H. A., Belani, C. P., O'Reilly, E. M., Patel, J. N., Yimer, H. A., Wildgoose, P., Burton, P., Vijapurkar, U., Kaul, S., Eikelboom, J., McBane, R., . . . Lyman, G. H. (2019). Rivaroxaban for thromboprophylaxis in high-risk ambulatory patients with cancer. *New England Journal of Medicine, 380*(8), 720–728. https://doi.org/10.1056/NEJMoa1814630（PMID: 30786186）

Kindler, H. L., Hammel, P., Reni, M., Van Cutsem, E., Macarulla, T., Hall, M. J., Park, J. O., Hochhauser, D., Arnold, D., Oh, D. Y., Reinacher-Schick, A., Tortora, G., Algül, H., O'Reilly, E. M., Bordia, S., McGuinness, D., Cui, K., Locker, G. Y., & Golan, T. (2022). Overall survival results from the POLO trial: A phase III study of active maintenance olaparib versus placebo for germline BRCA-mutated metastatic pancreatic cancer. *Journal of Clinical Oncology, 40*(34), 3929–3939. https://doi.org/10.1200/JCO.21.01604（PMID: 35834777）

Kiriyama, S., Kozaka, K., Takada, T., Strasberg, S. M., Pitt, H. A., Gabata, T., Hata, J., Liau, K.-H., Miura, F., Horiguchi, A., Liu, K.-H., Su, C.-H., Wada, K., Jagannath, P., Itoi, T., Gouma, D. J., Mori, Y., Mukai, S., Giménez, M. E., . . . Yamamoto, M. (2018). Tokyo Guidelines 2018: Diagnostic criteria and severity grading of acute cholangitis (with videos). *Journal of Hepato-Biliary-Pancreatic Sciences, 25*(1), 17–30. https://doi.org/10.1002/jhbp.512（PMID: 29032610）

Kirkegård, J., Mortensen, F. V., & Cronin-Fenton, D. (2017). Chronic pancreatitis and pancreatic cancer risk: A systematic review and meta-analysis. *American Journal of Gastroenterology, 112*(9), 1366–1372. https://doi.org/10.1038/ajg.2017.218（PMID: 28762376）

Ko, A. H., Malafa, M. P., Aguilera, T., Basturk, O., Benson, A. B., III, Cardin, D. B., Chiorean, E. G., Christensen, J. A., Chung, V., Czito, B., Del Chiaro, M., Dillhoff, M., Donahue, T. R., Fountzilas, C., Hardacre, J., Klute, K., Kunstman, J. W., Lim, K.-H., LoConte, N., . . . Ramakrishnan, S. (2026). Pancreatic adenocarcinoma, version 4.2026, NCCN Clinical Practice Guidelines in Oncology. *Journal of the National Comprehensive Cancer Network, 24*(10), Article e260046. https://doi.org/10.6004/jnccn.2026.0046（PMID: 42869082）

Labori, K. J., Bratlie, S. O., Andersson, B., Angelsen, J. H., Biörserud, C., Björnsson, B., Bringeland, E. A., Elander, N., Garresori, H., Grønbech, J. E., Haux, J., Hemmingsson, O., Liljefors, M. G., Myklebust, T. Å., Nymo, L. S., Peltola, K., Pfeiffer, P., Sallinen, V., Sandström, P., . . . Lassen, K. (2024). Neoadjuvant FOLFIRINOX versus upfront surgery for resectable pancreatic head cancer (NORPACT-1): A multicentre, randomised, phase 2 trial. *The Lancet Gastroenterology & Hepatology, 9*(3), 205–217. https://doi.org/10.1016/S2468-1253(23)00405-3（PMID: 38237621）

Laine, L., Barkun, A. N., Saltzman, J. R., Martel, M., & Leontiadis, G. I. (2021). ACG clinical guideline: Upper gastrointestinal and ulcer bleeding. *American Journal of Gastroenterology, 116*(5), 899–917. https://doi.org/10.14309/ajg.0000000000001245（PMID: 33929377）

Larsson, S. C., Orsini, N., & Wolk, A. (2007). Body mass index and pancreatic cancer risk: A meta-analysis of prospective studies. *International Journal of Cancer, 120*(9), 1993–1998. https://doi.org/10.1002/ijc.22535（PMID: 17266034）

Lena, J., Alamé, M., Italiano, A., Soubeyran, I., Blouin, L., Khalifa, E., Cousin, S., Pernot, S., & Palmieri, L.-J. (2025). Extensive molecular profiling of KRAS wild-type as compared to KRAS mutated pancreatic ductal adenocarcinoma on 318 patients. *European Journal of Cancer, 216*, Article 115197. https://doi.org/10.1016/j.ejca.2024.115197（PMID: 39729677）

Leonhardt, C. S., Niesen, W., Kalkum, E., Klotz, R., Hank, T., Büchler, M. W., Strobel, O., & Probst, P. (2022). Prognostic relevance of the revised R status definition in pancreatic cancer: Meta-analysis. *BJS Open, 6*(2), Article zrac010. https://doi.org/10.1093/bjsopen/zrac010（PMID: 35301513）

Lin, Y.-M., Lin, E. Y., Tseng, H.-S., Lee, R.-C., Huang, H.-E., Wang, S.-E., Shyr, Y.-M., & Liu, C.-A. (2021). Preventive covered stent placement at the gastroduodenal artery stump in angiogram-negative sentinel hemorrhage after pancreaticoduodenectomy. *Abdominal Radiology, 46*(10), 4995–5006. https://doi.org/10.1007/s00261-021-03123-7（PMID: 34037809）

Liu, C., Deng, S., Jin, K., Gong, Y., Cheng, H., Fan, Z., Qian, Y., Huang, Q., Ni, Q., Luo, G., & Yu, X. (2020). Lewis antigen-negative pancreatic cancer: An aggressive subgroup. *International Journal of Oncology, 56*(4), 900–908. https://doi.org/10.3892/ijo.2020.4989（PMID: 32319567）

Liu, C.-Y., Chen, P.-M., Chiou, T.-J., Liu, J.-H., Lin, J.-K., Lin, T.-C., Chen, W.-S., Jiang, J.-K., Wang, H.-S., & Wang, W.-S. (2008). UGT1A1*28 polymorphism predicts irinotecan-induced severe toxicities without affecting treatment outcome and survival in patients with metastatic colorectal carcinoma. *Cancer, 112*(9), 1932–1940. https://doi.org/10.1002/cncr.23370（PMID: 18300238）

Luo, G., Liu, C., Guo, M., Cheng, H., Lu, Y., Jin, K., Liu, L., Long, J., Xu, J., Lu, R., Ni, Q., & Yu, X. (2017). Potential biomarkers in Lewis negative patients with pancreatic cancer. *Annals of Surgery, 265*(4), 800–805. https://doi.org/10.1097/SLA.0000000000001741（PMID: 28267695）

Maio, M., Ascierto, P. A., Manzyuk, L., Motola-Kuba, D., Penel, N., Cassier, P. A., Bariani, G. M., De Jesus Acosta, A., Doi, T., Longo, F., Miller, W. H., Oh, D. Y., Gottfried, M., Xu, L., Jin, F., Norwood, K., & Marabelle, A. (2022). Pembrolizumab in microsatellite instability high or mismatch repair deficient cancers: Updated analysis from the phase II KEYNOTE-158 study. *Annals of Oncology, 33*(9), 929–938. https://doi.org/10.1016/j.annonc.2022.05.519（PMID: 35680043）

Maltoni, M., Scarpi, E., Dall'Agata, M., Zagonel, V., Bertè, R., Ferrari, D., Broglia, C. M., Bortolussi, R., Trentin, L., Valgiusti, M., Pini, S., Farolfi, A., Casadei Gardini, A., Nanni, O., Amadori, D., & Early Palliative Care Italian Study Group (EPCISG). (2016). Systematic versus on-demand early palliative care: Results from a multicentre, randomised clinical trial. *European Journal of Cancer, 65*, 61–68. https://doi.org/10.1016/j.ejca.2016.06.007（PMID: 27472648）

Marabelle, A., Le, D. T., Ascierto, P. A., Di Giacomo, A. M., De Jesus-Acosta, A., Delord, J. P., Geva, R., Gottfried, M., Penel, N., Hansen, A. R., Piha-Paul, S. A., Doi, T., Gao, B., Chung, H. C., Lopez-Martin, J., Bang, Y. J., Frommer, R. S., Shah, M., Ghori, R., . . . Diaz, L. A. (2020). Efficacy of pembrolizumab in patients with noncolorectal high microsatellite instability/mismatch repair-deficient cancer: Results from the phase II KEYNOTE-158 study. *Journal of Clinical Oncology, 38*(1), 1–10. https://doi.org/10.1200/JCO.19.02105（PMID: 31682550）

Masugi, Y., Takamatsu, M., Tanaka, M., Hara, K., Inoue, Y., Hamada, T., Suzuki, T., Arita, J., Hirose, Y., Kawaguchi, Y., Nakai, Y., Oba, A., Sasahira, N., Shimane, G., Takeda, T., Tateishi, K., Uemura, S., Fujishiro, M., Hasegawa, K., . . . GTK Pancreatic Cancer Study Group in Japan. (2023). Post-operative mortality and recurrence patterns in pancreatic cancer according to KRAS mutation and CDKN2A, p53, and SMAD4 expression. *The Journal of Pathology: Clinical Research, 9*(5), 339–353. https://doi.org/10.1002/cjp2.323（PMID: 37291757）

McHugh, K. E., Mukhopadhyay, S., Doxtader, E. E., Lanigan, C., & Allende, D. S. (2020). INSM1 is a highly specific marker of neuroendocrine differentiation in primary neoplasms of the gastrointestinal tract, appendix, and pancreas. *American Journal of Clinical Pathology, 153*(6), 811–820. https://doi.org/10.1093/ajcp/aqaa014（PMID: 32128564）

Meitheal. (2024). *Oxaliplatin injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=11377169-7986-45b1-8298-6f0533efa3c3（版本日期 2024-10-03）

Meitheal. (2025). *Gemcitabine injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c0b1b715-9ff8-43ca-9e49-465f1f380084（版本日期 2025-07-23）

Merck Sharp & Dohme LLC. (2026). *Keytruda (pembrolizumab) injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9333c79b-d487-4538-a9f0-71b91a02b287（版本日期 2026-07-10）

Miura, F., Okamoto, K., Takada, T., Strasberg, S. M., Asbun, H. J., Pitt, H. A., Gomi, H., Solomkin, J. S., Schlossberg, D., Han, H.-S., Kim, M.-H., Hwang, T.-L., Chen, M.-F., Huang, W. S.-W., Kiriyama, S., Itoi, T., Garden, O. J., Liau, K.-H., Horiguchi, A., . . . Yamamoto, M. (2018). Tokyo Guidelines 2018: Initial management of acute biliary infection and flowchart for acute cholangitis. *Journal of Hepato-Biliary-Pancreatic Sciences, 25*(1), 31–40. https://doi.org/10.1002/jhbp.509（PMID: 28941329）

Moekotte, A. L., Malleo, G., van Roessel, S., Bonds, M., Halimi, A., Zarantonello, L., Napoli, N., Dreyer, S. B., Wellner, U. F., Bolm, L., Mavroeidis, V. K., Robinson, S., Khalil, K., Ferraro, D., Mortimer, M. C., Harris, S., Al-Sarireh, B., Fusai, G. K., Roberts, K. J., . . . Abu Hilal, M. (2020). Gemcitabine-based adjuvant chemotherapy in subtypes of ampullary adenocarcinoma: International propensity score-matched cohort study. *British Journal of Surgery, 107*(9), 1171–1182. https://doi.org/10.1002/bjs.11555（PMID: 32259295）

Moore, M. J., Goldstein, D., Hamm, J., Figer, A., Hecht, J. R., Gallinger, S., Au, H. J., Murawa, P., Walde, D., Wolff, R. A., Campos, D., Lim, R., Ding, K., Clark, G., Voskoglou-Nomikos, T., Ptasynski, M., & Parulekar, W. (2007). Erlotinib plus gemcitabine compared with gemcitabine alone in patients with advanced pancreatic cancer: A phase III trial of the National Cancer Institute of Canada Clinical Trials Group. *Journal of Clinical Oncology, 25*(15), 1960–1966. https://doi.org/10.1200/JCO.2006.07.9525（PMID: 17452677）

Murphy, K., McLaughlin, P., O'Connor, B. R., Breen, M., O'Súilleabháin, C., Maceneaney, P., & Maher, M. M. (2012). Does Courvoisier's sign stand the test of time? *Clinical Radiology, 67*(11), e27–e30. https://doi.org/10.1016/j.crad.2012.07.008（PMID: 22964366）

Muscaritoli, M., Arends, J., Bachmann, P., Baracos, V., Barthelemy, N., Bertz, H., Bozzetti, F., Hütterer, E., Isenring, E., Kaasa, S., Krznaric, Z., Laird, B., Larsson, M., Laviano, A., Mühlebach, S., Oldervoll, L., Ravasco, P., Solheim, T. S., Strasser, F., . . . Bischoff, S. C. (2021). ESPEN practical guideline: Clinical nutrition in cancer. *Clinical Nutrition, 40*(5), 2898–2913. https://doi.org/10.1016/j.clnu.2021.02.005（PMID: 33946039）

Nagtegaal, I. D., Odze, R. D., Klimstra, D., Paradis, V., Rugge, M., Schirmacher, P., Washington, K. M., Carneiro, F., & Cree, I. A. (2020). The 2019 WHO classification of tumours of the digestive system. *Histopathology, 76*(2), 182–188. https://doi.org/10.1111/his.13975（PMID: 31433515）

National Comprehensive Cancer Network. (2026). *NCCN Guidelines for Patients: Pancreatic cancer* (based on NCCN Guidelines for Pancreatic Adenocarcinoma, Version 2.2026, April 22, 2026). https://www.nccn.org/patients/guidelines/content/PDF/pancreatic-patient.pdf

Neoptolemos, J. P., Palmer, D. H., Ghaneh, P., Psarelli, E. E., Valle, J. W., Halloran, C. M., Faluyi, O., O'Reilly, D. A., Cunningham, D., Wadsley, J., Darby, S., Meyer, T., Gillmore, R., Anthoney, A., Lind, P., Glimelius, B., Falk, S., Izbicki, J. R., Middleton, G. W., . . . Büchler, M. W. (2017). Comparison of adjuvant gemcitabine and capecitabine with gemcitabine monotherapy in patients with resected pancreatic cancer (ESPAC-4): A multicentre, open-label, randomised, phase 3 trial. *The Lancet, 389*(10073), 1011–1024. https://doi.org/10.1016/S0140-6736(16)32409-6（PMID: 28129987）

Neoptolemos, J. P., Stocken, D. D., Friess, H., Bassi, C., Dunn, J. A., Hickey, H., Beger, H., Fernandez-Cruz, L., Dervenis, C., Lacaine, F., Falconi, M., Pederzoli, P., Pap, A., Spooner, D., Kerr, D. J., Büchler, M. W., & European Study Group for Pancreatic Cancer. (2004). A randomized trial of chemoradiotherapy and chemotherapy after resection of pancreatic cancer. *New England Journal of Medicine, 350*(12), 1200–1210. https://doi.org/10.1056/NEJMoa032295（PMID: 15028824）

Neuss, M. N., Polovich, M., McNiff, K., Esper, P., Gilmore, T. R., LeFebvre, K. B., Schulmeister, L., & Jacobson, J. O. (2013). 2013 updated American Society of Clinical Oncology/Oncology Nursing Society chemotherapy administration safety standards including standards for the safe administration and management of oral chemotherapy. *Journal of Oncology Practice, 9*(2 Suppl), 5s–13s. https://doi.org/10.1200/JOP.2013.000874（PMID: 23914148）

Norton, C., Shaw, M. S., Rubnitz, Z., Smith, J., Soares, H. P., Nevala-Plagemann, C. D., Garrido-Laguna, I., & Florou, V. (2025). KRAS mutation status and treatment outcomes in patients with metastatic pancreatic adenocarcinoma. *JAMA Network Open, 8*(1), Article e2453588. https://doi.org/10.1001/jamanetworkopen.2024.53588（PMID: 39777438）

Oar, A., Kneebone, A., Sjoquist, K. M., Espinoza, D., Lee, M., Le, H., Gholamrezaei, L., Chu, J., Lynam, J., Mallesara, G., Lee, D., Vignarajah, D., Ward, I., Samra, J., Barbour, A., Whitehead, A., Brooks, S., Nicholson, A., Wang, T. W., . . . Goldstein, D. (2026). Perioperative chemotherapy and stereotactic body radiotherapy versus perioperative chemotherapy alone in patients with high-risk, localised pancreatic cancer (MASTERPLAN): An open-label, phase 2, multicentre, randomised trial of the Australasian Gastro-Intestinal Trials Group. *The Lancet Oncology*. Advance online publication. https://doi.org/10.1016/S1470-2045(26)00532-2（PMID: 42914998）

Oettle, H., Neuhaus, P., Hochhaus, A., Hartmann, J. T., Gellert, K., Ridwelski, K., Niedergethmann, M., Zülke, C., Fahlke, J., Arning, M. B., Sinn, M., Hinke, A., & Riess, H. (2013). Adjuvant chemotherapy with gemcitabine and long-term outcomes among patients with resected pancreatic cancer: The CONKO-001 randomized trial. *JAMA, 310*(14), 1473–1481. https://doi.org/10.1001/jama.2013.279201（PMID: 24104372）

Oettle, H., Riess, H., Stieler, J. M., Heil, G., Schwaner, I., Seraphin, J., Görner, M., Mölle, M., Greten, T. F., Lakner, V., Bischoff, S., Sinn, M., Dörken, B., & Pelzer, U. (2014). Second-line oxaliplatin, folinic acid, and fluorouracil versus folinic acid and fluorouracil alone for gemcitabine-refractory pancreatic cancer: Outcomes from the CONKO-003 trial. *Journal of Clinical Oncology, 32*(23), 2423–2429. https://doi.org/10.1200/JCO.2013.53.6995（PMID: 24982456）

O'Grady, N. P., Alexander, M., Burns, L. A., Dellinger, E. P., Garland, J., Heard, S. O., Lipsett, P. A., Masur, H., Mermel, L. A., Pearson, M. L., Raad, I. I., Randolph, A. G., Rupp, M. E., Saint, S., & Healthcare Infection Control Practices Advisory Committee. (2011). Guidelines for the prevention of intravascular catheter-related infections. *American Journal of Infection Control, 39*(4 Suppl 1), S1–S34. https://doi.org/10.1016/j.ajic.2011.01.003（PMID: 21511081）

Ohba, A., Ozaka, M., Mizusawa, J., Okusaka, T., Kobayashi, S., Yamashita, T., Ikeda, M., Yasuda, I., Sugimori, K., Sasahira, N., Ikezawa, K., Miki, I., Okano, N., Mizuno, N., Furukawa, M., Shirakawa, H., Sano, Y., Katayama, H., Furuse, J., . . . Hepatobiliary and Pancreatic Oncology Group of the Japan Clinical Oncology Group (JCOG-HBPOG). (2025). Modified fluorouracil, leucovorin, irinotecan, and oxaliplatin or S-1, irinotecan, and oxaliplatin versus nab-paclitaxel + gemcitabine in metastatic or recurrent pancreatic cancer (GENERATE, JCOG1611): A randomized, open-label, phase II/III trial. *Journal of Clinical Oncology, 43*(31), 3345–3354. https://doi.org/10.1200/JCO.24.00936（PMID: 40720715）

Ohtsuka, T., Fernandez-Del Castillo, C., Furukawa, T., Hijioka, S., Jang, J.-Y., Lennon, A. M., Miyasaka, Y., Ohno, E., Salvia, R., Wolfgang, C. L., & Wood, L. D. (2024). International evidence-based Kyoto guidelines for the management of intraductal papillary mucinous neoplasm of the pancreas. *Pancreatology, 24*(2), 255–270. https://doi.org/10.1016/j.pan.2023.12.009（PMID: 38182527）

Omiya, K., Oba, A., Tanaka, K., Miyazaki, N., Otsuka, S., Ohgi, K., Sugiura, T., Shintakuya, R., Okada, K., Uemura, K., Yamaki, S., Hashimoto, D., Inoue, K., Mizuma, M., Unno, M., Nakagawa, N., Tanaka, H., Takami, H., Takeuchi, S., . . . Satoi, S. (2026). Duke pancreatic monoclonal antigen type 2 for monitoring carbohydrate antigen 19-9 nonexpressor pancreatic cancer. *JAMA Surgery, 161*(8), 805–815. https://doi.org/10.1001/jamasurg.2026.1810（PMID: 42234435）

O'Reilly, E. M., Lee, J. W., Zalupski, M., Capanu, M., Park, J., Golan, T., Tahover, E., Lowery, M. A., Chou, J. F., Sahai, V., Brenner, R., Kindler, H. L., Yu, K. H., Zervoudakis, A., Vemuri, S., Stadler, Z. K., Do, R. K. G., Dhani, N., Chen, A. P., & Kelsen, D. P. (2020). Randomized, multicenter, phase II trial of gemcitabine and cisplatin with or without veliparib in patients with pancreas adenocarcinoma and a germline BRCA/PALB2 mutation. *Journal of Clinical Oncology, 38*(13), 1378–1388. https://doi.org/10.1200/JCO.19.02931（PMID: 31976786）

O'Reilly, E. M., Wainberg, Z. A., Hendifar, A. E., Borad, M. J., Pietrantonio, F., Pant, S., Hammel, P., Cremolini, C., Manji, G. A., Oberstein, P. E., Garrido-Laguna, I., Springfeld, C., Azad, N. S., Ueno, M., Chui, S. Y., Zhang, Y., Patel, H., Lee, Y., Salman, Z., & Wolpin, B. M. (2026). Daraxonrasib or chemotherapy in previously treated metastatic pancreatic cancer. *New England Journal of Medicine, 395*(4), 325–337. https://doi.org/10.1056/NEJMoa2605555（PMID: 42223072）

Palmer, D. H., Jackson, R., Springfeld, C., Ghaneh, P., Rawcliffe, C., Halloran, C. M., Faluyi, O., Cunningham, D., Wadsley, J., Darby, S., Meyer, T., Gillmore, R., Lind, P., Glimelius, B., Falk, S., Ma, Y. T., Middleton, G. W., Cummins, S., Ross, P. J., . . . Neoptolemos, J. P. (2025). Pancreatic adenocarcinoma: Long-term outcomes of adjuvant therapy in the ESPAC4 phase III trial. *Journal of Clinical Oncology, 43*(10), 1240–1253. https://doi.org/10.1200/JCO.24.01118（PMID: 39637340）

Pannala, R., Leirness, J. B., Bamlet, W. R., Basu, A., Petersen, G. M., & Chari, S. T. (2008). Prevalence and clinical profile of pancreatic cancer-associated diabetes mellitus. *Gastroenterology, 134*(4), 981–987. https://doi.org/10.1053/j.gastro.2008.01.039（PMID: 18395079）

Park, W., Chawla, A., & O'Reilly, E. M. (2021). Pancreatic cancer: A review. *JAMA, 326*(9), 851–862. https://doi.org/10.1001/jama.2021.13027（PMID: 34547082）

Park, W., Kasi, A., Spira, A. I., Paz-Ares Rodríguez, L., Herzberg, B. O., Pelster, M. S., Tolcher, A. W., Kuboki, Y., Kitano, S., Shoji, H., Wang, J. S., Berlin, J. D., Hollebecque, A., LoRusso, P., Fountzilas, C., Cassier, P. A., Nishina, T., Sakai, D., Inagaki, C., . . . Goldman, J. W. (2026). Setidegrasib in advanced non-small-cell lung cancer and pancreatic cancer. *New England Journal of Medicine, 394*(14), 1409–1420. https://doi.org/10.1056/NEJMoa2600752（PMID: 41879829）

Permuth-Wey, J., & Egan, K. M. (2009). Family history is a significant risk factor for pancreatic cancer: Results from a systematic review and meta-analysis. *Familial Cancer, 8*(2), 109–117. https://doi.org/10.1007/s10689-008-9214-8（PMID: 18763055）

Pharmacia & Upjohn. (2026). *Camptosar (irinotecan hydrochloride) injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e518dfc6-7e93-4fee-a66c-51e1ab71c056（版本日期 2026-05-12）

Philip, P. A., Azar, I., Xiu, J., Hall, M. J., Hendifar, A. E., Lou, E., Hwang, J. J., Gong, J., Feldman, R., Ellis, M., Stafford, P., Spetzler, D., Khushman, M. M., Sohal, D., Lockhart, A. C., Weinberg, B. A., El-Deiry, W. S., Marshall, J., Shields, A. F., & Korn, W. M. (2022). Molecular characterization of KRAS wild-type tumors in patients with pancreatic adenocarcinoma. *Clinical Cancer Research, 28*(12), 2704–2714. https://doi.org/10.1158/1078-0432.CCR-21-3581（PMID: 35302596）

Philip, P. A., Lacy, J., Portales, F., Sobrero, A., Pazo-Cid, R., Manzano Mozo, J. L., Kim, E. J., Dowden, S., Zakari, A., Borg, C., Terrebonne, E., Rivera, F., Sastre, J., Bathini, V., López-Trabada, D., Asselah, J., Saif, M. W., Shiansong Li, J., Ong, T. J., . . . Hammel, P. (2020). Nab-paclitaxel plus gemcitabine in patients with locally advanced pancreatic cancer (LAPACT): A multicentre, open-label phase 2 study. *The Lancet Gastroenterology & Hepatology, 5*(3), 285–294. https://doi.org/10.1016/S2468-1253(19)30327-9（PMID: 31953079）

Porta, M., Fabregat, X., Malats, N., Guarner, L., Carrato, A., de Miguel, A., Ruiz, L., Jariod, M., Costafreda, S., Coll, S., Alguacil, J., Corominas, J. M., Solà, R., Salas, A., & Real, F. X. (2005). Exocrine pancreatic cancer: Symptoms at presentation and their relation to tumour site and stage. *Clinical & Translational Oncology, 7*(5), 189–197. https://doi.org/10.1007/BF02712816（PMID: 15960930）

Porter, N., Laheru, D., Lau, B., He, J., Zheng, L., Narang, A., Roberts, N. J., Canto, M. I., Lennon, A. M., Goggins, M. G., Hruban, R. H., & Klein, A. P. (2022). Risk of pancreatic cancer in the long-term prospective follow-up of familial pancreatic cancer kindreds. *Journal of the National Cancer Institute, 114*(12), 1681–1688. https://doi.org/10.1093/jnci/djac167（PMID: 36029239）

Raymond, E., Dahan, L., Raoul, J.-L., Bang, Y.-J., Borbath, I., Lombard-Bohas, C., Valle, J., Metrakos, P., Smith, D., Vinik, A., Chen, J.-S., Hörsch, D., Hammel, P., Wiedenmann, B., Van Cutsem, E., Patyna, S., Lu, D. R., Blanckmeister, C., Chao, R., & Ruszniewski, P. (2011). Sunitinib malate for the treatment of pancreatic neuroendocrine tumors. *New England Journal of Medicine, 364*(6), 501–513. https://doi.org/10.1056/NEJMoa1003825（PMID: 21306237）

Regine, W. F., Winter, K. A., Abrams, R., Safran, H., Hoffman, J. P., Konski, A., Benson, A. B., Macdonald, J. S., Rich, T. A., & Willett, C. G. (2011). Fluorouracil-based chemoradiation with either gemcitabine or fluorouracil chemotherapy after resection of pancreatic adenocarcinoma: 5-year analysis of the U.S. Intergroup/RTOG 9704 phase III trial. *Annals of Surgical Oncology, 18*(5), 1319–1326. https://doi.org/10.1245/s10434-011-1630-6（PMID: 21499862）

Revolution Medicines. (2026). *Rasonque (daraxonrasib) tablets* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=13a65923-d072-4dac-8620-8eabbf8c3641（版本日期 2026-08-27）

Rhee, H., & Park, M.-S. (2021). The role of imaging in current treatment strategies for pancreatic adenocarcinoma. *Korean Journal of Radiology, 22*(1), 23–40. https://doi.org/10.3348/kjr.2019.0862（PMID: 32901458）

Roberts, K. J., Bannister, C. A., & Schrem, H. (2019). Enzyme replacement improves survival among patients with pancreatic cancer: Results of a population based study. *Pancreatology, 19*(1), 114–121. https://doi.org/10.1016/j.pan.2018.10.010（PMID: 30385188）

Roeland, E. J., Bohlke, K., Baracos, V. E., Bruera, E., Del Fabbro, E., Dixon, S., Fallon, M., Herrstedt, J., Lau, H., Platek, M., Rugo, H. S., Schnipper, H. H., Smith, T. J., Tan, W., & Loprinzi, C. L. (2020). Management of cancer cachexia: ASCO guideline. *Journal of Clinical Oncology, 38*(21), 2438–2453. https://doi.org/10.1200/JCO.20.00611（PMID: 32432946）

Roeland, E. J., Bohlke, K., Baracos, V. E., Smith, T. J., & Loprinzi, C. L. (2023). Cancer cachexia: ASCO guideline rapid recommendation update. *Journal of Clinical Oncology, 41*(25), 4178–4179. https://doi.org/10.1200/JCO.23.01280（PMID: 37467399）

Rompen, I. F., Dekker, E. N., Stoop, T. F., Janssen, Q. P., Homs, M. Y. V., van Tienhoven, G., Wilmink, J. W., Dijkgraaf, M. G. W., van der Kolk, B. M., Bonsing, B. A., de Hingh, I. H., Festen, S., van der Schelling, G., van der Harst, E., van Dam, R. M., Patijn, G. A., Liem, M. S. L., van Santvoort, H. C., Busch, O. R., . . . Dutch Pancreatic Cancer Group. (2026). Staging laparoscopy after neoadjuvant treatment for pancreatic cancer to prevent non-therapeutic laparotomy: Analysis in the PREOPANC-2 randomized trial. *Annals of Surgery*. Advance online publication. https://doi.org/10.1097/SLA.0000000000007025（PMID: 41673930）

Sandhya, L., Devi Sreenivasan, N., Goenka, L., Dubashi, B., Kayal, S., Solaiappan, M., Govindarajalou, R., Kt, H., & Ganesan, P. (2023). Randomized double-blind placebo-controlled study of olanzapine for chemotherapy-related anorexia in patients with locally advanced or metastatic gastric, hepatopancreaticobiliary, and lung cancer. *Journal of Clinical Oncology, 41*(14), 2617–2627. https://doi.org/10.1200/JCO.22.01997（PMID: 36977285）

Sawas, T., Al Halabi, S., Parsi, M. A., & Vargo, J. J. (2015). Self-expandable metal stents versus plastic stents for malignant biliary obstruction: A meta-analysis. *Gastrointestinal Endoscopy, 82*(2), 256–267.e7. https://doi.org/10.1016/j.gie.2015.03.1980（PMID: 25982849）

Schram, A. M., Goto, K., Kim, D. W., Macarulla, T., Hollebecque, A., O'Reilly, E. M., Ou, S. I., Rodon, J., Rha, S. Y., Nishino, K., Duruisseaux, M., Park, J. O., Neuzillet, C., Liu, S. V., Weinberg, B. A., Cleary, J. M., Calvo, E., Umemoto, K., Nagasaka, M., . . . Drilon, A. (2025). Efficacy of zenocutuzumab in NRG1 fusion-positive cancer. *New England Journal of Medicine, 392*(6), 566–576. https://doi.org/10.1056/NEJMoa2405008（PMID: 39908431）

Sharma, A., Kandlakunta, H., Nagpal, S. J. S., Feng, Z., Hoos, W., Petersen, G. M., & Chari, S. T. (2018). Model to determine risk of pancreatic cancer in patients with new-onset diabetes. *Gastroenterology, 155*(3), 730–739.e3. https://doi.org/10.1053/j.gastro.2018.05.023（PMID: 29775599）

Shi, S., Wei, M., Du, N., Li, J., Han, B., Wang, W., Hu, X., Luo, F., Xu, J., & Yu, X. (2026). Chemotherapy-free phase 1/2 trial of HRS-4642 plus adebrelimab in previously treated metastatic KRAS G12D-mutant pancreatic cancer. *Cancer Cell, 44*(10), 2100–2107.e2. https://doi.org/10.1016/j.ccell.2026.08.012（PMID: 42748921）

Singhi, A. D., George, B., Greenbowe, J. R., Chung, J., Suh, J., Maitra, A., Klempner, S. J., Hendifar, A., Javle, M. M., Golan, T., Brand, R. E., Zureikat, A. H., Roy, S., Schrock, A. B., Miller, V. A., Ross, J. S., Ali, S. M., & Bahary, N. (2019). Real-time targeted genome profile analysis of pancreatic ductal adenocarcinomas identifies genetic alterations that might be targeted with existing drugs or used as biomarkers. *Gastroenterology, 156*(8), 2242–2253.e4. https://doi.org/10.1053/j.gastro.2019.02.037（PMID: 30836094）

Singhi, A. D., Lilo, M., Hruban, R. H., Cressman, K. L., Fuhrer, K., & Seethala, R. R. (2014). Overexpression of lymphoid enhancer-binding factor 1 (LEF1) in solid-pseudopapillary neoplasms of the pancreas. *Modern Pathology, 27*(10), 1355–1363. https://doi.org/10.1038/modpathol.2014.40（PMID: 24658583）

Sohal, D. P. S., Duong, M., Ahmad, S. A., Gandhi, N. S., Beg, M. S., Wang-Gillam, A., Wade, J. L., Chiorean, E. G., Guthrie, K. A., Lowy, A. M., Philip, P. A., & Hochster, H. S. (2021). Efficacy of perioperative chemotherapy for resectable pancreatic adenocarcinoma: A phase 2 randomized clinical trial. *JAMA Oncology, 7*(3), 421–427. https://doi.org/10.1001/jamaoncol.2020.7328（PMID: 33475684）

Søreide, K., & Jamieson, N. B. (2026). Outcomes after surgery for locally advanced pancreatic cancer compared to borderline and upfront resectable pancreatic cancer [Editorial]. *Hepatobiliary Surgery and Nutrition, 15*(3), 83. https://doi.org/10.21037/hbsn-2025-aw-868（PMID: 42273578）

Stoffel, E. M., McKernin, S. E., Brand, R., Canto, M., Goggins, M., Moravek, C., Nagarajan, A., Petersen, G. M., Simeone, D. M., Yurgelun, M., & Khorana, A. A. (2019). Evaluating susceptibility to pancreatic cancer: ASCO provisional clinical opinion. *Journal of Clinical Oncology, 37*(2), 153–164. https://doi.org/10.1200/JCO.18.01489（PMID: 30457921）

Strickler, J. H., Satake, H., George, T. J., Yaeger, R., Hollebecque, A., Garrido-Laguna, I., Schuler, M., Burns, T. F., Coveler, A. L., Falchook, G. S., Vincent, M., Sunakawa, Y., Dahan, L., Bajor, D., Rha, S. Y., Lemech, C., Juric, D., Rehn, M., Ngarmchamnanrith, G., . . . Hong, D. S. (2023). Sotorasib in KRAS p.G12C-mutated advanced pancreatic cancer. *New England Journal of Medicine, 388*(1), 33–43. https://doi.org/10.1056/NEJMoa2208470（PMID: 36546651）

Su, Y.-Y., Chiang, N.-J., Li, C.-P., Yen, C.-J., Yang, S.-H., Chou, W.-C., Chen, J.-S., Chiu, T.-J., Chen, Y.-Y., Chuang, S.-C., Bai, L.-Y., Chiu, C.-F., Peng, C.-M., Chan, D.-C., Chiu, S.-C., Yang, Y.-H., Shan, Y.-S., & Chen, L.-T. (2022). Dosing pattern and early cumulative dose of liposomal irinotecan in metastatic pancreatic cancer: A real-world multicenter study. *Frontiers in Oncology, 12*, Article 800842. https://doi.org/10.3389/fonc.2022.800842（PMID: 35814374）

Tai, D., Conroy, T., Lee, J. J. X., Chee, C. E., Hao, C. Y., Wijaya, I., Aggarwal, S., Ueno, M., Jeung, H. C., Hashim, N. M., Tan Chun Bing, J., Chen, L. T., Korphaisarn, K., Tanasanvimon, S., Chou, W. C., Cargullo, E., Muin, N. F. A., Lee, M. A., Ohba, A., . . . Ducreux, M. (2025). Pan-Asian adapted ESMO Clinical Practice Guidelines for the diagnosis, treatment and follow-up of patients with pancreatic cancer. *ESMO Open, 10*(10), Article 105826. https://doi.org/10.1016/j.esmoop.2025.105826（PMID: 41067164）

Taiwan Food and Drug Administration. (2026). *全部藥品許可證資料集* [Data set; InfoId 36; file dated 2026-10-27; downloaded 2026-10-29]. https://data.fda.gov.tw/opendata/exportDataList.do?method=ExportData&InfoId=36&logType=2

Tanaka, M., Ito, H., Ono, Y., Matsueda, K., Mise, Y., Ishizawa, T., Inoue, Y., Takahashi, Y., Hiratsuka, M., Unno, T., & Saiura, A. (2019). Impact of portal vein resection with splenic vein reconstruction after pancreatoduodenectomy on sinistral portal hypertension: Who needs reconstruction? *Surgery, 165*(2), 291–297. https://doi.org/10.1016/j.surg.2018.08.025（PMID: 30268375）

Tempero, M. A., Pelzer, U., O'Reilly, E. M., Winter, J., Oh, D. Y., Li, C. P., Tortora, G., Chang, H. M., Lopez, C. D., Bekaii-Saab, T., Ko, A. H., Santoro, A., Park, J. O., Noel, M. S., Frassineti, G. L., Shan, Y. S., Dean, A., Riess, H., Van Cutsem, E., . . . Reni, M. (2023). Adjuvant nab-paclitaxel + gemcitabine in resected pancreatic ductal adenocarcinoma: Results from a randomized, open-label, phase III trial. *Journal of Clinical Oncology, 41*(11), 2007–2019. https://doi.org/10.1200/JCO.22.01134（PMID: 36521097）

Teoh, A. Y. B., Lakhtakia, S., Tarantino, I., Perez-Miranda, M., Kunda, R., Maluf-Filho, F., Dhir, V., Basha, J., Chan, S. M., Ligresti, D., Ma, M. T. W., de la Serna-Higuera, C., Yip, H. C., Ng, E. K. W., Chiu, P. W. Y., & Itoi, T. (2025). Endoscopic ultrasonography-guided gastroenterostomy versus uncovered duodenal metal stenting for unresectable malignant gastric outlet obstruction (DRA-GOO): A multicentre randomised controlled trial. *The Lancet Gastroenterology & Hepatology, 10*(6), e8–e16. https://doi.org/10.1016/S2468-1253(25)00136-0（PMID: 40347959）

Troncone, E., Fugazza, A., Cappello, A., Del Vecchio Blanco, G., Monteleone, G., Repici, A., Teoh, A. Y. B., & Anderloni, A. (2020). Malignant gastric outlet obstruction: Which is the best therapeutic option?. *World Journal of Gastroenterology, 26*(16), 1847–1860. https://doi.org/10.3748/wjg.v26.i16.1847（PMID: 32390697）

Tsai, H.-L., Huang, C.-W., Lin, Y.-W., Wang, J.-H., Wu, C.-C., Sung, Y.-C., Chen, T.-L., Wang, H.-M., Tang, H.-C., Chen, J.-B., Ke, T.-W., Tsai, C.-S., Huang, H.-Y., & Wang, J.-Y. (2020). Determination of the UGT1A1 polymorphism as guidance for irinotecan dose escalation in metastatic colorectal cancer treated with first-line bevacizumab and FOLFIRI (PURE FIST). *European Journal of Cancer, 138*, 19–29. https://doi.org/10.1016/j.ejca.2020.05.031（PMID: 32829105）

Tufano, A., Ageno, W., Di Micco, P., Niglio, A., Rosa, V., Ballaz, A., Braester, A., Rubio, C. M., Isern, V., Imbalzano, E., Monreal, M., & RIETE Investigators. (2018). Outcomes during anticoagulation in patients with symptomatic vs. incidental splanchnic vein thrombosis. *Thrombosis Research, 164*, 69–74. https://doi.org/10.1016/j.thromres.2018.02.143（PMID: 29499439）

Ueno, H., Ioka, T., Ikeda, M., Ohkawa, S., Yanagimoto, H., Boku, N., Fukutomi, A., Sugimori, K., Baba, H., Yamao, K., Shimamura, T., Sho, M., Kitano, M., Cheng, A. L., Mizumoto, K., Chen, J. S., Furuse, J., Funakoshi, A., Hatori, T., . . . Tanaka, M. (2013). Randomized phase III study of gemcitabine plus S-1, S-1 alone, or gemcitabine alone in patients with locally advanced and metastatic pancreatic cancer in Japan and Taiwan: GEST study. *Journal of Clinical Oncology, 31*(13), 1640–1648. https://doi.org/10.1200/JCO.2012.43.3680（PMID: 23547081）

Uesaka, K., Boku, N., Fukutomi, A., Okamura, Y., Konishi, M., Matsumoto, I., Kaneoka, Y., Shimizu, Y., Nakamori, S., Sakamoto, H., Morinaga, S., Kainuma, O., Imai, K., Sata, N., Hishinuma, S., Ojima, H., Yamaguchi, R., Hirano, S., Sudo, T., & Ohashi, Y. (2016). Adjuvant chemotherapy of S-1 versus gemcitabine for resected pancreatic cancer: A phase 3, open-label, randomised, non-inferiority trial (JASPAC 01). *The Lancet, 388*(10041), 248–257. https://doi.org/10.1016/S0140-6736(16)30583-9（PMID: 27265347）

Umpierrez, G. E., Davis, G. M., ElSayed, N. A., Fadini, G. P., Galindo, R. J., Hirsch, I. B., Klonoff, D. C., McCoy, R. G., Misra, S., Gabbay, R. A., Bannuru, R. R., & Dhatariya, K. K. (2024). Hyperglycemic crises in adults with diabetes: A consensus report. *Diabetes Care, 47*(8), 1257–1275. https://doi.org/10.2337/dci24-0032（PMID: 39052901）

UNICANCER. (n.d.-a). *Multicentric randomized phase III trial comparing adjuvant chemotherapy with gemcitabine versus 5-fluorouracil, leucovorin, irinotecan and oxaliplatin (mFolfirinox) in patients with resected pancreatic adenocarcinoma* (ClinicalTrials.gov Identifier NCT01526135). Retrieved October 29, 2026, from https://clinicaltrials.gov/study/NCT01526135

UNICANCER. (n.d.-b). *Randomized phase II/III trial comparing Folfirinox association [oxaliplatin/irinotecan/LV5FU2] versus gemcitabine in first line of chemotherapy in metastatics pancreas cancers patients* (ClinicalTrials.gov Identifier NCT00112658). Retrieved October 29, 2026, from https://clinicaltrials.gov/study/NCT00112658

Unno, M., Motoi, F., Matsuyama, Y., Satoi, S., Toyama, H., Matsumoto, I., Aosasa, S., Shirakawa, H., Wada, K., Fujii, T., Yoshitomi, H., Takahashi, S., Sho, M., Ueno, H., & Kosuge, T. (2026). Neoadjuvant chemotherapy with gemcitabine and S-1 versus upfront surgery for resectable pancreatic cancer: Results of the randomized phase II/III Prep-02/JSAP05 trial. *Annals of Surgery, 283*(1), 57–64. https://doi.org/10.1097/SLA.0000000000006730（PMID: 40235447）

Vadhan-Raj, S., McNamara, M. G., Venerito, M., Riess, H., O'Reilly, E. M., Overman, M. J., Zhou, X., Vijapurkar, U., Kaul, S., Wildgoose, P., & Khorana, A. A. (2020). Rivaroxaban thromboprophylaxis in ambulatory patients with pancreatic cancer: Results from a pre-specified subgroup analysis of the randomized CASSINI study. *Cancer Medicine, 9*(17), 6196–6204. https://doi.org/10.1002/cam4.3269（PMID: 32663379）

Valeriani, E., Di Nisio, M., Riva, N., Caiano, L. M., Porreca, E., Bang, S.-M., Beyer-Westendorf, J., Sartori, M. T., Barillari, G., Santoro, R., Kamphuisen, P. W., Alatri, A., Malato, A., Vidili, G., Oh, D., Schulman, S., Ageno, W., & International Registry on Splanchnic Vein Thrombosis (IRSVT) study group. (2021). Clinical history of cancer-associated splanchnic vein thrombosis. *Journal of Thrombosis and Haemostasis, 19*(4), 983–991. https://doi.org/10.1111/jth.15214（PMID: 33306241）

van der Gaag, N. A., Rauws, E. A. J., van Eijck, C. H. J., Bruno, M. J., van der Harst, E., Kubben, F. J. G. M., Gerritsen, J. J. G. M., Greve, J. W., Gerhards, M. F., de Hingh, I. H. J. T., Klinkenbijl, J. H., Nio, C. Y., de Castro, S. M. M., Busch, O. R. C., van Gulik, T. M., Bossuyt, P. M. M., & Gouma, D. J. (2010). Preoperative biliary drainage for cancer of the head of the pancreas. *New England Journal of Medicine, 362*(2), 129–137. https://doi.org/10.1056/NEJMoa0903230（PMID: 20071702）

van der Merwe, S. W., van Wanrooij, R. L. J., Bronswijk, M., Everett, S., Lakhtakia, S., Rimbas, M., Hucl, T., Kunda, R., Badaoui, A., Law, R., Arcidiacono, P. G., Larghi, A., Giovannini, M., Khashab, M. A., Binmoeller, K. F., Barthet, M., Perez-Miranda, M., & van Hooft, J. E. (2022). Therapeutic endoscopic ultrasound: European Society of Gastrointestinal Endoscopy (ESGE) guideline. *Endoscopy, 54*(2), 185–205. https://doi.org/10.1055/a-1717-1391（PMID: 34937098）

Van Laethem, J.-L., Hammel, P., Mornex, F., Azria, D., Van Tienhoven, G., Vergauwe, P., Peeters, M., Polus, M., Praet, M., Mauer, M., Collette, L., Budach, V., Lutz, M., Van Cutsem, E., & Haustermans, K. (2010). Adjuvant gemcitabine alone versus gemcitabine-based chemoradiotherapy after curative resection for pancreatic cancer: A randomized EORTC-40013-22012/FFCD-9203/GERCOR phase II study. *Journal of Clinical Oncology, 28*(29), 4450–4456. https://doi.org/10.1200/JCO.2010.30.3446（PMID: 20837948）

van Riet, P. A., Erler, N. S., Bruno, M. J., & Cahen, D. L. (2021). Comparison of fine-needle aspiration and fine-needle biopsy devices for endoscopic ultrasound-guided sampling of solid lesions: A systemic review and meta-analysis. *Endoscopy, 53*(4), 411–423. https://doi.org/10.1055/a-1206-5552（PMID: 32583392）

van Roessel, S., Kasumova, G. G., Verheij, J., Najarian, R. M., Maggino, L., de Pastena, M., Malleo, G., Marchegiani, G., Salvia, R., Ng, S. C., de Geus, S. W., Lof, S., Giovinazzo, F., van Dam, J. L., Kent, T. S., Busch, O. R., van Eijck, C. H., Groot Koerkamp, B., Abu Hilal, M., . . . Besselink, M. G. (2018). International validation of the eighth edition of the American Joint Committee on Cancer (AJCC) TNM staging system in patients with resected pancreatic cancer. *JAMA Surgery, 153*(12), Article e183617. https://doi.org/10.1001/jamasurg.2018.3617（PMID: 30285076）

Vara-Luiz, F., Fernandes, A., Bispo, M., Vilas-Boas, F., Cúrdia-Gonçalves, T., Rodrigues-Pinto, E., & Pinto-Marques, P. (2025). Portuguese Pancreatic Club perspective on the surveillance strategy for intraductal papillary mucinous neoplasms: When and how to do it? *GE Portuguese Journal of Gastroenterology, 32*(6), 438–446. https://doi.org/10.1159/000547298（PMID: 40746378）

Varki, A. (2007). Trousseau's syndrome: Multiple definitions and multiple mechanisms. *Blood, 110*(6), 1723–1729. https://doi.org/10.1182/blood-2006-10-053736（PMID: 17496204）

Vasen, H. F., Gruis, N. A., Frants, R. R., van der Velden, P. A., Hille, E. T., & Bergman, W. (2000). Risk of developing pancreatic cancer in families with familial atypical multiple mole melanoma associated with a specific 19 deletion of p16 (p16-Leiden). *International Journal of Cancer, 87*(6), 809–811. https://doi.org/10.1002/1097-0215(20000915)87:6<809::AID-IJC8>3.0.CO;2-U（PMID: 10956390）

Verbeke, C. S., Leitch, D., Menon, K. V., McMahon, M. J., Guillou, P. J., & Anthoney, A. (2006). Redefining the R1 resection in pancreatic cancer. *British Journal of Surgery, 93*(10), 1232–1237. https://doi.org/10.1002/bjs.5397（PMID: 16804874）

Versteijne, E., Suker, M., Groothuis, K., Akkermans-Vogelaar, J. M., Besselink, M. G., Bonsing, B. A., Buijsen, J., Busch, O. R., Creemers, G. M., van Dam, R. M., Eskens, F. A. L. M., Festen, S., de Groot, J. W. B., Groot Koerkamp, B., de Hingh, I. H., Homs, M. Y. V., van Hooft, J. E., Kerver, E. D., Luelmo, S. A. C., . . . van Tienhoven, G. (2020). Preoperative chemoradiotherapy versus immediate surgery for resectable and borderline resectable pancreatic cancer: Results of the Dutch randomized phase III PREOPANC trial. *Journal of Clinical Oncology, 38*(16), 1763–1773. https://doi.org/10.1200/JCO.19.02274（PMID: 32105518）

Versteijne, E., van Dam, J. L., Suker, M., Janssen, Q. P., Groothuis, K., Akkermans-Vogelaar, J. M., Besselink, M. G., Bonsing, B. A., Buijsen, J., Busch, O. R., Creemers, G. M., van Dam, R. M., Eskens, F. A. L. M., Festen, S., de Groot, J. W. B., Groot Koerkamp, B., de Hingh, I. H., Homs, M. Y. V., van Hooft, J. E., . . . van Eijck, C. H. J. (2022). Neoadjuvant chemoradiotherapy versus upfront surgery for resectable and borderline resectable pancreatic cancer: Long-term results of the Dutch randomized PREOPANC trial. *Journal of Clinical Oncology, 40*(11), 1220–1230. https://doi.org/10.1200/JCO.21.02233（PMID: 35084987）

Von Hoff, D. D., Ervin, T., Arena, F. P., Chiorean, E. G., Infante, J., Moore, M., Seay, T., Tjulandin, S. A., Ma, W. W., Saleh, M. N., Harris, M., Reni, M., Dowden, S., Laheru, D., Bahary, N., Ramanathan, R. K., Tabernero, J., Hidalgo, M., Goldstein, D., . . . Renschler, M. F. (2013). Increased survival in pancreatic cancer with nab-paclitaxel plus gemcitabine. *New England Journal of Medicine, 369*(18), 1691–1703. https://doi.org/10.1056/NEJMoa1304369（PMID: 24131140）

Wainberg, Z. A., Melisi, D., Macarulla, T., Pazo Cid, R., Chandana, S. R., De La Fouchardière, C., Dean, A., Kiss, I., Lee, W. J., Goetze, T. O., Van Cutsem, E., Paulson, A. S., Bekaii-Saab, T., Pant, S., Hubner, R. A., Xiao, Z., Chen, H., Benzaghou, F., & O'Reilly, E. M. (2023). NALIRIFOX versus nab-paclitaxel and gemcitabine in treatment-naive patients with metastatic pancreatic ductal adenocarcinoma (NAPOLI 3): A randomised, open-label, phase 3 trial. *The Lancet, 402*(10409), 1272–1281. https://doi.org/10.1016/S0140-6736(23)01366-1（PMID: 37708904）

Wakabayashi, H., Arai, H., & Inui, A. (2021). The regulatory approval of anamorelin for treatment of cachexia in patients with non-small cell lung cancer, gastric cancer, pancreatic cancer, and colorectal cancer in Japan: Facts and numbers. *Journal of Cachexia, Sarcopenia and Muscle, 12*(1), 14–16. https://doi.org/10.1002/jcsm.12675（PMID: 33382205）

Wang, D., & Jiao, Y. (2025). Pancreatogenic diabetes: Pathophysiology, diagnosis, and management challenges. *World Journal of Gastrointestinal Surgery, 17*(11), Article 112204. https://doi.org/10.4240/wjgs.v17.i11.112204（PMID: 41357647）

Wang-Gillam, A., Hubner, R. A., Siveke, J. T., Von Hoff, D. D., Belanger, B., de Jong, F. A., Mirakhur, B., & Chen, L. T. (2019). NAPOLI-1 phase 3 study of liposomal irinotecan in metastatic pancreatic cancer: Final overall survival analysis and characteristics of long-term survivors. *European Journal of Cancer, 108*, 78–87. https://doi.org/10.1016/j.ejca.2018.12.007（PMID: 30654298）

Wang-Gillam, A., Li, C. P., Bodoky, G., Dean, A., Shan, Y. S., Jameson, G., Macarulla, T., Lee, K. H., Cunningham, D., Blanc, J. F., Hubner, R. A., Chiu, C. F., Schwartsmann, G., Siveke, J. T., Braiteh, F., Moyo, V., Belanger, B., Dhindsa, N., Bayever, E., . . . Chen, L. T. (2016). Nanoliposomal irinotecan with fluorouracil and folinic acid in metastatic pancreatic cancer after previous gemcitabine-based therapy (NAPOLI-1): A global, randomised, open-label, phase 3 trial. *The Lancet, 387*(10018), 545–557. https://doi.org/10.1016/S0140-6736(15)00986-1（PMID: 26615328）

Wente, M. N., Bassi, C., Dervenis, C., Fingerhut, A., Gouma, D. J., Izbicki, J. R., Neoptolemos, J. P., Padbury, R. T., Sarr, M. G., Traverso, L. W., Yeo, C. J., & Büchler, M. W. (2007). Delayed gastric emptying (DGE) after pancreatic surgery: A suggested definition by the International Study Group of Pancreatic Surgery (ISGPS). *Surgery, 142*(5), 761–768. https://doi.org/10.1016/j.surg.2007.05.005（PMID: 17981197）

Wente, M. N., Veit, J. A., Bassi, C., Dervenis, C., Fingerhut, A., Gouma, D. J., Izbicki, J. R., Neoptolemos, J. P., Padbury, R. T., Sarr, M. G., Yeo, C. J., & Büchler, M. W. (2007). Postpancreatectomy hemorrhage (PPH): An International Study Group of Pancreatic Surgery (ISGPS) definition. *Surgery, 142*(1), 20–25. https://doi.org/10.1016/j.surg.2007.02.001（PMID: 17629996）

Wolpin, B. M., Park, W., Garrido-Laguna, I., Spira, A., Starodub, A., Sommerhalder, D., Punekar, S. R., Barve, M., Pelster, M., Herzberg, B., Azad, N. S., Hecht, J. R., Ou, S. H. I., Lin, T., Kar, S., Tao, L., Vora, R., Hegde, A., Aung, K., & Hong, D. S. (2026). Daraxonrasib in previously treated advanced RAS-mutated pancreatic cancer. *New England Journal of Medicine, 394*(18), 1790–1802. https://doi.org/10.1056/NEJMoa2505783（PMID: 42090791）

Wong, G. Y., Schroeder, D. R., Carns, P. E., Wilson, J. L., Martin, D. P., Kinney, M. O., Mantilla, C. B., & Warner, D. O. (2004). Effect of neurolytic celiac plexus block on pain relief, quality of life, and survival in patients with unresectable pancreatic cancer: A randomized controlled trial. *JAMA, 291*(9), 1092–1099. https://doi.org/10.1001/jama.291.9.1092（PMID: 14996778）

Wu, H., Guo, J.-C., Yang, S.-H., Tien, Y.-W., & Kuo, S.-H. (2019). Postoperative imaging and tumor marker surveillance in resected pancreatic cancer. *Journal of Clinical Medicine, 8*(8), Article 1115. https://doi.org/10.3390/jcm8081115（PMID: 31357636）

Wyse, J. M., Carone, M., Paquin, S. C., Usatii, M., & Sahai, A. V. (2011). Randomized, double-blind, controlled trial of early endoscopic ultrasound-guided celiac plexus neurolysis to prevent pain progression in patients with newly diagnosed, painful, inoperable pancreatic cancer. *Journal of Clinical Oncology, 29*(26), 3541–3546. https://doi.org/10.1200/JCO.2010.32.2750（PMID: 21844506）

Xiong, Q., Zhang, Z., Xu, Y., & Zhu, Q. (2022). Pancreatic adenosquamous carcinoma: A rare pathological subtype of pancreatic cancer. *Journal of Clinical Medicine, 11*(24), Article 7401. https://doi.org/10.3390/jcm11247401（PMID: 36556016）

Yang, X., Leslie, G., Doroszuk, A., Schneider, S., Allen, J., Decker, B., Dunning, A. M., Redman, J., Scarth, J., Plaskocinska, I., Luccarini, C., Shah, M., Pooley, K., Dorling, L., Lee, A., Adank, M. A., Adlard, J., Aittomäki, K., Andrulis, I. L., . . . Tischkowitz, M. (2020). Cancer risks associated with germline PALB2 pathogenic variants: An international study of 524 families. *Journal of Clinical Oncology, 38*(7), 674–685. https://doi.org/10.1200/JCO.19.01907（PMID: 31841383）

Yao, D.-W., Qin, M.-Z., Jiang, H.-X., & Qin, S.-Y. (2024). Comparison of EUS-FNA and EUS-FNB for diagnosis of solid pancreatic mass lesions: A meta-analysis of prospective studies. *Scandinavian Journal of Gastroenterology, 59*(8), 972–979. https://doi.org/10.1080/00365521.2024.2354908（PMID: 38769625）

Yao, J. C., Shah, M. H., Ito, T., Bohas, C. L., Wolin, E. M., Van Cutsem, E., Hobday, T. J., Okusaka, T., Capdevila, J., de Vries, E. G. E., Tomassetti, P., Pavel, M. E., Hoosen, S., Haas, T., Lincy, J., Lebwohl, D., Öberg, K., & RAD001 in Advanced Neuroendocrine Tumors, Third Trial (RADIANT-3) Study Group. (2011). Everolimus for advanced pancreatic neuroendocrine tumors. *New England Journal of Medicine, 364*(6), 514–523. https://doi.org/10.1056/NEJMoa1009290（PMID: 21306238）

Yokoi, K., Nakajima, Y., Matsuoka, H., Shinkai, Y., Ishihara, T., Maeda, Y., Kato, T., Katsuno, H., Masumori, K., Kawada, K., Yoshikawa, T., Ito, T., & Kurahashi, H. (2020). Impact of DPYD, DPYS, and UPB1 gene variations on severe drug-related toxicity in patients with cancer. *Cancer Science, 111*(9), 3359–3366. https://doi.org/10.1111/cas.14553（PMID: 32619063）

Zhao, K., Son, S. Y., Sarkar, D., & Santos, E. G. (2024). Trans-splenic percutaneous glue embolization of bleeding gastric varices in the setting of malignant sinistral portal hypertension. *CVIR Endovascular, 7*(1), Article 58. https://doi.org/10.1186/s42155-024-00467-1（PMID: 39066948）

癌症登記中心. (2025). *112年癌症登記長表年報*. https://twcr.tw/wp-content/uploads/2025/12/CA17_LF112.pdf

衛生福利部. (2025, December 30). *公布112年國人癌症登記資料分析結果 守護健康未來 從癌症篩檢開始* [新聞稿]. https://mohw.gov.tw/cp-2704-84987-1.html

衛生福利部. (2026, June 22). *國人死亡人數連續3年下降 十大死因中6項死因人數、死亡率都減少* [新聞稿]. https://mohw.gov.tw/cp-16-86970-1.html

衛生福利部中央健康保險署. (2026). *全民健康保險藥品給付規定：第9節 抗癌瘤藥物* [115年10月22日版公告原文]. https://www.nhi.gov.tw/
