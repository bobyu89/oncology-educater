# 抗癌藥物總論：從發現到臨床（From Discovery to Bedside）

| 項目 | 本章依據 |
|------|---------|
| 發現史 | 化療史回顧（DeVita & Chu, 2008；Falzone et al., 2018）與各藥的原始論文（第 1 段逐一引用） |
| 藥物開發與審查 | 美國 FDA 的藥物開發流程說明與加速審查機制（Food and Drug Administration, 2018；Food and Drug Administration, 2023）、第一期試驗設計（Le Tourneau et al., 2009）、成功率（Wong et al., 2019） |
| 試驗判讀 | FDA 腫瘤藥物試驗終點指引（Oncology Center of Excellence et al., 2018）；範例用本手冊癌別章已引用的試驗 |
| 命名規則 | WHO INN Stem Book 2024（World Health Organization, 2024） |
| 療效評估 | RECIST 1.1（Eisenhauer et al., 2009）、iRECIST（Seymour et al., 2017） |
| 台灣藥證與健保 | 本章不重述；台灣藥證與給付請見各癌別章第 9 段（藥品給付規定 115/10/22 版） |
| 最後更新 | 2026-11-11 |

> 本手冊是學習用整理，不能取代原始指引、仿單、健保公告與院內規範。實際處方以主治醫師判斷與院內流程為準。

**這一章的結論先講：** 抗癌藥的歷史，是從「毒殺分裂快的細胞」一路走到「鎖定特定標靶、放開免疫的煞車、把毒藥綁在抗體上」；每一步都留下一個你今天在病房會做的動作（為什麼給 leucovorin、為什麼追 LVEF、為什麼先驗基因再開藥）。對病人來說，從發現腫瘤到打第一劑藥的順序是固定的：**組織診斷 → 分期 → biomarker → 體能與器官功能 → 治療目標 → 處方**，專科護理師（專師）的工作是在每一步確認前一步已經完成。

這是藥物篇的第一章，也是整個學習路徑的入口。後面四章各講一類藥：[化療藥物](02-cytotoxic-chemotherapy.md)、[標靶藥物](03-targeted-therapy.md)、[免疫治療藥物](04-immunotherapy.md)、[荷爾蒙治療藥物](05-endocrine-therapy.md)。

---

## 0. 速查卡

| 主題 | 一句話重點 |
|------|-----------|
| 抗癌藥的八大類 | 細胞毒性化療、標靶小分子、單株抗體、抗體藥物複合體（ADC）、免疫治療、荷爾蒙治療、細胞治療、放射性配體治療（第 4 段） |
| 一顆藥的路 | 找標靶 → 臨床前 → IND → 第一期（找劑量）→ 第二期（看腫瘤會不會縮）→ 第三期（和標準治療比）→ 審查 → 上市後監測（第 2 段） |
| 第一期的三個詞 | DLT（劑量限制毒性）、MTD（最大耐受劑量）、RP2D（第二期建議劑量）；傳統設計是 3+3 |
| 腫瘤藥的淘汰率 | 從第一期走到核准只有 3.4%；用 biomarker 選病人的開發計畫 10.7%，沒有用的 1.6%（Wong et al., 2019） |
| 讀試驗先看五件事 | 收誰、跟誰比、主要終點、差多少（絕對值與相對值）、病人付出什麼代價（第 3 段） |
| 終點 | 整體存活（OS）最可靠；PFS、DFS／EFS、ORR、pCR 比較早看得到，但不一定代表活得比較久 |
| 風險比（HR） | HR 0.72 是「每個時間點的死亡風險低 28%」，不是「多活 28%」；要和中位數、存活率一起看 |
| RECIST 1.1 | PR：直徑總和比基準值減少 ≥30%；PD：比最小值增加 ≥20% 且 ≥5 mm，或出現新病灶（第 6 段） |
| iRECIST | 免疫治療第一次影像惡化記為 iUPD；臨床穩定者可續用，4–8 週後再照一次，確認才算 iCPD |
| 學名字尾 | -tinib 酪胺酸激酶抑制劑、-ciclib CDK 抑制劑、-parib PARP 抑制劑、-mab 單株抗體（2021 年起新藥改用 -tug、-bart、-mig、-ment） |
| 病人的路徑 | 組織診斷 → 分期 → biomarker → 體能與器官功能 → 治療目標 → 團隊會議 → 處方 → 評估療效與毒性（第 5 段） |
| 抗藥性 | 分先天與後天；後天常見四條路：標靶本身再突變、旁路活化、組織型轉化、藥物到不了或被打出細胞（第 7 段） |

> [!IMPORTANT]
> **必背數字**
> - RECIST 1.1：目標病灶最多 5 個、每個器官最多 2 個；非淋巴結病灶量長徑（CT 上 ≥10 mm 才可測量），淋巴結量短徑（≥15 mm 才可當目標病灶，<10 mm 視為正常）（Eisenhauer et al., 2009）。
> - 3+3 設計：3 人都沒有 DLT 就升一階；1 人有 DLT 就在同一劑量再收 3 人；3–6 人中有 2 人以上 DLT 就停止升階（Le Tourneau et al., 2009）。
> - 美國 FDA 加速核准 25 年的經驗（93 個腫瘤與血液適應症）：55% 之後確認了臨床效益，5% 被撤回（Beaver et al., 2018）。
> - 單株抗體新字尾：-tug（未修飾的免疫球蛋白）、-bart（人工改造）、-mig（多特異性）、-ment（片段）（World Health Organization, 2024）。

---

## 1. 抗癌藥物簡史

**先記結論：** 八十年的藥物史可以濃縮成四次轉彎。第一次是 1940 年代發現「藥物可以讓腫瘤縮小」（化療）；第二次是 1970 年代證明「合併用藥可以治癒，手術後看不到的病灶也要治」；第三次是 1997–2001 年開始「先找到標靶，再用藥」（抗體與標靶藥）；第四次是 2011 年以後「不直接打腫瘤，改成放開免疫系統」。每一類藥的完整故事在後面四章，這裡只講骨架。

| 年份 | 事件 | 意義 |
|------|------|------|
| 1942（1946 年發表） | 耶魯大學為一位淋巴肉瘤病人靜脈注射 nitrogen mustard（Goodman et al., 1946；Christakis, 2011） | 第一次證明全身性藥物能讓腫瘤縮小，也第一次看到骨髓抑制與復發 |
| 1948 | Farber 用葉酸拮抗劑 aminopterin 讓兒童急性白血病暫時緩解（Farber et al., 1948） | 抗代謝藥的起點；methotrexate 與 leucovorin 解救由此而來 |
| 1955 | 美國成立 Cancer Chemotherapy National Service Center（DeVita & Chu, 2008） | 國家級的抗癌藥篩選與開發體系 |
| 1965–1969 | Rosenberg 發現鉑電極的電解產物會抑制大腸桿菌分裂，接著證實鉑化合物有抗腫瘤活性（Rosenberg et al., 1965；Rosenberg et al., 1969） | cisplatin 的由來 |
| 1970 | 四種藥合併的 MOPP 用於晚期何杰金氏病（DeVita et al., 1970） | 合併化療可以治癒晚期癌症 |
| 1971 | 抗雌激素 ICI 46,474（tamoxifen）第一份乳癌臨床報告（Cole et al., 1971） | 荷爾蒙治療；後來成為第一個針對標靶（雌激素受體）的乳癌治療（Jordan, 2006） |
| 1975–1976 | 乳癌術後輔助化療：L-PAM（Fisher et al., 1975）、CMF（Bonadonna et al., 1976） | 手術後看不到的微小轉移也要治療 |
| 1977 | cisplatin ＋ vinblastine ＋ bleomycin 治療轉移性睪丸癌（Einhorn & Donohue, 1977） | 已經轉移的實體腫瘤也可能治癒 |
| 1997–1998 | rituximab（1997）與 trastuzumab（1998）獲美國 FDA 核准（Falzone et al., 2018） | 單株抗體進入臨床 |
| 2000 | gemtuzumab ozogamicin 成為第一個 FDA 核准的 ADC（Drago et al., 2021） | 讓抗體載著毒藥進細胞 |
| 2001 | imatinib 獲 FDA 核准用於慢性骨髓性白血病（Cohen et al., 2002） | 針對致癌激酶的口服標靶藥 |
| 2004 | bevacizumab 加化療延長轉移性大腸直腸癌的存活（Hurwitz et al., 2004） | 打腫瘤的血管，而不是腫瘤細胞本身 |
| 2005 | 發現 EGFR T790M 造成 gefitinib 抗藥（Kobayashi et al., 2005） | 抗藥機轉可以定序找出來，再設計下一代藥 |
| 2011 | ipilimumab（anti-CTLA-4）成為第一個核准的免疫檢查點抑制劑（Hodi et al., 2010；Falzone et al., 2018） | 免疫治療時代開始 |
| 2014 | FDA 核准 pembrolizumab（anti-PD-1）用於黑色素瘤（Chuk et al., 2017） | PD-1／PD-L1 抑制劑 |
| 2017 | pembrolizumab 獲准用於 MSI-H／dMMR 實體腫瘤（Marcus et al., 2019）；CAR-T 細胞 tisagenlecleucel 獲准（O'Leary et al., 2019） | 第一個不分癌別、只看 biomarker 的適應症；細胞治療 |
| 2018 | larotrectinib 獲准用於 NTRK 融合實體腫瘤（Scott, 2019）；Allison 與 Honjo 獲諾貝爾生理醫學獎（Huang & Chang, 2019） | 不分癌別的標靶藥；免疫檢查點的發現獲得肯定 |
| 2021 | sotorasib 獲 FDA 加速核准（Nakajima et al., 2022）；WHO 改用新的抗體字尾（Guimaraes Koch et al., 2022） | KRAS 不再是「不可成藥」的標靶 |
| 2022 | trastuzumab deruxtecan 在 HER2-low 乳癌延長存活（Modi et al., 2022） | ADC 改寫了 biomarker 的分類方式 |

### 1.1 化療：從毒氣到治癒（1940–1970 年代）

**Nitrogen mustard。** 第一次世界大戰後，Krumbhaar 在 1919 年報告接觸芥子氣的士兵白血球先升後降。二次大戰期間，美國政府委託耶魯大學的藥理學家 Alfred Gilman 與 Louis Goodman 研究解毒劑；他們在兔子身上看到淋巴球與顆粒球下降，想到可以用來治療淋巴系統的腫瘤，並在移植淋巴瘤的小鼠身上看到腫瘤縮小。1942 年 8 月 27 日，外科醫師 Lindskog 的團隊為一位放射治療已經無效的淋巴肉瘤病人（病歷代號 JD）注射第一劑，劑量 0.1 mg/kg，連續 10 天。腫瘤明顯縮小，切片找不到腫瘤；但接著白血球與血小板下降、牙齦出血、需要輸血；第 49 天復發，再給藥的效果變差，第 96 天過世。因為戰時保密，病歷上只寫「substance X」，結果到 1946 年才發表（Christakis, 2011；Goodman et al., 1946；Gilman & Philips, 1946）。1943 年 12 月義大利巴里港的芥子氣外洩，暴露者同樣出現骨髓抑制（Falzone et al., 2018），但耶魯的第一位病人在前一年就已經治療了。

