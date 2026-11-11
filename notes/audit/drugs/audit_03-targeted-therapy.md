# Audit log: handbook/05-drugs/03-targeted-therapy.md

Audited 2026-11-11. Lint after fixes: `python3 tools/lint_chapter.py handbook/05-drugs/03-targeted-therapy.md` gives 0 error, 0 warn.

## How it was checked

- **References.** All 126 PMIDs were fetched with the PubMed tool (`get_article_metadata`, 8 batches of 15 or 16) and again as PubMed XML through E-utilities. A script compared authors, year, title, journal, volume, issue, pages and DOI field by field. The 11 label entries were checked against the DailyMed SPL files (set ID, labeler, product title, effective date) and the EMA Alecensa PDF (creation date 2025-11-05).
- **Claims.** Every abstract was read against the chapter. Full text was opened where the chapter goes beyond the abstract: Bardia 2025, Drago 2021, Hendrikx 2017, Lacouture 2011, Leonetti 2019, Ogitani 2016, Porta-Sánchez 2017, Sequist 2011, Swain 2015 (PMC); Nowell 2007 (JCI site). Every label statement was searched in the ten FDA label texts and the EMA product information. A second script checked that each number next to a citation occurs in the cited abstract, full text or label; the only misses were years, month numbers and a trial name.
- **Imatinib dates.** FDA approval letters for NDA 21-335 and NDA 21-335/S-001, plus the Drugs@FDA record for NDA 021335.

## Fixes (section: what was wrong -> what it is now; source)

