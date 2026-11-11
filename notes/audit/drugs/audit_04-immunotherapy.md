# Audit log: handbook/05-drugs/04-immunotherapy.md

Auditor run: 2026-11-11. File edited: `handbook/05-drugs/04-immunotherapy.md` only.
Working files: `/tmp/claude-0/-home-user-oncology-educater/6a66dc7f-55e5-547a-b95f-33d6978992bf/scratchpad/drugs/audit04/` (PubMed XML and MCP metadata, five DailyMed labels, FDA pages, PMC full texts, comparison scripts).

## How it was checked

- References: all 140 PMIDs fetched twice (PubMed MCP `get_article_metadata` in 9 batches, and NCBI efetch XML) and compared field by field with a script (authors incl. the 19 + last rule, year, title, journal, volume, issue, pages, DOI). The two PubMed sources agree with each other. All 140 PMIDs point to the cited paper (no wrong-PMID entry). The 1985 and 1988 Rosenberg author lists (PubMed truncates at 10) were confirmed in Crossref.
- Labels: Keytruda v229 (effective 2026-10-16), Opdivo v68 (2026-08-12), Tecentriq v46 (2026-10-13), Imdelltra v8 (2026-09-11), Bavencio v25 (2026-09-22) re-downloaded from DailyMed today; version and date in the reference list are right. Every label number in the chapter was found in the label text.
- FDA: approval notifications page (content current 2026-11-10) and the three subcutaneous-formulation pages re-fetched.
- Claims: every abstract of the 140 papers read in full and compared with the chapter; PMC full text opened for Pardoll 2012, Rosenberg 2014, Sharma 2017, Marcus 2021, Porter 2011, Chiang & Mellman 2022, Liu 2026, Maude 2018, Lee 2019, Barnett 2025. A script then re-checked every number that sits next to a citation against the cited abstract, full text or label (no real miss left).
- Cross-chapter: lung, pancreatic, breast, sarcoma, irAE, emergencies (section 9), supportive care (section 13) and `sources/nhi/section9-1151022.md` grepped for the same trials, doses and rules.

## Writer's flagged items: outcome

- TMB-H cut-off: CONFIRMED. Keytruda label v229 (effective 2026-10-16), sections 1.18 and 14.18: TMB-H ≥13 mut/Mb "as determined by an FDA-authorized test"; "statistical analysis plan pre-specified ≥13 mutations per megabase using the FoundationOne CDx assay"; n = 220, ORR 36% (95% CI 30–43). The Keytruda Qlex label (v19, 2026-10-16) says the same. FDA notifications page: "On October 16, 2026 ... granted traditional approval ... TMB-H [≥13 mutations/megabase]" ("with updated indication"). Marcus 2021 full text confirms the 2020 approval was accelerated at ≥10 and that the SAP pre-specified both ≥10 and ≥13. The statement stays in the body; the existing 待核對 box now names the breast-chapter discrepancy.
- Cancer-immunity cycle: Chen & Mellman 2013, Chen & Mellman 2017, Mellman 2023 and Kim & Chen 2016 full texts are all blocked (HTTP 403 or paywall; not in PMC or Europe PMC). The seven step names and their order were confirmed verbatim in open-access PMC papers that quote them (PMC10618119, PMC11048616, PMC10757107, PMC11096532) and in an open-access review co-written by Mellman that restates the cycle in order and lists the therapy for each step (Chiang & Mellman 2022, PMID 35379739, PMC8981293). Step names kept; the therapy column was rebuilt from that review; one cell was wrong (see fixes).
- Ivonescimab: the FDA acceptance, the indication and the PDUFA goal date 2026-11-14 are confirmed in Summit Therapeutics' own press release of 2026-01-29 and again in its 2026-11-04 Q3 release (still pending, no change of date). First approval in China in May 2024 is in the same release. FDA page (current to 2026-11-10) has no ivonescimab entry. Citation switched from the trade-press article to the company release.
- History (section 1): Coley 1891/1893, McCarthy 2006, Burnet 1957 and Thomas (via Dunn 2002), Dunn/Schreiber 2002, Morales 1976 (9 patients), Rosenberg 1985 (11/25) and the 1984 first patient, IL-2 approvals 1992/1998, Krummel & Allison 1995, Leach 1996, Waterhouse 1995, Ishida/Honjo 1992 (Kyoto), Nishimura 1999, Dong/Chen 1999, Freeman/Honjo 2000, Hodi 2010, Topalian 2012 and Brahmer 2012 (same NEJM issue), Nobel 2018, Le 2015, 2017-05-23 MSI-H approval, tisagenlecleucel 2017-08-30, relatlimab March 2022, lifileucel 2024-02-16, tarlatamab 2024-05-16 and 2025-11-19: all match the sources.
- Doses: pembrolizumab 200 mg q3w / 400 mg q6w, nivolumab 240 mg q2w / 480 mg q4w, atezolizumab 840/1,200/1,680 mg, avelumab 800 mg q2w, tarlatamab 1 mg then 10 mg q2w, SC atezolizumab 1,875 mg q3w, SC pembrolizumab 395 mg q3w / 790 mg q6w, SC nivolumab (indication dependent): all match the US labels or FDA pages cited.
- CRS/ICANS, irAE, tarlatamab: agree with `00-shared/02-oncologic-emergencies.md` section 9, `00-shared/04-irae.md` and `01-lung-cancer.md` 7.7 (6–8 h monitoring, CRS 57%, 73% after first dose).
- Reused trial numbers (KEYNOTE-189, -024, -407, PACIFIC, ADRIATIC, IMpower133, CASPIAN, KEYNOTE-522, -355, CheckMate 816, KEYNOTE-671, DeLLphi-304, pancreatic MSI-H n = 22 / 18%, ASPS 37% and 24%, SARC028, A091401): match both the sources and the cancer chapters.
- Antibiotics, microbiome, baseline steroids, vaccines: section 4.4 already words these as association; the quick-card bullet did not and was fixed. Nothing goes beyond supportive care section 13 (which has no microbiome statement; vaccine wording agrees).

