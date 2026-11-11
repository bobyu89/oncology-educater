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
> - AI 對 tamoxifen（停經後，各 5 年）：10 年乳癌死亡 12.1% 對 14.2%；代價是 5 年骨折 8.2% 對 5.5%，但 10 年子宮內膜癌 0.4% 對 1.2%（Early Breast Cancer Trialists' Collaborative Group, 2015）。
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
| 1896 | 格拉斯哥外科醫師 Beatson 在愛丁堡報告：晚期乳癌病人切除卵巢後腫瘤明顯縮小（原文刊於 Transactions of the Medico-Chirurgical Society of Edinburgh 第 15 卷 153–179 頁，PMID 29584099）；1900 年 Boyd 彙整英國病例，只有約三分之一有反應，維持約一年 | 從此知道部分乳癌的生長依賴卵巢，也留下「為什麼只有三分之一有效」的問題（Jordan, 2006） |
| 1941 | Huggins 與 Hodges：轉移性攝護腺癌以去勢或雌激素治療，並用血清 acid phosphatase 追蹤反應 | 口服雌激素的藥物去勢成為第一個有效的全身性癌症治療；Huggins 在 1966 年獲諾貝爾生理醫學獎（Huggins & Hodges, 1972；Denmeade & Isaacs, 2002） |
| 1958 | Lerner 等報告第一個非類固醇抗雌激素 MER-25，後來因毒性大、效力低而停止臨床研究 | 「抗雌激素」這個藥理概念成立（Jordan, 2006） |
| 1962 | Jensen 與 Jacobson 證明放射標記的 estradiol 會被目標組織留住；同年 ICI 藥廠的化學家 Dora Richardson 合成 ICI 46,474 | ER 的概念誕生；tamoxifen 的分子出現（Jordan, 2006；Quirke, 2017） |
| 1967 | Harper 與 Walpole 發表 ICI 46,474 在大鼠抑制著床的作用 | 它原本是避孕藥計畫的產物（Harper & Walpole, 1967） |
| 1971 | Cole 等的第一個乳癌臨床試驗：46 位晚期乳癌病人，10 位反應良好，副作用少 | tamoxifen 轉向乳癌（Cole et al., 1971） |
| 1971 | Jensen 等報告腫瘤的 ER 與腎上腺切除等內分泌治療的反應有關 | ER 成為預測內分泌治療反應的 biomarker（Jensen et al., 1971；Jensen & Jordan, 2003） |
| 1971 | Schally 團隊從豬下視丘分離出 LHRH（即 GnRH），定出十胜肽結構並合成 | GnRH 類似物的起點；Schally 與 Guillemin 在 1977 年獲諾貝爾獎（Schally et al., 1971；Nobel Prize Outreach, 2026） |
| 1973 | 英國核發 Nolvadex（tamoxifen）許可並上市，適應症是不排卵性不孕與乳癌的緩和治療 | 乳癌的第一個標靶治療藥上市（Quirke, 2017；Jordan, 2006） |
| 1977 | Brodie 等：選擇性 aromatase 抑制劑 4-hydroxyandrostenedione 讓大鼠的雌激素依賴性乳腺腫瘤 80% 明顯縮小 | 「只關掉 aromatase」可行（Brodie et al., 1977） |
| 1982–1984 | LHRH agonist 用於攝護腺癌：10 位病人的初步報告，之後 leuprolide 與 diethylstilbestrol（DES）的隨機試驗 | 藥物去勢開始取代手術與雌激素（Tolis et al., 1982；Leuprolide Study Group, 1984） |
| 1984 | Coombes 等：4-hydroxyandrostenedione 肌肉注射治療 11 位停經後轉移性乳癌，4 位有反應 | 選擇性 AI 的臨床概念驗證（Coombes et al., 1984） |
| 1991 | Wakeling 等發表純抗雌激素 ICI 182,780，即後來的 fulvestrant | 第一個 SERD（Wakeling et al., 1991；Osborne et al., 2004） |
| 1998 | EBCTCG 整合 55 項試驗、約 37,000 人；同年 NSABP P-1 顯示 tamoxifen 讓高風險女性的侵襲性乳癌減少 49% | 輔助 tamoxifen 約 5 年成為標準；第一個癌症化學預防藥（Early Breast Cancer Trialists' Collaborative Group, 1998；Fisher et al., 1998；Jordan, 2006） |
| 2002–2005 | ATAC 與 BIG 1-98：anastrozole、letrozole 在停經後輔助治療勝過 tamoxifen | AI 成為停經後的首選（Baum et al., 2002；Breast International Group 1-98 Collaborative Group, 2005） |
| 2003 | MA.17：tamoxifen 吃滿 5 年後接 letrozole，4 年無病存活 93% 對 87% | 延長輔助治療的開始（Goss et al., 2003） |
| 2013 | ATLAS：tamoxifen 10 年優於 5 年；同年在轉移性腫瘤找到 ESR1 ligand-binding domain 突變 | 「吃多久」與「為什麼失效」同時有新答案（Davies et al., 2013；Toy et al., 2013） |
| 2014–2015 | SOFT 與 TEXT：停經前高風險者加 OFS，exemestane 加 OFS 再降低復發 | 停經前治療開始依風險分層（Pagani et al., 2014；Francis et al., 2015） |
| 2023 | 美國 FDA 核准口服 SERD elacestrant（第一個在第三期試驗勝過標準內分泌單藥的口服 SERD），限 ESR1 突變 | 內分泌治療進入 biomarker 導向（US Food and Drug Administration, 2023；Bardia et al., 2024） |
| 2025–2026 | imlunestrant、vepdegestrant、camizestrant 取得美國適應症（camizestrant 為加速核准） | 口服 SERD 與 PROTAC 降解劑進入臨床（Eli Lilly and Company, 2026；Arvinas Operations, 2026；AstraZeneca, 2026） |

### 1.1 Beatson 的卵巢切除：為什麼停經狀態決定一切

Beatson 在 1896 年報告一位晚期乳癌病人切除卵巢後戲劇性地好轉，這是用「拿掉荷爾蒙」治療乳癌的開端。但之後彙整的病例顯示只有約三分之一的病人有反應，而且大約一年後就失效（Jordan, 2006）。