1. §1 timeline, 1960: "第一次把特定的染色體異常和特定癌症連在一起" is a "first" claim that Nowell 2007 does not make -> "把一個固定出現的染色體異常和一種癌症連在一起". Source: Nowell 2007 (JCI full text).
2. §1 timeline, 1973: the 9;22 translocation was attributed to Rowley 1973 "用新的染色法", which goes beyond what a title-only source supports -> Rowley 1973 is now cited for the quinacrine fluorescence and Giemsa finding of a new consistent abnormality in CML (its title), and Nowell 2007 for the 9;22 translocation. Sources: PubMed record 4126434; Nowell 2007.
3. §1.1: imatinib CML approval was "2001 年" only -> 2001-05-10, accelerated approval, for blast crisis, accelerated phase, or chronic phase after interferon failure. Source: FDA approval letter NDA 21-335; Drugs@FDA lists ORIG-1 approved 05/10/2001. New reference added.
4. §1.1: GIST approval was "美國隨後核准" -> 2002-02-01, KIT-positive unresectable or metastatic GIST. Source: FDA letter NDA 21-335/S-001; Drugs@FDA lists SUPPL-1 approved 02/01/2002. The "February 1, 2001" in the Dagher 2002 abstract is a misprint: the supplement was submitted in October 2001. New reference added.
5. §1.7: "第一個 ADC 是…gemtuzumab ozogamicin" -> "最早核准的 ADC 是…". Drago 2021 says first ADC approved by the FDA, not the first ADC made.
6. §2.2 pathway table: inavolisib had no source in the citation list -> Turner et al., 2024 added.
7. §3.1: gefitinib and erlotinib "最早的 EGFR TKI" had no source -> "FLAURA 把這兩個藥當成標準 EGFR TKI 對照組（Soria 2018）；gefitinib 是可逆的抑制劑（Wu 2017）".
8. §3.3: pertuzumab "第二個抗 HER2 單株抗體" is not in Swain 2015 -> "人源化抗 HER2 單株抗體，結合的 HER2 位置與 trastuzumab 不同，兩者合用阻斷更完整". Source: Swain 2015 full text (PMC5584549).
9. §3.4 avapritinib: mechanism cell was uncited and described it as a PDGFRA exon 18 drug -> "KIT 與 PDGFRA 的 TKI，能強力抑制 PDGFRA D842V（Heinrich 2020）". The 2.9% and 33% figures were given without saying they are pooled across diseases -> intracranial haemorrhage 2.9% is 749 patients with GIST or AdvSM (GIST alone 3 of 267, 1.1%); cognitive effects 33% is 995 patients including low-dose ISM, and 41% of 601 GIST patients. Source: Ayvakit US label effective 2026-10-20, sections 5.1 and 5.2.
10. §3.5: "三個藥…一定和內分泌治療併用" is a false "always" (abemaciclib has monotherapy data, and the breast chapter gives a separate monotherapy dose) -> "本章列出的試驗都是和內分泌治療併用（abemaciclib 另有單用的研究；Goetz 2017）".
11. §3.8: Dato-DXd "不需驗 Trop-2" had no source -> adds that TROPION-Breast01 did not select patients by Trop-2 expression. Source: Bardia 2025 full text, eligibility criteria.
12. §4.1: "gefitinib、erlotinib、dacomitinib…與 PPI、H2 阻斷劑、制酸劑各自要錯開幾小時" contradicted lung chapter 5.4, which says avoid PPIs and space H2 blockers and antacids -> rewritten to match.
13. §4.2 warning box: removed "台灣肺癌病人同時需要抗結核藥並不少見" (unsourced Taiwan claim; decorative).
14. §5.2: CLEOPATRA OS 56.5 vs 40.8, HR 0.68 (Swain 2015) -> end-of-study 57.1 vs 40.8, HR 0.69, 8-year OS 37% vs 23% (Swain 2020), matching the breast chapter. Verified in PubMed (PMID 32171426, doi 10.1016/S1470-2045(19)30863-0). New reference added.
15. §5.2: DESTINY-Breast03 "OS HR 0.64" was unlabelled while the breast chapter gives the later 52.6 vs 42.7, HR 0.73 -> labelled as the interim analysis with medians not reached, with a link to breast chapter 4.8 for the update.
16. §5.2: HER2CLIMB OS 21.9 vs 17.4 was unlabelled while the breast chapter gives the final 24.7 vs 19.2 -> labelled "初次分析", pointer to breast chapter 4.8.
17. §6.2 warning box: "ILD 是這一章最容易致死…的毒性" is an unsupported superlative -> "ILD 會致死，也容易被延誤".
18. §6.9: avapritinib row -> same population wording as fix 9.
19. Label origin: ten label citations did not say which label -> "美國仿單" added (§6.3 T-DXd and osimertinib; §6.4 regorafenib; §6.9 embryo-fetal row; §8.1 exclusion row and pregnancy row; quiz explanations Q6, Q8, Q9, Q10, Q13).

### Drug cards (section 9)

20. gefitinib: "胃酸抑制劑降低吸收，要錯開" -> "盡量避免 PPI，H2 阻斷劑與制酸劑要錯開" (lung chapter 5.4).
21. dacomitinib: "胃酸抑制劑要錯開" -> "盡量避免 PPI，H2 阻斷劑要錯開" (lung chapter 5.4).
22. osimertinib: "新的喘咳立即停藥評估；心電圖；高風險者測 LVEF" -> "先暫停並評估 ILD，確診即永久停藥；高風險者做心電圖；有心臟危險因子者測 LVEF" (Tagrisso US label).
23. pertuzumab: "第二個抗 HER2 抗體" -> "結合的 HER2 位置與 trastuzumab 不同，兩者合用（雙標靶）".
24. imatinib: "腫瘤出血約 5%" -> "胃腸道或腹腔內出血約 5%" (Demetri 2002 wording).
25. avapritinib: class, mechanism and toxicity cells -> "KIT／PDGFRA TKI"; pooled 2.9% and GIST 41% labelled.
26. olaparib: "CYP3A 抑制劑要減量" -> "避免強效或中效 CYP3A 抑制劑，避不開才減量" (Lynparza US label 2.4).
27. T-DM1: "每次給藥前看血小板與肝功能" is not stated with a citation in this chapter's body -> "追蹤血小板與肝功能，時程見乳癌章 6.7".

### Quiz (section 10)