## Fixes (section: was -> now; source)

References
1. 11 Cercek 2022: last author "Diaz, L. A." -> "Diaz, L. A., Jr." (PubMed suffix).
2. 11 Marabelle 2020: last author "Diaz, L. A." -> "Diaz, L. A., Jr." (PubMed suffix).
3. 11 Waterhouse 2020: 19th author "Blumenschein, G." -> "Blumenschein, G., Jr." (PubMed suffix).
4. 11 Serani 2026 (Targeted Oncology news) removed -> Summit Therapeutics Inc. press release 2026-01-29 added (company source; page read via smmttx.com).
5. 11 added Chiang & Mellman 2022 (PMID 35379739; metadata from PubMed, article number e004711).
6. 11 added Baeuerle & Reinhardt 2009 (PMID 19509221; metadata from PubMed).

Claims
7. 0 必背數字: "prednisone ≥10 mg/day 的病人，療效較差" (reads as causal) -> "在觀察性研究中反應率與存活較差；這是相關，不是因果" (Arbour 2018 abstract: "associated with").
8. 1.1 row 2008: "雙特異性 T 細胞銜接抗體的第一份臨床證據" (unsupported "first") -> "在病人身上讓腫瘤縮小的早期證據" (Bargou 2008 abstract).
9. 1.1 row 2010: "first" claim now carries its source and context: the earlier tremelimumab phase 3 showed no survival benefit (Pardoll 2012 full text).
10. 1.1 row 2024: "細胞治療與 T 細胞銜接抗體進入實體腫瘤" -> "細胞治療（TIL、TCR-T）進入實體腫瘤；T 細胞銜接抗體進入小細胞肺癌" (a T-cell engager was already approved for a solid tumour in 2022: PMID 35880455 abstract; Liu 2026 only claims first DLL3 engager).
11. 1.3: "MHC 下調，ICI 沒有用" -> "T 細胞認不出腫瘤，再拆煞車效果也差，理論上要靠…" (evidence is the 4-patient series of Zaretsky 2016).
12. 2 intro: PD-1/PD-L1 "放開的是第 7 步" -> "主要放開的是第 7 步" (Pardoll 2012: PD-1 also acts at the priming stage).
13. 2.1 text: seven steps now cite a readable same-author source (Chiang & Mellman 2022) and the basis of the "location" column (Pardoll 2012: priming in lymph nodes, effector phase in tissues and tumour).
14. 2.1 table step 1: "沒有直接的藥" (wrong) -> "化療、放療等直接殺腫瘤的治療可以增加抗原釋出" (Chiang & Mellman 2022).
15. 2.1 table step 3: added "PD-1 抑制劑在這一步也有作用" (Chiang & Mellman 2022; Pardoll 2012).
16. 2.1 table step 4: name "T 細胞隨血流移動" -> "T 細胞移動到腫瘤" (trafficking of T cells to tumors); empty therapy cell filled: cell therapy and T-cell engagers (Chiang & Mellman 2022).
17. 2.1 table step 5: "合併治療" -> "抗血管新生藥等調整腫瘤微環境的合併治療" (Chiang & Mellman 2022).
18. 2.1 table step 6: uncited "不靠 MHC 的 CAR-T 與 T 細胞銜接抗體" -> sourced (Porter 2011 full text: "HLA-unrestricted"; Baeuerle & Reinhardt 2009 abstract: independent of TCR specificity and peptide antigen presentation).
19. 2.1 after table: self-sustaining cycle now cited (Chiang & Mellman 2022: "cyclic, self-propagating").
20. 3.5: ICANS "是隨之而來的神經毒性" (implies always after CRS) -> can occur with CRS, after CRS, or without CRS (Imdelltra label 5.2).
21. 3.5: new bullet giving the source for MHC-independence of T-cell engagers (Baeuerle & Reinhardt 2009); the TIP below it relied on this without a citation.
22. 3.5: warfarin monitoring advice was presented as if from the Imdelltra label; the label names no drug (the example is from the uncited Blincyto label). Now marked "本手冊的推論".
23. 3.6 table: CAR-T row "人工受體直接認細胞表面的抗原" + "不受 HLA 限制（Porter et al., 2011）".
24. 3.6 table: afami-cel approval date: Barnett 2025 says 2024-08-01, the FDA notifications page says 2024-08-02; both now shown.
25. 5.1 TMB-H bullet: added that ≥10 and ≥13 were both pre-specified (Marcus 2021), label version, 95% CI, and corrected the assay wording (indication says "FDA-authorized test"; FoundationOne CDx is the trial assay).
26. 5.1 TMB 待核對 box: now names breast chapter 2.6 as still saying ≥10 mut/Mb.
27. 5.2 IMpassion130: HR 0.84 is the analysis at 12.9 months' median follow-up (Schmid 2018); pointer added to the later figures in breast chapter 4.9 (which gives HR 0.87).
28. 5.3 CheckMate 153: added "這是探索性分析，證據強度有限" (Waterhouse 2020 abstract).
29. 7 intro: "或者直接繞過 MHC" -> "直接輸入 T 細胞，或者用 T 細胞銜接抗體繞過 MHC".
30. 7.2 HARMONi row: "與 HARMONi-A 相同的族群" -> "第三代 EGFR-TKI 治療後惡化的 EGFR 突變非鱗狀 NSCLC" (Le 2026 abstract).
31. 7.2 ivonescimab 待核對 box: source switched to company release; "已在中國核准" -> "2024 年 5 月首次在中國核准，在美國與歐洲仍是試驗用藥".
32. 7.2 ASCENT-04: "三陰性乳癌第一線" -> "PD-L1 陽性三陰性乳癌第一線" (Tolaney 2026 abstract; breast chapter 4.9).
33. 7.2 heading 四: "不靠腫瘤自己的抗原呈現" listed TIL and TCR-T, which both need MHC/HLA presentation (contradicts 3.6 of the same chapter). Heading -> "直接補上 T 細胞，或把 T 細胞拉到腫瘤旁"; text now says only the T-cell engager is independent of antigen presentation (Baeuerle & Reinhardt 2009), TIL needs MHC-presented peptide (Rosenberg 2014 full text), TCR-T needs HLA (Barnett 2025). "在 2024 年進入實體腫瘤" -> "都在 2024 年獲美國核准用於實體腫瘤".

