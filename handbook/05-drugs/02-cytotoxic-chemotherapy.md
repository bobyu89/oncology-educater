# 化療藥物（Cytotoxic Chemotherapy）

| 項目 | 本章依據 |
|------|---------|
| 發現史 | 原始論文（Goodman & Wintrobe, 1946; Farber et al., 1948; Heidelberger et al., 1957; Rosenberg et al., 1965; Wani et al., 1971）與史料回顧（DeVita & Chu, 2008; Christakis, 2011; Falzone et al., 2018） |
| 機轉、藥動、毒性 | 美國 FDA 仿單（DailyMed，2026-11-11 讀取；各藥的版本日期見[第 11 段](#11-參考文獻)）；S-1 沒有美國仿單，用歐盟 EMA 的 Teysuno 仿單 |
| 治療原則 | Log-kill（Skipper et al., 1964）、Goldie–Coldman（Goldie & Coldman, 1979）、Norton–Simon（Norton & Simon, 1977）、CALGB 9741（Citron et al., 2003）、EBCTCG 2019 統合分析 |
| 本章不重複的內容 | 處方劑量見各癌別章第 5 段；CTCAE 分級處置、解毒劑、外滲與止吐見共用章；健保給付與台灣藥證見各癌別章第 9 段（藥品給付規定 115/10/22 版） |
| 最後更新 | 2026-11-11 |

**這一章的結論先講：** 化療藥不認得癌細胞，它認得的是「正在複製 DNA 或正在分裂的細胞」，所以一類藥的機轉同時決定它殺哪一種細胞、先傷哪一個正常器官。照「類別 → 機轉 → 招牌毒性 → 給藥前要查什麼」這條線去記，比背個別藥名有用。

> 本手冊是學習用整理，不能取代原始指引、仿單、健保公告與院內規範。實際處方以主治醫師判斷與院內流程為準。

---

## 0. 速查卡

| 類別 | 代表藥 | 一句話機轉 | 招牌毒性 | 給藥前先看 |
|------|--------|-----------|---------|-----------|
| 烷化劑（alkylating agents） | cyclophosphamide、ifosfamide、dacarbazine、temozolomide | 把烷基接到 DNA 上，造成交聯與斷裂 | 骨髓抑制；出血性膀胱炎；ifosfamide 另有腦病變與腎毒性 | CBC、肌酸酐、尿液；ifosfamide 有沒有配 mesna 與水化 |
| 鉑類（platinum） | cisplatin、carboplatin、oxaliplatin | 鉑與 DNA 形成鏈內與鏈間交聯 | cisplatin：腎、耳、嘔吐；carboplatin：血小板；oxaliplatin：遇冷的神經症狀 | 腎功能（carboplatin 用 Calvert 公式）、電解質、神經症狀 |
| 抗代謝物（antimetabolites） | methotrexate、pemetrexed、5-FU、capecitabine、S-1、gemcitabine | 冒充葉酸或核苷，卡住 DNA 合成 | 黏膜炎、腹瀉、骨髓抑制；capecitabine 手足症候群 | 腎功能、DPYD、交互作用藥（NSAID、PPI、warfarin） |
| Topoisomerase I 抑制劑 | irinotecan、liposomal irinotecan、topotecan | 卡住 topoisomerase I 與 DNA 的複合物，複製時變成雙股斷裂 | irinotecan：早發與遲發腹瀉、嗜中性球低下；topotecan：骨髓抑制 | UGT1A1、膽紅素、ANC |
| Topoisomerase II 抑制劑 | doxorubicin、epirubicin、pegylated liposomal doxorubicin、etoposide | 卡住 topoisomerase II 與 DNA 的可切割複合物；anthracycline 還會嵌入 DNA | anthracycline：累積劑量相關的心肌病變、外滲壞死；etoposide：骨髓抑制 | 累積劑量、LVEF、膽紅素 |
| 抗微管藥（antimicrotubule agents） | vincristine、vinorelbine、paclitaxel、nab-paclitaxel、docetaxel、eribulin | vinca 與 eribulin 讓微管長不出來；taxane 讓微管拆不掉 | 周邊神經病變；paclitaxel 過敏；docetaxel 水腫；vincristine 便秘與腸阻塞 | 神經症狀、前置用藥、肝功能、CYP3A4 交互作用 |
| 其他 | bleomycin、dactinomycin、mitomycin、trabectedin | 各不相同：DNA 斷裂、抑制 RNA 合成、DNA 交聯、小溝烷化 | bleomycin：肺；mitomycin：延遲性骨髓抑制與 HUS；trabectedin：肝與橫紋肌溶解 | 累積劑量、呼吸症狀、肝功能與 CPK |

各格的出處在第 3、4、6 段逐項標註。

> [!IMPORTANT]
> **一類藥記一個器官**
> - Cisplatin 看腎與耳；carboplatin 看血小板；oxaliplatin 看神經（WG Critical Care, 2026; Natco, 2026; Sagent, 2025）。
> - Anthracycline 看心臟，而且要自己加總累積劑量（Pfizer, 2026）。
> - Bleomycin 看肺，總量超過 400 units 風險更高（Meitheal, 2026）。
> - Vinca 與 taxane 看神經；vincristine 只能靜脈給（Hospira, 2026）。
> - Ifosfamide 看膀胱、腦、腎，mesna 一定要配（Fresenius Kabi, 2026）。
> - 5-FU、capecitabine 開藥前想 DPYD；irinotecan 開藥前想 UGT1A1（Alembic, 2026; Actavis, 2025）。

---

## 1. 怎麼被發現的

**結論先講：** 化療藥的來源只有四條路：戰爭毒氣（烷化劑）、營養學（抗葉酸藥）、實驗室的意外（cisplatin）、大自然（植物、土壤細菌、海洋生物）。之後幾十年的工作，大多是把這些分子改得比較不毒、能口服，或送得更準。知道來源，就能解釋今天床邊的很多規矩。

### 1.1 時間軸

| 年份 | 事件 | 意義 |
|------|------|------|
| 1919 | Krumbhaar 報告芥子氣中毒的士兵白血球先升後降（Christakis, 2011） | 第一次有人注意到芥子氣的標靶是骨髓 |
| 1942 | Yale 的 Gilman 與 Goodman 做完兔子與小鼠實驗後，8 月 27 日第一位淋巴肉瘤病人接受 nitrogen mustard 靜脈注射（Christakis, 2011; Fenn & Udelsman, 2011） | 第一次靜脈化療：腫瘤縮小、很快復發、骨髓被打垮 |
| 1943 | 義大利 Bari 港空襲，超過 100 噸芥子氣意外外洩（Turner & Sapp, 2026; Alexander, 1947） | 傷患的醫學報告讓芥子類化合物對血球的作用更受注意 |
| 1946 | Nitrogen mustard 治療 Hodgkin 病、淋巴肉瘤與白血病的臨床結果在 JAMA 發表（Goodman & Wintrobe, 1946） | 戰時保密解除，化療正式進入醫學文獻 |
| 1948 | Farber 用葉酸拮抗劑 aminopterin 讓急性白血病兒童得到暫時緩解（Farber et al., 1948） | 第一個抗代謝物；之後由 methotrexate 接手 |
| 1957 | Heidelberger 等人發表氟化嘧啶，其中包括 5-fluorouracil（Heidelberger et al., 1957） | 第一個嘧啶類抗代謝物，至今仍是腸胃道癌的骨幹（Falzone et al., 2018） |
| 1959 | Cyclophosphamide 在美國核准（BluePoint, 2026） | 把 nitrogen mustard 做成「運送型」前驅藥，治療指數提高（Brock, 1989） |
| 1950 年代末 | 從長春花（Catharanthus roseus）找到 vinblastine 與 vincristine 兩個生物鹼（Noble, 1990; Falzone et al., 2018） | 第一類抗微管藥 |
| 1960 年代 | 從 Streptomyces peucetius 得到 daunorubicin，再從突變株得到 doxorubicin（Arcamone et al., 1969; Falzone et al., 2018） | Anthracycline 問世，心臟毒性也跟著來 |
| 1965 | Rosenberg 發現鉑電極的電解產物會抑制大腸桿菌分裂（Rosenberg et al., 1965） | Cisplatin 的意外發現 |
| 1966 | Wall 與 Wani 從喜樹（Camptotheca acuminata）分離出 camptothecin；同年日本發現 bleomycin（Falzone et al., 2018; Umezawa et al., 1966） | Topoisomerase I 抑制劑與 bleomycin 的起點 |
| 1971 | Wani 等人發表太平洋紫杉（Taxus brevifolia）中 taxol 的結構（Wani et al., 1971） | Paclitaxel 的起點 |
| 1974 | 高劑量 methotrexate 加 citrovorum factor（leucovorin）用於骨肉瘤術後輔助（Jaffe et al., 1974） | 「先下重藥、再救正常細胞」的做法成形 |
| 1977 | Cisplatin ＋ vinblastine ＋ bleomycin 治療轉移性睪丸癌，完全緩解 74%（Einhorn & Donohue, 1977） | 證明合併化療能治癒轉移性實體腫瘤 |
| 1978 | Cisplatin 獲美國 FDA 核准（Dasari & Tchounwou, 2014; WG Critical Care, 2026） | 第一個鉑類藥 |
| 1979 | Horwitz 團隊發現 taxol 會促進微管聚合（Schiff et al., 1979） | 和 vinca 相反的全新機轉 |
| 1985 | 證實 camptothecin 的標靶是 topoisomerase I（Hsiang et al., 1985） | 兩年後日本發表水溶性衍生物 CPT-11，即 irinotecan（Kunimoto et al., 1987） |
| 1989 | Calvert 公式發表：carboplatin 劑量 = 目標 AUC ×（GFR ＋ 25）（Calvert et al., 1989） | 劑量依腎功能計算，而不是依體表面積 |
| 1995 | Pegylated liposomal doxorubicin 成為第一個 FDA 核准的奈米藥物（Barenholz, 2012） | 化療進入「換包裝」的時代 |
| 1996 | Gemcitabine、irinotecan、topotecan、docetaxel 在美國核准（Meitheal, 2025; Actavis, 2025; Accord, 2025; Mylan, 2026） | 第二波天然物衍生物與核苷類似物 |
| 1998–2005 | Capecitabine（1998）、oxaliplatin（2002）、pemetrexed（2004）、nab-paclitaxel（2005）在美國核准（H2-Pharma, 2026; Sagent, 2025; Eli Lilly, 2023; Abraxis, 2022） | 口服前驅藥、第三代鉑類、多標靶抗葉酸藥、無溶劑紫杉醇 |
| 2010–2015 | Eribulin（2010）與 trabectedin（2015）在美國核准；liposomal irinotecan 於 2015 年核准用於胰臟癌（Eisai, 2025; Janssen, 2026; Thomas & Pommier, 2019） | 海洋生物來源的藥與脂質體劑型 |

表中的核准年份是美國仿單上的「Initial U.S. Approval」，不是台灣上市年份。台灣藥證與給付請見各癌別章第 9 段。

### 1.2 從毒氣到烷化劑

- **觀察**：一次大戰後就有人發現芥子氣會讓白血球大幅下降。二次大戰期間，美國政府委託 Yale 的藥理學家 Gilman 與 Goodman 研究 nitrogen mustard 的毒性。他們在兔子身上看到淋巴球與顆粒球下降，推想這也許能治療淋巴系統的腫瘤，並在移植淋巴瘤的小鼠身上看到腫瘤縮小（Christakis, 2011）。
- **第一位病人**：病歷上只寫 JD、1894 年出生的男性，淋巴肉瘤對放射治療已無效。1942 年 8 月 27 日起每天靜脈注射 0.1 mg/kg，共 10 天；第 5 劑後症狀改善，療程後切片找不到腫瘤。接著白血球與血小板下降、牙齦出血需要輸血；第 49 天腫瘤復發，再給藥的效果愈來愈短，第 96 天過世，解剖顯示骨髓極度再生不良。因為戰時保密，病歷上只寫「substance X」（Christakis, 2011; Fenn & Udelsman, 2011）。
- **Bari 事件**：1943 年 12 月 Bari 港遭空襲，一艘載有芥子氣彈的船被炸，毒氣外洩（Falzone et al., 2018; Turner & Sapp, 2026）。Alexander 的傷患醫學報告在 1947 年發表（Alexander, 1947）。時間上，Yale 的第一位病人比 Bari 事件早一年多。
- **改良**：nitrogen mustard 太活潑。Brock 等人把它做成沒有活性的「運送型」，進入體內再由酵素轉成「作用型」，這就是 cyclophosphamide 與 ifosfamide；後來再加上保護泌尿道的 mesna（Brock, 1989）。原本設想由癌細胞裡的 phosphamidase 活化，事後證明這個假說和藥效無關，真正讓它有選擇性的是代謝與 aldehyde dehydrogenase 的去活化（Emadi et al., 2009）。

**和今天的連結**：JD 的病程已經預告了化療的三件事：腫瘤會縮小、會復發（抗藥性）、骨髓會被壓垮。所以每個週期前都要看 CBC；ifosfamide 一定配 mesna（見[化療基礎第 11.6 節](../00-shared/01-chemo-basics.md#116-ifosfamide-安全摘要)）。

### 1.3 Farber、葉酸與 leucovorin 解救

- **觀察**：病理科醫師 Sidney Farber 注意到葉酸會刺激白血病細胞生長、讓病程加速，於是反過來想：葉酸的拮抗劑也許能讓癌細胞停下來（Miller, 2006）。
- **論文**：1948 年他在 NEJM 報告 aminopterin 讓急性白血病兒童得到暫時緩解（Farber et al., 1948）。之後毒性較低的 methotrexate（amethopterin）取代了 aminopterin（Falzone et al., 2018），美國仿單的首次核准年份是 1953 年（Accord, 2026）。
- **解救的概念**：methotrexate 抑制 dihydrofolate reductase（DHFR），細胞就沒有還原型葉酸可用（Accord, 2026）。Leucovorin（又叫 citrovorum factor、folinic acid）本身已是還原型葉酸，不需要經過 DHFR 就能用（Gland, 2026）。1974 年 Jaffe 等人把高劑量 methotrexate 加 citrovorum factor 用在骨肉瘤術後（Jaffe et al., 1974），這個做法延續到今天的 MAP 方案。

**和今天的連結**：
- 高劑量 methotrexate（≥ 500 mg/m²）一定要有 leucovorin 解救、水化與鹼化尿液（Howard et al., 2016; Accord, 2026）。病房流程見[肉瘤章 6.1](../04-sarcoma.md#61-高劑量-methotrexatehd-mtx完整病房流程)。
- Pemetrexed 也是抗葉酸藥。早期試驗發現治療前 homocysteine 偏高的病人容易出現嚴重毒性（Niyikiza et al., 2002）；惡性肋膜間皮瘤的第三期試驗在收了 117 人之後加上 folic acid 與維生素 B12，毒性明顯下降，存活沒有受影響（Vogelzang et al., 2003）。所以今天開 pemetrexed 前，一定先確認病人已經在吃 folic acid、打過 B12（Eli Lilly, 2023）。

> [!TIP]
> **葉酸是影印機的碳粉**
> 細胞要複製 DNA，就像影印機要碳粉；還原型葉酸就是碳粉。Methotrexate 把補碳粉的機器（DHFR）關掉，影印最勤快的細胞（癌細胞、骨髓、黏膜）最先停工。Leucovorin 是直接送來的現成碳粉，不必經過那台被關掉的機器，所以能救正常細胞。給得太晚救不回來，這是 leucovorin 要照時間表給的原因。

### 1.4 Heidelberger 與 5-FU：從設計出發的藥

1957 年 Heidelberger 等人在 Nature 發表氟化嘧啶這一類新的抑瘤化合物（Heidelberger et al., 1957）。5-FU 在體內變成 FdUMP，和葉酸輔因子一起把 thymidylate synthase 鎖住，細胞就做不出 thymidine（Alembic, 2026; H2-Pharma, 2026）。美國仿單的首次核准年份是 1962 年（Alembic, 2026）。

後來的改良都圍繞同一件事，就是讓 5-FU 口服、而且盡量只在腫瘤裡出現：

- **Capecitabine**：口服後經三個酵素接力才變成 5-FU。第一步的 carboxylesterase 幾乎只在肝臟；最後一步的 thymidine phosphorylase 在多種腫瘤組織中的濃度比正常組織高（Miwa et al., 1998）。
- **S-1**：tegafur（5-FU 的前驅藥）加兩個調節劑。Gimeracil 抑制分解 5-FU 的 DPD，讓血中濃度維持較久；oteracil 抑制腸黏膜裡活化 5-FU 的酵素，減少腸胃毒性（Shirasaka et al., 1996; European Medicines Agency, 2025）。

**和今天的連結**：分解 5-FU 的主要酵素是 DPD（European Medicines Agency, 2025）。DPD 完全缺乏的人用了 5-FU 或 capecitabine 可能致命，美國仿單把它列為加框警語，要求開藥前檢測 DPYD（Alembic, 2026; H2-Pharma, 2026）。檢測與減量見[化療基礎第 12.1 節](../00-shared/01-chemo-basics.md#121-dpyd-與-fluoropyrimidine)。

> [!CAUTION]
> **待核對：5-FU 的設計靈感來自大鼠肝癌對 uracil 的利用**
> 教科書常說，Heidelberger 是看到大鼠肝癌比正常肝臟更會利用 uracil，才設計出 5-FU。本章這次查證讀不到 1957 年原文的內文（PubMed 沒有摘要），也沒有讀到能證實這段因果的史料，所以不放進正文。

### 1.5 Rosenberg 的意外：鉑類

- **觀察**：1965 年 Rosenberg 原本要看電場對大腸桿菌生長的影響。細菌在通電後不再分裂，菌體卻變大到原來的 300 倍。原因不是電場，而是鉑電極產生的化合物，後來確認是 cisplatin（Monneret, 2011; Rosenberg et al., 1965）。這個分子其實在 1844 年就被 Peyrone 合成出來，放了一百多年沒人注意（Dasari & Tchounwou, 2014）。
- **論文**：1969 年同一個團隊報告鉑化合物對小鼠腫瘤有效（Rosenberg et al., 1969）。1977 年 Einhorn 用 cisplatin ＋ vinblastine ＋ bleomycin 治療 50 位轉移性睪丸癌病人，74% 完全緩解、26% 部分緩解（Einhorn & Donohue, 1977）。1978 年美國 FDA 核准（Dasari & Tchounwou, 2014）。
- **下一代**：carboplatin 的抗瘤譜和 cisplatin 相近但比較安全，1980 年代問世（Kelland, 2007）。Oxaliplatin 是第一個合併 5-FU 與 leucovorin 後對轉移性大腸直腸癌有效的鉑類藥（Monneret, 2011）。

**和今天的連結**：cisplatin 的腎毒性與嘔吐都寫在加框警語裡，所以每次都配水化與高效止吐（WG Critical Care, 2026）。Carboplatin 的血漿清除率和 GFR 呈線性關係，用 GFR 就能預測暴露量，才有 Calvert 公式（Calvert et al., 1989）；計算見[化療基礎第 3.2 節](../00-shared/01-chemo-basics.md#32-calvert-公式carboplatin)。

### 1.6 大自然的藥櫃：植物、土壤細菌與海洋生物

| 來源 | 故事 | 今天的藥 | 和今天的連結 |
|------|------|---------|-------------|
| 長春花（Catharanthus roseus，Madagascar periwinkle） | 民間拿它治糖尿病。研究者想驗證降血糖效果，結果找到的是兩個抗癌生物鹼（Noble, 1990） | vincristine、vinblastine；半合成的 vinorelbine（Sagent, 2024） | Vincristine 幾乎不壓骨髓，毒性在神經，所以常被放進合併處方（Hospira, 2026） |
| 鬼臼（podophyllin） | 幾百年的民俗藥。1950 年代開始找更有效的 podophyllotoxin 衍生物，最後得到一類新的 topoisomerase II 抑制劑（Hande, 1998） | etoposide（Hikma, 2024） | SCLC 的 EP 處方、Ewing sarcoma 的 IE |
| 土壤細菌 Streptomyces | 義大利藥廠 Farmitalia 與米蘭國家腫瘤研究所合作，1960 年起研究 Streptomyces peucetius，先得到 daunorubicin，再從突變株得到 doxorubicin；doxorubicin 的療效較好，但心臟毒性沒有消失（Falzone et al., 2018; Arcamone et al., 1969） | doxorubicin、epirubicin；同屬 Streptomyces 來源的還有 bleomycin、dactinomycin、mitomycin（Meitheal, 2026; Eugia, 2024; Hikma, 2026） | Anthracycline 傷心肌，所以要算累積劑量、追蹤 LVEF（Pfizer, 2026） |
| 喜樹（Camptotheca acuminata） | 1966 年 Wall 與 Wani 分離出 camptothecin（Wall & Wani, 1995; Falzone et al., 2018）。1985 年才知道標靶是 topoisomerase I（Hsiang et al., 1985）。之後的工作是找水溶性較好、毒性較低的衍生物（Kunimoto et al., 1987） | irinotecan、topotecan | Irinotecan 是前驅藥，活性代謝物 SN-38 靠 UGT1A1 清除，所以要想到 UGT1A1（Actavis, 2025） |
| 太平洋紫杉（Taxus brevifolia） | 1962 年美國農業部植物學家採到樹皮樣本，1967 年 Wall 與 Wani 分離出 taxol，1971 年發表結構，1979 年 Horwitz 發現它促進微管聚合，1984 年進入臨床試驗。剝樹皮會殺死樹，供應一度短缺，後來改用半合成（Weaver, 2014; Wani et al., 1971; Schiff et al., 1979） | paclitaxel、docetaxel（由紫杉針葉的前驅物半合成；Ringel & Horwitz, 1991; Mylan, 2026）、nab-paclitaxel | Paclitaxel 不溶於水，要用 polyoxyl 35 castor oil 當溶劑，這個溶劑會引起嚴重過敏，所以要前置用藥（Weaver, 2014; Teva Parenteral Medicines, 2026） |
| 海綿（Halichondria okadai） | 天然的 halichondrin B 活性很強但產量極少；2001 年報告全合成的簡化類似物保有活性（Towle et al., 2001） | eribulin，halichondrin B 的合成類似物（Eisai, 2025） | 轉移性乳癌後線：EMBRACE 的 OS 13.1 對 10.6 個月（HR 0.81；Cortes et al., 2011） |
| 海鞘（Ecteinascidia turbinata，加勒比海的被囊動物） | 分離出的生物鹼會結合在 DNA 小溝（D'Incalci & Galmarini, 2010） | trabectedin | 脂肪肉瘤與平滑肌肉瘤後線：對 dacarbazine 的 PFS 4.2 對 1.5 個月（HR 0.55），OS 無差異（Demetri et al., 2016） |

### 1.7 實驗室設計的藥與換包裝的藥

- **Gemcitabine**：1990 年發表的新 deoxycytidine 類似物，在 8 種小鼠腫瘤模型都有效，同類的 cytarabine 則活性差很多或無效（Hertel et al., 1990）。1997 年的晚期胰臟癌隨機試驗用「臨床效益反應」（疼痛、體能、體重的綜合指標）當主要指標，gemcitabine 23.8% 對 5-FU 4.8%，中位存活 5.65 對 4.41 個月（Burris et al., 1997）。這個試驗也提醒我們：緩和性化療的目標可以是症狀，而不只是存活。
- **Pemetrexed**：一個藥同時抑制 thymidylate synthase、DHFR 與 GARFT 三個葉酸酵素（Eli Lilly, 2023）。
- **Temozolomide 與 dacarbazine**：dacarbazine 在 1962 年合成（Falzone et al., 2018）。Temozolomide 是口服藥，在生理 pH 下不需酵素就轉成活性物 MTIC（Merck Sharp & Dohme, 2026）；膠質母細胞瘤放療合併 temozolomide 的中位存活 14.6 對 12.1 個月（HR 0.63；Stupp et al., 2005）。
- **脂質體 doxorubicin**：把 doxorubicin 包進有 PEG 外衣的奈米脂質體，延長循環時間，並靠腫瘤血管的 EPR 效應（enhanced permeability and retention）被動聚集在腫瘤（Barenholz, 2012）。
- **脂質體 irinotecan**：NAPOLI-1 中，gemcitabine 治療後的轉移性胰臟癌用 nal-IRI ＋ 5-FU／leucovorin，OS 6.1 對 4.2 個月（HR 0.67；Wang-Gillam et al., 2016）。
- **nab-paclitaxel**：把 paclitaxel 結合在白蛋白奈米粒子上，不需要 castor oil 溶劑。轉移性乳癌的第三期試驗不給前置用藥，反應率 33% 對 19%，第 4 級嗜中性球低下較少（9% 對 22%），但第 3 級感覺神經病變較多（10% 對 2%）（Gradishar et al., 2005）。

> [!WARNING]
> **換了包裝就是另一個藥**
> 脂質體與白蛋白結合劑型的劑量、藥動與毒性都和原來的藥不同，仿單都用大寫字寫著不可互換：Onivyde 不可取代一般 irinotecan（Ipsen, 2025），liposomal doxorubicin 不可取代一般 doxorubicin（Sagent, 2026），nab-paclitaxel 不可和其他 paclitaxel 劑型互換（Abraxis, 2022）。核對處方時，藥名、劑型、劑量三樣都要對。

---

## 2. 作用機轉

**結論先講：** 化療藥攻擊的是「細胞分裂」這件事本身。它對癌細胞和正常細胞的差別只在程度，所以療效與毒性是同一個機轉的兩面。下面四個觀念可以解釋化療為什麼要分次給、合併給、定期給。

### 2.1 細胞週期：藥在哪一站下手

細胞分裂依序走 G1（準備）、S（複製 DNA）、G2（檢查）、M（有絲分裂）。有些藥只在特定一站有效（週期特異性），有些藥直接破壞 DNA，不挑時間（週期非特異性）。

| 下手的地方 | 藥物 | 仿單怎麼寫 |
|-----------|------|-----------|
| S 期（DNA 合成） | gemcitabine、methotrexate、5-FU、pemetrexed | Gemcitabine 殺死正在合成 DNA 的細胞，並擋在 G1／S 交界（Meitheal, 2025）；methotrexate 干擾 DNA 合成、修復與細胞複製（Accord, 2026） |
| S 期（複製叉撞上去才致命） | irinotecan、topotecan | 細胞毒性來自 DNA 合成時，複製酵素撞上藥物－topoisomerase I－DNA 複合物所產生的雙股斷裂（Actavis, 2025; Accord, 2025） |
| G2 期 | etoposide、bleomycin | Etoposide 主要作用在 G2（Hikma, 2024）；bleomycin 讓細胞停在 G2 與有絲分裂期（Meitheal, 2026） |
| M 期（有絲分裂） | vinca、taxane、eribulin | Vincristine 與 vinorelbine 讓細胞停在中期（Hospira, 2026; Sagent, 2024）；docetaxel 抑制有絲分裂（Mylan, 2026）；eribulin 造成 G2／M 阻斷（Eisai, 2025） |
| 不挑週期 | 鉑類、烷化劑 | Carboplatin 與 oxaliplatin 的仿單都寫 cell-cycle nonspecific（Natco, 2026; Sagent, 2025）；cyclophosphamide 對活躍與靜止的細胞都有作用（Falzone et al., 2018） |

> [!TIP]
> **工廠的四個部門**
> 把細胞想成一間工廠：S 期是影印部（複製藍圖）、M 期是搬運部（把兩份藍圖分到兩邊）。抗代謝物斷影印部的原料，topoisomerase 抑制劑讓影印機卡紙，抗微管藥把搬運部的吊車弄壞；這些藥只對「那個部門正在上班」的細胞有效，所以要重複給、或拉長輸注，等更多細胞輪到那一班。烷化劑與鉑類則是直接在藍圖上亂釘釘子，哪個部門上班都受影響。這是教學上的簡化，實際上同一個藥對各期的作用不是全有全無。

> [!IMPORTANT]
> **週期特異性的臨床意義**
> 週期特異性藥物只殺得到「剛好走到那一站」的細胞，所以處方常設計成拉長輸注或連續數天給藥，例如 FOLFIRINOX 的 5-FU 連續輸注 46 小時（Conroy et al., 2011）。但輸注時間是處方的一部分，不能自己改：gemcitabine 輸注超過 60 分鐘或比每週一次更頻繁，毒性會增加（Meitheal, 2025）。

### 2.2 Log-kill：一次殺固定比例，不是固定數目

Skipper 等人在小鼠白血病 L1210 的實驗提出 log-kill 假說：一個劑量的化療殺死的是固定「比例」的腫瘤細胞，和腫瘤大小無關，每次治療讓腫瘤縮小同樣的比例（Skipper et al., 1964; Hughes et al., 2026）。

用假設的數字算一次：如果一個週期能殺掉 99%（2 個 log），10 億個細胞打完一次還剩 1,000 萬個，要重複很多次才可能歸零，而且兩次治療之間腫瘤還會長回來。這個模型解釋了三件事：

1. **化療要打很多個週期**，影像上看不到腫瘤不代表沒有細胞了。
2. **腫瘤負荷愈小愈有機會清光**，這是術後輔助化療的邏輯：用全身治療清掉看不到的微轉移（Fornier & Norton, 2005）。1976 年 Bonadonna 的 CMF 輔助試驗裡，淋巴結陽性乳癌術後 27 個月的復發率是 24% 對 5.3%（Bonadonna et al., 1976）。
3. **劑量不是加愈高愈好**。乳癌的 AC 處方把劑量再往上加並沒有改善結果，doxorubicin 60 mg/m²、cyclophosphamide 600 mg/m² 之上有門檻效應；在乳癌也沒有可信的證據顯示高劑量化療加幹細胞支持優於標準劑量（Fornier & Norton, 2005）。

> [!TIP]
> **洗衣服的比喻**
> 每洗一次，洗掉的是「九成九的污漬」，不是「固定幾克」。第一次洗完看起來已經乾淨，其實布料裡還有；要洗到真的乾淨得洗好幾次，而且兩次之間不能放太久，否則又髒回來。這也是為什麼不該因為「影像已經看不到了」就自行減少輔助化療的次數。

### 2.3 Goldie–Coldman：抗藥性是算機率的

Goldie 與 Coldman 用數學模型把腫瘤的藥物敏感性和自發突變率連在一起：抗藥細胞的比例與數目都隨時間增加，而且「腫瘤裡至少有一個抗藥細胞」的機率，會在腫瘤生長史中很短的一段時間內從很低變成很高（Goldie & Coldman, 1979）。

臨床上的推論是：愈早治療愈好，而且一開始就用多種機轉不同的藥。這個假說原本預測「交替給不同處方」最好，但米蘭的試驗裡，先打完 doxorubicin 再接 CMF 的序列給法反而勝過交替給法（Fornier & Norton, 2005）。這個結果把大家引向下一個模型。

### 2.4 Norton–Simon 與劑量密集（dose-dense）

實體腫瘤的生長不是等速的指數曲線，而是 Gompertz 曲線：腫瘤愈大，倍增時間愈長（Fornier & Norton, 2005）。Norton 與 Simon 提出：化療讓腫瘤縮小的速率，和那個大小的腫瘤原本的生長速率成正比（Norton & Simon, 1977; Hughes et al., 2026）。腫瘤被打小之後反而長得更快，所以兩次化療之間的空檔愈短愈好。

- **做法**：每次劑量不變，把間隔從 3 週縮成 2 週，用 G-CSF 支撐白血球，這叫劑量密集。
- **CALGB 9741**（Citron et al., 2003）— 2,005 位淋巴結陽性乳癌術後病人；2 × 2 設計比較 q2w（加 filgrastim）對 q3w、序列對同時；劑量密集組 DFS 的 RR 0.74（P = .010）、OS 的 RR 0.69（P = .013），4 年 DFS 82% 對 75%；嚴重嗜中性球低下在劑量密集組反而較少。
- **EBCTCG 統合分析**（Early Breast Cancer Trialists' Collaborative Group, 2019）— 26 個試驗、37,298 人；劑量密集或序列給法的 10 年復發風險 28.0% 對 31.4%（RR 0.86，95% CI 0.82–0.89），10 年乳癌死亡率 18.9% 對 21.3%（RR 0.87，95% CI 0.83–0.92）。

處方見[乳癌章 5.1](../03-breast-cancer.md#51-靜脈化療骨幹anthracyclinetaxanecyclophosphamidecapecitabine)，醫囑範例見[乳癌章 7.2](../03-breast-cancer.md#72-order-set-範例一輔助-ddac--paclitaxelq2w含-g-csf)。

### 2.5 為什麼要合併用藥

單一藥物很少能治癒癌症。1960 到 1970 年代初，合併化療治癒了兒童急性白血病與晚期 Hodgkin 病，才扭轉了「藥物治不好晚期癌症」的悲觀看法，並帶動輔助化療的研究（DeVita & Chu, 2008）。Hodgkin 病的 MOPP 四藥處方讓八成病人達到完全緩解（Falzone et al., 2018）。

設計合併處方的三個原則：

1. **機轉不同**：抗藥性來自隨機突變，一開始就用幾種機轉不同的藥，比較不會被同一個抗藥細胞株全部躲過（Goldie & Coldman, 1979）。
2. **毒性不重疊**：每個藥才能都給到足夠的劑量。Vincristine 的仿單就寫，它常被選進合併處方，是因為在建議劑量下沒有明顯的骨髓抑制，毒性是神經病變（Hospira, 2026）。
3. **給藥間隔盡量短**，理由見 2.4。

以 Einhorn 的睪丸癌處方為例（Einhorn & Donohue, 1977）：cisplatin 的招牌毒性在腎（WG Critical Care, 2026），bleomycin 在肺（Meitheal, 2026），vinblastine 是抗微管藥，三個藥的機轉都不同。

### 2.6 治療指數，以及為什麼是骨髓、腸道、頭髮

**治療指數（therapeutic index）** 是「產生毒性的劑量」與「產生療效的劑量」之間的距離。化療藥的治療指數窄，所以劑量要依體表面積或腎功能個別計算（見[化療基礎第 2 節](../00-shared/01-chemo-basics.md#2-體表面積bsa計算)）。化療史上的改良大多是在把這個距離拉開：cyclophosphamide 的設計目標就是提高烷化劑的治療指數，mesna 又進一步加寬（Brock, 1989）。

化療攻擊分裂中的細胞，而身體裡分裂最快的正常組織就是骨髓、口腔與腸道黏膜（Accord, 2026）以及毛囊。

| 正常組織 | 為什麼受傷 | 看到什麼 | 連到哪裡 |
|---------|-----------|---------|---------|
| 骨髓 | 造血前驅細胞持續分裂 | 嗜中性球低下、血小板低下、貧血 | [腫瘤急症第 1 節](../00-shared/02-oncologic-emergencies.md#1-發燒性嗜中性球低下)、[支持性照護第 10 節](../00-shared/03-supportive-care.md#10-化療相關貧血血小板低下與輸血) |
| 口腔與腸道黏膜 | 上皮細胞持續更新 | 口腔黏膜炎、腹瀉 | [支持性照護第 4 節](../00-shared/03-supportive-care.md#4-口腔黏膜炎)、[第 5 節](../00-shared/03-supportive-care.md#5-腹瀉) |
| 毛囊 | 毛基質角質細胞快速分裂，化療引發 p53 依賴的細胞凋亡；毛囊幹細胞受損的程度決定掉髮能不能恢復（Paus et al., 2013） | 掉髮 | [乳癌章 6.3](../03-breast-cancer.md#63-taxane-與其他化療藥的特殊毒性頭皮冷卻)（頭皮冷卻） |
| 性腺 | 對烷化劑敏感；cyclophosphamide 仿單把不孕列為警語（BluePoint, 2026） | 不孕、停經 | [化療基礎第 12.5 節](../00-shared/01-chemo-basics.md#125-生育力保存與避孕諮詢) |

心肌與神經細胞幾乎不分裂，卻也會受傷；那不是因為「分裂快」，而是個別藥物的特殊機轉，例如 anthracycline 與心肌細胞的 topoisomerase IIβ（3.5）、抗微管藥與神經軸突（3.6）。

---

## 3. 分類與代表藥

**結論先講：** 七個類別，每一類記三件事：它對 DNA 或分裂機器做了什麼、招牌毒性是什麼、本手冊哪些處方用到它。劑量限制毒性與累積劑量上限的完整表格在[化療基礎第 11 節](../00-shared/01-chemo-basics.md#11-抗癌藥分類劑量限制毒性與解毒劑)，這裡不重複。

### 3.1 烷化劑（alkylating agents）

**來源**：nitrogen mustard 的後代（1.2）。**機轉**：活性代謝物把烷基接到 DNA 上；cyclophosphamide 與 ifosfamide 的主要作用是造成 DNA 交聯（BluePoint, 2026; Fresenius Kabi, 2026），temozolomide 的活性物 MTIC 主要烷化鳥糞嘌呤的 O6 與 N7 位置（Merck Sharp & Dohme, 2026）。

| 藥物 | 特點 | 招牌毒性與監測 | 本手冊用在哪 |
|------|------|--------------|-------------|
| cyclophosphamide | 前驅藥，經肝臟 CYP450 活化；代謝產生有活性的 phosphoramide mustard 與 acrolein（BluePoint, 2026）；ifosfamide 的仿單指出 acrolein 具泌尿毒性（Fresenius Kabi, 2026） | 骨髓抑制；出血性膀胱炎（大量水化與勤排尿可減少，並定期檢查尿沉渣有無紅血球）；心臟毒性（心肌炎、心包膜積液、心衰竭）；不孕；次發性惡性腫瘤（BluePoint, 2026） | 乳癌 AC、EC、TC（[乳癌章 5.1](../03-breast-cancer.md#51-靜脈化療骨幹anthracyclinetaxanecyclophosphamidecapecitabine)）；Ewing sarcoma VDC（[肉瘤章 5.2](../04-sarcoma.md#52-ewing-sarcomavdcie以及高劑量-ifosfamide)） |
| ifosfamide | Cyclophosphamide 的合成類似物，同樣是前驅藥，由 CYP3A4 與 CYP2B6 代謝（Fresenius Kabi, 2026） | 加框警語：骨髓抑制、神經毒性（腦病變，可致死）、泌尿與腎毒性；出血性膀胱炎用 mesna 預防（Fresenius Kabi, 2026） | 肉瘤 AI、IE（[肉瘤章 5.3](../04-sarcoma.md#53-軟組織肉瘤細胞毒性處方)、[6.2](../04-sarcoma.md#62-ifosfamide腦病變出血性膀胱炎與腎小管損傷)） |
| dacarbazine | 靜脈給；確切機轉未明，假說之一是烷化作用（Hikma, 2025） | 仿單警語：造血抑制、肝壞死（約 0.01%）；噁心嘔吐是最常見的毒性；外滲會造成組織傷害與劇痛（Hikma, 2025） | 美國仿單適應症是黑色素瘤與 Hodgkin 病；肉瘤後線與試驗對照組（[肉瘤章 5.3](../04-sarcoma.md#53-軟組織肉瘤細胞毒性處方)） |
| temozolomide | 口服；不需酵素就轉成 MTIC（Merck Sharp & Dohme, 2026） | 骨髓抑制；合併放療時要給 Pneumocystis 肺炎預防；肝毒性；每個 28 天週期的第 1 與第 22 天驗 CBC（Merck Sharp & Dohme, 2026） | 美國仿單適應症是膠質母細胞瘤與分化不良星狀細胞瘤；復發 Ewing sarcoma 與 irinotecan 併用屬適應症外（[肉瘤章 4.2](../04-sarcoma.md#42-ewing-sarcoma)） |

Mesna 會在尿液中和 ifosfamide 的代謝物 acrolein 與 4-hydroxy-ifosfamide 結合，讓它們失去毒性（Eugia, 2026）。Trabectedin 在仿單上也歸為烷化藥，但作用方式特殊，放在 3.7。

### 3.2 鉑類（platinum compounds）

**來源**：Rosenberg 的意外發現（1.5）。**機轉**：鉑與 DNA 結合，形成鏈內與鏈間交聯，干擾轉錄與複製（WG Critical Care, 2026）；鏈內相鄰兩個嘌呤的交聯占絕大多數（Dasari & Tchounwou, 2014）。

| 藥物 | 特點 | 招牌毒性與監測 | 本手冊用在哪 |
|------|------|--------------|-------------|
| cisplatin | 第一代；主要由腎臟排出（WG Critical Care, 2026） | 加框警語：腎毒性（劑量相關且累積）、周邊神經病變、噁心嘔吐、骨髓抑制；耳毒性會累積。要水化、監測腎功能與電解質、用高效止吐，考慮聽力檢查（WG Critical Care, 2026） | 肺癌（[肺癌章 5.1–5.3](../01-lung-cancer.md#5-常用處方regimen)）；骨肉瘤 MAP（[肉瘤章 5.1](../04-sarcoma.md#51-骨肉瘤map-與高劑量-methotrexate)、[6.4](../04-sarcoma.md#64-cisplatin腎耳與神經)） |
| carboplatin | 第二代；活化（aquation）比 cisplatin 慢；主要經腎排出（Natco, 2026） | 骨髓抑制是劑量相關的主要毒性，血小板低下比 cisplatin 明顯，最低點約在第 21 天；可能在幾分鐘內發生類過敏反應；嘔吐、神經、耳、腎毒性都比 cisplatin 少（Natco, 2026） | 肺癌；乳癌 TCH、TCHP 與 KEYNOTE-522（[乳癌章 5.2](../03-breast-cancer.md#52-her2-陽性抗-her2-抗體與化療組合)） |
| oxaliplatin | 第三代；帶 DACH 配位基（Sagent, 2025） | 加框警語：過敏與 anaphylaxis，任何週期、幾分鐘內都可能發生。急性感覺神經病變約 56%，遇冷誘發或加重；另有持續性神經病變。CrCl < 30 mL/min 要減量（Sagent, 2025） | 胰臟癌 FOLFIRINOX、NALIRIFOX（[胰臟癌章 5.1](../02-pancreatic-cancer.md#51-folfirinox-家族輔助-mfolfirinox-與轉移性-folfirinox)、[6.3](../02-pancreatic-cancer.md#63-oxaliplatin)） |

> [!IMPORTANT]
> **三個鉑類，三種劑量限制毒性**
> Cisplatin 是腎，carboplatin 是骨髓（尤其血小板），oxaliplatin 是神經。Carboplatin 用 Calvert 公式算劑量：劑量（mg）= 目標 AUC ×（GFR ＋ 25）（Calvert et al., 1989）。

### 3.3 抗代謝物（antimetabolites）

**來源**：Farber 的抗葉酸藥與 Heidelberger 的氟化嘧啶（1.3、1.4）。**機轉**：長得像葉酸或核苷，占住酵素或被接進 DNA，讓 DNA 合成停下來。

**葉酸拮抗劑**

| 藥物 | 特點 | 招牌毒性與監測 | 本手冊用在哪 |
|------|------|--------------|-------------|
| methotrexate | 抑制 DHFR；靜脈給藥後 80–90% 在 24 小時內以原形從尿液排出（Accord, 2026） | 黏膜炎、骨髓抑制、腎毒性、肝毒性；≥ 500 mg/m² 要 leucovorin 解救；第三空間積液會延長半衰期（Accord, 2026） | 骨肉瘤 MAP 的高劑量 methotrexate（[肉瘤章 5.1](../04-sarcoma.md#51-骨肉瘤map-與高劑量-methotrexate)） |
| pemetrexed | 同時抑制 thymidylate synthase、DHFR、GARFT；主要經腎排出（Eli Lilly, 2023） | 骨髓抑制。沒有補充維生素時，第 3–4 級嗜中性球低下 38% 對 23%、發燒性嗜中性球低下 9% 對 0.6%；所以要 folic acid 與 B12；CrCl ≥ 45 mL/min 才給（Eli Lilly, 2023） | 非鱗狀 NSCLC（[肺癌章 5.1](../01-lung-cancer.md#51-nsclc-靜脈處方)） |

**氟化嘧啶（fluoropyrimidines）**

| 藥物 | 特點 | 招牌毒性與監測 | 本手冊用在哪 |
|------|------|--------------|-------------|
| 5-fluorouracil（5-FU） | 代謝物 FdUMP 抑制 thymidylate synthase，另有代謝物被接進 RNA 與 DNA（Alembic, 2026） | 加框警語：DPD 完全缺乏者可致死。腹瀉、黏膜炎、骨髓抑制、手足症候群；心臟毒性（心絞痛、心肌梗塞、心律不整、心衰竭）；高血氨腦病變；與 warfarin 併用 INR 上升（Alembic, 2026） | 胰臟癌 FOLFIRINOX、NALIRIFOX（[胰臟癌章 5.1](../02-pancreatic-cancer.md#51-folfirinox-家族輔助-mfolfirinox-與轉移性-folfirinox)、[6.4](../02-pancreatic-cancer.md#64-5-fucapecitabine-與-s-1)） |
| capecitabine | 口服前驅藥，三個酵素接力轉成 5-FU（H2-Pharma, 2026） | 加框警語：DPD 完全缺乏，以及與 warfarin 等維生素 K 拮抗劑併用的出血風險。手足症候群、腹瀉、心臟毒性；CrCl 30–50 mL/min 減量 25%（H2-Pharma, 2026） | 乳癌（[乳癌章 6.4](../03-breast-cancer.md#64-capecitabine手足症候群dpyd-與-warfarin)）；胰臟癌 GemCap（[胰臟癌章 5.4](../02-pancreatic-cancer.md#54-口服與維持用藥s-1capecitabineolaparib以及不建議的-erlotinib)） |
| S-1（tegafur／gimeracil／oteracil） | Tegafur 經 CYP2A6 轉成 5-FU；gimeracil 抑制 DPD；oteracil 減少腸胃毒性（European Medicines Agency, 2025） | 腹瀉與脫水是劑量限制毒性；骨髓抑制；DPD 完全缺乏者禁用；gimeracil 經腎清除，嚴重腎功能不全（CrCl < 30 mL/min）不建議使用（European Medicines Agency, 2025） | 歐盟適應症為晚期胃癌等；胰臟癌術後輔助的亞洲選項，JASPAC 01 的 5 年存活 44.1% 對 gemcitabine 24.4%（HR 0.57；Uesaka et al., 2016）（[胰臟癌章 5.4](../02-pancreatic-cancer.md#54-口服與維持用藥s-1capecitabineolaparib以及不建議的-erlotinib)） |

**核苷類似物（nucleoside analogues）**

| 藥物 | 特點 | 招牌毒性與監測 | 本手冊用在哪 |
|------|------|--------------|-------------|
| gemcitabine | Deoxycytidine 類似物。二磷酸代謝物抑制 ribonucleotide reductase，三磷酸代謝物和 dCTP 競爭被接進 DNA（Meitheal, 2025） | 骨髓抑制；肺毒性（間質性肺炎、ARDS）；溶血性尿毒症候群（HUS）；微血管滲漏症候群；肝毒性；會加重放射治療的毒性，不建議與放療併用（Meitheal, 2025） | 胰臟癌 GnP（[胰臟癌章 5.3](../02-pancreatic-cancer.md#53-以-gemcitabine-為骨幹的處方)、[6.5](../02-pancreatic-cancer.md#65-nab-paclitaxel-與-gemcitabinegnp)）；鱗狀 NSCLC；肉瘤 gemcitabine ＋ docetaxel |

### 3.4 Topoisomerase I 抑制劑

**來源**：喜樹的 camptothecin（1.6）。**機轉**：topoisomerase I 平常會把 DNA 剪開一股、鬆開扭力後再接回去。Irinotecan、SN-38 與 topotecan 卡在酵素與 DNA 的複合物上，讓剪開的那一股接不回去；複製叉撞上來時就變成細胞修不好的雙股斷裂（Actavis, 2025; Accord, 2025）。

| 藥物 | 特點 | 招牌毒性與監測 | 本手冊用在哪 |
|------|------|--------------|-------------|
| irinotecan | 前驅藥，經 carboxylesterase 變成活性的 SN-38（Actavis, 2025） | 加框警語：腹瀉與骨髓抑制。早發性腹瀉伴隨膽鹼性症狀，用 atropine；遲發性腹瀉可致命，立刻用 loperamide。UGT1A1\*28 或 \*6 同型合子考慮起始劑量至少降一級；膽紅素 > 2 mg/dL 無建議劑量（Actavis, 2025） | 胰臟癌 FOLFIRINOX（[胰臟癌章 6.2](../02-pancreatic-cancer.md#62-irinotecan-與脂質體-irinotecan)）；復發 Ewing sarcoma |
| liposomal irinotecan（Onivyde） | 把 irinotecan 包在脂質體裡；小鼠模型中用 5 分之 1 的劑量就達到相近的腫瘤內暴露（Ipsen, 2025） | 加框警語：嚴重嗜中性球低下與嚴重腹瀉；ANC < 1,500/mm³ 暫停。早發性腹瀉給 atropine，遲發性給 loperamide。不可取代一般 irinotecan（Ipsen, 2025） | 胰臟癌 NALIRIFOX 與二線（[胰臟癌章 5.2](../02-pancreatic-cancer.md#52-脂質體-irinotecannalirifox-與二線-nal-iri--5-fuleucovorin)） |
| topotecan | 半合成 camptothecin 衍生物（Accord, 2025） | 加框警語：骨髓抑制，基線 ANC 要 ≥ 1,500/mm³；嗜中性球低下性結腸炎；間質性肺病；CrCl 20–39 mL/min 減為 0.75 mg/m²（Accord, 2025） | SCLC 二線（[肺癌章 5.3](../01-lung-cancer.md#53-sclc-處方)）；復發 Ewing sarcoma |

> [!TIP]
> **電話線與剪刀手**
> DNA 複製時會愈轉愈緊，像捲成一團的電話線。Topoisomerase 是專門的剪刀手：剪開、鬆開、再接回去。Topoisomerase I 一次剪一股，topoisomerase II 一次剪兩股。這兩類藥做的事一樣，就是在剪刀剪下去的那一刻把它卡住，讓它接不回去。斷掉的 DNA 加上卡在上面的酵素，就是細胞的死因。

### 3.5 Topoisomerase II 抑制劑

**來源**：Streptomyces 的 anthracycline 與鬼臼的 podophyllotoxin（1.6）。**機轉**：和 topoisomerase II 形成可切割複合物，DNA 兩股都斷。Anthracycline 另外會嵌入 DNA 鹼基對之間，抑制 DNA 與 RNA 聚合酶（Pfizer, 2026）。

| 藥物 | 特點 | 招牌毒性與監測 | 本手冊用在哪 |
|------|------|--------------|-------------|
| doxorubicin | 主要經代謝與膽汁排出（Pfizer, 2026） | 加框警語：心肌病變（累積 300–500 mg/m² 時 1–20%）、次發性 AML／MDS、外滲組織壞死、嚴重骨髓抑制。嗜中性球最低點在第 10–14 天。膽紅素升高要減量，嚴重肝功能不全禁用；會加重放射毒性並引起放射回憶反應（Pfizer, 2026） | 乳癌 AC（[乳癌章 6.1](../03-breast-cancer.md#61-anthracycline累積劑量與心臟毒性)）；肉瘤單藥、AI、MAP、VDC（[肉瘤章 6.3](../04-sarcoma.md#63-doxorubicin累積劑量dexrazoxane-與外滲)） |
| epirubicin | Doxorubicin 的 4-epimer（Pharmacia & Upjohn, 2026） | 加框警語同 doxorubicin。心肌病變：累積 550 mg/m² 約 0.9%、700 約 1.6%、900 約 3.3%；肝功能異常要減量（Pharmacia & Upjohn, 2026） | 乳癌 EC、FEC（[乳癌章 5.1](../03-breast-cancer.md#51-靜脈化療骨幹anthracyclinetaxanecyclophosphamidecapecitabine)）；肉瘤 EI |
| pegylated liposomal doxorubicin | PEG 脂質體劑型（Barenholz, 2012） | 加框警語：心肌病變、輸注相關反應（實體腫瘤病人 11%）；手足症候群；治療前、中、後都要評估左心室功能；不可取代一般 doxorubicin（Sagent, 2026） | 美國仿單適應症含鉑類治療後的卵巢癌與 AIDS 相關 Kaposi sarcoma（Sagent, 2026）；本手冊在[乳癌章 6.1](../03-breast-cancer.md#61-anthracycline累積劑量與心臟毒性)與肉瘤章提到 |
| etoposide | Podophyllotoxin 的半合成衍生物；腎清除約占總清除的 35%（Hikma, 2024） | 嚴重骨髓抑制；輸注太快會低血壓，要用 30–60 分鐘慢慢滴；anaphylaxis；罕見的次發性急性白血病；CrCl 15–50 mL/min 給 75% 劑量（Hikma, 2024） | SCLC（[肺癌章 5.3](../01-lung-cancer.md#53-sclc-處方)）；Ewing sarcoma IE（[肉瘤章 5.2](../04-sarcoma.md#52-ewing-sarcomavdcie以及高劑量-ifosfamide)） |

**為什麼 anthracycline 傷心臟、所以要追蹤 LVEF？** Topoisomerase II 有兩型：α 型在分裂中的細胞很多，β 型在不分裂的細胞（例如成人心肌細胞）比較多（McGowan et al., 2017）。Doxorubicin 抓住癌細胞的 α 型是療效，抓住心肌細胞的 β 型則造成 DNA 雙股斷裂與粒線體功能異常；把小鼠心肌細胞的 Top2b 基因剔除，就不會發生 doxorubicin 引起的心衰竭（Zhang et al., 2012）。心肌病變的風險和累積劑量成正比（Pfizer, 2026）：回溯分析估計累積 550 mg/m² 時約 26% 的病人會發生心衰竭，65 歲以上在 400 mg/m² 之後風險更高（Swain et al., 2003）。累積劑量表與 dexrazoxane 見[化療基礎第 11.3 節](../00-shared/01-chemo-basics.md#113-累積劑量上限)。

### 3.6 抗微管藥（antimicrotubule agents）

**來源**：長春花、紫杉、海綿（1.6）。**機轉**：有絲分裂時，微管要不斷地長出來又拆掉，才能把染色體拉到兩邊。Vinca 抑制微管形成，讓細胞停在中期（Hospira, 2026）；taxane 相反，促進微管聚合並阻止解聚，微管變成一束束拆不掉的構造（Teva Parenteral Medicines, 2026）；eribulin 抑制微管的生長期，並把 tubulin 困在沒有功能的聚集物裡（Eisai, 2025）。

| 藥物 | 特點 | 招牌毒性與監測 | 本手冊用在哪 |
|------|------|--------------|-------------|
| vincristine | 長春花生物鹼；由肝臟 CYP3A 代謝（Hospira, 2026） | **只能靜脈給，其他途徑會致死**。神經毒性、便秘、麻痺性腸阻塞；外滲造成刺激；直接膽紅素 > 3 mg/dL 劑量減半（Hospira, 2026） | Ewing sarcoma VDC（[肉瘤章 5.2](../04-sarcoma.md#52-ewing-sarcomavdcie以及高劑量-ifosfamide)） |
| vinorelbine | 半合成 vinca（Sagent, 2024） | 加框警語：骨髓抑制。嚴重便秘與腸阻塞、周邊神經病變、外滲造成組織壞死、肺毒性；膽紅素升高要減量；與 CYP3A 抑制劑併用要小心（Sagent, 2024） | NSCLC 術後輔助 cisplatin ＋ vinorelbine（[肺癌章 5.1](../01-lung-cancer.md#51-nsclc-靜脈處方)）；轉移性乳癌 |
| paclitaxel | 溶劑是 polyoxyl 35 castor oil；主要由 CYP2C8 代謝，CYP3A4 次之（Teva Parenteral Medicines, 2026） | 加框警語：anaphylaxis 與嚴重過敏（2–4%），所有病人都要前置類固醇、diphenhydramine 與 H2 阻斷劑。骨髓抑制是劑量限制毒性，最低點中位數第 11 天；周邊神經病變常見（Teva Parenteral Medicines, 2026） | 乳癌、肺癌、血管肉瘤（[乳癌章 6.3](../03-breast-cancer.md#63-taxane-與其他化療藥的特殊毒性頭皮冷卻)） |
| nab-paclitaxel | 白蛋白結合的奈米粒子，不含 castor oil 溶劑（Gradishar et al., 2005） | 加框警語：嚴重骨髓抑制，基線 ANC < 1,500/mm³ 不可給。感覺神經病變、敗血症、肺炎；中重度肝功能不全要降低起始劑量（Abraxis, 2022） | 胰臟癌 GnP（[胰臟癌章 6.5](../02-pancreatic-cancer.md#65-nab-paclitaxel-與-gemcitabinegnp)）；乳癌、肺癌 |
| docetaxel | 由紫杉針葉的前驅物半合成；溶劑含 polysorbate 80（Mylan, 2026） | 加框警語：治療相關死亡、肝毒性、嗜中性球低下、過敏、體液滯留。膽紅素 > ULN，或 AST／ALT > 1.5 × ULN 合併 ALP > 2.5 × ULN 要避免使用。前置口服 dexamethasone 3 天；避免與強效 CYP3A4 抑制劑併用（Mylan, 2026） | 乳癌 TC、TCHP；肺癌二線；肉瘤 gemcitabine ＋ docetaxel |
| eribulin | Halichondrin B 的合成類似物（Eisai, 2025） | 嗜中性球低下、周邊神經病變、QT 延長；每劑前評估神經病變並驗 CBC；肝功能不全與中重度腎功能不全要減量；不可用含 dextrose 的溶液稀釋（Eisai, 2025） | 轉移性乳癌（[乳癌章 5.4](../03-breast-cancer.md#54-三陰性與其他靜脈處方keynote-522eribulin)）；脂肪肉瘤，對 dacarbazine 的 OS 13.5 對 11.5 個月（HR 0.77；Schöffski et al., 2016）（[肉瘤章 5.3](../04-sarcoma.md#53-軟組織肉瘤細胞毒性處方)） |

> [!TIP]
> **鷹架的比喻**
> 微管像工地的鷹架，蓋的時候要搭、蓋完要拆，細胞分裂時每幾分鐘就搭拆一輪。Vinca 與 eribulin 讓鷹架搭不起來；taxane 是把鷹架焊死、拆不掉。兩種做法都讓工程停擺。神經細胞的長軸突也靠微管運送物質，所以這一類藥的共同毒性是周邊神經病變，而且從最長的神經（手指、腳趾）開始。

> [!WARNING]
> **Vincristine 只能靜脈給**
> Vincristine 打進脊髓腔會致死。仿單要求稀釋在軟袋裡，並標示「FOR INTRAVENOUS USE ONLY – FATAL IF GIVEN BY OTHER ROUTES」（Hospira, 2026）。不用針筒交付的原因與流程見[化療基礎第 14.3 節](../00-shared/01-chemo-basics.md#143-vinca-類為什麼一定用-minibag)。

### 3.7 其他：bleomycin、dactinomycin、mitomycin、trabectedin

| 藥物 | 來源與機轉 | 招牌毒性與監測 | 本手冊用在哪 |
|------|-----------|--------------|-------------|
| bleomycin | Streptomyces verticillus 產生的醣肽類抗生素；造成 DNA 單股與雙股斷裂。約 65% 在 24 小時內由尿液排出（Meitheal, 2026） | 加框警語：肺纖維化是最嚴重的毒性，年長者與總量 > 400 units 風險較高，肺毒性約 10%；淋巴瘤病人約 1% 發生嚴重特異體質反應，前 2 劑用 2 units 以下；之後手術給氧氣時肺毒性風險增加（Meitheal, 2026） | 四個癌別的處方沒有用到；歷史上是睪丸癌 PVB 處方的一員（Einhorn & Donohue, 1977） |
| dactinomycin（actinomycin D） | Streptomyces parvullus 產生；結合 DNA 並抑制 RNA 合成（Eugia, 2024）。Farber 把它引進 Wilms 腫瘤的治療（Miller, 2006） | 外滲造成嚴重組織傷害；肝靜脈阻塞病（VOD）；加重放射毒性與放射回憶反應（Eugia, 2024） | 四個癌別的處方沒有用到；美國仿單適應症含 Wilms 腫瘤、橫紋肌肉瘤、Ewing sarcoma 與妊娠滋養層腫瘤（Eugia, 2024） |
| mitomycin | Streptomyces caespitosus 產生；選擇性抑制 DNA 合成，造成交聯（Hikma, 2026） | 仿單警語：骨髓抑制（血小板與白血球）是最常見也最嚴重的毒性，另有溶血性尿毒症候群。骨髓抑制出現得晚，8 週內都可能發生，平均在第 4 週，所以血球要追蹤到治療後至少 8 週；外滲造成壞死（Hikma, 2026） | 四個癌別的處方沒有用到；美國仿單適應症是合併治療瀰漫性胃腺癌或胰臟腺癌（Hikma, 2026） |
| trabectedin | 來自海鞘；結合 DNA 小溝的鳥糞嘌呤，使雙螺旋彎曲，影響轉錄因子與 DNA 修復（Janssen, 2026; D'Incalci & Galmarini, 2010） | 嗜中性球低下敗血症、橫紋肌溶解（CPK 上升 32%）、肝毒性、心肌病變、微血管滲漏、外滲組織壞死。24 小時輸注，**只能經中心靜脈導管**；每次給藥前 30 分鐘 dexamethasone 20 mg 靜脈注射，並驗 CPK 與肝功能；與 ketoconazole 併用暴露量增加 66%（Janssen, 2026） | 脂肪肉瘤與平滑肌肉瘤（[肉瘤章 5.3](../04-sarcoma.md#53-軟組織肉瘤細胞毒性處方)、[6.5](../04-sarcoma.md#65-trabectedin肝cpk骨髓與導管)） |

---

## 4. 藥物動力學與交互作用

**結論先講：** 開化療前問三件事：這個藥要不要先被身體「拆封」才有效（前驅藥）？它從腎還是從肝離開？病人正在吃的藥會不會擋住它的活化或出口？這三題答完，大部分的劑量調整與交互作用都找得到。

### 4.1 前驅藥：要先活化才有效

| 前驅藥 | 活化步驟 | 臨床意義 |
|--------|---------|---------|
| cyclophosphamide | 肝臟 CYP450（CYP2A6、2B6、3A、2C9、2C19）代謝，最後生成 phosphoramide mustard 與 acrolein（BluePoint, 2026） | 藥本身是前驅藥；泌尿毒性可以致命，大量水化與勤排尿能減少膀胱毒性（BluePoint, 2026） |
| ifosfamide | 肝臟 CYP3A4 與 CYP2B6 羥化，生成 isophosphoramide mustard 與 acrolein（Fresenius Kabi, 2026） | CYP3A4 誘導劑（carbamazepine、phenytoin、rifampin、St. John's wort 等）可能增加有神經與腎毒性的代謝物 chloroacetaldehyde；CYP3A4 抑制劑（azole 類抗黴菌藥、aprepitant、葡萄柚汁等）可能減少活化（Fresenius Kabi, 2026） |
| capecitabine | Carboxylesterase → cytidine deaminase → thymidine phosphorylase，三步變成 5-FU（H2-Pharma, 2026; Miwa et al., 1998） | 口服；之後的代謝與毒性就是 5-FU 的 |
| tegafur（S-1 的成分） | CYP2A6 轉成 5-FU（European Medicines Agency, 2025） | 避免併用 CYP2A6 抑制劑，否則療效可能下降 |
| irinotecan | Carboxylesterase 切掉側鏈變成 SN-38（Actavis, 2025）；SN-38 再經葡萄糖醛酸化由膽汁排出（Thomas & Pommier, 2019） | UGT1A1 活性低的人 SN-38 清得慢，嗜中性球低下的風險較高（Actavis, 2025） |
| temozolomide | 在生理 pH 下自行水解成 MTIC，不需酵素（Merck Sharp & Dohme, 2026） | 口服即可 |
| gemcitabine | 進入細胞後由 nucleoside kinase 磷酸化成二磷酸與三磷酸代謝物（Meitheal, 2025） | 活化在細胞內進行 |

> [!TIP]
> **前驅藥是未拆封的包裹**
> 前驅藥像一個要到指定地點才拆封的包裹。Cyclophosphamide 在肝臟拆封，capecitabine 要拆三層、最後一層在腫瘤附近才拆開，irinotecan 拆開後才是真正有活性的 SN-38。「拆封的酵素」和「回收的酵素」因人而異：DPD 是回收 5-FU 的，UGT1A1 是回收 SN-38 的，回收站不夠力，包裹裡的東西就堆在體內。

> [!IMPORTANT]
> **兩個回收酵素**
> - **DPD（基因 DPYD）** 分解 5-FU。完全缺乏者用 5-FU 或 capecitabine 可能致死，美國仿單要求開藥前檢測，除非必須立即治療（Alembic, 2026; H2-Pharma, 2026）。
> - **UGT1A1** 清除 SN-38。\*28 或 \*6 同型合子，或 \*6/\*28 複合異型合子，irinotecan 起始劑量考慮至少降一級（Actavis, 2025）。
> - 檢測時機、台灣族群的基因頻率與減量表都在[化療基礎第 12 節](../00-shared/01-chemo-basics.md#12-藥物基因檢測與特殊族群評估)，這裡不重複。

### 4.2 從腎走還是從肝走

| 主要出口 | 藥物 | 器官功能不好時，美國仿單怎麼寫 |
|---------|------|------------------------------|
| 腎 | cisplatin | 主要由腎排出；腎功能不全時考慮減量或改用其他治療（WG Critical Care, 2026） |
| 腎 | carboplatin | 主要由腎排出（Natco, 2026）；劑量直接用 GFR 算（Calvert et al., 1989） |
| 腎 | methotrexate | 靜脈給藥後 80–90% 在 24 小時內以原形由尿液排出；腎功能一差，濃度就降不下來（Accord, 2026） |
| 腎 | pemetrexed | CrCl < 45 mL/min 沒有建議劑量（Eli Lilly, 2023） |
| 腎 | capecitabine、S-1 | Capecitabine：CrCl 30–50 mL/min 減量 25%，< 30 mL/min 沒有建議劑量（H2-Pharma, 2026）。S-1：CrCl < 30 mL/min 不建議使用（European Medicines Agency, 2025） |
| 腎 | topotecan、etoposide | Topotecan：CrCl 20–39 mL/min 減為 0.75 mg/m²（Accord, 2025）。Etoposide：CrCl 15–50 mL/min 給 75% 劑量（Hikma, 2024） |
| 腎 | oxaliplatin、eribulin、bleomycin | Oxaliplatin：CrCl < 30 mL/min 減為 65 mg/m²（Sagent, 2025）。Eribulin：CrCl 15–49 mL/min 減為 1.1 mg/m²（Eisai, 2025）。Bleomycin：約 65% 在 24 小時內由尿液排出（Meitheal, 2026） |
| 肝與膽汁 | doxorubicin、epirubicin | Doxorubicin：膽紅素 1.2–3 mg/dL 減量 50%，3.1–5 mg/dL 減量 75%，> 5 mg/dL 不可給（Pfizer, 2026）。Epirubicin：AST 或膽紅素升高要減量（Pharmacia & Upjohn, 2026） |
| 肝 | paclitaxel、nab-paclitaxel、docetaxel | Paclitaxel 由 CYP2C8 與 CYP3A4 代謝，膽紅素異常時暴露量增加（Teva Parenteral Medicines, 2026）。nab-paclitaxel：中重度肝功能不全降低起始劑量（Abraxis, 2022）。Docetaxel：膽紅素 > ULN，或 AST／ALT > 1.5 × ULN 合併 ALP > 2.5 × ULN 避免使用（Mylan, 2026） |
| 肝 | vincristine、vinorelbine | Vincristine：直接膽紅素 > 3 mg/dL 劑量減半（Hospira, 2026）。Vinorelbine：總膽紅素 2.1–3.0 mg/dL 給 50%，> 3.0 mg/dL 給 25%（Sagent, 2024） |
| 肝與膽汁 | irinotecan、eribulin | Irinotecan：膽紅素 > 2 mg/dL 沒有建議劑量（Actavis, 2025）。Eribulin：Child-Pugh A 減為 1.1 mg/m²，Child-Pugh B 減為 0.7 mg/m²（Eisai, 2025） |

記法：**鉑類、抗葉酸藥、capecitabine、topotecan、etoposide、bleomycin 看腎；anthracycline、taxane、vinca、irinotecan 看膽紅素**。上表是仿單文字，臨床處方的減量還要看治療目的與病人狀況，原則見[化療基礎第 7 節](../00-shared/01-chemo-basics.md#7-劑量調整原則)。

### 4.3 第三空間與 methotrexate

Methotrexate 會跑進肋膜積水、腹水這類「第三空間」，再慢慢滲回血液，等於體內多了一個緩釋儲槽：半衰期被拉長，毒性跟著上來。仿單要求給藥前先把明顯的積液引流掉（Accord, 2026）。高劑量 methotrexate 前要確認的事項見[化療基礎第 11.5 節](../00-shared/01-chemo-basics.md#115-高劑量-methotrexatehd-mtx安全摘要)。

### 4.4 重要交互作用

| 化療藥 | 會出事的併用藥 | 後果 | 專師怎麼做 |
|--------|--------------|------|-----------|
| methotrexate | NSAID 與 aspirin、PPI、penicillin 類與 sulfonamide 類抗生素（TMP-SMX 含 sulfamethoxazole）、probenecid（Accord, 2026） | Methotrexate 血中濃度上升；高劑量 methotrexate 併用 NSAID 曾發生嚴重甚至致死的腸胃毒性（Accord, 2026） | 給藥前把這幾類藥從醫囑與病人自備藥裡找出來，和主治與藥師討論停用或替換 |
| pemetrexed | ibuprofen（Eli Lilly, 2023） | Ibuprofen 讓 pemetrexed 清除變慢、暴露量增加（腎功能正常者 AUC 約增加 20%） | CrCl 45–79 mL/min 的病人，給藥前 2 天、當天與之後 2 天避免 ibuprofen（Eli Lilly, 2023） |
| capecitabine、5-FU | warfarin（H2-Pharma, 2026; Alembic, 2026） | INR 上升與出血，capecitabine 為加框警語，曾有死亡案例 | 更頻繁監測 INR，調整抗凝血藥劑量（H2-Pharma, 2026）；細節見[乳癌章 6.4](../03-breast-cancer.md#64-capecitabine手足症候群dpyd-與-warfarin) |
| capecitabine | CYP2C9 受質；仿單另列 phenytoin（H2-Pharma, 2026） | 併用藥的暴露量增加 | 追蹤併用藥的濃度與毒性 |
| irinotecan | 強效 CYP3A4 誘導劑：phenytoin、phenobarbital、carbamazepine、St. John's wort（Actavis, 2025） | Irinotecan 與 SN-38 的暴露量大幅下降，療效打折 | 開始前至少 2 週考慮換成不誘導酵素的藥；沒有替代藥才併用（Actavis, 2025） |
| irinotecan | 強效 CYP3A4 或 UGT1A1 抑制劑，例如 ketoconazole（Actavis, 2025） | Irinotecan 與 SN-38 的暴露量上升 | 開始前至少 1 週停用強效 CYP3A4 抑制劑（Actavis, 2025） |
| docetaxel | 強效 CYP3A4 抑制劑：ketoconazole、itraconazole、voriconazole、clarithromycin、ritonavir 等（Mylan, 2026） | Docetaxel 暴露量上升 | 避免併用（Mylan, 2026） |
| paclitaxel | CYP2C8 或 CYP3A4 的抑制劑與誘導劑（Teva Parenteral Medicines, 2026） | 藥動可能改變 | 併用時小心，留意骨髓與神經毒性 |
| vincristine、vinorelbine | CYP3A 抑制劑；vincristine 仿單點名 itraconazole 與 fluconazole（Hospira, 2026; Sagent, 2024） | 神經肌肉毒性更早出現、更嚴重 | 住院病人正在用 azole 類抗黴菌藥時，給 vinca 前先和主治與藥師確認 |
| trabectedin | Ketoconazole 使暴露量增加 66%；rifampin 使暴露量減少 31%（Janssen, 2026） | 毒性增加或療效下降 | 查併用藥中的 CYP3A 強效抑制劑與誘導劑 |
| doxorubicin | CYP3A4、CYP2D6 或 P-gp 的抑制劑（Pfizer, 2026） | Doxorubicin 濃度上升，毒性增加 | 仿單建議避免併用（Pfizer, 2026） |
| cisplatin | 其他腎毒性藥物（WG Critical Care, 2026） | 更容易發生腎毒性 | 檢查同時段有沒有其他腎毒性藥物與顯影劑檢查 |

> [!IMPORTANT]
> **三組最常考的交互作用**
> 1. Methotrexate ＋ NSAID、PPI、TMP-SMX：methotrexate 排不出去。
> 2. Capecitabine（或 5-FU）＋ warfarin：INR 飆高、出血。
> 3. CYP3A4 抑制劑（azole 類、clarithromycin、ritonavir）＋ docetaxel、vinca、irinotecan、trabectedin：化療藥濃度上升；CYP3A4 誘導劑（phenytoin、carbamazepine、St. John's wort）則讓 irinotecan 與 SN-38 的濃度大幅下降。

口服抗癌藥的交互作用與服藥衛教見[化療基礎第 14.5 節](../00-shared/01-chemo-basics.md#145-口服抗癌藥)。

---

## 5. 臨床怎麼用

**結論先講：** 同一個處方放在不同的治療目的裡，能容忍的毒性與減量的態度完全不同。看處方前先問「這次化療是為了治癒，還是為了延長存活與控制症狀？」。處方的劑量、週期與前置用藥都在各癌別章第 5 段，這裡只講怎麼讀懂它。

### 5.1 治療目的與時機

| 情境 | 目的 | 本手冊的例子 | 對毒性與減量的態度 |
|------|------|-------------|------------------|
| 術前（neoadjuvant） | 手術前先縮小腫瘤，同時提早處理微轉移 | 乳癌 TCHP、KEYNOTE-522（[乳癌章第 5 段](../03-breast-cancer.md#5-常用處方regimen)）；骨肉瘤 MAP（[肉瘤章 5.1](../04-sarcoma.md#51-骨肉瘤map-與高劑量-methotrexate)）；邊緣可切除胰臟癌（[胰臟癌章 4.6](../02-pancreatic-cancer.md#46-邊緣可切除borderline-resectable)） | 目標是治癒，盡量維持劑量與時程 |
| 術後輔助（adjuvant） | 清除看不到的微轉移，降低復發（Fornier & Norton, 2005; Bonadonna et al., 1976） | 乳癌 AC → paclitaxel；胰臟癌 mFOLFIRINOX（[胰臟癌章 4.4](../02-pancreatic-cancer.md#44-術後輔助治療)）；NSCLC 的 cisplatin 雙藥處方 | 同上；用 G-CSF 與支持性照護守住劑量，而不是先減量 |
| 同步化放療（concurrent chemoradiotherapy, CCRT） | 化療和放療同時給，化療藥（如鉑類、taxane）加強放療的局部效果（Seiwert et al., 2007） | 第三期 NSCLC 與局限期 SCLC（[肺癌章 5.2](../01-lung-cancer.md#52-同步化放療ccrt處方)） | 毒性會疊加。Gemcitabine 會加重放療毒性，仿單不建議併用（Meitheal, 2025）；doxorubicin 與 dactinomycin 會引起放射回憶反應（Pfizer, 2026; Eugia, 2024） |
| 緩和性（palliative） | 延長存活、減輕症狀、維持生活品質 | 轉移性胰臟癌 FOLFIRINOX：OS 11.1 對 6.8 個月，6 個月時生活品質明顯惡化的比例 31% 對 66%（Conroy et al., 2011）；GnP：OS 8.5 對 6.7 個月（Von Hoff et al., 2013） | 生活品質優先，毒性大就減量或延後 |
| 高劑量化療加自體幹細胞救援 | 用超過骨髓耐受的劑量，再輸回事先收集的造血幹細胞 | 本手冊只在高風險 Ewing sarcoma 提到（[肉瘤章 4.2](../04-sarcoma.md#42-ewing-sarcoma)）；乳癌沒有可信的證據支持（Fornier & Norton, 2005） | 屬移植病房的治療 |

治療目的怎麼影響減量決定，見[化療基礎第 7.3 節](../00-shared/01-chemo-basics.md#73-治療目標決定調整的方向)。

### 5.2 處方縮寫怎麼讀

縮寫的規則很簡單：一個字母代表一個藥，多半取自學名或舊商品名的第一個字母；前面的小寫字是修飾語，後面的箭頭或斜線表示順序。

| 記號 | 意思 | 例子 |
|------|------|------|
| m | modified，改良版 | mFOLFIRINOX |
| dd | dose-dense，劑量密集（q2w 加 G-CSF） | ddAC |
| nab-、nal- | 白蛋白結合劑型、奈米脂質體劑型 | nab-paclitaxel、nal-IRI |
| HD | high-dose，高劑量 | HD-MTX |
| → 或 -T | 序列，打完前面再接後面 | AC → T |
| ／ | 兩組處方交替 | VDC/IE |
| q2w、q3w、q28d | 每 2 週、每 3 週、每 28 天一個週期 | |
| D1,8 | 每個週期的第 1 天與第 8 天給藥 | |

| 縮寫 | 拆解 | 用在哪裡 | 處方細節 |
|------|------|---------|---------|
| FOLFIRINOX | FOL（folinic acid，即 leucovorin）＋ F（5-FU）＋ IRIN（irinotecan）＋ OX（oxaliplatin）（Conroy et al., 2011） | 胰臟癌 | [胰臟癌章 5.1](../02-pancreatic-cancer.md#51-folfirinox-家族輔助-mfolfirinox-與轉移性-folfirinox) |
| mFOLFIRINOX | 拿掉 5-FU bolus、irinotecan 降為 150 mg/m² 的改良版 | 胰臟癌術後輔助 | 同上 |
| NALIRIFOX | NAL-IRI（liposomal irinotecan）＋ F（5-FU 與 leucovorin）＋ OX（oxaliplatin）（Ipsen, 2025） | 轉移性胰臟癌第一線 | [胰臟癌章 5.2](../02-pancreatic-cancer.md#52-脂質體-irinotecannalirifox-與二線-nal-iri--5-fuleucovorin) |
| GnP | Gemcitabine ＋ nab-Paclitaxel（Von Hoff et al., 2013） | 胰臟癌 | [胰臟癌章 5.3](../02-pancreatic-cancer.md#53-以-gemcitabine-為骨幹的處方) |
| GemCap | Gemcitabine ＋ Capecitabine | 胰臟癌術後輔助 | [胰臟癌章 4.4](../02-pancreatic-cancer.md#44-術後輔助治療) |
| AC、EC | A（Adriamycin，即 doxorubicin）或 E（epirubicin）＋ C（cyclophosphamide） | 乳癌 | [乳癌章 5.1](../03-breast-cancer.md#51-靜脈化療骨幹anthracyclinetaxanecyclophosphamidecapecitabine) |
| AC-T、ddAC-T | AC 之後接 T（Taxol，即 paclitaxel）；dd 表示 q2w（Citron et al., 2003） | 乳癌 | 同上 |
| TC、TAC | T（Taxotere，即 docetaxel）＋ C（cyclophosphamide），TAC 再加 A（doxorubicin） | 乳癌 | 同上 |
| FEC、CMF | F（5-FU）＋ E（epirubicin）＋ C（cyclophosphamide）；C（cyclophosphamide）＋ M（methotrexate）＋ F（5-FU）（Bonadonna et al., 1976） | 乳癌 | 同上 |
| TCH、TCHP | T（docetaxel）＋ C（**carboplatin**）＋ H（Herceptin，即 trastuzumab）± P（pertuzumab） | HER2 陽性乳癌 | [乳癌章 5.2](../03-breast-cancer.md#52-her2-陽性抗-her2-抗體與化療組合) |
| EP | E（etoposide）＋ P（Platinol，即 cisplatin） | SCLC；NSCLC 的同步化放療 | [肺癌章 5.2](../01-lung-cancer.md#52-同步化放療ccrt處方)、[5.3](../01-lung-cancer.md#53-sclc-處方) |
| ABCP | A（**atezolizumab**）＋ B（bevacizumab）＋ C（carboplatin）＋ P（**paclitaxel**） | 非鱗狀 NSCLC | [肺癌章 5.1](../01-lung-cancer.md#51-nsclc-靜脈處方) |
| MAP | M（高劑量 methotrexate）＋ A（doxorubicin）＋ P（cisplatin） | 骨肉瘤 | [肉瘤章 5.1](../04-sarcoma.md#51-骨肉瘤map-與高劑量-methotrexate) |
| VDC/IE | V（vincristine）＋ D（doxorubicin）＋ C（cyclophosphamide），與 I（ifosfamide）＋ E（etoposide）交替 | Ewing sarcoma | [肉瘤章 5.2](../04-sarcoma.md#52-ewing-sarcomavdcie以及高劑量-ifosfamide) |
| AI、EI | A（doxorubicin）或 E（epirubicin）＋ I（ifosfamide），併 mesna | 軟組織肉瘤 | [肉瘤章 5.3](../04-sarcoma.md#53-軟組織肉瘤細胞毒性處方) |
| TC（肉瘤） | T（**topotecan**）＋ C（cyclophosphamide） | 復發 Ewing sarcoma | [肉瘤章 4.2](../04-sarcoma.md#42-ewing-sarcoma) |

縮寫裡的舊商品名：A 是 Adriamycin（doxorubicin；Falzone et al., 2018），T 是 Taxol（paclitaxel；Weaver, 2014）或 Taxotere（docetaxel；Ringel & Horwitz, 1991），P 是 Platinol（cisplatin；Monneret, 2011），MOPP 裡的 O 是 Oncovin（vincristine；Falzone et al., 2018）。

> [!IMPORTANT]
> **同一個字母，不同的藥**
> - **T**：AC-T 是 paclitaxel；TC、TCH 是 docetaxel；肉瘤的 TC 是 topotecan。
> - **C**：AC、TC 是 cyclophosphamide；TCH、ABCP 是 carboplatin。
> - **P**：EP、MAP 是 cisplatin；TCHP 是 pertuzumab；ABCP 是 paclitaxel。
> - **A**：AC、MAP、AI 是 doxorubicin；ABCP 是 atezolizumab。
> - **E**：EC、FEC、EI 是 epirubicin；EP、IE 是 etoposide。
> 核對醫囑時不要只看縮寫，要把每個藥的學名、劑量與給藥日逐一對過。

### 5.3 週期的邏輯：為什麼是 q2w、q3w

化療一個週期的長度，是由「正常骨髓多久能恢復」決定的。打完藥後血球逐漸下降，降到最低的那一點叫 nadir，之後回升；下一個週期要等血球回到安全範圍才能打。

| 藥物 | 仿單描述的最低點 | 常見的週期 |
|------|----------------|-----------|
| doxorubicin | 嗜中性球在第 10–14 天最低，通常第 21 天恢復（Pfizer, 2026） | q3w |
| paclitaxel | 嗜中性球最低點中位數在第 11 天（Teva Parenteral Medicines, 2026） | q3w，或每週低劑量 |
| carboplatin | 單藥時最低點約在第 21 天（Natco, 2026） | q3w 到 q4w |
| mitomycin | 血小板與白血球低下平均在第 4 週，8 週內都可能發生（Hikma, 2026） | 間隔要拉得更長 |

- **q3w 是預設值**：多數藥的最低點在第 2 週前後，第 3 週恢復。
- **q2w 要有條件**：劑量密集處方靠 G-CSF 把恢復時間提前（Citron et al., 2003）；FOLFIRINOX 與 NALIRIFOX 本來就設計成每 2 週一次（Conroy et al., 2011）。
- **每週給藥**（如 gemcitabine D1,8,15、每週 paclitaxel）：單次劑量較低，每次給藥前都要看當天的 CBC。
- **最低點也是感染風險最高的時候**：病人衛教要講清楚「打完藥後第 7–14 天發燒要立刻回來」，處置見[腫瘤急症第 1 節](../00-shared/02-oncologic-emergencies.md#1-發燒性嗜中性球低下)，G-CSF 的使用時機見[支持性照護第 2 節](../00-shared/03-supportive-care.md#2-g-csf預防發燒性嗜中性球低下)。

> [!TIP]
> **割草的比喻**
> 化療像割草：一次割掉一定比例，草（腫瘤）和旁邊的草皮（骨髓）都會被割到。草皮長回來要兩三週，所以不能天天割；但等太久，雜草也長回來了。週期長度就是「草皮剛好恢復、雜草還來不及長回來」的那個時間點。G-CSF 是幫草皮施肥，讓我們能早一週再割一次。

---

## 6. 毒性與處置

**結論先講：** 化療毒性分兩種。一種是「殺分裂細胞」的共同毒性（骨髓、黏膜、毛囊），幾乎每個藥都有；另一種是個別藥物的招牌毒性（腎、耳、心、肺、神經），要靠累積劑量與症狀去抓。CTCAE 分級後的處置表、解毒劑劑量與外滲流程都在共用章，本段只講「看到什麼、第一步做什麼、去哪裡查」。

| 系統 | 常見元兇 | 怎麼認 | 專師第一步 | 詳見 |
|------|---------|--------|-----------|------|
| 骨髓 | 幾乎所有細胞毒性藥；最低點時間見 5.3 | 化療後發燒、畏寒；瘀青、出血；喘與疲倦 | 發燒就當急症：生命徵象、抽血與血液培養、盡快給經驗性抗生素，不等報告 | [腫瘤急症第 1 節](../00-shared/02-oncologic-emergencies.md#1-發燒性嗜中性球低下)、[支持性照護第 2 節](../00-shared/03-supportive-care.md#2-g-csf預防發燒性嗜中性球低下)、[第 10 節](../00-shared/03-supportive-care.md#10-化療相關貧血血小板低下與輸血) |
| 噁心嘔吐 | cisplatin（加框警語；WG Critical Care, 2026）；dacarbazine（最常見的毒性；Hikma, 2025） | 急性、延遲性、預期性 | 給藥前確認止吐組合符合處方的致吐等級，第一個週期就給足 | [支持性照護第 1 節](../00-shared/03-supportive-care.md#1-化療引起的噁心嘔吐cinv) |
| 口腔與腸道 | 5-FU、capecitabine、S-1、methotrexate、irinotecan | 口腔潰瘍、水瀉次數、脫水；irinotecan 輸注後幾小時內的腹瀉常伴隨膽鹼性症狀，24 小時後的遲發性腹瀉可以很嚴重（Thomas & Pommier, 2019） | Irinotecan 早發性腹瀉給 atropine，遲發性立刻開始 loperamide 並補液；出現腸阻塞、發燒或嚴重嗜中性球低下要加抗生素（Actavis, 2025） | [支持性照護第 4 節](../00-shared/03-supportive-care.md#4-口腔黏膜炎)、[第 5 節](../00-shared/03-supportive-care.md#5-腹瀉)；[胰臟癌章 6.2](../02-pancreatic-cancer.md#62-irinotecan-與脂質體-irinotecan)；[腫瘤急症第 11.6 節](../00-shared/02-oncologic-emergencies.md#116-嗜中性球低下性小腸結腸炎ne) |
| 腎與泌尿 | cisplatin；高劑量 methotrexate；ifosfamide 與 cyclophosphamide（出血性膀胱炎）；gemcitabine 與 mitomycin（HUS；Meitheal, 2025; Hikma, 2026） | 肌酸酐上升、尿量減少、血尿、低血鎂；HUS 是貧血、血小板低下加腎功能惡化（Hikma, 2026） | 確認水化與 mesna 已開立；找出併用的腎毒性藥物；懷疑 HUS 先暫停給藥並通知主治 | [化療基礎第 11.5 節](../00-shared/01-chemo-basics.md#115-高劑量-methotrexatehd-mtx安全摘要)、[第 11.6 節](../00-shared/01-chemo-basics.md#116-ifosfamide-安全摘要)；[肉瘤章 6.4](../04-sarcoma.md#64-cisplatin腎耳與神經) |
| 周邊神經 | oxaliplatin（遇冷）、cisplatin、taxane、vinca、eribulin | 手腳麻刺、扣鈕扣困難、走路不穩 | 每次給藥前問功能；oxaliplatin 病人避免冰飲與冰敷（Sagent, 2025）；vinorelbine 第 2 級以上神經病變仿單要求停藥（Sagent, 2024） | [支持性照護第 11 節](../00-shared/03-supportive-care.md#11-化療相關周邊神經病變與手足症候群)、[第 11.4 節](../00-shared/03-supportive-care.md#114-oxaliplatin-的急性與累積神經病變) |
| 中樞與自主神經 | ifosfamide（腦病變）；5-FU（高血氨腦病變）；vincristine（便秘、麻痺性腸阻塞） | 意識或行為改變、嗜睡；多日未排便、腹脹 | Ifosfamide 出現腦病變就停藥（Fresenius Kabi, 2026）；5-FU 高血氨腦病變要暫停並降血氨（Alembic, 2026）；vincristine 病人一律預防性使用軟便藥（Hospira, 2026） | [化療基礎第 11.6 節](../00-shared/01-chemo-basics.md#116-ifosfamide-安全摘要)；[肉瘤章 6.2](../04-sarcoma.md#62-ifosfamide腦病變出血性膀胱炎與腎小管損傷)；[支持性照護第 6 節](../00-shared/03-supportive-care.md#6-便秘) |
| 心臟 | anthracycline（累積劑量；Pfizer, 2026）；5-FU 與 capecitabine（心絞痛、心律不整；Alembic, 2026; H2-Pharma, 2026）；cyclophosphamide（BluePoint, 2026）；trabectedin（Janssen, 2026）；paclitaxel（嚴重傳導異常 < 1%；Teva Parenteral Medicines, 2026） | 喘、下肢水腫、胸痛、心悸 | 給藥前自己加總 anthracycline 累積劑量、確認 LVEF 有做；5-FU 出現心臟毒性仿單要求暫停（Alembic, 2026），輸注中胸痛先停止輸注、做心電圖、通知主治 | [化療基礎第 11.3 節](../00-shared/01-chemo-basics.md#113-累積劑量上限)；[乳癌章 6.1](../03-breast-cancer.md#61-anthracycline累積劑量與心臟毒性)；[肉瘤章 6.3](../04-sarcoma.md#63-doxorubicin累積劑量dexrazoxane-與外滲) |
| 肺 | bleomycin（Meitheal, 2026）；gemcitabine（Meitheal, 2025）；mitomycin（Hikma, 2026）；methotrexate（Accord, 2026）；topotecan 的間質性肺病（Accord, 2025）；nab-paclitaxel 的肺炎（Abraxis, 2022） | 新的乾咳、活動喘、血氧下降 | 暫緩下一劑，安排影像並排除感染；用過 bleomycin 的病人日後手術要告知麻醉科（Meitheal, 2026） | [肺癌章 6.5](../01-lung-cancer.md#65-化療) |
| 肝 | trabectedin（Janssen, 2026）；docetaxel（Mylan, 2026）；dacarbazine（Hikma, 2025）；dactinomycin 的 VOD（Eugia, 2024）；methotrexate（Accord, 2026） | AST、ALT、膽紅素上升；右上腹痛、腹水 | 給藥當天對照處方的肝功能門檻，不符合就先不給並通知主治 | [肉瘤章 6.5](../04-sarcoma.md#65-trabectedin肝cpk骨髓與導管) |
| 皮膚與血管 | 手足症候群：capecitabine、5-FU、liposomal doxorubicin（H2-Pharma, 2026; Alembic, 2026; Sagent, 2026）；外滲壞死：anthracycline、vinorelbine、dactinomycin、mitomycin、trabectedin（Pfizer, 2026; Sagent, 2024; Eugia, 2024; Hikma, 2026; Janssen, 2026） | 手掌腳掌紅腫痛；注射部位疼痛、腫、回血不順 | 懷疑外滲立刻停止輸注，照外滲流程處理；vinca 外滲用熱敷加 hyaluronidase（Hospira, 2026），doxorubicin 外滲可嚴重到需要植皮（Pfizer, 2026） | [化療基礎第 9 節](../00-shared/01-chemo-basics.md#9-血管外滲extravasation)；[支持性照護第 11.6 節](../00-shared/03-supportive-care.md#116-手足症候群hfs與手足皮膚反應hfsr) |
| 過敏與輸注反應 | paclitaxel（溶劑；Teva Parenteral Medicines, 2026）、docetaxel（polysorbate 80；Mylan, 2026）、carboplatin 與 oxaliplatin（Natco, 2026; Sagent, 2025）、etoposide（Hikma, 2024）、liposomal doxorubicin（Sagent, 2026）、bleomycin 的特異體質反應（Meitheal, 2026） | 潮紅、蕁麻疹、喘、低血壓、胸悶、背痛 | 停止輸注、保留管路、依過敏流程處理；事後確認前置用藥有沒有給、給的時間對不對 | [腫瘤急症第 10 節](../00-shared/02-oncologic-emergencies.md#10-輸注反應過敏反應與過敏性休克) |
| 生殖與長期 | 烷化劑（不孕）；烷化劑與 topoisomerase II 抑制劑（次發性白血病，見第 7 段） | 治療前就要談 | 第一個週期前完成生育力保存諮詢與避孕衛教，並記錄 | [化療基礎第 12.5 節](../00-shared/01-chemo-basics.md#125-生育力保存與避孕諮詢) |

> [!WARNING]
> **化療後發燒是急症**
> 骨髓抑制本身不會痛，病人第一個症狀常常就是發燒。打過化療的病人只要發燒，在證明不是之前都當成發燒性嗜中性球低下處理，不要先給退燒藥觀察。Topotecan 的嗜中性球低下還可能併發嗜中性球低下性結腸炎（Accord, 2025），所以「發燒加腹痛」更要警覺。

> [!WARNING]
> **5-FU 或 capecitabine 第一個週期就出現嚴重毒性**
> 很早就出現、或嚴重得不尋常的黏膜炎、腹瀉、嗜中性球低下或神經毒性，要想到 DPD 缺乏：先停藥、通知主治（Alembic, 2026; H2-Pharma, 2026）。美國仿單記載，5-FU 過量時 uridine triacetate 要在輸注結束後 96 小時內給（Alembic, 2026）；台灣能不能取得見[化療基礎第 11.4 節](../00-shared/01-chemo-basics.md#114-解毒劑與防護劑何時給給多少台灣有沒有)。

> [!IMPORTANT]
> **Irinotecan 的兩種腹瀉**
> - **早發性**：給藥中或給藥後不久，伴隨流汗、流淚、腹絞痛等膽鹼性症狀，用 **atropine**。
> - **遲發性**：可致命，一開始就用 **loperamide**，並補充水分與電解質（Actavis, 2025）。
> 兩種腹瀉的藥不能搞反。Liposomal irinotecan 的處理原則相同（Ipsen, 2025）。

> [!NOTE]
> **流程與備藥依院內規範**
> 外滲處理包的內容、過敏反應的給藥順序、G-CSF 與止吐藥的品項，各院不同。實習的第一週先找到院內的「化療外滲處理流程」與「化療過敏反應處理流程」，並確認病房的急救藥品放在哪裡。

---
