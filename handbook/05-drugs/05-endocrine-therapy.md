# 荷爾蒙治療藥物（Endocrine Therapy）

| 項目 | 本章依據 |
|------|---------|
| 發現史 | 原始論文與史料回顧：Cole et al., 1971；Harper & Walpole, 1967；Jordan, 2006；Quirke, 2017；Santen et al., 2009；Denmeade & Isaacs, 2002 |
| 治療指引 | ASCO 輔助內分泌治療指引（Burstein et al., 2010；Burstein et al., 2014；Burstein et al., 2016；Burstein et al., 2019）、CPIC 的 CYP2D6 與 tamoxifen 指引（Goetz et al., 2018）、ASCO 骨質疏鬆指引（Shapiro et al., 2019）、ASCO 男性乳癌指引（Hassett et al., 2020）。NCCN 與 ESMO 的建議見[乳癌章](../03-breast-cancer.md) |
| 藥品仿單 | 美國仿單（DailyMed，2026-11-11 讀取）。本章的劑量都註明出處；台灣藥證與給付請見各癌別章第 9 段 |
| 健保給付 | 本章不重述條文，乳癌內分泌藥物見[乳癌章 9.2](../03-breast-cancer.md#92-hr-陽性內分泌治療cdk46-抑制劑與-pi3kaktmtorhdac-抑制劑) |
| 最後更新 | 2026-11-11 |

**這一章的結論先講：** 荷爾蒙治療只做兩件事：**把荷爾蒙抽掉**，或**把受體堵住、拆掉**。選藥的第一個問題不是「哪個藥比較強」，而是「**雌激素從哪裡來**」：停經前來自卵巢，停經後來自周邊組織的 aromatase。停經狀態判斷錯，藥就選錯。

> 本手冊是學習用整理，不能取代原始指引、仿單、健保公告與院內規範。實際處方以主治醫師判斷與院內流程為準。

---

## 0. 速查卡

| 類別 | 代表藥 | 一句話機轉 | 誰可以用 | 必記毒性 |
|------|--------|-----------|---------|---------|
| 選擇性雌激素受體調節劑（selective estrogen receptor modulator, SERM） | tamoxifen、toremifene；raloxifene 只用於預防 | 佔住雌激素受體（estrogen receptor, ER）：在乳房是拮抗劑，在子宮內膜與骨是部分促效劑 | 停經前、停經後、男性 | 熱潮紅、靜脈血栓（VTE）、子宮內膜癌 |
| 芳香環轉化酶抑制劑（aromatase inhibitor, AI） | letrozole、anastrozole（非類固醇）；exemestane（類固醇） | 關掉周邊組織把雄性素轉成雌激素的 aromatase | **只有停經後**；停經前一定要加卵巢功能抑制 | 關節痛、骨質流失與骨折、血脂上升 |
| 卵巢功能抑制（ovarian function suppression, OFS）與卵巢去除 | goserelin、leuprolide、triptorelin；雙側卵巢切除 | GnRH agonist 持續刺激腦下垂體，受體 downregulation 之後卵巢停工 | 停經前 | 提早停經的症狀、骨質流失；第一劑後短暫 flare |
| 選擇性雌激素受體降解劑（selective estrogen receptor degrader, SERD） | fulvestrant（肌肉注射）；口服 elacestrant、imlunestrant、camizestrant | 拮抗 ER，並讓 ER 被降解 | 轉移性；口服 SERD 的美國適應症都綁 ESR1 突變 | fulvestrant：注射部位疼痛；口服藥各有不同（血脂、心搏過緩、QTc） |
| PROTAC 降解劑 | vepdegestrant | 一端抓 ER、一端抓 E3 ligase，把 ER 送進 proteasome | 轉移性、ESR1 突變 | QTc 延長 |
| 黃體素（progestin） | megestrol | 抗腫瘤機轉不明；現在多用來促進食慾 | 後線緩和治療、惡病質 | 血栓、腎上腺抑制、高血糖 |
| 攝護腺癌的雄性素路徑藥 | LHRH agonist 與 antagonist、bicalutamide、abiraterone、enzalutamide | 去勢，或阻斷雄性素受體 | 不在本手冊四個癌別內，見 [3.6](#36-攝護腺癌的雄性素路徑藥對照用不在本手冊四個癌別內) | 熱潮紅、骨質流失、代謝與心血管 |

（各格的出處與數字見第 2–6 段。）

**開處方前照順序問三個問題：**

1. **停經了嗎？** 決定用 tamoxifen 還是 AI、要不要加 OFS（[5.1](#51-開藥前先確定兩件事er-與停經狀態)）。
2. **早期還是轉移性？復發風險多高？** 決定吃 5 年還是延長、要不要加 OFS 或 CDK4/6 抑制劑（[5.2](#52-早期乳癌)）。
3. **轉移性惡化之後，biomarker 是什麼？** ESR1、PIK3CA／AKT1／PTEN、germline BRCA 各有對應的藥（[5.3](#53-轉移性-hrher2)）。

> [!IMPORTANT]
> **必背數字**
> - Tamoxifen 5 年：ER 陽性乳癌的復發率在第 0–4 年降到一半左右（RR 0.53），乳癌死亡率在前 15 年降低約三分之一；ER 陰性無效（Early Breast Cancer Trialists' Collaborative Group, 2011；以下簡稱 EBCTCG）。
> - AI 對 tamoxifen（停經後，各 5 年）：10 年乳癌死亡 12.1% 對 14.2%；代價是 5 年骨折 8.2% 對 5.5%，但子宮內膜癌 0.4% 對 1.2%（Early Breast Cancer Trialists' Collaborative Group, 2015）。
> - Tamoxifen 10 年對 5 年（ATLAS）：第 5–14 年乳癌死亡 12.2% 對 15.0%；子宮內膜癌累積風險 3.1% 對 1.6%（Davies et al., 2013）。
> - Fulvestrant 500 mg 肌肉注射：第 1、15、29 天，之後每月一次（美國仿單；AstraZeneca, 2020）。
> - Tamoxifen 是 prodrug，靠 CYP2D6 變成 endoxifen；強效 CYP2D6 抑制劑有 paroxetine、fluoxetine、bupropion（Goetz et al., 2018；US Food and Drug Administration, 2026）。
> - ESR1 突變在原發腫瘤只有 1.8%，轉移性腫瘤 16.3%，是治療壓力下「後天」出現的（Hanker et al., 2020）。

> [!WARNING]
> **三個最常出事的錯**
> - **停經前病人單用 AI。** 卵巢還在運轉時 AI 無效，ASCO 指引寫明 AI 禁用於仍有卵巢功能的病人（Burstein et al., 2010）。
> - **把「化療後沒有月經」當成停經。** 45 位化療後無月經而開始 AI 的女性，27% 的卵巢功能恢復，其中 1 位懷孕（Smith et al., 2006）。
> - **把 tamoxifen 當成避孕藥，或忽略異常陰道出血。** Tamoxifen 可造成胎兒傷害，仿單要求使用屏障或非荷爾蒙避孕，異常陰道出血要立刻回報（Bryant Ranch Prepack, 2026）。

---

## 1. 怎麼被發現的

**結論：** 荷爾蒙治療是最早的「標靶治療」。順序是反過來的：先有臨床觀察（切掉卵巢，腫瘤縮小），幾十年後才找到標靶（ER），最後才有藥。每一步都留下一個我們今天還在做的臨床動作。

| 年份 | 事件 | 意義 |
|------|------|------|
| 1896 | 格拉斯哥外科醫師 Beatson 在愛丁堡報告：晚期乳癌病人切除卵巢後腫瘤明顯縮小（原文刊於 Transactions of the Medico-Chirurgical Society of Edinburgh 第 15 卷 153–179 頁，PMID 29584099）；1900 年 Boyd 彙整英國病例，只有約三分之一有反應，維持約一年 | 第一次證明乳癌受荷爾蒙控制，也留下「為什麼只有三分之一有效」的問題（Jordan, 2006） |
| 1941 | Huggins 與 Hodges：轉移性攝護腺癌以去勢或雌激素治療，並用血清 acid phosphatase 追蹤反應 | 第一個全身性的癌症荷爾蒙治療；Huggins 在 1966 年獲諾貝爾生理醫學獎（Huggins & Hodges, 1972；Denmeade & Isaacs, 2002） |
| 1958 | Lerner 等發現第一個非類固醇抗雌激素 MER-25，因毒性大、效力低而停止開發 | 「抗雌激素」這個藥理概念成立（Jordan, 2006） |
| 1962 | Jensen 與 Jacobson 證明放射標記的 estradiol 會被目標組織留住；同年 ICI 藥廠的化學家 Dora Richardson 合成 ICI 46,474 | ER 的概念誕生；tamoxifen 的分子出現（Jordan, 2006；Quirke, 2017） |
| 1967 | Harper 與 Walpole 發表 ICI 46,474 在大鼠抑制著床的作用 | 它原本是避孕藥計畫的產物（Harper & Walpole, 1967） |
| 1971 | Cole 等的第一個乳癌臨床試驗：46 位晚期乳癌病人，10 位反應良好，副作用少 | tamoxifen 轉向乳癌（Cole et al., 1971） |
| 1971 | Jensen 等報告腫瘤的 ER 與腎上腺切除等內分泌治療的反應有關 | ER 成為第一個預測療效的 biomarker（Jensen et al., 1971；Jensen & Jordan, 2003） |
| 1971 | Schally 團隊從豬下視丘分離出 LHRH（即 GnRH），定出十胜肽結構並合成 | GnRH 類似物的起點；Schally 與 Guillemin 在 1977 年獲諾貝爾獎（Schally et al., 1971；Nobel Prize Outreach, 2026） |
| 1973 | 英國核發 Nolvadex（tamoxifen）許可，適應症是不排卵性不孕與晚期乳癌的緩和治療 | 第一個上市的 ER 標靶藥（Quirke, 2017） |
| 1977 | Brodie 等：選擇性 aromatase 抑制劑 4-hydroxyandrostenedione 讓大鼠的雌激素依賴性乳腺腫瘤 80% 明顯縮小 | 「只關掉 aromatase」可行（Brodie et al., 1977） |
| 1982–1984 | LHRH agonist 用於攝護腺癌：10 位病人的初步報告，之後 leuprolide 與 diethylstilbestrol（DES）的隨機試驗 | 藥物去勢開始取代手術與雌激素（Tolis et al., 1982；Leuprolide Study Group, 1984） |
| 1984 | Coombes 等：4-hydroxyandrostenedione 單次肌肉注射治療 11 位停經後轉移性乳癌，4 位有反應 | 選擇性 AI 的臨床概念驗證（Coombes et al., 1984） |
| 1991 | Wakeling 等發表純抗雌激素 ICI 182,780，即後來的 fulvestrant | 第一個 SERD（Wakeling et al., 1991） |
| 1998 | EBCTCG 整合 55 項試驗、約 37,000 人；同年 NSABP P-1 顯示 tamoxifen 讓高風險女性的侵襲性乳癌減少 49% | 輔助 tamoxifen 約 5 年成為標準；第一個癌症化學預防藥（Early Breast Cancer Trialists' Collaborative Group, 1998；Fisher et al., 1998） |
| 2002–2005 | ATAC 與 BIG 1-98：anastrozole、letrozole 在停經後輔助治療勝過 tamoxifen | AI 成為停經後的首選（Baum et al., 2002；Breast International Group 1-98 Collaborative Group, 2005） |
| 2003 | MA.17：tamoxifen 吃滿 5 年後接 letrozole，4 年無病存活 93% 對 87% | 延長輔助治療的開始（Goss et al., 2003） |
| 2013 | ATLAS：tamoxifen 10 年優於 5 年；同年在轉移性腫瘤找到 ESR1 ligand-binding domain 突變 | 「吃多久」與「為什麼失效」同時有新答案（Davies et al., 2013；Toy et al., 2013） |
| 2014–2015 | SOFT 與 TEXT：停經前高風險者加 OFS，exemestane 加 OFS 再降低復發 | 停經前治療開始依風險分層（Pagani et al., 2014；Francis et al., 2015） |
| 2023 | 美國 FDA 核准第一個口服 SERD elacestrant，限 ESR1 突變 | 內分泌治療進入 biomarker 導向（US Food and Drug Administration, 2023） |
| 2025–2026 | imlunestrant、vepdegestrant、camizestrant 取得美國適應症（camizestrant 為加速核准） | 口服 SERD 與 PROTAC 降解劑進入臨床（Eli Lilly and Company, 2026；Arvinas Operations, 2026；AstraZeneca, 2026） |

### 1.1 Beatson 的卵巢切除：為什麼停經狀態決定一切

Beatson 在 1896 年報告一位晚期乳癌病人切除卵巢後戲劇性地好轉。這是第一次有人用「拿掉荷爾蒙」治療癌症。但之後彙整的病例顯示只有約三分之一的病人有反應，而且大約一年後就失效（Jordan, 2006）。

**和今天的連結：** 停經前病人的卵巢仍是雌激素的主要來源，所以高風險的停經前病人到今天還在做同一件事，只是把手術刀換成每月一針的 GnRH agonist（見 [3.3](#33-卵巢功能抑制與卵巢去除)）。「為什麼只有三分之一有效」要等到 ER 被發現才有答案。

### 1.2 Huggins：攝護腺癌證明了同一個道理

1941 年，Huggins 與 Hodges 讓轉移性攝護腺癌病人接受去勢或雌激素治療，並用血清 acid phosphatase 追蹤反應（Huggins & Hodges, 1972，重刊 1941 年原文）。Huggins 因此在 1966 年得到諾貝爾獎。後來的美國退伍軍人醫院試驗發現，口服 DES 的效果與睪丸切除相當，但心血管與血栓栓塞毒性明顯（Denmeade & Isaacs, 2002）。這個毒性讓大家開始找更安全的藥物去勢方法，也就是後來的 LHRH agonist（見 1.6）。

**和今天的連結：** 乳癌與攝護腺癌的荷爾蒙治療用的是同一套邏輯（抽掉荷爾蒙，或擋住受體），所以毒性也像：熱潮紅、骨質流失、代謝與心血管問題。攝護腺癌的藥整理在 [3.6](#36-攝護腺癌的雄性素路徑藥對照用不在本手冊四個癌別內)。

### 1.3 Jensen 與雌激素受體：第一個預測性 biomarker

Jensen 在 1960 年代初證明，放射標記的 estradiol 會被子宮等目標組織留住，推論一定有一個受體在接它。1971 年他的團隊把這件事變成檢驗：腫瘤有 ER，內分泌治療才可能有效；沒有 ER，幾乎不會有反應（Jensen et al., 1971；Jordan, 2006）。Beatson 的三分之一之謎就此解開。Jensen 與 Jordan 的回顧把 ER 稱為分子醫學的範本：先找到標靶，再用檢驗預測誰會對藥有反應（Jensen & Jordan, 2003）。

**和今天的連結：** 每一個乳癌檢體都要驗 ER。ASCO／CAP 的切點是腫瘤細胞核染色 ≥1% 即為 ER 陽性；1–10% 另外報告為 ER low positive，因為這一群用內分泌治療的效益資料有限（Allison et al., 2020）。EBCTCG 的資料證實 ER 是唯一能預測 tamoxifen 效益的因子，ER 陰性者用了沒有幫助（EBCTCG, 2011）。判讀細節見[乳癌章 2.2](../03-breast-cancer.md#22-erpr-與免疫組織化學亞型)。

### 1.4 Tamoxifen：一個失敗的避孕藥

1962 年，ICI 藥廠的化學家 Dora Richardson 在避孕藥計畫中合成了 ICI 46,474。計畫主持人是生物學家 Arthur Walpole，內分泌學家 Mike Harper 負責動物試驗（Quirke, 2017）。在大鼠，它是很有效的事後避孕藥（Harper & Walpole, 1967）。但用在女性時結果相反：它**誘發排卵**，不能避孕。加上在美國拿不到專利，ICI 董事會一度決定終止計畫，Walpole 以辭職相逼才保住它，並把它轉向乳癌（Quirke, 2017）。

- **第一個臨床試驗**：曼徹斯特 Christie 醫院，46 位晚期乳癌病人，10 位反應良好；療效與當時使用的雌激素、雄性素相當，但副作用少得多（Cole et al., 1971）。
- **實驗室的轉折**：V. Craig Jordan 1974 年起在里茲大學證明 tamoxifen 會擋住 estradiol 與 ER 的結合，並能預防致癌物誘發的大鼠乳腺腫瘤；他在動物身上發現，腫瘤負荷小的時候長期給藥效果最好，這成為「長期輔助治療」的依據（Jordan, 2006）。
- **整合分析定案**：EBCTCG 1998 年的整合分析顯示，tamoxifen 用 1 年、2 年、約 5 年，復發分別減少 21%、29%、47%，死亡減少 12%、17%、26%，用得越久越好；ER 很低或沒有的腫瘤效果很小（EBCTCG, 1998）。2011 年的更新確認 5 年 tamoxifen 讓 ER 陽性病人的乳癌死亡率在之後 15 年都降低約三分之一（EBCTCG, 2011）。
- **預防**：NSABP P-1 於 1992 年開始，13,388 位高風險女性，tamoxifen 讓侵襲性乳癌減少 49%（Fisher et al., 1998）；美國 FDA 於 1998 年核准它用於降低乳癌風險（Jordan, 2006）。

**和今天的連結：**

1. **Tamoxifen 不是避孕藥，還可能誘發排卵。** 停經前病人即使月經不規則也可能懷孕，所以一定要談避孕（見 [6.8](#68-生育避孕與懷孕)）。
2. **吃得夠久才有效。** 從 1 年、2 年、5 年到 10 年，每一次延長都有試驗支持，所以服藥遵從性是療效的一部分（見 [6.10](#610-遵從性最大的毒性是沒有吃)）。
3. **先驗 ER 再開藥。** 這是所有「先驗 biomarker、再開標靶藥」的原型。

### 1.5 Aromatase 抑制劑：從非選擇性到第三代

第一個被當成 AI 使用的藥是 aminoglutethimide。它原本的目的是阻斷腎上腺功能來治療乳癌，後來才意外發現它是強力但**非選擇性**的 aromatase 抑制劑（Santen et al., 2009）。Angela Brodie 與 Harry Brodie 走另一條路：用類固醇受質的類似物專門抑制 aromatase。他們的 4-hydroxyandrostenedione（formestane）在大鼠讓血中 estradiol 降低 80%，並讓雌激素依賴性乳腺腫瘤縮小（Brodie et al., 1977）；1984 年 Coombes 與 Brodie 合作，把它用在 11 位停經後轉移性乳癌病人，4 位有反應（Coombes et al., 1984）。這兩個藥證明了概念，之後才有更強、更專一的第三代 AI：anastrozole、letrozole、exemestane（Santen et al., 2009），美國分別於 1995、1997、1999 年核准（ANI Pharmaceuticals, 2026；Novartis Pharmaceuticals Corporation, 2024；Pharmacia & Upjohn, 2025）。

兩個大型輔助試驗確立了 AI 的地位：

- **ATAC**（9,366 人）：anastrozole 對 tamoxifen 的 3 年無病存活 89.4% 對 87.4%（HR 0.83，95% CI 0.71–0.96）；**兩藥合併並不比 tamoxifen 單用好**（HR 1.02）（Baum et al., 2002）。
- **BIG 1-98**（8,010 人）：letrozole 對 tamoxifen 的 5 年無病存活 84.0% 對 81.4%（HR 0.81，0.70–0.93），遠端復發 HR 0.73（Breast International Group 1-98 Collaborative Group, 2005）。

**和今天的連結：** 第三代 AI 只關 aromatase，anastrozole 仿單寫明它不影響 cortisol 與 aldosterone，不需要補充類固醇（ANI Pharmaceuticals, 2026）。ATAC 的合併組沒有比較好，所以仿單寫「tamoxifen 不可與 anastrozole 併用」，我們只會「先後」使用，不會「同時」使用。

### 1.6 GnRH：先升後降的十胜肽

1971 年，Schally 團隊定出 LHRH 的結構：一個十胜肽，同時調控黃體成長激素（LH）與濾泡刺激素（FSH）的分泌（Schally et al., 1971）。接下來的發現很反直覺：**持續**給 LHRH agonist，一開始 LH 與性荷爾蒙短暫上升，之後腦下垂體的受體 downregulation，性荷爾蒙反而掉到去勢的程度（Denmeade & Isaacs, 2002）。

- 攝護腺癌：Schally 與臨床團隊在 10 位病人身上看到腫瘤縮小與骨痛緩解（Tolis et al., 1982）；隨後的隨機試驗顯示 leuprolide 的客觀反應率與 DES 相當（86% 對 85%），副作用較少（Leuprolide Study Group, 1984）。
- 乳癌：停經前轉移性乳癌的四項隨機試驗整合分析顯示，LHRH agonist 加 tamoxifen 優於 LHRH agonist 單用（整體存活 HR 0.78，無惡化存活 HR 0.70）（Klijn et al., 2001）；之後 SOFT 與 TEXT 把 OFS 帶進早期乳癌（見 [5.2](#52-早期乳癌)）。

**和今天的連結：** 「先升後降」就是 flare。Goserelin 仿單記載，開始治療後 estradiol 要大約 3 週才降到停經後範圍，最初幾週腫瘤症狀與骨痛可能暫時加重（TerSera, 2026）。所以第一劑之後的頭幾週不能假設卵巢已經被壓住（見 [4.4](#44-gnrh-agonistflare-與確認卵巢真的被壓住)）。

### 1.7 Fulvestrant、口服 SERD，以及攝護腺癌的新藥

Tamoxifen 在某些組織有雌激素作用。ICI 的化學家想要一個「純」的抗雌激素：ICI 182,780 對 ER 的親和力接近 estradiol，沒有促效作用，在乳癌細胞株抑制生長的效果比 tamoxifen 的活性代謝物更完全（Wakeling et al., 1991）。它還會讓 ER 蛋白減少，所以被稱為第一個 SERD（Osborne et al., 2004）。Fulvestrant 於 2002 年在美國核准，當時劑量是每月 250 mg；CONFIRM 試驗證明 500 mg 加上負荷劑量的無惡化存活更好（HR 0.80，0.68–0.94），才改成今天的給法（Di Leo et al., 2010；AstraZeneca, 2020）。

Fulvestrant 只能肌肉注射，藥廠因此開發口服 SERD。第一個成功的是 elacestrant，美國 FDA 在 2023 年 1 月 27 日核准，適應症限 ESR1 突變（US Food and Drug Administration, 2023）；之後的 imlunestrant、camizestrant 與 PROTAC 降解劑 vepdegestrant 見 [7.3](#73-下一代藥物證據與限制)。

攝護腺癌走的是平行的路：去勢後腫瘤仍靠腎上腺與腫瘤自己製造的雄性素生長。Abiraterone 抑制雄性素合成，enzalutamide 更徹底地阻斷雄性素受體，兩者都在去勢抗性攝護腺癌延長存活（de Bono et al., 2011；Scher et al., 2012）。

> [!IMPORTANT]
> **歷史留下來的五個臨床動作**
> - 開藥前驗 ER（Jensen）。
> - 先問停經狀態，停經前高風險者壓卵巢（Beatson、Schally）。
> - Tamoxifen 要談避孕，因為它原本是失敗的避孕藥，會誘發排卵（Walpole）。
> - Tamoxifen 與 AI 不同時使用（ATAC）。
> - 內分泌治療以年為單位，遵從性就是療效（EBCTCG）。

---

## 2. 作用機轉

**結論：** ER 陽性乳癌的油門是「雌激素加上 ER」。四類藥在四個位置下手：卵巢（OFS）、周邊的 aromatase（AI）、受體的口袋（SERM）、受體本身（SERD 與 PROTAC）。先知道雌激素從哪裡來，才知道該在哪裡下手。

### 2.1 雌激素從哪裡來：停經前後完全不同

| 項目 | 停經前 | 停經後（以及男性） |
|------|--------|------------------|
| 主要來源 | **卵巢**；estradiol 是循環全身的荷爾蒙 | **性腺以外的組織**：脂肪（包含乳房）的間質細胞、骨、血管、腦；雌激素在當地製造、當地作用 |
| 原料與酵素 | 卵巢內的 aromatase，受 FSH 調控 | 腎上腺來的雄性素（androstenedione、testosterone）被周邊的 aromatase 轉成 estrone 與 estradiol |
| 腫瘤內的濃度 | 來自循環 | 乳癌組織內的雌激素可比血中高一個數量級以上，因為乳房自己會製造 |
| AI 單用 | **無效** | 有效 |
| 該用的藥 | tamoxifen；高風險者 OFS 加 tamoxifen 或 AI | AI；或 tamoxifen |

（出處：Simpson, 2003；Novartis Pharmaceuticals Corporation, 2024。）

為什麼停經前單用 AI 無效？Anastrozole 仿單寫得很直接：在停經前女性，腎上腺雄性素的周邊轉化不是 estradiol 的重要來源，所以不預期它能降低 estradiol（ANI Pharmaceuticals, 2026）。EBCTCG 也指出 AI 在沒有卵巢抑制的停經前女性無效（Early Breast Cancer Trialists' Collaborative Group, 2022）。更麻煩的是，AI 可能促使化療後暫時停擺的卵巢恢復功能（Smith et al., 2006）。

> [!TIP]
> **大工廠與家庭代工**
> 把雌激素想成一種產品。停經前，卵巢是日夜運轉的大工廠，周邊脂肪只是幾家家庭代工。停經後大工廠關門，產品全靠家庭代工。AI 只會查封家庭代工：大工廠關門以後它很有用；大工廠還在的時候，查封幾家代工根本不影響產量。所以停經前要先讓大工廠停工（OFS 或卵巢切除），AI 才派得上用場。

### 2.2 ER 訊號：受體怎麼讓細胞分裂

雌激素結合 ER 之後，受體兩兩配對進入細胞核，召集輔助活化因子（coactivator），啟動目標基因的轉錄，其中包括 MYC 與 cyclin D1（CCND1），推動細胞週期前進（Hanker et al., 2020）。兩個細節決定了後面所有的藥：

- **受體的形狀決定開或關。** ER 的 ligand-binding domain 有一段稱為 helix 12 的結構。促效劑結合時，受體表面露出一道溝槽讓 coactivator 接上；tamoxifen 的活性代謝物 4-hydroxytamoxifen 結合時，helix 12 改蓋在這道溝槽上，coactivator 接不上去（Shiau et al., 1998）。
- **ER 不只聽雌激素的。** 生長因子路徑（PI3K／mTOR、RAS／RAF／MEK／ERK）可以把 ER 磷酸化，在沒有雌激素的情況下重新啟動它（Hanker et al., 2020）。這是抗藥性的伏筆（見[第 7 段](#7-抗藥性與下一代藥物)），也是內分泌治療要和 CDK4/6、PI3K、AKT 抑制劑合用的原因（見[標靶藥物](03-targeted-therapy.md)）。

### 2.3 四個下手的位置

| 位置 | 藥 | 做了什麼 | 血中雌激素 | ER 蛋白 |
|------|-----|---------|-----------|--------|
| 卵巢（源頭） | GnRH agonist、卵巢切除 | 讓卵巢停止製造雌激素；goserelin 約 3 週把 estradiol 壓到停經後範圍 | 降到停經後程度 | 不變 |
| 周邊 aromatase | AI | anastrozole 1 mg 在 14 天後讓 estradiol 降約 80%；letrozole 讓雌激素降 75–95%；exemestane 讓全身 aromatization 降 98% | 停經後再降到極低 | 不變 |
| 受體的口袋 | SERM | 與雌激素競爭 ER，讓受體擺成「關」的形狀 | 不降 | 不變 |
| 受體本身 | SERD、PROTAC | 拮抗 ER，並使 ER 蛋白減少 | 不降 | 減少 |

（出處：TerSera, 2026；ANI Pharmaceuticals, 2026；Novartis Pharmaceuticals Corporation, 2024；Pharmacia & Upjohn, 2025；Shiau et al., 1998；AstraZeneca, 2020。）

> [!TIP]
> **鑰匙、假鑰匙與拆鎖**
> 雌激素是鑰匙，ER 是鎖，門後是細胞分裂。OFS 與 AI 把鑰匙收走；tamoxifen 是一把插得進去卻轉不動的假鑰匙，佔著鎖孔讓真鑰匙進不來；SERD 與 PROTAC 乾脆把鎖拆掉。這個比喻也預告了抗藥性：如果鎖自己壞在「開」的位置（ESR1 突變），收走鑰匙就沒有用，只能拆鎖。

### 2.4 Tamoxifen 為什麼在乳房是拮抗劑，在子宮和骨頭卻像雌激素

SERM 的「選擇性」不在藥，而在組織。在乳腺細胞，tamoxifen 與 raloxifene 都讓 ER 召集輔助抑制因子（corepressor）。在子宮內膜細胞，tamoxifen 卻像雌激素一樣召集 coactivator，raloxifene 不會；這個作用需要細胞內有高濃度的 coactivator SRC-1（Shang & Brown, 2002）。所以同一個藥在不同器官有相反的效果（Jensen & Jordan, 2003）：

| 組織 | tamoxifen 的作用 | 臨床結果 |
|------|----------------|---------|
| 乳房 | 拮抗 | 抗腫瘤、降低對側乳癌 |
| 子宮內膜 | 部分促效 | 內膜增生、息肉、子宮內膜癌（主要在 ≥50 歲）（Fisher et al., 1998） |
| 骨 | 停經後偏促效；停經前相反 | P-1 中停經後女性沒有骨質流失，停經前女性的腰椎與髖部骨密度下降（Bryant Ranch Prepack, 2026） |
| 血管與凝血 | 血栓風險上升 | 靜脈血栓、肺栓塞、中風（見 [6.2](#62-靜脈血栓與中風)） |
| 心血管 | 偏保護 | 輔助試驗中，tamoxifen 的心血管事件比安慰劑少（RR 0.67）（Khosrow-Khavar et al., 2017） |

Raloxifene 不刺激子宮內膜，所以被拿來做停經後女性的乳癌預防；toremifene 的結構與 tamoxifen 相近（見 [3.1](#31-serm)）。

> [!TIP]
> **同一把假鑰匙，插在不同的門上**
> Tamoxifen 這把假鑰匙在乳房的門上轉不動。但子宮內膜的門後站了很多幫手（coactivator），假鑰匙只要插著，幫手就能把門推開一點。骨頭的門也類似。所以 tamoxifen 最有名的毒性（子宮內膜增生與癌）其實是「雌激素作用」，AI 的毒性（骨頭、關節、陰道乾澀）則是「沒有雌激素」。記住這一點，兩類藥的副作用就不用硬背。

> [!IMPORTANT]
> **機轉對應毒性**
> - Tamoxifen 要記子宮內膜癌（部分促效作用）與 VTE；它在停經後不傷骨。
> - AI 與 OFS 的毒性來自雌激素缺乏：骨質流失與骨折、關節痛、陰道乾澀、血脂上升。
> - 熱潮紅兩邊都有。
> - 考題若問「哪個藥會增加子宮內膜癌」答 tamoxifen；問「哪個藥要追蹤骨密度」答 AI。

---

## 3. 分類與代表藥

**結論：** 乳癌的內分泌藥只有四類常用（SERM、AI、OFS、SERD），加上後線的 progestin。同一類裡面，藥與藥的差別主要在給藥方式、交互作用與少數特殊毒性，選藥的關鍵是停經狀態與治療情境。處方劑量表在[乳癌章 5.5](../03-breast-cancer.md#55-內分泌治療與-cdk46-抑制劑)，本段只寫理解這類藥需要的數字。

### 3.1 SERM

| 藥 | 美國仿單的用途與劑量 | 特點 |
|-----|-------------------|------|
| **tamoxifen** | 轉移性乳癌（女性與男性）、輔助治療、DCIS 術後、高風險女性的風險降低（≥35 歲且 5 年 Gail 風險 ≥1.67%）；輔助治療的試驗劑量為每天 20–40 mg，超過 20 mg 沒有更有效 | 停經前後都可用；prodrug，注意 CYP2D6（見 [4.1](#41-tamoxifen-是-prodrug)）；加框警語針對 DCIS 與風險降低的族群：子宮惡性腫瘤、中風、肺栓塞（Bryant Ranch Prepack, 2026） |
| **toremifene** | 停經後、ER 陽性或不明的轉移性乳癌；60 mg 每天一次 | 結構與 tamoxifen 相近的 triphenylethylene 衍生物；**加框警語：QT 延長**，與劑量和濃度相關，先天或後天 QT 延長、未矯正的低血鉀或低血鎂禁用；避免併用延長 QT 的藥與強效 CYP3A4 抑制劑（Kyowa Kirin, 2024） |
| **raloxifene** | 停經後骨質疏鬆的治療與預防；降低「停經後、有骨質疏鬆或乳癌高風險」女性的侵襲性乳癌風險；60 mg 每天一次 | **不能用來治療乳癌，也不用於降低復發風險**；停經前不用；加框警語：VTE 與中風死亡（Eli Lilly and Company, 2023） |

Raloxifene 的定位來自 STAR 試驗：19,747 位停經後高風險女性，raloxifene 預防侵襲性乳癌的效果與 tamoxifen 相當（RR 1.02，0.82–1.28），血栓栓塞較少（RR 0.70，0.54–0.91），白內障較少，子宮癌 23 例對 36 例（RR 0.62，0.35–1.08）（Vogel et al., 2006）。

### 3.2 Aromatase 抑制劑

| 藥 | 類型 | 美國仿單劑量 | 半衰期與代謝 | 特點 |
|-----|------|------------|------------|------|
| **letrozole** | 非類固醇，競爭性抑制 | 2.5 mg 每天一次，與進食無關 | 約 2 天；CYP3A4 與 CYP2A6 | 肝硬化或重度肝功能不全減為 2.5 mg 隔天一次（Novartis Pharmaceuticals Corporation, 2024） |
| **anastrozole** | 非類固醇 | 1 mg 每天一次 | 約 50 小時；約 85% 經肝代謝 | 已有缺血性心臟病的女性，缺血性心血管事件 17%，tamoxifen 為 10%（ANI Pharmaceuticals, 2026） |
| **exemestane** | 類固醇，不可逆的「自殺性抑制」 | 25 mg 每天一次，**餐後** | 約 24 小時；CYP3A4 | 併用強效 CYP3A4 誘導劑（rifampicin、phenytoin）時改為 50 mg；開始前查 25-OH vitamin D（Pharmacia & Upjohn, 2025） |

- 三個藥的適應症略有不同（例如 exemestane 的輔助適應症是 tamoxifen 用 2–3 年後接續），但整合分析把三者合併看，結論一致：比 tamoxifen 多降低約三成的復發（Early Breast Cancer Trialists' Collaborative Group, 2015）。
- 非類固醇與類固醇 AI 的結構不同，臨床上的意義之一是「換一個試試看」：因副作用停掉第一個 AI 的病人，換成另一個之後 38.6% 可以繼續服用（Henry et al., 2012）。
- Anastrozole 與 exemestane 的仿單都寫明不要與含雌激素的製劑併用，因為會抵銷藥效（ANI Pharmaceuticals, 2026；Pharmacia & Upjohn, 2025）。

> [!WARNING]
> **停經前病人不可單用 AI**
> AI 在卵巢仍有功能的病人無效（Burstein et al., 2010；ANI Pharmaceuticals, 2026）。停經前要用 AI，只能是「AI 加 OFS」；ribociclib 的仿單也要求停經前、停經中女性與男性在併用 AI 或 fulvestrant 時合併 LHRH agonist（Novartis Pharmaceuticals Corporation, 2026）。開 AI 之前，病歷上一定要有停經狀態的依據（見 [5.1](#51-開藥前先確定兩件事er-與停經狀態)）。

### 3.3 卵巢功能抑制與卵巢去除

| 方法 | 做法 | 可逆嗎 | 重點 |
|------|------|-------|------|
| GnRH agonist | goserelin 3.6 mg 皮下注射於前腹壁，每 28 天（美國仿單；TerSera, 2026）；SOFT 與 TEXT 用 triptorelin（Pagani et al., 2014）；leuprolide 是同類藥 | 可逆；子宮內膜異位症的試驗中，停藥後月經多在 8 週內恢復 | 先 flare 後抑制；要按時注射；不保證避孕 |
| 雙側卵巢切除 | 手術 | 不可逆 | 立即、確定；SOFT 與 TEXT 允許以它達成 OFS（Pagani et al., 2014） |
| 卵巢放射線照射 | 放射治療 | 不可逆 | SOFT 與 TEXT 允許的第三種方法（Pagani et al., 2014） |

- **機轉**：GnRH agonist 持續佔住腦下垂體的受體，LH 與 FSH 先上升、後下降，卵巢最後停工（TerSera, 2026）。
- **代價**：等於提早停經。ASCO 指出，與單用 tamoxifen 相比，加上卵巢抑制會明顯增加更年期症狀與性功能障礙，生活品質下降（Burstein et al., 2016）。
- **台灣**：goserelin、leuprorelin、triptorelin 的許可證狀態與健保 5.5.1 的條件，乳癌章已整理（[乳癌章 4.4](../03-breast-cancer.md#44-早期-hrher2內分泌治療是底其他是加分) 的警示框與 [5.5](../03-breast-cancer.md#55-內分泌治療與-cdk46-抑制劑)），開立前先確認院內有哪一個藥。
- GnRH agonist 在化療期間保護卵巢的用途（POEMS）是另一個題目，見[乳癌章 6.12](../03-breast-cancer.md#612-生育力懷孕與避孕)。

### 3.4 SERD 與 PROTAC 降解劑

**Fulvestrant** 是唯一的注射型 SERD：ER 拮抗劑，會讓乳癌細胞的 ER 蛋白減少，沒有促效作用（Osborne et al., 2004；AstraZeneca, 2020）。美國仿單的適應症是停經後 HR 陽性、HER2 陰性晚期乳癌的單獨使用（未曾用過內分泌治療，或內分泌治療後惡化），以及與 palbociclib、abemaciclib、ribociclib 合用。未曾用過內分泌治療的病人，fulvestrant 的無惡化存活比 anastrozole 長（FALCON：16.6 對 13.8 個月，HR 0.797，0.637–0.999）（Robertson et al., 2016）。給法見 [4.3](#43-fulvestrant長效肌肉注射與負荷劑量)。

**口服 SERD 與 PROTAC**（以下都是美國仿單；台灣的藥證與健保狀態見[乳癌章 4.12](../03-breast-cancer.md#412-新藥與常用藥在台灣的藥證與健保狀態)）：

| 藥 | 美國適應症（都需 FDA 認可的檢測驗出 ESR1 突變） | 劑量與服法 | 交互作用 | 必記毒性 |
|-----|-------------------------------------------|-----------|---------|---------|
| **elacestrant**（2023 年核准） | 停經後女性或成年男性，ER 陽性、HER2 陰性晚期乳癌，至少一線內分泌治療後惡化 | 345 mg 每天一次，**隨餐** | 避免強效與中效 CYP3A4 抑制劑、誘導劑 | 高膽固醇 30%、高三酸甘油酯 27%，治療前與治療中驗血脂；噁心 35%（Stemline Therapeutics, 2026） |
| **imlunestrant**（2025 年核准） | 成人 ER 陽性、HER2 陰性晚期乳癌，至少一線內分泌治療後惡化；單用或併用 abemaciclib | 400 mg 每天一次，**空腹**（餐前至少 2 小時或餐後 1 小時） | 強效 CYP3A 抑制劑：避免，不得已時減為 200 mg；強效誘導劑：避免，不得已時增為 600 mg | 血紅素下降 30%、肌肉骨骼疼痛 30%、疲倦 23%、腹瀉 22%（Eli Lilly and Company, 2026） |
| **camizestrant**（2026 年加速核准） | 與 CDK4/6 抑制劑合用；在「AI 加 CDK4/6 抑制劑」治療期間驗出 ESR1 突變時，把 AI 換成它 | 75 mg 每天一次，與進食無關 | 見下方警示框 | 心搏過緩 8%、QTc 延長 2.6%、視覺異常 34%（AstraZeneca, 2026） |
| **vepdegestrant**（2026 年核准） | 成人 ER 陽性、HER2 陰性晚期乳癌，至少一線內分泌治療後惡化 | 200 mg 每天一次，**隨餐** | 強效 CYP3A 抑制劑：避免，不得已時減為 100 mg；強效誘導劑：避免，不得已時增為 300 mg；避免併用延長 QT 的藥 | QTc 延長 10%：治療前驗 ECG 與電解質，QTc >470 ms 不開始，約 4 週後再驗一次（Arvinas Operations, 2026） |

Vepdegestrant 不是傳統的 SERD。仿單稱它為異質雙功能蛋白降解劑：一端結合 ER，另一端結合 E3 ligase cereblon，讓 ER 被多重泛素化後送進 proteasome 分解（Arvinas Operations, 2026）。這就是 PROTAC（proteolysis-targeting chimera）的作法（Campone et al., 2025）。

> [!WARNING]
> **Camizestrant 加 ribociclib：心律不整的加框警語**
> 美國仿單的加框警語指出，camizestrant 與 ribociclib 併用（ribociclib 本身延長 QTc，又是強效 CYP3A 抑制劑）可能增加 Torsades de Pointes、其他心室性心律不整與猝死的風險；ribociclib 以外會延長 QTc 的藥也要避免。開始前驗 ECG，前 2 週每週一次，之後依臨床需要；同時矯正電解質異常（AstraZeneca, 2026）。病人若原本的 CDK4/6 抑制劑是 ribociclib，換藥前一定要先和主治醫師、藥師確認。

### 3.5 Progestin：megestrol

Megestrol acetate 錠劑的美國仿單適應症是晚期乳癌或子宮內膜癌的緩和治療，乳癌劑量為每天 160 mg（40 mg 一天四次），至少連續治療 2 個月才能判斷療效；確切的抗腫瘤機轉不明，可能與抑制腦下垂體促性腺激素、使雌激素分泌下降有關（Teva Pharmaceuticals, 2022）。在 AI、fulvestrant 與標靶藥出現之後，它已經很少用來治療乳癌。

現在比較常看到它用在食慾不振與惡病質：ASCO 2020 指引認為沒有任何藥物足以列為惡病質的標準治療，但若決定試用藥物，progesterone analog 是可用的選項之一（Roeland et al., 2020）。用法、證據與健保 5.3.6 見[支持性照護 12.1](../00-shared/03-supportive-care.md#121-惡病質與食慾不振)。

要記的毒性都寫在仿單上：血栓栓塞（含肺栓塞）、長期使用造成腎上腺抑制（停藥時可出現腎上腺功能不全，也有 Cushing 症候群的報告）、新發生或惡化的糖尿病、體重增加（Teva Pharmaceuticals, 2022）。

### 3.6 攝護腺癌的雄性素路徑藥（對照用，不在本手冊四個癌別內）

攝護腺癌不是本手冊涵蓋的癌別，這一小節只為了讓分類完整，也因為這些藥常出現在病人的藥單上。邏輯與乳癌完全相同：把雄性素抽掉（去勢），或把雄性素受體（androgen receptor, AR）擋住。台灣的藥證與給付不在本手冊範圍，請查仿單與健保第 9 節原文。

| 類別 | 代表藥 | 機轉 | 重點 |
|------|--------|------|------|
| 手術去勢 | 雙側睪丸切除 | 拿掉睪丸 | 最早的方法，不可逆（Crawford et al., 2019） |
| LHRH agonist | leuprolide、goserelin、triptorelin | 與乳癌的 OFS 相同：先 flare，受體 downregulation 需 2–3 週 | flare 可使骨痛與阻塞症狀加重，可先併用 antiandrogen 來擋（Crawford et al., 2019；Denmeade & Isaacs, 2002） |
| GnRH antagonist | degarelix（注射）、relugolix（口服） | 直接阻斷受體，沒有 flare | degarelix 在 2–3 天內壓低 testosterone（Crawford et al., 2019）；HERO 試驗：relugolix 維持去勢 96.7%，leuprolide 88.8%，重大心血管事件 2.9% 對 6.2%（Shore et al., 2020） |
| 第一代 antiandrogen | bicalutamide、flutamide、nilutamide | 擋住雄性素與 AR 結合，不降低 testosterone | 多用於擋 flare 或合併去勢（Crawford et al., 2019）；27 項合併去勢的隨機試驗只有 3 項顯示存活好處（Denmeade & Isaacs, 2002） |
| 雄性素合成抑制劑 | abiraterone，**併用 prednisone** | 抑制 CYP17，阻斷睪丸、腎上腺與腫瘤內的雄性素合成 | 礦物皮質素過多：高血壓、低血鉀、水腫；要追蹤肝功能、血壓與血鉀。COU-AA-301：整體存活 14.8 對 10.9 個月，HR 0.65（de Bono et al., 2011；Crawford et al., 2019） |
| 新一代 AR 抑制劑 | enzalutamide、apalutamide、darolutamide | 結合 AR，並阻止它進入細胞核與結合 DNA | AFFIRM：enzalutamide 的整體存活 18.4 對 13.6 個月，HR 0.63；癲癇 0.6%（Scher et al., 2012；Crawford et al., 2019） |

**對乳癌與其他癌別照護有用的兩點：**

- 去勢的副作用與乳癌的 OFS 很像：熱潮紅、性功能障礙、骨質疏鬆、糖尿病與心血管事件風險上升（Crawford et al., 2019）。
- 這幾個藥是交互作用的大戶。FDA 的範例表把 enzalutamide 與 apalutamide 列為**強效 CYP3A 誘導劑**，abiraterone 列為**中效 CYP2D6 抑制劑**（US Food and Drug Administration, 2026）。病人若同時有別的癌症或慢性病用藥，要請藥師檢查。

---

## 4. 藥物動力學與交互作用

**結論：** 這一類藥的藥物動力學只要記四件事。Tamoxifen 要靠 CYP2D6 活化；AI 幾乎沒有交互作用，但把雌激素壓到極低，骨頭要付代價；fulvestrant 半衰期約 40 天，所以需要負荷劑量；GnRH agonist 先升後降，要確認卵巢真的被壓住。真正需要查交互作用的，多半是一起開的標靶藥。

### 4.1 Tamoxifen 是 prodrug

- **代謝路徑**：tamoxifen 本身活性弱。CYP3A4 先把它去甲基成 N-desmethyltamoxifen（占代謝的九成以上），CYP2D6 再把它氧化成 endoxifen。Endoxifen 與 4-hydroxytamoxifen 的抗雌激素效力約為原型藥的 100 倍（Goetz et al., 2018）。
- **半衰期很長**：tamoxifen 約 5–7 天，N-desmethyltamoxifen 約 14 天，約 4 週達到穩定濃度（Bryant Ranch Prepack, 2026）。偶爾漏一天影響不大；但停藥後藥物還會留在體內數週，所以仿單要求停藥後 2 個月內不可懷孕。
- **CYP2D6 抑制劑會讓它「吃了等於沒吃」**：加拿大安大略的世代研究納入 2,430 位 66 歲以上、同時使用 tamoxifen 與一種 SSRI 的女性。Tamoxifen 用藥期間與 paroxetine 重疊的比例每增加 25%、50%、75%，乳癌死亡風險分別增加 24%、54%、91%；其他抗憂鬱藥沒有這個現象（Kelly et al., 2010）。

| FDA 範例表的 CYP2D6 抑制強度 | 藥物 | tamoxifen 病人怎麼辦 |
|---------------------------|------|-------------------|
| **強效** | paroxetine、fluoxetine、bupropion、quinidine、terbinafine | 避免 |
| **中效** | duloxetine、cinacalcet、mirabegron、rolapitant、abiraterone | 避免（CPIC 對代謝正常者也建議避開中效與強效抑制劑） |
| **弱效** | sertraline、escitalopram、fluvoxamine、celecoxib、cimetidine、amiodarone | 代謝正常者 CPIC 未要求避免；代謝較差者連弱效也要避免 |

（出處：US Food and Drug Administration, 2026；Goetz et al., 2018。名單裡有幾個不是精神科藥：terbinafine 是口服抗黴菌藥，mirabegron 治療膀胱過動，rolapitant 是止吐藥，查藥單時容易漏掉。）

**CPIC 依 CYP2D6 表現型的建議**（Goetz et al., 2018）：

| 表現型 | 建議 | 建議強度 |
|--------|------|---------|
| ultrarapid、normal metabolizer | tamoxifen 標準劑量 20 mg/day；避免中效與強效 CYP2D6 抑制劑 | 強 |
| intermediate metabolizer（含 activity score 1.0） | 考慮改用 AI（停經前加 OFS）；AI 有禁忌時考慮 tamoxifen 40 mg/day；弱效到強效的抑制劑都避免 | 中等（部分情況為 optional） |
| poor metabolizer | 改用其他內分泌治療，例如 AI（停經前加 OFS）；tamoxifen 40 mg/day 可提高 endoxifen 但無法恢復正常 | 強 |

**要不要常規驗 CYP2D6 基因型？** CPIC 指引處理的是「已經有基因型時怎麼開藥」（Goetz et al., 2018）。ASCO 2010 年的指引明確反對用 CYP2D6 基因型來選擇輔助內分泌治療，但提醒併用 CYP2D6 抑制劑（bupropion、paroxetine、fluoxetine）時要小心（Burstein et al., 2010）；本章讀到的 ASCO 後續更新（2014 年全文、2016 與 2019 年摘要）沒有再處理這個問題。兩份文件都同意的是**查藥單**，這也是專師每次都做得到的事。藥物基因檢測的通則見[化療基礎第 12 節](../00-shared/01-chemo-basics.md#12-藥物基因檢測與特殊族群評估)。

**Tamoxifen 的其他交互作用**（美國仿單；Bryant Ranch Prepack, 2026）：

- **Coumarin 類抗凝血藥（warfarin）**：抗凝血效果可能顯著增加，要監測 PT。用於 DCIS 與風險降低時，正在使用 coumarin 類抗凝血藥，或有深部靜脈栓塞、肺栓塞病史，都是禁忌。
- **Rifampin**：讓 tamoxifen 的 AUC 下降 86%。結核病治療期間要特別留意。
- **AI**：不可與 anastrozole 併用；tamoxifen 會讓 letrozole 的血中濃度下降約 37%。

> [!TIP]
> **生咖啡豆與烘豆機**
> Tamoxifen 像生的咖啡豆，吞下去的時候還沒有香味。肝臟的 CYP2D6 是烘豆機，把它烘成真正有效的 endoxifen。Paroxetine、fluoxetine 這類藥等於把烘豆機的插頭拔掉：豆子照吃，卻喝不到咖啡。有些人天生烘豆機功率就低（poor metabolizer），加倍放豆子（40 mg）也補不回來，所以 CPIC 建議直接換別種藥。

### 4.2 AI：交互作用少，代價在骨頭

- **Letrozole**：與進食無關；半衰期約 2 天，2–6 週達穩定濃度；由 CYP3A4 與 CYP2A6 代謝；肝硬化或重度肝功能不全者減為 2.5 mg 隔天一次（Novartis Pharmaceuticals Corporation, 2024）。
- **Anastrozole**：半衰期約 50 小時；約 85% 經肝代謝，腎排除約占總清除的 10%（ANI Pharmaceuticals, 2026）。
- **Exemestane**：餐後服用；半衰期約 24 小時；主要經 CYP3A4 代謝，併用強效 CYP3A4 誘導劑時劑量改為 50 mg（Pharmacia & Upjohn, 2025）。
- **藥效學的代價**：雌激素被壓得越低，骨頭流失越快。Letrozole 用 24 個月，腰椎骨密度中位數下降 4.1%，tamoxifen 組上升 0.3%；延長輔助的 MA.17 中，新診斷的骨質疏鬆 14.5% 對 7.8%（Novartis Pharmaceuticals Corporation, 2024）。處置見 [6.5](#65-骨質流失與骨折)。

### 4.3 Fulvestrant：長效肌肉注射與負荷劑量

美國仿單的給法（AstraZeneca, 2020）：

- **500 mg**，分成兩支各 5 mL，**左右臀各一支**，每支慢慢推 1–2 分鐘。
- **第 1、15、29 天各一次，之後每月一次。**
- 中度肝功能不全（Child-Pugh B）減為 250 mg；重度（Child-Pugh C）沒有研究資料。

**為什麼要在第 15 天多打一次？** 肌肉注射後的半衰期約 40 天（AstraZeneca, 2020），只照每月一次給藥，血中濃度要好幾個月才會爬到穩定。CONFIRM 試驗把「500 mg 加第 14 天的負荷劑量」與原本核准的每月 250 mg 相比，無惡化存活較好（HR 0.80，0.68–0.94），毒性沒有增加（Di Leo et al., 2010）。

給藥前要想到的四件事（AstraZeneca, 2020）：

1. **出血**：使用抗凝血藥、血小板低下或有出血體質的病人，肌肉注射要小心。
2. **坐骨神經**：臀部背側注射點靠近坐骨神經，曾有坐骨神經痛、神經痛與周邊神經病變的報告。
3. **檢驗干擾**：fulvestrant 會讓 estradiol 免疫分析出現**假性偏高**。用 estradiol 判斷停經狀態或卵巢抑制是否足夠時，要把這一點考慮進去。
4. **交互作用**：CYP3A4 參與它的代謝，但 ketoconazole 與 rifampin 都不改變它的藥物動力學，不需要因此調整劑量。

### 4.4 GnRH agonist：flare 與確認卵巢真的被壓住

**Flare（先升）**：開始 goserelin 後，LH 與 FSH 先上升，estradiol 跟著短暫上升，大約 3 週才降到停經後範圍；最初幾週腫瘤症狀可能暫時加重，有骨轉移的病人曾有高血鈣的報告（TerSera, 2026）。骨轉移病人在頭幾週出現嗜睡、口渴、便秘、意識改變時，要驗血鈣，處置見[急症章第 5 節](../00-shared/02-oncologic-emergencies.md#5-惡性高血鈣hypercalcemia-of-malignancy)。

**壓不完全（後降得不夠）**：

- SOFT 的 SOFT-EST 子研究追蹤每月打 triptorelin 加 exemestane 的停經前病人：第 3、6、12 個月各有 25%、24%、17% 的人 estradiol 高於研究設定的門檻（2.72 pg/mL）。與壓不下去相關的因子是沒有做過化療、BMI 較高、基線 FSH 與 LH 較低（Bellet et al., 2016）。
- 化療後無月經不等於停經：45 位化療後無月經而開始 AI 的女性（中位年齡 47 歲），12 位（27%）卵巢功能恢復，恢復時的年齡中位數 44 歲（範圍 40–50 歲）；作者提醒，監測卵巢功能需要高敏感度的 estradiol 分析法（Smith et al., 2006）。
- ASCO 也寫明，化療或 tamoxifen 造成的無月經不可靠，單靠抽血也不夠，因為卵巢功能可能在之後恢復（Burstein et al., 2010）。

**專師可以做的事：**

1. 注射日期排好，不要拖延；病人請假或出國前先安排。
2. 每次回診問月經有沒有回來、有沒有陰道出血、熱潮紅是否突然消失。
3. 有疑慮時抽 estradiol 與 FSH、LH，並確認檢驗室用的方法在低濃度是否可靠。
4. 懷疑壓不住時回報主治醫師，討論改用 tamoxifen 或改做卵巢切除。

> [!NOTE]
> **多久驗一次 estradiol，各院不同**
> 本章讀到的 ASCO 指引摘要與試驗摘要沒有規定「AI 加 OFS 的病人多久驗一次 estradiol」（Burstein et al., 2016；Bellet et al., 2016）。是否常規驗、多久驗一次、用哪一種分析法，請依院內乳癌團隊的流程。

> [!TIP]
> **一直按電鈴，屋主把電鈴拆了**
> 正常的 GnRH 是一陣一陣釋放的，像偶爾按一下電鈴，腦下垂體就開門送出 LH 與 FSH。GnRH agonist 是把電鈴按住不放。屋主一開始被吵得衝出來好幾次（flare），之後乾脆把電鈴線剪掉（受體 downregulation），從此再按也沒有人應門，卵巢或睪丸就收不到訊號。GnRH antagonist 則是一開始就把電鈴封住，所以沒有 flare。

### 4.5 一起開的標靶藥，才是交互作用的重點

- **CDK4/6 抑制劑**：ribociclib 主要經 CYP3A4 清除。強效 CYP3A 抑制劑要避免，不得已時減量（早期乳癌 200 mg、轉移性 400 mg）；強效誘導劑要避免。Ribociclib 也不與 tamoxifen 併用：MONALEESA-7 中 QTcF 比基線增加超過 60 ms 的比例，併用 tamoxifen 為 16%，併用非類固醇 AI 為 7%（Novartis Pharmaceuticals Corporation, 2026）。三個 CDK4/6 抑制劑的劑量調整表在[乳癌章 5.5](../03-breast-cancer.md#55-內分泌治療與-cdk46-抑制劑)，藥理見[標靶藥物](03-targeted-therapy.md)。
- **口服 SERD 與 PROTAC**：都受 CYP3A 影響，調整方式見 [3.4](#34-serd-與-protac-降解劑) 的表。
- **FDA 範例表上的強效 CYP3A 抑制劑**：clarithromycin、itraconazole、ketoconazole、posaconazole、voriconazole、ritonavir。**強效誘導劑**：rifampin、carbamazepine、phenytoin、St. John's wort、enzalutamide、apalutamide（US Food and Drug Administration, 2026）。

| 病人在用的藥 | 藥單上要找什麼 | 為什麼 |
|------------|--------------|-------|
| tamoxifen | paroxetine、fluoxetine、bupropion、duloxetine、terbinafine；warfarin；rifampin | CYP2D6 被抑制，endoxifen 下降；抗凝血效果增加；rifampin 讓 tamoxifen 濃度大降 |
| AI | 含雌激素的製劑；exemestane 另查 rifampin、phenytoin | 抵銷藥效；誘導劑讓 exemestane 濃度下降 |
| fulvestrant | 抗凝血藥 | 肌肉注射的出血風險，不是藥物動力學交互作用 |
| toremifene、camizestrant、vepdegestrant、ribociclib | 其他會延長 QT 的藥、強效 CYP3A 抑制劑 | QT 延長的風險疊加 |
| elacestrant、imlunestrant、vepdegestrant、CDK4/6 抑制劑 | 強效 CYP3A 抑制劑與誘導劑，包含 St. John's wort | 血中濃度升高或下降 |

（出處：各藥美國仿單，見 3.1–3.4 與本段引用。）

---

## 5. 臨床怎麼用

**結論：** 先確定 ER 陽性與停經狀態。早期乳癌依「停經狀態乘以復發風險」選藥、決定吃幾年；轉移性乳癌先用內分泌治療加 CDK4/6 抑制劑，惡化後依 biomarker 換藥。處方劑量、試驗細節與健保條件都在乳癌章（[第 4 段](../03-breast-cancer.md#4-治療策略依分期)、[第 5 段](../03-breast-cancer.md#5-常用處方regimen)、[第 9 段](../03-breast-cancer.md#9-健保給付與事前審查)），這裡只給決策骨架。

### 5.1 開藥前先確定兩件事：ER 與停經狀態

- **ER**：腫瘤細胞核染色 ≥1% 為陽性；1–10% 是 ER low positive，內分泌治療的效益資料有限。DCIS 也要驗 ER，才能判斷內分泌治療有沒有機會降低日後的乳癌風險（Allison et al., 2020）。
- **停經狀態**：ASCO 的說法是「停經一年沒有月經」是臨床上的標誌，但這個定義不適用於很多乳癌病人，例如化療或 tamoxifen 造成的無月經（Burstein et al., 2010）。有疑問就抽 FSH 與 estradiol，並記得兩個陷阱：低濃度的 estradiol 需要高敏感度的分析法（Smith et al., 2006）；fulvestrant 會造成 estradiol 假性偏高（AstraZeneca, 2020）。
- **健保的寫法**：CDK4/6 抑制劑條文對「停經後」列出三種證據（年滿 55 歲、曾雙側卵巢切除、FSH 與 estradiol 在停經後範圍），單純「月經停了」不在其中，見[乳癌章 9.2](../03-breast-cancer.md#92-hr-陽性內分泌治療cdk46-抑制劑與-pi3kaktmtorhdac-抑制劑)。

> [!CAUTION]
> **待核對：NCCN 現行版的停經定義**
> 臨床上最常引用的是 NCCN 乳癌指引的停經定義。本章無法開啟 NCCN 指引全文，只在二手資料（引用 NCCN 2023 年版的機構文件）讀到下列條件，現行版是否相同請對照原文：(1) 曾雙側卵巢切除；(2) 年齡 ≥60 歲；(3) 年齡 <60 歲、在沒有化療、tamoxifen、toremifene 或卵巢抑制的情況下無月經 ≥12 個月，且 FSH 與 estradiol 在停經後範圍；(4) 年齡 <60 歲且正在使用 tamoxifen 或 toremifene 者，以 FSH 與 estradiol 在停經後範圍為準；(5) 正在使用 LHRH agonist 或 antagonist 的人無法判定停經狀態。

### 5.2 早期乳癌

| 情境 | 選擇 | 依據 |
|------|------|------|
| 停經後 | AI 5 年；或 tamoxifen 2–3 年後換 AI | AI 對 tamoxifen 各 5 年：復發 RR 第 0–1 年 0.64、第 2–4 年 0.80；10 年乳癌死亡 12.1% 對 14.2%（RR 0.85，0.75–0.96）。先 tamoxifen 再換 AI，也比 tamoxifen 吃滿 5 年好（10 年乳癌死亡 8.7% 對 10.1%）（Early Breast Cancer Trialists' Collaborative Group, 2015） |
| 停經前、低復發風險 | tamoxifen 5 年，不加 OFS | ASCO：不需要化療的 stage I，以及 ≤1 cm 的淋巴結陰性腫瘤，不應加 OFS（Burstein et al., 2016） |
| 停經前、高復發風險 | OFS 加 tamoxifen 或加 AI，5 年 | ASCO：一般會建議化療的 stage II–III 應加 OFS，可搭配 tamoxifen 或 AI（Burstein et al., 2016）。SOFT 中曾化療而仍未停經者，5 年無乳癌比例：tamoxifen 78.0%、tamoxifen 加 OFS 82.5%、exemestane 加 OFS 85.7%（Francis et al., 2015） |
| 停經前、已用 OFS：tamoxifen 還是 AI？ | AI 的復發較少，存活尚無差異 | SOFT 加 TEXT 合併：exemestane 加 OFS 對 tamoxifen 加 OFS 的 5 年無病存活 91.1% 對 87.3%（HR 0.72，0.60–0.85）（Pagani et al., 2014）。四項試驗、7,030 人的整合分析：復發 RR 0.79（0.69–0.90），乳癌死亡無差異（RR 1.01），骨折 6.4% 對 5.1%（EBCTCG, 2022） |

SOFT 與 TEXT 的 15 年最終報告把訊息說得更清楚：在 SOFT 沒有化療的族群，不論用哪一組，遠端復發與存活都維持在很高的水準；真正有存活差異的是高風險者，例如 35 歲以下、HER2 陰性的病人，15 年整體存活為 exemestane 加 OFS 82.5%、tamoxifen 加 OFS 77.9%、tamoxifen 單用 68.1%（Francis et al., 2026）。所以「要不要壓卵巢」是風險分層的問題，不是每個停經前病人都要。完整的試驗表見[乳癌章 4.4](../03-breast-cancer.md#44-早期-hrher2內分泌治療是底其他是加分)。

**吃 5 年還是 10 年？**

- **ATLAS**：12,894 位吃滿 5 年 tamoxifen 的女性，隨機分派到繼續吃到 10 年或停藥。ER 陽性的 6,846 人中，復發 617 對 711 人，乳癌死亡 331 對 397 人。好處主要出現在第 10 年以後：復發 RR 在第 5–9 年為 0.90，之後為 0.75；乳癌死亡 RR 分別是 0.97 與 0.71。代價是肺栓塞（RR 1.87）與子宮內膜癌（RR 1.74）（Davies et al., 2013）。
- **aTTom**：設計相同的另一個試驗，6,953 人，繼續吃到 10 年的復發 580 例，停藥組 672 例；子宮內膜癌 102 例（2.9%）對 45 例（1.3%）。這個試驗只以 2013 年的會議摘要發表，以上數字取自 ASCO 指引的整理（Burstein et al., 2014）。
- **MA.17**：5,187 位吃滿 5 年 tamoxifen 的停經後女性，接著用 letrozole 或安慰劑。第一次期中分析的 4 年無病存活為 93% 對 87%，試驗因此提前解盲（Goss et al., 2003）。
- **AI 之後再延長 AI**：12 項試驗、22,031 人的整合分析顯示，延長 AI 讓復發減少 27%（RR 0.73）。已用過 AI 的人再吃 5 年，第 5–15 年的復發風險為 11.6% 對 15.2%，但乳癌死亡的差異未達顯著（RR 0.90，0.70–1.15）；絕對好處在淋巴結陽性（16.3% 對 20.1%）大於陰性（9.1% 對 11.8%）；5 年骨折風險增加（RR 1.35）；約 39% 的人沒有照分派服藥（EBCTCG, 2025）。
- **為什麼值得延長**：停藥後復發不會停。吃滿 5 年內分泌治療後，第 5–20 年的遠端復發風險依原始的 T、N 與分級從 10% 到 41% 不等，連 T1N0、低分級的腫瘤也有 10%（Pan et al., 2017）。
- **指引怎麼說**：停經前或停經狀態不明者，吃滿 5 年 tamoxifen 後應提供繼續吃到 10 年；已確定停經者，可以繼續 tamoxifen 或換成 AI，總長 10 年（Burstein et al., 2014）。淋巴結陽性者建議延長治療（含 AI）到總長最多 10 年；淋巴結陰性者依復發風險個別決定。延長 AI 沒有整體存活的好處，骨骼毒性較多，要與病人共同決定（Burstein et al., 2019）。

> [!IMPORTANT]
> **延長治療的考點**
> - ATLAS 與 aTTom 比的是 **tamoxifen 10 年對 5 年**；MA.17 是 **tamoxifen 5 年後接 letrozole**。不要混在一起。
> - Tamoxifen 10 年的好處在**第 10 年以後**才明顯，代價是子宮內膜癌與肺栓塞。
> - 延長 AI 降低復發與對側乳癌，但**沒有證明延長整體存活**，骨折增加。
> - 淋巴結陽性的人從延長治療得到的絕對好處較大。

**輔助 CDK4/6 抑制劑（一句話版）**：高復發風險者在內分泌治療之外，可以加 abemaciclib 2 年（monarchE：7 年無侵襲性疾病存活 77.4% 對 70.9%，整體存活也達顯著；Johnston et al., 2026）或 ribociclib 3 年加非類固醇 AI（NATALEE：5 年絕對差 4.5%，整體存活 HR 0.800、未達顯著；Crown et al., 2025）。入組條件、毒性與健保見[乳癌章 4.4](../03-breast-cancer.md#44-早期-hrher2內分泌治療是底其他是加分)，藥理見[標靶藥物](03-targeted-therapy.md)。

### 5.3 轉移性 HR+/HER2−

原則：只要腫瘤還對內分泌治療敏感，而且沒有 visceral crisis，就一線接一線用內分泌治療為主的組合，把化療與抗體藥物複合體往後放。visceral crisis 的定義與內分泌抗藥性的分類見[乳癌章 4.7](../03-breast-cancer.md#47-轉移性-hrher2先排除-visceral-crisis再走內分泌路線)。

| 步驟 | 做什麼 | 關鍵證據 |
|------|-------|---------|
| 第一線 | AI（停經前加 OFS）加 CDK4/6 抑制劑 | 這是轉移性 ER 陽性乳癌的標準第一線（Hanker et al., 2020）。MONALEESA-2：ribociclib 加 letrozole 的整體存活 63.9 對 51.4 個月（HR 0.76，0.63–0.93）（Hortobagyi et al., 2022） |
| 惡化時 | 驗血中 ctDNA 的 ESR1；確認 PIK3CA、AKT1、PTEN 與 germline BRCA 的結果 | ASCO 建議在內分泌治療（含或不含 CDK4/6 抑制劑）復發或惡化時常規驗 ESR1，優先用血液 ctDNA（Burstein et al., 2023；措辭取自 ASCO Post 對該更新的報導，指引全文未能開啟） |
| ESR1 突變 | 口服 SERD 或 PROTAC 降解劑 | 見 [7.3](#73-下一代藥物證據與限制) |
| PIK3CA、AKT1 或 PTEN 變異 | fulvestrant 加 alpelisib 或 capivasertib | SOLAR-1 與 CAPItello-291 都顯示無惡化存活延長；alpelisib 的 grade 3–4 高血糖 36.6%，capivasertib 的 grade ≥3 皮疹 12.1%、腹瀉 9.3%（André et al., 2019；Turner et al., 2023） |
| PIK3CA 突變且內分泌抗藥，尚未治療轉移 | inavolisib 加 palbociclib 加 fulvestrant | INAVO120（Turner et al., 2024） |
| germline BRCA 突變 | PARP 抑制劑 | OlympiAD：olaparib 讓疾病惡化或死亡的風險比化療低 42%（Robson et al., 2017）；見[乳癌章 4.10](../03-breast-cancer.md#410-gbrca-突變parp-抑制劑) |
| 沒有可用的 biomarker | fulvestrant 為主的組合，或 everolimus 加 exemestane | 見乳癌章 4.7 |

各線的數字、選擇順序與台灣能不能用，都以乳癌章 4.7 與 [4.12](../03-breast-cancer.md#412-新藥與常用藥在台灣的藥證與健保狀態) 為準。PI3K、AKT 抑制劑的高血糖與皮疹處置見[乳癌章第 6 段](../03-breast-cancer.md#6-副作用評估與處置)。

### 5.4 DCIS 與風險降低

**DCIS**：ER 陽性的 DCIS 在保乳手術與放療後，可以用 tamoxifen 5 年降低日後的乳癌事件（NSABP B-24：5 年 8.2% 對 13.4%）（Fisher et al., 1999）。停經後可以改用 anastrozole：NSABP B-35 中它的無乳癌間期較好，但好處主要在 60 歲以下；grade 4 以上的血栓或栓塞事件，tamoxifen 組 17 件，anastrozole 組 4 件（Margolese et al., 2016）。細節見[乳癌章 4.2](../03-breast-cancer.md#42-原位癌dcis)。

**還沒有得乳癌的高風險女性：**

| 藥 | 對象 | 試驗結果 | 要注意 |
|-----|------|---------|-------|
| tamoxifen 20 mg × 5 年 | 停經前後皆可 | NSABP P-1：侵襲性乳癌減少 49%；ER 陽性腫瘤減少 69%，ER 陰性不變（Fisher et al., 1998） | 子宮內膜癌 RR 2.53，中風、肺栓塞、深部靜脈栓塞增加，都集中在 ≥50 歲 |
| raloxifene 60 mg × 5 年 | 只限停經後 | STAR：預防侵襲性乳癌與 tamoxifen 相當，血栓較少（Vogel et al., 2006） | 不能用於治療乳癌（Eli Lilly and Company, 2023） |
| anastrozole 1 mg × 5 年 | 只限停經後 | IBIS-II：中位追蹤 131 個月，乳癌 85 對 165 例（HR 0.51，0.39–0.66），停藥後仍有效（Cuzick et al., 2020） | 長期追蹤沒有看到骨折或心血管疾病增加 |
| exemestane 25 mg | 只限停經後 | MAP.3：中位追蹤 35 個月，侵襲性乳癌 11 對 32 例（HR 0.35，0.18–0.70）（Goss et al., 2011） | 追蹤時間短 |
| 低劑量 tamoxifen 5 mg × 3 年 | 乳房上皮內腫瘤（非典型增生、LCIS、DCIS）術後 | 500 人，腫瘤事件 14 對 28 例（HR 0.48，0.26–0.92）（DeCensi et al., 2019） | 病人數少；嚴重不良事件與安慰劑相近 |

Tamoxifen 的美國仿單把「高風險」定為 35 歲以上、5 年 Gail 風險 ≥1.67%（Bryant Ranch Prepack, 2026）。台灣的適應症與給付請見各癌別章第 9 段；高風險族群的辨識與遺傳諮詢見[乳癌章 1.4](../03-breast-cancer.md#14-遺傳性乳癌與基因檢測)。

### 5.5 男性乳癌

ASCO 指引：輔助內分泌治療以 **tamoxifen 5 年**為首選；tamoxifen 有禁忌時可用 GnRH agonist 或 antagonist 加 AI；轉移性疾病除非有 visceral crisis 或快速惡化，第一線仍是內分泌治療，標靶藥的用法與女性相同（Hassett et al., 2020）。

---

## 6. 毒性與處置

**結論：** 內分泌治療的毒性很少讓人住進加護病房，卻很容易讓人不想吃藥。病人一吃就是 5 到 10 年，「不嚴重但每天都在」的副作用如果沒有人處理，下一步就是自己停藥。記法很簡單：tamoxifen 看**血栓與子宮**，AI 看**骨頭與關節**，OFS 等於**提早停經的全部**。

| 問題 | tamoxifen | AI | OFS | 第一步 |
|------|-----------|-----|-----|-------|
| 熱潮紅、盜汗 | 常見 | 常見 | 常見 | 非荷爾蒙治療；tamoxifen 病人避開 CYP2D6 抑制劑 |
| 血栓、中風 | 增加 | 較少 | 不是主要問題 | 問病史、教警訊 |
| 子宮內膜 | 增生、息肉、癌 | 較少 | 不是主要問題 | 異常出血立刻轉婦科 |
| 骨 | 停經後不流失，停經前流失 | 流失、骨折 | 流失 | 評估骨折風險、骨密度、維生素 D、必要時用藥 |
| 關節與肌肉 | 較少 | 常見 | 併用 AI 時常見 | 運動、換另一個 AI、duloxetine、針灸 |
| 陰道乾澀、性功能 | 分泌物與出血較多 | 乾澀 | 明顯 | 潤滑劑與陰道保濕劑 |
| 血脂、心血管 | 偏保護 | 膽固醇上升 | 不是主要問題 | 追蹤血脂、控制危險因子 |
| 懷孕 | 可傷害胎兒 | 可傷害胎兒 | 不保證避孕 | 驗孕、非荷爾蒙避孕 |

（出處與數字見以下各小節。）

### 6.1 熱潮紅與盜汗

**多常見**：tamoxifen 的輔助試驗中，熱潮紅 64%，安慰劑 48%（Bryant Ranch Prepack, 2026）。AI 並沒有比較少太多：BIG 1-98 中 letrozole 33.5%、tamoxifen 38.0%（Novartis Pharmaceuticals Corporation, 2024）；ATAC 中 anastrozole 36%、tamoxifen 41%（ANI Pharmaceuticals, 2026）。

**非荷爾蒙的選擇：**

| 治療 | 證據 | 要注意 |
|------|------|-------|
| venlafaxine | 4 週的隨機試驗：75 mg/day 的熱潮紅分數中位下降 61%，安慰劑 27%（Loprinzi et al., 2000） | 口乾、食慾下降、噁心、便秘；不在 FDA 的 CYP2D6 抑制劑範例表上 |
| gabapentin | 420 位乳癌女性：900 mg/day（分三次）在第 4 與第 8 週讓熱潮紅嚴重度分數下降 49% 與 46%，安慰劑 21% 與 15%；300 mg/day 無效（Pandya et al., 2005） | 分次服用 |
| oxybutynin | 150 位女性，6 週：2.5 mg 與 5 mg 一天兩次都比安慰劑明顯降低熱潮紅分數與次數（Leon-Ferre et al., 2020） | 口乾、排尿困難、腹痛 |
| elinzanetant | OASIS-4：內分泌治療引起中重度熱潮紅的女性，120 mg 每天一次，第 4 週每日次數減少 6.5 次，安慰劑減少 3.0 次（Cardoso et al., 2025） | 頭痛、疲倦、嗜睡；本章未核對台灣是否上市 |
| 非藥物 | 認知行為治療、慢呼吸、催眠（Carter et al., 2018） | ASCO 把它們與 venlafaxine、gabapentin 並列為可提供的選項 |

**Tamoxifen 病人選藥的陷阱**：paroxetine 與 fluoxetine 是強效 CYP2D6 抑制劑，duloxetine 是中效（US Food and Drug Administration, 2026），都不適合。含雌激素的全身性荷爾蒙補充與治療目的相反；anastrozole 與 exemestane 的仿單寫明不與含雌激素的製劑併用（ANI Pharmaceuticals, 2026；Pharmacia & Upjohn, 2025）。

### 6.2 靜脈血栓與中風

- **數字**：tamoxifen 仿單的加框警語（DCIS 與風險降低族群）：每 1,000 人年的肺栓塞 0.75 對 0.25，中風 1.43 對 1.00，部分是致命的；同一段也寫明，對已經診斷乳癌的女性，tamoxifen 的效益大於風險（Bryant Ranch Prepack, 2026）。ATLAS 中延長到 10 年的肺栓塞 RR 1.87（1.13–3.07），中風 RR 1.06（0.83–1.36）（Davies et al., 2013）。AI 的血栓比 tamoxifen 少：BIG 1-98 的血栓栓塞事件 3.2% 對 4.6%（Novartis Pharmaceuticals Corporation, 2024）。
- **誰的風險高**：P-1 中，中風、肺栓塞與深部靜脈栓塞多發生在 50 歲以上的女性（Fisher et al., 1998）。
- **開藥前**：問血栓與中風病史、是否使用抗凝血藥。有血栓病史的停經後病人，AI 通常是較合理的選擇。
- **治療中**：教病人認得警訊。確診後的抗凝血治療見[支持性照護第 7 節](../00-shared/03-supportive-care.md#7-癌症相關靜脈血栓vte)。

> [!WARNING]
> **Tamoxifen 病人的四個警訊，出現就立刻就醫**
> 單側小腿或大腿腫痛；突然喘或胸痛；突然單側無力、臉歪或說話不清楚；停經後陰道出血或不正常的陰道出血。前三項是血栓與中風，最後一項要排除子宮內膜癌。仿單記載這些事件有致命的案例（Bryant Ranch Prepack, 2026）。

### 6.3 子宮內膜：增生、息肉與癌

- **數字**：P-1 的子宮內膜癌 RR 2.53（1.35–4.97），主要增加在 50 歲以上；tamoxifen 組的病例都是第 I 期，沒有人死於子宮內膜癌（Fisher et al., 1998）。輔助治療中，AI 的 10 年子宮內膜癌發生率 0.4%，tamoxifen 1.2%（EBCTCG, 2015）。延長到 10 年時，第 5–14 年的累積風險是 3.1% 對 1.6%，死亡 0.4% 對 0.2%（Davies et al., 2013）。
- **怎麼追蹤**：美國婦產科醫學會的意見是，停經後使用 tamoxifen 的女性要密切注意內膜增生或癌的症狀；停經前女性的子宮癌風險沒有已知的增加，照一般婦科照護即可；除非本來就是子宮內膜癌的高風險者，**不建議對沒有症狀的人做常規的內膜監測**（例如定期超音波或切片），因為沒有證據顯示能提早發現癌症；若出現非典型內膜增生，要重新評估是否繼續 tamoxifen（American College of Obstetricians and Gynecologists, 2014）。
- **專師要做的**：每次回診問月經型態、出血、骨盆疼痛或壓迫感；仿單建議每年做婦科檢查，異常陰道出血要立刻評估（Bryant Ranch Prepack, 2026）。

### 6.4 AI 相關的關節肌肉症狀

- **多常見、多重要**：使用 AI 的乳癌存活者最多有一半出現關節痛，這是服藥遵從性不佳最常見的原因（Irwin et al., 2015）。在一個 503 人的前瞻試驗中，32.4% 在 2 年內因副作用停掉第一個 AI，單是因肌肉骨骼症狀而停的就占全體的 24.3%；停藥時間的中位數只有 6.1 個月（Henry et al., 2012）。
- **有隨機試驗證據的處置：**

| 處置 | 試驗 | 結果 |
|------|------|------|
| 運動 | HOPE：121 人，每週 150 分鐘有氧運動加每週 2 次有人指導的肌力訓練，12 個月 | 最痛關節的分數下降 1.6 分（29%），對照組上升 0.2 分（Irwin et al., 2015） |
| 換另一個 AI | 同上的前瞻試驗，83 人換藥 | 38.6% 能繼續服用第二個 AI（Henry et al., 2012） |
| duloxetine | SWOG S1202：299 人，13 週 | 12 週時平均關節痛比安慰劑多降 0.82 分；任何級別的不良事件 78% 對 50%（Henry et al., 2018） |
| 針灸 | SWOG S1200：226 人，前 6 週每週 2 次、後 6 週每週 1 次 | 6 週時最痛分數下降 2.05 分，假針灸 1.07 分，候補組 0.99 分；輕微瘀青較多（Hershman et al., 2018） |

- **提醒**：duloxetine 是中效 CYP2D6 抑制劑，可以用在吃 AI 的病人，不適合吃 tamoxifen 的病人（US Food and Drug Administration, 2026）。以上方法都無效而病人想放棄時，與主治醫師討論換成 tamoxifen；ASCO 支持依副作用與病人偏好決定何時使用 AI（Burstein et al., 2010）。

### 6.5 骨質流失與骨折

- **數字**：AI 對 tamoxifen 的 5 年骨折風險 8.2% 對 5.5%（RR 1.42）（EBCTCG, 2015）；停經前用 AI 加 OFS 的骨折 6.4%，tamoxifen 加 OFS 5.1%（EBCTCG, 2022）；延長 AI 再增加骨折（RR 1.35）（EBCTCG, 2025）。
- **評估**：ASCO 建議用已建立的工具評估骨折風險，風險明顯者做骨密度（BMD）；營養、運動與生活型態對所有人都有幫助；需要用藥時，以骨質疏鬆劑量的 bisphosphonate 或 denosumab 為首選（Shapiro et al., 2019）。Exemestane 仿單另外建議開始前驗 25-OH vitamin D，缺乏者補充；有骨質疏鬆或其風險者在開始時做 BMD（Pharmacia & Upjohn, 2025）。
- **預防骨折的證據**：ABCSG-18 中，使用 AI 的停經後病人每 6 個月皮下注射 denosumab 60 mg，首次臨床骨折的風險減半（HR 0.50，0.39–0.65；骨折 92 對 176 例）（Gnant et al., 2015）。
- **別混淆**：預防骨質疏鬆的劑量、輔助 bisphosphonate 降低復發的用法、骨轉移的劑量是三件事，整理在[乳癌章 7.8](../03-breast-cancer.md#78-骨骼健康)；骨轉移用藥與顎骨壞死見[支持性照護第 8 節](../00-shared/03-supportive-care.md#8-骨轉移的骨骼保護劑bone-modifying-agents)。

### 6.6 陰道乾澀與性健康

AI 與 OFS 把雌激素壓到很低，陰道乾澀與性交疼痛很常見，病人卻很少主動說。ASCO 指出，卵巢抑制會明顯增加更年期症狀與性功能障礙（Burstein et al., 2016）。

- **第一步**：陰道保濕劑加上潤滑劑。ASCO 的性健康指引把它們列為陰道與外陰萎縮症狀的第一選擇；低劑量陰道雌激素、lidocaine 與 dehydroepiandrosterone 只在部分情況考慮；男性的勃起功能問題可用第五型磷酸二酯酶抑制劑（Carter et al., 2018）。
- **專師要主動問**：把「性生活有沒有受影響」放進例行的症狀詢問。

> [!NOTE]
> **吃 AI 的病人能不能用陰道雌激素，由腫瘤科決定**
> AI 的仿單寫明不與含雌激素的製劑併用（ANI Pharmaceuticals, 2026）。局部低劑量雌激素是否可以例外，本章沒有取得婦產科與腫瘤科共識文件的全文。病人詢問時，先提供非荷爾蒙的方法，其餘由主治醫師與婦產科依院內做法決定。

### 6.7 血脂與心血管

- **AI**：BIG 1-98 中，letrozole 組出現高膽固醇的比例是 52.3%，tamoxifen 組 28.6%（Novartis Pharmaceuticals Corporation, 2024）。Anastrozole 仿單記載膽固醇升高 9% 對 3.5%；原本就有缺血性心臟病的女性，缺血性心血管事件 17% 對 10%（ANI Pharmaceuticals, 2026）。
- **怎麼解讀**：19 項隨機試驗、62,345 人的整合分析中，AI 的心血管事件比 tamoxifen 多（RR 1.19，1.07–1.34），但 AI 與安慰劑相比沒有增加（RR 1.01），而 tamoxifen 比安慰劑少（RR 0.67）。作者的結論是，兩者的差距多半來自 tamoxifen 的保護作用，不是 AI 的傷害（Khosrow-Khavar et al., 2017）。
- **Elacestrant**：高膽固醇 30%、高三酸甘油酯 27%，仿單要求治療前與治療中監測血脂（Stemline Therapeutics, 2026）。
- **專師要做的**：開始 AI 前留一筆血脂基線，之後定期追蹤；血壓、血糖、抽菸這些心血管危險因子照一般原則處理。

### 6.8 生育、避孕與懷孕

- **Tamoxifen 可造成胎兒傷害，而且不是避孕藥。** 仿單要求治療期間與停藥後 2 個月內不可懷孕，性生活活躍的女性要用屏障或非荷爾蒙避孕；有生育可能的女性在月經期間開始服藥，月經不規則者要先驗孕（Bryant Ranch Prepack, 2026）。它的前身正是因為會誘發排卵而當不成避孕藥（見 [1.4](#14-tamoxifen一個失敗的避孕藥)）。
- **GnRH agonist 不保證避孕。** Goserelin 通常抑制排卵並使月經停止，但仿單寫明不能確保避孕，治療期間與停藥後 12 週要用非荷爾蒙避孕（TerSera, 2026）。
- **其他藥最後一劑後的避孕期間**（美國仿單）：fulvestrant 1 年（AstraZeneca, 2020）；letrozole、anastrozole 至少 3 週，exemestane 1 個月（Novartis Pharmaceuticals Corporation, 2024；ANI Pharmaceuticals, 2026；Pharmacia & Upjohn, 2025）；elacestrant、imlunestrant 1 週（Stemline Therapeutics, 2026；Eli Lilly and Company, 2026）；vepdegestrant 2 週（Arvinas Operations, 2026）；camizestrant 4 週且須為非荷爾蒙避孕（AstraZeneca, 2026）。完整的對照表在[乳癌章 6.12](../03-breast-cancer.md#612-生育力懷孕與避孕)。
- **想懷孕的病人：POSITIVE 試驗。** 516 位 42 歲以下、I–III 期 HR 陽性乳癌、已接受 18–30 個月輔助內分泌治療的女性，暫停治療最多 2 年去嘗試懷孕；計畫書要求停藥後先有 3 個月的洗脫期，生產與哺乳後強烈建議恢復治療。74.0% 至少懷孕一次，63.8% 至少一次活產。3 年乳癌事件 8.9%，外部對照 9.2%。中位追蹤只有 41 個月，作者強調更長期的安全性仍待觀察（Partridge et al., 2023）。
- 生育力保存的時間軸與轉介見[乳癌章 7.7](../03-breast-cancer.md#77-生育力懷孕與避孕諮詢)與[化療基礎 12.5](../00-shared/01-chemo-basics.md#125-生育力保存與避孕諮詢)。

> [!WARNING]
> **有生育可能的女性：開藥前驗孕，開藥時談避孕**
> Tamoxifen、AI、fulvestrant、GnRH agonist 與口服 SERD 的美國仿單都有胚胎胎兒毒性的警語（各藥出處見 6.8）。最容易出錯的是 tamoxifen（病人以為「荷爾蒙藥會避孕」）與 GnRH agonist（病人以為「月經停了就不會懷孕」）。避孕方式要選非荷爾蒙的，並記在病歷上（Bryant Ranch Prepack, 2026；TerSera, 2026）。

### 6.9 其他要認得的毒性

- **眼睛（tamoxifen）**：P-1 中做白內障手術的人數，tamoxifen 組 201 人，安慰劑組 129 人；另有角膜變化、視網膜病變與視網膜靜脈栓塞的報告。視力改變要轉眼科（Bryant Ranch Prepack, 2026）。
- **肝（tamoxifen）**：肝酵素變化，少見的脂肪肝、膽汁鬱積、肝炎；仿單建議定期驗肝功能與全血球計數（Bryant Ranch Prepack, 2026）。
- **高血鈣與腫瘤 flare**：有骨轉移的病人開始 tamoxifen 或 toremifene 後的頭幾週可能出現高血鈣，嚴重時要停藥（Bryant Ranch Prepack, 2026；Kyowa Kirin, 2024）。
- **QT 與心搏過緩**：toremifene、camizestrant、vepdegestrant 都要注意，見 [3.1](#31-serm) 與 [3.4](#34-serd-與-protac-降解劑)。
- **Megestrol**：長期使用後腎上腺軸被抑制，仿單警告若沒有認出來可能致命（Teva Pharmaceuticals, 2022）。停藥或遇到感染、手術等壓力時，出現低血壓、噁心、無力要想到腎上腺功能不全。

### 6.10 遵從性：最大的毒性是沒有吃

- **多少人沒吃完**：美國北加州 8,769 位早期乳癌病人的藥局紀錄顯示，到 4.5 年時 32% 已經停藥；還在吃的人裡面只有 72% 吃得夠（藥物持有率 ≥80%）。合起來，**只有 49% 的人照建議吃滿全程**。40 歲以下的女性停藥風險最高（HR 1.51）（Hershman et al., 2010）。
- **沒吃的後果**：同一個世代中，提早停藥者的死亡風險較高（HR 1.26，1.09–1.46），繼續吃但吃不夠的人也是（HR 1.49，1.23–1.81）；10 年存活 80.7% 對 73.6%（Hershman et al., 2011）。
- **連臨床試驗也一樣**：延長 AI 的安慰劑對照試驗中，約 39% 的人沒有照分派服藥（EBCTCG, 2025）。

> [!IMPORTANT]
> **內分泌治療失敗，先想遵從性**
> 早期乳癌的內分泌治療「失敗」，最常見的原因不是抗藥性，而是沒有吃、吃不夠或太早停。每次回診都要問兩件事：「上個月大概漏了幾天？」「有沒有哪個副作用讓你想停藥？」副作用處理好，病人才吃得下去。做法見 [8.4](#84-遵從性支持)。

---