Quiz
34. Q5 stem: "腹瀉每天 7 次" is Grade 2 if baseline is one stool a day (irAE 5.2: Grade 3 = increase of ≥7 over baseline), but the explanation called it Grade 3. Stem -> "每天比平常多解 7 次以上的稀便"; explanation -> "比基線每天增加 7 次以上屬 Grade 3". Key unchanged (B).
35. Q6 explanation: added that whether to resume after Grade 3 hepatitis is covered in irAE 5.3 (ASCO/ESMO are stricter than "hold"). Key unchanged (D).
All 15 questions were solved before reading the answers; the other 13 keys are the single best answer and the distractors are wrong.

Drug cards
36. nivolumab, pembrolizumab, atezolizumab, avelumab, tarlatamab: doses now say "美國仿單" (5 cards); atezolizumab "兩者不可互換" -> "毫克數不能直接互換" and SC interval q3w added.
37. aldesleukin: 監測與處置 cell held a response rate ("反應率約 16%…") -> "監測體液滯留與敗血症徵象；TIL 流程中最多給 6 劑"; 必記毒性 "2% 死於不良事件" -> "2% 死於敗血症相關的不良事件" (Atkins 1999; Sarnaik 2021).

待核對 boxes: none added; three existing boxes kept, two of them revised (TMB-H, ivonescimab).

