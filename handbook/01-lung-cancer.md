# 肺癌（Lung Cancer）

| 項目 | 本章依據 |
|------|---------|
| 治療指引 | NCCN Guidelines：Non-Small Cell Lung Cancer **Version 9.2026**（National Comprehensive Cancer Network, 2026a）、Small Cell Lung Cancer **Version 1.2027**（National Comprehensive Cancer Network, 2026b）（2026-10-29 查詢）；ESMO metastatic NSCLC living guidelines |
| 分期 | AJCC／IASLC 第 9 版，2025 年 1 月 1 日起診斷者適用 |
| 副作用分級 | NCI CTCAE v5.0（本手冊一律用 v5.0 分級，因為指引與藥品仿單的處置門檻都以 v5.0 撰寫；NCI 已於 2025-07-22 發布 v6.0，NCI 贊助的進行中試驗仍用 v5.0；理由與差異見[化療基礎](00-shared/01-chemo-basics.md#8-ctcae-分級原則)第 8 節） |
| 健保給付 | 藥品給付規定 115/10/22 版（全民健康保險藥品給付規定第 9 節「抗癌瘤藥物」），見 [第 9 段](#9-健保給付與事前審查) |
| 最後更新 | 2026-11-01 |

**這一章的結論先講：** 肺癌治療的第一個岔路是組織型（NSCLC 或 SCLC），第二個岔路是 **biomarker**。晚期非鱗狀 NSCLC 在拿到 EGFR、ALK 等基因結果之前，不要急著開免疫治療；有驅動基因（driver mutation）的病人用標靶藥，沒有的才看 PD-L1 決定免疫治療怎麼用。

---

## 0. 速查卡

| 主題 | 一句話重點 |
|------|-----------|
| 分型 | 國際文獻 NSCLC 約 85%、SCLC 約 15%；**台灣 SCLC 只占約 6%**，非小細胞癌中腺癌占 83% |
| 台灣特色 | 2023 年新診斷人數、2025 年死亡人數都是癌症第 1 名；非吸菸女性肺腺癌多，**EGFR 突變占台灣肺腺癌 55.7%** |
| 晚期非鱗狀 NSCLC 必驗 | EGFR、ALK、ROS1、BRAF V600E、KRAS G12C、MET exon 14 skipping、RET、NTRK1–3、HER2（ERBB2）突變、NRG1 fusion（建議 RNA-based NGS），加上 PD-L1（22C3, TPS） |
| 早期（I–II） | 手術為主；≤2 cm 周邊型且淋巴結陰性（N0）可做 segmentectomy；不能開刀用 SBRT |
| 術後輔助 | 依 biomarker：EGFR 用 osimertinib 3 年、ALK 用 alectinib 2 年、其餘用化療 ± 免疫治療 |
| 不可切除 III 期 | 同步化放療（CCRT）→ durvalumab 鞏固 12 個月；EGFR ex19del／L858R 且同步或序列性化放療後未惡化者，改用 osimertinib（LAURA；健保 9.80 無此給付文字） |
| 晚期（IV） | 有 driver：對應標靶藥；無 driver：PD-L1 ≥50% 可單用 pembrolizumab，否則化療 ＋ 免疫 |
| SCLC 局限期 | Cisplatin ＋ etoposide ＋ 同步胸部放療 → durvalumab 鞏固（ADRIATIC） |
| SCLC 廣泛期 | Carboplatin ＋ etoposide ＋ atezolizumab 或 durvalumab，接著免疫維持 |
| 健保第一線（115/10/22 版） | **EGFR**：第一線 TKI 有六種（gefitinib、erlotinib、afatinib、dacomitinib、osimertinib、aumolertinib）；各條寫「擇一、除耐受性不良不得互換」，但 gefitinib、erlotinib、afatinib 彼此之間原文只寫「不得併用」（細節見 9.1）；osimertinib 與 aumolertinib 需事前審查（每 3 個月），前四種條文不需事審；osimertinib、aumolertinib、dacomitinib 只給付 ex19del／L858R。**ALK／ROS-1**：ALK 第一線五選一，ALK 與 ROS-1 TKI 都需事審（每 3 個月）；crizotinib 的 ALK 適應症限 113/9/1 前已核准者續用。**免疫治療（9.69）**：一律事審（每次 12 週，最長 2 年）；單用需 PD-L1 TPS≧50%（atezolizumab：TC≧50% 或 IC≧10%），化療併用多數免附 PD-L1 報告。Lazertinib、sotorasib、tarlatamab 等**原文未見**。細節見[第 9 段](#9-健保給付與事前審查) |

> [!IMPORTANT]
> **必背數字**
> - Carboplatin 劑量 = 目標 AUC ×（GFR ＋ 25），GFR 上限 125 mL/min → AUC 5 最多 750 mg、AUC 6 最多 900 mg。
> - Pemetrexed 要 CrCl ≥45 mL/min，給藥前 7 天開始吃 folic acid，第一劑前 1 週打 vitamin B12（之後每 9 週）。
> - Osimertinib 80 mg QD；brigatinib 先 90 mg QD × 7 天再加到 180 mg QD。
> - Bevacizumab 不用在鱗狀細胞癌（大咳血風險）。
> - Tarlatamab：C1D1 1 mg → C1D8 10 mg → C1D15 10 mg → 之後 10 mg q2w；前兩劑輸注前 1 小時內 dexamethasone 8 mg IV、輸注後 NS 1 L，自輸注開始監測 6–8 小時（美國 2026-09 版仿單；Amgen, 2026；見 7.7）。
> - Bevacizumab／ramucirumab：蛋白尿 ≥2 g/24 小時暫停；擇期手術前至少 28 天停藥；近期咳血（≥1/2 茶匙）暫停 bevacizumab（見 6.8）。
> - 術前評估：ppoFEV1 與 ppoDLCO 都 >60% 為低風險；介於 60% 與 30% 之間先做爬樓梯（>22 m）或 shuttle walk（>400 m）；<30% 做 CPET（Brunelli et al., 2013；見 3.4）。

---

## 1. 流行病學與危險因子

### 1.1 台灣現況

| 指標 | 數字 | 資料來源與年份 |
|------|------|--------------|
| 新診斷人數 | **19,986 人，所有癌症第 1 名**（連續 3 年） | 衛福部 2023 年癌症登記（2025-12-30 公布；衛生福利部, 2025a） |
| 年齡標準化發生率 | 每 10 萬人 44.9 人；診斷中位年齡 66 歲 | 同上 |
| 死亡人數 | **10,831 人，癌症死因第 1 名**（男女皆第 1），占癌症死亡 19.75% | 衛福部 2025 年死因統計（2026-06-22 公布；衛生福利部, 2026b） |
| 組織型 | 非小細胞癌中**腺癌占 82.85%**（女性 92.99%、男性 71.73%），鱗狀細胞癌 10.06%；SCLC 約占全部肺癌 5.7% | 2023 年癌登長表（癌症登記中心, 2025） |
| 診斷時期別 | 非小細胞癌 IV 期 38.79%（男 45.96%、女 32.65%）、I 期 40.21%；SCLC IV 期 74.57% | 2023 年癌登長表（AJCC 第 8 版） |

長表資料只涵蓋長表申報醫院、且包含原位癌，所以總數和官方發生人數不同。

> [!IMPORTANT]
> **台灣肺癌和西方不一樣的地方**
> 台灣肺癌以**腺癌**為主，女性病人超過九成是腺癌、且多數不吸菸；SCLC 比例（約 6%）明顯低於西方常引用的 15%。腺癌病人多，所以標靶藥用得多；而肺腺癌本身 EGFR 突變率高，主要和東亞族裔、不吸菸、女性有關（PIONEER：亞洲晚期肺腺癌 51.4%，不吸菸者 60.7%；Shi et al., 2014）。

### 1.2 危險因子

| 類別 | 危險因子 | 臨床意義 |
|------|---------|---------|
| 吸菸 | 主動吸菸（看 pack-years）、二手菸 | SCLC 與鱗狀細胞癌幾乎都和吸菸有關；戒菸後風險逐年下降：重度吸菸者戒菸 5 年內肺癌風險就比持續吸菸者低約 39%，但即使戒菸 25 年仍是從未吸菸者的 3 倍以上（Tindle et al., 2018）；確診後的戒菸見 7.9 |
| 環境 | 廚房油煙、空氣污染（PM2.5）、氡氣、石綿 | 台灣非吸菸女性肺腺癌的可能相關因子 |
| 個人病史 | COPD、肺纖維化、結核病史、胸部放療史 | 慢性發炎與疤痕組織 |
| 家族史 | 一等親罹患肺癌 | 台灣 LDCT 篩檢的收案條件之一 |

### 1.3 篩檢：低劑量電腦斷層（LDCT）

- **NLST**（National Lung Screening Trial Research Team, 2011）：高風險吸菸者用 LDCT 篩檢，比胸部 X 光降低肺癌死亡率 20%。
- **NELSON**（de Koning et al., 2020）：男性高風險族群 10 年追蹤，肺癌死亡率下降約 24%。

**台灣肺癌早期偵測計畫**（國民健康署，2022 年 7 月 1 日開辦，2025 年 1 月 1 日放寬；衛生福利部, 2025b）

| 族群 | 條件 | 頻率 |
|------|------|------|
| 肺癌家族史 | 父母、子女或兄弟姊妹（有血緣）曾罹患肺癌；**男性 45–74 歲、女性 40–74 歲** | 每 2 年 1 次免費 LDCT |
| 重度吸菸者 | **50–74 歲**、吸菸史 **≥20 包年**（2025 年起由 30 包年下修），仍在吸菸或戒菸未滿 15 年 | 每 2 年 1 次免費 LDCT |

- 包年（pack-years）= 每天幾包 × 抽幾年。例如每天 1 包抽 20 年，或每天半包抽 40 年，都是 20 包年。
- 吸菸者篩檢時要同時轉介戒菸服務；確診肺癌之後仍要戒菸，見 7.9。
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
| 小細胞癌（small cell lung cancer, SCLC） | 國際約 15%；台灣約 6% | 中央 | synaptophysin、chromogranin、INSM1、CD56(+)；Ki-67 很高；多數 TTF-1(+) |

> [!TIP]
> **TTF-1 和 p40 怎麼記**
> 把 TTF-1 想成「腺體的身分證」，p40 想成「鱗狀上皮的身分證」。病理報告寫 TTF-1(+)、p40(−) 就往腺癌走；反過來就往 SCC 走。小活檢分不出來時，報告會寫 NSCLC-NOS，這時仍應送 biomarker。

### 2.2 必驗 biomarker

| 基因變異 | 東亞肺腺癌約略比例 | 代表藥物 | 備註 |
|---------|-----------------|---------|------|
| EGFR exon 19 del／L858R | 任何 EGFR 突變：亞洲 51.4%（PIONEER）、台灣 55.7%；其中 exon 19 del＋L858R 約占 EGFR 突變九成（台灣研究 44.8%＋47.9%），即約占全部肺腺癌一半 | osimertinib 等 EGFR TKI | 非吸菸、女性、腺癌較常見 |
| EGFR 非典型突變（G719X、L861Q、S768I） | 少見 | afatinib、osimertinib | |
| EGFR exon 20 insertion | 少見 | amivantamab ＋ 化療 | 對傳統 EGFR TKI 反應差 |
| ALK 融合 | 台灣約 4%（EGFR 陰性者中 9.8%） | alectinib、brigatinib、lorlatinib | 年輕、非吸菸；腦轉移常見 |
| ROS1 融合 | 1–2% | entrectinib、crizotinib、repotrectinib | |
| KRAS 突變（含 G12C） | 台灣約 5%，遠低於西方 | sotorasib、adagrasib（G12C，二線） | 多見於吸菸者 |
| BRAF 突變 | 台灣約 0.7% | dabrafenib ＋ trametinib（V600E） | |
| MET exon 14 skipping | 約 2–3% | capmatinib、tepotinib | 高齡者較多 |
| RET 融合 | 1–2% | selpercatinib、pralsetinib | |
| HER2（ERBB2）突變 | 台灣約 2% | trastuzumab deruxtecan（二線）；HER2 TKI zongertinib、sevabertinib（美國 FDA 2026 年已加速核准一線；台灣僅 sevabertinib 核准用於曾接受治療者，zongertinib 未上市） | |
| NTRK1–3 融合 | <1% | larotrectinib、entrectinib | 跨癌別適應症 |

台灣數字來自 1,772 位未治療肺腺癌的多中心研究（Hsu et al., 2015），ALK 只在 EGFR 陰性者檢測；亞洲數字來自 PIONEER（Shi et al., 2014）。沒有標台灣的列為國際文獻的約略值，依族群與檢測方法而異。

**PD-L1（22C3 抗體）TPS 分層：** <1%、1–49%、≥50%。PD-L1 決定的是「沒有 driver 時」免疫治療怎麼用，**不能**取代基因檢測。

> [!WARNING]
> **為什麼要等 biomarker 才開免疫治療**
> EGFR、ALK 陽性的病人對免疫單藥效果差；如果先打 PD-1/PD-L1 抑制劑、之後再接 osimertinib，15% 發生 3–4 級 irAE，**3 個月內接上的更高達 24%**，中位發生時間是開始 osimertinib 後 20 天，幾乎都要住院用類固醇。反過來（先 osimertinib 再免疫）或免疫後改用其他 EGFR TKI，則沒有觀察到嚴重 irAE（Schoenfeld et al., 2019）。臨床上寧可多等一兩週基因報告，或先用 plasma ctDNA 送驗加快速度。

### 2.3 檢測方法

| 方法 | 優點 | 限制 |
|------|------|------|
| 組織 NGS（next-generation sequencing） | 一次驗多個基因；RNA-based NGS 偵測融合基因較完整 | 需要足夠組織、等待時間較長；DNA-based NGS 可能漏掉部分融合基因與 MET exon 14 skipping，DNA 驗不到 driver 時應加做 RNA NGS |
| 血液 ctDNA（liquid biopsy） | 快、免侵入；可找抗藥機轉（如 T790M） | 陰性不能排除，需再驗組織 |
| 單基因 PCR（如 EGFR） | 快、便宜 | 驗不到其他基因，容易耗盡組織 |
| IHC／FISH（ALK、ROS1） | 普及 | ROS1 IHC 陽性需確認 |

> [!CAUTION]
> **待核對：健保 NGS 給付**
> 健保自 2024 年起給付部分癌別的 NGS 檢測（屬醫療服務給付項目，不在藥品給付規定第 9 節）。給付癌別、檢測時機與次數限制，請以健保署公告原文為準，本段待核對後補上。

---

## 3. 診斷與分期

### 3.0 臨床表現與身體評估

**這一段的結論先講：** 肺癌早期常沒有症狀；病人出現症狀時通常同時有呼吸道與全身性症狀，而且從症狀出現到確診常有時間延遲（Spiro et al., 2007）。專師的工作是把「症狀或徵象」對到「腫瘤侵犯的解剖位置」或「副腫瘤症候群」，在入院評估時就抓出需要加快分期或馬上處置的訊號。

**依解剖位置對照症狀與徵象**

| 位置 | 症狀與徵象 | 為什麼會這樣 | 接下來 |
|------|-----------|-------------|--------|
| 支氣管／肺實質 | 咳嗽、咳血、喘、局部喘鳴、同一肺葉反覆肺炎 | 腫瘤阻塞或侵蝕氣道，阻塞後遠端肺葉感染 | 見 7.8；影像與支氣管鏡 |
| 肋膜 | 吸氣時胸痛、喘；患側呼吸音減弱、叩診濁音 | 肋膜轉移或惡性積水（M1a，見 3.2） | 見 8.1 與[腫瘤急症章](00-shared/02-oncologic-emergencies.md#12-惡性肋膜積水)第 12 節 |
| 肺尖（上溝腫瘤，Pancoast 症候群；Arcasoy & Jett, 1997） | 肩膀和上臂痛、手內側麻木無力；**同側 Horner 徵象**（上眼瞼下垂 ptosis、瞳孔縮小 miosis、無汗 anhidrosis） | 腫瘤往上長，壓到下臂叢與頸交感神經（星狀神經節）一帶 | MRI 評估侵犯範圍，MDT 決定能否切除；3.2 的 T 分類把上溝列在胸壁侵犯 |
| 左側縱膈腔（主動脈肺動脈窗） | **聲音沙啞** | 左喉返神經繞過主動脈弓，左側縱膈腔腫瘤或淋巴結容易壓到；3.2 的 T4 定義含喉返神經侵犯 | 喉部評估、縱膈腔分期 |
| 膈神經 | 呃逆、患側橫膈抬高、運動時喘 | 膈神經被侵犯或壓迫；3.2 的 T3 定義含膈神經侵犯 | 胸部 X 光看橫膈位置 |
| 上腔靜脈 | 臉頸腫、上肢水腫、胸壁靜脈曲張、彎腰或平躺加重 | 縱膈腔腫瘤或淋巴結壓迫 SVC | [腫瘤急症章](00-shared/02-oncologic-emergencies.md#3-上腔靜脈症候群svc-syndrome)第 3 節與本章第 8 節 |
| 食道、心包膜 | 吞嚥困難；心包膜積液、低血壓、頸靜脈怒張 | 局部侵犯或心包膜轉移 | 第 8 節 |
| 遠端轉移 | 骨痛、ALP 與血鈣上升；頭痛、局部神經症狀；上腹痛、肝功能異常；鎖骨上或斜角肌淋巴結腫大（N3） | 骨、腦、肝、腎上腺與遠端淋巴結是常見轉移處 | 影像分期；背痛加上肢體無力要想到脊髓壓迫（急症章第 4 節） |
| 全身 | 體重減輕、倦怠、食慾不振 | 腫瘤造成的全身性影響 | ECOG 與預後（3.5）；惡病質見[支持性照護](00-shared/03-supportive-care.md#12-惡病質疲憊呼吸困難譫妄與困擾篩檢)第 12 節 |

> [!TIP]
> **用管線圖記解剖位置**
> 肺尖像一個「電纜出入口」：下臂叢、頸交感神經和鎖骨下血管都從這裡經過。腫瘤往上長，壓到哪一條線就出現哪一種症狀：壓到臂叢是肩臂痛，壓到交感神經是 Horner。左喉返神經則像一條繞過主動脈弓再折回喉嚨的線，縱膈腔左側的淋巴結一腫，就把這條線拉住，聲音就啞了。

**依組織型對照副腫瘤症候群**（症狀常早於肺癌診斷出現，治療腫瘤通常是最有效的處置；Kanaji et al., 2014）

| 組織型 | 症候群 | 辨識線索 | 處置入口 |
|--------|--------|---------|---------|
| 鱗狀細胞癌（SCC） | 高血鈣（腫瘤分泌 PTHrP，humoral hypercalcemia of malignancy） | 倦怠、便秘、多尿、意識改變；血鈣高 | [急症章](00-shared/02-oncologic-emergencies.md#5-惡性高血鈣hypercalcemia-of-malignancy)第 5 節；SCC 與 SCLC 兩種最常見的副腫瘤症候群之一（Kanaji et al., 2014） |
| SCLC | SIADH | 等容性低血鈉、尿滲透壓偏高；嚴重時抽搐、意識改變 | [急症章](00-shared/02-oncologic-emergencies.md#6-siadh-與低血鈉)第 6 節；本章第 8 節 |
| SCLC | 異位 ACTH（ectopic Cushing 症候群） | 低血鉀、血糖高或新發糖尿病、難控制的高血壓、水腫；瑞典 213 位 SCLC 中確診 0.5%、很可能 1%、可能 11%，這些病人存活較短（8 對 14 個月；Piasecka et al., 2022） | 懷疑時檢測皮質醇與 ACTH，請內分泌科會診 |
| SCLC | Lambert-Eaton 肌無力症候群（LEMS，抗 VGCC 抗體） | 近端肌無力、活動後改善（見第 8 節） | 神經科會診；治療腫瘤（Kanaji et al., 2014） |
| NSCLC | 肥厚性肺性骨關節病（HPOA） | 杵狀指（趾）、關節與長骨疼痛；占 NSCLC 的 1–5%，可早於肺癌的其他症狀出現（Lommatzsch et al., 2012） | 手腳骨 X 光或骨掃描；找肺部原發 |
| 腺癌（尤其黏液性） | Trousseau 症候群（癌症相關高凝血） | 反覆或遊走性血栓；與黏液素（mucin）活化血小板和選擇素有關（Varki, 2007） | 見[支持性照護](00-shared/03-supportive-care.md#7-癌症相關靜脈血栓vte)第 7 節 VTE |

> [!IMPORTANT]
> **副腫瘤症候群與組織型：是「最常見」，不是「專屬」**
> - **SCLC 與異位 ACTH**：在所有異位 Cushing 症候群病例中，類癌占 36–46%、SCLC 占 8–20%；SCLC 病人中臨床明顯者約 1.6–4.5%（上表引的瑞典 213 位 SCLC 回溯系列只有 0.5% 確診、1% 很可能，數字低於此範圍）；NSCLC 來源少見（Kanaji et al., 2014）。所以「ACTH 配 SCLC」成立，但就整個異位 ACTH 的來源而言，類癌比 SCLC 更常見。
> - **SCLC 與 LEMS**：LEMS 病人約一半有腫瘤，腫瘤幾乎都是 SCLC，NSCLC 只有少數個案報告（Kanaji et al., 2014）。反過來，SCLC 病人中 LEMS 的發生率在有限的前瞻與回溯研究約 3–6%；但美國申報資料中，推定為 SCLC 的病人只有 0.16% 有 LEMS 診斷，作者認為診斷率遠低於預期（Drapkin et al., 2025）。
> - **HPOA 與腺癌**：兩個 HPOA 病例系列都是腺癌最多，鱗癌也占兩到四成。日本 2,625 位肺癌病人中 19 位（0.72%）有 HPOA，其中腺癌 53%、鱗癌 21%（Ito et al., 2010；組織型數字引自 Kanaji et al., 2014 對該系列的敘述）；法國 53 位可切除 NSCLC 併 HPOA，腺癌 50%、鱗癌 40%（Magdeleinat et al., 1999）。「HPOA 配腺癌」是最常見的配對，不是腺癌專屬。
> - **HPOA 的頻率因研究而異**：1–5% 是 NSCLC 的綜述數字（Lommatzsch et al., 2012）；上述日本系列在 2,625 位肺癌病人（做過骨掃描者）中只有 0.72%。

**聚焦的身體評估（入院或回診時 5 分鐘能做完的版本）**

1. **一般**：ECOG、體重（與上次比較）、有無惡病質外觀。
2. **生命徵象**：呼吸速率、休息與活動後 SpO₂、血壓、體溫。
3. **頭頸**：眼瞼下垂、瞳孔大小與對稱性、臉部是否出汗（Horner）；聲音是否沙啞；頸部與鎖骨上淋巴結；臉頸與上肢水腫、頸靜脈怒張（SVC）。
4. **胸部**：呼吸型態與輔助肌；兩側呼吸音是否對稱；叩診濁音（積水）；局部喘鳴（氣道阻塞）；胸壁靜脈曲張。
5. **手與四肢**：杵狀指、關節腫痛（HPOA）；手內側（C8–T1）感覺與握力；近端肌力（LEMS）；單側肢體腫脹（VTE）。
6. **腹部與骨骼**：肝腫大、上腹壓痛；脊椎叩痛。
7. **神經**：定向感、顱神經、四肢肌力與感覺（脊髓壓迫的早期線索）、步態。

這份清單是依 ACCP 指引「用標準化方式評估症狀、徵象與實驗室結果，篩出有副腫瘤症候群與較可能已有轉移的病人」的原則整理（Spiro et al., 2007）；各院的入院護理評估表欄位不同，以院內表單為準。

> [!IMPORTANT]
> **考試重點：解剖位置對照症狀**
> - Pancoast（肺尖）＝肩臂痛 ＋ 同側 Horner（ptosis、miosis、anhidrosis）。
> - 聲音沙啞＝喉返神經麻痺，左側比右側常見，常來自主動脈肺動脈窗的淋巴結。
> - 呃逆、橫膈抬高＝膈神經。
> - 臉頸腫、胸壁靜脈曲張＝SVC。
> - SCC＝PTHrP 高血鈣；SCLC＝SIADH；兩者是最常見的副腫瘤症候群。

### 3.1 Work-up 流程

1. **病史與身體評估**：吸菸 pack-years、職業暴露、ECOG performance status、體重減輕；症狀、徵象與副腫瘤症候群的對照見 3.0。
2. **抽血**：CBC、腎肝功能、電解質（Na、Ca）、ALP、LDH。
3. **影像**：胸部及上腹部（含腎上腺）顯影 CT；預計根治性治療（I–III 期）做 PET-CT；II–IV 期做腦部 MRI（NCCN 建議；IB 期可考慮）。
4. **取得組織**：依病灶位置選擇 CT 導引切片、支氣管鏡、EBUS-TBNA；有肋膜積水抽水送細胞學。原則是**同一次檢查同時取得診斷與最高分期**（例如 EBUS 一次做縱膈腔淋巴結）。
5. **縱膈腔分期**：PET-CT 懷疑 N2/N3、中央型腫瘤或腫瘤 >3 cm，手術前以 EBUS-TBNA 或縱膈腔鏡確認。
6. **手術評估**：肺功能（FEV1、DLCO），計算術後預估值 ppoFEV1、ppoDLCO，再依結果決定要不要做運動測試或 CPET（公式與門檻見 3.4）。

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

- **台灣癌症登記的版次：** 依《台灣癌症登記長表摘錄手冊》民國 114 年 12 月修訂版的分期版本對照表，肺癌（V9036）自 **2025 年診斷**的個案起申報 AJCC 第 9 版；2018–2024 年診斷者仍是第 8 版（衛生福利部國民健康署, 2025）。因此本手冊第 1 節引用的 2023 年癌登統計是第 8 版期別；讀 2025 年以後診斷的統計或病歷時，先確認寫的是哪一版。

### 3.3 SCLC 分期

臨床上仍常用退伍軍人醫院（VA）二分法，NCCN 同時要求記錄 TNM：

- **局限期（limited stage, LS）**：病灶可以涵蓋在一個安全的放射治療照野內（大致是 TNM I–III 期，排除肺內多發結節太廣的 T3–4）。
- **廣泛期（extensive stage, ES）**：超出單一放射照野，包括 IV 期、惡性肋膜積水。約 2/3 病人診斷時已是廣泛期。

### 3.4 手術前生理評估與術後病房照護

**這一段的結論先講：** 先評估心血管風險，再用肺量計測 FEV1 與 DLCO，算出術後預估值（ppo）。ppoFEV1 與 ppoDLCO 都 >60% 為低風險，不需要再做檢查；任一項介於 60% 與 30% 之間，先做低科技運動測試；任一項 <30% 或運動測試不及格，做心肺運動測試（CPET）（Brunelli et al., 2013）。

**ppoFEV1 與 ppoDLCO 怎麼算（segment counting）**

- 公式：ppoFEV1 ＝ 術前 FEV1 ×（1 − S × 0.0526），S ＝ 預定切除的功能性肺節數；0.0526 ＝ 1/19，也就是把全肺看成 19 個肺節（Zeiher et al., 1995）。ppoDLCO 用同一個算法，把 FEV1 換成 DLCO。
- 例子：術前 FEV1 為預測值的 80%，預定切除右下葉（5 個肺節）。ppoFEV1 ＝ 80% ×（1 − 5 × 0.0526）＝ 80% × 0.737 ≈ **59%**，落在 30–60% 之間，下一步是低科技運動測試。
- 這個公式在肺葉切除時與實測值相關良好（r ＝ 0.87），但會低估實際的術後 FEV1（約 250 mL）；全肺切除的預測較不準（Zeiher et al., 1995）。

> [!NOTE]
> **肺節數的算法各院略有不同，左肺尤其如此**
> 右肺三葉的肺節數在兩篇論文一致：右上葉 3、右中葉 2、右下葉 5，合計 10 節（Bae et al., 2022；Lim et al., 2024）。左肺在 19 節模型裡共 9 節，但左上葉與左下葉各算幾節沒有統一算法：Bae 等人把左上葉算 4（上區 2、舌區 2）、左下葉算 5；Lim 等人指出左肺 9 節的分配沒有共識（左上區 2 節，或左下葉 4 節、也就是左上葉 5 節，兩種說法），因此改用 20 節模型（每節占 5%，左上葉 5、左下葉 5）。兩種 19 節分法對左側肺葉切除的 S 差 1 節，ppo 值約差術前值的 1/19（約 5%）。本章例子用右下葉（5 節），不受左肺分配差異影響；左側手術請以胸腔外科部的計算表為準。

**風險分層與下一步（ACCP 2013；Brunelli et al., 2013）**

| 條件 | 風險 | 下一步 |
|------|------|--------|
| ppoFEV1 與 ppoDLCO 皆 >60% | 低 | 不需要再做檢查 |
| ppoFEV1 或 ppoDLCO 介於 60% 與 30% | 需分層 | 低科技運動測試：爬樓梯高度 >22 m 或 shuttle walk 距離 >400 m 為及格，視為低風險 |
| ppoFEV1 或 ppoDLCO <30%，或運動測試不及格 | 需 CPET | 測 VO₂ peak：<10 mL/kg/min 或 <35% 預測值＝高風險（死亡與長期失能）；>20 mL/kg/min 或 >75% 預測值＝低風險 |

ERS／ESTS 2009 指引把心臟評估、FEV1、DLCO 與運動測試整合成同一套演算法；對放化療的適合度則因資料不足，無法建議特定的檢查或切點（Brunelli et al., 2009）。高風險不等於不能治療，而是要和病人談 SBRT、較小的切除範圍等替代方案（Brunelli et al., 2013）。

> [!TIP]
> **ppo 值像「開刀後剩下的肺活量存款」**
> 手術前的 FEV1 是帳戶裡的錢，切掉一個肺節就像提走 1/19。ppo 值不是在問「有沒有錢開刀」，而是在問「提走之後剩下的錢夠不夠過日子」；剩下的錢在 60% 以上就放心，30% 到 60% 要先走一圈（爬樓梯）看看體力，30% 以下就要做最完整的壓力測試（CPET）。

**術後病房照護（肺葉切除或肺節切除）**

ERAS Society／ESTS 2019 指引把肺手術的加速復原措施整理成 45 項，核心包括：術前衛教與營養篩檢、戒菸、高風險者的術前復健、預防靜脈血栓、減少鴉片類藥物的多模式止痛、維持正常容積的輸液、盡早拔除胸管、避免導尿管、術後早期下床（Batchelor et al., 2019）。轉成病房工作清單：

| 項目 | 護理與專師的重點 |
|------|----------------|
| 呼吸 | 每班評估呼吸速率、SpO₂、呼吸音；鼓勵深呼吸、咳嗽與誘發性肺量計；出現喘或血氧下降先排除氣胸、積水、痰栓、肺炎 |
| 胸管 | 每班記錄引流量、顏色、水封瓶有無氣泡（漏氣）與呼吸性波動；皮下氣腫範圍是否擴大；盡早拔管（ERAS 建議）；拔管標準依外科 |
| 止痛 | 多模式、減少鴉片類；疼痛會讓病人不敢咳嗽而增加肺部併發症 |
| 活動 | 術後早期下床（ERAS 建議），有胸管也可以走動 |
| 輸液 | 維持正常容積，避免過量（肺水腫風險） |
| 血栓 | 預防靜脈血栓（ERAS 建議）；術後腿腫、胸痛或喘要想到肺栓塞 |
| 管路 | 盡早移除導尿管（ERAS 建議） |
| 戒菸 | 住院期間是很好的戒菸時機，見 7.9 |

> [!NOTE]
> **胸管、止痛與拔管流程依院內規範**
> 胸管的負壓設定、拔管時機、止痛處方與出院衛教各院不同。上表是 ERAS 指引的原則轉成的檢查清單，不是醫囑；實際以胸腔外科的術後 order set 為準。

### 3.5 預後

**這一段的結論先講：** 期別是最強的預後因子。IASLC 第 9 版資料庫分析了 76,518 位 NSCLC 病人（臨床分期 58,193 位、病理分期 39,192 位），新的分期組合在各期之間的排序一致，區辨預後的能力良好（Rami-Porta et al., 2024）。除了期別，體能狀態、年齡與性別也各自獨立影響存活。

> [!CAUTION]
> **待核對：第 9 版各期別的 5 年存活率**
> IASLC 第 9 版各期別（IA1 到 IVB）的 5 年整體存活率，原論文（Rami-Porta et al., 2024）與 IASLC 出版品的全文本次無法取得（出版社擋下自動下載，PubMed 只有摘要），因此本手冊**不列**這張表，避免用二手網站的數字。請在使用前查閱 Rami-Porta 等人的論文，或 IASLC Staging Manual in Thoracic Oncology 第 3 版的存活圖表。

**台灣的數字（衛福部新聞稿，統計年份不全相同）**

| 期別 | 5 年存活率 | 來源 |
|------|-----------|------|
| 第 1 期 | 約 9 成 | 衛福部 2025-04-08 新聞稿（統計年份未標示；衛生福利部, 2025c） |
| 第 2 期 | 接近 6 成以上 | 同上 |
| 第 3 期 | 近 3 成 | 同上 |
| 第 4 期 | 僅剩 1 成 | 同上；另一則 2023-01-05 新聞稿也寫第 4 期降到 1 成（衛生福利部, 2023） |
| 全部（105–109 年新發個案） | 5 年相對存活率 38.2% | 衛福部 2023-01-05 新聞稿（衛生福利部, 2023） |

這些數字是新聞稿的敘述，不是完整的存活率報告：期別版次、是否為相對存活率、統計年份都未標明（新聞稿只有 105–109 年那一筆明寫「相對存活率」）。引用時要註明來源與日期。

**預後因子**

| 因子 | 重點 | 來源 |
|------|------|------|
| 期別 | 最重要；第 9 版把 N2 細分為 N2a／N2b，M1c 細分為 M1c1／M1c2（兩者仍同屬 IVB） | Rami-Porta et al., 2024 |
| 體能狀態（PS） | 在期別之外仍是非常重要的獨立因子；年齡與性別次之 | Sculier et al., 2008 |
| 檢驗值 | 晚期（IIIB／IV）NSCLC：白血球數與高血鈣有預後意義；SCLC：白蛋白是獨立因子 | Sculier et al., 2008 |
| 手術切除的 NSCLC | 病理期別、年齡與性別獨立影響存活；組織型影響較小（BAC 亞型較好） | Chansky et al., 2009 |
| 驅動基因與治療 | 有 driver 且用對標靶藥，存活明顯拉長，例如 EGFR TKI（FLAURA 整體存活中位數 38.6 個月；Ramalingam et al., 2020）、ALK TKI（CROWN 5 年 PFS 60%；Solomon et al., 2024） | 見 4.3 |
| 免疫治療 | PD-L1 ≥50% 單用 pembrolizumab 5 年 OS 31.9%（Reck et al., 2021）；ES-SCLC 加免疫後中位 OS 約 12–13 個月（Horn et al., 2018；Paz-Ares et al., 2019） | 見 4.3、4.4 |
| 體重減輕、惡病質 | 本手冊沒有取得肺癌專屬的預後數據；惡病質的定義與處置見[支持性照護](00-shared/03-supportive-care.md#12-惡病質疲憊呼吸困難譫妄與困擾篩檢)第 12 節 | — |

預後資訊用在兩個地方：跟病人與家屬談治療目標，以及早期緩和照護與預立醫療照護諮商（ACP）的時機（見[支持性照護](00-shared/03-supportive-care.md#9-早期緩和照護)第 9 節）。講的時候要用「同樣期別的病人中位數大概是…，個別差異很大」的語氣，不要把平均數說成個人的命運。


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
| II–IIIA 期（IB 期有高風險因子時考慮，如低分化、血管侵犯、楔狀切除、臟層肋膜侵犯、Nx；第 7 版「IB 期 ≥4 cm」中 >4–5 cm 的腫瘤，第 8／9 版已屬 T2b N0、IIA 期） | Cisplatin 為主的雙藥化療 × 4 週期 | LACE 匯總分析：死亡風險 HR 0.89，5 年存活絕對增加 5.4%；IA 期反而可能有害（HR 1.40），所以 IA 期不做輔助化療（Pignon et al., 2008） |
| EGFR ex19del／L858R，IB–IIIA 期 | 化療（視情況）後 **osimertinib 80 mg QD × 3 年** | ADAURA：DFS HR 0.20；整體存活 HR 0.49（Wu et al., 2020；Tsuboi et al., 2023） |
| ALK 陽性，IB（≥4 cm）–IIIA 期 | **Alectinib 600 mg BID × 2 年** | ALINA：II–IIIA 期 DFS HR 0.24（Wu et al., 2024） |
| PD-L1 ≥1%、無 EGFR/ALK，II–IIIA 期 | 輔助化療後 atezolizumab 1,200 mg q3w × 16 週期（1 年） | IMpower010：初次分析 DFS HR 0.66（Felip et al., 2021）。5 年更新中只有 **PD-L1 ≥50%** 的整體存活有顯著改善（HR 0.47），PD-L1 ≥1% 整體的存活差異不顯著（Felip et al., 2025） |
| 無 EGFR/ALK，IB（≥4 cm）–IIIA 期 | 輔助化療後 pembrolizumab 200 mg q3w，最多 18 週期（約 1 年） | PEARLS/KEYNOTE-091：DFS 53.6 對 42.0 個月（HR 0.76）；但 PD-L1 ≥50% 這個共同主要終點未達顯著（O'Brien et al., 2022） |

**術前／圍術期（腫瘤 ≥4 cm 或淋巴結陽性，先排除 EGFR/ALK）**

| 方案 | 內容 | 結果 |
|------|------|------|
| 術前（neoadjuvant） | Nivolumab 360 mg ＋ 含鉑雙藥 q3w × 3 → 手術 | CheckMate 816：pCR 24.0% 對 2.2%，EFS 31.6 對 20.8 個月（Forde et al., 2022）；5 年整體存活 65.4% 對 55.0%（HR 0.72；Forde et al., 2025） |
| 圍術期：pembrolizumab | 術前 pembrolizumab 200 mg ＋ cisplatin 雙藥 q3w × 4 → 手術 → 術後 pembrolizumab 最多 13 週期 | KEYNOTE-671：EFS 47.2 對 18.3 個月；36 個月整體存活 71% 對 64%（HR 0.72）（Wakelee et al., 2023；Spicer et al., 2024） |
| 圍術期：durvalumab | 術前 durvalumab 1,500 mg ＋ 化療 q3w × 4 → 手術 → 術後 durvalumab q4w × 12 | AEGEAN：EFS HR 0.68、pCR 17.2% 對 4.3%（Heymach et al., 2023）；期中整體存活尚未顯著（Heymach et al., 2026a） |
| 圍術期：nivolumab | 術前 nivolumab 360 mg ＋ 化療 q3w × 4 → 手術 → 術後 nivolumab 480 mg q4w × 1 年 | CheckMate 77T：EFS HR 0.58、pCR 25.3% 對 4.7%（Cascone et al., 2024）；整體存活結果尚未發表 |

> [!TIP]
> **術前免疫的比喻**
> 腫瘤還在身體裡的時候，它本身就是「抗原教材」。術前先給免疫治療，免疫系統可以邊看教材邊學怎麼認腫瘤；等手術拿掉腫瘤後，學會的 T 細胞繼續巡邏殘存的微小轉移。術前治療的另一個好處是手術時就能直接量到 pCR（病理完全反應）：CheckMate 816 中達到 pCR 的病人 5 年整體存活率 95.3%，未達到者 55.7%（Forde et al., 2025）。但 pCR 能否在試驗層級取代整體存活當替代指標（surrogate endpoint），目前仍未確立。

### 4.2 NSCLC III 期

III 期是異質性最高的一期，**一定要多專科團隊（MDT）討論**可不可以切。

- **可切除（多為 IIIA）**：沒有 EGFR/ALK 變異者走 4.1 的圍術期化療 ＋ 免疫路線；EGFR ex19del／L858R 或 ALK 陽性者先手術，術後接 osimertinib 或 alectinib 輔助治療（ADAURA、ALINA），因為 CheckMate 816、77T 排除這兩類病人，AEGEAN 的療效分析也排除，KEYNOTE-671 未強制檢測、帶此類變異者極少，免疫治療對他們的效益證據不足。
- **不可切除**：
  1. **同步化放療（concurrent chemoradiotherapy, CCRT）**：放療 60 Gy／30 次，搭配含鉑雙藥（cisplatin ＋ etoposide、carboplatin ＋ paclitaxel 每週，或非鱗狀用 cisplatin ＋ pemetrexed）。
  2. CCRT 後沒有惡化 → **durvalumab 鞏固治療 12 個月**。PACIFIC：PFS 16.8 對 5.6 個月；5 年整體存活率 42.9% 對 33.4%（Antonia et al., 2017；Spigel et al., 2022）。
  3. **EGFR ex19del／L858R**：同步（CCRT）或序列性（sequential）含鉑化放療後沒有惡化 → 改用 **osimertinib 直到疾病惡化**。LAURA：PFS 39.1 對 5.6 個月；放射性肺炎 48% 對 38%，多為 1–2 級（Lu et al., 2024）。

> [!WARNING]
> **CCRT 後的肺炎要分清楚**
> CCRT 後接 durvalumab 的病人，咳嗽、喘、CT 毛玻璃病灶可能是放射性肺炎、免疫相關肺炎或感染。放射性肺炎通常在放療後 1–6 個月、病灶貼著照野邊界；免疫性肺炎可跨出照野。處置先排除感染，G2 暫停 durvalumab 並給 prednisone 1–2 mg/kg/day，緩解到 G0–1 且類固醇減量後才可恢復；G3–4 永久停用 durvalumab，住院給 IV methylprednisolone 1–2 mg/kg/day（見 [irAE 章](00-shared/04-irae.md)）。

### 4.3 NSCLC IV 期

**決策順序：組織型 → biomarker → PD-L1 → ECOG。**

#### 有驅動基因：標靶治療優先

| 變異 | 第一線（偏好） | 其他選擇／惡化後 | 關鍵試驗 |
|------|-------------|---------------|---------|
| EGFR ex19del／L858R | **Osimertinib**；osimertinib ＋ pemetrexed/鉑類；amivantamab ＋ lazertinib | Gefitinib、erlotinib、afatinib、dacomitinib；惡化後再切片找抗藥機轉 | FLAURA、FLAURA2、MARIPOSA |
| EGFR T790M（第一、二代 TKI 後） | Osimertinib | | AURA3（Mok et al., 2017）：PFS 10.1 對 4.4 個月 |
| Osimertinib 後惡化 | Amivantamab ＋ carboplatin ＋ pemetrexed；含鉑化療 | 依抗藥機轉（如 MET 放大）；datopotamab deruxtecan（EGFR TKI 與含鉑化療都用過後） | MARIPOSA-2（Passaro et al., 2024）：PFS 6.3 對 4.2 個月；Dato-DXd 匯總分析反應率 43%（Ahn et al., 2025） |
| EGFR 非典型突變 | Afatinib 或 osimertinib | | |
| EGFR exon 20 insertion | Amivantamab ＋ carboplatin ＋ pemetrexed | 含鉑化療後惡化：sunvozertinib（美國 FDA 2025-07 加速核准；第一線適應症仍在審查，台灣無藥證） | PAPILLON（Zhou et al., 2023b）：PFS 11.4 對 6.7 個月；WU-KONG28（第一線；Zhou et al., 2026）：sunvozertinib 對化療 PFS 10.3 對 7.5 個月，整體存活尚未成熟 |
| ALK | **Alectinib**、brigatinib、**lorlatinib** | 第二代後惡化用 lorlatinib | ALEX（Peters et al., 2017）、ALTA-1L（Camidge et al., 2018）、CROWN（Shaw et al., 2020） |
| ROS1 | Entrectinib、crizotinib、repotrectinib、taletrectinib | 後線 repotrectinib、taletrectinib（對 G2032R 抗藥突變仍有效） | PROFILE 1001（Shaw et al., 2014）、TRIDENT-1（Drilon et al., 2024）、TRUST（Pérol et al., 2025） |
| BRAF V600E | Dabrafenib ＋ trametinib；encorafenib ＋ binimetinib | | BRF113928（Planchard et al., 2017）、PHAROS（Riely et al., 2023；未治療者反應率 75%） |
| MET exon 14 | Capmatinib、tepotinib | | GEOMETRY mono-1（Wolf et al., 2020）、VISION（Paik et al., 2020） |
| RET | Selpercatinib、pralsetinib | | LIBRETTO-431（Zhou et al., 2023a）：PFS 24.8 對 11.2 個月；pralsetinib：ARROW（Gainor et al., 2021） |
| NTRK | Larotrectinib、entrectinib | | larotrectinib 跨癌別整合分析（Drilon et al., 2018） |
| KRAS G12C | 化療 ＋ 免疫（同無 driver） | 二線 sotorasib、adagrasib | CodeBreaK 200（de Langen et al., 2023）：PFS 5.6 對 4.5 個月；KRYSTAL-12（Barlesi et al., 2025）：PFS 5.5 對 3.8 個月 |
| HER2 突變 | 化療 ＋ 免疫（台灣目前沒有第一線 HER2 標靶藥證）；HER2 TKD 突變者，美國 FDA 已加速核准 zongertinib（2026-02）與 sevabertinib（2026-09）用於第一線 | 二線 trastuzumab deruxtecan 5.4 mg/kg、zongertinib、sevabertinib（台灣 T-DXd 與 sevabertinib 有藥證，皆限曾接受全身性治療者；zongertinib 無藥證） | DESTINY-Lung02（Goto et al., 2023）：反應率 49.0%；Beamion LUNG-1：zongertinib 反應率 71%（已治療、TKD 突變；Heymach et al., 2025），第一線 76%（Heymach et al., 2026b） |

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
> 很多標靶試驗 PFS 大幅改善，整體存活（OS）卻沒有顯著差異，例如 IPASS（Mok et al., 2009）、AURA3（Mok et al., 2017）、PROFILE 1014（Solomon et al., 2014）、ALTA-1L（Camidge et al., 2018）、ALEX 最終分析（Peters et al., 2026）。主要原因是**交叉治療（crossover）**：對照組惡化後多數會換到試驗藥或同類藥（例如 IPASS 的 EGFR 突變陽性者化療組約 64%、AURA3 73%、PROFILE 1014 84%），存活差距被拉平；ALEX、ALTA-1L 則還要考慮後線治療與追蹤時間。讀試驗時，PFS 像「這條路能撐多久不塞車」，OS 是「最後到不到得了終點」；換路的人多了，終點時間就會接近。

#### 沒有驅動基因：看 PD-L1

| PD-L1 TPS | 非鱗狀 | 鱗狀 |
|-----------|-------|------|
| ≥50% | Pembrolizumab、atezolizumab 或 cemiplimab 單藥；或化療 ＋ 免疫 | 同左 |
| 1–49% | 化療 ＋ 免疫 | 化療 ＋ 免疫 |
| <1% | 化療 ＋ 免疫（含雙免疫選項，如 CheckMate 9LA、POSEIDON） | 化療 ＋ 免疫（含雙免疫選項，如 CheckMate 9LA、POSEIDON） |

常用的化療 ＋ 免疫組合：

- **非鱗狀**：carboplatin（或 cisplatin）＋ pemetrexed ＋ pembrolizumab × 4 → pembrolizumab ＋ pemetrexed 維持（KEYNOTE-189；Gandhi et al., 2018）。
- **鱗狀**：carboplatin ＋ paclitaxel 或 nab-paclitaxel ＋ pembrolizumab × 4 → pembrolizumab 維持（KEYNOTE-407；Paz-Ares et al., 2018）。
- **其他**：atezolizumab ＋ bevacizumab ＋ carboplatin ＋ paclitaxel（IMpower150，僅非鱗狀；Socinski et al., 2018；劑量見 5.1）；nivolumab ＋ ipilimumab ± 兩週期化療（CheckMate 227、9LA；Hellmann et al., 2019；Paz-Ares et al., 2021）；durvalumab ＋ tremelimumab ＋ 化療（POSEIDON；Johnson et al., 2023）。

| 試驗 | 族群 | 主要結果 |
|------|------|---------|
| KEYNOTE-024（Reck et al., 2016；Reck et al., 2021） | PD-L1 ≥50% | Pembrolizumab 對化療 PFS 10.3 對 6.0 個月；5 年 OS 31.9% 對 16.3% |
| KEYNOTE-189（Gandhi et al., 2018） | 非鱗狀，不分 PD-L1 | 加 pembrolizumab 死亡風險 HR 0.49；5 年 OS 19.4% 對 11.3%（HR 0.60；Garassino et al., 2023） |
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

1. **Carboplatin ＋ etoposide ＋ atezolizumab**（IMpower133：OS 12.3 對 10.3 個月，HR 0.70；Horn et al., 2018）或 **＋ durvalumab**（CASPIAN：OS 13.0 對 10.3 個月，HR 0.73；3 年存活 17.6% 對 5.8%；Paz-Ares et al., 2019；Paz-Ares et al., 2022），共 4 週期 → 免疫維持。
2. 以 atezolizumab ＋ carboplatin ＋ etoposide 誘導 4 週期後沒有惡化者，維持期可改用 **lurbinectedin ＋ atezolizumab**（適應症限 atezolizumab 誘導，不含 durvalumab 方案）：IMforte 試驗中 PFS（HR 0.54）與整體存活（HR 0.73）都優於 atezolizumab 單獨維持，但 3–4 級副作用較多（38% 對 22%），lurbinectedin 要合併 G-CSF 預防（Paz-Ares et al., 2025）。台灣也是 IMforte 的收案國家。
3. 腦部：以 MRI 定期追蹤為主。日本試驗中，在每 3 個月 MRI 追蹤下做 PCI 不但沒有存活好處，數字上還較差（11.6 對 13.7 個月，HR 1.27）（Takahashi et al., 2017）。

**復發 SCLC**

| 情境 | 選擇 | 依據 |
|------|------|------|
| 距上次含鉑化療結束 ≥90 天才復發（敏感型，sensitive relapse） | **Tarlatamab**；或再用含鉑 ＋ etoposide（rechallenge） | Baize et al., 2020：CTFI ≥90 天者 carboplatin ＋ etoposide 再挑戰對 topotecan，PFS 4.7 對 2.7 個月。NCCN 自 v2.2026 起已刪除「>6 個月才再用原方案」的 CTFI 分流，後線治療改依臨床判斷，tarlatamab 為 category 1 優先選擇 |
| 距最後一劑含鉑化療 <90 天就復發（抗藥型 resistant）、含鉑化療期間無反應或惡化（refractory），或不適合再用鉑 | **Tarlatamab**（第一優先）、topotecan；lurbinectedin 單藥二線在美國已無適應症（台灣藥證是否調整待確認） | DeLLphi-304：tarlatamab 對化療 OS 13.6 對 8.3 個月（HR 0.60），3 級以上副作用 54% 對 80%（Mountzios et al., 2025）；lurbinectedin 單臂第 2 期反應率 35.2%（Trigo et al., 2020），但確認性第 3 期 LAGOON 試驗（2026-06-12 公布頂線結果，尚未正式發表）OS 未優於 topotecan 或 irinotecan（8.7 對 10.7 個月，HR 1.19，95% CI 0.96–1.48），美國 FDA 已於 2026-09-30 撤銷其二線加速核准（Zepzelca 美國仿單 2026-09 修訂版）；第一線維持（IMforte）適應症不受影響 |

**Tarlatamab** 是 DLL3 × CD3 雙特異性 T 細胞銜接抗體（bispecific T-cell engager），仿單有 CRS 與神經毒性（含 ICANS）的加框警語。階梯式起始：C1D1 1 mg → C1D8 10 mg → C1D15 10 mg，之後 10 mg q2w（Amgen, 2026）。前兩劑（C1D1、C1D8）輸注前 1 小時內給 dexamethasone 8 mg IV、輸注後補 NS 1 L，並自輸注開始在醫療機構監測 6–8 小時（美國仿單 2026-09 版；2026-07 以前的版本是 22–24 小時），第 2、9 天評估生命徵象，48 小時內由照顧者陪同、停留在 1 小時內可到醫療機構處。之後每劑仍需輸注後觀察（C1D15 與第 2 週期 6–8 小時、第 3–4 週期 3–4 小時、第 5 週期起 2 小時）；ICANS 可在數週後才出現。**病房的醫囑範本、監測表與出院衛教見 7.7**；CRS 與 ICANS 的 ASTCT 分級見[腫瘤急症章](00-shared/02-oncologic-emergencies.md#9-細胞激素釋放症候群crs與神經毒性icans)第 9 節。

> [!TIP]
> **雙特異性抗體的比喻**
> Tarlatamab 一手抓住腫瘤細胞上的 DLL3，一手抓住 T 細胞的 CD3，像幫 T 細胞和腫瘤細胞「牽線配對」。配對成功、T 細胞大量活化時，會一口氣放出細胞激素，所以第一次給藥最容易發生 CRS。

### 4.5 新藥在台灣的上市狀態

指引寫的藥，台灣不一定買得到；買得到也不一定有健保。下表是近兩年國外核准的肺癌新藥在台灣的藥證狀態（TFDA 藥品許可證資料，2026-10-27 版）。健保欄是用藥名（學名與商品名）逐一搜尋 115/10/22 版第 9 節原文的結果：「原文未見」代表該版第 9 節完全沒有這個藥的條文；各藥給付條件見[第 9 段](#9-健保給付與事前審查)，沒有條文的藥另列在 9.5。

| 藥物 | 用途 | 美國 FDA | 台灣藥證 | 健保（115/10/22 版） |
|------|------|---------|---------|---------------------|
| Tarlatamab | 含鉑後惡化的 ES-SCLC | 2024-05 加速核准，2025-11 依 DeLLphi-304 完全核准 | **有**（2025-02-26） | 原文未見，無健保給付 |
| Lurbinectedin ＋ atezolizumab | ES-SCLC 第一線維持 | 2025-10 | 有 lurbinectedin 藥證，含維持治療適應症（加入日期待確認） | lurbinectedin 原文未見，無健保給付；atezolizumab 的肺癌給付見 9.69（第 9.3 節） |
| Amivantamab 皮下劑型 | 與靜脈劑型相同的 EGFR 適應症 | 2025-12 | **有**（2026-06-10） | 9.126 有給付 amivantamab，但只限 EGFR exon 20 插入突變第一線；原文沒有區分劑型，未見皮下劑型的文字 |
| Lazertinib | 合併 amivantamab 第一線 | 已核准 | **有**（2025-06-24） | 原文未見，無健保給付 |
| Repotrectinib | ROS1、NTRK | 已核准 | **有**（2025-04-11） | **有給付**（9.131，115/2/1）：限 crizotinib 或 entrectinib 治療中惡化的 ROS1 陽性 NSCLC；NTRK 原文未見 |
| Sevabertinib | HER2 突變 NSCLC | 2025-11（後線）、2026-09（第一線） | **有**（2026-06-11，僅限曾接受治療者） | 原文未見，無健保給付 |
| Datopotamab deruxtecan | EGFR 突變 NSCLC（後線） | 2025-06 加速核准 | 台灣只有乳癌適應症，**沒有肺癌適應症** | 原文未見，無健保給付 |
| Zongertinib | HER2 突變 NSCLC | 2025-08（後線）、2026-02（第一線） | **無** | 原文未見，無健保給付 |
| Sunvozertinib | EGFR exon 20 insertion | 2025-07 加速核准 | **無** | 原文未見，無健保給付 |
| Taletrectinib | ROS1 | 2025-06 | **無** | 原文未見，無健保給付 |

> [!NOTE]
> **藥證、健保、院內處方集是三件事**
> 有藥證代表可以合法使用；健保給付要另外符合第 9 節條件；醫院是否進藥則看院內藥事委員會。病人問「這個新藥可以用嗎」，要分這三層回答。上表藥證依 2026-10-27 資料、健保依 115/10/22 版原文整理，兩者都會持續更新。

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
| Carboplatin ＋ nab-paclitaxel ＋ pembrolizumab | nab-Paclitaxel 100 mg/m² D1,8,15 ＋ carboplatin AUC 6 D1 ＋ pembrolizumab 200 mg D1，q3w × 4 → pembrolizumab 維持 | 不需過敏預防用藥 |
| Atezolizumab ＋ bevacizumab ＋ carboplatin ＋ paclitaxel（ABCP，僅非鱗狀、無 EGFR/ALK 異常） | Atezolizumab 1,200 mg ＋ bevacizumab 15 mg/kg ＋ paclitaxel 175 或 200 mg/m² ＋ carboplatin AUC 6，皆 D1，q3w，最多 4 或 6 週期 → atezolizumab 1,200 mg ＋ bevacizumab 15 mg/kg q3w 維持（Genentech, 2026c；試驗：Socinski et al., 2018） | 每次給藥前檢核血壓、尿蛋白、近期咳血與手術計畫（6.8）；paclitaxel 過敏預防；給藥順序依院內。健保：9.37 第 7 項（條號最新修訂 114/10/1）與 9.69，bevacizumab 與 pemetrexed 限指定廠牌，見 9.4 |
| Bevacizumab ＋ erlotinib（EGFR L858R，第一線） | Erlotinib 150 mg QD ＋ bevacizumab q3w。NEJ026 用 bevacizumab 15 mg/kg，PFS 16.9 對 13.3 個月（HR 0.605），3 級以上不良事件 88% 對 46%（Saito et al., 2019）；ARTEMIS-CTONG1509 PFS 17.9 對 11.2 個月（HR 0.55；Zhou et al., 2021）。**健保條文限 bevacizumab 7.5 mg/kg q3w**（9.29 第 2 項 114/4/1；9.37 第 5 項 114/3/1，見 9.1） | 檢核同上（6.8）；erlotinib 的皮疹與腹瀉見 6.1；給付條件：第 IV 期、L858R、腦轉移、非鱗狀 |
| Cisplatin ＋ pemetrexed（術後輔助，非鱗狀） | Cisplatin 75 mg/m² D1 ＋ pemetrexed 500 mg/m² D1，q3w × 4 | Cisplatin 水化與高致吐性止吐 |
| Cisplatin ＋ vinorelbine（術後輔助） | Cisplatin 75–80 mg/m² D1 ＋ vinorelbine 25–30 mg/m² D1,8，q3w × 4 | Vinorelbine 為起泡劑（vesicant），注意外滲 |
| Cisplatin ＋ gemcitabine（鱗狀） | Cisplatin 75 mg/m² D1 ＋ gemcitabine 1,250 mg/m² D1,8，q3w | |
| Docetaxel ± ramucirumab（二線） | Ramucirumab 10 mg/kg D1 ＋ docetaxel 75 mg/m² D1，q3w | Ramucirumab 每次輸注前給 IV H1 阻斷劑（如 diphenhydramine），曾發生 G1–2 輸注反應者再加 dexamethasone 與 acetaminophen；ramucirumab 先於 docetaxel 輸注。Docetaxel 前 dexamethasone 8 mg BID × 3 天（從前一天開始），預防體液滯留與過敏 |
| Durvalumab 鞏固（PACIFIC） | 10 mg/kg q2w 或 1,500 mg q4w，共 12 個月 | 每次前看甲狀腺、肝腎功能 |
| Atezolizumab | 1,200 mg q3w（或 840 mg q2w、1,680 mg q4w） | |
| Nivolumab | 240 mg q2w 或 480 mg q4w；術前 360 mg q3w × 3 合併化療 | |

**Pemetrexed 前置用藥（考試必考）**

- **Folic acid** 400–1,000 µg PO QD：第一劑前 7 天開始（美國仿單；歐盟仿單寫法為第一劑前 7 天內至少吃 5 天），持續到最後一劑後 21 天；實際以台灣核准仿單與院內處方為準。
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
| Lurbinectedin ＋ atezolizumab（ES-SCLC 第一線維持，限 atezolizumab 誘導 4 週期後沒有惡化者） | Lurbinectedin 3.2 mg/m² ＋ atezolizumab 1,200 mg，D1，q3w，並預防性使用 G-CSF（IMforte；單藥二線用法見 4.4，美國已無適應症） |
| Topotecan | 1.5 mg/m² IV D1–5，q3w |
| Tarlatamab | 第 1 天 1 mg、第 8 天 10 mg、第 15 天 10 mg，之後 10 mg q2w（Amgen, 2026）；C1D1、C1D8 輸注前 1 小時內 dexamethasone 8 mg IV、輸注後 NS 1 L，自輸注開始監測 6–8 小時（美國 2026-09 版）；之後每劑輸注後觀察 2–8 小時（依週期）；流程見 7.7 |

### 5.4 口服標靶藥

| 藥物 | 劑量 | 與食物 | 減量／注意 |
|------|------|-------|-----------|
| Osimertinib | 80 mg QD | 不限 | 減為 40 mg；QTc、ILD、心衰竭 |
| Gefitinib | 250 mg QD | 不限 | 避免 PPI |
| Erlotinib | 150 mg QD | 空腹（飯前 1 小時或飯後 2 小時） | 吸菸降低血中濃度；避免 PPI |
| Afatinib | 40 mg QD | 空腹（台灣與歐盟仿單：服藥前至少 3 小時、服藥後至少 1 小時內不可進食；美國仿單：飯前 1 小時或飯後 2 小時） | 減為 30、20 mg；腹瀉、甲溝炎常見 |
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
> - **Gefitinib、erlotinib、dacomitinib、selpercatinib、sotorasib 的吸收需要胃酸**：盡量避免 PPI。必須用制酸藥時，依美國仿單錯開服藥時間：
>   - Gefitinib：在 H2 阻斷劑或制酸劑前後 6 小時服用；非用 PPI 不可時，在前一劑 PPI 後 12 小時或下一劑 PPI 前 12 小時服用。
>   - Erlotinib：在 H2 阻斷劑後 10 小時、下一劑前 2 小時服用；與制酸劑間隔數小時。
>   - Dacomitinib：在 H2 阻斷劑前 6 小時或後 10 小時服用；也可改用局部制酸劑。
>   - Selpercatinib：PPI、H2 阻斷劑、局部制酸劑都要避免。非用不可時：併用 PPI 要隨餐服藥；在 H2 阻斷劑前 2 小時或後 10 小時服用；在制酸劑前後 2 小時服用。
>   - Sotorasib：PPI 與 H2 阻斷劑都要避免。非用不可時只用局部制酸劑，sotorasib 在制酸劑前 4 小時或後 10 小時服用。
> - 多數 TKI 經 **CYP3A4** 代謝，但誘導劑與抑制劑的處置**因藥而異，不是一律避免**：葡萄柚、azole 類抗黴菌藥是抑制劑；rifampin、carbamazepine、phenytoin、St. John's wort 是強效誘導劑。併用強效誘導劑時，osimertinib、gefitinib、erlotinib、afatinib 是「加量」，lorlatinib 是「禁忌」，alectinib 則不受影響；逐藥規則見下表。
> - 開立任何新藥（包括抗生素、抗黴菌藥）前，先查交互作用。

**強效 CYP3A 誘導劑（以 rifampin 為代表）併用時，各藥美國仿單怎麼寫**

台灣是結核病中度流行地區，肺癌病人同時要吃 TKI 與抗結核藥並不少見（TB 與免疫治療的關係見 6.6）。下表只列仿單的文字，台灣核准仿單、劑量細節與實際處理，必須和感染科及藥劑部一起決定。

| 藥物 | 與強效 CYP3A 誘導劑（rifampin 等）併用 | 來源 |
|------|-------------------------------------|------|
| Osimertinib | 避免；無法避免時加到 160 mg QD，停用誘導劑 3 週後回到 80 mg | AstraZeneca, 2026 |
| Gefitinib | 在沒有嚴重不良反應下加到 500 mg QD，停用誘導劑 7 天後回到 250 mg | AstraZeneca, 2023 |
| Erlotinib | 避免；必要時每 2 週加 50 mg，視耐受度最高 450 mg（仿單把 rifampin、rifabutin、rifapentine 都列為誘導劑） | Alembic, 2024 |
| Afatinib | rifampicin 屬 P-gp 誘導劑：需長期併用時每日加 10 mg（耐受下），停用 2–3 天後回原劑量 | Boehringer Ingelheim, 2025 |
| Dacomitinib | 本手冊檢索 2026-06 版仿單，未見針對 CYP3A 誘導劑的劑量建議，請藥師確認 | Pfizer, 2026b |
| Alectinib | rifampin 對 alectinib 加 M4 的暴露沒有臨床上有意義的影響 | Genentech, 2026a |
| Brigatinib | 避免強效與中效誘導劑；rifampin 使 AUC 下降 80% | Takeda, 2026 |
| **Lorlatinib** | **禁忌**：10/12 位健康受試者與 rifampin 併用後出現嚴重肝毒性（50% 為 4 級 ALT／AST 上升）；開始 lorlatinib 前，要先停誘導劑達 3 個血漿半衰期 | Pfizer, 2026a |
| Crizotinib | 避免；rifampin 使 AUC 下降 84% | Pfizer, 2025 |
| Entrectinib | 避免強效與中效誘導劑；rifampin 使 AUC 下降 77% | Genentech, 2026b |
| Capmatinib | 避免強效與中效誘導劑；rifampicin 使 AUC 下降 67% | Novartis, 2026a |
| Tepotinib | 仿單以 carbamazepine（強效誘導劑）做試驗，藥動學無臨床顯著差異；rifampin 本身未列 | EMD Serono, 2025 |
| Selpercatinib | 避免強效與中效誘導劑；rifampin 使 AUC 下降 87% | Eli Lilly, 2026b |
| Repotrectinib | 避免強效與中效誘導劑 | Bristol-Myers Squibb, 2024 |
| Sotorasib | 避免強效誘導劑；rifampin 使 AUC 下降 51% | Amgen, 2025 |
| Larotrectinib | 避免；無法避免時劑量加倍 | Bayer, 2026 |

> [!WARNING]
> **TKI 病人被開 rifampin 時先停一下**
> 這是真實的病房錯誤：感染科或急診開了含 rifampin 的抗結核處方，沒有人想到病人正在吃 lorlatinib（禁忌，有嚴重肝毒性風險）或 osimertinib（暴露量大幅下降）。TB 處方（含 LTBI 的 4R、3HR；3HP、1HP 含 rifapentine，erlotinib 仿單也把 rifapentine 列為誘導劑）開立前要核對 TKI；專師不要自己停 rifampin、也不要自己改 TKI 劑量，聯絡主治醫師、感染科與藥劑部一起決定。LTBI 與 TB 的處方見 [irAE 章](00-shared/04-irae.md#21-結核病tb史與篩檢)第 2.1 節。

### 5.5 口服標靶藥的實務：漏服、嘔吐、管灌與居家安全

**這一段的結論先講：** 通則是「漏服不補吃、不加倍」，但各藥的細節不同（漏服的時間窗從 4 小時到 12 小時不等，entrectinib 吃完馬上吐還要重吃）。EGFR 陽性病人常在臥床、吞嚥困難或插管時開始 TKI，所以「這顆藥能不能磨粉、能不能打鼻胃管」是每週都會被問的問題；能不能分散，先查仿單，沒有仿單依據就會診藥劑部，不要自己壓碎或打開膠囊。下表整理美國仿單文字，台灣核准仿單可能不同（例如 afatinib 的空腹規定見 5.4）；口服抗癌藥的通用衛教流程見[化療基礎](00-shared/01-chemo-basics.md#145-口服抗癌藥)第 14.5 節。

| 藥物 | 漏服 | 吃完藥後嘔吐 | 吞不下或管灌 | 來源 |
|------|------|-------------|-------------|------|
| Osimertinib | 不補，下一劑照時間 | 仿單未訂 | 可：錠劑放入 60 mL 不含氣泡的水散成小塊後立即吞；鼻胃管用 15 mL 水；**不可壓碎、加熱、超音波** | AstraZeneca, 2026 |
| Gefitinib | 距下一劑 12 小時內不補 | 仿單未訂 | 可：錠劑放入 4–8 盎司水攪拌約 15 分鐘，立即喝下或由鼻胃管給 | AstraZeneca, 2023 |
| Erlotinib | 仿單未載 | 仿單未載 | 仿單未載，請藥師 | Alembic, 2024 |
| Afatinib | 距下一劑 12 小時內不補 | 仿單未訂 | 美國仿單未載 | Boehringer Ingelheim, 2025 |
| Dacomitinib | 不補、不加倍 | 不補、不加倍，下一劑照時間 | 美國仿單未載 | Pfizer, 2026b |
| Alectinib | 不補，下一劑照時間 | 不補 | **膠囊整顆吞，不可打開或溶解** | Genentech, 2026a |
| Brigatinib | 不補 | 不補 | 整顆吞，不可壓碎或咀嚼 | Takeda, 2026 |
| Lorlatinib | 想起來就補，除非距下一劑 <4 小時 | 不補 | 整顆吞，不可咀嚼、壓碎或分割；破損或裂開的錠劑不要吞 | Pfizer, 2026a |
| Crizotinib | 想起來就補，除非距下一劑 <6 小時 | 不補 | 膠囊整顆吞，不可咀嚼、壓碎或分割 | Pfizer, 2025 |
| Capmatinib | 不補 | 不補 | 整顆吞，不可剝開、壓碎或咀嚼 | Novartis, 2026a |
| Tepotinib | 同一天想起來就補，除非距下一劑 <8 小時 | 下一劑照時間 | 可：30 mL 不含氣泡的水中攪拌分散（不壓碎），立即或 1 小時內喝下，再用 30 mL 水沖杯；仿單另有鼻胃管步驟 | EMD Serono, 2025 |
| Selpercatinib | 除非距下一劑超過 6 小時，否則不補 | 不補 | 只有 40 mg 錠劑可分散，經口、胃造口或鼻胃管給；膠囊與其他錠不可壓碎 | Eli Lilly, 2026b |
| Entrectinib | 補，除非距下一劑 <12 小時 | **剛吃完立刻吐，要重吃一劑** | 膠囊可製成懸液，經口或鼻胃管 | Genentech, 2026b |
| Repotrectinib | 跳過，照下一劑 | 跳過 | 整顆吞，不可打開、咀嚼、壓碎或溶解 | Bristol-Myers Squibb, 2024 |
| Sotorasib | 漏服超過 6 小時就跳過，隔天照常吃，不補 | 不補 | 可：錠劑放入 120 mL 不含氣泡的水（不壓碎）攪拌約 3 分鐘，立即或 2 小時內喝下 | Amgen, 2025 |
| Dabrafenib | 距下一劑 <6 小時不補 | 不補 | 膠囊不可打開、壓碎或折斷；空腹服用 | Novartis, 2026b |

**居家與衛教重點**

- **服藥提醒與順從度**：每次回診問「上個月有沒有漏服？怎麼處理？」，並請病人說出自己的漏服與嘔吐規則（做法見化療基礎 14.5）；規則因藥而異，衛教單要寫該藥的版本，不要發通用版。
- **症狀日誌**：皮疹、腹瀉、水腫、喘、咳嗽、發燒，寫下日期與嚴重度；新的喘或咳嗽要當天聯絡（ILD，見 6.1）。
- **交互作用**：不要自行加中草藥、保健食品；任何新處方先給專師或藥師核對（誘導劑、抑酸劑，見 5.4 上表）。
- **安全處理與丟棄**：藥放原包裝、避免兒童與寵物接觸、剩藥交回藥局；處理藥物與病人體液的防護，依院內規範與藥劑部衛教單（見化療基礎第 10 節與 14.5）。

---

## 6. 副作用評估與處置

通用原則：用 CTCAE v5.0 分級 → 依級數決定**繼續、暫停、減量或永久停藥**。化療的骨髓抑制、噁心嘔吐見 [支持性照護](00-shared/03-supportive-care.md)，外滲處置見 [化療基礎與劑量計算](00-shared/01-chemo-basics.md#9-血管外滲extravasation) 第 9 節；免疫治療見 [irAE 章](00-shared/04-irae.md)。

### 6.1 EGFR TKI

| 副作用 | 處置重點 |
|-------|---------|
| 痤瘡樣皮疹（acneiform rash） | G1：外用低效類固醇（hydrocortisone 2.5%）或 clindamycin 1%。G2：加口服 doxycycline 100 mg BID 或 minocycline 100 mg BID。G3：暫停，恢復門檻與減量方式依各藥仿單，規則如下。預防：保濕、防曬，afatinib／dacomitinib 可預防性口服 doxycycline。**G3 的各藥規則（美國仿單 Gilotrif 2025-11-13、Vizimpro 2026-06-23、Iressa 2023-02-28、Tagrisso 2026-09 版；台灣以核准仿單為準）：** afatinib、dacomitinib、gefitinib 要恢復到 ≤G1 才能再用，afatinib 每次比原劑量少 10 mg/day，dacomitinib 恢復後減量，gefitinib 沒有較低劑量、仍用 250 mg；osimertinib 最多暫停 3 週，3 週內恢復到 ≤G2 可用 80 或 40 mg 重新開始，3 週內沒改善就永久停藥。G2 也有暫停條件：afatinib 的 G2 皮膚反應持續超過 7 天或無法忍受，dacomitinib 的持續性 G2，都要暫停（dacomitinib 恢復到 ≤G1 後可用原劑量，再發才減量） |
| 甲溝炎（paronychia） | 稀釋白醋泡手腳、外用類固醇或抗生素；肉芽組織可用硝酸銀；避免剪太短、穿太緊的鞋 |
| 腹瀉 | Loperamide 首劑 4 mg，之後每次稀便 2 mg，每日最多 16 mg；補充水分電解質；G3 以上暫停；afatinib 的 G2 經止瀉藥仍持續 ≥2 天、dacomitinib 出現 G2 即需暫停至 ≤G1，再依仿單恢復或減量（afatinib 最常見） |
| 口腔炎 | 溫和漱口水、避免刺激食物；G3 暫停 |
| 間質性肺病（ILD） | AURA3 中 osimertinib 的 ILD 類事件約 4%。新發或惡化的咳嗽、喘、發燒：**立即暫停**、安排胸部 CT、排除感染；確診 ILD 通常永久停藥，給予類固醇 |
| QTc 延長（osimertinib） | AURA3 中約 4%。開始前與定期做心電圖；QTc >500 ms 暫停，恢復後減量；同時矯正 K、Mg |
| 左心室射出率下降（osimertinib） | 發生率約 3.8%（併用化療的 FLAURA2 約 9%）。**單藥**：有心臟危險因子者，開始前與治療中定期評估 LVEF（心臟超音波）；**併用 pemetrexed／鉑類化療**：所有病人開始前與治療中都要評估 LVEF。治療中出現心臟症狀時隨時評估；出現有症狀心衰竭永久停藥 |

> [!IMPORTANT]
> **皮疹不是壞事**
> EGFR TKI 的皮疹和療效有相關性，臨床上常有病人想自行停藥。衛教重點是「預防 ＋ 早期處理」，不是停藥。真正要立刻停藥、立刻回診的是**新的喘或咳嗽**（可能是 ILD）。

### 6.2 ALK／ROS1 TKI

| 藥物 | 特殊副作用 | 處置 |
|------|-----------|------|
| Alectinib | 肌肉痛與 CK 上升、心搏過緩、膽紅素上升、水腫、光敏感、體重增加 | 定期驗 CK、肝功能；定期量心跳與血壓；有症狀的心搏過緩即暫停（不設心跳門檻；無症狀者不需調整），並檢查併用的降心率藥與降血壓藥；至無症狀或心跳 ≥60 再用：相關併用藥已停用或調整則原劑量，否則減一級；危及生命且無相關併用藥則永久停藥 |
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
| Datopotamab deruxtecan | 口腔炎（約 56%）、ILD（約 7–9%） | 每日口腔照護；依仿單預防性使用含類固醇漱口水（dexamethasone 0.1 mg/mL 含漱，每日 4 次及需要時），輸注全程口含冰塊或冰水；ILD 處置同上 |
| Zongertinib（HER2） | 腹瀉（54%）、肝毒性（27%，含藥物性肝損傷）、左心室射出率下降（6%）、ILD／肺炎（美國仿單合併安全族群 2.1%，含 1 例死亡；Beamion LUNG-1 2025 年報告的三個 cohort 未見藥物相關 ILD） | 開始前、前 12 週每 2 週、之後每月驗肝功能；開始前與定期評估 LVEF；新發喘、咳、發燒依 ILD 處置（G2 暫停至緩解後減量，G3 以上永久停藥） |

### 6.4 Amivantamab（± lazertinib）

| 副作用 | 處置 |
|-------|------|
| 輸注反應（infusion-related reaction, IRR） | MARIPOSA 中 63%，多發生在**第一劑**：第一劑拆成兩天給（D1、D2）；給藥前 antihistamine、antipyretic、glucocorticoid；美國仿單自 2025 年 9 月起，第一劑前 2 天（D−2、D−1）另加口服 dexamethasone 8 mg BID，D1 給藥前 1 小時再口服 8 mg，原本 D1 的 IV dexamethasone 20 mg 照給，所以要提前 2 天讓病人開始吃藥。依據是 **SKIPPirr**（Spira et al., 2025；第 2 期單臂研究，osimertinib 與含鉑化療後惡化、靜脈 amivantamab ＋ lazertinib 的病人，口服 dexamethasone 8 mg BID 於 C1D−2、C1D−1 及 C1D1 早上共 5 劑）：第一劑輸注反應 22.5%（9/40），歷史對照 67.4%；發生時暫停、處理症狀、降速再給。**皮下劑型**的全身性給藥反應約 13%，明顯低於靜脈劑型約 66%（PALOMA-3，美國 FDA 核准資料），台灣 2026 年已有藥證 |
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
- **結核病（TB）再活化**：台灣是結核病中度流行地區，肺癌病人本來就是 TB 的高風險族群。台大醫院團隊的回溯世代（配對後）顯示，肺癌病人用 ICI 的 TB 發生率高於用 TKI（每 10 萬人年 2,298 對 412；校正後風險比 6.29，95% CI 1.23–32.09）；前瞻世代中 IGRA 轉陽的比例 ICI 組 18%、TKI 組 0%（Chen et al., 2024）。這是觀察性研究，兩組的基線不同（ICI 組鱗癌、化療與全身性類固醇較多），不能直接說是 ICI 造成；機轉與其他研究的爭議見 [irAE 章](00-shared/04-irae.md#21-結核病tb史與篩檢)第 2.1 節，文獻回顧也把「ICI 病人的 TB 要怎麼處理」列為尚待回答的問題（Anastasopoulou et al., 2019）。
  - **開始 ICI 前**：問 TB 病史（治療是否完成）與接觸史，看胸部影像並與舊片比較；要不要加驗 IGRA 依院內感染科流程。
  - **ICI 期間**：新的咳嗽、發燒、盜汗、體重下降、新的空洞或浸潤，要想到 TB（與腫瘤惡化或免疫性肺炎很難分），送痰檢；不要只當成腫瘤惡化。
  - **準備用長期類固醇或 infliximab、tocilizumab 等處理 irAE 前**：先做 TB 基線評估，細則與 LTBI 處方見 irAE 章 2.1 與第 4 節。
  - **治療 TB 時別忘了 TKI**：rifampin 與多數 TKI 有交互作用，lorlatinib 是禁忌（見 5.4 的表）。
- 處置流程見 [irAE 章](00-shared/04-irae.md)。

### 6.7 放射治療相關

| 副作用 | 時間 | 處置 |
|-------|------|------|
| 放射性食道炎 | 放療第 2–3 週開始 | 黏膜保護劑、止痛（含 viscous lidocaine）、PPI、營養諮詢；吞嚥痛嚴重時評估管灌 |
| 放射性肺炎 | 放療後 1–6 個月 | 排除感染；有症狀者 prednisone 約 1 mg/kg/day，慢慢減量（數週） |

### 6.8 抗血管新生藥物：bevacizumab 與 ramucirumab

**這一段的結論先講：** 兩種藥共同的毒性是高血壓、蛋白尿、出血、傷口癒合不良、GI 穿孔、動脈血栓與 PRES。專師每次給藥前要做的事很固定：量血壓、驗尿試紙、問咳血與出血、問近期有沒有手術或侵入性處置（Genentech, 2025b；Eli Lilly, 2026a）。Bevacizumab 只用於非鱗狀 NSCLC（見第 8 節的警示）。

| 毒性 | Bevacizumab（Avastin 仿單） | Ramucirumab（Cyramza 仿單） | 給藥前與病房重點 |
|------|---------------------------|---------------------------|----------------|
| 高血壓 | 3–4 級 5%–18%；每 2–3 週量血壓；嚴重且藥物控制不良時暫停，控制後恢復；高血壓危象或腦病變永久停藥 | 所有等級 11%–26%、3–5 級 6%–15%；嚴重時暫停至控制；無法控制或高血壓危象、腦病變永久停藥 | 每次給藥前量血壓；血壓門檻依院內（仿單未訂數值）；開始前先把原有高血壓控制好 |
| 蛋白尿 | 以尿試紙連續追蹤；試紙 ≥2+ 再收 24 小時尿；**≥2 g/24 小時暫停，降到 <2 g 才恢復**；腎病症候群永久停藥 | 以尿試紙或 UPCR 追蹤；**≥2 g/24 小時暫停**，降到 <2 g 後減一階劑量恢復（10 → 8 mg/kg；再發 8 → 6 mg/kg）；>3 g/24 小時或腎病症候群永久停藥 | 每次給藥前驗尿試紙。Bevacizumab 仿單指出 UPCR 與 24 小時尿蛋白的相關性差（相關係數 0.39），所以 UPCR 高時仍以 24 小時尿為準 |
| 手術與傷口 | **擇期手術前至少 28 天停藥**；大手術後至少 28 天且傷口癒合才可給；傷口癒合併發症時暫停至癒合；壞死性筋膜炎永久停藥 | **擇期手術前 28 天停藥**；大手術後至少 2 週且傷口癒合才可恢復 | 排任何手術、侵入性牙科或其他處置前先通知主治醫師；植入式血管通路算不算「手術」，仿單未說明，由主治醫師與外科決定 |
| GI 穿孔 | 0.3%–3%；任何等級永久停藥（氣管食道瘻管同） | <1%–2%；永久停藥 | 新的腹痛、嘔吐、發燒、腹部僵硬立即通知，安排腹部影像 |
| 動脈血栓（ATE） | 嚴重 ATE 永久停藥；化療併用下 3–5 級 ATE 約 5%；4 級靜脈血栓（含肺栓塞）也停藥 | 所有等級 1%–3%；任何 ATE 永久停藥 | 胸痛、單側無力、言語不清、視力突變當作急症 |
| 出血 | **近期咳血 ≥1/2 茶匙（2.5 mL）紅血：暫停**；3–4 級出血永久停藥 | 所有等級 13%–55%、3–5 級 2%–5%；3–4 級出血永久停藥 | 問咳血量與次數、鼻出血、黑便；分級與首要處置見 7.8 |
| PRES | <0.5%；永久停藥 | <0.1%；永久停藥 | 頭痛、癲癇、視覺異常、意識混亂：急症，安排腦部 MRI |
| 輸注反應 | 輕者降速，嚴重者永久停藥 | 每次輸注前給 IV H1 阻斷劑；曾有 1–2 級反應者加 dexamethasone 與 acetaminophen；1–2 級降速 50%，3–4 級永久停藥 | 反應處置見[急症章](00-shared/02-oncologic-emergencies.md#10-輸注反應過敏反應與過敏性休克)第 10 節 |

**給藥前檢核（每次）**

1. 血壓（坐姿，使用適當大小的袖帶）。
2. 尿液試紙；≥2+ 或比上次明顯升高，收 24 小時尿。
3. 咳血、鼻出血、黑便、傷口滲血；抗凝血藥與 NSAID 使用狀況。
4. 近期或預定的手術、拔牙、侵入性處置（停藥 28 天的規則）。
5. 腹痛、發燒（GI 穿孔）；胸痛或肢體無力（ATE）；頭痛、視力變化（PRES）。

> [!TIP]
> **Anti-VEGF 像關掉腫瘤的供水管線**
> 腫瘤需要新生血管送養分，VEGF 是蓋水管的指令。把指令關掉，腫瘤斷糧；但全身其他血管也一起受影響：血管張力改變所以高血壓，腎絲球的過濾屏障受影響所以蛋白尿，新生血管不足所以傷口不好癒合，血管變脆所以容易出血、穿孔，也比較容易形成血栓。

> [!IMPORTANT]
> **考試重點：bevacizumab 與 ramucirumab 的三個數字**
> - 蛋白尿 **≥2 g/24 小時暫停**；試紙 ≥2+ 要收 24 小時尿。
> - **擇期手術前 28 天停藥**；bevacizumab 大手術後至少 28 天，ramucirumab 至少 2 週，且傷口癒合。
> - 近期咳血 ≥1/2 茶匙（2.5 mL）暫停 bevacizumab；鱗狀細胞癌不用 bevacizumab。

> [!NOTE]
> **這兩個藥在健保的位置（115/10/22 版）**
> Bevacizumab 的肺癌給付只有兩種：與 erlotinib 併用（9.29 第 2 項 114/4/1；9.37 第 5 項 114/3/1，限 7.5 mg/kg）以及與 atezolizumab、carboplatin、paclitaxel 併用（9.37 第 7 項，條號最新修訂 114/10/1）。Ramucirumab 在 9.92（110/5/1）只給付肝細胞癌，肺癌的 docetaxel ＋ ramucirumab 原文未見給付；細節見 9.1 與 9.4。

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
| 免疫治療 | TSH、free T4（約每 6 週）、血糖、皮質醇（有症狀時）；開始前問 TB 病史與接觸史並看胸部影像（6.6） |
| Anti-VEGF（bevacizumab、ramucirumab） | 血壓、尿液試紙、咳血與出血、近期手術或侵入性處置（6.8） |
| B 型肝炎 | 開始任何全身性抗癌治療前驗 HBsAg、anti-HBc、anti-HBs；HBsAg 陽性要會診並預防性抗病毒（見 [化療基礎](00-shared/01-chemo-basics.md#6-b-型肝炎篩檢與預防性抗病毒)） |
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
  Dexamethasone ＋ olanzapine，D2–4（延遲性嘔吐預防，依止吐規範）
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
  - CR：所有目標病灶消失，且所有病理性淋巴結短軸縮小到 <10 mm。
  - PR：目標病灶直徑總和比基準值（baseline）減少 ≥30%。
  - PD：直徑總和比最小值增加 ≥20% 且絕對值增加 ≥5 mm，或出現新病灶。
  - SD：介於 PR 與 PD 之間。
- **免疫治療的假性惡化（pseudoprogression）**：少數病人影像先變大後縮小，臨床穩定時可依 iRECIST 在 4–8 週後再確認。
- **晚期病人**：治療中每 2–3 個週期（約 6–9 週）做影像評估。
- **根治性治療後**：手術（± 化療）治療的第 I–II 期：前 2–3 年每 6 個月做胸部 CT，之後每年低劑量胸部 CT；放療治療的第 I–II 期或第 III 期（如同步化放療後）：前 3 年每 3–6 個月、之後 2 年每 6 個月，再改為每年（NCCN）。

### 7.7 Tarlatamab 病房實務（C1D1、C1D8 的醫囑、監測與出院衛教）

**這一段的結論先講：** Tarlatamab 的 CRS 在安全性合併族群是 57%（268/473；1 級 39%、2 級 15%、3 級 1.7%、4 級 0.2%），CRS 病人中 73% 發生在第一劑之後，從最近一次給藥起算的中位發生時間是 16 小時；ICANS 的徵象約 10%，從第一劑起算的中位發生時間是 16 天（範圍 1–862 天），可以在數週後才出現（Amgen, 2026）。所以安全重點有三個：**前兩劑照仿單做好前置用藥與水化並在院內監測；出院前把症狀教給病人與照顧者；之後每一劑也要留觀，不是只有前兩劑**。

> [!IMPORTANT]
> **台灣狀態：藥證、健保、院內處方集是三件事**
> - **藥證**：安泰適（衛部菌疫輸字第 001281／001282 號），2025-02-26 核准，適應症為含鉑化療期間或之後惡化的 ES-SCLC（TFDA 開放資料 2026-10-27 版）。
> - **健保**：115/10/22 版《藥品給付規定》第 9 節原文未見 tarlatamab，**無健保給付**（見 9.5）。
> - **院內處方集**：依各院藥事委員會；病人要用之前，先確認院內有沒有進藥。

> [!CAUTION]
> **待核對：台灣核准仿單的監測時間**
> 美國仿單在 2026-07 版（DailyMed 第 7 版）寫的是 C1D1、C1D8 在醫療機構監測 22–24 小時，2026-09 版（第 8 版，生效日 2026-09-11）改為自輸注開始 6–8 小時，並新增第 2、9 天的評估（Amgen, 2026）。本手冊沒有取得台灣核准仿單的文字，也不知道台灣仿單是否已隨之修訂；不少醫院的 protocol 可能仍沿用 22–24 小時的過夜觀察。實際留觀時間以台灣仿單與院內 protocol 為準，下表是美國 2026-09 版。

**給藥日程、前置用藥與輸注後觀察（美國仿單 2026-09 版；Amgen, 2026）**

| 日程 | 劑量 | 前置用藥與水化 | 輸注後觀察與其他 |
|------|------|--------------|----------------|
| C1D1 | 1 mg | 輸注前 1 小時內 dexamethasone 8 mg IV（或等效）；輸注完立刻 NS 1 L IV，2–4 小時滴完；確保輸注前已充分水化 | 自輸注開始在醫療機構監測 6–8 小時；自輸注開始共 48 小時內，停留在 1 小時內可到醫療機構處並有照顧者陪同；第 2 天評估（含生命徵象） |
| C1D8 | 10 mg | 同 C1D1 | 同 C1D1；第 9 天評估（含生命徵象） |
| C1D15 | 10 mg | 仿單的前置用藥只列 C1D1、C1D8 | 輸注後觀察 6–8 小時；除非先前出現 2 級以上 CRS、ICANS 或神經毒性，不需延長留院 |
| C2D1、D15 | 10 mg | 同上 | 6–8 小時 |
| C3、C4 的 D1、D15 | 10 mg | 同上 | 3–4 小時 |
| C5 起的 D1、D15 | 10 mg | 同上 | 2 小時 |

- **輸注方式**：1 小時 IV 輸注，使用可程式、可上鎖、非彈性囊式且有警示的輸注幫浦；用 NS 沖管；仿單不建議使用封閉式藥品傳輸裝置（CSTD）（Amgen, 2026）。
- **抽血**：每次給藥前驗 CBC、肝酵素與 bilirubin，一直到 C5D15；從第 6 週期起，每個週期 D1 驗一次，臨床需要時更密。其他（Na、Cr、血糖）屬院內常規，SCLC 病人要特別留意低血鈉（見第 8 節）。
- **耽誤劑量後怎麼重新開始**：C1D1 之後間隔 ≤14 天，直接給 10 mg；>14 天，重新給 1 mg，耐受再於 1 週後給 10 mg。C1D8 之後 ≤21 天給 10 mg，>21 天重新從 1 mg 開始。C1D15 與之後的每 2 週給藥，間隔 ≤28 天給 10 mg，>28 天重新從 1 mg 開始。重新開始時，C1D1／C1D8 的前置用藥與監測要再做一次（Amgen, 2026）。
- **不減量**：仿單不建議減量，只有暫停或永久停藥。

**CRS 的分級與處置**（ASTCT 分級，Lee et al., 2019，見[腫瘤急症章](00-shared/02-oncologic-emergencies.md#9-細胞激素釋放症候群crs與神經毒性icans)第 9 節；下表為美國仿單 2026-09 版）

| 分級 | 定義重點 | 處置 | Tarlatamab 的下一步 |
|------|---------|------|-------------------|
| 1 | 發燒 ≥38°C，沒有低血壓或缺氧 | 退燒藥（如 acetaminophen）；可考慮 dexamethasone 4–10 mg PO／IV，之後依標準減量 | 暫停到症狀緩解，下次排定劑量恢復 |
| 2 | 發燒；低血壓對輸液有反應、不需升壓劑，和（或）低流量鼻導管缺氧 | 住院至少 24 小時，心電圖監測與血氧監測；氧氣與輸液；可考慮 dexamethasone 8 mg PO／IV；可考慮 tocilizumab | 暫停到緩解；恢復下一劑時，自輸注開始監測 6–8 小時 |
| 3 | 發燒；需要一種升壓劑，和（或）高流量鼻導管（>6 L/min）或面罩 | 加護病房；dexamethasone 8 mg IV q8h，最多 3 劑；升壓劑與高流量氧氣；建議 tocilizumab | 暫停到緩解；下一劑前再給 C1D1／C1D8 的前置用藥；恢復時監測 22–24 小時；**再發 3 級永久停藥** |
| 4 | 需要多種升壓劑（vasopressin 除外），和（或）需要正壓通氣 | 加護病房，同 3 級處置，建議 tocilizumab | **永久停藥** |

> [!WARNING]
> **退燒藥、類固醇與 tocilizumab 會壓住發燒**
> Tarlatamab 的前兩劑本來就有 dexamethasone 前置用藥。已經給過退燒藥、類固醇或 tocilizumab 的病人，發燒可能被壓住：沒發燒不代表沒有 CRS，分級要改看低血壓和缺氧（見急症章第 9 節）。每次生命徵象都要同時看血壓和血氧，不是只看體溫。

**ICANS 與神經毒性**（ICE 評分，見急症章第 9 節；下表為美國仿單 2026-09 版）

| 分級 | 定義重點 | 處置 | Tarlatamab 的下一步 |
|------|---------|------|-------------------|
| 1 | ICE 7–9 分 | 支持性照護 | 暫停到緩解，下次排定劑量恢復 |
| 2 | ICE 3–6 分，和（或）輕度嗜睡、聲音可喚醒 | Dexamethasone 8–10 mg PO／IV，可每 12 小時重複；惡化時改 methylprednisolone 1 mg/kg IV q12h；神經科會診 | 暫停到緩解；下一劑自輸注開始監測 22–24 小時 |
| 3 | ICE 0–2 分、只有觸覺才喚醒、很快緩解的癲癇、局部腦水腫 | 加護病房；dexamethasone 10 mg IV q6h 或 methylprednisolone 1 mg/kg IV q12h；視需要插管保護氣道；持續 3 級以上時每 2–3 天重複腦部影像 | 暫停到緩解；**7 天內未改善到 1 級以下，或再發 3 級，永久停藥**；下一劑監測 22–24 小時 |
| 4 | 無法喚醒（ICE 0）、昏迷、持續癲癇、瀰漫性腦水腫 | 加護病房；高劑量類固醇（例如 methylprednisolone 1,000 mg/day 分次 IV 共 3 天）；癲癇持續狀態依院內流程 | **永久停藥** |

- **Tocilizumab**：Imdelltra 仿單只寫「建議 tocilizumab」，沒有給 mg 數。Actemra 仿單針對 CAR-T 引起的重度或危及生命的 CRS：體重 ≥30 kg 者 8 mg/kg IV 輸注 60 分鐘，無改善可再給最多 3 劑，每劑至少間隔 8 小時，單次不超過 800 mg（Genentech, 2025a）。Tarlatamab 的 CRS 沿用此劑量屬於參考，由主治醫師依院內 CRS 流程決定。
- **ICANS 主要靠類固醇**：tocilizumab 不易通過血腦屏障，對 ICANS 不是主力（見急症章第 9.3 節）。
- **第一個徵象就要停**：輸注中出現 CRS 或神經症狀，立刻停止輸注（Amgen, 2026）。

**什麼時候暫停、什麼時候永久停藥（其他毒性，美國仿單 Table 7）**

| 毒性 | 暫停 | 永久停藥 |
|------|------|---------|
| 3 級嗜中性球低下 | 暫停到 ≤2 級，可考慮 G-CSF | 3 週內沒恢復到 ≤2 級 |
| 4 級嗜中性球低下 | 暫停到 ≤2 級，可考慮 G-CSF | 1 週內沒恢復；再發 4 級 |
| 嗜中性球低下性發燒 | 暫停到嗜中性球恢復到 ≤2 級且退燒 | — |
| Hb <8 g/dL | 暫停到 ≥8 g/dL | — |
| 血小板 3–4 級 | 暫停到 ≤2 級且沒有出血 | 3 週內沒恢復；再發 4 級 |
| 感染 | 階梯劑量期間任何等級感染都暫停到痊癒；3 級感染暫停到 ≤1 級 | 4 級感染 |
| 肝毒性 | 3 級 ALT／AST／bilirubin 上升，暫停到 ≤1 級 | 4 級；或 AST／ALT >3 × ULN 且 bilirubin >2 × ULN 且無其他原因 |
| 其他 3–4 級不良反應 | 暫停到 ≤1 級或基線 | 28 天未緩解時考慮永久停藥；4 級可考慮永久停藥 |

**住院或觀察醫囑範本（C1D1、C1D8，概念範本；括號內標示出處）**

```text
[Tarlatamab C1D1（1 mg）／C1D8（10 mg）— 範本，依院內 protocol 調整]
入院前或入院時
  - 確認：ES-SCLC 含鉑化療期間或之後惡化；同意書（CRS、ICANS 加框警語）；
          病人與照顧者已衛教；48 小時內可停留在 1 小時內可到院處且有人陪同（仿單）
  - 感染篩檢：階梯劑量期間有感染要先治療到痊癒再給（仿單）；生育年齡女性確認未懷孕
  - Lab：CBC/DC、AST/ALT、total bilirubin（仿單，每次給藥前）；Na、K、Cr、glucose（院內）
  - 基線：ECOG、生命徵象、神經學檢查與 ICE 評分（0–10）、SpO2（室內空氣）
給藥日
  - 輸注前 1 小時內：Dexamethasone 8 mg IV（仿單）
  - 輸注前確認水化良好（仿單）
  - Tarlatamab 1 mg（C1D1）／10 mg（C1D8）IV 輸注 1 小時，可程式、可上鎖、非彈性囊式、
    有警示的輸注幫浦，250 mL 袋 250 mL/hr；輸注後 NS 沖管；不用 CSTD（仿單）
  - 輸注結束立刻：NS 1,000 mL IV over 2–4 hr（仿單）
  - 生命徵象、SpO2、體溫、ICE／神經學檢查：輸注前、中、後定時，發燒或症狀時加密（頻率依院內 CRS protocol）
  - 備用：acetaminophen（劑量依院內）、氧氣、急救設備；確認院內藥局 tocilizumab 可立即取得
  - 發燒 ≥38°C、低血壓、缺氧、任何神經症狀：停止輸注（若尚在輸注）→ 通知醫師 → 依 CRS／ICANS 分級處置；
    發燒時抽血液培養（嗜中性球低下依 FN 流程）
  - 自輸注開始監測 6–8 小時（美國 2026-09 版仿單；台灣仿單與院內規定可能不同）
  - 離院條件：無 CRS／神經症狀、生命徵象穩定；離院前口頭與書面衛教，照顧者回覆示教
隔天
  - C1D2／C1D9：生命徵象與症狀評估（門診、電話或訪視，依院內，仿單）
```

**SOAP 範例（假設個案：C1D8 輸注結束後，監測期間出現發燒）**

```text
情境：62 歲男性，ES-SCLC，一線 carboplatin ＋ etoposide ＋ atezolizumab 後惡化，今天 C1D8 tarlatamab 10 mg，
      自輸注開始第 5 小時。
S：畏寒、頭痛，覺得「有點熱」；沒有喘、胸痛，能正常對話。
O：BT 38.4°C（輸注前 36.9°C），HR 108，BP 112/68 mmHg（基線 124/74），RR 18，SpO2 96%（室內空氣）。
   ICE 10/10，能寫完整一句話。NS 1 L 輸注中，尿量正常。昨日 CBC：ANC 3,400/µL。
A：1. CRS Grade 1（發燒，無低血壓、無缺氧；ASTCT）；ICANS 無（ICE 10/10）
   2. ES-SCLC，tarlatamab C1D8，仍在仿單監測期內
P：1. 通知主治醫師；繼續留院觀察，離院時間由主治醫師決定
   2. Acetaminophen 退燒；續 NS；dexamethasone 4–10 mg 是仿單 1 級的「可考慮」選項，由主治醫師決定
   3. 生命徵象與體溫、ICE 與神經學檢查加密（頻率依院內）；一旦低血壓或缺氧，升級為 2 級處置
      （住院至少 24 小時、心電圖與血氧監測）
   4. 抽血液培養、CBC、CRP、肝功能、電解質
   5. 下一次排定劑量（C1D15）：1 級緩解後依排程恢復（仿單）；告知病人與照顧者
   6. 衛教：發燒、冷顫、頭暈、意識或說話改變，立即告知護理人員
```

**出院衛教（病人與照顧者都要聽，回覆示教）**

| 要教的事 | 內容 | 依據 |
|---------|------|------|
| 留在醫院附近 | C1D1、C1D8 自輸注開始 48 小時內，停留在 1 小時內可到醫療機構處，且有照顧者陪同 | 仿單 |
| CRS 症狀 | 發燒（≥38°C，即 100.4°F）、畏寒、頭痛、暈、血壓低、心跳快、喘、噁心嘔吐、疲倦；出現就立即就醫或回院 | 仿單 5.1 與病人說明 |
| ICANS 與神經症狀 | 意識混亂、定向感變差、嗜睡、說話或寫字困難、手抖、手腳無力或麻木、走路不穩、癲癇、頭痛；**可在數週後才出現**（中位第一劑後 16 天） | 仿單 5.2 |
| 開車與危險作業 | 仿單寫：出現神經症狀時，要避免開車與危險作業，直到症狀消失；仿單沒有訂固定的小時數 | 仿單 5.2 |
| 感染 | 感染（肺炎、泌尿道感染、COVID-19 等）很常見，發燒時不要只當成 CRS；有發燒就聯絡 | 仿單 5.4 |
| 避孕 | 有生育可能的女性，治療期間與最後一劑後 2 個月使用有效避孕 | 仿單 5.7 |
| 聯絡方式 | 寫下病房或腫瘤個管師的電話與夜間急診流程；帶藥物清單就醫 | 院內 |

> [!NOTE]
> **「不能開車的時間窗」仿單沒有訂，由院內決定**
> 仿單的說法是「神經症狀消失之前」。很多醫院會在 C1D1、C1D8 後的 48 小時（與留在醫院附近的 48 小時一致）請病人由他人接送，這是院內的保守作法，不是仿單的固定規定；本手冊沒有查到訂有固定天數的指引。實際請依院內衛教單。

> [!TIP]
> **階梯劑量像「先小火、再中火」**
> 1 mg 先讓 T 細胞「試試水溫」，一週後再給 10 mg 全量；前兩劑的 dexamethasone 與水化，像在爐子旁先放好一盆水。最容易冒煙（CRS）的就是前兩劑，所以這兩天要有人在爐邊守著；火開穩之後，每一劑還是要看著，只是守的時間愈來愈短（8 小時 → 4 小時 → 2 小時）。

### 7.8 呼吸困難、咳嗽與咳血

**這一段的結論先講：**

- **呼吸困難以病人自己打的 0–10 分為準**，不是只看呼吸速率與血氧（Hui et al., 2020）。
- 先找並處理可逆原因；風扇對著臉有效；**血氧正常（靜息 SpO₂ ≥90%）不給氧**；非藥物措施不夠時，用低劑量規則口服 morphine，並同時開緩瀉劑。藥物劑量與完整階梯見[支持性照護](00-shared/03-supportive-care.md#123-呼吸困難)第 12.3 節。
- **咳嗽**：先處理原因，再依階梯用藥；肺癌咳嗽的證據品質低，指引建議採逐步升級的方式（Molassiotis et al., 2017）。
- **咳血**：量不是唯一標準，氣道與血行動力學優先；大咳血是急症（見第 8 節與下方）。

**護理的呼吸評估（每班或有症狀時）**

| 項目 | 怎麼評估 | 為什麼 |
|------|---------|--------|
| 病人自述 | 0–10 分數字量表，分「休息時」與「活動時」，問最近 24 小時最嚴重的程度 | 呼吸困難是主觀感受，自述與血氧常不一致（Hui et al., 2020） |
| 客觀徵象 | 呼吸速率、休息與走動後 SpO₂、輔助肌使用、能否說完整句子、意識 | 判斷嚴重度與是否需要急救 |
| 聽診與叩診 | 單側呼吸音減弱加叩診濁音＝積水；局部喘鳴＝氣道阻塞；吸氣性喘鳴要通知醫師 | 找可逆原因 |
| 痰與咳血 | 痰量、顏色、有無血；咳血用杯子估量並記錄次數 | 咳血分級（下方） |
| 伴隨症狀 | 發燒、胸痛、下肢腫脹、體重、焦慮 | 感染、肺栓塞、心因性因素 |
| 目前的治療 | EGFR TKI、ICI、T-DXd 等藥物，近期放療，anti-VEGF，抗凝血藥 | 藥物性或放射性肺炎、出血風險 |

**肺癌病人喘的可逆原因檢核表**

| 原因 | 線索 | 下一步 |
|------|------|--------|
| 惡性肋膜積水 | 患側呼吸音減弱、叩診濁音、X 光或超音波 | 見 8.1 |
| 中央氣道阻塞或腫瘤增大 | 局部或吸氣性喘鳴、肺塌陷、同一肺葉反覆肺炎 | 胸部 CT、支氣管鏡；與主治醫師和放射腫瘤科討論 |
| 藥物性或放射性肺炎（ILD） | 新的乾咳、喘、發燒、CT 毛玻璃影；用 EGFR TKI、ICI、T-DXd、Dato-DXd，或放療後 1–6 個月 | 暫停可疑藥物，見 6.1、6.3、6.6、6.7 與 [irAE 章](00-shared/04-irae.md) |
| 感染（含阻塞性肺炎、PJP、TB） | 發燒、痰變色；嗜中性球低下、長期類固醇 | [急症章](00-shared/02-oncologic-emergencies.md#1-發燒性嗜中性球低下)第 1 節；TB 見 6.6 |
| 肺栓塞 | 突發喘、胸痛、心跳快 | [支持性照護](00-shared/03-supportive-care.md#7-癌症相關靜脈血栓vte)第 7 節 |
| SVC 症候群、心包膜積液 | 臉頸腫；低血壓、頸靜脈怒張 | 本章第 8 節 |
| 貧血 | 倦怠、活動後喘 | [支持性照護](00-shared/03-supportive-care.md#10-化療相關貧血血小板低下與輸血)第 10 節 |
| COPD 惡化、心衰竭、焦慮 | 原有疾病、水腫、情緒 | 依內科處置 |

**氧氣、風扇與 opioid：證據在哪**

| 措施 | 重點 | 依據 |
|------|------|------|
| 氧氣 | 非低血氧的難治性呼吸困難，氧氣 2 L/min 對比室內空氣 7 天，早晚喘的分數沒有差別（早上下降 0.9 對 0.7 分，P = .504；239 人）；ESMO 對靜息 SpO₂ ≥90% 不建議姑息性氧氣 | Abernethy et al., 2010；Hui et al., 2020 |
| 風扇 | 手持風扇對著臉，不論血氧高低都可以用，成本低、無害 | Hui et al., 2020；Hui et al., 2021 |
| 口服 morphine | Opioid-naïve 病人規則給予 10–30 mg／24 小時；opioid-tolerant（已規則使用 opioid 止痛）者可考慮把基礎劑量增加 25%–50%（ESMO 證據等級低：V, C，由醫師個別評估）；一律同時給緩瀉劑 | Hui et al., 2020 |
| Benzodiazepine | 不當第一線；opioid 無效且合併焦慮時小心使用 | Hui et al., 2020 |

**咳嗽的階梯處置**

| 步驟 | 做法 | 備註 |
|------|------|------|
| 1. 找原因 | 感染、藥物性或放射性肺炎、積水、心衰竭，以及腫瘤本身造成的氣道刺激或阻塞 | 新的咳嗽加喘，在 EGFR TKI 或免疫治療期間要先想到 ILD，立即暫停並安排影像（6.1、6.6） |
| 2. 非藥物 | 咳嗽抑制技巧（cough suppression）與衛教 | CHEST 2017 評估的非藥物介入（Molassiotis et al., 2017） |
| 3. 藥物，逐步升級 | 潤喉糖漿類（demulcents）→ opioid → 周邊作用的鎮咳藥或局部麻醉 | CHEST 2017 評估的藥物類別，證據品質低；藥品、劑量與品項依藥師與院內處方集 |
| 4. 腫瘤導向 | 支氣管內近接放療（endobronchial brachytherapy）等 | CHEST 2017 系統性回顧有納入此類治療；適用性由放射腫瘤科決定 |

**咳血的分級與第一步**（量的界線沒有統一標準，以下為病房分流用的臨床分級，院內分級可能不同）

| 程度 | 描述 | 第一步 |
|------|------|--------|
| 痰中帶血、少量 | 痰有血絲或偶爾少量；生命徵象與血氧正常 | 用杯子記錄量與次數；找原因（腫瘤、感染、血小板低下、凝血異常、抗凝血藥、anti-VEGF）；通知醫師；用 bevacizumab 的病人，近期咳出 ≥1/2 茶匙（2.5 mL）紅血要暫停（Genentech, 2025b） |
| 中量或反覆 | 反覆咳出明顯鮮血，量增加，但氣道與血壓尚穩定 | 住院；兩條靜脈通路；血型、凝血功能與血小板；胸部 CT；檢視並暫停加重出血的藥物（anti-VEGF、抗凝血藥、NSAID，由醫師決定）。非大量咳血的隨機試驗：吸入 tranexamic acid 500 mg tid（47 人），5 天內咳血停止 96% 對 50%（Wand et al., 2018） |
| 大量或危及生命 | 影響氣道、氣體交換或血行動力學；量的定義不一致，文獻從 24 小時 100 mL 到 1,000 mL 都有，多數落在 300–600 mL，Wand 試驗以 >200 mL/24 小時並伴不穩定為排除條件 | 見下方警示：氣道優先 |

> [!WARNING]
> **大咳血的第一個小時：先保住氣道，不是先找出血點**
> 1. 叫人（急救小組、麻醉科或加護病房），不要離開病人。
> 2. **出血側朝下側躺**（已知出血側時），給氧，準備抽吸；氣道無法維持時準備插管。
> 3. 建立大口徑靜脈通路，抽血型、凝血與血小板，備血；暫停抗凝血藥、NSAID 與 anti-VEGF。
> 4. 通知醫師安排支氣管鏡（隔離出血、控制氣道）與支氣管動脈栓塞：栓塞是周邊肺出血的第一線治療，止血成功率 75%–98%（Ittrich et al., 2017；Davidson & Shojaee, 2020）。
> 5. 中央型鱗癌、腫瘤侵犯大血管或空洞的病人要預期這種情況，事先確認「出血側」與急救計畫。

### 7.9 診斷後的戒菸

**這一段的結論先講：** 確診肺癌之後戒菸仍然有好處，專師的角色是「每次都問、每次都建議、給藥物、安排追蹤」。20 多項研究的整合分析顯示，在診斷前後戒菸與較好的整體存活有關（風險比 0.71，95% CI 0.64–0.80）；NSCLC 為 0.77（0.66–0.90），SCLC 為 0.75（0.57–0.99）（Caini et al., 2022）。吸菸也改變藥物濃度：erlotinib 在吸菸者的暴露量較低。

**證據**

| 項目 | 結果 | 來源 |
|------|------|------|
| 診斷前後戒菸與存活 | 21 項研究、逾 10,000 位肺癌病人；整體存活 SRR 0.71（0.64–0.80）；NSCLC 0.77（8 項研究）；SCLC 0.75（4 項研究）。研究的設計、定義與追蹤時間差異大 | Caini et al., 2022 |
| 早期肺癌確診後繼續吸菸 | 早期 NSCLC：全因死亡 HR 2.94（1.15–7.54）、復發 HR 1.86（1.01–3.41）；局限期 SCLC：全因死亡 HR 1.86（1.33–2.59）、第二原發癌 HR 4.31（1.09–16.98）、復發 HR 1.26（1.06–1.50）。生命表模型推估 5 年存活：65 歲早期 NSCLC 繼續吸菸 33%、戒菸 70%；局限期 SCLC 29% 對 63%（模型推估，不是試驗結果） | Parsons et al., 2010 |
| 對 erlotinib 的影響 | 吸菸使暴露量下降：吸菸者每 2 週加 50 mg，最高 300 mg；**一戒菸要立刻減回 150 mg（或 100 mg）** | Alembic, 2024 |
| 手術 | ERAS 指引的核心建議包括戒菸 | Batchelor et al., 2019 |

**NCCN 戒菸指引的三個原則（要同時做）**：①有實證的動機策略與行為治療（諮商，可以很簡短）；②有實證的藥物治療；③密切追蹤，必要時重新治療（Shields et al., 2023）。

**簡短介入的 5A 流程**

| 步驟 | 病房做法 |
|------|---------|
| Ask 問 | 每次評估都問：現在有沒有吸菸？吸多少？有沒有其他菸品？同住者有沒有吸菸？ |
| Advise 建議 | 清楚、個人化：「戒菸可以讓治療效果更好、副作用更少、活得比較久」 |
| Assess 評估 | 現在準備好戒了嗎？上次戒菸為什麼失敗？ |
| Assist 協助 | 訂戒菸日；開藥物（見下表）；轉介戒菸服務；教病人辨識觸發情境；請家人配合 |
| Arrange 安排追蹤 | 每次回診再問；復吸不是失敗，重新開始（NCCN 原則③） |

5A 流程見於美國公共衛生署（PHS）《Treating Tobacco Use and Dependence》2008 年更新版。本手冊讀的是該指引發表在期刊的摘要版（Clinical Practice Guideline Treating Tobacco Use and Dependence 2008 Update Panel et al., 2008），不是指引全文。摘要版把 5A 定義為在基層照護提供簡短介入的五個主要步驟（詢問是否使用菸品、建議戒菸、評估戒菸意願、協助有意願者、安排追蹤以預防復發），設計為直接臨床時間 3 分鐘以內，並註明可依臨床情況調整順序或形式。上表右欄的「病房做法」是本手冊依此架構改寫的提示，沒有逐項對照指引原文。

**戒菸藥物（ATS 2020 指引，針對一般吸菸成人）**

| 建議 | 內容 |
|------|------|
| 強建議 | Varenicline 優於尼古丁貼片；varenicline 優於 bupropion；即使病人還沒準備好戒菸，也可以開始 varenicline；療程超過 12 週的延長治療 |
| 有條件建議 | 尼古丁貼片加 varenicline 優於單用 varenicline；varenicline 優於電子菸 |

（Leone et al., 2020）。這份指引不是癌症專屬，劑量、禁忌與肺癌病人的使用要與主治醫師與藥師確認；NCCN 指引也要求所有吸菸的癌症病人使用有實證的藥物治療（Shields et al., 2023）。

**台灣的戒菸服務（衛福部新聞稿，2026-03-07；國健署作業須知）**

- 台灣自 2002 年起提供戒菸服務，2012 年推動二代戒菸計畫，**2022 年取消戒菸藥品部分負擔**，**2023 年實施新的戒菸服務制度**，提高補助鼓勵更多人參與；至 2025 年全國有 2,803 間戒菸服務機構與 11,510 名專業人員（衛生福利部, 2026a）。
- 推動方向包括把「戒菸門診」轉型為「門診戒菸」，讓各專科門診提供戒菸（衛生福利部, 2026a）。

- **補助對象與療程**（國健署《戒菸服務補助計畫作業須知》，112/1/1 生效、113/9/1 修訂；國健署網站現列的 115/3/1 生效版附註「115.3 月修正附錄五」）：戒菸治療限滿 18 歲的健保被保險人，尼古丁成癮度測試分數 ≥4 分（1991 年版 Fagerström 量表）或平均每天吸紙菸 ≥10 支，且有明確戒菸意願（延續療程不受此限）；戒菸衛教不限年齡，同樣要有明確戒菸意願。每年補助 2 個療程（有特定情事並於病歷說明理由時，可提供第三療程），每療程含 8 次診察、8 週用藥、8 次衛教與 3 次追蹤（3 個月、6 個月、1 年），須在同一機構、90 日內完成；超次使用須全額自付（衛生福利部國民健康署, 2026）。
- **補助藥物**（同作業須知附錄五，115/3/1 生效版）：尼古丁貼片、咀嚼錠、口含錠、口腔吸入劑與噴霧，以及處方藥 varenicline（0.5 mg、1 mg 錠）與 bupropion SR 150 mg；bupropion 與 varenicline 依健保處方規定辦理（衛生福利部國民健康署, 2026）。附錄五的品項與補助單價會隨公告異動（113/4/1 版與 115/3/1 版之間，varenicline 的品牌與補助單價就不同），以國健署網站最新公告為準。第 9 節（115/10/22 版）全文沒有 varenicline 或「戒菸」字樣。
- **部分負擔**：戒菸輔助用藥的部分負擔自 2022-05-15 起不分對象免收（衛生福利部, 2022）；作業須知的申報說明對補助的服務一律填部分負擔 0 元，並註明因皆不須繳交部分負擔（衛生福利部國民健康署, 2026）。
- **轉介**：免付費戒菸專線 0800-636363（衛生福利部, 2022）。

> [!CAUTION]
> **待核對：合約院所與是否再修訂**
> 上列依國健署網站現列的 115/3/1 生效版作業須知與 2022 年新聞稿整理。作業須知註明藥品品項與補助額度以國健署網站最新公告為準，且補助由菸品健康福利捐支付、國健署得視預算暫停或減支。本手冊未核對 115/3/1 之後是否又有修訂、附錄五補助額度以外病人是否另有自付項目，也未再核對 0800-636363 現在是否仍是專線號碼（只讀到 2022 年新聞稿）。病人附近的戒菸服務合約院所，以院內個管師與國健署最新公告為準。

> [!IMPORTANT]
> **考試重點：診斷後戒菸**
> - 診斷後戒菸仍與較好的存活有關（Caini 整合分析 SRR 0.71）。
> - 戒菸要「藥物 ＋ 諮商 ＋ 追蹤」三者同時做。
> - Erlotinib：吸菸者要加量，戒菸後要立刻減回 150 mg。
> - 住院、手術前後是戒菸的好時機。

---

## 8. 腫瘤急症（肺癌相關）

通用的嗜中性球低下性發燒、腫瘤溶解症候群、脊髓壓迫、高血鈣等，見 [腫瘤急症章](00-shared/02-oncologic-emergencies.md)。以下是肺癌特別常見的。

| 急症 | 為什麼肺癌常見 | 辨識 | 立即處置 |
|------|-------------|------|---------|
| 上腔靜脈症候群（SVC syndrome） | 右上葉腫瘤、SCLC、縱膈腔淋巴結 | 臉頸腫、上肢水腫、胸壁靜脈曲張、平躺喘 | 抬高床頭、給氧；嚴重症狀（喉頭水腫、意識改變）考慮支架；儘快取得組織，SCLC 對化療反應快 |
| 大咳血 | 中央型鱗狀細胞癌、腫瘤侵犯血管 | 大量咳血（常見定義 24 小時 >100–600 mL） | **出血側朝下側躺**、保護呼吸道、準備插管；tranexamic acid；支氣管鏡、支氣管動脈栓塞 |
| SIADH 低血鈉 | SCLC（副腫瘤症候群） | 意識混亂、抽搐；等容性低血鈉、尿滲透壓高 | **抽搐、意識改變等嚴重症狀：先給 3% NaCl 150 mL IV over 20 分鐘（可重複），目標先升約 5 mEq/L**；輕症或慢性：限水、鹽錠，難治者考慮 tolvaptan（須住院起始並密切追蹤血鈉）；**矯正速度每 24 小時不超過 8–10 mEq/L**；治療 SCLC 本身 |
| 高血鈣 | 鱗狀細胞癌分泌 PTHrP、骨轉移 | 倦怠、便秘、意識改變、多尿 | 水化、zoledronic acid 或 denosumab |
| 腦轉移／顱內壓上升 | NSCLC 診斷時腦轉移常見，ALK、EGFR 更高 | 頭痛、嘔吐、局部神經症狀、癲癇 | Dexamethasone（常用 4–16 mg/day）；放射腫瘤科會診（SRS 或全腦放療）；中樞穿透好的 TKI |
| 惡性肋膜積水 | 肋膜轉移（M1a） | 喘、單側呼吸音減弱 | 有症狀才處理，先做治療性胸腔穿刺；演算法與 IPC、沾黏術見[腫瘤急症章](00-shared/02-oncologic-emergencies.md#12-惡性肋膜積水)第 12 節，肺癌的特別考量見 8.1 |
| 心包膜填塞 | 心包膜轉移 | 低血壓、頸靜脈怒張、心音遙遠、奇脈 | 緊急心臟超音波與心包膜穿刺 |

其他 SCLC 副腫瘤症候群：**Lambert-Eaton 肌無力症候群**（抗 VGCC 抗體，近端肌無力、活動後改善）、**異位性 ACTH**（低血鉀、高血糖、水腫）；依組織型整理的副腫瘤症候群總表見 3.0。

> [!WARNING]
> **Bevacizumab 的禁忌**
> 鱗狀細胞癌、近期咳血、腫瘤侵犯大血管或有空洞的病人，使用 bevacizumab 可能發生致命性大咳血。這是 bevacizumab 只用於非鱗狀 NSCLC 的原因，也是常考題。

### 8.1 肺癌的惡性肋膜積水（肺癌特有的重點）

通用演算法（有症狀才處理 → 超音波引導的大量穿刺 → 肺能否復張 → IPC 或沾黏術）、穿刺技術、IPC 居家引流與併發症，都在[腫瘤急症章](00-shared/02-oncologic-emergencies.md#12-惡性肋膜積水)第 12 節，這裡不重複，只補肺癌特有的三件事。積水本身在分期上屬 M1a（第 9 版 IVA；見 3.2）。

**1. 先確認肺能不能復張（expandable 或 trapped lung）**

- ATS／STS／STR 2018：肺可以復張，IPC 與化學沾黏術二擇一；**肺不復張或沾黏失敗，IPC 優先**（Feller-Kopman et al., 2018）。
- 肺癌常見的不復張原因：腫瘤造成支氣管阻塞（中央型病灶合併肺塌陷）、肋膜纖維化或腫瘤把肺包住；IPC-PLUS 試驗把「肺復張不良」定義為視覺上的肋膜纖維化或支氣管阻塞（見急症章 12.3）。
- 護理上要看的是：穿刺或引流中出現持續咳嗽、胸悶、胸痛，引流後 X 光或超音波肺沒有貼回胸壁，都要通報，這時候做 talc 沾黏術多半會失敗。

**2. IPC 或沾黏術怎麼選（肺癌病人）**

| 情境 | 偏向 | 理由 |
|------|------|------|
| 肺不復張，或沾黏失敗 | IPC | ATS 2018（Feller-Kopman et al., 2018） |
| 肺可復張，想少住院、可在家引流 | IPC | TIME2：初次住院天數中位數 0 對 4 天，6 個月時喘的改善 IPC 較好；但 IPC 組不良事件較多、talc 組較常需要再次肋膜介入（Davies et al., 2012） |
| 肺可復張，不想帶導管 | Talc 沾黏術 | 90 天沾黏失敗約 22–24%（見急症章 12.5） |
| 預期存活很短 | 住院負擔低的選項（IPC） | LENT 分數可協助分層（見急症章 12.2） |

**3. 有 EGFR 敏感突變：積水可能隨 TKI 治療縮減**

- 新加坡單中心觀察研究（70 位肺腺癌合併 MPE，56 人做 EGFR 檢測、39 人突變、34 人用 TKI）：單純引流 20 人、talc 沾黏術 14 人，積水再積的時間 9.9 個月（有沾黏）對 11.7 個月（無沾黏），P = .59；作者認為適合 TKI 的病人，早期 talc 沾黏術可能沒有額外的好處。EGFR 突變者較常見整側胸腔全白（25.6% 對 0%，P = .02）（Verma et al., 2016）。
- 日本單中心回溯研究：EGFR 突變合併 MPE 的病人一線用 TKI，沒有做沾黏術者的中位存活有較長的傾向（31.1 對 21.8 個月），而且沒有低白蛋白血症或體能惡化（Kashiwabara et al., 2020）。
- 日本單中心回溯研究（229 位 osimertinib）：未用過 TKI 的病人，有 MPE 者治療失敗時間中位數 14.8 個月，無 MPE 者 19.8 個月（HR 1.40，0.90–2.18，P = .12），整體存活 32.0 對 42.0 個月（HR 1.43，0.86–2.38，P = .16），差異未達統計顯著（Kiritani et al., 2024）。

> [!CAUTION]
> **待核對：這三項都是單中心觀察資料**
> 以上沒有隨機試驗，樣本小、可能有選擇偏差，只能支持「EGFR 突變合併積水的病人，TKI 仍然有效；不一定要急著做沾黏術」，不能當成定論。喘得明顯的病人，仍然要先引流緩解症狀，因為沒有證據支持用全身治療取代症狀性 MPE 的引流（Bibby et al., 2018；見急症章 12.2）。

**實務連結**

- 已知 EGFR 敏感突變或 ALK 融合、體能允許的病人：同時進行治療性穿刺與盡快開始標靶藥；是否馬上裝 IPC 或做沾黏術，與主治醫師討論，並看標靶藥開始後積水是否減少。
- 細胞學陰性但高度懷疑時，需要肋膜切片（急症章 12.2）。
- 化療期間有 IPC 的病人發燒，除了走嗜中性球低下性發燒流程（急症章第 1 節），還要檢查出口與引流液（IPC 相關感染，見急症章 12.7）。

---

## 9. 健保給付與事前審查

**這一段的結論先講：** 開肺癌藥之前，先確認三件事：基因或 PD-L1 報告的來源合格嗎（通則十二）？病人的組織型、期別、線別和該條文字一字不差嗎？這條要不要事前審查、多久再送一次？第一線 ALK TKI 是五選一、除嚴重不良反應或耐受不良不得互換；第一線 EGFR TKI 也有擇一規定，但名單各條寫法不一（見下方「擇一使用、不得互換」的原則）；免疫治療（9.69）一律事前審查。有藥證不等於有健保給付，章節 4.5 的新藥多數在 115/10/22 版原文找不到條文（見 9.5）。

### 9.0 先讀這裡：怎麼讀給付規定

- **依據版本**：全民健康保險藥品給付規定第 9 節「抗癌瘤藥物」，**115/10/22 版**（原文存於 `sources/nhi/section9-1151022.md`）。日期是民國紀年，115 年 ＝ 2026 年。
- **條號欄的日期**是該條「條號列」上最新的修訂日期，不是每一小項自己的日期；小項日期在原文括號裡。
- **原文用詞照錄**：期別寫「局部侵犯性或轉移性（即為 IIIB、IIIC 期或第 IV 期）」「局部晚期或轉移性」「晚期」「轉移性（第 IV 期）」各條不同，原文沒有註明 AJCC 版次，不要自行換算成第 9 版的期別。
- **ECOG**：標靶藥條文大多沒有寫 ECOG；9.26 pemetrexed 的 1.(3)（第一線併含鉑化療）寫「ECOG 0~1」；免疫治療 9.69 要求 ECOG≦1。
- **讀每一條的五個欄位**：適應症限制（病理、biomarker、期別、線別）→ 事前審查（送審資料）→ 療程與續用評估（多久再送審、附什麼影像）→ 停用條件 → 不可併用或互換的限制。

> [!IMPORTANT]
> **通則十二：生物標記報告要合格**
> 給付規定要求附生物標記檢測報告時（EGFR、ALK、ROS-1、BRAF V600E、MET exon 14 skipping、NTRK、PD-L1 等），報告必須符合下列**任一**條件（113/6/1）：
> - （一）符合全民健康保險醫療服務給付項目及支付標準的規定；
> - （二）使用經衛生福利部許可的伴隨式診斷用體外診斷醫療器材（IVD）檢測；
> - （三）由衛生福利部核定之實驗室開發檢測（LDT）施行計畫所列醫療機構的認證實驗室執行，且技術項目符合核定的分析標的。
>
> 送審前先確認手上的報告屬於哪一種。報告出自哪裡，以及檢測項目是否在核定範圍內，都要在病歷上看得到。

**各類藥物的事前審查與送審週期**

| 藥品類別 | 條文是否規定事前審查 | 每次申請或處方的期間 |
|---------|-------------------|-------------------|
| gefitinib、erlotinib（單用）、afatinib、dacomitinib | 條文沒有規定（只要求病歷留存資料） | 每次處方以 4 週為限 |
| osimertinib、aumolertinib | 是 | 每次申請 3 個月；每次處方 4 週 |
| bevacizumab ＋ erlotinib | 是 | 每次申請 12 週 |
| amivantamab | 是 | 每次申請 3 個月 |
| crizotinib、ceritinib、alectinib、lorlatinib、brigatinib、entrectinib、repotrectinib、dabrafenib ＋ trametinib、tepotinib | 是 | 每次申請 3 個月 |
| larotrectinib | 是 | 每次申請 12 週 |
| 免疫檢查點抑制劑（9.69） | 是 | 每次申請 12 週，最長 2 年（另有規定者從其規定） |
| 化療（carboplatin、docetaxel、gemcitabine、paclitaxel、vinorelbine、topotecan） | 條文沒有寫；併用免疫治療者依 9.69 | 條文未訂 |
| pemetrexed | 條文沒有寫；併用免疫治療者依 9.69 | 每 4 個療程評估療效，無惡化才可繼續 |

**「擇一使用、不得互換」的原則**

- **EGFR 第一線**：gefitinib、erlotinib、afatinib、dacomitinib、osimertinib、aumolertinib 和 bevacizumab ＋ erlotinib 組合，各條都有「擇一、除耐受性不良不得互換」的文字，但名單不完全一致。各條列出的名單略有出入（例如 9.29 erlotinib 的擇一名單沒有列 gefitinib、afatinib，這兩個藥改列在「不得併用」），合併來讀：gefitinib、erlotinib、afatinib 三者彼此之間，條文只寫「不得併用」（afatinib 另有 2.(4)：使用後除耐受性不良，不得轉換類似藥理機轉的其他 TKI）；明文的「擇一、除耐受性不良不得互換」，是這三者各自與 osimertinib、dacomitinib、aumolertinib 之間的規定，gefitinib 與 afatinib 另包含 bevacizumab ＋ erlotinib 組合。換藥前先和藥事部門確認。換藥時，必須符合新藥自己的第一線條件。
- **ALK 第一線**：crizotinib、ceritinib、alectinib、brigatinib、lorlatinib 五選一，除嚴重不良反應或耐受不良外不得互換。
- **ROS-1**：crizotinib 與 entrectinib 擇一，條件同上。
- **免疫治療**：每位病人每個適應症限給付一種免疫檢查點抑制劑，不得互換。

> [!NOTE]
> **版本與更新**
> 以 115/10/22 版為準；給付規定改版時，對照 `sources/nhi/` 的新舊原文，重新核對條號、修訂日期、適應症與事前審查期間。2026 年的條文多次修訂，新聞稿與院內公告不可直接當成給付條件。

### 9.1 EGFR 標靶藥

| 藥品（商品名） | 條號（最新修訂） | 給付適應症與條件 | 事前審查 | 療程／續用評估 | 停用／互換／併用限制 |
|--------------|---------------|----------------|---------|--------------|------------------|
| gefitinib（Iressa） | 9.24（115/8/1） | 限單獨使用。①第一線：具 EGFR-TK 基因突變（原文沒有限定突變型）、局部侵犯性或轉移性（即第 IIIB、IIIC 或第 IV 期）的肺腺癌；需檢附 EGFR 基因檢測報告並符合通則十二。②第二線以上：先前用過第一線含鉑化療，或 70 歲以上接受過第一線化療，但仍局部惡化或轉移的肺腺癌（原文沒有要求 EGFR 突變，也沒有寫期別） | 條文沒有規定。病歷應留存：肺腺癌病理或細胞檢查報告、EGFR-TK 報告（第一線）；前線化療證明與惡化影像（第二線）。附表九之一寫有事前審查，與條文不一致，見 9.6 | 每次處方 ≤4 週；再次處方時於病歷記錄臨床資料（每 4 週影像追蹤，每 8 至 12 週完整療效評估）；原文未設總療程上限 | 原文沒有明列停用條件。不得與 erlotinib、afatinib 併用；第一線與 osimertinib、dacomitinib、bevacizumab ＋ erlotinib、aumolertinib 擇一，除耐受性不良不得互換 |
| erlotinib（Tarceva） | 9.29（115/8/1） | 第 1 項限單獨使用。①第一線：具 EGFR-TK 突變、局部侵犯性或轉移性（第 IIIB、IIIC 或第 IV 期）的肺腺癌，需 EGFR 報告並符合通則十二。②維持療法：已接受 4 個週期 platinum 類第一線化療後腫瘤穩定（SD，不含 PR 或 CR）的局部晚期或轉移性肺腺癌。③第二線：用過 platinum 類第一線化療，或 70 歲以上接受過第一線化療，仍局部惡化或轉移的腺性 NSCLC。④第三線：用過 platinum 類及 docetaxel 或 paclitaxel 後仍惡化的 NSCLC（未限組織型）。②至④原文沒有要求 EGFR 突變 | 單獨使用：條文沒有規定。病歷應留存各線別的病理或細胞檢查報告、前線化療證明、惡化影像（維持療法留存 SD 影像）。與 bevacizumab 併用見下一列 | 每次處方 ≤4 週；再次處方時記錄臨床資料（同 gefitinib）；原文未設總療程上限 | 原文沒有明列停用條件。不得與 gefitinib、afatinib 併用；第一線與 osimertinib、dacomitinib、aumolertinib 擇一，除耐受性不良不得互換 |
| bevacizumab（Avastin）＋ erlotinib | 9.29 第 2 項（114/4/1）；9.37 第 5 項（114/3/1） | 第一線：無法手術切除的轉移性（第 IV 期）、帶有 EGFR Exon 21 L858R 活化性突變、**腦轉移**的非鱗狀 NSCLC。bevacizumab 限 7.5 mg/kg，每 3 週 1 次。廠牌排除：9.29 寫「除 Zirabev 以外」，9.37 寫「除 Zirabev 及 Abevmy 以外」，兩條寫法不一致 | 是（9.37 5.(2)）：每次申請 12 週；初次需附 EGFR Exon 21 L858R 檢測報告並符合通則十二 | 每 12 週再申請，必須提出客觀證據（如影像學）證實無惡化才可繼續；erlotinib 仍受每次處方 ≤4 週的規定 | 未證實無惡化即不得續用。此組合與 gefitinib、afatinib 擇一，除耐受性不良不得互換 |
| afatinib（Giotrif） | 9.45（115/8/1） | 限單獨使用。①第一線：具 EGFR-TK 基因突變、局部晚期或轉移性（第 IIIB、IIIC 期或第 IV 期）的肺腺癌；需 EGFR 報告並符合通則十二。②第二線：用過第一線含鉑化療後仍惡化的局部晚期或轉移性**鱗狀**組織 NSCLC（原文沒有要求 EGFR 突變，也沒有 70 歲的替代條件） | 條文沒有規定。病歷應留存：肺腺癌病理或細胞檢查報告與 EGFR-TK 報告（第一線）；含鉑化療證明與惡化影像（第二線） | 每次處方 ≤4 週；再次處方時記錄臨床資料（同 gefitinib）；原文未設總療程上限 | 原文沒有明列停用條件。使用 afatinib 後，除耐受性不良不得轉換類似藥理機轉的其他 TKI（2.(4)，不限線別）；不得與 gefitinib、erlotinib 併用；第一線與 osimertinib、dacomitinib、bevacizumab ＋ erlotinib、aumolertinib 擇一 |
| dacomitinib（Vizimpro） | 9.83（115/8/1） | 限單獨使用，只有第一線：具 EGFR-TK Exon 19 Del 或 Exon 21 L858R 點突變，**且無腦轉移（non-CNS）**、局部侵犯性或轉移性（第 IIIB、IIIC 或第 IV 期）的肺腺癌；需 EGFR 報告並符合通則十二 | 條文沒有規定。病歷應留存肺腺癌病理或細胞檢查報告與 EGFR-TK 報告 | 每次處方 ≤4 週；再次處方時記錄臨床資料；每日限用 1 粒 | 原文沒有明列停用條件。與 gefitinib、erlotinib、afatinib、osimertinib、aumolertinib 擇一，除耐受性不良不得互換，換藥須符合本藥第一線條件 |
| osimertinib（Tagrisso） | 9.80（115/8/1） | 限單獨使用。①第一線：具 EGFR Exon 19 Del 或 Exon 21 L858R 基因突變、局部侵犯性或轉移性（即為 IIIB、IIIC 期或第 IV 期）的肺腺癌。②第二線：先前用過 gefitinib、erlotinib、afatinib 或 dacomitinib 治療失敗，且具 EGFR T790M 基因突變的局部侵犯性或轉移性 NSCLC（不限肺腺癌） | 是：每次申請以 3 個月為限。初次需附肺腺癌或 NSCLC 的病理或細胞檢查報告與 EGFR 基因檢測報告（通則十二）；第二線另附 T790M、曾用前線 TKI 的證明、目前惡化的影像（可測量病灶優先，無則可評估病灶） | 再次申請需附影像等臨床資料證實無惡化；每次處方 ≤4 週，給藥 4 週後追蹤胸部 X 光或 CT，每 8 至 12 週完整療效評估；每日限用 1 粒 | 病情惡化、復發或產生不可接受之毒性，即不得再次申請。第一線與 gefitinib、erlotinib、afatinib、dacomitinib、aumolertinib 擇一，換用本藥須符合本藥第一線條件；第二線與 aumolertinib 擇一；皆除耐受性不良不得互換 |
| aumolertinib（Pulmivex） | 9.138（115/8/1，條文只標這一個日期） | 限單獨使用。①第一線：具 EGFR Exon 19 Del 或 Exon 21 L858R 基因突變、局部侵犯性或轉移性（即為 IIIB、IIIC 期或第 IV 期）的肺腺癌。②第二線：先前用過 gefitinib、erlotinib、afatinib 或 dacomitinib（前線藥物名單沒有列 osimertinib）治療失敗，且具 EGFR T790M 的局部侵犯性或轉移性 NSCLC | 是：條件與送審資料同 osimertinib（每次申請 3 個月；初次附病理或細胞檢查報告與 EGFR 基因檢測報告，通則十二） | 同 osimertinib（再次申請證實無惡化；每次處方 ≤4 週；每 8 至 12 週完整療效評估）；**每日限給付 2 粒**（osimertinib 與 dacomitinib 為 1 粒） | 病情惡化、復發或產生不可接受之毒性，即不得再次申請。第一線與 gefitinib、erlotinib、afatinib、dacomitinib、osimertinib 擇一；第二線與 osimertinib 擇一；皆除耐受性不良不得互換 |
| amivantamab（Rybrevant）＋ carboplatin ＋ pemetrexed | 9.126（114/10/1）；併用藥見 9.2 第 7 項、9.26 第 1.(5) 項（皆 114/10/1） | 第一線：成人、帶有 EGFR exon 20 插入突變的局部晚期或轉移性 NSCLC（原文沒有寫期別數字）。amivantamab ＋ lazertinib 用於 ex19del／L858R 的 MARIPOSA 用法，原文未見 | 是：初次需附 NSCLC 病理或細胞檢查報告與 EGFR exon 20 插入突變分析檢測報告（通則十二）；每次申請 3 個月 | 每 3 個月再申請，並附療效評估資料；併用的 pemetrexed 依 9.26 第 2 項，每 4 個療程評估療效，無惡化才可繼續 | 病情惡化即不得再次申請。原文沒有擇一或不得互換的規定，也沒有數量限制 |

**EGFR 這一組讀表時最容易踩的地方**

- **第三代 EGFR TKI 有給付的是兩種**：osimertinib（9.80，第一線條文日期標示 111/4/1、113/10/1）與 aumolertinib（9.138）；兩者的第一線、第二線都彼此擇一。lazertinib 原文未見（見 9.5）。
- **突變型有差別**：osimertinib、aumolertinib、dacomitinib 的第一線只給付 **Exon 19 Del 或 Exon 21 L858R**；gefitinib、erlotinib、afatinib 的條文寫的是「EGFR-TK 基因突變」，沒有限定突變型。照條文字面讀，非典型突變（G719X、L861Q、S768I）的第一線給付只有這三條可以對應，而 4.3 的指引表偏好 afatinib 或 osimertinib，指引與給付之間有落差，開藥前先確認。
- **dacomitinib 要「無腦轉移」**：病人已有腦轉移時，不符合 9.83 的條件。
- **換藥的例外只有「耐受性不良」**：疾病惡化不在第一線 TKI 之間互換的例外內；惡化後走第二線條件（osimertinib 與 aumolertinib 需要 T790M，並且曾用過 gefitinib、erlotinib、afatinib 或 dacomitinib）。
- **9.80 只寫了兩個適應症**：第一線與 T790M 第二線。術後輔助（ADAURA）和 CCRT 後鞏固（LAURA）這兩種用法，原文未見給付文字。

> [!CAUTION]
> **待核對：afatinib 之後轉用 osimertinib**
> 9.45 的 2.(4) 寫「使用本藥品後，除因耐受性不良，否則不得轉換類似藥理機轉之其他 TKI」，而 9.80 與 9.138 的第二線條件又把 afatinib 列為可以治療失敗的前線藥物。原文沒有說明兩條的關係。afatinib 惡化且有 T790M 的病人能不能申請 osimertinib 或 aumolertinib 第二線，本手冊不下結論，送審前向院內藥事部門或健保審查窗口確認。

### 9.2 ALK、ROS1、BRAF、MET、NTRK、HER2 與其他標靶藥

下表的 ALK 與 ROS-1 藥物，**影像追蹤的寫法一致**（除非特別註明）：給藥 4 週後追蹤胸部 X 光或電腦斷層（CT）評估療效，往後每 4 週做胸部 X 光，每 3 個月追蹤一次評估藥效的影像（胸部 X 光或 CT）。entrectinib 與 repotrectinib 是「每隔 8 週」追蹤評估藥效的影像。各條都是「病情惡化即不得再次申請」。

| 藥品（商品名） | 條號（最新修訂） | 給付適應症與條件 | 事前審查 | 療程／續用評估 | 停用／互換／併用限制 |
|--------------|---------------|----------------|---------|--------------|------------------|
| crizotinib（Xalkori）：ALK | 9.50 第 1 點（113/9/1） | ALK 陽性晚期 NSCLC 第一線，**且於 113 年 9 月 1 日前經審核同意用藥、後續評估符合續用條件者**。原文沒有提供 113/9/1 以後新 ALK 個案的給付途徑 | 是：每次 3 個月；初次需附 NSCLC 病理或細胞檢查報告與 ALK 突變檢測報告（通則十二） | 再次申請附治療後臨床資料與影像（寫法見上）；每日最大劑量 500 mg | 病情惡化即不得再次申請。與 ceritinib、alectinib、brigatinib、lorlatinib 第一線擇一，除嚴重不良反應或耐受不良不得互換 |
| crizotinib（Xalkori）：ROS-1 | 9.50 第 2 點（113/9/1；本點 108/9/1） | 單獨使用於 ROS-1 陽性晚期 NSCLC（原文未限線別） | 是：每次 3 個月；初次附病理或細胞檢查報告與 ROS-1 突變檢測報告（通則十二） | 同上；每日最大劑量 500 mg | 病情惡化即不得再次申請。與 entrectinib 擇一，除嚴重不良反應或耐受不良不得互換 |
| ceritinib（Zykadia） | 9.59（113/6/1） | ALK 陽性晚期 NSCLC 第一線 | 是：每次 3 個月；初次附病理或細胞檢查報告與 ALK 突變檢測報告（通則十二） | 同上；每日最大劑量 450 mg | 病情惡化即不得再次申請。ALK 第一線五藥擇一，除嚴重不良反應或耐受不良不得互換 |
| alectinib（Alecensa） | 9.60（113/6/1） | ALK 陽性晚期 NSCLC 第一線。9.60 只有這一個適應症，**術後輔助（ALINA）原文未見** | 是：每次 3 個月；初次附病理或細胞檢查報告與 ALK 突變檢測報告（通則十二） | 同上；每日最大劑量 1200 mg | 病情惡化即不得再次申請。ALK 第一線五藥擇一，除嚴重不良反應或耐受不良不得互換 |
| brigatinib（Alunbrig） | 9.82（113/6/1） | ①ALK 陽性晚期 NSCLC 第一線。②在 **crizotinib** 治療中惡化的 ALK 陽性晚期 NSCLC | 是：每次 3 個月。①初次附病理或細胞檢查報告與 ALK 突變檢測報告（通則十二）；②原文沒有另列檢附文件 | ①影像追蹤同上；②再次申請附治療後臨床資料（未訂影像頻率）。**全條每日最大劑量 180 mg**（第 3 點，111/8/1） | 病情惡化即不得再次申請。①與其他四種 ALK TKI 擇一，除嚴重不良反應或耐受不良不得互換 |
| lorlatinib（Lorviqua） | 9.81（113/6/1） | ①ALK 陽性晚期 NSCLC 第一線。②在 **ceritinib、alectinib 或 brigatinib** 治療中惡化的 ALK 陽性晚期 NSCLC（原文沒有列 crizotinib） | 是：每次 3 個月。①初次附病理或細胞檢查報告與 ALK 突變檢測報告（通則十二）；②原文沒有另列檢附文件 | ①影像追蹤同上；②再次申請附治療後臨床資料（未訂影像頻率）；原文未訂每日劑量上限 | 病情惡化即不得再次申請。①與其他四種 ALK TKI 擇一，除嚴重不良反應或耐受不良不得互換 |
| entrectinib（Rozlytrek） | 9.93（113/6/1） | 單獨使用於 ROS-1 陽性的局部晚期或轉移性 NSCLC 成人（未限線別）。**NTRK 融合適應症原文未見** | 是：每次 3 個月；附病理或細胞檢查報告與符合診斷的 ROS-1 突變檢測報告（通則十二） | 影像：4 週後，之後每 4 週胸部 X 光，**每隔 8 週**追蹤評估藥效的影像；每日最大劑量 600 mg | 病情惡化即不得再次申請。與 crizotinib 擇一，除嚴重不良反應或耐受不良不得互換 |
| repotrectinib（Augtyro） | 9.131（115/2/1） | 單獨給付於在 **crizotinib 或 entrectinib** 治療中惡化的 ROS1 陽性局部晚期或轉移性 NSCLC 成人 | 是：每次申請以 3 個月為限；附病理或細胞檢查報告與符合診斷的 ROS-1 突變檢測報告（通則十二） | 影像同 entrectinib（每隔 8 週）；每日最大劑量 320 mg | 病情惡化即不得再次申請。原文沒有擇一條款 |
| dabrafenib（Tafinlar）＋ trametinib（Mekinist） | 9.91 第 4 點（113/6/1） | 併用；BRAF V600E 突變的轉移性（第 IV 期）NSCLC 成人，**第二線**：先前接受過第一線含鉑化療仍惡化者 | 是：每次 3 個月；初次附病理或細胞檢查報告與 BRAF V600E 突變檢測報告（通則十二） | 再次申請附治療後臨床資料（未訂影像頻率） | 病情惡化即不得再次申請。使用本品無效後，**不再給付**該適應症相關的 PD-1、PD-L1 抑制劑；本品與 vemurafenib 僅能擇一，除耐受性不良不得互換（第 3 點） |
| tepotinib（Tepmetko） | 9.101（113/6/1） | 轉移性 NSCLC 成人，腫瘤帶有 MET exon 14 skipping mutation（未限線別） | 是：每次 3 個月；初次附病理或細胞檢查報告與符合診斷的 MET exon 14 skipping mutation 檢測報告（通則十二） | 再次申請附治療後臨床資料（未訂影像頻率）；每日最多處方 2 粒 | 病情惡化即不得再次申請。使用本品無效後，不再給付該適應症相關的 PD-1、PD-L1 抑制劑 |
| larotrectinib（Vitrakvi） | 9.95（113/6/1） | NTRK 基因融合實體腫瘤；共通條件：具 NTRK 融合且無已知的後天阻抗性突變、為轉移性或手術切除極可能造成嚴重病症、沒有合適的替代治療（含免疫檢查點抑制劑）。成人 NSCLC 符合任一：Ⅰ.不適合化療的晚期 NSCLC（非鱗狀需 EGFR/ALK/ROS-1 原生型，鱗狀需 EGFR/ALK 原生型）；Ⅱ.含鉑化療失敗後惡化，且 EGFR/ALK 原生型的晚期鱗狀 NSCLC；Ⅲ.含鉑及 docetaxel／paclitaxel 類二線（含）以上化療均失敗後惡化，且 EGFR/ALK/ROS-1 原生型的晚期肺腺癌；Ⅳ.至少一線 anti-EGFR TKI 失敗，且因 NTRK 融合對 anti-EGFR TKI 產生抗性的局部侵犯性或轉移性 EGFR 突變 NSCLC | 是：每次 12 週；初次附 NTRK 基因融合檢測報告，NTRK 1/2/3 檢測符合通則十二 | 每 12 週再申請，檢附療效評估資料證實無疾病進展才可繼續使用 | 未能證實無疾病進展即不得續用。原文沒有擇一規定 |
| trastuzumab deruxtecan（Enhertu） | 9.115（114/2/1） | **肺癌：原文未見。** 9.115 只有乳癌適應症，全檔沒有 HER2 突變 NSCLC 的給付文字 | 乳癌：是（每次 12 週）；肺癌不適用 | 肺癌不適用 | 肺癌不適用 |

**ALK、ROS-1 這一組讀表時的重點**

- **ALK 第一線五選一**後，惡化的後線有方向限制：lorlatinib 的後線只接在 ceritinib、alectinib 或 brigatinib 之後；brigatinib 的後線只接在 crizotinib 之後。第一線用了 alectinib 的病人，後線條文可對應的是 lorlatinib。
- **劑量上限是給付上限**：alectinib 每日最大 1200 mg（相當於 600 mg BID）、brigatinib 每日最大 180 mg、ceritinib 450 mg、crizotinib 500 mg、entrectinib 600 mg、repotrectinib 320 mg。
- **指引與給付有落差的地方**：BRAF V600E 在指引是第一線選項（4.3），健保給付是含鉑化療後的第二線，並且用藥無效後不再給付該適應症的 PD-1、PD-L1 抑制劑；MET exon 14 只有 tepotinib 有條文（capmatinib 見 9.5）；RET、KRAS G12C、HER2 突變沒有任何肺癌標靶藥條文（見 9.5）。

### 9.3 免疫檢查點抑制劑（9.69）

9.69 的條文最新修訂為 **115/10/1**（全條共有 28 個修訂日期）。肺癌的給付就是下面表中的 8 個適應症列，**一律要事前審查**。PD-1、PD-L1 是藥理分類，條文不是按這個分類寫的，下表按適應症排列。

**共同規則（9.69 的 3. 與 4.，肺癌每一列都適用）**

| 項目 | 規則 |
|------|------|
| 使用方式 | 在藥品許可證登載的適應症及仿單內，單獨使用（9.69.1）或併用其他藥品（9.69.2） |
| 病人條件（3.(1)、3.(2)） | ECOG≦1；NYHA Functional Class I 或 II；GOT<60 U/L、GPT<60 U/L 且 T-bilirubin<1.5 mg/dL；腎功能：肺癌不在泌尿道上皮癌的 i 至 iii 項內，適用 iv「其他癌別」：Creatinine<1.5 mg/dL 且 eGFR>60 mL/min/1.73m²（115/2/1） |
| PD-L1 檢測（3.(3)） | 要用各藥對應的第三等級體外診斷醫療器材（class III IVD）：pembrolizumab 與 cemiplimab 用 Dako 22C3 或 Ventana SP263；nivolumab 用 Dako 28-8 或 Ventana SP263；atezolizumab 用 Ventana SP142；durvalumab 與 tislelizumab 用 Ventana SP263。SP263 只適用於檢測 NSCLC、泌尿道上皮癌維持療法或食道鱗狀細胞癌。結果要符合下面的 PD-L1 表 |
| 初次申請要附（3.(7)） | Ⅰ.病理或細胞檢查報告，以及 NSCLC 的腫瘤基因檢測報告（符合給付適應症內容規定，並符合通則十二）；Ⅱ.PD-L1 報告（符合通則十二；PD-L1 表標示「不需檢附報告」者免附）；Ⅲ.ECOG≦1 及心肺與肝腎功能評估；Ⅳ.12 週內的影像檢查及報告（可測量病灶優先，無則可評估病灶；**影像給付範圍不含 PET**）；Ⅴ.先前治療與完整用藥資料（含化療、標靶及自費用藥的劑量與療程）及治療結果；Ⅵ.treatment protocol；其他佐證病歷 |
| 事前審查（3.(6)、3.(7)） | 需經事前審查核准後使用；每次申請以 12 週為限 |
| 續用（3.(8)、3.(9)） | 用藥後每 12 週至少評估一次，以 i-RECIST 評定。iPR（PR）或 iCR（CR）可繼續；iSD（SD）僅限 nivolumab、avelumab、ipilimumab、cemiplimab、dostarlimab、tislelizumab 或 pembrolizumab 可繼續。atezolizumab、durvalumab、tremelimumab 評估為 SD 時，可再用 12 週後再評估，**連續二次評估皆為 SD 者不得申請續用**（durvalumab 用於 NSCLC 鞏固治療不在此限）。續用要附 12 週內的 ECOG 與器官功能、i-RECIST 療效反應資料及影像報告（不含 PET）、其他佐證病歷 |
| 停用（3.(8)） | 初始用藥後評估為 iUPD 者，可持續用藥 4 至 8 週後再評估，再評估為 iCPD（PD）即停藥；出現 iCPD（PD），或出現中、重度或危及生命的藥物不良反應，應停藥 |
| 給付時程（3.(5)） | 自初次處方用藥日起算 **2 年**；例外：durvalumab 鞏固治療為 1 年，nivolumab 用於 NSCLC 術前輔助治療至多 3 個療程 |
| 擇一與標靶藥（3.(4)） | 每位病人每個適應症限給付一種免疫檢查點抑制劑，不得互換；治療期間不可合併申報該適應症的標靶藥物（atezolizumab 與 bevacizumab 併用於非鱗狀 NSCLC 第一線除外）；無效後或給付時程期滿後，不再給付該適應症相關的標靶藥物 |
| 登錄與結案（4.） | 病人結束治療、停止用藥、未通過續用申請或達給付時程期限時，醫事機構須在 **28 天內於 VPN 系統登錄結案**。逾期未登錄者由系統自動結案，且不支付該個案自前次事前審查核定日後申報的藥費；已結案者，自結案日後不支付藥費 |

**PD-L1 表（9.69 的 3.(3)，肺癌各列；欄位是藥品，格內是門檻）**

| 事審代碼 | 適應症 | pembrolizumab | nivolumab | atezolizumab | durvalumab | cemiplimab | tislelizumab |
|---------|-------|--------------|-----------|--------------|------------|-----------|--------------|
| P011 | 鱗狀 NSCLC 第二線（單用） | TPS≧50% | TC≧50% | TC≧50% 或 IC≧10% | 尚未給付 | 尚未給付 | TC≧50% |
| P012 | 非鱗狀 NSCLC 第三線（單用；條文稱肺腺癌） | TPS≧50% | TC≧50% | TC≧50% 或 IC≧10% | 尚未給付 | 尚未給付 | TC≧50% |
| P013 | 鱗狀、非鱗狀 NSCLC 第一線（單用） | TPS≧50% | 尚未給付 | TC≧50% 或 IC≧10% | 尚未給付 | TPS≧50% | 尚未給付 |
| P013 | 非鱗狀 NSCLC 第一線（併用） | 不需檢附報告 | 尚未給付 | 不需檢附報告 | 尚未給付 | 尚未給付 | TC≧50% |
| P014 | 鱗狀 NSCLC 第一線（併用化療） | TPS 1~49% | 尚未給付 | 尚未給付 | 尚未給付 | 尚未給付 | 不需檢附報告 |
| P015 | NSCLC 鞏固治療 | 尚未給付 | 尚未給付 | 尚未給付 | PD-L1≧1% | 尚未給付 | 尚未給付 |
| P016 | NSCLC 術前輔助治療（併用） | 尚未給付 | 不需檢附報告 | 尚未給付 | 尚未給付 | 尚未給付 | 尚未給付 |
| P021 | 小細胞肺癌（併用化療） | 尚未給付 | 尚未給付 | 不需檢附報告 | 不需檢附報告 | 尚未給付 | 尚未給付 |

TPS ＝ tumor proportion score（pembrolizumab、cemiplimab）；TC ＝ tumor cell；IC ＝ immune cell。PD-L1 表另有 avelumab 與 dostarlimab 兩欄，肺癌各列都是「尚未給付」，此處省略。這張表是條文內附的表格（原文稱「下表」），不是需要填寫的附表。

> [!IMPORTANT]
> **PD-L1 報告什麼時候不用附**
> 單用免疫治療的 NSCLC 列（P011、P012、P013 單用）都要有 PD-L1 報告且達門檻。表中標示「不需檢附報告」的是：nivolumab 術前輔助（P016）、pembrolizumab 與 atezolizumab 的非鱗狀第一線併用（P013 併用）、tislelizumab 的鱗狀第一線併用（P014）、SCLC 的 atezolizumab 與 durvalumab（P021）。免附的是 PD-L1 報告，**NSCLC 的腫瘤基因檢測報告仍要附**（3.(7)Ⅰ，須符合通則十二）。

| 藥品 | 條號（最新修訂） | 給付適應症與條件 | 事前審查 | 療程／續用評估 | 停用／互換／併用限制 |
|------|---------------|----------------|---------|--------------|------------------|
| durvalumab：NSCLC 鞏固 | 9.69.1.(2)第 1 項（114/8/1） | 單用；第三期局部晚期、無法手術切除的 NSCLC 成人，PD-L1≧1%；非鱗狀需 EGFR/ALK/ROS-1 原生型，鱗狀需 EGFR/ALK 原生型；須於根治性同步放射治療合併至少 2 個週期含鉑化療後無惡化（無 PD） | 是（P015）；每次 12 週 | **至多使用 12 個月**（自初次處方起 1 年）；每 12 週 i-RECIST 評估；3.(8)Ⅳ 的 SD 規則原文註明「durvalumab 用於非小細胞肺癌之鞏固治療不在此限」 | 共同停用條件；滿 12 個月即止。局限期 SCLC 的 durvalumab 鞏固（ADRIATIC）9.69 原文未見 |
| pembrolizumab、atezolizumab、cemiplimab：NSCLC 第一線單用 | 9.69.1.(2)第 2 項（114/6/1） | 轉移性 NSCLC 成人；非鱗狀需 EGFR/ALK/ROS-1 原生型，鱗狀需 EGFR/ALK 原生型；PD-L1：pembrolizumab 與 cemiplimab TPS≧50%，atezolizumab TC≧50% 或 IC≧10% | 是（P013）；每次 12 週 | 每 12 週 i-RECIST；pembrolizumab 與 cemiplimab 的 iSD 可續用；atezolizumab 評估 SD 可再用 12 週後再評估；最長 2 年 | 三藥擇一不得互換；atezolizumab 連續二次 SD 不得續用 |
| pembrolizumab、nivolumab、atezolizumab、tislelizumab：鱗狀 NSCLC 第二線單用 | 9.69.1.(2)第 3 項（本項無日期；1.(2) 標題 109/4/1、109/11/1、114/6/1、114/8/1） | 晚期鱗狀 NSCLC 成人；先前用過 platinum 類化療失敗後又惡化；EGFR/ALK 原生型；PD-L1 見表（P011） | 是（P011）；每次 12 週 | 每 12 週 i-RECIST；pembrolizumab、nivolumab、tislelizumab 的 iSD 可續用；atezolizumab 適用 SD 規則；最長 2 年 | 四藥擇一不得互換；atezolizumab 連續二次 SD 不得續用 |
| pembrolizumab、nivolumab、atezolizumab、tislelizumab：肺腺癌第三線單用 | 9.69.1.(2)第 4 項（日期同上） | 晚期非小細胞肺腺癌成人；先前用過 platinum 類及 docetaxel／paclitaxel 類二線（含）以上化療均失敗又惡化；EGFR/ALK/ROS-1 原生型；PD-L1 見表（P012） | 是（P012）；每次 12 週 | 同上列 | 同上列 |
| pembrolizumab、tislelizumab：鱗狀 NSCLC 第一線併用化療 | 9.69.2.(2)第 2 項（115/10/1） | 轉移性鱗狀 NSCLC：pembrolizumab 或 tislelizumab ＋ carboplatin ＋ paclitaxel，**至多 4 個療程**，接續單用同一種免疫藥；PD-L1：pembrolizumab TPS 1~49%，tislelizumab 不需檢附報告。本項未列基因條件，但 3.(7)Ⅰ 規定 NSCLC 初次申請要附符合給付適應症內容的基因檢測報告 | 是（P014）；每次 12 週 | 併用至多 4 個療程後單用；每 12 週 i-RECIST；iSD 可續用；最長 2 年 | 兩藥擇一不得互換 |
| pembrolizumab、tislelizumab、atezolizumab：非鱗狀 NSCLC 第一線併用 | 9.69.2.(2)第 3 項（115/10/1） | 轉移性、不具 EGFR/ALK/ROS-1 腫瘤基因異常的非鱗狀 NSCLC：pembrolizumab 或 tislelizumab ＋ pemetrexed（限 Pexeda、Apeta、Pemetrexed Sandoz 或 Alimta Avos）＋含鉑化療；或 atezolizumab ＋ bevacizumab（限 Alymsys、Avastin、Abevmy、Vegzelma 或 Mvasi）＋ carboplatin ＋ paclitaxel。PD-L1：pembrolizumab、atezolizumab 不需檢附報告，tislelizumab TC≧50% | 是（P013）；每次 12 週 | 本項沒有訂化療療程上限；每 12 週 i-RECIST；pembrolizumab 與 tislelizumab 的 iSD 可續用；atezolizumab 適用 SD 規則；最長 2 年 | 三種組合擇一不得互換；atezolizumab ＋ bevacizumab 是 3.(4)「不可合併申報標靶藥物」的明文例外 |
| nivolumab：NSCLC 術前輔助 | 9.69.2.(2)第 1 項（115/8/1） | 可切除（腫瘤≧4 公分或淋巴結陽性 N1/N2，排除 N3，且無疾病轉移 M0）、不具 EGFR 或 ALK 腫瘤基因異常的成人。非鱗狀：nivolumab ＋ pemetrexed（限上列 4 個廠牌）＋含鉑化療；鱗狀：nivolumab ＋含鉑化療。PD-L1 不需檢附報告 | 是（P016）；每次 12 週 | **至多 3 個療程**；術前之後接續單用 nivolumab 的給付，原文未見 | 共同停用條件；滿 3 個療程即止 |
| atezolizumab、durvalumab：擴散期 SCLC | 9.69.2.(3)（114/2/1） | 擴散期（extensive stage）SCLC 成人，先前未曾接受化療，且無腦部或無脊髓轉移：atezolizumab ＋ carboplatin ＋ etoposide，或 durvalumab ＋ etoposide ＋（carboplatin 或 cisplatin 兩者之一）。PD-L1 不需檢附報告 | 是（P021）；每次 12 週 | 本項沒有訂化療療程上限；每 12 週 i-RECIST；最長 2 年；SD 可再用 12 週，連續二次 SD 不得續用 | 兩藥擇一不得互換 |

**9.69 原文找不到文字的肺癌用法**

9.69 的肺癌給付只有上表這 8 列，下列用法沒有任何給付文字：NSCLC 術後輔助免疫治療（IMpower010、PEARLS）、pembrolizumab 或 durvalumab 的圍術期治療（KEYNOTE-671、AEGEAN）、nivolumab 圍術期的術後部分（CheckMate 77T）、局限期 SCLC 的 durvalumab 鞏固（ADRIATIC）、nivolumab ＋ ipilimumab（CheckMate 9LA）、durvalumab ＋ tremelimumab ＋化療（POSEIDON）、cemiplimab 併用化療。ipilimumab 在 9.69 沒有肺癌用法；原文點名的併用適應症只有惡性肋膜間皮瘤（9.69.2.(4)，併 nivolumab），黑色素瘤條文（9.69.1.(1)）寫「本類藥品」，本手冊未逐一確認 ipilimumab 單用是否可申請。tremelimumab 在 9.69 沒有肺癌用法，原文點名的用法為晚期肝細胞癌第一線併 durvalumab。

> [!WARNING]
> **免疫治療與標靶藥的先後順序**
> 9.69 對 NSCLC 免疫治療的基因條件是：非鱗狀病人要 EGFR/ALK/ROS-1 原生型，鱗狀病人要 EGFR/ALK 原生型（術前輔助則是不具 EGFR 或 ALK 異常）；例外是鱗狀 NSCLC 第一線併用化療（P014），該項條文未列基因條件，但 3.(7)Ⅰ 仍要求附符合給付適應症內容的基因檢測報告。這和 2.2 的臨床警示一致：基因報告出來之前不要先開免疫治療。此外，3.(4) 規定免疫治療無效後或給付時程期滿後，不再給付該適應症相關的標靶藥物；病人若先用免疫治療、之後才發現有驅動基因，後續標靶藥的給付要先和藥事部門確認，不要自行推定。

### 9.4 化療與抗血管新生藥物

化療條文大多只規定「給付於哪些癌別」，**條文本身沒有寫事前審查**；併用免疫治療的組合，要同時符合 9.69（事前審查、ECOG≦1、每 12 週評估，見 9.3）。下表只列與肺癌有關的部分。

| 藥品（商品名） | 條號（最新修訂） | 給付適應症與條件 | 事前審查 | 療程／續用評估 | 停用／互換／併用限制 |
|--------------|---------------|----------------|---------|--------------|------------------|
| carboplatin（Paraplatin） | 9.2（115/10/1） | 條文以「限」列舉（圈號是 9.2 的項次）。肺癌相關：②腎功能不佳（CCr<60）或曾作單側以上腎切除的惡性腫瘤；③轉移性鱗狀 NSCLC 第一線，與 pembrolizumab 或 tislelizumab 及 paclitaxel 併用；④擴散期 SCLC 成人，與 atezolizumab 或 durvalumab 及 etoposide 併用；⑤轉移性且不具 EGFR/ALK/ROS-1 異常的非鱗狀 NSCLC 第一線，與 pembrolizumab 及 pemetrexed 併用，或與 atezolizumab 及 bevacizumab、paclitaxel 併用（兩者的 pemetrexed、bevacizumab 廠牌限制同 9.3）；⑦EGFR exon 20 插入突變 NSCLC 第一線，與 amivantamab 及 pemetrexed 併用；⑧可切除、不具 EGFR 或 ALK 異常 NSCLC 的術前輔助，與 nivolumab 併用。③④⑤⑧都要求病人符合免疫檢查點抑制劑的給付規定 | 9.2 沒有寫；併用免疫治療者依 9.69 | ⑧至多 3 個療程；③依 9.69 化療併用至多 4 個療程，接續單用免疫藥；其他沒有訂 | 原文未列停用條件；沒有擇一或互換規定 |
| docetaxel | 9.3（115/8/1） | 本類藥品（除 Doce 外）在許可證登載的適應症範圍內，給付於乳癌、NSCLC、前列腺癌、頭頸癌及胃腺癌。Doce 及 Phyxotere 的 NSCLC 寫為「局部晚期或轉移性非小細胞肺癌」。肺癌沒有限線別與組織型。併用標靶或免疫治療時，須符合該藥的給付規定 | 條文沒有寫 | 肺癌未訂療程或評估頻率 | 原文未列停用條件 |
| gemcitabine（Gemzar） | 9.4（115/9/1） | 在許可證登載的適應症範圍內，給付於 NSCLC、胰臟癌、膀胱癌、乳癌、卵巢癌及膽道癌；肺癌沒有限線別、期別、組織型。併用標靶或免疫治療時，須符合該藥的給付規定 | 條文沒有寫 | 條文沒有寫 | 原文未列停用條件 |
| paclitaxel 注射劑 | 9.5.1（115/10/1） | ①除 GENETAXYL CREM LESS 及 TAXOL 外，在許可證登載的適應症範圍內給付於卵巢癌、NSCLC、乳癌及卡波西氏肉瘤。②GENETAXYL CREM LESS 與 TAXOL：NSCLC 作為第一線用藥時**需與 cisplatin 併用**。③併用免疫治療：轉移性鱗狀 NSCLC 第一線，與 pembrolizumab 或 tislelizumab 及 carboplatin 併用；轉移性非鱗狀 NSCLC 第一線，與 atezolizumab 及 bevacizumab（限 Alymsys、Avastin、Abevmy、Vegzelma 或 Mvasi）、carboplatin 併用 | 9.5.1 沒有寫；併用免疫治療者依 9.69 | 9.5.1 肺癌未訂療程；鱗狀 NSCLC 的免疫併用依 9.69 至多 4 個療程 | 原文未列停用條件 |
| albumin-based paclitaxel（Abraxane） | 9.5.2（108/11/1） | 只給付於轉移性胰腺癌第一線併用 gemcitabine，**肺癌原文未見** | 條文沒有寫 | 條文沒有寫 | 原文未列 |
| vinorelbine | 9.9（106/11/1） | ①晚期或無法手術切除的 NSCLC，以及轉移性乳癌。②病理分期第二期及第三期前半（stage II & IIIA）的 NSCLC，於根治性手術後與鉑金類藥品併用的輔助治療，最多 4 療程 | 條文沒有寫（附表九之十二寫有事前審查，與條文不一致，見 9.6） | 輔助治療最多 4 療程；晚期用途未訂 | 原文未列停用條件；口服劑型與注射劑型不得併用 |
| uracil-tegafur（Ufur） | 9.11（100/1/1） | 第 3 項：與 cisplatin 併用治療轉移及末期肺癌。第 5 項：病理分期為 T2 且腫瘤≧3 cm 的肺腺癌，作為手術後輔助治療 | 條文沒有寫 | 第 5 項使用期限以 2 年為限 | 原文未列停用條件 |
| irinotecan（Campto） | 9.12（114/12/1）；9.12.1（112/2/1） | 只給付於轉移性大腸直腸癌第一線，以及轉移性胰臟癌第一線 FOLFIRINOX（限指定廠牌）；**沒有肺癌（含 SCLC）適應症** | 9.12.1 沒有寫（微脂體 9.12.2 需事前審查，僅用於胰腺癌） | 條文沒有寫 | 原文未列 |
| topotecan（Hycamtin） | 9.16（100/6/1）：注射劑 9.16.1（98/11/1）、口服 9.16.2（100/6/1） | 注射劑：限卵巢癌及小細胞肺癌的**第二線**化學治療（第一線應包括白金化合物），另有子宮頸癌。口服劑型：限 SCLC 的第二線化學治療（第一線應包括白金化合物） | 條文沒有寫 | 條文沒有寫 | 原文未列；注射劑與口服劑型之間沒有寫併用或互換限制 |
| pemetrexed（Alimta） | 9.26（115/10/1） | 肺癌各項中，(2)(3)排除顯著鱗狀細胞組織型，(4)(6)明寫非鱗狀，(5)amivantamab 組合條文未限組織型。(2)單一藥物：以含鉑化療治療，或 70 歲以上接受過第一線化療，但仍失敗的局部晚期或轉移性 NSCLC。(3)第一線併含鉑化療：局部晚期或轉移性 NSCLC，**ECOG 0~1**。(4)第一線併 pembrolizumab 或 tislelizumab 及含鉑化療：轉移性、不具 EGFR/ALK/ROS-1 異常的非鱗狀 NSCLC。(5)第一線併 amivantamab 及 carboplatin：EGFR exon 20 插入突變的局部晚期或轉移性 NSCLC 成人。(6)術前輔助併 nivolumab 及含鉑化療：非鱗狀 NSCLC。(4)與(6)限用 Pexeda、Apeta、Pemetrexed Sandoz 或 Alimta Avos，且病人須符合免疫檢查點抑制劑的給付規定 | 條文沒有寫；(4)(6)的免疫組合依 9.69（附表八之三見 9.6） | **每 4 個療程需進行療效評估，病歷應留存評估紀錄，無疾病惡化方可繼續使用**（第 2 項，全條適用）；原文未設總療程上限 | 疾病惡化即不可繼續；沒有擇一或互換規定 |
| bevacizumab（Avastin）：非鱗狀 NSCLC | 9.37 第 5、7 項（114/10/1） | 第 5 項與 erlotinib 併用的第一線（EGFR Exon 21 L858R、腦轉移），見 9.1。第 7 項：bevacizumab（限 Alymsys、Avastin、Abevmy、Vegzelma 或 Mvasi）＋ atezolizumab ＋ carboplatin ＋ paclitaxel，轉移性非鱗狀 NSCLC 第一線，病人須符合免疫檢查點抑制劑的給付規定 | 第 5 項是（每次 12 週）；第 7 項本身沒有寫，免疫部分依 9.69 事前審查 | 第 5 項每 12 週再申請，須證實無惡化；第 7 項依 9.69 每 12 週評估 | 第 5 項：未證實無惡化即不得續用。第 7 項：9.69 3.(4) 明文允許與 atezolizumab 合併申報 |
| ramucirumab（Cyramza） | 9.92（110/5/1） | 只給付於 sorafenib 治療失敗後、AFP≧400 ng/mL 的 Child-Pugh A 晚期肝細胞癌；**沒有肺癌適應症** | 是（肝細胞癌：初次 12 週） | 肝細胞癌：之後每 8 週評估 | 肝細胞癌：疾病惡化即停；與 regorafenib、nivolumab 擇一 |
| cisplatin、etoposide | 無專條 | 第 9 節沒有這兩個藥的條號。cisplatin 只作為併用藥出現在他條（如 9.5.1 的 GENETAXYL CREM LESS／TAXOL、9.26 的惡性肋膜間質細胞瘤、9.69 的 SCLC durvalumab 組合）；etoposide 只出現在 9.2 第 4 項與 9.69 的擴散期 SCLC 條文 | — | — | — |

**判讀提醒**

- **docetaxel ＋ ramucirumab（REVEL）**：ramucirumab 在 9.92 只給付肝細胞癌，肺癌二線的 ramucirumab 原文未見給付；docetaxel 單用則有 9.3 的 NSCLC 給付。
- **pemetrexed 的廠牌限制**：與 pembrolizumab、tislelizumab 或 nivolumab 併用時，pemetrexed 只限 Pexeda、Apeta、Pemetrexed Sandoz 或 Alimta Avos；bevacizumab 與 atezolizumab 併用時只限 Alymsys、Avastin、Abevmy、Vegzelma 或 Mvasi。開醫囑與送審前先確認品項。
- **pemetrexed 的 ECOG 條件**：只有 9.26 1.(3)（第一線併含鉑化療）明寫 ECOG 0~1；(4)(6) 的免疫組合適用 9.69 的 ECOG≦1。

> [!CAUTION]
> **待核對：沒有併用免疫治療的 carboplatin、以及兩個 paclitaxel 品牌**
> ①9.2 是用「限」字列舉給付範圍，肺癌的單純化療（沒有併用免疫治療或 amivantamab），例如 carboplatin ＋ pemetrexed、carboplatin ＋ paclitaxel、局限期 SCLC 的 carboplatin ＋ etoposide，照條文字面只有第 2 項（CCr<60 或曾作單側以上腎切除）可以對應。是否另有給付依據，條文沒有說明，開立前向藥事部門確認。②9.2 第 5 項只列 pembrolizumab ＋ pemetrexed，但 9.26 1.(4) 與 9.69 已把 tislelizumab ＋ pemetrexed ＋含鉑化療列入非鱗狀第一線；tislelizumab 組合若用 carboplatin，9.2 第 5 項沒有對應文字，請另行核對。③GENETAXYL CREM LESS 與 TAXOL 在 NSCLC 第一線限與 cisplatin 併用（9.5.1 第 2 項），但 9.5.1 第 3.(1)、3.(3) 項的 carboplatin 免疫組合沒有排除這兩個品牌，用它們做 carboplatin 組合是否給付，原文沒有說清楚。

### 9.5 本章提到、但第 9 節沒有條文的藥

下表的藥，在 115/10/22 版第 9 節用學名與商品名逐一搜尋，**原文未見**，也就是沒有健保給付。有台灣藥證的藥（見 4.5）可以合法處方，但沒有健保給付時，費用怎麼處理（自費或院內其他安排）由主治醫師與院內流程決定；有藥證、有健保、院內有進藥是三件事，要分開回答病人。

| 藥品 | 本章出現的位置 | 115/10/22 版原文 | 說明 |
|------|--------------|----------------|------|
| lazertinib | 4.3 EGFR 第一線選項、4.5 | 原文未見 | amivantamab ＋ lazertinib（MARIPOSA）用於 ex19del／L858R 第一線的用法沒有給付文字；9.126 的 amivantamab 只給付 exon 20 插入突變、併 carboplatin 與 pemetrexed |
| capmatinib | 4.3、5.4、6.3 | 原文未見 | MET exon 14 skipping 只有 tepotinib（9.101）有條文 |
| selpercatinib、pralsetinib | 4.3、5.4、6.3 | 原文未見 | RET 融合沒有任何給付文字 |
| sotorasib、adagrasib | 4.3、5.4 | 原文未見 | KRAS G12C 沒有任何給付文字 |
| lurbinectedin | 4.4、4.5、5.3 | 原文未見 | 第一線維持（IMforte）與復發 SCLC 的用法都沒有給付文字 |
| tarlatamab | 4.4、4.5、5.3 | 原文未見 | 台灣已有藥證（4.5）；復發 SCLC 的給付文字沒有 |
| sevabertinib、zongertinib | 4.3、4.5、6.3 | 原文未見 | HER2 突變 NSCLC 沒有任何標靶藥給付文字 |
| sunvozertinib | 4.3、4.5 | 原文未見 | 無台灣藥證，也無健保 |
| taletrectinib | 4.3、4.5 | 原文未見 | ROS1 只有 crizotinib、entrectinib、repotrectinib 有條文 |
| datopotamab deruxtecan | 4.3、4.5、6.3 | 原文未見 | 無台灣肺癌藥證，也無健保 |
| encorafenib ＋ binimetinib | 4.3（BRAF V600E 選項） | binimetinib 原文未見；encorafenib 只有 9.134 的結直腸癌條文 | NSCLC 的 BRAF V600E 只有 dabrafenib ＋ trametinib（9.91）有條文 |

**有條文，但本章用到的肺癌用法原文未見**

| 藥品 | 有條文的部分 | 本章的肺癌用法（原文未見給付文字） |
|------|------------|--------------------------------|
| osimertinib（9.80） | 第一線、T790M 第二線 | 術後輔助 3 年（ADAURA）、CCRT 後鞏固（LAURA） |
| alectinib（9.60） | ALK 陽性晚期 NSCLC 第一線 | 術後輔助 2 年（ALINA） |
| amivantamab（9.126） | exon 20 插入突變第一線，併 carboplatin 與 pemetrexed | ex19del／L858R 的 MARIPOSA 用法、MARIPOSA-2 用法、皮下劑型 |
| trastuzumab deruxtecan（9.115） | 乳癌 | HER2 突變 NSCLC 二線 |
| entrectinib（9.93） | ROS-1 陽性 NSCLC | NTRK 融合（larotrectinib 的 9.95 另有 NTRK 條文） |
| ramucirumab（9.92） | 肝細胞癌 | docetaxel ＋ ramucirumab 二線（REVEL） |
| albumin-based paclitaxel（9.5.2） | 轉移性胰腺癌 | nab-paclitaxel 的鱗狀 NSCLC 免疫組合 |
| irinotecan（9.12） | 大腸直腸癌、胰臟癌 | 復發 SCLC 的選項 |
| 免疫檢查點抑制劑（9.69） | 見 9.3 的 8 個肺癌適應症 | 術後輔助、圍術期、局限期 SCLC durvalumab 鞏固、nivolumab ＋ ipilimumab、durvalumab ＋ tremelimumab、cemiplimab 併用化療；avelumab 與 dostarlimab 在肺癌各列都是「尚未給付」 |

> [!NOTE]
> **病人問「這個藥可以用嗎」**
> 先分三層回答：①有沒有台灣藥證（TFDA；見 4.5）；②有沒有健保給付、符不符合條件（本段）；③院內有沒有進藥。原文未見代表 115/10/22 版第 9 節沒有條文，不代表藥物無效或不該用；這類藥若指引建議，由主治醫師與病人討論自費或其他途徑，專師的角色是把三層的狀態講清楚。

### 9.6 專師送事前審查前的檢核

**先講結論：** 事前審查被退件的原因，本手冊沒有原文可查，不推測；能做的是把原文要求的文件一項一項備齊，並把「條文怎麼寫」和「病人怎麼分類」逐字對照。

| 藥品群組 | 初次申請（或病歷留存）要備的文件 | 續用要備的文件 |
|---------|------------------------------|--------------|
| 所有事前審查案件的共同底線 | 病理或細胞檢查報告（該條寫「肺腺癌」就附肺腺癌，寫「非小細胞肺癌」就附 NSCLC）；符合通則十二的生物標記檢測報告；期別、線別、組織型照條文用字填寫 | 治療後的相關臨床資料與影像，證實無惡化 |
| osimertinib、aumolertinib 第一線 | 肺腺癌或 NSCLC 的病理或細胞檢查報告；EGFR 基因檢測報告（Exon 19 Del 或 Exon 21 L858R；通則十二） | 每 3 個月再申請：影像等資料證實無惡化；給藥 4 週後追蹤影像，每 8 至 12 週完整療效評估 |
| osimertinib、aumolertinib 第二線 | 同上，另加：EGFR T790M 報告；曾用 gefitinib、erlotinib、afatinib 或 dacomitinib 的證明；目前惡化的影像（可測量病灶優先，無則可評估病灶） | 同上 |
| gefitinib、erlotinib、afatinib、dacomitinib（條文不需事前審查） | 病歷留存：病理或細胞檢查報告、EGFR-TK 基因突變檢測報告（第一線）；第二線以上留存前線化療證明與惡化影像；erlotinib 維持療法留存 4 週期含鉑化療後 SD 的影像 | 每次處方 ≤4 週；再次處方時於病歷記錄臨床資料（每 4 週影像追蹤，每 8 至 12 週完整療效評估） |
| bevacizumab ＋ erlotinib | EGFR Exon 21 L858R 活化性突變檢測報告（通則十二；原文只明列這一項，但適應症要求第 IV 期、無法手術切除、腦轉移，病歷要對得上） | 每 12 週再申請：客觀證據（如影像學）證實無惡化 |
| amivantamab ＋ carboplatin ＋ pemetrexed | NSCLC 病理或細胞檢查報告；EGFR exon 20 插入突變分析檢測報告（通則十二） | 每 3 個月再申請：附療效評估資料；pemetrexed 每 4 個療程評估並留存紀錄 |
| ALK TKI、ROS-1 TKI | NSCLC 病理或細胞檢查報告；ALK 或 ROS-1 突變檢測報告（通則十二）。後線藥（lorlatinib、brigatinib、repotrectinib）的適應症是「在特定前線藥物治療中惡化」，原文沒有另列檢附文件，病歷要看得出前一線用藥與惡化 | 每 3 個月再申請：給藥 4 週後影像，往後每 4 週胸部 X 光，每 3 個月（entrectinib、repotrectinib 為每隔 8 週）評估藥效的影像 |
| dabrafenib ＋ trametinib、tepotinib、larotrectinib | NSCLC 病理或細胞檢查報告；BRAF V600E、MET exon 14 skipping 或 NTRK 融合的檢測報告（通則十二）；dabrafenib ＋ trametinib 的適應症是第一線含鉑化療後惡化，原文沒有另列這項檢附文件，但病歷要看得出前線用藥與惡化；larotrectinib 原文初次申請只列 NTRK 融合檢測報告，適應症依 9.95 對應的成人 NSCLC 條件對照 | 每 3 個月（larotrectinib 每 12 週）再申請：附治療後臨床資料或療效評估資料，證實無惡化或無進展 |
| 免疫檢查點抑制劑（9.69） | 病理或細胞檢查報告；NSCLC 的腫瘤基因檢測報告與 PD-L1 報告（皆符合通則十二；PD-L1 表標示免附者除外）；ECOG≦1 與心肺肝腎功能評估；12 週內影像（不含 PET）；先前治療與完整用藥資料（含自費）及結果；treatment protocol；其他佐證病歷 | 每 12 週：12 週內的 ECOG 與器官功能、i-RECIST 療效反應資料、影像報告（不含 PET）、其他佐證病歷。結束治療、停藥、未通過續用或達給付時程時，28 天內於 VPN 登錄結案 |

**送審前的小提醒（都來自原文）**

- **記下每個藥的送審週期**：3 個月（EGFR 第三代 TKI、ALK 與 ROS-1 TKI、amivantamab、dabrafenib ＋ trametinib、tepotinib）、12 週（免疫治療、bevacizumab ＋ erlotinib、larotrectinib）。
- **換藥前先對照新藥的第一線條件**：EGFR 第一線 TKI 之間互換，除耐受性不良外不允許，而且換入的藥必須符合自己的第一線條件（例如 dacomitinib 要無腦轉移）。
- **確認廠牌**：pemetrexed 與免疫治療併用只限 Pexeda、Apeta、Pemetrexed Sandoz、Alimta Avos；bevacizumab 與 atezolizumab 併用只限 Alymsys、Avastin、Abevmy、Vegzelma、Mvasi。
- **影像不含 PET**：免疫治療送審與續用的影像給付範圍不包括正子造影。
- **合併其他藥時，要同時符合各藥的規定**：docetaxel、gemcitabine、paclitaxel 與標靶或免疫治療併用時，病人須符合併用藥自己的給付規定。

> [!CAUTION]
> **待核對：原文裡的舊版申請表（附表）**
> 第 9 節原文附有 附表九之一（gefitinib 申請表）、附表九之二（erlotinib 申請表）、附表八之三（pemetrexed 申請表）、附表九之十二（vinorelbine 申請表），但 9.24、9.29、9.26、9.9 的現行條文都沒有引用這些附表，表單內容也和現行條文不一致：附表九之一把期別寫成「第 IIIB 期或第 IV 期」，並寫有「需經事前審查核准後使用」與每三個月再申請，但 9.24 條文沒有規定事前審查；附表九之二只列第二線與第三線；附表八之三只列 Alimta，勾選項是舊的 1.(1) 至 (3)；附表九之十二把輔助治療寫成需事前審查，但 9.9 條文沒有這四個字。這些表單現在是否仍要填，原文看不出來，以院內藥事部門與健保署實際要求為準。9.69 的「PD-L1 表」是條文內附的表格，不是申請表。

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

**答案：B**。葉酸要在第一劑前 7 天開始每日服用（美國仿單；歐盟仿單寫法為第一劑前 7 天內至少吃 5 天），兩種寫法都不是「第一劑當天才開始」，所以 A 錯；B12 第一劑前 1 週打、之後每 9 週；dexamethasone 是預防皮疹。CrCl <45 是不給 pemetrexed。

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

**Q15.** 依 RECIST 1.1，目標病灶直徑總和基線為 50 mm、治療中最小值 40 mm，現在增加到 47 mm，沒有新病灶，評估為？

A. PR　B. SD　C. PD　D. 無法評估

<details>
<summary>答案與詳解</summary>

**答案：B**。與最小值比 (47 − 40) ÷ 40 = 17.5%，未達 PD 要求的 20%（雖然絕對值增加 7 mm 已超過 5 mm，兩個條件要同時成立）；與基線比 (50 − 47) ÷ 50 = 6%，也未達 PR 要求的縮小 30%，所以是 SD。注意 PD 以治療中最小值（含基線）為參考、PR 以基線為參考：比最小值的增加未達 PD 標準時，若現在總和仍比基線小 ≥30%，即使比最小值變大，該次評估仍是 PR；反過來，只要達到 PD 標準（或出現新病灶），即使總和仍比基線小很多，也是 PD。

</details>

**Q16.** 肺鱗狀細胞癌病人血鈣 13.2 mg/dL，最可能的機轉是？

A. 骨轉移造成的局部溶骨，與荷爾蒙無關　B. 腫瘤分泌 PTHrP　C. 維生素 D 中毒　D. 原發性副甲狀腺亢進

<details>
<summary>答案與詳解</summary>

**答案：B**。鱗狀細胞癌最常見的副腫瘤高血鈣機轉是 PTHrP（humoral hypercalcemia of malignancy）。

</details>

**Q17.** 病人第一次使用 tarlatamab（C1D1 1 mg、C1D8 10 mg），下列哪一項符合美國仿單 2026-09 版的做法？

A. C1D1 與 C1D8 輸注前 1 小時內 dexamethasone 8 mg IV、輸注後 NS 1 L，並自輸注開始監測 6–8 小時　B. 只有 C1D1 需要前置用藥，C1D8 不需要　C. 前兩劑之後不需要再做輸注後觀察　D. 出現 1 級 CRS 就要永久停藥

<details>
<summary>答案與詳解</summary>

**答案：A**。前置用藥與水化在 C1D1 與 C1D8 都要做（B 錯）。之後每一劑仍要輸注後觀察：C1D15 與第 2 週期 6–8 小時、第 3–4 週期 3–4 小時、第 5 週期起 2 小時（C 錯）。1 級 CRS 是暫停到緩解後在下次排定劑量恢復，永久停藥的條件是 4 級 CRS（第一次出現就停）或再發的 3 級 CRS（D 錯）（Amgen, 2026）。台灣核准仿單與院內 protocol 的留觀時間可能不同（美國 2026-07 以前的版本是 22–24 小時），以院內為準。

</details>

**Q18.** 使用 bevacizumab 的病人，給藥前尿液試紙 2+。最適當的下一步是？

A. 照常給藥，下次再驗　B. 收 24 小時尿；若 ≥2 g/24 小時就暫停，降到 <2 g/24 小時才恢復　C. 立即永久停藥　D. 用尿蛋白／肌酸酐比值（UPCR）取代 24 小時尿，數值不高就照常給藥

<details>
<summary>答案與詳解</summary>

**答案：B**。仿單：試紙 ≥2+ 要做 24 小時尿；蛋白尿 ≥2 g/24 小時暫停，降到 <2 g/24 小時再恢復；發生腎病症候群才永久停藥（C 錯）。仿單也指出 UPCR 與 24 小時尿蛋白的相關性差（D 錯）（Genentech, 2025b）。另一個必背數字：擇期手術前至少 28 天停藥。

</details>

**Q19.** ALK 陽性病人正在服用 lorlatinib，因結核病要加開含 rifampin 的處方。最正確的處理是？

A. 同時使用，lorlatinib 加量到 150 mg　B. Lorlatinib 與強效 CYP3A 誘導劑併用為禁忌，先聯絡主治醫師、感染科與藥劑部　C. 只需要追蹤血糖　D. 兩者沒有交互作用

<details>
<summary>答案與詳解</summary>

**答案：B**。Lorlatinib 仿單把強效 CYP3A 誘導劑列為禁忌，與 rifampin 併用的健康受試者 10/12 出現嚴重肝毒性；開始 lorlatinib 前要先停誘導劑達 3 個血漿半衰期（Pfizer, 2026a）。相對地，osimertinib 是無法避免時加到 160 mg（AstraZeneca, 2026），gefitinib 加到 500 mg（AstraZeneca, 2023），alectinib 不受影響（Genentech, 2026a）。

</details>

**Q20.** 病人術前 FEV1 與 DLCO 都是預測值的 80%，預定做右下葉切除（5 個肺節）。ppoFEV1 約多少？下一步是？

A. 約 59%，先做爬樓梯或 shuttle walk　B. 約 59%，不需要其他檢查直接手術　C. 約 74%，不需要其他檢查　D. 約 29%，直接做 CPET

<details>
<summary>答案與詳解</summary>

**答案：A**。ppoFEV1 ＝ 80% ×（1 − 5 × 0.0526）≈ 59%（Zeiher et al., 1995）；DLCO 算法相同。介於 60% 與 30% 之間，先做低科技運動測試（爬樓梯高度 >22 m 或 shuttle walk 距離 >400 m 為及格）；兩者都 >60% 才可以不再檢查；<30% 或運動測試不及格做 CPET（Brunelli et al., 2013）。

</details>

---

## 12. 參考文獻

APA 第 7 版。作者超過 20 位時列前 19 位、省略號與最後一位。每筆附 DOI 與 PMID，2026-10-29 於 PubMed 核對；2026-11-01 新增的文獻同樣在 PubMed 核對。藥品仿單取自 DailyMed（2026-10-30 版資料庫），列出仿單版本與生效日。

Abernethy, A. P., McDonald, C. F., Frith, P. A., Clark, K., Herndon, J. E., II, Marcello, J., Young, I. H., Bull, J., Wilcock, A., Booth, S., Wheeler, J. L., Tulsky, J. A., Crockett, A. J., & Currow, D. C. (2010). Effect of palliative oxygen versus room air in relief of breathlessness in patients with refractory dyspnoea: A double-blind, randomised controlled trial. *The Lancet, 376*(9743), 784–793. https://doi.org/10.1016/S0140-6736(10)61115-4（PMID: 20816546）

Ahn, M.-J., Lisberg, A., Goto, Y., Sands, J., Hong, M. H., Paz-Ares, L., Pons-Tostivint, E., Pérol, M., Felip, E., Sugawara, S., Hayashi, H., Cho, B. C., Blumenschein, G., Jr., Shum, E., Lee, J.-S., Heist, R. S., Cornelissen, R., Chang, W.-C., Kowalski, D., . . . Okamoto, I. (2025). A pooled analysis of datopotamab deruxtecan in patients with EGFR-mutated NSCLC. *Journal of Thoracic Oncology, 20*(11), 1669–1682. https://doi.org/10.1016/j.jtho.2025.06.002（PMID: 40516821）

Alembic Pharmaceuticals Limited. (2024). *Erlotinib tablets: Prescribing information* (version 3, effective 2024-06-10) [Generic of Tarceva®; Tarceva 原廠仿單未列於 DailyMed，以同文字的學名藥仿單為準]. https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=ab6f3cb3-34a8-4492-a5d7-fb6b055a2d6b

Altorki, N., Wang, X., Kozono, D., Watt, C., Landrenau, R., Wigle, D., Port, J., Jones, D. R., Conti, M., Ashrafi, A. S., Liberman, M., Yasufuku, K., Yang, S., Mitchell, J. D., Pass, H., Keenan, R., Bauer, T., Miller, D., Kohman, L. J., . . . Vokes, E. (2023). Lobar or sublobar resection for peripheral stage IA non-small-cell lung cancer. *New England Journal of Medicine, 388*(6), 489–498. https://doi.org/10.1056/NEJMoa2212083（PMID: 36780674）

Amgen Inc. (2025). *LUMAKRAS (sotorasib) tablets: Prescribing information* (effective 2025-01-22). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=c80a362c-7ac3-4894-a076-0691e68ef8c1

Amgen Inc. (2026). *IMDELLTRA (tarlatamab-dlle) for injection: Prescribing information* (version 8, effective 2026-09-11). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=1e7b6163-5d83-42ea-82c9-cf7620cdc782

Anastasopoulou, A., Ziogas, D. C., Samarkos, M., Kirkwood, J. M., & Gogas, H. (2019). Reactivation of tuberculosis in cancer patients following administration of immune checkpoint inhibitors: Current evidence and clinical practice recommendations. *Journal for ImmunoTherapy of Cancer, 7*(1), Article 239. https://doi.org/10.1186/s40425-019-0717-7（PMID: 31484550）

Antonia, S. J., Villegas, A., Daniel, D., Vicente, D., Murakami, S., Hui, R., Yokoi, T., Chiappori, A., Lee, K. H., de Wit, M., Cho, B. C., Bourhaba, M., Quantin, X., Tokito, T., Mekhail, T., Planchard, D., Kim, Y.-C., Karapetis, C. S., Hiret, S., . . . Özgüroğlu, M. (2017). Durvalumab after chemoradiotherapy in stage III non-small-cell lung cancer. *New England Journal of Medicine, 377*(20), 1919–1929. https://doi.org/10.1056/NEJMoa1709937（PMID: 28885881）

Arcasoy, S. M., & Jett, J. R. (1997). Superior pulmonary sulcus tumors and Pancoast's syndrome. *New England Journal of Medicine, 337*(19), 1370–1376. https://doi.org/10.1056/NEJM199711063371907（PMID: 9358132）

AstraZeneca Pharmaceuticals LP. (2023). *IRESSA (gefitinib) tablets: Prescribing information* (effective 2023-02-28). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=827d60e8-7e07-41b7-c28b-49ef1c4a5a41

AstraZeneca Pharmaceuticals LP. (2026). *TAGRISSO (osimertinib) tablets: Prescribing information* (effective 2026-09-14). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=5e81b4a7-b971-45e1-9c31-29cea8c87ce7

Bae, S. Y., Lee, H., Na, K. J., Na, B., Park, S., Park, I. K., Kang, C. H., & Kim, Y. T. (2022). Computed tomography volumetric analysis for predicting postoperative lung function for segmentectomy. *Interactive CardioVascular and Thoracic Surgery, 35*(2), Article ivac195. https://doi.org/10.1093/icvts/ivac195（PMID: 35876799）

Baize, N., Monnet, I., Greillier, L., Geier, M., Lena, H., Janicot, H., Vergnenegre, A., Crequit, J., Lamy, R., Auliac, J.-B., Letreut, J., Le Caer, H., Gervais, R., Dansin, E., Madroszyk, A., Renault, P.-A., Le Garff, G., Falchero, L., Berard, H., . . . Chouaid, C. (2020). Carboplatin plus etoposide versus topotecan as second-line treatment for patients with sensitive relapsed small-cell lung cancer: An open-label, multicentre, randomised, phase 3 trial. *The Lancet Oncology, 21*(9), 1224–1233. https://doi.org/10.1016/S1470-2045(20)30461-7（PMID: 32888454）

Barlesi, F., Yao, W., Duruisseaux, M., Doucet, L., Martínez, A. A., Gregorc, V., Juan-Vidal, O., Lu, S., De Bondt, C., de Marinis, F., Linardou, H., Kim, Y.-C., Jotte, R., Felip, E., Lo Russo, G., Reck, M., Michenzie, M. F., Yang, W., Meade, J. N., . . . Mok, T. S. K. (2025). Adagrasib versus docetaxel in KRASG12C-mutated non-small-cell lung cancer (KRYSTAL-12): A randomised, open-label, phase 3 trial. *The Lancet, 406*(10503), 615–626. https://doi.org/10.1016/S0140-6736(25)00866-9（PMID: 40783289）

Batchelor, T. J. P., Rasburn, N. J., Abdelnour-Berchtold, E., Brunelli, A., Cerfolio, R. J., Gonzalez, M., Ljungqvist, O., Petersen, R. H., Popescu, W. M., Slinger, P. D., & Naidu, B. (2019). Guidelines for enhanced recovery after lung surgery: Recommendations of the Enhanced Recovery After Surgery (ERAS®) Society and the European Society of Thoracic Surgeons (ESTS). *European Journal of Cardio-Thoracic Surgery, 55*(1), 91–115. https://doi.org/10.1093/ejcts/ezy301（PMID: 30304509）

Bayer HealthCare Pharmaceuticals Inc. (2026). *VITRAKVI (larotrectinib) capsules and oral solution: Prescribing information* (effective 2026-05-22). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=0c8ca614-58b2-4aa4-83d3-0387a8f782fd

Bibby, A. C., Dorn, P., Psallidas, I., Porcel, J. M., Janssen, J., Froudarakis, M., Subotic, D., Astoul, P., Licht, P., Schmid, R., Scherpereel, A., Rahman, N. M., Cardillo, G., & Maskell, N. A. (2018). ERS/EACTS statement on the management of malignant pleural effusions. *European Respiratory Journal, 52*(1), Article 1800349. https://doi.org/10.1183/13993003.00349-2018（PMID: 30054348）

Boehringer Ingelheim Pharmaceuticals, Inc. (2025). *GILOTRIF (afatinib) tablets: Prescribing information* (effective 2025-11-13). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=fd638e5e-8032-e7ca-0179-95e96ab5d387

Bristol-Myers Squibb Company. (2024). *AUGTYRO (repotrectinib) capsules: Prescribing information* (effective 2024-06-13). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=fb526827-40ba-4462-94cf-179ae3b0cb8a

Brunelli, A., Charloux, A., Bolliger, C. T., Rocco, G., Sculier, J.-P., Varela, G., Licker, M., Ferguson, M. K., Faivre-Finn, C., Huber, R. M., Clini, E. M., Win, T., De Ruysscher, D., & Goldman, L. (2009). ERS/ESTS clinical guidelines on fitness for radical therapy in lung cancer patients (surgery and chemo-radiotherapy). *European Respiratory Journal, 34*(1), 17–41. https://doi.org/10.1183/09031936.00184308（PMID: 19567600）

Brunelli, A., Kim, A. W., Berger, K. I., & Addrizzo-Harris, D. J. (2013). Physiologic evaluation of the patient with lung cancer being considered for resectional surgery: Diagnosis and management of lung cancer, 3rd ed: American College of Chest Physicians evidence-based clinical practice guidelines. *Chest, 143*(5, Suppl.), e166S–e190S. https://doi.org/10.1378/chest.12-2395（PMID: 23649437）

Caini, S., Del Riccio, M., Vettori, V., Scotti, V., Martinoli, C., Raimondi, S., Cammarata, G., Palli, D., Banini, M., Masala, G., & Gandini, S. (2022). Quitting smoking at or around diagnosis improves the overall survival of lung cancer patients: A systematic review and meta-analysis. *Journal of Thoracic Oncology, 17*(5), 623–636. https://doi.org/10.1016/j.jtho.2021.12.005（PMID: 34995798）

Camidge, D. R., Kim, H. R., Ahn, M.-J., Yang, J. C.-H., Han, J.-Y., Lee, J.-S., Hochmair, M. J., Li, J. Y.-C., Chang, G.-C., Lee, K. H., Gridelli, C., Delmonte, A., Garcia Campelo, R., Kim, D.-W., Bearz, A., Griesinger, F., Morabito, A., Felip, E., Califano, R., . . . Popat, S. (2018). Brigatinib versus crizotinib in ALK-positive non-small-cell lung cancer. *New England Journal of Medicine, 379*(21), 2027–2039. https://doi.org/10.1056/NEJMoa1810171（PMID: 30280657）

Cascone, T., Awad, M. M., Spicer, J. D., He, J., Lu, S., Sepesi, B., Tanaka, F., Taube, J. M., Cornelissen, R., Havel, L., Karaseva, N., Kuzdzal, J., Petruzelka, L. B., Wu, L., Pujol, J.-L., Ito, H., Ciuleanu, T.-E., de Oliveira Muniz Koch, L., Janssens, A., . . . Provencio Pulla, M. (2024). Perioperative nivolumab in resectable lung cancer. *New England Journal of Medicine, 390*(19), 1756–1769. https://doi.org/10.1056/NEJMoa2311926（PMID: 38749033）

Chang, G.-C., Chiu, C.-H., Yu, C.-J., Chang, Y.-C., Chang, Y.-H., Hsu, K.-H., Wu, Y.-C., Chen, C.-Y., Hsu, H.-H., Wu, M.-T., Yang, C.-T., Chong, I.-W., Lin, Y.-C., Hsia, T.-C., Lin, M.-C., Su, W.-C., Lin, C.-B., Lee, K.-Y., Wei, Y.-F., . . . Yang, P.-C. (2024). Low-dose CT screening among never-smokers with or without a family history of lung cancer in Taiwan: A prospective cohort study. *The Lancet Respiratory Medicine, 12*(2), 141–152. https://doi.org/10.1016/S2213-2600(23)00338-7（PMID: 38042167）

Chansky, K., Sculier, J.-P., Crowley, J. J., Giroux, D., Van Meerbeeck, J., & Goldstraw, P. (2009). The International Association for the Study of Lung Cancer Staging Project: Prognostic factors and pathologic TNM stage in surgically managed non-small cell lung cancer. *Journal of Thoracic Oncology, 4*(7), 792–801. https://doi.org/10.1097/JTO.0b013e3181a7716e（PMID: 19458556）

Chen, H.-W., Kuo, Y.-W., Chen, C.-Y., Chang, C.-H., Wang, S.-M., Chien, Y.-C., Lu, W.-C., Chen, J.-P., Chang, C.-Y., Wei, Y.-F., Chang, S.-C., Shu, C.-C., Wang, J.-Y., Liao, W.-Y., Wang, H.-C., & Yu, C.-J. (2024). Increased tuberculosis reactivation risk in patients receiving immune checkpoint inhibitor-based therapy. *The Oncologist, 29*(4), e498–e506. https://doi.org/10.1093/oncolo/oyad340（PMID: 38227604）

Cheng, Y., Spigel, D. R., Cho, B. C., Laktionov, K. K., Fang, J., Chen, Y., Zenke, Y., Lee, K. H., Wang, Q., Navarro, A., Bernabe, R., Buchmeier, E. L., Chang, J. W.-C., Shiraishi, Y., Sezgin Goksu, S., Badzio, A., Shi, A., Daniel, D. B., Hoa, N. T. T., . . . Senan, S. (2024). Durvalumab after chemoradiotherapy in limited-stage small-cell lung cancer. *New England Journal of Medicine, 391*(14), 1313–1327. https://doi.org/10.1056/NEJMoa2404873（PMID: 39268857）

Cho, B. C., Li, W., Spira, A. I., Sauder, M., Feldman, J., Bozorgmehr, F., Mak, M., Smith, J., Voon, P. J., Liu, B., Tian, P., Tan, J.-L., Yang, C.-T., Shih, J.-Y., Karadurmus, N., Cundom, J. E., Bertollo, G., Cicin, I., Nieva, J., . . . Girard, N. (2025). Enhanced versus standard dermatologic management with amivantamab-lazertinib in EGFR-mutated advanced NSCLC: The COCOON global randomized controlled trial. *Journal of Thoracic Oncology, 20*(10), 1517–1530. https://doi.org/10.1016/j.jtho.2025.07.117（PMID: 40923969）

Cho, B. C., Lu, S., Felip, E., Spira, A. I., Girard, N., Lee, J.-S., Lee, S.-H., Ostapenko, Y., Danchaivijitr, P., Liu, B., Alip, A., Korbenfeld, E., Mourão Dias, J., Besse, B., Lee, K.-H., Xiong, H., How, S.-H., Cheng, Y., Chang, G.-C., . . . Hayashi, H. (2024). Amivantamab plus lazertinib in previously untreated EGFR-mutated advanced NSCLC. *New England Journal of Medicine, 391*(16), 1486–1498. https://doi.org/10.1056/NEJMoa2403614（PMID: 38924756）

Clinical Practice Guideline Treating Tobacco Use and Dependence 2008 Update Panel, Liaisons, and Staff. (2008). A clinical practice guideline for treating tobacco use and dependence: 2008 update. A U.S. Public Health Service report. *American Journal of Preventive Medicine, 35*(2), 158–176. https://doi.org/10.1016/j.amepre.2008.04.009（PMID: 18617085）

Davidson, K., & Shojaee, S. (2020). Managing massive hemoptysis. *Chest, 157*(1), 77–88. https://doi.org/10.1016/j.chest.2019.07.012（PMID: 31374211）

Davies, H. E., Mishra, E. K., Kahan, B. C., Wrightson, J. M., Stanton, A. E., Guhan, A., Davies, C. W. H., Grayez, J., Harrison, R., Prasad, A., Crosthwaite, N., Lee, Y. C. G., Davies, R. J. O., Miller, R. F., & Rahman, N. M. (2012). Effect of an indwelling pleural catheter vs chest tube and talc pleurodesis for relieving dyspnea in patients with malignant pleural effusion: The TIME2 randomized controlled trial. *JAMA, 307*(22), 2383–2389. https://doi.org/10.1001/jama.2012.5535（PMID: 22610520）

de Koning, H. J., van der Aalst, C. M., de Jong, P. A., Scholten, E. T., Nackaerts, K., Heuvelmans, M. A., Lammers, J.-W. J., Weenink, C., Yousaf-Khan, U., Horeweg, N., van 't Westeinde, S., Prokop, M., Mali, W. P., Mohamed Hoesein, F. A. A., van Ooijen, P. M. A., Aerts, J. G. J. V., den Bakker, M. A., Thunnissen, E., Verschakelen, J., . . . Oudkerk, M. (2020). Reduced lung-cancer mortality with volume CT screening in a randomized trial. *New England Journal of Medicine, 382*(6), 503–513. https://doi.org/10.1056/NEJMoa1911793（PMID: 31995683）

de Langen, A. J., Johnson, M. L., Mazieres, J., Dingemans, A.-M. C., Mountzios, G., Pless, M., Wolf, J., Schuler, M., Lena, H., Skoulidis, F., Yoneshima, Y., Kim, S.-W., Linardou, H., Novello, S., van der Wekken, A. J., Chen, Y., Peters, S., Felip, E., Solomon, B. J., . . . Paz-Ares, L. (2023). Sotorasib versus docetaxel for previously treated non-small-cell lung cancer with KRASG12C mutation: A randomised, open-label, phase 3 trial. *The Lancet, 401*(10378), 733–746. https://doi.org/10.1016/S0140-6736(23)00221-0（PMID: 36764316）

Drapkin, B. J., Morrell, D. J., Grebla, R., Shechter, G., & Gerber, D. E. (2025). Marked under-diagnosis of Lambert-Eaton myasthenic syndrome in small cell lung cancer: An analysis of real-world claims data. *Frontiers in Oncology, 15*, Article 1650373. https://doi.org/10.3389/fonc.2025.1650373（PMID: 41179675）

Drilon, A., Camidge, D. R., Lin, J. J., Kim, S.-W., Solomon, B. J., Dziadziuszko, R., Besse, B., Goto, K., de Langen, A. J., Wolf, J., Lee, K. H., Popat, S., Springfeld, C., Nagasaka, M., Felip, E., Yang, N., Velcheti, V., Lu, S., Kao, S., . . . Cho, B. C. (2024). Repotrectinib in ROS1 fusion-positive non-small-cell lung cancer. *New England Journal of Medicine, 390*(2), 118–131. https://doi.org/10.1056/NEJMoa2302299（PMID: 38197815）

Drilon, A., Laetsch, T. W., Kummar, S., DuBois, S. G., Lassen, U. N., Demetri, G. D., Nathenson, M., Doebele, R. C., Farago, A. F., Pappo, A. S., Turpin, B., Dowlati, A., Brose, M. S., Mascarenhas, L., Federman, N., Berlin, J., El-Deiry, W. S., Baik, C., Deeken, J., . . . Hyman, D. M. (2018). Efficacy of larotrectinib in TRK fusion-positive cancers in adults and children. *New England Journal of Medicine, 378*(8), 731–739. https://doi.org/10.1056/NEJMoa1714448（PMID: 29466156）

Eli Lilly and Company. (2026a). *CYRAMZA (ramucirumab) injection: Prescribing information* (effective 2026-06-09). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=c6080942-dee6-423e-b688-1272c2ae90d4

Eli Lilly and Company. (2026b). *RETEVMO (selpercatinib) capsules and tablets: Prescribing information* (effective 2026-09-11). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=7fa848ba-a59c-4144-9f52-64d090f4d828

EMD Serono, Inc. (2025). *TEPMETKO (tepotinib) tablets: Prescribing information* (effective 2025-04-17). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=80a0f1b9-071a-47f5-9e67-32d638a669dc

Faivre-Finn, C., Snee, M., Ashcroft, L., Appel, W., Barlesi, F., Bhatnagar, A., Bezjak, A., Cardenal, F., Fournel, P., Harden, S., Le Pechoux, C., McMenemin, R., Mohammed, N., O'Brien, M., Pantarotto, J., Surmont, V., Van Meerbeeck, J. P., Woll, P. J., Lorigan, P., & Blackhall, F. (2017). Concurrent once-daily versus twice-daily chemoradiotherapy in patients with limited-stage small-cell lung cancer (CONVERT): An open-label, phase 3, randomised, superiority trial. *The Lancet Oncology, 18*(8), 1116–1125. https://doi.org/10.1016/S1470-2045(17)30318-2（PMID: 28642008）

Felip, E., Altorki, N., Zhou, C., Csőszi, T., Vynnychenko, I., Goloborodko, O., Luft, A., Akopov, A., Martinez-Marti, A., Kenmotsu, H., Chen, Y.-M., Chella, A., Sugawara, S., Voong, D., Wu, F., Yi, J., Deng, Y., McCleland, M., Bennett, E., . . . Wakelee, H. (2021). Adjuvant atezolizumab after adjuvant chemotherapy in resected stage IB-IIIA non-small-cell lung cancer (IMpower010): A randomised, multicentre, open-label, phase 3 trial. *The Lancet, 398*(10308), 1344–1357. https://doi.org/10.1016/S0140-6736(21)02098-5（PMID: 34555333）

Felip, E., Altorki, N., Zhou, C., Vallières, E., Csoszi, T., Vynnychenko, I. O., Goloborodko, O., Rittmeyer, A., Reck, M., Martinez-Marti, A., Kenmotsu, H., Chen, Y.-M., Chella, A., Sugawara, S., Fu, C., Ballinger, M., Deng, Y., Srivastava, M. K., Bennett, E., . . . Wakelee, H. A. (2025). Five-year survival outcomes with atezolizumab after chemotherapy in resected stage IB-IIIA non-small cell lung cancer (IMpower010): An open-label, randomized, phase III trial. *Journal of Clinical Oncology, 43*(21), 2343–2349. https://doi.org/10.1200/JCO-24-01681（PMID: 40446184）

Feller-Kopman, D. J., Reddy, C. B., DeCamp, M. M., Diekemper, R. L., Gould, M. K., Henry, T., Iyer, N. P., Lee, Y. C. G., Lewis, S. Z., Maskell, N. A., Rahman, N. M., Sterman, D. H., Wahidi, M. M., & Balekian, A. A. (2018). Management of malignant pleural effusions: An official ATS/STS/STR clinical practice guideline. *American Journal of Respiratory and Critical Care Medicine, 198*(7), 839–849. https://doi.org/10.1164/rccm.201807-1415ST（PMID: 30272503）

Forde, P. M., Spicer, J., Lu, S., Provencio, M., Mitsudomi, T., Awad, M. M., Felip, E., Broderick, S. R., Brahmer, J. R., Swanson, S. J., Kerr, K., Wang, C., Ciuleanu, T.-E., Saylors, G. B., Tanaka, F., Ito, H., Chen, K.-N., Liberman, M., Vokes, E. E., . . . Girard, N. (2022). Neoadjuvant nivolumab plus chemotherapy in resectable lung cancer. *New England Journal of Medicine, 386*(21), 1973–1985. https://doi.org/10.1056/NEJMoa2202170（PMID: 35403841）

Forde, P. M., Spicer, J. D., Provencio, M., Mitsudomi, T., Awad, M. M., Wang, C., Lu, S., Felip, E., Swanson, S. J., Brahmer, J. R., Kerr, K., Taube, J. M., Ciuleanu, T.-E., Tanaka, F., Saylors, G. B., Chen, K.-N., Ito, H., Liberman, M., Martin, C., . . . Girard, N. (2025). Overall survival with neoadjuvant nivolumab plus chemotherapy in lung cancer. *New England Journal of Medicine, 393*(8), 741–752. https://doi.org/10.1056/NEJMoa2502931（PMID: 40454642）

Gainor, J. F., Curigliano, G., Kim, D.-W., Lee, D. H., Besse, B., Baik, C. S., Doebele, R. C., Cassier, P. A., Lopes, G., Tan, D. S. W., Garralda, E., Paz-Ares, L. G., Cho, B. C., Gadgeel, S. M., Thomas, M., Liu, S. V., Taylor, M. H., Mansfield, A. S., Zhu, V. W., . . . Subbiah, V. (2021). Pralsetinib for RET fusion-positive non-small-cell lung cancer (ARROW): A multi-cohort, open-label, phase 1/2 study. *The Lancet Oncology, 22*(7), 959–969. https://doi.org/10.1016/S1470-2045(21)00247-3（PMID: 34118197）

Gandhi, L., Rodríguez-Abreu, D., Gadgeel, S., Esteban, E., Felip, E., De Angelis, F., Domine, M., Clingan, P., Hochmair, M. J., Powell, S. F., Cheng, S. Y.-S., Bischoff, H. G., Peled, N., Grossi, F., Jennens, R. R., Reck, M., Hui, R., Garon, E. B., Boyer, M., . . . Garassino, M. C. (2018). Pembrolizumab plus chemotherapy in metastatic non-small-cell lung cancer. *New England Journal of Medicine, 378*(22), 2078–2092. https://doi.org/10.1056/NEJMoa1801005（PMID: 29658856）

Garassino, M. C., Gadgeel, S., Speranza, G., Felip, E., Esteban, E., Dómine, M., Hochmair, M. J., Powell, S. F., Bischoff, H. G., Peled, N., Grossi, F., Jennens, R. R., Reck, M., Hui, R., Garon, E. B., Kurata, T., Gray, J. E., Schwarzenberger, P., Jensen, E., . . . Rodríguez-Abreu, D. (2023). Pembrolizumab plus pemetrexed and platinum in nonsquamous non-small-cell lung cancer: 5-year outcomes from the phase 3 KEYNOTE-189 study. *Journal of Clinical Oncology, 41*(11), 1992–1998. https://doi.org/10.1200/JCO.22.01989（PMID: 36809080）

Garon, E. B., Ciuleanu, T.-E., Arrieta, O., Prabhash, K., Syrigos, K. N., Goksel, T., Park, K., Gorbunova, V., Kowalyszyn, R. D., Pikiel, J., Czyzewicz, G., Orlov, S. V., Lewanski, C. R., Thomas, M., Bidoli, P., Dakhil, S., Gans, S., Kim, J.-H., Grigorescu, A., . . . Pérol, M. (2014). Ramucirumab plus docetaxel versus placebo plus docetaxel for second-line treatment of stage IV non-small-cell lung cancer after disease progression on platinum-based therapy (REVEL): A multicentre, double-blind, randomised phase 3 trial. *The Lancet, 384*(9944), 665–673. https://doi.org/10.1016/S0140-6736(14)60845-X（PMID: 24933332）

Genentech, Inc. (2025a). *ACTEMRA (tocilizumab) injection: Prescribing information* (effective 2025-12-16). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=2e5365ff-cb2a-4b16-b2c7-e35c6bf2de13

Genentech, Inc. (2025b). *AVASTIN (bevacizumab) injection: Prescribing information* (effective 2025-01-06). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=939b5d1f-9fb2-4499-80ef-0607aa6b114e

Genentech, Inc. (2026a). *ALECENSA (alectinib) capsules: Prescribing information* (effective 2026-08-21). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=42c49deb-713b-427a-9670-08af08adcffb

Genentech, Inc. (2026b). *ROZLYTREK (entrectinib) capsules and pellets: Prescribing information* (effective 2026-10-08). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=c7c71b0c-2549-4495-86b6-c2807fa54908

Genentech, Inc. (2026c). *TECENTRIQ (atezolizumab) injection: Prescribing information* (version 46, effective 2026-10-13). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=6fa682c9-a312-4932-9831-f286908660ee

Goto, K., Goto, Y., Kubo, T., Ninomiya, K., Kim, S.-W., Planchard, D., Ahn, M.-J., Smit, E. F., de Langen, A. J., Pérol, M., Pons-Tostivint, E., Novello, S., Hayashi, H., Shimizu, J., Kim, D.-W., Kuo, C.-H., Yang, J. C.-H., Pereira, K., Cheng, F.-C., . . . Jänne, P. A. (2023). Trastuzumab deruxtecan in patients with HER2-mutant metastatic non-small-cell lung cancer: Primary results from the randomized, phase II DESTINY-Lung02 trial. *Journal of Clinical Oncology, 41*(31), 4852–4863. https://doi.org/10.1200/JCO.23.01361（PMID: 37694347）

Hellmann, M. D., Paz-Ares, L., Bernabe Caro, R., Zurawski, B., Kim, S.-W., Carcereny Costa, E., Park, K., Alexandru, A., Lupinacci, L., de la Mora Jimenez, E., Sakai, H., Albert, I., Vergnenegre, A., Peters, S., Syrigos, K., Barlesi, F., Reck, M., Borghaei, H., Brahmer, J. R., . . . Ramalingam, S. S. (2019). Nivolumab plus ipilimumab in advanced non-small-cell lung cancer. *New England Journal of Medicine, 381*(21), 2020–2031. https://doi.org/10.1056/NEJMoa1910231（PMID: 31562796）

Heymach, J. V., Harpole, D., Mitsudomi, T., Taube, J. M., Galffy, G., Hochmair, M., Winder, T., Zukov, R., Garbaos, G., Gao, S., Kuroda, H., Ostoros, G., Tran, T. V., You, J., Lee, K.-Y., Antonuzzo, L., Papai-Szekely, Z., Akamatsu, H., Biswas, B., . . . Reck, M. (2023). Perioperative durvalumab for resectable non-small-cell lung cancer. *New England Journal of Medicine, 389*(18), 1672–1684. https://doi.org/10.1056/NEJMoa2304875（PMID: 37870974）

Heymach, J. V., He, J., Harpole, D., Mitsudomi, T., Taube, J. M., Gao, S., Urban, L., Kang, J. H., Orlandi, F. J., Rodriguez-Cid, J., Massuti, B., Mateos, L. L., Pasello, G., Chu, Q., Kolb-Sielecki, J., Nakata, M., Galffy, G., Hochmair, M., Winder, T., . . . Reck, M. (2026a). Perioperative durvalumab for resectable non-small cell lung cancer: Updated outcomes from the phase III AEGEAN trial. *Journal of Clinical Oncology*. Advance online publication. https://doi.org/10.1200/JCO-25-02659（PMID: 42664473）

Heymach, J. V., Ruiter, G., Ahn, M.-J., Girard, N., Smit, E. F., Planchard, D., Wu, Y.-L., Cho, B. C., Yamamoto, N., Sabari, J. K., Zhao, Y., Tu, H.-Y., Yoh, K., Nadal, E., Sadrolhefazi, B., Rohrbacher, M., von Wangenheim, U., Eigenbrod-Giese, S., & Zugazagoitia, J. (2025). Zongertinib in previously treated HER2-mutant non-small-cell lung cancer. *New England Journal of Medicine, 392*(23), 2321–2333. https://doi.org/10.1056/NEJMoa2503704（PMID: 40293180）

Heymach, J. V., Yamamoto, N., Girard, N., Ruiter, G., Smit, E. F., Planchard, D., Nadal, E., Wu, Y.-L., Zugazagoitia, J., Tu, H.-Y., Baik, C. S., Yoh, K., Soo, R. A., Zhao, Y., Sabari, J. K., Wermke, M., Scheffler, M., Ahn, M.-J., Fernamberg, K., . . . Popat, S. (2026b). First-line zongertinib in advanced HER2-mutant non-small-cell lung cancer. *New England Journal of Medicine, 394*(17), 1675–1684. https://doi.org/10.1056/NEJMoa2516969（PMID: 41985129）

Horn, L., Mansfield, A. S., Szczęsna, A., Havel, L., Krzakowski, M., Hochmair, M. J., Huemer, F., Losonczy, G., Johnson, M. L., Nishio, M., Reck, M., Mok, T., Lam, S., Shames, D. S., Liu, J., Ding, B., Lopez-Chavez, A., Kabbinavar, F., Lin, W., . . . Liu, S. V. (2018). First-line atezolizumab plus chemotherapy in extensive-stage small-cell lung cancer. *New England Journal of Medicine, 379*(23), 2220–2229. https://doi.org/10.1056/NEJMoa1809064（PMID: 30280641）

Hsu, K.-H., Ho, C.-C., Hsia, T.-C., Tseng, J.-S., Su, K.-Y., Wu, M.-F., Chiu, K.-L., Yang, T.-Y., Chen, K.-C., Ooi, H., Wu, T.-C., Chen, H.-J., Chen, H.-Y., Chang, C.-S., Hsu, C.-P., Hsia, J.-Y., Chuang, C.-Y., Lin, C.-H., Chen, J. J. W., . . . Chang, G.-C. (2015). Identification of five driver gene mutations in patients with treatment-naïve lung adenocarcinoma in Taiwan. *PLoS ONE, 10*(3), Article e0120852. https://doi.org/10.1371/journal.pone.0120852（PMID: 25789627）

Hui, D., Bohlke, K., Bao, T., Campbell, T. C., Coyne, P. J., Currow, D. C., Gupta, A., Leiser, A. L., Mori, M., Nava, S., Reinke, L. F., Roeland, E. J., Seigel, C., Walsh, D., & Campbell, M. L. (2021). Management of dyspnea in advanced cancer: ASCO guideline. *Journal of Clinical Oncology, 39*(12), 1389–1411. https://doi.org/10.1200/JCO.20.03465（PMID: 33617290）

Hui, D., Maddocks, M., Johnson, M. J., Ekström, M., Simon, S. T., Ogliari, A. C., Booth, S., & Ripamonti, C. (2020). Management of breathlessness in patients with cancer: ESMO clinical practice guidelines. *ESMO Open, 5*(6), Article e001038. https://doi.org/10.1136/esmoopen-2020-001038（PMID: 33303485）

Ito, T., Goto, K., Yoh, K., Niho, S., Ohmatsu, H., Kubota, K., Nagai, K., Miyazaki, E., Kumamoto, T., & Nishiwaki, Y. (2010). Hypertrophic pulmonary osteoarthropathy as a paraneoplastic manifestation of lung cancer. *Journal of Thoracic Oncology, 5*(7), 976–980. https://doi.org/10.1097/JTO.0b013e3181dc1f3c（PMID: 20453688）

Ittrich, H., Bockhorn, M., Klose, H., & Simon, M. (2017). The diagnosis and treatment of hemoptysis. *Deutsches Ärzteblatt International, 114*(21), 371–381. https://doi.org/10.3238/arztebl.2017.0371（PMID: 28625277）

Jänne, P. A., Planchard, D., Kobayashi, K., Yang, J. C.-H., Liu, Y., Valdiviezo, N., Kim, T. M., Jiang, L., Kagamu, H., Yanagitani, N., Wang, J., Biswas, B., Poltoratskiy, A., Neron, Y., Rojas, C., Koubkova, L., Escriu, C., Ezeife, D. A., Mann, H., . . . Lee, C. K. (2026). Survival with osimertinib plus chemotherapy in EGFR-mutated advanced NSCLC. *New England Journal of Medicine, 394*(1), 27–38. https://doi.org/10.1056/NEJMoa2510308（PMID: 41104938）

Johnson, M. L., Cho, B. C., Luft, A., Alatorre-Alexander, J., Geater, S. L., Laktionov, K., Kim, S.-W., Ursol, G., Hussein, M., Lim, F. L., Yang, C.-T., Araujo, L. H., Saito, H., Reinmuth, N., Shi, X., Poole, L., Peters, S., Garon, E. B., & Mok, T. (2023). Durvalumab with or without tremelimumab in combination with chemotherapy as first-line therapy for metastatic non-small-cell lung cancer: The phase III POSEIDON study. *Journal of Clinical Oncology, 41*(6), 1213–1227. https://doi.org/10.1200/JCO.22.00975（PMID: 36327426）

Kanaji, N., Watanabe, N., Kita, N., Bandoh, S., Tadokoro, A., Ishii, T., Dobashi, H., & Matsunaga, T. (2014). Paraneoplastic syndromes associated with lung cancer. *World Journal of Clinical Oncology, 5*(3), 197–223. https://doi.org/10.5306/wjco.v5.i3.197（PMID: 25114839）

Kashiwabara, K., Fuji, S., Tsumura, S., & Sakamoto, K. (2020). Prognosis of EGFR-mutant lung adenocarcinoma patients with malignant pleural effusion receiving first-line EGFR-TKI therapy without pleurodesis: A single-institute retrospective study. *Anticancer Research, 40*(2), 1117–1121. https://doi.org/10.21873/anticanres.14051（PMID: 32014962）

Kiritani, A., Amino, Y., Uchibori, K., Akita, T., Harutani, Y., Ogusu, S., Tsugitomi, R., Manabe, R., Ariyasu, R., Kitazono, S., Yanagitani, N., & Nishio, M. (2024). Efficacy of osimertinib in patients with EGFR-mutation positive non-small cell lung cancer with malignant pleural effusion. *Thoracic Cancer, 15*(5), 402–409. https://doi.org/10.1111/1759-7714.15210（PMID: 38226415）

Lee, D. W., Santomasso, B. D., Locke, F. L., Ghobadi, A., Turtle, C. J., Brudno, J. N., Maus, M. V., Park, J. H., Mead, E., Pavletic, S., Go, W. Y., Eldjerou, L., Gardner, R. A., Frey, N., Curran, K. J., Peggs, K., Pasquini, M., DiPersio, J. F., van den Brink, M. R. M., . . . Neelapu, S. S. (2019). ASTCT consensus grading for cytokine release syndrome and neurologic toxicity associated with immune effector cells. *Biology of Blood and Marrow Transplantation, 25*(4), 625–638. https://doi.org/10.1016/j.bbmt.2018.12.758（PMID: 30592986）

Leone, F. T., Zhang, Y., Evers-Casey, S., Evins, A. E., Eakin, M. N., Fathi, J., Fennig, K., Folan, P., Galiatsatos, P., Gogineni, H., Kantrow, S., Kathuria, H., Lamphere, T., Neptune, E., Pacheco, M. C., Pakhale, S., Prezant, D., Sachs, D. P. L., Toll, B., . . . Farber, H. J. (2020). Initiating pharmacologic treatment in tobacco-dependent adults: An official American Thoracic Society clinical practice guideline. *American Journal of Respiratory and Critical Care Medicine, 202*(2), e5–e31. https://doi.org/10.1164/rccm.202005-1982ST（PMID: 32663106）

Lim, E., Seif, K., Goetz, T., Marsicola, O., Law, J. J., De Sousa, P., Aw, T. C., & Lim, E. (2024). Agreement between observed and predicted postoperative forced expiratory volume in one second, forced vital capacity, and diffusing capacity for carbon monoxide after anatomic lung resection. *Journal of Thoracic Disease, 16*(1), 247–252. https://doi.org/10.21037/jtd-23-1390（PMID: 38410582）

Lommatzsch, M., Julius, P., Lück, W., Bier, A., & Virchow, J. C. (2012). [Hypertrophic pulmonary osteoarthropathy as a cue for NSCLC: Four cases in the light of the current literature]. *Pneumologie, 66*(2), 67–73. https://doi.org/10.1055/s-0031-1291476（PMID: 22249782）

Lu, S., Kato, T., Dong, X., Ahn, M.-J., Quang, L.-V., Soparattanapaisarn, N., Inoue, T., Wang, C.-L., Huang, M., Yang, J. C.-H., Cobo, M., Özgüroğlu, M., Casarini, I., Khiem, D.-V., Sriuranpong, V., Cronemberger, E., Takahashi, T., Runglodvatana, Y., Chen, M., . . . Ramalingam, S. S. (2024). Osimertinib after chemoradiotherapy in stage III EGFR-mutated NSCLC. *New England Journal of Medicine, 391*(7), 585–597. https://doi.org/10.1056/NEJMoa2402614（PMID: 38828946）

Magdeleinat, P., Icard, P., Regnard, J.-F., Nicolosi, M., Oulid-Aissa, D., Sarnacki, S., & Levasseur, P. (1999). [A retrospective study of 53 cases of resectable primary bronchopulmonary cancers associated with Pierre Marie syndrome]. *Revue de Pneumologie Clinique, 55*(2), 94–99.（PMID: 10418053；PubMed 無 DOI）

Mok, T., Camidge, D. R., Gadgeel, S. M., Rosell, R., Dziadziuszko, R., Kim, D.-W., Pérol, M., Ou, S.-H. I., Ahn, J. S., Shaw, A. T., Bordogna, W., Smoljanović, V., Hilton, M., Ruf, T., Noé, J., & Peters, S. (2020). Updated overall survival and final progression-free survival data for patients with treatment-naive advanced ALK-positive non-small-cell lung cancer in the ALEX study. *Annals of Oncology, 31*(8), 1056–1064. https://doi.org/10.1016/j.annonc.2020.04.478（PMID: 32418886）

Mok, T. S., Wu, Y.-L., Ahn, M.-J., Garassino, M. C., Kim, H. R., Ramalingam, S. S., Shepherd, F. A., He, Y., Akamatsu, H., Theelen, W. S. M. E., Lee, C. K., Sebastian, M., Templeton, A., Mann, H., Marotti, M., Ghiorghiu, S., & Papadimitrakopoulou, V. A. (2017). Osimertinib or platinum-pemetrexed in EGFR T790M-positive lung cancer. *New England Journal of Medicine, 376*(7), 629–640. https://doi.org/10.1056/NEJMoa1612674（PMID: 27959700）

Mok, T. S., Wu, Y.-L., Thongprasert, S., Yang, C.-H., Chu, D.-T., Saijo, N., Sunpaweravong, P., Han, B., Margono, B., Ichinose, Y., Nishiwaki, Y., Ohe, Y., Yang, J.-J., Chewaskulyong, B., Jiang, H., Duffield, E. L., Watkins, C. L., Armour, A. A., & Fukuoka, M. (2009). Gefitinib or carboplatin-paclitaxel in pulmonary adenocarcinoma. *New England Journal of Medicine, 361*(10), 947–957. https://doi.org/10.1056/NEJMoa0810699（PMID: 19692680）

Molassiotis, A., Smith, J. A., Mazzone, P., Blackhall, F., & Irwin, R. S. (2017). Symptomatic treatment of cough among adult patients with lung cancer: CHEST guideline and expert panel report. *Chest, 151*(4), 861–874. https://doi.org/10.1016/j.chest.2016.12.028（PMID: 28108179）

Mountzios, G., Sun, L., Cho, B. C., Demirci, U., Baka, S., Gümüş, M., Lugini, A., Zhu, B., Yu, Y., Korantzis, I., Han, J.-Y., Ciuleanu, T.-E., Ahn, M.-J., Rocha, P., Mazières, J., Lau, S. C. M., Schuler, M., Blackhall, F., Yoshida, T., . . . Rudin, C. M. (2025). Tarlatamab in small-cell lung cancer after platinum-based chemotherapy. *New England Journal of Medicine, 393*(4), 349–361. https://doi.org/10.1056/NEJMoa2502099（PMID: 40454646）

National Comprehensive Cancer Network. (2026a). *NCCN Clinical Practice Guidelines in Oncology: Non-small cell lung cancer* (Version 9.2026). https://www.nccn.org/guidelines/category_1

National Comprehensive Cancer Network. (2026b). *NCCN Clinical Practice Guidelines in Oncology: Small cell lung cancer* (Version 1.2027). https://www.nccn.org/guidelines/category_1

National Lung Screening Trial Research Team, Aberle, D. R., Adams, A. M., Berg, C. D., Black, W. C., Clapp, J. D., Fagerstrom, R. M., Gareen, I. F., Gatsonis, C., Marcus, P. M., & Sicks, J. D. (2011). Reduced lung-cancer mortality with low-dose computed tomographic screening. *New England Journal of Medicine, 365*(5), 395–409. https://doi.org/10.1056/NEJMoa1102873（PMID: 21714641）

Novartis Pharmaceuticals Corporation. (2026a). *TABRECTA (capmatinib) tablets: Prescribing information* (effective 2026-10-26). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=455892c3-d144-4ba8-9ab4-79cabff9876d

Novartis Pharmaceuticals Corporation. (2026b). *TAFINLAR (dabrafenib) capsules and tablets for oral suspension: Prescribing information* (effective 2026-05-20). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=fee1e6b1-e1a5-4254-9f2e-a70e0f8dbdea

O'Brien, M., Paz-Ares, L., Marreaud, S., Dafni, U., Oselin, K., Havel, L., Esteban, E., Isla, D., Martinez-Marti, A., Faehling, M., Tsuboi, M., Lee, J.-S., Nakagawa, K., Yang, J., Samkari, A., Keller, S. M., Mauer, M., Jha, N., Stahel, R., . . . Peters, S. (2022). Pembrolizumab versus placebo as adjuvant therapy for completely resected stage IB-IIIA non-small-cell lung cancer (PEARLS/KEYNOTE-091): An interim analysis of a randomised, triple-blind, phase 3 trial. *The Lancet Oncology, 23*(10), 1274–1286. https://doi.org/10.1016/S1470-2045(22)00518-6（PMID: 36108662）

Paik, P. K., Felip, E., Veillon, R., Sakai, H., Cortot, A. B., Garassino, M. C., Mazieres, J., Viteri, S., Senellart, H., Van Meerbeeck, J., Raskin, J., Reinmuth, N., Conte, P., Kowalski, D., Cho, B. C., Patel, J. D., Horn, L., Griesinger, F., Han, J.-Y., . . . Le, X. (2020). Tepotinib in non-small-cell lung cancer with MET exon 14 skipping mutations. *New England Journal of Medicine, 383*(10), 931–943. https://doi.org/10.1056/NEJMoa2004407（PMID: 32469185）

Parsons, A., Daley, A., Begh, R., & Aveyard, P. (2010). Influence of smoking cessation after diagnosis of early stage lung cancer on prognosis: Systematic review of observational studies with meta-analysis. *BMJ, 340*, Article b5569. https://doi.org/10.1136/bmj.b5569（PMID: 20093278）

Passaro, A., Wang, J., Wang, Y., Lee, S.-H., Melosky, B., Shih, J.-Y., Wang, J., Azuma, K., Juan-Vidal, O., Cobo, M., Felip, E., Girard, N., Cortot, A. B., Califano, R., Cappuzzo, F., Owen, S., Popat, S., Tan, J.-L., Salinas, J., . . . Cho, B. C. (2024). Amivantamab plus chemotherapy with and without lazertinib in EGFR-mutant advanced NSCLC after disease progression on osimertinib: Primary results from the phase III MARIPOSA-2 study. *Annals of Oncology, 35*(1), 77–90. https://doi.org/10.1016/j.annonc.2023.10.117（PMID: 37879444）

Paz-Ares, L., Borghaei, H., Liu, S. V., Peters, S., Herbst, R. S., Stencel, K., Majem, M., Şendur, M. A. N., Czyżewicz, G., Caro, R. B., Lee, K. H., Johnson, M. L., Karadurmuş, N., Grohé, C., Baka, S., Csőszi, T., Ahn, J. S., Califano, R., Yang, T.-Y., . . . Reck, M. (2025). Efficacy and safety of first-line maintenance therapy with lurbinectedin plus atezolizumab in extensive-stage small-cell lung cancer (IMforte): A randomised, multicentre, open-label, phase 3 trial. *The Lancet, 405*(10495), 2129–2143. https://doi.org/10.1016/S0140-6736(25)01011-6（PMID: 40473449）

Paz-Ares, L., Chen, Y., Reinmuth, N., Hotta, K., Trukhin, D., Statsenko, G., Hochmair, M. J., Özgüroğlu, M., Ji, J. H., Garassino, M. C., Voitko, O., Poltoratskiy, A., Musso, E., Havel, L., Bondarenko, I., Losonczy, G., Conev, N., Mann, H., Dalvi, T. B., . . . Goldman, J. W. (2022). Durvalumab, with or without tremelimumab, plus platinum-etoposide in first-line treatment of extensive-stage small-cell lung cancer: 3-year overall survival update from CASPIAN. *ESMO Open, 7*(2), Article 100408. https://doi.org/10.1016/j.esmoop.2022.100408（PMID: 35279527）

Paz-Ares, L., Ciuleanu, T.-E., Cobo, M., Schenker, M., Zurawski, B., Menezes, J., Richardet, E., Bennouna, J., Felip, E., Juan-Vidal, O., Alexandru, A., Sakai, H., Lingua, A., Salman, P., Souquet, P.-J., De Marchi, P., Martin, C., Pérol, M., Scherpereel, A., . . . Reck, M. (2021). First-line nivolumab plus ipilimumab combined with two cycles of chemotherapy in patients with non-small-cell lung cancer (CheckMate 9LA): An international, randomised, open-label, phase 3 trial. *The Lancet Oncology, 22*(2), 198–211. https://doi.org/10.1016/S1470-2045(20)30641-0（PMID: 33476593）

Paz-Ares, L., Dvorkin, M., Chen, Y., Reinmuth, N., Hotta, K., Trukhin, D., Statsenko, G., Hochmair, M. J., Özgüroğlu, M., Ji, J. H., Voitko, O., Poltoratskiy, A., Ponce, S., Verderame, F., Havel, L., Bondarenko, I., Kazarnowicz, A., Losonczy, G., Conev, N. V., . . . Goldman, J. W. (2019). Durvalumab plus platinum-etoposide versus platinum-etoposide in first-line treatment of extensive-stage small-cell lung cancer (CASPIAN): A randomised, controlled, open-label, phase 3 trial. *The Lancet, 394*(10212), 1929–1939. https://doi.org/10.1016/S0140-6736(19)32222-6（PMID: 31590988）

Paz-Ares, L., Luft, A., Vicente, D., Tafreshi, A., Gümüş, M., Mazières, J., Hermes, B., Çay Şenler, F., Csőszi, T., Fülöp, A., Rodríguez-Cid, J., Wilson, J., Sugawara, S., Kato, T., Lee, K. H., Cheng, Y., Novello, S., Halmos, B., Li, X., . . . Kowalski, D. M. (2018). Pembrolizumab plus chemotherapy for squamous non-small-cell lung cancer. *New England Journal of Medicine, 379*(21), 2040–2051. https://doi.org/10.1056/NEJMoa1810865（PMID: 30280635）

Pérol, M., Li, W., Pennell, N. A., Liu, G., Ohe, Y., De Braud, F., Nagasaka, M., Felip, E., Xiong, A., Zhang, Y., Fan, H., Wang, X., Li, S., Lai, R. K., Ran, F., Zhang, X., Chen, W., Bazhenova, L., & Zhou, C. (2025). Taletrectinib in ROS1+ non-small cell lung cancer: TRUST. *Journal of Clinical Oncology, 43*(16), 1920–1929. https://doi.org/10.1200/JCO-25-00275（PMID: 40179330）

Peters, S., Camidge, D. R., Shaw, A. T., Gadgeel, S., Ahn, J. S., Kim, D.-W., Ou, S.-H. I., Pérol, M., Dziadziuszko, R., Rosell, R., Zeaiter, A., Mitry, E., Golding, S., Balas, B., Noe, J., Morcos, P. N., & Mok, T. (2017). Alectinib versus crizotinib in untreated ALK-positive non-small-cell lung cancer. *New England Journal of Medicine, 377*(9), 829–838. https://doi.org/10.1056/NEJMoa1704795（PMID: 28586279）

Peters, S., Camidge, R., Dziadziuszko, R., Gadgeel, S., Shaw, A. T., Kim, D.-W., Pérol, M., Rosell, D. R., Cheema, P., Wan-Teck Lim, D., Lin, J. J., Pavlakis, N., Ahn, J. S., Zhang, L., Henschel, V., Higgerson, A. A., McNally, V., Rooney, I., Scalori, A., . . . Mok, T. (2026). Alectinib versus crizotinib in previously untreated ALK-positive advanced non-small cell lung cancer: Final overall survival analysis of the phase III ALEX study. *Annals of Oncology, 37*(1), 92–103. https://doi.org/10.1016/j.annonc.2025.09.018（PMID: 41110693）

Pfizer Laboratories Div Pfizer Inc. (2025). *XALKORI (crizotinib) capsules and pellets: Prescribing information* (effective 2025-07-22). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=2a51b0de-47d6-455e-a94c-d2c737b04ff7

Pfizer Laboratories Div Pfizer Inc. (2026a). *LORBRENA (lorlatinib) tablets: Prescribing information* (effective 2026-06-26). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=2b34d62d-e02a-4af3-bc0d-1571dd4ee76d

Pfizer Laboratories Div Pfizer Inc. (2026b). *VIZIMPRO (dacomitinib) tablets: Prescribing information* (effective 2026-06-23). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=4ab27d2f-e385-4e9c-b324-fa69c10b855a

Piasecka, M., Larsson, M., Papakokkinou, E., Olsson, L., & Ragnarsson, O. (2022). Is ectopic Cushing's syndrome underdiagnosed in patients with small cell lung cancer? *Frontiers in Medicine, 9*, Article 954033. https://doi.org/10.3389/fmed.2022.954033（PMID: 36111117）

Pignon, J.-P., Tribodet, H., Scagliotti, G. V., Douillard, J.-Y., Shepherd, F. A., Stephens, R. J., Dunant, A., Torri, V., Rosell, R., Seymour, L., Spiro, S. G., Rolland, E., Fossati, R., Aubert, D., Ding, K., Waller, D., & Le Chevalier, T. (2008). Lung adjuvant cisplatin evaluation: A pooled analysis by the LACE Collaborative Group. *Journal of Clinical Oncology, 26*(21), 3552–3559. https://doi.org/10.1200/JCO.2007.13.9030（PMID: 18506026）

Planchard, D., Jänne, P. A., Cheng, Y., Yang, J. C.-H., Yanagitani, N., Kim, S.-W., Sugawara, S., Yu, Y., Fan, Y., Geater, S. L., Laktionov, K., Lee, C. K., Valdiviezo, N., Ahmed, S., Maurel, J.-M., Andrasina, I., Goldman, J., Ghiorghiu, D., Rukazenkov, Y., . . . Kobayashi, K. (2023). Osimertinib with or without chemotherapy in EGFR-mutated advanced NSCLC. *New England Journal of Medicine, 389*(21), 1935–1948. https://doi.org/10.1056/NEJMoa2306434（PMID: 37937763）

Planchard, D., Smit, E. F., Groen, H. J. M., Mazieres, J., Besse, B., Helland, Å., Giannone, V., D'Amelio, A. M., Jr., Zhang, P., Mookerjee, B., & Johnson, B. E. (2017). Dabrafenib plus trametinib in patients with previously untreated BRAFV600E-mutant metastatic non-small-cell lung cancer: An open-label, phase 2 trial. *The Lancet Oncology, 18*(10), 1307–1316. https://doi.org/10.1016/S1470-2045(17)30679-4（PMID: 28919011）

Ramalingam, S. S., Vansteenkiste, J., Planchard, D., Cho, B. C., Gray, J. E., Ohe, Y., Zhou, C., Reungwetwattana, T., Cheng, Y., Chewaskulyong, B., Shah, R., Cobo, M., Lee, K. H., Cheema, P., Tiseo, M., John, T., Lin, M.-C., Imamura, F., Kurata, T., . . . Soria, J.-C. (2020). Overall survival with osimertinib in untreated, EGFR-mutated advanced NSCLC. *New England Journal of Medicine, 382*(1), 41–50. https://doi.org/10.1056/NEJMoa1913662（PMID: 31751012）

Rami-Porta, R., Nishimura, K. K., Giroux, D. J., Detterbeck, F., Cardillo, G., Edwards, J. G., Fong, K. M., Giuliani, M., Huang, J., Kernstine, K. H., Sr., Marom, E. M., Nicholson, A. G., Van Schil, P. E., Travis, W. D., Tsao, M. S., Watanabe, S.-I., Rusch, V. W., Asamura, H., & Members of the IASLC Staging and Prognostic Factors Committee and of the Advisory Boards, and Participating Institutions. (2024). The International Association for the Study of Lung Cancer Lung Cancer Staging Project: Proposals for revision of the TNM stage groups in the forthcoming (ninth) edition of the TNM classification for lung cancer. *Journal of Thoracic Oncology, 19*(7), 1007–1027. https://doi.org/10.1016/j.jtho.2024.02.011（PMID: 38447919）

Reck, M., Rodríguez-Abreu, D., Robinson, A. G., Hui, R., Csőszi, T., Fülöp, A., Gottfried, M., Peled, N., Tafreshi, A., Cuffe, S., O'Brien, M., Rao, S., Hotta, K., Leal, T. A., Riess, J. W., Jensen, E., Zhao, B., Pietanza, M. C., & Brahmer, J. R. (2021). Five-year outcomes with pembrolizumab versus chemotherapy for metastatic non-small-cell lung cancer with PD-L1 tumor proportion score ≥ 50%. *Journal of Clinical Oncology, 39*(21), 2339–2349. https://doi.org/10.1200/JCO.21.00174（PMID: 33872070）

Reck, M., Rodríguez-Abreu, D., Robinson, A. G., Hui, R., Csőszi, T., Fülöp, A., Gottfried, M., Peled, N., Tafreshi, A., Cuffe, S., O'Brien, M., Rao, S., Hotta, K., Leiby, M. A., Lubiniecki, G. M., Shentu, Y., Rangwala, R., & Brahmer, J. R. (2016). Pembrolizumab versus chemotherapy for PD-L1-positive non-small-cell lung cancer. *New England Journal of Medicine, 375*(19), 1823–1833. https://doi.org/10.1056/NEJMoa1606774（PMID: 27718847）

Riely, G. J., Smit, E. F., Ahn, M.-J., Felip, E., Ramalingam, S. S., Tsao, A., Johnson, M., Gelsomino, F., Esper, R., Nadal, E., Offin, M., Provencio, M., Clarke, J., Hussain, M., Otterson, G. A., Dagogo-Jack, I., Goldman, J. W., Morgensztern, D., Alcasid, A., . . . Johnson, B. E. (2023). Phase II, open-label study of encorafenib plus binimetinib in patients with BRAFV600-mutant metastatic non-small-cell lung cancer. *Journal of Clinical Oncology, 41*(21), 3700–3711. https://doi.org/10.1200/JCO.23.00774（PMID: 37270692）

Saito, H., Fukuhara, T., Furuya, N., Watanabe, K., Sugawara, S., Iwasawa, S., Tsunezuka, Y., Yamaguchi, O., Okada, M., Yoshimori, K., Nakachi, I., Gemma, A., Azuma, K., Kurimoto, F., Tsubata, Y., Fujita, Y., Nagashima, H., Asai, G., Watanabe, S., . . . Maemondo, M. (2019). Erlotinib plus bevacizumab versus erlotinib alone in patients with EGFR-positive advanced non-squamous non-small-cell lung cancer (NEJ026): Interim analysis of an open-label, randomised, multicentre, phase 3 trial. *The Lancet Oncology, 20*(5), 625–635. https://doi.org/10.1016/S1470-2045(19)30035-X（PMID: 30975627）

Saji, H., Okada, M., Tsuboi, M., Nakajima, R., Suzuki, K., Aokage, K., Aoki, T., Okami, J., Yoshino, I., Ito, H., Okumura, N., Yamaguchi, M., Ikeda, N., Wakabayashi, M., Nakamura, K., Fukuda, H., Nakamura, S., Mitsudomi, T., Watanabe, S.-I., & Asamura, H. (2022). Segmentectomy versus lobectomy in small-sized peripheral non-small-cell lung cancer (JCOG0802/WJOG4607L): A multicentre, open-label, phase 3, randomised, controlled, non-inferiority trial. *The Lancet, 399*(10335), 1607–1617. https://doi.org/10.1016/S0140-6736(21)02333-3（PMID: 35461558）

Schoenfeld, A. J., Arbour, K. C., Rizvi, H., Iqbal, A. N., Gadgeel, S. M., Girshman, J., Kris, M. G., Riely, G. J., Yu, H. A., & Hellmann, M. D. (2019). Severe immune-related adverse events are common with sequential PD-(L)1 blockade and osimertinib. *Annals of Oncology, 30*(5), 839–844. https://doi.org/10.1093/annonc/mdz077（PMID: 30847464）

Sculier, J.-P., Chansky, K., Crowley, J. J., Van Meerbeeck, J., & Goldstraw, P. (2008). The impact of additional prognostic factors on survival and their relationship with the anatomical extent of disease expressed by the 6th edition of the TNM classification of malignant tumors and the proposals for the 7th edition. *Journal of Thoracic Oncology, 3*(5), 457–466. https://doi.org/10.1097/JTO.0b013e31816de2b8（PMID: 18448996）

Shaw, A. T., Bauer, T. M., de Marinis, F., Felip, E., Goto, Y., Liu, G., Mazieres, J., Kim, D.-W., Mok, T., Polli, A., Thurm, H., Calella, A. M., Peltz, G., & Solomon, B. J. (2020). First-line lorlatinib or crizotinib in advanced ALK-positive lung cancer. *New England Journal of Medicine, 383*(21), 2018–2029. https://doi.org/10.1056/NEJMoa2027187（PMID: 33207094）

Shaw, A. T., Ou, S.-H. I., Bang, Y.-J., Camidge, D. R., Solomon, B. J., Salgia, R., Riely, G. J., Varella-Garcia, M., Shapiro, G. I., Costa, D. B., Doebele, R. C., Le, L. P., Zheng, Z., Tan, W., Stephenson, P., Shreeve, S. M., Tye, L. M., Christensen, J. G., Wilner, K. D., . . . Iafrate, A. J. (2014). Crizotinib in ROS1-rearranged non-small-cell lung cancer. *New England Journal of Medicine, 371*(21), 1963–1971. https://doi.org/10.1056/NEJMoa1406766（PMID: 25264305）

Shaw, A. T., Solomon, B. J., Felip, E., Bauer, T. M., Liu, G., Goto, Y., Wu, Y.-L., Soo, R. A., Mazieres, J., Kim, D.-W., Wang, I.-M., Paolini, J., Polli, A., Rifi, N., Toffalorio, F., & Mok, T. S. K. (2026). Lorlatinib versus crizotinib as first-line treatment for advanced ALK-positive non-small-cell lung cancer: 7-year update from the phase III CROWN study. *Annals of Oncology, 37*(9), 1242–1252. https://doi.org/10.1016/j.annonc.2026.05.692（PMID: 42217582）

Shi, Y., Au, J. S.-K., Thongprasert, S., Srinivasan, S., Tsai, C.-M., Khoa, M. T., Heeroma, K., Itoh, Y., Cornelio, G., & Yang, P.-C. (2014). A prospective, molecular epidemiology study of EGFR mutations in Asian patients with advanced non-small-cell lung cancer of adenocarcinoma histology (PIONEER). *Journal of Thoracic Oncology, 9*(2), 154–162. https://doi.org/10.1097/JTO.0000000000000033（PMID: 24419411）

Shields, P. G., Bierut, L., Arenberg, D., Balis, D., Cinciripini, P. M., Davis, J., Edmondson, D., Feliciano, J., Hitsman, B., Hudmon, K. S., Jaklitsch, M. T., Leone, F. T., Ling, P., McCarthy, D. E., Ong, M. K., Park, E. R., Prochaska, J., Sandoval, A. J., Sheffer, C. E., . . . Darlow, S. (2023). Smoking cessation, version 3.2022, NCCN clinical practice guidelines in oncology. *Journal of the National Comprehensive Cancer Network, 21*(3), 297–322. https://doi.org/10.6004/jnccn.2023.0013（PMID: 36898367）

Socinski, M. A., Jotte, R. M., Cappuzzo, F., Orlandi, F., Stroyakovskiy, D., Nogami, N., Rodríguez-Abreu, D., Moro-Sibilot, D., Thomas, C. A., Barlesi, F., Finley, G., Kelsch, C., Lee, A., Coleman, S., Deng, Y., Shen, Y., Kowanetz, M., Lopez-Chavez, A., Sandler, A., & Reck, M. (2018). Atezolizumab for first-line treatment of metastatic nonsquamous NSCLC. *New England Journal of Medicine, 378*(24), 2288–2301. https://doi.org/10.1056/NEJMoa1716948（PMID: 29863955）

Solomon, B. J., Liu, G., Felip, E., Mok, T. S. K., Soo, R. A., Mazieres, J., Shaw, A. T., de Marinis, F., Goto, Y., Wu, Y.-L., Kim, D.-W., Martini, J.-F., Messina, R., Paolini, J., Polli, A., Thomaidou, D., Toffalorio, F., & Bauer, T. M. (2024). Lorlatinib versus crizotinib in patients with advanced ALK-positive non-small cell lung cancer: 5-year outcomes from the phase III CROWN study. *Journal of Clinical Oncology, 42*(29), 3400–3409. https://doi.org/10.1200/JCO.24.00581（PMID: 38819031）

Solomon, B. J., Mok, T., Kim, D.-W., Wu, Y.-L., Nakagawa, K., Mekhail, T., Felip, E., Cappuzzo, F., Paolini, J., Usari, T., Iyer, S., Reisman, A., Wilner, K. D., Tursi, J., & Blackhall, F. (2014). First-line crizotinib versus chemotherapy in ALK-positive lung cancer. *New England Journal of Medicine, 371*(23), 2167–2177. https://doi.org/10.1056/NEJMoa1408440（PMID: 25470694）

Soria, J.-C., Ohe, Y., Vansteenkiste, J., Reungwetwattana, T., Chewaskulyong, B., Lee, K. H., Dechaphunkul, A., Imamura, F., Nogami, N., Kurata, T., Okamoto, I., Zhou, C., Cho, B. C., Cheng, Y., Cho, E. K., Voon, P. J., Planchard, D., Su, W.-C., Gray, J. E., . . . Ramalingam, S. S. (2018). Osimertinib in untreated EGFR-mutated advanced non-small-cell lung cancer. *New England Journal of Medicine, 378*(2), 113–125. https://doi.org/10.1056/NEJMoa1713137（PMID: 29151359）

Spicer, J. D., Garassino, M. C., Wakelee, H., Liberman, M., Kato, T., Tsuboi, M., Lee, S.-H., Chen, K.-N., Dooms, C., Majem, M., Eigendorff, E., Martinengo, G. L., Bylicki, O., Rodríguez-Abreu, D., Chaft, J. E., Novello, S., Yang, J., Arunachalam, A., Keller, S. M., . . . Gao, S. (2024). Neoadjuvant pembrolizumab plus chemotherapy followed by adjuvant pembrolizumab compared with neoadjuvant chemotherapy alone in patients with early-stage non-small-cell lung cancer (KEYNOTE-671): A randomised, double-blind, placebo-controlled, phase 3 trial. *The Lancet, 404*(10459), 1240–1252. https://doi.org/10.1016/S0140-6736(24)01756-2（PMID: 39288781）

Spigel, D. R., Faivre-Finn, C., Gray, J. E., Vicente, D., Planchard, D., Paz-Ares, L., Vansteenkiste, J. F., Garassino, M. C., Hui, R., Quantin, X., Rimner, A., Wu, Y.-L., Özgüroğlu, M., Lee, K. H., Kato, T., de Wit, M., Kurata, T., Reck, M., Cho, B. C., . . . Antonia, S. J. (2022). Five-year survival outcomes from the PACIFIC trial: Durvalumab after chemoradiotherapy in stage III non-small-cell lung cancer. *Journal of Clinical Oncology, 40*(12), 1301–1311. https://doi.org/10.1200/JCO.21.01308（PMID: 35108059）

Spira, A. I., Paz-Ares, L., Han, J.-Y., Shih, J.-Y., Mascaux, C., Roy, U. B., Zugazagoitia, J., Kim, Y. J., Chiu, C.-H., Kim, S.-W., Nadal, E., Gil-Bazo, I., Murphy, S. P., Anderson, B. G., Xia, Y., Wang, G., Bauml, J. M., Chioda, M., Simoes, J., . . . Lopes, G. (2025). Preventing infusion-related reactions with intravenous amivantamab: Results from SKIPPirr, a phase 2 study: A brief report. *Journal of Thoracic Oncology, 20*(6), 809–816. https://doi.org/10.1016/j.jtho.2025.01.018（PMID: 39864547）

Spiro, S. G., Gould, M. K., & Colice, G. L. (2007). Initial evaluation of the patient with lung cancer: Symptoms, signs, laboratory tests, and paraneoplastic syndromes: ACCP evidenced-based clinical practice guidelines (2nd edition). *Chest, 132*(3, Suppl.), 149S–160S. https://doi.org/10.1378/chest.07-1358（PMID: 17873166）

Takahashi, T., Yamanaka, T., Seto, T., Harada, H., Nokihara, H., Saka, H., Nishio, M., Kaneda, H., Takayama, K., Ishimoto, O., Takeda, K., Yoshioka, H., Tachihara, M., Sakai, H., Goto, K., & Yamamoto, N. (2017). Prophylactic cranial irradiation versus observation in patients with extensive-disease small-cell lung cancer: A multicentre, randomised, open-label, phase 3 trial. *The Lancet Oncology, 18*(5), 663–671. https://doi.org/10.1016/S1470-2045(17)30230-9（PMID: 28343976）

Takeda Pharmaceuticals America, Inc. (2026). *ALUNBRIG (brigatinib) tablets: Prescribing information* (effective 2026-01-12). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=0fe9ff20-d402-41f3-bc1e-7002ea7007db

Tindle, H. A., Stevenson Duncan, M., Greevy, R. A., Vasan, R. S., Kundu, S., Massion, P. P., & Freiberg, M. S. (2018). Lifetime smoking history and risk of lung cancer: Results from the Framingham Heart Study. *Journal of the National Cancer Institute, 110*(11), 1201–1207. https://doi.org/10.1093/jnci/djy041（PMID: 29788259）

Trigo, J., Subbiah, V., Besse, B., Moreno, V., López, R., Sala, M. A., Peters, S., Ponce, S., Fernández, C., Alfaro, V., Gómez, J., Kahatt, C., Zeaiter, A., Zaman, K., Boni, V., Arrondeau, J., Martínez, M., Delord, J.-P., Awada, A., . . . Paz-Ares, L. (2020). Lurbinectedin as second-line treatment for patients with small-cell lung cancer: A single-arm, open-label, phase 2 basket trial. *The Lancet Oncology, 21*(5), 645–654. https://doi.org/10.1016/S1470-2045(20)30068-1（PMID: 32224306）

Tsuboi, M., Herbst, R. S., John, T., Kato, T., Majem, M., Grohé, C., Wang, J., Goldman, J. W., Lu, S., Su, W.-C., de Marinis, F., Shepherd, F. A., Lee, K. H., Le, N. T., Dechaphunkul, A., Kowalski, D., Poole, L., Bolanos, A., Rukazenkov, Y., & Wu, Y.-L. (2023). Overall survival with osimertinib in resected EGFR-mutated NSCLC. *New England Journal of Medicine, 389*(2), 137–147. https://doi.org/10.1056/NEJMoa2304594（PMID: 37272535）

Turrisi, A. T., III, Kim, K., Blum, R., Sause, W. T., Livingston, R. B., Komaki, R., Wagner, H., Aisner, S., & Johnson, D. H. (1999). Twice-daily compared with once-daily thoracic radiotherapy in limited small-cell lung cancer treated concurrently with cisplatin and etoposide. *New England Journal of Medicine, 340*(4), 265–271. https://doi.org/10.1056/NEJM199901283400403（PMID: 9920950）

Varki, A. (2007). Trousseau's syndrome: Multiple definitions and multiple mechanisms. *Blood, 110*(6), 1723–1729. https://doi.org/10.1182/blood-2006-10-053736（PMID: 17496204）

Verma, A., Chopra, A., Lee, Y. W., Bharwani, L. D., Asmat, A. B., Aneez, D. B. A., Akbar, F. A., Lim, A. Y. H., Chotirmall, S. H., & Abisheganaden, J. (2016). Can EGFR-tyrosine kinase inhibitors (TKI) alone without talc pleurodesis prevent recurrence of malignant pleural effusion (MPE) in lung adenocarcinoma. *Current Drug Discovery Technologies, 13*(2), 68–76. https://doi.org/10.2174/1570163813666160524142846（PMID: 27216707）

Wakelee, H., Liberman, M., Kato, T., Tsuboi, M., Lee, S.-H., Gao, S., Chen, K.-N., Dooms, C., Majem, M., Eigendorff, E., Martinengo, G. L., Bylicki, O., Rodríguez-Abreu, D., Chaft, J. E., Novello, S., Yang, J., Keller, S. M., Samkari, A., & Spicer, J. D. (2023). Perioperative pembrolizumab for early-stage non-small-cell lung cancer. *New England Journal of Medicine, 389*(6), 491–503. https://doi.org/10.1056/NEJMoa2302983（PMID: 37272513）

Wand, O., Guber, E., Guber, A., Epstein Shochet, G., Israeli-Shani, L., & Shitrit, D. (2018). Inhaled tranexamic acid for hemoptysis treatment: A randomized controlled trial. *Chest, 154*(6), 1379–1384. https://doi.org/10.1016/j.chest.2018.09.026（PMID: 30321510）

Wolf, J., Seto, T., Han, J.-Y., Reguart, N., Garon, E. B., Groen, H. J. M., Tan, D. S. W., Hida, T., de Jonge, M., Orlov, S. V., Smit, E. F., Souquet, P.-J., Vansteenkiste, J., Hochmair, M., Felip, E., Nishio, M., Thomas, M., Ohashi, K., Toyozawa, R., . . . Heist, R. S. (2020). Capmatinib in MET exon 14-mutated or MET-amplified non-small-cell lung cancer. *New England Journal of Medicine, 383*(10), 944–957. https://doi.org/10.1056/NEJMoa2002787（PMID: 32877583）

Wu, Y.-L., Dziadziuszko, R., Ahn, J. S., Barlesi, F., Nishio, M., Lee, D. H., Lee, J.-S., Zhong, W., Horinouchi, H., Mao, W., Hochmair, M., de Marinis, F., Migliorino, M. R., Bondarenko, I., Lu, S., Wang, Q., Ochi Lohmann, T., Xu, T., Cardona, A., . . . Solomon, B. J. (2024). Alectinib in resected ALK-positive non-small-cell lung cancer. *New England Journal of Medicine, 390*(14), 1265–1276. https://doi.org/10.1056/NEJMoa2310532（PMID: 38598794）

Wu, Y.-L., Tsuboi, M., He, J., John, T., Grohe, C., Majem, M., Goldman, J. W., Laktionov, K., Kim, S.-W., Kato, T., Vu, H.-V., Lu, S., Lee, K.-Y., Akewanlop, C., Yu, C.-J., de Marinis, F., Bonanno, L., Domine, M., Shepherd, F. A., . . . Herbst, R. S. (2020). Osimertinib in resected EGFR-mutated non-small-cell lung cancer. *New England Journal of Medicine, 383*(18), 1711–1723. https://doi.org/10.1056/NEJMoa2027071（PMID: 32955177）

Yang, J. C.-H., Lu, S., Hayashi, H., Felip, E., Spira, A. I., Girard, N., Kim, Y. J., Lee, S.-H., Ostapenko, Y., Danchaivijitr, P., Liu, B., Alip, A., Korbenfeld, E., Mourão Dias, J., Besse, B., Passaro, A., Lee, K.-H., Xiong, H., How, S.-H., . . . Cho, B. C. (2025). Overall survival with amivantamab-lazertinib in EGFR-mutated advanced NSCLC. *New England Journal of Medicine, 393*(17), 1681–1693. https://doi.org/10.1056/NEJMoa2503001（PMID: 40923797）

Zeiher, B. G., Gross, T. J., Kern, J. A., Lanza, L. A., & Peterson, M. W. (1995). Predicting postoperative pulmonary function in patients undergoing lung resection. *Chest, 108*(1), 68–72. https://doi.org/10.1378/chest.108.1.68（PMID: 7606994）

Zhou, C., Greillier, L., Liu, G., John, T., Xing, L., Kowalski, D., Memmott, R. M., Yazici, O., Sun, M., Shu, C. A., Pons-Tostivint, E., Fan, Y., Fernandez-Hinojal, G., Shum, E., Wang, M., Bertolini, F., Camidge, D. R., Zhou, C., Doucet, L., . . . Heymach, J. V. (2026). First-line sunvozertinib in NSCLC with EGFR exon 20 insertion mutations. *New England Journal of Medicine, 395*(8), 765–775. https://doi.org/10.1056/NEJMoa2604461（PMID: 42212913）

Zhou, C., Solomon, B., Loong, H. H., Park, K., Pérol, M., Arriola, E., Novello, S., Han, B., Zhou, J., Ardizzoni, A., Mak, M. P., Santini, F. C., Elamin, Y. Y., Drilon, A., Wolf, J., Payakachat, N., Uh, M. K., Rajakumar, D., Han, H., . . . Goto, K. (2023a). First-line selpercatinib or chemotherapy and pembrolizumab in RET fusion-positive NSCLC. *New England Journal of Medicine, 389*(20), 1839–1850. https://doi.org/10.1056/NEJMoa2309457（PMID: 37870973）

Zhou, C., Tang, K.-J., Cho, B. C., Liu, B., Paz-Ares, L., Cheng, S., Kitazono, S., Thiagarajan, M., Goldman, J. W., Sabari, J. K., Sanborn, R. E., Mansfield, A. S., Hung, J.-Y., Boyer, M., Popat, S., Mourão Dias, J., Felip, E., Majem, M., Gumus, M., . . . Girard, N. (2023b). Amivantamab plus chemotherapy in NSCLC with EGFR exon 20 insertions. *New England Journal of Medicine, 389*(22), 2039–2051. https://doi.org/10.1056/NEJMoa2306441（PMID: 37870976）

Zhou, Q., Xu, C.-R., Cheng, Y., Liu, Y.-P., Chen, G.-Y., Cui, J.-W., Yang, N., Song, Y., Li, X.-L., Lu, S., Zhou, J.-Y., Ma, Z.-Y., Yu, S.-Y., Huang, C., Shu, Y.-Q., Wang, Z., Yang, J.-J., Tu, H.-Y., Zhong, W.-Z., & Wu, Y.-L. (2021). Bevacizumab plus erlotinib in Chinese patients with untreated, EGFR-mutated, advanced NSCLC (ARTEMIS-CTONG1509): A multicenter phase 3 study. *Cancer Cell, 39*(9), 1279–1291.e3. https://doi.org/10.1016/j.ccell.2021.07.005（PMID: 34388377）

癌症登記中心. (2025). *民國112年長表申報17種癌症期別與治療方式統計*. https://twcr.tw/wp-content/uploads/2025/12/CA17_LF112.pdf

衛生福利部. (2022, May 11). *111年5月15日起免收戒菸藥品部分負擔費用 戒菸省錢又輕鬆* [新聞稿]. https://www.mohw.gov.tw/cp-5268-69501-1.html

衛生福利部. (2023, January 5). *第五癌肺癌篩檢 半年救一百多個家庭* [新聞稿]. https://mohw.gov.tw/cp-2704-73083-1.html

衛生福利部. (2025a, December 30). *公布112年國人癌症登記資料分析結果 守護健康未來 從癌症篩檢開始* [新聞稿]. https://mohw.gov.tw/cp-2704-84987-1.html

衛生福利部. (2025b, January 10). *114年擴大肺癌篩檢服務 新年從健康開始* [新聞稿]. https://mohw.gov.tw/cp-16-81184-1.html

衛生福利部. (2025c, April 8). *肺癌死亡率連9年下降 早期診斷是關鍵* [新聞稿]. https://mohw.gov.tw/cp-16-82095-1.html

衛生福利部. (2026a, March 7). *預防勝治療　推動戒菸強化心血管防治力* [新聞稿]. https://mohw.gov.tw/cp-16-85729-1.html

衛生福利部. (2026b, June 22). *國人死亡人數連續3年下降 十大死因中6項死因人數、死亡率都減少* [新聞稿]. https://mohw.gov.tw/cp-16-86970-1.html

衛生福利部國民健康署. (2025). *台灣癌症登記長表摘錄手冊：民國 114 年（Long Form Revision 2025v.1）*. 台灣癌症登記中心. https://twcr.tw/wp-content/uploads/2025/12/Longform-Manual_Official-version_20251203_W.pdf

衛生福利部國民健康署. (2026, March 1). *「戒菸服務補助計畫」作業須知*（112 年 1 月 1 日生效，113 年 9 月 1 日修訂；115 年 3 月 1 日生效並修正附錄五）[作業須知]. https://www.hpa.gov.tw/Pages/ashx/GetFile.ashx?lang=c&type=2&sid=432b4a45777146169728b89b0119fd46
