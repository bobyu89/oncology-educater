# Sarcoma 4. Soft-tissue sarcoma / GIST / rare-subtype regimens, exact doses, toxicity management, AYA survivorship and TFDA licence status: fact-check report

Handbook: Taiwanese oncology NP handbook (專科護理師), sarcoma chapter (ward practice + 專師甄審 exam)
Verification date: 2026-10-29
Scope: doxorubicin, doxorubicin–ifosfamide (AI/AIM), high-dose ifosfamide, gemcitabine–docetaxel, trabectedin, eribulin, pazopanib, VDC/IE; GIST TKIs (imatinib, sunitinib, regorafenib, ripretinib, avapritinib); rare-subtype agents (tazemetostat, nirogacestat, pexidartinib, vimseltinib, afamitresgene autoleucel). Toxicity: ifosfamide encephalopathy, haemorrhagic cystitis and mesna, ifosfamide nephrotoxicity, anthracycline cardiotoxicity and dexrazoxane, extravasation, trabectedin liver/CK, pazopanib liver/BP, imatinib oedema/myelosuppression/DDI, regorafenib HFSR/liver, febrile neutropenia and G-CSF, AYA fertility, growth and psychosocial issues, limb-salvage rehabilitation and endoprosthesis infection. TFDA licence status for 14 named agents plus supportive drugs.

Cross-references: MAP, EURAMOS-1, mifamurtide trial data, HD-MTX/glucarpidase, cisplatin ototoxicity, regorafenib/cabozantinib in bone sarcoma (REGOBONE, SARC024, CABONE) and Ewing trials (INT-0091, EE2012, Euro-EWING 99, rEECur) are in `sarcoma_2_bone_trials_regimens.md`. Epidemiology, staging and GIST risk tables are in `sarcoma_1_taiwan_dx.md`. Generic anthracycline/dexrazoxane points also appear in `breast_4_regimens_tox_tfda.md`.

**Method.** Doses, hold rules and monitoring schedules come from current US prescribing information that I opened through the openFDA `drug/label` API (effective date and SPL set ID in section J). Trial regimens and results come from PubMed abstracts (NCBI E-utilities efetch, same database as the PubMed MCP tools), PMC full text where open, or ClinicalTrials.gov API v2. Two full-text points (AEWS0031 per-day doses; AEWS1031 dexrazoxane timing) were read through a WebFetch summary of the PMC page because the publisher blocks XML download; they are tagged [FT-WF]. Taiwan licence status comes from my own download of the TFDA licence dataset (InfoId 36, `36_2.csv`, file timestamp **2026-10-27**, downloaded 2026-10-29). NCCN versions from nccn.org category pages (read 2026-10-29; content behind login, not read). www.nhi.gov.tw and www.hpa.gov.tw were not reachable, so **NHI reimbursement status is not covered** here. Nothing was filled from memory; anything I could not confirm is **[UNVERIFIED]**.

**Source tags used inline**
- [A] = PubMed abstract of the cited paper
- [FT] = PMC full text (methods/results unless stated)
- [FT-WF] = PMC full-text page read via WebFetch summary (publisher blocks XML); treat as [PARTIAL] for exact wording
- [L-xxx] = US prescribing information via openFDA, e.g. [L-Yondelis] (dates in section J)
- [TFDA] = TFDA licence dataset InfoId 36 (file dated 2026-10-27)
- [CT] = ClinicalTrials.gov API v2 record (read 2026-10-29)
- [NCCN] = nccn.org category page (version number only)
- [calc] = my arithmetic from verified inputs (shown)

**Status tags**
- **[VERIFIED]** = confirmed in a primary or official source I opened
- **[PARTIAL]** = only part confirmed, or confirmed only in a secondary source
- **[UNVERIFIED]** = not confirmed; do not print without checking

**APA 7 notes.** All authors up to 20; 21 or more: first 19, ". . .", final author. Study-group bylines omitted unless the group is the lead author (MetaGIST, PARITY). Titles in sentence case from the PubMed record. Year = journal-issue year. Errata listed when PubMed links one (content not read unless stated). Full list in section J.

---

## 0. Corrections and flags for the editor (read first)

1. **Taiwan licence surprises (TFDA file 2026-10-27).**
   - **Pexidartinib (TURALIO 圖拉留膠囊200毫克, 衛部藥輸字第028293號, 台灣第一三共) was CANCELLED on 2026-02-03, reason 自請註銷** (issued 2022-05-27) [VERIFIED; TFDA]. Do not list it as available in Taiwan.
   - **Not in the dataset at all (never licensed):** tazemetostat, nirogacestat, vimseltinib, afamitresgene autoleucel (Tecelra), glucarpidase (Voraxaze), dexrazoxane (any brand, including Savene/Cardioxane/Zinecard) [VERIFIED; TFDA]. The dataset does list CAR-T products (Kymriah 衛部菌疫輸字第001176號; Yescarta 衛部菌疫輸字第001312號), so absence of afami-cel is meaningful.
   - **Mifamurtide (MEPACT 秘配得) cancelled 2023-10-17 (自請註銷)** [VERIFIED; TFDA] (same finding as sarcoma_2).
   - **Avapritinib Taiwan indication is narrower than the US label**: TFDA = PDGFRA **D842V** GIST only; US = PDGFRA **exon 18** mutations including D842V [VERIFIED; TFDA; L-Ayvakit 2026-08-05].
   - **Eribulin in Taiwan is licensed for liposarcoma only (not leiomyosarcoma)**, matching the US label [VERIFIED; TFDA; L-Halaven].
   - **Regorafenib and cabozantinib have no sarcoma/bone indication in Taiwan or the US** (regorafenib: CRC, GIST after imatinib + sunitinib, HCC; cabozantinib: RCC, HCC, DTC, NET) [VERIFIED; TFDA; L-Stivarga; L-Cabometyx].
   - **Votrient 400 mg tablet cancelled 2021-06-08**; only 200-mg tablets remain (Votrient 衛署藥輸字第025433號 and two generics), so **800 mg = four 200-mg tablets** [VERIFIED; TFDA; calc]. **Glivec 400 mg (衛署藥輸字第024026號) cancelled 2021-05-10**; Glivec is now 100-mg only, but generic imatinib 400-mg tablets are licensed (e.g., Alvotinib 400 mg 衛部藥輸字第026614號; Redistra 400 mg 衛部藥輸字第027973號) [VERIFIED; TFDA].
   - **Methylene blue in Taiwan** (安星 甲烯藍注射液 10 mg/mL, **rare-disease licence 衛部罕藥製字第000013號**) is licensed only for **methemoglobinemia**; use for ifosfamide encephalopathy is off-label [VERIFIED; TFDA].
   - **Dacarbazine** (the comparator in the trabectedin and eribulin phase 3 trials) is licensed in Taiwan only for melanoma (惡性黑色素腫瘤症狀之改善) [VERIFIED; TFDA].
2. **Pexidartinib trial dose ≠ label dose.** ENLIVEN gave a 1000 mg/day loading dose for 2 weeks, then **800 mg/day** [A]. The current US label is **250 mg twice daily (500 mg/day) with a low-fat meal**, under a REMS for hepatotoxicity [L-Turalio 2025-01-16]. Never print the trial dose as the dose to give.
3. **Vincristine dose in AEWS0031 (VDC) is internally inconsistent in the paper.** Abstract and Appendix Table A1: **2 mg/m² (max 2 mg)**; Figure 1 legend: **1.5 mg/m² (max 2 mg)** [A; FT-WF]. The abstract also prints filgrastim as "5 mg/kg per day; maximum, 300 mg" — the unit must be **µg/kg** (pegfilgrastim/filgrastim pediatric sarcoma trial: filgrastim **5 µg/kg/day**, pegfilgrastim **100 µg/kg** once per cycle [Spunt 2010, A]). An erratum to Womer 2012 exists (PMID 25721580; content not read).
4. **Two "versions" of the pivotal STS results circulate — quote the source you cite.**
   - Trabectedin SAR-3007: paper (interim OS, 64% censored) **OS 12.4 vs 12.9 months, HR 0.87, P = .37** [A]; US label (final OS) **13.7 vs 13.1 months, HR 0.93 (0.75–1.15)**. PFS identical in both: **4.2 vs 1.5 months, HR 0.55** [A; L-Yondelis]. Trabectedin improves PFS, **not OS**.
   - PALETTE (pazopanib): paper **PFS HR 0.31 (0.24–0.40), OS 12.5 vs 10.7 months, HR 0.86** [A]; label (independent review) **PFS 4.6 vs 1.6 months, HR 0.35 (0.26–0.48); OS 12.6 vs 10.7, HR 0.87 (0.67–1.12)** [L-Votrient]. Pazopanib improves PFS, **not OS**.
   - GRID (regorafenib): crossover after progression 85% (56 patients) in the paper [A] vs 88% (58) in the label [L-Stivarga] (different data cuts).
5. **Doxorubicin + ifosfamide (EORTC 62012) did not improve OS** (12.8 vs 14.3 months, HR 0.83, 95.5% CI 0.67–1.03, P = .076) but doubled response (26% vs 14%) and PFS (7.4 vs 4.6 months) — and **febrile neutropenia was 46% vs 13% even though the combination arm received pegfilgrastim** [A; CT]. Teaching point: AI/AIM is for when **tumour shrinkage** is the goal, and it requires **primary G-CSF prophylaxis**.
6. **Gemcitabine–docetaxel is not superior to doxorubicin first line** (GeDDiS: alive and progression-free at 24 weeks 46.3% vs 46.4%) [A]. Doses differ by source: **Hensley 2002 gem 900 mg/m² D1,8 + doc 100 mg/m² D8 + G-CSF D9–15 (25% lower if prior pelvic RT)** [A]; **GeDDiS gem 675 mg/m² D1,8 + doc 75 mg/m² D8** [A; FT]; **ISG-STS 1001 UPS arm gem 900 mg/m² D1,8 (90 min) + doc 75 mg/m² D8 (1 h)** [A]. The GeDDiS authors quote Maki 2007 that the 900/100 schedule was "too high for long-term use" (46% dose reductions) [FT]. Maki 2007's own doses: **[PARTIAL]** (abstract does not state them; GeDDiS full text says Maki "had used the higher dose schedule").
7. **Eribulin benefit is confined to liposarcoma.** Whole study: OS 13.5 vs 11.5 months, HR 0.77 [A]. Liposarcoma stratum: **OS 15.6 vs 8.4 months, HR 0.51 (0.35–0.75)**; label states "no evidence of efficacy" in leiomyosarcoma [L-Halaven].
8. **Methylene blue (MB) for ifosfamide encephalopathy carries a boxed serotonin-syndrome warning** with SSRIs, SNRIs, MAOIs **and opioids** [L-ProvayBlue 2025-05-28]; a case of serotonin syndrome during MB for ifosfamide encephalopathy is published [McDonnell 2012, A]. Sarcoma inpatients are often on opioids — check the medication list before MB.
9. **Evidence for MB/thiamine prophylaxis is weak and partly negative.** Retrospective sarcoma cohort: **more** encephalopathy with MB/thiamine/albumin prophylaxis (21.1% vs 8.4% of cycles, p = 0.026) [Richards 2011, A]; thiamine prophylaxis in lymphoma ICE: 10.3% vs 18.2%, p = 0.51 [Lentz 2020, A]; MB did not prevent recurrence after high-dose ifosfamide (5/5 recurred) [Sweiss 2008, A].
10. **Taiwan data on ifosfamide encephalopathy exist:** NTUH-affiliated cohort, **11% (38/337)**; independent risk factors ECOG PS 2–4, higher serum creatinine, lower albumin; **dose and brain metastasis not significant** [Lo 2016, A].
11. **Mesna for continuous-infusion or high-dose ifosfamide: no label schedule.** The label gives only bolus schedules for ifosfamide 1.2 g/m²/day and says the IV+oral regimen is not established above 2 g/m²/day [L-Mesnex]. ASCO 1999 found insufficient evidence for ifosfamide > 2.5 g/m²/day [A]. The ASCO continuous-infusion mesna schedule is **[UNVERIFIED]** (full texts paywalled).
12. **Imatinib label lists dexamethasone as a strong CYP3A4 inducer** (with phenytoin, carbamazepine, rifampin, phenobarbital); if a strong inducer cannot be avoided, imatinib dose should be **increased by at least 50%** [L-Gleevec 2026-07-13]. Also: **use LMWH or heparin, not warfarin** [L-Gleevec].
13. **Regorafenib HFSR is worse in Asian patients:** all grades **72%**, grade 3 **18%** (vs 53% / 16% overall) [L-Stivarga] — relevant for Taiwan.
14. **Nirogacestat causes ovarian toxicity in 75% (27/36) of women of childbearing potential** (resolved in 74%) [Gounder 2023, A; L-Ogsiveo]. Fertility counselling needed for AYA women with desmoid tumours.
15. **PARITY RCT:** 5 days vs 1 day of post-operative IV cefazolin/cefuroxime after endoprosthetic reconstruction gave **no difference in surgical site infection (15.0% vs 16.7%, HR 0.93)** and **more antibiotic complications (5.1% vs 1.6%)** [A]. This supersedes the older pooled retrospective suggestion that long courses lower infection (13% vs 8%) [Racano 2013, A].
16. **Tecelra (afami-cel) label changed in June 2026:** accelerated-approval statement removed and dose/indication sections updated; current indication includes **patients ≥ 12 years** [L-Tecelra 2026-07-15]. What the earlier label said is **[UNVERIFIED]** here.
17. **Dexrazoxane US label remains restricted** to women with metastatic breast cancer after ≥ 300 mg/m² doxorubicin ("Do not use with doxorubicin initiation") [L-dexrazoxane Eugia 2026-08-10], although COG data support use in children (POG 9404) [Asselin 2016, A] and COG AEWS1031 gave dexrazoxane during the last two doxorubicin cycles [FT-WF]. **Not licensed in Taiwan** [TFDA].

---

# A. SOFT-TISSUE SARCOMA CYTOTOXIC REGIMENS

## 1. Regimen table (doses exactly as verified)