第一位病人就示範了今天每天在看的三件事：腫瘤會縮小、骨髓會被抑制、復發後再用同一個藥效果變差。所以每次給藥前要看血球（[化療基礎第 5 節](../00-shared/01-chemo-basics.md#5-化療前檢核pre-chemo-checklist)），發燒要當急症處理（[腫瘤急症第 1 節](../00-shared/02-oncologic-emergencies.md#1-發燒性嗜中性球低下)）。

**Farber 與抗葉酸藥。** 1948 年，波士頓的病理科醫師 Sidney Farber 發表用葉酸拮抗劑 aminopterin 治療兒童急性白血病，得到暫時緩解（Farber et al., 1948）。大約十年後才知道這類藥抑制的是二氫葉酸還原酶（DHFR）；同屬葉酸類似物的 methotrexate 至今仍是重要的抗癌藥（Falzone et al., 2018）。

> [!TIP]
> **假零件與備用零件**
> 細胞要複製 DNA 需要葉酸這個「零件」。抗葉酸藥是長得很像的假零件，卡在生產線上（DHFR），生產線就停了。Leucovorin 是已經加工好的備用零件，可以繞過被卡住的那一站，讓正常細胞先恢復生產。所以高劑量 methotrexate 之後要在固定時間開始給 leucovorin 解救，不能早也不能忘（[化療基礎 11.5](../00-shared/01-chemo-basics.md#115-高劑量-methotrexatehd-mtx安全摘要)）；pemetrexed 要先補葉酸與 vitamin B12 也是同一條路上的事（[肺癌章第 5 段](../01-lung-cancer.md#5-常用處方regimen)）。

**合併化療與治癒。** DeVita 等人在美國國家癌症研究院提出 MOPP（mechlorethamine、vincristine、procarbazine、prednisone）治療晚期何杰金氏病（DeVita et al., 1970；Falzone et al., 2018）。長期追蹤 198 位病人，80% 達到完全緩解，其中 68% 在治療結束 10 年後仍無病（DeVita et al., 1980）。兒童急性白血病與晚期何杰金氏病在 1960 到 1970 年代初被合併化療治癒，扭轉了「藥物治不好晚期癌症」的悲觀，也促成了輔助化療的研究（DeVita & Chu, 2008）。今天的處方幾乎都是多藥合併、分週期給，原因見[化療藥物](02-cytotoxic-chemotherapy.md)與本章第 7 段。

**輔助化療。** Fisher 等人把淋巴結陽性的乳癌病人在乳房切除後隨機分到 L-PAM（melphalan）或安慰劑：治療失敗在安慰劑組 108 人中占 22%，L-PAM 組 103 人中占 9.7%（Fisher et al., 1975）。Bonadonna 等人用 CMF（cyclophosphamide、methotrexate、fluorouracil）做同樣的事：追蹤 27 個月，復發在對照組 179 人中占 24%，CMF 組 207 人中占 5.3%（Bonadonna et al., 1976）。這就是病人常問「腫瘤都切乾淨了，為什麼還要化療」的答案：治療的對象是影像看不到的微小轉移。

**Cisplatin。** Rosenberg 等人先發現鉑電極的電解產物讓大腸桿菌不再分裂（Rosenberg et al., 1965），接著報告鉑化合物是一類新的強效抗腫瘤藥（Rosenberg et al., 1969）。這是一個從細菌實驗意外走到抗癌藥的例子。Einhorn 與 Donohue 把 cisplatin 加上 vinblastine、bleomycin 用在 50 位轉移性睪丸癌病人（3 位因早期死亡無法評估）：74% 完全緩解、26% 部分緩解，加上手術切除殘存病灶後 85% 達到無病狀態（Einhorn & Donohue, 1977）。鉑類的毒性與給藥前後的水化，見[化療基礎第 11 節](../00-shared/01-chemo-basics.md#11-抗癌藥分類劑量限制毒性與解毒劑)。

### 1.2 荷爾蒙治療：一顆失敗的避孕藥

Tamoxifen（ICI 46,474）是 1960 年代藥廠在找「事後避孕藥」時合成的非類固醇抗雌激素。它在大鼠有很好的抗生育效果，在人身上卻會誘發排卵，避孕藥的開發就此停掉（Jordan, 2006）。1971 年第一份乳癌臨床報告：46 位晚期或復發乳癌病人中 10 位反應良好，效果和當時使用的雌激素、雄性素相近，但副作用少（Cole et al., 1971）。後來的研究把它和雌激素受體（ER）連在一起，tamoxifen 成為第一個針對標靶的乳癌治療（Jordan, 2006）。

留到今天的動作：開荷爾蒙治療之前，病理報告一定要有 ER、PR 的結果（[乳癌章 2.2](../03-breast-cancer.md#22-erpr-與免疫組織化學亞型)）。完整內容見[荷爾蒙治療藥物](05-endocrine-therapy.md)。

### 1.3 單株抗體與標靶藥（1997–2004 年）

| 藥物 | 關鍵試驗 | 留到今天的臨床動作 |
|------|---------|------------------|
| rituximab（anti-CD20；1997 年 FDA 核准） | 166 位復發的低惡性度或濾泡性淋巴瘤病人，每週 375 mg/m² 共 4 劑，反應率 48%；不良事件多數發生在第一次輸注，以發燒、寒顫最常見（McLaughlin et al., 1998） | 單株抗體第一次輸注要慢慢調速、備好處置（[腫瘤急症第 10 節](../00-shared/02-oncologic-emergencies.md#10-輸注反應過敏反應與過敏性休克)） |
| trastuzumab（anti-HER2；1998 年 FDA 核准） | HER2 過度表現的轉移性乳癌，化療加 trastuzumab 的中位存活 25.1 對 20.3 個月；但和 anthracycline 併用時，27% 發生 NYHA III–IV 級心臟功能不全（Slamon et al., 2001） | 先驗 HER2 才能用藥；治療前與治療中追 LVEF，併用 anthracycline 時風險最高（[乳癌章 6.2](../03-breast-cancer.md#62-抗-her2-治療lvef-監測與暫停規則)） |
| imatinib（BCR-ABL 激酶抑制劑；2001 年 5 月 10 日 FDA 核准） | 第一期試驗 83 位干擾素失敗的慢性期 CML 病人，劑量 25–1,000 mg/日；每日 ≥300 mg 的 54 人中 53 人達到完全血液學反應，而且沒有找到最大耐受劑量（Druker et al., 2001；Cohen et al., 2002） | 標靶藥要先確認病人有那個標靶；標靶藥的劑量不一定是「吃到受不了為止」（第 2.1 段） |
| bevacizumab（anti-VEGF；2004 年 FDA 核准） | 轉移性大腸直腸癌，化療加 bevacizumab 的中位存活 20.3 對 15.6 個月（HR 0.66）；3 級高血壓 11.0% 對 2.3%（Hurwitz et al., 2004） | 每次給藥前量血壓、驗尿蛋白（[肺癌章 6.8](../01-lung-cancer.md#68-抗血管新生藥物bevacizumab-與-ramucirumab)） |

核准年份取自 Falzone 等的整理（Falzone et al., 2018）與 FDA 的核准摘要（Cohen et al., 2002）。完整內容見[標靶藥物](03-targeted-therapy.md)。

### 1.4 免疫治療（2011 年以後）

Allison 的團隊研究 T 細胞上的 CTLA-4，Honjo 的團隊發現 PD-1；兩者都是 T 細胞的抑制訊號，腫瘤會利用它們逃過免疫系統。兩人在 2018 年獲得諾貝爾生理醫學獎（Huang & Chang, 2019）。

- **Ipilimumab**（anti-CTLA-4）：治療過的轉移性黑色素瘤，中位存活 10.0 對 6.4 個月（HR 0.68）；3–4 級免疫相關不良事件 10–15%，14 例治療相關死亡中 7 例與免疫相關不良事件有關（Hodi et al., 2010）。這個試驗的存活曲線到大約第 4 個月才分開，是免疫治療「效果出現得晚、但尾巴長」的典型（Chen, 2013；第 3.3 段）。
- **Pembrolizumab**（anti-PD-1）：2014 年 9 月 4 日獲 FDA 加速核准，用於 ipilimumab 治療後惡化的黑色素瘤，依據是第一期試驗 89 人的反應率 24%，追蹤 6 個月時 86% 的反應仍持續（Chuk et al., 2017）。
- **CAR-T**：tisagenlecleucel 用於兒童與年輕成人復發或難治的 B 細胞急性淋巴性白血病，3 個月內緩解率 81%；細胞激素釋放症候群 77%、神經事件 40%（Maude et al., 2018）。FDA 在 2017 年 8 月 30 日核准時，附帶風險管控計畫（REMS）與 15 年的安全性追蹤研究（O'Leary et al., 2019）。

留到今天的動作：免疫治療的病人出現任何新症狀都要先想到免疫相關不良事件（[irAE 章](../00-shared/04-irae.md#3-通用分級處置)）；細胞治療與雙特異性抗體要會看 CRS 與 ICANS（[腫瘤急症第 9 節](../00-shared/02-oncologic-emergencies.md#9-細胞激素釋放症候群crs與神經毒性icans)）。完整內容見[免疫治療藥物](04-immunotherapy.md)。

### 1.5 不分癌別、ADC 與 KRAS（2017 年以後）

- **不分癌別（tumour-agnostic）的適應症。** Le 等人發現錯配修復缺陷（dMMR）的腫瘤對 pembrolizumab 反應好：dMMR 大腸直腸癌的免疫相關反應率 40%，錯配修復正常者 0%（Le et al., 2015）。2017 年 5 月 23 日 FDA 核准 pembrolizumab 用於 MSI-H 或 dMMR 的實體腫瘤，依據是 5 個單臂試驗、15 種腫瘤共 149 人的反應率 39.6%；這是 FDA 第一次依共同的 biomarker、而不是原發部位核准抗癌藥（Marcus et al., 2019）。Larotrectinib 接著在 2018 年 11 月獲准用於 NTRK 融合的實體腫瘤（Scott, 2019），依據是 17 種腫瘤共 55 人、年齡 4 個月到 76 歲的合併分析，反應率 75%（Drilon et al., 2018）。
- **抗體藥物複合體（antibody-drug conjugate, ADC）。** 由抗體、連接子（linker）與細胞毒性載藥（payload）三部分組成；gemtuzumab ozogamicin 在 2000 年成為第一個 FDA 核准的 ADC（Drago et al., 2021）。Trastuzumab deruxtecan（T-DXd）在過去被歸為「HER2 陰性」的 HER2-low 轉移性乳癌仍然有效：荷爾蒙受體陽性族群的 PFS 10.1 對 5.4 個月（HR 0.51），OS 23.9 對 17.5 個月（HR 0.64）；藥物相關間質性肺病 12.1%，其中 0.8% 致死（Modi et al., 2022）。
- **KRAS G12C。** KRAS 長期被認為無法用藥物抑制；2013 年 Ostrem 等人找到只和 G12C 突變的半胱胺酸結合、把 KRAS 鎖在不活化狀態的小分子（Ostrem et al., 2013）。Sotorasib 在治療過的 KRAS G12C 肺癌反應率 37.1%（Skoulidis et al., 2021），2021 年 5 月 28 日獲 FDA 加速核准（Nakajima et al., 2022）。

留到今天的動作：晚期實體腫瘤要問「MSI／MMR 和 NTRK 驗了沒」；用 T-DXd 的病人新出現咳嗽或喘，先當成間質性肺病處理（[乳癌章 6.7](../03-breast-cancer.md#67-抗體藥物複合體t-dxdt-dm1sacituzumab-govitecandato-dxd)）。

---

## 2. 一顆藥怎麼從實驗室到病人

**先記結論：** 一顆藥要依序回答四個問題：打得到標靶嗎（臨床前）、人可以用多少（第一期）、腫瘤會不會縮（第二期）、比現在的標準治療好嗎（第三期）。腫瘤藥從第一期走到核准的機率只有 3.4%（Wong et al., 2019），你在病房看到的每一個藥都是少數走完全程的。

| 階段 | 要回答的問題 | FDA 對一般藥物的描述 | 腫瘤藥的例子 |
|------|------------|--------------------|------------|
| 找標靶與臨床前研究 | 這個分子是不是腫瘤的弱點？在動物身上安全嗎？ | 動物實驗與毒理資料是之後送件的內容 | BCR-ABL 激酶之於 CML（Druker et al., 2001）；KRAS G12C 的結合口袋（Ostrem et al., 2013） |
| 試驗用新藥申請（Investigational New Drug, IND） | 可以開始用在人身上嗎？ | 送件內容包括動物試驗與毒性資料、製造資訊、試驗計畫書、既有的人體資料與研究者資料；FDA 有 30 天審查 | 送件後才能開始第一期 |
| 第一期（phase I） | 安全嗎？劑量多少？ | 20–100 人；數個月；約 70% 進入下一期 | imatinib 的第一期直接收 83 位 CML 病人（Druker et al., 2001） |
| 第二期（phase II） | 在這個癌別有沒有活性？副作用是什麼？ | 最多數百人；數個月到 2 年；約 33% 進入下一期 | 單臂、看反應率：sotorasib 的 CodeBreaK 100 收 126 人（Skoulidis et al., 2021） |
| 第三期（phase III） | 比標準治療好嗎？ | 300–3,000 人；1–4 年；約 25–30% 進入下一期 | 隨機分派、雙盲：FLAURA 收 556 人（Soria et al., 2018） |
| 審查與核准 | 效益是否大於風險？ | 見 2.3 | 一般核准或加速核准 |
| 第四期（phase IV）與上市後監測 | 更多人、更久之後還安全嗎？ | 數千人；看安全性與療效 | CAR-T 的 15 年追蹤研究（O'Leary et al., 2019） |

FDA 的描述取自其藥物開發流程說明（Food and Drug Administration, 2018），是所有藥物的一般數字，不是腫瘤藥專屬。

### 2.1 第一期：找劑量

第一期的目的是找出給第二期用的建議劑量與給藥時程。細胞毒性藥物的傳統假設是「劑量越高、毒性越大、效果也越好」，所以用毒性當終點，一階一階往上加（Le Tourneau et al., 2009）。

| 名詞 | 定義（Le Tourneau et al., 2009） |
|------|------|
| 劑量限制毒性（dose-limiting toxicity, DLT） | 被認為與藥物有關、嚴重到不能再往上加劑量的毒性；試驗開始前就在計畫書裡定義好，通常看第一個週期，用 CTCAE 分級 |
| 最大耐受劑量（maximum tolerated dose, MTD） | 美國的用法：DLT 發生率不超過 33% 的最高劑量。歐洲與日本的用法：DLT 發生率達到 33% 的最低劑量（其實已經不可耐受） |
| 第二期建議劑量（recommended phase II dose, RP2D） | 美國：等於 MTD。歐洲與日本：MTD 的下一階 |
| 目標毒性水準 | 試驗可接受的 DLT 機率，通常設在 20–33% |

**3+3 設計怎麼走**（Le Tourneau et al., 2009）：

1. 第一組 3 位病人用起始劑量（依動物毒理資料推估的安全劑量）。
2. 3 人都沒有 DLT：下一組 3 人升到下一個預先設定的劑量。
3. 3 人中 1 人有 DLT：同一個劑量再收 3 人。
4. 同一劑量的 3–6 人中有 2 人以上發生 DLT：停止升階。傳統上，第二期建議劑量取這個劑量的下一階。

> [!TIP]
> **走樓梯試水溫**
> 3+3 像帶人走進一池越來越燙的水：每一階先讓 3 個人下去站一下。都沒事就往下一階；有 1 個人喊燙，再找 3 個人確認；有 2 個人喊燙，就退回上一階，那一階就是之後大家泡的水溫。缺點也很明顯：前面幾階的水根本是涼的，站在那裡的人泡不到效果。Le Tourneau 等的回顧指出，用 3+3 的試驗超過一半有 6 個以上的劑量階，很多病人接受的是可能無效的低劑量（Le Tourneau et al., 2009）。

> [!IMPORTANT]
> **DLT、MTD、RP2D 的考點**
> - DLT 是「事先定義」的毒性，通常只算第一個週期；後面週期才出現的累積毒性（例如神經病變）第一期不一定看得到。
> - 3+3 的停止規則：同一劑量 3–6 人中 ≥2 人發生 DLT。
> - CTCAE 是 DLT 的共同語言，分級原則見[化療基礎第 8 節](../00-shared/01-chemo-basics.md#8-ctcae-分級原則)。

**標靶藥不一定適用「越高越好」。** Imatinib 的第一期一路加到 1,000 mg/日都沒有找到 MTD，但 300 mg 以上幾乎所有人都有血液學反應（Druker et al., 2001）。因此新的設計會加入藥物濃度、標靶抑制程度等指標，找「最佳生物劑量」（Le Tourneau et al., 2009）。FDA 審查人員回顧 2019–2021 年核准的小分子藥與 ADC 後指出，隨機比較多個劑量的做法仍不普遍，而劑量沒有最佳化的代價是毒性、生活品質變差、病人撐不到下一線治療（Fourie Zirkelbach et al., 2022）。Sotorasib 就是例子：因為低劑量組的藥物動力學與反應率資料，FDA 核准時要求廠商再做劑量比較試驗（Nakajima et al., 2022）。臨床上的意思是：新藥上市後仿單劑量可能再改，以最新仿單為準。

### 2.2 第二期與第三期：有沒有效、是不是更好

- **第二期**多半是單臂試驗，主要終點是客觀反應率（ORR）。反應率夠高、反應夠持久時，可能直接據此取得加速核准，例如 sotorasib（反應率 37.1%；Skoulidis et al., 2021）與 larotrectinib（三個試驗合併 55 人，反應率 75%；Drilon et al., 2018）。
- **第三期**把病人隨機分到新藥或標準治療，看 PFS 或 OS。例如 FLAURA 把 556 位 EGFR 突變的晚期肺癌病人隨機分到 osimertinib 或第一代 EGFR-TKI（Soria et al., 2018）。怎麼讀第三期的結果，見第 3 段。

### 2.3 審查與核准：一般核准與加速核准

- **一般核准（regular／traditional approval）**：依據臨床效益（活得更久、症狀改善），或已經確立能預測臨床效益的替代終點（Oncology Center of Excellence et al., 2018）。
- **加速核准（accelerated approval）**：1992 年建立的制度。針對嚴重或危及生命的疾病，可以依「合理推測能預測臨床效益」的替代終點（例如反應率）先核准，條件是廠商之後要做試驗確認效益（Oncology Center of Excellence et al., 2018）。

| FDA 的加速機制 | 一句話（Food and Drug Administration, 2023） |
|--------------|------|
| Fast track | 加快嚴重疾病、未被滿足醫療需求的藥物開發與審查 |
| Breakthrough therapy（突破性療法認定） | 可能比現有治療有明顯改善的藥物，加快開發與審查 |
| Accelerated approval（加速核准） | 依替代終點核准治療嚴重疾病、填補未滿足需求的藥物 |
| Priority review（優先審查） | FDA 的目標是在 6 個月內完成審查 |

FDA 回顧 1992 年 12 月到 2017 年 5 月的腫瘤與血液加速核准：64 個產品、93 個適應症；87% 以反應率為依據，72% 的資料來自單臂試驗；55% 已完成確認（中位數 3.4 年），40% 尚未完成，5% 被撤回（Beaver et al., 2018）。Sotorasib 的確認性第三期試驗 CodeBreaK 200 顯示 PFS 5.6 對 4.5 個月（HR 0.66），優於 docetaxel（de Langen et al., 2023）。

> [!WARNING]
> **加速核准不等於已經證明活得比較久**
> 加速核准的依據多半是單臂試驗的反應率，確認性試驗可能要好幾年才有結果，也可能失敗而撤回適應症（Beaver et al., 2018）。向病人說明時，不要把「FDA 已核准」說成「證實可以延長存活」。適應症與劑量都可能在上市後修改，開藥與衛教以最新仿單為準。

**台灣的兩道關卡。** 美國 FDA 核准之後，藥物在台灣還要經過衛生福利部食品藥物管理署（TFDA）的藥品許可證審查，以及全民健康保險的給付審議。美國核准不代表台灣有藥證，有藥證也不代表健保給付。例子見[肺癌章 4.5](../01-lung-cancer.md#45-新藥在台灣的上市狀態)與[乳癌章 4.12](../03-breast-cancer.md#412-新藥與常用藥在台灣的藥證與健保狀態)；台灣藥證與給付請見各癌別章第 9 段。

### 2.4 上市後：第四期與藥物安全監視

試驗收的病人少、追蹤時間有限，罕見或晚發的毒性要等上市後更多人使用才看得到，所以核准不是終點。例子：tisagenlecleucel 核准時附帶風險管控計畫與 15 年的安全性追蹤研究（O'Leary et al., 2019）；加速核准的藥要完成確認性試驗（Beaver et al., 2018）；sotorasib 核准後被要求比較不同劑量（Nakajima et al., 2022）。

> [!NOTE]
> **藥物不良反應通報**
> 臨床人員是上市後安全監視的第一線。懷疑是藥物造成的嚴重或非預期不良反應時，依院內流程通報（通常經藥劑部），並在病歷記下藥名、劑量、發生時間、CTCAE 等級與處置。各院的通報窗口與表單不同，實習時先問清楚。

### 2.5 要花多久、淘汰多少

| 階段 | 所有藥物進入下一期的比例（Food and Drug Administration, 2018） | 腫瘤藥的階段成功率（Wong et al., 2019） |
|------|------|------|
| 第一期 → 第二期 | 約 70% | 57.6% |
| 第二期 → 第三期 | 約 33% | 32.7% |
| 第三期 → 核准 | 約 25–30% 進入下一階段 | 35.5% |
| 第一期 → 核准（整體） | 未列 | 3.4%，是各治療領域中最低的 |

- Wong 等分析 2000–2015 年超過 2 萬個化合物的試驗資料。腫瘤藥的整體成功率最低；用 biomarker 選病人的腫瘤藥開發計畫，成功率是 10.7%，沒有用的是 1.6%（Wong et al., 2019）。這是「先驗 biomarker 再用藥」在藥物開發端的證據。
- 時間：2010–2020 年 FDA 核准的創新藥，從第一次用在人身上到核准，典型的臨床開發時間是 9.1 年（95% CI 8.2–10.0）；取得加速核准的藥平均少約 1,100 天。最快的是 osimertinib，從進入臨床試驗到加速核准只花了 984 天（Brown et al., 2022）。

---

## 3. 怎麼讀臨床試驗

**先記結論：** 讀一篇試驗先問五件事：收了誰、跟誰比、主要終點是什麼、差多少（絕對值和相對值都要看）、病人付出什麼代價。專師不需要會算統計，但要能把「HR 0.72」翻譯成病人聽得懂的話，也要看得出一個數字什麼時候不能照字面相信。

### 3.1 終點（endpoint）

| 終點 | 定義 | 優點 | 要小心 | 本手冊的例子 |
|------|------|------|-------|------------|
| 整體存活（overall survival, OS） | 從隨機分派到任何原因死亡的時間 | 最可靠，不受判讀偏差影響 | 追蹤時間長；後線治療會干擾 | MPACT：8.5 對 6.7 個月（Von Hoff et al., 2013） |
| 無惡化存活（progression-free survival, PFS） | 從隨機分派到腫瘤惡化或死亡，先發生者為準 | 比 OS 早知道，不受後線治療影響 | 靠影像判讀，最好由不知道分組的中央判讀；PFS 進步不一定換成 OS 進步 | FLAURA：18.9 對 10.2 個月（Soria et al., 2018） |
| 無病存活（disease-free survival, DFS）與無事件存活（event-free survival, EFS） | DFS：從隨機分派到復發或死亡，用在術後輔助治療。EFS：在手術前就隨機分派，事件包括惡化到無法手術、復發與死亡 | 治癒性治療要追很久才看得到 OS，DFS／EFS 比較實際 | 各試驗對「事件」的定義不完全一樣，要看原文 | KATHERINE：3 年無侵襲性疾病存活 88.3% 對 77.0%（von Minckwitz et al., 2019）；KEYNOTE-522 的 EFS（Schmid et al., 2020） |
| 客觀反應率（objective response rate, ORR） | 腫瘤縮小達到預設標準並維持一段時間的病人比例，即 CR 加 PR；不含 SD | 直接反映藥物的抗腫瘤活性，單臂試驗就能評估 | 腫瘤縮小不等於活得久 | FLAURA 兩組反應率 80% 對 76% 幾乎一樣，PFS 卻差將近一倍（Soria et al., 2018） |
| 反應持續時間（duration of response, DoR） | 從第一次達到反應到確定惡化的時間 | 和 ORR 一起看，才知道反應是否持久 | 只計算有反應的病人 | FLAURA：17.2 對 8.5 個月（Soria et al., 2018） |
| 病理完全反應（pathological complete response, pCR） | 術前治療後，手術檢體的乳房與淋巴結都找不到侵襲癌 | 手術時就知道結果 | 對個別病人是很強的預後因子，但不能直接代表試驗的長期結果（見 3.4） | KEYNOTE-522：64.8% 對 51.2%（Schmid et al., 2020） |

定義取自 FDA 的終點指引（Oncology Center of Excellence et al., 2018）；pCR 的定義取自 KEYNOTE-522（Schmid et al., 2020）。

### 3.2 風險比（hazard ratio, HR）與信賴區間

- **HR 是什麼。** HR 是兩組「事件發生速率」的比值（Spruance et al., 2004）。MPACT 的死亡 HR 是 0.72（95% CI 0.62–0.83；Von Hoff et al., 2013），意思是追蹤期間的每一個時間點，gemcitabine 加 nab-paclitaxel 組的死亡風險大約是單用 gemcitabine 組的 72%。
- **HR 不是什麼。** HR 不告訴你事件「晚多久」發生；時間要回去看存活曲線與中位數（Spruance et al., 2004）。MPACT 的 HR 0.72 對應的中位存活是 8.5 對 6.7 個月，差 1.8 個月。
- **換成機率。** HR 相當於「風險較高那一組的人先發生事件」的勝算，機率 = HR ÷（1 ＋ HR）（Spruance et al., 2004）。套到 MPACT：兩組各抽一個人來比，合併治療組那個人活得比較久的機率是 1 ÷（1 ＋ 0.72）≈ 58%。
- **信賴區間。** 95% 信賴區間是 HR 真實值可能落在的範圍；區間包含 1，就不能排除兩組沒有差別。FLAURA 的 OS：HR 0.80，95.05% CI 0.64–1.00，P = 0.046（Ramalingam et al., 2020），上限剛好碰到 1，是「勉強達到統計顯著」的例子；KEYNOTE-189 五年追蹤的 OS：HR 0.60，95% CI 0.50–0.72（Garassino et al., 2023），整個區間離 1 很遠。
- **前提。** 用一個 HR 代表整個試驗，前提是 HR 不隨時間改變（Spruance et al., 2004）。免疫治療的存活曲線常常前幾個月重疊、之後才分開，這個前提就不成立（Chen, 2013）。

> [!TIP]
> **兩條高速公路**
> 把兩組病人想成走兩條高速公路。HR 是兩條路「每公里的事故率」的比值：0.72 表示新路每公里出事的機率比舊路少 28%。但 HR 沒有告訴你路有多長、平均可以多開幾公里；那要看中位數（一半的車開到哪裡）和里程碑存活率（開到 100 公里時還有幾成的車在路上）。對病人說明時，三個數字一起講才完整。

### 3.3 中位數與里程碑存活率（landmark survival）

中位存活是「一半的病人還活著」的時間點，只描述曲線的中間；里程碑存活率（例如 1 年、5 年存活率）描述曲線的尾巴。

| 試驗 | 中位 OS | 里程碑存活率 | 看出什麼 |
|------|--------|------------|---------|
| MPACT（Von Hoff et al., 2013） | 8.5 對 6.7 個月 | 1 年 35% 對 22%；2 年 9% 對 4% | 中位數只差 1.8 個月，但 1 年時多了 13 個百分點的人活著 |
| KEYNOTE-189（Gandhi et al., 2018；Garassino et al., 2023） | 第一次報告以 12 個月存活率呈現 | 1 年 69.2% 對 49.4%；5 年 19.4% 對 11.3% | 免疫治療的價值在尾巴：5 年時仍有約五分之一的人活著 |
| PACIFIC（Spigel et al., 2022） | 47.5 對 29.1 個月 | 5 年 42.9% 對 33.4% | 治癒性治療後的鞏固治療，看的是 5 年存活 |

免疫治療常見兩個現象：存活曲線分開得晚，以及有一群長期存活者讓曲線尾巴拉平。這時只看中位數會低估效果，要一起看里程碑存活率（Chen, 2013）。

### 3.4 常見的陷阱

| 陷阱 | 一句話 | 例子 |
|------|-------|------|
| 交叉治療（crossover） | 對照組惡化後也用到試驗藥，OS 的差距會被拉近 | KEYNOTE-189 對照組的有效交叉率 57.3%，OS 仍有差異（HR 0.60；Garassino et al., 2023）；PFS 進步卻沒有換成 OS 進步的例子，見[肺癌章 4.3](../01-lung-cancer.md#43-nsclc-iv-期) |
| 替代終點（surrogate endpoint） | 比較早看得到的終點，不一定能代表 OS | 腫瘤領域 65 個「替代終點對存活」的試驗層次相關分析中，52% 屬低度相關（r ≤0.7），只有 23% 高度相關（r ≥0.85）（Prasad et al., 2015） |
| pCR | 個別病人達到 pCR 預後好，不代表「pCR 率比較高的試驗，存活一定比較好」 | CTNeoBC 匯總 11,955 人：達 pCR 者 EFS 的 HR 0.48；但試驗層次上 pCR 率的增加與 EFS 幾乎無關（R² = 0.03）（Cortazar et al., 2014） |
| 次族群分析（subgroup analysis） | 人數少、比較次數多，容易出現碰巧的結果；要看有沒有事先設定、有沒有做交互作用檢定 | 50 篇主要期刊的試驗報告中三分之二列出次族群結果，多數沒有做適當的交互作用檢定（Assmann et al., 2000）。DESTINY-Breast04 的荷爾蒙受體陰性族群只有 63 人（11.3%）（Modi et al., 2022），解讀要保守 |
| 不劣性試驗（non-inferiority trial） | 目標不是「比較好」，而是「沒有差到超過事先設定的界限」；界限怎麼訂是關鍵 | PERSEPHONE：trastuzumab 6 個月對 12 個月，界限設為 4 年 DFS 相差 3 個百分點；結果 89.4% 對 89.8%，HR 1.07（90% CI 0.93–1.24），達到不劣性（Earl et al., 2019）。FDA 指出不劣性試驗依賴歷史資料，交叉治療也會干擾（Oncology Center of Excellence et al., 2018）；報告規範見 CONSORT 延伸版（Piaggio et al., 2012） |
| 不死時間偏差（immortal-time bias，又稱 guarantee-time bias） | 用「追蹤期間才發生的事」分組再比存活，會有偏差：病人要先活得夠久，才有機會被分到那一組 | 「有反應的人活得比沒反應的人久」「發生某種毒性的人活得比較久」都屬這一類。BIG 1-98 的資料用一般方法分析，雙磷酸鹽看起來有好處；用三種校正方法後好處消失（Giobbie-Hurder et al., 2013） |
| 跨試驗比較 | 不同試驗的族群與對照組不同，中位數不能直接排名 | MPACT 收 KPS ≥70 的病人（Von Hoff et al., 2013）；其他胰臟癌試驗的比較見[胰臟癌章第 4 段](../02-pancreatic-cancer.md#4-治療策略依分期) |
| 只看療效不看代價 | 3 級以上不良事件、停藥率、回診負擔都要看 | MPACT：3 級以上神經病變 17% 對 1%（Von Hoff et al., 2013）；FLAURA：3 級以上不良事件 34% 對 45%（Soria et al., 2018） |

> [!IMPORTANT]
> **終點與判讀的考點**
> - OS 是最可靠的終點；PFS 把「惡化或死亡」都算事件；ORR = CR ＋ PR，不含 SD（Oncology Center of Excellence et al., 2018）。
> - DFS 用在術後輔助治療，EFS 用在術前就隨機分派的試驗。
> - HR <1 表示試驗組風險較低；信賴區間包含 1 表示未達統計顯著。
> - 單臂試驗的 ORR 可以支持加速核准，之後要有確認性試驗（Beaver et al., 2018）。

---

## 4. 藥物分類總覽與命名規則

**先記結論：** 抗癌藥可以分成八大類，差別在「打哪裡」。學名的字尾（INN stem）由 WHO 統一規定，看到字尾就能猜出機轉，也就知道要先驗什麼、要盯什麼毒性。

### 4.1 八大類一張表

| 類別 | 怎麼作用 | 代表藥 | 開藥前與用藥中的重點 | 去哪裡讀 |
|------|---------|-------|-------------------|---------|
| 細胞毒性化療（cytotoxic chemotherapy） | 傷害 DNA 或干擾細胞分裂，細胞更新越快受影響越大，所以骨髓也一起受傷（Falzone et al., 2018） | cisplatin、methotrexate、paclitaxel、doxorubicin | 血球、器官功能、各藥的劑量限制毒性 | [化療藥物](02-cytotoxic-chemotherapy.md)；[化療基礎第 11 節](../00-shared/01-chemo-basics.md#11-抗癌藥分類劑量限制毒性與解毒劑) |
| 標靶小分子（small-molecule targeted therapy） | 口服小分子，抑制腫瘤賴以生長的特定激酶或蛋白，例如 BCR-ABL、EGFR、KRAS G12C（Druker et al., 2001；Soria et al., 2018；Skoulidis et al., 2021） | imatinib、osimertinib、sotorasib | 有對應的 biomarker 才用；口服藥的交互作用與服藥方式 | [標靶藥物](03-targeted-therapy.md)；[化療基礎 14.5](../00-shared/01-chemo-basics.md#145-口服抗癌藥) |
| 單株抗體（monoclonal antibody） | 在細胞外結合表面抗原、受體或生長因子，例如 CD20、HER2、VEGF（McLaughlin et al., 1998；Slamon et al., 2001；Hurwitz et al., 2004） | rituximab、trastuzumab、bevacizumab | 輸注反應；各標靶的特有毒性（心臟、血壓） | [標靶藥物](03-targeted-therapy.md) |
| 抗體藥物複合體（ADC） | 抗體把細胞毒性載藥帶進表現標靶的細胞；由抗體、連接子、載藥三部分組成（Drago et al., 2021） | trastuzumab emtansine、trastuzumab deruxtecan、sacituzumab govitecan | 兼有抗體與化療的毒性；T-DXd 要盯間質性肺病（Modi et al., 2022） | [標靶藥物](03-targeted-therapy.md)；[乳癌章 6.7](../03-breast-cancer.md#67-抗體藥物複合體t-dxdt-dm1sacituzumab-govitecandato-dxd) |
| 免疫治療（immunotherapy） | 免疫檢查點抑制劑阻斷 CTLA-4 或 PD-1／PD-L1，放開 T 細胞的煞車（Hodi et al., 2010；Huang & Chang, 2019） | ipilimumab、pembrolizumab、durvalumab | 免疫相關不良事件可以發生在任何器官 | [免疫治療藥物](04-immunotherapy.md)；[irAE 章](../00-shared/04-irae.md#1-為什麼會有-irae) |
| 荷爾蒙治療（endocrine therapy） | 阻斷荷爾蒙受體的訊號；tamoxifen 作用在雌激素受體（Jordan, 2006） | tamoxifen、fulvestrant | 先確認荷爾蒙受體陽性 | [荷爾蒙治療藥物](05-endocrine-therapy.md) |
| 細胞治療（cellular therapy） | 把病人自己的 T 細胞做基因改造，裝上辨認 CD19 的嵌合抗原受體（CAR）再輸回（Maude et al., 2018；O'Leary et al., 2019） | tisagenlecleucel | 細胞激素釋放症候群與神經毒性 | [腫瘤急症第 9 節](../00-shared/02-oncologic-emergencies.md#9-細胞激素釋放症候群crs與神經毒性icans) |
| 放射性配體治療（radioligand therapy） | 把放射性同位素接在會結合腫瘤標靶的分子上；鎦-177-PSMA-617 把 β 射線送到表現 PSMA 的細胞，在轉移性去勢抗性攝護腺癌延長存活（15.3 對 11.3 個月）（Sartor et al., 2021） | lutetium-177-PSMA-617 | 先用 PSMA 正子攝影確認腫瘤有表現 | 本手冊尚無專章 |

雙特異性抗體（例如 tarlatamab）的病房實務見[肺癌章 7.7](../01-lung-cancer.md#77-tarlatamab-病房實務c1d1c1d8-的醫囑監測與出院衛教)。

> [!TIP]
> **攻城的五種打法**
> 把腫瘤想成一座城。化療是地毯式轟炸，城裡城外分裂快的細胞都會中彈。標靶小分子是潛進城裡，把某一台關鍵機器的開關卡住。單株抗體守在城門外，攔下進城的訊號。ADC 是特洛伊木馬：抗體是木馬的外殼，認得城門；載藥是藏在裡面的士兵，進城後才放出來。免疫治療不直接攻城，而是把自己軍隊（T 細胞）被敵人踩住的煞車放開。打法不同，誤傷的地方也不同，所以每一類藥要盯的毒性不一樣。

### 4.2 小分子藥與化療藥的字尾

| 字尾 | WHO 的定義 | 例子 | 看到要想到 |
|------|-----------|------|-----------|
| -tinib | 酪胺酸激酶抑制劑 | imatinib、alectinib、lenvatinib | 先確認對應的標靶或適應症 |
| -ertinib（-tinib 的次字尾） | EGFR 抑制劑 | osimertinib、lazertinib | EGFR 突變報告 |
| -trectinib（-tinib 的次字尾） | TRK 抑制劑 | larotrectinib、entrectinib | NTRK 融合 |
| -metinib（-tinib 的次字尾） | MEK 抑制劑 | trametinib、binimetinib | 常和 -rafenib 搭配 |
| -rafenib | Raf 激酶抑制劑 | dabrafenib、encorafenib | BRAF V600E |
| -rasib | Ras 蛋白抑制劑 | sotorasib、adagrasib | KRAS G12C |
| -ciclib | 細胞週期素依賴性激酶（CDK）抑制劑 | palbociclib、ribociclib、abemaciclib | 乳癌 CDK4/6 抑制劑 |
| -parib | PARP 抑制劑 | olaparib、talazoparib | BRCA 檢測 |
| -lisib | PI3K 抑制劑 | alpelisib、inavolisib | PIK3CA 突變 |
| -sertib | 絲胺酸／蘇胺酸激酶抑制劑 | capivasertib | |
| -anib | 血管新生抑制劑 | pazopanib、nintedanib | pazopanib 見[肉瘤章](../04-sarcoma.md#4-治療策略依分期) |
| -zomib | 蛋白酶體抑制劑 | bortezomib | 本手冊癌別章未涵蓋 |
| -toclax | Bcl-2 抑制劑 | venetoclax | 本手冊癌別章未涵蓋 |
| -estrant | 雌激素拮抗劑，含雌激素受體下調劑 | fulvestrant、elacestrant、vepdegestrant | ER 陽性乳癌 |
| -ifene | 抗雌激素或雌激素受體調節劑（clomifene、tamoxifen 的衍生物） | toremifene | 和 tamoxifen 同一類 |
| -lutamide | 非類固醇抗雄性素 | enzalutamide | 攝護腺癌的抗雄性素（Vasan et al., 2019） |
| -relin／-relix | -relin：促進腦下垂體激素釋放的胜肽；-relix：GnRH 抑制劑 | leuprorelin、goserelin／degarelix | 乳癌的卵巢功能抑制見[乳癌章第 4 段](../03-breast-cancer.md#4-治療策略依分期) |
| -platin | 鉑類衍生物 | cisplatin、carboplatin、oxaliplatin | 腎功能、神經、過敏 |
| -taxel | 紫杉烷類衍生物 | paclitaxel、docetaxel | 過敏與前置用藥、神經病變 |
| -rubicin | daunorubicin 衍生物（anthracycline） | doxorubicin、epirubicin | 累積劑量與心臟 |
| -tecan | 第一型拓撲異構酶抑制劑 | irinotecan、topotecan | 腹瀉、UGT1A1 |
| -trexate／-trexed | -trexate：葉酸類似物；-trexed：胸苷酸合成酶抑制劑 | methotrexate／pemetrexed | 腎功能、葉酸相關的配套 |
| -citabine | 核苷類抗病毒或抗腫瘤藥（cytarabine、azacitidine 的衍生物） | gemcitabine、capecitabine | |
| -mustine | 烷化劑，β-氯乙基胺衍生物 | bendamustine | nitrogen mustard 的後代 |
| -bulin | 有絲分裂抑制劑，與微管蛋白結合 | eribulin | |

字尾定義與例子都取自 WHO 的 Stem Book 2024（World Health Organization, 2024）；「看到要想到」一欄是本手冊的臨床提醒，細節在各癌別章（biomarker 見[肺癌章 2.2](../01-lung-cancer.md#22-必驗-biomarker)與[乳癌章第 2 段](../03-breast-cancer.md#2-病理與分子標記)，累積劑量見[化療基礎 11.3](../00-shared/01-chemo-basics.md#113-累積劑量上限)，UGT1A1 見[化療基礎 12.2](../00-shared/01-chemo-basics.md#122-ugt1a1-與-irinotecansacituzumab-govitecan)）。蛋白降解劑的命名方式 WHO 還在制定；Stem Book 2024 把 vepdegestrant 歸在 -estrant、bavdegalutamide 歸在 -lutamide，名字中間的 -deg- 提示它是降解劑（degrader）。

### 4.3 單株抗體：舊名字怎麼拆，新名字怎麼認

**舊制（2021 年以前命名的藥，名字不會改）。** 名字由「自選字首 ＋ 標靶字節 ＋ 來源字節 ＋ -mab」組成（World Health Organization, 2024）。

| 字節 | 意思 | 例子 |
|------|------|------|
| 標靶：-t(u)-／-ta- | 腫瘤 | ri-**tu**-xi-mab、tras-**tu**-zu-mab |
| 標靶：-l(i)- | 免疫調節 | pembro-**li**-zu-mab、atezo-**li**-zu-mab |
| 標靶：-c(i)- | 心血管 | beva-**ci**-zu-mab |
| 來源：-xi- | 嵌合型（chimeric） | rituximab |
| 來源：-zu- | 人源化（humanized） | trastuzumab、pembrolizumab、bevacizumab |
| 來源：-u- | 全人源（human） | ipilimumab、nivolumab、durvalumab |

**兩次改制。**

- **2017 年**：WHO 在第 64 次 INN 會議（2017 年 4 月）決定，新命名的抗體不再使用來源字節。理由是抗體工程進步後，用序列判定「嵌合」或「人源化」已經不準確，來源字節也被當成行銷工具（Parren et al., 2017；Guimaraes Koch et al., 2022）。
- **2021 年**：以 -mab 結尾的 INN 已有 879 個，新名字越來越難取。WHO 在第 73 次 INN 會議（2021 年 10 月）決定新藥停用 -mab，改用四個字尾；已經命名的藥不追溯修改（Guimaraes Koch et al., 2022；World Health Organization, 2024）。

| 新字尾 | 適用對象 | 白話 |
|--------|---------|------|
| -tug | 未修飾的免疫球蛋白：單一特異性、全長、恆定區未經改造 | 最接近「天然抗體」的一群 |
| -bart | 人工免疫球蛋白：單一特異性、全長，但恆定區有工程改造的胺基酸變化 | 改造過 Fc 的抗體 |
| -mig | 多特異性免疫球蛋白：雙特異性或多特異性，不論形式 | 一個分子抓兩個以上的標靶 |
| -ment | 免疫球蛋白片段：單一特異性的片段 | 不是完整抗體 |

新制的標靶字節也調整：腫瘤用 -ta-；原本的 -li-（免疫調節）拆成 -sto-（免疫刺激）與 -pru-（免疫抑制）（Guimaraes Koch et al., 2022；World Health Organization, 2024）。所以將來看到「-tatug」「-tabart」「-tamig」結尾的新藥，就是打腫瘤標靶的抗體類藥物。

### 4.4 ADC 的名字是兩個字

ADC 的 INN 由兩個字組成：第一個字是抗體，第二個字是接在抗體上的載藥（Guimaraes Koch et al., 2022；World Health Organization, 2024）。

| 第二個字 | 載藥的種類 | 例子 |
|---------|-----------|------|
| vedotin（字尾 -dotin） | dolastatin 系列的合成衍生物；auristatin（MMAE）屬於這一類，破壞微小管 | brentuximab vedotin、enfortumab vedotin |
| emtansine（字尾 -tansine） | maytansinoid 衍生物（DM1），與微管蛋白結合 | trastuzumab emtansine（T-DM1） |
| deruxtecan、govitecan（字尾 -tecan） | 第一型拓撲異構酶抑制劑：DXd 是 exatecan 衍生物，govitecan 帶的是 irinotecan 的代謝物 SN-38 | trastuzumab deruxtecan（T-DXd）、sacituzumab govitecan |
| ozogamicin | calicheamicin 類，造成 DNA 雙股斷裂 | gemtuzumab ozogamicin |

字尾取自 WHO（World Health Organization, 2024），載藥的機轉取自 Drago 等的回顧（Drago et al., 2021）。新制下的 ADC 也是同樣的組法，例如 raludotatug deruxtecan（-ta- ＋ -tug ＋ deruxtecan）。

> [!WARNING]
> **名字只差一個字，是完全不同的藥**
> Trastuzumab、trastuzumab emtansine（T-DM1）、trastuzumab deruxtecan（T-DXd）的第一個字相同，但劑量、毒性與適應症都不同，不能互換。T-DXd 的間質性肺病發生率 12.1%，有致死案例（Modi et al., 2022）。核對醫囑時要把兩個字都念完，並對照適應症與劑量（[乳癌章 5.3](../03-breast-cancer.md#53-抗體藥物複合體adc與-her2-小分子藥)）。

> [!IMPORTANT]
> **字尾的考點**
> - -tinib 是酪胺酸激酶抑制劑的總字尾；-ertinib（EGFR）、-metinib（MEK）、-trectinib（TRK）是它的次字尾。
> - -ciclib：CDK 抑制劑；-parib：PARP 抑制劑；-rafenib：Raf 抑制劑；-rasib：Ras 抑制劑；-lisib：PI3K 抑制劑；-zomib：蛋白酶體抑制劑。
> - -platin、-taxel、-rubicin、-tecan 分別是鉑類、紫杉烷類、anthracycline、第一型拓撲異構酶抑制劑。
> - 舊制抗體：-xi- 嵌合、-zu- 人源化、-u- 全人源；2021 年起新抗體改用 -tug、-bart、-mig、-ment，舊名不改。
> - ADC 第二個字看載藥：vedotin、emtansine 打微小管；deruxtecan、govitecan 是第一型拓撲異構酶抑制劑。

---

## 5. 從發現腫瘤到決定治療：一位病人的路徑

**先記結論：** 不管哪一種癌，順序都一樣：先有組織診斷，再分期，再看 biomarker，再看病人撐不撐得住，然後才談治療目標與處方。順序錯了會出事：沒有病理就治療、基因報告沒回來就開免疫治療、沒看體能狀態就給高強度化療，都是可以避免的錯誤。

### 5.1 十三個步驟

| 步驟 | 要回答的問題 | 專師在這一步的工作 | 手冊哪裡教 |
|------|------------|------------------|-----------|
| 1. 發現：症狀或篩檢 | 這個表現像不像癌症？有沒有急症？ | 問病史與危險因子，辨認需要立刻處理的警訊 | [肺癌章 3.0](../01-lung-cancer.md#30-臨床表現與身體評估)、[肺癌章 1.3](../01-lung-cancer.md#13-篩檢低劑量電腦斷層ldct)、[乳癌章 1.3](../03-breast-cancer.md#13-篩檢乳房x光攝影) |
| 2. 影像 | 病灶在哪裡、多大、哪裡最適合取檢體？ | 確認影像已安排，調出舊片比較 | [肺癌章 3.1](../01-lung-cancer.md#31-work-up-流程)、[乳癌章 3.2](../03-breast-cancer.md#32-診斷流程臨床影像病理三合一) |
| 3. 組織診斷 | 是不是癌？哪一種細胞？ | 追病理報告；確認檢體夠不夠做後續的 biomarker | 各癌別章第 2 段，例如[肺癌章](../01-lung-cancer.md#2-病理與分子標記)、[肉瘤章](../04-sarcoma.md#2-病理與分子標記) |
| 4. 分期 | 局部、局部晚期，還是已經轉移？ | 確認分期檢查做齊，在病歷寫下 TNM 與版次 | [肺癌章 3.2](../01-lung-cancer.md#32-tnm-第-9-版)、[乳癌章第 3 段](../03-breast-cancer.md#3-診斷與分期)、[胰臟癌章第 3 段](../02-pancreatic-cancer.md#3-診斷與分期) |
| 5. Biomarker | 有沒有可以用藥的標靶？ | 確認該驗的都送了、追報告；報告回來前提醒團隊不要先開免疫治療 | [肺癌章 2.2](../01-lung-cancer.md#22-必驗-biomarker)、[乳癌章 2.3](../03-breast-cancer.md#23-her2-判讀) |
| 6. 體能狀態與器官功能 | 病人承受得了哪一種強度的治療？ | 評估 ECOG（Oken et al., 1982）、肝腎功能、心臟、B 型肝炎、老年評估、生育力 | [化療基礎第 1 節](../00-shared/01-chemo-basics.md#1-體能狀態ecog-與-kps)、[第 6 節](../00-shared/01-chemo-basics.md#6-b-型肝炎篩檢與預防性抗病毒)、[第 12 節](../00-shared/01-chemo-basics.md#12-藥物基因檢測與特殊族群評估) |
| 7. 治療目標 | 目標是治癒，還是延長生命與控制症狀？ | 確認團隊、病人與家屬對目標的理解一致，並寫進病歷 | 本段 5.2；[化療基礎 7.3](../00-shared/01-chemo-basics.md#73-治療目標決定調整的方向) |
| 8. 多專科團隊會議（MDT） | 手術、放射、藥物怎麼排順序？ | 準備病例摘要（病理、分期、biomarker、ECOG、共病），記錄決議 | 各癌別章第 4 段 |
| 9. 選處方 | 哪一個處方有證據、病人適合、而且付得起？ | 對照指引與試驗的收案條件；確認健保給付與事前審查 | 各癌別章第 4、5、9 段 |
| 10. 同意與給藥前檢核 | 病人了解並同意了嗎？今天可以打嗎？ | 衛教、確認同意書、逐項核對給藥前檢核表 | [化療基礎第 5 節](../00-shared/01-chemo-basics.md#5-化療前檢核pre-chemo-checklist)、[第 14 節](../00-shared/01-chemo-basics.md#14-給藥安全標準與口服抗癌藥)、[肺癌章 7.1](../01-lung-cancer.md#71-每次化療前檢核) |
| 11. 療效評估 | 腫瘤有沒有縮小？ | 確認影像按時安排，和基準影像比較 | 本章第 6 段；[肺癌章 7.6](../01-lung-cancer.md#76-療效評估與追蹤)、[乳癌章 7.6](../03-breast-cancer.md#76-療效評估與追蹤) |
| 12. 毒性處置 | 副作用幾級？要不要延後、減量或停藥？ | 用 CTCAE 分級、依處方規則處理、需要時通報 | [化療基礎第 7、8 節](../00-shared/01-chemo-basics.md#7-劑量調整原則)、[支持性照護](../00-shared/03-supportive-care.md#1-化療引起的噁心嘔吐cinv)、[irAE 章](../00-shared/04-irae.md#3-通用分級處置)、[腫瘤急症](../00-shared/02-oncologic-emergencies.md#急症速覽) |
| 13. 下一步 | 惡化了換哪一線？治療結束後怎麼追蹤？什麼時候加入緩和照護？ | 惡化時確認要不要重新切片或驗抗藥機轉；提早轉介緩和照護 | 本章第 7 段；[支持性照護第 9 節](../00-shared/03-supportive-care.md#9-早期緩和照護) |

> [!WARNING]
> **基因報告回來之前，不要先開免疫治療**
> EGFR 突變的肺癌病人如果先用 PD-1／PD-L1 抑制劑、之後再接 osimertinib，15% 發生 3–4 級免疫相關不良事件；間隔在 3 個月內的更高達 24%，發生時間的中位數是開始 osimertinib 後 20 天，全部需要類固醇、多數需要住院。順序反過來（先 osimertinib 再免疫治療）則沒有觀察到（Schoenfeld et al., 2019）。第 5 步沒完成就跳到第 9 步，代價由病人承擔。細節見[肺癌章 2.2](../01-lung-cancer.md#22-必驗-biomarker)。

### 5.2 治療目標與常見名詞

| 名詞 | 意思 | 本手冊的例子 |
|------|------|------------|
| 治癒性（curative） | 目標是讓病人不再復發 | 早期乳癌、可切除的肺癌 |
| 緩和性（palliative） | 無法治癒；目標是延長生命、控制症狀、維持生活品質 | 轉移性胰臟癌的化療（Von Hoff et al., 2013） |
| 術前治療（neoadjuvant） | 手術前先給全身性治療 | HER2 陽性乳癌的術前化療加抗 HER2 治療（[乳癌章 4.5](../03-breast-cancer.md#45-早期-her2-陽性抗-her2-治療的階梯)） |
| 術後輔助治療（adjuvant） | 手術後清除看不到的微小轉移 | CMF（Bonadonna et al., 1976）；術後有殘存病灶改用 T-DM1（von Minckwitz et al., 2019） |
| 圍手術期治療（perioperative） | 手術前後都給 | KEYNOTE-522：術前 pembrolizumab 加化療，術後續用 pembrolizumab（Schmid et al., 2020） |
| 根治性（definitive）放化療 | 不手術，以放射治療合併化療作為根治手段 | 不可切除第 III 期肺癌的同步化放療（Antonia et al., 2017） |
| 鞏固治療（consolidation） | 根治性治療後沒有惡化，再加一段治療降低復發 | 化放療後 durvalumab 最多 12 個月（Antonia et al., 2017） |
| 維持治療（maintenance） | 誘導治療有效後，用較低強度的治療延長控制時間 | KEYNOTE-189：4 個週期後以 pembrolizumab 加 pemetrexed 維持（Gandhi et al., 2018） |
| 線別（line of therapy） | 第一線是診斷晚期後的第一個全身性治療；惡化後換的是第二線，依此類推 | AURA3 收的是第一線 EGFR-TKI 治療後惡化的病人（Mok et al., 2017） |

治療目標會改變所有後續決定。以治癒為目標時，要盡量維持劑量與時程，用支持性治療撐過毒性；以緩和為目標時，生活品質和存活一樣重要（[化療基礎 7.3](../00-shared/01-chemo-basics.md#73-治療目標決定調整的方向)）。轉移性肺癌病人在診斷後就加入緩和照護，生活品質較好、憂鬱症狀較少，中位存活 11.6 對 8.9 個月（Temel et al., 2010）；所以「緩和照護」不是放棄治療之後才做的事。

### 5.3 範例一：肺腺癌

58 歲不吸菸的女性，咳嗽兩個月。

1. **發現與影像**：胸部 X 光看到右上肺結節，接著做胸部電腦斷層（[肺癌章 3.1](../01-lung-cancer.md#31-work-up-流程)）。
2. **組織診斷**：切片報告為腺癌（[肺癌章第 2 段](../01-lung-cancer.md#2-病理與分子標記)）。
3. **分期**：完成全身分期檢查後發現骨轉移，屬第 IV 期（[肺癌章 3.2](../01-lung-cancer.md#32-tnm-第-9-版)）。
4. **Biomarker**：送基因檢測與 PD-L1。等報告期間不開免疫治療（Schoenfeld et al., 2019）。結果是 EGFR exon 19 deletion（[肺癌章 2.2](../01-lung-cancer.md#22-必驗-biomarker)）。
5. **體能與器官功能**：ECOG 1，肝腎功能正常。
6. **治療目標**：第 IV 期，緩和性治療的第一線；同時轉介緩和照護團隊（Temel et al., 2010）。
7. **處方**：osimertinib。依據是 FLAURA：PFS 18.9 對 10.2 個月（HR 0.46），OS 38.6 對 31.8 個月（HR 0.80）（Soria et al., 2018；Ramalingam et al., 2020）。其他第一線選項的比較見[肺癌章 4.3](../01-lung-cancer.md#43-nsclc-iv-期)，健保條件見[肺癌章第 9 段](../01-lung-cancer.md#9-健保給付與事前審查)。
8. **開始用藥**：醫囑與衛教見[肺癌章 7.4](../01-lung-cancer.md#74-order-set-範例三門診開始-osimertinib)。
9. **療效評估**：依 RECIST 1.1 比較基準影像（本章第 6 段；[肺癌章 7.6](../01-lung-cancer.md#76-療效評估與追蹤)）。
10. **惡化之後**：先找抗藥機轉。第一線 osimertinib 惡化時，MET 放大約 15%、EGFR C797S 約 7%，也可能轉化成小細胞癌（Leonetti et al., 2019）；結果決定下一線（本章第 7 段）。

### 5.4 範例二：HER2 陽性乳癌

46 歲女性，自己摸到左側乳房腫塊。

1. **發現與影像**：乳房攝影與超音波（[乳癌章 3.2](../03-breast-cancer.md#32-診斷流程臨床影像病理三合一)）。
2. **組織診斷與 biomarker**：粗針切片為侵襲性乳癌，ER 陰性、PR 陰性、HER2 IHC 3+（[乳癌章 2.2](../03-breast-cancer.md#22-erpr-與免疫組織化學亞型)、[2.3](../03-breast-cancer.md#23-her2-判讀)）。乳癌的 biomarker 在切片時就一起做，因為亞型決定整條治療路線（[乳癌章 4.1](../03-breast-cancer.md#41-治療總覽三種亞型各走一條路)）。
3. **分期**：臨床分期 cT2N1，第 II 期；要不要做全身分期檢查見[乳癌章 3.3](../03-breast-cancer.md#33-依情境選擇全身分期檢查)。
4. **體能與器官功能**：ECOG 0。因為要用 trastuzumab，治療前先做心臟超音波看 LVEF（Slamon et al., 2001；[乳癌章 6.2](../03-breast-cancer.md#62-抗-her2-治療lvef-監測與暫停規則)）；另外驗 B 型肝炎、談生育力（[化療基礎第 12 節](../00-shared/01-chemo-basics.md#12-藥物基因檢測與特殊族群評估)）。
5. **治療目標**：治癒。
6. **團隊會議與處方**：先做術前治療，再手術（[乳癌章 4.5](../03-breast-cancer.md#45-早期-her2-陽性抗-her2-治療的階梯)；醫囑範例見[乳癌章 7.3](../03-breast-cancer.md#73-order-set-範例二術前-tchp首次輸注與心臟監測)）。
7. **用手術病理決定下一步**：達到 pCR 的病人預後好（HER2 陽性、荷爾蒙受體陰性且用過 trastuzumab 者，EFS 的 HR 0.15；Cortazar et al., 2014），術後續用抗 HER2 抗體。有殘存侵襲癌者，術後改用 T-DM1 14 個週期：KATHERINE 的 3 年無侵襲性疾病存活 88.3% 對 77.0%（HR 0.50）（von Minckwitz et al., 2019）。
8. **追蹤**：治療期間與結束後的 LVEF 追蹤見[乳癌章 6.2](../03-breast-cancer.md#62-抗-her2-治療lvef-監測與暫停規則)，存活者照護見[乳癌章第 7 段](../03-breast-cancer.md#7-專師實務)。

兩個範例放在一起看：肺腺癌是「先分期、再等基因報告」，乳癌是「切片時就知道亞型」；一個以緩和為目標、用藥到惡化為止，一個以治癒為目標、療程有固定長度。步驟相同，每一步的答案不同。

---

## 6. 療效評估：RECIST 1.1 與 iRECIST

**先記結論：** RECIST 1.1 用「目標病灶直徑總和」的變化來判定反應：縮小 30% 是 PR，比最小值增加 20% 且至少 5 mm 是 PD，出現新病灶也是 PD（Eisenhauer et al., 2009）。免疫治療偶爾會先變大再縮小，所以 iRECIST 多了一個「先不下結論、4–8 週後再確認」的步驟（Seymour et al., 2017）。

### 6.1 RECIST 1.1 怎麼做

1. **基準影像**：越接近開始治療越好，不可早於治療前 4 週。之後每次評估都用同一種檢查方法。
2. **哪些病灶可測量**：非淋巴結病灶在 CT 上長徑 ≥10 mm（切片厚度不超過 5 mm）；淋巴結短徑 ≥15 mm。
3. **選目標病灶（target lesion）**：最多 5 個、每個器官最多 2 個，挑大的、好重複測量的。把每個病灶的直徑加起來（非淋巴結量長徑、淋巴結量短徑），就是「直徑總和」。
4. **其餘是非目標病灶（non-target lesion）**：只記錄「有、沒有、明確惡化」，不量大小。短徑 10 到未滿 15 mm 的淋巴結、肋膜或心包膜積液、腹水、腦膜轉移、淋巴管性轉移都屬於不可測量；成骨性骨轉移不可測量，骨掃描與正子攝影只能用來確認骨病灶存在或消失。
5. **每次評估**：依下表判定。

| 反應 | 目標病灶的定義 | 比較的基準 |
|------|--------------|-----------|
| 完全反應（complete response, CR） | 所有目標病灶消失；所有病理性淋巴結短徑縮到 <10 mm | — |
| 部分反應（partial response, PR） | 直徑總和減少 ≥30% | 和**基準值**比 |
| 疾病惡化（progressive disease, PD） | 直徑總和增加 ≥20%，**而且**絕對值增加 ≥5 mm；或出現新病灶 | 和治療中的**最小值**（nadir）比 |
| 疾病穩定（stable disease, SD） | 縮小不到 PR、增加不到 PD | — |

（Eisenhauer et al., 2009）

**兩個算給你看的例子。**

- 基準總和 80 mm → 第 8 週 52 mm（減少 35%，PR）→ 第 16 週 48 mm（最小值）→ 第 24 週 58 mm。和最小值比增加 10 mm、20.8%，兩個條件都符合，判定 PD；雖然和基準值比還是小了 27.5%。
- 基準總和 20 mm → 最小值 12 mm → 這次 15 mm。增加 25%，但絕對值只多 3 mm，不到 5 mm，不算 PD。5 mm 的規定就是為了避免總和很小時被測量誤差誤判（Eisenhauer et al., 2009）。

其他要記的規則（Eisenhauer et al., 2009）：

- **新病灶**必須是明確的，不是掃描技術不同或癒合中的骨病灶造成的假象。在基準影像沒有掃到的部位發現病灶（例如治療中才做腦部影像而發現腦轉移），算新病灶。不確定時繼續治療並追蹤；之後確認是新病灶，惡化日期回溯到第一次看到的那天。
- **非目標病灶**的惡化必須「明確」（unequivocal），才能單獨判定 PD。
- **腫瘤標記**不能單獨用來判定反應。
- 臨床上的評估間隔與追蹤時程，見[肺癌章 7.6](../01-lung-cancer.md#76-療效評估與追蹤)與[乳癌章 7.6](../03-breast-cancer.md#76-療效評估與追蹤)。

> [!TIP]
> **量身高要用同一面牆**
> RECIST 像幫小孩量身高：每次用同一面牆、同一把尺（同一種影像、同一批目標病灶），才比得出變化。判斷「長高」要和歷史最矮的那一次比（最小值），判斷「變矮」要和第一次比（基準值）。差一兩毫米可能只是站姿不同，所以規定至少要差 5 mm 才算數。

> [!IMPORTANT]
> **RECIST 1.1 的考點**
> - PR 和基準值比（減少 ≥30%）；PD 和最小值比（增加 ≥20% 且 ≥5 mm）。兩個的分母不一樣，是最常考的陷阱。
> - 目標病灶最多 5 個、每個器官最多 2 個；淋巴結量短徑，≥15 mm 才能當目標病灶，<10 mm 算正常。
> - 出現明確的新病灶就是 PD，不管目標病灶縮了多少。
> - 腫瘤標記上升不能單獨當作 PD。

### 6.2 iRECIST：免疫治療的修正版

**為什麼需要。** 免疫治療活化 T 細胞，少數病人的影像會先出現病灶變大或新病灶，之後才縮小，稱為假性惡化（pseudoprogression）。這種情形並不常見：文獻報告的比例通常在 10% 以下，而且主要來自黑色素瘤；在肺癌等其他腫瘤的真實比例不清楚，可能更低（Seymour et al., 2017）。

**怎麼做**（Seymour et al., 2017）：

1. 第一次符合 RECIST 1.1 的 PD 時，先記為**未確認的惡化（iUPD）**。
2. 病人**臨床穩定**才考慮繼續治療。臨床穩定的定義是：體能狀態沒有變差、疾病相關症狀（疼痛、喘）沒有明顯加重、不需要加強症狀處置（增加止痛藥、放射治療或其他緩和處置）。
3. **4–8 週後**再做一次影像。
4. 確認惡化（**iCPD**）的條件：目標病灶總和比 iUPD 時再增加 ≥5 mm；或非目標病灶進一步變大；或新病灶變大、數目變多。
5. 如果第二次影像反而縮小到符合 iCR、iPR 或 iSD，之前的 iUPD 就「歸零」，之後要再出現 iUPD 並再次確認才算惡化。
6. 新病灶另外記錄（最多量 5 個、每個器官最多 2 個），不加進原本目標病灶的總和。

iRECIST 是給臨床試驗統一收集資料用的規範；要不要繼續治療，仍由病人與醫療團隊決定（Seymour et al., 2017）。健保對免疫檢查點抑制劑續用的評估規定見[肺癌章第 9 段](../01-lung-cancer.md#9-健保給付與事前審查)。

> [!WARNING]
> **不要把真的惡化當成假性惡化**
> 假性惡化是少數（通常 ≤10%）；影像變大時，多數就是真的惡化。只有臨床穩定的病人才適合「再等 4–8 週確認」。體能變差、症狀加重的病人，繼續用無效的藥會耽誤下一線治療的時機（Seymour et al., 2017）。看到影像報告寫 PD、而病人同時變喘或更痛，應立刻回報主治醫師，不要用「可能是假性惡化」帶過。

---

## 7. 抗藥性的共通原理

**先記結論：** 抗藥性不是藥突然壞掉，而是治療把抗藥的細胞「篩選」出來。先分兩種：一開始就沒效是先天抗藥（intrinsic resistance），先有效、後來失效是後天抗藥（acquired resistance）；實際上兩者常常重疊（Vasan et al., 2019）。後天抗藥要問的是「走了哪一條路」，因為答案決定下一線用什麼。

### 7.1 為什麼一定會發生

- **腫瘤是會演化的族群。** Nowell 在 1976 年提出：腫瘤多半起源於單一細胞，之後不斷產生遺傳變異，比較有優勢的次族群被選出來；他當時就預言，針對個別病人設計的治療，也可能因為出現抗藥的變異株而失效（Nowell, 1976）。
- **腫瘤越大，越可能已經藏著抗藥細胞。** Goldie 與 Coldman 的數學模型指出，腫瘤內出現抗藥細胞的機率隨突變率上升，而且會在腫瘤生長過程中很短的一段時間內，從「機率很低」變成「機率很高」（Goldie & Coldman, 1979）。也就是說，突變率固定時，腫瘤大小決定有沒有抗藥細胞（Vasan et al., 2019）。
- **治療本身就是篩選壓力。** Sequist 等人為 37 位對 EGFR-TKI 抗藥的肺癌病人重新切片：所有腫瘤都保留原本的 EGFR 突變，另外多了抗藥的變化；其中 3 位停藥一段時間後，抗藥機轉消失，再用 EGFR-TKI 又有效（Sequist et al., 2011）。

> [!TIP]
> **除草劑與雜草**
> 一塊田噴了除草劑，大部分雜草死了，但本來就有幾株不怕這種藥。沒有競爭者之後，它們長滿整塊田，這時再噴同一種藥就沒用了。藥沒有變，是田裡的草換了一批。田越大，藏著抗藥雜草的機會越高；所以腫瘤小的時候治療（術後輔助治療）、一次用幾種機轉不同的藥（合併化療），比等腫瘤長大再一種一種試來得有利。

### 7.2 後天抗藥的四條路（以 EGFR 突變肺癌為例）

| 路徑 | 發生了什麼 | EGFR 肺癌的例子 | 臨床對策 |
|------|-----------|---------------|---------|
| 標靶本身再突變（on-target） | 藥物結合的位置變形，藥卡不上去 | 第一代 TKI 治療兩年後復發的病人，切片發現第二個突變 T790M（Kobayashi et al., 2005）。Osimertinib 惡化後常見 C797S：它讓 osimertinib 無法與 EGFR 形成共價鍵，在第二線 osimertinib 的抗藥病人占 10–26%，第一線約 7%（Thress et al., 2015；Leonetti et al., 2019） | 換成對新突變有效的下一代藥：T790M 陽性者用 osimertinib，PFS 10.1 對 4.4 個月（Mok et al., 2017） |
| 旁路活化（bypass track） | 標靶還被藥壓著，但細胞改走另一條訊號路 | MET 放大：18 個抗藥檢體中有 4 個（22%），經由 ERBB3 重新活化 PI3K（Engelman et al., 2007）；第一線 osimertinib 惡化時約 15%，是最常見的機轉（Leonetti et al., 2019） | 找出旁路後加上對應的藥（[肺癌章 4.3](../01-lung-cancer.md#43-nsclc-iv-期)） |
| 組織型轉化（histologic transformation） | 腫瘤變成另一種細胞，不再依賴原本的標靶 | 37 位抗藥病人中 5 位（14%）從非小細胞癌轉成小細胞癌（Sequist et al., 2011） | 比照小細胞癌用鉑類加 etoposide，但效果有限（Vasan et al., 2019）。這種變化要靠組織切片才看得出來 |
| 藥物到不了或被排出 | 藥物進不去腫瘤所在的地方，或被細胞打出去 | 腦是藥物濃度不足的「庇護所」（Vasan et al., 2019）；細胞膜上依賴 ATP 的運輸蛋白把藥排出，造成對多種藥同時抗藥（Gottesman et al., 2002） | 選腦部穿透好的藥，或加上局部治療 |

> [!IMPORTANT]
> **抗藥機轉的考點**
> - T790M 是第一、二代 EGFR-TKI 最有名的抗藥突變，對策是 osimertinib（Mok et al., 2017）。
> - C797S 讓 osimertinib 失去共價結合（Leonetti et al., 2019）。
> - MET 放大是旁路活化的代表（Engelman et al., 2007）。
> - 轉化成小細胞癌要靠切片診斷，治療改用小細胞癌的化療（Sequist et al., 2011）。

### 7.3 所以治療才要合併、要排順序

- **合併用藥。** 早期的 log-kill 假說認為，多種藥各殺掉固定比例的細胞，幾個週期後可以把腫瘤清除；這在對化療很敏感的腫瘤（部分淋巴瘤、生殖細胞瘤）成立，MOPP 與含 cisplatin 的睪丸癌處方就是例子（Vasan et al., 2019；DeVita et al., 1980；Einhorn & Donohue, 1977）。Goldie–Coldman 假說進一步主張：越早讓腫瘤接觸到越多種互不交叉抗藥的藥越好；不過這個假說在臨床上沒有一致被證實（Vasan et al., 2019）。細節見[化療藥物](02-cytotoxic-chemotherapy.md)。
- **把最強的藥放前面。** Osimertinib 對 T790M 也有效，直接放在第一線，OS 比先用第一代 TKI 長（38.6 對 31.8 個月；Ramalingam et al., 2020）。
- **惡化時重新檢查。** 抗藥機轉不只一種，而且不同轉移病灶可能不同；用血液 ctDNA 找 T790M 已經是常規做法，必要時再切片（Vasan et al., 2019；Sequist et al., 2011）。

專師在這裡的工作：影像顯示惡化時，先確認不是「假的抗藥」（有沒有按時服藥、有沒有交互作用影響藥物濃度，見[化療基礎 14.5](../00-shared/01-chemo-basics.md#145-口服抗癌藥)），再提醒團隊安排抗藥機轉的檢查。

---

## 8. 專師在藥物治療中的角色

**先記結論：** 專師是處方到病人之間的最後一道核對，也是病人回報副作用的第一個窗口。四件事要做好：核對醫囑、衛教、把毒性分級並回報、把這些都寫進病歷。

### 8.1 核對醫囑：拿處方對照六樣東西

| 核對項目 | 要問的問題 | 手冊哪裡教 |
|---------|-----------|-----------|
| 診斷與分期 | 病理報告的癌別、分期與治療線別，和這張處方的適應症相符嗎？ | 各癌別章第 4 段 |
| Biomarker | 報告回來了嗎？結果和藥對得起來嗎（EGFR 突變對 -ertinib、HER2 陽性對 trastuzumab）？ | [肺癌章 2.2](../01-lung-cancer.md#22-必驗-biomarker)、[乳癌章 2.3](../03-breast-cancer.md#23-her2-判讀) |
| 身高、體重與劑量計算 | 今天的體重和計算劑量用的一樣嗎？BSA、mg/kg 或 AUC 算對了嗎？ | [化療基礎第 2–4 節](../00-shared/01-chemo-basics.md#2-體表面積bsa計算) |
| 器官功能與基線檢查 | 血球、肝腎功能符合給藥條件嗎？這個藥需要的基線檢查（LVEF、B 型肝炎、甲狀腺功能）做了嗎？ | [化療基礎第 5 節](../00-shared/01-chemo-basics.md#5-化療前檢核pre-chemo-checklist)、[irAE 章第 2 節](../00-shared/04-irae.md#2-開始免疫治療前的基線評估) |
| 前一次的毒性 | 上次的副作用恢復了嗎？需不需要延後或減量？ | [化療基礎第 7 節](../00-shared/01-chemo-basics.md#7-劑量調整原則) |
| 給藥細節 | 藥名（兩個字的要念完）、劑量、途徑、速率、順序、前置用藥都對嗎？ | [化療基礎 14.2](../00-shared/01-chemo-basics.md#142-ascoons-化療給藥安全標準) |

ASCO 與 ONS 的化療給藥安全標準依「處方、調配、給藥」的順序訂定；2016 年版新增調配過程的兩人核對、有給鞘內藥物的機構 vinca 類一律用小袋輸注、以及病人帶回家的藥要標示（Neuss et al., 2016）。

> [!WARNING]
> **核對不是蓋章**
> 多數嚴重的給藥錯誤，在「處方」這一步就看得出來：biomarker 與藥不符、體重是舊的、藥名看錯。前面提過的兩個例子都會致命或造成嚴重傷害：把 trastuzumab deruxtecan 當成 trastuzumab emtansine（第 4.4 段），以及 EGFR 報告沒回來就開免疫治療（第 5.1 段）。vinca 類藥物的給藥途徑錯誤同樣致命，見[化療基礎第 14 節](../00-shared/01-chemo-basics.md#14-給藥安全標準與口服抗癌藥)。看到不符合，先停下來問，不要先給藥。

> [!NOTE]
> **專師的執行範圍與院內核對流程**
> 專師可以開立哪些醫囑、哪些要醫師核簽，雙人核對由誰執行、在哪一個時間點執行，各院依法規與院內規定訂定。夜間與假日找誰、哪些情況可以先依預立醫囑處理、哪些一定要先通知主治醫師（對照 8.5 的表），各院也不同。實習第一週先拿到院內的化療給藥規範、專師預立醫療流程與病房的聯絡流程。

### 8.2 衛教：第一劑之前要講完的事

1. 治療目標與預計的療程（治癒或緩和、幾個週期、什麼時候評估療效）。
2. 這個藥最常見與最危險的副作用，以及出現時的處理方式。
3. 什麼情況要立刻聯絡或回急診（範例見[乳癌章 6.13](../03-breast-cancer.md#613-病人要立刻聯絡團隊的警訊衛教用)）。
4. 口服藥：怎麼吃、漏服怎麼辦、哪些藥與食物要避開（[化療基礎 14.5](../00-shared/01-chemo-basics.md#145-口服抗癌藥)、[肺癌章 5.5](../01-lung-cancer.md#55-口服標靶藥的實務漏服嘔吐管灌與居家安全)）。
5. 避孕與生育力（[化療基礎 12.5](../00-shared/01-chemo-basics.md#125-生育力保存與避孕諮詢)）、感染預防（[支持性照護第 13 節](../00-shared/03-supportive-care.md#13-感染預防疫苗與嗜中性球低下衛教)）。

教病人「早點說」是有證據的：一項隨機試驗收了 766 位接受化療的轉移性癌症病人，一組用電子系統定期回報 12 項症狀，症狀嚴重或惡化時系統通知護理師；這一組的中位存活 31.2 個月，一般照護組 26.0 個月。護理師對 77% 的警示做了處置，回報組接受化療的時間也比較長（8.2 對 6.3 個月）（Basch et al., 2017）。

### 8.3 毒性分級與通報

- 每次看病人都用 CTCAE 把副作用分級；等級決定繼續、延後、減量或停藥（[化療基礎第 8 節](../00-shared/01-chemo-basics.md#8-ctcae-分級原則)）。
- 各類藥的處置：化療與支持性照護見[支持性照護](../00-shared/03-supportive-care.md#本章重點)；免疫治療見[irAE 章](../00-shared/04-irae.md#3-通用分級處置)；危及生命的情況見[腫瘤急症](../00-shared/02-oncologic-emergencies.md#急症速覽)。
- 懷疑是藥物造成的嚴重或非預期不良反應，要通報（第 2.4 段的提示框）。

### 8.4 病歷要留下什麼

每次給藥或回診的紀錄至少要有：處方名稱與第幾個週期、今天的 ECOG 與體重、各項毒性的 CTCAE 等級、關鍵檢驗值、這次有沒有延後或減量與理由、有累積劑量上限的藥目前累積多少（[化療基礎 11.3](../00-shared/01-chemo-basics.md#113-累積劑量上限)）、上一次與下一次療效評估的日期、已經向病人說明的事項。寫法見[肺癌章 7.5](../01-lung-cancer.md#75-soap-範例)與[乳癌章 7.5](../03-breast-cancer.md#75-soap-範例t-dxd-治療中出現新的咳嗽)的 SOAP 範例。

### 8.5 什麼時候要立刻找醫師

| 情況 | 為什麼急 | 先做什麼、去哪裡讀 |
|------|---------|------------------|
| 化療期間發燒 | 可能是發燒性嗜中性球低下 | [腫瘤急症第 1 節](../00-shared/02-oncologic-emergencies.md#1-發燒性嗜中性球低下) |
| 免疫治療病人出現新的喘、腹瀉、胸痛、極度疲倦 | 免疫相關不良事件可能致命；ipilimumab 的試驗中 7 位病人死於免疫相關不良事件（Hodi et al., 2010） | [irAE 章第 5 節](../00-shared/04-irae.md#5-各器官-irae-處置)，心肌炎見 [5.10](../00-shared/04-irae.md#510-心肌炎最致命的-irae) |
| T-DXd 病人新出現咳嗽、喘或發燒 | 間質性肺病，有致死案例（Modi et al., 2022） | [乳癌章 8.3](../03-breast-cancer.md#83-乳癌病人新出現的呼吸困難先問吃什麼藥做過什麼治療) |
| 輸注中出現寒顫、皮疹、喘、血壓下降 | 輸注反應或過敏性休克 | 先停止輸注；[腫瘤急症第 10 節](../00-shared/02-oncologic-emergencies.md#10-輸注反應過敏反應與過敏性休克) |
| 細胞治療或雙特異性抗體後發燒、低血壓、意識改變 | 細胞激素釋放症候群與神經毒性；tisagenlecleucel 的試驗中發生率分別為 77% 與 40%（Maude et al., 2018） | [腫瘤急症第 9 節](../00-shared/02-oncologic-emergencies.md#9-細胞激素釋放症候群crs與神經毒性icans) |
| 懷疑藥物外滲 | 發泡劑會造成組織壞死 | 先停止輸注、不要拔針；[化療基礎第 9 節](../00-shared/01-chemo-basics.md#9-血管外滲extravasation) |
| 給藥前檢核有任何一項不符合，或處方與 biomarker、診斷對不起來 | 給了就收不回來 | 暫不給藥，先聯絡開立醫囑的醫師 |
| 影像報告惡化，而且病人症狀加重 | 需要盡快決定下一線 | 本章第 6.2 段 |

---

## 9. 名詞對照

| 中文 | English | 一句話解釋 |
|------|---------|-----------|
| 國際非專利藥名（學名） | International Nonproprietary Name, INN | WHO 指定的全球通用藥名，處方與病歷用這個名字 |
| 字尾 | stem | 學名中代表藥物類別的固定字根，例如 -tinib |
| 生物標記 | biomarker | 用來選藥或預測療效的檢驗結果，例如 EGFR 突變、HER2、PD-L1 |
| 試驗用新藥申請 | Investigational New Drug, IND | 新藥第一次用在人身上之前，向主管機關提出的申請 |
| 劑量限制毒性 | dose-limiting toxicity, DLT | 第一期試驗事先定義、嚴重到不能再加劑量的毒性 |
| 最大耐受劑量 | maximum tolerated dose, MTD | DLT 發生率仍可接受的最高劑量 |
| 第二期建議劑量 | recommended phase II dose, RP2D | 第一期試驗結束後，建議後續試驗使用的劑量 |
| 加速核准 | accelerated approval | 依替代終點先核准，之後要用確認性試驗證明臨床效益 |
| 整體存活 | overall survival, OS | 從隨機分派到任何原因死亡的時間 |
| 無惡化存活 | progression-free survival, PFS | 從隨機分派到腫瘤惡化或死亡的時間 |
| 無病存活／無事件存活 | disease-free survival, DFS／event-free survival, EFS | 治癒性治療後到復發或死亡的時間；EFS 用在手術前就隨機分派的試驗 |
| 客觀反應率 | objective response rate, ORR | 腫瘤達到完全反應或部分反應的病人比例 |
| 病理完全反應 | pathological complete response, pCR | 術前治療後，手術檢體找不到侵襲癌 |
| 替代終點 | surrogate endpoint | 比存活更早看得到、用來推測臨床效益的指標 |
| 風險比 | hazard ratio, HR | 兩組事件發生速率的比值；小於 1 表示試驗組風險較低 |
| 里程碑存活率 | landmark survival rate | 某個固定時間點（例如 5 年）還存活的比例 |
| 交叉治療 | crossover | 對照組病人惡化後改用試驗藥 |
| 不劣性試驗 | non-inferiority trial | 證明新治療沒有比標準治療差超過事先設定界限的試驗 |
| 固體腫瘤反應評估標準 | Response Evaluation Criteria in Solid Tumours, RECIST | 用影像上病灶直徑總和的變化判定 CR、PR、SD、PD 的標準 |
| 假性惡化 | pseudoprogression | 免疫治療後影像先變大或出現新病灶，之後才縮小 |
| 未確認／已確認的惡化 | iUPD／iCPD | iRECIST 的用語：第一次惡化先記 iUPD，4–8 週後確認才是 iCPD |
| 術前治療／術後輔助治療 | neoadjuvant／adjuvant therapy | 手術前或手術後給的全身性治療，目標都是提高治癒機會 |
| 治療線別 | line of therapy | 晚期疾病依序使用的第幾個全身性治療 |
| 抗體藥物複合體 | antibody-drug conjugate, ADC | 抗體經連接子接上細胞毒性載藥 |
| 免疫檢查點抑制劑 | immune checkpoint inhibitor, ICI | 阻斷 CTLA-4 或 PD-1／PD-L1、放開 T 細胞煞車的抗體 |
| 免疫相關不良事件 | immune-related adverse event, irAE | 免疫治療活化的免疫系統攻擊正常器官造成的副作用 |
| 不分癌別的適應症 | tumour-agnostic indication | 只看 biomarker、不看原發部位的適應症 |
| 後天抗藥 | acquired resistance | 治療原本有效，之後腫瘤再度生長 |
| 組織型轉化 | histologic transformation | 腫瘤在治療壓力下變成另一種組織型，例如轉成小細胞癌 |
| 不良事件常用術語標準 | Common Terminology Criteria for Adverse Events, CTCAE | 把副作用分成 1 到 5 級的共同標準 |

---

## 10. 自我測驗

**Q1.** 48 歲女性，HER2 陽性乳癌，準備開始含 trastuzumab 的治療。專師發現病歷裡沒有心臟超音波報告。下列哪一個說明最正確？

A. trastuzumab 是抗體不是化療，不需要基線檢查　B. 只有出現症狀時才需要做心臟超音波　C. trastuzumab 的樞紐試驗就看到心臟功能不全，併用 anthracycline 時最高，治療前要有基線 LVEF　D. 心臟毒性只和累積劑量有關，前幾個週期不必檢查

<details>
<summary>答案與詳解</summary>

**答案：C**。Slamon 等的試驗中，trastuzumab 併用 anthracycline 與 cyclophosphamide 的病人有 27% 發生 NYHA III–IV 級心臟功能不全（Slamon et al., 2001）。這是「開藥前先做什麼」直接來自藥物發現史的例子。監測時程與暫停規則見乳癌章 6.2。

</details>

**Q2.** 某新藥的第一期試驗採用 3+3 設計。第三個劑量階的 3 位病人中，1 位在第一個週期發生劑量限制毒性（DLT）。下一步是什麼？

A. 直接升到第四個劑量階　B. 在同一個劑量階再收 3 位病人　C. 宣布第三階為最大耐受劑量，試驗結束　D. 退回第二階，並把第二階訂為第二期建議劑量

<details>
<summary>答案與詳解</summary>

**答案：B**。3 人中 1 人發生 DLT，要在同一劑量再收 3 人；同一劑量的 3–6 人中有 2 人以上發生 DLT 才停止升階（Le Tourneau et al., 2009）。A 是 3 人都沒有 DLT 時的做法；C、D 是還沒有足夠資料就下結論。

</details>

**Q3.** 病人拿著新聞來問：「這個藥美國已經加速核准了，是不是代表可以讓我活比較久？」最恰當的回答是？

A. 是，FDA 核准就代表已經證明延長存活　B. 加速核准的藥之後都會被撤回，不建議使用　C. 加速核准代表第三期試驗已經完成　D. 加速核准多半依據腫瘤縮小的比例，能不能延長存活要等確認性試驗；而且台灣是否有藥證與給付要另外確認

<details>
<summary>答案與詳解</summary>

**答案：D**。加速核准依據的是合理推測能預測臨床效益的替代終點，條件是之後要確認效益（Oncology Center of Excellence et al., 2018）。FDA 回顧 93 個腫瘤與血液的加速核准適應症，87% 以反應率為依據，55% 已確認效益，5% 被撤回（Beaver et al., 2018）。台灣藥證與給付請見各癌別章第 9 段。

</details>

**Q4.** MPACT 試驗中，gemcitabine 加 nab-paclitaxel 對單用 gemcitabine 的死亡風險比（HR）為 0.72（95% CI 0.62–0.83），中位存活 8.5 對 6.7 個月。下列哪一個說法正確？

A. 合併治療組的病人平均多活 28%　B. 追蹤期間每個時間點，合併治療組的死亡風險大約低 28%；中位存活差 1.8 個月　C. 有 72% 的病人對合併治療有反應　D. 信賴區間沒有包含 0，所以達到統計顯著

<details>
<summary>答案與詳解</summary>

**答案：B**。HR 是兩組事件發生速率的比值，不代表時間長短；時間要看中位數與存活率（Spruance et al., 2004）。MPACT 的 1 年存活率是 35% 對 22%（Von Hoff et al., 2013）。D 錯在 HR 的信賴區間要看有沒有包含 1，不是 0。

</details>

**Q5.** FLAURA 試驗中，osimertinib 與第一代 EGFR-TKI 的客觀反應率是 80% 對 76%，PFS 是 18.9 對 10.2 個月。這組數字說明什麼？

A. 兩種藥的療效相同　B. 反應率沒有差異，所以 PFS 的差異不可信　C. 反應率只告訴你腫瘤有沒有縮，沒有告訴你能維持多久；要搭配反應持續時間與 PFS 一起看　D. 反應率比 PFS 更能代表整體存活

<details>
<summary>答案與詳解</summary>

**答案：C**。兩組腫瘤縮小的比例相近，但 osimertinib 的反應持續時間是 17.2 個月，對照組 8.5 個月（Soria et al., 2018）。ORR 是藥物活性的直接指標，但不含時間的資訊（Oncology Center of Excellence et al., 2018）。

</details>

**Q6.** 依 RECIST 1.1，病人目標病灶直徑總和的基準值是 60 mm，治療中最小值是 30 mm，這次是 37 mm，沒有新病灶，非目標病灶沒有明確惡化。這次的評估是？

A. CR　B. PR，因為比基準值小了 38%　C. SD，因為增加不到 30%　D. PD

<details>
<summary>答案與詳解</summary>

**答案：D**。PD 要和最小值比：從 30 mm 增加到 37 mm，增加 23%（≥20%），絕對值增加 7 mm（≥5 mm），兩個條件都符合（Eisenhauer et al., 2009）。B 是最常見的錯誤：PR 和基準值比，PD 和最小值比。

</details>

**Q7.** 轉移性黑色素瘤病人使用免疫檢查點抑制劑 9 週，第一次 CT 顯示目標病灶總和比基準值增加 25%（增加 12 mm）。病人體能狀態與 9 週前相同，沒有新症狀，也不需要增加止痛藥。依 iRECIST 的原則，最合理的處理是？

A. 記為 iCPD，立刻換藥　B. 記為 iSD，照原訂時程 12 週後再評估　C. 記為 iUPD；病人臨床穩定，與病人討論後可繼續治療，4–8 週後再做影像確認　D. 影像不可信，改用腫瘤標記判斷

<details>
<summary>答案與詳解</summary>

**答案：C**。第一次符合 RECIST 1.1 的惡化先記為 iUPD；臨床穩定者可繼續治療，4–8 週後確認，目標病灶總和再增加 ≥5 mm 等條件成立才是 iCPD（Seymour et al., 2017）。要不要繼續，由病人與團隊決定。

</details>

**Q8.** 承上題，如果同一位病人這 9 週體重下降、疼痛加劇需要增加嗎啡劑量、ECOG 從 1 退到 2，處理原則應該是？

A. 仍然等 4–8 週確認，因為免疫治療常見假性惡化　B. 病人不符合臨床穩定，應視為真的惡化並盡快討論下一步治療　C. 加倍免疫治療的劑量　D. 先停止所有影像檢查

<details>
<summary>答案與詳解</summary>

**答案：B**。假性惡化並不常見（通常 ≤10%）。只有體能沒變差、症狀沒加重、不需要加強症狀處置的病人，才適合等待確認；繼續使用無效的藥會耽誤後續治療（Seymour et al., 2017）。

</details>

**Q9.** 藥局新進一個藥，學名的第一個字以「-tatug」結尾，第二個字是「deruxtecan」。只看名字，可以推測它是什麼？

A. 一個打腫瘤標靶的抗體接上第一型拓撲異構酶抑制劑的 ADC　B. 口服的酪胺酸激酶抑制劑　C. 雙特異性抗體　D. 免疫檢查點抑制劑

<details>
<summary>答案與詳解</summary>

**答案：A**。-ta- 是腫瘤標靶的字節，-tug 是 2021 年新制中「未修飾免疫球蛋白」的字尾；第二個字 deruxtecan 屬 -tecan，即第一型拓撲異構酶抑制劑（World Health Organization, 2024）。雙特異性抗體的新字尾是 -mig；酪胺酸激酶抑制劑是 -tinib。

</details>

**Q10.** 醫囑開的是 trastuzumab deruxtecan。藥局送來的藥袋標示 trastuzumab emtansine，藥師說：「都是 trastuzumab 的 ADC，劑量差不多。」專師應該怎麼做？

A. 兩者第一個字相同，可以互相取代　B. 兩者載藥不同、劑量與毒性都不同，不可取代；暫不給藥，退回藥局並通知開立醫囑的醫師　C. 先給藥，之後再補開醫囑　D. 把劑量換算後給藥

<details>
<summary>答案與詳解</summary>

**答案：B**。emtansine（DM1）是破壞微小管的 maytansinoid，deruxtecan 是第一型拓撲異構酶抑制劑（Drago et al., 2021；von Minckwitz et al., 2019）。兩者是不同的藥；T-DXd 還有間質性肺病的風險（Modi et al., 2022）。ADC 的名字要把兩個字都核對完。

</details>

**Q11.** 62 歲不吸菸女性，新診斷第 IV 期肺腺癌，PD-L1 80%，EGFR 等基因檢測結果要再等一週。住院醫師想今天就開 pembrolizumab。專師最應該提醒的是？

A. PD-L1 ≥50% 就可以開，不必等基因報告　B. 先打一劑沒有關係，報告出來再換藥　C. 等基因報告；如果是 EGFR 突變，先用免疫治療再接 osimertinib，3 個月內發生嚴重免疫相關不良事件的比例達 24%　D. 免疫治療與標靶藥同時開始最有效

<details>
<summary>答案與詳解</summary>

**答案：C**。Schoenfeld 等的研究中，PD-(L)1 抑制劑之後接 osimertinib 的病人 15% 發生 3–4 級免疫相關不良事件，間隔 3 個月內者 24%；先 osimertinib 再免疫治療則沒有觀察到（Schoenfeld et al., 2019）。病人路徑的第 5 步（biomarker）要在第 9 步（選處方）之前完成。

</details>

**Q12.** 不可切除的第 III 期非小細胞肺癌病人，完成同步化放療後沒有惡化，接著使用 durvalumab 最多 12 個月。這段 durvalumab 治療稱為什麼？

A. 鞏固治療（consolidation）　B. 術前治療（neoadjuvant）　C. 第二線治療　D. 緩和性治療

<details>
<summary>答案與詳解</summary>

**答案：A**。PACIFIC 試驗在根治性化放療後、沒有惡化的病人使用 durvalumab 作為鞏固治療（Antonia et al., 2017），5 年存活率 42.9% 對 33.4%（Spigel et al., 2022）。沒有手術，所以不是術前治療；病人沒有惡化，所以不是第二線。

</details>

**Q13.** EGFR exon 19 deletion 的肺腺癌病人，osimertinib 治療 20 個月後影像惡化，血液 ctDNA 沒有驗到新的抗藥突變。主治醫師安排重新切片。最重要的理由是？

A. 確認原本的 EGFR 突變是否消失　B. 切片可以縮小腫瘤　C. 健保規定每次惡化都要切片　D. 有些抗藥機轉（例如轉化成小細胞癌）只有組織檢查看得出來，而且會改變治療

<details>
<summary>答案與詳解</summary>

**答案：D**。Sequist 等重新切片 37 位 EGFR-TKI 抗藥的病人，14% 轉成小細胞癌，而且所有腫瘤都保留原本的 EGFR 突變（Sequist et al., 2011）。組織型轉化之後改用小細胞癌的化療（Vasan et al., 2019）。A 不對：原本的突變通常還在。

</details>

**Q14.** 一項研究發現「免疫治療期間發生甲狀腺功能異常的病人，存活比沒有發生的人長」。判讀這個結論時，最需要注意哪一種偏差？

A. 交叉治療　B. 發表偏差　C. 不死時間偏差：病人要先活得夠久，才有機會發生這個副作用　D. 不劣性界限訂得太寬

<details>
<summary>答案與詳解</summary>

**答案：C**。用追蹤期間才發生的事件（反應、毒性）分組再比較存活，會讓「發生事件」那一組看起來比較好，稱為 guarantee-time bias 或不死時間偏差；要用里程碑分析等方法校正（Giobbie-Hurder et al., 2013）。

</details>

**Q15.** 門診化療的病人說：「上次打完吐了三天、幾乎沒吃，我想說忍一忍就好，沒有打電話。」專師衛教的重點應該是？

A. 告訴病人症狀要早點回報；有隨機試驗顯示，化療期間定期回報症狀、由護理師及早處理的病人，存活比一般照護長　B. 稱讚病人忍耐，請他下次也盡量不要打擾醫護人員　C. 告訴病人嘔吐是化療有效的表現　D. 直接幫病人把下次化療取消

<details>
<summary>答案與詳解</summary>

**答案：A**。Basch 等的隨機試驗中，定期回報症狀、嚴重時自動通知護理師的病人，中位存活 31.2 個月，一般照護組 26.0 個月（Basch et al., 2017）。接著要做的是把這次的嘔吐分級、調整止吐處方（支持性照護第 1 節），並把聯絡方式再教一次。

</details>

---

## 11. 參考文獻

Antonia, S. J., Villegas, A., Daniel, D., Vicente, D., Murakami, S., Hui, R., Yokoi, T., Chiappori, A., Lee, K. H., de Wit, M., Cho, B. C., Bourhaba, M., Quantin, X., Tokito, T., Mekhail, T., Planchard, D., Kim, Y.-C., Karapetis, C. S., Hiret, S., . . . Özgüroğlu, M. (2017). Durvalumab after chemoradiotherapy in stage III non-small-cell lung cancer. *New England Journal of Medicine, 377*(20), 1919–1929. https://doi.org/10.1056/NEJMoa1709937（PMID: 28885881）

Assmann, S. F., Pocock, S. J., Enos, L. E., & Kasten, L. E. (2000). Subgroup analysis and other (mis)uses of baseline data in clinical trials. *The Lancet, 355*(9209), 1064–1069. https://doi.org/10.1016/S0140-6736(00)02039-0（PMID: 10744093）

Basch, E., Deal, A. M., Dueck, A. C., Scher, H. I., Kris, M. G., Hudis, C., & Schrag, D. (2017). Overall survival results of a trial assessing patient-reported outcomes for symptom monitoring during routine cancer treatment. *JAMA, 318*(2), 197–198. https://doi.org/10.1001/jama.2017.7156（PMID: 28586821）

Beaver, J. A., Howie, L. J., Pelosof, L., Kim, T., Liu, J., Goldberg, K. B., Sridhara, R., Blumenthal, G. M., Farrell, A. T., Keegan, P., Pazdur, R., & Kluetz, P. G. (2018). A 25-year experience of US Food and Drug Administration accelerated approval of malignant hematology and oncology drugs and biologics: A review. *JAMA Oncology, 4*(6), 849–856. https://doi.org/10.1001/jamaoncol.2017.5618（PMID: 29494733）

Bonadonna, G., Brusamolino, E., Valagussa, P., Rossi, A., Brugnatelli, L., Brambilla, C., De Lena, M., Tancini, G., Bajetta, E., Musumeci, R., & Veronesi, U. (1976). Combination chemotherapy as an adjuvant treatment in operable breast cancer. *New England Journal of Medicine, 294*(8), 405–410. https://doi.org/10.1056/NEJM197602192940801（PMID: 1246307）

Brown, D. G., Wobst, H. J., Kapoor, A., Kenna, L. A., & Southall, N. (2022). Clinical development times for innovative drugs. *Nature Reviews Drug Discovery, 21*(11), 793–794. https://doi.org/10.1038/d41573-021-00190-9（PMID: 34759309）

Chen, T.-T. (2013). Statistical issues and challenges in immuno-oncology. *Journal for ImmunoTherapy of Cancer, 1*, Article 18. https://doi.org/10.1186/2051-1426-1-18（PMID: 24829754）

Christakis, P. (2011). The birth of chemotherapy at Yale. Bicentennial lecture series: Surgery Grand Round. *Yale Journal of Biology and Medicine, 84*(2), 169–172. https://pmc.ncbi.nlm.nih.gov/articles/PMC3117414/（PMID: 21698052）

Chuk, M. K., Chang, J. T., Theoret, M. R., Sampene, E., He, K., Weis, S. L., Helms, W. S., Jin, R., Li, H., Yu, J., Zhao, H., Zhao, L., Paciga, M., Schmiel, D., Rawat, R., Keegan, P., & Pazdur, R. (2017). FDA approval summary: Accelerated approval of pembrolizumab for second-line treatment of metastatic melanoma. *Clinical Cancer Research, 23*(19), 5666–5670. https://doi.org/10.1158/1078-0432.CCR-16-0663（PMID: 28235882）

Cohen, M. H., Williams, G., Johnson, J. R., Duan, J., Gobburu, J., Rahman, A., Benson, K., Leighton, J., Kim, S. K., Wood, R., Rothmann, M., Chen, G., U, K. M., Staten, A. M., & Pazdur, R. (2002). Approval summary for imatinib mesylate capsules in the treatment of chronic myelogenous leukemia. *Clinical Cancer Research, 8*(5), 935–942.（PMID: 12006504）

Cole, M. P., Jones, C. T., & Todd, I. D. (1971). A new anti-oestrogenic agent in late breast cancer: An early clinical appraisal of ICI46474. *British Journal of Cancer, 25*(2), 270–275. https://doi.org/10.1038/bjc.1971.33（PMID: 5115829）

Cortazar, P., Zhang, L., Untch, M., Mehta, K., Costantino, J. P., Wolmark, N., Bonnefoi, H., Cameron, D., Gianni, L., Valagussa, P., Swain, S. M., Prowell, T., Loibl, S., Wickerham, D. L., Bogaerts, J., Baselga, J., Perou, C., Blumenthal, G., Blohmer, J., . . . von Minckwitz, G. (2014). Pathological complete response and long-term clinical benefit in breast cancer: The CTNeoBC pooled analysis. *The Lancet, 384*(9938), 164–172. https://doi.org/10.1016/S0140-6736(13)62422-8（PMID: 24529560）

de Langen, A. J., Johnson, M. L., Mazieres, J., Dingemans, A.-M. C., Mountzios, G., Pless, M., Wolf, J., Schuler, M., Lena, H., Skoulidis, F., Yoneshima, Y., Kim, S.-W., Linardou, H., Novello, S., van der Wekken, A. J., Chen, Y., Peters, S., Felip, E., Solomon, B. J., . . . Paz-Ares, L. (2023). Sotorasib versus docetaxel for previously treated non-small-cell lung cancer with KRASG12C mutation: A randomised, open-label, phase 3 trial. *The Lancet, 401*(10378), 733–746. https://doi.org/10.1016/S0140-6736(23)00221-0（PMID: 36764316）

DeVita, V. T., & Chu, E. (2008). A history of cancer chemotherapy. *Cancer Research, 68*(21), 8643–8653. https://doi.org/10.1158/0008-5472.CAN-07-6611（PMID: 18974103）

DeVita, V. T., Serpick, A. A., & Carbone, P. P. (1970). Combination chemotherapy in the treatment of advanced Hodgkin's disease. *Annals of Internal Medicine, 73*(6), 881–895. https://doi.org/10.7326/0003-4819-73-6-881（PMID: 5525541）

DeVita, V. T., Simon, R. M., Hubbard, S. M., Young, R. C., Berard, C. W., Moxley, J. H., Frei, E., Carbone, P. P., & Canellos, G. P. (1980). Curability of advanced Hodgkin's disease with chemotherapy: Long-term follow-up of MOPP-treated patients at the National Cancer Institute. *Annals of Internal Medicine, 92*(5), 587–595. https://doi.org/10.7326/0003-4819-92-5-587（PMID: 6892984）

Drago, J. Z., Modi, S., & Chandarlapaty, S. (2021). Unlocking the potential of antibody-drug conjugates for cancer therapy. *Nature Reviews Clinical Oncology, 18*(6), 327–344. https://doi.org/10.1038/s41571-021-00470-8（PMID: 33558752）

Drilon, A., Laetsch, T. W., Kummar, S., DuBois, S. G., Lassen, U. N., Demetri, G. D., Nathenson, M., Doebele, R. C., Farago, A. F., Pappo, A. S., Turpin, B., Dowlati, A., Brose, M. S., Mascarenhas, L., Federman, N., Berlin, J., El-Deiry, W. S., Baik, C., Deeken, J., . . . Hyman, D. M. (2018). Efficacy of larotrectinib in TRK fusion-positive cancers in adults and children. *New England Journal of Medicine, 378*(8), 731–739. https://doi.org/10.1056/NEJMoa1714448（PMID: 29466156）

Druker, B. J., Talpaz, M., Resta, D. J., Peng, B., Buchdunger, E., Ford, J. M., Lydon, N. B., Kantarjian, H., Capdeville, R., Ohno-Jones, S., & Sawyers, C. L. (2001). Efficacy and safety of a specific inhibitor of the BCR-ABL tyrosine kinase in chronic myeloid leukemia. *New England Journal of Medicine, 344*(14), 1031–1037. https://doi.org/10.1056/NEJM200104053441401（PMID: 11287972）

Earl, H. M., Hiller, L., Vallier, A.-L., Loi, S., McAdam, K., Hughes-Davies, L., Harnett, A. N., Ah-See, M.-L., Simcock, R., Rea, D., Raj, S., Woodings, P., Harries, M., Howe, D., Raynes, K., Higgins, H. B., Wilcox, M., Plummer, C., Mansi, J., . . . Dunn, J. A. (2019). 6 versus 12 months of adjuvant trastuzumab for HER2-positive early breast cancer (PERSEPHONE): 4-year disease-free survival results of a randomised phase 3 non-inferiority trial. *The Lancet, 393*(10191), 2599–2612. https://doi.org/10.1016/S0140-6736(19)30650-6（PMID: 31178152）

Einhorn, L. H., & Donohue, J. (1977). Cis-diamminedichloroplatinum, vinblastine, and bleomycin combination chemotherapy in disseminated testicular cancer. *Annals of Internal Medicine, 87*(3), 293–298. https://doi.org/10.7326/0003-4819-87-3-293（PMID: 71004）

Eisenhauer, E. A., Therasse, P., Bogaerts, J., Schwartz, L. H., Sargent, D., Ford, R., Dancey, J., Arbuck, S., Gwyther, S., Mooney, M., Rubinstein, L., Shankar, L., Dodd, L., Kaplan, R., Lacombe, D., & Verweij, J. (2009). New response evaluation criteria in solid tumours: Revised RECIST guideline (version 1.1). *European Journal of Cancer, 45*(2), 228–247. https://doi.org/10.1016/j.ejca.2008.10.026（PMID: 19097774）

Engelman, J. A., Zejnullahu, K., Mitsudomi, T., Song, Y., Hyland, C., Park, J. O., Lindeman, N., Gale, C. M., Zhao, X., Christensen, J., Kosaka, T., Holmes, A. J., Rogers, A. M., Cappuzzo, F., Mok, T., Lee, C., Johnson, B. E., Cantley, L. C., & Jänne, P. A. (2007). MET amplification leads to gefitinib resistance in lung cancer by activating ERBB3 signaling. *Science, 316*(5827), 1039–1043. https://doi.org/10.1126/science.1141478（PMID: 17463250）

Falzone, L., Salomone, S., & Libra, M. (2018). Evolution of cancer pharmacological treatments at the turn of the third millennium. *Frontiers in Pharmacology, 9*, Article 1300. https://doi.org/10.3389/fphar.2018.01300（PMID: 30483135）

Farber, S., Diamond, L. K., Mercer, R. D., Sylvester, R. F., Jr., & Wolff, J. A. (1948). Temporary remissions in acute leukemia in children produced by folic acid antagonist, 4-aminopteroyl-glutamic acid (aminopterin). *New England Journal of Medicine, 238*(23), 787–793. https://doi.org/10.1056/NEJM194806032382301（PMID: 18860765）

Fisher, B., Carbone, P., Economou, S. G., Frelick, R., Glass, A., Lerner, H., Redmond, C., Zelen, M., Band, P., Katrych, D. L., Wolmark, N., & Fisher, E. R. (1975). L-phenylalanine mustard (L-PAM) in the management of primary breast cancer: A report of early findings. *New England Journal of Medicine, 292*(3), 117–122. https://doi.org/10.1056/NEJM197501162920301（PMID: 1105174）

Food and Drug Administration. (2018, January 4). *Step 3: Clinical research*. U.S. Department of Health and Human Services. https://www.fda.gov/patients/drug-development-process/step-3-clinical-research

Food and Drug Administration. (2023, June 12). *Fast track, breakthrough therapy, accelerated approval, priority review*. U.S. Department of Health and Human Services. https://www.fda.gov/patients/learn-about-drug-and-device-approvals/fast-track-breakthrough-therapy-accelerated-approval-priority-review

Fourie Zirkelbach, J., Shah, M., Vallejo, J., Cheng, J., Ayyoub, A., Liu, J., Hudson, R., Sridhara, R., Ison, G., Amiri-Kordestani, L., Tang, S., Gwise, T., Rahman, A., Pazdur, R., & Theoret, M. R. (2022). Improving dose-optimization processes used in oncology drug development to minimize toxicity and maximize benefit to patients. *Journal of Clinical Oncology, 40*(30), 3489–3500. https://doi.org/10.1200/JCO.22.00371（PMID: 36095296）

Gandhi, L., Rodríguez-Abreu, D., Gadgeel, S., Esteban, E., Felip, E., De Angelis, F., Domine, M., Clingan, P., Hochmair, M. J., Powell, S. F., Cheng, S. Y.-S., Bischoff, H. G., Peled, N., Grossi, F., Jennens, R. R., Reck, M., Hui, R., Garon, E. B., Boyer, M., . . . Garassino, M. C. (2018). Pembrolizumab plus chemotherapy in metastatic non-small-cell lung cancer. *New England Journal of Medicine, 378*(22), 2078–2092. https://doi.org/10.1056/NEJMoa1801005（PMID: 29658856）

Garassino, M. C., Gadgeel, S., Speranza, G., Felip, E., Esteban, E., Dómine, M., Hochmair, M. J., Powell, S. F., Bischoff, H. G., Peled, N., Grossi, F., Jennens, R. R., Reck, M., Hui, R., Garon, E. B., Kurata, T., Gray, J. E., Schwarzenberger, P., Jensen, E., . . . Rodríguez-Abreu, D. (2023). Pembrolizumab plus pemetrexed and platinum in nonsquamous non-small-cell lung cancer: 5-year outcomes from the phase 3 KEYNOTE-189 study. *Journal of Clinical Oncology, 41*(11), 1992–1998. https://doi.org/10.1200/JCO.22.01989（PMID: 36809080）

Gilman, A., & Philips, F. S. (1946). The biological actions and therapeutic applications of the B-chloroethyl amines and sulfides. *Science, 103*(2675), 409–436. https://doi.org/10.1126/science.103.2675.409（PMID: 17751251）

Giobbie-Hurder, A., Gelber, R. D., & Regan, M. M. (2013). Challenges of guarantee-time bias. *Journal of Clinical Oncology, 31*(23), 2963–2969. https://doi.org/10.1200/JCO.2013.49.5283（PMID: 23835712）

Goldie, J. H., & Coldman, A. J. (1979). A mathematic model for relating the drug sensitivity of tumors to their spontaneous mutation rate. *Cancer Treatment Reports, 63*(11–12), 1727–1733.（PMID: 526911）

Goodman, L. S., Wintrobe, M. M., Dameshek, W., Goodman, M. J., Gilman, A., & McLennan, M. T. (1946). Nitrogen mustard therapy: Use of methyl-bis(beta-chloroethyl)amine hydrochloride and tris(beta-chloroethyl)amine hydrochloride for Hodgkin's disease, lymphosarcoma, leukemia and certain allied and miscellaneous disorders. *Journal of the American Medical Association, 132*(3), 126–132. https://doi.org/10.1001/jama.1946.02870380008004（PMID: 20997191）

Gottesman, M. M., Fojo, T., & Bates, S. E. (2002). Multidrug resistance in cancer: Role of ATP-dependent transporters. *Nature Reviews Cancer, 2*(1), 48–58. https://doi.org/10.1038/nrc706（PMID: 11902585）

Guimaraes Koch, S. S., Thorpe, R., Kawasaki, N., Lefranc, M.-P., Malan, S., Martin, A. C. R., Mignot, G., Plückthun, A., Rizzi, M., Shubat, S., Weisser, K., & Balocco, R. (2022). International nonproprietary names for monoclonal antibodies: An evolving nomenclature system. *mAbs, 14*(1), Article 2075078. https://doi.org/10.1080/19420862.2022.2075078（PMID: 35584276）

Hodi, F. S., O'Day, S. J., McDermott, D. F., Weber, R. W., Sosman, J. A., Haanen, J. B., Gonzalez, R., Robert, C., Schadendorf, D., Hassel, J. C., Akerley, W., van den Eertwegh, A. J., Lutzky, J., Lorigan, P., Vaubel, J. M., Linette, G. P., Hogg, D., Ottensmeier, C. H., Lebbé, C., . . . Urba, W. J. (2010). Improved survival with ipilimumab in patients with metastatic melanoma. *New England Journal of Medicine, 363*(8), 711–723. https://doi.org/10.1056/NEJMoa1003466（PMID: 20525992）

Huang, P. W., & Chang, J. W. (2019). Immune checkpoint inhibitors win the 2018 Nobel Prize. *Biomedical Journal, 42*(5), 299–306. https://doi.org/10.1016/j.bj.2019.09.002（PMID: 31783990）

Hurwitz, H., Fehrenbacher, L., Novotny, W., Cartwright, T., Hainsworth, J., Heim, W., Berlin, J., Baron, A., Griffing, S., Holmgren, E., Ferrara, N., Fyfe, G., Rogers, B., Ross, R., & Kabbinavar, F. (2004). Bevacizumab plus irinotecan, fluorouracil, and leucovorin for metastatic colorectal cancer. *New England Journal of Medicine, 350*(23), 2335–2342. https://doi.org/10.1056/NEJMoa032691（PMID: 15175435）

Jordan, V. C. (2006). Tamoxifen (ICI46,474) as a targeted therapy to treat and prevent breast cancer. *British Journal of Pharmacology, 147*(Suppl. 1), S269–S276. https://doi.org/10.1038/sj.bjp.0706399（PMID: 16402113）

Kobayashi, S., Boggon, T. J., Dayaram, T., Jänne, P. A., Kocher, O., Meyerson, M., Johnson, B. E., Eck, M. J., Tenen, D. G., & Halmos, B. (2005). EGFR mutation and resistance of non-small-cell lung cancer to gefitinib. *New England Journal of Medicine, 352*(8), 786–792. https://doi.org/10.1056/NEJMoa044238（PMID: 15728811）

Le, D. T., Uram, J. N., Wang, H., Bartlett, B. R., Kemberling, H., Eyring, A. D., Skora, A. D., Luber, B. S., Azad, N. S., Laheru, D., Biedrzycki, B., Donehower, R. C., Zaheer, A., Fisher, G. A., Crocenzi, T. S., Lee, J. J., Duffy, S. M., Goldberg, R. M., de la Chapelle, A., . . . Diaz, L. A. (2015). PD-1 blockade in tumors with mismatch-repair deficiency. *New England Journal of Medicine, 372*(26), 2509–2520. https://doi.org/10.1056/NEJMoa1500596（PMID: 26028255）

Le Tourneau, C., Lee, J. J., & Siu, L. L. (2009). Dose escalation methods in phase I cancer clinical trials. *Journal of the National Cancer Institute, 101*(10), 708–720. https://doi.org/10.1093/jnci/djp079（PMID: 19436029）

Leonetti, A., Sharma, S., Minari, R., Perego, P., Giovannetti, E., & Tiseo, M. (2019). Resistance mechanisms to osimertinib in EGFR-mutated non-small cell lung cancer. *British Journal of Cancer, 121*(9), 725–737. https://doi.org/10.1038/s41416-019-0573-8（PMID: 31564718）

Marcus, L., Lemery, S. J., Keegan, P., & Pazdur, R. (2019). FDA approval summary: Pembrolizumab for the treatment of microsatellite instability-high solid tumors. *Clinical Cancer Research, 25*(13), 3753–3758. https://doi.org/10.1158/1078-0432.CCR-18-4070（PMID: 30787022）

Maude, S. L., Laetsch, T. W., Buechner, J., Rives, S., Boyer, M., Bittencourt, H., Bader, P., Verneris, M. R., Stefanski, H. E., Myers, G. D., Qayed, M., De Moerloose, B., Hiramatsu, H., Schlis, K., Davis, K. L., Martin, P. L., Nemecek, E. R., Yanik, G. A., Peters, C., . . . Grupp, S. A. (2018). Tisagenlecleucel in children and young adults with B-cell lymphoblastic leukemia. *New England Journal of Medicine, 378*(5), 439–448. https://doi.org/10.1056/NEJMoa1709866（PMID: 29385370）

McLaughlin, P., Grillo-López, A. J., Link, B. K., Levy, R., Czuczman, M. S., Williams, M. E., Heyman, M. R., Bence-Bruckler, I., White, C. A., Cabanillas, F., Jain, V., Ho, A. D., Lister, J., Wey, K., Shen, D., & Dallaire, B. K. (1998). Rituximab chimeric anti-CD20 monoclonal antibody therapy for relapsed indolent lymphoma: Half of patients respond to a four-dose treatment program. *Journal of Clinical Oncology, 16*(8), 2825–2833. https://doi.org/10.1200/JCO.1998.16.8.2825（PMID: 9704735）

Modi, S., Jacot, W., Yamashita, T., Sohn, J., Vidal, M., Tokunaga, E., Tsurutani, J., Ueno, N. T., Prat, A., Chae, Y. S., Lee, K. S., Niikura, N., Park, Y. H., Xu, B., Wang, X., Gil-Gil, M., Li, W., Pierga, J.-Y., Im, S.-A., . . . Cameron, D. A. (2022). Trastuzumab deruxtecan in previously treated HER2-low advanced breast cancer. *New England Journal of Medicine, 387*(1), 9–20. https://doi.org/10.1056/NEJMoa2203690（PMID: 35665782）

Mok, T. S., Wu, Y.-L., Ahn, M.-J., Garassino, M. C., Kim, H. R., Ramalingam, S. S., Shepherd, F. A., He, Y., Akamatsu, H., Theelen, W. S. M. E., Lee, C. K., Sebastian, M., Templeton, A., Mann, H., Marotti, M., Ghiorghiu, S., & Papadimitrakopoulou, V. A. (2017). Osimertinib or platinum-pemetrexed in EGFR T790M-positive lung cancer. *New England Journal of Medicine, 376*(7), 629–640. https://doi.org/10.1056/NEJMoa1612674（PMID: 27959700）

Nakajima, E. C., Drezner, N., Li, X., Mishra-Kalyani, P. S., Liu, Y., Zhao, H., Bi, Y., Liu, J., Rahman, A., Wearne, E., Ojofeitimi, I., Hotaki, L. T., Spillman, D., Pazdur, R., Beaver, J. A., & Singh, H. (2022). FDA approval summary: Sotorasib for KRAS G12C-mutated metastatic NSCLC. *Clinical Cancer Research, 28*(8), 1482–1486. https://doi.org/10.1158/1078-0432.CCR-21-3074（PMID: 34903582）

Neuss, M. N., Gilmore, T. R., Belderson, K. M., Billett, A. L., Conti-Kalchik, T., Harvey, B. E., Hendricks, C., LeFebvre, K. B., Mangu, P. B., McNiff, K., Olsen, M., Schulmeister, L., Von Gehr, A., & Polovich, M. (2016). 2016 updated American Society of Clinical Oncology/Oncology Nursing Society chemotherapy administration safety standards, including standards for pediatric oncology. *Journal of Oncology Practice, 12*(12), 1262–1271. https://doi.org/10.1200/JOP.2016.017905（PMID: 27868581）

Nowell, P. C. (1976). The clonal evolution of tumor cell populations. *Science, 194*(4260), 23–28. https://doi.org/10.1126/science.959840（PMID: 959840）

Oken, M. M., Creech, R. H., Tormey, D. C., Horton, J., Davis, T. E., McFadden, E. T., & Carbone, P. P. (1982). Toxicity and response criteria of the Eastern Cooperative Oncology Group. *American Journal of Clinical Oncology, 5*(6), 649–655.（PMID: 7165009）

O'Leary, M. C., Lu, X., Huang, Y., Lin, X., Mahmood, I., Przepiorka, D., Gavin, D., Lee, S., Liu, K., George, B., Bryan, W., Theoret, M. R., & Pazdur, R. (2019). FDA approval summary: Tisagenlecleucel for treatment of patients with relapsed or refractory B-cell precursor acute lymphoblastic leukemia. *Clinical Cancer Research, 25*(4), 1142–1146. https://doi.org/10.1158/1078-0432.CCR-18-2035（PMID: 30309857）

Oncology Center of Excellence, Center for Drug Evaluation and Research, & Center for Biologics Evaluation and Research. (2018). *Clinical trial endpoints for the approval of cancer drugs and biologics: Guidance for industry*. U.S. Department of Health and Human Services, Food and Drug Administration. https://www.fda.gov/media/71195/download

Ostrem, J. M., Peters, U., Sos, M. L., Wells, J. A., & Shokat, K. M. (2013). K-Ras(G12C) inhibitors allosterically control GTP affinity and effector interactions. *Nature, 503*(7477), 548–551. https://doi.org/10.1038/nature12796（PMID: 24256730）

Parren, P. W. H. I., Carter, P. J., & Plückthun, A. (2017). Changes to International Nonproprietary Names for antibody therapeutics 2017 and beyond: Of mice, men and more. *mAbs, 9*(6), 898–906. https://doi.org/10.1080/19420862.2017.1341029（PMID: 28621572）

Piaggio, G., Elbourne, D. R., Pocock, S. J., Evans, S. J. W., Altman, D. G., & CONSORT Group. (2012). Reporting of noninferiority and equivalence randomized trials: Extension of the CONSORT 2010 statement. *JAMA, 308*(24), 2594–2604. https://doi.org/10.1001/jama.2012.87802（PMID: 23268518）

Prasad, V., Kim, C., Burotto, M., & Vandross, A. (2015). The strength of association between surrogate end points and survival in oncology: A systematic review of trial-level meta-analyses. *JAMA Internal Medicine, 175*(8), 1389–1398. https://doi.org/10.1001/jamainternmed.2015.2829（PMID: 26098871）

Ramalingam, S. S., Vansteenkiste, J., Planchard, D., Cho, B. C., Gray, J. E., Ohe, Y., Zhou, C., Reungwetwattana, T., Cheng, Y., Chewaskulyong, B., Shah, R., Cobo, M., Lee, K. H., Cheema, P., Tiseo, M., John, T., Lin, M.-C., Imamura, F., Kurata, T., . . . Soria, J.-C. (2020). Overall survival with osimertinib in untreated, EGFR-mutated advanced NSCLC. *New England Journal of Medicine, 382*(1), 41–50. https://doi.org/10.1056/NEJMoa1913662（PMID: 31751012）

Rosenberg, B., VanCamp, L., & Krigas, T. (1965). Inhibition of cell division in Escherichia coli by electrolysis products from a platinum electrode. *Nature, 205*, 698–699. https://doi.org/10.1038/205698a0（PMID: 14287410）

Rosenberg, B., VanCamp, L., Trosko, J. E., & Mansour, V. H. (1969). Platinum compounds: A new class of potent antitumour agents. *Nature, 222*(5191), 385–386. https://doi.org/10.1038/222385a0（PMID: 5782119）

Sartor, O., de Bono, J., Chi, K. N., Fizazi, K., Herrmann, K., Rahbar, K., Tagawa, S. T., Nordquist, L. T., Vaishampayan, N., El-Haddad, G., Park, C. H., Beer, T. M., Armour, A., Pérez-Contreras, W. J., DeSilvio, M., Kpamegan, E., Gericke, G., Messmann, R. A., Morris, M. J., . . . Krause, B. J. (2021). Lutetium-177-PSMA-617 for metastatic castration-resistant prostate cancer. *New England Journal of Medicine, 385*(12), 1091–1103. https://doi.org/10.1056/NEJMoa2107322（PMID: 34161051）

Schmid, P., Cortes, J., Pusztai, L., McArthur, H., Kümmel, S., Bergh, J., Denkert, C., Park, Y. H., Hui, R., Harbeck, N., Takahashi, M., Foukakis, T., Fasching, P. A., Cardoso, F., Untch, M., Jia, L., Karantza, V., Zhao, J., Aktan, G., . . . O'Shaughnessy, J. (2020). Pembrolizumab for early triple-negative breast cancer. *New England Journal of Medicine, 382*(9), 810–821. https://doi.org/10.1056/NEJMoa1910549（PMID: 32101663）

Schoenfeld, A. J., Arbour, K. C., Rizvi, H., Iqbal, A. N., Gadgeel, S. M., Girshman, J., Kris, M. G., Riely, G. J., Yu, H. A., & Hellmann, M. D. (2019). Severe immune-related adverse events are common with sequential PD-(L)1 blockade and osimertinib. *Annals of Oncology, 30*(5), 839–844. https://doi.org/10.1093/annonc/mdz077（PMID: 30847464）

Scott, L. J. (2019). Larotrectinib: First global approval. *Drugs, 79*(2), 201–206. https://doi.org/10.1007/s40265-018-1044-x（PMID: 30635837）

Sequist, L. V., Waltman, B. A., Dias-Santagata, D., Digumarthy, S., Turke, A. B., Fidias, P., Bergethon, K., Shaw, A. T., Gettinger, S., Cosper, A. K., Akhavanfard, S., Heist, R. S., Temel, J., Christensen, J. G., Wain, J. C., Lynch, T. J., Vernovsky, K., Mark, E. J., Lanuti, M., . . . Engelman, J. A. (2011). Genotypic and histological evolution of lung cancers acquiring resistance to EGFR inhibitors. *Science Translational Medicine, 3*(75), Article 75ra26. https://doi.org/10.1126/scitranslmed.3002003（PMID: 21430269）

Seymour, L., Bogaerts, J., Perrone, A., Ford, R., Schwartz, L. H., Mandrekar, S., Lin, N. U., Litière, S., Dancey, J., Chen, A., Hodi, F. S., Therasse, P., Hoekstra, O. S., Shankar, L. K., Wolchok, J. D., Ballinger, M., Caramella, C., de Vries, E. G. E., & RECIST working group. (2017). iRECIST: Guidelines for response criteria for use in trials testing immunotherapeutics. *The Lancet Oncology, 18*(3), e143–e152. https://doi.org/10.1016/S1470-2045(17)30074-8（PMID: 28271869）

Skoulidis, F., Li, B. T., Dy, G. K., Price, T. J., Falchook, G. S., Wolf, J., Italiano, A., Schuler, M., Borghaei, H., Barlesi, F., Kato, T., Curioni-Fontecedro, A., Sacher, A., Spira, A., Ramalingam, S. S., Takahashi, T., Besse, B., Anderson, A., Ang, A., . . . Govindan, R. (2021). Sotorasib for lung cancers with KRAS p.G12C mutation. *New England Journal of Medicine, 384*(25), 2371–2381. https://doi.org/10.1056/NEJMoa2103695（PMID: 34096690）

Slamon, D. J., Leyland-Jones, B., Shak, S., Fuchs, H., Paton, V., Bajamonde, A., Fleming, T., Eiermann, W., Wolter, J., Pegram, M., Baselga, J., & Norton, L. (2001). Use of chemotherapy plus a monoclonal antibody against HER2 for metastatic breast cancer that overexpresses HER2. *New England Journal of Medicine, 344*(11), 783–792. https://doi.org/10.1056/NEJM200103153441101（PMID: 11248153）

Soria, J.-C., Ohe, Y., Vansteenkiste, J., Reungwetwattana, T., Chewaskulyong, B., Lee, K. H., Dechaphunkul, A., Imamura, F., Nogami, N., Kurata, T., Okamoto, I., Zhou, C., Cho, B. C., Cheng, Y., Cho, E. K., Voon, P. J., Planchard, D., Su, W.-C., Gray, J. E., . . . Ramalingam, S. S. (2018). Osimertinib in untreated EGFR-mutated advanced non-small-cell lung cancer. *New England Journal of Medicine, 378*(2), 113–125. https://doi.org/10.1056/NEJMoa1713137（PMID: 29151359）

Spigel, D. R., Faivre-Finn, C., Gray, J. E., Vicente, D., Planchard, D., Paz-Ares, L., Vansteenkiste, J. F., Garassino, M. C., Hui, R., Quantin, X., Rimner, A., Wu, Y.-L., Özgüroğlu, M., Lee, K. H., Kato, T., de Wit, M., Kurata, T., Reck, M., Cho, B. C., . . . Antonia, S. J. (2022). Five-year survival outcomes from the PACIFIC trial: Durvalumab after chemoradiotherapy in stage III non-small-cell lung cancer. *Journal of Clinical Oncology, 40*(12), 1301–1311. https://doi.org/10.1200/JCO.21.01308（PMID: 35108059）

Spruance, S. L., Reid, J. E., Grace, M., & Samore, M. (2004). Hazard ratio in clinical trials. *Antimicrobial Agents and Chemotherapy, 48*(8), 2787–2792. https://doi.org/10.1128/AAC.48.8.2787-2792.2004（PMID: 15273082）

Temel, J. S., Greer, J. A., Muzikansky, A., Gallagher, E. R., Admane, S., Jackson, V. A., Dahlin, C. M., Blinderman, C. D., Jacobsen, J., Pirl, W. F., Billings, J. A., & Lynch, T. J. (2010). Early palliative care for patients with metastatic non-small-cell lung cancer. *New England Journal of Medicine, 363*(8), 733–742. https://doi.org/10.1056/NEJMoa1000678（PMID: 20818875）

Thress, K. S., Paweletz, C. P., Felip, E., Cho, B. C., Stetson, D., Dougherty, B., Lai, Z., Markovets, A., Vivancos, A., Kuang, Y., Ercan, D., Matthews, S. E., Cantarini, M., Barrett, J. C., Jänne, P. A., & Oxnard, G. R. (2015). Acquired EGFR C797S mutation mediates resistance to AZD9291 in non-small cell lung cancer harboring EGFR T790M. *Nature Medicine, 21*(6), 560–562. https://doi.org/10.1038/nm.3854（PMID: 25939061）

Vasan, N., Baselga, J., & Hyman, D. M. (2019). A view on drug resistance in cancer. *Nature, 575*(7782), 299–309. https://doi.org/10.1038/s41586-019-1730-1（PMID: 31723286）

Von Hoff, D. D., Ervin, T., Arena, F. P., Chiorean, E. G., Infante, J., Moore, M., Seay, T., Tjulandin, S. A., Ma, W. W., Saleh, M. N., Harris, M., Reni, M., Dowden, S., Laheru, D., Bahary, N., Ramanathan, R. K., Tabernero, J., Hidalgo, M., Goldstein, D., . . . Renschler, M. F. (2013). Increased survival in pancreatic cancer with nab-paclitaxel plus gemcitabine. *New England Journal of Medicine, 369*(18), 1691–1703. https://doi.org/10.1056/NEJMoa1304369（PMID: 24131140）

von Minckwitz, G., Huang, C.-S., Mano, M. S., Loibl, S., Mamounas, E. P., Untch, M., Wolmark, N., Rastogi, P., Schneeweiss, A., Redondo, A., Fischer, H. H., Jacot, W., Conlin, A. K., Arce-Salinas, C., Wapnir, I. L., Jackisch, C., DiGiovanna, M. P., Fasching, P. A., Crown, J. P., . . . Geyer, C. E., Jr. (2019). Trastuzumab emtansine for residual invasive HER2-positive breast cancer. *New England Journal of Medicine, 380*(7), 617–628. https://doi.org/10.1056/NEJMoa1814017（PMID: 30516102）

Wong, C. H., Siah, K. W., & Lo, A. W. (2019). Estimation of clinical trial success rates and related parameters. *Biostatistics, 20*(2), 273–286. https://doi.org/10.1093/biostatistics/kxx069（PMID: 29394327）

World Health Organization. (2024). *Use of stems in the selection of International Nonproprietary Names (INN) for pharmaceutical substances, 2024* (Stem book 2024). https://www.who.int/publications/i/item/9789240099388
