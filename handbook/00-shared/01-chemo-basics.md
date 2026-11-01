# 化療基礎與劑量計算（Chemotherapy Basics & Dosing）

| 項目 | 內容 |
|------|------|
| 主要依據 | ASCO 肥胖病人劑量指引 2021、ASCO HBV 臨床意見 2020、ESMO-EONS 外滲指引 2012、ASHP 危害藥品操作指引 2018；第 11–14 節另依各藥美國仿單、ASCO 防護劑指引 2008、CPIC DPYD 指引 2017、ASCO 老年評估指引 2023、ASCO 生育力保存指引 2025、IDSA 導管感染指引 2009、ASCO 中心靜脈導管指引 2013、ASCO／ONS 化療給藥安全標準 2016 |
| 毒性分級 | NCI CTCAE v5.0（理由與 v6.0 差異見第 8 節） |
| 健保規定 | 藥品給付規定 115/10/22 版：10.7.3（化療病人 B 肝預防，第 6 節）、5.5.6 rasburicase 與 11.2.3 mesna（第 11 節）；dexrazoxane、glucarpidase 等逐項註明「原文未見」 |
| 最後更新 | 2026-11-01 |

> 本手冊是學習用整理，不能取代原始指引、仿單、健保公告與院內規範。實際處方以主治醫師判斷與院內流程為準。

---

## 本章重點

- **開化療前先問三件事**：病人撐得住嗎（ECOG）？器官功能夠嗎（CBC、腎、肝）？有沒有隱藏地雷（B 肝、懷孕、過敏史）？
- **劑量三把尺**：細胞毒性藥用 **BSA**（mg/m²）、carboplatin 用 **Calvert 公式**（AUC）、部分藥用 **體重**（mg/kg）或固定劑量（flat dose）。
- **Calvert 公式算出來是「總毫克數」**，不是 mg/m²；GFR 上限 125 mL/min，所以 AUC 5 最多 750 mg、AUC 6 最多 900 mg。
- **肥胖病人用實際體重算足量**，不要常規把 BSA 封頂在 2.0 m²（ASCO 2021）。
- **HBsAg 陽性者開任何全身性抗癌治療都要預防性抗病毒**（單用荷爾蒙治療除外，可依一般 HBV 照護原則追蹤），治療結束後至少再吃 12 個月（ASCO 2020）。健保 10.7.3 第 2 項 (4) 只給付到化療結束後 6 個月（115/10/22 版），兩者不同，見第 6 節。
- **外滲先停、先抽、再處置**；anthracycline 外滲 6 小時內可給 dexrazoxane（台灣無藥證，見第 9、11 節）。
- **輸血門檻不是 8 g/dL**：血流動力學穩定的住院成人 Hb < 7 g/dL 才考慮輸血；心臟手術 7.5、骨科手術或既有心血管疾病 8 g/dL（AABB 2023，第 5 節）。
- **Capecitabine 腎功能**：CrCl 30–50 起始劑量 75%；< 30 一般不使用（歐盟仿單列禁忌，美國現行仿單為「劑量未建立」），以台灣核准仿單為準（第 5、7 節）。
- **抗癌藥四個必背**：累積劑量上限（doxorubicin 心肌病變風險隨累積劑量上升、bleomycin > 400 units）、劑量限制毒性、解毒劑配對（mesna、leucovorin、glucarpidase、dexrazoxane、uridine triacetate、rasburicase）、禁止的給藥途徑（vincristine 只能靜脈）（第 11、14 節）。
- **開 fluoropyrimidine 前先想 DPYD、開 irinotecan 前先想 UGT1A1**：美國仿單對 DPYD 已加框警語；亞洲人 UGT1A1\*6 比白人常見得多（第 12 節）。
- **中心靜脈導管**：給發泡劑前一定先確認有回血；懷疑導管感染（發燒、寒顫）時，導管與周邊靜脈各抽一組血液培養；嗜中性球低下發燒的慣例是每個管腔都抽（第 13 節）。
- **給藥安全**：化療醫囑要有兩個病人識別碼與完整劑量變數，給藥前由兩位合格人員獨立核對（第 14 節）。

---

## 1. 體能狀態：ECOG 與 KPS

體能狀態（performance status, PS）是決定「能不能化療、用多強的化療」最重要的單一指標，也是幾乎所有臨床試驗的收案條件。

| ECOG | 定義（Oken et al., 1982） | 大約對應 KPS |
|------|------------------------|-------------|
| 0 | 完全活動自如，病前活動都能做，無限制 | 90–100 |
| 1 | 劇烈活動受限，但可走動、可做輕度或坐式工作（如輕家事、文書） | 70–80 |
| 2 | 可走動、能自我照顧，但無法工作；清醒時間 >50% 可下床活動 | 50–60 |
| 3 | 僅能有限度自我照顧；清醒時間 >50% 臥床或坐在椅上 | 30–40 |
| 4 | 完全失能，無法自我照顧，完全臥床或坐椅 | 10–20 |
| 5 | 死亡 | 0 |

> [!IMPORTANT]
> **ECOG 判讀的考點**
> - 大多數第三期試驗只收 ECOG 0–1；ECOG 2 需個別評估，ECOG 3–4 一般不建議細胞毒性化療。
> - 例外：有 driver mutation（如 EGFR、ALK）的病人，即使 ECOG 3–4，標靶藥仍可能讓體能狀態明顯改善，不應直接放棄。
> - 關鍵分界：**ECOG 2 =「清醒時間一半以上可下床」**，ECOG 3 =「一半以上躺著或坐著」。

> [!TIP]
> **用「一天的作息」記 ECOG**
> 想像病人一天的清醒時間是一個 16 小時的餅：ECOG 2 的人有超過 8 小時在外面走動；ECOG 3 的人超過 8 小時窩在床或椅子上。查房時直接問「白天大部分時間是躺著還是起來走動？」最快。

---

## 2. 體表面積（BSA）計算

### 2.1 公式

| 公式 | 算式 | 備註 |
|------|------|------|
| Mosteller | BSA (m²) = √[身高 (cm) × 體重 (kg) ÷ 3600] | 計算簡單，臨床最常用（Mosteller, 1987） |
| DuBois | BSA (m²) = 0.007184 × 體重 (kg)^0.425 × 身高 (cm)^0.725 | 歷史最久，部分系統仍採用 |

兩個公式在一般體型差距很小；極端體型（極瘦、極胖）時差距會變大。

> [!NOTE]
> **院內採用哪一個公式**
> 各院化療處方系統（CPOE）內建的 BSA 公式不同，也各有「體重變化多少需重新計算」的規定（常見為 ±5% 或 ±10%），以及劑量四捨五入（dose rounding）規則。請以院內系統與藥劑部規範為準。

### 2.2 肥胖病人怎麼算

ASCO 2021 指引（Griggs et al., 2021）的結論：

- 細胞毒性化療：**用實際體重（actual body weight）計算足量**。肥胖病人對足量化療的耐受度與非肥胖者相當。
- 免疫治療與標靶藥：**給予核准的足量**。
- 不要因為肥胖就常規封頂 BSA（例如 2.0 m²）或用理想體重減量；出現毒性時，減量原則與非肥胖病人相同。

> [!WARNING]
> **「怕太多」而自行減量反而有害**
> 以治癒為目標的化療（如輔助性化療）若因肥胖而經驗性減量，等於降低劑量強度（dose intensity），可能影響療效。看到 BSA 很大的病人，先確認身高體重量測無誤，而不是先砍劑量。

---

## 3. 腎功能估算與 Calvert 公式

### 3.1 Cockcroft-Gault 公式

CrCl (mL/min) = [(140 − 年齡) × 體重 (kg)] ÷ [72 × 血清肌酸酐 (mg/dL)]，女性再 × 0.85（Cockcroft & Gault, 1976）。

很多化療藥的腎功能調整（如 pemetrexed、capecitabine）是用 CrCl 寫在仿單上的，所以腫瘤科仍常用 Cockcroft-Gault。

> [!NOTE]
> **體重與肌酸酐的取捨**
> - 肥胖病人用實際體重代入 Cockcroft-Gault 會高估腎功能；部分醫院改用調整體重（adjusted body weight）。
> - 惡病質或長期臥床病人肌肉量少，肌酸酐偏低（如 0.4–0.5 mg/dL），算出來的 CrCl 會被高估；有些醫院規定肌酸酐低於某值時以固定值代入。
> - 這些做法各院不同，請依院內規範；必要時可用 24 小時尿液 CrCl 或核醫 GFR 實測。

### 3.2 Calvert 公式（carboplatin）

**Carboplatin 劑量（mg）= 目標 AUC ×（GFR + 25）**（Calvert et al., 1989）

- 算出來是**總毫克數（mg）**，不是 mg/m²。
- 實務上以 CrCl 代替 GFR。
- **GFR 上限 125 mL/min**：在使用 IDMS 標準化肌酸酐檢驗的情況下，估算 GFR 可能被高估，美國 FDA 與 NCI CTEP 自 2010 年起建議 GFR 代入值不超過 125 mL/min，因此：

| 目標 AUC | 最大劑量（GFR 以 125 代入） |
|---------|---------------------------|
| AUC 4 | 4 × 150 = **600 mg** |
| AUC 5 | 5 × 150 = **750 mg** |
| AUC 6 | 6 × 150 = **900 mg** |

> [!IMPORTANT]
> **Calvert 公式必背**
> Dose (mg) = AUC × (GFR + 25)；GFR 上限 125 → AUC 5 最多 750 mg、AUC 6 最多 900 mg。
> 「+25」代表 carboplatin 非腎臟途徑的清除。

> [!WARNING]
> **最常見的兩個錯誤**
> 1. 把 Calvert 的結果再乘一次 BSA（當成 mg/m²）→ 劑量變成近兩倍。
> 2. 惡病質病人肌酸酐很低，CrCl 算出 150 以上卻沒有封頂 → 劑量過高、嚴重骨髓抑制。

> [!TIP]
> **Calvert 公式的直覺**
> Carboplatin 主要經腎臟排出（CrCl ≥ 60 mL/min 者約 70% 劑量於 24 小時內由尿液排出），另有一部分經非腎臟途徑清除，公式中的「+25」就是代表這部分。AUC 是「藥物在血中停留的總量」，你想要的總量固定，腎臟排得越快（GFR 越高），就要給越多；排得越慢，就給越少。就像往有破洞的水桶裡倒水，想維持一樣的水位，洞越大要倒越多。

---

## 4. 劑量計算實例

**病人**：62 歲男性，身高 165 cm，體重 64 kg，血清肌酸酐 1.0 mg/dL。醫囑：carboplatin AUC 5 + paclitaxel 175 mg/m² q3w。

**步驟 1：算 BSA（Mosteller）**

BSA = √(165 × 64 ÷ 3600) = √(10,560 ÷ 3600) = √2.933 ≈ **1.71 m²**

**步驟 2：算 paclitaxel**

175 mg/m² × 1.71 m² = 299.25 mg → 依院內 rounding 規則約 **300 mg**

**步驟 3：算 CrCl（Cockcroft-Gault，男性不乘 0.85）**

CrCl = (140 − 62) × 64 ÷ (72 × 1.0) = 4,992 ÷ 72 ≈ **69.3 mL/min**

**步驟 4：算 carboplatin（Calvert）**

Dose = 5 × (69.3 + 25) = 5 × 94.3 ≈ **471 mg**（依院內規則約 470 mg）

**變化題**：同一位病人若因惡病質肌酸酐只有 0.5 mg/dL：

CrCl = 4,992 ÷ (72 × 0.5) = 4,992 ÷ 36 ≈ 138.7 mL/min → **超過 125，以 125 代入** → 5 × (125 + 25) = **750 mg**（若未封頂會算成 818 mg）。

> [!IMPORTANT]
> **考題陷阱**
> 題目給的肌酸酐偏低、算出的 CrCl > 125 時，一定要記得封頂。題目若問「女性」，Cockcroft-Gault 要再乘 0.85。

---

## 5. 化療前檢核（Pre-chemo checklist）

每次給藥前都要逐項確認，並記錄在病歷（progress note 或化療前評估單）。

