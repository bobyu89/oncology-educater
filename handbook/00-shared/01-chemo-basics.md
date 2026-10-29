# 化療基礎與劑量計算（Chemotherapy Basics & Dosing）

| 項目 | 內容 |
|------|------|
| 主要依據 | ASCO 肥胖病人劑量指引 2021、ASCO HBV 臨床意見 2020、ESMO-EONS 外滲指引 2012、ASHP 危害藥品操作指引 2018 |
| 毒性分級 | NCI CTCAE v5.0（理由與 v6.0 差異見第 8 節） |
| 健保規定 | 本章不涉及第 9 節條文；B 肝預防用藥給付另見對應章節（見第 6 節提示框） |
| 最後更新 | 2026-10-29 |

> 本手冊是學習用整理，不能取代原始指引、仿單、健保公告與院內規範。實際處方以主治醫師判斷與院內流程為準。

---

## 本章重點

- **開化療前先問三件事**：病人撐得住嗎（ECOG）？器官功能夠嗎（CBC、腎、肝）？有沒有隱藏地雷（B 肝、懷孕、過敏史）？
- **劑量三把尺**：細胞毒性藥用 **BSA**（mg/m²）、carboplatin 用 **Calvert 公式**（AUC）、部分藥用 **體重**（mg/kg）或固定劑量（flat dose）。
- **Calvert 公式算出來是「總毫克數」**，不是 mg/m²；GFR 上限 125 mL/min，所以 AUC 5 最多 750 mg、AUC 6 最多 900 mg。
- **肥胖病人用實際體重算足量**，不要常規把 BSA 封頂在 2.0 m²（ASCO 2021）。
- **HBsAg 陽性者開任何全身性抗癌治療都要預防性抗病毒**，治療結束後至少再吃 12 個月（ASCO 2020）。
- **外滲先停、先抽、再處置**；anthracycline 外滲 6 小時內可給 dexrazoxane。

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
> Carboplatin 幾乎全靠腎臟排出。AUC 是「藥物在血中停留的總量」，你想要的總量固定，腎臟排得越快（GFR 越高），就要給越多；排得越慢，就給越少。就像往有破洞的水桶裡倒水，想維持一樣的水位，洞越大要倒越多。

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
| 血紅素（Hb） | 無固定門檻；有症狀或 < 8 g/dL 考慮輸血 | 化療前貧血需找原因（出血、缺鐵、腎性） |
| 腎功能 | 依藥物：pemetrexed 在 CrCl < 45 mL/min 不建議使用；capecitabine 在 CrCl 30–50 mL/min 起始劑量減為 75%、< 30 禁用 | Cisplatin 的腎功能門檻各院不同 |
| 肝功能 | 依藥物：docetaxel 在 bilirubin > ULN，或 AST/ALT > 1.5 × ULN 且 ALP > 2.5 × ULN 時不應使用（仿單警語） | Taxane、anthracycline、irinotecan、vinca 類對肝功能敏感 |
| 前次毒性 | 非血液毒性恢復到 ≤ Grade 1（脫髮除外） | 未恢復 → 延後或減量 |
| 身高、體重 | 體重變化超過院內規定比例須重算 BSA | 見第 2 節提示框 |
| B 型肝炎 | 開始全身治療前驗 HBsAg、anti-HBc、anti-HBs | 見第 6 節 |
| 懷孕 | 有生育可能的女性做懷孕檢測，並討論避孕 | 多數抗癌藥具致畸性 |
| 過敏史與前置用藥 | Taxane、platinum、單株抗體類需確認 premedication | 第 2 次以後的 carboplatin 仍可能過敏（累積劑量相關） |
| 血管通路 | 周邊靜脈或 port-A 狀況；發泡劑盡量走中心靜脈 | 見第 9 節 |
| 知情同意 | 新處方或改變處方須重新說明並簽署 | — |

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

> [!CAUTION]
> **健保給付需另行核對**
> 化療病人 B 型肝炎預防性抗病毒藥的健保給付條件（可用藥品、起訖時間、需檢附的檢驗）不屬於第 9 節「抗癌瘤藥物」，本手冊尚未取得對應章節原文。開立前請依最新《藥品給付規定》相關章節與院內流程核對。