All 16 questions were solved independently. Every key is the single best answer and the distractors are clearly wrong. No stem, option or key was changed. Five explanations (Q6, Q8, Q9, Q10, Q13) gained a "美國仿單" tag (fix 19). Format is unchanged.

### References (section 11)

- 126 PMID entries: no mismatch in authors, year, title, journal, volume, issue, pages or DOI. No PMID points to a different paper. The only differences from PubMed are editorial (suffixes written "III" and "II" where PubMed has "3rd" and "2nd"; "Letter:" and "Cancer." title prefixes omitted for Rowley 1973 and Weinstein 2002).
- 11 label entries: set IDs, labelers and effective dates all match DailyMed and EMA.
- Added three entries: Swain et al. 2020 (PMID 32171426); Food and Drug Administration 2001 (NDA 21-335 approval letter); Food and Drug Administration 2002 (NDA 21-335/S-001 approval letter).

## Writer's notes: outcome

- Rowley 1973, Köhler & Milstein 1975, Folkman 1971, Weinstein 2002 (no abstract): Rowley tightened (fix 2). The other three statements do not go beyond the titles. The Weinstein description matches his own later abstract (Weinstein & Joe 2008, PMID 18451130), read as a check and not cited.
- Imatinib dates: tightened (fixes 3 and 4).
- CLEOPATRA: aligned to the breast chapter (fix 14).
- Avapritinib label: the 2026-10-20 version still carries every statement the sarcoma chapter takes from the 2026-08-05 version.
- Facts re-sourced after dropping PAPILLON, the Datroway label and the US Alecensa label: every alectinib figure is in the EMA product information (myalgia 35.3%, CPK 56.2%, bradycardia 11.3%, with food, LFT every 2 weeks for 3 months, CPK every 2 weeks for the first month, heart rate and blood pressure). Every Dato-DXd figure is in Bardia 2025 (stomatitis 50%, nausea 51.1%, ocular surface events 40%, dry eye 21.7%, keratitis 14.4%, adjudicated ILD 3.3%, PFS HR 0.63, OS HR 0.84). No PAPILLON figure remains.
- Dose, monitoring and class-toxicity statements: all match the cited labels (ILD, LVEF, QT, hyperglycaemia, hypertension, proteinuria, surgery interval, lipids, CYP3A rules).

## Problems found in other files (not edited)

- `handbook/03-breast-cancer.md`, reference list: the Swain et al. (2020) entry omits the group author "CLEOPATRA study group" that PubMed lists after Cortés, J.
- `handbook/04-sarcoma.md`, reference list: Ayvakit label cited as effective 2026-08-05; DailyMed now serves the version effective 2026-10-20. The statements used are unchanged.
- `handbook/04-sarcoma.md`, lines 1165 and 1906: "avapritinib 顱內出血 2.9%" without the pooled denominator (GIST and AdvSM, 749 patients). The label's GIST-only figure is 1.1% (3 of 267). Lines 1394 and 1837 do give the denominator.
- No numerical conflict found with the lung, pancreatic or sarcoma chapters for the trials this chapter shares with them.

## Not checked, and why

- Imai & Takaoka 2006: no open full text. Only two general statements rest on it (where antibodies and small molecules act).
- Folkman 1971, Köhler & Milstein 1975, Rowley 1973, Weinstein 2002: no abstract and no open full text. Checked against titles and secondary sources only.
- Nowell 2007: PMC serves only the abstract. The full text was read through WebFetch on the JCI site, which returns a model summary with quotes, not the raw page.
- Keizer 2010 and van Leeuwen 2014: abstract only. The chapter's statements are all in the abstracts.
- Taiwan-approved labels: not compared. The chapter's existing 待核對 box already says so. The chapter makes no Taiwan licence or NHI claim of its own, so `sources/nhi/section9-1151022.md` was not needed.
- Sibling chapters 01, 02, 04, 05 in `handbook/05-drugs/`: read-only spot check for imatinib, gemtuzumab and CLEOPATRA; no conflict seen, nothing edited.