**和今天的連結：** 停經前病人的卵巢仍是雌激素的主要來源，所以高風險的停經前病人到今天還在做同一件事，只是把手術刀換成每月一針的 GnRH agonist（見 [3.3](#33-卵巢功能抑制與卵巢去除)）。「為什麼只有三分之一有效」要等到 ER 被發現才有答案。

### 1.2 Huggins：攝護腺癌證明了同一個道理

1941 年，Huggins 與 Hodges 讓轉移性攝護腺癌病人接受去勢或雌激素治療，並用血清 acid phosphatase 追蹤反應（Huggins & Hodges, 1972，重刊 1941 年原文）。Huggins 因此在 1966 年得到諾貝爾獎。後來的美國退伍軍人醫院試驗發現，口服 DES 的效果與睪丸切除相當，但心血管與血栓栓塞毒性明顯（Denmeade & Isaacs, 2002）。這個毒性讓大家開始找更安全的藥物去勢方法，也就是後來的 LHRH agonist（見 1.6）。

**和今天的連結：** 乳癌與攝護腺癌的荷爾蒙治療用的是同一套邏輯（抽掉荷爾蒙，或擋住受體），所以毒性也像：熱潮紅、骨質流失、代謝與心血管問題。攝護腺癌的藥整理在 [3.6](#36-攝護腺癌的雄性素路徑藥對照用不在本手冊四個癌別內)。

### 1.3 Jensen 與雌激素受體：預測內分泌治療反應的 biomarker

Jensen 在 1960 年代初證明，放射標記的 estradiol 會被子宮等目標組織留住，推論一定有一個受體在接它。1971 年他的團隊把這件事變成檢驗：腫瘤有 ER，內分泌治療才可能有效；沒有 ER，幾乎不會有反應（Jensen et al., 1971；Jordan, 2006）。Beatson 的三分之一之謎就此解開。Jensen 與 Jordan 的回顧把 ER 稱為分子醫學的範本：先找到標靶，再用檢驗預測誰會對藥有反應（Jensen & Jordan, 2003）。

**和今天的連結：** 每一個乳癌檢體都要驗 ER。ASCO／CAP 的切點是腫瘤細胞核染色 ≥1% 即為 ER 陽性；1–10% 另外報告為 ER low positive，因為這一群用內分泌治療的效益資料有限（Allison et al., 2020）。EBCTCG 的資料證實 ER 是唯一能預測 tamoxifen 效益的因子，ER 陰性者用了沒有幫助（EBCTCG, 2011）。判讀細節見[乳癌章 2.2](../03-breast-cancer.md#22-erpr-與免疫組織化學亞型)。

### 1.4 Tamoxifen：一個失敗的避孕藥

1962 年，ICI 藥廠的化學家 Dora Richardson 在避孕藥計畫中合成了 ICI 46,474。計畫主持人是生物學家 Arthur Walpole，內分泌學家 Mike Harper 同年加入團隊，協助篩選化合物（Quirke, 2017）。在大鼠，它是很有效的事後避孕藥（Harper & Walpole, 1967）。但用在女性時結果相反：它**誘發排卵**，不能避孕。加上在美國拿不到專利，ICI 董事會一度決定終止計畫，Walpole 以辭職相逼才保住它，並把它轉向乳癌（Quirke, 2017）。

- **第一個臨床試驗**：曼徹斯特 Christie 醫院，46 位晚期乳癌病人，10 位反應良好；療效與當時使用的雌激素、雄性素相當，但副作用少得多（Cole et al., 1971）。
- **實驗室的轉折**：V. Craig Jordan 從 1972 年起先在美國的 Worcester Foundation、1974 年回到里茲大學後繼續，證明 tamoxifen 會擋住 estradiol 與 ER 的結合，並能預防致癌物誘發的大鼠乳腺腫瘤；他在動物身上發現，腫瘤負荷小的時候長期給藥效果最好，這成為「長期輔助治療」的依據（Jordan, 2006）。
- **整合分析定案**：EBCTCG 1998 年的整合分析顯示，tamoxifen 用 1 年、2 年、約 5 年，復發分別減少 21%、29%、47%，死亡減少 12%、17%、26%，用得越久越好；ER 很低或沒有的腫瘤效果很小（EBCTCG, 1998）。2011 年的更新確認 5 年 tamoxifen 讓 ER 陽性病人的乳癌死亡率在之後 15 年都降低約三分之一（EBCTCG, 2011）。
- **預防**：NSABP P-1 於 1992 年開始，13,388 位高風險女性，tamoxifen 讓侵襲性乳癌減少 49%（Fisher et al., 1998）；美國 FDA 於 1998 年核准它用於降低乳癌風險（Jordan, 2006）。

**和今天的連結：**

1. **Tamoxifen 不是避孕藥，還可能誘發排卵。** 停經前病人即使月經不規則也可能懷孕，所以一定要談避孕（見 [6.8](#68-生育避孕與懷孕)）。
2. **吃得夠久才有效。** 從 1 年、2 年、5 年到 10 年，每一次延長都有試驗支持，所以服藥遵從性是療效的一部分（見 [6.10](#610-遵從性最大的毒性是沒有吃)）。
3. **先驗 ER 再開藥。** 這是所有「先驗 biomarker、再開標靶藥」的原型。

### 1.5 Aromatase 抑制劑：從非選擇性到第三代

早期被當成 AI 使用的藥是 aminoglutethimide。它原本的目的是阻斷腎上腺功能來治療乳癌，後來才意外發現它是強力但**非選擇性**的 aromatase 抑制劑（Santen et al., 2009）。Angela Brodie 與 Harry Brodie 走另一條路：用類固醇受質的類似物專門抑制 aromatase。他們的 4-hydroxyandrostenedione（formestane）在大鼠讓血中 estradiol 降低 80%，並讓雌激素依賴性乳腺腫瘤縮小（Brodie et al., 1977）；1984 年 Coombes 與 Brodie 合作，把它用在 11 位停經後轉移性乳癌病人，4 位有反應（Coombes et al., 1984）。這兩個藥證明了概念，之後才有更強、更專一的第三代 AI：anastrozole、letrozole、exemestane（Santen et al., 2009），美國分別於 1995、1997、1999 年核准（ANI Pharmaceuticals, 2026；Novartis Pharmaceuticals Corporation, 2024；Pharmacia & Upjohn, 2025）。

兩個大型輔助試驗確立了 AI 的地位：

- **ATAC**（9,366 人）：anastrozole 對 tamoxifen 的 3 年無病存活 89.4% 對 87.4%（HR 0.83，95% CI 0.71–0.96）；**兩藥合併並不比 tamoxifen 單用好**（HR 1.02）（Baum et al., 2002）。
- **BIG 1-98**（8,010 人）：letrozole 對 tamoxifen 的 5 年無病存活 84.0% 對 81.4%（HR 0.81，0.70–0.93），遠端復發 HR 0.73（Breast International Group 1-98 Collaborative Group, 2005）。

**和今天的連結：** 第三代 AI 只關 aromatase，anastrozole 仿單寫明它不影響 cortisol 與 aldosterone，不需要補充類固醇（ANI Pharmaceuticals, 2026）。ATAC 的合併組沒有比較好，所以仿單寫「tamoxifen 不可與 anastrozole 併用」，我們只會「先後」使用，不會「同時」使用。

### 1.6 GnRH：先升後降的十胜肽

1971 年，Schally 團隊定出 LHRH 的結構：一個十胜肽，同時調控黃體生成素（LH）與濾泡刺激素（FSH）的分泌（Schally et al., 1971）。接下來的發現很反直覺：**持續**給 LHRH agonist，一開始 LH 與性荷爾蒙短暫上升，之後腦下垂體的受體 downregulation，性荷爾蒙反而掉到去勢的程度（Denmeade & Isaacs, 2002）。

- 攝護腺癌：Schally 與臨床團隊在 10 位病人身上看到腫瘤縮小與骨痛緩解（Tolis et al., 1982）；隨後的隨機試驗顯示 leuprolide 的客觀反應率與 DES 相當（86% 對 85%），副作用較少（Leuprolide Study Group, 1984）。
- 乳癌：停經前轉移性乳癌的四項隨機試驗整合分析顯示，LHRH agonist 加 tamoxifen 優於 LHRH agonist 單用（整體存活 HR 0.78，無惡化存活 HR 0.70）（Klijn et al., 2001）；之後 SOFT 與 TEXT 把 OFS 帶進早期乳癌（見 [5.2](#52-早期乳癌)）。

**和今天的連結：** 「先升後降」就是 flare。Goserelin 仿單記載，開始治療後 estradiol 要大約 3 週才降到停經後範圍，最初幾週腫瘤症狀與骨痛可能暫時加重（TerSera, 2026）。所以第一劑之後的頭幾週不能假設卵巢已經被壓住（見 [4.4](#44-gnrh-agonistflare-與確認卵巢真的被壓住)）。

### 1.7 Fulvestrant、口服 SERD，以及攝護腺癌的新藥

Tamoxifen 在某些組織有雌激素作用。ICI 的化學家想要一個「純」的抗雌激素：ICI 182,780 對 ER 的親和力接近 estradiol，沒有促效作用，在乳癌細胞株抑制生長的效果比 tamoxifen 的活性代謝物更完全（Wakeling et al., 1991）。它還會讓 ER 蛋白減少，所以被稱為第一個 SERD（Osborne et al., 2004）。Fulvestrant 於 2002 年在美國核准，當時劑量是每月 250 mg；CONFIRM 試驗證明 500 mg 加上負荷劑量的無惡化存活更好（HR 0.80，0.68–0.94），才改成今天的給法（Di Leo et al., 2010；AstraZeneca, 2020）。

Fulvestrant 只能肌肉注射，藥廠因此開發口服 SERD。第一個在第三期試驗勝過標準內分泌單藥的是 elacestrant（Bardia et al., 2024），美國 FDA 在 2023 年 1 月 27 日核准，適應症限 ESR1 突變（US Food and Drug Administration, 2023）；之後的 imlunestrant、camizestrant 與 PROTAC 降解劑 vepdegestrant 見 [7.3](#73-下一代藥物證據與限制)。

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

| 位置 | 藥 | 做了什麼 | 對雌激素濃度 | 對 ER 蛋白 |
|------|-----|---------|-----------|--------|
| 卵巢（源頭） | GnRH agonist、卵巢切除 | 讓卵巢停止製造雌激素；goserelin 約 3 週把 estradiol 壓到停經後範圍 | 降到停經後程度 | 不變 |
| 周邊 aromatase | AI | anastrozole 1 mg 在 14 天後讓 estradiol 降約 80%；letrozole 讓雌激素降 75–95%；exemestane 讓全身 aromatization 降 98% | 停經後再降到極低 | 不變 |
| 受體的口袋 | SERM | 與雌激素競爭 ER，讓受體擺成「關」的形狀 | 不靠降低雌激素 | 不變 |
| 受體本身 | SERD、PROTAC | 拮抗 ER，並使 ER 蛋白減少 | 不靠降低雌激素 | 減少 |

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
| **raloxifene** | 停經後骨質疏鬆的治療與預防；降低「停經後、有骨質疏鬆或乳癌高風險」女性的侵襲性乳癌風險；60 mg 每天一次 | **不能用來治療乳癌，也不用於降低復發風險**；停經前不用；加框警語：VTE 與中風死亡，現在或過去有 VTE 者禁用（Eli Lilly and Company, 2023） |

Raloxifene 的定位來自 STAR 試驗：19,747 位停經後高風險女性，raloxifene 預防侵襲性乳癌的效果與 tamoxifen 相當（RR 1.02，0.82–1.28），血栓栓塞較少（RR 0.70，0.54–0.91），白內障較少，子宮癌 23 例對 36 例（RR 0.62，0.35–1.08）（Vogel et al., 2006）。

### 3.2 Aromatase 抑制劑

| 藥 | 類型 | 美國仿單劑量 | 半衰期與代謝 | 特點 |
|-----|------|------------|------------|------|
| **letrozole** | 非類固醇，競爭性抑制 | 2.5 mg 每天一次，與進食無關 | 約 2 天；CYP3A4 與 CYP2A6 | 肝硬化或重度肝功能不全減為 2.5 mg 隔天一次（Novartis Pharmaceuticals Corporation, 2024） |
| **anastrozole** | 非類固醇 | 1 mg 每天一次 | 約 50 小時；約 85% 經肝代謝 | 已有缺血性心臟病的女性，缺血性心血管事件 17%，tamoxifen 為 10%（ANI Pharmaceuticals, 2026） |
| **exemestane** | 類固醇，不可逆的「自殺性抑制」 | 25 mg 每天一次，**餐後** | 約 24 小時；CYP3A4 | 併用強效 CYP3A4 誘導劑（rifampicin、phenytoin）時改為 50 mg；開始前查 25-OH vitamin D（Pharmacia & Upjohn, 2025） |

- 三個藥的適應症略有不同（例如 exemestane 的輔助適應症是 tamoxifen 用 2–3 年後接續），但整合分析把三者合併看，結論一致：在兩組用藥不同的期間，比 tamoxifen 多降低約三成的復發（Early Breast Cancer Trialists' Collaborative Group, 2015）。
- Exemestane 的輔助試驗中，關節痛 15%，tamoxifen 9%；熱潮紅兩者相近（21% 對 20%）（Pharmacia & Upjohn, 2025）。
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
- **代價**：等於提早停經。ASCO 指出，與單用 tamoxifen 相比，加上卵巢抑制會明顯增加更年期症狀與性功能障礙，生活品質下降（Burstein et al., 2016）；goserelin 仿單的警語也包括骨密度下降（TerSera, 2026）。
- **台灣**：goserelin、leuprorelin、triptorelin 的許可證狀態與健保 5.5.1 的條件，乳癌章已整理（[乳癌章 4.4](../03-breast-cancer.md#44-早期-hrher2內分泌治療是底其他是加分) 的警示框與 [5.5](../03-breast-cancer.md#55-內分泌治療與-cdk46-抑制劑)），開立前先確認院內有哪一個藥。
- GnRH agonist 在化療期間保護卵巢的用途（POEMS）是另一個題目，見[乳癌章 6.12](../03-breast-cancer.md#612-生育力懷孕與避孕)。

### 3.4 SERD 與 PROTAC 降解劑

**Fulvestrant** 是唯一的注射型 SERD：ER 拮抗劑，會讓乳癌細胞的 ER 蛋白減少，沒有促效作用（Osborne et al., 2004；AstraZeneca, 2020）。美國仿單的單獨使用適應症限停經後女性的 HR 陽性晚期乳癌（未曾用過內分泌治療而 HER2 陰性者，或內分泌治療後惡化者）；也可與 ribociclib（停經後）或與 palbociclib、abemaciclib（內分泌治療後惡化的女性）合用，停經前、停經中女性併用這些藥時要加 LHRH agonist（AstraZeneca, 2020）。未曾用過內分泌治療的病人，fulvestrant 的無惡化存活比 anastrozole 長（FALCON：16.6 對 13.8 個月，HR 0.797，0.637–0.999）（Robertson et al., 2016）。CONFIRM 試驗 500 mg 組最常見的不良反應是注射部位疼痛 12%、噁心 10%、骨痛 9%（AstraZeneca, 2020）。給法見 [4.3](#43-fulvestrant長效肌肉注射與負荷劑量)。

**口服 SERD 與 PROTAC**（以下都是美國仿單；台灣的藥證與健保狀態見[乳癌章 4.12](../03-breast-cancer.md#412-新藥與常用藥在台灣的藥證與健保狀態)）：

| 藥 | 美國適應症（都需 FDA 認可的檢測驗出 ESR1 突變） | 劑量與服法 | 交互作用 | 必記毒性 |
|-----|-------------------------------------------|-----------|---------|---------|
| **elacestrant**（2023 年核准） | 停經後女性或成年男性，ER 陽性、HER2 陰性晚期乳癌，至少一線內分泌治療後惡化 | 345 mg 每天一次，**隨餐** | 避免強效與中效 CYP3A4 抑制劑、誘導劑 | 高膽固醇 30%、高三酸甘油酯 27%，治療前與治療中驗血脂；噁心 35%（Stemline Therapeutics, 2026） |
| **imlunestrant**（2025 年核准） | 成人 ER 陽性、HER2 陰性晚期乳癌，至少一線內分泌治療後惡化；單用或併用 abemaciclib | 400 mg 每天一次，**空腹**（餐前至少 2 小時或餐後 1 小時） | 強效 CYP3A 抑制劑：避免，不得已時減為 200 mg；強效誘導劑：避免，不得已時增為 600 mg | 血紅素下降 30%、肌肉骨骼疼痛 30%、疲倦 23%、腹瀉 22%（Eli Lilly and Company, 2026） |
| **camizestrant**（2026 年加速核准） | 與 CDK4/6 抑制劑合用；在「AI 加 CDK4/6 抑制劑」治療期間驗出 ESR1 突變時，把 AI 換成它 | 75 mg 每天一次，與進食無關 | 見下方警示框 | 心搏過緩 8%、QTc 延長 2.6%、視覺異常 34%（AstraZeneca, 2026） |
| **vepdegestrant**（2026 年核准） | 成人 ER 陽性、HER2 陰性晚期乳癌，至少一線內分泌治療後惡化 | 200 mg 每天一次，**隨餐** | 強效 CYP3A 抑制劑：避免，不得已時減為 100 mg；強效誘導劑：避免，不得已時增為 300 mg；避免併用延長 QT 的藥 | QTc 延長 10%：治療前驗 ECG 與電解質，QTc >470 ms 不開始，約 4 週後再驗一次（Arvinas Operations, 2026） |

肝功能不全時的劑量：elacestrant 在中度（Child-Pugh B）減為 258 mg，重度避免使用（Stemline Therapeutics, 2026）；imlunestrant 在中度或重度減為 200 mg（Eli Lilly and Company, 2026）。

**停經前病人與 imlunestrant：仿單改過版。** Imlunestrant 仿單在 2026-06-04 以前的版本，劑量段有一句「停經前、停經中女性與男性應併用 GnRH agonist」；本章讀取的 2026-09-18 版新增了併用 abemaciclib 的適應症，劑量段已經沒有這一句（Eli Lilly and Company, 2026）。乳癌章引用的是舊版，所以兩章寫法不同。VERITAC-2 中，停經前、停經中女性與男性都併用 GnRH agonist（Arvinas Operations, 2026）。開立時以當時的仿單為準，並和主治醫師確認是否需要卵巢抑制。

Vepdegestrant 不是傳統的 SERD。仿單稱它為異質雙功能蛋白降解劑：一端結合 ER，另一端結合 E3 ligase cereblon，讓 ER 被多重泛素化後送進 proteasome 分解（Arvinas Operations, 2026）。這就是 PROTAC（proteolysis-targeting chimera）的作法（Campone et al., 2025）。

> [!WARNING]
> **Camizestrant 加 ribociclib：心律不整的加框警語**
> 美國仿單的加框警語指出，camizestrant 與 ribociclib 併用（ribociclib 本身延長 QTc，又是強效 CYP3A 抑制劑）可能增加 Torsades de Pointes、其他心室性心律不整與猝死的風險；ribociclib 以外會延長 QTc 的藥也要避免。開始前驗 ECG，前 2 週每週一次，之後依臨床需要；同時矯正電解質異常（AstraZeneca, 2026）。病人若原本的 CDK4/6 抑制劑是 ribociclib，換藥前一定要先和主治醫師、藥師確認。

### 3.5 Progestin：megestrol

Megestrol acetate 錠劑的美國仿單適應症是晚期乳癌或子宮內膜癌的緩和治療，乳癌劑量為每天 160 mg（40 mg 一天四次），至少連續治療 2 個月才能判斷療效。仿單寫它對子宮內膜癌的確切抗腫瘤機轉不明，可能與抑制腦下垂體促性腺激素、使雌激素分泌下降有關；對乳癌則是改變其他類固醇荷爾蒙的作用，並直接作用於腫瘤細胞（Teva Pharmaceuticals, 2022）。在 AI、fulvestrant 與標靶藥出現之後，它已經很少用來治療乳癌。

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
| 新一代 AR 抑制劑 | enzalutamide、apalutamide、darolutamide | 結合 AR，並阻止它進入細胞核與結合 DNA | AFFIRM：enzalutamide 的整體存活 18.4 對 13.6 個月，HR 0.63；疲倦、腹瀉、熱潮紅較多，癲癇 0.6%（Scher et al., 2012；Crawford et al., 2019） |

**對乳癌與其他癌別照護有用的兩點：**

- 去勢的副作用與乳癌的 OFS 很像：熱潮紅、性功能障礙、骨質疏鬆、糖尿病與心血管事件風險上升（Crawford et al., 2019）。
- 這幾個藥是交互作用的大戶。FDA 的範例表把 enzalutamide 與 apalutamide 列為**強效 CYP3A 誘導劑**，abiraterone 列為**中效 CYP2D6 抑制劑**（US Food and Drug Administration, 2026）。病人若同時有別的癌症或慢性病用藥，要請藥師檢查。

---

## 4. 藥物動力學與交互作用

**結論：** 這一類藥的藥物動力學只要記四件事。Tamoxifen 要靠 CYP2D6 活化；AI 幾乎沒有交互作用，但把雌激素壓到極低，骨頭要付代價；fulvestrant 半衰期約 40 天，所以需要負荷劑量；GnRH agonist 先升後降，要確認卵巢真的被壓住。真正需要查交互作用的，多半是一起開的標靶藥。

### 4.1 Tamoxifen 是 prodrug

- **代謝路徑**：tamoxifen 本身活性弱。CYP3A4 先把它去甲基成 N-desmethyltamoxifen（占代謝的九成以上），CYP2D6 再把它氧化成 endoxifen。Endoxifen 與 4-hydroxytamoxifen 的抗雌激素效力約為原型藥的 100 倍（Goetz et al., 2018）。
- **半衰期很長**：tamoxifen 約 5–7 天，N-desmethyltamoxifen 約 14 天，tamoxifen 約 4 週達到穩定濃度。停藥後藥物還會留在體內，仿單的病人須知寫大約 2 個月才清除，所以要求停藥後 2 個月內不可懷孕（Bryant Ranch Prepack, 2026）。
- **強效 CYP2D6 抑制劑會壓低 endoxifen，療效可能打折**：加拿大安大略的世代研究納入 2,430 位 66 歲以上、同時使用 tamoxifen 與一種 SSRI 的女性。Tamoxifen 用藥期間與 paroxetine 重疊的比例每增加 25%、50%、75%，乳癌死亡風險分別增加 24%、54%、91%；其他抗憂鬱藥沒有這個現象（Kelly et al., 2010）。這是觀察性研究，看到的是相關；ASCO 也說這類交互作用影響乳癌結果的證據有限而間接，但仍建議小心（Burstein et al., 2010）。

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

**為什麼要在第 15 天多打一次？** 肌肉注射後的半衰期約 40 天；仿單寫明，第一劑後兩週多打的這一劑，讓血中濃度在第一個月內就達到穩定（AstraZeneca, 2020）。CONFIRM 試驗把「500 mg 加第 14 天的負荷劑量」與原本核准的每月 250 mg 相比，無惡化存活較好（HR 0.80，0.68–0.94），毒性沒有增加（Di Leo et al., 2010）。

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
- **aTTom**：設計相同的另一個試驗，6,953 人，繼續吃到 10 年的復發 580 例，停藥組 672 例；子宮內膜癌 102 例（2.9%）對 45 例（1.3%）。ASCO 指引引用的是這個試驗 2013 年的會議摘要，以上數字取自指引的整理（Burstein et al., 2014）。
- **MA.17**：5,187 位吃滿 5 年 tamoxifen 的停經後女性，接著用 letrozole 或安慰劑。第一次期中分析的 4 年無病存活為 93% 對 87%，試驗因此提前解盲（Goss et al., 2003）。
- **AI 之後再延長 AI**：12 項試驗、22,031 人的整合分析顯示，延長 AI 讓復發減少 27%（RR 0.73）。已用過 AI 的人再吃 5 年，第 5–15 年的復發風險為 11.6% 對 15.2%，但乳癌死亡的差異未達顯著（RR 0.90，0.70–1.15）；絕對好處在淋巴結陽性（16.3% 對 20.1%）大於陰性（9.1% 對 11.8%）；5 年骨折風險增加（RR 1.35）；約 39% 的人沒有照分派服藥（Early Breast Cancer Trialists' Collaborative Group, 2025）。
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
| 惡化時 | 驗血中 ctDNA 的 ESR1；確認 PIK3CA、AKT1、PTEN 與 germline BRCA 的結果 | ASCO 建議在內分泌治療（含或不含 CDK4/6 抑制劑）復發或惡化時常規驗 ESR1，優先用血液 ctDNA（Burstein et al., 2023；指引全文未能開啟，措辭取自 ASCO Post 報導的摘要，見 7.4 的待核對框） |
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

## 7. 抗藥性與下一代藥物

**結論：** 轉移性乳癌用內分泌治療，遲早會遇到抗藥。先排除「假性抗藥」（沒吃、停經狀態判斷錯、交互作用），再想腫瘤的三條逃生路線：受體自己卡在「開」（ESR1 突變）、繞過受體（PI3K、AKT 等旁路）、乾脆不要受體（ER 消失）。每條路對應不同的下一步，所以惡化時要重新驗 biomarker。

### 7.1 先排除假性抗藥

1. **沒吃或吃不夠**（見 [6.10](#610-遵從性最大的毒性是沒有吃)）。
2. **卵巢沒有被壓住**：停經前單用 AI，或 AI 加 OFS 但 estradiol 沒有降下來（見 [4.4](#44-gnrh-agonistflare-與確認卵巢真的被壓住)）。
3. **Tamoxifen 加 CYP2D6 抑制劑**（見 [4.1](#41-tamoxifen-是-prodrug)）。
4. **併用藥被誘導劑拉低濃度**：rifampin、phenytoin、carbamazepine、St. John's wort（見 [4.5](#45-一起開的標靶藥才是交互作用的重點)）。

### 7.2 三條逃生路線

| 機轉 | 多常見 | 發生什麼事 | 怎麼驗 | 下一步 |
|------|-------|-----------|-------|-------|
| **ESR1 ligand-binding domain 突變** | 原發腫瘤 1.8%，轉移性 16.3%；在轉移階段才接觸 AI 的病人 36.4%，只在輔助階段用過 AI 的 5.8% | Y537S、D538G 等突變讓 helix 12 固定在活化的位置，沒有雌激素也持續啟動轉錄；AI 失效，tamoxifen 與 fulvestrant 的效力下降 | 血液 ctDNA | 口服 SERD、PROTAC 降解劑，或含 fulvestrant 的組合 |
| **生長因子旁路** | PIK3CA 突變約四成（原發 43.7%、轉移 38.1%）；AKT1 約 6%；PTEN 約 9%；FGFR1 擴增在轉移性約 15%；NF1 與 ERBB2 的變異在轉移性各約 6–7% | PI3K／mTOR 與 MAPK 路徑不靠雌激素就能重新啟動 ER，或直接推動細胞分裂 | 組織或血液的基因檢測，依各藥仿單 | fulvestrant 加 PI3K 或 AKT 抑制劑（見 [5.3](#53-轉移性-hrher2)） |
| **ER 表現消失** | 內分泌抗藥腫瘤的約 10% | 腫瘤不再依賴 ER | 轉移病灶重新切片驗 ER | 不再用內分泌治療，依新的亞型選藥 |

（出處：Hanker et al., 2020；Schiavon et al., 2015；Toy et al., 2013。）

三個要點：

- **ESR1 突變是「後天」的。** 2013 年的研究在接受過內分泌治療的轉移性腫瘤找到這些突變，突變的受體在沒有荷爾蒙時仍驅動轉錄與增生，並降低 ER 拮抗劑的效果（Toy et al., 2013）。在輔助 AI 治療後惡化的 32 個腫瘤切片中，一個突變也沒有找到；在一位連續採血的病人身上，可以看到突變株在轉移性 AI 治療期間變成主要的細胞株（Schiavon et al., 2015）。所以用診斷時的舊檢體驗 ESR1 沒有意義。
- **ESR1 突變的腫瘤，fulvestrant 比 AI 好，但不夠好。** SoFEA 試驗的血漿分析中，39.1% 的病人有 ESR1 突變；有突變者用 fulvestrant 的無惡化存活優於 exemestane（HR 0.52，0.30–0.92），沒有突變者兩者相同。PALOMA-3 中 25.3% 有突變，fulvestrant 加 palbociclib 不論有無突變都有效（Fribbens et al., 2016）。
- **PIK3CA 突變不是抗藥後才出現的。** 它在原發與轉移腫瘤的比例相近（Hanker et al., 2020），可以在轉移診斷時就驗；它是「可以打的標靶」，不是抗藥的證據。RB1 等細胞週期基因的變異則主要與 CDK4/6 抑制劑的抗藥有關（Hanker et al., 2020）。

> [!TIP]
> **門被鎖上之後，腫瘤的三種逃法**
> 內分泌治療把大樓的正門（ER）鎖上。腫瘤有三種逃法：把門鎖焊死在「開」的位置（ESR1 突變）；改走側門與窗戶（PI3K、MAPK 旁路）；把整道門拆掉，從此不需要門（ER 消失）。對策跟著不同：焊死的鎖要整組拆掉（SERD、PROTAC）；側門要另外派人守（PI3K、AKT、CDK4/6 抑制劑）；門都拆了，就不必再守門，改用化療或抗體藥物複合體。

### 7.3 下一代藥物：證據與限制

| 藥與試驗 | 對象與對照 | ESR1 突變族群的無惡化存活 | 全體族群 |
|---------|-----------|------------------------|---------|
| **elacestrant**，EMERALD | 478 位，內分泌治療加 CDK4/6 抑制劑後；對照為 fulvestrant 或 AI | 3.8 對 1.9 個月（HR 0.55，0.39–0.77）；整體存活 HR 0.90（0.63–1.30），無差異。事後分析：前一線 CDK4/6 抑制劑用了 ≥12 個月者 8.6 對 1.9 個月（HR 0.41） | 美國只核准 ESR1 突變（US Food and Drug Administration, 2023；Stemline Therapeutics, 2026；Bardia et al., 2024） |
| **imlunestrant**，EMBER-3 | 874 位，AI（含或不含 CDK4/6 抑制劑）治療中或治療後惡化；對照為標準內分泌單藥 | 5.5 對 3.8 個月（仿單 HR 0.62，0.46–0.82） | 5.6 對 5.5 個月（HR 0.87，0.72–1.04），未達顯著。imlunestrant 加 abemaciclib 對 imlunestrant 單用：9.4 對 5.5 個月（HR 0.57，0.44–0.73），不論 ESR1 狀態；但美國仿單的併用適應症仍限 ESR1 突變（Jhaveri et al., 2025；Eli Lilly and Company, 2026） |
| **vepdegestrant**，VERITAC-2 | 624 位，曾用過一線 CDK4/6 抑制劑加內分泌治療；對照為 fulvestrant | 5.0 對 2.1 個月（HR 0.58，0.43–0.78；美國仿單的分析為 HR 0.57，0.42–0.77） | 3.8 對 3.6 個月（HR 0.83，0.69–1.01），未達顯著（Campone et al., 2025；Arvinas Operations, 2026） |
| **camizestrant**，SERENA-6 | 一線 AI 加 CDK4/6 抑制劑期間 ctDNA 出現 ESR1 突變、影像尚未惡化的 315 位；把 AI 換成 camizestrant 或維持原治療 | 16.0 對 9.2 個月（HR 0.44，0.31–0.60） | 不適用，全部都是 ESR1 突變（Bidard et al., 2025） |

> [!IMPORTANT]
> **口服 SERD 與 PROTAC 的考點**
> - 單用時，好處**只出現在 ESR1 突變的病人**；EMBER-3 與 VERITAC-2 的全體族群都沒有達到統計顯著。開藥前一定要有 ESR1 突變的檢測報告。
> - ESR1 突變族群的對照組（fulvestrant 或 AI 單用）無惡化存活只有 2–4 個月：CDK4/6 抑制劑之後，舊的內分泌單藥效果很有限。
> - 到目前為止沒有一個證明延長整體存活：elacestrant 的整體存活無差異；imlunestrant、vepdegestrant 與 camizestrant 的仿單都寫存活資料尚未成熟（Eli Lilly and Company, 2026；Arvinas Operations, 2026；AstraZeneca, 2026）。
> - 新藥各有特殊毒性：elacestrant 看血脂，camizestrant 與 vepdegestrant 看心電圖（見 [3.4](#34-serd-與-protac-降解劑)）。

**合併治療是另一條路。** 與其只換一個更強的 ER 藥，不如同時守住旁路：imlunestrant 加 abemaciclib（EMBER-3）、camizestrant 加原本的 CDK4/6 抑制劑（SERENA-6）、fulvestrant 加 PI3K 或 AKT 抑制劑（SOLAR-1、CAPItello-291），以及第一線就用三種藥的 inavolisib 加 palbociclib 加 fulvestrant（INAVO120）。各試驗的數字與台灣能不能用，見[乳癌章 4.7](../03-breast-cancer.md#47-轉移性-hrher2先排除-visceral-crisis再走內分泌路線)與[標靶藥物](03-targeted-therapy.md)。

### 7.4 用液態切片追 ESR1：惡化才驗，還是邊治療邊驗

**惡化時驗**是目前指引的做法：ASCO 建議在內分泌治療復發或惡化時常規驗 ESR1，優先用血液 ctDNA；結果為野生型的人，下次惡化時可以再驗（Burstein et al., 2023；措辭取自 ASCO Post 報導的摘要）。

**邊治療邊驗**有兩個隨機試驗：

- **PADA-1**（法國，1,017 人）：一線 AI 加 palbociclib 治療期間定期驗血中的 ESR1 突變。279 人（27%）出現上升的突變，其中 172 人在影像還沒惡化時隨機分派：把 AI 換成 fulvestrant（palbociclib 不變），或維持原治療。換藥組的無惡化存活 11.9 個月，維持組 5.7 個月（HR 0.61，0.43–0.86）（Bidard et al., 2022）。
- **SERENA-6**（23 國）：一線 AI 加 CDK4/6 抑制劑至少 6 個月後，每 2–3 個月驗一次 ctDNA。3,256 人受檢，548 人驗出 ESR1 突變（Turner et al., 2026），315 人隨機分派。把 AI 換成 camizestrant 的無惡化存活 16.0 對 9.2 個月（HR 0.44）；生活品質開始惡化的時間 21.0 對 6.4 個月（HR 0.54，0.34–0.84）（Bidard et al., 2025）。延伸分析中，第二次無惡化存活也達到統計顯著（Turner et al., 2026）。美國仿單因此建議每 3 個月驗一次 ctDNA，直到出現 ESR1 突變；但整體存活資料尚未成熟，核准屬於加速核准（AstraZeneca, 2026）。

**怎麼對病人解釋：** 這兩個試驗證明「看到突變就提早換藥」可以把疾病穩定的時間拉長，還沒有證明這樣做能活得更久。每 2–3 個月抽一次 ctDNA 也有費用與可近性的問題。

> [!CAUTION]
> **待核對：台灣的 ESR1 ctDNA 檢測與新藥可近性**
> 乳癌章依 TFDA 2026-10-27 資料與健保 115/10/22 版整理：imlunestrant 有藥證但無健保給付，elacestrant、camizestrant、vepdegestrant 沒有藥證（見[乳癌章 4.12](../03-breast-cancer.md#412-新藥與常用藥在台灣的藥證與健保狀態)）。ESR1 ctDNA 檢測在台灣是否有健保給付、院內用哪一種檢測平台，本章沒有查到資料，請向院內分子病理與個案管理師確認。另外，ASCO 2023 年 ESR1 檢測快速更新的全文無法開啟（PubMed 沒有摘要），本章對它的描述來自 ASCO Post 報導的摘要，引用前請對照原文（Burstein et al., 2023）。

---

## 8. 專師實務

**結論：** 這類藥的風險不在給藥當天，而在接下來的好幾年。專師的價值在三件事：開藥前把停經狀態、懷孕與藥單確認清楚；追蹤時把副作用問出來並處理；每一次都確認病人還在吃。

### 8.1 開藥前檢核

| 項目 | 要確認什麼 | 為什麼 |
|------|-----------|-------|
| 病理 | ER、PR、HER2 報告；轉移性疾病是否重新切片 | ER 陰性無效；轉移後 ER 可能改變（見 7.2） |
| 停經狀態 | 年齡、最後一次月經、是否做過卵巢或子宮切除、是否剛做完化療、是否正在用 tamoxifen 或 GnRH agonist；有疑問抽 FSH 與 estradiol | 決定能不能用 AI；化療後無月經不等於停經（見 [5.1](#51-開藥前先確定兩件事er-與停經狀態)） |
| 懷孕與避孕 | 有生育可能者驗孕；確認非荷爾蒙避孕方式；問未來的生育計畫 | 這些藥可傷害胎兒；tamoxifen 與 GnRH agonist 都不保證避孕（見 [6.8](#68-生育避孕與懷孕)） |
| 藥單 | CYP2D6 抑制劑、warfarin、rifampin、抗癲癇藥、含雌激素的製劑、St. John's wort 等草藥、其他延長 QT 的藥 | 見 [4.5](#45-一起開的標靶藥才是交互作用的重點) 的對照表 |
| 血栓與中風病史 | 深部靜脈栓塞、肺栓塞、中風；是否正在使用抗凝血藥 | tamoxifen、raloxifene、megestrol 的血栓風險（見 [6.2](#62-靜脈血栓與中風)） |
| 婦科 | 子宮是否還在、有無異常出血、上次婦科檢查的時間 | tamoxifen 的子宮內膜風險（見 [6.3](#63-子宮內膜增生息肉與癌)） |
| 骨骼 | 骨折史、骨質疏鬆危險因子、25-OH vitamin D；骨折風險明顯者做骨密度 | AI 與 OFS 造成骨質流失（見 [6.5](#65-骨質流失與骨折)） |
| 心血管與血脂 | 血壓、血脂基線、缺血性心臟病史 | AI 與 elacestrant 影響血脂 |
| 肝功能 | AST、ALT、膽紅素；是否有肝硬化 | letrozole、fulvestrant、elacestrant、imlunestrant 在肝功能不全時要調整劑量 |
| 心電圖與電解質 | 要開 toremifene、camizestrant、vepdegestrant 或 ribociclib 時 | QT 延長 |
| 注射前（fulvestrant） | 抗凝血藥、血小板數 | 肌肉注射的出血風險 |
| 給付 | 適應症、線別、事前審查文件 | 見[乳癌章第 9 段](../03-breast-cancer.md#9-健保給付與事前審查) |

### 8.2 追蹤時程

| 時間 | 要做的事 |
|------|---------|
| **每次回診** | 問服藥情形（漏幾天、有沒有自己停）；問熱潮紅、關節痛、陰道乾澀、情緒與睡眠、性生活；停經前病人問月經與出血；問小腿腫痛、喘、胸痛、神經學症狀 |
| **tamoxifen** | 每年婦科檢查，異常出血隨時轉診；定期全血球計數與肝功能；視力改變轉眼科；每次核對新加的藥有沒有 CYP2D6 抑制劑 |
| **AI** | 骨密度追蹤；血脂追蹤；鈣與維生素 D 的攝取；關節症狀影響生活時，照 [6.4](#64-ai-相關的關節肌肉症狀) 的順序處理 |
| **GnRH agonist** | 核對每一針的日期；第一劑後頭幾週注意 flare；併用 AI 者留意卵巢是否壓住 |
| **fulvestrant** | 第 1、15、29 天與之後每月的注射；注射部位、坐骨神經症狀 |
| **口服 SERD、PROTAC** | elacestrant：治療前與治療中驗血脂。camizestrant：治療前與前 2 週每週做 ECG。vepdegestrant：治療前與約 4 週後做 ECG、驗電解質 |
| **轉移性疾病** | 依院內時程做影像評估（見[乳癌章 7.6](../03-breast-cancer.md#76-療效評估與追蹤)）；惡化時抽 ctDNA 驗 ESR1，並確認其他 biomarker 是否驗過 |

> [!NOTE]
> **骨密度多久追蹤一次、多久驗一次肝功能，依院內流程**
> 仿單只寫「定期」監測，ASCO 骨質疏鬆指引的摘要也沒有給固定間隔（Shapiro et al., 2019）。乳癌章 7.8 已把「重複 DXA 的間隔」列為待核對。實習時請找到院內乳癌團隊的追蹤表，照表安排。

### 8.3 衛教怎麼說

下面是可以直接拿來用的說法，請依病人的情況調整。

- **為什麼要吃這麼久**：「這個藥不是在治療看得到的腫瘤，而是在餓死可能躲在身體裡、還看不到的癌細胞。它們長得很慢，所以藥要吃很多年。研究顯示吃滿 5 年的人，之後 15 年的乳癌死亡率少了大約三分之一。」（EBCTCG, 2011）
- **Tamoxifen 與避孕、出血**：「這個藥不能避孕，吃的時候懷孕會傷到寶寶，所以要用保險套或其他不含荷爾蒙的方法。停經後如果有任何陰道出血，或是月經變得很不規則、下腹悶痛，不要等下次回診，請先打電話給我們。」
- **Tamoxifen 與其他藥**：「有些抗憂鬱藥、戒菸藥和口服的灰指甲藥會讓這個藥失效。以後不管哪一科開新的藥，都請先給我們或藥師看過。」
- **AI 的關節痛**：「最多大約一半的人吃這類藥會關節僵硬或痠痛，不少人在頭半年就因此想停藥。這不代表癌症轉移到骨頭。規律運動在臨床試驗中證明可以減輕疼痛；如果還是很不舒服，我們可以換另一個同類的藥，或加上止痛的方法。請不要自己停藥，先跟我們說。」
- **打停經針加 AI**：「停經針要按時打，拖太久卵巢可能恢復功能，口服藥就會失效。如果月經又來了，或原本的熱潮紅突然完全消失，請告訴我們。月經停了也還是可能懷孕，要繼續避孕。」
- **忘記吃藥**：依各藥仿單與院內衛教單回答；原則是不要一次補吃兩倍的劑量。口服抗癌藥的通用衛教見[化療基礎 14.5](../00-shared/01-chemo-basics.md#145-口服抗癌藥)。

### 8.4 遵從性支持

1. **每次都問，而且不帶責備。** 問「上個月大概漏了幾天」，不要問「你有沒有按時吃」。
2. **把副作用當成停藥的前兆來處理。** 熱潮紅、關節痛、陰道乾澀、情緒低落，都有可以做的事（[第 6 段](#6-毒性與處置)）。因副作用停掉第一個 AI 的人，換另一個 AI 後有近四成能繼續吃（Henry et al., 2012）。
3. **特別留意年輕病人。** 40 歲以下的女性停藥風險最高（Hershman et al., 2010），她們同時面對生育、提早停經與工作家庭的壓力。想懷孕的人要主動談 POSITIVE 試驗的做法，不要讓她自己默默停藥。
4. **讓吃藥變簡單。** 固定在每天同一個時間吃、用藥盒或手機提醒、把回診與領藥日期對齊。
5. **把團隊拉進來。** 藥師查交互作用，個案管理師追蹤回診與領藥，復健或運動團隊協助關節症狀，婦產科處理出血與陰道症狀，必要時轉介身心科。
6. **在病歷上留下紀錄。** 遵從性、副作用與處置寫進每次的 progress note，下一位照顧者才接得上。

---

## 9. 藥物卡

<!-- drug-cards -->
| 藥名 | 分類 | 機轉 | 主要用途 | 必記毒性 | 監測與處置 |
|------|------|------|----------|----------|------------|
| tamoxifen | SERM | 佔住 ER；乳房拮抗、子宮內膜部分促效；prodrug，靠 CYP2D6 活化 | 停經前後與男性的 ER 陽性乳癌；DCIS；風險降低 | 熱潮紅、VTE 與中風、子宮內膜癌、白內障；可傷害胎兒 | 避開 paroxetine、fluoxetine；異常出血轉婦科；非荷爾蒙避孕 |
| toremifene (Fareston) | SERM | 結構近似 tamoxifen 的 ER 調節劑 | 停經後 ER 陽性或不明的轉移性乳癌（美國仿單） | QT 延長（加框警語）、高血鈣與腫瘤 flare | 矯正低血鉀與低血鎂；避免延長 QT 的藥與強效 CYP3A4 抑制劑 |
| raloxifene (Evista) | SERM | 乳房拮抗，不刺激子宮內膜 | 停經後骨質疏鬆；降低停經後高風險女性的侵襲性乳癌風險 | VTE、中風死亡（加框警語） | 不能用來治療乳癌；有 VTE 病史者不用；停經前不用 |
| letrozole (Femara) | 非類固醇 AI | 競爭性抑制 aromatase，雌激素降 75–95% | 停經後輔助、延長輔助與晚期乳癌；停經前須加 OFS | 關節痛、骨質流失與骨折、高膽固醇 | 評估骨折風險與骨密度；追蹤血脂；肝硬化減為隔天一次 |
| anastrozole (Arimidex) | 非類固醇 AI | 選擇性抑制 aromatase，estradiol 降約 80% | 停經後輔助與晚期乳癌；DCIS 與預防有試驗證據 | 關節痛、骨折、膽固醇上升；缺血性心臟病者事件較多 | 不與 tamoxifen 或含雌激素製劑併用；追蹤骨密度與血脂 |
| exemestane (Aromasin) | 類固醇 AI | 不可逆的自殺性抑制，全身 aromatization 降 98% | 停經後 tamoxifen 2–3 年後接續、晚期乳癌；停經前須加 OFS | 關節痛、熱潮紅、骨質流失 | 餐後服用；先驗 25-OH vitamin D；併強效 CYP3A4 誘導劑時 50 mg |
| goserelin (Zoladex) | GnRH agonist | 持續刺激使腦下垂體受體 downregulation，性腺停工 | 停經前乳癌的卵巢功能抑制；攝護腺癌去勢 | flare、提早停經的症狀、骨質流失；骨轉移者可有高血鈣 | 3.6 mg 皮下每 28 天，按時注射；非荷爾蒙避孕 |
| leuprolide | GnRH agonist | 同 goserelin | 攝護腺癌去勢；同類藥也用於停經前乳癌的卵巢抑制 | flare、熱潮紅、骨質疏鬆 | 攝護腺癌可先併用 antiandrogen 擋 flare；按時注射 |
| triptorelin | GnRH agonist | 同 goserelin | SOFT 與 TEXT 使用的卵巢抑制藥；攝護腺癌去勢 | 更年期症狀、性功能障礙、骨質流失 | 併 exemestane 時約兩成壓不完全；月經恢復要回報 |
| fulvestrant (Faslodex) | SERD（注射） | 拮抗 ER 並使 ER 蛋白減少，沒有促效作用 | HR 陽性晚期乳癌：停經後單用，或併 CDK4/6 抑制劑 | 注射部位疼痛、噁心、骨痛；出血與坐骨神經風險 | 500 mg IM 第 1、15、29 天後每月；干擾 estradiol 檢驗 |
| elacestrant (Orserdu) | 口服 SERD | 拮抗並降解 ER | ESR1 突變的 ER 陽性、HER2 陰性晚期乳癌（美國） | 噁心、高膽固醇、高三酸甘油酯 | 345 mg 隨餐；治療前後驗血脂；避免 CYP3A4 抑制劑與誘導劑 |
| imlunestrant (Inluriyo) | 口服 SERD | 拮抗並降解 ER | ESR1 突變晚期乳癌，單用或併 abemaciclib（美國） | 血紅素下降、肌肉骨骼疼痛、疲倦、腹瀉 | 400 mg 空腹；併強效 CYP3A 抑制劑或誘導劑時調整劑量 |
| camizestrant (Etcamah) | 口服 SERD | 拮抗並降解 ER | 一線治療中驗出 ESR1 突變時取代 AI，併 CDK4/6 抑制劑（美國加速核准） | 心搏過緩、QTc 延長、視覺異常；併 ribociclib 有加框警語 | 治療前與前 2 週每週 ECG；每 3 個月驗 ctDNA 直到出現突變 |
| vepdegestrant (Veppanu) | PROTAC 降解劑 | 同時結合 ER 與 cereblon，使 ER 泛素化後被 proteasome 分解 | ESR1 突變晚期乳癌（美國） | QTc 延長 | 200 mg 隨餐；治療前與約 4 週後 ECG；QTc >470 ms 不開始 |
| megestrol | progestin | 確切抗腫瘤機轉不明；仿單提到抑制促性腺激素與直接作用於腫瘤細胞 | 晚期乳癌或子宮內膜癌的緩和治療；惡病質的食慾促進 | 血栓、腎上腺抑制、糖尿病惡化、體重增加 | 停藥或遇壓力時想到腎上腺功能不全 |
| abiraterone | 雄性素合成抑制劑 | 抑制 CYP17，阻斷睪丸、腎上腺與腫瘤內的雄性素合成 | 攝護腺癌，須併用 prednisone | 高血壓、低血鉀、水腫、肝功能異常 | 追蹤血壓、血鉀、肝功能；是中效 CYP2D6 抑制劑 |
| enzalutamide | AR 抑制劑 | 結合 AR，阻止它進入細胞核與結合 DNA | 攝護腺癌 | 疲倦、腹瀉、熱潮紅、癲癇（0.6%） | 是強效 CYP3A 誘導劑，併用藥要查交互作用 |

---

## 10. 自我測驗

**Q1.** 44 歲女性，月經規則，ER 陽性、HER2 陰性乳癌術後，準備開始輔助內分泌治療。不論她的復發風險高低，下列哪一個處方都**不適當**？

A. tamoxifen 20 mg 每天一次　B. letrozole 2.5 mg 每天一次，單獨使用　C. goserelin 加 tamoxifen　D. goserelin 加 exemestane

<details>
<summary>答案與詳解</summary>

**答案：B**。停經前的雌激素主要來自卵巢，AI 只能抑制周邊的 aromatase，單用無效，ASCO 寫明 AI 禁用於仍有卵巢功能的病人（Burstein et al., 2010）。A 是低風險者的標準選擇；C 與 D 是高風險者（一般會建議化療的 stage II–III）加上卵巢抑制的做法，不需要化療的 stage I 則不應加（Burstein et al., 2016）。只有 B 在任何風險層級都不成立（見 2.1、5.2）。

</details>

**Q2.** 48 歲女性完成輔助化療後已經 8 個月沒有月經。主治醫師想開 anastrozole。專師最應該提出哪一件事？

A. 無月經超過 6 個月即可視為停經，直接開藥　B. 只要驗孕陰性就可以開 AI　C. 化療後無月經不等於停經，應抽 FSH 與 estradiol，並討論先用 tamoxifen 或加上卵巢抑制　D. 改開 fulvestrant 就不需要考慮停經狀態

<details>
<summary>答案與詳解</summary>

**答案：C**。化療後無月經而開始 AI 的 45 位女性中，27% 的卵巢功能恢復（Smith et al., 2006）。化療或 tamoxifen 造成的無月經不可靠，卵巢功能可能在之後恢復，所以即使抽血在停經後範圍也要持續留意。Fulvestrant 的適應症同樣以停經後為主，而且它會讓 estradiol 檢驗假性偏高（見 4.3、4.4、5.1）。

</details>

**Q3.** 52 歲女性服用 tamoxifen，因憂鬱與熱潮紅想加藥。下列哪一個藥**最不適合**？

A. paroxetine　B. venlafaxine　C. gabapentin　D. 認知行為治療

<details>
<summary>答案與詳解</summary>

**答案：A**。Tamoxifen 是 prodrug，要靠 CYP2D6 變成 endoxifen。Paroxetine 是強效 CYP2D6 抑制劑；世代研究中，與 paroxetine 重疊使用的時間越長，乳癌死亡風險越高（Kelly et al., 2010）。Venlafaxine、gabapentin 與認知行為治療都是有證據的非荷爾蒙選擇（見 4.1、6.1）。

</details>

**Q4.** 63 歲女性服用 tamoxifen 第 3 年，回診時提到上週有兩天陰道出血。最適當的處置是？

A. 停經後偶爾出血是 tamoxifen 的正常現象，繼續觀察　B. 排明年的例行婦科檢查時再一起看　C. 先停 tamoxifen 一個月看出血會不會停　D. 儘快轉介婦科評估子宮內膜

<details>
<summary>答案與詳解</summary>

**答案：D**。Tamoxifen 在子宮內膜有部分促效作用，子宮內膜癌的風險增加，而且集中在 50 歲以上（Fisher et al., 1998）。沒有症狀的人不需要常規做內膜監測，但**任何異常陰道出血都要立刻評估**（American College of Obstetricians and Gynecologists, 2014）（見 6.3）。

</details>

**Q5.** 關於 fulvestrant 的給藥，下列何者正確？

A. 250 mg 皮下注射，每週一次　B. 500 mg 肌肉注射，第 1、15、29 天各一次，之後每月一次　C. 500 mg 口服，每天一次，隨餐　D. 500 mg 靜脈輸注，每 3 週一次

<details>
<summary>答案與詳解</summary>

**答案：B**。Fulvestrant 是長效肌肉注射劑，半衰期約 40 天，所以需要第 15 天的負荷劑量；每次分兩支、左右臀各一支，每支慢慢推 1–2 分鐘。CONFIRM 試驗證明這個給法優於原本的每月 250 mg（Di Leo et al., 2010）（見 4.3）。

</details>

**Q6.** 58 歲停經後女性服用 letrozole 6 個月，雙手晨間僵硬、膝蓋痠痛，說「我想乾脆不要吃了」。下列哪一項做法最適當？

A. 關節痛代表骨轉移，先安排全身骨掃描　B. 請她忍耐，副作用會自己消失　C. 說明這是 AI 常見的副作用，安排規律運動；無效時換另一個 AI，或加上 duloxetine、針灸　D. 立刻永久停止所有內分泌治療

<details>
<summary>答案與詳解</summary>

**答案：C**。關節肌肉症狀是 AI 最常見的停藥原因。運動、換另一個 AI、duloxetine 與針灸都有前瞻性或隨機試驗的證據（Irwin et al., 2015；Henry et al., 2012；Henry et al., 2018；Hershman et al., 2018）。重點是在病人自己停藥之前先介入（見 6.4）。

</details>

**Q7.** 38 歲停經前女性，ER 陽性乳癌合併多處骨轉移，打了第一劑 goserelin 後第 10 天骨痛加重，血鈣上升。最合理的解釋與處置是？

A. GnRH agonist 的 flare；先處理高血鈣與疼痛，暫時不判定為治療失敗　B. 確定是疾病惡化，立刻改成化療　C. 藥物過敏，永久停用 goserelin　D. 卵巢已被完全抑制所造成的骨質流失

<details>
<summary>答案與詳解</summary>

**答案：A**。GnRH agonist 一開始會讓 LH、FSH 與 estradiol 短暫上升，estradiol 約 3 週才降到停經後範圍；仿單記載最初幾週腫瘤症狀與骨痛可能暫時加重，骨轉移病人可出現高血鈣（TerSera, 2026）。高血鈣照急症流程處理（見 1.6、4.4）。

</details>

**Q8.** 關於 ESR1 突變，下列敘述何者正確？

A. 多數在診斷時的原發腫瘤就存在，用舊的手術檢體檢測即可　B. 突變會讓腫瘤完全失去 ER 表現　C. 有 ESR1 突變的腫瘤對 AI 特別敏感　D. 多在轉移性疾病接受 AI 治療後出現，建議在惡化時用血液 ctDNA 檢測

<details>
<summary>答案與詳解</summary>

**答案：D**。ESR1 突變在原發腫瘤只有 1.8%，轉移性腫瘤 16.3%（Hanker et al., 2020）；輔助 AI 後惡化的切片中幾乎找不到（Schiavon et al., 2015）。突變讓受體不靠雌激素就持續活化，所以 AI 失效；它不是讓 ER 消失（那是另一種機轉）。ASCO 建議惡化時以 ctDNA 檢測（見 7.2、7.4）。

</details>

**Q9.** ATLAS 試驗比較 tamoxifen 吃 10 年與 5 年。下列對結果的描述何者正確？

A. 吃 10 年對復發與死亡都沒有幫助　B. 吃 10 年進一步降低復發與乳癌死亡，好處主要在第 10 年以後才明顯，代價是子宮內膜癌與肺栓塞增加　C. 吃 10 年的好處在前 2 年最明顯，之後消失　D. 吃 10 年會增加對側乳癌

<details>
<summary>答案與詳解</summary>

**答案：B**。ER 陽性病人繼續吃到 10 年，乳癌死亡 331 對 397 人；復發 RR 在第 5–9 年為 0.90，之後為 0.75。子宮內膜癌 RR 1.74，肺栓塞 RR 1.87（Davies et al., 2013）。所以延長治療要依復發風險與副作用，和病人共同決定（見 5.2）。

</details>

**Q10.** 31 歲女性開始服用 tamoxifen，詢問避孕方式。下列衛教何者正確？

A. Tamoxifen 是荷爾蒙藥，本身就有避孕效果　B. 建議改用口服避孕藥最可靠　C. 使用保險套等屏障或其他非荷爾蒙避孕；依美國仿單，停藥後 2 個月內也不可懷孕　D. 月經不規則就代表不會懷孕

<details>
<summary>答案與詳解</summary>

**答案：C**。Tamoxifen 可造成胎兒傷害，而且它不能避孕，當年正是因為在女性身上會誘發排卵才當不成避孕藥。仿單要求屏障或非荷爾蒙避孕（Bryant Ranch Prepack, 2026）。想懷孕的病人可以討論 POSITIVE 試驗的做法：治療 18–30 個月後暫停，先有 3 個月洗脫期（Partridge et al., 2023）（見 1.4、6.8）。

</details>

**Q11.** Tamoxifen 的下列哪一個不良反應，是它在該組織的「雌激素樣（促效）作用」造成的？

A. 子宮內膜增生與子宮內膜癌　B. 停經後女性的骨質疏鬆性骨折　C. 乳癌細胞增生　D. 陰道極度乾澀

<details>
<summary>答案與詳解</summary>

**答案：A**。在乳腺細胞，tamoxifen 讓 ER 召集 corepressor；在子宮內膜細胞，它像雌激素一樣召集 coactivator（Shang & Brown, 2002）。所以它在乳房是拮抗劑，在子宮內膜是部分促效劑。停經後骨質流失與陰道乾澀是 AI 這類「雌激素缺乏」的毒性（見 2.4）。

</details>

**Q12.** 依 SOFT、TEXT 與 ASCO 指引，下列哪一位病人最應該在內分泌治療中加上卵巢功能抑制？

A. 49 歲，stage I，腫瘤 0.8 cm，淋巴結陰性，不需化療　B. 62 歲，停經 10 年，stage II　C. 46 歲，DCIS 術後　D. 33 歲，淋巴結陽性，化療後月經恢復

<details>
<summary>答案與詳解</summary>

**答案：D**。ASCO 建議風險高到需要化療的 stage II–III 停經前病人加上卵巢抑制；不需化療的 stage I 與 ≤1 cm 的淋巴結陰性腫瘤不應加（Burstein et al., 2016）。SOFT 與 TEXT 的 15 年結果顯示，存活的好處集中在年輕、高風險的病人（Francis et al., 2026）。B 已經停經，C 是原位癌（見 5.2）。

</details>

**Q13.** 60 歲女性即將開始 5 年的 anastrozole。關於骨骼健康，下列哪一項做法符合指引？

A. 所有人一律每 3–4 週注射 zoledronic acid 4 mg　B. 評估骨折風險，風險明顯者做骨密度；鼓勵運動與足夠的鈣和維生素 D，需要用藥時以骨質疏鬆劑量的 bisphosphonate 或 denosumab 為主　C. 等到發生骨折再處理　D. 為了避免骨質流失，所有停經後病人都改用 tamoxifen

<details>
<summary>答案與詳解</summary>

**答案：B**。這是 ASCO 骨質疏鬆指引的做法（Shapiro et al., 2019）。AI 的 5 年骨折風險 8.2%，tamoxifen 5.5%（EBCTCG, 2015）；ABCSG-18 中 denosumab 60 mg 每 6 個月讓臨床骨折減半（Gnant et al., 2015）。Zoledronic acid 4 mg 每 3–4 週是骨轉移的給法，不是預防骨質疏鬆的劑量（見 6.5 與乳癌章 7.8）。

</details>

**Q14.** 一線 letrozole 加 ribociclib 治療 14 個月的病人，ctDNA 驗出 ESR1 突變，影像穩定。主治醫師考慮依 SERENA-6 把 letrozole 換成 camizestrant。專師最應該提醒哪一件事？

A. Camizestrant 必須肌肉注射　B. 換藥後不需要做心電圖　C. Camizestrant 與 ribociclib 併用有心律不整的加框警語，要先確認 CDK4/6 抑制劑的選擇與 ECG 監測計畫　D. 應該同時把 tamoxifen 加回來

<details>
<summary>答案與詳解</summary>

**答案：C**。美國仿單的加框警語指出，camizestrant 與 ribociclib 併用可能增加 Torsades de Pointes 與猝死的風險；治療前與前 2 週每週要做 ECG（AstraZeneca, 2026）。另外要記得 SERENA-6 目前只有無惡化存活的好處，整體存活尚未成熟；台灣的藥證狀態見乳癌章 4.12（見 3.4、7.4）。

</details>

**Q15.** 55 歲女性，stage II 乳癌術後服用 exemestane 第 2 年，病歷顯示過去 6 個月只領了 3 個月的藥。下一步最重要的是？

A. 直接判定內分泌抗藥，改用化療　B. 用不帶責備的方式問她漏藥的原因與副作用，處理副作用並協助恢復規律服藥　C. 把劑量加倍來補回漏掉的藥　D. 改成每 3 個月回診一次以減少她的負擔

<details>
<summary>答案與詳解</summary>

**答案：B**。只有約一半的早期乳癌病人照建議吃滿全程（Hershman et al., 2010），提早停藥與吃不夠都與死亡風險上升有關（Hershman et al., 2011）。所以發現領藥紀錄不足時，先處理遵從性與副作用，而不是把它當成抗藥（見 6.10、8.4）。

</details>

---

## 11. 參考文獻

APA 第 7 版。作者超過 20 位時列前 19 位、省略號與最後一位。期刊文獻於 2026-11-11 以 PubMed 核對作者、年份、卷期、頁碼、DOI 與 PMID（線上先行發表與紙本年份不同時採紙本卷期的年份）；PubMed 沒有登錄 DOI 的舊文獻只列 PMID（EBCTCG 1998 的 DOI 另以 doi.org 解析結果與 PubMed 的 PII 相符確認）。美國仿單於同日自 DailyMed 讀取，條目年份為仿單生效或修訂的年份。內文引用仿單時用廠商名稱的簡稱（例如 AstraZeneca、TerSera、Teva Pharmaceuticals、Pharmacia & Upjohn）。

Allison, K. H., Hammond, M. E. H., Dowsett, M., McKernin, S. E., Carey, L. A., Fitzgibbons, P. L., Hayes, D. F., Lakhani, S. R., Chavez-MacGregor, M., Perlmutter, J., Perou, C. M., Regan, M. M., Rimm, D. L., Symmans, W. F., Torlakovic, E. E., Varella, L., Viale, G., Weisberg, T. F., McShane, L. M., & Wolff, A. C. (2020). Estrogen and progesterone receptor testing in breast cancer: ASCO/CAP guideline update. *Journal of Clinical Oncology, 38*(12), 1346–1366. https://doi.org/10.1200/JCO.19.02309（PMID: 31928404）

American College of Obstetricians and Gynecologists. (2014). Committee Opinion No. 601: Tamoxifen and uterine cancer. *Obstetrics & Gynecology, 123*(6), 1394–1397. https://doi.org/10.1097/01.AOG.0000450757.18294.cf（PMID: 24848920）

André, F., Ciruelos, E., Rubovszky, G., Campone, M., Loibl, S., Rugo, H. S., Iwata, H., Conte, P., Mayer, I. A., Kaufman, B., Yamashita, T., Lu, Y.-S., Inoue, K., Takahashi, M., Pápai, Z., Longin, A.-S., Mills, D., Wilke, C., Hirawat, S., & Juric, D. (2019). Alpelisib for PIK3CA-mutated, hormone receptor-positive advanced breast cancer. *New England Journal of Medicine, 380*(20), 1929–1940. https://doi.org/10.1056/NEJMoa1813904（PMID: 31091374）

ANI Pharmaceuticals, Inc. (2026). *ARIMIDEX (anastrozole): Prescribing information* (revised 2025-12; DailyMed version effective 2026-03-02). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=acbfaaa9-503c-4691-9828-76a7146ed6de

Arvinas Operations, Inc. (2026). *VEPPANU (vepdegestrant): Prescribing information* (revised 2026-04; DailyMed version 2, published 2026-05-20). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=751e18d5-1d41-4b67-b1f3-10272ca5312d

AstraZeneca Pharmaceuticals LP. (2020). *FASLODEX (fulvestrant): Prescribing information* (effective 2020-09-25). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=83d7a440-e904-4e36-afb5-cb02b1c919f7

AstraZeneca Pharmaceuticals LP. (2026). *ETCAMAH (camizestrant): Prescribing information* (effective 2026-09-04). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=c54223d3-f3c7-4186-afa0-429d84805826

Bardia, A., Cortés, J., Bidard, F.-C., Neven, P., Garcia-Sáenz, J., Aftimos, P., O'Shaughnessy, J., Lu, J., Tonini, G., Scartoni, S., Paoli, A., Binaschi, M., Wasserman, T., & Kaklamani, V. (2024). Elacestrant in ER+, HER2− metastatic breast cancer with ESR1-mutated tumors: Subgroup analyses from the phase III EMERALD trial by prior duration of endocrine therapy plus CDK4/6 inhibitor and in clinical subgroups. *Clinical Cancer Research, 30*(19), 4299–4309. https://doi.org/10.1158/1078-0432.CCR-24-1073（PMID: 39087959）

Baum, M., Budzar, A. U., Cuzick, J., Forbes, J., Houghton, J. H., Klijn, J. G., Sahmoud, T., & ATAC Trialists' Group. (2002). Anastrozole alone or in combination with tamoxifen versus tamoxifen alone for adjuvant treatment of postmenopausal women with early breast cancer: First results of the ATAC randomised trial. *The Lancet, 359*(9324), 2131–2139. https://doi.org/10.1016/S0140-6736(02)09088-8（PMID: 12090977）

Bellet, M., Gray, K. P., Francis, P. A., Láng, I., Ciruelos, E., Lluch, A., Climent, M. A., Catalán, G., Avella, A., Bohn, U., González-Martin, A., Ferrer, R., Catalán, R., Azaro, A., Rajasekaran, A., Morales, J., Vázquez, J., Fleming, G. F., Price, K. N., & Regan, M. M. (2016). Twelve-month estrogen levels in premenopausal women with hormone receptor–positive breast cancer receiving adjuvant triptorelin plus exemestane or tamoxifen in the Suppression of Ovarian Function Trial (SOFT): The SOFT-EST substudy. *Journal of Clinical Oncology, 34*(14), 1584–1593. https://doi.org/10.1200/JCO.2015.61.2259（PMID: 26729437）

Bidard, F.-C., Hardy-Bessard, A.-C., Dalenc, F., Bachelot, T., Pierga, J.-Y., de la Motte Rouge, T., Sabatier, R., Dubot, C., Frenel, J.-S., Ferrero, J. M., Ladoire, S., Levy, C., Mouret-Reynier, M.-A., Lortholary, A., Grenier, J., Chakiba, C., Stefani, L., Plaza, J. E., Clatot, F., . . . Delaloge, S. (2022). Switch to fulvestrant and palbociclib versus no switch in advanced breast cancer with rising ESR1 mutation during aromatase inhibitor and palbociclib therapy (PADA-1): A randomised, open-label, multicentre, phase 3 trial. *The Lancet Oncology, 23*(11), 1367–1377. https://doi.org/10.1016/S1470-2045(22)00555-1（PMID: 36183733）

Bidard, F.-C., Mayer, E. L., Park, Y. H., Janni, W., Ma, C., Cristofanilli, M., Bianchini, G., Kalinsky, K., Iwata, H., Chia, S., Fasching, P. A., Brufsky, A., Nowecki, Z., Pascual, J., Moreau, L., Chen, S.-C., Karadurmus, N., Gal-Yam, E. N., Jung, K. H., . . . Turner, N. C. (2025). First-line camizestrant for emerging ESR1-mutated advanced breast cancer. *New England Journal of Medicine, 393*(6), 569–580. https://doi.org/10.1056/NEJMoa2502929（PMID: 40454637）

Breast International Group (BIG) 1-98 Collaborative Group. (2005). A comparison of letrozole and tamoxifen in postmenopausal women with early breast cancer. *New England Journal of Medicine, 353*(26), 2747–2757. https://doi.org/10.1056/NEJMoa052258（PMID: 16382061）

Brodie, A. M., Schwarzel, W. C., Shaikh, A. A., & Brodie, H. J. (1977). The effect of an aromatase inhibitor, 4-hydroxy-4-androstene-3,17-dione, on estrogen-dependent processes in reproduction and breast cancer. *Endocrinology, 100*(6), 1684–1695. https://doi.org/10.1210/endo-100-6-1684（PMID: 404132）

Bryant Ranch Prepack. (2026). *Tamoxifen citrate tablets [repackager label]: Prescribing information* (effective 2026-03-19). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=8c0eb763-420a-4106-ba56-526b53a7f72b

Burstein, H. J., DeMichele, A., Somerfield, M. R., & Henry, N. L. (2023). Testing for ESR1 mutations to guide therapy for hormone receptor–positive, human epidermal growth factor receptor 2–negative metastatic breast cancer: ASCO guideline rapid recommendation update. *Journal of Clinical Oncology, 41*(18), 3423–3425. https://doi.org/10.1200/JCO.23.00638（PMID: 37196213）

Burstein, H. J., Lacchetti, C., Anderson, H., Buchholz, T. A., Davidson, N. E., Gelmon, K. E., Giordano, S. H., Hudis, C. A., Solky, A. J., Stearns, V., Winer, E. P., & Griggs, J. J. (2016). Adjuvant endocrine therapy for women with hormone receptor–positive breast cancer: American Society of Clinical Oncology clinical practice guideline update on ovarian suppression. *Journal of Clinical Oncology, 34*(14), 1689–1701. https://doi.org/10.1200/JCO.2015.65.9573（PMID: 26884586）

Burstein, H. J., Lacchetti, C., Anderson, H., Buchholz, T. A., Davidson, N. E., Gelmon, K. A., Giordano, S. H., Hudis, C. A., Solky, A. J., Stearns, V., Winer, E. P., & Griggs, J. J. (2019). Adjuvant endocrine therapy for women with hormone receptor–positive breast cancer: ASCO clinical practice guideline focused update. *Journal of Clinical Oncology, 37*(5), 423–438. https://doi.org/10.1200/JCO.18.01160（PMID: 30452337）

Burstein, H. J., Prestrud, A. A., Seidenfeld, J., Anderson, H., Buchholz, T. A., Davidson, N. E., Gelmon, K. E., Giordano, S. H., Hudis, C. A., Malin, J., Mamounas, E. P., Rowden, D., Solky, A. J., Sowers, M. R., Stearns, V., Winer, E. P., Somerfield, M. R., & Griggs, J. J. (2010). American Society of Clinical Oncology clinical practice guideline: Update on adjuvant endocrine therapy for women with hormone receptor–positive breast cancer. *Journal of Clinical Oncology, 28*(23), 3784–3796. https://doi.org/10.1200/JCO.2009.26.3756（PMID: 20625130）

Burstein, H. J., Temin, S., Anderson, H., Buchholz, T. A., Davidson, N. E., Gelmon, K. E., Giordano, S. H., Hudis, C. A., Rowden, D., Solky, A. J., Stearns, V., Winer, E. P., & Griggs, J. J. (2014). Adjuvant endocrine therapy for women with hormone receptor–positive breast cancer: American Society of Clinical Oncology clinical practice guideline focused update. *Journal of Clinical Oncology, 32*(21), 2255–2269. https://doi.org/10.1200/JCO.2013.54.2258（PMID: 24868023）

Campone, M., De Laurentiis, M., Jhaveri, K., Hu, X., Ladoire, S., Patsouris, A., Zamagni, C., Cui, J., Cazzaniga, M., Cil, T., Jerzak, K. J., Fuentes, C., Yoshinami, T., Rodriguez-Lescure, A., Sezer, A., Fontana, A., Guarneri, V., Molckovsky, A., Mouret-Reynier, M.-A., . . . Hamilton, E. P. (2025). Vepdegestrant, a PROTAC estrogen receptor degrader, in advanced breast cancer. *New England Journal of Medicine, 393*(6), 556–568. https://doi.org/10.1056/NEJMoa2505725（PMID: 40454645）

Cardoso, F., Parke, S., Brennan, D. J., Briggs, P., Donders, G., Panay, N., Haseli-Mashhadi, N., Block, M., Caetano, C., Francuski, M., Haberland, C., Laapas, K., Seitz, C., & Zuurman, L. (2025). Elinzanetant for vasomotor symptoms from endocrine therapy for breast cancer. *New England Journal of Medicine, 393*(8), 753–763. https://doi.org/10.1056/NEJMoa2415566（PMID: 40454634）

Carter, J., Lacchetti, C., Andersen, B. L., Barton, D. L., Bolte, S., Damast, S., Diefenbach, M. A., DuHamel, K., Florendo, J., Ganz, P. A., Goldfarb, S., Hallmeyer, S., Kushner, D. M., & Rowland, J. H. (2018). Interventions to address sexual problems in people with cancer: American Society of Clinical Oncology clinical practice guideline adaptation of Cancer Care Ontario guideline. *Journal of Clinical Oncology, 36*(5), 492–511. https://doi.org/10.1200/JCO.2017.75.8995（PMID: 29227723）

Cole, M. P., Jones, C. T., & Todd, I. D. (1971). A new anti-oestrogenic agent in late breast cancer: An early clinical appraisal of ICI46474. *British Journal of Cancer, 25*(2), 270–275. https://doi.org/10.1038/bjc.1971.33（PMID: 5115829）

Coombes, R. C., Goss, P., Dowsett, M., Gazet, J. C., & Brodie, A. (1984). 4-Hydroxyandrostenedione in treatment of postmenopausal patients with advanced breast cancer. *The Lancet, 2*(8414), 1237–1239. https://doi.org/10.1016/S0140-6736(84)92795-8（PMID: 6150277）

Crawford, E. D., Heidenreich, A., Lawrentschuk, N., Tombal, B., Pompeo, A. C. L., Mendoza-Valdes, A., Miller, K., Debruyne, F. M. J., & Klotz, L. (2019). Androgen-targeted therapy in men with prostate cancer: Evolving practice and future considerations. *Prostate Cancer and Prostatic Diseases, 22*(1), 24–38. https://doi.org/10.1038/s41391-018-0079-0（PMID: 30131604）

Crown, J., Stroyakovskii, D., Yardley, D. A., Huang, C.-S., Fasching, P. A., Bardia, A., Chia, S., Im, S.-A., Martin, M., Xu, B., Barrios, C. H., Untch, M., Moroose, R., Hurvitz, S. A., Hortobagyi, G. N., Slamon, D. J., Visco, F., Spera, G., Zarate, J. P., . . . Loi, S. (2025). Adjuvant ribociclib plus nonsteroidal aromatase inhibitor therapy in patients with HR-positive/HER2-negative early breast cancer: 5-year follow-up of NATALEE efficacy outcomes and updated overall survival. *ESMO Open, 10*(11), Article 105858. https://doi.org/10.1016/j.esmoop.2025.105858（PMID: 41320342）

Cuzick, J., Sestak, I., Forbes, J. F., Dowsett, M., Cawthorn, S., Mansel, R. E., Loibl, S., Bonanni, B., Evans, D. G., & Howell, A. (2020). Use of anastrozole for breast cancer prevention (IBIS-II): Long-term results of a randomised controlled trial. *The Lancet, 395*(10218), 117–122. https://doi.org/10.1016/S0140-6736(19)32955-1（PMID: 31839281）

Davies, C., Pan, H., Godwin, J., Gray, R., Arriagada, R., Raina, V., Abraham, M., Medeiros Alencar, V. H., Badran, A., Bonfill, X., Bradbury, J., Clarke, M., Collins, R., Davis, S. R., Delmestri, A., Forbes, J. F., Haddad, P., Hou, M.-F., Inbar, M., . . . Peto, R. (2013). Long-term effects of continuing adjuvant tamoxifen to 10 years versus stopping at 5 years after diagnosis of oestrogen receptor-positive breast cancer: ATLAS, a randomised trial. *The Lancet, 381*(9869), 805–816. https://doi.org/10.1016/S0140-6736(12)61963-1（PMID: 23219286）

de Bono, J. S., Logothetis, C. J., Molina, A., Fizazi, K., North, S., Chu, L., Chi, K. N., Jones, R. J., Goodman, O. B., Saad, F., Staffurth, J. N., Mainwaring, P., Harland, S., Flaig, T. W., Hutson, T. E., Cheng, T., Patterson, H., Hainsworth, J. D., Ryan, C. J., . . . Scher, H. I. (2011). Abiraterone and increased survival in metastatic prostate cancer. *New England Journal of Medicine, 364*(21), 1995–2005. https://doi.org/10.1056/NEJMoa1014618（PMID: 21612468）

DeCensi, A., Puntoni, M., Guerrieri-Gonzaga, A., Caviglia, S., Avino, F., Cortesi, L., Taverniti, C., Pacquola, M. G., Falcini, F., Gulisano, M., Digennaro, M., Cariello, A., Cagossi, K., Pinotti, G., Lazzeroni, M., Serrano, D., Branchi, D., Campora, S., Petrera, M., . . . Bonanni, B. (2019). Randomized placebo controlled trial of low-dose tamoxifen to prevent local and contralateral recurrence in breast intraepithelial neoplasia. *Journal of Clinical Oncology, 37*(19), 1629–1637. https://doi.org/10.1200/JCO.18.01779（PMID: 30973790）

Denmeade, S. R., & Isaacs, J. T. (2002). A history of prostate cancer treatment. *Nature Reviews Cancer, 2*(5), 389–396. https://doi.org/10.1038/nrc801（PMID: 12044015）

Di Leo, A., Jerusalem, G., Petruzelka, L., Torres, R., Bondarenko, I. N., Khasanov, R., Verhoeven, D., Pedrini, J. L., Smirnova, I., Lichinitser, M. R., Pendergrass, K., Garnett, S., Lindemann, J. P. O., Sapunar, F., & Martin, M. (2010). Results of the CONFIRM phase III trial comparing fulvestrant 250 mg with fulvestrant 500 mg in postmenopausal women with estrogen receptor-positive advanced breast cancer. *Journal of Clinical Oncology, 28*(30), 4594–4600. https://doi.org/10.1200/JCO.2010.28.8415（PMID: 20855825）

Early Breast Cancer Trialists' Collaborative Group (EBCTCG). (1998). Tamoxifen for early breast cancer: An overview of the randomised trials. *The Lancet, 351*(9114), 1451–1467. https://doi.org/10.1016/S0140-6736(97)11423-4（PMID: 9605801）

Early Breast Cancer Trialists' Collaborative Group (EBCTCG). (2011). Relevance of breast cancer hormone receptors and other factors to the efficacy of adjuvant tamoxifen: Patient-level meta-analysis of randomised trials. *The Lancet, 378*(9793), 771–784. https://doi.org/10.1016/S0140-6736(11)60993-8（PMID: 21802721）

Early Breast Cancer Trialists' Collaborative Group (EBCTCG). (2015). Aromatase inhibitors versus tamoxifen in early breast cancer: Patient-level meta-analysis of the randomised trials. *The Lancet, 386*(10001), 1341–1352. https://doi.org/10.1016/S0140-6736(15)61074-1（PMID: 26211827）

Early Breast Cancer Trialists' Collaborative Group (EBCTCG). (2022). Aromatase inhibitors versus tamoxifen in premenopausal women with oestrogen receptor-positive early-stage breast cancer treated with ovarian suppression: A patient-level meta-analysis of 7030 women from four randomised trials. *The Lancet Oncology, 23*(3), 382–392. https://doi.org/10.1016/S1470-2045(21)00758-0（PMID: 35123662）

Early Breast Cancer Trialists' Collaborative Group (EBCTCG). (2025). Extending the duration of endocrine treatment for early breast cancer: Patient-level meta-analysis of 12 randomised trials of aromatase inhibitors in 22 031 postmenopausal women already treated with at least 5 years of endocrine therapy. *The Lancet, 406*(10503), 603–614. https://doi.org/10.1016/S0140-6736(25)01013-X（PMID: 40783288）

Eli Lilly and Company. (2023). *EVISTA (raloxifene hydrochloride): Prescribing information* (revised 2023-03; DailyMed version effective 2026-02-11). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=fcaaa6dc-74e8-4fb8-800c-5574bf0f8de9

Eli Lilly and Company. (2026). *INLURIYO (imlunestrant): Prescribing information* (effective 2026-09-18). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=5bc172e4-e8a2-441a-be52-279a7f890196

Fisher, B., Costantino, J. P., Wickerham, D. L., Redmond, C. K., Kavanah, M., Cronin, W. M., Vogel, V., Robidoux, A., Dimitrov, N., Atkins, J., Daly, M., Wieand, S., Tan-Chiu, E., Ford, L., & Wolmark, N. (1998). Tamoxifen for prevention of breast cancer: Report of the National Surgical Adjuvant Breast and Bowel Project P-1 Study. *Journal of the National Cancer Institute, 90*(18), 1371–1388. https://doi.org/10.1093/jnci/90.18.1371（PMID: 9747868）

Fisher, B., Dignam, J., Wolmark, N., Wickerham, D. L., Fisher, E. R., Mamounas, E., Smith, R., Begovic, M., Dimitrov, N. V., Margolese, R. G., Kardinal, C. G., Kavanah, M. T., Fehrenbacher, L., & Oishi, R. H. (1999). Tamoxifen in treatment of intraductal breast cancer: National Surgical Adjuvant Breast and Bowel Project B-24 randomised controlled trial. *The Lancet, 353*(9169), 1993–2000. https://doi.org/10.1016/S0140-6736(99)05036-9（PMID: 10376613）

Francis, P. A., Pagani, O., Fleming, G. F., Walley, B. A., Colleoni, M., Rubovszky, G., Tondini, C., Ciruelos, E. M., Gomez, H. L., Bonnefoi, H. R., Burstein, H. J., Chini, C., Puglisi, F., Spazzapan, S., Bernardo, A., Climent, M. A., Bellet, M., Ruhstaller, T., Bermejo, B., . . . Regan, M. M. (2026). Final outcomes of the SOFT and TEXT phase III trials in premenopausal hormone receptor-positive early breast cancer. *Annals of Oncology, 37*(10), 1367–1385. https://doi.org/10.1016/j.annonc.2026.05.704（PMID: 42229584）

Francis, P. A., Regan, M. M., Fleming, G. F., Láng, I., Ciruelos, E., Bellet, M., Bonnefoi, H. R., Climent, M. A., Da Prada, G. A., Burstein, H. J., Martino, S., Davidson, N. E., Geyer, C. E., Jr., Walley, B. A., Coleman, R., Kerbrat, P., Buchholz, S., Ingle, J. N., Winer, E. P., . . . Gelber, R. D. (2015). Adjuvant ovarian suppression in premenopausal breast cancer. *New England Journal of Medicine, 372*(5), 436–446. https://doi.org/10.1056/NEJMoa1412379（PMID: 25495490）

Fribbens, C., O'Leary, B., Kilburn, L., Hrebien, S., Garcia-Murillas, I., Beaney, M., Cristofanilli, M., Andre, F., Loi, S., Loibl, S., Jiang, J., Bartlett, C. H., Koehler, M., Dowsett, M., Bliss, J. M., Johnston, S. R. D., & Turner, N. C. (2016). Plasma ESR1 mutations and the treatment of estrogen receptor–positive advanced breast cancer. *Journal of Clinical Oncology, 34*(25), 2961–2968. https://doi.org/10.1200/JCO.2016.67.3061（PMID: 27269946）

Gnant, M., Pfeiler, G., Dubsky, P. C., Hubalek, M., Greil, R., Jakesz, R., Wette, V., Balic, M., Haslbauer, F., Melbinger, E., Bjelic-Radisic, V., Artner-Matuschek, S., Fitzal, F., Marth, C., Sevelda, P., Mlineritsch, B., Steger, G. G., Manfreda, D., Exner, R., . . . Singer, C. F. (2015). Adjuvant denosumab in breast cancer (ABCSG-18): A multicentre, randomised, double-blind, placebo-controlled trial. *The Lancet, 386*(9992), 433–443. https://doi.org/10.1016/S0140-6736(15)60995-3（PMID: 26040499）

Goetz, M. P., Sangkuhl, K., Guchelaar, H.-J., Schwab, M., Province, M., Whirl-Carrillo, M., Symmans, W. F., McLeod, H. L., Ratain, M. J., Zembutsu, H., Gaedigk, A., van Schaik, R. H., Ingle, J. N., Caudle, K. E., & Klein, T. E. (2018). Clinical Pharmacogenetics Implementation Consortium (CPIC) guideline for *CYP2D6* and tamoxifen therapy. *Clinical Pharmacology & Therapeutics, 103*(5), 770–777. https://doi.org/10.1002/cpt.1007（PMID: 29385237）

Goss, P. E., Ingle, J. N., Alés-Martínez, J. E., Cheung, A. M., Chlebowski, R. T., Wactawski-Wende, J., McTiernan, A., Robbins, J., Johnson, K. C., Martin, L. W., Winquist, E., Sarto, G. E., Garber, J. E., Fabian, C. J., Pujol, P., Maunsell, E., Farmer, P., Gelmon, K. A., Tu, D., & Richardson, H. (2011). Exemestane for breast-cancer prevention in postmenopausal women. *New England Journal of Medicine, 364*(25), 2381–2391. https://doi.org/10.1056/NEJMoa1103507（PMID: 21639806）

Goss, P. E., Ingle, J. N., Martino, S., Robert, N. J., Muss, H. B., Piccart, M. J., Castiglione, M., Tu, D., Shepherd, L. E., Pritchard, K. I., Livingston, R. B., Davidson, N. E., Norton, L., Perez, E. A., Abrams, J. S., Therasse, P., Palmer, M. J., & Pater, J. L. (2003). A randomized trial of letrozole in postmenopausal women after five years of tamoxifen therapy for early-stage breast cancer. *New England Journal of Medicine, 349*(19), 1793–1802. https://doi.org/10.1056/NEJMoa032312（PMID: 14551341）

Hanker, A. B., Sudhan, D. R., & Arteaga, C. L. (2020). Overcoming endocrine resistance in breast cancer. *Cancer Cell, 37*(4), 496–513. https://doi.org/10.1016/j.ccell.2020.03.009（PMID: 32289273）

Harper, M. J., & Walpole, A. L. (1967). A new derivative of triphenylethylene: Effect on implantation and mode of action in rats. *Journal of Reproduction and Fertility, 13*(1), 101–119. https://doi.org/10.1530/jrf.0.0130101（PMID: 6066766）

Hassett, M. J., Somerfield, M. R., Baker, E. R., Cardoso, F., Kansal, K. J., Kwait, D. C., Plichta, J. K., Ricker, C., Roshal, A., Ruddy, K. J., Safer, J. D., Van Poznak, C., Yung, R. L., & Giordano, S. H. (2020). Management of male breast cancer: ASCO guideline. *Journal of Clinical Oncology, 38*(16), 1849–1863. https://doi.org/10.1200/JCO.19.03120（PMID: 32058842）

Henry, N. L., Azzouz, F., Desta, Z., Li, L., Nguyen, A. T., Lemler, S., Hayden, J., Tarpinian, K., Yakim, E., Flockhart, D. A., Stearns, V., Hayes, D. F., & Storniolo, A. M. (2012). Predictors of aromatase inhibitor discontinuation as a result of treatment-emergent symptoms in early-stage breast cancer. *Journal of Clinical Oncology, 30*(9), 936–942. https://doi.org/10.1200/JCO.2011.38.0261（PMID: 22331951）

Henry, N. L., Unger, J. M., Schott, A. F., Fehrenbacher, L., Flynn, P. J., Prow, D. M., Sharer, C. W., Burton, G. V., Kuzma, C. S., Moseley, A., Lew, D. L., Fisch, M. J., Moinpour, C. M., Hershman, D. L., & Wade, J. L. (2018). Randomized, multicenter, placebo-controlled clinical trial of duloxetine versus placebo for aromatase inhibitor-associated arthralgias in early-stage breast cancer: SWOG S1202. *Journal of Clinical Oncology, 36*(4), 326–332. https://doi.org/10.1200/JCO.2017.74.6651（PMID: 29136387）

Hershman, D. L., Kushi, L. H., Shao, T., Buono, D., Kershenbaum, A., Tsai, W.-Y., Fehrenbacher, L., Gomez, S. L., Miles, S., & Neugut, A. I. (2010). Early discontinuation and nonadherence to adjuvant hormonal therapy in a cohort of 8,769 early-stage breast cancer patients. *Journal of Clinical Oncology, 28*(27), 4120–4128. https://doi.org/10.1200/JCO.2009.25.9655（PMID: 20585090）

Hershman, D. L., Shao, T., Kushi, L. H., Buono, D., Tsai, W. Y., Fehrenbacher, L., Kwan, M., Gomez, S. L., & Neugut, A. I. (2011). Early discontinuation and non-adherence to adjuvant hormonal therapy are associated with increased mortality in women with breast cancer. *Breast Cancer Research and Treatment, 126*(2), 529–537. https://doi.org/10.1007/s10549-010-1132-4（PMID: 20803066）

Hershman, D. L., Unger, J. M., Greenlee, H., Capodice, J. L., Lew, D. L., Darke, A. K., Kengla, A. T., Melnik, M. K., Jorgensen, C. W., Kreisle, W. H., Minasian, L. M., Fisch, M. J., Henry, N. L., & Crew, K. D. (2018). Effect of acupuncture vs sham acupuncture or waitlist control on joint pain related to aromatase inhibitors among women with early-stage breast cancer: A randomized clinical trial. *JAMA, 320*(2), 167–176. https://doi.org/10.1001/jama.2018.8907（PMID: 29998338）

Hortobagyi, G. N., Stemmer, S. M., Burris, H. A., Yap, Y.-S., Sonke, G. S., Hart, L., Campone, M., Petrakova, K., Winer, E. P., Janni, W., Conte, P., Cameron, D. A., André, F., Arteaga, C. L., Zarate, J. P., Chakravartty, A., Taran, T., Le Gac, F., Serra, P., & O'Shaughnessy, J. (2022). Overall survival with ribociclib plus letrozole in advanced breast cancer. *New England Journal of Medicine, 386*(10), 942–950. https://doi.org/10.1056/NEJMoa2114663（PMID: 35263519）

Huggins, C., & Hodges, C. V. (1972). Studies on prostatic cancer: I. The effect of castration, of estrogen and androgen injection on serum phosphatases in metastatic carcinoma of the prostate. *CA: A Cancer Journal for Clinicians, 22*(4), 232–240. https://doi.org/10.3322/canjclin.22.4.232（PMID: 4625049；重刊 1941 年原文）

Irwin, M. L., Cartmel, B., Gross, C. P., Ercolano, E., Li, F., Yao, X., Fiellin, M., Capozza, S., Rothbard, M., Zhou, Y., Harrigan, M., Sanft, T., Schmitz, K., Neogi, T., Hershman, D., & Ligibel, J. (2015). Randomized exercise trial of aromatase inhibitor–induced arthralgia in breast cancer survivors. *Journal of Clinical Oncology, 33*(10), 1104–1111. https://doi.org/10.1200/JCO.2014.57.1547（PMID: 25452437）

Jensen, E. V., Block, G. E., Smith, S., Kyser, K., & DeSombre, E. R. (1971). Estrogen receptors and breast cancer response to adrenalectomy. *National Cancer Institute Monograph, 34*, 55–70.（PMID: 5140877）

Jensen, E. V., & Jordan, V. C. (2003). The estrogen receptor: A model for molecular medicine. *Clinical Cancer Research, 9*(6), 1980–1989.（PMID: 12796359）

Jhaveri, K. L., Neven, P., Casalnuovo, M. L., Kim, S.-B., Tokunaga, E., Aftimos, P., Saura, C., O'Shaughnessy, J., Harbeck, N., Carey, L. A., Curigliano, G., Llombart-Cussac, A., Lim, E., García Tinoco, M. D. L. L., Sohn, J., Mattar, A., Zhang, Q., Huang, C.-S., Hung, C.-C., . . . Bidard, F.-C. (2025). Imlunestrant with or without abemaciclib in advanced breast cancer. *New England Journal of Medicine, 392*(12), 1189–1202. https://doi.org/10.1056/NEJMoa2410858（PMID: 39660834）

Johnston, S., Martin, M., O'Shaughnessy, J., Hegg, R., Tolaney, S. M., Guarneri, V., Del Mastro, L., Campone, M., Sohn, J., Boyle, F., Cortes, J., Rugo, H. S., Goetz, M. P., Hamilton, E. P., Huang, C.-S., Senkus, E., Cicin, I., Testa, L., Neven, P., . . . Harbeck, N. (2026). Overall survival with abemaciclib in early breast cancer. *Annals of Oncology, 37*(2), 155–165. https://doi.org/10.1016/j.annonc.2025.10.005（PMID: 41110697）

Jordan, V. C. (2006). Tamoxifen (ICI46,474) as a targeted therapy to treat and prevent breast cancer. *British Journal of Pharmacology, 147*(Suppl. 1), S269–S276. https://doi.org/10.1038/sj.bjp.0706399（PMID: 16402113）

Kelly, C. M., Juurlink, D. N., Gomes, T., Duong-Hua, M., Pritchard, K. I., Austin, P. C., & Paszat, L. F. (2010). Selective serotonin reuptake inhibitors and breast cancer mortality in women receiving tamoxifen: A population based cohort study. *BMJ, 340*, Article c693. https://doi.org/10.1136/bmj.c693（PMID: 20142325）

Khosrow-Khavar, F., Filion, K. B., Al-Qurashi, S., Torabi, N., Bouganim, N., Suissa, S., & Azoulay, L. (2017). Cardiotoxicity of aromatase inhibitors and tamoxifen in postmenopausal women with breast cancer: A systematic review and meta-analysis of randomized controlled trials. *Annals of Oncology, 28*(3), 487–496. https://doi.org/10.1093/annonc/mdw673（PMID: 27998966）

Klijn, J. G., Blamey, R. W., Boccardo, F., Tominaga, T., Duchateau, L., & Sylvester, R. (2001). Combined tamoxifen and luteinizing hormone-releasing hormone (LHRH) agonist versus LHRH agonist alone in premenopausal advanced breast cancer: A meta-analysis of four randomized trials. *Journal of Clinical Oncology, 19*(2), 343–353. https://doi.org/10.1200/JCO.2001.19.2.343（PMID: 11208825）

Kyowa Kirin, Inc. (2024). *FARESTON (toremifene citrate): Prescribing information* (effective 2024-11-13). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=2cab8dd1-3a10-48e6-86ce-0e5275ed49e5

Leon-Ferre, R. A., Novotny, P. J., Wolfe, E. G., Faubion, S. S., Ruddy, K. J., Flora, D., Dakhil, C. S. R., Rowland, K. M., Graham, M. L., Le-Lindqwister, N., Smith, T. J., & Loprinzi, C. L. (2020). Oxybutynin vs placebo for hot flashes in women with or without breast cancer: A randomized, double-blind clinical trial (ACCRU SC-1603). *JNCI Cancer Spectrum, 4*(1), Article pkz088. https://doi.org/10.1093/jncics/pkz088（PMID: 32337497）

Leuprolide Study Group. (1984). Leuprolide versus diethylstilbestrol for metastatic prostate cancer. *New England Journal of Medicine, 311*(20), 1281–1286. https://doi.org/10.1056/NEJM198411153112004（PMID: 6436700）

Loprinzi, C. L., Kugler, J. W., Sloan, J. A., Mailliard, J. A., LaVasseur, B. I., Barton, D. L., Novotny, P. J., Dakhil, S. R., Rodger, K., Rummans, T. A., & Christensen, B. J. (2000). Venlafaxine in management of hot flashes in survivors of breast cancer: A randomised controlled trial. *The Lancet, 356*(9247), 2059–2063. https://doi.org/10.1016/S0140-6736(00)03403-6（PMID: 11145492）

Margolese, R. G., Cecchini, R. S., Julian, T. B., Ganz, P. A., Costantino, J. P., Vallow, L. A., Albain, K. S., Whitworth, P. W., Cianfrocca, M. E., Brufsky, A. M., Gross, H. M., Soori, G. S., Hopkins, J. O., Fehrenbacher, L., Sturtz, K., Wozniak, T. F., Seay, T. E., Mamounas, E. P., & Wolmark, N. (2016). Anastrozole versus tamoxifen in postmenopausal women with ductal carcinoma in situ undergoing lumpectomy plus radiotherapy (NSABP B-35): A randomised, double-blind, phase 3 clinical trial. *The Lancet, 387*(10021), 849–856. https://doi.org/10.1016/S0140-6736(15)01168-X（PMID: 26686957）

Nobel Prize Outreach. (2026). *The Nobel Prize in Physiology or Medicine 1977*. NobelPrize.org. Retrieved November 11, 2026, from https://www.nobelprize.org/prizes/medicine/1977/summary/

Novartis Pharmaceuticals Corporation. (2024). *FEMARA (letrozole): Prescribing information* (revised 2024-12; DailyMed version effective 2026-06-11). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=82b77d74-085f-45ac-a7dd-1f5c038bf406

Novartis Pharmaceuticals Corporation. (2026). *KISQALI (ribociclib): Prescribing information* (effective 2026-07-01). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aaeaef94-f3f5-4367-8ea2-b181d7be2da8

Osborne, C. K., Wakeling, A., & Nicholson, R. I. (2004). Fulvestrant: An oestrogen receptor antagonist with a novel mechanism of action. *British Journal of Cancer, 90*(Suppl. 1), S2–S6. https://doi.org/10.1038/sj.bjc.6601629（PMID: 15094757）

Pagani, O., Regan, M. M., Walley, B. A., Fleming, G. F., Colleoni, M., Láng, I., Gomez, H. L., Tondini, C., Burstein, H. J., Perez, E. A., Ciruelos, E., Stearns, V., Bonnefoi, H. R., Martino, S., Geyer, C. E., Jr., Pinotti, G., Puglisi, F., Crivellari, D., Ruhstaller, T., . . . Francis, P. A. (2014). Adjuvant exemestane with ovarian suppression in premenopausal breast cancer. *New England Journal of Medicine, 371*(2), 107–118. https://doi.org/10.1056/NEJMoa1404037（PMID: 24881463）

Pan, H., Gray, R., Braybrooke, J., Davies, C., Taylor, C., McGale, P., Peto, R., Pritchard, K. I., Bergh, J., Dowsett, M., & Hayes, D. F. (2017). 20-year risks of breast-cancer recurrence after stopping endocrine therapy at 5 years. *New England Journal of Medicine, 377*(19), 1836–1846. https://doi.org/10.1056/NEJMoa1701830（PMID: 29117498）

Pandya, K. J., Morrow, G. R., Roscoe, J. A., Zhao, H., Hickok, J. T., Pajon, E., Sweeney, T. J., Banerjee, T. K., & Flynn, P. J. (2005). Gabapentin for hot flashes in 420 women with breast cancer: A randomised double-blind placebo-controlled trial. *The Lancet, 366*(9488), 818–824. https://doi.org/10.1016/S0140-6736(05)67215-7（PMID: 16139656）

Partridge, A. H., Niman, S. M., Ruggeri, M., Peccatori, F. A., Azim, H. A., Colleoni, M., Saura, C., Shimizu, C., Sætersdal, A. B., Kroep, J. R., Mailliez, A., Warner, E., Borges, V. F., Amant, F., Gombos, A., Kataoka, A., Rousset-Jablonski, C., Borstnar, S., Takei, J., . . . Pagani, O. (2023). Interrupting endocrine therapy to attempt pregnancy after breast cancer. *New England Journal of Medicine, 388*(18), 1645–1656. https://doi.org/10.1056/NEJMoa2212856（PMID: 37133584）

Pharmacia & Upjohn Company LLC. (2025). *AROMASIN (exemestane): Prescribing information* (effective 2025-12-24). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=cf066b7a-032a-416c-8d40-15ba581423e3

Quirke, V. M. (2017). Tamoxifen from failed contraceptive pill to best-selling breast cancer medicine: A case-study in pharmaceutical innovation. *Frontiers in Pharmacology, 8*, Article 620. https://doi.org/10.3389/fphar.2017.00620（PMID: 28955226）

Robertson, J. F. R., Bondarenko, I. M., Trishkina, E., Dvorkin, M., Panasci, L., Manikhas, A., Shparyk, Y., Cardona-Huerta, S., Cheung, K.-L., Philco-Salas, M. J., Ruiz-Borrego, M., Shao, Z., Noguchi, S., Rowbottom, J., Stuart, M., Grinsted, L. M., Fazal, M., & Ellis, M. J. (2016). Fulvestrant 500 mg versus anastrozole 1 mg for hormone receptor-positive advanced breast cancer (FALCON): An international, randomised, double-blind, phase 3 trial. *The Lancet, 388*(10063), 2997–3005. https://doi.org/10.1016/S0140-6736(16)32389-3（PMID: 27908454）

Robson, M., Im, S.-A., Senkus, E., Xu, B., Domchek, S. M., Masuda, N., Delaloge, S., Li, W., Tung, N., Armstrong, A., Wu, W., Goessl, C., Runswick, S., & Conte, P. (2017). Olaparib for metastatic breast cancer in patients with a germline BRCA mutation. *New England Journal of Medicine, 377*(6), 523–533. https://doi.org/10.1056/NEJMoa1706450（PMID: 28578601）

Roeland, E. J., Bohlke, K., Baracos, V. E., Bruera, E., Del Fabbro, E., Dixon, S., Fallon, M., Herrstedt, J., Lau, H., Platek, M., Rugo, H. S., Schnipper, H. H., Smith, T. J., Tan, W., & Loprinzi, C. L. (2020). Management of cancer cachexia: ASCO guideline. *Journal of Clinical Oncology, 38*(21), 2438–2453. https://doi.org/10.1200/JCO.20.00611（PMID: 32432946）

Santen, R. J., Brodie, H., Simpson, E. R., Siiteri, P. K., & Brodie, A. (2009). History of aromatase: Saga of an important biological mediator and therapeutic target. *Endocrine Reviews, 30*(4), 343–375. https://doi.org/10.1210/er.2008-0016（PMID: 19389994）

Schally, A. V., Arimura, A., Kastin, A. J., Matsuo, H., Baba, Y., Redding, T. W., Nair, R. M., Debeljuk, L., & White, W. F. (1971). Gonadotropin-releasing hormone: One polypeptide regulates secretion of luteinizing and follicle-stimulating hormones. *Science, 173*(4001), 1036–1038. https://doi.org/10.1126/science.173.4001.1036（PMID: 4938639）

Scher, H. I., Fizazi, K., Saad, F., Taplin, M.-E., Sternberg, C. N., Miller, K., de Wit, R., Mulders, P., Chi, K. N., Shore, N. D., Armstrong, A. J., Flaig, T. W., Fléchon, A., Mainwaring, P., Fleming, M., Hainsworth, J. D., Hirmand, M., Selby, B., Seely, L., & de Bono, J. S. (2012). Increased survival with enzalutamide in prostate cancer after chemotherapy. *New England Journal of Medicine, 367*(13), 1187–1197. https://doi.org/10.1056/NEJMoa1207506（PMID: 22894553）

Schiavon, G., Hrebien, S., Garcia-Murillas, I., Cutts, R. J., Pearson, A., Tarazona, N., Fenwick, K., Kozarewa, I., Lopez-Knowles, E., Ribas, R., Nerurkar, A., Osin, P., Chandarlapaty, S., Martin, L.-A., Dowsett, M., Smith, I. E., & Turner, N. C. (2015). Analysis of ESR1 mutation in circulating tumor DNA demonstrates evolution during therapy for metastatic breast cancer. *Science Translational Medicine, 7*(313), Article 313ra182. https://doi.org/10.1126/scitranslmed.aac7551（PMID: 26560360）

Shang, Y., & Brown, M. (2002). Molecular determinants for the tissue specificity of SERMs. *Science, 295*(5564), 2465–2468. https://doi.org/10.1126/science.1068537（PMID: 11923541）

Shapiro, C. L., Van Poznak, C., Lacchetti, C., Kirshner, J., Eastell, R., Gagel, R., Smith, S., Edwards, B. J., Frank, E., Lyman, G. H., Smith, M. R., Mhaskar, R., Henderson, T., & Neuner, J. (2019). Management of osteoporosis in survivors of adult cancers with nonmetastatic disease: ASCO clinical practice guideline. *Journal of Clinical Oncology, 37*(31), 2916–2946. https://doi.org/10.1200/JCO.19.01696（PMID: 31532726）

Shiau, A. K., Barstad, D., Loria, P. M., Cheng, L., Kushner, P. J., Agard, D. A., & Greene, G. L. (1998). The structural basis of estrogen receptor/coactivator recognition and the antagonism of this interaction by tamoxifen. *Cell, 95*(7), 927–937. https://doi.org/10.1016/S0092-8674(00)81717-1（PMID: 9875847）

Shore, N. D., Saad, F., Cookson, M. S., George, D. J., Saltzstein, D. R., Tutrone, R., Akaza, H., Bossi, A., van Veenhuyzen, D. F., Selby, B., Fan, X., Kang, V., Walling, J., & Tombal, B. (2020). Oral relugolix for androgen-deprivation therapy in advanced prostate cancer. *New England Journal of Medicine, 382*(23), 2187–2196. https://doi.org/10.1056/NEJMoa2004325（PMID: 32469183）

Simpson, E. R. (2003). Sources of estrogen and their importance. *The Journal of Steroid Biochemistry and Molecular Biology, 86*(3–5), 225–230. https://doi.org/10.1016/S0960-0760(03)00360-1（PMID: 14623515）

Smith, I. E., Dowsett, M., Yap, Y.-S., Walsh, G., Lønning, P. E., Santen, R. J., & Hayes, D. (2006). Adjuvant aromatase inhibitors for early breast cancer after chemotherapy-induced amenorrhoea: Caution and suggested guidelines. *Journal of Clinical Oncology, 24*(16), 2444–2447. https://doi.org/10.1200/JCO.2005.05.3694（PMID: 16735701）

Stemline Therapeutics, Inc. (2026). *ORSERDU (elacestrant): Prescribing information* (effective 2026-06-24). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aa66ae5c-2bd2-4444-8178-b55651e054ef

TerSera Therapeutics LLC. (2026). *ZOLADEX (goserelin implant) 3.6 mg: Prescribing information* (effective 2026-03-24). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=294b168b-6e5f-4db9-bf70-d599271458b3

Teva Pharmaceuticals USA, Inc. (2022). *Megestrol acetate tablets USP: Prescribing information* (effective 2022-11-30). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=66573d39-f2a7-49fd-9ed2-97ac8f6e8456

Tolis, G., Ackman, D., Stellos, A., Mehta, A., Labrie, F., Fazekas, A. T., Comaru-Schally, A. M., & Schally, A. V. (1982). Tumor growth inhibition in patients with prostatic carcinoma treated with luteinizing hormone-releasing hormone agonists. *Proceedings of the National Academy of Sciences of the United States of America, 79*(5), 1658–1662. https://doi.org/10.1073/pnas.79.5.1658（PMID: 6461861）

Toy, W., Shen, Y., Won, H., Green, B., Sakr, R. A., Will, M., Li, Z., Gala, K., Fanning, S., King, T. A., Hudis, C., Chen, D., Taran, T., Hortobagyi, G., Greene, G., Berger, M., Baselga, J., & Chandarlapaty, S. (2013). ESR1 ligand-binding domain mutations in hormone-resistant breast cancer. *Nature Genetics, 45*(12), 1439–1445. https://doi.org/10.1038/ng.2822（PMID: 24185512）

Turner, N. C., Im, S.-A., Saura, C., Juric, D., Loibl, S., Kalinsky, K., Schmid, P., Loi, S., Sunpaweravong, P., Musolino, A., Li, H., Zhang, Q., Nowecki, Z., Leung, R., Thanopoulou, E., Shankar, N., Lei, G., Stout, T. J., Hutchinson, K. E., . . . Jhaveri, K. L. (2024). Inavolisib-based therapy in PIK3CA-mutated advanced breast cancer. *New England Journal of Medicine, 391*(17), 1584–1596. https://doi.org/10.1056/NEJMoa2404625（PMID: 39476340）

Turner, N. C., Mayer, E. L., Park, Y. H., Janni, W., Ma, C., Cristofanilli, M., Bianchini, G., Kalinsky, K., Iwata, H., Chia, S., Brufsky, A. M., Fasching, P. A., Nowecki, Z., Pascual, J., Karadurmus, N., Gal-Yam, E., Chung, W.-P., Im, S.-A., Zambelli, A., . . . Bidard, F.-C. (2026). Switching to camizestrant at ESR1 mutation emergence before disease progression during first-line treatment of hormone receptor-positive advanced breast cancer (SERENA-6): Extended analysis of a double-blind, placebo-controlled, randomised, phase 3 trial. *The Lancet Oncology, 27*(8), 941–958. https://doi.org/10.1016/S1470-2045(26)00287-1（PMID: 42442380）

Turner, N. C., Oliveira, M., Howell, S. J., Dalenc, F., Cortes, J., Gomez Moreno, H. L., Hu, X., Jhaveri, K., Krivorotko, P., Loibl, S., Morales Murillo, S., Okera, M., Park, Y. H., Sohn, J., Toi, M., Tokunaga, E., Yousef, S., Zhukova, L., de Bruin, E. C., . . . Rugo, H. S. (2023). Capivasertib in hormone receptor–positive advanced breast cancer. *New England Journal of Medicine, 388*(22), 2058–2070. https://doi.org/10.1056/NEJMoa2214131（PMID: 37256976）

US Food and Drug Administration. (2023, January 27). *FDA approves elacestrant for ER-positive, HER2-negative, ESR1-mutated advanced or metastatic breast cancer*. https://www.fda.gov/drugs/cancer-approvals/fda-approves-elacestrant-er-positive-her2-negative-esr1-mutated-advanced-or-metastatic-breast-cancer

US Food and Drug Administration. (2026, May 29). *For healthcare professionals: FDA's examples of drugs that interact with CYP enzymes and transporter systems*. https://www.fda.gov/drugs/drug-interactions-labeling/healthcare-professionals-fdas-examples-drugs-interact-cyp-enzymes-and-transporter-systems

Vogel, V. G., Costantino, J. P., Wickerham, D. L., Cronin, W. M., Cecchini, R. S., Atkins, J. N., Bevers, T. B., Fehrenbacher, L., Pajon, E. R., Wade, J. L., Robidoux, A., Margolese, R. G., James, J., Lippman, S. M., Runowicz, C. D., Ganz, P. A., Reis, S. E., McCaskill-Stevens, W., Ford, L. G., . . . Wolmark, N. (2006). Effects of tamoxifen vs raloxifene on the risk of developing invasive breast cancer and other disease outcomes: The NSABP Study of Tamoxifen and Raloxifene (STAR) P-2 trial. *JAMA, 295*(23), 2727–2741. https://doi.org/10.1001/jama.295.23.joc60074（PMID: 16754727）

Wakeling, A. E., Dukes, M., & Bowler, J. (1991). A potent specific pure antiestrogen with clinical potential. *Cancer Research, 51*(15), 3867–3873.（PMID: 1855205）