---

## 7. 劑量調整原則

### 7.1 因毒性調整

| 情況 | 常見處理 |
|------|---------|
| 下一週期開始時血球未恢復 | 延後 1 週再評估（ANC、PLT 恢復到門檻） |
| 前一週期發生 Grade 3–4 血液毒性或發燒性嗜中性球低下 | 下一週期減一個劑量等級（常見為減 20–25%），或在治癒目標下加上 G-CSF 次級預防 |
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
> - Pemetrexed：CrCl < 45 mL/min 不建議使用；capecitabine：CrCl 30–50 起始劑量 75%，< 30 禁用。

---

## 8. CTCAE 分級原則

### 8.1 版本說明

美國國家癌症研究院（NCI）於 2025 年發布 **CTCAE v6.0**（實施 FAQ 日期為 2025-09-09），主要更新三個方向：基線檢驗值已異常病人的分級方式、免疫治療相關不良事件的描述、心臟相關不良事件的分類（NCI, 2025, 2026）。NCI 表示 v6.0 可立即用於多數研究，但 NCI CTEP/DCP 既有研究維持使用 v5.0，新研究則在其資料系統更新後改用 v6.0。

**本手冊以 CTCAE v5.0 為主要分級依據**，原因是：目前大多數已發表的關鍵試驗、藥品仿單的劑量調整表，以及 ASCO 2021、ESMO 2022 的 irAE 指引，都是以 v5.0（或更早版本）撰寫。

v6.0 最明顯的差異之一是**以病人自己的基線值分級**：例如基線肌酸酐 0.5 mg/dL（低於正常下限）上升到 2.0 mg/dL，v5.0 為 Grade 2（約 1.54 × ULN），v6.0 則因為是基線的 4 倍而判為 Grade 3（Oncology Nursing Society, 2026）。

> [!NOTE]
> **院內若已改用 v6.0**
> 部分醫院或新開的臨床試驗可能已改用 v6.0，請依院內規範或試驗 protocol 指定的版本記錄。

> [!CAUTION]
> **v6.0 細項門檻尚待逐項核對**
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
> **分類在不同文獻並不一致**
> Paclitaxel、docetaxel、oxaliplatin 在不同參考資料中被歸為發泡劑或刺激劑。本表參考 ESMO-EONS 2012 的分類架構（Pérez Fidalgo et al., 2012），因未能取得原文全文逐項核對，請以院內藥劑部公告的發泡劑清單為準。

### 9.2 處置流程

**通用步驟（所有藥物）：**

1. **立即停止輸注**，但先**不要拔針**。
2. 接空針，**從原管路回抽**殘留藥液與血液。
3. 拔除針頭；**不要對外滲部位加壓**。
4. 用筆標出範圍、拍照，抬高患肢。
5. 通知醫師，依藥物給予特定解毒劑與冷敷或熱敷。
6. 記錄：時間、藥名、濃度、估計外滲量、症狀、處置；安排 24 小時、1 週等追蹤，持續疼痛或壞死時會診整形外科。

**依藥物的特定處置：**

| 藥物類別 | 敷法 | 解毒劑或特殊處置 |
|---------|------|---------------|
| Anthracyclines | 冷敷 | **Dexrazoxane IV**，**6 小時內**開始：D1 1,000 mg/m²、D2 1,000 mg/m²、D3 500 mg/m²，打在對側肢體（Mouridsen et al., 2007）；給藥前至少 15 分鐘移除冷敷 |
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

## 11. 自我測驗

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

**答案：B**。外滲的第一步是停止輸注、保留針頭、從原管路回抽殘留藥液，之後才拔針。Epirubicin 屬 anthracycline，應冷敷（不是熱敷），並評估在 6 小時內給予 dexrazoxane。

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

---

## 12. 參考文獻