| Regimen | Dose and schedule | Source | Status |
|---|---|---|---|
| **Doxorubicin single agent** | **75 mg/m² IV day 1 q3w** (bolus, or 72-h continuous infusion in EORTC 62012); up to 6 cycles | Label: single agent **60–75 mg/m² q21d**; in combination 40–75 mg/m² q21–28d [L-doxorubicin Pfizer 2026-04-30]; EORTC 62012 and GeDDiS control arms [A] | [VERIFIED] |
| **AI (EORTC 62012 "intensified")** | Doxorubicin **75 mg/m² (25 mg/m²/day D1–3)** + ifosfamide **10 g/m² over 4 days** (= 2.5 g/m²/day [calc]; CT.gov: ifosfamide over 4 h D1–4) + mesna + **pegfilgrastim D5**; q3w up to 6 cycles; age 18–60 | [A; CT NCT00061984] | [VERIFIED] (mesna dose [UNVERIFIED]) |
| **EI (ISG-STS 1001 standard neoadjuvant)** | Epirubicin **60 mg/m²/day D1–2** + ifosfamide **3 g/m²/day D1–3**, q21d × 3 | [A] | [VERIFIED] |
| "AIM" (generic name) | Doxorubicin + ifosfamide + mesna; exact per-protocol AIM doses beyond the two trials above **not verified** | — | [UNVERIFIED] |
| **High-dose ifosfamide (HDI), 14-day infusion** | **14 g/m² over 14 days by external pump, q28d** (ISG-STS synovial arm) [A]; Meazza 2010: **14 g/m² + mesna 14 g/m²** over 14 days q3w, no G-CSF [A]; Royal Marsden: **1 g/m²/day × 14 days** [Martin-Liberal 2013, A] | [A] | [VERIFIED] |
| HDI, short schedules | Lee 2011: "2 g/m² over 3 h … 2 g/m² per day … on 6 consecutive days", total **14 g/m²** q3w (abstract wording ambiguous) [A]; Modi 2021 defined high dose as **≥ 1,800 mg/m²** per administration [A] | [A] | [PARTIAL] |
| **Gemcitabine + docetaxel** | Gem **900 mg/m² D1,8** (90-min infusion from cycle 3) + doc **100 mg/m² D8** + **G-CSF D9–15**, q21d; **25% lower doses after pelvic RT** [Hensley 2002, A] / Gem **675 mg/m² D1,8 (90 min)** + doc **75 mg/m² D8 (60 min)**, q3w × 6 [GeDDiS, A; FT] / Gem **900 + doc 75** [ISG-STS 1001 UPS arm, A; TAUL trial, CT NCT02249702] | as cited | [VERIFIED] |
| **Trabectedin** | **1.5 mg/m² IV over 24 h q21d through a central venous line**; **dexamethasone 20 mg IV 30 min before each dose**; moderate hepatic impairment 0.9 mg/m² | [L-Yondelis 2026-01-06] | [VERIFIED] |
| **Eribulin** | **1.4 mg/m² IV over 2–5 min D1 and D8 q21d**; Child-Pugh A 1.1, Child-Pugh B 0.7; CLcr 15–49 mL/min 1.1 mg/m² | [L-Halaven Eisai 2025-11-07] | [VERIFIED] |
| **Pazopanib** | **800 mg PO once daily without food** (≥ 1 h before or 2 h after a meal); STS reductions **600 → 400 mg**; moderate hepatic impairment 200 mg | [L-Votrient 2025-12-16] | [VERIFIED] |
| **VDC/IE (Ewing, AEWS0031)** | VDC: vincristine **1.5 or 2 mg/m² (max 2 mg)** (see flag 3), doxorubicin **37.5 mg/m²/day D1–2** (48-h CI per CT.gov), cyclophosphamide **1,200 mg/m² D1**; IE: ifosfamide **1,800 mg/m²/day D1–5** + mesna, etoposide **100 mg/m²/day D1–5**; cumulative doxorubicin **375 mg/m²** (VC replaces VDC thereafter); 14 cycles q2w (intensified) or q3w; filgrastim between cycles | [A; FT-WF; CT NCT00006734] | [VERIFIED] except vincristine dose [PARTIAL] |

## 2. Trial evidence behind the regimens

### 2a. EORTC 62012 (doxorubicin vs doxorubicin + ifosfamide) — [VERIFIED]
- Phase 3, 38 hospitals, 10 countries; high-grade advanced STS; age 18–60; WHO PS 0–1; n = 228 vs 227 [A].
- **OS 12.8 vs 14.3 months, HR 0.83 (95.5% CI 0.67–1.03), P = .076 (not significant)** [A].
- **PFS 4.6 vs 7.4 months, HR 0.74 (0.60–0.90), P = .003; ORR 14% vs 26%** [A].
- Grade 3–4 (AI vs doxorubicin): leucopenia 43% vs 18%; neutropenia 42% vs 37%; **febrile neutropenia 46% vs 13%**; anaemia 35% vs 5%; thrombocytopenia 33% vs < 1% [A].
- Interpretation (authors): do not use AI for palliation "unless the specific goal is tumour shrinkage" [A].

### 2b. GeDDiS (gemcitabine–docetaxel vs doxorubicin, first line) — [VERIFIED]
- n = 257 (129 vs 128), UK + one Swiss site; doses as in table [A].
- Alive and progression free at 24 weeks **46.3% vs 46.4%**; PFS HR 1.28 (0.99–1.65), p = 0.06 [A].
- Grade 3–4 (doxorubicin vs gem-doc): neutropenia 25% vs 20%; **febrile neutropenia 20% vs 12%**; fatigue 6% vs 14%; mucositis 14% vs 2% [A].
- G-CSF permitted **only after an episode of febrile neutropenia** (no primary prophylaxis) [FT].
- Doxorubicin stopped if LVEF < 45% or fall ≥ 20% from baseline (protocol rule) [FT].
- Conclusion: **doxorubicin remains standard first line** [A].

### 2c. SARC 002 (Maki 2007) and Hensley 2002 — [VERIFIED results; PARTIAL Maki doses]
- Maki 2007: Bayesian adaptive randomisation, 122 patients (73 gem-doc, 49 gem). ORR 16% vs 8%; **median PFS 6.2 vs 3.0 months; median OS 17.9 vs 11.5 months**; posterior probability of superiority 0.98 (PFS) and 0.97 (OS); more toxicity discontinuations with gem-doc [A]. Erratum: J Clin Oncol 2007;25(24):3790 (content not read).
- Hensley 2002: unresectable LMS (29 uterine), n = 34; **ORR 53% (95% CI 35–70%)**; 50% response after prior doxorubicin; grade 3/4 neutropenia 15%/6%, thrombocytopenia 26%/3%; **neutropenic fever 6%**; median TTP 5.6 months [A].

### 2d. ISG-STS 1001 (neoadjuvant histotype-tailored vs standard EI) — [VERIFIED]
- n = 287, high-risk extremity/trunk STS (UPS, high-grade myxoid LPS, synovial, MPNST, LMS) [A].
- Histotype-tailored arms included **trabectedin 1.3 mg/m² 24-h CI q21d** (myxoid LPS), **gemcitabine 1800 mg/m² (180 min) + dacarbazine 500 mg/m² q14d** (LMS), **HDI 14 g/m² over 14 days q28d** (synovial), **etoposide 150 mg/m²/day + ifosfamide 3 g/m²/day D1–3** (MPNST), **gem 900 + doc 75** (UPS) [A].
- **Projected 46-month DFS 62% (standard EI) vs 38% (tailored), HR 2.00 (1.22–3.26)**; closed for futility. Grade ≥ 3 neutropenia **86%** with EI vs 26% [A]. Erratum: Lancet Oncol 2017;18(6):e301 (content not read).
- Teaching point: full-dose anthracycline + ifosfamide is the neoadjuvant benchmark; it is intensely myelotoxic.

### 2e. Trabectedin (SAR-3007; Demetri 2016) — [VERIFIED]
- 2:1, n = 518 (345 vs 173), liposarcoma or leiomyosarcoma after anthracycline + ≥ 1 more regimen; dacarbazine 1000 mg/m² q3w comparator [A; L-Yondelis].
- PFS **4.2 vs 1.5 months, HR 0.55, P < .001**; OS: see flag 4 [A; L-Yondelis].
- Label: 73% LMS, 27% LPS; 89% had ≥ 2 prior regimens; ORR 7% vs 6% [L-Yondelis].

### 2f. Eribulin (Study 309; Schöffski 2016) — [VERIFIED]
- n = 452 (228 vs 224); LPS or LMS after ≥ 2 regimens incl. anthracycline; dacarbazine 850/1000/1200 mg/m² q21d [A].
- **OS 13.5 vs 11.5 months, HR 0.77 (0.62–0.95), p = 0.0169**; grade ≥ 3 AEs 67% vs 56% [A].
- Liposarcoma stratum (label Table 6): OS 15.6 vs 8.4 months, HR 0.51; PFS 2.9 vs 1.7 months, HR 0.52; LMS: no evidence of efficacy [L-Halaven].

### 2g. Pazopanib (PALETTE; van der Graaf 2012) — [VERIFIED]
- Non-adipocytic metastatic STS after chemotherapy; 2:1, n = 369 (246 vs 123); no crossover [A].
- PFS 4.6 vs 1.6 months; OS not significantly different (see flag 4) [A; L-Votrient].
- Pazopanib vs placebo AEs: fatigue 65% vs 49%; diarrhoea 58% vs 16%; nausea 54% vs 28%; weight loss 48% vs 20%; **hypertension 41% vs 7%** [A].
- Label limitation of use: efficacy **not shown in adipocytic STS or GIST** (same wording in TFDA indication) [L-Votrient; TFDA].

### 2h. VDC/IE interval compression (AEWS0031) and Asian feasibility — [VERIFIED]
- AEWS0031: n = 568 eligible; median cycle interval 15 vs 21 days; **5-year EFS 73% vs 65% (P = .048)**; toxicity similar [A]. 10-year EFS 70% vs 61% (P = .03), OS 76% vs 69% (P = .04) [Cash 2023, A]. (Full trial details in sarcoma_2.)
- AEWS1031 (VDC/IE ± VTC): "Dexrazoxane was administered only during the last two doxorubicin-containing cycles"; "All patients received myeloid growth factor support"; GM-CSF not permitted [FT-WF]. Per-day doses are in a Table 1 image: **[UNVERIFIED]**.
- **Taiwan/Asian experience** (Huang 2023, Taipei-based authors): 12 patients, 129 cycles of interval-compressed VDC (vincristine 2 mg/m², doxorubicin 75 mg/m², cyclophosphamide 1200–2200 mg/m²) / IE (ifosfamide 9000 mg/m², etoposide 500 mg/m²), filgrastim 5–10 µg/kg/day; **median achieved interval 19 days (IQR 15–24)**; ANC nadir day 11, recovery day 15; platelet nadir day 11, recovery day 17; **fever in 36% and bacteraemia in 8% of cycles**; 7/9 measurable tumours responded [A]. Teaching point: q2w is often not achievable in Asian practice; plan for fever.

---

# B. GIST TYROSINE KINASE INHIBITORS

## 3. Dose table

| Drug (line) | Dose | Key label rules | Source |
|---|---|---|---|
| **Imatinib** (1st line, adjuvant) | **400 mg/day with a meal and a large glass of water**; may increase to **800 mg/day (400 mg BID)** for progression; adjuvant **400 mg/day, 3 years** recommended for the Study 2 population | Severe hepatic impairment 300 mg/day | [L-Gleevec 2026-07-13] [VERIFIED] |
| **Sunitinib** (2nd line) | **50 mg once daily, 4 weeks on / 2 weeks off (Schedule 4/2)**, with or without food; GIST reductions **37.5 → 25 mg** | Boxed hepatotoxicity; LFT at baseline and each cycle | [L-Sutent 2026-02-20] [VERIFIED] |
| **Regorafenib** (3rd line) | **160 mg (4 × 40 mg) once daily D1–21 of 28**, after a **low-fat meal** (< 600 kcal, < 30% fat); reduce in 40-mg steps to **120 → 80 mg** (lowest) | Boxed hepatotoxicity | [L-Stivarga 2026-02-09]; TFDA 用法用量 identical [TFDA] [VERIFIED] |
| **Ripretinib** (4th line) | **150 mg once daily** with or without food; reduce to **100 mg** | Re-escalate PPES after ≥ 28 days at grade ≤ 1 | [L-Qinlock 2025-05-12] [VERIFIED] |
| **Avapritinib** (PDGFRA exon 18/D842V) | **300 mg once daily on an empty stomach** (≥ 1 h before / 2 h after meal); reductions 200 → 100 mg | Intracranial haemorrhage: stop permanently | [L-Ayvakit 2026-08-05] [VERIFIED] |

## 4. GIST trial data — [VERIFIED unless marked]
- **B2222 (imatinib 400 vs 600 mg):** n = 147; PR 53.7%, SD 27.9%; early resistance 13.6%; GI/intra-abdominal haemorrhage ~5%; no difference between doses [Demetri 2002, A].
- **MetaGIST (400 mg daily vs 400 mg BID, n = 1,640):** small PFS advantage for high dose, **essentially confined to KIT exon 9**; **no OS difference** [A].
- **Adjuvant:** ACOSOG Z9001 (1 year vs placebo, tumours ≥ 3 cm): 1-year RFS 98% vs 83%, HR 0.35 [DeMatteo 2009, A]. SSG XVIII (36 vs 12 months, high risk): **5-year RFS 65.6% vs 47.9% (HR 0.46); 5-year OS 92.0% vs 81.7% (HR 0.45)**; discontinuation for reasons other than recurrence 25.8% vs 12.6% [Joensuu 2012, A].
- **Sunitinib after imatinib failure:** TTP **27.3 vs 6.4 weeks, HR 0.33** [Demetri 2006, A].
- **GRID (regorafenib):** PFS **4.8 vs 0.9 months, HR 0.27**; grade ≥ 3 regorafenib-related: **hypertension 23%, HFSR 20%, diarrhoea 5%** [A]. Label: no significant OS difference at final analysis [L-Stivarga].
- **INVICTUS (ripretinib, ≥ 4th line):** PFS **6.3 vs 1.0 months, HR 0.15** [A]; label OS 15.1 vs 6.6 months, HR 0.36 (0.21–0.62) [L-Qinlock]. Whether OS was formally tested: **[UNVERIFIED]** (Lin 2022 calls the OS benefit "insignificant" [A]). Erratum: Lancet Oncol 2020;21(7):e341 (content not read).
- **NAVIGATOR (avapritinib, PDGFRA D842V):** ORR **88% (49/56)**, CR 9%; MTD 400 mg, **RP2D 300 mg** [A]. Label (exon 18, n = 43): ORR 84%; D842V subgroup 89% [L-Ayvakit]. Erratum: Lancet Oncol 2020;21(9):e418 (content not read).
- **Taiwan real-world data:**
  - TCOG nationwide registry (2010–2020, n = 224): imatinib **48-month PFS 50.5%, OS 79.5%**; sunitinib median PFS **12.76 months**; regorafenib median PFS **7.14 months**; KIT exon 9 and PDGFRA mutations = poor PFS on imatinib [Tsai 2024, A].
  - Chang Gung regorafenib cohort (n = 28): median PFS 4.4, OS 29.3 months [Hu 2020, A].
  - Ripretinib compassionate use, Taiwan + Hong Kong (n = 20): ORR 25%, median PFS 6.1 months; **alopecia 55%**; albumin < 3.5 predicted worse PFS [Lin 2022, A]. Erratum exists (PMID 36313668, content not read).

---

# C. RARE-SUBTYPE AGENTS (mostly not licensed in Taiwan)

