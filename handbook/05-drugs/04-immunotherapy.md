# 免疫治療藥物（Cancer Immunotherapy）

| 項目 | 本章依據 |
|------|---------|
| 發現史與機轉 | 原始論文與史料回顧（例如 Krummel & Allison, 1995；Leach et al., 1996；Ishida et al., 1992；Freeman et al., 2000；Chen & Mellman, 2013；Pardoll, 2012），全部列在第 11 段，書目資料逐筆以 PubMed 核對 |
| 藥品資料 | 美國 FDA 仿單（DailyMed，2026-11-11 下載：Keytruda 2026-10-16 版、Opdivo 2026-08-12 版、Tecentriq 2026-10-13 版、Imdelltra 2026-09-11 版、Bavencio 2026-09-22 版）與美國 FDA 核准公告（頁面更新至 2026-11-10；US Food and Drug Administration, 2026）。**本章的劑量與核准日期都是美國資料** |
| 毒性分級與處置 | irAE：ASCO 2021（Schneider et al., 2021）、ESMO 2022（Haanen et al., 2022），處置表在[免疫治療副作用](../00-shared/04-irae.md)；CRS／ICANS：ASTCT 2019 共識（Lee et al., 2019），處置在[腫瘤急症](../00-shared/02-oncologic-emergencies.md#9-細胞激素釋放症候群crs與神經毒性icans)第 9 節 |
| 台灣藥證與健保 | 本章不重述。台灣藥證與給付請見各癌別章第 9 段（藥品給付規定 115/10/22 版）；免疫檢查點抑制劑 9.69 的整理在[肺癌章 9.3](../01-lung-cancer.md#93-免疫檢查點抑制劑969) |
| 最後更新 | 2026-11-11 |

> 本手冊是學習用整理，不能取代原始指引、仿單、健保公告與院內規範。實際處方以主治醫師判斷與院內流程為準。

**這一章的結論先講：** 免疫治療不直接殺癌細胞，而是讓病人自己的 T 細胞去殺：檢查點抑制劑拆掉 T 細胞的煞車，T 細胞銜接抗體把 T 細胞拉到腫瘤旁，細胞治療直接輸入會認腫瘤的 T 細胞。所以它的療效來得慢、但可以很久；它的毒性不是骨髓抑制，而是**自體免疫（irAE）**或**細胞激素風暴（CRS）**。接受過免疫治療的病人出現任何新症狀，都先想到免疫。

---

## 0. 速查卡

| 主題 | 一句話重點 |
|------|-----------|
| 這類藥在做什麼 | 解除 T 細胞的煞車（免疫檢查點抑制劑，ICI）、把 T 細胞和腫瘤細胞拉在一起（雙特異性 T 細胞銜接抗體），或直接輸入會認腫瘤的 T 細胞（CAR-T、TCR-T、TIL） |
| ICI 的分類 | **PD-1**：nivolumab、pembrolizumab、cemiplimab、tislelizumab、dostarlimab、toripalimab。**PD-L1**：atezolizumab、durvalumab、avelumab。**CTLA-4**：ipilimumab、tremelimumab。**LAG-3**：relatlimab（與 nivolumab 做成固定劑量合併製劑） |
| 兩個煞車、兩個地點 | CTLA-4 管 T 細胞活化的早期（啟動階段）；PD-1 管 T 細胞在周邊組織與腫瘤裡的作用階段（Pardoll, 2012） |
| 療效長什麼樣 | 反應率不一定高，但有反應的人可以維持很久：ipilimumab 的存活曲線約從第 3 年起持平在 21% 左右（Schadendorf et al., 2015）。影像可能先變大再變小（假性惡化），也可能真的加速惡化（超進展） |
| 開藥前要有的報告 | NSCLC 先有 EGFR／ALK 結果；PD-L1（TPS、CPS、IC 是三種不同的算法）；MSI-H／dMMR；TMB |
| 類別毒性 | ICI：irAE，任何器官、任何時間，包含停藥之後。T 細胞銜接抗體與細胞治療：CRS 與 ICANS |
| 最會死人的 | 心肌炎（通報病例的致死比例 39.7%）、肺炎、大腸炎、肝炎、神經毒性（Wang et al., 2018）；內分泌的急症是 DKA 與腎上腺危象 |
| 劑量 | 固定劑量；**不因毒性減量**，只有「暫停」或「永久停用」（Merck Sharp & Dohme, 2026） |
| 交互作用 | 抗體不經 CYP 代謝。要查的是病人的狀況：開始時 prednisone ≥10 mg/day、自體免疫疾病、器官移植、之後會不會接 osimertinib |
| 本手冊四個癌別 | 肺癌用得最廣；三陰性乳癌靠 KEYNOTE-522 與 KEYNOTE-355；胰臟癌只有 MSI-H／dMMR；肉瘤只有少數組織型 |

> [!IMPORTANT]
> **必背數字**
> - Pembrolizumab 200 mg q3w 或 400 mg q6w；nivolumab 240 mg q2w 或 480 mg q4w（美國仿單；Merck Sharp & Dohme, 2026；Bristol-Myers Squibb, 2026）。
> - 半衰期：pembrolizumab 22 天、nivolumab 25 天、atezolizumab 27 天（同上；Genentech, 2026）。停藥後藥效還在，irAE 可以在停藥後數月才出現。
> - 開始 ICI 時 prednisone ≥10 mg/day（或等效劑量）的病人，療效較差（Arbour et al., 2018）。
> - NSCLC 單用 pembrolizumab：KEYNOTE-024 與健保給付的門檻都是 PD-L1 TPS ≥50%（Reck et al., 2016）；轉移性三陰性乳癌併用化療的門檻是 CPS ≥10（KEYNOTE-355；Cortes et al., 2022）。
> - irAE 通則：G1 多可繼續、G2 多半暫停、G3 暫停並給高劑量類固醇、G4 永久停用（以荷爾蒙補充控制的內分泌病變除外）；類固醇至少 4–6 週慢慢減（Schneider et al., 2021）。
> - 免疫性心肌炎中位發生時間是開始治療後 34 天（Mahmood et al., 2018）。

---

## 1. 怎麼被發現的

**這一段的結論先講：** 免疫治療走了一百多年，轉折只有一個：從「踩油門」（細菌毒素、細胞激素、疫苗）改成「拆煞車」（CTLA-4、PD-1）。前者偶爾出現奇蹟，後者才讓免疫治療變成常規。今天病房裡的 PD-L1 報告、MSI 檢測、irAE 警示卡、tocilizumab 備藥，都可以在這段歷史裡找到來源。

### 1.1 時間軸

| 年份 | 事件 | 意義 |
|------|------|------|
| 1891–1893 | 紐約的骨腫瘤外科醫師 William Coley 把鏈球菌注射到無法手術的腫瘤病人體內，1893 年發表 10 個病例（Coley, 1991，為 1893 年原文的重刊；McCarthy, 2006） | 第一次有系統地用免疫反應治療癌症；他報告的好結果集中在骨與軟組織肉瘤 |
| 1957 | Burnet 提出免疫監視（immunosurveillance）：免疫系統會辨認並清除剛出現的癌細胞（Burnet, 1957；Dunn et al., 2002） | 假說後來因為缺乏實驗證據一度被放棄 |
| 1976 | Morales 用膀胱內灌注加皮內注射卡介苗（BCG）治療 9 位反覆復發的表淺性膀胱腫瘤（Morales et al., 1976） | 細菌製劑的免疫治療，沿用到今天 |
| 1984–1985 | Rosenberg 用高劑量介白素-2（IL-2）加 LAK 細胞治療 25 位標準治療無效的病人，11 位腫瘤明顯縮小（Rosenberg et al., 1985；Rosenberg, 2014） | 證明只靠刺激 T 細胞，就能讓大而有血管的腫瘤消失 |
| 1988 | 腫瘤浸潤淋巴球（TIL）加 IL-2 治療轉移性黑色素瘤：沒用過 IL-2 的 15 人中 9 人腫瘤縮小（Rosenberg et al., 1988） | 細胞治療的起點，36 年後成為 lifileucel |
| 1992 | 京都大學本庶佑實驗室選殖出 PD-1 基因（Ishida et al., 1992）；美國 FDA 核准高劑量 IL-2 用於轉移性腎細胞癌，1998 年加上轉移性黑色素瘤（Rosenberg, 2014） | PD-1 當時被以為和細胞死亡有關；Rosenberg 稱 IL-2 是第一個獲核准用於癌症病人的免疫治療 |
| 1995–1996 | Allison 實驗室證明 CTLA-4 和 CD28 送出相反的訊號（Krummel & Allison, 1995）；用抗體擋住 CTLA-4，小鼠的腫瘤被排斥（Leach et al., 1996） | 「拆煞車」的想法誕生 |
| 1999–2000 | PD-1 剔除小鼠出現類狼瘡的自體免疫病（Nishimura et al., 1999）；陳列平實驗室發現 B7-H1（Dong et al., 1999），隔年確認它就是 PD-1 的配體 PD-L1（Freeman et al., 2000） | PD-1 是第二個煞車，配體長在周邊組織 |
| 2002 | 免疫編輯（immunoediting）：免疫系統清除腫瘤，同時也「雕塑」出能逃脫的腫瘤（Dunn et al., 2002） | 解釋為什麼臨床看到的腫瘤多半已經會躲 |
| 2008 | Blinatumomab（CD19 × CD3）用極低劑量就讓淋巴瘤縮小（Bargou et al., 2008） | 雙特異性 T 細胞銜接抗體的第一份臨床證據 |
| 2010 | Ipilimumab 第 3 期試驗：轉移性黑色素瘤的整體存活，含 ipilimumab 的組別 10.0 對 6.4 個月（Hodi et al., 2010）；一位晚期濾泡性淋巴瘤病人接受 CD19 CAR-T 後腫瘤明顯縮小（Kochenderfer et al., 2010） | 檢查點抑制劑第一次在第 3 期試驗延長存活 |
| 2011 | Ipilimumab 在美國核准（Cameron et al., 2011）；June 團隊的 CAR-T 讓一位頑固型慢性淋巴性白血病完全緩解（Porter et al., 2011） | |
| 2012 | Anti-PD-1 與 anti-PD-L1 的第 1 期報告在同一期刊出（Topalian et al., 2012；Brahmer et al., 2012） | 肺癌也有反應；PD-L1 陰性的 17 人無人有反應，PD-L1 檢測由此而來 |
| 2014 | Nivolumab 在日本、pembrolizumab 在美國先後核准用於黑色素瘤（Deeks, 2014；Poole, 2014）；blinatumomab 於 2014-12-03 獲美國加速核准（Przepiorka et al., 2015） | PD-1 抑制劑上市 |
| 2015 | Pembrolizumab 在錯配修復缺失（dMMR）腫瘤有高反應率，修復正常的大腸直腸癌 18 人無人有反應（Le et al., 2015） | 生物標記比器官別重要 |
| 2017 | 2017-05-23 美國核准 pembrolizumab 用於 MSI-H／dMMR 實體腫瘤（Marcus et al., 2019）；2017-08-30 核准 tisagenlecleucel（O'Leary et al., 2019） | 第一個不分癌別的適應症；第一個 CAR-T |
| 2018 | Allison 與本庶佑獲諾貝爾生理醫學獎（Huang & Chang, 2019） | |
| 2022 | Relatlimab ＋ nivolumab（LAG-3 ＋ PD-1）於 3 月在美國核准（Paik, 2022） | 第三個臨床可用的檢查點 |
| 2024 | 美國核准 lifileucel（2 月；Hu et al., 2025）、tarlatamab（5 月；Liu et al., 2026）、afamitresgene autoleucel（8 月；Barnett et al., 2025） | 細胞治療與 T 細胞銜接抗體進入實體腫瘤 |
| 2025–2026 | Tarlatamab 於 2025-11-19 轉為傳統核准；dostarlimab 於 2026-10-19 獲加速核准，用於 MSI-H／dMMR 的局部晚期直腸癌（US Food and Drug Administration, 2026） | |

### 1.2 Coley 的毒素：免疫治療從肉瘤病房開始

1891 年，Coley 把鏈球菌注射到一位無法手術的癌症病人體內，想靠感染引起的反應讓腫瘤縮小，而且成功了。之後 40 年，他在紐約 Memorial Hospital 主持骨腫瘤部門，用細菌或細菌產物（後來稱為 Coley's toxins）治療超過 1,000 位病人，在骨與軟組織肉瘤報告的結果最好。但同儕不相信他的結果，加上放射治療與化療興起，這個做法逐漸消失（McCarthy, 2006）。

**和今天的關係：** Coley 的方法是不分對象地「踩油門」，有效與否無法預測。留下來的後代是膀胱內 BCG（Morales et al., 1976）。現代免疫治療和它最大的差別，是我們知道藥物作用在哪一個分子上。有趣的是，免疫治療從肉瘤開始，今天肉瘤卻是 ICI 效果最有限的癌別之一（見 5.2）。

### 1.3 免疫監視與免疫編輯：腫瘤為什麼逃得掉

Burnet 與 Thomas 的免疫監視假說認為免疫系統會清除新生的癌細胞，但因為缺少實驗證據而被放棄。後來的小鼠實驗證實免疫監視存在，並把它擴充成免疫編輯：免疫系統一邊清除腫瘤，一邊也篩選出免疫原性較低、能逃脫的腫瘤（Dunn et al., 2002）。

> [!TIP]
> **警察與慣犯**
> 免疫系統像巡邏的警察，剛出現的癌細胞像生手，多半當場被抓。逃過幾輪追捕、最後長成腫瘤的，是學會變裝的慣犯：有的把身分證（抗原與 MHC）藏起來，有的舉起「自己人」的牌子（PD-L1）要警察停手。臨床上看得到的腫瘤，都是已經通過這場篩選的。所以免疫治療要做的不是「增加警力」而已，還要拆穿變裝。

**和今天的關係：** 腫瘤逃脫的方式決定了治療的方向。舉牌子的，用 PD-1／PD-L1 抑制劑；把身分證藏起來的（MHC 下調），ICI 沒有用，要靠不看 MHC 的 CAR-T 或 T 細胞銜接抗體（見第 7 段）。

### 1.4 IL-2：第一個證明 T 細胞能治癌的藥

1984 年 11 月，一位 33 歲、多線治療失敗的轉移性黑色素瘤女性接受高劑量 IL-2，幾個月後腫瘤全部消失，29 年後仍無病（Rosenberg, 2014）。高劑量 IL-2 在 270 位轉移性黑色素瘤病人的反應率只有 16%，完全反應 6%；但 17 位完全反應者有 10 位持續無惡化，反應超過 30 個月的病人沒有人再惡化，另有 6 人（2%）死於敗血症相關的不良事件（Atkins et al., 1999）。最早的報告就指出主要毒性是嚴重的體液滯留（Rosenberg et al., 1985）。另一個細胞激素 interferon alfa-2b，以高劑量用一年，在高風險黑色素瘤術後輔助的隨機試驗（287 人）延長了無復發存活與整體存活，但多數病人需要因毒性調整劑量（Kirkwood et al., 1996）。

**和今天的關係：** 「少數人、但很久」的存活曲線尾巴，最早是在 IL-2 看到的，後來成為整類免疫治療的特徵（見 2.3）。今天在本章會再遇到 IL-2 的地方，是 TIL 治療的流程（見 3.6）。

### 1.5 CTLA-4：把煞車找出來

1990 年代初，大家知道 T 細胞活化需要兩個訊號：T 細胞受體認抗原，加上 CD28 與 B7 結合的共同刺激。CTLA-4 長得像 CD28，也結合 B7，功能卻有爭議。Krummel 與 Allison 證明 CD28 與 CTLA-4 送出相反的訊號，CTLA-4 抑制 T 細胞增殖與 IL-2 分泌（Krummel & Allison, 1995）。同年，CTLA-4 剔除小鼠的報告顯示：活化的 T 細胞浸潤肝、心、肺、胰臟，小鼠在 3 到 4 週大時瀕死（Waterhouse et al., 1995）。Allison 接著想到，暫時擋住這個煞車也許可以讓免疫系統攻擊腫瘤；注射 anti-CTLA-4 抗體的小鼠果然排斥了腫瘤，包含已經長出來的腫瘤，而且之後再接種同一種腫瘤也長不起來（Leach et al., 1996）。這個抗體由加州大學柏克萊分校授權給 Medarex，後來併入 Bristol-Myers Squibb，成為 ipilimumab（Cameron et al., 2011）。

第 3 期試驗收了 676 位治療過的轉移性黑色素瘤病人，ipilimumab 3 mg/kg q3w 共 4 次：ipilimumab ＋ gp100 胜肽疫苗對 gp100 單用的整體存活是 10.0 對 6.4 個月（HR 0.68），ipilimumab 單用是 10.1 個月（HR 0.66）；用 ipilimumab 的病人 3–4 級免疫相關不良事件 10–15%，14 人（2.1%）死於藥物相關事件，其中 7 人是免疫相關（Hodi et al., 2010）。

**和今天的關係：** 剔除小鼠的器官浸潤，就是 irAE 的預告。CTLA-4 管的是活化的源頭，拆掉它影響的 T 細胞範圍廣，所以含 ipilimumab 的處方 irAE 最多、也最嚴重（見 2.2 與 6.1）。

### 1.6 PD-1 與 PD-L1：一個被取錯名字的基因

本庶佑實驗室在找「細胞計畫性死亡」相關基因時，從正在死亡的細胞株裡選殖出一個新基因，命名為 programmed death-1（Ishida et al., 1992）。它真正的功能要等到剔除小鼠才明白：PD-1 剔除的小鼠到了老年才出現類狼瘡的關節炎與腎絲球腎炎，代表 PD-1 是維持周邊自體耐受的負向調節者（Nishimura et al., 1999）。配體則由兩個團隊接力找到：陳列平實驗室發現 B7 家族的新成員 B7-H1（Dong et al., 1999）；Freeman 等證明它與 PD-1 結合後抑制 T 細胞增殖與細胞激素分泌，並指出它表現在抗原呈現細胞，也表現在心、肺等非淋巴組織（Freeman et al., 2000）。

2010 年發表的第 1 期試驗（抗體當時的代號是 MDX-1106，即後來的 nivolumab）就看到三件後來一再出現的事：抗體半衰期 12–20 天，但給藥後 2 個月以上，T 細胞上的 PD-1 仍有七成以上被占住；有一位病人發生發炎性大腸炎；腫瘤表現 B7-H1 的病人似乎比較會有反應（Brahmer et al., 2010）。2012 年的大型第 1 期報告收了 296 人：反應率 NSCLC 18%、黑色素瘤 28%、腎細胞癌 27%；31 個追蹤滿 1 年的反應中有 20 個持續 1 年以上；3 人死於肺毒性；PD-L1 陰性的 17 人無人有反應，陽性的 25 人有 9 人（36%）有反應（Topalian et al., 2012）。同期的 anti-PD-L1 抗體也有 6–17% 的反應率（Brahmer et al., 2012）。

**和今天的關係：**

- **PD-1 剔除小鼠比 CTLA-4 剔除小鼠溫和得多**（老年才發病，對比 3–4 週瀕死）。臨床上也一樣：單用 PD-1 抑制劑的 3–4 級治療相關不良事件 16.3%，ipilimumab 27.3%，兩者合併 55.0%（Larkin et al., 2015）。
- **PD-L1 長在心與肺**，可以幫忙記住為什麼心肌炎與肺炎是要命的 irAE。
- **PD-L1 檢測**從 2012 年那 42 個檢體開始；**停藥後 irAE 還會出現**，從 2010 年的受體占有率資料就看得出來。
- 第 1 期試驗裡死於肺毒性的 3 個人，是今天每次給藥前都要問咳嗽與喘的原因。

### 1.7 MSI-H：生物標記贏過器官別

Le 等假設：錯配修復缺失的腫瘤突變多，產生的新抗原（neoantigen）也多，應該比較容易被免疫系統認出來。41 位病人的第 2 期試驗證實了這一點：dMMR 大腸直腸癌的免疫相關反應率 40%（4/10），dMMR 的其他癌別 71%（5/7），修復正常的大腸直腸癌 0%（0/18）；dMMR 腫瘤平均有 1,782 個體細胞突變，修復正常的只有 73 個（Le et al., 2015）。2017-05-23，美國 FDA 依 5 個單臂試驗、15 種癌別、149 位病人的資料（反應率 39.6%，78% 的反應持續 6 個月以上）核准 pembrolizumab 用於 MSI-H／dMMR 實體腫瘤，這是第一個依生物標記而不是原發部位的癌症適應症（Marcus et al., 2019）。後來在 dMMR 的局部晚期直腸癌，12 位完成 dostarlimab 治療的病人全部達到臨床完全反應，沒有人接受化放療或手術（Cercek et al., 2022）。

**和今天的關係：** 胰臟癌對 ICI 幾乎沒有反應，唯一的例外就是 MSI-H／dMMR（見 5.2）。所以胰臟癌病人的病理報告要有錯配修復蛋白的免疫染色或 MSI 檢測。

### 1.8 直接把 T 細胞送進去，或把 T 細胞拉過來

- **TIL**：從切下來的腫瘤裡分離淋巴球，體外擴增後輸回，再給 IL-2（Rosenberg et al., 1988）。
- **CAR-T**：替 T 細胞裝上人工受體，直接認腫瘤表面的抗原。Rosenberg 團隊治療的一位晚期濾泡性淋巴瘤病人，輸注 CD19 CAR-T 後淋巴瘤明顯縮小，血中 B 細胞至少 39 週測不到（Kochenderfer et al., 2010）。June 團隊在受體上加了 4-1BB 共同刺激區，一位頑固型慢性淋巴性白血病病人輸入的細胞在體內擴增超過 1,000 倍，達到完全緩解，並出現延遲的腫瘤溶解症候群（Porter et al., 2011）。
- **Tocilizumab 的由來**：2 位復發且難治的急性淋巴性白血病兒童接受 CD19 CAR-T 後，都發生細胞激素釋放症候群，其中一位很嚴重，用 etanercept 與 tocilizumab 阻斷細胞激素後逆轉（Grupp et al., 2013）。
- **T 細胞銜接抗體**：不改造細胞，改用一個同時抓住 CD3 與腫瘤抗原的抗體把兩者拉在一起（Bargou et al., 2008）。2024 年核准的 tarlatamab 把這個做法帶進小細胞肺癌（Liu et al., 2026）。

**和今天的關係：** 健保對 CAR-T 執行醫院的條件之一，就是藥局要備有 tocilizumab（見[腫瘤急症 9.4](../00-shared/02-oncologic-emergencies.md#94-台灣藥證與健保給付)）；tarlatamab 的病房醫囑、監測與出院衛教在[肺癌章 7.7](../01-lung-cancer.md#77-tarlatamab-病房實務c1d1c1d8-的醫囑監測與出院衛教)。

---

## 2. 作用機轉

**這一段的結論先講：** T 細胞要殺掉腫瘤得走完七個步驟，腫瘤只要卡住其中一步就能逃。CTLA-4 抑制劑放開的是第 3 步（淋巴結裡的啟動），PD-1／PD-L1 抑制劑放開的是第 7 步（腫瘤裡的執行）。藥物作用在 T 細胞而不是腫瘤細胞，所以反應的時間、影像的樣子、毒性的型態都和化療不同。

### 2.1 癌症免疫循環（cancer-immunity cycle）

Chen 與 Mellman 把抗腫瘤免疫整理成一個循環：T 細胞殺死癌細胞只是其中一步，循環同時要在「認出非我」與「避免自體免疫」之間維持平衡（Chen & Mellman, 2013）。循環有七個步驟，每一步失敗都對應一種免疫逃脫（Kim & Chen, 2016）。

| 步驟 | 發生的地方 | 卡住時的原因（Kim & Chen, 2016） | 對準這一步的治療 |
|------|-----------|-------------------------------|----------------|
| 1. 癌細胞死亡，釋出抗原 | 腫瘤 | 沒有夠強的腫瘤抗原 | 沒有直接的藥；MSI-H 或突變多的腫瘤在這一步占優勢（Le et al., 2015） |
| 2. 抗原呈現細胞呈現抗原 | 腫瘤到淋巴結 | 同上 | 癌症疫苗（見 3.8） |
| 3. T 細胞啟動與活化 | 淋巴結 | 腫瘤專一的 T 細胞活化不足 | **CTLA-4 抑制劑** |
| 4. T 細胞隨血流移動 | 血液 | | |
| 5. T 細胞浸潤腫瘤 | 腫瘤的血管與基質 | T 細胞進不了腫瘤 | 合併治療（見第 7 段） |
| 6. T 細胞辨認癌細胞 | 腫瘤 | 癌細胞把 MHC 下調 | 不靠 MHC 的 CAR-T 與 T 細胞銜接抗體 |
| 7. T 細胞殺死癌細胞 | 腫瘤 | 腫瘤微環境裡的抑制因子與抑制性細胞 | **PD-1／PD-L1 抑制劑** |

第 7 步殺死的癌細胞又釋出抗原，回到第 1 步，所以免疫反應一旦轉起來可以自己維持。這是療效能持續的理論基礎，也解釋了為什麼單用 PD-1 抑制劑只在「本來就有抗腫瘤免疫反應」的病人有效（Pardoll, 2012）。

### 2.2 兩個煞車，兩個地點

| 比較 | CTLA-4 | PD-1 與 PD-L1 |
|------|--------|--------------|
| 管哪個階段 | T 細胞活化的早期，調節活化的幅度（Pardoll, 2012） | 發炎時限制 T 細胞在周邊組織的活性，避免自體免疫（Pardoll, 2012） |
| 怎麼踩煞車 | 對 CD80／CD86 的親和力比 CD28 高，把共同刺激訊號搶走，也送出抑制訊號（Pardoll, 2012） | PD-1 與 PD-L1 結合後，抑制 T 細胞受體引發的增殖與細胞激素分泌（Freeman et al., 2000） |
| 配體在哪裡 | 抗原呈現細胞上的 CD80／CD86 | 抗原呈現細胞、心與肺等非淋巴組織（Freeman et al., 2000），以及腫瘤 |
| 腫瘤怎麼利用 | | 腫瘤被 T 細胞攻擊時把 PD-L1 表現拉高，借用正常組織保護自己的機制，稱為適應性免疫抵抗（adaptive immune resistance）（Pardoll, 2012） |
| 剔除小鼠 | 3 到 4 週大就瀕死，多器官 T 細胞浸潤（Waterhouse et al., 1995） | 老年才出現類狼瘡病變（Nishimura et al., 1999） |
| 黑色素瘤第一線的 3–4 級治療相關不良事件 | ipilimumab 27.3% | nivolumab 16.3%；兩者合併 55.0%（Larkin et al., 2015） |

> [!TIP]
> **警校的門檻與現場的停手令**
> CTLA-4 像警校的結業門檻：它決定有多少新訓練好的 T 細胞能畢業上街。PD-1 像現場的停手令：T 細胞已經到了腫瘤旁邊，看到 PD-L1 這面牌子就收手。拆掉校門的門檻，上街的人變多，哪一區都可能出事，所以 CTLA-4 抑制劑的 irAE 多而廣。撤掉現場的停手令，影響的主要是已經到場的 T 細胞，所以 PD-1 抑制劑相對溫和。兩個一起拆，療效與毒性都疊加。

> [!IMPORTANT]
> **PD-1 抑制劑和 PD-L1 抑制劑擋的不是同一邊**
> - Anti-PD-1 抗體結合 T 細胞上的 PD-1，同時擋住它與 PD-L1、PD-L2 的結合（Markham & Duggan, 2018）。
> - Anti-PD-L1 抗體結合 PD-L1，擋住 PD-L1 與 PD-1、CD80 的結合（Syed, 2017）。
> - NSCLC 試驗的統合分析中，任何等級的肺炎在 PD-1 抑制劑是 3.6%，PD-L1 抑制劑是 1.3%；3–4 級是 1.1% 對 0.4%（Khunger et al., 2017）。這是跨試驗的間接比較，不能當成換藥的依據，但可以幫忙記住哪一類藥的肺炎較多。

### 2.3 和化療哪裡不一樣

化療藥直接攻擊分裂中的細胞（機轉與劑量限制毒性見[化療藥物](02-cytotoxic-chemotherapy.md)與[化療基礎第 11 節](../00-shared/01-chemo-basics.md#11-抗癌藥分類劑量限制毒性與解毒劑)）。ICI 的對象是 T 細胞，差別整理如下。

| 比較 | 細胞毒性化療 | 免疫檢查點抑制劑 |
|------|------------|----------------|
| 藥物直接作用的對象 | 分裂中的細胞，包含正常的骨髓與黏膜 | T 細胞 |
| 反應的時間 | 幾個週期內 | 可能較晚；影像可能先變大再變小 |
| 存活曲線 | 中位數延長，尾巴逐漸下降 | 一部分病人長期存活，曲線出現平台 |
| 劑量 | 依體表面積計算，依毒性減量 | 固定劑量，不減量；nivolumab 的分析中，暴露量和不良事件的頻率、嚴重度沒有明顯關係（Zhao et al., 2017） |
| 典型毒性 | 骨髓抑制、噁心嘔吐、黏膜炎、掉髮 | 自體免疫：皮膚、腸、肝、內分泌、肺、心、神經 |
| 毒性的時間 | 跟著給藥週期，可以預期 | 不跟週期走，停藥後仍可能發生 |
| 類固醇 | 常用來止吐與當前置用藥 | 開始前盡量不用；治療 irAE 時則是主角 |

**「曲線的尾巴」有多長：**

- **Ipilimumab**：1,861 位黑色素瘤病人的合併分析，3 年存活率 22%，曲線約從第 3 年起持平，最長追蹤 10 年（Schadendorf et al., 2015）。
- **Nivolumab ＋ ipilimumab**（CheckMate 067，追蹤至少 10 年）：中位整體存活 71.9 個月，nivolumab 單用 36.9 個月，ipilimumab 單用 19.9 個月；第 3 年時還活著而且沒有惡化的病人，10 年的黑色素瘤專一存活率是 96%（合併）與 97%（nivolumab）（Wolchok et al., 2025）。
- **肺癌**：KEYNOTE-024 的 5 年存活率 31.9% 對 16.3%，而且化療組有 66% 後來也用了 PD-1／PD-L1 抑制劑；完成 35 個週期（約 2 年）的 39 人，在約 5 年時 82.1% 仍存活（Reck et al., 2021）。KEYNOTE-189 的 5 年存活率是 19.4% 對 11.3%（Garassino et al., 2023）。

> [!TIP]
> **除草劑與巡邏隊**
> 化療像噴除草劑：藥在的時候雜草被壓住，藥一停、沒死的草就長回來。免疫治療像訓練一支巡邏隊：一開始看不出差別，甚至因為隊員湧進現場而顯得更亂（影像變大）；但巡邏隊一旦認得目標，藥停了它們還在。這就是存活曲線尾巴翹起來的原因，也是為什麼停藥幾個月後巡邏隊「誤傷」正常器官時，我們還是要把它當成 irAE。

### 2.4 假性惡化與超進展

- **假性惡化（pseudoprogression）**：ipilimumab 的試驗歸納出四種反應型態，其中兩種是傳統標準會判成惡化的：腫瘤總量先增加之後才縮小，以及出現新病灶但整體縮小；四種型態的存活都不差（Wolchok et al., 2009）。RECIST 工作小組因此訂了給免疫治療試驗用的 iRECIST（Seymour et al., 2017）。健保 9.69 的續用評估也採 i-RECIST，初次評估為 iUPD 時可再用 4 至 8 週後複評（見[肺癌章 9.3](../01-lung-cancer.md#93-免疫檢查點抑制劑969)）。
- **超進展（hyperprogressive disease）**：用藥後腫瘤生長速度反而明顯加快。406 位接受 PD-1／PD-L1 抑制劑的 NSCLC 病人中 13.8% 屬於超進展，同一研究的化療組是 5.1%（3/59）；前 6 週內發生超進展者的中位存活只有 3.4 個月（Ferrara et al., 2018）。
- **兩個數字放在一起看**：同一個世代的假性惡化只有 4.7%（Ferrara et al., 2018）。影像變大時，真的惡化遠比假性惡化常見。

> [!WARNING]
> **不要用「可能是假性惡化」拖延處理**
> 影像變大、同時病人的體能、症狀、檢驗都在變差時，先當成真的惡化來處理並通知主治醫師。等 4 到 8 週再照一次影像，是留給臨床穩定的病人的。

---

## 3. 分類與代表藥

**這一段的結論先講：** 先記標的，再記藥名。拆煞車的抗體依標的分成 PD-1、PD-L1、CTLA-4、LAG-3 四類，毒性是 irAE；把 T 細胞帶到腫瘤旁的雙特異性抗體與細胞治療，毒性是 CRS 與 ICANS。細胞激素、BCG 與疫苗是歷史上的「踩油門」路線，今天用得少。

| 類別 | 代表藥 | 作用方式 | 類別毒性 |
|------|--------|---------|---------|
| PD-1 抑制劑 | nivolumab、pembrolizumab、cemiplimab、tislelizumab、dostarlimab、toripalimab | 結合 T 細胞上的 PD-1 | irAE |
| PD-L1 抑制劑 | atezolizumab、durvalumab、avelumab | 結合腫瘤與免疫細胞上的 PD-L1 | irAE |
| CTLA-4 抑制劑 | ipilimumab、tremelimumab | 放開 T 細胞活化早期的煞車 | irAE，比 PD-1 類多而重 |
| LAG-3 抑制劑 | relatlimab（與 nivolumab 合併） | 第三個煞車 | irAE |
| 雙特異性 T 細胞銜接抗體 | tarlatamab、blinatumomab | 一端抓 CD3，一端抓腫瘤抗原 | CRS、神經毒性（含 ICANS） |
| 細胞治療 | CAR-T（tisagenlecleucel）、TCR-T（afamitresgene autoleucel）、TIL（lifileucel） | 輸入會認腫瘤的 T 細胞 | CRS、ICANS、淋巴球清除化療的血球低下 |
| 細胞激素、BCG、疫苗 | aldesleukin（IL-2）、interferon、膀胱內 BCG、sipuleucel-T | 非專一地活化免疫，或訓練免疫認抗原 | 依藥而異 |

> [!IMPORTANT]
> **用字尾和字首記分類**
> - PD-1：**nivo**lumab、**pembro**lizumab、**cemi**plimab、**tisle**lizumab、**dostar**limab、**tori**palimab。
> - PD-L1：**a**tezolizumab、**d**urvalumab、**a**velumab（A-D-A）。
> - CTLA-4：**ipi**limumab、**treme**limumab。
> - 看到含 ipilimumab 或 tremelimumab 的處方，irAE 的警覺要再拉高一級。

### 3.1 PD-1 抑制劑

| 藥名 | 第一個核准 | 代表試驗（本手冊相關） | 備註 |
|------|-----------|---------------------|------|
| nivolumab | 2014 年，日本，無法切除的黑色素瘤（Deeks, 2014） | CheckMate 017：鱗狀 NSCLC 二線，對 docetaxel 的整體存活 9.2 對 6.0 個月（HR 0.59），3–4 級治療相關不良事件 7% 對 55%（Brahmer et al., 2015）；CheckMate 057：非鱗狀 12.2 對 9.4 個月（HR 0.73）（Borghaei et al., 2015） | 240 mg q2w 或 480 mg q4w（Bristol-Myers Squibb, 2026）；有皮下劑型（見 4.3） |
| pembrolizumab | 2014 年，美國，ipilimumab 治療後惡化的黑色素瘤（Poole, 2014） | KEYNOTE-001：495 位 NSCLC，整體反應率 19.4%，用訓練組選出 PD-L1 ≥50% 當切點，驗證組中達切點者反應率 45.2%（Garon et al., 2015）；其餘見 5.2 | 200 mg q3w 或 400 mg q6w（Merck Sharp & Dohme, 2026）；適應症很廣，含不分癌別的 MSI-H／dMMR 與 TMB-H |
| cemiplimab | 2018 年 9 月，美國，晚期皮膚鱗狀細胞癌（Markham & Duggan, 2018） | EMPOWER-Lung 1：PD-L1 ≥50% 的晚期 NSCLC 第一線單用，對化療的死亡風險 HR 0.57，無惡化存活 8.2 對 5.7 個月（Sezer et al., 2021） | 肺癌 PD-L1 ≥50% 第一線單用的選項之一（另外兩個是 pembrolizumab 與 atezolizumab，見[肺癌章 4.3](../01-lung-cancer.md#43-nsclc-iv-期)） |
| tislelizumab | 2019 年 12 月，中國，復發或難治的典型何杰金氏淋巴瘤（Lee & Keam, 2020） | RATIONALE-306：晚期食道鱗狀細胞癌第一線併化療，整體存活 17.2 對 10.6 個月（HR 0.66）（Xu et al., 2023） | 健保 9.69 的肺癌給付列有 tislelizumab，條件見[肺癌章 9.3](../01-lung-cancer.md#93-免疫檢查點抑制劑969) |
| dostarlimab | 2021 年，歐盟與美國，dMMR 的復發或晚期子宮內膜癌（Markham, 2021） | dMMR 局部晚期直腸癌：12 位完成治療者全部達到臨床完全反應（Cercek et al., 2022）；美國於 2026-10-19 加速核准此用法（US Food and Drug Administration, 2026） | 第一個核准就是依 dMMR 選病人，而不是依器官 |
| toripalimab | 2018 年 12 月，中國，治療後惡化的黑色素瘤（Keam, 2019） | JUPITER-02：復發或轉移性鼻咽癌第一線，併 gemcitabine ＋ cisplatin，無惡化存活 21.4 對 8.2 個月（HR 0.52），死亡風險 HR 0.63；收案地區包含台灣（Mai et al., 2023） | 美國於 2023-10-27 核准用於鼻咽癌（US Food and Drug Administration, 2026） |

同一類的藥彼此之間很少有直接比較的試驗。實際選哪一個，取決於哪個藥在那個癌別有試驗、有藥證、有給付。台灣藥證與給付請見各癌別章第 9 段。

### 3.2 PD-L1 抑制劑

| 藥名 | 第一個核准 | 代表試驗（本手冊相關） | 備註 |
|------|-----------|---------------------|------|
| atezolizumab | 2016 年，美國，泌尿上皮癌二線（Markham, 2016） | IMpower110：PD-L1 高表現、EGFR 與 ALK 野生型的 NSCLC 第一線單用，整體存活 20.2 對 13.1 個月（HR 0.59）（Herbst et al., 2020）；IMpower133 與肺泡狀軟組織肉瘤見 5.2 | 840 mg q2w、1,200 mg q3w 或 1,680 mg q4w（Genentech, 2026）；有皮下劑型；PD-L1 常用 SP142 判讀（見 5.1） |
| durvalumab | 2017 年，美國，泌尿上皮癌（加速核准）（Syed, 2017） | PACIFIC、ADRIATIC、CASPIAN（見 5.2） | 「化放療之後接著打」的代表藥 |
| avelumab | 2017 年，美國，轉移性 Merkel 細胞癌（加速核准）（Kim, 2017） | JAVELIN Bladder 100：晚期泌尿上皮癌第一線化療後的維持治療，整體存活 21.4 對 14.3 個月（HR 0.69）（Powles et al., 2020） | 半衰期只有 6.1 天，800 mg q2w；**前 4 次輸注前要先給抗組織胺與 acetaminophen**（EMD Serono, 2026） |

### 3.3 CTLA-4 抑制劑

- **Ipilimumab**：2011 年在美國核准用於黑色素瘤（Cameron et al., 2011）。現在多半和 nivolumab 合併。在 NSCLC，nivolumab ＋ ipilimumab 對化療的整體存活，PD-L1 ≥1% 者是 17.1 對 14.9 個月，PD-L1 <1% 者是 17.2 對 12.2 個月（CheckMate 227；Hellmann et al., 2019）。
- **Tremelimumab**：2022 年 10 月在美國核准，與 durvalumab 合併用於無法切除的肝細胞癌，11 月加上轉移性 NSCLC（與 durvalumab、含鉑化療合併）（Keam, 2023）。肝細胞癌的 HIMALAYA 試驗只給一劑 300 mg 的 tremelimumab 當「起動」，之後 durvalumab 每 4 週一次，對 sorafenib 的整體存活 16.43 對 13.77 個月（HR 0.78）（Abou-Alfa et al., 2022）。NSCLC 的 POSEIDON 試驗中，tremelimumab ＋ durvalumab ＋ 化療對化療的整體存活 14.0 對 11.7 個月（HR 0.77）；只加 durvalumab 的那一組，整體存活的差異沒有達到統計顯著（HR 0.86）（Johnson et al., 2023）。
- **共同的設計思路**：CTLA-4 抑制劑毒性大，所以新的處方傾向把它用得少：HIMALAYA 只給一劑，POSEIDON 只給限定的療程，把它當成 PD-1／PD-L1 抑制劑的「起動器」。
- 健保 9.69 中，ipilimumab 與 tremelimumab 都沒有肺癌用法（見[肺癌章 9.3](../01-lung-cancer.md#93-免疫檢查點抑制劑969)）。

### 3.4 LAG-3 抑制劑

Relatlimab 是第一個 LAG-3 抗體，和 nivolumab 做成固定劑量的合併製劑，每 4 週給一次；2022 年 3 月在美國核准用於 12 歲以上、體重至少 40 kg 的無法切除或轉移性黑色素瘤（Paik, 2022）。RELATIVITY-047 試驗中，合併組對 nivolumab 單用的無惡化存活是 10.1 對 4.6 個月（HR 0.75），3–4 級治療相關不良事件 18.9% 對 9.7%（Tawbi et al., 2022）。這個毒性數字比 CheckMate 067 中 nivolumab ＋ ipilimumab 的 55.0% 低（Larkin et al., 2015），但兩個試驗不能直接比較。本手冊的四個癌別目前沒有用到它。

### 3.5 雙特異性 T 細胞銜接抗體（bispecific T-cell engager）

| 比較 | blinatumomab | tarlatamab |
|------|-------------|-----------|
| 兩端抓什麼 | CD19（B 細胞）與 CD3（T 細胞） | DLL3（小細胞肺癌）與 CD3（T 細胞） |
| 半衰期與給法 | 約 2 小時，所以要連續靜脈輸注（Zhu et al., 2016） | 11 天，每 2 週給一次（Amgen, 2026） |
| 美國核准 | 2014-12-03 加速核准，費城染色體陰性的復發或難治 B 細胞急性淋巴性白血病，完全緩解率 32%（Przepiorka et al., 2015） | 2024-05-16 加速核准，含鉑化療後惡化的擴散期小細胞肺癌（Liu et al., 2026）；2025-11-19 轉為傳統核准（US Food and Drug Administration, 2026） |
| 關鍵數字 | 0.06 mg/m²/day 劑量組的 7 位淋巴瘤病人全部腫瘤縮小（Bargou et al., 2008） | DeLLphi-301：10 mg 組反應率 40%（Ahn et al., 2023）；DeLLphi-304：對化療的整體存活 13.6 對 8.3 個月（HR 0.60），3 級以上不良事件 54% 對 80%（Mountzios et al., 2025） |
| 類別毒性 | CRS 與神經毒性是嚴重毒性（Przepiorka et al., 2015） | 仿單合併族群 CRS 57%（3 級 1.7%、4 級 0.2%），發生 CRS 的病人有 73% 是在第一劑之後；神經毒性 65%，3 級以上 7%；加框警語（Amgen, 2026） |
| 怎麼降低 CRS | 階梯式劑量（Zhu et al., 2016） | 先給 1 mg 的起始劑量，一週後才升到 10 mg；前兩劑在醫療機構監測 6–8 小時（Amgen, 2026） |

- **CRS（cytokine release syndrome）** 是 T 細胞一口氣被活化、大量釋放細胞激素造成的發燒、低血壓與缺氧。**ICANS（immune effector cell-associated neurotoxicity syndrome）** 是隨之而來的神經毒性。兩者的 ASTCT 分級（Lee et al., 2019）與處置在[腫瘤急症第 9 節](../00-shared/02-oncologic-emergencies.md#9-細胞激素釋放症候群crs與神經毒性icans)。
- Tarlatamab 的醫囑範本、監測表與出院衛教在[肺癌章 7.7](../01-lung-cancer.md#77-tarlatamab-病房實務c1d1c1d8-的醫囑監測與出院衛教)，本章不重複。
- 這類藥還有一個容易漏掉的交互作用：細胞激素短暫升高會抑制 CYP450，CRS 發生期間到之後 14 天內，併用的 CYP 受質藥物濃度可能上升（Amgen, 2026）。病人若在吃 warfarin 這類治療範圍窄的藥，CRS 之後要加強監測。

> [!TIP]
> **把警察和小偷銬在一起**
> ICI 是對警察喊「可以動手了」，但警察得自己找到小偷。T 細胞銜接抗體更直接：它是一副手銬，一邊銬住 T 細胞的 CD3，一邊銬住腫瘤細胞的抗原，不管這個 T 細胞原本認不認得腫瘤，銬在一起就會動手。好處是不必靠 MHC；代價是第一次給藥時，全身的 T 細胞同時被叫醒，細胞激素一口氣放出來。所以這類藥都從很小的劑量開始。

### 3.6 細胞治療：CAR-T、TCR-T 與 TIL

| 比較 | CAR-T | TCR-T | TIL |
|------|-------|-------|-----|
| 代表藥 | tisagenlecleucel（標的 CD19） | afamitresgene autoleucel（標的 MAGE-A4） | lifileucel |
| 怎麼認腫瘤 | 人工受體直接認細胞表面的抗原 | 轉入的 T 細胞受體，認的是 HLA 呈現的抗原；病人要先驗 HLA-A*02 型別與腫瘤的 MAGE-A4（Barnett et al., 2025） | 腫瘤裡原本就在的 T 細胞，取出後擴增；它是第一個獲美國核准、取自腫瘤的 T 細胞治療（Hu et al., 2025） |
| 細胞從哪裡來 | 病人自己的 T 細胞，經基因改造 | 病人自己的 T 細胞，經基因改造 | 手術取下的腫瘤，在製造廠擴增約 22 天（Sarnaik et al., 2021） |
| 流程 | fludarabine ＋ cyclophosphamide 淋巴球清除，2 至 14 天後單次輸注（O'Leary et al., 2019） | 淋巴球清除後單次輸注（Barnett et al., 2025） | 淋巴球清除、單次輸注，之後最多 6 劑高劑量 IL-2（Sarnaik et al., 2021） |
| 核准時的療效 | 25 歲以下的復發或難治 B 細胞急性淋巴性白血病，完全緩解率 63%（O'Leary et al., 2019）；ELIANA 試驗 3 個月內緩解率 81%（Maude et al., 2018） | 滑膜肉瘤反應率 43.2%，中位反應持續 6.0 個月（Barnett et al., 2025）；SPEARHEAD-1 論文中全體 52 人（含黏液樣／圓細胞脂肪肉瘤）的反應率是 37%，滑膜肉瘤 39%（D'Angelo et al., 2024） | PD-1 抑制劑治療過的黑色素瘤，反應率 31.5%（Hu et al., 2025） |
| 主要毒性 | CRS 77%（其中 48% 用到 tocilizumab）、神經事件 40%（Maude et al., 2018） | CRS 75%（3 級以上 2%），加框警語（Barnett et al., 2025） | 3 級不良事件 95.5%、4 級 87.8%；加框警語包含治療相關死亡、長期嚴重血球低下、嚴重感染、心肺與腎功能損害（Hu et al., 2025） |
| 美國核准 | 2017-08-30（O'Leary et al., 2019） | 2024-08-01 加速核准（Barnett et al., 2025） | 2024-02-16 加速核准（Hu et al., 2025） |

- TIL 的療效另有一個第 3 期試驗：168 位晚期黑色素瘤病人（86% 對 PD-1 抑制劑無效），TIL（此試驗用的不是 lifileucel）對 ipilimumab 的無惡化存活 7.2 對 3.1 個月（HR 0.50）；TIL 組所有病人都有 3 級以上的治療相關不良事件，主要是化療造成的骨髓抑制（Rohaan et al., 2022）。
- **和本手冊的關係**：afamitresgene autoleucel 是肉瘤的第一個細胞治療，台灣沒有藥證，細節在[肉瘤章 4.4.4](../04-sarcoma.md#444-依組織型選藥)。CAR-T 目前用在血液腫瘤；病房會遇到的是 CRS 的處置，以及執行醫院必須備妥 tocilizumab 的規定（[腫瘤急症 9.4](../00-shared/02-oncologic-emergencies.md#94-台灣藥證與健保給付)）。

> [!TIP]
> **三種增援方式**
> 現場的警察不夠用時，有三種增援。TIL 是把已經在現場、認得犯人的警察帶回基地，複製成一大隊再送回去。TCR-T 是替一般警察配一副專看某個標記的眼鏡，眼鏡只對特定的 HLA 型別對得了焦，所以要先驗 HLA。CAR-T 是替警察裝上導航與自動鎖定，直接追細胞表面的目標，不需要 MHC。三種都要先用化療把體內原有的淋巴球清掉，替新來的隊伍騰出空間，所以血球低下與感染是共同的代價。

### 3.7 細胞激素與膀胱內 BCG

- **高劑量 IL-2（aldesleukin）**：美國 1992 年核准用於轉移性腎細胞癌，1998 年加上轉移性黑色素瘤（Rosenberg, 2014）。反應率約 16%，但完全反應可以很持久；毒性大，270 人的系列中 2% 死於不良事件（Atkins et al., 1999）。
- **Interferon alfa-2b**：高劑量用一年，在高風險黑色素瘤術後輔助的隨機試驗中延長存活，但多數病人因毒性需要調整劑量（Kirkwood et al., 1996）。
- **膀胱內 BCG**：用於表淺性膀胱腫瘤，是 Coley 那條路線留到今天的代表（Morales et al., 1976）。本手冊的四個癌別用不到。

### 3.8 癌症疫苗

Sipuleucel-T 是第一個獲美國 FDA 核准的治療性癌症疫苗，設計來誘發針對前列腺酸性磷酸酶（prostatic acid phosphatase）的免疫反應（Cheever & Higano, 2011）；在轉移性去勢抗性攝護腺癌，整體存活 25.8 對 21.7 個月（HR 0.78），但客觀惡化時間沒有差別（Kantoff et al., 2010）。個人化 mRNA 新抗原疫苗仍在試驗階段：切除後的高風險黑色素瘤，mRNA-4157 ＋ pembrolizumab 對 pembrolizumab 單用的無復發存活 HR 0.561（95% CI 0.309–1.017，雙尾 p = 0.053），這是第 2b 期試驗（Weber et al., 2024）；胰臟癌術後的第 1 期試驗（16 人，atezolizumab、autogene cevumeran 與 mFOLFIRINOX 依序給予）中，8 人產生疫苗誘發的 T 細胞，這 8 人的中位無復發存活尚未達到，其餘 8 人是 13.4 個月（Rojas et al., 2023）。兩者都還不是標準治療。另外，美國於 2026-08-06 加速核准溶瘤病毒 vusolimogene oderparepvec 與 nivolumab 併用於 PD-1 抑制劑治療後惡化的晚期黑色素瘤（US Food and Drug Administration, 2026）。

---

## 4. 藥物動力學與交互作用

**這一段的結論先講：** ICI 是抗體，打進靜脈、不經 CYP 代謝、半衰期約 3 到 4 週、不必依肝腎功能調整劑量。真正影響療效與安全的「交互作用」不是藥對藥，而是病人的免疫狀態：類固醇、自體免疫疾病、器官移植，以及之後要接的標靶藥。

### 4.1 抗體藥的動力學

| 藥 | 半衰期 | 美國仿單的常用給法 | 來源 |
|----|--------|------------------|------|
| pembrolizumab | 22 天 | 200 mg q3w 或 400 mg q6w，靜脈輸注 30 分鐘 | Merck Sharp & Dohme, 2026 |
| nivolumab | 25 天 | 240 mg q2w 或 480 mg q4w | Bristol-Myers Squibb, 2026 |
| atezolizumab | 27 天 | 840 mg q2w、1,200 mg q3w 或 1,680 mg q4w | Genentech, 2026 |
| avelumab | 6.1 天 | 800 mg q2w | EMD Serono, 2026 |
| tarlatamab | 11 天 | 階梯起始後 10 mg q2w | Amgen, 2026 |
| blinatumomab | 約 2 小時 | 連續靜脈輸注 | Zhu et al., 2016 |

- **代謝**：抗體被分解成小胜肽，不靠 CYP。仿單對 avelumab 的描述是「主要經蛋白分解排除」（EMD Serono, 2026），tarlatamab 是「預期經分解代謝路徑變成小胜肽」（Amgen, 2026）。
- **器官功能**：pembrolizumab 的清除率不受年齡、性別、腎功能不全（eGFR ≥15 mL/min/1.73 m²）、輕到中度肝功能不全影響，重度肝功能不全的影響未知（Merck Sharp & Dohme, 2026）；nivolumab 的仿單寫法相同（Bristol-Myers Squibb, 2026）。這和需要依肌酸酐清除率調整的 carboplatin、pemetrexed 很不一樣。
- **藥效比血中濃度更久**：第 1 期試驗中，anti-PD-1 抗體的血清半衰期是 12–20 天，但輸注後 2 個月以上，T 細胞上仍有七成以上的 PD-1 被占住（Brahmer et al., 2010）。
- **所以 irAE 會在停藥後出現**：仿單寫明免疫相關不良反應可以在開始治療後的任何時間發生，包含停藥之後（Merck Sharp & Dohme, 2026）。文獻回顧整理了 23 個停藥 90 天以後才發生的案例，距離最後一劑的中位時間是 6 個月（範圍 3 至 28 個月）（Couey et al., 2019）。
- **避孕**：pembrolizumab 仿單要求有生育可能的女性在治療期間與最後一劑後 4 個月內有效避孕（Merck Sharp & Dohme, 2026）。

> [!TIP]
> **藥停了，煞車線還沒接回去**
> 化療藥幾天內就排掉，毒性跟著藥走。ICI 不一樣：抗體本身要好幾個月才代謝完，它叫醒的 T 細胞更是不會因為停藥就回去睡。所以「最後一次打免疫治療是三個月前」不能排除 irAE。病人到急診、到別科門診時，這個病史要寫在最前面。

### 4.2 固定劑量與延長間隔

- 早期試驗依體重給藥（mg/kg）。後來用族群藥動學模型證明，固定劑量的暴露量和依體重給藥相當：nivolumab 240 mg q2w 的暴露量分布與 3 mg/kg q2w 相近，這個改變靠的是模型分析，沒有另外做臨床試驗（Zhao et al., 2017）。
- 延長間隔也是同樣的方法：nivolumab 480 mg q4w 的平均濃度與 3 mg/kg q2w 相近，谷濃度約低 16%、峰濃度約高 45%（Long et al., 2018）；pembrolizumab 400 mg q6w 的預測暴露量與 200 mg q3w 相近（Lala et al., 2020）。
- **對病房的意義**：q6w 與 q4w 讓病人少跑醫院，但兩次回診之間沒有人幫忙問症狀。間隔拉長時，衛教與電話追蹤要補上（見第 8 段）。

> [!IMPORTANT]
> **ICI 沒有「減量」這個選項**
> Pembrolizumab 與 nivolumab 的仿單都寫明不建議減量：原則上 3 級免疫相關不良反應暫停，4 級永久停用（Merck Sharp & Dohme, 2026；Bristol-Myers Squibb, 2026）。化療遇到毒性是「減 20% 再打」，ICI 遇到毒性只有「等」或「停」兩條路。考題出現「pembrolizumab 減為 150 mg」的選項，一定是錯的。

### 4.3 皮下劑型

| 藥 | 美國核准日 | 依據的試驗 | 給法與重點 |
|----|-----------|-----------|-----------|
| atezolizumab ＋ hyaluronidase | 2024-09-12 | IMscin001：第 1 週期谷濃度的幾何平均比 1.05、曲線下面積 0.87，無惡化存活 HR 1.08（Burotto et al., 2023） | 1,875 mg，大腿皮下注射約 7 分鐘，q3w；適用於靜脈劑型的所有成人適應症（US Food and Drug Administration, 2024） |
| nivolumab ＋ hyaluronidase | 2024-12-27 | CheckMate-67T：495 位腎細胞癌，藥動學不劣於靜脈劑型，反應率 24.2% 對 18.2%（Albiges et al., 2025） | 核准日期見 US Food and Drug Administration（2026）；劑量依適應症，見仿單 |
| pembrolizumab ＋ berahyaluronidase alfa | 2025-09-19 | 3475A-D77：377 位轉移性 NSCLC，皮下 790 mg q6w 對靜脈 400 mg q6w，暴露量不劣，反應率 45.4% 對 42.1%，注射時間中位數 2 分鐘（Felip et al., 2025） | 395 mg q3w 或 790 mg q6w；適用於靜脈劑型的實體腫瘤適應症（12 歲以上）（US Food and Drug Administration, 2025） |

> [!WARNING]
> **皮下劑型和靜脈劑型的毫克數不一樣**
> Pembrolizumab 靜脈 400 mg q6w 對應皮下 790 mg q6w；atezolizumab 靜脈 1,200 mg q3w 對應皮下 1,875 mg q3w。兩種劑型是不同的品項，不能互相替代，也不能把皮下製劑接到靜脈管路。核對醫囑時，劑型、劑量、途徑三項要一起看。

> [!CAUTION]
> **待核對：皮下劑型在台灣的狀態**
> 上表是美國核准資料。台灣方面，本手冊只在[肉瘤章 4.4.4](../04-sarcoma.md#444-依組織型選藥)記載 atezolizumab 皮下劑型有藥證；nivolumab 與 pembrolizumab 皮下劑型的台灣藥證與給付，本章沒有查證，請以各癌別章第 9 段與院內處方集為準。

### 4.4 真正要查的「交互作用」

| 情境 | 證據 | 實務 |
|------|------|------|
| 開始 ICI 時正在用類固醇 | 640 位 NSCLC 病人中 14% 在開始時使用 prednisone ≥10 mg/day，原因以喘（33%）、疲倦（21%）、腦轉移（19%）最多；多變項分析的無惡化存活 HR 1.3、整體存活 HR 1.7（Arbour et al., 2018）。另一個 650 人的世代發現，差別只出現在「因緩和症狀而用」的病人（中位存活 2.2 個月），因非癌症原因而用的病人（10.7 個月）和用量 <10 mg 的病人（11.2 個月）相近（Ricciuti et al., 2019） | 類固醇可能有一部分只是預後差的標記。開始前檢視每一顆類固醇，沒有必要的減到 <10 mg/day；腦水腫這類必要的使用不要硬停 |
| 治療 irAE 的類固醇 | 298 位用 ipilimumab 的病人中 35% 需要全身性類固醇，整體存活與治療失敗時間不受影響（Horvat et al., 2015）；576 位用 nivolumab 的病人中 24% 用過全身性免疫調節藥物，不影響反應率（Weber et al., 2017） | irAE 該用類固醇就用，不要因為怕影響療效而延誤 |
| 抗生素 | 開始 ICI 前 30 天內用過抗生素的 NSCLC 病人，無惡化存活 1.9 對 3.8 個月、整體存活 7.9 對 24.6 個月（Derosa et al., 2018）；另一個研究同樣看到用過抗生素的病人 ICI 療效較差，並在小鼠實驗中發現，移植有反應病人的糞便菌相可以改善 PD-1 抑制劑的效果，移植無反應病人的則不行（Routy et al., 2018） | 人的資料是觀察性的**相關**，不是因果：需要抗生素的病人本來就比較嚴重。感染該治療就治療；沒有適應症的抗生素本來就不該開 |
| 疫苗 | ASCO 2024 指引把疫苗接種列為癌症照護的一環（Kamboj et al., 2024） | 不活化疫苗（流感、COVID-19 等）可以打，活性減毒疫苗不可以；ICI 病人的細節整理在[支持性照護 13.2](../00-shared/03-supportive-care.md#132-疫苗) |
| 原有自體免疫疾病 | 52 位有自體免疫疾病的黑色素瘤病人使用 PD-1 抑制劑：38% 原疾病發作而需要免疫抑制，4% 因此停藥，反應率 33%；腸胃道與神經系統疾病者無人發作（Menzies et al., 2017） | 不是絕對禁忌，但要先和原本的專科醫師討論、把基線狀態記清楚，並告知病人發作的機率 |
| 器官移植 | 39 位實體器官移植後使用 ICI 的病人，41% 發生排斥，中位發生時間 21 天；發生排斥者 81% 失去移植器官（Abdel-Wahab et al., 2019）。仿單也把移植器官排斥列為免疫相關不良反應，並對異體造血幹細胞移植前後使用提出警語（Merck Sharp & Dohme, 2026） | 開藥前一定要問移植史；要用時由移植團隊共同決定 |
| 之後要接 osimertinib | PD-(L)1 抑制劑之後 3 個月內開始 osimertinib，24% 發生 3–4 級 irAE；順序反過來或接其他 EGFR-TKI 則沒有觀察到（Schoenfeld et al., 2019） | NSCLC 先等基因報告；細節見[肺癌章 2.2](../01-lung-cancer.md#22-必驗-biomarker) |
| 結核病與 B 型肝炎 | 見其他章 | [irAE 章 2.1](../00-shared/04-irae.md#21-結核病tb史與篩檢)與[化療基礎第 6 節](../00-shared/01-chemo-basics.md#6-b-型肝炎篩檢與預防性抗病毒) |

---

## 5. 臨床怎麼用

**這一段的結論先講：** 開免疫治療前先回答三個問題：這個癌別有沒有試驗支持？病人有沒有對應的 biomarker？有沒有不該先用免疫治療的理由（EGFR／ALK）？處方劑量在各癌別章第 5 段，給付條件在第 9 段，本段只講「為什麼這樣用」。

### 5.1 Biomarker：PD-L1 有三種算法

| 算法 | 算的是什麼 | 本手冊會遇到的用法 |
|------|-----------|-----------------|
| TPS（tumor proportion score） | 有 PD-L1 染色的腫瘤細胞占全部腫瘤細胞的百分比 | NSCLC：KEYNOTE-024 以 TPS ≥50% 選病人單用 pembrolizumab（Reck et al., 2016），健保單用的門檻也是 TPS ≧50%；美國仿單的單用適應症則寫 TPS ≥1%（Merck Sharp & Dohme, 2026） |
| CPS（combined positive score） | 把染色的腫瘤細胞和免疫細胞合在一起算（Kulangara et al., 2019）；公式見[乳癌章 2.6](../03-breast-cancer.md#26-轉移或復發時的-biomarker) | 轉移性三陰性乳癌：pembrolizumab ＋ 化療要 CPS ≥10（Cortes et al., 2022） |
| IC（immune cell） | 腫瘤浸潤免疫細胞的 PD-L1 染色 | atezolizumab 的判讀方式；健保對 NSCLC 單用的門檻是 TC ≥50% 或 IC ≥10%（見[肺癌章 9.3](../01-lung-cancer.md#93-免疫檢查點抑制劑969)） |

- **抗體株不能任意互換**：Blueprint 計畫第 2 階段用 81 個肺癌檢體比較五種抗體株，22C3、28-8、SP263 在腫瘤細胞上的染色高度相近，SP142 比較不敏感，73-10 比較敏感（Tsao et al., 2018）。
- **免疫細胞的判讀不穩定**：病理醫師之間，腫瘤細胞評分的一致性很好（組內相關係數 0.86–0.93），免疫細胞評分的一致性很差（0.18–0.19）（Tsao et al., 2018）。
- **TPS 和 CPS 不是同一個數字**：同一批胃癌檢體，CPS ≥1 的有 57.6%，TPS ≥1% 的只有 12.5%（Kulangara et al., 2019）。報告上寫「PD-L1 10%」而沒有寫算法，等於沒有寫。
- 健保 9.69 規定每個藥要用哪一個抗體株檢測，對照表在[肺癌章 9.3](../01-lung-cancer.md#93-免疫檢查點抑制劑969)。

> [!IMPORTANT]
> **讀 PD-L1 報告先問四件事**
> 1. 哪一個抗體株（22C3、28-8、SP263、SP142）？
> 2. 哪一種算法（TPS、CPS、IC）？
> 3. 這個癌別、這個藥的切點是多少（NSCLC 單用 TPS ≥50%；三陰性乳癌 CPS ≥10）？
> 4. 病人有沒有驅動基因？PD-L1 再高，也不能取代 EGFR／ALK 檢測。

**MSI-H／dMMR 與 TMB：不分癌別的 biomarker**

- **MSI-H／dMMR**：KEYNOTE-158 收了 233 位非大腸直腸癌的 MSI-H／dMMR 病人（27 種癌別），反應率 34.3%，中位整體存活 23.5 個月（Marabelle et al., 2020）。
- **TMB-H**：2020-06-16 美國加速核准 pembrolizumab 用於 TMB ≥10 mut/Mb 的實體腫瘤，依據是 KEYNOTE-158 中 102 位病人的反應率 29%（Marcus et al., 2021）。2026-10-16 改為傳統核准（US Food and Drug Administration, 2026），現行美國仿單把 TMB-H 定義為 **≥13 mut/Mb**（FoundationOne CDx），220 位病人的反應率 36%（Merck Sharp & Dohme, 2026）。

> [!CAUTION]
> **待核對：TMB-H 的切點正在改**
> 美國仿單的 TMB-H 切點在 2026-10 的版本是 ≥13 mut/Mb，2020 年加速核准時是 ≥10 mut/Mb（Marcus et al., 2021）。本手冊其他章節引用的指引與台灣仿單是否已跟著修改，本章沒有查證。看到 TMB 報告時，要同時確認檢測平台與當時適用的切點；台灣藥證與給付請見各癌別章第 9 段。

### 5.2 本手冊四個癌別怎麼用

| 癌別與情境 | 用法 | 關鍵試驗與數字 | 處方與給付 |
|-----------|------|--------------|-----------|
| NSCLC 轉移性，無驅動基因，PD-L1 ≥50% | PD-1／PD-L1 抑制劑單用，或化療 ＋ 免疫 | KEYNOTE-024：無惡化存活 10.3 對 6.0 個月（HR 0.50），5 年存活 31.9% 對 16.3%（Reck et al., 2016；Reck et al., 2021） | [肺癌 4.3](../01-lung-cancer.md#43-nsclc-iv-期)、[9.3](../01-lung-cancer.md#93-免疫檢查點抑制劑969) |
| NSCLC 轉移性，無驅動基因，其餘 PD-L1 | 含鉑化療 ＋ pembrolizumab | KEYNOTE-189（非鱗狀）：死亡風險 HR 0.49（Gandhi et al., 2018），5 年存活 19.4% 對 11.3%（Garassino et al., 2023）；KEYNOTE-407（鱗狀）：整體存活 15.9 對 11.3 個月（HR 0.64）（Paz-Ares et al., 2018） | 同上 |
| NSCLC III 期不可切除，同步化放療後未惡化 | durvalumab 鞏固 | PACIFIC：無惡化存活 16.8 對 5.6 個月（HR 0.52）（Antonia et al., 2017），5 年存活 42.9% 對 33.4%（Spigel et al., 2022） | [肺癌 4.2](../01-lung-cancer.md#42-nsclc-iii-期) |
| NSCLC 可切除 | 術前化療 ＋ nivolumab，或圍術期 pembrolizumab | CheckMate 816：病理完全反應 24.0% 對 2.2%（Forde et al., 2022），5 年存活 65.4% 對 55.0%（HR 0.72）（Forde et al., 2025）；KEYNOTE-671：無事件存活 47.2 對 18.3 個月，36 個月存活 71% 對 64%（HR 0.72）（Spicer et al., 2024） | [肺癌 4.1](../01-lung-cancer.md#41-nsclc-iii-期可切除) |
| SCLC 擴散期第一線 | carboplatin ＋ etoposide ＋ atezolizumab 或 durvalumab | IMpower133：整體存活 12.3 對 10.3 個月（HR 0.70）（Horn et al., 2018）；CASPIAN：13.0 對 10.3 個月（HR 0.73）（Paz-Ares et al., 2019） | [肺癌 4.4](../01-lung-cancer.md#44-sclc) |
| SCLC 局限期，同步化放療後未惡化 | durvalumab 鞏固 | ADRIATIC：整體存活 55.9 對 33.4 個月（HR 0.73）（Cheng et al., 2024） | 同上 |
| SCLC 含鉑化療後惡化 | tarlatamab | DeLLphi-304：整體存活 13.6 對 8.3 個月（HR 0.60）（Mountzios et al., 2025） | [肺癌 4.4](../01-lung-cancer.md#44-sclc)、[7.7](../01-lung-cancer.md#77-tarlatamab-病房實務c1d1c1d8-的醫囑監測與出院衛教) |
| 早期三陰性乳癌（II–III 期） | 術前化療 ＋ pembrolizumab，術後續用 pembrolizumab | KEYNOTE-522：病理完全反應 63.0% 對 55.6%（Merck Sharp & Dohme, 2026），36 個月無事件存活 84.5% 對 76.8%（HR 0.63）（Schmid et al., 2022），5 年存活 86.6% 對 81.7%（Schmid et al., 2024） | [乳癌 4.6](../03-breast-cancer.md#46-早期三陰性keynote-522-為骨幹殘存病灶再加碼)、[9.3](../03-breast-cancer.md#93-三陰性與-gbrca免疫治療parp-抑制劑sacituzumab-govitecan-與-larotrectinib) |
| 轉移性三陰性乳癌 | 化療 ＋ pembrolizumab，限 CPS ≥10 | KEYNOTE-355：CPS ≥10 的整體存活 23.0 對 16.1 個月（HR 0.73）；CPS ≥1 是 17.6 對 16.0 個月，未達顯著（Cortes et al., 2022）。Atezolizumab ＋ nab-paclitaxel 的 IMpassion130：全體整體存活 21.3 對 17.6 個月（HR 0.84），未達顯著（Schmid et al., 2018） | [乳癌 4.9](../03-breast-cancer.md#49-轉移性三陰性看-pd-l1看前線用藥) |
| 胰臟癌 | 只有 MSI-H／dMMR 才考慮 pembrolizumab | KEYNOTE-158 的胰臟癌 22 人，反應率 18%（95% CI 5–40）（Merck Sharp & Dohme, 2026）。不挑 biomarker 時，durvalumab ± tremelimumab 二線的反應率只有 3.1% 與 0%（O'Reilly et al., 2019） | [胰臟癌 4.10](../02-pancreatic-cancer.md#410-生物標記導向治療與-kras-標靶)、[9.5](../02-pancreatic-cancer.md#95-有藥證或指引建議但原文沒有胰臟條文的藥) |
| 肉瘤：肺泡狀軟組織肉瘤（ASPS） | atezolizumab | 論文反應率 37%（19/52，中位反應持續 24.7 個月）（Chen et al., 2023）；美國仿單的獨立審查反應率 24%（49 人）（Genentech, 2026） | [肉瘤 4.4.4](../04-sarcoma.md#444-依組織型選藥)、[9.4](../04-sarcoma.md#94-本章提到但第-9-節沒有肉瘤條文的藥) |
| 肉瘤：其他組織型 | 不是常規；依組織型差很多 | SARC028（pembrolizumab）：軟組織肉瘤 18%（7/40），其中未分化多形性肉瘤 4/10、脂肪肉瘤 2/10、滑膜肉瘤 1/10、平滑肌肉瘤 0/10；骨肉瘤 1/22、Ewing 肉瘤 0/13（Tawbi et al., 2017）。Alliance A091401：nivolumab 單用 5%，加 ipilimumab 16%（D'Angelo et al., 2018） | [肉瘤 4.4.4](../04-sarcoma.md#444-依組織型選藥) |
| 肉瘤：滑膜肉瘤 | TCR-T（afamitresgene autoleucel） | 反應率 43.2%（Barnett et al., 2025） | 台灣無藥證，見[肉瘤 4.4.4](../04-sarcoma.md#444-依組織型選藥) |

> [!TIP]
> **為什麼肺癌用得多、胰臟癌幾乎用不上**
> 回到 2.1 的循環想。單用 PD-1 抑制劑，只在腫瘤裡本來就有抗腫瘤免疫反應時有效（Pardoll, 2012）。有 T 細胞浸潤的「熱」腫瘤，拆掉煞車就有人可以動手；沒有 T 細胞的「冷」腫瘤，拆了煞車也沒有人在現場（Galon & Bruni, 2019）。不挑 biomarker 的胰臟癌，反應率只有 0 到 3%，表現得像冷腫瘤；MSI-H／dMMR 突變多、抗原多，是例外。三陰性乳癌要靠 CPS 挑病人。肉瘤種類多，只有少數組織型有反應。

### 5.3 用多久、什麼時候停

- **轉移性疾病**：KEYNOTE-024 與 KEYNOTE-189 的 pembrolizumab 都設計成最多 35 個週期（約 2 年）（Reck et al., 2021；Garassino et al., 2023）。KEYNOTE-024 完成 35 個週期的 39 人，約 5 年時 82.1% 仍存活（Reck et al., 2021）。健保 9.69 的給付時程也是 2 年（見[肺癌章 9.3](../01-lung-cancer.md#93-免疫檢查點抑制劑969)）。
- **不要太早停**：CheckMate 153 把用滿 1 年的 NSCLC 病人隨機分成繼續用與停藥，繼續用的無惡化存活 24.7 對 9.4 個月（HR 0.56）（Waterhouse et al., 2020）。
- **輔助、鞏固與圍術期**：療程是固定的，例如 PACIFIC 的 durvalumab 是 12 個月；各試驗的療程長度見上表連結的章節。
- **因 irAE 停藥**：停藥不等於失去療效，已經啟動的免疫反應可以持續（見 2.3）；能不能重新給藥見第 8 段。

### 5.4 為什麼 EGFR／ALK 報告要先出來

> [!WARNING]
> **有驅動基因的 NSCLC，不要先打免疫治療**
> - **效果差**：三個二線試驗的統合分析中，ICI 對 docetaxel 的整體存活在 EGFR 野生型是 HR 0.66，在 EGFR 突變型是 HR 1.05，沒有好處（Lee et al., 2017）。
> - **之後接 osimertinib 會出事**：3 個月內接上，24% 發生 3–4 級 irAE，中位發生在開始 osimertinib 後 20 天（Schoenfeld et al., 2019）。
> - **給付也受影響**：健保 9.69 要求附基因檢測報告，而且免疫治療無效後不再給付該適應症的標靶藥（見[肺癌章 9.3](../01-lung-cancer.md#93-免疫檢查點抑制劑969)）。
> - 所以專師在排第一次免疫治療前，要親眼看到 EGFR、ALK 的報告，而不是「已送驗」三個字。

---

## 6. 毒性與處置

**這一段的結論先講：** ICI 的毒性叫 irAE，本質是自體免疫，治療是暫停藥物加類固醇；T 細胞銜接抗體與細胞治療的毒性是 CRS 與 ICANS，治療是 tocilizumab 與類固醇。兩者的處置表都不在這裡：irAE 在[免疫治療副作用](../00-shared/04-irae.md)，CRS／ICANS 在[腫瘤急症第 9 節](../00-shared/02-oncologic-emergencies.md#9-細胞激素釋放症候群crs與神經毒性icans)。這一段只幫你建立「什麼時候該翻那兩章」的直覺。

### 6.1 irAE 一頁看完

**多常見：**

- 單用 PD-1 抑制劑：2,799 位用 pembrolizumab 的病人中，甲狀腺功能低下 8%、免疫性肺炎 3.4%（其中致死 0.1%）、免疫性大腸炎 1.7%（Merck Sharp & Dohme, 2026）。
- 合併 CTLA-4 抑制劑：3–4 級治療相關不良事件從 16.3% 升到 55.0%（Larkin et al., 2015）。
- 會致死的比例：112 個試驗、19,217 人的統合分析，毒性致死率是 anti-PD-1 0.36%、anti-PD-L1 0.38%、anti-CTLA-4 1.08%、合併治療 1.23%（Wang et al., 2018）。

**什麼時候發生：**

| 時間點 | 資料 | 來源 |
|--------|------|------|
| 最早出現的器官 | 皮膚，中位約第 5 週 | Weber et al., 2017 |
| 最晚出現的器官 | 腎，中位約第 15 週；其他器官（腸胃、肝、內分泌等）介於兩者之間 | Weber et al., 2017 |
| 心肌炎 | 中位第 34 天（四分位距 21–75 天） | Mahmood et al., 2018 |
| 致死性毒性 | 合併治療中位第 14.5 天；單用 anti-PD-1 或 ipilimumab 中位第 40 天；從症狀出現到死亡中位 32 天 | Wang et al., 2018 |
| 停藥之後 | 個案報告中位在停藥後 6 個月，最長 28 個月 | Couey et al., 2019 |

**怎麼處理（通則）：** G1 多數繼續用藥並密切監測；G2 多數暫停，可給類固醇，回到 G1 以下再考慮恢復；G3 暫停並給高劑量類固醇，至少 4 到 6 週慢慢減；G4 原則上永久停用，以荷爾蒙補充控制的內分泌病變除外（Schneider et al., 2021）。完整的分級表、類固醇劑量與第二線免疫抑制劑見 [irAE 章第 3 節](../00-shared/04-irae.md#3-通用分級處置)與[第 6 節](../00-shared/04-irae.md#6-第二線免疫抑制劑)。

> [!WARNING]
> **會死人的 irAE：看到下列線索，當天處理**
> 通報資料庫的 613 個致死案例中，anti-CTLA-4 的死因七成是大腸炎；anti-PD-1／PD-L1 是肺炎（35%）、肝炎（22%）、神經毒性（15%）；合併治療是大腸炎（37%）與心肌炎（25%）。心肌炎的通報病例有 39.7% 死亡，是所有 irAE 中最高的（Wang et al., 2018）。
> - **心肌炎**：胸悶、喘、心悸、暈厥，或眼瞼下垂、複視、肌肉無力（常和肌炎、重症肌無力一起來）。立刻驗 troponin、CK、心電圖。見 [irAE 5.10](../00-shared/04-irae.md#510-心肌炎最致命的-irae)。
> - **肺炎**：新的咳嗽、喘、血氧下降。見 [irAE 5.4](../00-shared/04-irae.md#54-肺炎pneumonitis)。
> - **大腸炎**：腹瀉次數增加、血便、腹痛；腹痛加劇或腹膜徵象要想到穿孔。見 [irAE 5.2](../00-shared/04-irae.md#52-腸胃道腹瀉大腸炎)。
> - **肝炎**：AST、ALT 上升，先排除 B 肝再活化。見 [irAE 5.3](../00-shared/04-irae.md#53-肝炎)。
> - **神經**：肢體無力、吞嚥或呼吸困難、意識改變。見 [irAE 5.11](../00-shared/04-irae.md#511-神經系統)。
> - **內分泌急症**：口渴多尿、嘔吐、呼吸深快要想到糖尿病酮酸中毒（[irAE 5.8](../00-shared/04-irae.md#58-免疫治療相關糖尿病)）；低血壓、低血鈉、極度倦怠要想到腎上腺危象（[irAE 5.6](../00-shared/04-irae.md#56-腦下垂體炎hypophysitis)、[5.7](../00-shared/04-irae.md#57-原發性腎上腺功能不全)）。

**兩個常考的例外：**

- 內分泌 irAE 多半不可逆，但補充荷爾蒙後通常可以繼續 ICI；免疫治療相關糖尿病用胰島素，類固醇無效（見 [irAE 5.5](../00-shared/04-irae.md#55-甲狀腺) 至 5.8）。
- 懷疑腦下垂體炎或腎上腺功能不全時，先補糖皮質素，再補甲狀腺素（見 [irAE 5.6](../00-shared/04-irae.md#56-腦下垂體炎hypophysitis)）。

### 6.2 CRS 與 ICANS

- **誰會發生**：這是 T 細胞銜接抗體與細胞治療的類別毒性；ICI 的類別毒性是 irAE。
- **分級**：ASTCT 共識統一了 CRS 與神經毒性的定義與分級，適用於各種免疫效應細胞治療（Lee et al., 2019）。分級表（CRS 看發燒、低血壓、缺氧；ICANS 看 ICE 評分）在[腫瘤急症 9.2](../00-shared/02-oncologic-emergencies.md#92-astct-分級lee-et-al-2019)，處置在 [9.3](../00-shared/02-oncologic-emergencies.md#93-處置原則)。

| 治療 | CRS | 神經毒性 | 來源 |
|------|-----|---------|------|
| tarlatamab | 57%（3 級 1.7%、4 級 0.2%）；CRS 病人中 31% 用類固醇、10% 用 tocilizumab | 65%（3 級以上 7%），最常見是味覺異常與頭痛 | Amgen, 2026 |
| tisagenlecleucel | 77%，其中 48% 用 tocilizumab | 40% | Maude et al., 2018 |
| afamitresgene autoleucel | 75%（3 級以上 2%） | 1 人發生 1 級 ICANS | Barnett et al., 2025 |

- **時間**：tarlatamab 的 CRS 集中在前兩劑（第 1 天與第 8 天之後 2 級以上 CRS 分別是 24% 與 8%，第 15 天之後 1%）（Amgen, 2026）。所以仿單把院內監測集中在前兩劑；ICANS 則可以在數週後才出現，出院衛教要包含神經症狀（見[肺癌章 7.7](../01-lung-cancer.md#77-tarlatamab-病房實務c1d1c1d8-的醫囑監測與出院衛教)）。
- **先排除感染**：CRS 的發燒和敗血症分不開。處置流程見腫瘤急症 9.3。

### 6.3 輸注反應

ICI 的輸注反應不多：pembrolizumab 的嚴重或危及生命的輸注反應是 0.2%（2,799 人），輕到中度時暫停或減慢輸注（Merck Sharp & Dohme, 2026）。例外是 avelumab，前 4 次輸注前要常規給抗組織胺與 acetaminophen，3–4 級輸注反應要永久停用（EMD Serono, 2026）。床邊的辨識與處置流程和其他抗體相同，見[腫瘤急症第 10 節](../00-shared/02-oncologic-emergencies.md#10-輸注反應過敏反應與過敏性休克)。

### 6.4 和化療、放療合併時，症狀是誰造成的

- 化療期間的腹瀉、肝功能異常、疲倦、嗜中性球低下，可能是化療，也可能是 irAE，兩者處置相反。判讀方法以 KEYNOTE-522 為例，見[乳癌章 6.10](../03-breast-cancer.md#610-免疫治療keynote-522和化療毒性分開看)。
- 化放療後接 durvalumab 的病人出現喘與肺部毛玻璃病灶時，放射性肺炎、免疫性肺炎與感染的鑑別見[肺癌章 4.2](../01-lung-cancer.md#42-nsclc-iii-期)與 [6.6](../01-lung-cancer.md#66-免疫治療肺癌要特別注意的點)。

---

## 7. 抗藥性與下一代藥物

**這一段的結論先講：** ICI 失效分兩種：一開始就沒效（原發性抗藥），以及有效一段時間後又惡化（後天性抗藥）（Sharma et al., 2017）。兩種都能對回 2.1 免疫循環的某一步。下一代藥物的思路就是把缺的那一步補上：加化療、加抗血管新生藥、加第二個檢查點，把兩個標的做進同一個抗體，或者直接繞過 MHC。

### 7.1 為什麼失效

| 類型 | 機轉 | 證據 | 臨床上的意義 |
|------|------|------|------------|
| 原發 | 腫瘤裡沒有 T 細胞（「冷」腫瘤） | 腫瘤依 T 細胞浸潤分成熱、中間型與冷，免疫治療的效果取決於原本有沒有免疫反應（Galon & Bruni, 2019）；胰臟癌用 durvalumab ± tremelimumab 的反應率只有 0 到 3.1%（O'Reilly et al., 2019） | 胰臟癌只在 MSI-H／dMMR 考慮 ICI |
| 原發 | 有驅動基因的肺癌 | EGFR 突變者 ICI 對 docetaxel 的整體存活 HR 1.05（Lee et al., 2017） | 標靶藥優先 |
| 原發 | 肺腺癌的 STK11、KEAP1 突變 | KRAS 突變肺腺癌中，合併 STK11 突變者對 PD-1 抑制劑的反應率 7.4%，合併 TP53 突變者 35.7%，只有 KRAS 突變者 28.6%（Skoulidis et al., 2018）。POSEIDON 的分析中，STK11 或 KEAP1 突變者要加上 tremelimumab 才看到好處，只加 durvalumab 沒有（Skoulidis et al., 2024） | 這些是**相關性**與事後分析，目前不是常規的選藥依據，也不是給付條件 |
| 後天 | 抗原呈現壞掉 | 復發的黑色素瘤出現 B2M 截斷突變，MHC class I 上不了細胞表面（Zaretsky et al., 2016） | T 細胞看不到腫瘤，再拆煞車也沒有用；理論上要靠不看 MHC 的治療 |
| 後天 | 腫瘤對 interferon-γ 沒有反應 | 4 位復發的黑色素瘤病人中，2 位出現 JAK1 或 JAK2 的功能喪失突變（Zaretsky et al., 2016） | 同上 |

### 7.2 下一代怎麼解決

**一、合併治療（已經是標準）**

- **加化療**：KEYNOTE-189、KEYNOTE-407、KEYNOTE-522 都是化療 ＋ pembrolizumab（見 5.2）。
- **加抗血管新生藥**：IMpower150 中，atezolizumab ＋ bevacizumab ＋ carboplatin ＋ paclitaxel 對不含 atezolizumab 的三藥組合，無惡化存活 8.3 對 6.8 個月（HR 0.62），整體存活 19.2 對 14.7 個月（HR 0.78）（Socinski et al., 2018）。
- **加第二個檢查點**：CTLA-4（CheckMate 227、POSEIDON，見 3.3）與 LAG-3（見 3.4）。

**二、把 PD-1 和 VEGF 做進同一個抗體：ivonescimab**

| 試驗 | 族群 | 比較 | 結果 |
|------|------|------|------|
| HARMONi-2（Xiong et al., 2025） | 中國；PD-L1 陽性的晚期 NSCLC 第一線，398 人 | ivonescimab 對 pembrolizumab | 無惡化存活 11.1 對 5.8 個月（HR 0.51）；3 級以上治療相關不良事件 29% 對 16% |
| HARMONi-6（Lu et al., 2026） | 中國；晚期鱗狀 NSCLC 第一線，532 人 | ivonescimab ＋ 化療對 tislelizumab ＋ 化療 | 整體存活 27.9 對 23.7 個月（HR 0.66）；3 級以上治療相關不良事件 69% 對 59%，3 級以上出血 3% 對 1% |
| HARMONi-A（Fang et al., 2026） | 中國；EGFR-TKI 治療後惡化的 EGFR 突變非鱗狀 NSCLC，322 人 | ivonescimab ＋ 化療對化療 | 整體存活 16.8 對 14.1 個月（HR 0.74） |
| HARMONi（Le et al., 2026） | 跨國（亞洲人占 70%）；與 HARMONi-A 相同的族群，438 人 | ivonescimab ＋ 化療對化療 | 無惡化存活 6.8 對 4.4 個月（HR 0.52）；整體存活 16.8 對 14.0 個月（HR 0.79，95% CI 0.62–1.01），**未達顯著** |

讀這張表要注意兩件事：四個試驗中三個只在中國收案；唯一的跨國試驗，整體存活沒有達到統計顯著。

> [!CAUTION]
> **待核對：ivonescimab 的美國審查結果**
> Ivonescimab 已在中國核准。美國 FDA 於 2026 年 1 月受理它併用化療治療 EGFR-TKI 後惡化的 EGFR 突變非鱗狀 NSCLC 的申請，目標審查日期是 2026-11-14（Serani, 2026），也就是本章定稿後 3 天；美國 FDA 核准公告頁到 2026-11-10 為止沒有 ivonescimab 的條目（US Food and Drug Administration, 2026）。審查結果、台灣藥證與給付都有時效性，請以最新公告為準。

**三、抗體藥物複合體（ADC）＋ 免疫**

- 泌尿上皮癌第一線的 EV-302：enfortumab vedotin ＋ pembrolizumab 對化療，整體存活 31.5 對 16.1 個月（HR 0.47）（Powles et al., 2024）。
- 三陰性乳癌第一線的 ASCENT-04：sacituzumab govitecan ＋ pembrolizumab 對化療 ＋ pembrolizumab，無惡化存活 11.2 對 7.8 個月（HR 0.65），整體存活資料尚未成熟（Tolaney et al., 2026）。美國於 2026-06-24 核准 sacituzumab govitecan 新的三陰性乳癌適應症（US Food and Drug Administration, 2026）；台灣的狀態見[乳癌章 4.9](../03-breast-cancer.md#49-轉移性三陰性看-pd-l1看前線用藥)。
- ADC 的機轉與毒性見[標靶藥物](03-targeted-therapy.md)。

**四、不靠腫瘤自己的抗原呈現**

T 細胞銜接抗體（tarlatamab）、TIL（lifileucel）與 TCR-T（afamitresgene autoleucel）在 2024 年進入實體腫瘤（見 3.5、3.6）。它們共同的限制是毒性大、製程或監測複雜，而且台灣不一定有藥證。

**五、仍在試驗階段**

個人化 mRNA 新抗原疫苗（黑色素瘤的第 2b 期、胰臟癌的第 1 期，見 3.8）目前都不是標準治療。病人拿著新聞來問時，可以說明「有初步結果、還沒有第 3 期試驗證實」，並由主治醫師評估有沒有適合的臨床試驗。

---

## 8. 專師實務

**這一段的結論先講：** 免疫治療的安全靠三件事：開始前把病人的免疫背景問清楚；每次給藥前用同一套問題把各器官問一遍；讓病人和家屬知道「任何新症狀都要講，而且停藥後也一樣」。

### 8.1 第一次給藥前的檢核

| 項目 | 要確認什麼 | 參考 |
|------|-----------|------|
| 適應症與 biomarker | 病理診斷；PD-L1 的抗體株與算法；MSI／dMMR；NSCLC 的 EGFR 與 ALK 報告已經出來 | 5.1、5.4 |
| 給付 | 事前審查已核准；ECOG、肝腎功能符合條件 | [肺癌章 9.3](../01-lung-cancer.md#93-免疫檢查點抑制劑969)與各癌別章第 9 段 |
| 免疫背景 | 自體免疫疾病、器官或造血幹細胞移植、先前的 irAE | 4.4 |
| 感染與肺 | 結核病史、B 型與 C 型肝炎、間質性肺病、胸部放療史 | [irAE 章第 2 節](../00-shared/04-irae.md#2-開始免疫治療前的基線評估) |
| 目前用藥 | 類固醇的劑量與原因（是否 ≥10 mg/day）、其他免疫抑制劑 | 4.4 |
| 基線檢驗 | 仿單要求基線與治療中定期檢查肝功能、肌酸酐、甲狀腺功能（Merck Sharp & Dohme, 2026）；其他項目依 irAE 章第 2 節與院內流程 | [irAE 章第 2 節](../00-shared/04-irae.md#2-開始免疫治療前的基線評估) |
| 生育 | 懷孕檢測；pembrolizumab 仿單要求避孕到最後一劑後 4 個月（Merck Sharp & Dohme, 2026） | 4.1 |
| 疫苗 | 流感、COVID-19 等不活化疫苗的接種狀態 | [支持性照護 13.2](../00-shared/03-supportive-care.md#132-疫苗) |
| 衛教 | 已說明 irAE、給了警示卡、留了聯絡電話 | 8.3 |

> [!NOTE]
> **基線要抽哪些，以院內流程為準**
> Cortisol、troponin、心電圖、HbA1c 是否列為常規基線，各指引與各醫院不同。實習時先找到院內的免疫治療開始前檢核表，照表執行。

### 8.2 每次給藥前

1. **問症狀**：用 [irAE 章第 8 節](../00-shared/04-irae.md#8-病人衛教重點)的清單，從腸胃、呼吸、皮膚、肝、內分泌、心臟、神經肌肉逐項問，並和上一次比較。
2. **看檢驗**：血球、肝腎功能、電解質、血糖；甲狀腺功能依 irAE 章的時程。
3. **有新症狀或異常，先分級再決定打不打**：分級與處置見 [irAE 章第 3 節](../00-shared/04-irae.md#3-通用分級處置)。ICI 不減量，只有照打、暫停、停用三種決定（見 4.2）。
4. **合併化療時**：化療本身的給藥前檢核照舊；症狀的歸因見 6.4。
5. **間隔拉長的處方**（q4w、q6w）：兩次回診之間要有電話追蹤或明確的聯絡管道。

### 8.3 衛教重點與警示卡

給病人與家屬的五句話：

1. 這個藥是讓你的免疫系統去打腫瘤，免疫系統偶爾也會打到自己的器官。
2. **任何新的不舒服都要告訴我們**，特別是腹瀉、咳嗽或喘、皮疹、極度疲倦、頭痛、胸悶心悸、眼皮下垂或肌肉無力、口渴多尿。完整清單見 [irAE 章第 8 節](../00-shared/04-irae.md#8-病人衛教重點)。
3. **停藥之後幾個月內也一樣**，不要覺得「已經沒打了」就不講。
4. 到急診或看其他科時，第一句話先說「我打過免疫治療」，並拿出警示卡。
5. 不要自己吃止瀉藥把腹瀉壓下來；正在吃類固醇的人不要自己停藥。

**警示卡（wallet card）上要有的內容：** 藥名、開始日期與最後一次給藥日期、主治醫師與聯絡電話，以及一句給其他醫療人員看的話：「此病人接受過免疫檢查點抑制劑，可能發生免疫相關不良反應，請聯絡腫瘤科。」接受 tarlatamab 的病人另有 CRS 與神經毒性的警示內容，見[肺癌章 7.7](../01-lung-cancer.md#77-tarlatamab-病房實務c1d1c1d8-的醫囑監測與出院衛教)。

> [!NOTE]
> **警示卡的格式依院內規範**
> 各院不一定有制式的免疫治療警示卡。沒有的話，至少把上面幾項寫在病人的用藥紀錄卡或手機備忘錄裡，並教家屬怎麼出示。

### 8.4 類固醇管理

- **開始前**：把沒有必要的類固醇減到 prednisone <10 mg/day（Arbour et al., 2018）。必要的不要硬停，劑量與原因寫進病歷。
- **發生 irAE 時**：該用就用足量，不要因為擔心療效而減量或延後（Horvat et al., 2015）。
- **減量**：至少 4 到 6 週慢慢減（Schneider et al., 2021）；長期使用的配套（肺囊蟲肺炎預防、腸胃道保護、B 肝、血糖）見 [irAE 章第 4 節](../00-shared/04-irae.md#4-長期類固醇的配套措施)。
- **恢復 ICI 的時機**與第二線免疫抑制劑見 [irAE 章第 3 節](../00-shared/04-irae.md#3-通用分級處置)與[第 6 節](../00-shared/04-irae.md#6-第二線免疫抑制劑)。

### 8.5 重新給藥（rechallenge）

irAE 緩解後能不能再用 ICI，取決於是哪一個器官、當時幾級、病人還有沒有別的治療選擇。原則、復發率與不建議再用的情況整理在 [irAE 章第 7 節](../00-shared/04-irae.md#7-重新給藥rechallenge)，由主治醫師與病人討論後決定；重新給藥後的追蹤要比原本更密。

### 8.6 T 細胞銜接抗體與細胞治療

- 給藥前確認院內有 tocilizumab，並知道 CRS 與 ICANS 的分級表放在哪裡（[腫瘤急症第 9 節](../00-shared/02-oncologic-emergencies.md#9-細胞激素釋放症候群crs與神經毒性icans)）。
- Tarlatamab 的前置用藥、輸注後監測時數與出院條件見[肺癌章 7.7](../01-lung-cancer.md#77-tarlatamab-病房實務c1d1c1d8-的醫囑監測與出院衛教)。
- 檢視併用藥：CRS 期間與之後 14 天內，CYP 受質藥物的濃度可能上升（Amgen, 2026）。

### 8.7 監測時程

| 時間 | 做什麼 |
|------|--------|
| 開始前 | 8.1 的檢核表 |
| 每次給藥前 | 症狀逐項詢問、血球、肝腎功能、電解質、血糖 |
| 約每 4 到 6 週 | 甲狀腺功能（依 [irAE 章第 2 節](../00-shared/04-irae.md#2-開始免疫治療前的基線評估)） |
| 每 12 週 | 影像評估；健保續用以 i-RECIST 判定（見[肺癌章 9.3](../01-lung-cancer.md#93-免疫檢查點抑制劑969)） |
| 停藥後 | 回診時仍要問 irAE 症狀；個案報告中最晚在停藥後 28 個月發生（Couey et al., 2019） |

---

## 9. 藥物卡

<!-- drug-cards -->
| 藥名 | 分類 | 機轉 | 主要用途 | 必記毒性 | 監測與處置 |
|------|------|------|----------|----------|------------|
| nivolumab (Opdivo) | PD-1 抑制劑 | 結合 T 細胞上的 PD-1，放開作用階段的煞車 | NSCLC 二線與術前、黑色素瘤；常與 ipilimumab 合併 | irAE；3–4 級單用 16.3%，合併 ipilimumab 55% | 240 mg q2w 或 480 mg q4w；不減量，只暫停或停用 |
| pembrolizumab (Keytruda) | PD-1 抑制劑 | 結合 PD-1，擋住它與 PD-L1、PD-L2 結合 | NSCLC、三陰性乳癌、MSI-H／dMMR 實體腫瘤 | irAE：甲狀腺低下 8%、肺炎 3.4%、大腸炎 1.7% | 200 mg q3w 或 400 mg q6w；定期驗肝功能、肌酸酐、甲狀腺 |
| cemiplimab (Libtayo) | PD-1 抑制劑 | 結合 PD-1，擋住它與 PD-L1、PD-L2 結合 | 皮膚鱗狀細胞癌；PD-L1 ≥50% 的 NSCLC 第一線單用 | irAE | 每次給藥前逐項問症狀；處置見 irAE 章 |
| tislelizumab | PD-1 抑制劑 | 結合 T 細胞上的 PD-1 | 食道鱗狀細胞癌；健保 9.69 列有肺癌給付 | irAE | 給付條件與指定抗體株見肺癌章 9.3 |
| dostarlimab (Jemperli) | PD-1 抑制劑 | 結合 T 細胞上的 PD-1 | dMMR 子宮內膜癌；dMMR 局部晚期直腸癌 | irAE | 開藥前確認 dMMR 或 MSI-H 報告 |
| toripalimab | PD-1 抑制劑 | 結合 T 細胞上的 PD-1 | 鼻咽癌第一線，併 gemcitabine ＋ cisplatin | irAE | 同類別：每次給藥前逐項問症狀 |
| atezolizumab (Tecentriq) | PD-L1 抑制劑 | 結合 PD-L1，擋住它與 PD-1、CD80 結合 | 擴散期 SCLC、NSCLC、肺泡狀軟組織肉瘤 | irAE | 靜脈 1,200 mg q3w；皮下 1,875 mg，兩者不可互換 |
| durvalumab (Imfinzi) | PD-L1 抑制劑 | 結合 PD-L1，擋住它與 PD-1、CD80 結合 | 化放療後鞏固（III 期 NSCLC、局限期 SCLC）；擴散期 SCLC | irAE；化放療後的肺炎要和放射性肺炎鑑別 | 新的咳嗽或喘先排除肺炎，見肺癌章 4.2 |
| avelumab (Bavencio) | PD-L1 抑制劑 | 結合腫瘤與免疫細胞上的 PD-L1 | Merkel 細胞癌；泌尿上皮癌化療後維持 | irAE、輸注反應 | 前 4 次輸注前給抗組織胺與 acetaminophen；800 mg q2w |
| ipilimumab (Yervoy) | CTLA-4 抑制劑 | 放開 T 細胞活化早期的煞車 | 黑色素瘤；與 nivolumab 合併用於 NSCLC | irAE 多而重；致死個案七成是大腸炎 | 腹瀉當天回報；懷疑腦下垂體炎先補糖皮質素 |
| tremelimumab (Imjudo) | CTLA-4 抑制劑 | 放開 T 細胞活化早期的煞車 | 肝細胞癌（單劑 300 mg ＋ durvalumab）；NSCLC 併化療 | irAE | 健保 9.69 無肺癌用法，見肺癌章 9.3 |
| relatlimab | LAG-3 抑制劑 | 擋住第三個檢查點 LAG-3，與 nivolumab 做成合併製劑 | 無法切除或轉移性黑色素瘤 | irAE；3–4 級 18.9%，nivolumab 單用 9.7% | 每 4 週給藥；監測同其他 ICI |
| tarlatamab (Imdelltra) | 雙特異性 T 細胞銜接抗體 | 一端抓腫瘤的 DLL3，一端抓 T 細胞的 CD3 | 含鉑化療後惡化的擴散期 SCLC | CRS 57%、神經毒性（含 ICANS） | 先 1 mg 再升 10 mg；前兩劑院內監測 6–8 小時 |
| blinatumomab (Blincyto) | 雙特異性 T 細胞銜接抗體 | 一端抓 B 細胞的 CD19，一端抓 T 細胞的 CD3 | 復發或難治 B 細胞急性淋巴性白血病 | CRS、神經毒性 | 半衰期約 2 小時，連續靜脈輸注；階梯式劑量 |
| tisagenlecleucel (Kymriah) | CAR-T 細胞治療 | 自體 T 細胞裝上認 CD19 的人工受體 | 25 歲以下復發或難治 B 細胞急性淋巴性白血病 | CRS 77%、神經事件 40% | 院內備 tocilizumab；依 ASTCT 分級處置 |
| afamitresgene autoleucel (Tecelra) | TCR-T 細胞治療 | 自體 T 細胞轉入認 MAGE-A4 的 T 細胞受體 | 化療後的滑膜肉瘤 | CRS 75%；長時間嚴重血球低下 | 先驗 HLA-A*02 與 MAGE-A4；台灣無藥證 |
| lifileucel (Amtagvi) | TIL 細胞治療 | 取腫瘤內的 T 細胞擴增後輸回，再給 IL-2 | PD-1 抑制劑治療過的黑色素瘤 | 3 級不良事件 95.5%；有治療相關死亡 | 監測血球低下、感染、心肺與腎功能 |
| aldesleukin (IL-2) | 細胞激素 | 刺激 T 細胞增殖 | 轉移性腎細胞癌與黑色素瘤；TIL 輸注後使用 | 嚴重體液滯留；2% 死於不良事件 | 反應率約 16%，少數完全反應可長期持續 |

---

<!-- END-PART -->