Lint: `python3 tools/lint_chapter.py handbook/05-drugs/04-immunotherapy.md` -> 0 error, 0 warn. Reference list is now 151 entries (142 with PMID).

## Problems found in other files (not edited)

1. `handbook/03-breast-cancer.md` 2.6 (line 359): "TMB-H（≥10 mut/Mb）". The current US Keytruda label (v229, effective 2026-10-16) and the FDA notice of 2026-10-16 define TMB-H as ≥13 mut/Mb. The ≥10 figure is the 2020 accelerated-approval cut-off.
2. `handbook/03-breast-cancer.md` lines 45 and 749, and `handbook/02-pancreatic-cancer.md` line 249, cite the Keytruda US label "2026-07-10 版" (v228). DailyMed now serves v229 (effective 2026-10-16, published 2026-11-02). The numbers those chapters take from it are unchanged in v229 (KEYNOTE-522 pCR 63.0% vs 55.6%, OS HR 0.66; pancreatic MSI-H n = 22, ORR 18%), so only the version label is stale.
3. `handbook/00-shared/02-oncologic-emergencies.md` section 9 calls the class "雙特異性 T 細胞接合劑"; the lung chapter and this chapter use "雙特異性 T 細胞銜接抗體". Terminology is inconsistent across the handbook.
4. Not errors, but different datasets the reader may notice: IMpassion130 overall-survival HR 0.87 in breast 4.9 (later analysis) vs 0.84 here (Schmid 2018, now labelled); afami-cel CRS 71% in sarcoma 4.4.4 (D'Angelo 2024, n = 52) vs 75% here (FDA summary, n = 44).

## Could not check, and why

- Chen & Mellman 2013 (Immunity), Chen & Mellman 2017 (Nature), Mellman et al. 2023 (Immunity), Kim & Chen 2016 (Ann Oncol) full texts: publisher sites return 403 or a paywall; none is in PMC. The original Figure 1 (anatomical location of each step) was therefore not seen; the "發生的地方" column rests on the step names and Pardoll 2012.
- Text of errata attached in PubMed to cited papers could not be opened: Routy 2018 (Science erratum dated 2026-11-05, science.org 403), Le X 2026 (Lancet Oncol 2026-10), Xiong 2025 (Lancet 2025-11), Albiges 2025 and Felip 2025 (Ann Oncol 2026-09), Larkin 2015, Tawbi 2017 (two), Spigel 2022, Wang 2018, Hodi 2010, Lala 2020, Burotto 2023, Abdel-Wahab 2019, Sarnaik 2021, Schneider 2021, Seymour 2017, Skoulidis 2024, Xu 2023, Syed 2017, Grupp 2013, Porter 2011. No record carries a retraction or expression of concern. Chapter numbers were compared with the current PubMed abstracts.
- Most trial papers (NEJM, Lancet, JCO not in PMC) were checked against the PubMed abstract only; every number the chapter takes from them is in the abstract.
- O'Leary 2019 full text (AACR 403): "first CAR-T" in the 2017 timeline row is not in its abstract. It was confirmed in other PubMed abstracts (PMID 30518999, 30296188) but no citation was added.
- Coley 1991 (reprint), Burnet 1957 and Haanen 2022 have no PubMed abstract; the first two rest on the title plus McCarthy 2006 and Dunn 2002.
- Section 4.3 WARNING ("不能互相替代…不能接到靜脈管路") has no citation. It agrees with the Tecentriq Hybreza and Keytruda Qlex labels ("Do not substitute…"; both also allow switching at the next scheduled dose), which I opened but which are not in the reference list.
- FDA's own sources disagree by one day on the afami-cel approval date (see fix 24); the approval letter was not retrieved.
- Taiwan labels were not opened; the chapter states no Taiwan dose and refers to the cancer chapters.
- Ivonescimab: the FDA decision is due 2026-11-14, after this audit.
