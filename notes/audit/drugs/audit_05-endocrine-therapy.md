# Audit log: handbook/05-drugs/05-endocrine-therapy.md

Auditor run 2026-11-11. Only this chapter file was edited. Lint after fixes: 0 error, 0 warn.

How things were checked: all 91 PMIDs (plus the inline Beatson PMID 29584099) fetched from PubMed and compared field by field; abstracts read for every PMID; full text read for Jordan 2006, Quirke 2017, Denmeade & Isaacs 2002, Cole 1971, CPIC 2018, ASCO 2010 and 2014, Hanker 2020, Crawford 2019, Bardia 2024, Toy 2013, Kelly 2010, POSITIVE, and parts of others; all 14 DailyMed labels downloaded as SPL XML and searched for each cited statement; FDA elacestrant approval page, FDA CYP examples table and NobelPrize.org page read directly; NHI 9.72 read in `sources/nhi/section9-1151022.md`. Every number in the chapter body was also machine-matched against the collected source texts (no unmatched numbers).

## Fixes (section | what was wrong | what it is now | source)

### References (section 11)
- Baum 2002 | author initial "Klijn, J. G. M." not in PubMed | "Klijn, J. G." | PubMed 12090977
- Huggins & Hodges 1972 | title had "of estrogen and of androgen injection" | "of estrogen and androgen injection" | PubMed 4625049
- Nobel Prize Outreach 2026 | note said the page was read only through a search summary | note removed; page read directly (Guillemin 1/4, Schally 1/4, Yalow 1/2) | nobelprize.org
- Arvinas 2026 (Veppanu) | "(revised 2026-04)" only | "(revised 2026-04; DailyMed version 2, published 2026-05-20)" | DailyMed page and history API
- All other 104 entries matched PubMed or DailyMed (authors, year, title, journal, volume, issue, pages, DOI, setid, effective date). No PMID pointed to a different paper.

