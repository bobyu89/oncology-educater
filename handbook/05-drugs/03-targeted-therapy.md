# 標靶藥物（Targeted Therapy and Antibody-Drug Conjugates）

| 項目 | 本章依據 |
|------|---------|
| 主要來源 | 原始論文與關鍵試驗（見[第 11 段](#11-參考文獻)，全部以 PubMed 資料核對）；歷史與機轉回顧：Strebhardt & Ullrich, 2008；Imai & Takaoka, 2006；Drago et al., 2021；藥動學：Keizer et al., 2010；van Leeuwen et al., 2014 |
| 仿單 | 美國 FDA 核准仿單（DailyMed，2026-11-11 查詢）：Herceptin、Enhertu、Avastin、Tagrisso、Lorbrena、Kisqali、Votrient、Stivarga、Ayvakit、Lynparza；歐盟 EMA 產品資訊：Alecensa。本章引用仿單數字時都會註明是哪一份；台灣核准仿單可能不同 |
| 副作用分級 | NCI CTCAE v5.0（理由見[化療基礎](../00-shared/01-chemo-basics.md#8-ctcae-分級原則)第 8 節） |
| 台灣藥證與健保 | 本章不重述。請見各癌別章第 9 段：[肺癌](../01-lung-cancer.md#9-健保給付與事前審查)、[胰臟癌](../02-pancreatic-cancer.md#9-健保給付與事前審查)、[乳癌](../03-breast-cancer.md#9-健保給付與事前審查)、[肉瘤](../04-sarcoma.md#9-健保給付與事前審查) |
| 最後更新 | 2026-11-11 |

**這一章的結論先講：** 標靶藥不是「比較溫和的化療」，而是「先驗到靶、才有藥可用」的治療。開藥前先有 biomarker 報告；每一類藥有一個固定要盯的器官（EGFR 看皮膚與肺、HER2 看心臟、VEGF 看血壓與尿蛋白、ADC 看肺與血球）；腫瘤終究會抗藥，所以惡化時要再驗一次，而不是直接換下一種藥。

相關章節：[藥物是怎麼來的](01-drug-development.md)、[細胞毒性化療](02-cytotoxic-chemotherapy.md)、[免疫治療藥物](04-immunotherapy.md)、[內分泌治療](05-endocrine-therapy.md)。本手冊是學習用整理，不能取代原始指引、仿單、健保公告與院內規範；實際處方以主治醫師判斷與院內流程為準。

---

## 0. 速查卡

| 類別 | 代表藥 | 開藥前先確認 | 必背毒性 | 處置細節在哪 |
|------|--------|-------------|---------|-------------|
| EGFR 小分子（TKI） | gefitinib、erlotinib、afatinib、dacomitinib、osimertinib | 腫瘤 EGFR 突變報告 | 痤瘡樣皮疹、腹瀉、甲溝炎；間質性肺病（ILD）；osimertinib 另看 QTc 與 LVEF | [肺癌章 6.1](../01-lung-cancer.md#61-egfr-tki) |
| EGFR 抗體 | cetuximab、amivantamab | cetuximab 看 KRAS（突變者無效）；amivantamab 看 EGFR 突變型別 | 輸注反應、皮疹、甲溝炎；amivantamab ＋ lazertinib 另有靜脈血栓 | [肺癌章 6.4](../01-lung-cancer.md#64-amivantamab-lazertinib)、[急症章第 10 節](../00-shared/02-oncologic-emergencies.md#10-輸注反應過敏反應與過敏性休克) |
| ALK、ROS1、RET、MET、NTRK、BRAF、KRAS G12C | alectinib、lorlatinib、crizotinib、selpercatinib、capmatinib、larotrectinib、dabrafenib ＋ trametinib、sotorasib | 對應的融合或突變報告 | 各藥不同：肌痛與 CK、血脂與情緒認知、高血壓與肝功能、周邊水腫、發燒 | [肺癌章 6.2](../01-lung-cancer.md#62-alkros1-tki)、[6.3](../01-lung-cancer.md#63-其他標靶藥) |
| 抗 HER2 | trastuzumab、pertuzumab；lapatinib、neratinib、tucatinib；T-DM1、T-DXd | HER2 的 IHC／ISH 結果 | 心臟（LVEF）；小分子藥腹瀉；T-DM1 血小板與肝；**T-DXd 的 ILD** | [乳癌章 6.2](../03-breast-cancer.md#62-抗-her2-治療lvef-監測與暫停規則)、[6.7](../03-breast-cancer.md#67-抗體藥物複合體t-dxdt-dm1sacituzumab-govitecandato-dxd) |
| 抗 VEGF／VEGFR 與多激酶 TKI | bevacizumab、ramucirumab；imatinib、sunitinib、regorafenib、ripretinib、avapritinib、pazopanib | 抗 VEGF 沒有預測性 biomarker，看組織型與出血風險；GIST 看 KIT／PDGFRA 基因型 | 高血壓、蛋白尿、出血、穿孔、傷口癒合不良；pazopanib 與 regorafenib 的肝毒性 | [肺癌章 6.8](../01-lung-cancer.md#68-抗血管新生藥物bevacizumab-與-ramucirumab)、[肉瘤章 6.7](../04-sarcoma.md#67-pazopanib肝毒性與高血壓)、[6.8](../04-sarcoma.md#68-gist-的-tkiimatinibsunitinibregorafenibripretinibavapritinib) |
| CDK4/6 抑制劑 | palbociclib、ribociclib、abemaciclib | HR 陽性、HER2 陰性乳癌 | 嗜中性球低下；ribociclib 的 QT 與肝；abemaciclib 的腹瀉 | [乳癌章 6.5](../03-breast-cancer.md#65-cdk46-抑制劑嗜中性球肝功能心電圖腹瀉) |
| PI3K／AKT／mTOR 抑制劑 | alpelisib、inavolisib、capivasertib、everolimus | PIK3CA（capivasertib 另含 AKT1、PTEN）變異；everolimus 不需基因檢測 | 高血糖、皮疹、腹瀉、口腔炎、非感染性肺炎 | [乳癌章 6.6](../03-breast-cancer.md#66-pi3kaktmtor-抑制劑高血糖皮疹腹瀉口腔炎) |
| PARP 抑制劑 | olaparib、talazoparib | germline BRCA1/2 致病變異 | 貧血、噁心、疲倦；MDS／AML（少見但要記） | [乳癌章 6.9](../03-breast-cancer.md#69-parp-抑制劑與-her2-小分子藥)、[胰臟癌章 6.6](../02-pancreatic-cancer.md#66-olaparib) |
| HER2 以外的 ADC | sacituzumab govitecan、datopotamab deruxtecan（Dato-DXd） | 不需驗 Trop-2 | 嗜中性球低下與腹瀉；口腔炎、眼睛、ILD | [乳癌章 6.7](../03-breast-cancer.md#67-抗體藥物複合體t-dxdt-dm1sacituzumab-govitecandato-dxd) |

> [!IMPORTANT]
> **必背數字（出處都在正文）**
> - **IPASS**：EGFR 突變陽性者用 gefitinib 的惡化風險 HR 0.48；突變陰性者 HR 2.85，反而比化療差（Mok et al., 2009）。這是「先驗再開藥」的原始證據。
> - **Trastuzumab 的 LVEF**：開始前測一次，治療中每 3 個月，輔助治療結束後每 6 個月、至少 2 年（美國仿單；Genentech, 2026）。
> - **T-DXd 的 ILD**：Grade 1 暫停；**Grade 2 以上永久停藥**（美國仿單；Daiichi Sankyo, 2026）。
> - **Bevacizumab**：擇期手術前至少停 28 天、大手術後至少 28 天且傷口癒合才給；尿蛋白 ≥2 g/24 小時暫停（美國仿單；Genentech, 2025）。
> - **Lorlatinib 禁止與強效 CYP3A 誘導劑（如 rifampin）併用**（美國仿單；Pfizer, 2026）。
> - **Ribociclib**：QTcF <450 ms 才開始；基線與第 1 週期約第 14 天做心電圖；避免與 tamoxifen 併用（美國仿單；Novartis, 2026）。

---

## 1. 怎麼被發現的

**結論先講：** 標靶治療的歷史是同一個故事重複很多次：先在腫瘤裡找到一個「癌細胞特別依賴」的分子，再做出鎖住它的藥，最後才發現只有帶著那個分子的病人有效。所以今天每一張標靶處方前面，都要有一份 biomarker 報告。

| 年份 | 事件 | 意義 |
|------|------|------|
| 1908 | Paul Ehrlich 獲得諾貝爾獎；他提出「魔術子彈（magic bullet）」的想法：做出只打病灶、不傷正常組織的藥（Strebhardt & Ullrich, 2008） | 標靶治療的理念源頭 |
| 1960 | Nowell 與 Hungerford 在慢性骨髓性白血病（chronic myeloid leukemia, CML）病人的細胞中看到一條異常小的染色體，後來稱為費城染色體（Nowell, 2007） | 把一個固定出現的染色體異常和一種癌症連在一起 |
| 1971 | Folkman 提出腫瘤血管新生（angiogenesis）可以當治療標的（Folkman, 1971） | 抗血管新生藥物的起點 |
| 1973 | Rowley 用 quinacrine 螢光與 Giemsa 染色，在 CML 找到一個新的、固定出現的染色體異常（Rowley, 1973）；費城染色體後來確認來自 9 號與 22 號染色體的易位（Nowell, 2007） | 之後才找到融合基因 BCR-ABL 與它製造的異常激酶 |
| 1975 | Köhler 與 Milstein 發表融合瘤（hybridoma）技術，可以連續培養只分泌單一專一性抗體的細胞（Köhler & Milstein, 1975） | 單株抗體藥物的技術基礎 |
| 1984–1992 | 嵌合抗體：鼠的可變區接上人的恆定區（Morrison et al., 1984）；人源化的抗 HER2 抗體（Carter et al., 1992） | 解決鼠抗體會引發人抗鼠抗體反應、又缺乏作用功能的問題 |
| 1987 | Slamon：189 例乳癌中約 30% 有 HER2 基因擴增，而且和復發、存活較差有關（Slamon et al., 1987） | HER2 從預後因子變成治療標的 |
| 1998 | Hirota：胃腸道基質瘤（gastrointestinal stromal tumor, GIST）帶有 KIT 的功能獲得性突變（Hirota et al., 1998） | 為 imatinib 用在 GIST 鋪路 |
| 2000 | 第一個抗體藥物複合體（antibody-drug conjugate, ADC）gemtuzumab ozogamicin 在美國核准，2010 年下市，2017 年重新核准（Drago et al., 2021） | 早期 ADC 的教訓：連接子不夠穩定，載藥在血中提早釋出就變成毒性 |
| 2001 | Imatinib 第一期試驗：每日 300 mg 以上的 CML 病人，54 人中 53 人達到血液學完全緩解（Druker et al., 2001）；trastuzumab 加化療延長 HER2 過度表現的轉移性乳癌病人的存活（Slamon et al., 2001） | 小分子與抗體兩條路在同一年成功 |
| 2002 | Imatinib 用於晚期 GIST：147 人中 53.7% 部分反應（Demetri et al., 2002） | 同一顆藥用在不同癌別，靠的是同一類靶點 |
| 2003 | Gefitinib 在美國取得加速核准，依據的反應率只有 10.6%（Cohen et al., 2003） | 當時還不知道誰會有效 |
| 2004 | Lynch 與 Paez 兩個團隊同時發現：對 gefitinib 有反應的肺癌帶有 EGFR 活化突變（Lynch et al., 2004；Paez et al., 2004）；bevacizumab 加化療延長轉移性大腸直腸癌的存活（Hurwitz et al., 2004） | 「先驗基因再用藥」的開始；抗血管新生藥有了第 3 期的存活證據 |
| 2005 | EGFR T790M 抗藥突變（Kobayashi et al., 2005）；BRCA 缺陷的細胞對 PARP 抑制劑特別敏感（Bryant et al., 2005；Farmer et al., 2005） | 抗藥性研究與「合成致死」的起點 |
| 2007 | Soda：非小細胞肺癌（non-small cell lung cancer, NSCLC）的 EML4-ALK 融合基因，75 例中 5 例（6.7%）（Soda et al., 2007） | 新的可標靶族群 |
| 2009 | IPASS：EGFR 突變陽性者 gefitinib 優於化療，陰性者反而較差（Mok et al., 2009） | biomarker 決定用藥成為標準 |
| 2010–2011 | Crizotinib 在 ALK 陽性 NSCLC 的反應率 57%（Kwak et al., 2010）；2011 年 8 月 26 日美國加速核准（Kazandjian et al., 2014） | 從發現靶點到核准只有 4 年 |
| 2012 | Trastuzumab emtansine（T-DM1）優於 lapatinib ＋ capecitabine（Verma et al., 2012） | ADC 在實體腫瘤站穩 |
| 2013 | Ostrem：KRAS G12C 的 switch-II 口袋（Ostrem et al., 2013） | 被認為「不可成藥」的 KRAS 有了下手處 |
| 2016–2017 | Palbociclib 加 letrozole（Finn et al., 2016）；osimertinib 用於 T790M（Mok et al., 2017）；olaparib 用於 germline BRCA 乳癌（Robson et al., 2017） | CDK4/6、第三代 EGFR TKI、PARP 抑制劑進入常規 |
| 2018 | Larotrectinib：55 位病人、17 種腫瘤，反應率 75%（Drilon et al., 2018）；同年 11 月在美國核准（Scott, 2019） | 依基因、不依器官的跨癌別（tumour-agnostic）適應症 |
| 2021 | Sotorasib 於 5 月 28 日在美國取得加速核准（Nakajima et al., 2022） | 第一個 KRAS G12C 標靶藥 |

### 1.1 費城染色體 → imatinib → GIST

CML 的細胞帶著一條變短的 22 號染色體。Nowell 回憶，Hungerford 先在兩位病人身上看到，後來分析的 7 位病人全都有（Nowell, 2007）。這條染色體來自 9 號與 22 號染色體的易位，產生的 BCR-ABL 融合蛋白是一個關不掉的酪胺酸激酶（tyrosine kinase）（Nowell, 2007；Druker et al., 2001）。Druker 的第一期試驗讓 83 位干擾素治療失敗的慢性期病人口服 STI571（imatinib），每日 300 mg 以上的 54 人中有 53 人達到血液學完全緩解，副作用以噁心、肌痛、水腫、腹瀉為主（Druker et al., 2001）。美國 FDA 在 2001 年 5 月 10 日以加速核准的方式核准 imatinib 用於 CML（急性轉化期、加速期，或干擾素治療失敗的慢性期）（Food and Drug Administration, 2001；Dagher et al., 2002）。

同一顆藥也抑制 KIT。GIST 帶有讓 KIT 持續活化的突變（Hirota et al., 1998），而傳統化療對 GIST 無效；147 位晚期 GIST 病人用 imatinib 後，53.7% 部分反應、27.9% 疾病穩定（Demetri et al., 2002）。美國依這個試驗，在 2002 年 2 月 1 日核准 KIT 陽性、無法切除或轉移性 GIST 的適應症（Food and Drug Administration, 2002；Dagher et al., 2002）。

**和今天的關係：** GIST 用藥前要先有基因型，因為 KIT exon 11、exon 9 與 PDGFRA D842V 對 imatinib 的反應不同（第 7 段），選藥流程見[肉瘤章 4.5](../04-sarcoma.md#45-gist)。

### 1.2 融合瘤 → 人源化抗體 → trastuzumab

融合瘤技術讓實驗室可以大量製造同一種抗體（Köhler & Milstein, 1975），但鼠抗體打進人體會引發人抗鼠抗體反應，也缺乏啟動人體免疫細胞的功能（Carter et al., 1992）。解法分兩步：先把鼠的可變區接上人的恆定區做成嵌合抗體（Morrison et al., 1984），再進一步只保留鼠抗體的抗原結合環，其餘換成人的序列，稱為人源化。Carter 等人源化的正是抗 HER2 抗體（Carter et al., 1992），臨床使用的 trastuzumab 就是人源化的抗 HER2 抗體（Clynes et al., 2000）。

靶點來自 Slamon 的觀察：約 30% 的乳癌有 HER2 擴增，而且預後差（Slamon et al., 1987）。關鍵試驗把 469 位 HER2 過度表現的轉移性乳癌病人隨機分成化療或化療加 trastuzumab：疾病惡化時間 7.4 對 4.6 個月，中位存活 25.1 對 20.3 個月。同一篇也報告了代價：NYHA 第 III–IV 級心臟功能不全在 anthracycline ＋ cyclophosphamide ＋ trastuzumab 組為 27%，單用 anthracycline ＋ cyclophosphamide 為 8%；paclitaxel ＋ trastuzumab 為 13%，單用 paclitaxel 為 1%（Slamon et al., 2001）。

**和今天的關係：** 這就是為什麼 (1) 要先確認 HER2 陽性才用抗 HER2 藥；(2) 抗 HER2 治療要定期測左心室射出率（left ventricular ejection fraction, LVEF），而且和 anthracycline 併用時風險最高（Seidman et al., 2002；Genentech, 2026）。

### 1.3 血管新生 → bevacizumab

Folkman 在 1971 年提出，腫瘤要長大必須長出新血管，阻斷血管新生可以當成治療（Folkman, 1971）。三十多年後，抗血管內皮生長因子（vascular endothelial growth factor, VEGF）的單株抗體 bevacizumab 在 813 位轉移性大腸直腸癌病人的試驗中，把中位存活從 15.6 個月延長到 20.3 個月（死亡 HR 0.66），3 級高血壓 11.0% 對 2.3%（Hurwitz et al., 2004）。肺癌的 ECOG 4599 試驗一開始就排除鱗狀細胞癌、腦轉移與明顯咳血的病人；加 bevacizumab 後中位存活 12.3 對 10.3 個月，但臨床上明顯的出血 4.4% 對 0.7%，15 例治療相關死亡中有 5 例是肺出血（Sandler et al., 2006）。

**和今天的關係：** bevacizumab 只用在非鱗狀 NSCLC；每次給藥前量血壓、驗尿蛋白、問咳血與近期手術（見 6.4）。

### 1.4 EGFR：先核准，後來才知道誰有效

Gefitinib 在 2003 年 5 月 5 日取得美國加速核准時，依據是化療失敗病人 10.6% 的反應率，只觀察到女性與不吸菸者反應較多（Cohen et al., 2003）。隔年，Lynch 的團隊在 9 位對 gefitinib 有反應的病人中找到 8 位帶有 EGFR 酪胺酸激酶區的突變，7 位無反應者都沒有；突變集中在 ATP 結合口袋附近（Lynch et al., 2004）。Paez 的團隊同時發現這類突變在日本的檢體是 58 例中 15 例，在美國只有 61 例中 1 例（Paez et al., 2004）。不挑病人的 ISEL 試驗則顯示，gefitinib 對整體族群的存活沒有顯著好處（5.6 對 5.1 個月，HR 0.89），只有不吸菸者與亞洲裔受益（Thatcher et al., 2005）。

IPASS 把答案定下來：東亞、不吸菸或輕度吸菸的肺腺癌病人中，EGFR 突變陽性者用 gefitinib 的惡化風險 HR 0.48，陰性者 HR 2.85（Mok et al., 2009）。台灣 1,772 位未治療肺腺癌的研究中，55.7% 帶 EGFR 突變（Hsu et al., 2015），所以台灣肺腺癌病人幾乎都要先等這份報告。

抗藥的故事也從這裡開始：一位 gefitinib 完全緩解兩年後復發的病人，腫瘤多了第二個突變 T790M（Kobayashi et al., 2005）。針對它設計的 osimertinib 對敏感突變與 T790M 都有選擇性，在 T790M 陽性病人的無惡化存活期（progression-free survival, PFS）為 10.1 對 4.4 個月（Mok et al., 2017），之後又前移到第一線（Soria et al., 2018）。

### 1.5 ALK、NTRK、KRAS：越來越快，也越來越「不看器官」

- **ALK**：2007 年發現 EML4-ALK 融合（Soda et al., 2007）。研究團隊篩了約 1,500 位 NSCLC 病人，找到 82 位 ALK 陽性者給 crizotinib，反應率 57%（Kwak et al., 2010），2011 年 8 月即取得美國加速核准（Kazandjian et al., 2014）。之後是更具選擇性的 alectinib（Peters et al., 2017）與第三代的 lorlatinib（Shaw et al., 2020）。
- **NTRK**：larotrectinib 的試驗不分器官，只收帶 TRK 融合的腫瘤，病人年齡從 4 個月到 76 歲、涵蓋 17 種腫瘤，反應率 75%（Drilon et al., 2018）。它在 2018 年 11 月取得美國核准，適應症寫的是基因變異而不是器官（Scott, 2019）。
- **KRAS**：KRAS 是人類癌症最常見的活化突變，但它和 GTP 的結合力極強，表面又找不到可以卡藥的位置，長期被認為無法直接抑制。Ostrem 等人利用 G12C 突變多出來的半胱胺酸，做出只和突變蛋白共價結合的小分子，並在結晶結構中發現一個先前看不到的口袋，位於 switch-II 區下方（Ostrem et al., 2013）。八年後 sotorasib 以 36% 的反應率取得美國加速核准（Nakajima et al., 2022）。

### 1.6 BRCA 與合成致死；細胞週期與 CDK4/6

2005 年同一期 *Nature* 的兩篇論文指出：BRCA1 或 BRCA2 功能缺失的細胞無法用同源重組修復 DNA，一旦再抑制 PARP，DNA 損傷就累積到細胞死亡；正常細胞還有同源重組可用，受的影響小（Bryant et al., 2005；Farmer et al., 2005）。這個「兩個缺陷加在一起才致命」的現象稱為合成致死（synthetic lethality），後來成為 olaparib 用於 germline BRCA 乳癌（Robson et al., 2017）與胰臟癌維持治療（Golan et al., 2019）的依據。這也是為什麼開 PARP 抑制劑前要有 germline BRCA 報告。

CDK4/6 抑制劑的病人選擇則來自細胞株實驗：47 株乳癌細胞中，管腔型、雌激素受體陽性的細胞對 PD 0332991（palbociclib）最敏感，基底型最不敏感（Finn et al., 2009）。臨床試驗因此直接鎖定荷爾蒙受體陽性乳癌（Finn et al., 2016）。

### 1.7 ADC：從 gemtuzumab ozogamicin 到 T-DXd

最早核准的 ADC 是把 calicheamicin 接在抗 CD33 抗體上的 gemtuzumab ozogamicin：2000 年成為美國核准的第一個 ADC，2010 年下市，2017 年才重新核准；它的 hydrazone 連接子在生理 pH 下就會部分水解，被認為和脫靶毒性有關（Drago et al., 2021）。實體腫瘤的突破是 T-DM1：trastuzumab 用穩定的連接子接上微管抑制劑 DM1，在曾用過 trastuzumab 與 taxane 的 HER2 陽性乳癌，PFS 9.6 對 6.4 個月、整體存活期（overall survival, OS）30.9 對 25.1 個月（Verma et al., 2012）。下一代的 trastuzumab deruxtecan（T-DXd）換成可被溶酶體酵素切斷的胜肽連接子與拓樸異構酶 I 抑制劑，每個抗體接約 7–8 個藥物分子，釋出的藥物能穿過細胞膜、殺死旁邊 HER2 陰性的細胞（Ogitani et al., 2016）。它在頭對頭試驗中勝過 T-DM1（Hurvitz et al., 2023），並把適應症擴大到 HER2 低表現的乳癌（Modi et al., 2022）。

---

## 2. 作用機轉

**結論先講：** 標靶藥有效，是因為某些腫瘤把生存押在單一條訊號路上，這叫致癌基因成癮（oncogene addiction）（Weinstein, 2002）。藥物分三種打法：小分子進到細胞裡塞住激酶；抗體在細胞外擋住受體；ADC 則用抗體把化療藥送進細胞。

### 2.1 致癌基因成癮

Weinstein 在 2002 年提出：癌細胞雖然累積很多基因異常，卻常常只依賴其中一個致癌基因維持生長，把它關掉，細胞就停止生長或死亡（Weinstein, 2002）。CML 的 BCR-ABL、GIST 的 KIT、肺腺癌的 EGFR 突變都是例子：只抑制一個激酶，就得到很高的反應率（Druker et al., 2001；Demetri et al., 2002；Mok et al., 2009）。

> [!TIP]
> **只靠一根柱子撐著的房子**
> 正常細胞像有很多根柱子的房子，抽掉一根不會倒。帶驅動基因的癌細胞把重量都壓在同一根柱子上（例如突變的 EGFR），標靶藥抽掉這一根，房子就垮了；正常細胞不靠這根柱子，所以受的傷少。反過來說，如果腫瘤根本沒有這根柱子（biomarker 陰性），藥再貴也抽不到東西。

### 2.2 一條訊號路：從受體到細胞核

受體酪胺酸激酶（receptor tyrosine kinase, RTK）的共同流程是：生長因子（配體）結合受體 → 受體兩兩配對 → 細胞內的激酶區被活化並磷酸化 → 訊號往下游傳遞（Lemmon & Schlessinger, 2010）。臨床上要記兩條下游路徑：

| 位置 | 分子 | 作用在這裡的藥 |
|------|------|--------------|
| 細胞外的配體 | VEGF | bevacizumab（Hurwitz et al., 2004） |
| 細胞膜上的受體 | EGFR、HER2、ALK、ROS1、RET、MET、TRK、KIT、PDGFRA、VEGFR2 | 抗體（trastuzumab、cetuximab、amivantamab、ramucirumab）與各種 TKI |
| 下游路徑一 | RAS → RAF → MEK → ERK | sotorasib（KRAS G12C；de Langen et al., 2023）、dabrafenib（BRAF）＋ trametinib（MEK）（Planchard et al., 2017） |
| 下游路徑二 | PI3K → AKT → mTOR | alpelisib、inavolisib（PI3Kα）、capivasertib（AKT）、everolimus（mTOR）（André et al., 2019；Turner et al., 2024；Turner et al., 2023；Baselga et al., 2012） |
| 細胞週期 | cyclin D–CDK4/6 → Rb 磷酸化 → 進入 S 期 | palbociclib、ribociclib、abemaciclib（Finn et al., 2009） |
| DNA 修復 | PARP | olaparib、talazoparib（Farmer et al., 2005） |

> [!TIP]
> **訊號像接力賽**
> 配體把棒子交給受體，受體交給 RAS，一路傳到細胞核，細胞才開始分裂。突變就像某一棒的選手不等接棒就自己起跑。藥要擋在「搶跑的那一棒」或它的下游才有用：EGFR 突變擋 EGFR 有效；但如果搶跑的是下游的 KRAS，去擋上游的 EGFR 就沒有用。這正是 KRAS 突變的大腸直腸癌用 cetuximab 無效的原因（Karapetis et al., 2008）。

### 2.3 小分子與單株抗體

| 比較 | 小分子激酶抑制劑（字尾 -nib） | 單株抗體（字尾 -mab） |
|------|---------------------------|-------------------|
| 作用位置 | 進入細胞，作用在激酶區；對 gefitinib 敏感的 EGFR 突變就集中在 ATP 結合口袋周圍（Lynch et al., 2004；Imai & Takaoka, 2006） | 留在細胞外，結合配體或受體的胞外區（Imai & Takaoka, 2006） |
| 給藥途徑 | 口服 | 靜脈或皮下；分子太大又會被胃酸分解，不能口服（Keizer et al., 2010） |
| 半衰期 | 多數以小時計，每天吃 | 長，可達約 4 週，所以 2–4 週打一次（Keizer et al., 2010） |
| 代謝 | 多經 CYP3A4，交互作用多；吸收受胃酸與食物影響（van Leeuwen et al., 2014） | 在體內被分解成胜肽與胺基酸，代謝性交互作用少見（Keizer et al., 2010） |
| 額外的殺傷方式 | 無 | 抗體的 Fc 端可以招來免疫細胞，稱為抗體依賴性細胞毒殺（antibody-dependent cellular cytotoxicity, ADCC）（Clynes et al., 2000） |
| 典型問題 | 漏服、交互作用、腹瀉、皮疹、QT | 輸注反應 |

> [!TIP]
> **鑰匙孔和門口的路障**
> 激酶像一台要插鑰匙（ATP）才會發動的機器。小分子藥是一把斷在鑰匙孔裡的假鑰匙，要進到細胞裡面才塞得到，所以做成小小的口服藥。抗體是又大又重的路障，進不了細胞，只能擋在門外的受體上，還會順便招來免疫細胞（ADCC）；因為體積大，只能用打的，但也因此在血中停留很久。

### 2.4 ADC 的構造

ADC 由三個零件組成，三個都影響療效與毒性（Drago et al., 2021）：

| 零件 | 功能 | 臨床意義 |
|------|------|---------|
| 抗體 | 認出腫瘤表面的抗原（HER2、Trop-2） | 決定藥送到哪裡 |
| 連接子（linker） | 把藥綁在抗體上；分可切斷與不可切斷兩類 | 可切斷的連接子在腫瘤環境或細胞內被酵素、酸性或還原環境切開 |
| 載藥（payload） | 真正殺細胞的藥；效力強到不適合直接全身給藥，所以才要靠抗體運送 | 毒性類型跟著載藥走：DM1 是微管抑制劑（Verma et al., 2012），DXd 與 SN-38 是拓樸異構酶 I 抑制劑（Ogitani et al., 2016；Bardia et al., 2021） |
| 藥物抗體比（drug-to-antibody ratio, DAR） | 每個抗體平均帶幾個載藥分子 | 比值高不一定好：動物實驗中 DAR 8 的 ADC 清除較快、毒性較高（Drago et al., 2021） |

**旁觀者效應（bystander effect）**：載藥釋出後如果能穿過細胞膜，就會擴散到旁邊抗原陰性的癌細胞。T-DXd 的載藥穿膜能力高，在混合培養中能同時殺死 HER2 陽性與陰性細胞；T-DM1 釋出的 Lys-SMCC-DM1 穿膜能力低，沒有這個效果（Ogitani et al., 2016）。這可以解釋 T-DXd 為什麼對 HER2 低表現的腫瘤也有效（Modi et al., 2022）。

> [!TIP]
> **特洛伊木馬**
> ADC 像一匹木馬：抗體是木馬的外殼，負責讓城門（腫瘤細胞表面的抗原）打開；連接子是綁住士兵的繩子；載藥是藏在裡面的士兵。進城之後繩子被切斷，士兵才出來。繩子太鬆，士兵在城外就跑出來，傷到正常組織；士兵如果還能翻牆到隔壁（旁觀者效應），連沒有開門的鄰居也一起被攻下。所以 ADC 的副作用看起來像化療（血球低下、噁心、掉髮），不像單純的抗體。

### 2.5 為什麼驗完 biomarker 才能開處方

- **沒有靶，藥不只無效，還可能有害。** IPASS 中 EGFR 突變陰性者用 gefitinib 的惡化風險是化療的 2.85 倍（Mok et al., 2009）。
- **有些 biomarker 是用來排除病人的。** 大腸直腸癌 KRAS 突變者用 cetuximab 沒有存活好處（HR 0.98），野生型才有（HR 0.55）（Karapetis et al., 2008）。
- **同一個基因，不同突變用不同藥。** GIST 的 KIT exon 11 對 imatinib 的部分反應率 83.5%，exon 9 為 47.8%，沒有突變者為 0%（Heinrich et al., 2003）。
- **順序錯了會出事。** 見下方警示。

> [!WARNING]
> **基因報告出來之前，不要先打免疫治療**
> 先用 PD-1／PD-L1 抑制劑、之後才接 osimertinib 的病人，15%（41 人中 6 人）發生嚴重免疫相關不良事件；3 個月內接上的更高達 24%（21 人中 5 人）。反過來先用 osimertinib 再用免疫治療的 29 人，則沒有人發生（Schoenfeld et al., 2019）。晚期非鱗狀 NSCLC 寧可多等幾天基因報告，細節見[肺癌章 2.2](../01-lung-cancer.md#22-必驗-biomarker)。

> [!IMPORTANT]
> **biomarker 的三種角色**
> - **選進來**：EGFR 突變、ALK 融合、HER2 陽性、germline BRCA、PIK3CA 突變、NTRK 融合。
> - **排除掉**：KRAS 突變之於 cetuximab；鱗狀細胞癌之於 bevacizumab（這是組織型，不是基因）。
> - **惡化時再驗一次**：T790M、MET 放大、小細胞轉化、KIT 次發突變（第 7 段）。考題常問「下一步是什麼」，答案多半是「先再切片或驗血中腫瘤 DNA」，不是直接換藥。

---

## 3. 分類與代表藥

**結論先講：** 記每一類藥要記四件事：打哪個靶、用哪個 biomarker 選病人、最有代表性的毒性、在哪個癌別用。下面依靶點分節；劑量與減量規則都在各癌別章，這裡只放連結。

### 3.1 EGFR

| 藥物 | 特性 | 選病人的 biomarker | 代表性毒性 | 本手冊用在哪 |
|------|------|------------------|-----------|-------------|
| gefitinib、erlotinib（第一代） | FLAURA 把這兩個藥當成標準 EGFR TKI 對照組（Soria et al., 2018）；gefitinib 是可逆的抑制劑（Wu et al., 2017） | EGFR 敏感突變（exon 19 缺失、L858R） | IPASS 的 gefitinib 組：皮疹或痤瘡 66.2%、腹瀉 46.6%（Mok et al., 2009） | [肺癌章 4.3](../01-lung-cancer.md#43-nsclc-iv-期)；erlotinib 在胰臟癌效益極小，見[胰臟癌章 5.4](../02-pancreatic-cancer.md#54-口服與維持用藥s-1capecitabineolaparib以及不建議的-erlotinib) |
| afatinib（第二代） | 不可逆地阻斷 EGFR、HER2、ErbB4 的訊號（Sequist et al., 2013） | 同上 | 腹瀉、皮疹或痤瘡、口腔炎（Sequist et al., 2013） | 肺癌章 4.3 |
| dacomitinib（第二代） | 不可逆的 EGFR TKI（Wu et al., 2017） | 同上 | 3–4 級痤瘡樣皮膚炎 14%、腹瀉 8%（Wu et al., 2017） | 肺癌章 4.3 |
| osimertinib（第三代） | 不可逆，對敏感突變與 T790M 都有選擇性（Soria et al., 2018） | 敏感突變；或第一、二代後出現 T790M | ILD 約 4%（致死 0.4%）、QTc >500 ms 約 1.1%、心肌病變 3.8%（美國仿單；AstraZeneca, 2026） | 肺癌章 4.1–4.3、[6.1](../01-lung-cancer.md#61-egfr-tki) |
| cetuximab（抗體） | 抗 EGFR 單株抗體 | KRAS 野生型的大腸直腸癌（Karapetis et al., 2008） | 輸注反應；皮膚毒性是 EGFR 抑制劑的類別效應（Lacouture et al., 2011） | 本手冊四個癌別不用；輸注反應見[急症章第 10 節](../00-shared/02-oncologic-emergencies.md#10-輸注反應過敏反應與過敏性休克) |
| amivantamab（抗體） | EGFR 與 MET 的雙特異性抗體，結合胞外區，繞過 TKI 結合位置的抗藥（Park et al., 2021） | EGFR exon 20 插入；或與 lazertinib 併用於敏感突變 | CHRYSALIS：皮疹 86%、輸注反應 66%、甲溝炎 45%（Park et al., 2021） | [肺癌章 6.4](../01-lung-cancer.md#64-amivantamab-lazertinib) |

三代的差別可以這樣記：第一代是原型；第二代改成「不可逆、打得廣」，皮膚與腸胃毒性較重（dacomitinib 的 3–4 級痤瘡樣皮膚炎 14%，對照的 gefitinib 為 0；Wu et al., 2017）；第三代「不可逆、專打突變型（含 T790M）」，3 級以上不良事件比第一代少（34% 對 45%；Soria et al., 2018），但要注意肺、心電圖與心臟。各藥的皮膚與腹瀉處置依仿單不同，見肺癌章 6.1。

### 3.2 其他驅動基因：ALK、ROS1、RET、MET、NTRK、BRAF／MEK、KRAS G12C

| 靶點 | 代表藥 | 選病人的 biomarker | 代表性毒性 | 本手冊用在哪 |
|------|--------|------------------|-----------|-------------|
| ALK | crizotinib（第一代）、alectinib、lorlatinib（第三代，可進入腦部；Solomon et al., 2018） | ALK 融合 | crizotinib：視覺異常、腸胃症狀、水腫、轉胺酶上升，另有肝毒性、ILD、QT 延長（Kazandjian et al., 2014）。alectinib：肌痛 35.3%、CPK 上升 56.2%、心搏過緩 11.3%（歐盟產品資訊；European Medicines Agency, 2025）。lorlatinib：3–4 級膽固醇上升 18%、三酸甘油酯上升 19%、中樞神經作用 52%（美國仿單；Pfizer, 2026） | [肺癌章 4.3](../01-lung-cancer.md#43-nsclc-iv-期)、[6.2](../01-lung-cancer.md#62-alkros1-tki) |
| ROS1 | crizotinib 等（Shaw et al., 2014） | ROS1 融合 | 同 crizotinib | 肺癌章 4.3 |
| RET | selpercatinib | RET 融合 | 3 級以上高血壓 14%、ALT 上升 12%、AST 上升 10%（Drilon et al., 2020） | [肺癌章 6.3](../01-lung-cancer.md#63-其他標靶藥) |
| MET | capmatinib、tepotinib | MET exon 14 跳躍突變 | 周邊水腫（capmatinib 51%）、噁心（Wolf et al., 2020；Paik et al., 2020） | 肺癌章 6.3 |
| TRK | larotrectinib | NTRK1–3 融合，不分癌別 | 多為 1 級；沒有任何一種 3–4 級藥物相關事件超過 5%（Drilon et al., 2018） | 肺癌章 4.3、[胰臟癌章 4.10](../02-pancreatic-cancer.md#410-生物標記導向治療與-kras-標靶)、[肉瘤章 5.4](../04-sarcoma.md#54-gist非脂肪細胞型-sts-與-ntrk-融合口服標靶藥) |
| BRAF ＋ MEK | dabrafenib ＋ trametinib | BRAF V600E | 發燒是最常見的 3–4 級事件之一（11%）（Planchard et al., 2017） | 肺癌章 6.3 |
| KRAS G12C | sotorasib | KRAS G12C | 腹瀉、ALT 與 AST 上升（de Langen et al., 2023）；肝毒性（Nakajima et al., 2022） | 肺癌章 4.3、胰臟癌章 4.10 |

Sotorasib 是專一、不可逆的 KRAS G12C 抑制劑（de Langen et al., 2023），只對 G12C 這一種突變有效。G12C 只占胰臟癌的 1–2%（Strickler et al., 2023），所以胰臟癌要靠不挑 G12 突變型別的新一代 RAS 抑制劑（見第 5、7 段）。

### 3.3 HER2

| 藥物 | 類型與特性 | 選病人的 biomarker | 代表性毒性 | 本手冊用在哪 |
|------|-----------|------------------|-----------|-------------|
| trastuzumab | 人源化抗 HER2 單株抗體；動物模型顯示療效有一部分來自 Fc 受體媒介的 ADCC（Clynes et al., 2000） | HER2 陽性（判讀見[乳癌章 2.3](../03-breast-cancer.md#23-her2-判讀)） | 加框警語：心肌病變、輸注反應、胚胎胎兒毒性、肺毒性（美國仿單；Genentech, 2026） | [乳癌章 4.5](../03-breast-cancer.md#45-早期-her2-陽性抗-her2-治療的階梯)、[4.8](../03-breast-cancer.md#48-轉移性-her2-陽性從-thp-到-adc再到-tucatinib) |
| pertuzumab | 人源化抗 HER2 單株抗體，結合的 HER2 位置與 trastuzumab 不同，兩者合用阻斷更完整（雙標靶）（Swain et al., 2015） | HER2 陽性 | 與 trastuzumab、docetaxel 併用時，多數不良事件發生在 docetaxel 期間，長期心臟安全性維持（Swain et al., 2015） | 乳癌章 4.5、4.8 |
| lapatinib | HER2 與 EGFR 的小分子 TKI（Geyer et al., 2006） | HER2 陽性 | 與 capecitabine 併用時腹瀉、噁心嘔吐、手足症候群比 T-DM1 多（Verma et al., 2012）；吸收受食物影響極大（第 4 段） | 乳癌章 4.8 |
| neratinib | 不可逆的 HER1、HER2、HER4 抑制劑（Chan et al., 2016） | HER2 陽性早期乳癌的延長輔助治療 | **3 級腹瀉 40%**（Chan et al., 2016） | 乳癌章 4.5 |
| tucatinib | 高選擇性的 HER2 TKI（Murthy et al., 2020） | HER2 陽性，含腦轉移 | 腹瀉、手足症候群、轉胺酶上升（Murthy et al., 2020） | 乳癌章 4.8 |
| trastuzumab emtansine（T-DM1） | ADC：穩定連接子 ＋ 微管抑制劑 DM1（Verma et al., 2012） | HER2 陽性 | 血小板低下、轉胺酶上升（Verma et al., 2012） | 乳癌章 4.5、[6.7](../03-breast-cancer.md#67-抗體藥物複合體t-dxdt-dm1sacituzumab-govitecandato-dxd) |
| trastuzumab deruxtecan（T-DXd） | ADC：可切斷連接子 ＋ 拓樸異構酶 I 抑制劑，DAR 約 7–8（Ogitani et al., 2016） | HER2 陽性或低表現的乳癌（Modi et al., 2022）；HER2 突變的 NSCLC（Goto et al., 2023） | 加框警語：**ILD** 與胚胎胎兒毒性；5.4 mg/kg 時 ILD 12%、致死 0.9%；高致吐（美國仿單；Daiichi Sankyo, 2026） | 乳癌章 4.8、6.7；[肺癌章 6.3](../01-lung-cancer.md#63-其他標靶藥) |

> [!WARNING]
> **三個「trastuzumab」不能互換**
> Trastuzumab（Herceptin）、trastuzumab emtansine（Kadcyla）、trastuzumab deruxtecan（Enhertu）名字很像，劑量與毒性完全不同。美國仿單明文寫：不可用 trastuzumab 替代 T-DM1 或 T-DXd，反之亦然（Genentech, 2026）。醫囑、調劑、給藥三個關卡都要核對完整學名。

### 3.4 VEGF／VEGFR 與多激酶 TKI

| 藥物 | 類型與靶點 | 選病人的依據 | 代表性毒性 | 本手冊用在哪 |
|------|-----------|-------------|-----------|-------------|
| bevacizumab | 抗 VEGF 單株抗體（Hurwitz et al., 2004） | 沒有預測性 biomarker；肺癌限非鱗狀（Sandler et al., 2006） | 高血壓、蛋白尿、出血、胃腸穿孔、傷口癒合不良、動脈血栓、PRES（美國仿單；Genentech, 2025） | [肺癌章 6.8](../01-lung-cancer.md#68-抗血管新生藥物bevacizumab-與-ramucirumab) |
| ramucirumab | 抗 VEGFR-2 的人類 IgG1 單株抗體（Garon et al., 2014） | 無 | REVEL：3 級以上高血壓 6% 對 2%；與 docetaxel 併用時發燒性嗜中性球低下 16% 對 10%（Garon et al., 2014） | 肺癌章 6.8 |
| imatinib | BCR-ABL、KIT 的 TKI（Druker et al., 2001；Demetri et al., 2002） | GIST 的 KIT／PDGFRA 基因型 | 水腫、腹瀉、疲倦；約 5% 發生胃腸道或腹腔內出血（Demetri et al., 2002） | [肉瘤章 4.5](../04-sarcoma.md#45-gist)、[6.8](../04-sarcoma.md#68-gist-的-tkiimatinibsunitinibregorafenibripretinibavapritinib) |
| sunitinib | 多靶點 TKI（Demetri et al., 2006） | imatinib 失敗或不耐受的 GIST | 疲倦、腹瀉、皮膚變色、噁心（Demetri et al., 2006） | 肉瘤章 4.5.3、6.8 |
| regorafenib | 口服激酶抑制劑（Demetri et al., 2013） | imatinib 與 sunitinib 都失敗的 GIST | 3 級以上高血壓 23%、手足皮膚反應 20%（Demetri et al., 2013）；加框警語：肝毒性；亞洲病人手足皮膚反應 72%（美國仿單；Bayer, 2026） | 肉瘤章 4.5.3、6.8 |
| ripretinib | 「開關控制」型 TKI，把激酶的活化環鎖在不活化的構形，涵蓋多種 KIT 與 PDGFRA 突變（Smith et al., 2019） | 多線治療後的晚期 GIST（線別見肉瘤章 4.5.3） | 3–4 級事件以 lipase 上升 5%、高血壓 4% 為主（Blay et al., 2020） | 肉瘤章 4.5.3、6.8 |
| avapritinib | KIT 與 PDGFRA 的 TKI，能強力抑制 PDGFRA D842V（Heinrich et al., 2020） | PDGFRA D842V 的 GIST（Heinrich et al., 2020） | 顱內出血 2.9%（GIST 與進階性全身性肥大細胞增生症合併的 749 人；其中 GIST 病人 267 人為 1.1%）；認知不良反應在 GIST 病人為 41%（601 人），連同肥大細胞增生症合併的 995 人為 33%（美國仿單；Blueprint Medicines, 2026） | 肉瘤章 4.5.3、6.8 |
| pazopanib | 多靶點 TKI（van der Graaf et al., 2012） | 化療後的晚期軟組織肉瘤 | 加框警語：肝毒性（美國仿單；Novartis, 2025）；疲倦、腹瀉、噁心、體重下降（van der Graaf et al., 2012） | [肉瘤章 4.4.3](../04-sarcoma.md#443-後線與寡轉移)、[6.7](../04-sarcoma.md#67-pazopanib肝毒性與高血壓) |

抗 VEGF 抗體沒有可以拿來選病人的基因檢測，所以「誰不能用」比「誰能用」重要：鱗狀細胞肺癌、近期咳血、未癒合的傷口、未控制的高血壓，都要先排除（見 6.4）。

### 3.5 CDK4/6 抑制劑

| 藥物 | 給法的特點 | 代表性毒性 | 本手冊用在哪 |
|------|-----------|-----------|-------------|
| palbociclib | 服 3 週停 1 週（劑量見[乳癌章 5.5](../03-breast-cancer.md#55-內分泌治療與-cdk46-抑制劑)） | 3–4 級嗜中性球低下 66.4%（Finn et al., 2016） | [乳癌章 4.7](../03-breast-cancer.md#47-轉移性-hrher2先排除-visceral-crisis再走內分泌路線)、[6.5](../03-breast-cancer.md#65-cdk46-抑制劑嗜中性球肝功能心電圖腹瀉) |
| ribociclib | 服 3 週停 1 週；轉移性 600 mg、早期 400 mg（美國仿單；Novartis, 2026） | QT 延長、肝毒性、嗜中性球低下、ILD、嚴重皮膚反應（美國仿單；Novartis, 2026） | 乳癌章 4.4、4.7、6.5 |
| abemaciclib | 每日兩次、連續服用（Goetz et al., 2017） | 腹瀉 81.3%（多為 1 級）；3–4 級嗜中性球低下 21.1%（Goetz et al., 2017） | 乳癌章 4.4、4.7、6.5 |

三個藥都用於荷爾蒙受體陽性、HER2 陰性乳癌；本章列出的試驗都是和內分泌治療併用（abemaciclib 另有單用的研究；Goetz et al., 2017）。內分泌藥本身見[內分泌治療](05-endocrine-therapy.md)。

### 3.6 PI3K／AKT／mTOR 抑制劑

| 藥物 | 靶點 | 選病人的 biomarker | 代表性毒性 | 本手冊用在哪 |
|------|------|------------------|-----------|-------------|
| alpelisib | PI3Kα（André et al., 2019） | PIK3CA 突變 | 3–4 級高血糖 36.6%、皮疹 9.9%（André et al., 2019） | [乳癌章 4.7](../03-breast-cancer.md#47-轉移性-hrher2先排除-visceral-crisis再走內分泌路線)、[6.6](../03-breast-cancer.md#66-pi3kaktmtor-抑制劑高血糖皮疹腹瀉口腔炎) |
| inavolisib | PI3Kα，並促進突變 p110α 降解（Turner et al., 2024） | PIK3CA 突變 | 3–4 級高血糖 5.6%、口腔炎或黏膜發炎 5.6%、腹瀉 3.7%（Turner et al., 2024） | 乳癌章 4.7、6.6 |
| capivasertib | AKT（Turner et al., 2023） | PIK3CA、AKT1 或 PTEN 變異 | 3 級以上皮疹 12.1%、腹瀉 9.3%（Turner et al., 2023） | 乳癌章 4.7、6.6 |
| everolimus | mTOR（Baselga et al., 2012） | 不需基因檢測 | 3–4 級口腔炎 8%、高血糖 4%、非感染性肺炎 3%（Baselga et al., 2012） | 乳癌章 4.7、6.6 |

PI3K 的 p110α 也負責細胞對胰島素的幾乎所有反應；抑制它，肝臟會分解肝醣、肌肉與脂肪無法攝取葡萄糖，幾小時內血糖就上升（Hopkins et al., 2018）。所以高血糖是「打中靶點才會有」的毒性（on-target toxicity），不是過敏或特異體質，原本就有胰島素阻抗的病人更明顯。

### 3.7 PARP 抑制劑

| 藥物 | 選病人的 biomarker | 代表性毒性 | 本手冊用在哪 |
|------|------------------|-----------|-------------|
| olaparib | germline BRCA1/2 | 最常見：噁心、疲倦、貧血、嘔吐、腹瀉；MDS／AML 累積發生率約 1.2%、肺炎 1.0%（美國仿單；AstraZeneca, 2025） | [乳癌章 4.10](../03-breast-cancer.md#410-gbrca-突變parp-抑制劑)；[胰臟癌章 4.9](../02-pancreatic-cancer.md#49-維持治療與二線以後) |
| talazoparib | germline BRCA1/2 | 3–4 級血液學事件 55%，以貧血為主（Litton et al., 2018） | 乳癌章 4.10 |

### 3.8 HER2 以外的 ADC

| 藥物 | 構造 | 選病人的依據 | 代表性毒性 | 本手冊用在哪 |
|------|------|-------------|-----------|-------------|
| sacituzumab govitecan | 抗 Trop-2 抗體 ＋ 可水解連接子 ＋ SN-38（拓樸異構酶 I 抑制劑）（Bardia et al., 2021） | 不需驗 Trop-2：存活好處不因 Trop-2 表現量而異（Rugo et al., 2023） | 3 級以上嗜中性球低下 51%、腹瀉 10%、發燒性嗜中性球低下 6%（Bardia et al., 2021） | [乳癌章 4.9](../03-breast-cancer.md#49-轉移性三陰性看-pd-l1看前線用藥)、[6.7](../03-breast-cancer.md#67-抗體藥物複合體t-dxdt-dm1sacituzumab-govitecandato-dxd) |
| datopotamab deruxtecan（Dato-DXd） | 人源化抗 Trop-2 抗體 ＋ 可切斷連接子 ＋ 拓樸異構酶 I 抑制劑載藥（Bardia et al., 2025） | 不需驗 Trop-2：TROPION-Breast01 收案時沒有用 Trop-2 表現量篩選病人（Bardia et al., 2025） | 口腔炎 50%、噁心 51.1%；眼表事件 40%（乾眼 21.7%），多為 1 級（Bardia et al., 2025） | 乳癌章 4.7、6.7；肺癌章 6.3 |

Sacituzumab govitecan 的嗜中性球低下與 UGT1A1 基因型的關係，見[化療基礎 12.2](../00-shared/01-chemo-basics.md#122-ugt1a1-與-irinotecansacituzumab-govitecan)。

### 3.9 骨骼標靶藥

Denosumab 是抗 RANKL 的單株抗體，用於骨轉移時延後骨骼相關事件（對 zoledronic acid 的 HR 0.82），低血鈣較多，顎骨壞死 2.0%（Stopeck et al., 2010）；用法與顎骨壞死的預防見[支持性照護第 8 節](../00-shared/03-supportive-care.md#8-骨轉移的骨骼保護劑bone-modifying-agents)，骨巨細胞瘤的用法見[肉瘤章 4.3](../04-sarcoma.md#43-軟骨肉瘤附骨巨細胞瘤-gctb)。

---

## 4. 藥物動力學與交互作用

**結論先講：** 口服 TKI 的變數在「吸收進去多少」與「被 CYP3A4 代謝多快」；抗體不經 CYP，重點是半衰期長、要打負載劑量（loading dose）、以及輸注反應。專師最容易攔到的處方錯誤有三種：TKI 配胃酸抑制劑、TKI 配 rifampin 或 azole 類抗黴菌藥、幾個會延長 QT 的藥疊在一起。

### 4.1 口服 TKI 的吸收：食物與胃酸

- **食物**：同一顆藥空腹吃和飯後吃，進到血液的量可以差好幾倍。Lapatinib 單次 1,500 mg 的研究中，低脂早餐讓 AUC 變成空腹的 2.67 倍，高脂早餐變成 4.25 倍，所以建議空腹服用，才能得到穩定的暴露量（Koch et al., 2009）。各藥規定不同，不能只教一句「飯後吃」：pazopanib 與 avapritinib 要空腹（餐前至少 1 小時或餐後至少 2 小時）（美國仿單；Novartis, 2025；Blueprint Medicines, 2026），alectinib 要隨餐（歐盟產品資訊；European Medicines Agency, 2025），regorafenib 要在低脂餐後（少於 600 大卡、脂肪少於 30%）（美國仿單；Bayer, 2026），osimertinib 不受食物限制（美國仿單；AstraZeneca, 2026）。逐藥整理見[肺癌章 5.4](../01-lung-cancer.md#54-口服標靶藥)與[肉瘤章 5.4](../04-sarcoma.md#54-gist非脂肪細胞型-sts-與-ntrk-融合口服標靶藥)。
- **胃酸**：多數口服標靶藥是弱鹼，要在酸性環境才溶得好。胃的 pH 平常約 1，用了胃酸抑制劑後約 4；溶解度在 pH 1–4 之間變化大的藥，吸收受影響最大，可能造成暴露量下降與治療失敗（Budha et al., 2012）。Pazopanib 的美國仿單要求避免併用胃酸抑制劑（Novartis, 2025）。Gefitinib、erlotinib、dacomitinib 等肺癌 TKI 要盡量避免 PPI；非用制酸藥不可時，與 H2 阻斷劑、制酸劑各自要錯開幾小時，逐藥的時間已整理在[肺癌章 5.4](../01-lung-cancer.md#54-口服標靶藥)的警示框，這裡不重複。
- **漏服與嘔吐**：規則因藥而異，見[肺癌章 5.5](../01-lung-cancer.md#55-口服標靶藥的實務漏服嘔吐管灌與居家安全)、[肉瘤章 5.5](../04-sarcoma.md#55-口服-tki-的實務漏服嘔吐吞嚥與交互作用)與[化療基礎 14.5](../00-shared/01-chemo-basics.md#145-口服抗癌藥)。

### 4.2 CYP3A4：誘導劑讓藥失效，抑制劑讓毒性上升

TKI 的交互作用主要有三類：胃內 pH 改變影響吸收、CYP 酵素代謝、QTc 延長；每位病人都需要做一次完整的用藥檢視（van Leeuwen et al., 2014）。CYP3A4 的方向很好記：誘導劑（rifampin、phenytoin、carbamazepine 等）讓 TKI 濃度下降；抑制劑（azole 類抗黴菌藥等）讓濃度上升。但**處理方式因藥而異**，不是一律避免：

| 藥物 | 美國仿單怎麼寫 |
|------|--------------|
| osimertinib | 避免強效 CYP3A 誘導劑；無法避免時加到 160 mg，每日一次，停用誘導劑 3 週後回到 80 mg（AstraZeneca, 2026） |
| lorlatinib | **禁忌**與強效 CYP3A 誘導劑併用（Pfizer, 2026） |
| ribociclib | 避免強效 CYP3A 抑制劑（無法避免時轉移性乳癌減為 400 mg）與強效誘導劑（Novartis, 2026） |
| olaparib | 避免強效或中效 CYP3A 抑制劑；無法避免時分別減為 100 mg 與 150 mg，每日兩次（AstraZeneca, 2025） |

其餘肺癌 TKI 的逐藥規則見[肺癌章 5.4](../01-lung-cancer.md#54-口服標靶藥)的表，GIST 用藥見[肉瘤章 5.5](../04-sarcoma.md#55-口服-tki-的實務漏服嘔吐吞嚥與交互作用)。

> [!WARNING]
> **Lorlatinib 加 rifampin：不是「效果變差」，是肝會壞**
> 12 位健康受試者同時用 rifampin 與單劑 lorlatinib，10 位出現嚴重肝毒性；仿單因此把強效 CYP3A 誘導劑列為禁忌，而且開始 lorlatinib 前要先停誘導劑達 3 個血漿半衰期（美國仿單；Pfizer, 2026）。看到抗結核處方時先核對病人正在吃的 TKI，但專師不要自己停藥或改劑量，聯絡主治醫師、感染科與藥師一起決定。

### 4.3 QT 延長

系統性回顧顯示，QTc 延長在部分 TKI 相當常見（dasatinib、vandetanib、sorafenib、sunitinib 超過 5%）；以 vandetanib 為例，任何程度的 QTc 延長 8.6%，超過 500 ms 的是 2.6%（Porta-Sánchez et al., 2017）。本手冊要記的藥：

- **osimertinib**：QTc >500 ms 約 1.1%；兩次心電圖都 >500 ms 時暫停，降到 481 ms 以下後以 40 mg 恢復（美國仿單；AstraZeneca, 2026）。
- **ribociclib**：QTcF <450 ms 才開始；基線與第 1 週期約第 14 天做心電圖；開始前與前 6 個週期開始時驗鉀、鈣、磷、鎂；避免併用 tamoxifen（美國仿單；Novartis, 2026）。
- **crizotinib**：QT 延長列在最嚴重的毒性之一（Kazandjian et al., 2014）。

處理原則是三件事：留基線心電圖、把鉀與鎂補到正常、檢查其他會延長 QT 的併用藥。各藥的暫停門檻見[乳癌章 6.5](../03-breast-cancer.md#65-cdk46-抑制劑嗜中性球肝功能心電圖腹瀉)與[肺癌章 6.1](../01-lung-cancer.md#61-egfr-tki)。

### 4.4 抗體的藥動學

單株抗體分子大、親水，分布慢、分布體積小；它們不靠肝臟 CYP 代謝，而是在組織中被分解成胜肽與胺基酸。抗體與體內的免疫球蛋白一樣，會被新生兒 Fc 受體（FcRn）保護而免於分解，所以半衰期可以長達約 4 週；有些抗體還會被自己的靶點「吃掉」（target-mediated disposition），靶點多的時候清除較快（Keizer et al., 2010）。兩個實際數字：bevacizumab 的半衰期約 20 天（美國仿單；Genentech, 2025），trastuzumab 約 18–27 天（Leyland-Jones et al., 2003）。

**臨床意義：** 停藥不等於藥馬上離開身體。Trastuzumab 停藥後約 7 個月，血中濃度才降到穩定狀態谷濃度的約 3%（美國仿單；Genentech, 2026）；bevacizumab 要在擇期手術前至少 28 天停藥（美國仿單；Genentech, 2025），可以從半衰期約 20 天來理解。排手術、談避孕、評估停藥後才出現的毒性時，都要把這段時間算進去。

### 4.5 體重劑量、固定劑量與負載劑量

- **為什麼有些抗體用固定劑量（flat dose）**：抗體主要分布在血漿與細胞外液，這些體積隨體重增加的幅度不成比例；清除主要靠蛋白分解與靶點結合，和靶點表現量的關係比體型大，加上治療窗通常很寬，所以多數抗體用固定劑量在藥動學上說得通，pertuzumab 就是一開始即以固定劑量核准的例子（Hendrikx et al., 2017）。Trastuzumab、bevacizumab 與 ADC 則仍以 mg/kg 計算，劑量見各癌別章第 5 段。
- **為什麼要負載劑量**：半衰期長的藥，要打好幾次才會累積到穩定濃度；trastuzumab 大約要 12 週（美國仿單；Genentech, 2026）。第一劑先給較高的劑量，可以一開始就達到有效濃度：每 3 週給法先給 8 mg/kg、之後 6 mg/kg，第 1 週期結束時谷濃度就超過 20 µg/mL（Leyland-Jones et al., 2003）。美國仿單的兩種給法是每週 4 → 2 mg/kg，或每 3 週 8 → 6 mg/kg（Genentech, 2026）。延遲給藥太久時是否要重打負載劑量，依仿單處理，見[乳癌章 5.2](../03-breast-cancer.md#52-her2-陽性抗-her2-抗體與化療組合)。

> [!TIP]
> **負載劑量像第一次幫浴缸放水**
> 浴缸有個小排水孔（藥物清除），水龍頭開固定流量（維持劑量），要放很久水位才會到標準線。第一次先用大水桶倒一桶進去（負載劑量），水位立刻到線，之後水龍頭只要補上流掉的量就好。排水孔越小（半衰期越長），越需要第一桶水。

### 4.6 ADC：藥動像抗體，毒性像化療

ADC 的抗體部分決定它在血中停留多久，所以和抗體一樣每 1–3 週靜脈給一次、以 mg/kg 計算（例如 T-DXd 5.4 mg/kg 每 3 週一次；美國仿單；Daiichi Sankyo, 2026）。但真正到達腫瘤細胞的只占給藥量的極小部分，載藥在其他組織釋出就成為毒性來源（Drago et al., 2021）。所以開 ADC 的醫囑要用化療的規格：T-DXd 屬高致吐，仿單要求預防性止吐（Daiichi Sankyo, 2026），止吐方案見[支持性照護第 1 節](../00-shared/03-supportive-care.md#1-化療引起的噁心嘔吐cinv)；給藥前看血球；外滲與安全操作依化療流程。

> [!IMPORTANT]
> **藥動學考點**
> - 字尾 **-nib**：口服、看 CYP3A4、看胃酸與食物、看 QT。字尾 **-mab**：注射、不看 CYP、半衰期以週計、注意輸注反應。
> - Lapatinib 與食物併服，AUC 可增為 2.67–4.25 倍（Koch et al., 2009）；「固定吃法」比「飯前或飯後」更重要。
> - 負載劑量的理由是半衰期長、到穩定濃度太慢；trastuzumab 每 3 週給法是 8 → 6 mg/kg（美國仿單；Genentech, 2026）。
> - 強效 CYP3A 誘導劑：osimertinib 是「加量」，lorlatinib 是「禁忌」。

---

## 5. 臨床怎麼用

**結論先講：** 四個癌別的標靶治療有共同的邏輯：(1) 有對應的 biomarker 才用；(2) 晚期先證明有效，再往前移到輔助治療；(3) 多數試驗先看到 PFS 改善，OS 不一定跟上，讀數字時兩個都要看。下表只列每個位置最關鍵的一個試驗與數字；完整的治療流程、劑量與台灣給付，請看各癌別章第 4、5、9 段。

### 5.1 肺癌（[肺癌章 4.3](../01-lung-cancer.md#43-nsclc-iv-期)）

| 情境 | 藥物 | 關鍵試驗與結果 |
|------|------|--------------|
| EGFR 敏感突變，晚期第一線 | osimertinib | FLAURA：PFS 18.9 對 10.2 個月（HR 0.46）；OS 38.6 對 31.8 個月（HR 0.80）（Soria et al., 2018；Ramalingam et al., 2020） |
| 同上，加強版 | osimertinib ＋ 含鉑化療 | FLAURA2：PFS HR 0.62；OS 47.5 對 37.6 個月（HR 0.77）；3 級以上不良事件 70% 對 34%（Planchard et al., 2023；Jänne et al., 2026） |
| 同上，加強版 | amivantamab ＋ lazertinib | MARIPOSA：PFS 23.7 對 16.6 個月（HR 0.70）；OS HR 0.75，3 年存活 60% 對 51%；3 級以上不良事件 80% 對 52%（Cho et al., 2024；Yang et al., 2025） |
| EGFR 突變，術後輔助 | osimertinib | ADAURA：5 年 OS 88% 對 78%（HR 0.49）（Tsuboi et al., 2023） |
| EGFR 突變，不可切除 III 期化放療後 | osimertinib | LAURA：PFS 39.1 對 5.6 個月（HR 0.16）（Lu et al., 2024） |
| 第一、二代 TKI 後出現 T790M | osimertinib | AURA3：PFS 10.1 對 4.4 個月（HR 0.30）（Mok et al., 2017） |
| osimertinib 後惡化 | amivantamab ＋ 化療 | MARIPOSA-2：PFS 6.3 對 4.2 個月（HR 0.48）（Passaro et al., 2024） |
| EGFR exon 20 插入 | amivantamab | CHRYSALIS（含鉑化療後）：反應率 40%（Park et al., 2021）；第一線併用化療見肺癌章 4.3 |
| ALK 融合 | alectinib；lorlatinib | ALEX：惡化或死亡 HR 0.47，中樞神經惡化 12% 對 45%（Peters et al., 2017）。CROWN：5 年 PFS 60% 對 8%（HR 0.19）（Solomon et al., 2024）。術後輔助 ALINA：II–IIIA 期 2 年無病存活 93.8% 對 63.0%（HR 0.24）（Wu et al., 2024） |
| ROS1 融合 | crizotinib 等 | 反應率 72%，PFS 19.2 個月（Shaw et al., 2014） |
| BRAF V600E | dabrafenib ＋ trametinib | 第一線反應率 64%（Planchard et al., 2017） |
| MET exon 14 | capmatinib；tepotinib | 未治療者反應率 68%、治療過者 41%（Wolf et al., 2020）；tepotinib 46%（Paik et al., 2020） |
| RET 融合 | selpercatinib | LIBRETTO-431：PFS 24.8 對 11.2 個月（HR 0.46）（Zhou et al., 2023） |
| KRAS G12C（第二線） | sotorasib | CodeBreaK 200：PFS 5.6 對 4.5 個月（HR 0.66）（de Langen et al., 2023） |
| NTRK 融合 | larotrectinib | 跨癌別反應率 75%（Drilon et al., 2018） |
| HER2 突變（治療過） | T-DXd 5.4 mg/kg | DESTINY-Lung02：反應率 49.0%（Goto et al., 2023） |
| 非鱗狀、無驅動基因 | bevacizumab ＋ 化療；docetaxel ＋ ramucirumab（第二線） | ECOG 4599：OS 12.3 對 10.3 個月（HR 0.79）（Sandler et al., 2006）。REVEL：OS 10.5 對 9.1 個月（HR 0.86）（Garon et al., 2014） |

### 5.2 乳癌（[乳癌章第 4 段](../03-breast-cancer.md#45-早期-her2-陽性抗-her2-治療的階梯)）

| 情境 | 藥物 | 關鍵試驗與結果 |
|------|------|--------------|
| HER2 陽性，早期 | 化療 ＋ trastuzumab | B-31／N9831 合併分析：OS HR 0.63，10 年 OS 由 75.2% 升到 84%（Perez et al., 2014） |
| HER2 陽性，術前治療後仍有殘存病灶 | T-DM1 | KATHERINE：3 年無侵襲性疾病存活 88.3% 對 77.0%（HR 0.50）（von Minckwitz et al., 2019） |
| HER2 陽性，延長輔助 | neratinib | ExteNET：2 年無侵襲性疾病存活 93.9% 對 91.6%（HR 0.67）；3 級腹瀉 40%（Chan et al., 2016） |
| HER2 陽性，轉移第一線 | trastuzumab ＋ pertuzumab ＋ docetaxel | CLEOPATRA 試驗結束時的分析：OS 57.1 對 40.8 個月（HR 0.69），8 年存活率 37% 對 23%（Swain et al., 2020） |
| HER2 陽性，轉移第二線 | T-DXd（對 T-DM1） | DESTINY-Breast03：PFS 28.8 對 6.8 個月（HR 0.33）；該次期中分析的 OS HR 0.64，兩組中位數都還沒到（Hurvitz et al., 2023）；之後更新的 OS 見[乳癌章 4.8](../03-breast-cancer.md#48-轉移性-her2-陽性從-thp-到-adc再到-tucatinib) |
| HER2 陽性，後線或腦轉移 | tucatinib ＋ trastuzumab ＋ capecitabine；lapatinib ＋ capecitabine | HER2CLIMB 初次分析：PFS 7.8 對 5.6 個月（HR 0.54），OS 21.9 對 17.4 個月（HR 0.66）（Murthy et al., 2020）；最終 OS 見乳癌章 4.8。Lapatinib ＋ capecitabine：疾病惡化時間 8.4 對 4.4 個月（HR 0.49）（Geyer et al., 2006） |
| HER2 低表現，轉移 | T-DXd | DESTINY-Breast04（HR 陽性族群）：PFS 10.1 對 5.4 個月（HR 0.51），OS 23.9 對 17.5 個月（HR 0.64）（Modi et al., 2022） |
| HR 陽性／HER2 陰性，轉移第一線 | CDK4/6 抑制劑 ＋ 內分泌治療 | PALOMA-2：PFS 24.8 對 14.5 個月（HR 0.58），但 OS 53.9 對 51.2 個月（HR 0.96）無差異（Finn et al., 2016；Slamon et al., 2024）。MONALEESA-2：OS 63.9 對 51.4 個月（HR 0.76）（Hortobagyi et al., 2022）。MONARCH 3：PFS HR 0.54（Goetz et al., 2017） |
| HR 陽性／HER2 陰性，高風險早期 | abemaciclib ＋ 內分泌治療 | monarchE：OS HR 0.842，7 年 OS 86.8% 對 85.0%（Johnston et al., 2026）；其他輔助試驗見[乳癌章 4.4](../03-breast-cancer.md#輔助-cdk46-抑制劑只有兩個是贏家) |
| PIK3CA 突變 | alpelisib；inavolisib | SOLAR-1：PFS 11.0 對 5.7 個月（HR 0.65）（André et al., 2019）。INAVO120：PFS 15.0 對 7.3 個月（HR 0.43），OS 34.0 對 27.0 個月（HR 0.67）（Turner et al., 2024；Jhaveri et al., 2025） |
| PIK3CA、AKT1 或 PTEN 變異 | capivasertib | CAPItello-291：變異族群 PFS 7.3 對 3.1 個月（HR 0.50）；全體 7.2 對 3.6 個月（HR 0.60）（Turner et al., 2023） |
| 內分泌治療失敗、無可用突變 | everolimus ＋ exemestane | BOLERO-2：PFS 6.9 對 2.8 個月（HR 0.43）（Baselga et al., 2012） |
| germline BRCA，轉移 | olaparib；talazoparib | OlympiAD：PFS 7.0 對 4.2 個月（HR 0.58）（Robson et al., 2017）。EMBRACA：PFS 8.6 對 5.6 個月（HR 0.54）（Litton et al., 2018） |
| germline BRCA，高風險早期 | olaparib 輔助 | OlympiA：3 年無侵襲性疾病存活 85.9% 對 77.1%（HR 0.58）（Tutt et al., 2021） |
| 三陰性，後線 | sacituzumab govitecan | ASCENT：PFS 5.6 對 1.7 個月（HR 0.41），OS 12.1 對 6.7 個月（HR 0.48）（Bardia et al., 2021） |
| HR 陽性／HER2 陰性，化療後 | sacituzumab govitecan；Dato-DXd | TROPiCS-02：OS 14.4 對 11.2 個月（HR 0.79）（Rugo et al., 2023）。TROPION-Breast01：PFS HR 0.63；該篇發表時 OS 尚未成熟（HR 0.84，0.62–1.14）（Bardia et al., 2025），最終結果見[乳癌章 4.7](../03-breast-cancer.md#第二線以後依-biomarker-選藥) |

### 5.3 胰臟癌（[胰臟癌章 4.9](../02-pancreatic-cancer.md#49-維持治療與二線以後)、[4.10](../02-pancreatic-cancer.md#410-生物標記導向治療與-kras-標靶)）

| 情境 | 藥物 | 關鍵試驗與結果 |
|------|------|--------------|
| germline BRCA1/2，第一線含鉑化療至少 16 週未惡化 | olaparib 維持 | POLO：PFS 7.4 對 3.8 個月（HR 0.53）；最終 OS 19.0 對 19.2 個月（HR 0.83），無顯著差異（Golan et al., 2019；Kindler et al., 2022） |
| 轉移性、先前治療後惡化（91.8% 帶 RAS G12 突變） | daraxonrasib | RASolute 302：OS 13.2 對 6.7 個月（HR 0.40），PFS 7.2 對 3.6 個月（O'Reilly et al., 2026）。藥證狀態見[胰臟癌章 4.10](../02-pancreatic-cancer.md#kras-突變daraxonrasib) |
| KRAS G12C（約 1–2%） | sotorasib | 38 人、反應率 21%、PFS 4.0 個月（Strickler et al., 2023） |
| 未選擇族群 | erlotinib ＋ gemcitabine | PA.3：OS 6.24 對 5.91 個月（HR 0.82）；統計顯著但只多約 10 天（Moore et al., 2007）。這是「沒有 biomarker 就用標靶藥」的典型結果，本手冊不建議常規使用 |
| NTRK 融合 | larotrectinib | 跨癌別資料（Drilon et al., 2018）；胰臟癌人數極少，見胰臟癌章 4.10 |

### 5.4 GIST 與肉瘤（[肉瘤章 4.5](../04-sarcoma.md#45-gist)、[4.4.3](../04-sarcoma.md#443-後線與寡轉移)）

| 情境 | 藥物 | 關鍵試驗與結果 |
|------|------|--------------|
| 晚期 GIST 第一線 | imatinib | 部分反應 53.7%（Demetri et al., 2002）；KIT exon 11 的部分反應率 83.5%，exon 9 為 47.8%，無突變者 0%（Heinrich et al., 2003） |
| 高風險 GIST 術後輔助 | imatinib 3 年 | SSG XVIII：3 年對 1 年，無復發存活 HR 0.46，5 年 OS 92.0% 對 81.7%（HR 0.45）（Joensuu et al., 2012） |
| GIST 第二線 | sunitinib | 疾病惡化時間 27.3 對 6.4 週（HR 0.33）（Demetri et al., 2006） |
| GIST 第三線 | regorafenib | GRID：PFS 4.8 對 0.9 個月（HR 0.27）（Demetri et al., 2013） |
| GIST 多線治療後（肉瘤章列為第四線以後） | ripretinib | INVICTUS：PFS 6.3 對 1.0 個月（HR 0.15）（Blay et al., 2020） |
| PDGFRA D842V 的 GIST | avapritinib | NAVIGATOR：反應率 88%（Heinrich et al., 2020） |
| 化療後的非脂肪細胞型軟組織肉瘤 | pazopanib | PALETTE：PFS 4.6 對 1.6 個月（HR 0.31）；OS 12.5 對 10.7 個月（HR 0.86），無顯著差異（van der Graaf et al., 2012） |
| NTRK 融合的肉瘤 | larotrectinib | 跨癌別資料（Drilon et al., 2018）；見[肉瘤章 5.4](../04-sarcoma.md#54-gist非脂肪細胞型-sts-與-ntrk-融合口服標靶藥) |

> [!IMPORTANT]
> **PFS 好不等於活得比較久**
> - **OS 有顯著改善的例子**：FLAURA、FLAURA2、MARIPOSA（肺癌）；CLEOPATRA、MONALEESA-2、monarchE、INAVO120、ASCENT（乳癌）；RASolute 302（胰臟癌）；SSG XVIII（GIST 輔助）。
> - **PFS 改善但 OS 無顯著差異的例子**：PALOMA-2（Slamon et al., 2024）、POLO（Kindler et al., 2022）、PALETTE（van der Graaf et al., 2012）。
> - 考題常把這兩組混在一起問。寫答案時不要說「某一類藥都延長存活」，要講到試驗名。

> [!CAUTION]
> **待核對：台灣核准仿單與本章引用仿單的差異**
> 本章的仿單數字來自美國 FDA 仿單（DailyMed）與歐盟 EMA 產品資訊，因為自動化工具無法取得台灣食藥署的仿單原文，沒有逐條比對。台灣核准的適應症、劑量與監測時程可能不同（例如肺癌章 5.4 指出 afatinib 的空腹規定台灣與美國不同）。開立前以院內藥典與台灣核准仿單為準；藥證與給付見各癌別章第 9 段。

---

## 6. 毒性與處置

**結論先講：** 標靶藥的毒性多半是「打中正常組織裡的同一個靶」造成的，所以從機轉就能預測：EGFR 在皮膚與腸道、HER2 在心肌、VEGF 在血管與腎絲球、PI3K 在胰島素訊號。病人出現新症狀時，先問「正在用哪一個標靶藥、用了多久」。分級與暫停門檻以各藥仿單為準，逐藥的表在各癌別章第 6 段，下面只講辨識與第一步。

| 毒性 | 最該想到的藥 | 第一步 | 詳細處置 |
|------|-------------|-------|---------|
| 痤瘡樣皮疹、甲溝炎 | EGFR TKI、cetuximab、amivantamab | 預防性保濕、防曬、口服 doxycycline；不要讓病人自行停藥 | 6.1；[肺癌章 6.1](../01-lung-cancer.md#61-egfr-tki) |
| 腹瀉 | afatinib、dacomitinib、neratinib、lapatinib、tucatinib、abemaciclib、capivasertib、sacituzumab govitecan | 依醫囑及早使用止瀉藥、補水；問次數與是否發燒 | 6.1；[支持性照護第 5 節](../00-shared/03-supportive-care.md#5-腹瀉) |
| **新的喘、乾咳、發燒** | osimertinib、T-DXd、Dato-DXd、CDK4/6 抑制劑、everolimus、crizotinib、lorlatinib | **先暫停藥物**、量血氧、安排胸部 CT、排除感染 | 6.2 |
| 心臟：LVEF 下降 | trastuzumab、pertuzumab、T-DM1、T-DXd、osimertinib | 依時程做心臟超音波；有喘、水腫、體重增加就提前做 | 6.3 |
| 高血壓、蛋白尿、出血、穿孔、傷口不癒合 | bevacizumab、ramucirumab、pazopanib、sunitinib、regorafenib | 每次給藥前量血壓、驗尿蛋白、問出血與手術 | 6.4 |
| 肝功能異常 | pazopanib、regorafenib、alectinib、ribociclib、sotorasib、T-DM1、tucatinib | 照仿單時程抽血，不要等門診日 | 6.5 |
| QT 延長 | osimertinib、ribociclib、crizotinib | 心電圖、電解質、併用藥 | 4.3 |
| 高血糖 | alpelisib、inavolisib、capivasertib、everolimus、lorlatinib | 開始前測空腹血糖與 HbA1c，前兩週加密監測 | 6.6 |
| 嗜中性球低下 | palbociclib、ribociclib、abemaciclib；sacituzumab govitecan | 照時程驗血球；發燒照發燒性嗜中性球低下處理 | 6.7 |
| 口腔炎 | everolimus、Dato-DXd、inavolisib、afatinib | 預防性含類固醇漱口水（依藥物） | 6.8 |
| 眼睛 | Dato-DXd、crizotinib | 人工淚液、眼科檢查 | 6.8 |
| 輸注反應 | amivantamab、trastuzumab、cetuximab | 停止輸注、依院內流程處置 | [急症章第 10 節](../00-shared/02-oncologic-emergencies.md#10-輸注反應過敏反應與過敏性休克) |

### 6.1 皮膚、甲溝炎與腹瀉

EGFR 抑制劑在多數病人造成皮膚副作用，處理得好才能維持劑量強度與生活品質。MASCC 指引建議預防性處置：開始 EGFR 抑制劑的前 6 週，使用 hydrocortisone 1% 乳膏加保濕劑、防曬，並口服 doxycycline 100 mg 每日兩次（Lacouture et al., 2011）。Amivantamab ＋ lazertinib 的 COCOON 試驗用加強版預防方案，把 2 級以上皮膚不良事件從 75% 降到 42%（Cho et al., 2025）；方案內容見[肺癌章 6.4](../01-lung-cancer.md#64-amivantamab-lazertinib)。

腹瀉在不可逆的泛 HER 抑制劑最明顯：neratinib 的 3 級腹瀉 40%（Chan et al., 2016）；abemaciclib 的腹瀉 81.3%，但多為 1 級（Goetz et al., 2017）。這類腹瀉是藥物作用而不是感染，原則是「及早用止瀉藥、補水、分級後暫停或減量」；abemaciclib 與 neratinib 的仿單規則見[乳癌章 6.5](../03-breast-cancer.md#65-cdk46-抑制劑嗜中性球肝功能心電圖腹瀉)與[4.5](../03-breast-cancer.md#45-早期-her2-陽性抗-her2-治療的階梯)。

### 6.2 間質性肺病（ILD）與非感染性肺炎

| 藥物 | 發生率與特點 | 仿單或試驗的處置重點 |
|------|-------------|-------------------|
| osimertinib | 約 4%，致死 0.4%（美國仿單；AstraZeneca, 2026） | 確診即永久停藥（剛做完化放療的病人另有規定，見肺癌章 6.1） |
| T-DXd | 5.4 mg/kg 時 12%、致死 0.9%，中位發生時間 5.5 個月（美國仿單；Daiichi Sankyo, 2026）。九個試驗合併分析 15.4%，5 級 2.2%，87% 的首次事件在 12 個月內（Powell et al., 2022） | Grade 1：暫停到完全恢復，可考慮類固醇（prednisolone ≥0.5 mg/kg/日）。**Grade 2 以上：永久停藥**，prednisolone ≥1 mg/kg/日至少 14 天，再慢慢減量至少 4 週 |
| Dato-DXd | TROPION-Breast01：經審查判定的藥物相關 ILD 3.3%（Bardia et al., 2025） | 分級處置與 T-DXd 同一套邏輯，見乳癌章 6.7 |
| everolimus | 3–4 級肺炎 3%（Baselga et al., 2012） | 見[乳癌章 6.6](../03-breast-cancer.md#66-pi3kaktmtor-抑制劑高血糖皮疹腹瀉口腔炎) |
| ribociclib 等 CDK4/6 抑制劑 | ILD／肺炎列在警語（美國仿單；Novartis, 2026） | 見[乳癌章 6.5](../03-breast-cancer.md#65-cdk46-抑制劑嗜中性球肝功能心電圖腹瀉) |
| lorlatinib、crizotinib | lorlatinib 1.9%（美國仿單；Pfizer, 2026）；crizotinib 列為最嚴重毒性之一（Kazandjian et al., 2014） | 見[肺癌章 6.2](../01-lung-cancer.md#62-alkros1-tki) |

> [!WARNING]
> **標靶藥病人「新的喘或乾咳」，先當 ILD，不要先當感冒**
> ILD 會致死，也容易被延誤。T-DXd 合併分析中，53.2% 的事件經審查委員會判定的發病日期比研究者記錄的早，中位差 43 天（Powell et al., 2022），代表早期變化常被忽略。處理順序：先暫停藥物、量血氧、安排胸部 CT、同時排除感染，不要等感染排除才停藥。鑑別診斷與類固醇原則可參考 [irAE 章 5.4](../00-shared/04-irae.md#54-肺炎pneumonitis)；T-DXd 的醫囑範例見[乳癌章 8.4](../03-breast-cancer.md#84-order-範例疑似-t-dxd-相關-ild)。

### 6.3 心臟：抗 HER2 治療與 LVEF

Trastuzumab 的心臟功能不全在與 anthracycline 同時使用時最高（27%），與 paclitaxel 併用 13%，單用 3–7%（Seidman et al., 2002）。美國仿單的監測時程：開始前測 LVEF，治療中每 3 個月，暫停期間每 4 週，輔助治療結束後每 6 個月、至少 2 年。暫停條件：LVEF 比治療前絕對值下降 16 個百分點以上，或低於正常下限且下降 10 個百分點以上；暫停至少 4 週（Genentech, 2026）。T-DXd 也要在治療前與治療中定期測 LVEF（美國仿單；Daiichi Sankyo, 2026）；osimertinib 的心肌病變 3.8%，有心臟危險因子者要測 LVEF（美國仿單；AstraZeneca, 2026）。各藥切點不同，完整對照表見[乳癌章 6.2](../03-breast-cancer.md#62-抗-her2-治療lvef-監測與暫停規則)。

### 6.4 抗 VEGF：血壓、尿蛋白、出血、穿孔、傷口

Bevacizumab 美國仿單（Genentech, 2025）的要點：

| 毒性 | 仿單的動作 |
|------|-----------|
| 高血壓 | 每 2–3 週量血壓；嚴重且藥物控制不住時暫停；高血壓危象或腦病變停用 |
| 蛋白尿 | ≥2 g/24 小時暫停；腎病症候群停用 |
| 手術與傷口 | 擇期手術前至少停 28 天；大手術後至少 28 天且傷口癒合才給；傷口癒合併發症時暫停 |
| 出血 | 近期咳血達半茶匙以上不給藥；3–4 級出血停用 |
| 胃腸穿孔 | 停用 |
| 動脈血栓、PRES | 嚴重動脈血栓停用；PRES 停用 |

口服的抗血管新生 TKI 有同樣的類別毒性：pazopanib 在血壓未控制時不可開始（美國仿單；Novartis, 2025）；regorafenib 前 6 週每週量血壓，GRID 試驗 3 級以上高血壓 23%、手足皮膚反應 20%（美國仿單；Bayer, 2026；Demetri et al., 2013）。手足皮膚反應的處置見[支持性照護 11.6](../00-shared/03-supportive-care.md#116-手足症候群hfs與手足皮膚反應hfsr)；bevacizumab 與 ramucirumab 的逐項比較見[肺癌章 6.8](../01-lung-cancer.md#68-抗血管新生藥物bevacizumab-與-ramucirumab)。

> [!WARNING]
> **抗 VEGF 病人的腹痛與咳血都是急症**
> 新出現的劇烈腹痛、腹部僵硬或發燒，要先排除胃腸穿孔；咳血量增加要先排除肺出血。ECOG 4599 的 15 例治療相關死亡中有 5 例是肺出血，而且試驗已經排除鱗狀細胞癌與明顯咳血的病人（Sandler et al., 2006）。給藥前「問咳血、問腹痛、問手術」三件事不能省。

### 6.5 肝毒性

Pazopanib 與 regorafenib 的美國仿單都有肝毒性加框警語，抽血時程要背：pazopanib 是基線、第 3、5、7、9 週、第 3 與第 4 個月（Novartis, 2025）；regorafenib 是用藥前、前 2 個月至少每 2 週、之後每月（Bayer, 2026）。Alectinib 前 3 個月每 2 週驗肝功能，第 1 個月每 2 週驗 CPK（歐盟產品資訊；European Medicines Agency, 2025）；ribociclib 前 2 個週期每 2 週驗肝功能與血球（美國仿單；Novartis, 2026）。Sotorasib 的 3 級以上 ALT 上升 8%（de Langen et al., 2023）。這些日期多半不會剛好落在回診日，開始用藥當天就要把抽血日排進醫囑，做法見[肉瘤章 6.7](../04-sarcoma.md#67-pazopanib肝毒性與高血壓)。

### 6.6 高血糖

Alpelisib 的 3–4 級高血糖 36.6%（André et al., 2019），3 級以上高血糖的中位發生時間只有 15 天，皮疹 13 天；發生高血糖的病人 87.1% 用 metformin 單獨或合併其他降血糖藥處理；預防性抗皮疹用藥把任何等級的皮疹從 64.1% 降到 26.7%；處置指引更詳細之後，因 3 級以上不良事件停藥的比例從 18.1% 降到 7.9%（Rugo et al., 2020）。Inavolisib 的 3–4 級高血糖 5.6%（Turner et al., 2024），everolimus 4%（Baselga et al., 2012），lorlatinib 9%（任何等級；美國仿單；Pfizer, 2026）；capivasertib 的血糖數字見[乳癌章 4.7](../03-breast-cancer.md#第二線以後依-biomarker-選藥)的警示框。結論：開藥前就要有基線空腹血糖與 HbA1c，前兩週的追蹤要先排好；各藥的血糖門檻見[乳癌章 6.6](../03-breast-cancer.md#66-pi3kaktmtor-抑制劑高血糖皮疹腹瀉口腔炎)。

### 6.7 嗜中性球低下

CDK4/6 抑制劑的嗜中性球低下很常見，但發燒性嗜中性球低下少見：palbociclib 的 3–4 級嗜中性球低下 66.4%，發燒性只有 1.8%（Finn et al., 2016）；abemaciclib 的 3–4 級為 21.1%（Goetz et al., 2017）。Ribociclib 的美國仿單要求開始前、前 2 個週期每 2 週、之後 4 個週期每週期開始時驗血球（Novartis, 2026）。處置以暫停與減量為主，規則見[乳癌章 6.5](../03-breast-cancer.md#65-cdk46-抑制劑嗜中性球肝功能心電圖腹瀉)。

ADC 則像化療：sacituzumab govitecan 的 3 級以上嗜中性球低下 51%、發燒性嗜中性球低下 6%（Bardia et al., 2021）。發燒時依[急症章第 1 節](../00-shared/02-oncologic-emergencies.md#1-發燒性嗜中性球低下)處理。

### 6.8 口腔炎與眼睛

- **口腔炎**：mTOR 抑制劑的類別毒性。SWISH 試驗讓使用 everolimus 的病人預防性使用 dexamethasone 漱口水，8 週內 2 級以上口腔炎 2%，BOLERO-2 的歷史對照為 33%（Rugo et al., 2017）。Dato-DXd 的口腔炎 50%（Bardia et al., 2025）。漱口水的用法見[乳癌章 6.7](../03-breast-cancer.md#67-抗體藥物複合體t-dxdt-dm1sacituzumab-govitecandato-dxd)與[支持性照護第 4 節](../00-shared/03-supportive-care.md#4-口腔黏膜炎)。
- **眼睛**：Dato-DXd 的眼表事件 40%，其中乾眼 21.7%、角膜炎 14.4%，多為 1 級（Bardia et al., 2025）；crizotinib 最常見的不良反應之一是視覺異常（Kazandjian et al., 2014）。衛教重點是人工淚液、暫時不戴隱形眼鏡、視力變化要回報，預防與眼科檢查時程見乳癌章 6.7。

### 6.9 其他要認得的毒性

| 毒性 | 藥物 | 重點 |
|------|------|------|
| 輸注反應 | amivantamab（66%；Park et al., 2021）、trastuzumab（加框警語；Genentech, 2026） | 前置用藥與處置見[肺癌章 6.4](../01-lung-cancer.md#64-amivantamab-lazertinib)與急症章第 10 節 |
| 靜脈血栓 | amivantamab ＋ lazertinib（Yang et al., 2025） | 預防性抗凝血的做法見肺癌章 6.4 |
| 中樞神經作用與血脂 | lorlatinib：中樞神經作用 52%；用藥前、第 1 與第 2 個月及之後定期驗膽固醇與三酸甘油酯（美國仿單；Pfizer, 2026） | 情緒、認知、說話改變要連家屬一起衛教 |
| 顱內出血與認知 | avapritinib：顱內出血 2.9%（GIST 與肥大細胞增生症合併分析），任何等級都永久停藥；認知不良反應在 GIST 病人 41%（美國仿單；Blueprint Medicines, 2026） | 新的頭痛、嗜睡當急症 |
| 水腫 | imatinib（Demetri et al., 2002）、capmatinib 51%（Wolf et al., 2020） | 固定時間量體重 |
| 發燒 | dabrafenib ＋ trametinib（Planchard et al., 2017） | 先排除感染；暫停規則見肺癌章 6.3 |
| 血液惡性疾病 | olaparib：MDS／AML 約 1.2%；基線與每月驗血球（美國仿單；AstraZeneca, 2025） | 持續的血球低下要查原因 |
| 胚胎胎兒毒性 | trastuzumab、T-DXd 的加框警語（美國仿單；Genentech, 2026；Daiichi Sankyo, 2026） | 開藥前確認懷孕狀態與避孕 |

---

## 7. 抗藥性與下一代藥物

**結論先講：** 抗藥幾乎一定會發生，機轉分三類：靶點自己再突變（on-target）、訊號改走旁路（bypass）、腫瘤細胞換了身分（組織型轉化）。三類的下一步完全不同，所以惡化時的第一個動作是重新取得腫瘤的資訊（再切片或驗血中腫瘤 DNA），不是直接換藥。

| 原本的藥 | 抗藥機轉 | 下一步 | 證據 |
|---------|---------|-------|------|
| 第一、二代 EGFR TKI | **T790M**（37 位重新切片的病人中 49%）；MET 放大（該系列 5%；另一系列 18 例中 4 例）；**轉化成小細胞肺癌 14%** | T790M 陽性用 osimertinib；小細胞轉化改用小細胞肺癌的化療 | Sequist et al., 2011；Engelman et al., 2007；Mok et al., 2017 |
| osimertinib | **C797S**（第二線使用後約 10–26%，第一線使用後約 7%）；**MET 放大**（第一線使用後最常見；AURA3 血漿分析近 19%）；RAS–MAPK 或 PI3K 路徑活化、新的融合基因、組織型轉化 | 沒有單一解法：amivantamab ＋ 化療，或依機轉選藥、參加試驗 | Thress et al., 2015；Leonetti et al., 2019；Passaro et al., 2024 |
| crizotinib、第二代 ALK TKI | 每個 ALK TKI 留下不同的 ALK 抗藥突變；**G1202R** 在第二代 ALK TKI 之後明顯增加 | lorlatinib（第三代，涵蓋多種 ALK 突變）；帶 ALK 抗藥突變的細胞株才對 lorlatinib 敏感 | Gainor et al., 2016；Solomon et al., 2018 |
| imatinib（GIST，原本有效後來失效） | **KIT 次發突變**：15 位獲得性抗藥的病人中 7 位（46%），原發突變都在 exon 11，次發突變多在 exon 17 | sunitinib → regorafenib → ripretinib | Antonescu et al., 2005；Demetri et al., 2006；Demetri et al., 2013；Blay et al., 2020 |
| imatinib（GIST，一開始就無效） | PDGFRA D842V 對一般 TKI 高度抗藥（原發性抗藥） | avapritinib | Heinrich et al., 2020 |
| 只打單一突變型的 KRAS G12C 抑制劑 | 不是抗藥，而是涵蓋面太窄：胰臟癌九成以上帶 RAS 突變，G12C 卻只占 1–2% | 新一代 daraxonrasib 同時抑制活化態（結合 GTP）的突變型與野生型 RAS | Strickler et al., 2023；O'Reilly et al., 2026 |
| 內分泌治療 | ESR1 突變 | 見[內分泌治療](05-endocrine-therapy.md)與[乳癌章 4.7](../03-breast-cancer.md#第二線以後依-biomarker-選藥) | |

三個觀念：

1. **原本的驅動突變通常還在。** Sequist 的 37 位抗藥病人，腫瘤全都保留原本的 EGFR 活化突變；有 3 位病人停用 TKI 一段時間後抗藥機轉消失，再用 EGFR TKI 又有效（Sequist et al., 2011）。腫瘤仍然依賴同一條路，只是學會了躲藥。
2. **下一代藥是照著抗藥機轉設計的。** T790M 之於 osimertinib（Mok et al., 2017）、G1202R 之於 lorlatinib（Gainor et al., 2016）、多種 KIT 次發突變之於 ripretinib 的「開關控制」設計（Smith et al., 2019），都是先看懂抗藥、再做藥。
3. **液態切片可以追蹤抗藥。** Thress 等人就是在 osimertinib 抗藥病人血漿的游離 DNA 裡找到 C797S 的（Thress et al., 2015）。血液陰性不能排除，檢測方法的優缺點見[肺癌章 2.3](../01-lung-cancer.md#23-檢測方法)。

**循序用藥，還是一開始就用最強的？**

| 策略 | 例子 | 好處 | 代價 |
|------|------|------|------|
| 循序（惡化再換下一代） | gefitinib → T790M → osimertinib（Mok et al., 2017） | 每一線毒性低 | 不是每個人都長出下一線打得到的突變；有人來不及接下一線 |
| 第一線就用下一代 | osimertinib 第一線：OS 38.6 對 31.8 個月（Ramalingam et al., 2020）。lorlatinib 第一線：5 年 PFS 60%，治療結束時的血中腫瘤 DNA 沒有偵測到新的 ALK 抗藥突變（Solomon et al., 2024） | 把抗藥往後推 | 下一代藥本身的毒性（lorlatinib 的血脂與中樞神經作用） |
| 第一線就合併 | osimertinib ＋ 化療（Jänne et al., 2026）；amivantamab ＋ lazertinib（Yang et al., 2025）；trastuzumab ＋ pertuzumab（Swain et al., 2015） | OS 更長 | 3 級以上不良事件明顯增加（FLAURA2 為 70% 對 34%；MARIPOSA 為 80% 對 52%），回診與輸注負擔加重 |

> [!TIP]
> **封路、改道、換車**
> 標靶藥像在癌細胞唯一的聯外道路上設路障。車流有三種應變：(1) 把路障撞出一個缺口（靶點再突變，例如 T790M、C797S、G1202R、KIT exon 17）；(2) 改走旁邊的小路（旁路，例如 MET 放大）；(3) 乾脆不開車、改搭船（組織型轉化，例如變成小細胞肺癌）。第一種換一個更合身的路障（下一代 TKI）；第二種要連小路一起封；第三種原本的路障完全沒用，要換一套打法。不先看清楚是哪一種，就會白白換藥。

> [!IMPORTANT]
> **抗藥性的考點**
> - 第一、二代 EGFR TKI 之後最常見的抗藥機轉是 **T790M**，對策是 osimertinib；osimertinib 之後要想到 **C797S 與 MET 放大**。
> - EGFR TKI 抗藥時要想到**小細胞轉化**（Sequist 系列中 14%），這只有再切片看組織才診斷得出來，驗血中腫瘤 DNA 看不到。
> - ALK：第二代之後的 **G1202R** → lorlatinib。
> - GIST：imatinib 之後依序 sunitinib、regorafenib、ripretinib；**PDGFRA D842V 一開始就不該用 imatinib**，要用 avapritinib。

---

## 8. 專師實務

**結論先講：** 標靶藥多半在門診開始、在家裡吃，出事的時候病人不在醫院。專師的工作集中在三個時間點：開藥前把基線檢查與交互作用查完；前幾週照時程追蹤；每次回診問出該問的警訊。

### 8.1 開藥前檢核

| 項目 | 要確認什麼 |
|------|-----------|
| biomarker 報告 | 病歷上有書面報告；變異型別對得上藥物（例如 EGFR exon 19 缺失或 L858R、KIT exon 11 或 PDGFRA D842V、germline 而不只是 somatic BRCA）；送健保事前審查的要求見各癌別章第 9 段 |
| 排除條件 | bevacizumab：鱗狀細胞癌、近期咳血、28 天內的手術或未癒合傷口（美國仿單；Genentech, 2025）；pazopanib：未控制的高血壓（美國仿單；Novartis, 2025）；免疫治療與 osimertinib 的先後順序（Schoenfeld et al., 2019） |
| 基線檢查 | 依類別：抗 HER2 藥與 osimertinib（有心臟危險因子者）測 LVEF；osimertinib、ribociclib 做心電圖與電解質；抗 VEGF 藥量血壓、驗尿蛋白；pazopanib、regorafenib、alectinib、ribociclib 驗肝功能；PI3K／AKT 抑制劑驗空腹血糖與 HbA1c；lorlatinib 驗血脂與血糖；CDK4/6 抑制劑、PARP 抑制劑與 ADC 驗血球（出處見第 6 段與 8.3） |
| 併用藥 | 胃酸抑制劑、CYP3A4 誘導劑與抑制劑（抗結核藥、抗黴菌藥、抗癲癇藥）、其他延長 QT 的藥、中草藥與保健食品（van Leeuwen et al., 2014） |
| 懷孕與避孕 | trastuzumab 與 T-DXd 有胚胎胎兒毒性加框警語（美國仿單；Genentech, 2026；Daiichi Sankyo, 2026）；其他藥依仿單 |
| 服藥能力 | 吞嚥、管灌、誰幫忙備藥、空腹或隨餐的規定能不能做到；流程見[化療基礎 14.5](../00-shared/01-chemo-basics.md#145-口服抗癌藥) |
| B 型肝炎 | 依[化療基礎第 6 節](../00-shared/01-chemo-basics.md#6-b-型肝炎篩檢與預防性抗病毒)的篩檢流程 |

### 8.2 衛教重點

- **怎麼吃**：每天固定時間、固定吃法（空腹或隨餐依該藥規定）；漏服與吐掉的處理每個藥不同，衛教單要寫該藥的版本。
- **不要自行停藥，也不要硬撐**：皮疹、腹瀉、手腳脫皮先回報，多數可以靠處置與減量繼續治療。GIST 病人停掉有效的 imatinib 後多數會惡化，見[肉瘤章 4.5.3](../04-sarcoma.md#453-晚期或轉移性-gist)。
- **當天就要聯絡團隊的警訊**：新的喘、乾咳或發燒（ILD）；胸悶、下肢水腫、體重快速增加（心臟）；劇烈腹痛、黑便、咳血（穿孔或出血）；一天腹瀉很多次或合併發燒；大片皮疹、水泡或口腔潰瘍；視力模糊或眼睛痛；突發頭痛、嗜睡、說話或情緒改變。
- **居家紀錄**：抗 VEGF 藥與 pazopanib、regorafenib 的病人在家量血壓；PI3K／AKT 抑制劑的病人依醫囑測血糖；imatinib 的病人固定時間量體重。
- **新處方先問**：到其他科或診所拿藥、買成藥或中草藥之前，先讓團隊或藥師核對交互作用。

### 8.3 監測時程速查

| 藥物 | 開始後要排的檢查（依仿單） | 出處 |
|------|-----------------------|------|
| trastuzumab | LVEF：開始前、每 3 個月、輔助結束後每 6 個月至少 2 年 | 美國仿單（Genentech, 2026） |
| T-DXd | 每次回診問呼吸症狀；LVEF 開始前與定期 | 美國仿單（Daiichi Sankyo, 2026） |
| bevacizumab | 每 2–3 週量血壓；尿蛋白 ≥2 g/24 小時暫停（驗尿的做法見肺癌章 6.8） | 美國仿單（Genentech, 2025） |
| osimertinib | 高風險者做心電圖與電解質；有心臟危險因子者測 LVEF | 美國仿單（AstraZeneca, 2026） |
| alectinib | 肝功能：前 3 個月每 2 週；CPK：第 1 個月每 2 週；心跳與血壓 | 歐盟產品資訊（European Medicines Agency, 2025） |
| lorlatinib | 血脂：開始前、第 1 與第 2 個月、之後定期；血壓：2 週後與之後至少每月；開始前空腹血糖 | 美國仿單（Pfizer, 2026） |
| ribociclib | 心電圖：開始前、第 1 週期約第 14 天；電解質：前 6 個週期開始時；血球與肝功能：前 2 個週期每 2 週、之後 4 個週期每週期開始時 | 美國仿單（Novartis, 2026） |
| pazopanib | 肝功能：基線、第 3、5、7、9 週、第 3 與第 4 個月 | 美國仿單（Novartis, 2025） |
| regorafenib | 肝功能：前 2 個月至少每 2 週、之後每月；血壓：前 6 週每週 | 美國仿單（Bayer, 2026） |
| olaparib | 血球：基線與每月 | 美國仿單（AstraZeneca, 2025） |
| alpelisib | 3 級以上高血糖中位在第 15 天、皮疹在第 13 天出現，前 2 週要加密追蹤 | Rugo et al., 2020 |

> [!NOTE]
> **抽血與檢查怎麼排，依院內流程**
> 上表是美國或歐盟仿單的時程。心臟超音波由誰開單、心電圖在門診還是檢查室做、第 3、5、7、9 週的抽血可不可以在住家附近的院所做再回傳，各院做法不同。實習時先找到該藥的院內開藥檢核表（checklist）與衛教單，沒有的話問臨床藥師。

---

## 9. 藥物卡

下表每一格的內容都出自本章第 3–6 段，出處見該段；劑量與減量規則見各癌別章。

<!-- drug-cards -->
| 藥名 | 分類 | 機轉 | 主要用途 | 必記毒性 | 監測與處置 |
|------|------|------|----------|----------|------------|
| gefitinib（Iressa） | EGFR TKI，第一代 | 抑制 EGFR 酪胺酸激酶 | EGFR 敏感突變的 NSCLC | 皮疹或痤瘡 66.2%、腹瀉 46.6% | 皮膚預防照護；盡量避免 PPI，H2 阻斷劑與制酸劑要錯開 |
| erlotinib（Tarceva） | EGFR TKI，第一代 | 抑制 EGFR 酪胺酸激酶 | EGFR 敏感突變的 NSCLC；胰臟癌效益極小 | 皮疹、腹瀉（EGFR 抑制劑的類別毒性） | 同 gefitinib；胰臟癌不建議常規使用 |
| afatinib（Giotrif） | EGFR TKI，第二代 | 不可逆阻斷 EGFR、HER2、ErbB4 | EGFR 突變的 NSCLC | 腹瀉、皮疹或痤瘡、口腔炎 | 及早止瀉；皮膚預防照護 |
| dacomitinib（Vizimpro） | EGFR TKI，第二代 | 不可逆的 EGFR TKI | EGFR 突變的 NSCLC 第一線 | 3–4 級痤瘡樣皮膚炎 14%、腹瀉 8% | 皮膚預防照護；盡量避免 PPI，H2 阻斷劑要錯開 |
| osimertinib（Tagrisso） | EGFR TKI，第三代 | 不可逆，選擇性抑制敏感突變與 T790M | EGFR 突變 NSCLC：輔助、III 期化放療後、晚期 | ILD 約 4%、QTc 延長、心肌病變 3.8% | 新的喘咳先暫停並評估 ILD，確診即永久停藥；高風險者做心電圖；有心臟危險因子者測 LVEF |
| amivantamab（Rybrevant） | 雙特異性抗體 | 結合 EGFR 與 MET 的胞外區 | EGFR exon 20 插入；併 lazertinib 用於敏感突變 | 輸注反應 66%、皮疹 86%、甲溝炎 45%、靜脈血栓 | 前置用藥；預防性皮膚照護；注意血栓症狀 |
| crizotinib（Xalkori） | ALK／ROS1 TKI，第一代 | 抑制 ALK 等激酶 | ALK 或 ROS1 融合的 NSCLC | 視覺異常、腸胃症狀、水腫、肝毒性、ILD、QT | 肝功能、心電圖；視力變化要回報 |
| alectinib（Alecensa） | ALK TKI，第二代 | 高選擇性抑制 ALK | ALK 融合 NSCLC：輔助與晚期 | 肌痛 35.3%、CPK 上升 56.2%、心搏過緩 11.3% | 肝功能前 3 個月每 2 週；CPK 第 1 個月每 2 週；隨餐 |
| lorlatinib（Lorbrena） | ALK TKI，第三代 | 可進入腦部，涵蓋多種 ALK 抗藥突變 | ALK 融合 NSCLC | 高血脂、中樞神經作用 52%、高血糖 | 驗血脂；禁併用強效 CYP3A 誘導劑（rifampin） |
| selpercatinib（Retevmo） | RET TKI | 抑制 RET 激酶 | RET 融合的 NSCLC | 3 級以上高血壓 14%、ALT 上升 12% | 量血壓、驗肝功能 |
| capmatinib（Tabrecta） | MET TKI | 抑制 MET 激酶 | MET exon 14 跳躍突變的 NSCLC | 周邊水腫 51%、噁心 45% | 量體重、看水腫 |
| larotrectinib（Vitrakvi） | TRK TKI | 抑制 TRK 激酶 | NTRK 融合的實體腫瘤，不分癌別 | 多為 1 級不良事件 | 先確認 NTRK 融合報告 |
| dabrafenib（Tafinlar） | BRAF TKI | 抑制 BRAF，與 MEK 抑制劑 trametinib 併用 | BRAF V600E 的 NSCLC | 發燒 | 發燒先排除感染，依仿單暫停 |
| sotorasib（Lumakras） | KRAS G12C 抑制劑 | 專一、不可逆地結合 KRAS G12C | KRAS G12C 的 NSCLC（第二線） | 腹瀉、ALT 與 AST 上升 | 驗肝功能；只對 G12C 有效 |
| trastuzumab（Herceptin） | 抗 HER2 單株抗體 | 人源化抗 HER2 抗體；Fc 端可引發 ADCC | HER2 陽性乳癌：早期與轉移 | 心肌病變、輸注反應 | LVEF 開始前、每 3 個月；不可與 T-DM1、T-DXd 互換 |
| pertuzumab（Perjeta） | 抗 HER2 單株抗體 | 結合的 HER2 位置與 trastuzumab 不同，兩者合用（雙標靶） | HER2 陽性乳癌 | 併用時不良事件多在化療期間 | 與 trastuzumab 一起監測 LVEF |
| lapatinib（Tykerb） | HER2／EGFR TKI | 抑制 HER2 與 EGFR 激酶 | HER2 陽性轉移性乳癌，併 capecitabine | 腹瀉、手足症候群 | 食物使 AUC 增為 2.67–4.25 倍，要固定空腹吃 |
| neratinib（Nerlynx） | 泛 HER TKI | 不可逆抑制 HER1、HER2、HER4 | HER2 陽性早期乳癌延長輔助 | 3 級腹瀉 40% | 開藥時就安排止瀉計畫 |
| tucatinib（Tukysa） | HER2 TKI | 高選擇性抑制 HER2 激酶 | HER2 陽性轉移性乳癌，含腦轉移 | 腹瀉、手足症候群、轉胺酶上升 | 驗肝功能 |
| trastuzumab emtansine（Kadcyla） | 抗 HER2 ADC | 穩定連接子 ＋ 微管抑制劑 DM1 | HER2 陽性乳癌：術後殘存病灶、轉移 | 血小板低下、轉胺酶上升 | 追蹤血小板與肝功能，時程見乳癌章 6.7 |
| trastuzumab deruxtecan（Enhertu） | 抗 HER2 ADC | 可切斷連接子 ＋ 拓樸異構酶 I 抑制劑，有旁觀者效應 | HER2 陽性或低表現乳癌；HER2 突變 NSCLC | ILD 12%（致死 0.9%）、高致吐、LVEF 下降 | ILD Grade 1 暫停、Grade 2 以上永久停藥；預防性止吐 |
| sacituzumab govitecan（Trodelvy） | 抗 Trop-2 ADC | 抗 Trop-2 抗體 ＋ SN-38 | 三陰性與 HR 陽性轉移性乳癌後線 | 3 級以上嗜中性球低下 51%、腹瀉 10% | 給藥前看血球；發燒照發燒性嗜中性球低下處理 |
| datopotamab deruxtecan（Datroway） | 抗 Trop-2 ADC | 抗 Trop-2 抗體 ＋ 拓樸異構酶 I 抑制劑 | HR 陽性／HER2 陰性轉移性乳癌化療後 | 口腔炎 50%、眼表事件 40% | 口腔與眼睛的預防照護；新的喘咳要評估 ILD |
| bevacizumab（Avastin） | 抗 VEGF 單株抗體 | 中和 VEGF，阻斷血管新生 | 非鱗狀 NSCLC 等 | 高血壓、蛋白尿、出血、穿孔、傷口癒合不良 | 每次量血壓與尿蛋白；手術前後各隔 28 天 |
| ramucirumab（Cyramza） | 抗 VEGFR-2 單株抗體 | 結合 VEGFR-2 胞外區 | NSCLC 第二線，併 docetaxel | 高血壓；併 docetaxel 時發燒性嗜中性球低下 16% | 量血壓、看血球 |
| imatinib（Glivec） | BCR-ABL／KIT TKI | 抑制 KIT 訊號 | GIST：晚期第一線、高風險術後輔助 3 年 | 水腫、腹瀉、疲倦；胃腸道或腹腔內出血約 5% | 量體重；不要自行停藥；先看基因型 |
| sunitinib（Sutent） | 多靶點 TKI | 抑制多種受體酪胺酸激酶 | imatinib 失敗的 GIST | 疲倦、腹瀉、皮膚變色、噁心 | 細節見肉瘤章 6.8 |
| regorafenib（Stivarga） | 激酶抑制劑 | 抑制多種激酶 | imatinib 與 sunitinib 失敗的 GIST | 肝毒性（加框）、高血壓 23%、手足皮膚反應 20% | 肝功能前 2 個月每 2 週；血壓前 6 週每週；低脂餐後吃 |
| ripretinib（Qinlock） | 開關控制型 TKI | 把激酶活化環鎖在不活化構形 | 多線治療後的 GIST | lipase 上升、高血壓 | 細節見肉瘤章 6.8 |
| avapritinib（Ayvakit） | KIT／PDGFRA TKI | 抑制 KIT 與 PDGFRA，對 PDGFRA D842V 效力強 | PDGFRA D842V 的 GIST | 顱內出血（合併分析 2.9%）、認知不良反應（GIST 病人 41%） | 顱內出血任何等級永久停藥；空腹吃 |
| pazopanib（Votrient） | 多靶點 TKI | 抑制多種受體酪胺酸激酶 | 化療後的晚期軟組織肉瘤 | 肝毒性（加框）、高血壓、腹瀉、疲倦 | 肝功能第 3、5、7、9 週；空腹；避免胃酸抑制劑 |
| palbociclib（Ibrance） | CDK4/6 抑制劑 | 阻斷 Rb 磷酸化，細胞停在 G1 期 | HR 陽性／HER2 陰性轉移性乳癌 | 3–4 級嗜中性球低下 66.4%，發燒性 1.8% | 照時程驗血球；暫停與減量為主 |
| ribociclib（Kisqali） | CDK4/6 抑制劑 | 抑制 CDK4/6 | HR 陽性／HER2 陰性乳癌：轉移與早期 | QT 延長、肝毒性、嗜中性球低下 | 心電圖基線與第 14 天；QTcF 低於 450 ms 才開始；避免 tamoxifen |
| abemaciclib（Verzenio） | CDK4/6 抑制劑 | 抑制 CDK4/6，連續服用 | HR 陽性／HER2 陰性乳癌：轉移與高風險早期 | 腹瀉 81.3%、3–4 級嗜中性球低下 21.1% | 及早止瀉、補水；驗血球 |
| alpelisib（Piqray） | PI3Kα 抑制劑 | 抑制 PI3K 的 p110α | PIK3CA 突變的 HR 陽性乳癌 | 3–4 級高血糖 36.6%、皮疹 9.9% | 基線血糖與 HbA1c；前 2 週加密追蹤；預防皮疹 |
| inavolisib（Itovebi） | PI3Kα 抑制劑 | 抑制並促進突變 p110α 降解 | PIK3CA 突變的 HR 陽性乳癌 | 高血糖、口腔炎、腹瀉 | 血糖監測；口腔照護 |
| capivasertib（Truqap） | AKT 抑制劑 | 抑制 AKT | PIK3CA、AKT1 或 PTEN 變異的 HR 陽性乳癌 | 3 級以上皮疹 12.1%、腹瀉 9.3% | 皮膚與腹瀉處置；血糖規則見乳癌章 6.6 |
| everolimus（Afinitor） | mTOR 抑制劑 | 抑制 mTOR | HR 陽性乳癌，併 exemestane | 口腔炎、非感染性肺炎、高血糖 | dexamethasone 漱口水預防口腔炎；新的喘咳要評估 |
| olaparib（Lynparza） | PARP 抑制劑 | 對 BRCA 缺陷細胞合成致死 | germline BRCA 乳癌；胰臟癌維持治療 | 貧血、噁心、疲倦；MDS／AML 約 1.2% | 血球基線與每月；避免強效或中效 CYP3A 抑制劑，避不開才減量 |
| talazoparib（Talzenna） | PARP 抑制劑 | 對 BRCA 缺陷細胞合成致死 | germline BRCA 的轉移性乳癌 | 3–4 級血液學事件 55%，以貧血為主 | 定期驗血球 |

---

## 10. 自我測驗

**Q1.** 一位 62 歲、不吸菸的女性，新診斷第 IV 期肺腺癌，體能良好，EGFR 與其他基因報告預計 5 天後出來。家屬希望「今天就先吃標靶藥」。依 IPASS 的結果，最適當的說明是？

A. EGFR TKI 對東亞不吸菸女性都有效，可以先吃　B. 先打免疫治療，等報告出來再改標靶藥　C. 沒有 EGFR 突變的人用 gefitinib 反而比化療差，應等報告再決定　D. 標靶藥副作用小，吃了沒效再換也沒有損失

<details>
<summary>答案與詳解</summary>

**答案：C**。IPASS 收的正是東亞、不吸菸或輕度吸菸的肺腺癌病人；EGFR 突變陽性者用 gefitinib 的惡化風險 HR 0.48，陰性者 HR 2.85，也就是比化療差（Mok et al., 2009）。臨床特徵只能提高突變的機率，不能取代檢測。B 更危險：先用免疫治療再接 osimertinib，嚴重免疫相關不良事件明顯增加（Schoenfeld et al., 2019）。

</details>

**Q2.** 一位 EGFR exon 19 缺失的肺腺癌病人，在外院因為「等不到基因報告」先打了一劑 PD-1 抑制劑，兩週後轉來準備開始 osimertinib。專師最應該提醒團隊與病人的風險是？

A. Osimertinib 會失效，需要加倍劑量　B. 免疫治療後短期內接 osimertinib，嚴重免疫相關不良事件（如肺炎、肝炎）的機率升高　C. 兩者併用會造成 QT 縮短　D. 沒有特別風險，照常開始即可

<details>
<summary>答案與詳解</summary>

**答案：B**。先用 PD-(L)1 抑制劑、之後接 osimertinib 的病人，15% 發生嚴重免疫相關不良事件；3 個月內接上的更高達 24%。反過來先用 osimertinib 再用免疫治療則沒有觀察到（Schoenfeld et al., 2019）。這位病人開始 osimertinib 後的前幾週要加密追蹤呼吸症狀與肝功能。

</details>

**Q3.** 關於小分子激酶抑制劑（-nib）與單株抗體（-mab）的比較，下列何者正確？

A. 單株抗體分子大、在體內被分解成胺基酸，半衰期以週計，很少有 CYP 交互作用　B. 單株抗體主要經 CYP3A4 代謝，要避開 rifampin　C. 小分子藥停留在細胞外，靠 ADCC 殺死腫瘤　D. 小分子藥半衰期長，通常每 3 週給一次

<details>
<summary>答案與詳解</summary>

**答案：A**。抗體不能口服、分布體積小、被分解成胜肽與胺基酸，並因 FcRn 的保護而半衰期長，代謝性交互作用少見（Keizer et al., 2010）。小分子進入細胞作用在激酶區，多經 CYP3A4 代謝，吸收受胃酸影響（van Leeuwen et al., 2014）。ADCC 是抗體 Fc 端的功能（Clynes et al., 2000）。

</details>

**Q4.** Trastuzumab deruxtecan 對「HER2 低表現」的乳癌也有效，而 trastuzumab emtansine 沒有這個適應症。最能解釋這個差別的機轉是？

A. T-DXd 的抗體對 HER2 的親和力高很多　B. T-DXd 不需要進入細胞就能作用　C. T-DM1 的載藥是拓樸異構酶抑制劑，對乳癌無效　D. T-DXd 釋出的載藥能穿過細胞膜，殺死旁邊 HER2 表現低或陰性的細胞（旁觀者效應）

<details>
<summary>答案與詳解</summary>

**答案：D**。兩個藥的抗體序列相同；差別在連接子與載藥。T-DXd 用可切斷的連接子，每個抗體帶約 7–8 個拓樸異構酶 I 抑制劑，釋出的載藥穿膜能力高；T-DM1 釋出的 Lys-SMCC-DM1 穿膜能力低，沒有旁觀者效應（Ogitani et al., 2016）。DESTINY-Breast04 證實 T-DXd 在 HER2 低表現乳癌延長 PFS 與 OS（Modi et al., 2022）。

</details>

**Q5.** 一位 HER2 陽性早期乳癌病人準備開始含 trastuzumab 的輔助治療。依美國仿單，LVEF 的監測時程何者正確？

A. 只有出現心衰竭症狀時才需要做　B. 開始前一次，治療中每 3 個月，治療結束後每 6 個月、至少 2 年　C. 開始前一次，之後每年一次　D. 每次給藥前都要做

<details>
<summary>答案與詳解</summary>

**答案：B**。這個時程來自 Herceptin 美國仿單；因心臟功能暫停期間則每 4 週測一次（Genentech, 2026）。要監測的原因可以追溯到關鍵試驗：與 anthracycline 同時使用時，心臟功能不全高達 27%（Slamon et al., 2001；Seidman et al., 2002）。

</details>

**Q6.** 使用 T-DXd 第 5 個月的病人回診，主訴兩週來乾咳、爬一層樓會喘，沒有發燒，SpO₂ 94%。胸部 CT 顯示雙側新的毛玻璃病灶，感染檢查陰性，判定為 Grade 2 ILD。依美國仿單，處置是？

A. 減一階劑量後繼續給藥　B. 暫停一次，症狀改善後以原劑量恢復　C. 永久停藥，並開始類固醇（prednisolone 至少 1 mg/kg/日）　D. 改成每 4 週給藥一次

<details>
<summary>答案與詳解</summary>

**答案：C**。T-DXd 的 ILD 規則是：Grade 1（無症狀）暫停到完全恢復；**Grade 2 以上永久停藥**，並給 prednisolone ≥1 mg/kg/日至少 14 天，再減量至少 4 週（美國仿單；Daiichi Sankyo, 2026）。合併分析中 ILD 發生率 15.4%、5 級 2.2%，87% 的首次事件發生在 12 個月內（Powell et al., 2022）。有症狀就已經是 Grade 2，不能再給。

</details>

**Q7.** 一位使用 bevacizumab 的非鱗狀肺腺癌病人，預定下週做擇期的腹股溝疝氣修補手術，今天是原訂的給藥日。最適當的處置是？

A. 今天不給 bevacizumab，並通知主治醫師：擇期手術前至少要停藥 28 天，手術日期需要重新安排　B. 今天照常給藥，手術後隔天恢復　C. 今天劑量減半　D. 改成 ramucirumab 就不受影響

<details>
<summary>答案與詳解</summary>

**答案：A**。美國仿單要求擇期手術前至少停 bevacizumab 28 天，大手術後至少 28 天且傷口癒合才能再給（Genentech, 2025）。它的半衰期約 20 天，停藥後藥效還會持續數週。排任何手術或侵入性處置前，都要先通知團隊。

</details>

**Q8.** ALK 陽性肺癌病人使用 lorlatinib 中，因為懷疑肺結核，感染科開立含 rifampin 的處方。專師核對用藥時應該怎麼做？

A. 兩藥沒有交互作用，可以併用　B. 把 lorlatinib 劑量加倍以補償濃度下降　C. 請病人把兩種藥間隔 12 小時服用　D. 立即聯絡主治醫師、感染科與藥師：lorlatinib 與強效 CYP3A 誘導劑併用屬禁忌，有嚴重肝毒性風險

<details>
<summary>答案與詳解</summary>

**答案：D**。12 位健康受試者併用 rifampin 與 lorlatinib，10 位出現嚴重肝毒性，美國仿單列為禁忌（Pfizer, 2026）。B 是把 osimertinib 的規則（美國仿單：併用強效誘導劑時加到 160 mg；AstraZeneca, 2026）套錯藥。誘導劑的處理因藥而異，專師不自行停藥或改劑量，但要把處方攔下來。

</details>

**Q9.** 一位服用口服 TKI 的病人因胃食道逆流被開了 PPI。這個組合可能出問題的主要機轉是？

A. PPI 誘導 CYP3A4，加速 TKI 代謝　B. 多數口服 TKI 是弱鹼，胃內 pH 上升後溶解度下降、吸收減少，暴露量可能不足　C. PPI 與 TKI 競爭血漿蛋白結合　D. PPI 會延長 QT，與 TKI 加成

<details>
<summary>答案與詳解</summary>

**答案：B**。多數口服標靶藥是弱鹼，溶解度隨 pH 改變；胃酸抑制劑把胃內 pH 從約 1 拉到約 4，溶解度在這個範圍變化大的藥受影響最大（Budha et al., 2012）。各藥要不要避開、怎麼錯開時間，規則不同，見肺癌章 5.4；pazopanib 的美國仿單直接要求避免（Novartis, 2025）。

</details>

**Q10.** Trastuzumab 每 3 週給法的第一劑是 8 mg/kg，之後是 6 mg/kg。第一劑給比較高的主要理由是？

A. 第一劑的輸注反應比較少，可以多給　B. 腫瘤一開始比較大，需要較高劑量　C. 抗體半衰期長，照維持劑量要很久才到穩定濃度；負載劑量讓血中濃度一開始就達標　D. 為了誘導免疫耐受

<details>
<summary>答案與詳解</summary>

**答案：C**。Trastuzumab 的半衰期約 18–27 天；8 → 6 mg/kg 的給法在第 1 週期結束時谷濃度就超過 20 µg/mL（Leyland-Jones et al., 2003），而穩定狀態大約要 12 週才達到（美國仿單；Genentech, 2026）。這是藥動學上的理由，和腫瘤大小無關。

</details>

**Q11.** EGFR L858R 肺腺癌病人使用 afatinib 14 個月後，CT 顯示肺部病灶變大。下一步最適當的是？

A. 重新取得腫瘤資訊（再切片或驗血中腫瘤 DNA），確認是否有 T790M 或其他抗藥機轉、組織型是否改變　B. 直接改用另一個第二代 EGFR TKI　C. 直接改成免疫治療單藥　D. 把 afatinib 劑量加倍

<details>
<summary>答案與詳解</summary>

**答案：A**。第一、二代 EGFR TKI 抗藥後，約一半的病人出現 T790M，另有 MET 放大與小細胞轉化（14%）等機轉（Sequist et al., 2011）。T790M 陽性者用 osimertinib 的 PFS 為 10.1 對 4.4 個月（Mok et al., 2017）；小細胞轉化則要換成小細胞肺癌的治療。不先確認機轉就換藥，可能選錯方向。

</details>

**Q12.** PIK3CA 突變的轉移性乳癌病人開始 alpelisib ＋ fulvestrant 第 12 天，空腹血糖從 98 上升到 262 mg/dL，沒有酮酸中毒的表現。關於這個毒性，下列敘述何者最正確？

A. 這是對 alpelisib 過敏，應永久停藥　B. 這是 fulvestrant 的副作用，與 alpelisib 無關　C. 這種高血糖通常在用藥半年後才出現，目前應另找原因　D. 這是抑制 PI3Kα（胰島素訊號的一部分）造成的靶點毒性，多在前兩週出現，依分級處置並以 metformin 為主要用藥

<details>
<summary>答案與詳解</summary>

**答案：D**。p110α 負責細胞對胰島素的幾乎所有反應，抑制它會讓肝臟釋出葡萄糖、周邊組織無法攝取（Hopkins et al., 2018）。SOLAR-1 中 3–4 級高血糖 36.6%（André et al., 2019），3 級以上高血糖的中位發生時間是 15 天，發生高血糖者 87.1% 使用 metformin 處理（Rugo et al., 2020）。分級門檻與暫停規則見乳癌章 6.6。

</details>

**Q13.** 一位轉移性 GIST 病人的基因報告為 PDGFRA exon 18 D842V 突變。第一線藥物應選？

A. Imatinib 400 mg，因為所有 GIST 第一線都用 imatinib　B. Avapritinib，因為 D842V 對 imatinib 等一般 TKI 高度抗藥　C. Sunitinib，因為它是多靶點 TKI　D. Pazopanib，因為它用於肉瘤

<details>
<summary>答案與詳解</summary>

**答案：B**。PDGFRA D842V 的 GIST 對一般 TKI 高度抗藥；avapritinib 在這個族群的反應率 88%（Heinrich et al., 2020）。這是「同一種腫瘤、不同基因型用不同藥」的例子：KIT exon 11 對 imatinib 的部分反應率 83.5%，沒有 KIT 或 PDGFRA 突變者為 0%（Heinrich et al., 2003）。Avapritinib 要注意顱內出血與認知影響（美國仿單；Blueprint Medicines, 2026）。

</details>

**Q14.** 三個 CDK4/6 抑制劑的代表性毒性與監測，下列配對何者正確？

A. Palbociclib：腹瀉為主，不需驗血球　B. Abemaciclib：QT 延長為主，需在第 14 天做心電圖　C. Ribociclib：QT 延長與肝毒性，開始前與第 1 週期約第 14 天做心電圖，且避免與 tamoxifen 併用　D. 三者毒性相同，監測方式可以互換

<details>
<summary>答案與詳解</summary>

**答案：C**。Ribociclib 的美國仿單要求 QTcF <450 ms 才開始、基線與第 1 週期約第 14 天做心電圖，並避免併用 tamoxifen（Novartis, 2026）。Palbociclib 的標誌是嗜中性球低下（3–4 級 66.4%；Finn et al., 2016）；abemaciclib 的標誌是腹瀉（81.3%；Goetz et al., 2017）。

</details>

**Q15.** 關於標靶治療試驗的「PFS 與 OS」，下列何者正確？

A. POLO 試驗中 olaparib 維持治療延長了 PFS（7.4 對 3.8 個月），但最終 OS 沒有顯著差異　B. PALOMA-2 證實 palbociclib 顯著延長 OS　C. 只要 PFS 的 HR 小於 0.6，OS 一定會顯著改善　D. PALETTE 證實 pazopanib 顯著延長軟組織肉瘤病人的 OS

<details>
<summary>答案與詳解</summary>

**答案：A**。POLO 的 PFS HR 0.53，最終 OS 19.0 對 19.2 個月（HR 0.83），無顯著差異（Golan et al., 2019；Kindler et al., 2022）。PALOMA-2 的 OS 為 53.9 對 51.2 個月（HR 0.96）（Slamon et al., 2024）；PALETTE 的 OS HR 0.86 也不顯著（van der Graaf et al., 2012）。PFS 改善不保證 OS 改善，答題時要講到試驗名。

</details>

**Q16.** 轉移性大腸直腸癌病人的腫瘤帶 KRAS 突變，為什麼抗 EGFR 抗體 cetuximab 對他沒有好處？

A. KRAS 突變會讓 cetuximab 被快速代謝　B. KRAS 突變的腫瘤不表現 EGFR　C. Cetuximab 只對肺癌有效　D. KRAS 在 EGFR 的下游，自己已經持續活化；擋住上游的受體，訊號照樣往下傳

<details>
<summary>答案與詳解</summary>

**答案：D**。訊號的順序是受體 → RAS → RAF → MEK → ERK。KRAS 突變的腫瘤用 cetuximab，存活與最佳支持療法沒有差別（HR 0.98）；KRAS 野生型才有好處（HR 0.55）（Karapetis et al., 2008）。這是「用 biomarker 排除病人」的例子，也說明為什麼要另外開發直接抑制 RAS 的藥（Ostrem et al., 2013）。

</details>

---

## 11. 參考文獻

APA 第 7 版格式。期刊論文都以 PubMed 資料核對過作者、年份、卷期頁碼與 DOI；仿單以 2026-11-11 查到的版本為準。

André, F., Ciruelos, E., Rubovszky, G., Campone, M., Loibl, S., Rugo, H. S., Iwata, H., Conte, P., Mayer, I. A., Kaufman, B., Yamashita, T., Lu, Y.-S., Inoue, K., Takahashi, M., Pápai, Z., Longin, A.-S., Mills, D., Wilke, C., Hirawat, S., . . . SOLAR-1 Study Group (2019). Alpelisib for PIK3CA-mutated, hormone receptor-positive advanced breast cancer. *New England Journal of Medicine, 380*(20), 1929–1940. https://doi.org/10.1056/NEJMoa1813904（PMID: 31091374）

Antonescu, C. R., Besmer, P., Guo, T., Arkun, K., Hom, G., Koryotowski, B., Leversha, M. A., Jeffrey, P. D., Desantis, D., Singer, S., Brennan, M. F., Maki, R. G., & DeMatteo, R. P. (2005). Acquired resistance to imatinib in gastrointestinal stromal tumor occurs through secondary gene mutation. *Clinical Cancer Research, 11*(11), 4182–4190. https://doi.org/10.1158/1078-0432.CCR-04-2245（PMID: 15930355）

AstraZeneca Pharmaceuticals LP. (2025). *LYNPARZA (olaparib) tablets: Prescribing information* (effective 2025-07-10). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=741ff3e3-dc1a-45a6-84e5-2481b27131aa

AstraZeneca Pharmaceuticals LP. (2026). *TAGRISSO (osimertinib) tablets: Prescribing information* (effective 2026-09-14). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=5e81b4a7-b971-45e1-9c31-29cea8c87ce7

Bardia, A., Hurvitz, S. A., Tolaney, S. M., Loirat, D., Punie, K., Oliveira, M., Brufsky, A., Sardesai, S. D., Kalinsky, K., Zelnak, A. B., Weaver, R., Traina, T., Dalenc, F., Aftimos, P., Lynce, F., Diab, S., Cortés, J., O'Shaughnessy, J., Diéras, V., . . . ASCENT Clinical Trial Investigators (2021). Sacituzumab govitecan in metastatic triple-negative breast cancer. *New England Journal of Medicine, 384*(16), 1529–1541. https://doi.org/10.1056/NEJMoa2028485（PMID: 33882206）

Bardia, A., Jhaveri, K., Im, S.-A., Pernas, S., De Laurentiis, M., Wang, S., Martínez Jañez, N., Borges, G., Cescon, D. W., Hattori, M., Lu, Y.-S., Hamilton, E., Zhang, Q., Tsurutani, J., Kalinsky, K., Rubini Liedke, P. E., Xu, L., Fairhurst, R. M., Khan, S., . . . TROPION-Breast01 Investigators (2025). Datopotamab deruxtecan versus chemotherapy in previously treated inoperable/metastatic hormone receptor-positive human epidermal growth factor receptor 2-negative breast cancer: Primary results from TROPION-Breast01. *Journal of Clinical Oncology, 43*(3), 285–296. https://doi.org/10.1200/JCO.24.00920（PMID: 39265124）

Baselga, J., Campone, M., Piccart, M., Burris, H. A., III, Rugo, H. S., Sahmoud, T., Noguchi, S., Gnant, M., Pritchard, K. I., Lebrun, F., Beck, J. T., Ito, Y., Yardley, D., Deleu, I., Perez, A., Bachelot, T., Vittori, L., Xu, Z., Mukhopadhyay, P., . . . Hortobagyi, G. N. (2012). Everolimus in postmenopausal hormone-receptor-positive advanced breast cancer. *New England Journal of Medicine, 366*(6), 520–529. https://doi.org/10.1056/NEJMoa1109653（PMID: 22149876）

Bayer HealthCare Pharmaceuticals Inc. (2026). *STIVARGA (regorafenib) tablets: Prescribing information* (effective 2026-02-09). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=824f19c9-0546-4a8a-8d8f-c4055c04f7c7

Blay, J.-Y., Serrano, C., Heinrich, M. C., Zalcberg, J., Bauer, S., Gelderblom, H., Schöffski, P., Jones, R. L., Attia, S., D'Amato, G., Chi, P., Reichardt, P., Meade, J., Shi, K., Ruiz-Soto, R., George, S., & von Mehren, M. (2020). Ripretinib in patients with advanced gastrointestinal stromal tumours (INVICTUS): A double-blind, randomised, placebo-controlled, phase 3 trial. *The Lancet Oncology, 21*(7), 923–934. https://doi.org/10.1016/S1470-2045(20)30168-6（PMID: 32511981）

Blueprint Medicines Corporation. (2026). *AYVAKIT (avapritinib) tablets: Prescribing information* (effective 2026-10-20). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=645c887c-8cd4-4623-8da9-ac223d71a8b9

Bryant, H. E., Schultz, N., Thomas, H. D., Parker, K. M., Flower, D., Lopez, E., Kyle, S., Meuth, M., Curtin, N. J., & Helleday, T. (2005). Specific killing of BRCA2-deficient tumours with inhibitors of poly(ADP-ribose) polymerase. *Nature, 434*(7035), 913–917. https://doi.org/10.1038/nature03443（PMID: 15829966）

Budha, N. R., Frymoyer, A., Smelick, G. S., Jin, J. Y., Yago, M. R., Dresser, M. J., Holden, S. N., Benet, L. Z., & Ware, J. A. (2012). Drug absorption interactions between oral targeted anticancer agents and PPIs: Is pH-dependent solubility the Achilles heel of targeted therapy?. *Clinical Pharmacology & Therapeutics, 92*(2), 203–213. https://doi.org/10.1038/clpt.2012.73（PMID: 22739140）

Carter, P., Presta, L., Gorman, C. M., Ridgway, J. B., Henner, D., Wong, W. L., Rowland, A. M., Kotts, C., Carver, M. E., & Shepard, H. M. (1992). Humanization of an anti-p185HER2 antibody for human cancer therapy. *Proceedings of the National Academy of Sciences of the United States of America, 89*(10), 4285–4289. https://doi.org/10.1073/pnas.89.10.4285（PMID: 1350088）

Chan, A., Delaloge, S., Holmes, F. A., Moy, B., Iwata, H., Harvey, V. J., Robert, N. J., Silovski, T., Gokmen, E., von Minckwitz, G., Ejlertsen, B., Chia, S. K. L., Mansi, J., Barrios, C. H., Gnant, M., Buyse, M., Gore, I., Smith, J., II, Harker, G., . . . ExteNET Study Group (2016). Neratinib after trastuzumab-based adjuvant therapy in patients with HER2-positive breast cancer (ExteNET): A multicentre, randomised, double-blind, placebo-controlled, phase 3 trial. *The Lancet Oncology, 17*(3), 367–377. https://doi.org/10.1016/S1470-2045(15)00551-3（PMID: 26874901）

Cho, B. C., Lu, S., Felip, E., Spira, A. I., Girard, N., Lee, J.-S., Lee, S.-H., Ostapenko, Y., Danchaivijitr, P., Liu, B., Alip, A., Korbenfeld, E., Mourão Dias, J., Besse, B., Lee, K.-H., Xiong, H., How, S.-H., Cheng, Y., Chang, G.-C., . . . MARIPOSA Investigators (2024). Amivantamab plus lazertinib in previously untreated EGFR-mutated advanced NSCLC. *New England Journal of Medicine, 391*(16), 1486–1498. https://doi.org/10.1056/NEJMoa2403614（PMID: 38924756）

Cho, B. C., Li, W., Spira, A. I., Sauder, M., Feldman, J., Bozorgmehr, F., Mak, M., Smith, J., Voon, P. J., Liu, B., Tian, P., Tan, J.-L., Yang, C.-T., Shih, J.-Y., Karadurmus, N., Cundom, J. E., Bertollo, G., Cicin, I., Nieva, J., . . . Girard, N. (2025). Enhanced versus standard dermatologic management with amivantamab-lazertinib in EGFR-mutated advanced NSCLC: The COCOON global randomized controlled trial. *Journal of Thoracic Oncology, 20*(10), 1517–1530. https://doi.org/10.1016/j.jtho.2025.07.117（PMID: 40923969）

Clynes, R. A., Towers, T. L., Presta, L. G., & Ravetch, J. V. (2000). Inhibitory Fc receptors modulate in vivo cytotoxicity against tumor targets. *Nature Medicine, 6*(4), 443–446. https://doi.org/10.1038/74704（PMID: 10742152）

Cohen, M. H., Williams, G. A., Sridhara, R., Chen, G., & Pazdur, R. (2003). FDA drug approval summary: Gefitinib (ZD1839) (Iressa) tablets. *The Oncologist, 8*(4), 303–306. https://doi.org/10.1634/theoncologist.8-4-303（PMID: 12897327）

Dagher, R., Cohen, M., Williams, G., Rothmann, M., Gobburu, J., Robbie, G., Rahman, A., Chen, G., Staten, A., Griebel, D., & Pazdur, R. (2002). Approval summary: Imatinib mesylate in the treatment of metastatic and/or unresectable malignant gastrointestinal stromal tumors. *Clinical Cancer Research, 8*(10), 3034–3038.（PMID: 12374669）

Daiichi Sankyo, Inc. (2026). *ENHERTU (fam-trastuzumab deruxtecan-nxki) for injection: Prescribing information* (effective 2026-05-15). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=7e67e73e-ddf4-4e4d-8b50-09d7514910b6

de Langen, A. J., Johnson, M. L., Mazieres, J., Dingemans, A.-M. C., Mountzios, G., Pless, M., Wolf, J., Schuler, M., Lena, H., Skoulidis, F., Yoneshima, Y., Kim, S.-W., Linardou, H., Novello, S., van der Wekken, A. J., Chen, Y., Peters, S., Felip, E., Solomon, B. J., . . . CodeBreaK 200 Investigators (2023). Sotorasib versus docetaxel for previously treated non-small-cell lung cancer with KRASG12C mutation: A randomised, open-label, phase 3 trial. *The Lancet, 401*(10378), 733–746. https://doi.org/10.1016/S0140-6736(23)00221-0（PMID: 36764316）

Demetri, G. D., von Mehren, M., Blanke, C. D., Van den Abbeele, A. D., Eisenberg, B., Roberts, P. J., Heinrich, M. C., Tuveson, D. A., Singer, S., Janicek, M., Fletcher, J. A., Silverman, S. G., Silberman, S. L., Capdeville, R., Kiese, B., Peng, B., Dimitrijevic, S., Druker, B. J., Corless, C., . . . Joensuu, H. (2002). Efficacy and safety of imatinib mesylate in advanced gastrointestinal stromal tumors. *New England Journal of Medicine, 347*(7), 472–480. https://doi.org/10.1056/NEJMoa020461（PMID: 12181401）

Demetri, G. D., van Oosterom, A. T., Garrett, C. R., Blackstein, M. E., Shah, M. H., Verweij, J., McArthur, G., Judson, I. R., Heinrich, M. C., Morgan, J. A., Desai, J., Fletcher, C. D., George, S., Bello, C. L., Huang, X., Baum, C. M., & Casali, P. G. (2006). Efficacy and safety of sunitinib in patients with advanced gastrointestinal stromal tumour after failure of imatinib: A randomised controlled trial. *The Lancet, 368*(9544), 1329–1338. https://doi.org/10.1016/S0140-6736(06)69446-4（PMID: 17046465）

Demetri, G. D., Reichardt, P., Kang, Y.-K., Blay, J.-Y., Rutkowski, P., Gelderblom, H., Hohenberger, P., Leahy, M., von Mehren, M., Joensuu, H., Badalamenti, G., Blackstein, M., Le Cesne, A., Schöffski, P., Maki, R. G., Bauer, S., Nguyen, B. B., Xu, J., Nishida, T., . . . GRID study investigators (2013). Efficacy and safety of regorafenib for advanced gastrointestinal stromal tumours after failure of imatinib and sunitinib (GRID): An international, multicentre, randomised, placebo-controlled, phase 3 trial. *The Lancet, 381*(9863), 295–302. https://doi.org/10.1016/S0140-6736(12)61857-1（PMID: 23177515）

Drago, J. Z., Modi, S., & Chandarlapaty, S. (2021). Unlocking the potential of antibody-drug conjugates for cancer therapy. *Nature Reviews Clinical Oncology, 18*(6), 327–344. https://doi.org/10.1038/s41571-021-00470-8（PMID: 33558752）

Drilon, A., Laetsch, T. W., Kummar, S., DuBois, S. G., Lassen, U. N., Demetri, G. D., Nathenson, M., Doebele, R. C., Farago, A. F., Pappo, A. S., Turpin, B., Dowlati, A., Brose, M. S., Mascarenhas, L., Federman, N., Berlin, J., El-Deiry, W. S., Baik, C., Deeken, J., . . . Hyman, D. M. (2018). Efficacy of larotrectinib in TRK fusion-positive cancers in adults and children. *New England Journal of Medicine, 378*(8), 731–739. https://doi.org/10.1056/NEJMoa1714448（PMID: 29466156）

Drilon, A., Oxnard, G. R., Tan, D. S. W., Loong, H. H. F., Johnson, M., Gainor, J., McCoach, C. E., Gautschi, O., Besse, B., Cho, B. C., Peled, N., Weiss, J., Kim, Y.-J., Ohe, Y., Nishio, M., Park, K., Patel, J., Seto, T., Sakamoto, T., . . . Subbiah, V. (2020). Efficacy of selpercatinib in RET fusion-positive non-small-cell lung cancer. *New England Journal of Medicine, 383*(9), 813–824. https://doi.org/10.1056/NEJMoa2005653（PMID: 32846060）

Druker, B. J., Talpaz, M., Resta, D. J., Peng, B., Buchdunger, E., Ford, J. M., Lydon, N. B., Kantarjian, H., Capdeville, R., Ohno-Jones, S., & Sawyers, C. L. (2001). Efficacy and safety of a specific inhibitor of the BCR-ABL tyrosine kinase in chronic myeloid leukemia. *New England Journal of Medicine, 344*(14), 1031–1037. https://doi.org/10.1056/NEJM200104053441401（PMID: 11287972）

Engelman, J. A., Zejnullahu, K., Mitsudomi, T., Song, Y., Hyland, C., Park, J. O., Lindeman, N., Gale, C.-M., Zhao, X., Christensen, J., Kosaka, T., Holmes, A. J., Rogers, A. M., Cappuzzo, F., Mok, T., Lee, C., Johnson, B. E., Cantley, L. C., & Jänne, P. A. (2007). MET amplification leads to gefitinib resistance in lung cancer by activating ERBB3 signaling. *Science, 316*(5827), 1039–1043. https://doi.org/10.1126/science.1141478（PMID: 17463250）

European Medicines Agency. (2025). *Alecensa: EPAR – Product information* (Annex I, Summary of product characteristics; PDF dated 2025-11-05). Retrieved November 11, 2026, from https://www.ema.europa.eu/en/documents/product-information/alecensa-epar-product-information_en.pdf

Farmer, H., McCabe, N., Lord, C. J., Tutt, A. N. J., Johnson, D. A., Richardson, T. B., Santarosa, M., Dillon, K. J., Hickson, I., Knights, C., Martin, N. M. B., Jackson, S. P., Smith, G. C. M., & Ashworth, A. (2005). Targeting the DNA repair defect in BRCA mutant cells as a therapeutic strategy. *Nature, 434*(7035), 917–921. https://doi.org/10.1038/nature03445（PMID: 15829967）

Finn, R. S., Dering, J., Conklin, D., Kalous, O., Cohen, D. J., Desai, A. J., Ginther, C., Atefi, M., Chen, I., Fowst, C., Los, G., & Slamon, D. J. (2009). PD 0332991, a selective cyclin D kinase 4/6 inhibitor, preferentially inhibits proliferation of luminal estrogen receptor-positive human breast cancer cell lines in vitro. *Breast Cancer Research, 11*(5), Article R77. https://doi.org/10.1186/bcr2419（PMID: 19874578）

Finn, R. S., Martin, M., Rugo, H. S., Jones, S., Im, S.-A., Gelmon, K., Harbeck, N., Lipatov, O. N., Walshe, J. M., Moulder, S., Gauthier, E., Lu, D. R., Randolph, S., Diéras, V., & Slamon, D. J. (2016). Palbociclib and letrozole in advanced breast cancer. *New England Journal of Medicine, 375*(20), 1925–1936. https://doi.org/10.1056/NEJMoa1607303（PMID: 27959613）

Folkman, J. (1971). Tumor angiogenesis: Therapeutic implications. *New England Journal of Medicine, 285*(21), 1182–1186. https://doi.org/10.1056/NEJM197111182852108（PMID: 4938153）

Food and Drug Administration. (2001, May 10). *NDA 21-335 approval letter: Gleevec (imatinib mesylate) capsules*. U.S. Department of Health and Human Services. https://www.accessdata.fda.gov/drugsatfda_docs/appletter/2001/21335ltr.pdf（核准日期依 Drugs@FDA 的 NDA 021335 紀錄，2026-11-11 查詢）

Food and Drug Administration. (2002, February 1). *NDA 21-335/S-001 approval letter: Gleevec (imatinib mesylate) capsules, gastrointestinal stromal tumors*. U.S. Department of Health and Human Services. https://www.accessdata.fda.gov/drugsatfda_docs/appletter/2002/21335s001ltr.pdf（核准日期依 Drugs@FDA 的 NDA 021335 紀錄，2026-11-11 查詢）

Gainor, J. F., Dardaei, L., Yoda, S., Friboulet, L., Leshchiner, I., Katayama, R., Dagogo-Jack, I., Gadgeel, S., Schultz, K., Singh, M., Chin, E., Parks, M., Lee, D., DiCecca, R. H., Lockerman, E., Huynh, T., Logan, J., Ritterhouse, L. L., Le, L. P., . . . Shaw, A. T. (2016). Molecular mechanisms of resistance to first- and second-generation ALK inhibitors in ALK-rearranged lung cancer. *Cancer Discovery, 6*(10), 1118–1133. https://doi.org/10.1158/2159-8290.CD-16-0596（PMID: 27432227）

Garon, E. B., Ciuleanu, T.-E., Arrieta, O., Prabhash, K., Syrigos, K. N., Goksel, T., Park, K., Gorbunova, V., Kowalyszyn, R. D., Pikiel, J., Czyzewicz, G., Orlov, S. V., Lewanski, C. R., Thomas, M., Bidoli, P., Dakhil, S., Gans, S., Kim, J.-H., Grigorescu, A., . . . Pérol, M. (2014). Ramucirumab plus docetaxel versus placebo plus docetaxel for second-line treatment of stage IV non-small-cell lung cancer after disease progression on platinum-based therapy (REVEL): A multicentre, double-blind, randomised phase 3 trial. *The Lancet, 384*(9944), 665–673. https://doi.org/10.1016/S0140-6736(14)60845-X（PMID: 24933332）

Genentech, Inc. (2025). *AVASTIN (bevacizumab) injection: Prescribing information* (effective 2025-01-06). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=939b5d1f-9fb2-4499-80ef-0607aa6b114e

Genentech, Inc. (2026). *HERCEPTIN (trastuzumab) for injection: Prescribing information* (effective 2026-05-29). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=492dbdb2-077e-4064-bff3-372d6af0a7a2

Geyer, C. E., Forster, J., Lindquist, D., Chan, S., Romieu, C. G., Pienkowski, T., Jagiello-Gruszfeld, A., Crown, J., Chan, A., Kaufman, B., Skarlos, D., Campone, M., Davidson, N., Berger, M., Oliva, C., Rubin, S. D., Stein, S., & Cameron, D. (2006). Lapatinib plus capecitabine for HER2-positive advanced breast cancer. *New England Journal of Medicine, 355*(26), 2733–2743. https://doi.org/10.1056/NEJMoa064320（PMID: 17192538）

Goetz, M. P., Toi, M., Campone, M., Sohn, J., Paluch-Shimon, S., Huober, J., Park, I. H., Trédan, O., Chen, S.-C., Manso, L., Freedman, O. C., Garnica Jaliffe, G., Forrester, T., Frenzel, M., Barriga, S., Smith, I. C., Bourayou, N., & Di Leo, A. (2017). MONARCH 3: Abemaciclib as initial therapy for advanced breast cancer. *Journal of Clinical Oncology, 35*(32), 3638–3646. https://doi.org/10.1200/JCO.2017.75.6155（PMID: 28968163）

Golan, T., Hammel, P., Reni, M., Van Cutsem, E., Macarulla, T., Hall, M. J., Park, J.-O., Hochhauser, D., Arnold, D., Oh, D.-Y., Reinacher-Schick, A., Tortora, G., Algül, H., O'Reilly, E. M., McGuinness, D., Cui, K. Y., Schlienger, K., Locker, G. Y., & Kindler, H. L. (2019). Maintenance olaparib for germline BRCA-mutated metastatic pancreatic cancer. *New England Journal of Medicine, 381*(4), 317–327. https://doi.org/10.1056/NEJMoa1903387（PMID: 31157963）

Goto, K., Goto, Y., Kubo, T., Ninomiya, K., Kim, S.-W., Planchard, D., Ahn, M.-J., Smit, E. F., de Langen, A. J., Pérol, M., Pons-Tostivint, E., Novello, S., Hayashi, H., Shimizu, J., Kim, D.-W., Kuo, C.-H., Yang, J. C.-H., Pereira, K., Cheng, F.-C., . . . Jänne, P. A. (2023). Trastuzumab deruxtecan in patients with HER2-mutant metastatic non-small-cell lung cancer: Primary results from the randomized, phase II DESTINY-Lung02 trial. *Journal of Clinical Oncology, 41*(31), 4852–4863. https://doi.org/10.1200/JCO.23.01361（PMID: 37694347）

Heinrich, M. C., Corless, C. L., Demetri, G. D., Blanke, C. D., von Mehren, M., Joensuu, H., McGreevey, L. S., Chen, C.-J., Van den Abbeele, A. D., Druker, B. J., Kiese, B., Eisenberg, B., Roberts, P. J., Singer, S., Fletcher, C. D. M., Silberman, S., Dimitrijevic, S., & Fletcher, J. A. (2003). Kinase mutations and imatinib response in patients with metastatic gastrointestinal stromal tumor. *Journal of Clinical Oncology, 21*(23), 4342–4349. https://doi.org/10.1200/JCO.2003.04.190（PMID: 14645423）

Heinrich, M. C., Jones, R. L., von Mehren, M., Schöffski, P., Serrano, C., Kang, Y.-K., Cassier, P. A., Mir, O., Eskens, F., Tap, W. D., Rutkowski, P., Chawla, S. P., Trent, J., Tugnait, M., Evans, E. K., Lauz, T., Zhou, T., Roche, M., Wolf, B. B., . . . George, S. (2020). Avapritinib in advanced PDGFRA D842V-mutant gastrointestinal stromal tumour (NAVIGATOR): A multicentre, open-label, phase 1 trial. *The Lancet Oncology, 21*(7), 935–946. https://doi.org/10.1016/S1470-2045(20)30269-2（PMID: 32615108）

Hendrikx, J. J. M. A., Haanen, J. B. A. G., Voest, E. E., Schellens, J. H. M., Huitema, A. D. R., & Beijnen, J. H. (2017). Fixed dosing of monoclonal antibodies in oncology. *The Oncologist, 22*(10), 1212–1221. https://doi.org/10.1634/theoncologist.2017-0167（PMID: 28754722）

Hirota, S., Isozaki, K., Moriyama, Y., Hashimoto, K., Nishida, T., Ishiguro, S., Kawano, K., Hanada, M., Kurata, A., Takeda, M., Muhammad Tunio, G., Matsuzawa, Y., Kanakura, Y., Shinomura, Y., & Kitamura, Y. (1998). Gain-of-function mutations of c-kit in human gastrointestinal stromal tumors. *Science, 279*(5350), 577–580. https://doi.org/10.1126/science.279.5350.577（PMID: 9438854）

Hopkins, B. D., Pauli, C., Du, X., Wang, D. G., Li, X., Wu, D., Amadiume, S. C., Goncalves, M. D., Hodakoski, C., Lundquist, M. R., Bareja, R., Ma, Y., Harris, E. M., Sboner, A., Beltran, H., Rubin, M. A., Mukherjee, S., & Cantley, L. C. (2018). Suppression of insulin feedback enhances the efficacy of PI3K inhibitors. *Nature, 560*(7719), 499–503. https://doi.org/10.1038/s41586-018-0343-4（PMID: 30051890）

Hortobagyi, G. N., Stemmer, S. M., Burris, H. A., Yap, Y.-S., Sonke, G. S., Hart, L., Campone, M., Petrakova, K., Winer, E. P., Janni, W., Conte, P., Cameron, D. A., André, F., Arteaga, C. L., Zarate, J. P., Chakravartty, A., Taran, T., Le Gac, F., Serra, P., & O'Shaughnessy, J. (2022). Overall survival with ribociclib plus letrozole in advanced breast cancer. *New England Journal of Medicine, 386*(10), 942–950. https://doi.org/10.1056/NEJMoa2114663（PMID: 35263519）

Hsu, K.-H., Ho, C.-C., Hsia, T.-C., Tseng, J.-S., Su, K.-Y., Wu, M.-F., Chiu, K.-L., Yang, T.-Y., Chen, K.-C., Ooi, H., Wu, T.-C., Chen, H.-J., Chen, H.-Y., Chang, C.-S., Hsu, C.-P., Hsia, J.-Y., Chuang, C.-Y., Lin, C.-H., Chen, J. J. W., . . . Chang, G.-C. (2015). Identification of five driver gene mutations in patients with treatment-naïve lung adenocarcinoma in Taiwan. *PLoS ONE, 10*(3), Article e0120852. https://doi.org/10.1371/journal.pone.0120852（PMID: 25789627）

Hurvitz, S. A., Hegg, R., Chung, W.-P., Im, S.-A., Jacot, W., Ganju, V., Chiu, J. W. Y., Xu, B., Hamilton, E., Madhusudan, S., Iwata, H., Altintas, S., Henning, J.-W., Curigliano, G., Perez-Garcia, J. M., Kim, S.-B., Petry, V., Huang, C.-S., Li, W., . . . Cortés, J. (2023). Trastuzumab deruxtecan versus trastuzumab emtansine in patients with HER2-positive metastatic breast cancer: Updated results from DESTINY-Breast03, a randomised, open-label, phase 3 trial. *The Lancet, 401*(10371), 105–117. https://doi.org/10.1016/S0140-6736(22)02420-5（PMID: 36495879）

Hurwitz, H., Fehrenbacher, L., Novotny, W., Cartwright, T., Hainsworth, J., Heim, W., Berlin, J., Baron, A., Griffing, S., Holmgren, E., Ferrara, N., Fyfe, G., Rogers, B., Ross, R., & Kabbinavar, F. (2004). Bevacizumab plus irinotecan, fluorouracil, and leucovorin for metastatic colorectal cancer. *New England Journal of Medicine, 350*(23), 2335–2342. https://doi.org/10.1056/NEJMoa032691（PMID: 15175435）

Imai, K., & Takaoka, A. (2006). Comparing antibody and small-molecule therapies for cancer. *Nature Reviews Cancer, 6*(9), 714–727. https://doi.org/10.1038/nrc1913（PMID: 16929325）

Jänne, P. A., Planchard, D., Kobayashi, K., Yang, J. C.-H., Liu, Y., Valdiviezo, N., Kim, T. M., Jiang, L., Kagamu, H., Yanagitani, N., Wang, J., Biswas, B., Poltoratskiy, A., Neron, Y., Rojas, C., Koubkova, L., Escriu, C., Ezeife, D. A., Mann, H., . . . FLAURA2 Investigators (2026). Survival with osimertinib plus chemotherapy in EGFR-mutated advanced NSCLC. *New England Journal of Medicine, 394*(1), 27–38. https://doi.org/10.1056/NEJMoa2510308（PMID: 41104938）

Jhaveri, K. L., Im, S.-A., Saura, C., Loibl, S., Kalinsky, K., Schmid, P., Loi, S., Thanopoulou, E., Shankar, N., Jin, Y., Stout, T. J., Clark, T. D., Song, C., Juric, D., & Turner, N. C. (2025). Overall survival with inavolisib in PIK3CA-mutated advanced breast cancer. *New England Journal of Medicine, 393*(2), 151–161. https://doi.org/10.1056/NEJMoa2501796（PMID: 40454641）

Joensuu, H., Eriksson, M., Sundby Hall, K., Hartmann, J. T., Pink, D., Schütte, J., Ramadori, G., Hohenberger, P., Duyster, J., Al-Batran, S.-E., Schlemmer, M., Bauer, S., Wardelmann, E., Sarlomo-Rikala, M., Nilsson, B., Sihto, H., Monge, O. R., Bono, P., Kallio, R., . . . Reichardt, P. (2012). One vs three years of adjuvant imatinib for operable gastrointestinal stromal tumor: A randomized trial. *JAMA, 307*(12), 1265–1272. https://doi.org/10.1001/jama.2012.347（PMID: 22453568）

Johnston, S., Martin, M., O'Shaughnessy, J., Hegg, R., Tolaney, S. M., Guarneri, V., Del Mastro, L., Campone, M., Sohn, J., Boyle, F., Cortes, J., Rugo, H. S., Goetz, M. P., Hamilton, E. P., Huang, C.-S., Senkus, E., Cicin, I., Testa, L., Neven, P., . . . Harbeck, N. (2026). Overall survival with abemaciclib in early breast cancer. *Annals of Oncology, 37*(2), 155–165. https://doi.org/10.1016/j.annonc.2025.10.005（PMID: 41110697）

Karapetis, C. S., Khambata-Ford, S., Jonker, D. J., O'Callaghan, C. J., Tu, D., Tebbutt, N. C., Simes, R. J., Chalchal, H., Shapiro, J. D., Robitaille, S., Price, T. J., Shepherd, L., Au, H.-J., Langer, C., Moore, M. J., & Zalcberg, J. R. (2008). K-ras mutations and benefit from cetuximab in advanced colorectal cancer. *New England Journal of Medicine, 359*(17), 1757–1765. https://doi.org/10.1056/NEJMoa0804385（PMID: 18946061）

Kazandjian, D., Blumenthal, G. M., Chen, H.-Y., He, K., Patel, M., Justice, R., Keegan, P., & Pazdur, R. (2014). FDA approval summary: Crizotinib for the treatment of metastatic non-small cell lung cancer with anaplastic lymphoma kinase rearrangements. *The Oncologist, 19*(10), e5–e11. https://doi.org/10.1634/theoncologist.2014-0241（PMID: 25170012）

Keizer, R. J., Huitema, A. D. R., Schellens, J. H. M., & Beijnen, J. H. (2010). Clinical pharmacokinetics of therapeutic monoclonal antibodies. *Clinical Pharmacokinetics, 49*(8), 493–507. https://doi.org/10.2165/11531280-000000000-00000（PMID: 20608753）

Kindler, H. L., Hammel, P., Reni, M., Van Cutsem, E., Macarulla, T., Hall, M. J., Park, J. O., Hochhauser, D., Arnold, D., Oh, D.-Y., Reinacher-Schick, A., Tortora, G., Algül, H., O'Reilly, E. M., Bordia, S., McGuinness, D., Cui, K., Locker, G. Y., & Golan, T. (2022). Overall survival results from the POLO trial: A phase III study of active maintenance olaparib versus placebo for germline BRCA-mutated metastatic pancreatic cancer. *Journal of Clinical Oncology, 40*(34), 3929–3939. https://doi.org/10.1200/JCO.21.01604（PMID: 35834777）

Kobayashi, S., Boggon, T. J., Dayaram, T., Jänne, P. A., Kocher, O., Meyerson, M., Johnson, B. E., Eck, M. J., Tenen, D. G., & Halmos, B. (2005). EGFR mutation and resistance of non-small-cell lung cancer to gefitinib. *New England Journal of Medicine, 352*(8), 786–792. https://doi.org/10.1056/NEJMoa044238（PMID: 15728811）

Koch, K. M., Reddy, N. J., Cohen, R. B., Lewis, N. L., Whitehead, B., Mackay, K., Stead, A., Beelen, A. P., & Lewis, L. D. (2009). Effects of food on the relative bioavailability of lapatinib in cancer patients. *Journal of Clinical Oncology, 27*(8), 1191–1196. https://doi.org/10.1200/JCO.2008.18.3285（PMID: 19188677）

Köhler, G., & Milstein, C. (1975). Continuous cultures of fused cells secreting antibody of predefined specificity. *Nature, 256*(5517), 495–497. https://doi.org/10.1038/256495a0（PMID: 1172191）

Kwak, E. L., Bang, Y.-J., Camidge, D. R., Shaw, A. T., Solomon, B., Maki, R. G., Ou, S.-H. I., Dezube, B. J., Jänne, P. A., Costa, D. B., Varella-Garcia, M., Kim, W.-H., Lynch, T. J., Fidias, P., Stubbs, H., Engelman, J. A., Sequist, L. V., Tan, W., Gandhi, L., . . . Iafrate, A. J. (2010). Anaplastic lymphoma kinase inhibition in non-small-cell lung cancer. *New England Journal of Medicine, 363*(18), 1693–1703. https://doi.org/10.1056/NEJMoa1006448（PMID: 20979469）

Lacouture, M. E., Anadkat, M. J., Bensadoun, R.-J., Bryce, J., Chan, A., Epstein, J. B., Eaby-Sandy, B., Murphy, B. A., & MASCC Skin Toxicity Study Group (2011). Clinical practice guidelines for the prevention and treatment of EGFR inhibitor-associated dermatologic toxicities. *Supportive Care in Cancer, 19*(8), 1079–1095. https://doi.org/10.1007/s00520-011-1197-6（PMID: 21630130）

Lemmon, M. A., & Schlessinger, J. (2010). Cell signaling by receptor tyrosine kinases. *Cell, 141*(7), 1117–1134. https://doi.org/10.1016/j.cell.2010.06.011（PMID: 20602996）

Leonetti, A., Sharma, S., Minari, R., Perego, P., Giovannetti, E., & Tiseo, M. (2019). Resistance mechanisms to osimertinib in EGFR-mutated non-small cell lung cancer. *British Journal of Cancer, 121*(9), 725–737. https://doi.org/10.1038/s41416-019-0573-8（PMID: 31564718）

Leyland-Jones, B., Gelmon, K., Ayoub, J.-P., Arnold, A., Verma, S., Dias, R., & Ghahramani, P. (2003). Pharmacokinetics, safety, and efficacy of trastuzumab administered every three weeks in combination with paclitaxel. *Journal of Clinical Oncology, 21*(21), 3965–3971. https://doi.org/10.1200/JCO.2003.12.109（PMID: 14507946）

Litton, J. K., Rugo, H. S., Ettl, J., Hurvitz, S. A., Gonçalves, A., Lee, K.-H., Fehrenbacher, L., Yerushalmi, R., Mina, L. A., Martin, M., Roché, H., Im, Y.-H., Quek, R. G. W., Markova, D., Tudor, I. C., Hannah, A. L., Eiermann, W., & Blum, J. L. (2018). Talazoparib in patients with advanced breast cancer and a germline BRCA mutation. *New England Journal of Medicine, 379*(8), 753–763. https://doi.org/10.1056/NEJMoa1802905（PMID: 30110579）

Lu, S., Kato, T., Dong, X., Ahn, M.-J., Quang, L.-V., Soparattanapaisarn, N., Inoue, T., Wang, C.-L., Huang, M., Yang, J. C.-H., Cobo, M., Özgüroğlu, M., Casarini, I., Khiem, D.-V., Sriuranpong, V., Cronemberger, E., Takahashi, T., Runglodvatana, Y., Chen, M., . . . LAURA Trial Investigators (2024). Osimertinib after chemoradiotherapy in stage III EGFR-mutated NSCLC. *New England Journal of Medicine, 391*(7), 585–597. https://doi.org/10.1056/NEJMoa2402614（PMID: 38828946）

Lynch, T. J., Bell, D. W., Sordella, R., Gurubhagavatula, S., Okimoto, R. A., Brannigan, B. W., Harris, P. L., Haserlat, S. M., Supko, J. G., Haluska, F. G., Louis, D. N., Christiani, D. C., Settleman, J., & Haber, D. A. (2004). Activating mutations in the epidermal growth factor receptor underlying responsiveness of non-small-cell lung cancer to gefitinib. *New England Journal of Medicine, 350*(21), 2129–2139. https://doi.org/10.1056/NEJMoa040938（PMID: 15118073）

Modi, S., Jacot, W., Yamashita, T., Sohn, J., Vidal, M., Tokunaga, E., Tsurutani, J., Ueno, N. T., Prat, A., Chae, Y. S., Lee, K. S., Niikura, N., Park, Y. H., Xu, B., Wang, X., Gil-Gil, M., Li, W., Pierga, J.-Y., Im, S.-A., . . . DESTINY-Breast04 Trial Investigators (2022). Trastuzumab deruxtecan in previously treated HER2-low advanced breast cancer. *New England Journal of Medicine, 387*(1), 9–20. https://doi.org/10.1056/NEJMoa2203690（PMID: 35665782）

Mok, T. S., Wu, Y.-L., Thongprasert, S., Yang, C.-H., Chu, D.-T., Saijo, N., Sunpaweravong, P., Han, B., Margono, B., Ichinose, Y., Nishiwaki, Y., Ohe, Y., Yang, J.-J., Chewaskulyong, B., Jiang, H., Duffield, E. L., Watkins, C. L., Armour, A. A., & Fukuoka, M. (2009). Gefitinib or carboplatin-paclitaxel in pulmonary adenocarcinoma. *New England Journal of Medicine, 361*(10), 947–957. https://doi.org/10.1056/NEJMoa0810699（PMID: 19692680）

Mok, T. S., Wu, Y.-L., Ahn, M.-J., Garassino, M. C., Kim, H. R., Ramalingam, S. S., Shepherd, F. A., He, Y., Akamatsu, H., Theelen, W. S. M. E., Lee, C. K., Sebastian, M., Templeton, A., Mann, H., Marotti, M., Ghiorghiu, S., Papadimitrakopoulou, V. A., & AURA3 Investigators (2017). Osimertinib or platinum-pemetrexed in EGFR T790M-positive lung cancer. *New England Journal of Medicine, 376*(7), 629–640. https://doi.org/10.1056/NEJMoa1612674（PMID: 27959700）

Moore, M. J., Goldstein, D., Hamm, J., Figer, A., Hecht, J. R., Gallinger, S., Au, H. J., Murawa, P., Walde, D., Wolff, R. A., Campos, D., Lim, R., Ding, K., Clark, G., Voskoglou-Nomikos, T., Ptasynski, M., Parulekar, W., & National Cancer Institute of Canada Clinical Trials Group (2007). Erlotinib plus gemcitabine compared with gemcitabine alone in patients with advanced pancreatic cancer: A phase III trial of the National Cancer Institute of Canada Clinical Trials Group. *Journal of Clinical Oncology, 25*(15), 1960–1966. https://doi.org/10.1200/JCO.2006.07.9525（PMID: 17452677）

Morrison, S. L., Johnson, M. J., Herzenberg, L. A., & Oi, V. T. (1984). Chimeric human antibody molecules: Mouse antigen-binding domains with human constant region domains. *Proceedings of the National Academy of Sciences of the United States of America, 81*(21), 6851–6855. https://doi.org/10.1073/pnas.81.21.6851（PMID: 6436822）

Murthy, R. K., Loi, S., Okines, A., Paplomata, E., Hamilton, E., Hurvitz, S. A., Lin, N. U., Borges, V., Abramson, V., Anders, C., Bedard, P. L., Oliveira, M., Jakobsen, E., Bachelot, T., Shachar, S. S., Müller, V., Braga, S., Duhoux, F. P., Greil, R., . . . Winer, E. P. (2020). Tucatinib, trastuzumab, and capecitabine for HER2-positive metastatic breast cancer. *New England Journal of Medicine, 382*(7), 597–609. https://doi.org/10.1056/NEJMoa1914609（PMID: 31825569）

Nakajima, E. C., Drezner, N., Li, X., Mishra-Kalyani, P. S., Liu, Y., Zhao, H., Bi, Y., Liu, J., Rahman, A., Wearne, E., Ojofeitimi, I., Hotaki, L. T., Spillman, D., Pazdur, R., Beaver, J. A., & Singh, H. (2022). FDA approval summary: Sotorasib for KRAS G12C-mutated metastatic NSCLC. *Clinical Cancer Research, 28*(8), 1482–1486. https://doi.org/10.1158/1078-0432.CCR-21-3074（PMID: 34903582）

Novartis Pharmaceuticals Corporation. (2025). *VOTRIENT (pazopanib) tablets: Prescribing information* (effective 2025-12-16). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=eeaaaf38-fb86-4d9f-a19d-0f61daac2fd7

Novartis Pharmaceuticals Corporation. (2026). *KISQALI (ribociclib) tablets: Prescribing information* (effective 2026-07-01). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aaeaef94-f3f5-4367-8ea2-b181d7be2da8

Nowell, P. C. (2007). Discovery of the Philadelphia chromosome: A personal perspective. *The Journal of Clinical Investigation, 117*(8), 2033–2035. https://doi.org/10.1172/JCI31771（PMID: 17671636）

Ogitani, Y., Hagihara, K., Oitate, M., Naito, H., & Agatsuma, T. (2016). Bystander killing effect of DS-8201a, a novel anti-human epidermal growth factor receptor 2 antibody-drug conjugate, in tumors with human epidermal growth factor receptor 2 heterogeneity. *Cancer Science, 107*(7), 1039–1046. https://doi.org/10.1111/cas.12966（PMID: 27166974）

O'Reilly, E. M., Wainberg, Z. A., Hendifar, A. E., Borad, M. J., Pietrantonio, F., Pant, S., Hammel, P., Cremolini, C., Manji, G. A., Oberstein, P. E., Garrido-Laguna, I., Springfeld, C., Azad, N. S., Ueno, M., Chui, S. Y., Zhang, Y., Patel, H., Lee, Y., Salman, Z., . . . RASolute 302 Trial Investigators (2026). Daraxonrasib or chemotherapy in previously treated metastatic pancreatic cancer. *New England Journal of Medicine, 395*(4), 325–337. https://doi.org/10.1056/NEJMoa2605555（PMID: 42223072）

Ostrem, J. M., Peters, U., Sos, M. L., Wells, J. A., & Shokat, K. M. (2013). K-Ras(G12C) inhibitors allosterically control GTP affinity and effector interactions. *Nature, 503*(7477), 548–551. https://doi.org/10.1038/nature12796（PMID: 24256730）

Paez, J. G., Jänne, P. A., Lee, J. C., Tracy, S., Greulich, H., Gabriel, S., Herman, P., Kaye, F. J., Lindeman, N., Boggon, T. J., Naoki, K., Sasaki, H., Fujii, Y., Eck, M. J., Sellers, W. R., Johnson, B. E., & Meyerson, M. (2004). EGFR mutations in lung cancer: Correlation with clinical response to gefitinib therapy. *Science, 304*(5676), 1497–1500. https://doi.org/10.1126/science.1099314（PMID: 15118125）

Paik, P. K., Felip, E., Veillon, R., Sakai, H., Cortot, A. B., Garassino, M. C., Mazieres, J., Viteri, S., Senellart, H., Van Meerbeeck, J., Raskin, J., Reinmuth, N., Conte, P., Kowalski, D., Cho, B. C., Patel, J. D., Horn, L., Griesinger, F., Han, J.-Y., . . . Le, X. (2020). Tepotinib in non-small-cell lung cancer with MET exon 14 skipping mutations. *New England Journal of Medicine, 383*(10), 931–943. https://doi.org/10.1056/NEJMoa2004407（PMID: 32469185）

Park, K., Haura, E. B., Leighl, N. B., Mitchell, P., Shu, C. A., Girard, N., Viteri, S., Han, J.-Y., Kim, S.-W., Lee, C. K., Sabari, J. K., Spira, A. I., Yang, T.-Y., Kim, D.-W., Lee, K. H., Sanborn, R. E., Trigo, J., Goto, K., Lee, J.-S., . . . Cho, B. C. (2021). Amivantamab in EGFR exon 20 insertion-mutated non-small-cell lung cancer progressing on platinum chemotherapy: Initial results from the CHRYSALIS phase I study. *Journal of Clinical Oncology, 39*(30), 3391–3402. https://doi.org/10.1200/JCO.21.00662（PMID: 34339292）

Passaro, A., Wang, J., Wang, Y., Lee, S.-H., Melosky, B., Shih, J.-Y., Wang, J., Azuma, K., Juan-Vidal, O., Cobo, M., Felip, E., Girard, N., Cortot, A. B., Califano, R., Cappuzzo, F., Owen, S., Popat, S., Tan, J.-L., Salinas, J., . . . MARIPOSA-2 Investigators (2024). Amivantamab plus chemotherapy with and without lazertinib in EGFR-mutant advanced NSCLC after disease progression on osimertinib: Primary results from the phase III MARIPOSA-2 study. *Annals of Oncology, 35*(1), 77–90. https://doi.org/10.1016/j.annonc.2023.10.117（PMID: 37879444）

Perez, E. A., Romond, E. H., Suman, V. J., Jeong, J.-H., Sledge, G., Geyer, C. E., Jr., Martino, S., Rastogi, P., Gralow, J., Swain, S. M., Winer, E. P., Colon-Otero, G., Davidson, N. E., Mamounas, E., Zujewski, J. A., & Wolmark, N. (2014). Trastuzumab plus adjuvant chemotherapy for human epidermal growth factor receptor 2-positive breast cancer: Planned joint analysis of overall survival from NSABP B-31 and NCCTG N9831. *Journal of Clinical Oncology, 32*(33), 3744–3752. https://doi.org/10.1200/JCO.2014.55.5730（PMID: 25332249）

Peters, S., Camidge, D. R., Shaw, A. T., Gadgeel, S., Ahn, J. S., Kim, D.-W., Ou, S.-H. I., Pérol, M., Dziadziuszko, R., Rosell, R., Zeaiter, A., Mitry, E., Golding, S., Balas, B., Noe, J., Morcos, P. N., Mok, T., & ALEX Trial Investigators (2017). Alectinib versus crizotinib in untreated ALK-positive non-small-cell lung cancer. *New England Journal of Medicine, 377*(9), 829–838. https://doi.org/10.1056/NEJMoa1704795（PMID: 28586279）

Pfizer Laboratories Div Pfizer Inc. (2026). *LORBRENA (lorlatinib) tablets: Prescribing information* (effective 2026-06-26). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=2b34d62d-e02a-4af3-bc0d-1571dd4ee76d

Planchard, D., Smit, E. F., Groen, H. J. M., Mazieres, J., Besse, B., Helland, Å., Giannone, V., D'Amelio, A. M., Jr., Zhang, P., Mookerjee, B., & Johnson, B. E. (2017). Dabrafenib plus trametinib in patients with previously untreated BRAFV600E-mutant metastatic non-small-cell lung cancer: An open-label, phase 2 trial. *The Lancet Oncology, 18*(10), 1307–1316. https://doi.org/10.1016/S1470-2045(17)30679-4（PMID: 28919011）

Planchard, D., Jänne, P. A., Cheng, Y., Yang, J. C.-H., Yanagitani, N., Kim, S.-W., Sugawara, S., Yu, Y., Fan, Y., Geater, S. L., Laktionov, K., Lee, C. K., Valdiviezo, N., Ahmed, S., Maurel, J.-M., Andrasina, I., Goldman, J., Ghiorghiu, D., Rukazenkov, Y., . . . FLAURA2 Investigators (2023). Osimertinib with or without chemotherapy in EGFR-mutated advanced NSCLC. *New England Journal of Medicine, 389*(21), 1935–1948. https://doi.org/10.1056/NEJMoa2306434（PMID: 37937763）

Porta-Sánchez, A., Gilbert, C., Spears, D., Amir, E., Chan, J., Nanthakumar, K., & Thavendiranathan, P. (2017). Incidence, diagnosis, and management of QT prolongation induced by cancer therapies: A systematic review. *Journal of the American Heart Association, 6*(12), Article e007724. https://doi.org/10.1161/JAHA.117.007724（PMID: 29217664）

Powell, C. A., Modi, S., Iwata, H., Takahashi, S., Smit, E. F., Siena, S., Chang, D.-Y., Macpherson, E., Qin, A., Singh, J., Taitt, C., Shire, N., & Camidge, D. R. (2022). Pooled analysis of drug-related interstitial lung disease and/or pneumonitis in nine trastuzumab deruxtecan monotherapy studies. *ESMO Open, 7*(4), Article 100554. https://doi.org/10.1016/j.esmoop.2022.100554（PMID: 35963179）

Ramalingam, S. S., Vansteenkiste, J., Planchard, D., Cho, B. C., Gray, J. E., Ohe, Y., Zhou, C., Reungwetwattana, T., Cheng, Y., Chewaskulyong, B., Shah, R., Cobo, M., Lee, K. H., Cheema, P., Tiseo, M., John, T., Lin, M.-C., Imamura, F., Kurata, T., . . . FLAURA Investigators (2020). Overall survival with osimertinib in untreated, EGFR-mutated advanced NSCLC. *New England Journal of Medicine, 382*(1), 41–50. https://doi.org/10.1056/NEJMoa1913662（PMID: 31751012）

Robson, M., Im, S.-A., Senkus, E., Xu, B., Domchek, S. M., Masuda, N., Delaloge, S., Li, W., Tung, N., Armstrong, A., Wu, W., Goessl, C., Runswick, S., & Conte, P. (2017). Olaparib for metastatic breast cancer in patients with a germline BRCA mutation. *New England Journal of Medicine, 377*(6), 523–533. https://doi.org/10.1056/NEJMoa1706450（PMID: 28578601）

Rowley, J. D. (1973). A new consistent chromosomal abnormality in chronic myelogenous leukaemia identified by quinacrine fluorescence and Giemsa staining. *Nature, 243*(5405), 290–293. https://doi.org/10.1038/243290a0（PMID: 4126434）

Rugo, H. S., Seneviratne, L., Beck, J. T., Glaspy, J. A., Peguero, J. A., Pluard, T. J., Dhillon, N., Hwang, L. C., Nangia, C., Mayer, I. A., Meiller, T. F., Chambers, M. S., Sweetman, R. W., Sabo, J. R., & Litton, J. K. (2017). Prevention of everolimus-related stomatitis in women with hormone receptor-positive, HER2-negative metastatic breast cancer using dexamethasone mouthwash (SWISH): A single-arm, phase 2 trial. *The Lancet Oncology, 18*(5), 654–662. https://doi.org/10.1016/S1470-2045(17)30109-2（PMID: 28314691）

Rugo, H. S., André, F., Yamashita, T., Cerda, H., Toledano, I., Stemmer, S. M., Jurado, J. C., Juric, D., Mayer, I., Ciruelos, E. M., Iwata, H., Conte, P., Campone, M., Wilke, C., Mills, D., Lteif, A., Miller, M., Gaudenzi, F., & Loibl, S. (2020). Time course and management of key adverse events during the randomized phase III SOLAR-1 study of PI3K inhibitor alpelisib plus fulvestrant in patients with HR-positive advanced breast cancer. *Annals of Oncology, 31*(8), 1001–1010. https://doi.org/10.1016/j.annonc.2020.05.001（PMID: 32416251）

Rugo, H. S., Bardia, A., Marmé, F., Cortés, J., Schmid, P., Loirat, D., Trédan, O., Ciruelos, E., Dalenc, F., Gómez Pardo, P., Jhaveri, K. L., Delaney, R., Valdez, T., Wang, H., Motwani, M., Yoon, O. K., Verret, W., & Tolaney, S. M. (2023). Overall survival with sacituzumab govitecan in hormone receptor-positive and human epidermal growth factor receptor 2-negative metastatic breast cancer (TROPiCS-02): A randomised, open-label, multicentre, phase 3 trial. *The Lancet, 402*(10411), 1423–1433. https://doi.org/10.1016/S0140-6736(23)01245-X（PMID: 37633306）

Sandler, A., Gray, R., Perry, M. C., Brahmer, J., Schiller, J. H., Dowlati, A., Lilenbaum, R., & Johnson, D. H. (2006). Paclitaxel-carboplatin alone or with bevacizumab for non-small-cell lung cancer. *New England Journal of Medicine, 355*(24), 2542–2550. https://doi.org/10.1056/NEJMoa061884（PMID: 17167137）

Schoenfeld, A. J., Arbour, K. C., Rizvi, H., Iqbal, A. N., Gadgeel, S. M., Girshman, J., Kris, M. G., Riely, G. J., Yu, H. A., & Hellmann, M. D. (2019). Severe immune-related adverse events are common with sequential PD-(L)1 blockade and osimertinib. *Annals of Oncology, 30*(5), 839–844. https://doi.org/10.1093/annonc/mdz077（PMID: 30847464）

Scott, L. J. (2019). Larotrectinib: First global approval. *Drugs, 79*(2), 201–206. https://doi.org/10.1007/s40265-018-1044-x（PMID: 30635837）

Seidman, A., Hudis, C., Pierri, M. K., Shak, S., Paton, V., Ashby, M., Murphy, M., Stewart, S. J., & Keefe, D. (2002). Cardiac dysfunction in the trastuzumab clinical trials experience. *Journal of Clinical Oncology, 20*(5), 1215–1221. https://doi.org/10.1200/JCO.2002.20.5.1215（PMID: 11870163）

Sequist, L. V., Waltman, B. A., Dias-Santagata, D., Digumarthy, S., Turke, A. B., Fidias, P., Bergethon, K., Shaw, A. T., Gettinger, S., Cosper, A. K., Akhavanfard, S., Heist, R. S., Temel, J., Christensen, J. G., Wain, J. C., Lynch, T. J., Vernovsky, K., Mark, E. J., Lanuti, M., . . . Engelman, J. A. (2011). Genotypic and histological evolution of lung cancers acquiring resistance to EGFR inhibitors. *Science Translational Medicine, 3*(75), Article 75ra26. https://doi.org/10.1126/scitranslmed.3002003（PMID: 21430269）

Sequist, L. V., Yang, J. C.-H., Yamamoto, N., O'Byrne, K., Hirsh, V., Mok, T., Geater, S. L., Orlov, S., Tsai, C.-M., Boyer, M., Su, W.-C., Bennouna, J., Kato, T., Gorbunova, V., Lee, K. H., Shah, R., Massey, D., Zazulina, V., Shahidi, M., & Schuler, M. (2013). Phase III study of afatinib or cisplatin plus pemetrexed in patients with metastatic lung adenocarcinoma with EGFR mutations. *Journal of Clinical Oncology, 31*(27), 3327–3334. https://doi.org/10.1200/JCO.2012.44.2806（PMID: 23816960）

Shaw, A. T., Ou, S.-H. I., Bang, Y.-J., Camidge, D. R., Solomon, B. J., Salgia, R., Riely, G. J., Varella-Garcia, M., Shapiro, G. I., Costa, D. B., Doebele, R. C., Le, L. P., Zheng, Z., Tan, W., Stephenson, P., Shreeve, S. M., Tye, L. M., Christensen, J. G., Wilner, K. D., . . . Iafrate, A. J. (2014). Crizotinib in ROS1-rearranged non-small-cell lung cancer. *New England Journal of Medicine, 371*(21), 1963–1971. https://doi.org/10.1056/NEJMoa1406766（PMID: 25264305）

Shaw, A. T., Bauer, T. M., de Marinis, F., Felip, E., Goto, Y., Liu, G., Mazieres, J., Kim, D.-W., Mok, T., Polli, A., Thurm, H., Calella, A. M., Peltz, G., Solomon, B. J., & CROWN Trial Investigators (2020). First-line lorlatinib or crizotinib in advanced ALK-positive lung cancer. *New England Journal of Medicine, 383*(21), 2018–2029. https://doi.org/10.1056/NEJMoa2027187（PMID: 33207094）

Slamon, D. J., Clark, G. M., Wong, S. G., Levin, W. J., Ullrich, A., & McGuire, W. L. (1987). Human breast cancer: Correlation of relapse and survival with amplification of the HER-2/neu oncogene. *Science, 235*(4785), 177–182. https://doi.org/10.1126/science.3798106（PMID: 3798106）

Slamon, D. J., Leyland-Jones, B., Shak, S., Fuchs, H., Paton, V., Bajamonde, A., Fleming, T., Eiermann, W., Wolter, J., Pegram, M., Baselga, J., & Norton, L. (2001). Use of chemotherapy plus a monoclonal antibody against HER2 for metastatic breast cancer that overexpresses HER2. *New England Journal of Medicine, 344*(11), 783–792. https://doi.org/10.1056/NEJM200103153441101（PMID: 11248153）

Slamon, D. J., Diéras, V., Rugo, H. S., Harbeck, N., Im, S.-A., Gelmon, K. A., Lipatov, O. N., Walshe, J. M., Martin, M., Chavez-MacGregor, M., Bananis, E., Gauthier, E., Lu, D. R., Kim, S., & Finn, R. S. (2024). Overall survival with palbociclib plus letrozole in advanced breast cancer. *Journal of Clinical Oncology, 42*(9), 994–1000. https://doi.org/10.1200/JCO.23.00137（PMID: 38252901）

Smith, B. D., Kaufman, M. D., Lu, W.-P., Gupta, A., Leary, C. B., Wise, S. C., Rutkoski, T. J., Ahn, Y. M., Al-Ani, G., Bulfer, S. L., Caldwell, T. M., Chun, L., Ensinger, C. L., Hood, M. M., McKinley, A., Patt, W. C., Ruiz-Soto, R., Su, Y., Telikepalli, H., . . . Flynn, D. L. (2019). Ripretinib (DCC-2618) is a switch control kinase inhibitor of a broad spectrum of oncogenic and drug-resistant KIT and PDGFRA variants. *Cancer Cell, 35*(5), 738–751.e9. https://doi.org/10.1016/j.ccell.2019.04.006（PMID: 31085175）

Soda, M., Choi, Y. L., Enomoto, M., Takada, S., Yamashita, Y., Ishikawa, S., Fujiwara, S.-I., Watanabe, H., Kurashina, K., Hatanaka, H., Bando, M., Ohno, S., Ishikawa, Y., Aburatani, H., Niki, T., Sohara, Y., Sugiyama, Y., & Mano, H. (2007). Identification of the transforming EML4-ALK fusion gene in non-small-cell lung cancer. *Nature, 448*(7153), 561–566. https://doi.org/10.1038/nature05945（PMID: 17625570）

Solomon, B. J., Besse, B., Bauer, T. M., Felip, E., Soo, R. A., Camidge, D. R., Chiari, R., Bearz, A., Lin, C.-C., Gadgeel, S. M., Riely, G. J., Tan, E. H., Seto, T., James, L. P., Clancy, J. S., Abbattista, A., Martini, J.-F., Chen, J., Peltz, G., . . . Shaw, A. T. (2018). Lorlatinib in patients with ALK-positive non-small-cell lung cancer: Results from a global phase 2 study. *The Lancet Oncology, 19*(12), 1654–1667. https://doi.org/10.1016/S1470-2045(18)30649-1（PMID: 30413378）

Solomon, B. J., Liu, G., Felip, E., Mok, T. S. K., Soo, R. A., Mazieres, J., Shaw, A. T., de Marinis, F., Goto, Y., Wu, Y.-L., Kim, D.-W., Martini, J.-F., Messina, R., Paolini, J., Polli, A., Thomaidou, D., Toffalorio, F., & Bauer, T. M. (2024). Lorlatinib versus crizotinib in patients with advanced ALK-positive non-small cell lung cancer: 5-year outcomes from the phase III CROWN study. *Journal of Clinical Oncology, 42*(29), 3400–3409. https://doi.org/10.1200/JCO.24.00581（PMID: 38819031）

Soria, J.-C., Ohe, Y., Vansteenkiste, J., Reungwetwattana, T., Chewaskulyong, B., Lee, K. H., Dechaphunkul, A., Imamura, F., Nogami, N., Kurata, T., Okamoto, I., Zhou, C., Cho, B. C., Cheng, Y., Cho, E. K., Voon, P. J., Planchard, D., Su, W.-C., Gray, J. E., . . . FLAURA Investigators (2018). Osimertinib in untreated EGFR-mutated advanced non-small-cell lung cancer. *New England Journal of Medicine, 378*(2), 113–125. https://doi.org/10.1056/NEJMoa1713137（PMID: 29151359）

Stopeck, A. T., Lipton, A., Body, J.-J., Steger, G. G., Tonkin, K., de Boer, R. H., Lichinitser, M., Fujiwara, Y., Yardley, D. A., Viniegra, M., Fan, M., Jiang, Q., Dansey, R., Jun, S., & Braun, A. (2010). Denosumab compared with zoledronic acid for the treatment of bone metastases in patients with advanced breast cancer: A randomized, double-blind study. *Journal of Clinical Oncology, 28*(35), 5132–5139. https://doi.org/10.1200/JCO.2010.29.7101（PMID: 21060033）

Strebhardt, K., & Ullrich, A. (2008). Paul Ehrlich's magic bullet concept: 100 years of progress. *Nature Reviews Cancer, 8*(6), 473–480. https://doi.org/10.1038/nrc2394（PMID: 18469827）

Strickler, J. H., Satake, H., George, T. J., Yaeger, R., Hollebecque, A., Garrido-Laguna, I., Schuler, M., Burns, T. F., Coveler, A. L., Falchook, G. S., Vincent, M., Sunakawa, Y., Dahan, L., Bajor, D., Rha, S.-Y., Lemech, C., Juric, D., Rehn, M., Ngarmchamnanrith, G., . . . Hong, D. S. (2023). Sotorasib in KRAS p.G12C-mutated advanced pancreatic cancer. *New England Journal of Medicine, 388*(1), 33–43. https://doi.org/10.1056/NEJMoa2208470（PMID: 36546651）

Swain, S. M., Baselga, J., Kim, S.-B., Ro, J., Semiglazov, V., Campone, M., Ciruelos, E., Ferrero, J.-M., Schneeweiss, A., Heeson, S., Clark, E., Ross, G., Benyunes, M. C., Cortés, J., & CLEOPATRA Study Group (2015). Pertuzumab, trastuzumab, and docetaxel in HER2-positive metastatic breast cancer. *New England Journal of Medicine, 372*(8), 724–734. https://doi.org/10.1056/NEJMoa1413513（PMID: 25693012）

Swain, S. M., Miles, D., Kim, S.-B., Im, Y.-H., Im, S.-A., Semiglazov, V., Ciruelos, E., Schneeweiss, A., Loi, S., Monturus, E., Clark, E., Knott, A., Restuccia, E., Benyunes, M. C., Cortés, J., & CLEOPATRA study group (2020). Pertuzumab, trastuzumab, and docetaxel for HER2-positive metastatic breast cancer (CLEOPATRA): End-of-study results from a double-blind, randomised, placebo-controlled, phase 3 study. *The Lancet Oncology, 21*(4), 519–530. https://doi.org/10.1016/S1470-2045(19)30863-0（PMID: 32171426）

Thatcher, N., Chang, A., Parikh, P., Rodrigues Pereira, J., Ciuleanu, T., von Pawel, J., Thongprasert, S., Tan, E. H., Pemberton, K., Archer, V., & Carroll, K. (2005). Gefitinib plus best supportive care in previously treated patients with refractory advanced non-small-cell lung cancer: Results from a randomised, placebo-controlled, multicentre study (Iressa Survival Evaluation in Lung Cancer). *The Lancet, 366*(9496), 1527–1537. https://doi.org/10.1016/S0140-6736(05)67625-8（PMID: 16257339）

Thress, K. S., Paweletz, C. P., Felip, E., Cho, B. C., Stetson, D., Dougherty, B., Lai, Z., Markovets, A., Vivancos, A., Kuang, Y., Ercan, D., Matthews, S. E., Cantarini, M., Barrett, J. C., Jänne, P. A., & Oxnard, G. R. (2015). Acquired EGFR C797S mutation mediates resistance to AZD9291 in non-small cell lung cancer harboring EGFR T790M. *Nature Medicine, 21*(6), 560–562. https://doi.org/10.1038/nm.3854（PMID: 25939061）

Tsuboi, M., Herbst, R. S., John, T., Kato, T., Majem, M., Grohé, C., Wang, J., Goldman, J. W., Lu, S., Su, W.-C., de Marinis, F., Shepherd, F. A., Lee, K. H., Le, N. T., Dechaphunkul, A., Kowalski, D., Poole, L., Bolanos, A., Rukazenkov, Y., . . . ADAURA Investigators (2023). Overall survival with osimertinib in resected EGFR-mutated NSCLC. *New England Journal of Medicine, 389*(2), 137–147. https://doi.org/10.1056/NEJMoa2304594（PMID: 37272535）

Turner, N. C., Oliveira, M., Howell, S. J., Dalenc, F., Cortes, J., Gomez Moreno, H. L., Hu, X., Jhaveri, K., Krivorotko, P., Loibl, S., Morales Murillo, S., Okera, M., Park, Y. H., Sohn, J., Toi, M., Tokunaga, E., Yousef, S., Zhukova, L., de Bruin, E. C., . . . CAPItello-291 Study Group (2023). Capivasertib in hormone receptor-positive advanced breast cancer. *New England Journal of Medicine, 388*(22), 2058–2070. https://doi.org/10.1056/NEJMoa2214131（PMID: 37256976）

Turner, N. C., Im, S.-A., Saura, C., Juric, D., Loibl, S., Kalinsky, K., Schmid, P., Loi, S., Sunpaweravong, P., Musolino, A., Li, H., Zhang, Q., Nowecki, Z., Leung, R., Thanopoulou, E., Shankar, N., Lei, G., Stout, T. J., Hutchinson, K. E., . . . Jhaveri, K. L. (2024). Inavolisib-based therapy in PIK3CA-mutated advanced breast cancer. *New England Journal of Medicine, 391*(17), 1584–1596. https://doi.org/10.1056/NEJMoa2404625（PMID: 39476340）

Tutt, A. N. J., Garber, J. E., Kaufman, B., Viale, G., Fumagalli, D., Rastogi, P., Gelber, R. D., de Azambuja, E., Fielding, A., Balmaña, J., Domchek, S. M., Gelmon, K. A., Hollingsworth, S. J., Korde, L. A., Linderholm, B., Bandos, H., Senkus, E., Suga, J. M., Shao, Z., . . . OlympiA Clinical Trial Steering Committee and Investigators (2021). Adjuvant olaparib for patients with BRCA1- or BRCA2-mutated breast cancer. *New England Journal of Medicine, 384*(25), 2394–2405. https://doi.org/10.1056/NEJMoa2105215（PMID: 34081848）

van der Graaf, W. T. A., Blay, J.-Y., Chawla, S. P., Kim, D.-W., Bui-Nguyen, B., Casali, P. G., Schöffski, P., Aglietta, M., Staddon, A. P., Beppu, Y., Le Cesne, A., Gelderblom, H., Judson, I. R., Araki, N., Ouali, M., Marreaud, S., Hodge, R., Dewji, M. R., Coens, C., . . . PALETTE study group (2012). Pazopanib for metastatic soft-tissue sarcoma (PALETTE): A randomised, double-blind, placebo-controlled phase 3 trial. *The Lancet, 379*(9829), 1879–1886. https://doi.org/10.1016/S0140-6736(12)60651-5（PMID: 22595799）

van Leeuwen, R. W. F., van Gelder, T., Mathijssen, R. H. J., & Jansman, F. G. A. (2014). Drug-drug interactions with tyrosine-kinase inhibitors: A clinical perspective. *The Lancet Oncology, 15*(8), e315–e326. https://doi.org/10.1016/S1470-2045(13)70579-5（PMID: 24988935）

Verma, S., Miles, D., Gianni, L., Krop, I. E., Welslau, M., Baselga, J., Pegram, M., Oh, D.-Y., Diéras, V., Guardino, E., Fang, L., Lu, M. W., Olsen, S., Blackwell, K., & EMILIA Study Group (2012). Trastuzumab emtansine for HER2-positive advanced breast cancer. *New England Journal of Medicine, 367*(19), 1783–1791. https://doi.org/10.1056/NEJMoa1209124（PMID: 23020162）

von Minckwitz, G., Huang, C.-S., Mano, M. S., Loibl, S., Mamounas, E. P., Untch, M., Wolmark, N., Rastogi, P., Schneeweiss, A., Redondo, A., Fischer, H. H., Jacot, W., Conlin, A. K., Arce-Salinas, C., Wapnir, I. L., Jackisch, C., DiGiovanna, M. P., Fasching, P. A., Crown, J. P., . . . KATHERINE Investigators (2019). Trastuzumab emtansine for residual invasive HER2-positive breast cancer. *New England Journal of Medicine, 380*(7), 617–628. https://doi.org/10.1056/NEJMoa1814017（PMID: 30516102）

Weinstein, I. B. (2002). Addiction to oncogenes—the Achilles heal of cancer. *Science, 297*(5578), 63–64. https://doi.org/10.1126/science.1073096（PMID: 12098689）

Wolf, J., Seto, T., Han, J.-Y., Reguart, N., Garon, E. B., Groen, H. J. M., Tan, D. S. W., Hida, T., de Jonge, M., Orlov, S. V., Smit, E. F., Souquet, P.-J., Vansteenkiste, J., Hochmair, M., Felip, E., Nishio, M., Thomas, M., Ohashi, K., Toyozawa, R., . . . GEOMETRY mono-1 Investigators (2020). Capmatinib in MET exon 14-mutated or MET-amplified non-small-cell lung cancer. *New England Journal of Medicine, 383*(10), 944–957. https://doi.org/10.1056/NEJMoa2002787（PMID: 32877583）

Wu, Y.-L., Cheng, Y., Zhou, X., Lee, K. H., Nakagawa, K., Niho, S., Tsuji, F., Linke, R., Rosell, R., Corral, J., Migliorino, M. R., Pluzanski, A., Sbar, E. I., Wang, T., White, J. L., Nadanaciva, S., Sandin, R., & Mok, T. S. (2017). Dacomitinib versus gefitinib as first-line treatment for patients with EGFR-mutation-positive non-small-cell lung cancer (ARCHER 1050): A randomised, open-label, phase 3 trial. *The Lancet Oncology, 18*(11), 1454–1466. https://doi.org/10.1016/S1470-2045(17)30608-3（PMID: 28958502）

Wu, Y.-L., Dziadziuszko, R., Ahn, J. S., Barlesi, F., Nishio, M., Lee, D. H., Lee, J.-S., Zhong, W., Horinouchi, H., Mao, W., Hochmair, M., de Marinis, F., Migliorino, M. R., Bondarenko, I., Lu, S., Wang, Q., Ochi Lohmann, T., Xu, T., Cardona, A., . . . ALINA Investigators (2024). Alectinib in resected ALK-positive non-small-cell lung cancer. *New England Journal of Medicine, 390*(14), 1265–1276. https://doi.org/10.1056/NEJMoa2310532（PMID: 38598794）

Yang, J. C.-H., Lu, S., Hayashi, H., Felip, E., Spira, A. I., Girard, N., Kim, Y. J., Lee, S.-H., Ostapenko, Y., Danchaivijitr, P., Liu, B., Alip, A., Korbenfeld, E., Mourão Dias, J., Besse, B., Passaro, A., Lee, K.-H., Xiong, H., How, S.-H., . . . MARIPOSA Investigators (2025). Overall survival with amivantamab-lazertinib in EGFR-mutated advanced NSCLC. *New England Journal of Medicine, 393*(17), 1681–1693. https://doi.org/10.1056/NEJMoa2503001（PMID: 40923797）

Zhou, C., Solomon, B., Loong, H. H., Park, K., Pérol, M., Arriola, E., Novello, S., Han, B., Zhou, J., Ardizzoni, A., Mak, M. P., Santini, F. C., Elamin, Y. Y., Drilon, A., Wolf, J., Payakachat, N., Uh, M. K., Rajakumar, D., Han, H., . . . LIBRETTO-431 Trial Investigators (2023). First-line selpercatinib or chemotherapy and pembrolizumab in RET fusion-positive NSCLC. *New England Journal of Medicine, 389*(20), 1839–1850. https://doi.org/10.1056/NEJMoa2309457（PMID: 37870973）
