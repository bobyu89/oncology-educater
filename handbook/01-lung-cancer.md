# 肺癌（Lung Cancer）

| 項目 | 本章依據 |
|------|---------|
| 治療指引 | NCCN Guidelines：Non-Small Cell Lung Cancer **Version 9.2026**、Small Cell Lung Cancer **Version 1.2027**（2026-10-29 查詢）；ESMO metastatic NSCLC living guidelines |
| 分期 | AJCC／IASLC 第 9 版，2025 年 1 月 1 日起診斷者適用 |
| 副作用分級 | NCI CTCAE v6.0（2025-07-22 發布）；進行中的臨床試驗仍沿用 v5.0 |
| 健保給付 | 全民健康保險藥品給付規定 第 9 節「抗癌瘤藥物」：等待原文，見 [第 9 段](#9-健保給付與事前審查) |
| 最後更新 | 2026-10-29 |

**這一章的結論先講：** 肺癌治療的第一個岔路是組織型（NSCLC 或 SCLC），第二個岔路是 **biomarker**。晚期非鱗狀 NSCLC 在拿到 EGFR、ALK 等基因結果之前，不要急著開免疫治療；有驅動基因（driver mutation）的病人用標靶藥，沒有的才看 PD-L1 決定免疫治療怎麼用。

---

## 0. 速查卡

| 主題 | 一句話重點 |
|------|-----------|
| 分型 | 國際文獻 NSCLC 約 85%、SCLC 約 15%；**台灣 SCLC 只占約 6%**，非小細胞癌中腺癌占 83% |
| 台灣特色 | 2023 年新診斷人數、2025 年死亡人數都是癌症第 1 名；非吸菸女性肺腺癌多，**EGFR 突變占台灣肺腺癌 55.7%** |
| 晚期非鱗狀 NSCLC 必驗 | EGFR、ALK、ROS1、BRAF V600E、KRAS G12C、MET exon 14 skipping、RET、NTRK1–3、HER2（ERBB2）突變，加上 PD-L1（22C3, TPS） |
| 早期（I–II） | 手術為主；≤2 cm 周邊型可做 segmentectomy；不能開刀用 SBRT |
| 術後輔助 | 依 biomarker：EGFR 用 osimertinib 3 年、ALK 用 alectinib 2 年、其餘用化療 ± 免疫治療 |
| 不可切除 III 期 | 同步化放療（CCRT）→ durvalumab 鞏固 12 個月；EGFR 陽性改用 osimertinib |
| 晚期（IV） | 有 driver：對應標靶藥；無 driver：PD-L1 ≥50% 可單用 pembrolizumab，否則化療 ＋ 免疫 |
| SCLC 局限期 | Cisplatin ＋ etoposide ＋ 同步胸部放療 → durvalumab 鞏固（ADRIATIC） |
| SCLC 廣泛期 | Carboplatin ＋ etoposide ＋ atezolizumab 或 durvalumab，接著免疫維持 |

> [!IMPORTANT]
> **必背數字**
> - Carboplatin 劑量 = 目標 AUC ×（GFR ＋ 25），GFR 上限 125 mL/min → AUC 5 最多 750 mg、AUC 6 最多 900 mg。
> - Pemetrexed 要 CrCl ≥45 mL/min，給藥前 7 天開始吃 folic acid，第一劑前 1 週打 vitamin B12（之後每 9 週）。
> - Osimertinib 80 mg QD；brigatinib 先 90 mg QD × 7 天再加到 180 mg QD。
> - Bevacizumab 不用在鱗狀細胞癌（大咳血風險）。

---

## 1. 流行病學與危險因子

### 1.1 台灣現況

| 指標 | 數字 | 資料來源與年份 |
|------|------|--------------|
| 新診斷人數 | **19,986 人，所有癌症第 1 名**（連續 3 年） | 衛福部 2023 年癌症登記（2025-12-30 公布） |
| 年齡標準化發生率 | 每 10 萬人 44.9 人；診斷中位年齡 66 歲 | 同上 |
| 死亡人數 | **10,831 人，癌症死因第 1 名**（男女皆第 1），占癌症死亡 19.75% | 衛福部 2025 年死因統計（2026-06-22 公布） |
| 組織型 | 非小細胞癌中**腺癌占 82.85%**（女性 92.99%、男性 71.73%），鱗狀細胞癌 10.06%；SCLC 約占全部肺癌 5.7% | 2023 年癌登長表 |
| 診斷時期別 | 非小細胞癌 IV 期 38.79%（男 45.96%、女 32.65%）、I 期 40.21%；SCLC IV 期 74.57% | 2023 年癌登長表（AJCC 第 8 版） |

長表資料只涵蓋長表申報醫院、且包含原位癌，所以總數和官方發生人數不同。

> [!IMPORTANT]
> **台灣肺癌和西方不一樣的地方**
> 台灣肺癌以**腺癌**為主，女性病人超過九成是腺癌、且多數不吸菸；SCLC 比例（約 6%）明顯低於西方常引用的 15%。這也是台灣 EGFR 突變比例高、標靶藥用得多的原因。

### 1.2 危險因子

| 類別 | 危險因子 | 臨床意義 |
|------|---------|---------|
| 吸菸 | 主動吸菸（看 pack-years）、二手菸 | SCLC 與鱗狀細胞癌幾乎都和吸菸有關；戒菸 15 年後風險才明顯下降 |
| 環境 | 廚房油煙、空氣污染（PM2.5）、氡氣、石綿 | 台灣非吸菸女性肺腺癌的可能相關因子 |
| 個人病史 | COPD、肺纖維化、結核病史、胸部放療史 | 慢性發炎與疤痕組織 |
| 家族史 | 一等親罹患肺癌 | 台灣 LDCT 篩檢的收案條件之一 |

### 1.3 篩檢：低劑量電腦斷層（LDCT）

- **NLST**（National Lung Screening Trial Research Team, 2011）：高風險吸菸者用 LDCT 篩檢，比胸部 X 光降低肺癌死亡率 20%。
- **NELSON**（de Koning et al., 2020）：男性高風險族群 10 年追蹤，肺癌死亡率下降約 24%。

**台灣肺癌早期偵測計畫**（國民健康署，2022 年 7 月 1 日開辦，2025 年 1 月 1 日放寬）

| 族群 | 條件 | 頻率 |
|------|------|------|
| 肺癌家族史 | 父母、子女或兄弟姊妹（有血緣）曾罹患肺癌；**男性 45–74 歲、女性 40–74 歲** | 每 2 年 1 次免費 LDCT |
| 重度吸菸者 | **50–74 歲**、吸菸史 **≥20 包年**（2025 年起由 30 包年下修），仍在吸菸或戒菸未滿 15 年 | 每 2 年 1 次免費 LDCT |

- 包年（pack-years）= 每天幾包 × 抽幾年。例如每天 1 包抽 20 年，或每天半包抽 40 年，都是 20 包年。
- 吸菸者篩檢時要同時轉介戒菸服務。
- 成效：截至 2024 年底篩檢 158,937 人，發現 1,957 例肺癌，其中 83% 為 0–I 期（衛福部）。

**TALENT 研究**：台灣 17 家醫學中心、12,011 位不吸菸（或輕度且已戒菸）的高風險民眾接受 LDCT，肺癌偵測率 2.6%（侵襲癌 2.1%、原位腺癌 0.5%），77.4% 為 I 期，幾乎都是腺癌。家族史、女性、60 歲以上是獨立危險因子；二手菸、烹飪油煙與過去肺病史**沒有**顯著相關。作者也提醒原位腺癌可能有過度診斷的問題（Chang et al., 2024）。

> [!IMPORTANT]
> **台灣篩檢的特色**
> 台灣是第一個把「家族史」納入國家肺癌篩檢的國家，依據就是 TALENT 研究。這和美國只篩重度吸菸者的做法不同，常被拿來比較。

---

## 2. 病理與分子標記

### 2.1 組織型與免疫組織化學染色

| 組織型 | 比例 | 好發位置 | 常用 IHC |
|--------|------|---------|---------|
| 腺癌（adenocarcinoma） | NSCLC 最多 | 周邊 | TTF-1(+)、Napsin A(+) |
| 鱗狀細胞癌（squamous cell carcinoma, SCC） | 次之 | 中央、近肺門 | p40(+)、CK5/6(+) |
| 大細胞癌（large cell carcinoma） | 少 | 不定 | 排除性診斷 |
| 小細胞癌（small cell lung cancer, SCLC） | 約 15% | 中央 | synaptophysin、chromogranin、INSM1、CD56(+)；Ki-67 很高；多數 TTF-1(+) |

> [!TIP]
> **TTF-1 和 p40 怎麼記**
> 把 TTF-1 想成「腺體的身分證」，p40 想成「鱗狀上皮的身分證」。病理報告寫 TTF-1(+)、p40(−) 就往腺癌走；反過來就往 SCC 走。小活檢分不出來時，報告會寫 NSCLC-NOS，這時仍應送 biomarker。

### 2.2 必驗 biomarker

| 基因變異 | 東亞肺腺癌約略比例 | 代表藥物 | 備註 |
|---------|-----------------|---------|------|
| EGFR exon 19 del／L858R | 亞洲 51.4%（PIONEER）；台灣 55.7%（兩者占 EGFR 突變約 85–90%） | osimertinib 等 EGFR TKI | 非吸菸、女性、腺癌較常見 |
| EGFR 非典型突變（G719X、L861Q、S768I） | 少見 | afatinib、osimertinib | |
| EGFR exon 20 insertion | 少見 | amivantamab ＋ 化療 | 對傳統 EGFR TKI 反應差 |
| ALK 融合 | 台灣約 4%（EGFR 陰性者中 9.8%） | alectinib、brigatinib、lorlatinib | 年輕、非吸菸；腦轉移常見 |
| ROS1 融合 | 1–2% | entrectinib、crizotinib、repotrectinib | |
| KRAS 突變（含 G12C） | 台灣約 5%，遠低於西方 | sotorasib、adagrasib（G12C，二線） | 多見於吸菸者 |
| BRAF 突變 | 台灣約 0.7% | dabrafenib ＋ trametinib（V600E） | |
| MET exon 14 skipping | 約 2–3% | capmatinib、tepotinib | 高齡者較多 |
| RET 融合 | 1–2% | selpercatinib、pralsetinib | |
| HER2（ERBB2）突變 | 台灣約 2% | trastuzumab deruxtecan、zongertinib 等（二線） | |
| NTRK1–3 融合 | <1% | larotrectinib、entrectinib | 跨癌別適應症 |

台灣數字來自 1,772 位未治療肺腺癌的多中心研究（Hsu et al., 2015），ALK 只在 EGFR 陰性者檢測；亞洲數字來自 PIONEER（Shi et al., 2014）。沒有標台灣的列為國際文獻的約略值，依族群與檢測方法而異。

**PD-L1（22C3 抗體）TPS 分層：** <1%、1–49%、≥50%。PD-L1 決定的是「沒有 driver 時」免疫治療怎麼用，**不能**取代基因檢測。

> [!WARNING]
> **為什麼要等 biomarker 才開免疫治療**
> EGFR、ALK 陽性的病人對免疫單藥效果差；如果先打 PD-1/PD-L1 抑制劑、之後再接 osimertinib，15% 發生 3–4 級 irAE，**3 個月內接上的更高達 24%**，中位發生時間是開始 osimertinib 後 20 天，幾乎都要住院用類固醇。反過來（先 osimertinib 再免疫）或免疫後改用其他 EGFR TKI，則沒有觀察到嚴重 irAE（Schoenfeld et al., 2019）。臨床上寧可多等一兩週基因報告，或先用 plasma ctDNA 送驗加快速度。

### 2.3 檢測方法

| 方法 | 優點 | 限制 |
|------|------|------|
| 組織 NGS（next-generation sequencing） | 一次驗完所有基因，含融合基因 | 需要足夠組織、等待時間較長 |
| 血液 ctDNA（liquid biopsy） | 快、免侵入；可找抗藥機轉（如 T790M） | 陰性不能排除，需再驗組織 |
| 單基因 PCR（如 EGFR） | 快、便宜 | 驗不到其他基因，容易耗盡組織 |
| IHC／FISH（ALK、ROS1） | 普及 | ROS1 IHC 陽性需確認 |

> [!CAUTION]
> **健保 NGS 給付**
> 健保自 2024 年起給付部分癌別的 NGS 檢測（屬醫療服務給付項目，不在藥品給付規定第 9 節）。給付癌別、檢測時機與次數限制，請以健保署公告原文為準，本段待核對後補上。

---

## 3. 診斷與分期

### 3.1 Work-up 流程

1. **病史與身體評估**：吸菸 pack-years、職業暴露、ECOG performance status、體重減輕。
2. **抽血**：CBC、腎肝功能、電解質（Na、Ca）、ALP、LDH。
3. **影像**：胸部及上腹部（含腎上腺）顯影 CT；預計根治性治療（I–III 期）做 PET-CT；II–IV 期做腦部 MRI（NCCN 建議；IB 期可考慮）。
4. **取得組織**：依病灶位置選擇 CT 導引切片、支氣管鏡、EBUS-TBNA；有肋膜積水抽水送細胞學。原則是**同一次檢查同時取得診斷與最高分期**（例如 EBUS 一次做縱膈腔淋巴結）。
5. **縱膈腔分期**：PET-CT 懷疑 N2/N3、中央型腫瘤或腫瘤 >3 cm，手術前以 EBUS-TBNA 或縱膈腔鏡確認。
6. **手術評估**：肺功能（FEV1、DLCO），計算術後預估值 ppoFEV1、ppoDLCO。

### 3.2 TNM 第 9 版

T 分類與第 8 版相同；第 9 版主要改在 **N2 細分為 N2a／N2b**，以及 **M1c 細分為 M1c1／M1c2**。

| 分類 | 定義 |
|------|------|
| Tis | 原位癌 |
| T1mi | 微侵犯腺癌（≤3 cm，侵犯 ≤5 mm） |
| T1a／T1b／T1c | ≤1 cm／>1–2 cm／>2–3 cm |
| T2a | >3–4 cm；或侵犯主支氣管（未達隆突）、臟層肋膜，或造成延伸到肺門的肺塌陷／阻塞性肺炎 |
| T2b | >4–5 cm |
| T3 | >5–7 cm；或侵犯胸壁（含壁層肋膜、上溝）、膈神經、壁層心包膜；或同一肺葉另有腫瘤結節 |
| T4 | >7 cm；或侵犯橫膈、縱膈腔、心臟、大血管、氣管、喉返神經、食道、椎體、隆突；或同側不同肺葉另有腫瘤結節 |
| N0 | 無區域淋巴結轉移 |
| N1 | 同側支氣管周圍、肺門或肺內淋巴結 |
| N2a | 同側縱膈腔或隆突下淋巴結，**單一站** |
| N2b | 同側縱膈腔或隆突下淋巴結，**多站** |
| N3 | 對側縱膈腔或肺門淋巴結；任何斜角肌或鎖骨上淋巴結 |
| M1a | 對側肺葉腫瘤結節；肋膜或心包膜結節、惡性肋膜或心包膜積水 |
| M1b | 單一器官的單一胸腔外轉移 |
| M1c1 | 單一器官系統的多處胸腔外轉移 |
| M1c2 | 多個器官系統的多處胸腔外轉移 |

**第 9 版分期組合（M0）**

| T ＼ N | N0 | N1 | N2a | N2b | N3 |
|--------|----|----|-----|-----|----|
| T1a | IA1 | **IIA** | **IIB** | IIIA | IIIB |
| T1b | IA2 | **IIA** | **IIB** | IIIA | IIIB |
| T1c | IA3 | **IIA** | **IIB** | IIIA | IIIB |
| T2a | IB | IIB | IIIA | **IIIB** | IIIB |
| T2b | IIA | IIB | IIIA | **IIIB** | IIIB |
| T3 | IIB | IIIA | **IIIA** | IIIB | IIIC |
| T4 | IIIA | IIIA | IIIB | IIIB | IIIC |

- 任何 T、任何 N 加上 **M1a 或 M1b → IVA**；**M1c1 或 M1c2 → IVB**。Tis N0 M0 為 0 期。
- **粗體是和第 8 版不同的格子**：T1N1 由 IIB 降為 IIA；T1N2a 由 IIIA 降為 IIB；T3N2a 由 IIIB 降為 IIIA；T2N2b 由 IIIA 升為 IIIB（Rami-Porta et al., 2024）。
- 適用時間：AJCC／IASLC 肺癌第 9 版自 2025 年 1 月 1 日起診斷的病人適用；UICC 第 9 版全書建議 2026 年 1 月 1 日起使用。SCLC 也已驗證適用第 9 版。

> [!CAUTION]
> **台灣癌登仍用第 8 版**
> 2023 年台灣癌症登記報告的肺癌期別仍以 AJCC 第 8 版統計，2025 年起診斷的個案何時改用第 9 版尚未確認。閱讀統計報表與臨床病歷時，先確認寫的是哪一版。

### 3.3 SCLC 分期

臨床上仍常用退伍軍人醫院（VA）二分法，NCCN 同時要求記錄 TNM：

- **局限期（limited stage, LS）**：病灶可以涵蓋在一個安全的放射治療照野內（大致是 TNM I–III 期，排除肺內多發結節太廣的 T3–4）。
- **廣泛期（extensive stage, ES）**：超出單一放射照野，包括 IV 期、惡性肋膜積水。約 2/3 病人診斷時已是廣泛期。

---

## 4. 治療策略（依分期）

### 4.1 NSCLC I–II 期：可切除

**手術是主角。**

- **標準術式**：肺葉切除（lobectomy）＋系統性縱膈腔淋巴結廓清。
- **≤2 cm 周邊型、N0**：肺節切除（segmentectomy）或楔狀切除不劣於肺葉切除。JCOG0802（Saji et al., 2022）中 segmentectomy 組 5 年整體存活率甚至較高（94.3% 對 91.1%），但局部復發較多（10.5% 對 5.4%），術後追蹤不能放鬆；CALGB 140503（Altorki et al., 2023）亞肺葉切除的無病存活不劣於肺葉切除（5 年 DFS 63.6% 對 64.1%）。
- **不能開刀或拒絕手術**：立體定位放射治療（stereotactic body radiotherapy, SBRT）。

**術後輔助治療（依 biomarker 分流）**

| 條件 | 輔助治療 | 依據 |
|------|---------|------|
| II–IIIA 期（IB 期 ≥4 cm 視風險） | Cisplatin 為主的雙藥化療 × 4 週期 | LACE 匯總分析：死亡風險 HR 0.89，5 年存活絕對增加 5.4%；IA 期反而可能有害（HR 1.40），所以 IA 期不做輔助化療（Pignon et al., 2008） |
| EGFR ex19del／L858R，IB–IIIA 期 | 化療（視情況）後 **osimertinib 80 mg QD × 3 年** | ADAURA：DFS HR 0.20；整體存活 HR 0.49（Wu et al., 2020；Tsuboi et al., 2023） |
| ALK 陽性，IB（≥4 cm）–IIIA 期 | **Alectinib 600 mg BID × 2 年** | ALINA：II–IIIA 期 DFS HR 0.24（Wu et al., 2024） |
| PD-L1 ≥1%、無 EGFR/ALK，II–IIIA 期 | 輔助化療後 atezolizumab 1,200 mg q3w × 16 週期（1 年） | IMpower010：初次分析 DFS HR 0.66（Felip et al., 2021）。5 年更新中只有 **PD-L1 ≥50%** 的整體存活有顯著改善（HR 0.47），PD-L1 ≥1% 整體的存活差異不顯著（Felip et al., 2025） |
| 無 EGFR/ALK，IB（≥4 cm）–IIIA 期 | 輔助化療後 pembrolizumab 200 mg q3w，最多 18 週期（約 1 年） | PEARLS/KEYNOTE-091：DFS 53.6 對 42.0 個月（HR 0.76）；但 PD-L1 ≥50% 這個共同主要終點未達顯著（O'Brien et al., 2022） |

**術前／圍術期（腫瘤 ≥4 cm 或淋巴結陽性，先排除 EGFR/ALK）**

| 方案 | 內容 | 結果 |
|------|------|------|
| 術前（neoadjuvant） | Nivolumab 360 mg ＋ 含鉑雙藥 q3w × 3 → 手術 | CheckMate 816：pCR 24.0% 對 2.2%，EFS 31.6 對 20.8 個月（Forde et al., 2022）；5 年整體存活 65.4% 對 55.0%（HR 0.72；Forde et al., 2025） |
| 圍術期：pembrolizumab | 術前 pembrolizumab 200 mg ＋ cisplatin 雙藥 q3w × 4 → 手術 → 術後 pembrolizumab 最多 13 週期 | KEYNOTE-671：EFS 47.2 對 18.3 個月；36 個月整體存活 71% 對 64%（HR 0.72）（Wakelee et al., 2023；Spicer et al., 2024） |
| 圍術期：durvalumab | 術前 durvalumab 1,500 mg ＋ 化療 q3w × 4 → 手術 → 術後 durvalumab q4w × 12 | AEGEAN：EFS HR 0.68、pCR 17.2% 對 4.3%（Heymach et al., 2023）；期中整體存活尚未顯著（Heymach et al., 2026） |
| 圍術期：nivolumab | 術前 nivolumab 360 mg ＋ 化療 q3w × 4 → 手術 → 術後 nivolumab 480 mg q4w × 1 年 | CheckMate 77T：EFS HR 0.58、pCR 25.3% 對 4.7%（Cascone et al., 2024）；整體存活結果尚未發表 |

> [!TIP]
> **術前免疫的比喻**
> 腫瘤還在身體裡的時候，它本身就是「抗原教材」。術前先給免疫治療，免疫系統可以邊看教材邊學怎麼認腫瘤；等手術拿掉腫瘤後，學會的 T 細胞繼續巡邏殘存的微小轉移。這也是 pCR（病理完全反應）能當早期療效指標的原因。

### 4.2 NSCLC III 期

III 期是異質性最高的一期，**一定要多專科團隊（MDT）討論**可不可以切。

- **可切除（多為 IIIA）**：走 4.1 的圍術期化療 ＋ 免疫路線。
- **不可切除**：
  1. **同步化放療（concurrent chemoradiotherapy, CCRT）**：放療 60 Gy／30 次，搭配含鉑雙藥（cisplatin ＋ etoposide、carboplatin ＋ paclitaxel 每週，或非鱗狀用 cisplatin ＋ pemetrexed）。
  2. CCRT 後沒有惡化 → **durvalumab 鞏固治療 12 個月**。PACIFIC：PFS 16.8 對 5.6 個月；5 年整體存活率 42.9% 對 33.4%（Antonia et al., 2017；Spigel et al., 2022）。
  3. **EGFR 陽性**：CCRT 後改用 **osimertinib 直到疾病惡化**。LAURA：PFS 39.1 對 5.6 個月；放射性肺炎 48% 對 38%，多為 1–2 級（Lu et al., 2024）。

> [!WARNING]
> **CCRT 後的肺炎要分清楚**
> CCRT 後接 durvalumab 的病人，咳嗽、喘、CT 毛玻璃病灶可能是放射性肺炎、免疫相關肺炎或感染。放射性肺炎通常在放療後 1–6 個月、病灶貼著照野邊界；免疫性肺炎可跨出照野。處置先排除感染，G2 以上暫停 durvalumab 並用類固醇（見 [irAE 章](00-shared/04-irae.md)）。

### 4.3 NSCLC IV 期

**決策順序：組織型 → biomarker → PD-L1 → ECOG。**

#### 有驅動基因：標靶治療優先

| 變異 | 第一線（偏好） | 其他選擇／惡化後 | 關鍵試驗 |
|------|-------------|---------------|---------|
| EGFR ex19del／L858R | **Osimertinib**；osimertinib ＋ pemetrexed/鉑類；amivantamab ＋ lazertinib | Gefitinib、erlotinib、afatinib、dacomitinib；惡化後再切片找抗藥機轉 | FLAURA、FLAURA2、MARIPOSA |
| EGFR T790M（第一、二代 TKI 後） | Osimertinib | | AURA3：PFS 10.1 對 4.4 個月 |
| Osimertinib 後惡化 | Amivantamab ＋ carboplatin ＋ pemetrexed；含鉑化療 | 依抗藥機轉（如 MET 放大）；datopotamab deruxtecan（EGFR TKI 與含鉑化療都用過後） | MARIPOSA-2：PFS 6.3 對 4.2 個月；Dato-DXd 匯總分析反應率 43% |
| EGFR 非典型突變 | Afatinib 或 osimertinib | | |
| EGFR exon 20 insertion | Amivantamab ＋ carboplatin ＋ pemetrexed；sunvozertinib | | PAPILLON：PFS 11.4 對 6.7 個月；WU-KONG28：sunvozertinib 對化療 PFS 10.3 對 7.5 個月 |
| ALK | **Alectinib**、brigatinib、**lorlatinib** | 第二代後惡化用 lorlatinib | ALEX、ALTA-1L、CROWN |
| ROS1 | Entrectinib、crizotinib、repotrectinib、taletrectinib | 後線 repotrectinib、taletrectinib（對 G2032R 抗藥突變仍有效） | PROFILE 1001、TRIDENT-1、TRUST |
| BRAF V600E | Dabrafenib ＋ trametinib；encorafenib ＋ binimetinib | | BRF113928、PHAROS（未治療者反應率 75%） |
| MET exon 14 | Capmatinib、tepotinib | | GEOMETRY mono-1、VISION |
| RET | Selpercatinib、pralsetinib | | LIBRETTO-431：PFS 24.8 對 11.2 個月 |
| NTRK | Larotrectinib、entrectinib | | |
| KRAS G12C | 化療 ＋ 免疫（同無 driver） | 二線 sotorasib、adagrasib | CodeBreaK 200：PFS 5.6 對 4.5 個月；KRYSTAL-12：PFS 5.5 對 3.8 個月 |
| HER2 突變 | 化療 ＋ 免疫 | 二線 trastuzumab deruxtecan 5.4 mg/kg、zongertinib | DESTINY-Lung02：反應率 49.0%；Beamion LUNG-1：zongertinib 反應率 71% |

**EGFR 第一線三個選項怎麼比**

| 方案 | PFS（月） | 整體存活 | 代價 |
|------|----------|---------|------|
| Osimertinib 單藥（FLAURA） | 18.9 對 10.2（HR 0.46） | 38.6 對 31.8 個月（HR 0.80） | 口服、最方便；3 級以上副作用 34% |
| Osimertinib ＋ 化療（FLAURA2） | 25.5 對 16.7（HR 0.62） | 47.5 對 37.6 個月（HR 0.77） | 3 級以上副作用 70% 對 34%，主要來自化療 |
| Amivantamab ＋ lazertinib（MARIPOSA） | 23.7 對 16.6（HR 0.70） | 優於 osimertinib（HR 0.75；3 年 60% 對 51%） | 3 級以上副作用 80% 對 52%；輸注反應 63%、皮疹 86%、靜脈血栓 36% |

（Soria et al., 2018；Ramalingam et al., 2020；Planchard et al., 2023；Jänne et al., 2026；Cho et al., 2024；Yang et al., 2025）

三個方案都比對照組好，差別在**病人願意付出多少副作用與回診負擔**。腦轉移多、腫瘤負荷大的病人，較常考慮合併治療；高齡或想維持生活品質的病人，osimertinib 單藥仍是合理選擇。

> [!TIP]
> **EGFR TKI 的比喻**
> EGFR 突變像油門卡住的車，一直往前衝（細胞一直分裂）。TKI 是卡在油門下的木塊。T790M 是車子把油門形狀改了，舊木塊卡不進去；osimertinib 是照新形狀做的木塊。Exon 20 insertion 則是油門從一開始就長得不一樣，傳統木塊都卡不住，所以要換成 amivantamab 這種從外面把整台車攔下來的方法。

> [!IMPORTANT]
> **ALK 的考點**
> ALK 陽性病人腦轉移比例高，第一線偏好穿透中樞神經系統好的藥。
> - CROWN：lorlatinib 5 年 PFS 60% 對 crizotinib 8%，顱內惡化風險 HR 0.06（Solomon et al., 2024）；7 年 PFS 55% 對 3%（Shaw et al., 2026）。
> - ALEX：alectinib PFS 34.8 對 10.9 個月（Mok et al., 2020）；最終整體存活 81.1 對 54.2 個月，但 HR 0.78（95% CI 0.56–1.08）未達統計顯著（Peters et al., 2026）。

> [!TIP]
> **PFS 好不等於活得比較久**
> 很多標靶試驗 PFS 大幅改善，整體存活（OS）卻沒有顯著差異，例如 IPASS、AURA3、PROFILE 1014、ALTA-1L、ALEX 最終分析。主要原因是**交叉治療（crossover）**：對照組惡化後幾乎都會換到試驗藥，存活差距被拉平。讀試驗時，PFS 像「這條路能撐多久不塞車」，OS 是「最後到不到得了終點」；換路的人多了，終點時間就會接近。

#### 沒有驅動基因：看 PD-L1

| PD-L1 TPS | 非鱗狀 | 鱗狀 |
|-----------|-------|------|
| ≥50% | Pembrolizumab、atezolizumab 或 cemiplimab 單藥；或化療 ＋ 免疫 | 同左 |
| 1–49% | 化療 ＋ 免疫 | 化療 ＋ 免疫 |
| <1% | 化療 ＋ 免疫（含雙免疫選項） | 化療 ＋ 免疫 |

常用的化療 ＋ 免疫組合：

- **非鱗狀**：carboplatin（或 cisplatin）＋ pemetrexed ＋ pembrolizumab × 4 → pembrolizumab ＋ pemetrexed 維持（KEYNOTE-189；Gandhi et al., 2018）。
- **鱗狀**：carboplatin ＋ paclitaxel 或 nab-paclitaxel ＋ pembrolizumab × 4 → pembrolizumab 維持（KEYNOTE-407；Paz-Ares et al., 2018）。
- **其他**：atezolizumab ＋ bevacizumab ＋ carboplatin ＋ paclitaxel（IMpower150，僅非鱗狀）；nivolumab ＋ ipilimumab ± 兩週期化療（CheckMate 227、9LA）；durvalumab ＋ tremelimumab ＋ 化療（POSEIDON）。

| 試驗 | 族群 | 主要結果 |
|------|------|---------|
| KEYNOTE-024（Reck et al., 2016） | PD-L1 ≥50% | Pembrolizumab 對化療 PFS 10.3 對 6.0 個月；5 年 OS 31.9% 對 16.3% |
| KEYNOTE-189（Gandhi et al., 2018） | 非鱗狀，不分 PD-L1 | 加 pembrolizumab 死亡風險 HR 0.49 |
| KEYNOTE-407（Paz-Ares et al., 2018） | 鱗狀 | OS 15.9 對 11.3 個月 |

**第二線（第一線已用過免疫）**：docetaxel ± ramucirumab（REVEL：OS 10.5 對 9.1 個月；Garon et al., 2014）。第一線沒用過免疫者，可用免疫單藥。

**ECOG 狀態**：ECOG 0–2 可考慮上述治療；ECOG 3–4 以最佳支持治療為主（有 driver 者，標靶藥仍可能讓體能狀態快速改善）。

**寡轉移（oligometastatic）**：轉移處少（常見定義 ≤3–5 處），系統治療有效後，可考慮對所有病灶做局部治療（手術或 SBRT）。

### 4.4 SCLC

SCLC 長得快、對化放療一開始很敏感，但復發快。**時間就是治療**：確診後盡快開始。

**局限期（LS-SCLC）**

1. T1–2 N0（極少數）：肺葉切除 ＋ 縱膈腔淋巴結廓清 → 輔助化療。
2. 多數：**cisplatin ＋ etoposide × 4 週期 ＋ 同步胸部放療**（儘早，第 1–2 週期開始）。
   - 45 Gy 一天兩次、3 週完成：比一天一次的 45 Gy 存活好（5 年 26% 對 16%），但 3 級食道炎較多（27% 對 11%）（Turrisi et al., 1999）。
   - 66 Gy 一天一次（33 次）：CONVERT 試驗中沒有優於一天兩次（OS 25 對 30 個月，差異不顯著），作者建議一天兩次仍是標準（Faivre-Finn et al., 2017）。
3. CCRT 後沒有惡化 → **durvalumab 1,500 mg q4w 鞏固最多 24 個月**。ADRIATIC：OS 55.9 對 33.4 個月（HR 0.73）；3–4 級肺炎 3.1% 對 2.6%（Cheng et al., 2024）。
4. 預防性全腦放療（PCI）或定期腦部 MRI 追蹤，與病人討論。

**廣泛期（ES-SCLC）**

1. **Carboplatin ＋ etoposide ＋ atezolizumab**（IMpower133：OS 12.3 對 10.3 個月，HR 0.70；Horn et al., 2018）或 **＋ durvalumab**（CASPIAN：OS 13.0 對 10.3 個月，HR 0.73；3 年存活 17.6% 對 5.8%；Paz-Ares et al., 2019, 2022），共 4 週期 → 免疫維持。
2. 維持期可用 **lurbinectedin ＋ atezolizumab**：IMforte 試驗中 PFS（HR 0.54）與整體存活（HR 0.73）都優於 atezolizumab 單獨維持，但 3–4 級副作用較多（38% 對 22%），lurbinectedin 要合併 G-CSF 預防（Paz-Ares et al., 2025）。台灣也是 IMforte 的收案國家。
3. 腦部：以 MRI 定期追蹤為主。日本試驗中，在每 3 個月 MRI 追蹤下做 PCI 不但沒有存活好處，數字上還較差（11.6 對 13.7 個月，HR 1.27）（Takahashi et al., 2017）。

**復發 SCLC**

| 情境 | 選擇 | 依據 |
|------|------|------|
| 距上次含鉑化療 ≥6 個月才復發（敏感型） | 再用含鉑 ＋ etoposide | |
| <6 個月復發（抗藥型）或不適合再用鉑 | **Tarlatamab**（第一優先）、lurbinectedin、topotecan | DeLLphi-304：tarlatamab 對化療 OS 13.6 對 8.3 個月（HR 0.60），3 級以上副作用 54% 對 80%（Mountzios et al., 2025）；lurbinectedin 二線反應率 35.2%（Trigo et al., 2020） |

**Tarlatamab** 是 DLL3 × CD3 雙特異性 T 細胞銜接抗體（bispecific T-cell engager），會引起細胞激素釋放症候群（CRS）與神經毒性（ICANS），前兩劑要監測（見 [腫瘤急症章](00-shared/02-oncologic-emergencies.md)）。

> [!TIP]
> **雙特異性抗體的比喻**
> Tarlatamab 一手抓住腫瘤細胞上的 DLL3，一手抓住 T 細胞的 CD3，像幫 T 細胞和腫瘤細胞「牽線配對」。配對成功、T 細胞大量活化時，會一口氣放出細胞激素，所以第一次給藥最容易發生 CRS。

### 4.5 新藥在台灣的上市狀態

指引寫的藥，台灣不一定買得到；買得到也不一定有健保。下表是近兩年國外核准的肺癌新藥在台灣的藥證狀態（TFDA 藥品許可證資料，2026-10-27 版）。健保給付另見第 9 段。

| 藥物 | 用途 | 美國 FDA | 台灣藥證 |
|------|------|---------|---------|
| Tarlatamab | 含鉑後惡化的 ES-SCLC | 2024-05 加速核准，2025-11 依 DeLLphi-304 完全核准 | **有**（2025-02-26） |
| Lurbinectedin ＋ atezolizumab | ES-SCLC 第一線維持 | 2025-10 | 有 lurbinectedin 藥證，含維持治療適應症（加入日期待確認） |
| Amivantamab 皮下劑型 | 與靜脈劑型相同的 EGFR 適應症 | 2025-12 | **有**（2026-06-10） |
| Lazertinib | 合併 amivantamab 第一線 | 已核准 | **有**（2025-06-24） |
| Repotrectinib | ROS1、NTRK | 已核准 | **有**（2025-04-11） |
| Sevabertinib | HER2 突變 NSCLC | 2025-11（後線）、2026-09（第一線） | **有**（2026-06-11，僅限曾接受治療者） |
| Datopotamab deruxtecan | EGFR 突變 NSCLC（後線） | 2025-06 加速核准 | 台灣只有乳癌適應症，**沒有肺癌適應症** |
| Zongertinib | HER2 突變 NSCLC | 2025-08（後線）、2026-02（第一線） | **無** |
| Sunvozertinib | EGFR exon 20 insertion | 2025-07 加速核准 | **無** |
| Taletrectinib | ROS1 | 2025-06 | **無** |

> [!NOTE]
> **藥證、健保、院內處方集是三件事**
> 有藥證代表可以合法使用；健保給付要另外符合第 9 節條件；醫院是否進藥則看院內藥事委員會。病人問「這個新藥可以用嗎」，要分這三層回答。上表依 2026-10-27 資料整理，藥證會持續更新。

---

## 5. 常用處方（Regimen）

> [!NOTE]
> **劑量與輸注時間依院內處方集**
> 以下為指引與試驗的標準劑量。輸注時間、水化液、止吐藥組合與調劑流程各院不同，開立前以單位的化療 protocol 為準。劑量計算方法見 [化療基礎與劑量計算](00-shared/01-chemo-basics.md)。

### 5.1 NSCLC 靜脈處方

| 處方 | 劑量與週期 | 前置用藥與注意 |
|------|-----------|--------------|
| Carboplatin ＋ pemetrexed ＋ pembrolizumab | Pembrolizumab 200 mg D1 ＋ pemetrexed 500 mg/m² D1 ＋ carboplatin AUC 5 D1，q3w × 4 → pembrolizumab ＋ pemetrexed q3w 維持 | Folic acid、vitamin B12、dexamethasone（見下方說明）；CrCl ≥45 |
| Carboplatin ＋ paclitaxel ＋ pembrolizumab | Pembrolizumab 200 mg D1 ＋ paclitaxel 200 mg/m² D1 ＋ carboplatin AUC 6 D1，q3w × 4 → pembrolizumab 維持 | Paclitaxel 過敏預防；先給 paclitaxel 再給 carboplatin |
| Carboplatin ＋ nab-paclitaxel ＋ pembrolizumab | nab-Paclitaxel 100 mg/m² D1,8,15 ＋ carboplatin AUC 6 D1 ＋ pembrolizumab 200 mg D1，q3w × 4 | 不需過敏預防用藥 |
| Cisplatin ＋ pemetrexed（術後輔助，非鱗狀） | Cisplatin 75 mg/m² D1 ＋ pemetrexed 500 mg/m² D1，q3w × 4 | Cisplatin 水化與高致吐性止吐 |
| Cisplatin ＋ vinorelbine（術後輔助） | Cisplatin 75–80 mg/m² D1 ＋ vinorelbine 25–30 mg/m² D1,8，q3w × 4 | Vinorelbine 為起泡劑（vesicant），注意外滲 |
| Cisplatin ＋ gemcitabine（鱗狀） | Cisplatin 75 mg/m² D1 ＋ gemcitabine 1,250 mg/m² D1,8，q3w | |
| Docetaxel ± ramucirumab（二線） | Ramucirumab 10 mg/kg D1 ＋ docetaxel 75 mg/m² D1，q3w | Docetaxel 前 dexamethasone 8 mg BID × 3 天（從前一天開始），預防體液滯留與過敏 |
| Durvalumab 鞏固（PACIFIC） | 10 mg/kg q2w 或 1,500 mg q4w，共 12 個月 | 每次前看甲狀腺、肝腎功能 |
| Atezolizumab | 1,200 mg q3w（或 840 mg q2w、1,680 mg q4w） | |
| Nivolumab | 240 mg q2w 或 480 mg q4w；術前 360 mg q3w × 3 合併化療 | |

**Pemetrexed 前置用藥（考試必考）**

- **Folic acid** 350–1,000 µg PO QD：第一劑前 7 天內至少吃 5 天，持續到最後一劑後 21 天。
- **Vitamin B12** 1,000 µg IM：第一劑前 1 週，之後每 9 週（約每 3 週期）一次。
- **Dexamethasone** 4 mg PO BID：給藥前一天、當天、後一天，預防皮疹。
- **NSAIDs**：CrCl 45–79 mL/min 時，短效 NSAID（如 ibuprofen）在給藥前後各 2 天避免使用；長效 NSAID 前 5 天到後 2 天避免。

> [!TIP]
> **為什麼要補葉酸和 B12**
> Pemetrexed 是抗葉酸代謝藥，會同時卡住正常細胞的葉酸路徑。先把葉酸和 B12「存糧」補足，正常骨髓和黏膜比較撐得住，腫瘤細胞仍會被打到。早期試驗沒有補充時，嚴重骨髓抑制與治療相關死亡明顯較多。

**Paclitaxel 過敏預防（常見組合）**

- Dexamethasone 20 mg PO（給藥前 12 小時與 6 小時）或 IV（給藥前 30–60 分鐘）。
- Diphenhydramine 50 mg IV、H2 阻斷劑（如 famotidine 20 mg IV），給藥前 30–60 分鐘。
- 使用非 PVC 輸液套與 0.22 µm in-line filter。

### 5.2 同步化放療（CCRT）處方

| 處方 | 劑量 |
|------|------|
| Cisplatin ＋ etoposide | Cisplatin 50 mg/m² D1,8,29,36 ＋ etoposide 50 mg/m² D1–5、D29–33 |
| Carboplatin ＋ paclitaxel（每週） | Carboplatin AUC 2 ＋ paclitaxel 45–50 mg/m²，放療期間每週 |
| Cisplatin ＋ pemetrexed（非鱗狀） | Cisplatin 75 mg/m² ＋ pemetrexed 500 mg/m²，q3w × 3 |

### 5.3 SCLC 處方

| 處方 | 劑量與週期 |
|------|-----------|
| Cisplatin ＋ etoposide（LS，合併放療） | Cisplatin 75 mg/m² D1 ＋ etoposide 100 mg/m² D1–3，q3w × 4 |
| Carboplatin ＋ etoposide ＋ atezolizumab（ES） | Carboplatin AUC 5 D1 ＋ etoposide 100 mg/m² D1–3 ＋ atezolizumab 1,200 mg D1，q3w × 4 → atezolizumab 1,200 mg q3w |
| Carboplatin ＋ etoposide ＋ durvalumab（ES） | 同上化療 ＋ durvalumab 1,500 mg D1，q3w × 4 → durvalumab 1,500 mg q4w |
| Durvalumab 鞏固（LS，ADRIATIC） | 1,500 mg q4w，最多 24 個月 |
| Lurbinectedin | 3.2 mg/m² q3w |
| Topotecan | 1.5 mg/m² IV D1–5，q3w |
| Tarlatamab | 第 1 天 1 mg、第 8 天 10 mg、第 15 天 10 mg，之後 10 mg q2w；前兩劑需監測 CRS／ICANS（監測時間依仿單與院內規範） |

### 5.4 口服標靶藥

| 藥物 | 劑量 | 與食物 | 減量／注意 |
|------|------|-------|-----------|
| Osimertinib | 80 mg QD | 不限 | 減為 40 mg；QTc、ILD、心衰竭 |
| Gefitinib | 250 mg QD | 不限 | 避免 PPI |
| Erlotinib | 150 mg QD | 空腹（飯前 1 小時或飯後 2 小時） | 吸菸降低血中濃度；避免 PPI |
| Afatinib | 40 mg QD | 空腹（美國仿單：飯前 1 小時或飯後 2 小時；歐盟仿單為飯後 3 小時，依台灣仿單） | 減為 30、20 mg；腹瀉、甲溝炎常見 |
| Dacomitinib | 45 mg QD | 不限 | 減為 30、15 mg |
| Alectinib | 600 mg BID | 隨餐 | 肌肉痛／CK 上升、心搏過緩、膽紅素上升 |
| Brigatinib | 90 mg QD × 7 天 → 180 mg QD | 不限 | 前 7 天低劑量導入，預防早發性肺部事件 |
| Lorlatinib | 100 mg QD | 不限 | 高膽固醇／三酸甘油酯、情緒與認知變化 |
| Crizotinib | 250 mg BID | 不限 | 視覺異常、水腫、心搏過緩 |
| Entrectinib | 600 mg QD | 不限 | 頭暈、味覺改變、體重增加 |
| Capmatinib | 400 mg BID | 不限 | 周邊水腫、光敏感 |
| Tepotinib | 450 mg QD | 隨餐 | 周邊水腫 |
| Selpercatinib | 160 mg BID（≥50 kg）；120 mg BID（<50 kg） | 不限 | 高血壓、肝功能異常、QTc |
| Dabrafenib ＋ trametinib | 150 mg BID ＋ 2 mg QD | 空腹 | 發燒症候群 |
| Sotorasib | 960 mg QD | 不限 | 腹瀉、肝功能異常 |
| Larotrectinib | 100 mg BID | 不限 | 頭暈、肝功能異常 |

> [!WARNING]
> **口服標靶藥的交互作用**
> - **Gefitinib、erlotinib 的吸收需要胃酸**：避免 PPI；必須用 H2 阻斷劑時，erlotinib 在 H2 阻斷劑後 10 小時、下一劑前 2 小時服用。
> - 多數 TKI 經 **CYP3A4** 代謝：避免葡萄柚、St. John's wort，以及強效 CYP3A4 抑制劑或誘導劑（如 rifampin、azole 類抗黴菌藥、carbamazepine）。
> - 開立任何新藥（包括抗生素、抗黴菌藥）前，先查交互作用。

---

## 6. 副作用評估與處置

通用原則：用 CTCAE 分級 → 依級數決定**繼續、暫停、減量或永久停藥**。化療的骨髓抑制、噁心嘔吐、外滲處置見 [支持性照護](00-shared/03-supportive-care.md)；免疫治療見 [irAE 章](00-shared/04-irae.md)。

### 6.1 EGFR TKI

| 副作用 | 處置重點 |
|-------|---------|
| 痤瘡樣皮疹（acneiform rash） | G1：外用低效類固醇（hydrocortisone 2.5%）或 clindamycin 1%。G2：加口服 doxycycline 100 mg BID 或 minocycline 100 mg BID。G3：暫停至 ≤G2 後減量再用。預防：保濕、防曬，afatinib／dacomitinib 可預防性口服 doxycycline |
| 甲溝炎（paronychia） | 稀釋白醋泡手腳、外用類固醇或抗生素；肉芽組織可用硝酸銀；避免剪太短、穿太緊的鞋 |
| 腹瀉 | Loperamide 首劑 4 mg，之後每次稀便 2 mg，每日最多 16 mg；補充水分電解質；G3 暫停（afatinib 最常見） |
| 口腔炎 | 溫和漱口水、避免刺激食物；G3 暫停 |
| 間質性肺病（ILD） | AURA3 中 osimertinib 的 ILD 類事件約 4%。新發或惡化的咳嗽、喘、發燒：**立即暫停**、安排胸部 CT、排除感染；確診 ILD 通常永久停藥，給予類固醇 |
| QTc 延長（osimertinib） | AURA3 中約 4%。開始前與定期做心電圖；QTc >500 ms 暫停，恢復後減量；同時矯正 K、Mg |
| 左心室射出率下降（osimertinib） | 有心臟病史者開始前做心臟超音波 |

> [!IMPORTANT]
> **皮疹不是壞事**
> EGFR TKI 的皮疹和療效有相關性，臨床上常有病人想自行停藥。衛教重點是「預防 ＋ 早期處理」，不是停藥。真正要立刻停藥、立刻回診的是**新的喘或咳嗽**（可能是 ILD）。

### 6.2 ALK／ROS1 TKI

| 藥物 | 特殊副作用 | 處置 |
|------|-----------|------|
| Alectinib | 肌肉痛與 CK 上升、心搏過緩、膽紅素上升、水腫、光敏感、體重增加 | 定期驗 CK、肝功能；心跳 <50 且有症狀暫停 |
| Brigatinib | 早發性肺部事件（多在開始後 7 天內）、高血壓、CK／lipase 上升 | 90 mg 導入 7 天；開始第一週注意呼吸症狀 |
| Lorlatinib | **高三酸甘油酯與高膽固醇**（CROWN 5 年：3–4 級分別 25% 與 21%）、中樞神經副作用 42%（情緒、認知、說話、幻覺，多為 1–2 級）、體重增加、高血壓、房室傳導阻滯 | 開始前與定期驗血脂，常需 statin；與家屬一起衛教情緒變化 |
| Crizotinib | 視覺異常（閃光、殘影）、水腫、肝功能上升、心搏過緩 | 開車注意；定期肝功能 |
| Entrectinib | 頭暈、味覺改變、體重增加、認知變化 | |

### 6.3 其他標靶藥

| 藥物 | 特殊副作用 | 處置 |
|------|-----------|------|
| Capmatinib、tepotinib（MET） | 周邊水腫（tepotinib 長期追蹤 67%、capmatinib 47%）、低白蛋白、肌酸酐上升；capmatinib 罕見致命性肺炎 | 水腫用壓力襪、抬高；利尿劑效果有限，嚴重時減量 |
| Selpercatinib（RET） | 肝功能異常、高血壓、QTc 延長；**東亞病人較常見**（LIBRETTO-431：3 級以上 ALT 上升 22%、高血壓 20%） | 先控制血壓再開始；前 3 個月每 2 週驗肝功能（依仿單） |
| Dabrafenib ＋ trametinib（BRAF） | **發燒（約 56%）**、皮膚、射出率下降、視網膜病變 | 發燒 ≥38°C 暫停兩藥，退燒後再用；定期心臟超音波 |
| Trastuzumab deruxtecan（HER2） | **ILD／肺炎**（5.4 mg/kg 組 12.9%）、骨髓抑制、噁心 | 任何疑似 ILD 暫停；確診 G2 以上永久停藥 |
| Datopotamab deruxtecan | 口腔炎（約 56%）、ILD（約 7–9%） | 每日口腔照護、預防性漱口；ILD 處置同上 |
| Zongertinib（HER2） | 腹瀉、肝功能異常；試驗中未見藥物相關 ILD | |

### 6.4 Amivantamab（± lazertinib）

| 副作用 | 處置 |
|-------|------|
| 輸注反應（infusion-related reaction, IRR） | MARIPOSA 中 63%，多發生在**第一劑**：第一劑拆成兩天給（D1、D2）；給藥前 antihistamine、antipyretic、glucocorticoid；發生時暫停、處理症狀、降速再給。**皮下劑型**的全身性給藥反應約 13%，明顯低於靜脈劑型約 66%（PALOMA-3，美國 FDA 核准資料），台灣 2026 年已有藥證 |
| 皮膚與指甲毒性 | 皮疹 86%。用 **COCOON 預防方案**：第 1–12 週口服 doxycycline 或 minocycline 100 mg BID；第 13–52 週頭皮每日外用 clindamycin 1%；手腳指甲每日用 chlorhexidine 4%；臉與身體每日擦含 ceramide 的保濕劑。2 級以上皮膚副作用從 75% 降到 42%（Cho et al., 2025） |
| 靜脈血栓（合併 lazertinib） | 發生率 36%，中位發生時間約 84 天：**前 4 個月預防性抗凝血**（DOAC 或低分子量肝素）；腳腫、胸痛、喘要立即評估 |
| 低白蛋白、水腫、ILD | 定期驗白蛋白；ILD 約 3%，處置同上 |

### 6.5 化療

| 藥物 | 特殊副作用 | 預防與處置 |
|------|-----------|-----------|
| Cisplatin | 腎毒性、低血鎂、耳毒性、周邊神經病變、**高致吐性（含延遲性嘔吐）** | 充足水化與補鎂；監測尿量與肌酸酐；聽力異常要回報；四藥止吐 |
| Carboplatin | 血小板低下為主；多次使用後過敏（常在第 6–8 次以上） | 每次給藥前看血小板；第一次過敏後評估減敏或換藥 |
| Pemetrexed | 骨髓抑制、皮疹、口腔炎、肌酸酐上升 | 前置用藥（5.1）；CrCl <45 不給 |
| Paclitaxel | 過敏反應、周邊神經病變、掉髮、肌肉關節痛 | 前置用藥；神經病變 G2 以上考慮減量 |
| nab-Paclitaxel | 骨髓抑制、周邊神經病變 | |
| Docetaxel | 嗜中性球低下性發燒、體液滯留、指甲變化、流淚 | 前置 dexamethasone；高風險者考慮 G-CSF |
| Gemcitabine | 骨髓抑制、類流感症狀、肺毒性、罕見溶血性尿毒症候群 | |
| Etoposide | 骨髓抑制、快速輸注時低血壓、掉髮 | 輸注時間不少於 30–60 分鐘 |
| Vinorelbine | 起泡劑、便秘、神經病變 | 確認回血再給；外滲處置見共用章 |

### 6.6 免疫治療：肺癌要特別注意的點

- **免疫相關肺炎（pneumonitis）** 在肺癌比其他癌別常見；症狀和原本的肺癌、COPD、感染重疊，判讀要小心。
- **免疫治療後接 osimertinib**：3 個月內接上時，3–4 級 irAE 約四分之一（Schoenfeld et al., 2019）。開立前確認最後一劑免疫治療的日期，並與主治醫師討論。
- 處置流程見 [irAE 章](00-shared/04-irae.md)。

### 6.7 放射治療相關

| 副作用 | 時間 | 處置 |
|-------|------|------|
| 放射性食道炎 | 放療第 2–3 週開始 | 黏膜保護劑、止痛（含 viscous lidocaine）、PPI、營養諮詢；吞嚥痛嚴重時評估管灌 |
| 放射性肺炎 | 放療後 1–6 個月 | 排除感染；有症狀者 prednisone 約 1 mg/kg/day，慢慢減量（數週） |

---

## 7. 專師實務

### 7.1 每次化療前檢核

| 項目 | 標準（常見門檻，依院內規範） |
|------|--------------------------|
| ECOG | 0–2；變差要回報主治醫師 |
| 體重 | 與上次比較；體重變化大時重算 BSA |
| CBC | ANC ≥1,500/µL、PLT ≥100,000/µL |
| 腎功能 | Cisplatin：CrCl 常要求 ≥60 mL/min；pemetrexed：CrCl ≥45 mL/min |
| 肝功能 | AST/ALT、bilirubin 在可接受範圍 |
| 電解質 | Na、K、Mg、Ca（cisplatin 後低鎂常見；SCLC 注意低血鈉） |
| 免疫治療 | TSH、free T4（約每 6 週）、血糖、皮質醇（有症狀時） |
| B 型肝炎 | 第一次化療前驗 HBsAg、anti-HBc；HBsAg 陽性要會診並預防性抗病毒（見 [化療基礎](00-shared/01-chemo-basics.md)） |
| 前置用藥 | Pemetrexed：確認葉酸與 B12；paclitaxel：確認 dexamethasone 已服用 |

### 7.2 Order set 範例一：非鱗狀 NSCLC，C1 carboplatin ＋ pemetrexed ＋ pembrolizumab

情境：62 歲男性，第 IV 期肺腺癌，EGFR、ALK、ROS1 等 driver 皆陰性，PD-L1 TPS 30%，ECOG 1。身高 170 cm、體重 65 kg（BSA 1.75 m²），血清肌酸酐 1.0 mg/dL。

**劑量計算**

- CrCl（Cockcroft-Gault）=（140 − 62）× 65 ÷（72 × 1.0）≈ 70 mL/min
- Carboplatin = AUC 5 ×（70 ＋ 25）= **475 mg**
- Pemetrexed = 500 mg/m² × 1.75 = **875 mg**
- Pembrolizumab = **200 mg**（固定劑量）

**醫囑範例**

```text
Day -7 起   Folic acid 400 mcg PO QD（持續至最後一劑後 21 天）
Day -7      Vitamin B12 1,000 mcg IM ST（之後每 9 週）
Day -1~+1   Dexamethasone 4 mg PO BID

Day 1
  Pre-chemo lab：CBC/DC、BUN/Cr、AST/ALT、bilirubin、Na/K/Mg、TSH/free T4、glucose
  止吐：Fosaprepitant 150 mg IV ＋ palonosetron 0.25 mg IV，化療前 30 分鐘
        （當天已口服 dexamethasone 4 mg BID，額外劑量依院內止吐規範）
  1. Pembrolizumab 200 mg in NS 100 mL IV drip over 30 min
  2. Pemetrexed 875 mg in NS 100 mL IV drip over 10 min
  3. Carboplatin 475 mg in D5W 250 mL IV drip over 30-60 min
  延遲性噁心：視需要 olanzapine 或 metoclopramide

衛教：發燒 ≥38°C、喘、腹瀉、皮疹立即回診
下次回診：Day 21 抽血評估 C2
```

> [!NOTE]
> **院內規範要確認的地方**
> 輸注溶液與時間、免疫治療與化療的給藥順序、止吐藥組合、dexamethasone 是否與止吐用 dexamethasone 合併計算，各院 protocol 不同。上面是格式示範，實際以單位 protocol 為準。

### 7.3 Order set 範例二：LS-SCLC，cisplatin ＋ etoposide 合併放療

```text
Pre-chemo lab：CBC/DC、BUN/Cr、Na/K/Mg/Ca、AST/ALT
體重、尿量紀錄；I/O 每 8 小時

Day 1
  前水化：NS 1,000 mL ＋ KCl 10 mEq ＋ MgSO4 1-2 g IV over 1-2 hr
  止吐（高致吐性）：NK1 拮抗劑 ＋ 5-HT3 拮抗劑 ＋ dexamethasone ＋ olanzapine
  1. Cisplatin 75 mg/m² in NS 500 mL IV over 1-2 hr
  2. Etoposide 100 mg/m² in NS 500 mL IV over ≥60 min
  後水化：NS 1,000 mL IV；目標尿量 ≥100 mL/hr
Day 2-3
  Etoposide 100 mg/m² IV over ≥60 min
  Dexamethasone（延遲性嘔吐預防，依止吐規範）
監測：Na（SCLC 合併 SIADH 風險）、Mg、Cr
```

### 7.4 Order set 範例三：門診開始 osimertinib

- **開始前**：心電圖（QTc）、有心臟病史者做心臟超音波、CBC、肝腎功能、電解質（K、Mg）。
- **處方**：Osimertinib 80 mg PO QD。
- **衛教**：皮膚保濕防曬、指甲照護、腹瀉處理、**新的喘或咳嗽立即回診**、交互作用（避免自行服用中草藥與 St. John's wort）。
- **追蹤**：開始後 2–4 週回診看副作用；影像評估約每 2–3 個月。

### 7.5 SOAP 範例

**情境：** 58 歲女性，第 IV 期肺腺癌（EGFR exon 19 deletion），osimertinib 第 8 週，門診主訴右腳大拇趾紅腫痛。

```text
S：右腳大拇趾甲周紅腫疼痛 1 週，穿鞋會痛，無發燒。
   無新的咳嗽或喘。食慾可，排便每日 2 次軟便。
O：BT 36.8°C，SpO2 98%。右腳大拇趾甲周紅腫，有少量肉芽組織，無化膿。
   臉部及前胸散在丘疹膿疱，約占體表 8%，無症狀。
   Lab：CBC、肝腎功能正常。
A：1. Osimertinib 相關甲溝炎，CTCAE G2（影響工具性日常活動）
   2. 痤瘡樣皮疹 G1
   3. 第 IV 期肺腺癌，EGFR ex19del，osimertinib 第 8 週，臨床上無惡化跡象
P：1. 繼續 osimertinib 80 mg QD（G2 甲溝炎不需停藥）
   2. 稀釋白醋泡腳每日 2 次；外用類固醇 ＋ 抗生素軟膏；
      doxycycline 100 mg PO BID × 2 週
   3. 臉部皮疹：外用 clindamycin 1% gel、保濕、防曬
   4. 衛教：鞋子要寬、不要剪甲溝；如出現喘、咳嗽、發燒立即回診
   5. 2 週後回診評估；若惡化至 G3，與主治醫師討論暫停或減量
```

### 7.6 療效評估與追蹤

- **RECIST 1.1**：
  - CR：所有目標病灶消失。
  - PR：目標病灶直徑總和減少 ≥30%。
  - PD：直徑總和比最小值增加 ≥20% 且絕對值增加 ≥5 mm，或出現新病灶。
  - SD：介於 PR 與 PD 之間。
- **免疫治療的假性惡化（pseudoprogression）**：少數病人影像先變大後縮小，臨床穩定時可依 iRECIST 在 4–8 週後再確認。
- **晚期病人**：治療中每 2–3 個週期（約 6–9 週）做影像評估。
- **根治性治療後**：前 2–3 年每 6 個月做胸部 CT，之後每年追蹤（NCCN）。

---

## 8. 腫瘤急症（肺癌相關）

通用的嗜中性球低下性發燒、腫瘤溶解症候群、脊髓壓迫、高血鈣等，見 [腫瘤急症章](00-shared/02-oncologic-emergencies.md)。以下是肺癌特別常見的。

| 急症 | 為什麼肺癌常見 | 辨識 | 立即處置 |
|------|-------------|------|---------|
| 上腔靜脈症候群（SVC syndrome） | 右上葉腫瘤、SCLC、縱膈腔淋巴結 | 臉頸腫、上肢水腫、胸壁靜脈曲張、平躺喘 | 抬高床頭、給氧；嚴重症狀（喉頭水腫、意識改變）考慮支架；儘快取得組織，SCLC 對化療反應快 |
| 大咳血 | 中央型鱗狀細胞癌、腫瘤侵犯血管 | 大量咳血（常見定義 24 小時 >100–600 mL） | **出血側朝下側躺**、保護呼吸道、準備插管；tranexamic acid；支氣管鏡、支氣管動脈栓塞 |
| SIADH 低血鈉 | SCLC（副腫瘤症候群） | 意識混亂、抽搐；等容性低血鈉、尿滲透壓高 | 限水、鹽錠、必要時 tolvaptan；**矯正速度每 24 小時不超過 8–10 mEq/L**；治療 SCLC 本身 |
| 高血鈣 | 鱗狀細胞癌分泌 PTHrP、骨轉移 | 倦怠、便秘、意識改變、多尿 | 水化、zoledronic acid 或 denosumab |
| 腦轉移／顱內壓上升 | NSCLC 診斷時腦轉移常見，ALK、EGFR 更高 | 頭痛、嘔吐、局部神經症狀、癲癇 | Dexamethasone（常用 4–16 mg/day）；放射腫瘤科會診（SRS 或全腦放療）；中樞穿透好的 TKI |
| 惡性肋膜積水 | 肋膜轉移（M1a） | 喘、單側呼吸音減弱 | 胸腔穿刺；反覆積水考慮肋膜沾黏術或留置導管 |
| 心包膜填塞 | 心包膜轉移 | 低血壓、頸靜脈怒張、心音遙遠、奇脈 | 緊急心臟超音波與心包膜穿刺 |

其他 SCLC 副腫瘤症候群：**Lambert-Eaton 肌無力症候群**（抗 VGCC 抗體，近端肌無力、活動後改善）、**異位性 ACTH**（低血鉀、高血糖、水腫）。

> [!WARNING]
> **Bevacizumab 的禁忌**
> 鱗狀細胞癌、近期咳血、腫瘤侵犯大血管或有空洞的病人，使用 bevacizumab 可能發生致命性大咳血。這是 bevacizumab 只用於非鱗狀 NSCLC 的原因，也是常考題。

---

## 9. 健保給付與事前審查

<!-- status: pending -->

> [!CAUTION]
> **等待第 9 節原文**
> 本段要依《全民健康保險藥品給付規定》第 9 節「抗癌瘤藥物」原文逐條整理（含條號與修訂日期）。原文提供後，下表會補上每個藥物的給付條件、事前審查、療程與停用條件。2026 年給付規定已多次修訂，新聞稿內容不可直接當作給付條件。

**整理架構（待補）**

| 藥品 | 條號 | 給付適應症與條件 | 事前審查 | 療程／續用評估 | 停用條件 |
|------|------|----------------|---------|--------------|---------|
| Osimertinib | 待原文 | | | | |
| Gefitinib／erlotinib／afatinib | 待原文 | | | | |
| Alectinib／brigatinib／lorlatinib | 待原文 | | | | |
| Crizotinib／entrectinib | 待原文 | | | | |
| Pembrolizumab／atezolizumab／nivolumab／durvalumab | 待原文 | | | | |
| Bevacizumab／ramucirumab | 待原文 | | | | |
| Amivantamab | 待原文 | | | | |
| Pemetrexed、docetaxel 等化療 | 待原文 | | | | |
| 其他（dabrafenib ＋ trametinib、capmatinib、selpercatinib、sotorasib、lurbinectedin 等） | 待原文 | | | | |

**讀給付規定的五個欄位**：適應症限制（病理、biomarker、期別、線別）→ 事前審查（送審資料）→ 療程與續用評估（多久要再送審、要附什麼影像）→ 停用條件（疾病惡化的定義）→ 不可併用或轉換的限制。

---

## 10. 個案練習

### 個案一：EGFR 陽性合併腦轉移

58 歲女性，不吸菸。咳嗽 2 個月，CT 顯示右上葉 3.5 cm 腫塊、多處骨轉移；腦部 MRI 有 2 處 <1 cm 無症狀轉移。切片為腺癌，**EGFR exon 19 deletion**，PD-L1 TPS 60%。ECOG 1。

1. 第一線治療怎麼選？為什麼 PD-L1 60% 卻不先用 pembrolizumab？
2. 開始 osimertinib 前要做哪些檢查？
3. 骨轉移還需要什麼支持性處置？

<details>
<summary>參考答案</summary>

1. 有 EGFR 驅動突變，第一線用 EGFR TKI：osimertinib 單藥，或 osimertinib ＋ 化療（FLAURA2，腦轉移者 PFS 獲益更明顯），或 amivantamab ＋ lazertinib。EGFR 陽性者免疫單藥效果差，且先用免疫再接 osimertinib 會增加嚴重 irAE 風險，所以 PD-L1 高也不先用免疫。
2. 心電圖（QTc）、電解質（K、Mg）、CBC、肝腎功能；有心臟病史做心臟超音波。
3. Denosumab 或 zoledronic acid（預防骨骼相關事件），開始前牙科評估（顎骨壞死風險），補充鈣與維生素 D；疼痛控制；評估是否需要放療止痛或預防病理性骨折。

</details>

### 個案二：CCRT 後的喘

70 歲男性，吸菸 50 pack-years，鱗狀細胞癌 IIIB 期不可切除，PD-L1 10%。完成 CCRT 後開始 durvalumab。第 3 個月出現乾咳、活動喘，SpO2 93%（室內空氣），CT 見照野內與照野外毛玻璃病灶。

1. 鑑別診斷有哪些？
2. 專師該先做哪些處置？

<details>
<summary>參考答案</summary>

1. 放射性肺炎（時間符合，但照野外也有病灶）、免疫相關肺炎、感染（含 PJP、病毒）、腫瘤惡化、心衰竭或肺栓塞。
2. 暫停 durvalumab；抽血（CBC、CRP、procalcitonin 視院內）、痰液與病毒檢驗，必要時支氣管鏡；評估為 G2 免疫肺炎時，prednisone 1–2 mg/kg/day，症狀改善後慢慢減量至少 4–6 週；長期高劑量類固醇考慮 PJP 預防；48–72 小時沒改善要升級處置（見 irAE 章）。

</details>

### 個案三：SCLC 化療後發燒

66 歲男性，ES-SCLC，C1 carboplatin ＋ etoposide ＋ atezolizumab 後第 9 天，發燒 38.6°C，血壓 95/60 mmHg，ANC 200/µL，Na 124 mEq/L。

1. 這是什麼急症？第一個小時要完成什麼？
2. 低血鈉要怎麼想？

<details>
<summary>參考答案</summary>

1. 嗜中性球低下性發燒（febrile neutropenia），合併低血壓屬高風險。一小時內：血液培養兩套（含導管）、尿液與其他培養，**開始廣效抗生素**（如 cefepime 或 piperacillin/tazobactam，依院內抗生素指引），輸液復甦，評估敗血症；後續週期考慮 G-CSF 次級預防。
2. SCLC 常見 SIADH；也要排除脫水、嘔吐、藥物（如 cisplatin、cyclophosphamide 類藥物）造成的低血鈉。評估容積狀態、血清與尿液滲透壓、尿鈉；症狀嚴重時用高張食鹽水，矯正速度每 24 小時不超過 8–10 mEq/L。

</details>

---

## 11. 自我測驗

**Q1.** 下列哪一種 EGFR 變異對 gefitinib 與 osimertinib 反應最差？

A. Exon 19 deletion　B. L858R　C. Exon 20 insertion　D. G719X

<details>
<summary>答案與詳解</summary>

**答案：C**。Exon 20 insertion 改變藥物結合位置，對傳統 EGFR TKI 反應差，第一線用 amivantamab ＋ carboplatin ＋ pemetrexed（PAPILLON）。G719X 屬非典型突變，可用 afatinib 或 osimertinib。

</details>

**Q2.** 病人預計下週開始 pemetrexed，下列前置用藥何者正確？

A. 第一劑當天開始吃葉酸　B. Vitamin B12 第一劑前 1 週肌肉注射，之後每 9 週　C. 只有 CrCl <45 時才需要補充　D. Dexamethasone 是為了止吐

<details>
<summary>答案與詳解</summary>

**答案：B**。葉酸要在第一劑前 7 天內至少吃 5 天；B12 第一劑前 1 週打、之後每 9 週；dexamethasone 是預防皮疹。CrCl <45 是不給 pemetrexed。

</details>

**Q3.** 病人 GFR 計算為 140 mL/min，處方 carboplatin AUC 5，劑量應為？

A. 825 mg　B. 750 mg　C. 700 mg　D. 625 mg

<details>
<summary>答案與詳解</summary>

**答案：B**。GFR 上限 125 mL/min：5 ×（125 ＋ 25）= 750 mg。若直接用 140 計算會得到 825 mg，超量。

</details>

**Q4.** 依 TNM 第 9 版，腫瘤 2.5 cm，轉移到同側**單一站**縱膈腔淋巴結，N 分類為？

A. N1　B. N2a　C. N2b　D. N3

<details>
<summary>答案與詳解</summary>

**答案：B**。第 9 版將 N2 分成單站（N2a）與多站（N2b）。

</details>

**Q5.** 不可切除 III 期 NSCLC（EGFR、ALK 陰性）完成 CCRT 後未惡化，durvalumab 鞏固治療的建議療程是？

A. 3 個月　B. 6 個月　C. 12 個月　D. 直到疾病惡化

<details>
<summary>答案與詳解</summary>

**答案：C**。PACIFIC 試驗為 12 個月。EGFR 陽性者改用 osimertinib 直到疾病惡化（LAURA）。

</details>

**Q6.** 下列哪一種病人最不適合使用 bevacizumab？

A. 肺腺癌，ECOG 1　B. 鱗狀細胞癌合併近期咳血　C. 肺腺癌合併骨轉移　D. 肺腺癌，PD-L1 <1%

<details>
<summary>答案與詳解</summary>

**答案：B**。鱗狀組織型與咳血是致命性大咳血的危險因子。

</details>

**Q7.** SCLC 病人出現意識混亂，Na 121 mEq/L、等容積、尿滲透壓高。最可能的原因與矯正上限是？

A. 腎上腺功能不全；每 24 小時 20 mEq/L　B. SIADH；每 24 小時 8–10 mEq/L　C. 心衰竭；不限制　D. SIADH；每小時 5 mEq/L

<details>
<summary>答案與詳解</summary>

**答案：B**。SCLC 是 SIADH 最常見的腫瘤原因。矯正過快會造成滲透壓性脫髓鞘症候群（osmotic demyelination syndrome）。

</details>

**Q8.** 使用 lorlatinib 最需要定期追蹤的實驗室數值是？

A. 血脂　B. 血鉀　C. 尿酸　D. 澱粉酶

<details>
<summary>答案與詳解</summary>

**答案：A**。高三酸甘油酯與高膽固醇是 lorlatinib 最常見的副作用（CROWN 5 年 3–4 級分別 25% 與 21%），常需 statin。也要注意情緒與認知變化。

</details>

**Q9.** Brigatinib 前 7 天用 90 mg 再加量到 180 mg，目的是？

A. 減少腹瀉　B. 減少早發性肺部事件　C. 增加腦部濃度　D. 減少肝毒性

<details>
<summary>答案與詳解</summary>

**答案：B**。早發性肺部事件多在開始後 7 天內，低劑量導入可降低風險。

</details>

**Q10.** 病人 2 個月前停用 pembrolizumab，現在發現 EGFR L858R，準備開始 osimertinib。最需要注意的風險是？

A. 高血糖　B. 嚴重 irAE（含肺炎、肝炎）　C. 腫瘤溶解症候群　D. 出血

<details>
<summary>答案與詳解</summary>

**答案：B**。PD-(L)1 抑制劑後短期內接 osimertinib，嚴重 irAE 風險上升（Schoenfeld et al., 2019）。這也是基因報告出來前不先開免疫治療的原因。

</details>

**Q11.** EGFR exon 19 deletion、IIA 期術後的輔助標靶治療與療程是？

A. Gefitinib 2 年　B. Osimertinib 3 年　C. Alectinib 2 年　D. Osimertinib 1 年

<details>
<summary>答案與詳解</summary>

**答案：B**。ADAURA。Alectinib 2 年是 ALK 陽性的輔助治療（ALINA）。

</details>

**Q12.** Amivantamab 第一劑分兩天給，主要是為了降低？

A. 皮疹　B. 輸注反應　C. 靜脈血栓　D. 間質性肺病

<details>
<summary>答案與詳解</summary>

**答案：B**。輸注反應多發生在第一劑。合併 lazertinib 時另需預防性抗凝血降低靜脈血栓。

</details>

**Q13.** 服用 erlotinib 的病人因胃食道逆流想吃 PPI，最適當的建議是？

A. 可以，同時服用即可　B. 避免 PPI；必要時改 H2 阻斷劑並錯開服藥時間　C. 改用 antacid 與 erlotinib 一起吞　D. 停用 erlotinib

<details>
<summary>答案與詳解</summary>

**答案：B**。Erlotinib 吸收需要胃酸。必須用 H2 阻斷劑時，erlotinib 在 H2 阻斷劑後 10 小時、下一劑前 2 小時服用；antacid 要間隔數小時。

</details>

**Q14.** LS-SCLC 完成 cisplatin ＋ etoposide 同步放療後未惡化，下一步的實證治療是？

A. Atezolizumab 維持　B. Durvalumab 鞏固最多 24 個月　C. Osimertinib　D. 觀察即可，沒有鞏固治療

<details>
<summary>答案與詳解</summary>

**答案：B**。ADRIATIC：OS 55.9 對 33.4 個月。

</details>

**Q15.** 依 RECIST 1.1，目標病灶直徑總和從最小值 40 mm 增加到 47 mm，沒有新病灶，評估為？

A. PR　B. SD　C. PD　D. 無法評估

<details>
<summary>答案與詳解</summary>

**答案：B**。(47 − 40) ÷ 40 = 17.5%，未達 PD 要求的 20%（雖然絕對值增加 7 mm 已超過 5 mm，兩個條件要同時成立），所以是 SD。

</details>

**Q16.** 肺鱗狀細胞癌病人血鈣 13.2 mg/dL，最可能的機轉是？

A. 骨轉移造成的局部溶骨，與荷爾蒙無關　B. 腫瘤分泌 PTHrP　C. 維生素 D 中毒　D. 原發性副甲狀腺亢進

<details>
<summary>答案與詳解</summary>

**答案：B**。鱗狀細胞癌最常見的副腫瘤高血鈣機轉是 PTHrP（humoral hypercalcemia of malignancy）。

</details>

---

## 12. 參考文獻

APA 第 7 版。作者超過 20 位時列前 19 位、省略號與最後一位。每筆附 DOI 與 PMID，2026-10-29 於 PubMed 核對。

Ahn, M.-J., Lisberg, A., Goto, Y., Sands, J., Hong, M. H., Paz-Ares, L., Pons-Tostivint, E., Pérol, M., Felip, E., Sugawara, S., Hayashi, H., Cho, B. C., Blumenschein, G., Shum, E., Lee, J.-S., Heist, R. S., Cornelissen, R., Chang, W.-C., Kowalski, D., . . . Okamoto, I. (2025). A pooled analysis of datopotamab deruxtecan in patients with EGFR-mutated NSCLC. *Journal of Thoracic Oncology, 20*(11), 1669–1682. https://doi.org/10.1016/j.jtho.2025.06.002（PMID: 40516821）

Altorki, N., Wang, X., Kozono, D., Watt, C., Landrenau, R., Wigle, D., Port, J., Jones, D. R., Conti, M., Ashrafi, A. S., Liberman, M., Yasufuku, K., Yang, S., Mitchell, J. D., Pass, H., Keenan, R., Bauer, T., Miller, D., Kohman, L. J., . . . Vokes, E. (2023). Lobar or sublobar resection for peripheral stage IA non-small-cell lung cancer. *New England Journal of Medicine, 388*(6), 489–498. https://doi.org/10.1056/NEJMoa2212083（PMID: 36780674）

Antonia, S. J., Villegas, A., Daniel, D., Vicente, D., Murakami, S., Hui, R., Yokoi, T., Chiappori, A., Lee, K. H., de Wit, M., Cho, B. C., Bourhaba, M., Quantin, X., Tokito, T., Mekhail, T., Planchard, D., Kim, Y. C., Karapetis, C. S., Hiret, S., . . . Özgüroğlu, M. (2017). Durvalumab after chemoradiotherapy in stage III non-small-cell lung cancer. *New England Journal of Medicine, 377*(20), 1919–1929. https://doi.org/10.1056/NEJMoa1709937（PMID: 28885881）

Barlesi, F., Yao, W., Duruisseaux, M., Doucet, L., Martínez, A. A., Gregorc, V., Juan-Vidal, O., Lu, S., De Bondt, C., de Marinis, F., Linardou, H., Kim, Y.-C., Jotte, R., Felip, E., Lo Russo, G., Reck, M., Michenzie, M. F., Yang, W., Meade, J. N., . . . Mok, T. S. K. (2025). Adagrasib versus docetaxel in KRASG12C-mutated non-small-cell lung cancer (KRYSTAL-12): A randomised, open-label, phase 3 trial. *The Lancet, 406*(10503), 615–626. https://doi.org/10.1016/S0140-6736(25)00866-9（PMID: 40783289）

Camidge, D. R., Kim, H. R., Ahn, M.-J., Yang, J. C.-H., Han, J.-Y., Lee, J.-S., Hochmair, M. J., Li, J. Y.-C., Chang, G.-C., Lee, K. H., Gridelli, C., Delmonte, A., Garcia Campelo, R., Kim, D.-W., Bearz, A., Griesinger, F., Morabito, A., Felip, E., Califano, R., . . . Popat, S. (2018). Brigatinib versus crizotinib in ALK-positive non-small-cell lung cancer. *New England Journal of Medicine, 379*(21), 2027–2039. https://doi.org/10.1056/NEJMoa1810171（PMID: 30280657）

Cascone, T., Awad, M. M., Spicer, J. D., He, J., Lu, S., Sepesi, B., Tanaka, F., Taube, J. M., Cornelissen, R., Havel, L., Karaseva, N., Kuzdzal, J., Petruzelka, L. B., Wu, L., Pujol, J. L., Ito, H., Ciuleanu, T. E., de Oliveira Muniz Koch, L., Janssens, A., . . . Provencio Pulla, M. (2024). Perioperative nivolumab in resectable lung cancer. *New England Journal of Medicine, 390*(19), 1756–1769. https://doi.org/10.1056/NEJMoa2311926（PMID: 38749033）

Chang, G.-C., Chiu, C.-H., Yu, C.-J., Chang, Y.-C., Chang, Y.-H., Hsu, K.-H., Wu, Y.-C., Chen, C.-Y., Hsu, H.-H., Wu, M.-T., Yang, C.-T., Chong, I.-W., Lin, Y.-C., Hsia, T.-C., Lin, M.-C., Su, W.-C., Lin, C.-B., Lee, K.-Y., Wei, Y.-F., . . . Yang, P.-C. (2024). Low-dose CT screening among never-smokers with or without a family history of lung cancer in Taiwan: A prospective cohort study. *The Lancet Respiratory Medicine, 12*(2), 141–152. https://doi.org/10.1016/S2213-2600(23)00338-7（PMID: 38042167）

Cheng, Y., Spigel, D. R., Cho, B. C., Laktionov, K. K., Fang, J., Chen, Y., Zenke, Y., Lee, K. H., Wang, Q., Navarro, A., Bernabe, R., Buchmeier, E. L., Chang, J. W., Shiraishi, Y., Sezgin Goksu, S., Badzio, A., Shi, A., Daniel, D. B., Hoa, N. T. T., . . . Senan, S. (2024). Durvalumab after chemoradiotherapy in limited-stage small-cell lung cancer. *New England Journal of Medicine, 391*(14), 1313–1327. https://doi.org/10.1056/NEJMoa2404873（PMID: 39268857）

Cho, B. C., Li, W., Spira, A. I., Sauder, M., Feldman, J., Bozorgmehr, F., Mak, M., Smith, J., Voon, P. J., Liu, B., Tian, P., Tan, J.-L., Yang, C.-T., Shih, J.-Y., Karadurmus, N., Cundom, J. E., Bertollo, G., Cicin, I., Nieva, J., . . . Girard, N. (2025). Enhanced versus standard dermatologic management with amivantamab-lazertinib in EGFR-mutated advanced NSCLC: The COCOON global randomized controlled trial. *Journal of Thoracic Oncology, 20*(10), 1517–1530. https://doi.org/10.1016/j.jtho.2025.07.117（PMID: 40923969）

Cho, B. C., Lu, S., Felip, E., Spira, A. I., Girard, N., Lee, J.-S., Lee, S.-H., Ostapenko, Y., Danchaivijitr, P., Liu, B., Alip, A., Korbenfeld, E., Mourão Dias, J., Besse, B., Lee, K.-H., Xiong, H., How, S.-H., Cheng, Y., Chang, G.-C., . . . Hayashi, H. (2024). Amivantamab plus lazertinib in previously untreated EGFR-mutated advanced NSCLC. *New England Journal of Medicine, 391*(16), 1486–1498. https://doi.org/10.1056/NEJMoa2403614（PMID: 38924756）

de Koning, H. J., van der Aalst, C. M., de Jong, P. A., Scholten, E. T., Nackaerts, K., Heuvelmans, M. A., Lammers, J. J., Weenink, C., Yousaf-Khan, U., Horeweg, N., van 't Westeinde, S., Prokop, M., Mali, W. P., Mohamed Hoesein, F. A. A., van Ooijen, P. M. A., Aerts, J. G. J. V., den Bakker, M. A., Thunnissen, E., Verschakelen, J., . . . Oudkerk, M. (2020). Reduced lung-cancer mortality with volume CT screening in a randomized trial. *New England Journal of Medicine, 382*(6), 503–513. https://doi.org/10.1056/NEJMoa1911793（PMID: 31995683）

de Langen, A. J., Johnson, M. L., Mazieres, J., Dingemans, A.-M. C., Mountzios, G., Pless, M., Wolf, J., Schuler, M., Lena, H., Skoulidis, F., Yoneshima, Y., Kim, S.-W., Linardou, H., Novello, S., van der Wekken, A. J., Chen, Y., Peters, S., Felip, E., Solomon, B. J., . . . Paz-Ares, L. (2023). Sotorasib versus docetaxel for previously treated non-small-cell lung cancer with KRASG12C mutation: A randomised, open-label, phase 3 trial. *The Lancet, 401*(10378), 733–746. https://doi.org/10.1016/S0140-6736(23)00221-0（PMID: 36764316）

Drilon, A., Camidge, D. R., Lin, J. J., Kim, S.-W., Solomon, B. J., Dziadziuszko, R., Besse, B., Goto, K., de Langen, A. J., Wolf, J., Lee, K. H., Popat, S., Springfeld, C., Nagasaka, M., Felip, E., Yang, N., Velcheti, V., Lu, S., Kao, S., . . . Cho, B. C. (2024). Repotrectinib in ROS1 fusion-positive non-small-cell lung cancer. *New England Journal of Medicine, 390*(2), 118–131. https://doi.org/10.1056/NEJMoa2302299（PMID: 38197815）

Drilon, A., Laetsch, T. W., Kummar, S., DuBois, S. G., Lassen, U. N., Demetri, G. D., Nathenson, M., Doebele, R. C., Farago, A. F., Pappo, A. S., Turpin, B., Dowlati, A., Brose, M. S., Mascarenhas, L., Federman, N., Berlin, J., El-Deiry, W. S., Baik, C., Deeken, J., . . . Hyman, D. M. (2018). Efficacy of larotrectinib in TRK fusion-positive cancers in adults and children. *New England Journal of Medicine, 378*(8), 731–739. https://doi.org/10.1056/NEJMoa1714448（PMID: 29466156）

Faivre-Finn, C., Snee, M., Ashcroft, L., Appel, W., Barlesi, F., Bhatnagar, A., Bezjak, A., Cardenal, F., Fournel, P., Harden, S., Le Pechoux, C., McMenemin, R., Mohammed, N., O'Brien, M., Pantarotto, J., Surmont, V., Van Meerbeeck, J. P., Woll, P. J., Lorigan, P., & Blackhall, F. (2017). Concurrent once-daily versus twice-daily chemoradiotherapy in patients with limited-stage small-cell lung cancer (CONVERT): An open-label, phase 3, randomised, superiority trial. *The Lancet Oncology, 18*(8), 1116–1125. https://doi.org/10.1016/S1470-2045(17)30318-2（PMID: 28642008）

Felip, E., Altorki, N., Zhou, C., Csőszi, T., Vynnychenko, I., Goloborodko, O., Luft, A., Akopov, A., Martinez-Marti, A., Kenmotsu, H., Chen, Y. M., Chella, A., Sugawara, S., Voong, D., Wu, F., Yi, J., Deng, Y., McCleland, M., Bennett, E., . . . Wakelee, H. (2021). Adjuvant atezolizumab after adjuvant chemotherapy in resected stage IB-IIIA non-small-cell lung cancer (IMpower010): A randomised, multicentre, open-label, phase 3 trial. *The Lancet, 398*(10308), 1344–1357. https://doi.org/10.1016/S0140-6736(21)02098-5（PMID: 34555333）

Felip, E., Altorki, N., Zhou, C., Vallières, E., Csoszi, T., Vynnychenko, I. O., Goloborodko, O., Rittmeyer, A., Reck, M., Martinez-Marti, A., Kenmotsu, H., Chen, Y. M., Chella, A., Sugawara, S., Fu, C., Ballinger, M., Deng, Y., Srivastava, M. K., Bennett, E., . . . Wakelee, H. A. (2025). Five-year survival outcomes with atezolizumab after chemotherapy in resected stage IB-IIIA non-small cell lung cancer (IMpower010): An open-label, randomized, phase III trial. *Journal of Clinical Oncology, 43*(21), 2343–2349. https://doi.org/10.1200/JCO-24-01681（PMID: 40446184）

Forde, P. M., Spicer, J. D., Provencio, M., Mitsudomi, T., Awad, M. M., Wang, C., Lu, S., Felip, E., Swanson, S. J., Brahmer, J. R., Kerr, K., Taube, J. M., Ciuleanu, T. E., Tanaka, F., Saylors, G. B., Chen, K. N., Ito, H., Liberman, M., Martin, C., . . . Girard, N. (2025). Overall survival with neoadjuvant nivolumab plus chemotherapy in lung cancer. *New England Journal of Medicine, 393*(8), 741–752. https://doi.org/10.1056/NEJMoa2502931（PMID: 40454642）

Forde, P. M., Spicer, J., Lu, S., Provencio, M., Mitsudomi, T., Awad, M. M., Felip, E., Broderick, S. R., Brahmer, J. R., Swanson, S. J., Kerr, K., Wang, C., Ciuleanu, T. E., Saylors, G. B., Tanaka, F., Ito, H., Chen, K. N., Liberman, M., Vokes, E. E., . . . Girard, N. (2022). Neoadjuvant nivolumab plus chemotherapy in resectable lung cancer. *New England Journal of Medicine, 386*(21), 1973–1985. https://doi.org/10.1056/NEJMoa2202170（PMID: 35403841）

Gainor, J. F., Curigliano, G., Kim, D.-W., Lee, D. H., Besse, B., Baik, C. S., Doebele, R. C., Cassier, P. A., Lopes, G., Tan, D. S. W., Garralda, E., Paz-Ares, L. G., Cho, B. C., Gadgeel, S. M., Thomas, M., Liu, S. V., Taylor, M. H., Mansfield, A. S., Zhu, V. W., . . . Subbiah, V. (2021). Pralsetinib for RET fusion-positive non-small-cell lung cancer (ARROW): A multi-cohort, open-label, phase 1/2 study. *The Lancet Oncology, 22*(7), 959–969. https://doi.org/10.1016/S1470-2045(21)00247-3（PMID: 34118197）

Gandhi, L., Rodríguez-Abreu, D., Gadgeel, S., Esteban, E., Felip, E., De Angelis, F., Domine, M., Clingan, P., Hochmair, M. J., Powell, S. F., Cheng, S. Y., Bischoff, H. G., Peled, N., Grossi, F., Jennens, R. R., Reck, M., Hui, R., Garon, E. B., Boyer, M., . . . Garassino, M. C. (2018). Pembrolizumab plus chemotherapy in metastatic non-small-cell lung cancer. *New England Journal of Medicine, 378*(22), 2078–2092. https://doi.org/10.1056/NEJMoa1801005（PMID: 29658856）

Garassino, M. C., Gadgeel, S., Speranza, G., Felip, E., Esteban, E., Dómine, M., Hochmair, M. J., Powell, S. F., Bischoff, H. G., Peled, N., Grossi, F., Jennens, R. R., Reck, M., Hui, R., Garon, E. B., Kurata, T., Gray, J. E., Schwarzenberger, P., Jensen, E., . . . Rodríguez-Abreu, D. (2023). Pembrolizumab plus pemetrexed and platinum in nonsquamous non-small-cell lung cancer: 5-year outcomes from the phase 3 KEYNOTE-189 study. *Journal of Clinical Oncology, 41*(11), 1992–1998. https://doi.org/10.1200/JCO.22.01989（PMID: 36809080）

Garon, E. B., Ciuleanu, T. E., Arrieta, O., Prabhash, K., Syrigos, K. N., Goksel, T., Park, K., Gorbunova, V., Kowalyszyn, R. D., Pikiel, J., Czyzewicz, G., Orlov, S. V., Lewanski, C. R., Thomas, M., Bidoli, P., Dakhil, S., Gans, S., Kim, J. H., Grigorescu, A., . . . Pérol, M. (2014). Ramucirumab plus docetaxel versus placebo plus docetaxel for second-line treatment of stage IV non-small-cell lung cancer after disease progression on platinum-based therapy (REVEL): A multicentre, double-blind, randomised phase 3 trial. *The Lancet, 384*(9944), 665–673. https://doi.org/10.1016/S0140-6736(14)60845-X（PMID: 24933332）

Goto, K., Goto, Y., Kubo, T., Ninomiya, K., Kim, S.-W., Planchard, D., Ahn, M.-J., Smit, E. F., de Langen, A. J., Pérol, M., Pons-Tostivint, E., Novello, S., Hayashi, H., Shimizu, J., Kim, D.-W., Kuo, C.-H., Yang, J. C.-H., Pereira, K., Cheng, F.-C., . . . Jänne, P. A. (2023). Trastuzumab deruxtecan in patients with HER2-mutant metastatic non-small-cell lung cancer: Primary results from the randomized, phase II DESTINY-Lung02 trial. *Journal of Clinical Oncology, 41*(31), 4852–4863. https://doi.org/10.1200/JCO.23.01361（PMID: 37694347）

Hellmann, M. D., Paz-Ares, L., Bernabe Caro, R., Zurawski, B., Kim, S. W., Carcereny Costa, E., Park, K., Alexandru, A., Lupinacci, L., de la Mora Jimenez, E., Sakai, H., Albert, I., Vergnenegre, A., Peters, S., Syrigos, K., Barlesi, F., Reck, M., Borghaei, H., Brahmer, J. R., . . . Ramalingam, S. S. (2019). Nivolumab plus ipilimumab in advanced non-small-cell lung cancer. *New England Journal of Medicine, 381*(21), 2020–2031. https://doi.org/10.1056/NEJMoa1910231（PMID: 31562796）

Heymach, J. V., Harpole, D., Mitsudomi, T., Taube, J. M., Galffy, G., Hochmair, M., Winder, T., Zukov, R., Garbaos, G., Gao, S., Kuroda, H., Ostoros, G., Tran, T. V., You, J., Lee, K. Y., Antonuzzo, L., Papai-Szekely, Z., Akamatsu, H., Biswas, B., . . . Reck, M. (2023). Perioperative durvalumab for resectable non-small-cell lung cancer. *New England Journal of Medicine, 389*(18), 1672–1684. https://doi.org/10.1056/NEJMoa2304875（PMID: 37870974）

Heymach, J. V., He, J., Harpole, D., Mitsudomi, T., Taube, J. M., Gao, S., Urban, L., Kang, J. H., Orlandi, F. J., Rodriguez-Cid, J., Massuti, B., Mateos, L. L., Pasello, G., Chu, Q., Kolb-Sielecki, J., Nakata, M., Galffy, G., Hochmair, M., Winder, T., . . . Reck, M. (2026). Perioperative durvalumab for resectable non-small cell lung cancer: Updated outcomes from the phase III AEGEAN trial. *Journal of Clinical Oncology*. Advance online publication. https://doi.org/10.1200/JCO-25-02659（PMID: 42664473）

Heymach, J. V., Ruiter, G., Ahn, M.-J., Girard, N., Smit, E. F., Planchard, D., Wu, Y.-L., Cho, B. C., Yamamoto, N., Sabari, J. K., Zhao, Y., Tu, H.-Y., Yoh, K., Nadal, E., Sadrolhefazi, B., Rohrbacher, M., von Wangenheim, U., Eigenbrod-Giese, S., & Zugazagoitia, J. (2025). Zongertinib in previously treated HER2-mutant non-small-cell lung cancer. *New England Journal of Medicine, 392*(23), 2321–2333. https://doi.org/10.1056/NEJMoa2503704（PMID: 40293180）

Horn, L., Mansfield, A. S., Szczęsna, A., Havel, L., Krzakowski, M., Hochmair, M. J., Huemer, F., Losonczy, G., Johnson, M. L., Nishio, M., Reck, M., Mok, T., Lam, S., Shames, D. S., Liu, J., Ding, B., Lopez-Chavez, A., Kabbinavar, F., Lin, W., . . . Liu, S. V. (2018). First-line atezolizumab plus chemotherapy in extensive-stage small-cell lung cancer. *New England Journal of Medicine, 379*(23), 2220–2229. https://doi.org/10.1056/NEJMoa1809064（PMID: 30280641）

Hsu, K.-H., Ho, C.-C., Hsia, T.-C., Tseng, J.-S., Su, K.-Y., Wu, M.-F., Chiu, K.-L., Yang, T.-Y., Chen, K.-C., Ooi, H., Wu, T.-C., Chen, H.-J., Chen, H.-Y., Chang, C.-S., Hsu, C.-P., Hsia, J.-Y., Chuang, C.-Y., Lin, C.-H., Chen, J. J. W., . . . Chang, G.-C. (2015). Identification of five driver gene mutations in patients with treatment-naïve lung adenocarcinoma in Taiwan. *PLoS ONE, 10*(3), Article e0120852. https://doi.org/10.1371/journal.pone.0120852（PMID: 25789627）

Jänne, P. A., Planchard, D., Kobayashi, K., Yang, J. C.-H., Liu, Y., Valdiviezo, N., Kim, T. M., Jiang, L., Kagamu, H., Yanagitani, N., Wang, J., Biswas, B., Poltoratskiy, A., Neron, Y., Rojas, C., Koubkova, L., Escriu, C., Ezeife, D. A., Mann, H., . . . Lee, C. K. (2026). Survival with osimertinib plus chemotherapy in EGFR-mutated advanced NSCLC. *New England Journal of Medicine, 394*(1), 27–38. https://doi.org/10.1056/NEJMoa2510308（PMID: 41104938）

Johnson, M. L., Cho, B. C., Luft, A., Alatorre-Alexander, J., Geater, S. L., Laktionov, K., Kim, S. W., Ursol, G., Hussein, M., Lim, F. L., Yang, C. T., Araujo, L. H., Saito, H., Reinmuth, N., Shi, X., Poole, L., Peters, S., Garon, E. B., & Mok, T. (2023). Durvalumab with or without tremelimumab in combination with chemotherapy as first-line therapy for metastatic non-small-cell lung cancer: The phase III POSEIDON study. *Journal of Clinical Oncology, 41*(6), 1213–1227. https://doi.org/10.1200/JCO.22.00975（PMID: 36327426）

Lu, S., Kato, T., Dong, X., Ahn, M.-J., Quang, L.-V., Soparattanapaisarn, N., Inoue, T., Wang, C.-L., Huang, M., Yang, J. C.-H., Cobo, M., Özgüroğlu, M., Casarini, I., Khiem, D.-V., Sriuranpong, V., Cronemberger, E., Takahashi, T., Runglodvatana, Y., Chen, M., . . . Ramalingam, S. S. (2024). Osimertinib after chemoradiotherapy in stage III EGFR-mutated NSCLC. *New England Journal of Medicine, 391*(7), 585–597. https://doi.org/10.1056/NEJMoa2402614（PMID: 38828946）

Mok, T. S., Wu, Y.-L., Ahn, M.-J., Garassino, M. C., Kim, H. R., Ramalingam, S. S., Shepherd, F. A., He, Y., Akamatsu, H., Theelen, W. S. M. E., Lee, C. K., Sebastian, M., Templeton, A., Mann, H., Marotti, M., Ghiorghiu, S., & Papadimitrakopoulou, V. A. (2017). Osimertinib or platinum-pemetrexed in EGFR T790M-positive lung cancer. *New England Journal of Medicine, 376*(7), 629–640. https://doi.org/10.1056/NEJMoa1612674（PMID: 27959700）

Mok, T. S., Wu, Y.-L., Thongprasert, S., Yang, C.-H., Chu, D.-T., Saijo, N., Sunpaweravong, P., Han, B., Margono, B., Ichinose, Y., Nishiwaki, Y., Ohe, Y., Yang, J.-J., Chewaskulyong, B., Jiang, H., Duffield, E. L., Watkins, C. L., Armour, A. A., & Fukuoka, M. (2009). Gefitinib or carboplatin-paclitaxel in pulmonary adenocarcinoma. *New England Journal of Medicine, 361*(10), 947–957. https://doi.org/10.1056/NEJMoa0810699（PMID: 19692680）

Mok, T., Camidge, D. R., Gadgeel, S. M., Rosell, R., Dziadziuszko, R., Kim, D.-W., Pérol, M., Ou, S.-H. I., Ahn, J. S., Shaw, A. T., Bordogna, W., Smoljanović, V., Hilton, M., Ruf, T., Noé, J., & Peters, S. (2020). Updated overall survival and final progression-free survival data for patients with treatment-naive advanced ALK-positive non-small-cell lung cancer in the ALEX study. *Annals of Oncology, 31*(8), 1056–1064. https://doi.org/10.1016/j.annonc.2020.04.478（PMID: 32418886）

Mountzios, G., Sun, L., Cho, B. C., Demirci, U., Baka, S., Gümüş, M., Lugini, A., Zhu, B., Yu, Y., Korantzis, I., Han, J. Y., Ciuleanu, T. E., Ahn, M. J., Rocha, P., Mazières, J., Lau, S. C. M., Schuler, M., Blackhall, F., Yoshida, T., . . . Rudin, C. M. (2025). Tarlatamab in small-cell lung cancer after platinum-based chemotherapy. *New England Journal of Medicine, 393*(4), 349–361. https://doi.org/10.1056/NEJMoa2502099（PMID: 40454646）

National Comprehensive Cancer Network. (2026). *NCCN Clinical Practice Guidelines in Oncology: Non-small cell lung cancer* (Version 9.2026). https://www.nccn.org/guidelines/category_1

National Comprehensive Cancer Network. (2026). *NCCN Clinical Practice Guidelines in Oncology: Small cell lung cancer* (Version 1.2027). https://www.nccn.org/guidelines/category_1

National Lung Screening Trial Research Team, Aberle, D. R., Adams, A. M., Berg, C. D., Black, W. C., Clapp, J. D., Fagerstrom, R. M., Gareen, I. F., Gatsonis, C., Marcus, P. M., & Sicks, J. D. (2011). Reduced lung-cancer mortality with low-dose computed tomographic screening. *New England Journal of Medicine, 365*(5), 395–409. https://doi.org/10.1056/NEJMoa1102873（PMID: 21714641）

O'Brien, M., Paz-Ares, L., Marreaud, S., Dafni, U., Oselin, K., Havel, L., Esteban, E., Isla, D., Martinez-Marti, A., Faehling, M., Tsuboi, M., Lee, J. S., Nakagawa, K., Yang, J., Samkari, A., Keller, S. M., Mauer, M., Jha, N., Stahel, R., . . . Peters, S. (2022). Pembrolizumab versus placebo as adjuvant therapy for completely resected stage IB-IIIA non-small-cell lung cancer (PEARLS/KEYNOTE-091): An interim analysis of a randomised, triple-blind, phase 3 trial. *The Lancet Oncology, 23*(10), 1274–1286. https://doi.org/10.1016/S1470-2045(22)00518-6（PMID: 36108662）

Paik, P. K., Felip, E., Veillon, R., Sakai, H., Cortot, A. B., Garassino, M. C., Mazieres, J., Viteri, S., Senellart, H., Van Meerbeeck, J., Raskin, J., Reinmuth, N., Conte, P., Kowalski, D., Cho, B. C., Patel, J. D., Horn, L., Griesinger, F., Han, J.-Y., . . . Le, X. (2020). Tepotinib in non-small-cell lung cancer with MET exon 14 skipping mutations. *New England Journal of Medicine, 383*(10), 931–943. https://doi.org/10.1056/NEJMoa2004407（PMID: 32469185）

Passaro, A., Wang, J., Wang, Y., Lee, S.-H., Melosky, B., Shih, J.-Y., Wang, J., Azuma, K., Juan-Vidal, O., Cobo, M., Felip, E., Girard, N., Cortot, A. B., Califano, R., Cappuzzo, F., Owen, S., Popat, S., Tan, J.-L., Salinas, J., . . . Cho, B. C. (2024). Amivantamab plus chemotherapy with and without lazertinib in EGFR-mutant advanced NSCLC after disease progression on osimertinib: Primary results from the phase III MARIPOSA-2 study. *Annals of Oncology, 35*(1), 77–90. https://doi.org/10.1016/j.annonc.2023.10.117（PMID: 37879444）

Paz-Ares, L., Borghaei, H., Liu, S. V., Peters, S., Herbst, R. S., Stencel, K., Majem, M., Şendur, M. A. N., Czyżewicz, G., Caro, R. B., Lee, K. H., Johnson, M. L., Karadurmuş, N., Grohé, C., Baka, S., Csőszi, T., Ahn, J. S., Califano, R., Yang, T. Y., . . . Reck, M. (2025). Efficacy and safety of first-line maintenance therapy with lurbinectedin plus atezolizumab in extensive-stage small-cell lung cancer (IMforte): A randomised, multicentre, open-label, phase 3 trial. *The Lancet, 405*(10495), 2129–2143. https://doi.org/10.1016/S0140-6736(25)01011-6（PMID: 40473449）

Paz-Ares, L., Chen, Y., Reinmuth, N., Hotta, K., Trukhin, D., Statsenko, G., Hochmair, M. J., Özgüroğlu, M., Ji, J. H., Garassino, M. C., Voitko, O., Poltoratskiy, A., Musso, E., Havel, L., Bondarenko, I., Losonczy, G., Conev, N., Mann, H., Dalvi, T. B., . . . Goldman, J. W. (2022). Durvalumab, with or without tremelimumab, plus platinum-etoposide in first-line treatment of extensive-stage small-cell lung cancer: 3-year overall survival update from CASPIAN. *ESMO Open, 7*(2), 100408. https://doi.org/10.1016/j.esmoop.2022.100408（PMID: 35279527）

Paz-Ares, L., Ciuleanu, T. E., Cobo, M., Schenker, M., Zurawski, B., Menezes, J., Richardet, E., Bennouna, J., Felip, E., Juan-Vidal, O., Alexandru, A., Sakai, H., Lingua, A., Salman, P., Souquet, P. J., De Marchi, P., Martin, C., Pérol, M., Scherpereel, A., . . . Reck, M. (2021). First-line nivolumab plus ipilimumab combined with two cycles of chemotherapy in patients with non-small-cell lung cancer (CheckMate 9LA): An international, randomised, open-label, phase 3 trial. *The Lancet Oncology, 22*(2), 198–211. https://doi.org/10.1016/S1470-2045(20)30641-0（PMID: 33476593）

Paz-Ares, L., Dvorkin, M., Chen, Y., Reinmuth, N., Hotta, K., Trukhin, D., Statsenko, G., Hochmair, M. J., Özgüroğlu, M., Ji, J. H., Voitko, O., Poltoratskiy, A., Ponce, S., Verderame, F., Havel, L., Bondarenko, I., Kazarnowicz, A., Losonczy, G., Conev, N. V., . . . Goldman, J. W. (2019). Durvalumab plus platinum-etoposide versus platinum-etoposide in first-line treatment of extensive-stage small-cell lung cancer (CASPIAN): A randomised, controlled, open-label, phase 3 trial. *The Lancet, 394*(10212), 1929–1939. https://doi.org/10.1016/S0140-6736(19)32222-6（PMID: 31590988）

Paz-Ares, L., Luft, A., Vicente, D., Tafreshi, A., Gümüş, M., Mazières, J., Hermes, B., Çay Şenler, F., Csőszi, T., Fülöp, A., Rodríguez-Cid, J., Wilson, J., Sugawara, S., Kato, T., Lee, K. H., Cheng, Y., Novello, S., Halmos, B., Li, X., . . . Kowalski, D. M. (2018). Pembrolizumab plus chemotherapy for squamous non-small-cell lung cancer. *New England Journal of Medicine, 379*(21), 2040–2051. https://doi.org/10.1056/NEJMoa1810865（PMID: 30280635）

Pérol, M., Li, W., Pennell, N. A., Liu, G., Ohe, Y., De Braud, F., Nagasaka, M., Felip, E., Xiong, A., Zhang, Y., Fan, H., Wang, X., Li, S., Lai, R. K., Ran, F., Zhang, X., Chen, W., Bazhenova, L., & Zhou, C. (2025). Taletrectinib in ROS1+ non-small cell lung cancer: TRUST. *Journal of Clinical Oncology, 43*(16), 1920–1929. https://doi.org/10.1200/JCO-25-00275（PMID: 40179330）

Peters, S., Camidge, D. R., Shaw, A. T., Gadgeel, S., Ahn, J. S., Kim, D.-W., Ou, S.-H. I., Pérol, M., Dziadziuszko, R., Rosell, R., Zeaiter, A., Mitry, E., Golding, S., Balas, B., Noe, J., Morcos, P. N., & Mok, T. (2017). Alectinib versus crizotinib in untreated ALK-positive non-small-cell lung cancer. *New England Journal of Medicine, 377*(9), 829–838. https://doi.org/10.1056/NEJMoa1704795（PMID: 28586279）

Peters, S., Camidge, R., Dziadziuszko, R., Gadgeel, S., Shaw, A. T., Kim, D.-W., Pérol, M., Rosell, D. R., Cheema, P., Wan-Teck Lim, D., Lin, J. J., Pavlakis, N., Ahn, J. S., Zhang, L., Henschel, V., Higgerson, A. A., McNally, V., Rooney, I., Scalori, A., . . . Mok, T. (2026). Alectinib versus crizotinib in previously untreated ALK-positive advanced non-small cell lung cancer: Final overall survival analysis of the phase III ALEX study. *Annals of Oncology, 37*(1), 92–103. https://doi.org/10.1016/j.annonc.2025.09.018（PMID: 41110693）

Pignon, J. P., Tribodet, H., Scagliotti, G. V., Douillard, J. Y., Shepherd, F. A., Stephens, R. J., Dunant, A., Torri, V., Rosell, R., Seymour, L., Spiro, S. G., Rolland, E., Fossati, R., Aubert, D., Ding, K., Waller, D., & Le Chevalier, T. (2008). Lung adjuvant cisplatin evaluation: A pooled analysis by the LACE Collaborative Group. *Journal of Clinical Oncology, 26*(21), 3552–3559. https://doi.org/10.1200/JCO.2007.13.9030（PMID: 18506026）

Planchard, D., Jänne, P. A., Cheng, Y., Yang, J. C.-H., Yanagitani, N., Kim, S.-W., Sugawara, S., Yu, Y., Fan, Y., Geater, S. L., Laktionov, K., Lee, C. K., Valdiviezo, N., Ahmed, S., Maurel, J.-M., Andrasina, I., Goldman, J., Ghiorghiu, D., Rukazenkov, Y., . . . Kobayashi, K. (2023). Osimertinib with or without chemotherapy in EGFR-mutated advanced NSCLC. *New England Journal of Medicine, 389*(21), 1935–1948. https://doi.org/10.1056/NEJMoa2306434（PMID: 37937763）

Planchard, D., Smit, E. F., Groen, H. J. M., Mazieres, J., Besse, B., Helland, Å., Giannone, V., D'Amelio, A. M., Zhang, P., Mookerjee, B., & Johnson, B. E. (2017). Dabrafenib plus trametinib in patients with previously untreated BRAFV600E-mutant metastatic non-small-cell lung cancer: An open-label, phase 2 trial. *The Lancet Oncology, 18*(10), 1307–1316. https://doi.org/10.1016/S1470-2045(17)30679-4（PMID: 28919011）

Ramalingam, S. S., Vansteenkiste, J., Planchard, D., Cho, B. C., Gray, J. E., Ohe, Y., Zhou, C., Reungwetwattana, T., Cheng, Y., Chewaskulyong, B., Shah, R., Cobo, M., Lee, K. H., Cheema, P., Tiseo, M., John, T., Lin, M.-C., Imamura, F., Kurata, T., . . . Soria, J.-C. (2020). Overall survival with osimertinib in untreated, EGFR-mutated advanced NSCLC. *New England Journal of Medicine, 382*(1), 41–50. https://doi.org/10.1056/NEJMoa1913662（PMID: 31751012）

Rami-Porta, R., Nishimura, K. K., Giroux, D. J., Detterbeck, F., Cardillo, G., Edwards, J. G., Fong, K. M., Giuliani, M., Huang, J., Kernstine, K. H., Marom, E. M., Nicholson, A. G., Van Schil, P. E., Travis, W. D., Tsao, M. S., Watanabe, S.-I., Rusch, V. W., Asamura, H., & Members of the IASLC Staging and Prognostic Factors Committee. (2024). The International Association for the Study of Lung Cancer Lung Cancer Staging Project: Proposals for revision of the TNM stage groups in the forthcoming (ninth) edition of the TNM classification for lung cancer. *Journal of Thoracic Oncology, 19*(7), 1007–1027. https://doi.org/10.1016/j.jtho.2024.02.011（PMID: 38447919）

Reck, M., Rodríguez-Abreu, D., Robinson, A. G., Hui, R., Csőszi, T., Fülöp, A., Gottfried, M., Peled, N., Tafreshi, A., Cuffe, S., O'Brien, M., Rao, S., Hotta, K., Leal, T. A., Riess, J. W., Jensen, E., Zhao, B., Pietanza, M. C., & Brahmer, J. R. (2021). Five-year outcomes with pembrolizumab versus chemotherapy for metastatic non-small-cell lung cancer with PD-L1 tumor proportion score ≥ 50%. *Journal of Clinical Oncology, 39*(21), 2339–2349. https://doi.org/10.1200/JCO.21.00174（PMID: 33872070）

Reck, M., Rodríguez-Abreu, D., Robinson, A. G., Hui, R., Csőszi, T., Fülöp, A., Gottfried, M., Peled, N., Tafreshi, A., Cuffe, S., O'Brien, M., Rao, S., Hotta, K., Leiby, M. A., Lubiniecki, G. M., Shentu, Y., Rangwala, R., & Brahmer, J. R. (2016). Pembrolizumab versus chemotherapy for PD-L1-positive non-small-cell lung cancer. *New England Journal of Medicine, 375*(19), 1823–1833. https://doi.org/10.1056/NEJMoa1606774（PMID: 27718847）

Riely, G. J., Smit, E. F., Ahn, M.-J., Felip, E., Ramalingam, S. S., Tsao, A., Johnson, M., Gelsomino, F., Esper, R., Nadal, E., Offin, M., Provencio, M., Clarke, J., Hussain, M., Otterson, G. A., Dagogo-Jack, I., Goldman, J. W., Morgensztern, D., Alcasid, A., . . . Johnson, B. E. (2023). Phase II, open-label study of encorafenib plus binimetinib in patients with BRAFV600-mutant metastatic non-small-cell lung cancer. *Journal of Clinical Oncology, 41*(21), 3700–3711. https://doi.org/10.1200/JCO.23.00774（PMID: 37270692）

Saji, H., Okada, M., Tsuboi, M., Nakajima, R., Suzuki, K., Aokage, K., Aoki, T., Okami, J., Yoshino, I., Ito, H., Okumura, N., Yamaguchi, M., Ikeda, N., Wakabayashi, M., Nakamura, K., Fukuda, H., Nakamura, S., Mitsudomi, T., Watanabe, S. I., & Asamura, H. (2022). Segmentectomy versus lobectomy in small-sized peripheral non-small-cell lung cancer (JCOG0802/WJOG4607L): A multicentre, open-label, phase 3, randomised, controlled, non-inferiority trial. *The Lancet, 399*(10335), 1607–1617. https://doi.org/10.1016/S0140-6736(21)02333-3（PMID: 35461558）

Schoenfeld, A. J., Arbour, K. C., Rizvi, H., Iqbal, A. N., Gadgeel, S. M., Girshman, J., Kris, M. G., Riely, G. J., Yu, H. A., & Hellmann, M. D. (2019). Severe immune-related adverse events are common with sequential PD-(L)1 blockade and osimertinib. *Annals of Oncology, 30*(5), 839–844. https://doi.org/10.1093/annonc/mdz077（PMID: 30847464）

Shaw, A. T., Bauer, T. M., de Marinis, F., Felip, E., Goto, Y., Liu, G., Mazieres, J., Kim, D.-W., Mok, T., Polli, A., Thurm, H., Calella, A. M., Peltz, G., & Solomon, B. J. (2020). First-line lorlatinib or crizotinib in advanced ALK-positive lung cancer. *New England Journal of Medicine, 383*(21), 2018–2029. https://doi.org/10.1056/NEJMoa2027187（PMID: 33207094）

Shaw, A. T., Ou, S.-H. I., Bang, Y.-J., Camidge, D. R., Solomon, B. J., Salgia, R., Riely, G. J., Varella-Garcia, M., Shapiro, G. I., Costa, D. B., Doebele, R. C., Le, L. P., Zheng, Z., Tan, W., Stephenson, P., Shreeve, S. M., Tye, L. M., Christensen, J. G., Wilner, K. D., . . . Iafrate, A. J. (2014). Crizotinib in ROS1-rearranged non-small-cell lung cancer. *New England Journal of Medicine, 371*(21), 1963–1971. https://doi.org/10.1056/NEJMoa1406766（PMID: 25264305）

Shaw, A. T., Solomon, B. J., Felip, E., Bauer, T. M., Liu, G., Goto, Y., Wu, Y.-L., Soo, R. A., Mazieres, J., Kim, D.-W., Wang, I.-M., Paolini, J., Polli, A., Rifi, N., Toffalorio, F., & Mok, T. S. K. (2026). Lorlatinib versus crizotinib as first-line treatment for advanced ALK-positive non-small-cell lung cancer: 7-year update from the phase III CROWN study. *Annals of Oncology, 37*(9), 1242–1252. https://doi.org/10.1016/j.annonc.2026.05.692（PMID: 42217582）

Shi, Y., Au, J. S.-K., Thongprasert, S., Srinivasan, S., Tsai, C.-M., Khoa, M. T., Heeroma, K., Itoh, Y., Cornelio, G., & Yang, P.-C. (2014). A prospective, molecular epidemiology study of EGFR mutations in Asian patients with advanced non-small-cell lung cancer of adenocarcinoma histology (PIONEER). *Journal of Thoracic Oncology, 9*(2), 154–162. https://doi.org/10.1097/JTO.0000000000000033（PMID: 24419411）

Socinski, M. A., Jotte, R. M., Cappuzzo, F., Orlandi, F., Stroyakovskiy, D., Nogami, N., Rodríguez-Abreu, D., Moro-Sibilot, D., Thomas, C. A., Barlesi, F., Finley, G., Kelsch, C., Lee, A., Coleman, S., Deng, Y., Shen, Y., Kowanetz, M., Lopez-Chavez, A., Sandler, A., & Reck, M. (2018). Atezolizumab for first-line treatment of metastatic nonsquamous NSCLC. *New England Journal of Medicine, 378*(24), 2288–2301. https://doi.org/10.1056/NEJMoa1716948（PMID: 29863955）

Solomon, B. J., Liu, G., Felip, E., Mok, T. S. K., Soo, R. A., Mazieres, J., Shaw, A. T., de Marinis, F., Goto, Y., Wu, Y.-L., Kim, D.-W., Martini, J.-F., Messina, R., Paolini, J., Polli, A., Thomaidou, D., Toffalorio, F., & Bauer, T. M. (2024). Lorlatinib versus crizotinib in patients with advanced ALK-positive non-small cell lung cancer: 5-year outcomes from the phase III CROWN study. *Journal of Clinical Oncology, 42*(29), 3400–3409. https://doi.org/10.1200/JCO.24.00581（PMID: 38819031）

Solomon, B. J., Mok, T., Kim, D.-W., Wu, Y.-L., Nakagawa, K., Mekhail, T., Felip, E., Cappuzzo, F., Paolini, J., Usari, T., Iyer, S., Reisman, A., Wilner, K. D., Tursi, J., & Blackhall, F. (2014). First-line crizotinib versus chemotherapy in ALK-positive lung cancer. *New England Journal of Medicine, 371*(23), 2167–2177. https://doi.org/10.1056/NEJMoa1408440（PMID: 25470694）

Soria, J.-C., Ohe, Y., Vansteenkiste, J., Reungwetwattana, T., Chewaskulyong, B., Lee, K. H., Dechaphunkul, A., Imamura, F., Nogami, N., Kurata, T., Okamoto, I., Zhou, C., Cho, B. C., Cheng, Y., Cho, E. K., Voon, P. J., Planchard, D., Su, W.-C., Gray, J. E., . . . Ramalingam, S. S. (2018). Osimertinib in untreated EGFR-mutated advanced non-small-cell lung cancer. *New England Journal of Medicine, 378*(2), 113–125. https://doi.org/10.1056/NEJMoa1713137（PMID: 29151359）

Spicer, J. D., Garassino, M. C., Wakelee, H., Liberman, M., Kato, T., Tsuboi, M., Lee, S. H., Chen, K. N., Dooms, C., Majem, M., Eigendorff, E., Martinengo, G. L., Bylicki, O., Rodríguez-Abreu, D., Chaft, J. E., Novello, S., Yang, J., Arunachalam, A., Keller, S. M., . . . Gao, S. (2024). Neoadjuvant pembrolizumab plus chemotherapy followed by adjuvant pembrolizumab compared with neoadjuvant chemotherapy alone in patients with early-stage non-small-cell lung cancer (KEYNOTE-671): A randomised, double-blind, placebo-controlled, phase 3 trial. *The Lancet, 404*(10459), 1240–1252. https://doi.org/10.1016/S0140-6736(24)01756-2（PMID: 39288781）

Spigel, D. R., Faivre-Finn, C., Gray, J. E., Vicente, D., Planchard, D., Paz-Ares, L., Vansteenkiste, J. F., Garassino, M. C., Hui, R., Quantin, X., Rimner, A., Wu, Y. L., Özgüroğlu, M., Lee, K. H., Kato, T., de Wit, M., Kurata, T., Reck, M., Cho, B. C., . . . Antonia, S. J. (2022). Five-year survival outcomes from the PACIFIC trial: Durvalumab after chemoradiotherapy in stage III non-small-cell lung cancer. *Journal of Clinical Oncology, 40*(12), 1301–1311. https://doi.org/10.1200/JCO.21.01308（PMID: 35108059）

Takahashi, T., Yamanaka, T., Seto, T., Harada, H., Nokihara, H., Saka, H., Nishio, M., Kaneda, H., Takayama, K., Ishimoto, O., Takeda, K., Yoshioka, H., Tachihara, M., Sakai, H., Goto, K., & Yamamoto, N. (2017). Prophylactic cranial irradiation versus observation in patients with extensive-disease small-cell lung cancer: A multicentre, randomised, open-label, phase 3 trial. *The Lancet Oncology, 18*(5), 663–671. https://doi.org/10.1016/S1470-2045(17)30230-9（PMID: 28343976）

Trigo, J., Subbiah, V., Besse, B., Moreno, V., López, R., Sala, M. A., Peters, S., Ponce, S., Fernández, C., Alfaro, V., Gómez, J., Kahatt, C., Zeaiter, A., Zaman, K., Boni, V., Arrondeau, J., Martínez, M., Delord, J. P., Awada, A., . . . Paz-Ares, L. (2020). Lurbinectedin as second-line treatment for patients with small-cell lung cancer: A single-arm, open-label, phase 2 basket trial. *The Lancet Oncology, 21*(5), 645–654. https://doi.org/10.1016/S1470-2045(20)30068-1（PMID: 32224306）

Tsuboi, M., Herbst, R. S., John, T., Kato, T., Majem, M., Grohé, C., Wang, J., Goldman, J. W., Lu, S., Su, W.-C., de Marinis, F., Shepherd, F. A., Lee, K. H., Le, N. T., Dechaphunkul, A., Kowalski, D., Poole, L., Bolanos, A., Rukazenkov, Y., & Wu, Y.-L. (2023). Overall survival with osimertinib in resected EGFR-mutated NSCLC. *New England Journal of Medicine, 389*(2), 137–147. https://doi.org/10.1056/NEJMoa2304594（PMID: 37272535）

Turrisi, A. T., Kim, K., Blum, R., Sause, W. T., Livingston, R. B., Komaki, R., Wagner, H., Aisner, S., & Johnson, D. H. (1999). Twice-daily compared with once-daily thoracic radiotherapy in limited small-cell lung cancer treated concurrently with cisplatin and etoposide. *New England Journal of Medicine, 340*(4), 265–271. https://doi.org/10.1056/NEJM199901283400403（PMID: 9920950）

Wakelee, H., Liberman, M., Kato, T., Tsuboi, M., Lee, S. H., Gao, S., Chen, K. N., Dooms, C., Majem, M., Eigendorff, E., Martinengo, G. L., Bylicki, O., Rodríguez-Abreu, D., Chaft, J. E., Novello, S., Yang, J., Keller, S. M., Samkari, A., & Spicer, J. D. (2023). Perioperative pembrolizumab for early-stage non-small-cell lung cancer. *New England Journal of Medicine, 389*(6), 491–503. https://doi.org/10.1056/NEJMoa2302983（PMID: 37272513）

Wolf, J., Seto, T., Han, J.-Y., Reguart, N., Garon, E. B., Groen, H. J. M., Tan, D. S. W., Hida, T., de Jonge, M., Orlov, S. V., Smit, E. F., Souquet, P.-J., Vansteenkiste, J., Hochmair, M., Felip, E., Nishio, M., Thomas, M., Ohashi, K., Toyozawa, R., . . . Heist, R. S. (2020). Capmatinib in MET exon 14-mutated or MET-amplified non-small-cell lung cancer. *New England Journal of Medicine, 383*(10), 944–957. https://doi.org/10.1056/NEJMoa2002787（PMID: 32877583）

Wu, Y.-L., Dziadziuszko, R., Ahn, J. S., Barlesi, F., Nishio, M., Lee, D. H., Lee, J.-S., Zhong, W., Horinouchi, H., Mao, W., Hochmair, M., de Marinis, F., Migliorino, M. R., Bondarenko, I., Lu, S., Wang, Q., Ochi Lohmann, T., Xu, T., Cardona, A., . . . Solomon, B. J. (2024). Alectinib in resected ALK-positive non-small-cell lung cancer. *New England Journal of Medicine, 390*(14), 1265–1276. https://doi.org/10.1056/NEJMoa2310532（PMID: 38598794）

Wu, Y.-L., Tsuboi, M., He, J., John, T., Grohe, C., Majem, M., Goldman, J. W., Laktionov, K., Kim, S.-W., Kato, T., Vu, H.-V., Lu, S., Lee, K.-Y., Akewanlop, C., Yu, C.-J., de Marinis, F., Bonanno, L., Domine, M., Shepherd, F. A., . . . Herbst, R. S. (2020). Osimertinib in resected EGFR-mutated non-small-cell lung cancer. *New England Journal of Medicine, 383*(18), 1711–1723. https://doi.org/10.1056/NEJMoa2027071（PMID: 32955177）

Yang, J. C.-H., Lu, S., Hayashi, H., Felip, E., Spira, A. I., Girard, N., Kim, Y. J., Lee, S.-H., Ostapenko, Y., Danchaivijitr, P., Liu, B., Alip, A., Korbenfeld, E., Mourão Dias, J., Besse, B., Passaro, A., Lee, K.-H., Xiong, H., How, S.-H., . . . Cho, B. C. (2025). Overall survival with amivantamab-lazertinib in EGFR-mutated advanced NSCLC. *New England Journal of Medicine, 393*(17), 1681–1693. https://doi.org/10.1056/NEJMoa2503001（PMID: 40923797）

Zhou, C., Greillier, L., Liu, G., John, T., Xing, L., Kowalski, D., Memmott, R. M., Yazici, O., Sun, M., Shu, C. A., Pons-Tostivint, E., Fan, Y., Fernandez-Hinojal, G., Shum, E., Wang, M., Bertolini, F., Camidge, D. R., Zhou, C., Doucet, L., . . . Heymach, J. V. (2026). First-line sunvozertinib in NSCLC with EGFR exon 20 insertion mutations. *New England Journal of Medicine, 395*(8), 765–775. https://doi.org/10.1056/NEJMoa2604461（PMID: 42212913）

Zhou, C., Solomon, B., Loong, H. H., Park, K., Pérol, M., Arriola, E., Novello, S., Han, B., Zhou, J., Ardizzoni, A., Mak, M. P., Santini, F. C., Elamin, Y. Y., Drilon, A., Wolf, J., Payakachat, N., Uh, M. K., Rajakumar, D., Han, H., . . . Goto, K. (2023). First-line selpercatinib or chemotherapy and pembrolizumab in RET fusion-positive NSCLC. *New England Journal of Medicine, 389*(20), 1839–1850. https://doi.org/10.1056/NEJMoa2309457（PMID: 37870973）

Zhou, C., Tang, K.-J., Cho, B. C., Liu, B., Paz-Ares, L., Cheng, S., Kitazono, S., Thiagarajan, M., Goldman, J. W., Sabari, J. K., Sanborn, R. E., Mansfield, A. S., Hung, J.-Y., Boyer, M., Popat, S., Mourão Dias, J., Felip, E., Majem, M., Gumus, M., . . . Girard, N. (2023). Amivantamab plus chemotherapy in NSCLC with EGFR exon 20 insertions. *New England Journal of Medicine, 389*(22), 2039–2051. https://doi.org/10.1056/NEJMoa2306441（PMID: 37870976）

癌症登記中心. (2025). *112年癌症登記長表年報*. https://twcr.tw/wp-content/uploads/2025/12/CA17_LF112.pdf

衛生福利部. (2025, December 30). *公布112年國人癌症登記資料分析結果 守護健康未來 從癌症篩檢開始* [新聞稿]. https://mohw.gov.tw/cp-2704-84987-1.html

衛生福利部. (2025, January 10). *114年擴大肺癌篩檢服務 新年從健康開始* [新聞稿]. https://mohw.gov.tw/cp-16-81184-1.html

衛生福利部. (2026, June 22). *國人死亡人數連續3年下降 十大死因中6項死因人數、死亡率都減少* [新聞稿]. https://mohw.gov.tw/cp-16-86970-1.html