### Claims
- 0 必背數字 | endometrial cancer 0.4% vs 1.2% had no time frame | "10 年子宮內膜癌" | EBCTCG 2015 abstract
- 1 timeline 1896 | "第一次證明乳癌受荷爾蒙控制" (a "first" the source does not state) | "從此知道部分乳癌的生長依賴卵巢" | Jordan 2006
- 1 timeline 1941 | "第一個全身性的癌症荷爾蒙治療" | "口服雌激素的藥物去勢成為第一個有效的全身性癌症治療" | Denmeade & Isaacs 2002
- 1 timeline 1958 | Lerner "發現" MER-25 in 1958, "停止開發" | "報告" (discovered mid-1950s, reported 1958), "停止臨床研究" | Jordan 2006; Quirke 2017
- 1 timeline 1971 | "ER 成為第一個預測療效的 biomarker" (unsupported "first") | "ER 成為預測內分泌治療反應的 biomarker" | Jensen & Jordan 2003 abstract; Jordan 2006
- 1 timeline 1973 | "第一個上市的 ER 標靶藥" (not in the cited source; Jordan 2006 notes clomiphene, another ER ligand, was also marketed for ovulation induction), "晚期乳癌" | "乳癌的第一個標靶治療藥上市"; licence and launch for anovulatory infertility and palliative treatment of breast cancer | Jordan 2006; Quirke 2017
- 1 timeline 1984 | "單次肌肉注射治療" (abstract: single injection for the estradiol measurement, responses up to 4 months) | "肌肉注射治療" | Coombes 1984 abstract
- 1 timeline 1991, 1998, 2023 | "first" claims cited to sources that do not say "first" | added Osborne 2004, Jordan 2006, Bardia 2024; 2023 row reworded to "第一個在第三期試驗勝過標準內分泌單藥的口服 SERD" | those sources
- 1.1 | "第一次有人用「拿掉荷爾蒙」治療癌症" | "用「拿掉荷爾蒙」治療乳癌的開端" | Jordan 2006
- 1.3 heading | "第一個預測性 biomarker" | "預測內分泌治療反應的 biomarker" | as above
- 1.4 | Jordan's ER-binding and DMBA work placed "1974 年起在里茲大學" | "從 1972 年起先在美國的 Worcester Foundation、1974 年回到里茲大學後繼續" | Jordan 2006 full text
- 1.5 | "第一個被當成 AI 使用的藥是 aminoglutethimide" | "早期被當成 AI 使用的藥" | Santen 2009 abstract
- 1.7 | "第一個成功的是 elacestrant" (FDA page does not say this) | "第一個在第三期試驗勝過標準內分泌單藥的是 elacestrant（Bardia et al., 2024）" | Bardia 2024 full text
- 3.1 raloxifene | VTE-history contraindication was on the card but not in the body | added "現在或過去有 VTE 者禁用" | Evista label
- 3.2 | "比 tamoxifen 多降低約三成的復發" without the qualifier | "在兩組用藥不同的期間" added | EBCTCG 2015 abstract
- 3.4 fulvestrant | indication summarised as postmenopausal for all uses | monotherapy postmenopausal; with ribociclib postmenopausal; with palbociclib or abemaciclib in women after endocrine therapy; pre/perimenopausal women on the combinations need an LHRH agonist | Faslodex label
- 3.4 imlunestrant | chapter silent on the GnRH-agonist question | new paragraph: the sentence existed in label versions up to 2026-06-04 and is absent from the current 2026-09-18 version, which also adds the abemaciclib combination | DailyMed versions 4, 6, 7, 8
- 3.5 megestrol | "確切的抗腫瘤機轉不明" stated for all uses | label says unknown for endometrial carcinoma; for breast, modifies other steroid hormones and has a direct effect on tumour cells | Teva label
- 4.1 half-life | unsourced "偶爾漏一天影響不大"; citation placed mid-sentence | removed; steady state about 4 weeks is for tamoxifen; "about 2 months to clear" attributed to the label's patient information | tamoxifen label
- 4.1 CYP2D6 | heading "CYP2D6 抑制劑會讓它「吃了等於沒吃」" (causal wording for a cohort study) | "強效 CYP2D6 抑制劑會壓低 endoxifen，療效可能打折" plus a sentence that the cohort shows association and that ASCO calls the outcome evidence limited and indirect | Kelly 2010; CPIC 2018; ASCO 2010
- 4.3 | unsourced "血中濃度要好幾個月才會爬到穩定" | label statement: the extra dose two weeks after the first lets steady state be reached within the first month | Faslodex label 12.3
- 5.2 aTTom | "這個試驗只以 2013 年的會議摘要發表" (cannot be confirmed as of 2026) | "ASCO 指引引用的是這個試驗 2013 年的會議摘要" | ASCO 2014 full text
- 7.3 table VERITAC-2 | only NEJM HR | NEJM HR 0.58 (0.43–0.78) kept; label HR 0.57 (0.42–0.77) added with label citation | Campone 2025; Veppanu label
- 7.3 table EMBER-3 | combination benefit "不論 ESR1 狀態" with no note on the indication | added "但美國仿單的併用適應症仍限 ESR1 突變" | Inluriyo label 2026-09
- 7.3 考點 | "imlunestrant 的整體存活結果本章沒有查到" | label states OS immature (31% of deaths in the ESR1m population) | Inluriyo label
- 7.4 SERENA-6 | "548 人驗出 ESR1 突變" cited only to Bidard 2025 | Turner 2026 added (the abstract that gives 548 and 23 countries) | PubMed 42442380
- 8.3 | "規律運動是目前證據最好的方法" (unsupported superlative) | "規律運動在臨床試驗中證明可以減輕疼痛" | Irwin 2015

### Quiz
- Q1 | stem described a stage I patient not needing chemotherapy; by ASCO 2016 options C and D (adding OFS) are also not recommended for her, so "不適當" had three defensible answers | stem now asks which prescription is inappropriate at any risk level; explanation rewritten with Burstein 2016 | ASCO 2010, 2016
- Q2–Q15 solved independently; keys and distractors hold. Format unchanged.

### Drug cards
- fulvestrant | "停經後 HR 陽性晚期乳癌，單用或併 CDK4/6 抑制劑" | "HR 陽性晚期乳癌：停經後單用，或併 CDK4/6 抑制劑" | Faslodex label
- megestrol | "抗腫瘤機轉不明，可能與抑制促性腺激素有關" | "確切抗腫瘤機轉不明；仿單提到抑制促性腺激素與直接作用於腫瘤細胞" | Teva label
- raloxifene card kept; its VTE cell is now backed by the body text.