| Agent / disease | Dose (US label) | Key efficacy | Key safety | Taiwan |
|---|---|---|---|---|
| **Tazemetostat** (EZH2) / epithelioid sarcoma, age ≥ 16, not eligible for complete resection | **800 mg PO BID**; reductions 600 → 400 mg BID | Phase 2 cohort 5 (n = 62, sites included Taiwan): **ORR 15%**, DCR at 32 weeks 26%, median PFS 5.5, OS 19.0 months [Gounder 2020, A] | **Secondary malignancies** (MDS/AML/B-ALL 1.7%; one T-LBL) — long-term monitoring; non-hormonal contraception [L-Tazverik 2026-04-29] | Not licensed [TFDA] |
| **Nirogacestat** (γ-secretase) / progressing desmoid tumour | **150 mg PO BID**; restart at 100 mg BID after holds | DeFi (n = 142): **PFS HR 0.29 (0.15–0.55)**; 2-year event-free 76% vs 44%; ORR 41% vs 8% [Gounder 2023, A] | Diarrhoea 84% (G3 16%); **ovarian toxicity 75% of women of reproductive potential**; ALT/AST rise; hypophosphataemia; hypokalaemia; non-melanoma skin cancer [A; L-Ogsiveo 2026-09-01] | Not licensed [TFDA] |
| **Pexidartinib** (CSF1R) / symptomatic TGCT | **250 mg PO BID with a low-fat meal (11–14 g fat)**; REMS | ENLIVEN: ORR **39% vs 0%** at week 25 [Tap 2019, A] | **Boxed hepatotoxicity incl. vanishing bile duct syndrome**; 5.3% liver injury events of concern among the first 609 REMS patients; LFT **weekly × 8 weeks, every 2 weeks for 1 month, then every 3 months** [L-Turalio] | **Licence cancelled 2026-02-03** [TFDA] |
| **Vimseltinib** (CSF1R) / symptomatic TGCT | **30 mg PO twice weekly, ≥ 72 h apart**; reductions 20 → 14 mg | MOTION (n = 123): **ORR 40% vs 0%** [Gelderblom 2024, A] | Grade 3–4 CPK rise 10%; no cholestatic DILI in MOTION [A]; serum creatinine rises without true renal change [L-Romvimza 2026-06-26]. FDA approval 2025-02-14 [openFDA drugsfda] | Not licensed [TFDA] |
| **Afamitresgene autoleucel** (MAGE-A4 TCR-T) / synovial sarcoma after chemo; HLA-A*02:01P, 02:02P, 02:03P or 02:06P and MAGE-A4+ | Lymphodepletion **fludarabine 30 mg/m²/day D−7 to D−4 + cyclophosphamide 600 mg/m²/day D−7 to D−5**; single dose **1.62–10 × 10⁹ TCR+ T cells**; premedicate acetaminophen + H1 antihistamine; **no prophylactic steroids; no leukodepleting filter** [L-Tecelra 2026-07-15] | SPEARHEAD-1 cohort 1: ORR **37%** overall, **39% synovial**, 25% MRCLS [D'Angelo 2024, A] | **Boxed CRS**: 72% (grade ≥ 3 2%), median onset day 2; ICANS — monitor ≥ 2 weeks, no driving ≥ 2 weeks; prolonged cytopenias (grade ≥ 3 lymphopenia 96%, neutropenia 85% in trial) [L-Tecelra; A] | Not licensed [TFDA] |

US approval dates (openFDA drugsfda, original NDA action date): trabectedin 2015-10-23; tazemetostat 2020-01-23; ripretinib 2020-05-15; pexidartinib 2019-08-02; nirogacestat 2023-11-27; vimseltinib 2025-02-14; eribulin liposarcoma efficacy supplement 2016-01-28 [VERIFIED; openFDA drugsfda].

---

# D. TOXICITY MANAGEMENT

## 5. Ifosfamide-induced encephalopathy (IIE)

### 5a. Incidence — [VERIFIED]
- Label (pooled fractionated monotherapy, 4–12 g/m² per course): **CNS toxicity 15.4% (154/1001)**; encephalopathy with coma and death reported [L-ifosfamide Fresenius 2026-04-09].
- Taiwan (adults, 2008–2010): **11% (38/337)** [Lo 2016, A].
- US academic centre: **14.5% (29/200)**; more common in sarcoma than lymphoma (24 vs 5 patients) [Szabatura 2015, A].
- Meanwell 1986: severe encephalopathy **9% (7/77)**; EEG changes in 56% of those tested [A].
- High-dose ifosfamide: literature range **10–40%**; 8/19 (42%) in one STS cohort [Sweiss 2008, A].
- Narrative review: "up to 30%"; reported incidence 10–15%; onset usually within 48 h, up to 6 days [Torchia 2025, A; FT].

### 5b. Clinical picture and course — [VERIFIED; L-ifosfamide]
- Somnolence, confusion, hallucinations, blurred vision, psychotic behaviour, extrapyramidal signs, urinary incontinence, seizures, coma.
- Onset within hours to a few days of the first dose; most cases **resolve within 48–72 h of stopping ifosfamide**; can recur after several uneventful cycles; occasionally incomplete recovery or death.
- **Discontinue ifosfamide if encephalopathy develops.** Use CNS-acting drugs (antiemetics, sedatives, opioids, antihistamines) with particular caution.
- Re-challenge after IIE: **26.3%** recurrence (fosaprepitant cohort) [Modi 2021, A].

### 5c. Risk factors — [VERIFIED]
- **Low serum albumin, high serum creatinine, pelvic disease** (nomogram) [Meanwell 1986, A].
- **ECOG PS 2–4, higher SCr, lower albumin**; ifosfamide dose and brain metastases not significant (Taiwan) [Lo 2016, A].
- **Prior cisplatin (OR 12.47), concomitant opioids (OR 2.81), CYP2B6 inhibitors (OR 5.17)**, higher creatinine, higher haemoglobin, lower albumin; sarcoma > lymphoma [Szabatura 2015, A].
- Female sex, obesity (actual/ideal weight 1.4 vs 1.1), low albumin, haemoglobin and bilirubin (high-dose, n = 19) [Sweiss 2008, A].
- Albumin < 3.5 g/dL (p < 0.001); co-administration of **fosaprepitant appeared safe** (9.3% of cycles) [Modi 2021, A].
- **CYP3A4 inducers** (carbamazepine, phenytoin, phenobarbital, rifampin, St John's wort) may increase the neurotoxic/nephrotoxic metabolite **chloroacetaldehyde** [L-ifosfamide].
- Candidate pharmacogenetic factors (CYP2B6, GSTM1, GSTP1, GSTT1) — hypothesis-level [Torchia 2025, A].

### 5d. Treatment and prevention — [VERIFIED as reported; evidence = case series/retrospective]
- **First step: stop the infusion and hydrate** [Torchia 2025, A; L-ifosfamide].
- **Methylene blue: 50 mg IV up to 6 times a day** (treatment); prophylaxis "50 mg up to every 6 h IV from the day before the start of IFO infusion" [Torchia 2025, FT]. Evidence: case reports and one chart review, no controlled trials; resolution sometimes within 10 minutes but often modest, and untreated cases resolved in a similar time frame [Patel 2006, A].
- **Thiamine: 100 mg IV every 4 h until symptoms resolve** (treatment); **100 mg every 6 h** for prophylaxis [Torchia 2025, FT]; based on Buesa 2003 (10 patients) and case reports [FT]. Thiamine injection is licensed in Taiwan (e.g., 內衛藥製字第010004號 Vitamin B1 Injection 50 mg/mL "T.F."; 15 active single-ingredient injection licences) [TFDA].
- **Haemodialysis** for severe IIE unresponsive to MB/thiamine, especially with nephrotoxicity [Torchia 2025, FT].
- **Prophylaxis evidence is conflicting** (flag 9).
- **Safety of MB:** boxed serotonin syndrome warning with SSRIs, SNRIs, MAOIs and opioids [L-ProvayBlue]; MB is a reversible MAO-A inhibitor; first reported serotonin syndrome during MB for IIE [McDonnell 2012, A]. MB label dose for methemoglobinemia is 1 mg/kg IV over 5–30 min [L-ProvayBlue] (different indication and dose from IIE use).
- Taiwan: MB licensed only for methemoglobinemia (rare-disease licence) [TFDA].

## 6. Haemorrhagic cystitis and mesna

### 6a. Ifosfamide urotoxicity — [VERIFIED; L-ifosfamide]
- Hydration: **at least 2 L oral or IV fluid per day**; mesna to reduce haemorrhagic cystitis.
- Haematuria (pooled): **44.1% without mesna vs 21.3% with mesna**; macrohaematuria **11.1% vs 5.2%**.
- Risk is dose-dependent and higher with **single high doses than fractionated** dosing; prior/concomitant bladder radiation or busulfan increases risk.
- **Urinalysis before each dose; if microscopic haematuria > 10 RBC/HPF, withhold until complete resolution.** Exclude or correct urinary outflow obstruction (contraindication).

### 6b. Mesna dosing (US label; ifosfamide 1.2 g/m²/day) — [VERIFIED; L-Mesnex 2025-12-10]

| Schedule | 0 h | +2 h | +4 h | +6 h | +8 h | Total mesna |
|---|---|---|---|---|---|---|
| **IV only** | **20% w/w IV bolus** (240 mg/m²) | — | **20% IV** | — | **20% IV** | **60%** of ifosfamide dose |
| **IV + oral** | **20% IV** (240 mg/m²) | **40% PO** (480 mg/m²) | — | **40% PO** | — | **100%** |

- Repeat on **each day** ifosfamide is given; keep the **mesna : ifosfamide ratio** when the ifosfamide dose changes.
- IV + oral regimen **not established for ifosfamide > 2 g/m²/day**; repeat the oral dose (or give IV) if vomiting within 2 h.
- Ifosfamide and mesna may be **mixed in the same bag** if ifosfamide ≤ 50 mg/mL.
- **False-positive urine ketones** (nitroprusside dipstick) and interference with enzymatic CPK assays; mesna IV contains benzyl alcohol (avoid in premature neonates); hypersensitivity, DRESS, SJS/TEN reported.
- ASCO 1999: mesna "dosed as detailed in these guidelines" recommended for standard-dose ifosfamide; **insufficient evidence for ifosfamide > 2.5 g/m²/day** [Hensley 1999, A]. 2008 update: no new mesna RCTs since 2002 [Hensley 2009, A].
- Pump-delivered HDI example: mesna **14 g/m²** with ifosfamide 14 g/m² over 14 days (1:1) [Meazza 2010, A].
- Taiwan: **Uromitexan (優路保注射液) 衛署藥輸字第018485號** active; indication 「防止OXAZAPHOSPHORINES類藥物所引起出血性膀胱發炎」 [TFDA].

## 7. Ifosfamide nephrotoxicity and Fanconi syndrome

- Label: glomerular and tubular dysfunction "very common"; **Fanconi syndrome, renal rickets and growth retardation in children, osteomalacia in adults**, SIADH-like syndrome; tubular damage may appear **months or even years after** treatment; monitor glomerular and tubular function, urinary sediment, **phosphorus and potassium**; replace as needed [VERIFIED; L-ifosfamide].
- **Dose-response in children (n = 593, LESS):** new tubulopathy 4.6% overall; **0.4% at ≤ 24 g/m², 6.5% at 24–60 g/m², 8.0% at ≥ 60 g/m²**; **age < 4 years: 8.7-fold risk** [Stöhr 2007a, A].
- UKCCSG (n = 148, median cumulative 62 g/m²): of fully evaluable patients 50% mild, 20% moderate, 8% severe nephrotoxicity; **keeping total dose < 84 g/m² reduces (does not abolish) risk; > 119 g/m² very high risk** [Skinner 2000, A].
- **Growth:** children with ifosfamide tubulopathy had height SDS −1.7 at renal diagnosis and −2.1 at last review; **7.3 cm shorter** than controls; slow GFR decline in severe cases [Stöhr 2007b, A].
- **Adults (n = 34, French nephrology units):** proximal tubulopathy ± AKI ± CKD; biopsy acute tubular necrosis 85.7%; **29.4% reached CKD stage 5, 17.6% needed haemodialysis**; risk factors age and **cisplatin co-administration** [Ensergueix 2020, A].
- **Survivorship surveillance (IGHG 2025):** glomerular function every **2–5 years** after ifosfamide (eGFR with creatinine ± cystatin C); **tubular function once at entry into long-term follow-up**, then as indicated [Kooijmans 2025, A].

## 8. Anthracycline cardiotoxicity, dexrazoxane and extravasation

### 8a. Doxorubicin cumulative dose — [VERIFIED]
- Label probability of cardiomyopathy (q3w dosing): **1–2% at 300 mg/m², 3–5% at 400, 5–8% at 450, 6–20% at 500 mg/m²**; cumulative > 550 mg/m² carries increased risk; count prior anthracyclines/anthracenediones; increase LVEF monitoring frequency above 300 mg/m²; use the same LVEF method each time [L-doxorubicin].
- Swain 2003 (630 patients on doxorubicin-placebo arms): estimated **26% CHF at 550 mg/m²**; age > 65 a risk factor after 400 mg/m²; > 50% of CHF cases had LVEF reduction < 30% (LVEF not a reliable predictor) [A].
- Sarcoma practice context: 6 cycles × 75 mg/m² = **450 mg/m²** [calc] (EORTC 62012 and GeDDiS both capped at 6 cycles [A]); AEWS0031 cumulative **375 mg/m²** [FT-WF].
- Continuous infusion vs bolus: real-world MarketScan sarcoma cohort found no cardiac advantage for CIV after adjustment (time-to-treatment failure favoured bolus, HR 0.71) [Cranmer 2023, A].
- Trabectedin label: prior cumulative anthracycline **≥ 300 mg/m²** is a risk factor for trabectedin cardiomyopathy; LVEF at baseline then every 2–3 months [L-Yondelis].

### 8b. Dexrazoxane — [VERIFIED]
- US label: **10:1 dexrazoxane : doxorubicin** (e.g., 500 mg/m² for 50 mg/m²); give doxorubicin **within 30 min after** the dexrazoxane infusion ends; **CLcr < 40 mL/min: reduce 50% (5:1)**; indication only MBC after 300 mg/m² [L-dexrazoxane Eugia 2026-08-10].
- ASCO 1999: may be considered in adults with other tumours after > 300 mg/m², with caution about tumour protection where doxorubicin improves survival; insufficient evidence for children [Hensley 1999, A]. ASCO 2008: consider after > 300 mg/m² when continued doxorubicin may benefit [Hensley 2009, A].
- POG 9404 (children, cumulative doxorubicin 360 mg/m²): dexrazoxane before every dose — no loss of EFS (77.2% vs 76.0%), better echo indices, no significant excess second malignancies (8 vs 3 of 11, P = .17); authors recommend dexrazoxane for children on anthracyclines [Asselin 2016, A]. Erratum J Clin Oncol 2017 (PMID 28618244, content not read).
- Taiwan: **no dexrazoxane licence** [TFDA].

### 8c. Doxorubicin extravasation — [VERIFIED]
- Label: stop infusion; **do not remove the needle until aspiration attempted; do not flush; no pressure; ice 15 min four times daily for 3 days; elevate the limb; in adults consider dexrazoxane**; continuous infusions only via a central line [L-doxorubicin].
- Dexrazoxane (Savene/Totect) for biopsy-proven anthracycline extravasation: **1000 mg/m² D1, 1000 mg/m² D2, 500 mg/m² D3, starting ≤ 6 h**; surgery avoided in **98.2% (53/54)** [Mouridsen 2007, A]. (Not available in Taiwan [TFDA].)

## 9. Trabectedin: liver, CK/rhabdomyolysis, neutropenia, line and extravasation — [VERIFIED; L-Yondelis unless stated]

**Before each dose:** CBC, LFTs (bilirubin, AST/ALT, ALP), **CPK**; LVEF at baseline then every 2–3 months.

| Test (prior cycle) | **Delay** next dose (≤ 3 weeks) | **Reduce** one level |
|---|---|---|
| Platelets | < 100,000/µL | < 25,000/µL |
| ANC | < 1,500/µL | < 1,000 with fever/infection, or < 500 for > 5 days |
| Total bilirubin | > ULN | > ULN |
| AST or ALT | > 2.5 × ULN | > 5 × ULN |
| ALP | > 2.5 × ULN | > 2.5 × ULN |
| **CPK** | **> 2.5 × ULN** | **> 5 × ULN** |
| Other non-haematological | Grade 3–4 | Grade 3–4 |

- Dose levels: **1.5 → 1.2 → 1.0 mg/m²** (moderate hepatic impairment 0.9 → 0.6 → 0.3); never re-escalate.
- **Permanently discontinue** for: delay > 3 weeks; need to reduce below 1.0 mg/m²; severe liver dysfunction (bilirubin 2 × ULN **and** AST/ALT 3 × ULN with ALP < 2 × ULN); **capillary leak syndrome; rhabdomyolysis**; grade 3–4 cardiac events or LVEF < LLN.
- SAR-3007 rates: grade 3–4 neutropenia 43%; **febrile neutropenia 5%**; neutropenic sepsis 2.6% (fatal 1.1%); **CPK elevation 32% (grade 3–4 6%)**; **fatal rhabdomyolysis 0.8%**; grade 3–4 LFT elevations **35%** (85% resolved, median 13 days); ALT/AST > 8 × ULN 18%; Hy's-law DILI 1.3%; cardiomyopathy 6%.
- Pharmacovigilance (10,841 patients): rhabdomyolysis **0.7%** (fatal 0.3%), mostly in **cycle 2**; no predictive factor found [Grosso 2012, A].
- **Dexamethasone premedication reduces hepatotoxicity and myelosuppression:** in a named-patient series, grade 3–4 transaminase rise **34% → 2%**, neutropenia **24% → 2%** of courses with oral dexamethasone 4 mg BID started 24 h before (historical schedule) [Grosso 2006, A]. Current label: **dexamethasone 20 mg IV 30 min before** each dose.
- **CYP3A:** ketoconazole ↑ trabectedin exposure **66%**; rifampin ↓ **31%**; avoid strong inhibitors/inducers; if a short (< 14 days) strong inhibitor is unavoidable, give it **1 week after** the infusion and stop it the day before the next.
- **Administration:** reconstitute 1 mg with 20 mL SWFI (0.05 mg/mL); dilute in **500 mL** NS or D5W; **0.2-µm PES in-line filter**; finish within **30 h of reconstitution**; **central venous line** only.
- **Extravasation:** tissue necrosis needing debridement; **necrosis may appear > 1 week later; no specific antidote** [L-Yondelis]. Sterile inflammation along tunnelled port catheters: **0/12 vs 5/9** patients depending on the port system (Tokyo) [Kubo 2024, A]. Nurse-inserted PICCs: 45 patients, 509 cycles, no complications needing device removal [Martella 2015, A].
- Contraception: females **8 months**, males **5 months** after the last dose.

## 10. Pazopanib: hepatotoxicity and hypertension — [VERIFIED; L-Votrient 2025-12-16]
- **Boxed warning: severe and fatal hepatotoxicity.** Age > 65 years = higher risk; **92% of transaminase rises occur in the first 18 weeks**.
- **LFT schedule:** baseline; **weeks 3, 5, 7 and 9; months 3 and 4**; then periodically; weekly if ALT elevated.
- STS trial: ALT > 3 × ULN 18%, > 8 × ULN 5%; Hy's-law pattern 2%; 1 hepatic-failure death.

| ALT event | Action |
|---|---|
| Isolated 3–8 × ULN | **Continue**; LFTs weekly until grade 1/baseline |
| Isolated > 8 × ULN | **Withhold**; if resuming, **≤ 400 mg daily** with weekly LFTs × 8 weeks; stop if > 3 × ULN recurs |
| > 3 × ULN **with** bilirubin > 2 × ULN | **Permanently discontinue** |
| Gilbert's (indirect bilirubin only) | Manage as isolated ALT (pazopanib inhibits UGT1A1) |

- **Hypertension:** ~**40%**, grade 3 in 4–7%; **~40% by day 9, ~90% within 18 weeks**; ~1% stop for HTN. Do not start with uncontrolled BP; **grade 2–3: dose-reduce + antihypertensives; persistent grade 3 despite reduction or grade 4/crisis: discontinue**.
- Other monitoring: QT/electrolytes, LVEF if at risk, thyroid, urinalysis/proteinuria (≥ 3 g/24 h → hold), VTE/ATE, haemorrhage, GI perforation/fistula, PRES, ILD, TLS, infection.
- Practical: take **without food**; avoid **gastric acid-reducing agents**; strong CYP3A4 inhibitor → 400 mg; hold **≥ 1 week before elective surgery**, restart ≥ 2 weeks after major surgery when healed.

## 11. Imatinib: oedema, myelosuppression and drug interactions — [VERIFIED; L-Gleevec 2026-07-13]
- **Oedema/fluid retention:** GIST phase 3 trials — oedema **76.7% (400 mg) vs 86.1% (800 mg)**, grade 3–5 **9.0% vs 13.1%**; severe fluid retention **9–13.1%** in GIST; superficial (periorbital, lower limb) oedema managed with diuretics, supportive care or dose reduction. **Weigh regularly; investigate rapid weight gain.**
- **CBC: weekly for month 1, every 2 weeks in month 2, then every 2–3 months.**
- **GIST cytopenia rule:** ANC < 1.0 × 10⁹/L and/or platelets < 50 × 10⁹/L → stop until ANC ≥ 1.5 and platelets ≥ 75 → resume **400 mg**; if it recurs → resume at **300 mg**.
- **Hepatotoxicity:** LFTs before start and **monthly**; bilirubin > 3 × IULN or transaminases > 5 × IULN → hold until < 1.5 × / < 2.5 × → resume reduced (400 → 300, 600 → 400, 800 → 600 mg). Fatal liver failure reported.
- **Drug interactions:**
  - Strong **CYP3A4 inducers** (label examples: **dexamethasone**, phenytoin, carbamazepine, rifampin, rifabutin, phenobarbital) → avoid; if unavoidable **increase imatinib ≥ 50%**.
  - Strong **CYP3A4 inhibitors** and **grapefruit juice** → ↑ imatinib exposure; avoid.
  - Imatinib **inhibits CYP3A4 and CYP2D6** → ↑ levels of triazolo-benzodiazepines, dihydropyridine CCBs, some statins; caution with narrow-therapeutic-index substrates.
  - **Anticoagulation: LMWH or heparin, not warfarin.**
  - May delay clearance of **HD-methotrexate (> 500 mg/m²)**.
- Other: CHF/LV dysfunction; **growth retardation in children** (monitor growth); renal function decline (median eGFR 85 → 75 at 12 months → 69 mL/min/1.73 m² at 60 months); hypothyroidism in thyroidectomised patients on levothyroxine (monitor TSH); TLS; GI irritation (take with food); embryo-fetal toxicity.

## 12. Regorafenib (and other GIST TKIs): HFSR, hepatotoxicity, hypertension — [VERIFIED]
- **HFSR (regorafenib):** pooled RCTs **53% vs 8%**; **grade 3 16%**; **Asian patients 72% (grade 3 18%)**; most cases in **cycle 1**; TEN 0.02% [L-Stivarga 2026-02-09].
- **Label HFSR rules:** first grade 2 → reduce to 120 mg; grade 2 recurrent or not improved within 7 days despite reduction → interrupt; **grade 3 → interrupt ≥ 7 days**, then reduce; recurrence at 120 → 80 mg [L-Stivarga].
- **Hepatotoxicity (boxed):** most within the **first 2 months**, hepatocellular pattern; GRID fatal hepatic failure 0.8%; postmarketing **hyperammonaemic encephalopathy**. **LFTs before start, at least every 2 weeks for 2 months, then monthly**; weekly while abnormal. **Permanently stop** for AST/ALT > 20 × ULN, > 3 × ULN with bilirubin > 2 × ULN, or recurrence > 5 × ULN despite 120 mg [L-Stivarga].
- **Hypertension:** 59% vs 27% in GRID; mostly cycle 1; **BP weekly for 6 weeks**, then each cycle [L-Stivarga].
- Surgery: hold **≥ 2 weeks** before elective surgery [L-Stivarga].
- **Dose-escalation strategy (CRC, not GIST):** ReDOS — 80 → 120 → 160 mg weekly escalation: **43% vs 26%** started cycle 3 (one-sided p = 0.043); clobetasol 0.05% cream to palms/soles pre-emptive vs reactive showed no interaction [Bekaii-Saab 2019, A]. Applying this to GIST is **[UNVERIFIED]** extrapolation.
- **Sunitinib:** boxed hepatotoxicity (LFT baseline and every cycle; grade 3 hold → reduce; grade 4 stop); HTN, LVEF, QT, haemorrhage, TMA, proteinuria, dermatologic toxicity [L-Sutent].
- **Ripretinib:** PPES grade 1–2 **21%**; **cutaneous SCC 4.7%** (median 4.6 months) → skin exams at start and routinely; HTN; LVEF baseline; photosensitivity; hold ≥ 1 week before surgery [L-Qinlock]. Alopecia 55% in the Taiwan/HK cohort [Lin 2022, A].
- **Avapritinib:** intracranial haemorrhage **2.9%** of 749 GIST/AdvSM patients → **permanently stop for any grade**; cognitive effects; photosensitivity [L-Ayvakit].

## 13. Febrile neutropenia risk and G-CSF primary prophylaxis — [VERIFIED unless marked]
- **Threshold:** ASCO 2015 — primary prophylaxis when FN risk is **~20% or higher** and no equally effective non-CSF regimen exists [Smith 2015, A]. EORTC 2010 — **high risk ≥ 20%, intermediate 10–20%** (add patient factors such as age ≥ 65); give G-CSF after a previous FN episode; filgrastim, lenograstim and pegfilgrastim all acceptable [Aapro 2011, A]. Whether EORTC's regimen list names AI/AIM: **[UNVERIFIED]** (full text not read).
- **Regimen FN rates (primary sources):**

| Regimen | FN / severe neutropenia | G-CSF in trial | Source |
|---|---|---|---|
| Doxorubicin 75 + ifosfamide 10 g/m² (EORTC 62012) | **FN 46%** (vs 13% doxorubicin alone) | **Pegfilgrastim D5 mandated** | [A; CT] |
| Epirubicin 60 mg/m²/day D1–2 + ifosfamide 3 g/m²/day D1–3 (ISG-STS 1001) | Grade ≥ 3 neutropenia **86%** | Not stated in abstract | [A] |
| Doxorubicin 75 alone (GeDDiS) | FN grade 3–4 **20%** | Only after FN | [A; FT] |
| Gem 675/doc 75 (GeDDiS) | FN **12%** | Only after FN | [A; FT] |
| Gem 900/doc 100 (Hensley 2002) | Neutropenic fever **6%** | G-CSF D9–15 | [A] |
| Trabectedin 1.5 mg/m² | FN **5%** | — | [L-Yondelis] |
| Eribulin (sarcoma Study 2) | FN **0.9%**; ANC < 500 > 1 week 12% | — | [L-Halaven] |
| Interval-compressed VDC/IE (Taiwan) | Fever **36%** of cycles, bacteraemia 8% | Filgrastim 5–10 µg/kg/day | [Huang 2023, A] |

- **Pediatric G-CSF dosing (VDC/IE):** pegfilgrastim **100 µg/kg once per cycle ≈ filgrastim 5 µg/kg/day**; younger children had more protracted neutropenia [Spunt 2010, A].
- Ifosfamide label: do not give ifosfamide with WBC < 2,000/µL or platelets < 50,000/µL unless essential; nadir ~week 2 [L-ifosfamide].
- NCCN Hematopoietic Growth Factors version **1.2027** exists [NCCN]; its regimen risk list was not read **[UNVERIFIED]**.

## 14. Fertility preservation in AYA sarcoma patients — [VERIFIED unless marked]
- **ASCO 2018:** discuss infertility risk **as early as possible** with patients (or parents) and refer to reproductive specialists; **document** the discussion; **sperm, oocyte and embryo cryopreservation are standard**; GnRH agonists have conflicting evidence and **must not replace proven methods**; ovarian tissue cryopreservation "may evolve to become standard" [Oktay 2018, A]. (ESMO 2020 guideline exists [Lambertini 2020]; no PubMed abstract; content **not read**.)
- **Cyclophosphamide equivalent dose (CED):** CED (mg/m²) = cyclophosphamide + **0.244 × ifosfamide** + 0.857 × procarbazine + 14.286 × chlorambucil + 15.0 × BCNU + 16.0 × CCNU + 40 × melphalan + 50 × thiotepa + 100 × nitrogen mustard + 8.823 × busulfan (all cumulative mg/m²) [Green 2014, FT].
  - Worked example [calc; illustrative]: AEWS0031-type therapy with 7 IE cycles (ifosfamide 9 g/m² each = 63 g/m²) and 7 cyclophosphamide 1.2 g/m² cycles (8.4 g/m²) → CED ≈ 8,400 + 0.244 × 63,000 ≈ **23,800 mg/m²**. The 7/7 cycle split is inferred from "14 cycles" alternating VDC/IE [A] and **not confirmed from the protocol [UNVERIFIED]**.
- **Ifosfamide and gonads:** males with cumulative ifosfamide **> 60 g/m²** — two-thirds of those with semen analysis subfertile, 31% raised FSH, 50% low inhibin B; **no dysfunction below 60 g/m²**; females had normal puberty and menses but **lower AMH** than age-matched references [Williams 2008, A].
- **Targeted-therapy examples:** nirogacestat ovarian toxicity 75% (section C); trabectedin, eribulin, TKIs require contraception per label (e.g., trabectedin 8 months F / 5 months M; eribulin 2 weeks F / 3.5 months M [L-Halaven]; regorafenib 2 months both [L-Stivarga]).
- NCCN **AYA Oncology version 2.2027** and **Survivorship 3.2026** exist [NCCN]; content not read.
- Taiwan-specific fertility-preservation subsidy or regulations: **[UNVERIFIED]** (HPA site unreachable).

## 15. Growth and psychosocial issues — [VERIFIED as stated]
- **Growth:** imatinib — growth retardation in children/pre-adolescents, monitor growth [L-Gleevec]; ifosfamide tubulopathy — mean height deficit 7.3 cm [Stöhr 2007b, A]; ifosfamide label — renal rickets/growth retardation [L-ifosfamide]; expandable endoprostheses — leg-length discrepancy **13.4%** at latest follow-up (pediatric systematic review) [Groundland 2016, A].
- **Quality of life:** AYA survivors more likely to report worse QoL than the general population; professionals often underestimate AYA support needs; authors call for AYA-specific multidisciplinary programmes [Quinn 2015, A].
- **Amputation vs limb salvage:** meta-analysis of 6 studies (256 patients, osteosarcoma/Ewing) — **similar functional outcomes and QoL** [Mei 2014, A]. A broader pediatric/AYA bone-tumour QoL meta-analysis exists (Stokke 2015, PMID 25820683) but was **not read**.
- Psychosocial screening tools, school/work reintegration data specific to Taiwan: **[UNVERIFIED]**.

## 16. Limb-salvage rehabilitation and endoprosthesis infection — [VERIFIED]
- **Infection rate:** pooled deep infection after lower-limb endoprosthetic reconstruction **~10% (95% CI 8–11%)**, mostly Gram-positive; retrospective data suggested 13% after short vs 8% after long antibiotic courses [Racano 2013, A].
- **PARITY RCT (n = 604, 48 sites, 12 countries):** cefazolin or cefuroxime every 8 h for **5 days vs 1 day** after surgery → SSI within 1 year **15.0% vs 16.7% (HR 0.93, 0.62–1.40, P = .73)**; antibiotic complications **5.1% vs 1.6% (HR 3.24)** [A]. Teaching point: longer prophylaxis does not prevent infection and causes harm.
- **Failure modes of tumour endoprostheses (Henderson):** Type 1 soft-tissue failure, Type 2 aseptic loosening, Type 3 structural failure, **Type 4 infection**, Type 5 tumour progression; infection was the most common failure in the five-institution series (n = 2,174; 534 failures) [Henderson 2011, A].
- **Pediatric limb salvage:** subsequent amputation **5.2% (vs 9.5% adults)**; MSTS scores 71.0–86.8%; infection a primary failure mode in all reconstruction types [Groundland 2016, A].
- **Exercise rehabilitation after lower-limb salvage:** 7 studies, 214 participants; no intervention therapeutically valid; very low-certainty evidence of +10–15° knee ROM and better compliance [van Kouswijk 2023, A]. Specific post-op protocols (weight-bearing timing, CPM, knee flexion targets): **[UNVERIFIED]**.

---

# E. TAIWAN LICENCE STATUS (TFDA dataset InfoId 36, file 2026-10-27) — [VERIFIED; TFDA]

| Drug | Taiwan status | Licence no. (product, holder) | TFDA indication (sarcoma-relevant wording) |
|---|---|---|---|
| **Trabectedin** | **Licensed** | 衛部藥輸字第027370號 「友待」凍晶注射劑 1 mg (Yondelis; 台灣東洋); issued 2018-01-09, valid to 2028-01-09 | 無法切除或轉移性**脂肪肉瘤或平滑肌肉瘤**，且曾接受一種含 anthracycline 療程 |
| **Eribulin** | **Licensed — liposarcoma only** | 衛部藥輸字第026140號 賀樂維 Halaven (衛采; 2013-08-28); generics 衛部藥製字第061399號 (台耀, 2022-12-30) and 衛部藥輸字第029002號 (瑞迪, 2025-07-29) | 無法手術切除或轉移性**脂肪肉瘤**，先前至少接受一次含 anthracycline 之全身化療 (plus MBC) |
| **Pazopanib** | **Licensed** (200-mg tablets only) | 衛署藥輸字第025433號 福退癌 Votrient 200 mg (台灣諾華; updated 2026-08-06); 衛部藥製字第060908號 Alvopanib (美時); 衛部藥輸字第029077號 Redpanib (瑞迪, 2026-01-05). Votrient 400 mg 衛署藥輸字第025434號 cancelled 2021-06-08 | 先前曾接受化療的晚期**軟組織肉瘤**；對 adipocytic STS 或 GIST 療效尚未證實 |
| **Tazemetostat** | **Not licensed** (no record) | — | — |
| **Nirogacestat** | **Not licensed** (no record) | — | — |
| **Pexidartinib** | **Cancelled 2026-02-03 (自請註銷)** | 衛部藥輸字第028293號 圖拉留 Turalio 200 mg (台灣第一三共; issued 2022-05-27) | (was) 症狀性**腱鞘巨細胞瘤 (TGCT)** |
| **Vimseltinib** | **Not licensed** (no record) | — | — |
| **Ripretinib** | **Licensed** | 衛部藥輸字第028106號 期樂錠 Qinlock 50 mg (再鼎; 2021-07-26; updated 2026-03-25) | 已接受 **3 種或以上激酶抑制劑 (包括 imatinib)** 的晚期 GIST 成人 |
| **Avapritinib** | **Licensed — D842V only** | 衛部藥輸字第028029/028030/028031號 泰時維 Ayvakit 100/200/300 mg (基石; 2021-03-25) | 具 **PDGFRA D842V** 突變，無法切除或轉移性 GIST 成人 |
| **Regorafenib** | **Licensed — GIST yes; osteosarcoma no** | 衛部藥輸字第026168號 癌瑞格 Stivarga 40 mg (台灣拜耳; 2013-10-11) | GIST 先前曾接受 imatinib 和 sunitinib；CRC；HCC |
| **Cabozantinib** | **Licensed — no sarcoma indication** | 衛部藥輸字第027511/027512/027513號 癌必定 Cabometyx 20/40/60 mg (益普生; 2018-10-12) | RCC, HCC, DTC (≥ 12 y), pNET/epNET (≥ 12 y) |
| **Mifamurtide** | **Cancelled 2023-10-17 (自請註銷)** | 衛部藥輸字第026319號 秘配得 MEPACT 4 mg (台灣武田) | (was) 非轉移性高惡性度骨肉瘤術後 |
| **Afamitresgene autoleucel** | **Not licensed** (no record; CAR-T products are in the dataset) | — | — |
| **Glucarpidase** | **Not licensed** (no record) | — | — |

Supportive and related products [VERIFIED; TFDA]:
- **Imatinib:** Glivec 100 mg 衛署藥輸字第024027號 active (GIST unresectable/metastatic, **adjuvant KIT+ GIST after complete gross resection**, DFSP, CML etc.); Glivec 400 mg cancelled 2021-05-10; generic 400-mg tablets active (Alvotinib 衛部藥輸字第026614號; Redistra 衛部藥輸字第027973號).
- **Sunitinib:** Sutent 12.5/25/50 mg (衛署藥輸字第024593/024594/024595號) — GIST after imatinib progression or intolerance; generics (e.g., Alsuni 衛部藥製字第060554號).
- **Ifosfamide:** Holoxan 500 mg/1 g/2 g (衛署藥輸字第018481/018480/018479號) — indication includes 軟組織肉瘤（平滑肌肉瘤、橫紋肌肉瘤、軟骨肉瘤）、骨肉瘤.
- **Doxorubicin:** Adriamycin 2 mg/mL 衛署藥輸字第022712號 — indication includes 軟纖維性肉瘤.
- **Mesna:** Uromitexan 衛署藥輸字第018485號 (active).
- **Dexrazoxane:** none. **Methylene blue:** 衛部罕藥製字第000013號 (methemoglobinemia only). **Thiamine injection:** 15 active single-ingredient licences.
- **Dacarbazine:** melanoma indication only (e.g., 衛署藥輸字第022131號).
- **Olaratumab (Lartruvo)** 衛部菌疫輸字第001075號: cancelled 2019-09-04 (自請註銷).
- **Denosumab (Xgeva)** 衛署菌疫輸字第000924號 and biosimilars: include **骨巨細胞瘤** (GCTB) indication.
- **NTRK-fusion agents** licensed tumour-agnostic: larotrectinib (Vitrakvi), entrectinib (Rozlytrek), repotrectinib (Augtyro).
- **Selumetinib** (Koselugo): NF1 plexiform neurofibroma, age ≥ 3.

---

# F. NCCN VERSIONS SHOWN ON nccn.org (2026-10-29) — [VERIFIED; NCCN; content not read]
Soft Tissue Sarcoma **1.2026**; Gastrointestinal Stromal Tumors **1.2026**; Bone Cancer **1.2027**; Hematopoietic Growth Factors **1.2027**; Adolescent and Young Adult (AYA) Oncology **2.2027**; Survivorship **3.2026**; Antiemesis **2.2026**.

---

# G. EXAM / WARD PEARLS (each tied to a verified source above)
1. Mesna IV = **20% of the ifosfamide dose at 0, 4 and 8 h (total 60%)**; IV + oral = 20% IV, then **40% PO at 2 and 6 h (total 100%)** (section 6b).
2. Hold ifosfamide if urinalysis shows **> 10 RBC/HPF**; hydrate **≥ 2 L/day** (6a).
3. IIE: **stop ifosfamide, hydrate**; MB 50 mg IV (check for opioids/SSRIs → serotonin syndrome); thiamine 100 mg IV; dialysis if refractory. Risk factors: **low albumin, high creatinine, poor PS, prior cisplatin, pelvic disease** (5).
4. Ifosfamide tubulopathy (Fanconi) → **check phosphate, potassium, bicarbonate, glycosuria**; risk ↑ with cumulative dose (> 60 g/m²) and age < 4 (7).
5. Doxorubicin cardiomyopathy probability **6–20% at 500 mg/m²**; **dexrazoxane 10:1**, not licensed in Taiwan (8).
6. Doxorubicin extravasation: **ice, not heat**; dexrazoxane 1000/1000/500 mg/m² within 6 h (8c). Trabectedin extravasation: **no antidote, central line only, necrosis can appear > 1 week later** (9).
7. Trabectedin before every dose: **CBC, LFT, CPK**; premed **dexamethasone 20 mg IV**; 24-h infusion with **0.2-µm filter** (9).
8. Pazopanib LFTs **weeks 3, 5, 7, 9, months 3, 4**; take on an empty stomach; HTN in ~40% (10).
9. Imatinib: **with food**; weigh for oedema; **no warfarin**; strong CYP3A4 inducers (incl. dexamethasone) → raise dose ≥ 50% (11).
10. Regorafenib: **160 mg × 21/28 after a low-fat meal**; HFSR most in cycle 1, **72% in Asians**; LFT every 2 weeks × 2 months; BP weekly × 6 weeks (12).
11. AI (EORTC 62012) FN **46%** despite pegfilgrastim → **primary G-CSF**; threshold for prophylaxis **≥ 20%** FN risk (13).
12. Fertility talk **before the first cycle** and document it; sperm/oocyte/embryo freezing are standard; GnRHa is not a substitute (14).
13. PARITY: **1 day of post-op antibiotics = 5 days** for endoprostheses; infection ~10–17% (16).
14. Taiwan licences: trabectedin ✓ (LPS/LMS), eribulin ✓ (**LPS only**), pazopanib ✓ (non-adipocytic STS), ripretinib ✓, avapritinib ✓ (**D842V only**), regorafenib ✓ (GIST, not bone sarcoma); **pexidartinib cancelled 2026**, mifamurtide cancelled 2023; **no** tazemetostat, nirogacestat, vimseltinib, afami-cel, glucarpidase, dexrazoxane (E).

---

# H. NOT VERIFIED / NOT FOUND (as of 2026-10-29)
- Exact SARC 002 (Maki 2007) doses (abstract silent; only secondary statement in GeDDiS full text).
- Mesna schedule for continuous-infusion or high-dose ifosfamide (ASCO 2002/2008 full texts paywalled); mesna dose in EORTC 62012 and in "AIM" protocols.
- Per-day doses and dexrazoxane dose in COG AEWS1031 Table 1 (image).
- AEWS0031 exact number of VDC vs VC vs IE cycles (used only in an illustrative CED calculation).
- Whether NCCN/EORTC regimen lists classify AIM or VDC/IE as high FN risk (> 20%).
- Ripretinib OS formal testing status in INVICTUS.
- Regorafenib dose-escalation (ReDOS) in GIST.
- NHI (健保) reimbursement criteria for any drug in this file (nhi.gov.tw unreachable).
- Taiwan package-insert (仿單) wording for Yondelis, Halaven, Votrient, Qinlock (dataset shows only 「詳見仿單」).
- Content of errata: Maki 2007, Womer 2012, INVICTUS, NAVIGATOR, Asselin 2016, ISG-STS 1001, Lin 2022.
- ESMO 2020 fertility guideline content; Stokke 2015 QoL meta-analysis content.
- Taiwan-specific fertility-preservation subsidies; Taiwan AYA psychosocial data; detailed post-limb-salvage rehabilitation protocols.

---

# J. REFERENCES (APA 7)

## J1. Official labels, datasets and registries (read 2026-10-29)
- American Regent, Inc. (2025). *PROVAYBLUE (methylene blue) injection* [Prescribing information; SPL set ID 4f6848e5-35ed-4046-b13c-3032b5ba3232; effective 2025-05-28]. openFDA. https://api.fda.gov/drug/label.json
- Bamboo US Bidco LLC. (2025). *MESNEX (mesna) injection and tablets* [Prescribing information; SPL set ID 1dd69e84-616d-fb77-e063-6394a90af2f4; effective 2025-12-10]. openFDA.
- Bayer HealthCare Pharmaceuticals Inc. (2026). *STIVARGA (regorafenib) tablets* [Prescribing information; SPL set ID 824f19c9-0546-4a8a-8d8f-c4055c04f7c7; effective 2026-02-09]. openFDA.
- Blueprint Medicines Corporation. (2026). *AYVAKIT (avapritinib) tablets* [Prescribing information; SPL set ID 645c887c-8cd4-4623-8da9-ac223d71a8b9; effective 2026-08-05]. openFDA; DailyMed.
- Daiichi Sankyo Inc. (2025). *TURALIO (pexidartinib) capsules* [Prescribing information; SPL set ID 7b0ec4bf-b2ac-49ee-96af-7740ad3f2e16; effective 2025-01-16]. openFDA.
- Deciphera Pharmaceuticals, LLC. (2025). *QINLOCK (ripretinib) tablets* [Prescribing information; SPL set ID 9f18e462-03dd-4296-a02a-a0577e3ee78d; effective 2025-05-12]. openFDA.
- Deciphera Pharmaceuticals, LLC. (2026). *ROMVIMZA (vimseltinib) capsules* [Prescribing information; SPL set ID f73c7a62-9601-4df0-810f-100f515d79ea; effective 2026-06-26]. openFDA.
- Eisai Inc. (2025). *HALAVEN (eribulin mesylate) injection* [Prescribing information; SPL set ID 31ce4750-ded5-4a0b-95e9-f229fa6bc822; effective 2025-11-07]. openFDA.
- Epizyme, Inc. (2026). *TAZVERIK (tazemetostat) tablets* [Prescribing information; SPL set ID 7db07b5f-4e22-467c-9c0a-f830b08dbb1d; effective 2026-04-29]. openFDA.
- Eugia US LLC. (2026). *Dexrazoxane for injection* [Prescribing information; SPL set ID cb72203a-0b09-42d5-bf51-7f479feb3adb; effective 2026-08-10]. openFDA.
- Exelixis, Inc. (2025). *CABOMETYX (cabozantinib) tablets* [Prescribing information; SPL set ID 3850cce2-6137-42e5-a792-d318c4a4b3b5; effective 2025-10-19]. openFDA.
- Fresenius Kabi USA, LLC. (2026). *Ifosfamide for injection* [Prescribing information; SPL set ID a311a947-7b78-4226-bfe0-f4aa0be20e27; effective 2026-04-09]. openFDA.
- Janssen Products, LP. (2026). *YONDELIS (trabectedin) for injection* [Prescribing information; SPL set ID 472bd78e-be17-4b9d-90f4-9482c3aec9ff; effective 2026-01-06]. openFDA.
- Novartis Pharmaceuticals Corporation. (2025). *VOTRIENT (pazopanib) tablets* [Prescribing information; SPL set ID eeaaaf38-fb86-4d9f-a19d-0f61daac2fd7; effective 2025-12-16]. openFDA.
- Novartis Pharmaceuticals Corporation. (2026). *GLEEVEC (imatinib mesylate) tablets* [Prescribing information; SPL set ID 211ef2da-2868-4a77-8055-1cb2cd78e24b; effective 2026-07-13]. openFDA.
- Pfizer Laboratories Div Pfizer Inc. (2026a). *Doxorubicin hydrochloride injection* [Prescribing information; SPL set ID 00634b2b-4e48-4178-8877-28582af894ad; effective 2026-04-30]. openFDA.
- Pfizer Laboratories Div Pfizer Inc. (2026b). *SUTENT (sunitinib malate) capsules* [Prescribing information; SPL set ID 43a4d7f8-48ae-4a63-9108-2fa8e3ea9d9c; effective 2026-02-20]. openFDA.
- SpringWorks Therapeutics, Inc. (2026). *OGSIVEO (nirogacestat) tablets* [Prescribing information; SPL set ID f172e6ff-3190-41b0-b95a-58a7ef9e9e1e; effective 2026-09-01]. openFDA.
- USWM CT, LLC. (2026). *TECELRA (afamitresgene autoleucel) suspension for intravenous infusion* [Prescribing information; SPL set ID ab24631f-3364-46e1-8074-7244863bcbab; effective 2026-07-15]. openFDA.
- U.S. Food and Drug Administration. (2026). *Drugs@FDA application data* (NDA207953, NDA211723, NDA211810, NDA213973, NDA217677, NDA219304, NDA201532) [Data set]. openFDA `drug/drugsfda`. https://api.fda.gov/drug/drugsfda.json
- 衛生福利部食品藥物管理署 [Taiwan Food and Drug Administration]. (2026). *全部藥品許可證資料集* [All drug licences dataset; InfoId 36; file 36_2.csv dated 2026-10-27] [Data set]. https://data.fda.gov.tw/opendata/exportDataList.do?method=ExportData&InfoId=36&logType=2
- ClinicalTrials.gov. (2026). *NCT00061984* (EORTC 62012); *NCT00006734* (COG AEWS0031); *NCT00227669* (gemcitabine ± docetaxel); *NCT02249702* (TAUL: trabectedin vs gemcitabine–docetaxel, uterine LMS) [Registry records, API v2]. https://clinicaltrials.gov
- National Comprehensive Cancer Network. (2026). *NCCN Guidelines by cancer type / supportive care / specific populations* [Category pages listing versions]. https://www.nccn.org/guidelines/category_1 ; https://www.nccn.org/guidelines/category_3 ; https://www.nccn.org/guidelines/category_4

## J2. Journal articles — regimens and trials

- Judson, I., Verweij, J., Gelderblom, H., Hartmann, J. T., Schöffski, P., Blay, J.-Y., Kerst, J. M., Sufliarsky, J., Whelan, J., Hohenberger, P., Krarup-Hansen, A., Alcindor, T., Marreaud, S., Litière, S., Hermans, C., Fisher, C., Hogendoorn, P. C. W., dei Tos, A. P., & van der Graaf, W. T. A. (2014). Doxorubicin alone versus intensified doxorubicin plus ifosfamide for first-line treatment of advanced or metastatic soft-tissue sarcoma: A randomised controlled phase 3 trial. *The Lancet Oncology*, *15*(4), 415–423. https://doi.org/10.1016/S1470-2045(14)70063-4 — PMID 24618336
- Maki, R. G., Wathen, J. K., Patel, S. R., Priebat, D. A., Okuno, S. H., Samuels, B., Fanucchi, M., Harmon, D. C., Schuetze, S. M., Reinke, D., Thall, P. F., Benjamin, R. S., Baker, L. H., & Hensley, M. L. (2007). Randomized phase II study of gemcitabine and docetaxel compared with gemcitabine alone in patients with metastatic soft tissue sarcomas: Results of Sarcoma Alliance for Research through Collaboration Study 002. *Journal of Clinical Oncology*, *25*(19), 2755–2763. https://doi.org/10.1200/JCO.2006.10.4117 — PMID 17602081 — Erratum: J Clin Oncol. 2007 Aug 20;25(24):3790
- Seddon, B., Strauss, S. J., Whelan, J., Leahy, M., Woll, P. J., Cowie, F., Rothermundt, C., Wood, Z., Benson, C., Ali, N., Marples, M., Veal, G. J., Jamieson, D., Küver, K., Tirabosco, R., Forsyth, S., Nash, S., Dehbi, H.-M., & Beare, S. (2017). Gemcitabine and docetaxel versus doxorubicin as first-line treatment in previously untreated advanced unresectable or metastatic soft-tissue sarcomas (GeDDiS): A randomised controlled phase 3 trial. *The Lancet Oncology*, *18*(10), 1397–1410. https://doi.org/10.1016/S1470-2045(17)30622-8 — PMID 28882536 (PMC5622179)
- Hensley, M. L., Maki, R., Venkatraman, E., Geller, G., Lovegren, M., Aghajanian, C., Sabbatini, P., Tong, W., Barakat, R., & Spriggs, D. R. (2002). Gemcitabine and docetaxel in patients with unresectable leiomyosarcoma: Results of a phase II trial. *Journal of Clinical Oncology*, *20*(12), 2824–2831. https://doi.org/10.1200/JCO.2002.11.050 — PMID 12065559
- Demetri, G. D., von Mehren, M., Jones, R. L., Hensley, M. L., Schuetze, S. M., Staddon, A., Milhem, M., Elias, A., Ganjoo, K., Tawbi, H., Van Tine, B. A., Spira, A., Dean, A., Khokhar, N. Z., Park, Y. C., Knoblauch, R. E., Parekh, T. V., Maki, R. G., & Patel, S. R. (2016). Efficacy and safety of trabectedin or dacarbazine for metastatic liposarcoma or leiomyosarcoma after failure of conventional chemotherapy: Results of a phase III randomized multicenter clinical trial. *Journal of Clinical Oncology*, *34*(8), 786–793. https://doi.org/10.1200/JCO.2015.62.4734 — PMID 26371143 (PMC5070559)
- Schöffski, P., Chawla, S., Maki, R. G., Italiano, A., Gelderblom, H., Choy, E., Grignani, G., Camargo, V., Bauer, S., Rha, S. Y., Blay, J.-Y., Hohenberger, P., D'Adamo, D., Guo, M., Chmielowski, B., Le Cesne, A., Demetri, G. D., & Patel, S. R. (2016). Eribulin versus dacarbazine in previously treated patients with advanced liposarcoma or leiomyosarcoma: A randomised, open-label, multicentre, phase 3 trial. *The Lancet*, *387*(10028), 1629–1637. https://doi.org/10.1016/S0140-6736(15)01283-0 — PMID 26874885
- van der Graaf, W. T. A., Blay, J.-Y., Chawla, S. P., Kim, D.-W., Bui-Nguyen, B., Casali, P. G., Schöffski, P., Aglietta, M., Staddon, A. P., Beppu, Y., Le Cesne, A., Gelderblom, H., Judson, I. R., Araki, N., Ouali, M., Marreaud, S., Hodge, R., Dewji, M. R., Coens, C., . . . Hohenberger, P. (2012). Pazopanib for metastatic soft-tissue sarcoma (PALETTE): A randomised, double-blind, placebo-controlled phase 3 trial. *The Lancet*, *379*(9829), 1879–1886. https://doi.org/10.1016/S0140-6736(12)60651-5 — PMID 22595799
- Gronchi, A., Ferrari, S., Quagliuolo, V., Broto, J. M., Pousa, A. L., Grignani, G., Basso, U., Blay, J.-Y., Tendero, O., Beveridge, R. D., Ferraresi, V., Lugowska, I., Merlo, D. F., Fontana, V., Marchesi, E., Donati, D. M., Palassini, E., Palmerini, E., De Sanctis, R., . . . Casali, P. G. (2017). Histotype-tailored neoadjuvant chemotherapy versus standard chemotherapy in patients with high-risk soft-tissue sarcomas (ISG-STS 1001): An international, open-label, randomised, controlled, phase 3, multicentre trial. *The Lancet Oncology*, *18*(6), 812–822. https://doi.org/10.1016/S1470-2045(17)30334-0 — PMID 28499583 — Erratum: Lancet Oncol. 2017 Jun;18(6):e301. doi: 10.1016/S1470-2045(17)30371-6. (PMID 28593858)
- Martin-Liberal, J., Alam, S., Constantinidou, A., Fisher, C., Khabra, K., Messiou, C., Olmos, D., Mitchell, S., Al-Muderis, O., Miah, A., Linch, M., Jones, R. L., Scurr, M., Judson, I., & Benson, C. (2013). Clinical activity and tolerability of a 14-day infusional ifosfamide schedule in soft-tissue sarcoma. *Sarcoma*, *2013*, Article 868973. https://doi.org/10.1155/2013/868973 — PMID 24369450 (PMC3867825)
- Lee, S. H., Chang, M. H., Baek, K. K., Han, B., Lim, T., Lee, J., & Park, J. O. (2011). High-dose ifosfamide as second- or third-line chemotherapy in refractory bone and soft tissue sarcoma patients. *Oncology*, *80*(3-4), 257–261. https://doi.org/10.1159/000328795 — PMID 21734417
- Meazza, C., Casanova, M., Luksch, R., Podda, M., Favini, F., Cefalo, G., Massimino, M., & Ferrari, A. (2010). Prolonged 14-day continuous infusion of high-dose ifosfamide with an external portable pump: Feasibility and efficacy in refractory pediatric sarcoma. *Pediatric Blood & Cancer*, *55*(4), 617–620. https://doi.org/10.1002/pbc.22596 — PMID 20589638
- Womer, R. B., West, D. C., Krailo, M. D., Dickman, P. S., Pawel, B. R., Grier, H. E., Marcus, K., Sailer, S., Healey, J. H., Dormans, J. P., & Weiss, A. R. (2012). Randomized controlled trial of interval-compressed chemotherapy for the treatment of localized Ewing sarcoma: A report from the Children's Oncology Group. *Journal of Clinical Oncology*, *30*(33), 4148–4154. https://doi.org/10.1200/JCO.2011.41.5703 — PMID 23091096 (PMC3494838) — Erratum: J Clin Oncol. 2015 Mar 1;33(7):814. doi: 10.1200/JCO.2015.61.1491. (PMID 25721580)
- Cash, T., Krailo, M. D., Buxton, A. B., Pawel, B. R., Healey, J. H., Binitie, O., Marcus, K. J., Grier, H. E., Grohar, P. J., Reed, D. R., Weiss, A. R., Gorlick, R., Janeway, K. A., DuBois, S. G., & Womer, R. B. (2023). Long-term outcomes in patients with localized Ewing sarcoma treated with interval-compressed chemotherapy on Children's Oncology Group study AEWS0031. *Journal of Clinical Oncology*, *41*(30), 4724–4728. https://doi.org/10.1200/JCO.23.00053 — PMID 37651654 (PMC10602538)
- Leavey, P. J., Laack, N. N., Krailo, M. D., Buxton, A., Randall, R. L., DuBois, S. G., Reed, D. R., Grier, H. E., Hawkins, D. S., Pawel, B., Nadel, H., Womer, R. B., Letson, G. D., Bernstein, M., Brown, K., Maciej, A., Chuba, P., Ahmed, A. A., Indelicato, D. J., . . . Mascarenhas, L. (2021). Phase III trial adding vincristine-topotecan-cyclophosphamide to the initial treatment of patients with nonmetastatic Ewing sarcoma: A Children's Oncology Group report. *Journal of Clinical Oncology*, *39*(36), 4029–4038. https://doi.org/10.1200/JCO.21.00358 — PMID 34652968 (PMC8677904) — Erratum: J Clin Oncol. 2022 Jul 20;40(21):2393. doi: 10.1200/JCO.22.01234. (PMID 35839523)
- Spunt, S. L., Irving, H., Frost, J., Sender, L., Guo, M., Yang, B.-B., Dreiling, L., & Santana, V. M. (2010). Phase II, randomized, open-label study of pegfilgrastim-supported VDC/IE chemotherapy in pediatric sarcoma patients. *Journal of Clinical Oncology*, *28*(8), 1329–1336. https://doi.org/10.1200/JCO.2009.24.8872 — PMID 20142595 (PMC2834494)
- Huang, J.-H., Chen, S.-H., Liao, Y.-M., Kao, Y.-C., Ho, W.-L., Chang, H., Tsai, M.-L., Lee, H.-L., Kuo, C.-C., Tseng, S.-H., Chang, C.-Y., Hsieh, K. L.-C., Lu, L.-S., Chen, Y.-J., Chiou, J.-F., Hsieh, T.-H., Liu, Y.-R., Hsu, W., Li, W.-T., . . . Liu, Y.-L. (2023). Feasibility and toxicity of interval-compressed chemotherapy in Asian children and young adults with sarcoma. *Journal of Personalized Medicine*, *13*(4), Article 668. https://doi.org/10.3390/jpm13040668 — PMID 37109054 (PMC10146212)
- Demetri, G. D., von Mehren, M., Blanke, C. D., Van den Abbeele, A. D., Eisenberg, B., Roberts, P. J., Heinrich, M. C., Tuveson, D. A., Singer, S., Janicek, M., Fletcher, J. A., Silverman, S. G., Silberman, S. L., Capdeville, R., Kiese, B., Peng, B., Dimitrijevic, S., Druker, B. J., Corless, C., . . . Joensuu, H. (2002). Efficacy and safety of imatinib mesylate in advanced gastrointestinal stromal tumors. *The New England Journal of Medicine*, *347*(7), 472–480. https://doi.org/10.1056/NEJMoa020461 — PMID 12181401
- Gastrointestinal Stromal Tumor Meta-Analysis Group (MetaGIST). (2010). Comparison of two doses of imatinib for the treatment of unresectable or metastatic gastrointestinal stromal tumors: A meta-analysis of 1,640 patients. *Journal of Clinical Oncology*, *28*(7), 1247–1253. https://doi.org/10.1200/JCO.2009.24.2099 — PMID 20124181 (PMC2834472)
- DeMatteo, R. P., Ballman, K. V., Antonescu, C. R., Maki, R. G., Pisters, P. W. T., Demetri, G. D., Blackstein, M. E., Blanke, C. D., von Mehren, M., Brennan, M. F., Patel, S., McCarter, M. D., Polikoff, J. A., Tan, B. R., & Owzar, K. (2009). Adjuvant imatinib mesylate after resection of localised, primary gastrointestinal stromal tumour: A randomised, double-blind, placebo-controlled trial. *The Lancet*, *373*(9669), 1097–1104. https://doi.org/10.1016/S0140-6736(09)60500-6 — PMID 19303137 (PMC2915459) — Erratum: Lancet. 2009 Aug 8;374(9688):450
- Joensuu, H., Eriksson, M., Sundby Hall, K., Hartmann, J. T., Pink, D., Schütte, J., Ramadori, G., Hohenberger, P., Duyster, J., Al-Batran, S.-E., Schlemmer, M., Bauer, S., Wardelmann, E., Sarlomo-Rikala, M., Nilsson, B., Sihto, H., Monge, O. R., Bono, P., Kallio, R., . . . Reichardt, P. (2012). One vs three years of adjuvant imatinib for operable gastrointestinal stromal tumor: A randomized trial. *JAMA*, *307*(12), 1265–1272. https://doi.org/10.1001/jama.2012.347 — PMID 22453568
- Demetri, G. D., van Oosterom, A. T., Garrett, C. R., Blackstein, M. E., Shah, M. H., Verweij, J., McArthur, G., Judson, I. R., Heinrich, M. C., Morgan, J. A., Desai, J., Fletcher, C. D., George, S., Bello, C. L., Huang, X., Baum, C. M., & Casali, P. G. (2006). Efficacy and safety of sunitinib in patients with advanced gastrointestinal stromal tumour after failure of imatinib: A randomised controlled trial. *The Lancet*, *368*(9544), 1329–1338. https://doi.org/10.1016/S0140-6736(06)69446-4 — PMID 17046465
- Demetri, G. D., Reichardt, P., Kang, Y.-K., Blay, J.-Y., Rutkowski, P., Gelderblom, H., Hohenberger, P., Leahy, M., von Mehren, M., Joensuu, H., Badalamenti, G., Blackstein, M., Le Cesne, A., Schöffski, P., Maki, R. G., Bauer, S., Nguyen, B. B., Xu, J., Nishida, T., . . . Casali, P. G. (2013). Efficacy and safety of regorafenib for advanced gastrointestinal stromal tumours after failure of imatinib and sunitinib (GRID): An international, multicentre, randomised, placebo-controlled, phase 3 trial. *The Lancet*, *381*(9863), 295–302. https://doi.org/10.1016/S0140-6736(12)61857-1 — PMID 23177515 (PMC3819942)
- Blay, J.-Y., Serrano, C., Heinrich, M. C., Zalcberg, J., Bauer, S., Gelderblom, H., Schöffski, P., Jones, R. L., Attia, S., D'Amato, G., Chi, P., Reichardt, P., Meade, J., Shi, K., Ruiz-Soto, R., George, S., & von Mehren, M. (2020). Ripretinib in patients with advanced gastrointestinal stromal tumours (INVICTUS): A double-blind, randomised, placebo-controlled, phase 3 trial. *The Lancet Oncology*, *21*(7), 923–934. https://doi.org/10.1016/S1470-2045(20)30168-6 — PMID 32511981 (PMC8383051) — Erratum: Lancet Oncol. 2020 Jul;21(7):e341. doi: 10.1016/S1470-2045(20)30353-3. (PMID 32615117)
- Heinrich, M. C., Jones, R. L., von Mehren, M., Schöffski, P., Serrano, C., Kang, Y.-K., Cassier, P. A., Mir, O., Eskens, F., Tap, W. D., Rutkowski, P., Chawla, S. P., Trent, J., Tugnait, M., Evans, E. K., Lauz, T., Zhou, T., Roche, M., Wolf, B. B., . . . George, S. (2020). Avapritinib in advanced PDGFRA D842V-mutant gastrointestinal stromal tumour (NAVIGATOR): A multicentre, open-label, phase 1 trial. *The Lancet Oncology*, *21*(7), 935–946. https://doi.org/10.1016/S1470-2045(20)30269-2 — PMID 32615108 — Erratum: Lancet Oncol. 2020 Sep;21(9):e418. doi: 10.1016/S1470-2045(20)30489-7. (PMID 32888469)
- Tsai, H.-J., Shan, Y.-S., Yang, C.-Y., Hsiao, C.-F., Tsai, C.-H., Wang, C.-C., Lin, M.-T., Ting, C.-F., Chan, D.-C., Chen, T.-H., Yen, C.-C., Chen, Y.-Y., Lin, H.-Y., Yeh, T.-S., Ho, C.-L., Shieh, T.-Y., Bai, L.-Y., Hsu, J.-T., Chen, I.-S., . . . Yeh, C.-N. (2024). Survival of advanced/recurrent gastrointestinal stromal tumors treated with tyrosine kinase inhibitors in Taiwan: A nationwide registry study. *BMC Cancer*, *24*(1), Article 828. https://doi.org/10.1186/s12885-024-12567-1 — PMID 38992597 (PMC11238460)
- Hu, C.-H., Yeh, C.-N., Chen, J.-S., Tsai, C.-Y., Wang, S.-Y., Cheng, C.-T., & Yeh, T.-S. (2020). Regorafenib treatment outcome for Taiwanese patients with metastatic gastrointestinal stromal tumors after failure of imatinib and sunitinib: A prospective, non-randomized, single-center study. *Oncology Letters*, *20*(3), 2131–2142. https://doi.org/10.3892/ol.2020.11756 — PMID 32782530 (PMC7400021)
- Lin, L.-C., Huang, W.-K., Yen, C.-C., Yang, C.-Y., Sung, M.-T., Wong, N. S., Chua, D. T. T., Lee, S. W. M., Chen, J.-S., & Yeh, C.-N. (2022). Compassionate use of ripretinib for patients with metastatic gastrointestinal stromal tumors: Taiwan and Hong Kong experience. *Frontiers in Oncology*, *12*, Article 883399. https://doi.org/10.3389/fonc.2022.883399 — PMID 35847924 (PMC9277435) — Erratum: Front Oncol. 2022 Oct 13;12:1028118. doi: 10.3389/fonc.2022.1028118. (PMID 36313668)
- Gounder, M., Schöffski, P., Jones, R. L., Agulnik, M., Cote, G. M., Villalobos, V. M., Attia, S., Chugh, R., Chen, T. W.-W., Jahan, T., Loggers, E. T., Gupta, A., Italiano, A., Demetri, G. D., Ratan, R., Davis, L. E., Mir, O., Dileo, P., Van Tine, B. A., . . . Stacchiotti, S. (2020). Tazemetostat in advanced epithelioid sarcoma with loss of INI1/SMARCB1: An international, open-label, phase 2 basket study. *The Lancet Oncology*, *21*(11), 1423–1432. https://doi.org/10.1016/S1470-2045(20)30451-4 — PMID 33035459
- Gounder, M., Ratan, R., Alcindor, T., Schöffski, P., van der Graaf, W. T., Wilky, B. A., Riedel, R. F., Lim, A., Smith, L. M., Moody, S., Attia, S., Chawla, S., D'Amato, G., Federman, N., Merriam, P., Van Tine, B. A., Vincenzi, B., Benson, C., Bui, N. Q., . . . Kasper, B. (2023). Nirogacestat, a γ-secretase inhibitor for desmoid tumors. *The New England Journal of Medicine*, *388*(10), 898–912. https://doi.org/10.1056/NEJMoa2210140 — PMID 36884323 (PMC11225596)
- Tap, W. D., Gelderblom, H., Palmerini, E., Desai, J., Bauer, S., Blay, J.-Y., Alcindor, T., Ganjoo, K., Martín-Broto, J., Ryan, C. W., Thomas, D. M., Peterfy, C., Healey, J. H., van de Sande, M., Gelhorn, H. L., Shuster, D. E., Wang, Q., Yver, A., Hsu, H. H., . . . Wagner, A. J. (2019). Pexidartinib versus placebo for advanced tenosynovial giant cell tumour (ENLIVEN): A randomised phase 3 trial. *The Lancet*, *394*(10197), 478–487. https://doi.org/10.1016/S0140-6736(19)30764-0 — PMID 31229240 (PMC6860022)
- Gelderblom, H., Bhadri, V., Stacchiotti, S., Bauer, S., Wagner, A. J., van de Sande, M., Bernthal, N. M., López Pousa, A., Razak, A. A., Italiano, A., Ahmed, M., Le Cesne, A., Tinoco, G., Boye, K., Martín-Broto, J., Palmerini, E., Tafuto, S., Pratap, S., Powers, B. C., . . . Tap, W. D. (2024). Vimseltinib versus placebo for tenosynovial giant cell tumour (MOTION): A multicentre, randomised, double-blind, placebo-controlled, phase 3 trial. *The Lancet*, *403*(10445), 2709–2719. https://doi.org/10.1016/S0140-6736(24)00885-7 — PMID 38843860 (PMC11740396)
- D'Angelo, S. P., Araujo, D. M., Abdul Razak, A. R., Agulnik, M., Attia, S., Blay, J.-Y., Carrasco Garcia, I., Charlson, J. A., Choy, E., Demetri, G. D., Druta, M., Forcade, E., Ganjoo, K. N., Glod, J., Keedy, V. L., Le Cesne, A., Liebner, D. A., Moreno, V., Pollack, S. M., . . . Van Tine, B. A. (2024). Afamitresgene autoleucel for advanced synovial sarcoma and myxoid round cell liposarcoma (SPEARHEAD-1): An international, open-label, phase 2 trial. *The Lancet*, *403*(10435), 1460–1471. https://doi.org/10.1016/S0140-6736(24)00319-2 — PMID 38554725 (PMC11419333)

## J3. Journal articles — toxicity, supportive care, fertility, survivorship and rehabilitation

- Lo, Y., Shen, L.-J., Chen, W.-H., Dong, Y.-H., & Wu, F.-L. L. (2016). Risk factors of ifosfamide-related encephalopathy in adult patients with cancer: A retrospective analysis. *Journal of the Formosan Medical Association*, *115*(9), 744–751. https://doi.org/10.1016/j.jfma.2015.07.016 — PMID 26302952
- Szabatura, A. H., Cirrone, F., Harris, C., McDonnell, A. M., Feng, Y., Voit, D., Neuberg, D., Butrynski, J., & Fisher, D. C. (2015). An assessment of risk factors associated with ifosfamide-induced encephalopathy in a large academic cancer center. *Journal of Oncology Pharmacy Practice*, *21*(3), 188–193. https://doi.org/10.1177/1078155214527143 — PMID 24664476
- Sweiss, K. I., Beri, R., & Shord, S. S. (2008). Encephalopathy after high-dose ifosfamide: A retrospective cohort study and review of the literature. *Drug Safety*, *31*(11), 989–996. https://doi.org/10.2165/00002018-200831110-00003 — PMID 18840018
- Meanwell, C. A., Blake, A. E., Kelly, K. A., Honigsberger, L., & Blackledge, G. (1986). Prediction of ifosfamide/mesna associated encephalopathy. *European Journal of Cancer & Clinical Oncology*, *22*(7), 815–819. https://doi.org/10.1016/0277-5379(86)90368-8 — PMID 3095121
- Patel, P. N. (2006). Methylene blue for management of ifosfamide-induced encephalopathy. *The Annals of Pharmacotherapy*, *40*(2), 299–303. https://doi.org/10.1345/aph.1G114 — PMID 16391008
- Ajithkumar, T., Parkinson, C., Shamshad, F., & Murray, P. (2007). Ifosfamide encephalopathy. *Clinical Oncology*, *19*(2), 108–114. https://doi.org/10.1016/j.clon.2006.11.003 — PMID 17355105
- Torchia, A., Vari, S., Onesti, C. E., Ceddia, S., Maschio, M., Maggi, G., Riva, F., Faltyn, W., Russillo, M., & Ferraresi, V. (2025). A narrative review on diagnosis and treatment of ifosfamide-induced encephalopathy, the perspective of a EURACAN reference center for sarcomas. *Frontiers in Pharmacology*, *16*, Article 1512966. https://doi.org/10.3389/fphar.2025.1512966 — PMID 40061960 (PMC11885513)
- McDonnell, A. M., Rybak, I., Wadleigh, M., & Fisher, D. C. (2012). Suspected serotonin syndrome in a patient being treated with methylene blue for ifosfamide encephalopathy. *Journal of Oncology Pharmacy Practice*, *18*(4), 436–439. https://doi.org/10.1177/1078155211433231 — PMID 22235061
- Modi, J. N., & Cimino, S. K. (2021). Incidence of ifosfamide induced encephalopathy in patients receiving concomitant fosaprepitant. *Journal of Oncology Pharmacy Practice*, *27*(8), 1891–1895. https://doi.org/10.1177/1078155220971794 — PMID 33166244
- Lentz, K. L., Clark, S. M., Ayarza, M., Liu, B., Morgan, K. P., Wind, L. S., & Hairston, A. (2020). Evaluation of thiamine for the prevention of ifosfamide-induced encephalopathy. *Journal of Oncology Pharmacy Practice*, *26*(2), 406–412. https://doi.org/10.1177/1078155219859644 — PMID 31288633
- Richards, A., Marshall, H., & McQuary, A. (2011). Evaluation of methylene blue, thiamine, and/or albumin in the prevention of ifosfamide-related neurotoxicity. *Journal of Oncology Pharmacy Practice*, *17*(4), 372–380. https://doi.org/10.1177/1078155210385159 — PMID 20861178
- Hensley, M. L., Schuchter, L. M., Lindley, C., Meropol, N. J., Cohen, G. I., Broder, G., Gradishar, W. J., Green, D. M., Langdon, R. J., Mitchell, R. B., Negrin, R., Szatrowski, T. P., Thigpen, J. T., Von Hoff, D., Wasserman, T. H., Winer, E. P., & Pfister, D. G. (1999). American Society of Clinical Oncology clinical practice guidelines for the use of chemotherapy and radiotherapy protectants. *Journal of Clinical Oncology*, *17*(10), 3333–3355. https://doi.org/10.1200/JCO.1999.17.10.3333 — PMID 10506637
- Hensley, M. L., Hagerty, K. L., Kewalramani, T., Green, D. M., Meropol, N. J., Wasserman, T. H., Cohen, G. I., Emami, B., Gradishar, W. J., Mitchell, R. B., Thigpen, J. T., Trotti, A., von Hoff, D., & Schuchter, L. M. (2009). American Society of Clinical Oncology 2008 clinical practice guideline update: Use of chemotherapy and radiation therapy protectants. *Journal of Clinical Oncology*, *27*(1), 127–145. https://doi.org/10.1200/JCO.2008.17.2627 — PMID 19018081
- Stöhr, W., Paulides, M., Bielack, S., Jürgens, H., Treuner, J., Rossi, R., Langer, T., & Beck, J. D. (2007). Ifosfamide-induced nephrotoxicity in 593 sarcoma patients: A report from the Late Effects Surveillance System. *Pediatric Blood & Cancer*, *48*(4), 447–452. https://doi.org/10.1002/pbc.20858 — PMID 16628552
- Stöhr, W., Patzer, L., Paulides, M., Kremers, A., Beck, J.-D., Langer, T., & Rossi, R. (2007). Growth impairment after ifosfamide-induced nephrotoxicity in children. *Pediatric Blood & Cancer*, *48*(5), 571–576. https://doi.org/10.1002/pbc.20920 — PMID 16755549
- Skinner, R., Cotterill, S. J., & Stevens, M. C. (2000). Risk factors for nephrotoxicity after ifosfamide treatment in children: A UKCCSG Late Effects Group study. United Kingdom Children's Cancer Study Group. *British Journal of Cancer*, *82*(10), 1636–1645. https://doi.org/10.1054/bjoc.2000.1214 — PMID 10817497 (PMC2374517)
- Ensergueix, G., Pallet, N., Joly, D., Levi, C., Chauvet, S., Trivin, C., Augusto, J.-F., Boudet, R., Aboudagga, H., Touchard, G., Nochy, D., Essig, M., Thervet, E., Lazareth, H., & Karras, A. (2020). Ifosfamide nephrotoxicity in adult patients. *Clinical Kidney Journal*, *13*(4), 660–665. https://doi.org/10.1093/ckj/sfz183 — PMID 32897279 (PMC7467602)
- Kooijmans, E. C. M., Mulder, R. L., Marks, S. D., Pavasovic, V., Motwani, S. S., Walwyn, T., Larkins, N. G., Kruseova, J., Constine, L. S., Wallace, W. H., Green, D. M., Bökenkamp, A., van der Pal, H. J. H., van den Heuvel-Eibrink, M. M., Hjorth, L., Andrés-Jensen, L., Bardi, E., van Dalen, E. C., Demoor-Goldschmidt, C., . . . Ehrhardt, M. J. (2025). Nephrotoxicity surveillance for childhood and young adult survivors of cancer: Recommendations from the International Late Effects of Childhood Cancer Guideline Harmonization Group. *Journal of Clinical Oncology*, *43*(21), 2433–2448. https://doi.org/10.1200/JCO-24-02534 — PMID 40393013
- Swain, S. M., Whaley, F. S., & Ewer, M. S. (2003). Congestive heart failure in patients treated with doxorubicin: A retrospective analysis of three trials. *Cancer*, *97*(11), 2869–2879. https://doi.org/10.1002/cncr.11407 — PMID 12767102
- Asselin, B. L., Devidas, M., Chen, L., Franco, V. I., Pullen, J., Borowitz, M. J., Hutchison, R. E., Ravindranath, Y., Armenian, S. H., Camitta, B. M., & Lipshultz, S. E. (2016). Cardioprotection and safety of dexrazoxane in patients treated for newly diagnosed T-cell acute lymphoblastic leukemia or advanced-stage lymphoblastic non-Hodgkin lymphoma: A report of the Children's Oncology Group randomized trial Pediatric Oncology Group 9404. *Journal of Clinical Oncology*, *34*(8), 854–862. https://doi.org/10.1200/JCO.2015.60.8851 — PMID 26700126 (PMC4872007) — Erratum: J Clin Oncol. 2017 Jun 20;35(18):2100. doi: 10.1200/JCO.2017.73.9433. (PMID 28618244)
- Cranmer, L. D., Hess, L. M., Sugihara, T., & Muntz, H. G. (2023). Cardiac events among patients with sarcoma treated with doxorubicin by method of infusion: A real-world database study. *Cancer Reports*, *6*(1), Article e1681. https://doi.org/10.1002/cnr2.1681 — PMID 35852051 (PMC9875654)
- Mouridsen, H. T., Langer, S. W., Buter, J., Eidtmann, H., Rosti, G., de Wit, M., Knoblauch, P., Rasmussen, A., Dahlstrøm, K., Jensen, P. B., & Giaccone, G. (2007). Treatment of anthracycline extravasation with Savene (dexrazoxane): Results from two prospective clinical multicentre studies. *Annals of Oncology*, *18*(3), 546–550. https://doi.org/10.1093/annonc/mdl413 — PMID 17185744
- Grosso, F., Dileo, P., Sanfilippo, R., Stacchiotti, S., Bertulli, R., Piovesan, C., Jimeno, J., D'Incalci, M., Gescher, A., & Casali, P. G. (2006). Steroid premedication markedly reduces liver and bone marrow toxicity of trabectedin in advanced sarcoma. *European Journal of Cancer*, *42*(10), 1484–1490. https://doi.org/10.1016/j.ejca.2006.02.010 — PMID 16737808
- Grosso, F., D'Incalci, M., Cartoafa, M., Nieto, A., Fernández-Teruel, C., Alfaro, V., Lardelli, P., Roy, E., Gómez, J., Kahatt, C., Soto-Matos, A., & Judson, I. (2012). A comprehensive safety analysis confirms rhabdomyolysis as an uncommon adverse reaction in patients treated with trabectedin. *Cancer Chemotherapy and Pharmacology*, *69*(6), 1557–1565. https://doi.org/10.1007/s00280-012-1864-4 — PMID 22484722 (PMC3362698)
- Kubo, T., Yasaka, K., & Kobayashi, H. (2024). Differences in the incidence of sterile inflammation after trabectedin infusion with two central venous port systems: A retrospective study. *Cureus*, *16*(4), Article e57507. https://doi.org/10.7759/cureus.57507 — PMID 38707007 (PMC11066724)
- Martella, F., Salutari, V., Marchetti, C., Pisano, C., Di Napoli, M., Pietta, F., Centineo, D., Caringella, A. M., Musella, A., & Fioretto, L. (2015). A retrospective analysis of trabectedin infusion by peripherally inserted central venous catheters: A multicentric Italian experience. *Anti-Cancer Drugs*, *26*(9), 990–994. https://doi.org/10.1097/CAD.0000000000000275 — PMID 26241804
- Bekaii-Saab, T. S., Ou, F.-S., Ahn, D. H., Boland, P. M., Ciombor, K. K., Heying, E. N., Dockter, T. J., Jacobs, N. L., Pasche, B. C., Cleary, J. M., Meyers, J. P., Desnoyers, R. J., McCune, J. S., Pedersen, K., Barzi, A., Chiorean, E. G., Sloan, J., Lacouture, M. E., Lenz, H.-J., & Grothey, A. (2019). Regorafenib dose-optimisation in patients with refractory metastatic colorectal cancer (ReDOS): A randomised, multicentre, open-label, phase 2 study. *The Lancet Oncology*, *20*(8), 1070–1082. https://doi.org/10.1016/S1470-2045(19)30272-4 — PMID 31262657 (PMC9187307)
- Smith, T. J., Bohlke, K., Lyman, G. H., Carson, K. R., Crawford, J., Cross, S. J., Goldberg, J. M., Khatcheressian, J. L., Leighl, N. B., Perkins, C. L., Somlo, G., Wade, J. L., Wozniak, A. J., & Armitage, J. O. (2015). Recommendations for the use of WBC growth factors: American Society of Clinical Oncology clinical practice guideline update. *Journal of Clinical Oncology*, *33*(28), 3199–3212. https://doi.org/10.1200/JCO.2015.62.3488 — PMID 26169616
- Aapro, M. S., Bohlius, J., Cameron, D. A., Dal Lago, L., Donnelly, J. P., Kearney, N., Lyman, G. H., Pettengell, R., Tjan-Heijnen, V. C., Walewski, J., Weber, D. C., & Zielinski, C. (2011). 2010 update of EORTC guidelines for the use of granulocyte-colony stimulating factor to reduce the incidence of chemotherapy-induced febrile neutropenia in adult patients with lymphoproliferative disorders and solid tumours. *European Journal of Cancer*, *47*(1), 8–32. https://doi.org/10.1016/j.ejca.2010.10.013 — PMID 21095116
- Oktay, K., Harvey, B. E., Partridge, A. H., Quinn, G. P., Reinecke, J., Taylor, H. S., Wallace, W. H., Wang, E. T., & Loren, A. W. (2018). Fertility preservation in patients with cancer: ASCO clinical practice guideline update. *Journal of Clinical Oncology*, *36*(19), 1994–2001. https://doi.org/10.1200/JCO.2018.78.1914 — PMID 29620997
- Lambertini, M., Peccatori, F. A., Demeestere, I., Amant, F., Wyns, C., Stukenborg, J.-B., Paluch-Shimon, S., Halaska, M. J., Uzan, C., Meissner, J., von Wolff, M., Anderson, R. A., & Jordan, K. (2020). Fertility preservation and post-treatment pregnancies in post-pubertal cancer patients: ESMO Clinical Practice Guidelines†. *Annals of Oncology*, *31*(12), 1664–1678. https://doi.org/10.1016/j.annonc.2020.09.006 — PMID 32976936
- Green, D. M., Nolan, V. G., Goodman, P. J., Whitton, J. A., Srivastava, D., Leisenring, W. M., Neglia, J. P., Sklar, C. A., Kaste, S. C., Hudson, M. M., Diller, L. R., Stovall, M., Donaldson, S. S., & Robison, L. L. (2014). The cyclophosphamide equivalent dose as an approach for quantifying alkylating agent exposure: A report from the Childhood Cancer Survivor Study. *Pediatric Blood & Cancer*, *61*(1), 53–67. https://doi.org/10.1002/pbc.24679 — PMID 23940101 (PMC3933293)
- Williams, D., Crofton, P. M., & Levitt, G. (2008). Does ifosfamide affect gonadal function? *Pediatric Blood & Cancer*, *50*(2), 347–351. https://doi.org/10.1002/pbc.21323 — PMID 17973323
- Racano, A., Pazionis, T., Farrokhyar, F., Deheshi, B., & Ghert, M. (2013). High infection rate outcomes in long-bone tumor surgery with endoprosthetic reconstruction in adults: A systematic review. *Clinical Orthopaedics and Related Research*, *471*(6), 2017–2027. https://doi.org/10.1007/s11999-013-2842-9 — PMID 23404421 (PMC3706642)
- Prophylactic Antibiotic Regimens in Tumor Surgery (PARITY) Investigators, Ghert, M., Schneider, P., Guyatt, G., Thabane, L., Vélez, R., O'Shea, T., Randall, R. L., Turcotte, R., Wilson, D., Wunder, J. S., Baptista, A. M., Cheng, E. Y., Doung, Y.-C., Ferguson, P. C., Giglio, V., Hayden, J., Heels-Ansdell, D., Khan, S. A., . . . Bhandari, M. (2022). Comparison of prophylactic intravenous antibiotic regimens after endoprosthetic reconstruction for lower extremity bone tumors: A randomized clinical trial. *JAMA Oncology*, *8*(3), 345–353. https://doi.org/10.1001/jamaoncol.2021.6628 — PMID 34989778 (PMC8739829)
- Henderson, E. R., Groundland, J. S., Pala, E., Dennis, J. A., Wooten, R., Cheong, D., Windhager, R., Kotz, R. I., Mercuri, M., Funovics, P. T., Hornicek, F. J., Temple, H. T., Ruggieri, P., & Letson, G. D. (2011). Failure mode classification for tumor endoprostheses: Retrospective review of five institutions and a literature review. *The Journal of Bone and Joint Surgery. American Volume*, *93*(5), 418–429. https://doi.org/10.2106/JBJS.J.00834 — PMID 21368074
- van Kouswijk, H. W., van Keeken, H. G., Ploegmakers, J. J. W., Seeber, G. H., & van den Akker-Scheek, I. (2023). Therapeutic validity and effectiveness of exercise interventions after lower limb-salvage surgery for sarcoma: A systematic review. *BMC Musculoskeletal Disorders*, *24*(1), Article 216. https://doi.org/10.1186/s12891-023-06315-y — PMID 36949467 (PMC10035240)
- Groundland, J. S., Ambler, S. B., Houskamp, L. D. J., Orriola, J. J., Binitie, O. T., & Letson, G. D. (2016). Surgical and functional outcomes after limb-preservation surgery for tumor in pediatric patients: A systematic review. *JBJS Reviews*, *4*(2), Article e2. https://doi.org/10.2106/JBJS.RVW.O.00013 — PMID 27490132
- Quinn, G. P., Gonçalves, V., Sehovic, I., Bowman, M. L., & Reed, D. R. (2015). Quality of life in adolescent and young adult cancer patients: A systematic review of the literature. *Patient Related Outcome Measures*, *6*, 19–51. https://doi.org/10.2147/PROM.S51658 — PMID 25733941 (PMC4337625)
- Mei, J., Zhu, X.-Z., Wang, Z.-Y., & Cai, X.-S. (2014). Functional outcomes and quality of life in patients with osteosarcoma treated with amputation versus limb-salvage surgery: A systematic review and meta-analysis. *Archives of Orthopaedic and Trauma Surgery*, *134*(11), 1507–1516. https://doi.org/10.1007/s00402-014-2086-5 — PMID 25234150

## J4. Local working files (for the editor)
- TFDA download: `/tmp/claude-0/-home-user-oncology-educater/6a66dc7f-55e5-547a-b95f-33d6978992bf/scratchpad/s4_dl/tfda/x/36_2.csv`
- openFDA label JSON: `/tmp/claude-0/-home-user-oncology-educater/6a66dc7f-55e5-547a-b95f-33d6978992bf/scratchpad/s4_dl/lbl/`
- PubMed records (JSON per PMID): `/tmp/claude-0/-home-user-oncology-educater/6a66dc7f-55e5-547a-b95f-33d6978992bf/scratchpad/s4_dl/pm/`