| 檢核項目 | 一般常見門檻或重點 | 備註 |
|---------|----------------|------|
| 體能狀態 | ECOG 與上次比較 | 明顯退步需與主治醫師討論 |
| 嗜中性球（ANC） | ≥ 1,500/µL | 部分每週給藥方案門檻較低，依處方規範 |
| 血小板（PLT） | ≥ 100,000/µL | 同上 |
| 血紅素（Hb） | 化療前沒有固定的給藥門檻。要不要輸血：血流動力學穩定的住院成人 Hb < 7 g/dL 才考慮（血液腫瘤病人同樣建議 7 g/dL，屬有條件建議、證據確信度低）；心臟手術可用 7.5 g/dL，骨科手術或既有心血管疾病用 8 g/dL（Carson et al., 2023） | 不要只看數字，仍要評估症狀與整體臨床狀況（AABB 也提醒要考慮整體臨床脈絡與輸血以外的選項）；化療前貧血需找原因（出血、缺鐵、腎性）。輸血、ESA 與鐵劑見[支持性照護第 10 節](03-supportive-care.md#10-化療相關貧血血小板低下與輸血) |
| 腎功能 | 依藥物：pemetrexed 在 CrCl < 45 mL/min 不建議使用；capecitabine 在 CrCl 30–50 mL/min 起始劑量減為 75%；< 30 一般不使用（歐盟仿單與舊版仿單列為禁忌，美國 2022 年後仿單改為「劑量未建立」，無替代方案時才個別減量並密切監測），以台灣核准仿單為準 | Cisplatin 的腎功能門檻各院不同。Capecitabine 的美國現行仿單（2026-02-05 版）只把「對 fluorouracil 或 capecitabine 嚴重過敏」列為禁忌（H2-Pharma, 2026）；歐盟 SmPC 仍把 CrCl < 30 mL/min 列為禁忌（European Medicines Agency, n.d.） |
| 肝功能 | 依藥物：docetaxel 在 bilirubin > ULN，或 AST/ALT > 1.5 × ULN 且 ALP > 2.5 × ULN 時不應使用（仿單警語） | Taxane、anthracycline、irinotecan、vinca 類對肝功能敏感 |
| 前次毒性 | 非血液毒性恢復到 ≤ Grade 1（脫髮除外） | 未恢復 → 延後或減量 |
| 身高、體重 | 體重變化超過院內規定比例須重算 BSA | 見第 2 節提示框 |
| B 型肝炎 | 開始全身治療前驗 HBsAg、anti-HBc、anti-HBs | 見第 6 節 |
| 懷孕 | 有生育可能的女性做懷孕檢測，並討論避孕 | 多數抗癌藥具致畸性；避孕與生育力評估見第 12.5 節 |
| 生育力與避孕 | 具生育可能的病人（男女皆然）在第一次性腺毒性化療前，說明對生育力的風險，視意願轉介生殖專科 | 要在治療前談，並記錄在病歷；ASCO 2025 指引（Su et al., 2025），見第 12.5 節 |
| DPYD（fluoropyrimidine 前） | 開 5-FU、capecitabine 前，除非必須立刻治療，美國仿單建議先檢測 DPYD 基因變異；已知完全 DPD 缺乏者避免使用（H2-Pharma, 2026） | 台灣能否檢測、是否有健保給付需向檢驗部確認；陰性不等於安全（東亞常見變異不同），見第 12.1 節 |
| UGT1A1（irinotecan 前） | UGT1A1\*28 或 \*6 同型合子、或 \*6/\*28 複合異型合子，irinotecan 起始劑量考慮至少降一個劑量等級（Pharmacia & Upjohn, 2026a） | 亞洲人 \*6 對偶基因頻率約 13%，比白人（約 0.5%）高很多（Chang et al., 2015 引用），見第 12.2 節 |
| 老年評估（≥ 65 歲） | 做老年評估（geriatric assessment, GA）或至少先做簡短篩檢（如 G8），再決定治療強度 | ASCO 2023 指引（Dale et al., 2023），見第 12.4 節 |
| 過敏史與前置用藥 | Taxane、platinum、單株抗體類需確認 premedication | 第 2 次以後的 carboplatin 仍可能過敏（累積劑量相關）；輸注反應與過敏性休克的處置見[腫瘤急症第 10 節](02-oncologic-emergencies.md#10-輸注反應過敏反應與過敏性休克) |
| 血管通路 | 周邊靜脈或 port-A 狀況；發泡劑盡量走中心靜脈，給藥前先確認回血 | 外滲見第 9 節；導管照護與併發症見第 13 節 |
| 知情同意與衛教 | 新處方或改變處方須重新說明並簽署；第一個週期前要有書面衛教 | 衛教內容與給藥安全標準見第 14 節 |

> [!NOTE]
> **給藥門檻依處方而定**
> 上表 ANC ≥ 1,500/µL、PLT ≥ 100,000/µL 是常見的通用門檻，實際以各處方的 protocol 與院內化療規範為準；例如每週低劑量方案、或以治癒為目標合併 G-CSF 的方案，門檻可能不同。

---

## 6. B 型肝炎篩檢與預防性抗病毒

台灣是 B 型肝炎盛行地區，化療、標靶藥、免疫抑制劑都可能讓潛伏的 HBV 再活化（HBV reactivation），嚴重時造成猛爆性肝炎而死亡，也會迫使抗癌治療中斷。

**ASCO 2020 臨床意見（Hwang et al., 2020）重點：**

1. **所有**即將接受全身性抗癌治療的病人，都要驗三項：**HBsAg、anti-HBc（total Ig 或 IgG）、anti-HBs**；但不要因等報告而延誤抗癌治療。
2. **慢性 HBV（HBsAg 陽性）**：接受**任何**全身性抗癌治療，都要給**預防性抗病毒藥**，持續整個療程，並在**治療結束後至少 12 個月**；之後與肝膽科共同決定。
3. **過去感染（HBsAg 陰性、anti-HBc 陽性）**：
   - 接受高再活化風險治療（**anti-CD20 單株抗體**如 rituximab、**造血幹細胞移植**）→ 預防性抗病毒，持續到治療結束後至少 12 個月；若能確保密切追蹤，也可改為監測、一有再活化跡象立即治療。
   - 其他全身治療 → 治療期間監測 **HBsAg 與 ALT**，出現再活化才開始抗病毒。
4. **單用荷爾蒙治療**：再活化風險低，依一般 HBV 照護原則追蹤即可。

> [!TIP]
> **HBV 是被免疫力蓋住的炭火**
> HBsAg 陽性的人，肝臟裡的 HBV 像被免疫系統壓住的炭火。化療、類固醇、標靶藥把蓋子掀開，火就會重新燒起來。預防性抗病毒藥是「先把炭火澆濕」，而不是等火燒起來再救。

> [!WARNING]
> **常被忽略的再活化情境**
> - 長期高劑量類固醇（例如治療 irAE、腦轉移水腫）。
> - 停止抗病毒藥後的數個月內：停藥後的再活化同樣可能致命，因此「治療結束後至少 12 個月」不能提早停。
> - 病人自行停藥：衛教時要說明為什麼化療結束後還要繼續吃。

### 6.1 健保給付：藥品給付規定 10.7.3

化療與免疫抑制相關的 B 肝抗病毒藥，規定在《藥品給付規定》第 10 節 10.7.3（不在第 9 節抗癌瘤藥物）。藥品範圍是 lamivudine 100 mg、entecavir、telbivudine、tenofovir disoproxil、tenofovir alafenamide。以下只整理與抗癌治療有關的部分，版本為 115/10/22 版。

| 情境 | 條號（修訂日期） | 給付對象與條件 | 事前審查 | 起訖時間 |
|------|----------------|--------------|---------|---------|
| 癌症化學療法，預防 B 肝發作 | 10.7.3 第 2 項 (4)（98/11/1；第 2 項總述最新修訂 114/6/1） | 對象為 HBsAg(+)，或 HBsAg(−) 但 anti-HBc(+)（第 2 項總述）；接受癌症化學療法。本款未限定化療藥物種類，也未要求 HBV DNA 數值 | 否；需照會消化系專科醫師同意 | 化療前 1 週開始，至化療結束後 6 個月 |
| 化療中 B 肝發作 | 10.7.3 第 2 項 (2)（98/11/1） | 同上對象，接受癌症化學療法中 B 肝發作者 | 否；需照會消化系專科醫師同意 | 可長期使用 |
| 免疫抑制劑，預防 | 10.7.3 第 2 項 (9) Ⅰ（110/3/1） | 限 HBsAg(+)，接受 rituximab、anthracycline 類衍生物，或中高劑量類固醇（prednisolone ≥ 20 mg/day 或相當劑量，使用超過 4 週） | 否（非消化系專科醫師需先照會消化系專科醫師，見第 7 項） | 免疫抑制藥物治療前一週起，至停用後 6 個月內 |
| 免疫抑制劑後 B 肝發作 | 10.7.3 第 2 項 (9) Ⅱ（110/3/1） | HBsAg(+)，或 HBsAg(−) 但 anti-HBc(+)，接受免疫抑制藥物治療後 B 肝發作 | 否（同上） | 發作時開始給付，至免疫抑制劑停用後 6 個月 |
| 異體造血幹細胞移植 | 10.7.3 第 2 項 (6)（104/12/1） | 受贈者 HBsAg(+) 或捐贈來源 HBsAg(+)；受贈者需照會消化系專科醫師同意 | 否 | 移植前一週起，至移植後免疫抑制藥物停用後 6 個月內 |

其他共用規定：

- **開立資格（第 7 項，114/6/1）**：醫院需有消化系內科或消化系兒科專科醫師；血液病、腫瘤內科、癌症相關科醫師可開立，但非消化系專科醫師需先照會消化系專科醫師。基層院所的條文未列血液病、腫瘤內科或癌症相關科醫師。
- **劑量**：第 2 項原文沒有訂劑量（entecavir 每日 0.5 mg 的規定寫在第 6 項，對象是第 3 至 4 項），劑量依仿單與消化系專科醫師建議。
- **抗藥株（第 5 項）**：治療或預防中出現 lamivudine、entecavir、telbivudine 抗藥株時，依 10.7.4 第 1 項換藥（HBV DNA 自治療期間最低值上升超過 1 log IU/mL 為抗藥株定義，各救援方案「擇一給付」）。

> [!IMPORTANT]
> **ASCO 的 12 個月與健保的 6 個月不一樣**
> ASCO 2020 建議 HBsAg 陽性者在治療結束後至少繼續預防性抗病毒 12 個月（Hwang et al., 2020）；10.7.3 第 2 項 (4) 只寫「至化學療法結束後 6 個月」。原文沒有寫 6 個月之後如何處理，所以要延長到 12 個月時，需與消化系專科醫師討論並向院內藥劑部確認給付方式，不要自行假設。
> 另一個差別：ASCO 對「HBsAg 陰性、anti-HBc 陽性」只在 anti-CD20 單株抗體或造血幹細胞移植等高風險治療才建議預防，其他治療是監測 HBsAg 與 ALT；健保 (4) 的對象包含這一群，且不限化療藥物種類。

> [!NOTE]
> **以 115/10/22 版為準**
> 以上條號、修訂日期與條件整理自使用者提供的 115/10/22 版《全民健康保險藥品給付規定》原文（`sources/nhi/section9-1151022.md` 與全文 docx）。健保規定會改版，開立前請以最新公告與院內流程為準。

---

## 7. 劑量調整原則

### 7.1 因毒性調整

| 情況 | 常見處理 |
|------|---------|
| 下一週期開始時血球未恢復 | 延後 1 週再評估（ANC、PLT 恢復到門檻） |
| 前一週期發生 Grade 4 嗜中性球低下（ANC < 500/µL，部分仿單要求持續 > 7 天）、Grade 3–4 血小板低下（< 50,000/µL）或發燒性嗜中性球低下（無併發症的 Grade 3 嗜中性球低下，多數仿單不要求減量） | 下一週期減一個劑量等級（常見為減 20–25%），或在治癒目標下加上 G-CSF 次級預防 |
| 非血液毒性 Grade 3–4（如腹瀉、口腔黏膜炎、神經病變） | 暫停至 ≤ Grade 1，再以較低劑量恢復；部分毒性（如嚴重神經病變）需停用該藥 |
| 已減量 | 一般不再往回加量（re-escalation），除非 protocol 允許 |

### 7.2 因器官功能調整

- **腎排除為主**：carboplatin（Calvert）、cisplatin、pemetrexed、methotrexate、capecitabine、etoposide、bleomycin 等。
- **肝代謝或膽道排除為主**：taxanes（paclitaxel、docetaxel）、anthracyclines、irinotecan、vinca alkaloids 等。

### 7.3 治療目標決定調整的方向

- **治癒目標**（輔助性、根治性）：盡量維持劑量強度，必要時加 G-CSF，而不是先減量。
- **緩和目標**（轉移性）：生活品質優先，毒性明顯時減量或延長間隔是合理選擇。

> [!IMPORTANT]
> **劑量調整的考點**
> - 減量通常以「劑量等級」計，常見每級減 20–25%。
> - 治癒性治療優先用 G-CSF 維持劑量強度；緩和性治療優先減量。
> - Pemetrexed：CrCl < 45 mL/min 不建議使用；capecitabine：CrCl 30–50 mL/min 起始劑量 75%；< 30 一般不使用（歐盟仿單與舊版仿單列為禁忌，美國 2022 年後仿單改為「劑量未建立」，無替代方案時才個別減量並密切監測），以台灣核准仿單為準。

---

## 8. CTCAE 分級原則

### 8.1 版本說明

美國國家癌症研究院（NCI）於 2025 年發布 **CTCAE v6.0**（實施 FAQ 日期為 2025-09-09），主要更新三個方向：基線檢驗值已異常病人的分級方式、免疫治療相關不良事件的描述、心臟相關不良事件的分類（NCI, 2025, 2026）。NCI 表示 v6.0 可立即用於多數研究，但 NCI CTEP/DCP 既有研究維持使用 v5.0，新研究則在其資料系統更新後改用 v6.0。

**本手冊以 CTCAE v5.0 為主要分級依據**，原因是：目前大多數已發表的關鍵試驗、藥品仿單的劑量調整表，以及 ASCO 2021、ESMO 2022 的 irAE 指引，都是以 v5.0（或更早版本）撰寫。

v6.0 最明顯的差異之一是**以病人自己的基線值分級**：例如基線肌酸酐 0.5 mg/dL（低於正常下限）上升到 2.0 mg/dL，即基線的 4 倍、約 1.54 × ULN（參考範圍 0.7–1.3 mg/dL）。照 v5.0 原文，肌酸酐上升的 Grade 3 為「> 3.0 × 基線；> 3.0–6.0 × ULN」，分號代表「或」，符合其一即可（見 8.3 表），所以本例在 v5.0 已是 Grade 3；ONS 的文章只對照 ULN 而判為 v5.0 Grade 2，與 v5.0 原文不符（Oncology Nursing Society, 2026）。v6.0 把基線倍數條件改為「基線低於 LLN 時」才適用，本例在 v6.0 同樣是 Grade 3。兩版真正會判得不同的是基線正常的病人：例如基線 0.8 mg/dL 升到 2.5 mg/dL（約 3.1 × 基線、1.9 × ULN），v5.0 照字面為 Grade 3，v6.0 不適用基線倍數、只看 ULN，判為 Grade 2。

> [!NOTE]
> **院內若已改用 v6.0**
> 部分醫院或新開的臨床試驗可能已改用 v6.0，請依院內規範或試驗 protocol 指定的版本記錄。

> [!CAUTION]
> **待核對：v6.0 細項門檻**
> 本手冊尚未逐項比對 v6.0 Excel 檔的所有門檻；下表數值為 v5.0。若院內已採 v6.0，請以 NCI 官方 v6.0 檔案及其 v5.0–v6.0 對照表為準。

### 8.2 通用分級定義（v5.0）

| Grade | 定義 |
|-------|------|
| 1 | 輕度；無症狀或輕微症狀；僅需臨床觀察；不需介入 |
| 2 | 中度；需最低限度、局部或非侵入性介入；**影響工具性日常生活活動**（instrumental ADL，如煮飯、購物、打電話、理財） |
| 3 | 嚴重或具醫療重要性但未立即危及生命；需住院或延長住院；失能；**影響自我照顧日常生活活動**（self-care ADL，如洗澡、穿衣、進食、如廁、服藥） |
| 4 | 危及生命；需緊急介入 |
| 5 | 與不良事件相關的死亡 |

> [!TIP]
> **Grade 2 與 3 的分界：ADL 的種類**
> Grade 2 影響的是「出門辦事的能力」（工具性 ADL），Grade 3 影響的是「照顧自己身體的能力」（自我照顧 ADL）。問病人「還能自己去市場、煮飯嗎？」和「洗澡、穿衣需要人幫忙嗎？」就能快速分級。

### 8.3 常用項目（v5.0）

| 項目 | Grade 1 | Grade 2 | Grade 3 | Grade 4 |
|------|---------|---------|---------|---------|
| 嗜中性球減少（/µL） | < LLN–1,500 | < 1,500–1,000 | < 1,000–500 | < 500 |
| 血小板減少（/µL） | < LLN–75,000 | < 75,000–50,000 | < 50,000–25,000 | < 25,000 |
| 貧血（Hb, g/dL） | < LLN–10.0 | < 10.0–8.0 | < 8.0；需輸血 | 危及生命 |
| ALT／AST 上升（基線正常） | > ULN–3.0 × ULN | > 3.0–5.0 × ULN | > 5.0–20.0 × ULN | > 20.0 × ULN |
| 膽紅素上升（基線正常） | > ULN–1.5 × ULN | > 1.5–3.0 × ULN | > 3.0–10.0 × ULN | > 10.0 × ULN |
| 肌酸酐上升 | > ULN–1.5 × ULN | > 1.5–3.0 × 基線；> 1.5–3.0 × ULN | > 3.0 × 基線；> 3.0–6.0 × ULN | > 6.0 × ULN |
| 腹瀉 | 比基線每日增加 < 4 次 | 增加 4–6 次 | 增加 ≥ 7 次；需住院；影響自我照顧 ADL | 危及生命 |
| 嘔吐 | 不需介入 | 需門診靜脈補液；需藥物介入 | 需管灌、TPN 或住院 | 危及生命 |
| 口腔黏膜炎 | 無症狀或輕微 | 中度疼痛或潰瘍，不影響進食；需調整飲食 | 嚴重疼痛，影響進食 | 危及生命 |
| 周邊感覺神經病變 | 無症狀 | 中度症狀；影響工具性 ADL | 嚴重症狀；影響自我照顧 ADL | 危及生命 |
| 斑丘疹 | < 10% BSA | 10–30% BSA；影響工具性 ADL；或 > 30% 但症狀輕微 | > 30% BSA 且有中重度症狀；影響自我照顧 ADL | — |
| 肺炎（pneumonitis） | 無症狀；僅影像發現 | 有症狀；需藥物治療；影響工具性 ADL | 嚴重症狀；影響自我照顧 ADL；需氧氣 | 危及生命的呼吸衰竭 |
| 發燒性嗜中性球低下 | — | — | ANC < 1,000/µL 合併單次體溫 > 38.3°C 或 ≥ 38°C 持續超過 1 小時 | 危及生命 |

> [!IMPORTANT]
> **CTCAE 與 IDSA 的發燒性嗜中性球低下定義不同**
> CTCAE v5.0 用 ANC < 1,000/µL 判定 Grade 3；IDSA 的臨床處置定義用 ANC < 500/µL（或預期 48 小時內降到 < 500）。考題問「分級」用 CTCAE，問「是否啟動 FN 處置」用 IDSA，詳見[腫瘤急症](02-oncologic-emergencies.md)。

---

## 9. 血管外滲（Extravasation）

### 9.1 藥物分類

| 分類 | 定義 | 代表藥物 |
|------|------|---------|
| 發泡劑（vesicant），與 DNA 結合 | 外滲後持續傷害組織，可能壞死、潰瘍 | Anthracyclines（doxorubicin、epirubicin、daunorubicin、idarubicin）、mitomycin、dactinomycin、mechlorethamine |
| 發泡劑，不與 DNA 結合 | 可造成壞死，但機轉與處置不同 | Vinca alkaloids（vincristine、vinblastine、vinorelbine）、taxanes（paclitaxel、docetaxel）、trabectedin |
| 刺激劑（irritant） | 疼痛、發炎、靜脈炎，大量外滲偶可壞死 | Platinum（cisplatin、carboplatin、oxaliplatin）、etoposide、irinotecan、topotecan、5-FU、dacarbazine、ifosfamide |
| 非發泡劑 | 一般不造成組織傷害 | 多數單株抗體、methotrexate、pemetrexed、gemcitabine、cyclophosphamide 等 |

> [!CAUTION]
> **待核對：發泡劑與刺激劑的分類在不同文獻並不一致**
> Paclitaxel、docetaxel、oxaliplatin 在不同參考資料中被歸為發泡劑或刺激劑。本表參考 ESMO-EONS 2012 的分類架構（Pérez Fidalgo et al., 2012），因未能取得原文全文逐項核對，請以院內藥劑部公告的發泡劑清單為準。

### 9.2 處置流程

**通用步驟（所有藥物）：**

1. **立即停止輸注**，但先**不要拔針**。
2. 接空針，**從原管路回抽**殘留藥液與血液。
3. 周邊靜脈針頭回抽後拔除；中心靜脈導管或植入式 port 的針頭／導管先保留，由醫師評估（必要時以影像確認針頭位置與導管完整性）後再處理（見 13.8）。**不要對外滲部位加壓**。
4. 用筆標出範圍、拍照，抬高患肢。
5. 通知醫師，依藥物給予特定解毒劑與冷敷或熱敷。
6. 記錄：時間、藥名、濃度、估計外滲量、症狀、處置；安排 24 小時、1 週等追蹤，持續疼痛或壞死時會診整形外科。

**依藥物的特定處置：**

| 藥物類別 | 敷法 | 解毒劑或特殊處置 |
|---------|------|---------------|
| Anthracyclines | 冷敷 | **Dexrazoxane IV**，**6 小時內**開始：D1 1,000 mg/m²、D2 1,000 mg/m²、D3 500 mg/m²（每日上限 D1、D2 各 2,000 mg、D3 1,000 mg；CrCl < 40 mL/min 劑量減半），每次輸注 1–2 小時，D2、D3 與 D1 同一時段（±3 小時）開始，打在對側肢體（Mouridsen et al., 2007；CNX Therapeutics, 2024，英國 Savene SmPC）；給藥前至少 15 分鐘移除冷敷 |
| Vinca alkaloids | **熱敷**（不可冷敷） | 局部皮下注射 hyaluronidase |
| Mitomycin、dactinomycin | 冷敷 | 依院內規範 |
| Oxaliplatin | 避免冷敷（冷會誘發神經症狀） | 依院內規範 |

> [!IMPORTANT]
> **外滲處置口訣：DNA 結合用冷、vinca 用熱**
> - Anthracycline：冷敷 + dexrazoxane（6 小時內，3 天療程：1,000／1,000／500 mg/m²）。
> - Vinca alkaloids：熱敷 + hyaluronidase。
> - 第一步永遠是「停、留針、回抽」。

> [!TIP]
> **冷熱敷的道理**
> 冷敷讓血管收縮，把藥「關」在原地、減少擴散，適合會與 DNA 結合、局部持續破壞的 anthracycline；熱敷讓血管擴張，把藥「推散」稀釋，適合 vinca 這類稀釋後傷害就減少的藥物。

> [!CAUTION]
> **待核對：dexrazoxane 在台灣的取得方式**
> 依 2026-10-27 的 TFDA 公開資料，查不到任何品牌的 dexrazoxane（含 Savene、Cardioxane、Zinecard）台灣藥證；115/10/22 版藥品給付規定全文搜尋 dexrazoxane 與上述品名也都沒有結果（原文未見／無健保給付）。是否可經專案進口或院內另有取得管道，本手冊無法確認。藥證、健保給付與院內是否備藥是三件不同的事，遇到 anthracycline 外滲時，實際可用的解毒劑以院內藥劑部公告與外滲處置包為準，不要假設一定有 dexrazoxane。其他防護劑與解毒劑的總表見第 11.4 節。

> [!NOTE]
> **院內外滲處置包**
> 解毒劑種類、存放位置與冷熱敷時間（例如每次 15–20 分鐘、每日幾次、持續幾天）各院規範不同，實習時先找到單位的外滲處置包與標準作業程序。

---

## 10. 抗癌藥物的安全操作

多數抗癌藥屬於危害藥品（hazardous drugs），長期低劑量暴露可能影響醫護人員的生殖與健康。ASHP 指引（Power & Coyne, 2018）的重點：

- **調配**：在生物安全櫃（Class II BSC）或密閉式隔離操作箱（CACI）內進行；建議使用密閉式藥物傳輸裝置（closed system drug-transfer device, CSTD）。
- **個人防護裝備**：給藥時戴**兩層**經化療測試的手套、穿低滲透性隔離衣；有噴濺風險時加護目鏡或面罩。
- **溢出處理**：使用溢出處理包（spill kit），依院內流程處理並通報。
- **病人排泄物**：給藥後一段時間內處理尿液、糞便、嘔吐物須戴手套與隔離衣（常見為 48 小時，依院內規範）。
- **懷孕或哺乳中的人員**：依院內職安規定調整工作。

---

## 11. 抗癌藥分類、劑量限制毒性與解毒劑

抗癌藥的考題與臨床判斷，幾乎都能還原成四個問題：這類藥怎麼殺細胞？先傷哪個器官（劑量限制毒性，dose-limiting toxicity, DLT）？累積到多少要停？出事用什麼救？本節是類別層級的整理；各藥的劑量、週期與前置用藥見各癌別章的處方表，高劑量 methotrexate 與 ifosfamide 的完整病房流程放在骨肉瘤與軟組織肉瘤章，本節只放安全摘要。

### 11.1 本節重點

- **DLT 決定一類藥的上限**：烷化劑與多數細胞毒性藥看骨髓；cisplatin 看腎；anthracycline 看心臟（累積劑量）；bleomycin 看肺（累積劑量）；vinca 與 taxane 看神經；fluoropyrimidine 看黏膜與腹瀉。
- **累積劑量要自己算**：doxorubicin 心肌病變機率在 300／400／450／500 mg/m² 分別約 1–2%、3–5%、5–8%、6–20%（每 3 週給藥）；epirubicin 累積 900 mg/m² 應盡量避免；bleomycin 總量超過 400 units 肺毒性明顯增加。前面用過的 anthracycline、縱隔腔放射治療與 trastuzumab 都要一併考慮。
- **解毒劑要配對、要抓時間點**：mesna 與 ifosfamide 同時給；leucovorin 在 HD-MTX 開始後 24 小時給；glucarpidase 只用在 MTX 清除延遲且腎功能受損時；uridine triacetate 要在 5-FU／capecitabine 結束後 96 小時內開始；dexrazoxane 用於 doxorubicin 累積 ≥ 300 mg/m² 後要繼續用藥的心臟保護，或 anthracycline 外滲 6 小時內；rasburicase 前先確認 G6PD。
- **台灣的取得狀況是另一回事**：dexrazoxane、glucarpidase、uridine triacetate、sodium thiosulfate（PEDMARK）在 2026-10-27 的 TFDA 資料中都查不到藥證，115/10/22 版健保原文也未見（第 11.4 節）。

### 11.2 細胞毒性藥物：依類別整理

| 類別（代表藥） | 機轉與細胞週期 | 劑量限制毒性 | 重點器官毒性與監測 |
|--------------|--------------|------------|------------------|
| 烷化劑（alkylating agents）：cyclophosphamide、ifosfamide | 兩者都是前驅藥，經肝臟 CYP450 活化，以烷基化使 DNA 交聯（BluePoint, 2026; Fresenius Kabi, 2026b）。對細胞週期沒有特異性 | 骨髓抑制（ifosfamide 為加框警語） | 出血性膀胱炎（代謝物 acrolein；用 mesna 與水化預防）。Ifosfamide 加框：神經毒性（腦病變，可致死）、腎毒性。Cyclophosphamide：心臟毒性（心肌炎、心包膜積液、心衰竭）、肺毒性、不孕、次發性惡性腫瘤。詳見 11.6 |
| 鉑類（platinum）：cisplatin、carboplatin、oxaliplatin | 與 DNA 形成鏈間與鏈內交聯（WG Critical Care, 2026）；carboplatin 仿單稱此作用與細胞週期無關（Natco, 2026） | cisplatin：腎毒性（劑量相關且累積）；carboplatin：骨髓抑制（劑量相關）；oxaliplatin：累積性感覺神經病變 | Cisplatin 加框：腎毒性、周邊神經病變、嚴重噁心嘔吐、骨髓抑制；耳毒性累積，先影響高頻（4,000–8,000 Hz）。Carboplatin：數分鐘內可出現類過敏反應，貧血可能累積。Oxaliplatin 加框：過敏／anaphylaxis（任何週期、數分鐘內都可能發生）；約 56% 的病人有急性冷誘發感覺異常，要避免冰冷（Sagent, 2025） |
| 抗代謝物（antimetabolites）：5-FU、capecitabine（前驅藥，在體內轉成 5-FU） | 代謝物 FdUMP 與葉酸輔因子結合 thymidylate synthase，阻斷 thymidylate 合成，抑制 DNA 合成；作用於 DNA 合成期（H2-Pharma, 2026） | 腹瀉、黏膜炎、骨髓抑制；capecitabine 另有手足症候群（EU SmPC 列為劑量限制毒性；European Medicines Agency, n.d.） | 加框：DPD 缺乏的嚴重或致死毒性（第 12.1 節）；capecitabine 併用 warfarin 出血風險。心臟毒性（心肌缺血、心律不整、心衰竭）。腎功能調整見第 5、7 節 |
| 抗代謝物：gemcitabine | 核苷類似物，殺死正在合成 DNA 的細胞並阻擋 G1／S 交界（Meitheal, 2025） | 骨髓抑制；輸注超過 60 分鐘或比每週一次更頻繁會增加毒性 | 肺毒性、溶血性尿毒症候群（HUS）、肝毒性、嚴重皮膚反應；用藥前與期間監測腎功能與肝功能（Meitheal, 2025） |
| 抗代謝物：pemetrexed | 葉酸類似物，抑制 thymidylate synthase、DHFR、GARFT（Eli Lilly, 2023） | 骨髓抑制 | 每次都要有前置：folic acid 400–1,000 mcg 每日（首劑前 7 天開始，至最後一劑後 21 天）、維生素 B12 1 mg 肌肉注射（首劑前 1 週，之後每 3 個週期）、dexamethasone 4 mg 一日兩次（給藥前一天、當天、隔天）；CrCl < 45 mL/min 不建議使用（第 5 節） |
| 抗代謝物：methotrexate | 抑制 dihydrofolate reductase，干擾 DNA 合成、修復與細胞複製；增殖快的組織（骨髓、口腔與腸黏膜）最敏感（Accord, 2026） | 黏膜炎、骨髓抑制；高劑量時腎毒性 | 高劑量（≥ 500 mg/m²）一定要 leucovorin 解救；與 PPI、NSAID、penicillin、sulfonamide（含 TMP-SMX）等交互作用。詳見 11.5 |
| 蒽環類（anthracyclines）：doxorubicin、epirubicin | DNA 嵌入並與 topoisomerase II 形成可切割複合物，抑制核酸複製與轉錄（Pfizer, 2026a; Pharmacia & Upjohn, 2026b） | 骨髓抑制（急性）；心肌病變（累積劑量相關） | 加框：心肌病變、次發性 AML／MDS、外滲組織壞死（doxorubicin）。給藥前與期間定期評估 LVEF；累積劑量見 11.3；外滲處置見第 9 節 |
| Topoisomerase I 抑制劑：irinotecan、topotecan | 與 topoisomerase I—DNA 複合物結合，阻止單股斷裂重接，DNA 合成時變成雙股斷裂（Pharmacia & Upjohn, 2026a; Fresenius Kabi, 2026c） | irinotecan：腹瀉、嗜中性球低下（加框）；topotecan：骨髓抑制（加框；第 1 週期需 ANC ≥ 1,500/mm³ 且血小板 ≥ 100,000/mm³） | Irinotecan 加框：早發與遲發性腹瀉、骨髓抑制；早發性腹瀉（膽鹼性）用 atropine，遲發性腹瀉用 loperamide，見[支持性照護](03-supportive-care.md#5-腹瀉)第 5 節；UGT1A1 基因型見第 12.2 節 |
| Topoisomerase II 抑制劑：etoposide | 抑制 topoisomerase II 造成 DNA 股斷裂，主要作用在細胞週期的 G2 期（Fresenius Kabi, 2026a） | 骨髓抑制（仿單警語：嚴重骨髓抑制可導致感染或出血） | 輸注反應；口服與靜脈劑型的劑量不同，依處方 |
| 紫杉醇類（taxanes）：paclitaxel、docetaxel、nab-paclitaxel | 與微管結合並使其穩定、阻止解聚，造成微管束與有絲分裂抑制（Teva Parenteral Medicines, 2026; Mylan, 2026） | paclitaxel：骨髓抑制（以嗜中性球低下為主）、周邊神經病變；docetaxel：嗜中性球低下；nab-paclitaxel：基線 ANC < 1,500/mm³ 不可使用（加框；Exelan, 2026） | Paclitaxel 加框：嚴重過敏（臨床試驗中 2–4% 的病人，即使前置用藥仍有致死案例；發生嚴重過敏者不可再用該藥）。前置用藥為 dexamethasone 20 mg 口服（給藥前約 12 與 6 小時）、diphenhydramine 50 mg 靜脈、H2 阻斷劑（給藥前 30–60 分鐘）。Docetaxel 加框：肝功能異常時治療相關死亡增加（bilirubin > ULN，或 AST／ALT > 1.5 × ULN 且 ALP > 2.5 × ULN 應避免使用）、液體滯留、過敏；前置 dexamethasone 8 mg 一日兩次共 3 天，從給藥前一天開始 |
| 長春花生物鹼（vinca alkaloids）：vincristine、vinorelbine | 抑制微管形成，使分裂中的細胞停在中期（vincristine 仿單；Hospira, 2026） | vincristine：神經毒性；vinorelbine：骨髓抑制（加框） | Vincristine 加框：**只能靜脈，其他途徑給藥會致死**（鞘內給藥是致命錯誤，見第 14.3 節）；周邊神經病變、便秘、腹部絞痛、麻痺性腸阻塞（絞痛合併空的直腸要想到便秘）。屬發泡劑：熱敷加 hyaluronidase（Hospira, 2026） |
| 其他：bleomycin | 引起 DNA 單股與雙股斷裂，使細胞停在 G2 與有絲分裂期（Meitheal, 2026） | 肺毒性（加框：肺炎進展為肺纖維化） | 累積劑量 > 400 units 風險明顯上升，但低劑量與年輕病人也可能發生；約 1% 的淋巴瘤病人出現特異體質反應（低血壓、意識混亂、發燒、寒顫、喘鳴） |

> [!TIP]
> **細胞週期特異性：像在關卡攔人**
> 週期特異性藥物像在固定關卡攔人：gemcitabine 與 methotrexate 攔在 DNA 合成期，vinca 與 taxane 攔在有絲分裂期，只對正在走到那一關的細胞有效，所以常要重複給藥，等更多細胞走過來。週期非特異性藥物如烷化劑與鉑類，是直接破壞 DNA 這個「地圖」，細胞走到哪都受影響，劑量越高殺得越多，骨髓也越容易被一起傷到。這是教學上的簡化，同一類藥對各週期的作用並非截然二分。

#### 標靶藥與免疫治療：各類別要記的毒性

標靶藥沒有「累積劑量上限」的概念，但每一類都有一個固定要查的器官。下表只列類別層級的重點，各藥劑量與減量規則見各癌別章。

| 類別（代表藥） | 作用 | 要記的毒性 | 開藥前與期間的監測 |
|--------------|------|----------|------------------|
| EGFR TKI：gefitinib、erlotinib、afatinib、dacomitinib、osimertinib | 抑制 EGFR 酪胺酸激酶 | 腹瀉、皮疹（痤瘡樣皮疹）、甲溝炎、間質性肺病（ILD）；afatinib 仿單另列肝毒性、胃腸穿孔、角膜炎（Boehringer Ingelheim, 2025） | 皮膚與腹瀉分級處置、呼吸症狀；各藥減量規則見[肺癌章](../01-lung-cancer.md)第 6 節 |
| ALK／ROS1 TKI：alectinib、lorlatinib 等 | 抑制 ALK／ROS1 | 各藥不同：alectinib 為肌痛與 CK 上升、心搏過緩、膽紅素上升；lorlatinib 為血脂異常與情緒認知變化 | 見[肺癌章](../01-lung-cancer.md)第 5、6 節；CYP3A 誘導劑與 lorlatinib 的交互作用見 14.5 |
| HER2 抗體與抗體藥物複合體：trastuzumab、trastuzumab deruxtecan（T-DXd） | 抗 HER2 | Trastuzumab 加框：心肌病變、輸注反應、胚胎胎兒毒性、肺毒性，與 anthracycline 併用風險最高（Genentech, 2026c）。T-DXd 加框：ILD 與胚胎胎兒毒性，另有嗜中性球低下與 LVEF 下降（Daiichi Sankyo, 2026） | 治療前與期間評估 LVEF；T-DXd 追蹤咳嗽、呼吸喘、發燒等 ILD 症狀；各藥 LVEF 暫停規則見[乳癌章](../03-breast-cancer.md#62-抗-her2-治療lvef-監測與暫停規則)第 6.2 節，T-DXd 的 ILD 見[第 6.7 節](../03-breast-cancer.md#67-抗體藥物複合體t-dxdt-dm1sacituzumab-govitecandato-dxd) |
| CDK4/6 抑制劑：ribociclib（其他藥物見乳癌章） | 抑制 CDK4/6 | Ribociclib 仿單警語：ILD／肺炎、嚴重皮膚反應、QT 間期延長、肝膽毒性、濃度相關的嗜中性球低下（早期乳癌 NATALEE 中 94% 嗜中性球數下降，含 45% Grade 3–4）（Novartis, 2026b） | CBC：開始前、前 2 個週期每 2 週、之後 4 個週期每個週期開始時；另有 ECG 與肝功能；其他 CDK4/6 抑制劑與完整監測時程見[乳癌章](../03-breast-cancer.md#65-cdk46-抑制劑嗜中性球肝功能心電圖腹瀉)第 6.5 節 |
| PARP 抑制劑：olaparib | 抑制 PARP | 貧血（常見）、骨髓發育不良症候群／AML、肺炎、靜脈血栓、肝毒性（AstraZeneca, 2025） | 定期血球；持續性血球低下要評估 MDS／AML |
| 抗血管新生：bevacizumab、ramucirumab | 抗 VEGF 或 VEGFR2 | 高血壓、蛋白尿、出血、動脈血栓、胃腸穿孔、傷口癒合不良；bevacizumab 另列 PRES（Genentech, 2025; Eli Lilly, 2026） | 每次給藥前量血壓與尿蛋白；擇期手術前依仿單停藥 |
| 免疫檢查點抑制劑 | 解除 T 細胞的抑制訊號 | 免疫相關不良事件（irAE），幾乎所有器官都可能 | 見[免疫治療副作用](04-irae.md)全章 |
| GIST／肉瘤 TKI：imatinib、pazopanib、regorafenib | 抑制 KIT、PDGFR、VEGFR 等多種激酶 | Pazopanib 與 regorafenib 加框：嚴重甚至致死的肝毒性（Sun Pharmaceutical Industries, 2026; Bayer, 2026）；imatinib：體液滯留與水腫、血液毒性、心衰竭、肝毒性（Novartis, 2026a）；regorafenib 另有皮膚毒性與高血壓 | 肝功能：regorafenib 開始前、前 2 個月至少每 2 週、之後每月；pazopanib 的肝功能與血壓見[肉瘤章](../04-sarcoma.md#67-pazopanib肝毒性與高血壓)第 6.7 節，imatinib、regorafenib 等 GIST 用 TKI 的監測與暫停規則見[第 6.8 節](../04-sarcoma.md#68-gist-的-tkiimatinibsunitinibregorafenibripretinibavapritinib) |
| 拓樸異構酶 I 抗體藥物複合體：sacituzumab govitecan | 抗 Trop-2 加 SN-38 | 加框：嗜中性球低下與腹瀉；UGT1A1\*28 同型合子風險較高（Gilead, 2026） | 見第 12.2 節；毒性與暫停規則見[乳癌章](../03-breast-cancer.md#67-抗體藥物複合體t-dxdt-dm1sacituzumab-govitecandato-dxd)第 6.7 節 |

### 11.3 累積劑量上限

| 藥物 | 仿單與文獻的累積劑量警示 | 補充 |
|------|----------------------|------|
| Doxorubicin | 心肌病變機率（每 3 週給藥）：300 mg/m² 約 1–2%、400 約 3–5%、450 約 5–8%、500 約 6–20%（Pfizer, 2026a）。回溯分析估計 550 mg/m² 時充血性心衰竭約 26%，且 > 65 歲在 400 mg/m² 後風險更高（Swain et al., 2003） | 肉瘤常見的 6 個週期 × 75 mg/m² 剛好是 450 mg/m²。縱隔腔放療與 cyclophosphamide、trastuzumab 併用會加乘風險 |
| Epirubicin | 心肌病變：550 mg/m² 約 0.9%、700 約 1.6%、900 約 3.3%；累積 900 mg/m² 應盡量避免（Pharmacia & Upjohn, 2026b） | 不同 anthracycline 的累積劑量要換算相加，但換算係數本手冊未取得可靠原文，見下方待核對 |
| Daunorubicin | 成人累積劑量超過 400–550 mg/m² 後心肌毒性增加；兒童 2 歲以上為 300 mg/m²（Hisun, 2026） | 縱隔腔放療後耐受上限更低 |
| Idarubicin | 成人累積劑量超過 90 mg/m² 後充血性心衰竭機率上升（Pfizer, 2026b） | 要把過去用過的其他 anthracycline 與 anthracenedione 一起算入 |
| Mitoxantrone | 癌症病人累積劑量最多 140 mg/m² 時，有症狀心衰竭風險估計 2.6%；多發性硬化症病人不可超過 140 mg/m²（Hospira, 2025） | 治療後仍需追蹤 LVEF |
| Bleomycin | 肺毒性隨劑量上升，總量超過 400 units 時明顯增加，需格外謹慎；與其他抗癌藥併用時更低劑量也可能發生（Meitheal, 2026） | 年長者風險較高 |
| Cisplatin | 腎毒性與周邊神經病變為劑量相關且累積，耳毒性也累積（WG Critical Care, 2026） | 仿單未訂單一的終身劑量上限，改以監測與減量處理 |
| Ifosfamide | 兒童研究：總劑量維持在 84 g/m² 以下可降低（不是消除）腎毒性，超過 119 g/m² 風險很高（Skinner et al., 2000） | 成人沒有對應的標準上限；腎小管損傷可在治療後數月甚至數年才出現 |

> [!CAUTION]
> **待核對：anthracycline 之間的累積劑量換算**
> 本手冊沒有取得 epirubicin 與 doxorubicin（或 daunorubicin、idarubicin）之間可靠的等效換算係數，所以上表是各藥各自的仿單警示，不可自行用某個「係數」把不同藥物加總。病人曾用過其他 anthracycline 時，請由主治醫師與藥劑部依院內規範換算並記錄累積劑量。

> [!WARNING]
> **心臟毒性監測用同一種方法**
> LVEF 的測量方法（超音波或 MUGA）每次要一致，不同方法的數值不能直接比較；曾用 anthracycline 後再用 trastuzumab 的病人，是心臟毒性的高風險族群（Pfizer, 2026a; Genentech, 2026c）。累積劑量超過 300 mg/m² 後，LVEF 追蹤頻率要增加。

### 11.4 解毒劑與防護劑：何時給、給多少、台灣有沒有

| 毒性或情境 | 解毒劑或防護劑 | 劑量與時機 | 證據與限制 | 台灣取得狀況 |
|-----------|-------------|----------|----------|-------------|
| Ifosfamide（與高劑量 cyclophosphamide）出血性膀胱炎 | **Mesna** | 靜脈單獨給法：與 ifosfamide 同時給 ifosfamide 劑量的 20%（w/w），並在 4 小時與 8 小時後各再給 20%，一天共 60%；ifosfamide 給藥的每一天都重複；改變 ifosfamide 劑量時維持比例。同時每天水化至少 2 L（Eugia, 2026b; Fresenius Kabi, 2026b） | 標準劑量 ifosfamide 有證據；ASCO 1999 認為 ifosfamide > 2.5 g/m²/day 的證據不足（Hensley et al., 1999），2008 年更新未再找到新的 mesna 隨機試驗（Hensley et al., 2009）。連續輸注或高劑量的 mesna 沒有仿單時程，依處方 | 健保 11.2.3 mesna（如 Uromitexan）：限癌症或骨髓移植病例使用大量 Endoxan、ifosphamide 類藥物時使用；原文未標修訂日期。TFDA 藥證本手冊未核對 |
| 高劑量 methotrexate（≥ 500 mg/m²） | **Leucovorin**（calcium folinate） | 從 MTX 開始後 24 小時起：15 mg（約 10 mg/m²）每 6 小時一次共 10 次，直到 MTX 低於 0.05 µM；延遲清除時依仿單 Table 2 加量（Sagent, 2026） | 不可晚於 42–48 小時才開始；過度解救可能與治療失敗有關，依使用的 protocol，不要混用不同算法（Ramsey et al., 2018） | TFDA 有 calcium folinate（適應症含葉酸拮抗劑如 methotrexate 過量之解毒劑）；levoleucovorin 無藥證。健保第 9 節與全檔無 leucovorin 專條，只出現在 FOLFIRINOX 等併用條文（原文未見專條） |
| HD-MTX 延遲清除且腎功能受損（MTX > 1 µmol/L） | **Glucarpidase** | 50 units/kg 靜脈 5 分鐘，單次；leucovorin 與其間隔 ≥ 2 小時；之後 48 小時內 MTX 用 HPLC 測定（DAMPA 會讓免疫分析高估）；最好在 MTX 開始後 48–60 小時內給（Ramsey et al., 2018; BTG International, 2024） | 預期清除正常者不要用，以免 MTX 暴露不足；沒有 glucarpidase 時用高劑量 leucovorin，透析效果不一 | TFDA 查無藥證；專案進口可行性未核對。健保原文未見 |
| Anthracycline 心臟保護 | **Dexrazoxane** | 與 doxorubicin 比例 10:1（例如 500 mg/m² 對 50 mg/m²），一定先給 dexrazoxane（不可先給 doxorubicin），dexrazoxane 輸注結束後 30 分鐘內再給 doxorubicin；CrCl < 40 mL/min 劑量減半；仿單適應症為轉移性乳癌、doxorubicin 已累積 300 mg/m² 且要繼續使用者，不可在 doxorubicin 開始時就用（Eugia, 2026a） | ASCO 2008：不建議常規用於輔助或初始 doxorubicin 治療，可考慮用於累積 > 300 mg/m² 且續用 doxorubicin 有益者（Hensley et al., 2009）；兒童研究未見療效損失（Asselin et al., 2016） | TFDA 查無藥證；健保原文未見 |
| Anthracycline 外滲 | **Dexrazoxane**（不同療程） | 6 小時內開始，共 3 天：1,000／1,000／500 mg/m²；每日上限與腎功能減量見第 9.2 節（Mouridsen et al., 2007） | 54 位病人中 98.2% 免於手術；為單臂前瞻研究 | 同上；外滲處置包內有沒有要自行確認 |
| Cisplatin 累積腎毒性 | **Amifostine** | 910 mg/m² 靜脈輸注 15 分鐘，在化療前 30 分鐘開始，每天一次；先給 dexamethasone 20 mg 與 5-HT3 拮抗劑（Legacy, 2026） | 仿單適應症為晚期卵巢癌的 cisplatin 累積腎毒性；仿單載明：化療可能帶來存活或治癒利益的情境應避免使用（Legacy, 2026）；ASCO 2008 認為可考慮用於預防 cisplatin 腎毒性，但不建議用來預防鉑類的神經毒性或耳毒性（Hensley et al., 2009） | 健保原文未見；TFDA 藥證本手冊未核對 |
| 兒童 cisplatin 耳毒性 | **Sodium thiosulfate**（PEDMARK） | 依體重 10／15／20 g/m²（< 5 kg／5–10 kg／> 10 kg），在 cisplatin 輸注結束後 6 小時開始，下一次 cisplatin 前至少 10 小時；cisplatin 輸注超過 6 小時者未建立（Fennec, 2025） | 限 ≥ 1 個月、局限性非轉移性實體瘤；ACCL0431 轉移性次群 3 年存活 45% 對 84%，所以 2020 指引對轉移性疾病建議不常規使用（Freyer et al., 2017; Freyer et al., 2020）；SIOPEL 6 聽力損失 33% 對 63%（Brock et al., 2018） | TFDA 查無藥證；健保原文未見；成人與 AYA 為仿單外使用 |
| 5-FU／capecitabine 過量，或早發、嚴重、危及生命的毒性 | **Uridine triacetate**（Vistogard） | 成人 10 g 口服，每 6 小時一次共 20 次，不論進食；5-FU 或 capecitabine 結束後 96 小時內開始，愈快愈好（BTG International, 2026） | 緊急使用；不建議用於非緊急的不良反應，因為可能減弱 5-FU 與 capecitabine 的療效 | TFDA 查無藥證；專案進口未核對；健保原文未見 |
| Ifosfamide 腦病變 | 停止輸注並補充水分；**methylene blue**；**thiamine** | 文獻常見 methylene blue 50 mg 靜脈（每日最多 6 次）、thiamine 100 mg 靜脈（治療每 4 小時一次，預防每 6 小時一次）（Torchia et al., 2025） | 證據僅限個案報告與一項病歷回顧，沒有對照試驗；預防性使用沒有可靠證據：回溯研究中，methylene blue／thiamine／albumin 預防組的腦病變反而較多（每週期 21.1% 對 8.4%）（Richards et al., 2011），thiamine 預防與否差異不顯著（10.3% 對 18.2%，p = 0.51）（Lentz et al., 2020），高劑量 ifosfamide 後預防性 methylene blue 無法避免再發（5 位全數再發）（Sweiss et al., 2008）。Methylene blue 有加框警語：與血清素類藥物及 opioid 併用可能造成嚴重甚至致死的血清素症候群（Hikma, 2026），已有用於 ifosfamide 腦病變時疑似血清素症候群的個案報告（McDonnell et al., 2012） | Methylene blue 在台灣只核准用於變性血紅素血症，用於 ifosfamide 腦病變為仿單外；thiamine 注射劑有藥證；健保原文未見 methylene blue |
| 腫瘤溶解症候群的高尿酸 | **Rasburicase** | 美國仿單 0.2 mg/kg 靜脈 30 分鐘，每日一次，最多 5 天；給藥前篩檢 G6PD，抽尿酸檢體要預冷並冰浴、4 小時內測定（Sanofi-Aventis, 2026） | 加框：G6PD 缺乏者禁用（溶血）、變性血紅素血症、過敏反應 | 健保 5.5.6（93/5/1）：限血液腫瘤（急性白血病、high grade 淋巴瘤）且尿酸 > 10 mg/dL（兒童 > 8）、心腎衰竭無法大量輸液，或對 allopurinol 過敏；每日 1–2 劑、以 3 日為限。TFDA 藥證本手冊未核對 |
| 長春花生物鹼外滲 | 熱敷加局部皮下 **hyaluronidase** | 見第 9.2 節 | 仿單載明（Hospira, 2026） | 健保原文未見 |
| Pemetrexed 毒性預防 | **Folic acid、維生素 B12、dexamethasone** | 見 11.2 的 pemetrexed 列 | 屬於「預先保護」，不是事後解毒 | 見各藥仿單 |

> [!NOTE]
> **以 115/10/22 版為準**
> 上表健保欄的條號、修訂日期與條件整理自使用者提供的 115/10/22 版《全民健康保險藥品給付規定》原文；「原文未見」是指該版全文搜尋藥名沒有專條。TFDA 藥證狀態來自 2026-10-27 的 TFDA 公開資料下載。藥證、健保給付與院內是否備藥是三件不同的事，開立或調用前請與藥劑部確認。

> [!IMPORTANT]
> **解毒劑配對與時間點**
> - Ifosfamide → mesna（同時、4 小時、8 小時）；HD-MTX → leucovorin（24 小時起）→ 清除延遲才用 glucarpidase。
> - Doxorubicin 累積 ≥ 300 mg/m² 後續用 → dexrazoxane（心臟保護）；anthracycline 外滲 → 冷敷加 dexrazoxane（6 小時內）。
> - 5-FU／capecitabine 早發嚴重毒性 → uridine triacetate（96 小時內）。
> - Rasburicase 前先查 G6PD；cisplatin 兒童耳毒性 → sodium thiosulfate（限非轉移性）。
> - Methylene blue 治療 ifosfamide 腦病變的證據等級低，且不應預防性使用。

> [!TIP]
> **mesna 像撐傘**
> Ifosfamide 的代謝物 acrolein 像會腐蝕膀胱的酸雨。Mesna 會在尿液中和 acrolein，像撐了一把傘，所以一定要在下雨前（與 ifosfamide 同時）和雨中（4、8 小時後）都撐著；等到血尿才補給藥，傘撐得太晚。Leucovorin 則像「繞過路障的備用路線」：MTX 把葉酸通路堵住，leucovorin 直接提供下游已還原的葉酸，讓正常細胞繼續運作。

### 11.5 高劑量 methotrexate（HD-MTX）安全摘要

高劑量定義為 ≥ 500 mg/m²（Howard et al., 2016）。骨肉瘤方案常用 12 g/m²（單次上限 20 g）靜脈輸注 4 小時（Accord, 2026）。急性腎損傷（AKI）是最重要的風險，高劑量 MTX 約 2–12%，骨肉瘤 12 g/m² 的療程約 1.8%（Howard et al., 2016; Ramsey et al., 2018）。MTX 與代謝物在酸性尿液（pH < 5.5）會結晶，尿液 pH 從 6.0 提高到 7.0，溶解度提高 5–8 倍；AKI 常是非少尿型，只看尿量會漏掉。

| 階段 | 重點 |
|------|------|
| 給藥前 | 使用不含防腐劑的 MTX（含 benzyl alcohol 的製劑不能用於高劑量）（Accord, 2026）；基線肌酸酐與電解質；**引流明顯的肋膜積水或腹水**（third space 會讓 MTX 排出變慢）；停掉或避開交互作用藥物：PPI、NSAID（高劑量併用有嚴重甚至致死的胃腸毒性）、penicillin 與 sulfonamide 類抗生素（含 TMP-SMX）、probenecid、其他抗葉酸藥（Accord, 2026）；尿液 pH ≥ 7；若病人正在給 leucovorin，就延後到隔天再給 MTX（Howard et al., 2016） |
| 給藥中 | 開始前就水化並鹼化尿液，維持尿 pH ≥ 7 並維持尿量（Ramsey 共識為每天 ≥ 2,500 mL/m²；Ramsey et al., 2018）；每次排尿都測 pH；嚴格記錄輸入輸出；MTX 濃度抽血要避開輸注管腔，以免假性偏高 |
| 解救與追蹤 | 24 小時起給 leucovorin（時間點與劑量見 11.4）；每天至少測 MTX 與肌酸酐；正常清除約為 24 小時 10 µM、48 小時 1 µM、72 小時 < 0.2 µM；24 小時 ≥ 50 µM、48 小時 ≥ 5 µM 或 24 小時肌酐上升 ≥ 100% 屬延遲早期清除，leucovorin 改為 150 mg 靜脈每 3 小時直到 MTX < 1 µM，之後 15 mg 靜脈每 3 小時直到 < 0.05 µM（Sagent, 2026） |
| 延遲清除 | 保持水化與鹼化；考慮 glucarpidase（Ramsey 共識的骨肉瘤閾值：24 小時 > 50 µM、36 小時 > 30 µM、42 小時 > 10 µM、48 小時 > 5 µM，且肌酸酐較基線上升）；glucarpidase 後 MTX 要用 HPLC 測定（Ramsey et al., 2018） |
| 其他毒性 | 暫時性轉胺酶上升（最多約 60% 的療程）、高膽紅素（約 25%）、暫時性中樞神經症狀（最多約 15%）、嘔吐（10–30%）；嚴重皮膚反應（Howard et al., 2016; Accord, 2026） |

> [!WARNING]
> **HD-MTX 的三個常見錯誤**
> 1. 沒停 PPI、NSAID 或 TMP-SMX，MTX 排出變慢。
> 2. 只看尿量判斷腎功能：AKI 常是非少尿型，要追肌酸酐與 MTX 濃度。
> 3. Glucarpidase 與 leucovorin 同時打：glucarpidase 會分解 leucovorin，兩者要錯開至少 2 小時。

### 11.6 Ifosfamide 安全摘要

| 項目 | 重點 |
|------|------|
| 加框警語 | 骨髓抑制（可致命感染）、神經毒性（腦病變，可致死，出現腦病變要停藥）、泌尿與腎毒性（腎衰竭、出血性膀胱炎）（Fresenius Kabi, 2026b） |
| 預防出血性膀胱炎 | 每天至少 2 L 口服或靜脈液體；mesna 與 ifosfamide 同天、比例維持；仿單合併資料：血尿發生率沒有 mesna 約 44.1%、有 mesna 約 21.3%；肉眼血尿 11.1% 對 5.2%（Fresenius Kabi, 2026b） |
| 腦病變 | 仿單合併資料（4–12 g/m² 分次單藥）中樞神經毒性 15.4%（154／1,001）；通常在數小時至數天內發生，多在停藥後 48–72 小時內緩解，但可能在順利完成數個週期後才第一次發生（Fresenius Kabi, 2026b）。台灣一個醫學中心的 337 位成人，腦病變 11%，危險因子為 ECOG 2–4、肌酸酐較高、白蛋白較低（Lo et al., 2016）。用 CNS 作用藥（止吐藥、鎮靜劑、opioid、抗組織胺）要特別小心；CYP3A4 誘導劑（carbamazepine、phenytoin、rifampin、St John's wort）可能增加神經毒性代謝物 |
| 腎毒性 | 腎絲球與腎小管功能不良，包括 Fanconi 症候群；追蹤磷與鉀；腎小管損傷可在治療結束後數月至數年才出現（Fresenius Kabi, 2026b） |
| 心臟、肺 | 高劑量時心律不整與心肌病變（劑量相關）；肺炎、肺纖維化（Fresenius Kabi, 2026b） |

Ifosfamide 基本醫囑範例（概念，劑量依處方）：

```
Ifosfamide ___ mg/m²/day IV，D1–D__
Mesna：與 ifosfamide 同時 IV bolus，劑量為當日 ifosfamide 劑量的 20%；
       4 小時後、8 小時後各再給 20%（一天共 60%）
水化：每天口服或靜脈至少 2 L（依處方調整）
每天：腦病變徵象（意識、定向、行為）、尿液顏色、肌酸酐
給藥前：CBC、肌酸酐、電解質（磷、鉀）、肝功能；排除泌尿道阻塞；每次給藥前驗尿（顯微鏡下血尿 > 10 RBC/HPF 先暫停，完全緩解才給）
```

> [!NOTE]
> **各院做法不同**
> 連續輸注或高劑量 ifosfamide（例如 14 天輸注泵浦）沒有仿單規定的 mesna 時程；ifosfamide 與 mesna 可混在同一袋的條件、mesna 是否改用口服，都依各院肉瘤方案與藥劑部規範。完整病房流程見[肉瘤章](../04-sarcoma.md#52-ewing-sarcomavdcie以及高劑量-ifosfamide)第 5.2 節（高劑量 ifosfamide 版本與 mesna 待核對框）、[第 6.1 節](../04-sarcoma.md#61-高劑量-methotrexatehd-mtx完整病房流程)（HD-MTX 病房流程）與[第 6.2 節](../04-sarcoma.md#62-ifosfamide腦病變出血性膀胱炎與腎小管損傷)（mesna 時程與腦病變處置）。

---

## 12. 藥物基因檢測與特殊族群評估

結論先行：開 **fluoropyrimidine（5-FU、capecitabine）前想 DPYD**，開 **irinotecan 類前想 UGT1A1**，**≥ 65 歲先做老年評估**，**有生育可能的病人在性腺毒性治療前先談生育力與避孕**。這四件事都應該在第一個週期之前做完並記錄，不是等毒性出現才補做。

| 對象 | 檢測或評估 | 結論 | 小節 |
|------|----------|------|------|
| 5-FU、capecitabine | DPYD 基因變異 | 美國仿單加框警語：開始前檢測，完全 DPD 缺乏者避免使用；部分缺乏者個別化減量；陰性不保證安全 | 12.1 |
| Irinotecan、sacituzumab govitecan | UGT1A1\*28、\*6 | 同型合子或 \*6/\*28 複合異型合子，irinotecan 起始劑量考慮至少降一級；亞洲人 \*6 很常見 | 12.2 |
| Rasburicase、allopurinol、carbamazepine 等 | G6PD、HLA-B 基因 | 各自有固定的檢測時機；NUDT15／TPMT 與本手冊癌別無關 | 12.3 |
| ≥ 65 歲、接受全身性治療 | 老年評估（GA）、G8、CARG | 做 GA 並依結果調整治療；G8 ≤ 14 分需完整評估 | 12.4 |
| 有生育可能者 | 生育力與避孕諮詢 | 治療前談、轉介生殖專科、記錄 | 12.5 |

### 12.1 DPYD 與 fluoropyrimidine

**機轉**：DPYD 基因編碼 dihydropyrimidine dehydrogenase（DPD），這個酵素負責分解超過 80% 的 fluorouracil（H2-Pharma, 2026）。DPD 活性低的人，5-FU 或 capecitabine 分解不掉，血中濃度過高，第一個週期（或加量後）就出現嚴重黏膜炎、腹瀉、嗜中性球低下與神經毒性（EU SmPC 描述 DPD 缺乏相關毒性多發生在第一個週期或加量後；European Medicines Agency, n.d.）。

> [!TIP]
> **DPD 是 5-FU 的「清道夫」**
> 5-FU 像一批要在體內及時清走的化學物質，DPD 是清道夫。清道夫少了一半（部分缺乏），藥物堆積比預期多；清道夫全部罷工（完全缺乏），同樣的劑量就像把整車垃圾倒在街上，第一個週期就出事。

**現行 FDA 規定**（Xeloda 與 5-FU 仿單 2025 年 10 月修訂，FDA 說明頁內容更新至 2026-02-05）：

- 加框警語標題為「完全 DPD 缺乏病人的嚴重不良反應或死亡」：**開始治療前檢測 DPYD 基因變異，除非必須立刻治療**；已知帶有會造成完全 DPD 缺乏的特定同型合子或複合異型合子變異者，避免使用（H2-Pharma, 2026）。
- 沒有任何劑量被證實對完全 DPD 缺乏者是安全的；**部分缺乏者**要個別化劑量，依耐受度與治療目的調整；證據不足以建議特定劑量。
- 仿單沒有指定要檢測哪些變異，也說目前沒有 FDA 核准的 DPYD 檢驗，各檢測的設計與準確度不同；**即使沒有找到變異，仍可能發生嚴重不良反應**（H2-Pharma, 2026）。
- 發生早發或異常嚴重的反應時，依臨床判斷暫停或永久停藥。
- 盛行率（白人）：部分 DPD 缺乏約 3–5%，完全缺乏約 0.2%（H2-Pharma, 2026）。

**CPIC 劑量建議**（Amstutz et al., 2018，依 DPYD 活性分數 activity score, AS）：

| AS | 代謝型 | 5-FU 與 capecitabine 建議 |
|----|-------|--------------------------|
| 2 | 正常 | 依仿單劑量 |
| 1.5 | 中間型 | 起始劑量減少 25–50%（50% 較保守；證據限於 capecitabine） |
| 1 | 中間型 | 起始劑量減少 50% |
| 0.5 | 不良型 | 避免使用；若沒有其他選擇，才考慮大幅減量並盡早做血中濃度監測 |
| 0 | 不良型 | 避免使用 |

前兩個週期若無毒性或可耐受，可滴定加量；若無法耐受起始劑量就減量。荷蘭前瞻性研究：治療前檢測 DPYD，對 \*2A（c.1905+1G>A）與 c.1679T>G 帶因者起始劑量減量 50% 後，這些帶因者的嚴重毒性比例已和非帶因者相近（Henricks et al., 2018）。

**歐盟仿單**：建議治療前做表現型或基因型檢測；列出 c.1905+1G>A、c.1679T>G、c.2846A>T、c.1236G>A／HapB3 四個變異，並說這四個變異在非洲與亞洲族群「幾乎不存在」；血中 uracil ≥ 16 ng/mL 且 < 150 ng/mL 視為部分缺乏，≥ 150 ng/mL 視為完全缺乏（European Medicines Agency, n.d.）。

> [!WARNING]
> **東亞病人：陰性的「標準 DPYD 檢驗」不等於安全**
> 常見的西方檢驗套組只涵蓋上述四個變異，這些變異在東亞人很少見。日本 301 位病人的研究發現，嚴重毒性與罕見的族群特異性功能喪失變異有關（等位基因頻率 < 0.01%）（Yokoi et al., 2020）。台灣只找到一項 2004 年的小型研究（Hsiao et al., 2004；300 位受試者、只檢測 11 個變異，沒有檢測 c.1679T>G、c.2846A>T、c.1236G>A，\*2A 未檢出，且檢出的變異與 DPD 蛋白量無關），缺乏涵蓋完整 DPYD 的族群頻率研究，東亞資料是外推的。因此：（1）檢測結果要看「檢測了哪些變異」；（2）DPD 缺乏相關毒性多出現在第一個週期或加量後，所以第一個週期內要主動聯絡病人，追蹤口腔潰瘍、腹瀉、發燒與意識變化；（3）出現早發嚴重毒性要停藥並評估解毒劑（第 11.4 節 uridine triacetate，96 小時內）。

> [!CAUTION]
> **待核對：台灣的 DPYD 檢測供給與健保給付**
> 本手冊無法確認：（1）台灣哪些檢驗室提供 DPYD 檢測、涵蓋哪些變異、報告時效；（2）檢測是否有健保給付或需自費。115/10/22 版藥品給付規定全文搜尋 DPYD 沒有任何結果，9.17 capecitabine 條文也未提及 DPYD（原文未見／無健保給付）；基因檢測屬《醫療服務給付項目及支付標準》範疇，不在本手冊取得的藥品給付規定內。請向檢驗部、病理部或腫瘤科確認。

### 12.2 UGT1A1 與 irinotecan、sacituzumab govitecan

**機轉**：irinotecan 的活性代謝物 SN-38 經 UGT1A1 葡萄糖醛酸化而失活。UGT1A1 的 \*28（TA 重複）與 \*6 等低功能對偶基因使 SN-38 清除變慢，嗜中性球低下與腹瀉風險升高（Pharmacia & Upjohn, 2026a）。

- **Camptosar 仿單**：UGT1A1\*28／\*28、\*6／\*6 或 \*6／\*28 的病人嚴重嗜中性球低下的風險較高，**起始劑量考慮至少降一個劑量等級**（單藥或合併療法皆同），之後依耐受度調整；異型合子（\*1／\*28、\*1／\*6）為中間代謝型，風險也可能上升（Pharmacia & Upjohn, 2026a）。
- **頻率差異**（仿單）：同型合子 \*28 在黑人約 20%、白人約 10%、東亞約 2%；同型合子 \*6 在東亞約 2–6%，在白人和黑人少見（Pharmacia & Upjohn, 2026a）。
- **亞洲資料（由台灣團隊的 PEP02 試驗引用，非台灣本土族群頻率調查）**：台灣 PEP02（nanoliposomal irinotecan）第一期試驗在討論段引用的亞洲族群頻率為 UGT1A1\*28 13.9%（白人 33.4%）、\*6 13.0%（白人 0.5%）；該試驗唯一一例治療相關死亡是 \*6／\*28 複合異型合子（Chang et al., 2015）。台灣轉移性大腸直腸癌 128 位病人中約 20% 帶有 \*28，帶因者 irinotecan 合併 5-FU／leucovorin 的 Grade 3–4 嗜中性球低下 53.8% 對 4.9%、腹瀉 26.9% 對 5.9%（Liu et al., 2008）。亞洲病人的統合分析顯示 \*6 加 \*28 合併檢測可預測嗜中性球低下與腹瀉（Atasilp et al., 2022）。
- **台灣的劑量研究**：PURE FIST 試驗用 UGT1A1 基因型指引 irinotecan 加量：\*1／\*1 與 \*1／\*28 起始 180 mg/m² 並可加量，\*28／\*28 起始 120 mg/m²（Tsai et al., 2020）。這是研究設計，不是仿單劑量。
- **Onivyde（nal-IRI）**：UGT1A1 的劑量規則因方案而異（二線與第一線 NALIRIFOX 不同），且仿單依據的對偶基因與東亞常見的 \*6 不完全一致，見[胰臟癌章](../02-pancreatic-cancer.md#52-脂質體-irinotecannalirifox-與二線-nal-iri--5-fuleucovorin)第 5.2 節、[第 6.2 節](../02-pancreatic-cancer.md#62-irinotecan-與脂質體-irinotecan)。
- **Sacituzumab govitecan**（Trodelvy）：\*28／\*28 同型合子的嚴重嗜中性球低下（Grade 3–4）57%、\*1／\*28 為 48%、\*1／\*1 為 41%；仿單未訂基因型起始劑量，需密切監測（Gilead, 2026）。

> [!CAUTION]
> **待核對：東亞常見的 UGT1A1 變異與 sacituzumab govitecan 毒性、台灣檢測供給**
> 目前查到的 sacituzumab govitecan 資料以 \*28 為主，\*6（東亞常見）對其毒性的影響本手冊未查到原文。台灣的 UGT1A1 檢測供給與給付也未核對：115/10/22 版藥品給付規定全文搜尋 UGT1A1 沒有結果（原文未見／無健保給付）；基因檢測屬《醫療服務給付項目及支付標準》範疇，請向檢驗部確認。

### 12.3 其他基因：NUDT15／TPMT、G6PD、HLA

| 基因 | 相關藥物 | 重點 | 本手冊對應 |
|------|---------|------|-----------|
| NUDT15、TPMT | thiopurine（6-MP、azathioprine） | 決定 thiopurine 骨髓毒性的基因（Relling et al., 2019）；本手冊四個癌別不使用 thiopurine，不展開。Cisplatin 仿單提到 TPMT 變異可能與耳毒性有關，但證據不一致（WG Critical Care, 2026），不需常規檢測 | 僅供辨識 |
| G6PD | rasburicase | 加框：G6PD 缺乏者不可使用（溶血），並建議對高風險族群先篩檢（Sanofi-Aventis, 2026） | [腫瘤急症](02-oncologic-emergencies.md#2-腫瘤溶解症候群tls)第 2 節（TLS）；第 11.4 節 |
| HLA-B\*5801 | allopurinol | 漢人帶有者使用 allopurinol 發生嚴重皮膚過敏的風險顯著升高（Hung et al., 2005） | [腫瘤急症](02-oncologic-emergencies.md#2-腫瘤溶解症候群tls)第 2 節（TLS） |
| HLA-B\*1502 | carbamazepine | 健保 1.3.2.6（100/8/1）：新病患處方 carbamazepine 前先檢查 IC 健保卡是否註記曾檢測帶有 HLA-B 1502，結果陽性者不得開立；未確認或未檢測者宜先檢測。已服藥 4 個月以上、且確認未曾出現喉嚨痛、口腔潰瘍或皮疹等類似 Stevens-Johnson 症候群症狀的舊病患，可依病情繼續處方，但仍要提醒病人注意這些症狀 | 癌痛輔助藥或癲癇用藥時 |

> [!NOTE]
> **以 115/10/22 版為準**
> HLA-B\*1502 與 carbamazepine 的規定整理自 115/10/22 版《藥品給付規定》1.3.2.6；NUDT15、TPMT、G6PD、HLA-B\*5801 的檢測在該版全文中沒有對應條文（原文未見）。Carbamazepine 是[肺癌章](../01-lung-cancer.md)口服標靶藥警示框列舉的 CYP3A4 誘導劑之一，併用標靶藥時要查交互作用（第 14.5 節）。

### 12.4 老年評估（≥ 65 歲）

**ASCO 2023 指引（Dale et al., 2023）**：

- **所有 ≥ 65 歲、接受全身性治療的癌症病人，都應做老年評估（geriatric assessment, GA）**，找出一般腫瘤評估抓不到的脆弱點。評估到有缺陷者，照護計畫要納入「依 GA 結果處置」（GA-guided management）：用 GA 結果輔助治療決策，並針對缺陷做介入、衛教或轉介。
- GA 至少涵蓋：**身體與認知功能、情緒、共病、多重用藥、營養、社會支持**。可依人力與時間調整；指引提出「實用老年評估（Practical Geriatric Assessment, PGA）」作為選項之一。
- 簡短篩檢：**G8**（8 題：食物攝取、體重下降、活動力、神經心理問題、BMI、用藥數、自覺健康、年齡），**分數 0–14 為異常切點**，需做完整 GA（Bellera et al., 2012; Dale et al., 2023）；Vulnerable Elders Survey-13（VES-13）是另一個選項。
- 化療毒性風險：**CARG 毒性量表**（0–5 低、6–9 中、≥ 10 高風險）（Hurria et al., 2011）；中、高風險者考慮完整 GA、**單藥而非雙藥**、調整劑量或時程（例如減量 20% 再依耐受度加量）；CRASH 是替代量表。
- 年齡切點：指引建議對象為 65 歲以上，但多數納入隨機試驗的收案年齡是 70 歲以上。

> [!IMPORTANT]
> **考試重點：年齡本身不是治療強度的依據**
> 老年病人的決策靠 GA，而不是只看實歲。治癒性治療仍要以不減損療效為優先（第 7.3 節），緩和性治療才優先考慮減量或單藥；每一次減量或換藥都要記錄理由。

**專師實務**：初診 ≥ 65 歲病人，在第一次全身性治療前完成 G8；異常者做完整 GA（或轉介老年醫學／個案管理師）；把 CARG 分數記在治療前評估單；有跌倒、營養不良、多重用藥時，在第一個週期前就安排介入；與家屬討論目標與預期。

### 12.5 生育力保存與避孕諮詢

**ASCO 2025 指引（Su et al., 2025）重點**：

- 對所有有生育可能的癌症病人，**在診斷時就評估並說明生殖風險**，並於存活期持續追蹤；**在癌症治療開始前**討論保存生育力的做法。有興趣或不確定的病人要轉介生殖專科。
- **男性**：治療前應提供精子冷凍保存；無法取得精液檢體時可考慮睪丸取精。治療開始後不久收集的精子可能有較高的遺傳損傷風險，需提醒。
- **女性**：既有的做法包括胚胎、卵子與卵巢組織冷凍、卵巢移位、保留生育的婦科手術；體外成熟卵子是新興做法。
- **GnRH 促效劑（GnRHa）不可取代**上述確立的方法，但乳癌女性可作為輔助選擇。
- 腫瘤團隊要確保病人能迅速轉介到多專科的生育力保存團隊，並協助爭取給付。

**避孕與懷孕檢測**：治療前對有生育可能的女性做懷孕檢測（第 5 節）；治療中與治療後需避孕的期間依各藥仿單不同（例如 sacituzumab govitecan：女性最後一劑後 6 個月、男性 3 個月；Gilead, 2026），開立前逐藥查仿單。

> [!WARNING]
> **常漏掉的情境**
> 最常漏掉的是「談了卻沒記錄」或「根本沒談」：ASCO 要求諮詢內容要記錄在病歷（Oktay et al., 2018）。急需治療而來不及保存生育力的病人，指引仍保留治療後的保存選項（post-treatment fertility preservation），要在存活期追蹤時再談；需要緊急治療的女性病人，GnRHa 可用於抑制月經（Su et al., 2025）。

> [!CAUTION]
> **待核對：台灣的生育力保存給付與轉介路徑**
> 115/10/22 版《藥品給付規定》全文搜尋「生育」沒有結果，第 9 節未見以保存生育力為適應症的藥品條文（原文未見／無健保給付）；取卵、冷凍保存等醫療服務的給付與補助政策不在本手冊取得的資料內，請向院內個案管理師或生殖醫學科確認。

---

## 13. 中心靜脈導管照護（Port-A、PICC、隧道式導管）

結論先行：**給發泡劑前先確認有回血；懷疑導管感染時導管與周邊靜脈各抽一組血液培養（嗜中性球低下發燒的慣例是每個管腔都抽）；導管不順先查機械性原因（夾子、針頭、姿勢、pinch-off）再用 alteplase；金黃色葡萄球菌、綠膿桿菌、黴菌、分枝桿菌引起的導管感染要拔管。** 台灣化療病人大多裝植入式輸液港（Port-A），Port 問題是病房最常接到的護理電話：沒有回血、輸注不順、發燒、手臂腫。

### 13.1 裝置類型

| 裝置 | 位置與構造 | 特點（CDC 2011） | 護理重點 |
|------|----------|-----------------|---------|
| 植入式輸液港（Port-A，totally implantable device） | 全部埋在皮下，皮下有 port，用針穿刺使用；植入鎖骨下或頸內靜脈 | 導管相關血流感染風險最低；不需要局部導管出口護理；病人自我形象較好；移除需要手術 | 每次使用都要用針穿刺；未使用期間仍需定期沖洗（間隔依產品與院內規範） |
| 周邊置入中心靜脈導管（PICC） | 由 basilic、cephalic 或 brachial 靜脈置入，尖端到上腔靜脈 | 感染率低於非隧道式 CVC | 有外露導管與敷料，要固定好並定期更換敷料 |
| 隧道式導管（tunneled CVC） | 經皮下隧道由鎖骨下、頸內或股靜脈置入，帶有 cuff | Cuff 阻擋微生物沿導管表面移行，感染率低於非隧道式 CVC | 出口處敷料與導管固定；長期使用 |
| 非隧道式 CVC | 經皮直接置入中心靜脈 | 導管相關血流感染（CRBSI）的大宗來源 | 短期使用（加護病房、急症） |

ASCO 2013 指引認為證據不足以推薦哪一種導管或哪個置入位置最好，並建議避免股靜脈置入、由訓練良好的人員置入並使用 CVC 照護組合（bundle）（Schiffer et al., 2013；O'Grady et al., 2011）。

### 13.2 使用 Port 前：穿刺與確認回血

1. 洗手；以含 > 0.5% chlorhexidine 的酒精溶液消毒皮膚（O'Grady et al., 2011，Category IA）；戴無菌手套。
2. 使用 port 專用的 non-coring（Huber）針（依產品說明與 INS 標準），穿刺到針尖碰到 port 底部；固定針頭並以無菌敷料覆蓋。
3. 每次接上管路或注射前，**用適當的消毒劑擦拭 access port（scrub the hub）**，之後只用無菌裝置接入（O'Grady et al., 2011，Category IA）。
4. **抽到回血**，再用生理食鹽水沖洗；沖洗時觀察 port 上方皮膚有沒有疼痛、腫脹、滲液，病人有沒有灼熱感。
5. **給發泡劑（vesicant）前，一定要確認有回血且沖洗順暢；沒有回血就不要直接給**，先排除阻塞與針頭位置問題。

> [!WARNING]
> **沒有回血，不要用發泡劑「試試看」**
> 沒有回血可能是針頭沒到底、導管尖端貼壁、纖維蛋白鞘、血栓、pinch-off，也可能是導管已經移位。此時推入發泡劑，外滲會發生在胸壁或縱隔腔，處置困難。先停下來、評估原因，必要時請醫師會診並以影像確認（外滲處置見第 9 節）。

> [!NOTE]
> **針頭更換間隔與敷料**
> CDC 2011 指引對「連續使用中的 port 針頭可以留多久」沒有建議（證據不足）；植入或隧道式導管部位的透明敷料，在傷口癒合前不超過每週更換一次，除非髒汙或鬆脫（O'Grady et al., 2011）。各院依 INS 標準與產品說明訂定針頭更換天數、注射器大小與沖洗容量，請依院內護理標準。

### 13.3 沖洗與封管（flush and lock）

- **目的**：沖洗（flush）把管腔內的藥物與血液推走；封管（lock）在不用的時候把溶液留在管腔內保持通暢。
- **生理食鹽水**：ASCO 2013 指引建議常規用生理食鹽水沖洗（Schiffer et al., 2013）。
- **肝素 vs 生理食鹽水**：Cochrane 2022 對成人 CVC 的統合分析（12 個隨機試驗、2,422 位病人）顯示，肝素封管可能減少阻塞（RR 0.70，95% CI 0.51–0.95），但證據確信度低；導管相關血流感染、死亡、出血與肝素引起的血小板低下沒有明確差異（確信度非常低）（López-Briz et al., 2022）。所以「用不用肝素、用多少濃度」是各院依 INS 標準與政策決定。
- **抗生素封管**：CDC 2011 只建議用於長期導管、且在嚴格無菌技術下仍反覆發生導管血流感染的病人（Category II）；IDSA 指引的抗生素封管需配合全身性抗生素，滯留時間一般不超過 48 小時（O'Grady et al., 2011；Mermel et al., 2009）。
- **不要常規用抗凝血藥預防導管血栓**：ASCO 2013 不建議常規使用 warfarin 或低分子量肝素預防導管血栓（Schiffer et al., 2013）。

> [!CAUTION]
> **待核對：INS 標準的具體條文**
> 《Infusion Therapy Standards of Practice, 9th Edition》（Nickel et al., 2024）規範了 CVAD 的沖洗容量與技術、封管溶液與濃度、port 針頭更換間隔與回血確認等細節。該標準全文為付費文件，本手冊未取得原文逐條核對，上述具體數字（沖洗毫升數、肝素 U/mL、針頭更換天數、未使用 port 的沖洗頻率）請以院內護理標準與產品說明書為準。

### 13.4 阻塞處理流程

| 步驟 | 做法 |
|------|------|
| 1. 先看機械性原因 | 管路夾子是否打開、管路是否折到、敷料或固定是否壓迫；Port：針頭是否到底、有沒有歪斜；請病人換姿勢（抬手臂、深呼吸、咳嗽、轉頭） |
| 2. 抽吸、沖洗 | 用生理食鹽水輕輕沖洗（不要用蠻力推）；若抬手臂才有回血，懷疑 pinch-off（13.7） |
| 3. 影像 | 胸部 X 光確認導管尖端與走向；其他影像檢查由醫師決定 |
| 4. 懷疑血栓性阻塞 | **Alteplase（Cathflo Activase）**：體重 ≥ 30 kg，2 mg／2 mL 灌入阻塞的導管；留置 30 分鐘後嘗試抽血，若仍不通就再留置到 120 分鐘；仍不通可再灌第二劑相同劑量（仿單沒有超過兩劑、總量 4 mg 的研究資料）（Genentech, 2026b）。ASCO 2013 也建議用 t-PA 恢復阻塞導管的通暢（Schiffer et al., 2013） |
| 5. 仍不通 | 通知醫師，評估換管或導管重置；不要重複用力推注 |

> [!NOTE]
> **台灣的 alteplase（Cathflo）取得**
> 115/10/22 版《藥品給付規定》全文搜尋 Cathflo 與導管灌注用 alteplase 沒有專條（第 2.1.2.1 條的 rt-PA 為血管血栓與心肌梗塞用途，不是導管灌注）（原文未見／無健保給付）；台灣是否有 Cathflo 藥證、院內是否備藥，本手冊未核對。實務上院內有沒有、怎麼領用請問藥劑部。

### 13.5 導管相關血流感染（CRBSI）

**什麼時候要想**：中心靜脈導管病人出現發燒、寒顫（尤其在沖洗或輸注之後）、port 皮下口袋紅腫熱痛或出口處有膿。一項華人癌症病人研究（1,391 位病人、1,449 個 port；發表於 *Journal of the Formosan Medical Association*），port 相關感染的發生率為每 1,000 導管日 0.21，血液惡性腫瘤與頭頸癌風險較高，最常培養出綠膿桿菌與念珠菌（Wang et al., 2015）。

**抽血培養（先於抗生素）**（Mermel et al., 2009）：

- 懷疑導管血流感染時，**同時從導管與周邊靜脈各抽一組培養**（A-II）；沒有周邊靜脈可抽時，從不同管腔至少抽 2 組（B-III）。多腔導管是否每個管腔都要抽，IDSA 指引認為不確定（C-III），但嗜中性球低下發燒的處置慣例是每個管腔都抽（見[腫瘤急症](02-oncologic-emergencies.md#1-發燒性嗜中性球低下)第 1 節）。
- **診斷標準**：導管端抽的血液比周邊血早至少 2 小時長出細菌（differential time to positivity, DTP），或導管端菌落數至少是周邊的 3 倍（A-II）。

**何時要拔掉長期導管**（Mermel et al., 2009）：

- 長期導管（隧道式導管或 port）併有下列任一情況要拔管（A-II）：**嚴重敗血症、化膿性血栓性靜脈炎、心內膜炎、經 72 小時敏感抗生素後仍持續菌血症，或感染 *Staphylococcus aureus*、*Pseudomonas aeruginosa*、黴菌、分枝桿菌**。
- *Candida* 的導管血流感染也建議拔管（A-II）；port 皮下口袋膿瘍或隧道感染要拔管並視情況切開引流（A-II）。
- 其他病原（例如 coagulase-negative staphylococci）的單純性感染，可以嘗試保留導管，同時使用全身性抗生素加抗生素封管（B-II）。
- 療程（概略）：coagulase-negative staphylococci，拔管者 5–7 天，保留導管者 10–14 天加封管；*S. aureus* 拔管後 4–6 週，符合所有條件者可縮短到至少 14 天（需經食道心臟超音波評估）。

> [!IMPORTANT]
> **考試重點：導管感染要拔管的病原**
> 記「金（S. aureus）、綠（Pseudomonas）、黴（Candida／fungi）、分（mycobacteria）」四類：這些病原引起的長期導管感染要拔管。持續菌血症超過 72 小時也要拔管。

**預防**：嚴格無菌技術與置入組合、> 0.5% chlorhexidine 酒精消毒、擦拭 access port；連續使用的輸液套管組至少每 7 天更換，且不要比每 96 小時更頻繁（O'Grady et al., 2011）。

### 13.6 導管相關血栓

- **表現**：同側手臂、頸部或臉部腫脹疼痛、淺靜脈怒張、肩頸疼痛，或 port 突然失去功能。
- **處置原則**：ASCO 2013 指引不建議常規使用 warfarin 或低分子量肝素預防導管血栓；導管不再需要，或影像確認的血栓在抗凝血治療下仍惡化時，建議拔管（Schiffer et al., 2013）。血栓的抗凝血治療用藥見[支持性照護](03-supportive-care.md#7-癌症相關靜脈血栓vte)第 7 節（VTE）。

> [!CAUTION]
> **待核對：導管血栓的抗凝血療程與導管留置條件**
> 本手冊取得的 ASCO 2013 摘要未寫抗凝血的最短療程，也沒有「功能良好、位置正確、無感染者可保留導管」的條文原文；ASCO VTE 指引 2023 年更新的摘要（Key et al., 2023）也沒有導管血栓的細節。這部分請對照 ASCO VTE 指引全文與院內流程，或與血液科、血管外科討論。

### 13.7 Pinch-off 症候群

- **是什麼**：植入式導管經鎖骨下靜脈置入時，導管被夾在鎖骨與第一肋骨之間而受壓，稱為 pinch-off 症候群（Hinke et al., 1990）。
- **什麼時候發生**：該研究 11 位病人中，8 位發生在置入後 3 週內（Hinke et al., 1990）。
- **怎麼分級（胸部 X 光）**：0 正常；1 導管走向突然改變但管腔沒有變窄；2 管腔變窄；3 導管完全斷裂。Grade 2 代表明顯受壓並有嚴重併發症的可能，長期壓迫的 5 例 Grade 2 中，2 例發生導管斷裂或碎裂；Grade 1 在對照組很常見（33%），臨床意義不確定（Hinke et al., 1990）。
- **床邊線索**：抬手臂、肩膀往後或換姿勢時才有回血或才推得動，一換姿勢又不通；推注時有阻力或疼痛。
- **處置**：停用、做胸部 X 光，Grade 2 以上通知醫師評估換管或移除，避免導管斷裂後碎片栓塞。

> [!TIP]
> **Pinch-off 像水管夾在門縫**
> 導管像一條軟水管，從鎖骨和第一肋骨這兩片「門板」中間穿過。手臂放鬆時門縫夠寬，水流順暢；肩膀往前或手臂放下，門縫變窄，水就不流。時間久了，水管被反覆夾壓，最後會從夾住的位置斷掉。

### 13.8 居家照護、MRI 與 port 外滲

- **衛教要說的**：出現發燒、寒顫、port 部位紅腫熱痛、滲液、手臂或頸部腫脹、胸痛或呼吸喘，要立即回診。CDC 對短期 CVC 的透明敷料建議至少每 7 天更換一次，淋浴時用不透水的覆蓋物保護導管與連接裝置（O'Grady et al., 2011，Category IB），PICC 的實際間隔依院內規範；植入或隧道式導管部位的敷料更換頻率見 13.2 的 NOTE。
- **MRI 與造影劑高壓注射**：植入裝置是否可做 MRI、是否可高壓注射，要以該廠牌與型號的說明書、病人持有的植入物識別卡與放射科規範為準，不要憑經驗判斷。
- **Port 外滲**：輸注中病人說 port 部位灼熱、疼痛，或 port 上方皮膚腫脹、輸注變慢、回血消失，視為外滲，立即**停止輸注、不拔針、回抽、通知醫師**，之後依藥物處置（第 9.2 節）；懷疑針頭脫出 port 隔膜時，以影像確認位置與有無導管斷裂或移位。

---

## 14. 給藥安全標準與口服抗癌藥

結論先行：化療的給藥錯誤多半發生在醫囑、調配與核對這幾個環節，不是在病人身上才出錯。ASCO／ONS 的安全標準把這些環節拆成可檢查的項目：**醫囑要有兩個病人識別碼與完整的劑量變數；給藥前由兩位合格人員獨立核對；第一個週期前要有書面衛教與同意；vincristine 等 vinca 類只能靜脈**。口服抗癌藥的風險一樣大，只是犯錯的地點從病房換成了家裡，所以處方、標示、衛教與追蹤都要有流程。

### 14.1 本節重點

- **兩個病人識別碼**：醫囑要有病人全名加第二個識別碼；給藥前由至少兩位人員在病人面前，用至少兩個識別碼核對身分（Neuss et al., 2013）。
- **獨立核對（independent double check）**：調配前由第二個人獨立核對每一張醫囑；給藥前由至少兩位合格人員核對藥名、劑量、體積、速率、效期、外觀與幫浦速率；2016 年標準另新增調配過程的兩人核對（Neuss et al., 2013; Neuss et al., 2016）。
- **口頭醫囑**：除了「暫停或停止」化療之外，不接受口頭醫囑（Neuss et al., 2013）。
- **Vincristine 只能靜脈**：仿單加框寫明「僅供靜脈使用，其他途徑給藥會致死」；ASCO／ONS 2016 要求在有給 intrathecal 藥物的機構，vinca 類以 minibag 給藥（Hospira, 2026; Neuss et al., 2016）。
- **口服抗癌藥也是危害藥品**：處方、標示、衛教、順從度與毒性追蹤都要有流程。

### 14.2 ASCO／ONS 化療給藥安全標準

| 項目 | 標準重點 | 專師做什麼 |
|------|---------|-----------|
| 醫囑內容（靜脈） | 病人全名加第二個識別碼、日期、診斷、方案名稱與週期數、過敏史、身高、體重與其他劑量變數、劑量計算方式、劑量、途徑、速率、輸注時間、支持性用藥、藥物順序（Neuss et al., 2013） | 用標準化醫囑模板，每一欄都填；體重與身高有改變要重算並寫出依據（見第 2 節） |
| 醫囑內容（口服） | 病人識別碼、藥名、日期、劑量計算參考、劑量、發藥數量、途徑與頻率、療程長度、可續領次數（含「無」）（Neuss et al., 2013） | 寫明「連續 X 天、停 X 天」與總療程，避免病人誤解 |
| 調配前核對 | 第二位人員獨立核對每張醫囑：兩個識別碼、藥名、劑量、體積、途徑、速率、劑量計算與變數、週期與天數（Neuss et al., 2013） | 醫囑送出前自己先把算式寫在病歷，方便藥師核對 |
| 給藥前核對 | 至少兩位合格人員核對藥名、劑量、體積、速率、效期（若適用）、外觀與完整性、幫浦速率；至少兩人在病人面前以至少兩個識別碼確認身分；給藥人員在每個週期前與病人確認計畫的治療（Neuss et al., 2013） | 病人若說「這次的藥跟上次不一樣」，先停下來核對 |
| 同意與衛教 | 開始前取得並記錄知情同意；病人要拿到書面資料，含診斷、治療目的、預期療程、藥物與時程、短期與長期不良反應（含不孕風險）、什麼症狀要聯絡誰、監測與追蹤計畫；第一次給藥前要記錄病人理解的程度（Neuss et al., 2013） | 衛教後用「請您說說看，發燒幾度要打電話？」確認理解並記錄 |
| 口頭醫囑 | 除了暫停或停止化療外，不接受口頭醫囑；新醫囑與變更（含口服）都要書面記錄，傳真與電子郵件視同書面（Neuss et al., 2013） | 化療醫囑有疑問時要打電話，但開立仍須書面 |
| 鞘內藥物 | 鞘內注射藥物不可與其他藥物一起調配，要隔離存放並有專屬標示，且只與其他中樞神經投藥的藥物一起配送（Neuss et al., 2013） | 鞘內藥物與靜脈化療分開準備與存放，細節依院內化療安全規範 |
| 外滲與急救準備 | 外滲處置程序要符合最新文獻，解毒劑與醫囑組合要隨時取得；給藥期間要有可立即到場的有執照醫師及具基本救命術證照的人員；要有危急狀況（含超出基本救命術）的處置程序（Neuss et al., 2013） | 確認外滲處置包與急救車的位置（第 9 節） |
| 2016 年新增 | 調配過程兩人核對；在給 intrathecal 藥物的機構 vinca 類以 minibag 給藥；病人帶回家的藥要標示（Neuss et al., 2016） | 見 14.3、14.4 |

> [!NOTE]
> **標準的版本**
> 上表的細項整理自 2013 年版標準（Neuss et al., 2013）全文，以及 2016 年更新版摘要列出的新增項目（Neuss et al., 2016）。2016 年版把標準重新排序與編號，並納入兒童腫瘤；細節以最新版與院內化療安全規範為準。

### 14.3 Vinca 類為什麼一定用 minibag

Vincristine 仿單加框警語：**僅供靜脈使用，其他途徑給藥會致死**（FOR INTRAVENOUS USE ONLY – FATAL IF GIVEN BY OTHER ROUTES）（Hospira, 2026）。鞘內給 vincristine 是教科書上的致命錯誤，ASCO／ONS 2016 的對策是：在有給 intrathecal 藥物的機構，vinca 類一律以 minibag（小型靜脈輸液袋）稀釋後給藥，而不是用針筒推注（Neuss et al., 2016）。

> [!TIP]
> **針筒會「插錯孔」，輸液袋不會**
> 鞘內注射用的是針筒；vincristine 如果也裝在針筒裡，在同一個病人、同一個時段，針筒就有機會被拿去接錯管路。把 vincristine 做成輸液袋，袋子接得上靜脈輸液管，卻接不上鞘內針，錯誤就從「要靠人記得」變成「根本做不到」。

> [!WARNING]
> **Vinca 的三個必記**
> 1. 只能靜脈，且只由熟練人員給藥；
> 2. 屬發泡劑，外滲處置是熱敷加局部皮下 hyaluronidase（第 9 節）；
> 3. 鞘內藥物不可與其他藥物一起調配，要隔離存放並有專屬標示（Neuss et al., 2013）。

### 14.4 化療醫囑範例（概念，劑量依處方）

```
病人：姓名、病歷號（兩個識別碼）；身高 ___ cm、體重 ___ kg（日期 ___）、BSA ___ m²（公式 ___）
診斷：___；方案：___；週期 ___ / 天 ___；過敏史：___
劑量計算：藥名 ___ 每 m²（或 AUC、mg/kg）___ × ___ = ___ mg，是否依院內規則四捨五入
途徑／速率／輸注時間：___；稀釋液與體積：___
Premedication：___（時間點）；支持性用藥（止吐、G-CSF 等）：___
藥物順序：___；給藥前檢驗與門檻：ANC ___、PLT ___、肌酸酐 ___、肝功能 ___
核對簽名：開立者 ___；調配前核對者 ___；給藥前核對者 1 ___、2 ___
```

### 14.5 口服抗癌藥

**口服抗癌藥的流程（Neuss et al., 2013）**：

- **開始前**：評估病人取得與服用藥物的能力（能不能領到藥、會不會吞、有沒有人幫忙），有問題要先有對策；治療計畫中要寫明追蹤頻率。
- **處方與標示**：處方內容見 14.2；標示要有用法、可續領次數與開立者。
- **衛教**：儲存、處理、準備、服用與丟棄；併用的藥與支持性用藥；藥物與食物的交互作用；**漏服怎麼辦**；視病人能力把家屬或照顧者納入。
- **首次順從度檢查**：確認處方有領到藥，並請病人說出怎麼吃、漏服怎麼辦。
- **之後每次看診**：評估順從度與毒性，並有處理問題的計畫。
- **停藥**：有停藥流程，包括教病人怎麼處理剩下的藥。

**漏服與嘔吐：每個藥不一樣，不要只教一條通則**。通則是「不要補吃、不要加倍」，但各藥仿單有不同的細節，例子如下，實際以該藥仿單與肺癌、乳癌等各癌別章的藥物表為準（肺癌口服標靶藥的漏服、嘔吐與管灌見[肺癌章](../01-lung-cancer.md)第 5.5 節，劑量與空腹／隨餐規定見第 5.4 節）：

| 藥物 | 漏服 | 吃完藥後嘔吐 | 來源 |
|------|------|-------------|------|
| Capecitabine | 不補吃，下一劑照原時間 | 不補吃，下一劑照原時間 | H2-Pharma, 2026 |
| Osimertinib | 不補吃，下一劑照原時間 | 未查到特別規定 | AstraZeneca, 2026 |
| Gefitinib | 距離下一劑不到 12 小時就不要補吃 | 未查到特別規定 | AstraZeneca, 2023 |
| Pazopanib | 距離下一劑不到 12 小時就不要補吃 | 未查到特別規定 | Sun Pharmaceutical Industries, 2026 |
| Alectinib | 不補吃，下一劑照原時間 | 不補吃，下一劑照原時間 | Genentech, 2026a |
| Ribociclib | 當天不補吃 | 當天不補吃 | Novartis, 2026b |
| Regorafenib | 當天想起來就補吃，但前一天漏的不能在當天補成兩劑 | 未查到特別規定 | Bayer, 2026 |
| Imatinib | 下一劑照原時間 | 未查到特別規定 | Novartis, 2026a |

> [!NOTE]
> **台灣仿單與美國仿單可能不同**
> 表中資料來自美國仿單。台灣核准仿單的漏服規定、空腹或隨餐規定可能不同（例如 afatinib 的空腹規定已在肺癌章 5.4 說明），衛教前先確認院內使用的仿單版本。

**不能吞藥或有鼻胃管時：先查仿單，不要自行壓碎或打開**

| 藥物 | 可否分散或管灌 | 做法或禁忌 | 來源 |
|------|-------------|-----------|------|
| Osimertinib | 可 | 將錠劑放入 60 mL 不含氣泡的水中攪拌到散成小塊後立即吞下；鼻胃管給藥則用 15 mL 水分散，再用額外 15 mL 水沖洗殘渣，之後依鼻胃管說明沖管；**不可壓碎、加熱或超音波處理**；仿單的病人說明寫在 30 分鐘內給完 | AstraZeneca, 2026 |
| Gefitinib | 可 | 錠劑放入 4–8 盎司的水中攪拌約 15 分鐘後立即喝下或由鼻胃管給藥，再用水沖洗容器並同樣給下 | AstraZeneca, 2023 |
| Imatinib | 可 | 可分散在水或蘋果汁中 | Novartis, 2026a |
| Capecitabine | 不可 | 不可咀嚼、切開或壓碎；以水吞服，餐後 30 分鐘內 | H2-Pharma, 2026 |
| Olaparib 錠劑 | 不可 | 整顆吞服，不可咀嚼、壓碎、溶解或分割 | AstraZeneca, 2025 |
| Pazopanib | 不可 | 整顆吞服；壓碎會加快吸收，可能影響全身暴露量 | Sun Pharmaceutical Industries, 2026 |
| Ribociclib | 不可 | 整顆吞服，不可咀嚼、壓碎或分割 | Novartis, 2026b |

沒有仿單依據的藥物，請藥劑部會診，不要自行壓碎、打開膠囊或溶解。管灌後要確認整劑量都進入管路，不要把藥混在整瓶管灌營養品裡。

**儲存、處理與丟棄**：Xeloda 仿單寫明 capecitabine 為危害藥品（hazardous drug），要依特殊處理與丟棄程序（H2-Pharma, 2026）。居家的做法：藥放在原包裝、避免兒童與寵物接觸；處理藥物時的防護、家屬（尤其孕婦或哺乳者）的接觸，以及剩藥回收，依院內規範與藥劑部衛教單；ASCO／ONS 要求這些內容在衛教時一併說明（Neuss et al., 2013）。病人體液的處理防護見第 10 節。

**藥物與食物交互作用**

- **抑酸劑（PPI、H2 阻斷劑）**：吸收依賴胃酸的口服標靶藥（如 gefitinib、erlotinib 等）暴露量會降低，要避免或錯開時間（Budha et al., 2012；各藥時間見肺癌章 5.4）。Gefitinib 仿單建議可能的話避免與 PPI 併用（AstraZeneca, 2023）。
- **CYP3A4**：osimertinib 要避免強效 CYP3A4 誘導劑，無法避免時加到 160 mg 每日，停誘導劑後 3 週再回到 80 mg（AstraZeneca, 2026）；gefitinib 併用強效誘導劑（如 rifampicin）時，在沒有嚴重藥物不良反應的前提下加到 500 mg 每日，停用誘導劑 7 天後回到 250 mg（AstraZeneca, 2023）；**lorlatinib 禁止與強效 CYP3A 誘導劑併用**，因為可能造成嚴重肝毒性（Pfizer, 2026c）。Carbamazepine、phenytoin、rifampin、St John's wort 都是常被漏掉的誘導劑。
- **Capecitabine**：與 warfarin 併用出血風險（加框，要更常監測 INR）；避免併用 allopurinol；含 folic acid 或葉酸類似物的產品除非醫師指示否則不要吃（H2-Pharma, 2026）。PPI 與 capecitabine 的關聯來自觀察性研究：回溯研究與 2025 年統合分析（676 位大腸癌病人）顯示併用 PPI 與較差的無復發存活有關（Sun et al., 2016; de Moraes et al., 2025），但美國仿單未把 PPI 列為交互作用，這是觀察性證據，無法據此要求所有病人停 PPI；可行時避免不必要的 PPI。
- **食物**：capecitabine 餐後 30 分鐘內服用；regorafenib 在低脂餐（< 600 kcal、脂肪 < 30%）後服用（H2-Pharma, 2026; Bayer, 2026）；其他標靶藥的空腹或隨餐規定見肺癌章 5.4 的表格。

> [!IMPORTANT]
> **考試重點：口服抗癌藥衛教六件事**
> 1. 怎麼吃（時間、與食物關係、整顆吞還是可分散）。
> 2. 漏服與吃完吐了怎麼辦（各藥不同，通則是不補、不加倍）。
> 3. 什麼症狀要打電話（發燒、腹瀉次數、口腔潰瘍、手腳脫皮、呼吸困難等）。
> 4. 藥與食物、保健食品、其他處方的交互作用（PPI、CYP3A4、warfarin、葡萄柚、St John's wort）。
> 5. 儲存、處理與丟棄（危害藥品）。
> 6. 追蹤時程與下次回診日。

> [!CAUTION]
> **待核對：口服抗癌藥的細節**
> 本節的漏服、嘔吐與管灌資料來自所列藥物的美國仿單，台灣核准仿單、藥廠衛教單與院內藥劑部規範可能不同；沒有列出的藥物（例如 S-1／TS-1、abemaciclib、palbociclib 的台灣規定）請逐藥查證。Capecitabine 與 PPI 的交互作用在不同研究結果不一致，建議的處置請與主治醫師與藥劑部討論。

---

## 15. 自我測驗

**Q1.** 一位 70 歲女性，體重 50 kg，血清肌酸酐 0.4 mg/dL，醫囑 carboplatin AUC 5。依 Calvert 公式並遵循 GFR 上限，劑量應為多少？

A. 約 640 mg　B. 約 730 mg　C. 約 750 mg　D. 約 960 mg

<details>
<summary>答案與詳解</summary>

**答案：A**。

- CrCl = (140 − 70) × 50 ÷ (72 × 0.4) = 3,500 ÷ 28.8 = 121.5；女性 × 0.85 = **103.3 mL/min**（未超過 125，不需封頂）。
- 劑量 = 5 × (103.3 + 25) = **約 641 mg**。

常見錯誤：忘了乘 0.85 → CrCl 121.5 → 約 732 mg（B）；以為肌酸酐低就一律封頂 → 750 mg（C）；把 Calvert 結果再乘 BSA（以 1.5 m² 計）→ 約 960 mg（D）。

臨床提醒：這是純計算題。實務上 70 歲、50 kg、肌酸酐 0.4 的病人，腎功能多半被高估，許多醫院規定肌酸酐低於某個值（常見 0.7–0.8 mg/dL）時以該值代入，算出的劑量會更低（見 3.1 的院內規範框）。

</details>

**Q2.** 依 ASCO 2021 指引，BMI 38 kg/m² 的乳癌病人接受輔助性化療，劑量計算應採用何者？

A. 理想體重　B. 調整體重　C. 實際體重，算出足量　D. BSA 封頂 2.0 m²

<details>
<summary>答案與詳解</summary>

**答案：C**。ASCO 2021 建議肥胖病人以實際體重計算足量的細胞毒性化療，不常規封頂或減量；出現毒性時，調整方式與非肥胖病人相同（Griggs et al., 2021）。

</details>

**Q3.** 一位 HBsAg 陽性的肺腺癌病人即將開始 pemetrexed + carboplatin + pembrolizumab。下列處置何者正確？

A. 抗癌治療期間監測 ALT 即可　B. 開始預防性抗病毒，並在治療結束後至少持續 12 個月　C. 僅在 HBV DNA 上升時才給藥　D. 只有使用 rituximab 時才需預防

<details>
<summary>答案與詳解</summary>

**答案：B**。依 ASCO 2020，慢性 HBV（HBsAg 陽性）接受任何全身性抗癌治療都應預防性抗病毒，持續整個療程並在結束後至少 12 個月（Hwang et al., 2020）。選項 D 描述的是「過去感染（HBsAg 陰性、anti-HBc 陽性）」才需要區分治療風險。

</details>

**Q4.** 病人接受 epirubicin 輸注時，護理師發現注射部位腫脹疼痛。第一步應該做什麼？

A. 立即拔針並加壓止血　B. 停止輸注，保留針頭並回抽　C. 立即熱敷　D. 以生理食鹽水沖管後繼續輸注

<details>
<summary>答案與詳解</summary>

**答案：B**。外滲的第一步是停止輸注、保留針頭、從原管路回抽殘留藥液，之後才拔針。Epirubicin 屬 anthracycline，應冷敷（不是熱敷），並評估在 6 小時內給予 dexrazoxane。台灣查無 dexrazoxane 藥證，院內是否備有要先確認（第 9 節）。

</details>

**Q5.** 下列何者是 CTCAE v5.0 中 Grade 3 與 Grade 2 的主要區分？

A. 是否需要藥物治療　B. 是否影響自我照顧 ADL　C. 是否危及生命　D. 是否有症狀

<details>
<summary>答案與詳解</summary>

**答案：B**。Grade 2 影響工具性 ADL（煮飯、購物、理財），Grade 3 影響自我照顧 ADL（洗澡、穿衣、進食），或需住院。危及生命是 Grade 4。

</details>

**Q6.** Vincristine 外滲時，下列處置何者正確？

A. 冷敷 + dexrazoxane　B. 熱敷 + hyaluronidase　C. 冷敷 + DMSO　D. 不需處理，因為是非發泡劑

<details>
<summary>答案與詳解</summary>

**答案：B**。Vinca alkaloids 屬於不與 DNA 結合的發泡劑，處置為熱敷加局部 hyaluronidase；冷敷反而可能加重傷害。

</details>

**Q7.** 一位 ECOG 3 的晚期肺腺癌病人，次世代定序（NGS）發現 EGFR exon 19 deletion。下列敘述何者最適當？

A. ECOG 3 不應接受任何抗癌治療　B. 可考慮 EGFR-TKI，體能狀態可能隨腫瘤反應改善　C. 應先給予含鉑化療　D. 應先轉安寧，不需討論標靶治療

<details>
<summary>答案與詳解</summary>

**答案：B**。ECOG 3–4 一般不建議細胞毒性化療，但有 driver mutation 的病人，標靶藥副作用相對低、反應率高，體能狀態可能因腫瘤縮小而改善，應與主治醫師討論。安寧照護可同時介入，不是二選一。

</details>

**Q8.** 一位 68 歲男性晚期肺腺癌，住院準備下一個週期化療，血流動力學穩定，沒有胸痛、心衰竭或已知心血管疾病，Hb 7.6 g/dL。依 AABB 2023 指引，下列何者最適當？

A. Hb < 8 g/dL 就應立即輸血 2 單位　B. 化療前 Hb 必須 ≥ 10 g/dL 才能給藥　C. 尚未低於 7 g/dL 的輸血門檻，先找貧血原因並追蹤症狀與 Hb　D. 腫瘤病人的輸血門檻應提高到 9 g/dL

<details>
<summary>答案與詳解</summary>

**答案：C**。AABB 2023 對血流動力學穩定的住院成人建議限制性輸血策略，Hb < 7 g/dL 才考慮輸血；血液與腫瘤疾患的住院病人同樣建議 7 g/dL（有條件建議、證據確信度低）；心臟手術可用 7.5 g/dL，骨科手術或既有心血管疾病用 8 g/dL（Carson et al., 2023）。本題 Hb 7.6 g/dL 高於 7，沒有症狀，不輸血，但要找原因（出血、缺鐵、腎性等）並持續評估整體臨床狀況。化療本身沒有固定的 Hb 給藥門檻。

</details>

**Q9.** 一位 66 歲大腸癌病人預計使用 capecitabine，Cockcroft-Gault 算出 CrCl 為 25 mL/min。下列何者最正確？

A. 歐盟仿單將 CrCl < 30 mL/min 列為禁忌；美國現行仿單改為「劑量未建立」，無替代方案時才個別減量並密切監測，實際以台灣核准仿單為準　B. 所有仿單都寫 CrCl < 30 時起始劑量減為 75%　C. 美國現行仿單把 CrCl < 30 mL/min 列為絕對禁忌　D. CrCl 低於 50 mL/min 都不需要調整劑量

<details>
<summary>答案與詳解</summary>

**答案：A**。CrCl 30–50 mL/min 起始劑量減 25%（即 75%）；CrCl < 30 mL/min，歐盟 SmPC 列為禁忌，美國 Xeloda 現行仿單（2026-02-05 版）只把對 fluorouracil 或 capecitabine 的嚴重過敏列為禁忌，並寫「劑量未建立」，無替代方案時才以減量起始並密切監測（H2-Pharma, 2026; European Medicines Agency, n.d.）。選項 B 把 30–50 的規則誤套到 < 30；選項 C 是舊版或歐盟的說法。

</details>

**Q10.** 一位 HBsAg 陽性的大腸癌病人要開始 FOLFOX 化療，準備開立 B 肝抗病毒藥。依 115/10/22 版藥品給付規定 10.7.3 第 2 項 (4)，下列何者正確？

A. 需事前審查核准，且僅限使用 rituximab 時　B. 化療一結束就必須停藥　C. 必須 HBV DNA 達特定數值才給付　D. 需照會消化系專科醫師同意，可從化療前 1 週給付到化療結束後 6 個月

<details>
<summary>答案與詳解</summary>

**答案：D**。10.7.3 第 2 項 (4)（98/11/1）：接受癌症化學療法，經照會消化系專科醫師同意後，可於化療前 1 週開始給付，直到化療結束後 6 個月，以預防 B 肝發作；本款未要求事前審查，未限定化療藥物種類，也未要求 HBV DNA 數值。選項 A 是 (9) Ⅰ（免疫抑制劑）的對象之一，且該款也不需事前審查。ASCO 2020 建議結束後至少 12 個月，與健保的 6 個月不同（Hwang et al., 2020），延長時要與消化系專科醫師討論。

</details>

**Q11.** 病人接受 ifosfamide 1.2 g/m²/day，連續數天。下列 mesna 的標準靜脈給法，何者符合美國仿單？

A. 只在 ifosfamide 結束後 24 小時給一次　B. 每個 ifosfamide 給藥日，在 ifosfamide 給藥時與 4、8 小時後，各給當日 ifosfamide 劑量的 20%（一天共 60%）　C. 只有出現血尿才給 mesna　D. 每天固定 500 mg，與 ifosfamide 劑量無關

<details>
<summary>答案與詳解</summary>

**答案：B**。仿單的標準方案是每次 ifosfamide 給藥的當下與 4、8 小時後，各給 ifosfamide 劑量 20%（w/w），一天共 60%，ifosfamide 給藥的每一天都重複，ifosfamide 劑量調整時維持比例；同時每天至少 2 L 水化（Eugia, 2026b; Fresenius Kabi, 2026b）。Mesna 是預防，血尿發生才補給已經太晚。連續輸注或高劑量 ifosfamide 沒有仿單時程，依處方。

</details>

**Q12.** 骨肉瘤病人接受 HD-MTX 12 g/m² 4 小時輸注。24 小時抽血 MTX 為 80 µM，肌酸酐較基線上升 100%。下列處置何者正確？

A. 維持 leucovorin 15 mg 每 6 小時，並停止鹼化尿液　B. 立即給 dexrazoxane　C. 同時推注 glucarpidase 與 leucovorin，不需間隔　D. 屬延遲清除與急性腎損傷：持續水化與鹼化，leucovorin 改為 150 mg 靜脈每 3 小時，並依規範考慮 glucarpidase（與 leucovorin 錯開至少 2 小時）

<details>
<summary>答案與詳解</summary>

**答案：D**。24 小時 MTX ≥ 50 µM 或 24 小時肌酸酐上升 ≥ 100% 都屬延遲早期清除，leucovorin 改為 150 mg 靜脈每 3 小時直到 MTX < 1 µM，再改 15 mg 每 3 小時直到 < 0.05 µM（Sagent, 2026）；Ramsey 共識在骨肉瘤方案中，24 小時 MTX > 50 µM 且肌酸酐上升時，glucarpidase 可能適用，最好在 48–60 小時內給（Ramsey et al., 2018）。Glucarpidase 會分解 leucovorin，兩者要間隔至少 2 小時（BTG International, 2024）。尿液要持續鹼化（pH ≥ 7）。Dexrazoxane 是 anthracycline 的保護劑，與 MTX 無關。

</details>

**Q13.** 下列抗癌藥與累積劑量相關毒性的配對，何者正確？

A. Cisplatin—心肌病變，累積 550 mg/m²　B. Doxorubicin—肺纖維化，累積 400 units　C. Bleomycin—肺纖維化，總量超過 400 units 風險明顯上升　D. Ifosfamide—手足皮膚反應

<details>
<summary>答案與詳解</summary>

**答案：C**。Bleomycin 的肺毒性與劑量相關，總量超過 400 units 時明顯上升（Meitheal, 2026）。Doxorubicin 的累積劑量警示是心肌病變（300／400／450／500 mg/m² 時機率約 1–2%、3–5%、5–8%、6–20%）（Pfizer, 2026a）。Cisplatin 的劑量限制毒性是腎毒性。Ifosfamide 的重點是出血性膀胱炎、腦病變與腎毒性；手足皮膚反應是 capecitabine、regorafenib 等。

</details>

**Q14.** 一位開始 capecitabine 的病人，用藥第 5 天出現嚴重口腔黏膜炎、血便腹瀉、嗜中性球低下與意識改變，capecitabine 已於昨天停止。下列何者最適當？

A. 等毒性緩解後再評估解毒劑　B. 立即聯絡醫師，並在 capecitabine 結束後 96 小時內考慮 uridine triacetate（台灣無藥證，先確認取得方式），同時評估 DPD 缺乏　C. 加 leucovorin 解救　D. 給 glucarpidase

<details>
<summary>答案與詳解</summary>

**答案：B**。Uridine triacetate（Vistogard）用於 fluorouracil 或 capecitabine 過量，或結束後 96 小時內出現早發、嚴重或危及生命的毒性（如胃腸毒性或嗜中性球低下、心臟或中樞神經毒性），成人 10 g 口服每 6 小時一次共 20 次（BTG International, 2026）。早發的嚴重毒性要想到 DPD 缺乏。Leucovorin 會增強 5-FU 毒性，不是解毒劑；glucarpidase 是 methotrexate 的解毒劑。台灣查無 uridine triacetate 藥證。

</details>

**Q15.** 關於 ifosfamide 腦病變，下列敘述何者正確？

A. 應立即停止 ifosfamide；methylene blue 與 thiamine 的證據主要是個案報告與回顧研究，預防性使用沒有可靠證據，methylene blue 與 opioid 併用要留意血清素症候群　B. Methylene blue 預防已被大型隨機試驗證實可降低腦病變發生率　C. 只會在第一個週期發生，之後的週期不會發生　D. 台灣仿單已核准 methylene blue 用於 ifosfamide 腦病變

<details>
<summary>答案與詳解</summary>

**答案：A**。腦病變通常在數小時至數天內出現，多在停藥後 48–72 小時內緩解，但可能在順利完成數個週期後才第一次發生。治療的證據是個案報告與一項病歷回顧；預防性使用的回溯研究沒有顯示效果，一項研究預防組反而更多（Richards et al., 2011; Lentz et al., 2020; Sweiss et al., 2008）。Methylene blue 有血清素症候群的加框警語（Hikma, 2026）。台灣的 methylene blue 只核准用於變性血紅素血症，用於 ifosfamide 腦病變是仿單外使用。

</details>

**Q16.** 依美國 FDA 對 capecitabine 與 5-FU 的現行仿單（加框警語，2025 年 10 月修訂），關於 DPYD 的敘述何者最正確？

A. 所有病人都必須先檢測 DPYD，否則不得開立　B. 開始治療前應檢測 DPYD 基因變異（除非必須立刻治療）；完全 DPD 缺乏者避免使用，部分缺乏者個別化劑量；沒找到變異仍可能發生嚴重毒性　C. 只有東亞族群需要檢測　D. DPYD 檢測陰性代表可安心使用標準劑量

<details>
<summary>答案與詳解</summary>

**答案：B**。仿單寫「除非需要立刻治療，開始前檢測 DPYD」，並說明沒有 FDA 核准的檢驗、沒有任何劑量被證實對完全 DPD 缺乏者安全、部分缺乏者要個別化劑量，且即使沒找到變異仍可能發生嚴重毒性（H2-Pharma, 2026）。西方常用的四個變異在東亞人很少見，陰性不等於安全（Yokoi et al., 2020; European Medicines Agency, n.d.）。

</details>

**Q17.** 關於 UGT1A1 與 irinotecan，下列何者正確？

A. UGT1A1\*28 同型合子在東亞人比白人常見　B. UGT1A1 只影響 irinotecan 的療效，與毒性無關　C. 亞洲人 UGT1A1\*6 比白人常見得多（對偶基因頻率約 13% 對 0.5%），只檢測 \*28 會漏掉東亞常見的風險　D. 美國仿單只對 \*1/\*1 基因型建議減量

<details>
<summary>答案與詳解</summary>

**答案：C**。台灣團隊 PEP02 試驗引用的亞洲資料：UGT1A1\*28 的頻率在亞洲較低（13.9% 對白人 33.4%），\*6 則高很多（13.0% 對 0.5%）（Chang et al., 2015）。Camptosar 仿單對 \*28／\*28、\*6／\*6 或 \*6／\*28 的病人建議起始劑量至少降一個劑量等級，因為 SN-38 暴露量增加，嚴重嗜中性球低下風險上升（Pharmacia & Upjohn, 2026a）。

</details>

**Q18.** 一位 76 歲男性大腸癌病人預計接受 FOLFOX，ECOG 1，G8 篩檢 12 分。下列做法何者最適當？

A. 年齡 ≥ 70 歲一律減量 25%　B. ECOG 1 代表不需任何老年評估　C. G8 分數 12 分表示狀況良好，免評估　D. G8 ≤ 14 分屬異常，應做完整老年評估（GA）並依結果介入與調整治療，必要時再評估 CARG 毒性風險

<details>
<summary>答案與詳解</summary>

**答案：D**。ASCO 2023 建議對所有 ≥ 65 歲、接受全身性治療的癌症病人做老年評估，有缺陷者要納入依 GA 結果的處置（Dale et al., 2023）。G8 的異常切點為 0–14 分（分數越低越差）（Bellera et al., 2012）；CARG 毒性量表分數 6–9 為中度、10–23 為高風險，可考慮單藥、減量（例如減 20% 再依耐受度加量）（Hurria et al., 2011; Dale et al., 2023）。依年齡一律減量沒有依據。

</details>

**Q19.** 26 歲女性乳癌，下週要開始含 cyclophosphamide 的化療。關於生育力，下列何者最符合 ASCO 2025 指引？

A. 治療前就說明生殖風險並轉介生殖專科，討論胚胎、卵子或卵巢組織冷凍等方法；GnRH 促效劑不能取代這些方法，乳癌可作為輔助　B. 等化療結束後再談生育力　C. GnRH 促效劑可完全取代卵子冷凍　D. 年輕病人不需要特別評估

<details>
<summary>答案與詳解</summary>

**答案：A**。ASCO 2025 指引：在診斷時就評估並說明生殖風險，治療開始前討論保存生育力，有興趣或不確定者轉介生殖專科；女性的確立做法包括胚胎、卵子、卵巢組織冷凍、卵巢移位等；GnRHa 不應取代這些方法，但乳癌女性可作為輔助（Su et al., 2025）。諮詢內容要記錄在病歷（Oktay et al., 2018）。

</details>

**Q20.** Port 病人準備給 vinorelbine（發泡劑），針頭穿刺後抽不到回血，沖生理食鹽水感覺順暢。下列做法何者正確？

A. 先給一小段藥觀察有沒有疼痛　B. 先不給發泡劑，排除針頭位置、阻塞、導管位置或 pinch-off 等原因，必要時影像確認並通知醫師　C. 熱敷手臂後直接給藥　D. 把針頭再往內壓，直接開始輸注

<details>
<summary>答案與詳解</summary>

**答案：B**。給發泡劑前要確認有回血且沖洗順暢；沒有回血可能是針頭沒到底、導管尖端貼壁、纖維蛋白鞘、血栓、pinch-off 或導管移位，直接給藥若外滲會發生在胸壁或縱隔腔，處置困難。先停下來評估，必要時以影像確認（外滲處置見第 9 節）。

</details>

**Q21.** Port 病人化療後發燒，導管端與周邊血液培養各一組，導管端長出 *Staphylococcus aureus*。下列何者最適當？

A. 保留 port，只加抗生素封管　B. 抗生素 5–7 天即可　C. 周邊培養沒有長就不是導管感染　D. 拔除 port 並給全身性抗生素，通常 4–6 週，符合所有條件時才可縮短到至少 14 天

<details>
<summary>答案與詳解</summary>

**答案：D**。IDSA 2009：長期導管遇到 *S. aureus*、*P. aeruginosa*、黴菌或分枝桿菌引起的感染要拔管；*S. aureus* 拔管後建議 4–6 週，符合多項條件（無糖尿病或免疫抑制、無人工血管內裝置、無心內膜炎、72 小時內退燒與培養轉陰、無轉移性感染，並先做心臟超音波）才可縮短到至少 14 天；封管不可單獨使用（Mermel et al., 2009）。5–7 天是 coagulase-negative staphylococci 拔管後的療程。

</details>

**Q22.** 一位體重 60 kg 的 port 病人輸注不順且抽不到血，排除機械性原因後懷疑血栓性阻塞。依 Cathflo Activase 仿單，下列何者正確？

A. 20 mg 靜脈輸注 2 小時　B. 每次 4 mg，留置 24 小時　C. 2 mg／2 mL 灌入導管，留置 30 分鐘後嘗試抽血，仍不通則留置到 120 分鐘，仍不通可再灌一劑　D. 以肝素 10,000 units 推注

<details>
<summary>答案與詳解</summary>

**答案：C**。體重 ≥ 30 kg 者用 2 mg／2 mL，留置 30 分鐘後評估，不通再留置到 120 分鐘，仍未恢復功能可再灌第二劑相同劑量（Genentech, 2026b）。ASCO 2013 也建議用 t-PA 恢復阻塞導管的通暢，不建議常規用抗凝血藥預防導管血栓（Schiffer et al., 2013）。

</details>

**Q23.** 一位 port 病人只有抬高手臂時才抽得到血，胸部 X 光顯示導管在鎖骨與第一肋骨交界處管腔變窄。最可能的診斷與處置為何？

A. Pinch-off 症候群，管腔變窄屬 Grade 2，有導管斷裂風險，應停用並通知醫師評估換管或移除　B. Port 皮下口袋感染，直接口服抗生素　C. 單純纖維蛋白鞘，繼續使用　D. 空氣栓塞

<details>
<summary>答案與詳解</summary>

**答案：A**。Pinch-off 症候群是經鎖骨下靜脈置入的導管被夾在鎖骨與第一肋骨之間；分級 0 正常、1 走向突然改變、2 管腔變窄、3 完全斷裂。Grade 2 代表明顯受壓並有嚴重併發症的可能（長期壓迫的 Grade 2 中有導管斷裂或碎裂的案例）（Hinke et al., 1990）。

</details>

**Q24.** 下列關於 vincristine 的安全規定，何者正確？

A. 可以經鞘內給藥治療中樞神經白血病　B. 稀釋後可以經任何途徑給藥　C. 僅供靜脈使用，其他途徑給藥會致死；在有給 intrathecal 藥物的機構，ASCO／ONS 2016 建議以 minibag 給藥　D. 外滲時應冷敷並給 dexrazoxane

<details>
<summary>答案與詳解</summary>

**答案：C**。Vincristine 仿單加框：僅供靜脈使用，其他途徑給藥會致死（Hospira, 2026）；ASCO／ONS 2016 標準要求在有給 intrathecal 藥物的機構，vinca 類用 minibag 給藥（Neuss et al., 2016）。外滲處置是熱敷加 hyaluronidase，不是冷敷與 dexrazoxane（第 9 節）。

</details>

**Q25.** 依 ASCO／ONS 化療給藥安全標準，下列何者正確？

A. 化療醫囑只需要病人姓名一個識別碼　B. 給藥前由至少兩位合格人員核對藥名、劑量、體積、速率等，並在病人面前以至少兩個識別碼確認身分　C. 口頭醫囑可用來開立新的化療處方　D. 第一個週期給藥後再補簽同意書

<details>
<summary>答案與詳解</summary>

**答案：B**。標準要求醫囑含病人全名與第二個識別碼；調配前第二位人員獨立核對醫囑；給藥前至少兩位合格人員核對藥物資訊，並在病人面前以至少兩個識別碼確認身分；除了暫停或停止化療之外不接受口頭醫囑；開始前要有知情同意與書面衛教（Neuss et al., 2013）。

</details>

**Q26.** 病人服用 capecitabine 後 20 分鐘嘔吐，下列衛教何者正確？

A. 立刻再吃一次相同劑量　B. 下一餐加倍劑量補回來　C. 把藥壓碎後再吃以加快吸收　D. 不要補吃，下一劑照原定時間服用（美國仿單），並聯絡團隊處理嘔吐

<details>
<summary>答案與詳解</summary>

**答案：D**。Xeloda 美國仿單：吃完藥後嘔吐不補吃、漏服也不補吃，下一劑照原時程；錠劑不可咀嚼、切開或壓碎，以水吞服（餐後 30 分鐘內）（H2-Pharma, 2026）。各藥的漏服與嘔吐規定不同（例如 ribociclib 當天不補吃，regorafenib 當天想起來可補吃但不可補成兩劑），要逐藥查仿單。

</details>

**Q27.** 昏迷、留置鼻胃管的 EGFR 突變肺癌病人需使用 osimertinib。下列做法何者正確？

A. 依仿單將錠劑放入少量不含氣泡的水中分散（不壓碎、不加熱），再由鼻胃管給藥並沖管　B. 把錠劑磨粉後和整瓶管灌營養品混合　C. 把錠劑加熱至溶解後灌入　D. 因為無法吞藥，一律停藥

<details>
<summary>答案與詳解</summary>

**答案：A**。Osimertinib 仿單：不能吞錠劑者，將錠劑放入不含氣泡的水中（口服用 60 mL，鼻胃管用 15 mL）攪拌至散成小塊，不可壓碎、加熱或超音波處理；鼻胃管給藥時再用額外的水沖洗殘渣並依鼻胃管說明沖管（AstraZeneca, 2026）。能否分散依藥物而定（例如 capecitabine、olaparib、pazopanib 不可壓碎），沒有仿單依據的藥請藥劑部會診。

</details>

---

## 16. 參考文獻

Accord. (2026). *Methotrexate injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=dd035a9f-cd40-4314-b9d8-2294b8a924e2（版本日期 2026-09-04）

Amstutz, U., Henricks, L. M., Offer, S. M., Barbarino, J., Schellens, J. H. M., Swen, J. J., Klein, T. E., McLeod, H. L., Caudle, K. E., Diasio, R. B., & Schwab, M. (2018). Clinical Pharmacogenetics Implementation Consortium (CPIC) guideline for dihydropyrimidine dehydrogenase genotype and fluoropyrimidine dosing: 2017 update. *Clinical Pharmacology & Therapeutics, 103*(2), 210–216. https://doi.org/10.1002/cpt.911（PMID: 29152729）

Asselin, B. L., Devidas, M., Chen, L., Franco, V. I., Pullen, J., Borowitz, M. J., Hutchison, R. E., Ravindranath, Y., Armenian, S. H., Camitta, B. M., & Lipshultz, S. E. (2016). Cardioprotection and safety of dexrazoxane in patients treated for newly diagnosed T-cell acute lymphoblastic leukemia or advanced-stage lymphoblastic non-Hodgkin lymphoma: A report of the Children's Oncology Group randomized trial Pediatric Oncology Group 9404. *Journal of Clinical Oncology, 34*(8), 854–862. https://doi.org/10.1200/JCO.2015.60.8851（PMID: 26700126）

AstraZeneca. (2023). *Iressa (gefitinib) tablets* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=827d60e8-7e07-41b7-c28b-49ef1c4a5a41（版本日期 2023-02-28）

AstraZeneca. (2025). *Lynparza (olaparib) tablets* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=741ff3e3-dc1a-45a6-84e5-2481b27131aa（版本日期 2025-07-10）

AstraZeneca. (2026). *Tagrisso (osimertinib) tablets* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5e81b4a7-b971-45e1-9c31-29cea8c87ce7（版本日期 2026-09-14）

Atasilp, C., Biswas, M., Jinda, P., Nuntharadthanaphong, N., Rachanakul, J., Hongkaew, Y., Vanwong, N., Saokaew, S., & Sukasem, C. (2022). Association of UGT1A1\*6, UGT1A1\*28, or ABCC2 c.3972C>T genetic polymorphisms with irinotecan-induced toxicity in Asian cancer patients: Meta-analysis. *Clinical and Translational Science, 15*(7), 1613–1633. https://doi.org/10.1111/cts.13277（PMID: 35506159）

Bayer. (2026). *Stivarga (regorafenib) tablets* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=824f19c9-0546-4a8a-8d8f-c4055c04f7c7（版本日期 2026-02-09）

Bellera, C. A., Rainfray, M., Mathoulin-Pélissier, S., Mertens, C., Delva, F., Fonck, M., & Soubeyran, P. L. (2012). Screening older cancer patients: First evaluation of the G-8 geriatric screening tool. *Annals of Oncology, 23*(8), 2166–2172. https://doi.org/10.1093/annonc/mdr587（PMID: 22250183）

BluePoint. (2026). *Cyclophosphamide injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1d3396d8-4c03-4a28-890a-d87c6c53a74e（版本日期 2026-03-12）

Boehringer Ingelheim. (2025). *Gilotrif (afatinib) tablets* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fd638e5e-8032-e7ca-0179-95e96ab5d387（版本日期 2025-11-13）

Brock, P. R., Maibach, R., Childs, M., Rajput, K., Roebuck, D., Sullivan, M. J., Laithier, V., Ronghe, M., Dall'Igna, P., Hiyama, E., Brichard, B., Skeen, J., Mateos, M. E., Capra, M., Rangaswami, A. A., Ansari, M., Rechnitzer, C., Veal, G. J., Covezzoli, A., . . . Neuwelt, E. A. (2018). Sodium thiosulfate for protection from cisplatin-induced hearing loss. *The New England Journal of Medicine, 378*(25), 2376–2385. https://doi.org/10.1056/NEJMoa1801109（PMID: 29924955）

BTG International. (2024). *Voraxaze (glucarpidase) for injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=acaef5a6-b740-40e3-8ffe-74a75c74745c（版本日期 2024-11-27）

BTG International. (2026). *Vistogard (uridine triacetate) granules* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=269f7363-63ed-444e-85f1-f0009e44818b（版本日期 2026-03-31）

Budha, N. R., Frymoyer, A., Smelick, G. S., Jin, J. Y., Yago, M. R., Dresser, M. J., Holden, S. N., Benet, L. Z., & Ware, J. A. (2012). Drug absorption interactions between oral targeted anticancer agents and PPIs: Is pH-dependent solubility the Achilles heel of targeted therapy? *Clinical Pharmacology & Therapeutics, 92*(2), 203–213. https://doi.org/10.1038/clpt.2012.73（PMID: 22739140）

Calvert, A. H., Newell, D. R., Gumbrell, L. A., O'Reilly, S., Burnell, M., Boxall, F. E., Siddik, Z. H., Judson, I. R., Gore, M. E., & Wiltshaw, E. (1989). Carboplatin dosage: Prospective evaluation of a simple formula based on renal function. *Journal of Clinical Oncology, 7*(11), 1748–1756. https://doi.org/10.1200/JCO.1989.7.11.1748（PMID: 2681557）

Carson, J. L., Stanworth, S. J., Guyatt, G., Valentine, S., Dennis, J., Bakhtary, S., Cohn, C. S., Dubon, A., Grossman, B. J., Gupta, G. K., Hess, A. S., Jacobson, J. L., Kaplan, L. J., Lin, Y., Metcalf, R. A., Murphy, C. H., Pavenski, K., Prochaska, M. T., Raval, J. S., . . . Pagano, M. B. (2023). Red blood cell transfusion: 2023 AABB international guidelines. *JAMA, 330*(19), 1892–1902. https://doi.org/10.1001/jama.2023.12914（PMID: 37824153）

Chang, T. C., Shiah, H. S., Yang, C. H., Yeh, K. H., Cheng, A. L., Shen, B. N., Wang, Y. W., Yeh, C. G., Chiang, N. J., Chang, J. Y., & Chen, L. T. (2015). Phase I study of nanoliposomal irinotecan (PEP02) in advanced solid tumor patients. *Cancer Chemotherapy and Pharmacology, 75*(3), 579–586. https://doi.org/10.1007/s00280-014-2671-x（PMID: 25577133）

CNX Therapeutics. (2024). *Savene 20 mg/ml powder and solvent for concentrate for solution for infusion* [Summary of product characteristics]. electronic medicines compendium (emc). https://www.medicines.org.uk/emc/product/100135/smpc（修訂日期 2024-10-01）

Cockcroft, D. W., & Gault, M. H. (1976). Prediction of creatinine clearance from serum creatinine. *Nephron, 16*(1), 31–41. https://doi.org/10.1159/000180580（PMID: 1244564）

Daiichi Sankyo. (2026). *Enhertu (fam-trastuzumab deruxtecan-nxki) for injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7e67e73e-ddf4-4e4d-8b50-09d7514910b6（版本日期 2026-05-15）

Dale, W., Klepin, H. D., Williams, G. R., Alibhai, S. M. H., Bergerot, C., Brintzenhofeszoc, K., Hopkins, J. O., Jhawer, M. P., Katheria, V., Loh, K. P., Lowenstein, L. M., McKoy, J. M., Noronha, V., Phillips, T., Rosko, A. E., Ruegg, T., Schiaffino, M. K., Simmons, J. F., Jr., Subbiah, I., . . . Mohile, S. G. (2023). Practical assessment and management of vulnerabilities in older patients receiving systemic cancer therapy: ASCO guideline update. *Journal of Clinical Oncology, 41*(26), 4293–4312. https://doi.org/10.1200/JCO.23.00933（PMID: 37459573）

de Moraes, F. C. A., de Laia, E. A., Sano, V. K. T., Dos Santos, A. G. E., Pereira, C. R. M., & Burbano, R. M. R. (2025). A systematic review and meta-analysis of users versus non-users: Unveiling the influence of proton pump inhibitors on capecitabine efficacy in colorectal cancer. *Expert Review of Clinical Pharmacology, 18*(1–2), 67–75. https://doi.org/10.1080/17512433.2024.2443183（PMID: 39690972）

Eli Lilly. (2023). *Alimta (pemetrexed) for injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f5a860f3-37ec-429c-ae04-9c88d7c55c08（版本日期 2023-05-19）

Eli Lilly. (2026). *Cyramza (ramucirumab) injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c6080942-dee6-423e-b688-1272c2ae90d4（版本日期 2026-06-09）

Eugia. (2026a). *Dexrazoxane for injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=cb72203a-0b09-42d5-bf51-7f479feb3adb（版本日期 2026-08-10）

Eugia. (2026b). *Mesna injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=49e9c804-9e88-4774-8faf-35bd61b3a8e9（版本日期 2026-01-27）

European Medicines Agency. (n.d.). *Xeloda: EPAR – Product information* (Annex I, Summary of product characteristics). 擷取日 2026-11-01. https://www.ema.europa.eu/en/documents/product-information/xeloda-epar-product-information_en.pdf

Exelan. (2026). *Paclitaxel protein-bound particles for injectable suspension (albumin-bound)* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=135502ff-002c-4a29-ba93-60855cf44f31（版本日期 2026-08-10）

Fennec. (2025). *Pedmark (sodium thiosulfate) injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f98c7076-2a7b-4fd7-ab90-eed5e9137bae（版本日期 2025-10-27）

Fresenius Kabi. (2026a). *Etoposide injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fe870629-104d-4d67-a7c6-f53bc588121e（版本日期 2026-07-14）

Fresenius Kabi. (2026b). *Ifosfamide injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a311a947-7b78-4226-bfe0-f4aa0be20e27（版本日期 2026-04-09）

Fresenius Kabi. (2026c). *Topotecan injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b6019088-cd94-43b4-b5ce-ba20b6b8021e（版本日期 2026-01-14）

Freyer, D. R., Brock, P. R., Chang, K. W., Dupuis, L. L., Epelman, S., Knight, K., Mills, D., Phillips, R., Potter, E., Risby, D., Simpkin, P., Sullivan, M., Cabral, S., Robinson, P. D., & Sung, L. (2020). Prevention of cisplatin-induced ototoxicity in children and adolescents with cancer: A clinical practice guideline. *The Lancet Child & Adolescent Health, 4*(2), 141–150. https://doi.org/10.1016/S2352-4642(19)30336-0（PMID: 31866182）

Freyer, D. R., Chen, L., Krailo, M. D., Knight, K., Villaluna, D., Bliss, B., Pollock, B. H., Ramdas, J., Lange, B., Van Hoff, D., VanSoelen, M. L., Wiernikowski, J., Neuwelt, E. A., & Sung, L. (2017). Effects of sodium thiosulfate versus observation on development of cisplatin-induced hearing loss in children with cancer (ACCL0431): A multicentre, randomised, controlled, open-label, phase 3 trial. *The Lancet Oncology, 18*(1), 63–74. https://doi.org/10.1016/S1470-2045(16)30625-8（PMID: 27914822）

Genentech. (2025). *Avastin (bevacizumab) injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=939b5d1f-9fb2-4499-80ef-0607aa6b114e（版本日期 2025-01-06）

Genentech. (2026a). *Alecensa (alectinib) capsules* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=42c49deb-713b-427a-9670-08af08adcffb（版本日期 2026-08-21）

Genentech. (2026b). *Cathflo Activase (alteplase) for injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=91ecdef2-95ff-42dd-a31c-c8a09cab3ad9（版本日期 2026-01-20）

Genentech. (2026c). *Herceptin (trastuzumab) for injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=492dbdb2-077e-4064-bff3-372d6af0a7a2（版本日期 2026-05-29）

Gilead. (2026). *Trodelvy (sacituzumab govitecan-hziy) for injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=57a597d2-03f0-472e-b148-016d7169169d（版本日期 2026-06-24）

Griggs, J. J., Bohlke, K., Balaban, E. P., Dignam, J. J., Hall, E. T., Harvey, R. D., Hecht, D. P., Klute, K. A., Morrison, V. A., Pini, T. M., Rosner, G. L., Runowicz, C. D., Shayne, M., Sparreboom, A., Turner, S., Zarwan, C., & Lyman, G. H. (2021). Appropriate systemic therapy dosing for obese adult patients with cancer: ASCO guideline update. *Journal of Clinical Oncology, 39*(18), 2037–2048. https://doi.org/10.1200/JCO.21.00471（PMID: 33939491）

H2-Pharma. (2026). *Xeloda (capecitabine) tablets* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e702d84d-7162-4751-bf37-d724cc7e45a5（版本日期 2026-02-05）

Henricks, L. M., Lunenburg, C. A. T. C., de Man, F. M., Meulendijks, D., Frederix, G. W. J., Kienhuis, E., Creemers, G.-J., Baars, A., Dezentjé, V. O., Imholz, A. L. T., Jeurissen, F. J. F., Portielje, J. E. A., Jansen, R. L. H., Hamberg, P., Ten Tije, A. J., Droogendijk, H. J., Koopman, M., Nieboer, P., van de Poel, M. H. W., . . . Schellens, J. H. M. (2018). DPYD genotype-guided dose individualisation of fluoropyrimidine therapy in patients with cancer: A prospective safety analysis. *The Lancet Oncology, 19*(11), 1459–1467. https://doi.org/10.1016/S1470-2045(18)30686-7（PMID: 30348537）

Hensley, M. L., Hagerty, K. L., Kewalramani, T., Green, D. M., Meropol, N. J., Wasserman, T. H., Cohen, G. I., Emami, B., Gradishar, W. J., Mitchell, R. B., Thigpen, J. T., Trotti, A., III, von Hoff, D., & Schuchter, L. M. (2009). American Society of Clinical Oncology 2008 clinical practice guideline update: Use of chemotherapy and radiation therapy protectants. *Journal of Clinical Oncology, 27*(1), 127–145. https://doi.org/10.1200/JCO.2008.17.2627（PMID: 19018081）

Hensley, M. L., Schuchter, L. M., Lindley, C., Meropol, N. J., Cohen, G. I., Broder, G., Gradishar, W. J., Green, D. M., Langdon, R. J., Jr., Mitchell, R. B., Negrin, R., Szatrowski, T. P., Thigpen, J. T., Von Hoff, D., Wasserman, T. H., Winer, E. P., & Pfister, D. G. (1999). American Society of Clinical Oncology clinical practice guidelines for the use of chemotherapy and radiotherapy protectants. *Journal of Clinical Oncology, 17*(10), 3333–3355. https://doi.org/10.1200/JCO.1999.17.10.3333（PMID: 10506637）

Hikma. (2026). *Methylene blue injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4f222ee5-df03-46d5-a060-c63565b7186f（版本日期 2026-02-09）

Hinke, D. H., Zandt-Stastny, D. A., Goodman, L. R., Quebbeman, E. J., Krzywda, E. A., & Andris, D. A. (1990). Pinch-off syndrome: A complication of implantable subclavian venous access devices. *Radiology, 177*(2), 353–356. https://doi.org/10.1148/radiology.177.2.2217768（PMID: 2217768）

Hisun. (2026). *Daunorubicin hydrochloride injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9705fa12-499e-41a3-8fb4-f6df0858b851（版本日期 2026-01-19）

Hospira. (2025). *Mitoxantrone injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=accf9569-4b57-4e83-a7db-4e890a75d1ba（版本日期 2025-07-14）

Hospira. (2026). *Vincristine sulfate injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b22e4c8e-dbe1-4d4b-a026-e1812974071c（版本日期 2026-02-17）

Howard, S. C., McCormick, J., Pui, C.-H., Buddington, R. K., & Harvey, R. D. (2016). Preventing and managing toxicities of high-dose methotrexate. *The Oncologist, 21*(12), 1471–1482. https://doi.org/10.1634/theoncologist.2015-0164（PMID: 27496039）

Hsiao, H. H., Yang, M. Y., Chang, J. G., Liu, Y. C., Liu, T. C., Chang, C. S., Chen, T. P., & Lin, S. F. (2004). Dihydropyrimidine dehydrogenase pharmacogenetics in the Taiwanese population. *Cancer Chemotherapy and Pharmacology, 53*(5), 445–451. https://doi.org/10.1007/s00280-003-0749-y（PMID: 15132136）

Hung, S. I., Chung, W. H., Liou, L. B., Chu, C. C., Lin, M., Huang, H. P., Lin, Y. L., Lan, J. L., Yang, L. C., Hong, H. S., Chen, M. J., Lai, P. C., Wu, M. S., Chu, C. Y., Wang, K. H., Chen, C. H., Fann, C. S. J., Wu, J. Y., & Chen, Y. T. (2005). HLA-B\*5801 allele as a genetic marker for severe cutaneous adverse reactions caused by allopurinol. *Proceedings of the National Academy of Sciences of the United States of America, 102*(11), 4134–4139. https://doi.org/10.1073/pnas.0409500102（PMID: 15743917）

Hurria, A., Togawa, K., Mohile, S. G., Owusu, C., Klepin, H. D., Gross, C. P., Lichtman, S. M., Gajra, A., Bhatia, S., Katheria, V., Klapper, S., Hansen, K., Ramani, R., Lachs, M., Wong, F. L., & Tew, W. P. (2011). Predicting chemotherapy toxicity in older adults with cancer: A prospective multicenter study. *Journal of Clinical Oncology, 29*(25), 3457–3465. https://doi.org/10.1200/JCO.2011.34.7625（PMID: 21810685）

Hwang, J. P., Feld, J. J., Hammond, S. P., Wang, S. H., Alston-Johnson, D. E., Cryer, D. R., Hershman, D. L., Loehrer, A. P., Sabichi, A. L., Symington, B. E., Terrault, N., Wong, M. L., Somerfield, M. R., & Artz, A. S. (2020). Hepatitis B virus screening and management for patients with cancer prior to therapy: ASCO provisional clinical opinion update. *Journal of Clinical Oncology, 38*(31), 3698–3715. https://doi.org/10.1200/JCO.20.01757（PMID: 32716741）

Key, N. S., Khorana, A. A., Kuderer, N. M., Bohlke, K., Lee, A. Y. Y., Arcelus, J. I., Wong, S. L., Balaban, E. P., Flowers, C. R., Gates, L. E., Kakkar, A. K., Tempero, M. A., Gupta, S., Lyman, G. H., & Falanga, A. (2023). Venous thromboembolism prophylaxis and treatment in patients with cancer: ASCO guideline update. *Journal of Clinical Oncology, 41*(16), 3063–3071. https://doi.org/10.1200/JCO.23.00294（PMID: 37075273）

Legacy. (2026). *Ethyol (amifostine) for injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a17563f2-d231-4385-bc94-0217be78b89d（版本日期 2026-03-03）

Lentz, K. L., Clark, S. M., Ayarza, M., Liu, B., Morgan, K. P., Wind, L. S., & Hairston, A. (2020). Evaluation of thiamine for the prevention of ifosfamide-induced encephalopathy. *Journal of Oncology Pharmacy Practice, 26*(2), 406–412. https://doi.org/10.1177/1078155219859644（PMID: 31288633）

Liu, C.-Y., Chen, P.-M., Chiou, T.-J., Liu, J.-H., Lin, J.-K., Lin, T.-C., Chen, W.-S., Jiang, J.-K., Wang, H.-S., & Wang, W.-S. (2008). UGT1A1\*28 polymorphism predicts irinotecan-induced severe toxicities without affecting treatment outcome and survival in patients with metastatic colorectal carcinoma. *Cancer, 112*(9), 1932–1940. https://doi.org/10.1002/cncr.23370（PMID: 18300238）

Lo, Y., Shen, L.-J., Chen, W.-H., Dong, Y.-H., & Wu, F.-L. L. (2016). Risk factors of ifosfamide-related encephalopathy in adult patients with cancer: A retrospective analysis. *Journal of the Formosan Medical Association, 115*(9), 744–751. https://doi.org/10.1016/j.jfma.2015.07.016（PMID: 26302952）

López-Briz, E., Ruiz Garcia, V., Cabello, J. B., Bort-Martí, S., & Carbonell Sanchis, R. (2022). Heparin versus 0.9% sodium chloride locking for prevention of occlusion in central venous catheters in adults. *Cochrane Database of Systematic Reviews, 2022*(7), Article CD008462. https://doi.org/10.1002/14651858.CD008462.pub4（PMID: 35849083）

McDonnell, A. M., Rybak, I., Wadleigh, M., & Fisher, D. C. (2012). Suspected serotonin syndrome in a patient being treated with methylene blue for ifosfamide encephalopathy. *Journal of Oncology Pharmacy Practice, 18*(4), 436–439. https://doi.org/10.1177/1078155211433231（PMID: 22235061）

Meitheal. (2025). *Gemcitabine injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c0b1b715-9ff8-43ca-9e49-465f1f380084（版本日期 2025-07-23）

Meitheal. (2026). *Bleomycin for injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=640602f9-a7df-46f0-a9b1-19c471008bee（版本日期 2026-04-17）

Mermel, L. A., Allon, M., Bouza, E., Craven, D. E., Flynn, P., O'Grady, N. P., Raad, I. I., Rijnders, B. J. A., Sherertz, R. J., & Warren, D. K. (2009). Clinical practice guidelines for the diagnosis and management of intravascular catheter-related infection: 2009 update by the Infectious Diseases Society of America. *Clinical Infectious Diseases, 49*(1), 1–45. https://doi.org/10.1086/599376（PMID: 19489710）

Mosteller, R. D. (1987). Simplified calculation of body-surface area. *The New England Journal of Medicine, 317*(17), 1098. https://doi.org/10.1056/NEJM198710223171717（PMID: 3657876）

Mouridsen, H. T., Langer, S. W., Buter, J., Eidtmann, H., Rosti, G., de Wit, M., Knoblauch, P., Rasmussen, A., Dahlstrøm, K., Jensen, P. B., & Giaccone, G. (2007). Treatment of anthracycline extravasation with Savene (dexrazoxane): Results from two prospective clinical multicentre studies. *Annals of Oncology, 18*(3), 546–550. https://doi.org/10.1093/annonc/mdl413（PMID: 17185744）

Mylan. (2026). *Docetaxel injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2992d633-08fa-44f3-b14d-41700f24686b（版本日期 2026-04-15）

Natco. (2026). *Carboplatin injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4c89cedc-e48b-445c-ad05-54dbe60e4fb0（版本日期 2026-07-21）

National Cancer Institute, Division of Cancer Treatment and Diagnosis. (2025, September 9). *CTCAE v6.0 implementation FAQs*. https://dctd.cancer.gov/research/ctep-trials/for-sites/adverse-events/ctcae-v6-faq.pdf

National Cancer Institute, Division of Cancer Treatment and Diagnosis. (2026). *CTCAE updated to version 6*. https://dctd.cancer.gov/about/news-events/news/2026-news/ctcae-updated-version-6

Neuss, M. N., Gilmore, T. R., Belderson, K. M., Billett, A. L., Conti-Kalchik, T., Harvey, B. E., Hendricks, C., LeFebvre, K. B., Mangu, P. B., McNiff, K., Olsen, M., Schulmeister, L., Von Gehr, A., & Polovich, M. (2016). 2016 updated American Society of Clinical Oncology/Oncology Nursing Society chemotherapy administration safety standards, including standards for pediatric oncology. *Journal of Oncology Practice, 12*(12), 1262–1271. https://doi.org/10.1200/JOP.2016.017905（PMID: 27868581）

Neuss, M. N., Polovich, M., McNiff, K., Esper, P., Gilmore, T. R., LeFebvre, K. B., Schulmeister, L., & Jacobson, J. O. (2013). 2013 updated American Society of Clinical Oncology/Oncology Nursing Society chemotherapy administration safety standards including standards for the safe administration and management of oral chemotherapy. *Journal of Oncology Practice, 9*(2 Suppl), 5s–13s. https://doi.org/10.1200/JOP.2013.000874（PMID: 23914148）

Nickel, B., Gorski, L., Kleidon, T., Kyes, A., DeVries, M., Keogh, S., Meyer, B., Sarver, M. J., Crickman, R., Ong, J., Clare, S., & Hagle, M. E. (2024). Infusion therapy standards of practice, 9th edition. *Journal of Infusion Nursing, 47*(1S Suppl 1), S1–S285. https://doi.org/10.1097/NAN.0000000000000532（PMID: 38211609）

Novartis. (2026a). *Gleevec (imatinib mesylate) tablets* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=211ef2da-2868-4a77-8055-1cb2cd78e24b（版本日期 2026-07-13）

Novartis. (2026b). *Kisqali (ribociclib) tablets* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=aaeaef94-f3f5-4367-8ea2-b181d7be2da8（版本日期 2026-07-01）

O'Grady, N. P., Alexander, M., Burns, L. A., Dellinger, E. P., Garland, J., Heard, S. O., Lipsett, P. A., Masur, H., Mermel, L. A., Pearson, M. L., Raad, I. I., Randolph, A. G., Rupp, M. E., Saint, S., & Healthcare Infection Control Practices Advisory Committee. (2011). Guidelines for the prevention of intravascular catheter-related infections. *American Journal of Infection Control, 39*(4 Suppl 1), S1–S34. https://doi.org/10.1016/j.ajic.2011.01.003（PMID: 21511081）

Oken, M. M., Creech, R. H., Tormey, D. C., Horton, J., Davis, T. E., McFadden, E. T., & Carbone, P. P. (1982). Toxicity and response criteria of the Eastern Cooperative Oncology Group. *American Journal of Clinical Oncology, 5*(6), 649–655.（PMID: 7165009）

Oktay, K., Harvey, B. E., Partridge, A. H., Quinn, G. P., Reinecke, J., Taylor, H. S., Wallace, W. H., Wang, E. T., & Loren, A. W. (2018). Fertility preservation in patients with cancer: ASCO clinical practice guideline update. *Journal of Clinical Oncology, 36*(19), 1994–2001. https://doi.org/10.1200/JCO.2018.78.1914（PMID: 29620997）

Oncology Nursing Society. (2026, July 9). *Here's what the updated CTCAE version 6.0 means for oncology nurses*. ONS Voice. https://www.ons.org/publications-research/voice/news-views/07-2026/heres-what-updated-ctcae-version-60-means-oncology-nurses

Pérez Fidalgo, J. A., García Fabregat, L., Cervantes, A., Margulies, A., Vidall, C., & Roila, F. (2012). Management of chemotherapy extravasation: ESMO-EONS clinical practice guidelines. *Annals of Oncology, 23*(Suppl 7), vii167–vii173. https://doi.org/10.1093/annonc/mds294（PMID: 22997449）

Pfizer. (2026a). *Doxorubicin hydrochloride injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=00634b2b-4e48-4178-8877-28582af894ad（版本日期 2026-04-30）

Pfizer. (2026b). *Idamycin PFS (idarubicin hydrochloride) injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0a5a6d93-cc1e-4d7f-8da1-446c134503b3（版本日期 2026-04-15）

Pfizer. (2026c). *Lorbrena (lorlatinib) tablets* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2b34d62d-e02a-4af3-bc0d-1571dd4ee76d（版本日期 2026-06-26）

Pharmacia & Upjohn. (2026a). *Camptosar (irinotecan hydrochloride) injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e518dfc6-7e93-4fee-a66c-51e1ab71c056（版本日期 2026-05-12）

Pharmacia & Upjohn. (2026b). *Ellence (epirubicin hydrochloride) injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0a03c798-a652-4895-b29c-3b521a89ba42（版本日期 2026-07-24）

Power, L. A., & Coyne, J. W. (2018). ASHP guidelines on handling hazardous drugs. *American Journal of Health-System Pharmacy, 75*(24), 1996–2031. https://doi.org/10.2146/ajhp180564（PMID: 30327293）

Ramsey, L. B., Balis, F. M., O'Brien, M. M., Schmiegelow, K., Pauley, J. L., Bleyer, A., Widemann, B. C., Askenazi, D., Bergeron, S., Shirali, A., Schwartz, S., Vinks, A. A., & Heldrup, J. (2018). Consensus guideline for use of glucarpidase in patients with high-dose methotrexate induced acute kidney injury and delayed methotrexate clearance. *The Oncologist, 23*(1), 52–61. https://doi.org/10.1634/theoncologist.2017-0243（PMID: 29079637）

Relling, M. V., Schwab, M., Whirl-Carrillo, M., Suarez-Kurtz, G., Pui, C.-H., Stein, C. M., Moyer, A. M., Evans, W. E., Klein, T. E., Antillon-Klussmann, F. G., Caudle, K. E., Kato, M., Yeoh, A. E. J., Schmiegelow, K., & Yang, J. J. (2019). Clinical Pharmacogenetics Implementation Consortium guideline for thiopurine dosing based on TPMT and NUDT15 genotypes: 2018 update. *Clinical Pharmacology & Therapeutics, 105*(5), 1095–1105. https://doi.org/10.1002/cpt.1304（PMID: 30447069）

Richards, A., Marshall, H., & McQuary, A. (2011). Evaluation of methylene blue, thiamine, and/or albumin in the prevention of ifosfamide-related neurotoxicity. *Journal of Oncology Pharmacy Practice, 17*(4), 372–380. https://doi.org/10.1177/1078155210385159（PMID: 20861178）

Sagent. (2025). *Oxaliplatin injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=29a5d098-bfa7-4a65-bb4f-5daa1fef1c2f（版本日期 2025-09-09）

Sagent. (2026). *Leucovorin calcium injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c0cbcbf6-6fd2-4cf3-877a-bb0fe3df4e59（版本日期 2026-06-16）

Sanofi-Aventis. (2026). *Elitek (rasburicase) for injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0ae10bc4-6b65-402f-9db5-2d7753054922（版本日期 2026-07-30）

Schiffer, C. A., Mangu, P. B., Wade, J. C., Camp-Sorrell, D., Cope, D. G., El-Rayes, B. F., Gorman, M., Ligibel, J., Mansfield, P., & Levine, M. (2013). Central venous catheter care for the patient with cancer: American Society of Clinical Oncology clinical practice guideline. *Journal of Clinical Oncology, 31*(10), 1357–1370. https://doi.org/10.1200/JCO.2012.45.5733（PMID: 23460705）

Skinner, R., Cotterill, S. J., & Stevens, M. C. (2000). Risk factors for nephrotoxicity after ifosfamide treatment in children: A UKCCSG Late Effects Group study. *British Journal of Cancer, 82*(10), 1636–1645. https://doi.org/10.1054/bjoc.2000.1214（PMID: 10817497）

Su, H. I., Lacchetti, C., Letourneau, J., Partridge, A. H., Qamar, R., Quinn, G. P., Reinecke, J., Smith, J. F., Tesch, M., Wallace, W. H., Wang, E. T., & Loren, A. W. (2025). Fertility preservation in people with cancer: ASCO guideline update. *Journal of Clinical Oncology, 43*(12), 1488–1515. https://doi.org/10.1200/JCO-24-02782（PMID: 40106739）

Sun, J., Ilich, A. I., Kim, C. A., Chu, M. P., Wong, G. G., Ghosh, S., Danilak, M., Mulder, K. E., Spratlin, J. L., Chambers, C. R., & Sawyer, M. B. (2016). Concomitant administration of proton pump inhibitors and capecitabine is associated with increased recurrence risk in early stage colorectal cancer patients. *Clinical Colorectal Cancer, 15*(3), 257–263. https://doi.org/10.1016/j.clcc.2015.12.008（PMID: 26803708）

Sun Pharmaceutical Industries. (2026). *Pazopanib tablets* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d3e8dd09-d7d2-43da-8f63-bdf0ea0fcdf5（版本日期 2026-05-19）

Swain, S. M., Whaley, F. S., & Ewer, M. S. (2003). Congestive heart failure in patients treated with doxorubicin: A retrospective analysis of three trials. *Cancer, 97*(11), 2869–2879. https://doi.org/10.1002/cncr.11407（PMID: 12767102）

Sweiss, K. I., Beri, R., & Shord, S. S. (2008). Encephalopathy after high-dose ifosfamide: A retrospective cohort study and review of the literature. *Drug Safety, 31*(11), 989–996. https://doi.org/10.2165/00002018-200831110-00003（PMID: 18840018）

Teva Parenteral Medicines. (2026). *Paclitaxel injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e4be6cbf-72b9-4f7f-9b1b-459b2d35961a（版本日期 2026-09-09）

Torchia, A., Vari, S., Onesti, C. E., Ceddia, S., Maschio, M., Maggi, G., Riva, F., Faltyn, W., Russillo, M., & Ferraresi, V. (2025). A narrative review on diagnosis and treatment of ifosfamide-induced encephalopathy, the perspective of a EURACAN reference center for sarcomas. *Frontiers in Pharmacology, 16*, Article 1512966. https://doi.org/10.3389/fphar.2025.1512966（PMID: 40061960）

Tsai, H.-L., Huang, C.-W., Lin, Y.-W., Wang, J.-H., Wu, C.-C., Sung, Y.-C., Chen, T.-L., Wang, H.-M., Tang, H.-C., Chen, J.-B., Ke, T.-W., Tsai, C.-S., Huang, H.-Y., & Wang, J.-Y. (2020). Determination of the UGT1A1 polymorphism as guidance for irinotecan dose escalation in metastatic colorectal cancer treated with first-line bevacizumab and FOLFIRI (PURE FIST). *European Journal of Cancer, 138*, 19–29. https://doi.org/10.1016/j.ejca.2020.05.031（PMID: 32829105）

Wang, T.-Y., Lee, K.-D., Chen, P.-T., Chen, M.-C., Chen, Y.-Y., Huang, C.-E., Kuan, F.-C., Chen, C.-C., & Lu, C.-H. (2015). Incidence and risk factors for central venous access port-related infection in Chinese cancer patients. *Journal of the Formosan Medical Association, 114*(11), 1055–1060. https://doi.org/10.1016/j.jfma.2015.06.013（PMID: 26253646）

WG Critical Care. (2026). *Cisplatin injection* [Package insert]. DailyMed. https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=508496cb-3441-46b3-a4fe-e0d440e6adc6（版本日期 2026-06-24）

Yokoi, K., Nakajima, Y., Matsuoka, H., Shinkai, Y., Ishihara, T., Maeda, Y., Kato, T., Katsuno, H., Masumori, K., Kawada, K., Yoshikawa, T., Ito, T., & Kurahashi, H. (2020). Impact of DPYD, DPYS, and UPB1 gene variations on severe drug-related toxicity in patients with cancer. *Cancer Science, 111*(9), 3359–3366. https://doi.org/10.1111/cas.14553（PMID: 32619063）