### Settled without a change to the chapter
- EMERALD numbers (478; 3.8 vs 1.9 months; HR 0.55, 0.39–0.77; OS HR 0.90, 0.63–1.30; ≥12 months subgroup 8.6 vs 1.9, HR 0.41) are all present in the three cited sources.
- aTTom numbers match the ASCO 2014 tables (6,953; 580 vs 672; 102, 2.9% vs 45, 1.3%).
- Veppanu date: DailyMed Highlights show "Revised: 4/2026"; SPL version 2 was published 2026-05-18 and 2026-05-20; the SPL document effective-time field reads 2025-05-01 (apparent labeler typo, shown on the page as "Updated May 1, 2025").
- CYP2D6 lists match the FDA table (content current 2026-05-29); venlafaxine is not on it. CPIC table, fulvestrant schedule, goserelin flare, SOFT-EST, Smith 2006, bone, VTE, endometrial and POSITIVE statements match their sources and the breast chapter.
- Label citations resolve correctly under the lint matcher (AstraZeneca 2020 = Faslodex, 2026 = Etcamah; Novartis 2024 = Femara, 2026 = Kisqali; Eli Lilly 2023 = Evista, 2026 = Inluriyo).
- NHI 9.72 menopause evidence (age 55, bilateral oophorectomy, FSH and estradiol) matches the NHI source file.

## Problems found in other files (not edited)
- `handbook/03-breast-cancer.md` lines 667 and 1081: say the imlunestrant label requires a GnRH agonist in pre/perimenopausal women (and men). This was true of Inluriyo label versions effective up to 2026-06-04 (the version that chapter cites at lines 980 and 3060). The current DailyMed version (version 8, effective 2026-09-18, "Revised: 09/2026", published 2026-10-01) no longer contains that sentence and adds an indication in combination with abemaciclib for ESR1-mutated disease. The breast chapter's version date and wording are out of date.
- `handbook/03-breast-cancer.md` line 939: vepdegestrant "美國仿單 2026-06-12". No date on the Veppanu DailyMed record matches (Revised 4/2026; published 2026-05-18 and 2026-05-20). 2026-06-12 is the Truqap label date listed at line 980. The breast chapter also has no reference-list entry for the Veppanu label.
- Not an error, for information: breast chapter line 1355 gives P-1 endometrial cancer RR 2.48 (1.27–4.92) from the tamoxifen label; this chapter gives RR 2.53 (1.35–4.97) from Fisher 1998. Each matches its own source.

## Could not check, and why
- ASCO 2023 ESR1 rapid update (Burstein 2023): publisher returns 403 and PubMed has no abstract. The chapter's wording still rests on an ASCO Post summary and stays inside the existing 待核對 box.
- NCCN menopause definition: no access to NCCN; stays in the existing 待核對 box.
- Abstract-only checks (no open full text): ASCO 2016 and 2019 endocrine updates, ASCO osteoporosis, sexual health, cachexia and male breast cancer guidelines, ASCO/CAP 2020, ACOG 2014, Simpson 2003, Santen 2009, and the NEJM, Lancet and JCO trials without PMC copies. Jensen 1971, Harper & Walpole 1967 and Huggins & Hodges 1972 have no abstract; their claims were checked through Jordan 2006, Quirke 2017, Cole 1971 and Denmeade & Isaacs 2002.
- First names "Angela" and "Harry" Brodie: confirmed only through a search-result summary (Santen 2009 full text is blocked).
- Taiwan licence statements in the 7.4 box were compared with the breast chapter only, not with TFDA.
- PMC began serving a CAPTCHA after a few requests and Europe PMC returned 500 for many articles, which is why some full texts were not read.


## Follow-up by the orchestrator (2026-11-11)

- The note above on `handbook/03-breast-cancer.md` line 939 is wrong: DailyMed holds two VEPPANU records. The Rigel Pharmaceuticals record (setid 484e21ba-8fe1-4c6d-b923-8ba4cf5b2f20) has effective date 2026-06-12, which is the date the breast chapter cites. No change was made to that line.
- Imlunestrant: the current INLURIYO label (effective 2026-09-18) was re-fetched from DailyMed. It contains no GnRH/LHRH agonist sentence and lists a combination indication with abemaciclib for ESR1-mutated disease. The breast chapter (sections 4.5 and 5.5) now says which label version each statement comes from.