Calvert, A. H., Newell, D. R., Gumbrell, L. A., O'Reilly, S., Burnell, M., Boxall, F. E., Siddik, Z. H., Judson, I. R., Gore, M. E., & Wiltshaw, E. (1989). Carboplatin dosage: Prospective evaluation of a simple formula based on renal function. *Journal of Clinical Oncology, 7*(11), 1748–1756. https://doi.org/10.1200/JCO.1989.7.11.1748 (PMID: 2681557)

Cockcroft, D. W., & Gault, M. H. (1976). Prediction of creatinine clearance from serum creatinine. *Nephron, 16*(1), 31–41. https://doi.org/10.1159/000180580 (PMID: 1244564)

Griggs, J. J., Bohlke, K., Balaban, E. P., Dignam, J. J., Hall, E. T., Harvey, R. D., Hecht, D. P., Klute, K. A., Morrison, V. A., Pini, T. M., Rosner, G. L., Runowicz, C. D., Shayne, M., Sparreboom, A., Turner, S., Zarwan, C., & Lyman, G. H. (2021). Appropriate systemic therapy dosing for obese adult patients with cancer: ASCO guideline update. *Journal of Clinical Oncology, 39*(18), 2037–2048. https://doi.org/10.1200/JCO.21.00471 (PMID: 33939491)

Hwang, J. P., Feld, J. J., Hammond, S. P., Wang, S. H., Alston-Johnson, D. E., Cryer, D. R., Hershman, D. L., Loehrer, A. P., Sabichi, A. L., Symington, B. E., Terrault, N., Wong, M. L., Somerfield, M. R., & Artz, A. S. (2020). Hepatitis B virus screening and management for patients with cancer prior to therapy: ASCO provisional clinical opinion update. *Journal of Clinical Oncology, 38*(31), 3698–3715. https://doi.org/10.1200/JCO.20.01757 (PMID: 32716741)

Mosteller, R. D. (1987). Simplified calculation of body-surface area. *New England Journal of Medicine, 317*(17), 1098. https://doi.org/10.1056/NEJM198710223171717 (PMID: 3657876)

Mouridsen, H. T., Langer, S. W., Buter, J., Eidtmann, H., Rosti, G., de Wit, M., Knoblauch, P., Rasmussen, A., Dahlstrøm, K., Jensen, P. B., & Giaccone, G. (2007). Treatment of anthracycline extravasation with Savene (dexrazoxane): Results from two prospective clinical multicentre studies. *Annals of Oncology, 18*(3), 546–550. https://doi.org/10.1093/annonc/mdl413 (PMID: 17185744)

National Cancer Institute, Division of Cancer Treatment and Diagnosis. (2025, September 9). *CTCAE v6.0 implementation FAQs*. https://dctd.cancer.gov/research/ctep-trials/for-sites/adverse-events/ctcae-v6-faq.pdf

National Cancer Institute, Division of Cancer Treatment and Diagnosis. (2026). *CTCAE updated to version 6*. https://dctd.cancer.gov/about/news-events/news/2026-news/ctcae-updated-version-6

Oken, M. M., Creech, R. H., Tormey, D. C., Horton, J., Davis, T. E., McFadden, E. T., & Carbone, P. P. (1982). Toxicity and response criteria of the Eastern Cooperative Oncology Group. *American Journal of Clinical Oncology, 5*(6), 649–655. (PMID: 7165009)

Oncology Nursing Society. (2026, July 9). *Here's what the updated CTCAE version 6.0 means for oncology nurses*. ONS Voice. https://www.ons.org/publications-research/voice/news-views/07-2026/heres-what-updated-ctcae-version-60-means-oncology-nurses

Pérez Fidalgo, J. A., García Fabregat, L., Cervantes, A., Margulies, A., Vidall, C., & Roila, F. (2012). Management of chemotherapy extravasation: ESMO-EONS clinical practice guidelines. *Annals of Oncology, 23*(Suppl 7), vii167–vii173. https://doi.org/10.1093/annonc/mds294 (PMID: 22997449)

Power, L. A., & Coyne, J. W. (2018). ASHP guidelines on handling hazardous drugs. *American Journal of Health-System Pharmacy, 75*(24), 1996–2031. https://doi.org/10.2146/ajhp180564 (PMID: 30327293)
