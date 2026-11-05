# Breast 1. Taiwan epidemiology, screening, hereditary risk, pathology and biomarkers, genomic assays, staging: fact-check report

Fact-check date: 2026-10-29. Prepared for the Taiwanese oncology NP (專科護理師) handbook, breast cancer chapter (ward practice and 專師甄審).

Confidence tags:
- **[VERIFIED]**: confirmed in a primary or official source that I opened (journal abstract or PMC full text, official government page or dataset, FDA label, TFDA licence dataset, nccn.org page or NCCN Guidelines for Patients PDF).
- **[PARTIAL]**: confirmed only in a secondary source, or only part of the claim could be confirmed.
- **[UNVERIFIED]**: could not be confirmed. Do not print without checking.

Values I calculated myself are marked "(computed)". Source tags inline: [A] = PubMed abstract; [FT] = PMC full text (or its supplementary file); [DS] = official dataset or report I downloaded and parsed; [L] = FDA label (openFDA JSON); [TFDA] = TFDA licence dataset (InfoId=36, copy downloaded 2026-10-29).

Method:
- PubMed records were pulled through NCBI E-utilities (the same database as the PubMed MCP tools). Full texts and supplements came from PMC / Europe PMC.
- Taiwan data were downloaded directly from twcr.tw and mohw.gov.tw. (The mohw.gov.tw server omits its TWCA intermediate certificate; I added the issuer certificate from its AIA URL to a local CA bundle instead of disabling verification.)
- NCCN versions came from nccn.org category pages, read 2026-10-29. The NCCN professional PDFs need a login, so NCCN wording comes from the NCCN Guidelines for Patients 2026 (Invasive Breast Cancer, based on professional v2.2026; Metastatic Breast Cancer, based on v3.2026; Genetic Testing for Hereditary Breast, Ovarian, Pancreatic and Prostate Cancers, based on Genetic/Familial High-Risk Assessment: BOPP v3.2026).
- ascopubs.org (JCO full texts) and the Arch Pathol Lab Med site returned HTTP 403. ASCO/CAP wording beyond the abstracts therefore comes from peer-reviewed reproductions.

---

## 0. Corrections and flags for the editor (read first)

1. **Two different official ASRs for the same year.** For 2023 female breast cancer, MOHW gives **91.2 per 100,000** (17,779 cases); the TCR yearly workbook gives **91.99**. For 2022, MOHW gives 17,366 cases, but the revised TCR workbook now gives **17,539**. Quote "MOHW 112年 report: 17,779 cases, ASR 91.2" and do not mix in workbook numbers.
2. **The ASR fell slightly in 2023** (91.2 vs 92.0 in 2022, −0.8, MOHW), even though case numbers rose (+413). Do not write "incidence keeps rising every year".
3. **Breast cancer is No. 1 in women but No. 3 overall.** By new cases (both sexes), breast is 3rd (after lung 19,986 and colorectal 19,074). Among women it is 1st by both count and ASR.
4. **Age peak is a plateau, not a single "45–49 peak".** In 2019–2023 TCR age-specific rates, 45–49 (248.7/10⁵) and **60–64 (254.4/10⁵, the highest band)** are almost equal. Every band from 45 to 69 is 236–254, and 70–84 still stays above 196. MOHW itself says 「發生高峰為45歲至69歲」.
5. **2025 screening expansion is real and verified.** Since **2025-01-01 (114年)**, free biennial mammography covers **all women 40–74** (previously 45–69, plus 40–44 only with a family history in a 2nd-degree relative). The family-history criterion is therefore no longer needed for ages 40–44. One MOHW release (2025-06-06) misprints the new band as "40至45歲".
6. **Two different MOHW "early-stage" figures for screen-detected cancers.** One release says **59.7%** of 2023 screen-detected cancers were stage 0–I (screening programme data). Two later releases cite the 112年 registry: **62.9%** stage 0+I if screen-detected vs **34.9%** if not screen-detected. Cite each with its source.
7. **Hereditary fraction differs inside NCCN's own patient guides.** The 2026 Invasive Breast Cancer guide says "about 1 out of 20" breast cancers are hereditary. The 2026 Genetic Testing guide says "about 1 in 10". Prefer "5–10%" with both cited, or avoid a single number.
8. **NCCN germline-testing threshold is age ≤50, not ≤65.** In NCCN (patient guide v3.2026), testing is *recommended* for breast cancer diagnosed ≤50 and *may be considered* for 51–65. **ASCO–SSO 2024** is broader: *offer* BRCA1/2 testing to **all** newly diagnosed patients ≤65. Do not merge the two.
9. **HER2-ultralow is not an ASCO/CAP category.** The 2023 ASCO/CAP update affirmed the 2018 rules and called new categories (HER2-low, HER2-ultralow) "premature". "Ultralow" comes from DESTINY-Breast06 and the FDA/TFDA labels: IHC 0 **with** membrane staining in **>0 and ≤10%** of tumour cells (FDA). TFDA Chinese terms: HER2弱陽性 = HER2-low; HER2微陽性 = HER2-ultralow.
10. **ESR1 testing is no longer only "at progression".** The ASCO 2023 rapid update recommends ctDNA ESR1 testing at recurrence or progression, with retesting at each later progression. Since **2026-09-04**, however, FDA-approved **camizestrant (Etcamah)** is used on **ESR1 detection during first-line AI + CDK4/6 inhibitor before radiological progression**: ctDNA every 3 months after ≥6 months of therapy (SERENA-6). Camizestrant is **not** in the TFDA dataset.
11. **Specimen differs by drug label.**
    - Capivasertib (PIK3CA/AKT1/PTEN): **tumour tissue** only.
    - Alpelisib: tissue **or** plasma; if plasma is negative, test tissue.
    - Inavolisib: plasma.
    - ESR1 drugs (elacestrant, imlunestrant, vepdegestrant, camizestrant): **plasma**.
12. **RxPONDER nuance (2026).** Among women <55 in RxPONDER, chemotherapy benefit was confined to those with **AMH ≥10 pg/mL** (normal ovarian reserve). AMH predicted benefit better than menopausal status. This is a research finding, not yet a guideline cut-off.
13. **AJCC edition.** Breast is **still AJCC 8th edition** on the AJCC "Current Staging System 2026" chart; there is no Version 9 for breast. Whether the Taiwan registry reports anatomic or prognostic stage for breast was not stated in the 112年 long-form report: [UNVERIFIED].
14. **Not found or not openable (marked [UNVERIFIED] below):**
    - official national in-situ (DCIS) count for 2023 (only the long-form hospital database was available)
    - a single nationwide Taiwanese subtype distribution for all stages (only age-stratified early-stage TCR data, 2007–2017)
    - NHI payment rules for PIK3CA/ESR1 testing
    - the NCCN professional Oncotype/MammaPrint algorithm wording
    - Nottingham grade sum cut-offs in a primary source

---

## 1. Taiwan epidemiology

### 1.1 Incidence: Taiwan Cancer Registry, data year 2023 (民國112年) [VERIFIED; DS]

2023 is the latest registry year. MOHW announced it on **2025-12-30** (press release 「公布112年國人癌症登記資料分析結果 守護健康未來 從癌症篩檢開始」, filed 114-12-30, updated 115-01-05; https://mohw.gov.tw/cp-2704-84987-1.html, attachment 附表/附圖 https://www.mohw.gov.tw/dl-98499-cd0fe70e-8e08-42cc-be15-3860b40d7f4d.html).

| Item (2023, female breast 女性乳房, invasive only) | Value | Source |
|---|---|---|
| New cases | **17,779** (2022: 17,366; +413) | MOHW 附表 |
| Rank by new cases, both sexes | **3rd** (lung 19,986; colorectal 19,074) | MOHW 附表 |
| Rank among women | **1st by count and by ASR** (next: lung 9,707 cases, 42.4/10⁵) | MOHW 附圖 |
| ASR (2000 WHO world standard, per 100,000 women) | **91.2** (2022: 92.0; change −0.8) | MOHW 附表 |
| Median age at diagnosis | **57 years** (same as 2022) | MOHW 附表 and press text ("子宮體癌及乳癌為57歲") |
| Age-standardized death rate shown in the same table | 13.3/10⁵ women (2023 deaths) | MOHW 附表 |
| Share of all 138,051 new cancers | 12.9% (computed) | |
| Share of 66,807 new cancers in women | **26.6%** (computed; about 1 in 4) | |

- Note: the MOHW registry figures exclude carcinoma in situ (「不含原位癌」).
- MOHW press text: 「十大癌症新發生人數(男女合計)依序為(1)肺癌(2)大腸癌(3)女性乳癌…」; women's ASR order 「乳癌、肺癌、大腸癌、甲狀腺癌、子宮體癌…」.

**TCR yearly workbook (same year, invasive, mid-year population, 2000 WHO world standard)** [DS]
- Source: https://twcr.tw/wp-content/uploads/2026/01/Year_Breast_2023.xlsx, sheets 174_YEAR_data and 175_YEAR_data.

| Year | Female cases | ASR (/10⁵) |
|---|---|---|
| 1980 | 789 | 12.96 |
| 2000 | 4,679 | 40.51 |
| 2010 | 9,835 | 65.03 |
| 2015 | 12,581 | 74.88 |
| 2020 | 15,442 | 83.44 |
| 2022 | 17,539 | 93.18 |
| 2023 | 17,779 | 91.99 |

- The ASR has more than doubled since 2000 (40.5 → 92.0).
- **Male breast cancer, 2023:** 67 cases; ASR 0.16/10⁵ [DS].

**Age-specific incidence, 2019–2023, women (per 100,000)** [DS]
- Source: TCR Period_Breast_2023.xlsx, sheet 174_AGE_data. https://twcr.tw/wp-content/uploads/2026/01/Period_Breast_2023.xlsx

Values read directly from the file (bands under 30: 15–19 0.15, 20–24 1.50, 25–29 11.90):

| 30–34 | 35–39 | 40–44 | 45–49 | 50–54 | 55–59 | 60–64 | 65–69 | 70–74 | 75–79 | 80–84 | 85+ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 35.92 | 83.58 | 162.96 | **248.68** | 235.99 | 242.03 | **254.42** | 250.86 | 218.64 | 217.82 | 196.45 | 146.04 |

- Teaching point: the rate climbs steeply from age 35 to 49, then stays on a plateau of about 236–254 per 100,000 from 45 to 69. The single highest band is **60–64 (254.42)**.
- Rates rose in every band ≥45 compared with 2009–2013. For example, 45–49 went from 187.71 to 248.68, and 60–64 from 195.87 to 254.42.
- MOHW (2024-09-05 release) states 「乳癌發生高峰為45歲至69歲」 [VERIFIED].

### 1.2 Stage, DCIS, histology and first-course treatment: 2023 long-form database (長表) [VERIFIED; DS]

Source: Taiwan Cancer Registry Center, 112年癌症登記長表 annual report (CA17_LF112.pdf), 表十四之一 and 表十四之二, pp. 102–105. https://twcr.tw/wp-content/uploads/2025/12/CA17_LF112.pdf

Caveats:
- Long-form hospitals only (106 hospitals reporting in 112年).
- **Includes carcinoma in situ.** Analysable n = **20,493** (women 20,420; men 73). This is not the official invasive count of 17,779.
- Staging: AJCC 8th edition; combined stage (整併期別) merges clinical and pathological stage.

**Combined stage (整併期別), all n = 20,493**

| Stage | All | Women | Medical centres | Non-medical centres |
|---|---|---|---|---|
| 0 | **16.53%** | 16.54% | 17.05% | 15.72% |
| I | **31.87%** (IA 6,333; IB 199) | 31.90% | 32.37% | 31.11% |
| II | **32.57%** (IIA 4,276; IIB 2,398) | 32.55% | 31.93% | 33.55% |
| III | 10.69% | 10.68% | 10.45% | 11.07% |
| IV | **7.32%** | 7.32% | 7.27% | 7.42% |
| Unknown | 1.01% | 1.01% | 0.94% | 1.13% |

- Stage 0 + I = 48.4% of women; stage III + IV = 18.0% (computed).
- Clinical stage IV alone: 7.10%. Kappa for clinical–pathological stage agreement: 0.6102.

**DCIS and other in-situ disease** [VERIFIED; DS]
- In-situ histology (all sexes): 管道內癌 (DCIS) **3,120**; 小葉原位癌 (LCIS) 131; 乳突狀原位癌 224; other specified 16; NOS 9.
- Total in situ 3,500 (computed) = **17.1%** of all long-form breast cases (computed). **DCIS alone = 15.2%** (3,120/20,493; computed). DCIS is 89.1% of in-situ cases (table).
- Stage 0 count (3,387) is lower than all in-situ cases (3,500). This is consistent with AJCC 8th edition no longer staging LCIS as Tis (Tis = DCIS and Paget disease only). [PARTIAL: the AJCC rule is from secondary knowledge; the counts are verified]
- **No official national (all-hospital) count of in-situ breast cancer for 2023 was found** in the MOHW release or TCR workbooks, which report invasive cancers only. [UNVERIFIED]

**Invasive histology, all sexes (n = 16,993 invasive, computed)**
- Invasive carcinoma NST (ductal): 14,519 (**85.44%**)
- Invasive lobular: 942 (**5.54%**)
- Mucinous: 554 (3.26%)
- Invasive papillary: 380 (2.24%)
- Metaplastic: 107 (0.63%)
- Paget disease: 29 (0.17%)
- Other / NOS: about 2.7%

**Age distribution, women (n = 20,420)**
- Largest 5-year band: 45–49 (15.32%).
- Age <50: 31.0% (computed). Age ≥70: 16.5% (computed).

**First-course treatment highlights (n = 20,493)**
- BCS + RT + endocrine therapy is the most common single pattern: 5,334 (26.03%).
- Mastectomy + endocrine therapy: 2,371 (11.57%).
- Palliative care only: 39 (0.19%).
- Stage IV: chemotherapy + targeted therapy 18.19%; targeted + endocrine 20.19%; "other" combinations 22.32%.

### 1.3 Survival: TCR, cases diagnosed 2019–2023, followed to 2024 [VERIFIED; DS]

Source: 台灣10大癌症108-112年新發個案存活率（追蹤至113年）, https://twcr.tw/wp-content/uploads/2025/12/Survival_108_112.pdf (invasive cancers only).

| Female breast | 1-yr | 3-yr | 5-yr |
|---|---|---|---|
| Observed survival | 96.7% | 90.5% | **85.5%** |
| Relative survival | 97.5% | 92.7% | **88.9%** |

- For comparison: all cancers in women, 5-year relative survival 70.1%.
- MOHW releases (2025-03-03, 2025-06-06) quote stage-specific survival from 107–111年 data: early breast cancer **>99%** 5-year survival vs about **39.2%** when found late. [VERIFIED as MOHW statement; I did not see the underlying stage table]

### 1.4 Mortality: MOHW cause-of-death statistics, data year 2025 (民國114年) [VERIFIED; DS]

Released **2026-06-22**. Sources:
- press release 「國人死亡人數連續3年下降…」 https://mohw.gov.tw/cp-16-86970-1.html
- analysis PDF 「114年死因統計結果分析」 https://www.mohw.gov.tw/dl-100915-0a572340-fabe-4a89-a8a0-199640a9053d.html (section 二(二)–(四), Table 3, Table 6)
- summary workbook 摘要表.xlsx, 表13 https://www.mohw.gov.tw/dl-100920-e5938c74-aa2a-4994-a15c-054787318303.html

| Item (2025; ICD-10 C50, women) | Value |
|---|---|
| Deaths | **3,116** (2024: 3,050; +2.2%, computed) |
| Rank among cancer deaths in women | **2nd** (after lung, 4,158) |
| Rank among all cancer deaths (both sexes, by rate) | **4th** |
| Crude death rate | 26.3 per 100,000 women |
| Age-standardized death rate (2000 WHO world) | **13.1** (2024: 13.2; 2023: 13.3) |
| Share of 22,301 female cancer deaths | **13.97%** |
| Median age at death | **65 years** (all cancers: 71) |

- MOHW: 「可篩檢癌症死因中，女性乳癌、口腔癌、胃癌標準化死亡率較113年下降」.
- MOHW: the median age at death is below the all-cancer median for breast (65), oral, oesophageal and ovarian cancer (64).
- 10-year change: female breast crude rate rose from 18.9 (2015, adjusted value) to 26.3 (2025), while the ASMR stayed flat at 12.2–13.8 throughout 2015–2025 (Table 6, conversion-adjusted values). The rising crude rate reflects population ageing, not a higher age-specific risk of dying.
- Teaching ratio: 2025 deaths are about 18% of 2023 new invasive cases (computed; different years), compared with about 93% for pancreas.

### 1.5 Taiwan subtype distribution

**No single official nationwide subtype distribution (all stages) was found** in MOHW or TCR public reports [UNVERIFIED]. The best published national data are below.

**(a) TCR 2007–2017, early breast cancer (stages 0–III, n = 71,928), by age** [VERIFIED; FT, Supplementary Table 2 of Huang & Tseng 2025]

| Age (y) | HR+/HER2+ | HR+/HER2− | HR−/HER2+ | HR−/HER2− (TN) | Any HER2+ (computed) |
|---|---|---|---|---|---|
| 20–29 | 18.8% | 60.9% | 6.2% | **14.1%** | 25.0% |
| 30–39 | 19.1% | 64.5% | 7.2% | 9.3% | 26.3% |
| 40–49 | 17.5% | **68.9%** | 6.8% | **6.8%** | 24.3% |
| 50–59 | 18.1% | 59.6% | **12.2%** | 10.1% | **30.3%** |
| 60–69 | 15.5% | 64.3% | 10.5% | 9.8% | 26.0% |
| 70–79 | 12.7% | 67.0% | 8.9% | 11.4% | 21.6% |
| 80–89 | 10.9% | 69.3% | 8.3% | 11.6% | 19.2% |
| ≥90 | 9.3% | 75.9% | 4.6% | 10.2% | 13.9% |

- The supplement labels the 70–79 row "70–70" (typo).
- Approximate ranges to teach: **HR+/HER2− 60–76%; HER2-positive (HR+ or HR−) 14–30%; triple-negative 7–14%** (computed from the table).
- Whole-cohort proxy from the main text: HR+ cases n = 58,461 and HER2+ cases n = 19,854 out of 71,928 early cancers, i.e. about **81% HR+** and **28% HER2+** (computed). [PARTIAL: denominators may include unknown-status cases]
- Other findings: TN is most frequent in women in their 20s, and HR+/HER2− rises with age. Women ≤40 were 12% of cases at the start and 8% at the end of 2007–2017; only 34% of cases were <50 years.
- Unlike the West, young Taiwanese patients have **more** luminal disease. In an NTUH series (2004–2006, n = 1,028), patients ≤50 vs >50 had luminal A 67% vs 57% and basal-like 9% vs 17% (Lin 2009) [VERIFIED; A].

**(b) HER2-low in Taiwan** [VERIFIED]
- TCR 2011–2020, stage 0–III HER2-negative cancers treated with upfront surgery (n = 38,773): **HER2-low 65.4%** (IHC 1+ 16,387; IHC 2+/ISH− 8,960) and HER2-zero 34.6% (IHC 0 13,426). HER2-low was 66.9% among HR+ and 56.9% among HR− cancers (Chen 2026) [FT].
- Metastatic HER2-negative cancers (2017–2020), slides re-scored: HER2-low **61.2%** (186/304); agreement with the original score 90.1% (Lee 2025) [A].

**(c) Context.** HR+/HER2−, node-positive high-risk early breast cancer was 10.4% of all early breast cancers in Taiwan, 2012–2018 (Tang 2024) [A].

---

## 2. Taiwan mammography screening programme (乳房X光攝影檢查)

### 2.1 Eligibility and its history [VERIFIED]

| Period | Eligible women (free, every 2 years) | Source |
|---|---|---|
| 2004 | 50–69 | Yao 2023 [A] |
| 2009 | 45–69 (mobile units added 2010) | Yao 2023 [A] |
| to 2024 | **45–69** (「45歲以上至未滿70歲」), plus **40–44 with a family history** of breast cancer in 祖母、外婆、母親、女兒、姊妹 (i.e. up to 2nd-degree relatives) | MOHW 2024-09-05 (cp-2704-79842) |
| **from 2025-01-01 (114年)** | **All women 40–74** (「40歲以上未滿75歲」 = 40–74), every 2 years; no family-history requirement | MOHW 2024-09-05 (announcing); 2025-03-03 「乳癌篩檢年齡擴大至40-74歲婦女」 (cp-16-81672); 2025-12-30 registry release; 2026-09-17 (cp-16-88006) |

- Test: **mammography only.** MOHW explains that breast ultrasound is less sensitive for calcifications and operator-dependent, so it is used for follow-up diagnosis, not as the publicly funded screening test (2025-03-03 release).
- Access: present the NHI card at an HPA-approved 「乳房X光攝影醫療機構」; eligibility can be checked in the 健保快易通／健康存摺 app (2026-09-17 release).
- No 2026 change to ages or interval was found in MOHW releases up to 2026-09-17. No publicly funded supplemental ultrasound for dense breasts and no programme for under-40s with a family history was found. [VERIFIED for the releases read; absence not proven]
- Exam tips quoted by MOHW: avoid the swollen premenstrual days; wear two-piece clothing; no deodorant, powder or cream on the breasts or axillae; the exam takes about 15 minutes; a female radiographer performs it.

### 2.2 Programme yield and performance

| Year / item | Value | Source |
|---|---|---|
| 2023 (112年) | 923,000 screened; **5,392** cancers found; "about 1 cancer per **169** women screened"; **59.7%** of screen-detected cancers were stage 0+I | MOHW 2024-09-05 [VERIFIED] (my calculation from the rounded figures gives 1 per 171) |
| Never screened (2024 statement) | about **34.5%** of eligible women 45–69 had never had a mammogram | MOHW 2024-09-05 [VERIFIED] |
| 2024 (113年) | **916,000** screens; 2-year screening rate **39.8%**; **5,250** cancers | MOHW 2025-03-03 [VERIFIED] |
| 2025 to 28 May | about 660,000 screens; 23.7% from the new age groups | MOHW 2025-06-06 [VERIFIED] |
| 2025 to mid-September | **1.04 million** screens (first time over 1 million; +33.57% year on year); new 40–44 and 70–74 groups about 262,000 (25.15%) | MOHW 2025-09-30 [VERIFIED] |
| 2025 full year | **1.26 million** screened (+36.3%); new age groups about **326,000 (25.9%)** | MOHW 2026-03-02 [VERIFIED] |
| Stage at diagnosis, 2023 registry | screen-detected **62.9%** stage 0+I vs **34.9%** if not screen-detected | MOHW 2026-03-02 and 2026-09-17 [VERIFIED] |
| Programme performance, 2004–2020 (8,169,869 exams; 3,665,078 women) | cancer detection rate **4.76 per 1,000** (2004–2009) and **4.08 per 1,000** (2010–2020); recall rate **9.90% → 8.15%**; participation 3.9% (2004) → 40% (2019); 10-year survival 89.68% → 97.33% | Yao 2023 [VERIFIED; A] |
| Pre-diagnosis screening | 47.6% of 50,831 breast cancer cases had ≥1 screening mammogram before diagnosis (2007–2017 linkage) | Huang 2025 Sci Rep [VERIFIED; A] |

### 2.3 Evidence for benefit (the "41%" and "30%" MOHW quote) [VERIFIED; A]

- MOHW repeatedly states that biennial mammography lowers breast-cancer mortality by **41%** and late-stage breast cancer by **30%**.
- These figures come from Yen et al. (2016): 1,429,890 Taiwanese women, 1999–2009.
  - Universal biennial mammography vs annual clinical breast examination: mortality **RR 0.59** (95% CI 0.48–0.73) and stage II+ **RR 0.70** (0.66–0.74).
  - Risk-based mammography: stage II+ RR 0.92; the mortality reduction was not significant (RR 0.86, 0.73–1.02).
  - Overdiagnosis: 13% higher than CBE for universal mammography.
  - Detection rates for universal mammography: 4.86 (first screen) and 2.98 (subsequent screens) per 1,000.
- The comparator was **annual CBE**, not "no screening". State this when quoting "41%".

---

## 3. Risk factors and hereditary syndromes

### 3.1 Risk factors

**MOHW list** (2024-09-05 and 2025-03-03 releases) [VERIFIED]: 初經早 (early menarche), 停經晚 (late menopause), 未曾生育 (nulliparity) or first birth after 30, 未曾哺乳 (never breastfed), family history of breast cancer, a pathogenic breast-cancer gene variant (乳癌變異型致病基因), and a previous breast, ovarian or endometrial cancer. Modifiable: tobacco, alcohol, diet, physical activity, weight.

**Taiwan big-data analysis** (NHI + screening + registry, 2,191,742 screened women; 38,815 incident cancers; Huang 2025 Sci Rep) [VERIFIED; A]
- Risk factors (OR): family history of any cancer 1.462; number of sisters with breast cancer 1.058 per sister; years of HRT 1.006 per year; breast symptoms 3.843; breast density 1.096.
- Protective: breastfeeding 0.908; menopausal status 0.935.
- The model AUC was only 0.68, so these factors stratify risk poorly on their own.

### 3.2 Hereditary genes: risk, tumour type and NCCN management highlights

| Gene / syndrome | Breast cancer risk | Tumour type | NCCN (patient guide, BOPP v3.2026) management highlights |
|---|---|---|---|
| **BRCA1** (HBOC) | Cumulative risk to age 80 **72%** (95% CI 65–79) [A, Kuchenbaecker 2017]. Ovarian risk to 80: 44%. Contralateral breast cancer at 20 years: 40%. Population OR 10.57 (BCAC) [FT]; 7.62 (CARRIERS) [A] | Stronger for ER-negative and triple-negative disease [A, Dorling] | CBE every 6–12 months from 25; **annual MRI 25–29**; **annual mammogram + MRI 30–75**; RRM is an option; RRSO at **35–40** [VERIFIED] |
| **BRCA2** (HBOC) | To age 80 **69%** (61–77). Ovarian 17%. Contralateral at 20 years: 26%. OR 5.85 (BCAC), 5.23 (CARRIERS) | Higher OR for ER-negative than ER-positive disease, but most BRCA2 cancers seen in practice are HR+ (in Lin 2016, 9 of 11 BRCA2 carriers were HR+/HER2−) | As BRCA1; RRSO may be delayed to **40–45** [VERIFIED] |
| **PALB2** | To age 80 **53%** (44–63) (Yang 2020, 524 families) [A]. RR 7.18. OR 5.02 (BCAC); 3.83 (CARRIERS). Ovarian 5%, pancreatic 2–3%, male breast 1% to age 80 | Higher OR for ER-negative disease | Annual mammogram + MRI **from 30**; discuss RRM; consider RRSO at about 45–50 [VERIFIED] |
| **TP53** (Li-Fraumeni) | Women: cumulative breast cancer **54% by age 70**; any cancer 50% by age 31 and nearly 100% by 70 (NCI cohort, Mai 2016) [A]. Overall cancer incidence about 24× the general population (de Andrade 2021) [A] | Early onset, often HER2+ [UNVERIFIED for HER2 association] | CBE every 6–12 months from 20; **annual MRI 20–29**; annual MRI + mammogram 30–75; RRM is an option; **avoid radiotherapy when other good options exist** (radiation-induced sarcoma); refer to a specialised centre [VERIFIED] |
| **CHEK2** | Moderate: OR **2.54** (BCAC; c.1100delC 2.66) [FT]; 2.47 (CARRIERS) [FT]. Absolute risk to 80 in the "moderate" 17–30% range (BCAC, UK) [FT]. Common missense variants p.Ile157Thr and p.Ser428Phe: OR <1.5 (limited importance) [FT] | **ER-positive** (OR 2.67 vs 1.64 for ER-negative); not associated with TNBC (OR 1.06) [FT] | **Annual mammogram from 40**; consider MRI from 30–35 depending on family history and density [VERIFIED] |
| Others to name | ATM OR 2.10 (ER+); BARD1, RAD51C, RAD51D (ER− / TN); CDH1 (lobular; diffuse gastric cancer); PTEN (Cowden); STK11 (Peutz–Jeghers); NF1 [FT; patient guide gene list] | | RRM is an option for BRCA1/2, CDH1, PALB2, PTEN, STK11, TP53 [VERIFIED] |

- In CARRIERS, P/LP variants in 12 established genes were found in 5.03% of cases and 1.63% of controls. The prevalence was lower in **Asian American** cases (1.64%). BRCA1/2/PALB2 variants were found in 8.13% of TNBC vs 1.84% of ER-positive cases [FT].
- Male carriers of BRCA1/2: breast self-exam training and annual CBE from 35; consider annual mammography from 50 (or 10 years before the earliest male breast cancer in the family) [VERIFIED; NCCN patient guide].

### 3.3 Taiwanese germline data [VERIFIED; A]

| Study (Taiwan) | Population | P/LP carrier rate | Notes |
|---|---|---|---|
| Lin PH 2016 (NTUH, 68-gene panel) | 133 early-onset or familial breast cancers | **22.6%** | BRCA1 9, BRCA2 11, TP53 2, RAD50 2. **TNBC 45.5%** carried a variant |
| Sung 2017 (VGH) | 272 HBOC patients | **18.4%** overall | BRCA1 7.7%, BRCA2 6.8%, non-BRCA 8.2%. No founder mutation; recurrent BRCA1 c.3607C>T and BRCA2 c.5164_5165delAG |
| Lin PH 2023 (NTUH) | 730 probands meeting HBOP criteria; 418 breast | 22.9% overall; **22.3% in breast** | BRCA1/2 dominant in breast/ovary; ATM most common in pancreas |
| Cheng HF 2023 (VGH-TAYLOR, tumour-only NGS) | 879 patients | BRCA1 3.1%, BRCA2 8.6%, PALB2 5.2% (tumour, not germline) | Many variants not in ClinVar. Tumour-only results need germline confirmation |

### 3.4 Germline testing criteria

**NCCN** (patient guide "Genetic Testing for Hereditary Breast, Ovarian, Pancreatic, and Prostate Cancers 2026", based on professional **v3.2026**, dated 2026-02-19) [VERIFIED as patient-guide wording]
- The current professional version on nccn.org is **v1.2027**. I did not read the v1.2027 professional criteria.

Testing **recommended** in a person with breast cancer (invasive or DCIS) if any of these apply:
- **Age:** diagnosed **≤50**.
- **Ancestry:** Ashkenazi Jewish.
- **Cancer type:** male breast cancer; **triple-negative**; more than one breast primary; lobular cancer with a personal or family history of diffuse gastric cancer.
- **Family history:** ≥1 close blood relative with breast cancer ≤50, male breast cancer, ovarian, pancreatic, or metastatic/high-risk prostate cancer; or **≥3 relatives (including the patient) on the same side** with breast or prostate cancer.
- **To guide therapy:** **metastatic** breast cancer (PARP inhibitor decision); **high-risk HER2-negative early breast cancer** (adjuvant PARP inhibitor, i.e. the olaparib/OlympiA setting).

Also recommended:
- for anyone with a relative who has a known P/LP variant;
- for an unaffected person (or one not meeting the above) with a **first- or second-degree** relative who meets the criteria above;
- when a model such as BRCAPro or CanRisk gives a BRCA1/2 probability **≥5%**.

Testing **may be considered**:
- breast cancer diagnosed at **51–65**;
- breast cancer at any age with close relatives who have certain prostate cancers;
- malignant phyllodes tumour;
- a model probability of 2.5–5%.

Testing is **unlikely to find high-risk variants** in women diagnosed after 65 without a relevant family history.

The NCCN Metastatic Breast Cancer patient guide (v3.2026) adds: **germline BRCA1/2 and PALB2 testing for everyone with metastatic breast cancer**, unless done after 2014 [VERIFIED].

**ASCO–SSO 2024** (Bedrosian 2024) [VERIFIED; A]
- **Offer BRCA1/2 testing to all newly diagnosed patients ≤65.** Above 65, test selectively based on personal or family history, ancestry, or PARP-inhibitor eligibility.
- Test all patients with recurrent breast cancer who are PARP-inhibitor candidates.
- Test women with a second primary in the same or the other breast.
- Offer genes beyond BRCA1/2 when the family history supports it.
- Variants of uncertain significance (VUS) should not change management.

### 3.5 Taiwan NHI coverage of genetic testing [PARTIAL]

- From **2024-05-01**, NHI pays for NGS in cancer at fixed amounts:
  - **BRCA test 10,000 points**
  - small panel (≤100 genes) 20,000 points
  - large panel (>100 genes) 30,000 points
- The covered solid tumours include **三陰性乳癌 (TNBC)**.
- Other conditions:
  - once per person per cancer type, for life;
  - the hospital must be a regional hospital or above, or a cancer-quality-certified hospital, listed in the LDT scheme, and must hold a molecular tumour board;
  - results must be uploaded to NHI.
- Source: MOHW 2024-04-19 (updated 2024-06-13) https://mohw.gov.tw/cp-16-78416-1.html [VERIFIED for these statements].
- The exact breast indications in the NHI payment rules (for example, BRCA testing for HER2-negative high-risk early disease or metastatic HR+ disease) and any coverage of PIK3CA/ESR1 testing: [UNVERIFIED] (nhi.gov.tw not reachable).

---

## 4. Pathology and biomarkers

### 4.1 ER and PR (ASCO/CAP 2020; Allison 2020) [VERIFIED; A]

- ER positive = **1–100%** of tumour nuclei stained.
- **ER Low Positive = 1–10%**, reported with a comment: limited data on endocrine benefit.
- ER negative = **<1%** or 0%.
- Report the status of controls for cases with 0–10% staining.
- PR follows the same principles and is used mainly for prognosis in ER-positive cancer.
- DCIS: ER testing is recommended (to judge endocrine risk reduction); PR is optional.
- The NCCN patient guide (MBC 2026) repeats ER+ = ≥1 in 100 cells and ER-low = 1–10 in 100 [VERIFIED].

### 4.2 HER2

**ASCO/CAP status** [VERIFIED; A]
- The **2023 update** (Wolff 2023) **affirmed the 2018 recommendations** without change. It judged new categories such as "HER2-Low" or "HER2-Ultra-Low" premature.
- It added best practice to distinguish **IHC 0 from 1+** and a new report comment, because trastuzumab deruxtecan is approved for IHC 1+ or 2+/ISH-negative disease.
- Best practice includes high-power examination and considering a second pathologist for borderline cases [PARTIAL; Koh & Im 2026 review].

**IHC scoring (2018 ASCO/CAP)**

| Score | Definition | Category | Tag |
|---|---|---|---|
| **3+** | Circumferential, complete, intense membrane staining in **>10%** of tumour cells | Positive | [PARTIAL: two peer-reviewed reproductions] |
| **2+** | Weak to moderate **complete** membrane staining in **>10%** | Equivocal → reflex ISH | [VERIFIED; 2018 abstract] |
| **1+** | Incomplete, faint/barely perceptible membrane staining in **>10%** | Negative ("HER2-low") | [PARTIAL] |
| **0** | No staining, or incomplete faint staining in **≤10%** | Negative | [PARTIAL] |
| 0 "with membrane staining" | Faint/barely perceptible incomplete staining in **>0 and ≤10%** | "**HER2-ultralow**" (trial and label term, not ASCO/CAP) | [VERIFIED; FDA Enhertu label §14.3] |
| 0 "null" | No membrane staining at all | HER2-null / zero | |

- CAP's biomarker reporting template now has an optional field for "0+ with membrane staining (≤10%)" [PARTIAL; Koh & Im 2026].

**Dual-probe ISH groups (2018)** [VERIFIED for the group definitions; final calls PARTIAL from Ahn 2020]

| Group | HER2/CEP17 ratio | Mean HER2 copies/cell | Final call |
|---|---|---|---|
| 1 | ≥2.0 | ≥4.0 | **Positive** |
| 2 | ≥2.0 | <4.0 | Negative, unless concurrent IHC 3+. If IHC 2+: blinded recount; if still group 2 → negative |
| 3 | <2.0 | ≥6.0 | IHC 3+ → positive. IHC 2+ → recount; if still group 3 → **positive**. IHC 0–1+ → negative |
| 4 | <2.0 | ≥4.0 and <6.0 | Negative, unless IHC 3+. IHC 2+ → recount; if still group 4 → negative |
| 5 | <2.0 | <4.0 | **Negative** |

- The 2018 update **removed the "ISH equivocal" category** and requires concurrent IHC review for groups 2–4.
- If a core biopsy is HER2-negative, a repeat test on the excision "may (not 'must')" be ordered [VERIFIED; A].

**Clinical HER2 categories in current use**

| Category | Definition | Where the term comes from |
|---|---|---|
| HER2-positive | IHC 3+ or ISH-amplified (IHC 2+/ISH+) | ASCO/CAP; FDA/TFDA labels |
| **HER2-low** (TFDA: HER2弱陽性) | IHC 1+ or IHC 2+/ISH− | DESTINY-Breast04 / -06; labels; NCCN |
| **HER2-ultralow** (TFDA: HER2微陽性) | IHC 0 **with** membrane staining (>0 and ≤10%) | DESTINY-Breast06; FDA and TFDA Enhertu labels |
| HER2-null / zero | IHC 0, no staining | |

- **DESTINY-Breast06** (Bardia 2024) [VERIFIED; A]: HR+ metastatic breast cancer after ≥1 endocrine line, chemotherapy-naive. n = 866 (713 HER2-low; 153 ultralow). In HER2-low disease, median PFS was **13.2 vs 8.1 months** (HR 0.62); results were consistent in the ultralow group. ILD/pneumonitis occurred in 11.3% (3 grade 5).
- Central review in DB-06 reclassified 24% of locally scored IHC 0 cases as HER2-low and 40% as ultralow. Reported ultralow prevalence is 10.6–29%, and interobserver agreement at the low end is poor [PARTIAL; Koh & Im 2026 review].
- **TFDA:** Enhertu 衛部菌疫輸字第001179號 includes 「HER2弱陽性(IHC 1+或IHC 2+/ISH-)或HER2微陽性(IHC 0且有細胞膜染色)」 HR+ mBC after ≥1 endocrine therapy [VERIFIED; TFDA].
- Re-test HER2 on post-neoadjuvant residual disease and on metastatic biopsies. HER2 status changed in about 3.4% after neoadjuvant chemotherapy in one series, and up to 15% in the literature [PARTIAL; Ahn 2020 review].

### 4.3 Ki-67 (International Ki67 Working Group 2021; Nielsen 2021) [VERIFIED; A]

- Analytical validity requires standardized pre-analytics and **standardized visual scoring**.
- Clinical utility is limited to **prognosis in ER+/HER2−, T1–2, N0–1** disease. In that group, **Ki-67 ≤5% or ≥30%** can be used to estimate prognosis, for example to identify patients who do not need adjuvant chemotherapy.
- Values between 5% and 30% should not drive decisions.
- ASCO 2022 [VERIFIED; A]: Ki-67 combined with other parameters (or IHC4) may be used in postmenopausal patients **without access to genomic tests**.
- Taiwan context: the TCR coded Ki-67 only recently, so registry analyses rarely use it (Huang & Tseng 2025, limitations) [VERIFIED; FT].

### 4.4 Histological grade (Nottingham / Elston–Ellis modification of Bloom–Richardson)

- Three features: **tubule formation, nuclear pleomorphism and mitotic count** (in a defined field area). Each is scored 1–3, and the sum gives grade 1–3 [VERIFIED; A, Elston & Ellis 1991].
- The summed score ranges from 3 to 9 [VERIFIED; FT, a 2022 deep-learning grading study].
- In 1,831 patients, grade was strongly prognostic (grade I better than II and III, P <0.0001).
- Grade is part of the Nottingham Prognostic Index (with size and nodal stage).
- **Sum cut-offs (3–5 = G1, 6–7 = G2, 8–9 = G3):** standard teaching, but I did not see them in a primary source I opened [PARTIAL]. Check against the CAP breast protocol or the WHO Blue Book before printing.
- Taiwan TCR (2011–2020, HER2-negative early cancers): nuclear grade III in 22.7% of HER2-low and 24.4% of HER2-zero tumours (Chen 2026) [FT].

---

## 5. Genomic assays (HR+/HER2− early breast cancer)

### 5.1 Oncotype DX (21-gene Recurrence Score, RS 0–100)

**TAILORx, node-negative** (tumour 1.1–5.0 cm, or 0.6–1.0 cm with intermediate/high grade)

- **RS 0–10** → endocrine therapy alone (Sparano 2015) [VERIFIED; A].
  - 1,626 of 10,253 (15.9%).
  - At 5 years: invasive disease-free survival (iDFS) 93.8%; distant recurrence-free **99.3%**; OS 98.0%.

- **RS 11–25** → randomized (Sparano 2018) [VERIFIED; A/FT].
  - n = 6,711 (69% of eligible patients).
  - Endocrine therapy alone was **non-inferior**: iDFS HR 1.08 (0.94–1.24).
  - 9-year rates, endocrine vs chemoendocrine: iDFS 83.3% vs 84.3%; distant recurrence-free 94.5% vs 95.0%; OS 93.9% vs 93.8%.
  - **Age nuance (exploratory):** in women **≤50**, chemotherapy lowered distant recurrence when:
    - RS **16–20**: by 0.8 percentage points at 5 years and **1.6** at 9 years;
    - RS **21–25**: by 3.2 at 5 years and **6.5** at 9 years.
    - OS was similar.
  - 40% of women ≤50 had RS 0–15, with about 2% distant recurrence at 9 years on endocrine therapy alone.
  - The authors note the benefit may partly reflect **chemotherapy-induced ovarian suppression**, and that it is unknown whether OFS plus an AI could replace chemotherapy.

- **RS 26–100** → chemoendocrine therapy (assigned, not randomized) [VERIFIED; FT].

- **Clinical risk added to RS** (Sparano 2019; clinical risk = size + grade) [VERIFIED; A].
  - In women ≤50 on endocrine therapy alone, 9-year distant recurrence was:
    - ≤1.8% with RS 0–10;
    - 4.7% with RS 11–25 and **low** clinical risk;
    - **12.3%** with RS 11–25 and **high** clinical risk.

- Summary from the authors: the assay can spare chemotherapy in up to 85% of node-negative patients — those **>50 with RS ≤25** and those **≤50 with RS ≤15**.

**RxPONDER (SWOG S1007): 1–3 positive nodes, RS ≤25** (Kalinsky 2021) [VERIFIED; A]
- n = 5,083 (33.2% premenopausal).
- **Postmenopausal:** 5-year iDFS 91.9% (endocrine) vs 91.3% (chemoendocrine), HR 1.02 → **no chemotherapy benefit.**
- **Premenopausal:** 5-year iDFS **89.0% vs 93.9%**, HR **0.60** (0.43–0.83); distant relapse-free survival HR 0.58 → **benefit.**
- The relative benefit did **not** increase with higher RS.
- **2026 ovarian-reserve analysis** (Kalinsky 2026; n = 1,556 aged <55) [VERIFIED; A]:
  - Chemotherapy benefit was confined to women with **AMH ≥10 pg/mL**: 64% of the group; iDFS HR **0.46**.
  - No benefit with AMH <10 pg/mL: HR 1.27.
  - AMH predicted benefit better than menopausal status, age or other hormones.
  - Practice relevance: this is not yet a guideline criterion. Most premenopausal patients in RxPONDER did **not** receive OFS.

### 5.2 MammaPrint (70-gene signature; result reported as genomic low vs high risk)

**MINDACT** (Cardoso 2016; Piccart 2021) [VERIFIED; A]
- 6,693 women, T1–T3 operable, 0–3 positive nodes, aged 18–70.
- Clinical risk was assessed with modified Adjuvant! Online.
- **High clinical / low genomic risk:** 1,550 patients (23.2%).
  - Without chemotherapy, 5-year distant metastasis-free survival (DMFS) was **94.7%** (95% CI 92.5–96.2). This was 1.5 percentage points below the chemotherapy group and met the 92% non-inferiority boundary.
  - About 46% of clinically high-risk women might not need chemotherapy.
- **8.7-year update** (high clinical / low genomic, ITT):
  - 8-year DMFS **92.0%** with chemotherapy vs **89.4%** without (HR 0.66).
  - In HR+/HER2− disease, by age (exploratory):
    - **≤50:** 93.6% vs 88.6% → **5.0 percentage-point** benefit;
    - **>50:** 90.2% vs 90.0% → **0.2 points.**
  - By nodes: N0 2.5 points; N1–3 1.3 points (not enhanced by nodal positivity).

### 5.3 Guideline positions

**ASCO 2022 biomarkers update** (Andre 2022) [VERIFIED; A]
- **Postmenopausal or >50, ER+/HER2−, N0 or 1–3 nodes:** Oncotype DX, MammaPrint, Breast Cancer Index or EndoPredict may be used.
- Prosigna and BCI: postmenopausal, node-negative only.
- **Premenopausal, node-negative:** Oncotype DX may be used.
- **Premenopausal with 1–3 nodes:** these patients benefit from chemotherapy regardless of genomic result.
- **≥4 nodes:** no data.
- Not for HER2+ or TNBC.

**NCCN** (patient guide, Invasive 2026, based on v2.2026) [VERIFIED]
- "Other tests might be helpful, but a **21-gene assay is the only test proven to predict who would benefit from chemotherapy**."
- The NCCN professional algorithm cut-offs were not read: [UNVERIFIED]. They are commonly summarized as RS <26 → endocrine alone if postmenopausal; RS ≤15 → endocrine alone if premenopausal; RS 16–25 → consider chemotherapy or OFS + endocrine therapy if premenopausal.

### 5.4 Handbook cut-off table (trial-verified)

| Situation (HR+/HER2−) | Oncotype RS | Chemotherapy benefit? | Evidence |
|---|---|---|---|
| N0, any age | 0–10 | No | TAILORx low-RS arm |
| N0, **>50** | 11–25 | No | TAILORx randomized |
| N0, **≤50** | 0–15 | No (about 2% distant recurrence at 9 years) | TAILORx exploratory |
| N0, **≤50** | **16–20** | Small (1.6 points at 9 years) | TAILORx exploratory |
| N0, **≤50** | **21–25** | Moderate (6.5 points at 9 years); may be ovarian-suppression effect | TAILORx exploratory |
| N0, any age | **≥26** | Yes (chemotherapy given) | TAILORx assigned arm |
| N1 (1–3 nodes), **postmenopausal** | ≤25 | **No** | RxPONDER |
| N1 (1–3 nodes), **premenopausal** | ≤25 | **Yes** (iDFS 89.0 → 93.9%) | RxPONDER |
| High clinical / low MammaPrint risk, **>50** | n/a | Negligible (0.2 points) | MINDACT |
| High clinical / low MammaPrint risk, **≤50** | n/a | About 5 points (exploratory) | MINDACT |

- AJCC 8th: a low Oncotype RS can **lower the prognostic stage** (see section 7).

---

## 6. Biomarker testing in recurrent or metastatic disease

### 6.1 Overview (NCCN Metastatic Breast Cancer patient guide 2026, based on v3.2026) [VERIFIED]

- Re-test ER, PR and HER2 on a new biopsy ("HER2 testing should be done on all new tumors").
- Targetable alterations: **PIK3CA, AKT1, PTEN, ESR1**, NTRK, RET.
- **ESR1 and RET testing is for HR+ tumours.**
- **Germline BRCA1/2 and PALB2 testing for everyone** with metastatic disease (unless done after 2014).
- PD-L1 testing "usually … when hormone receptors and HER2 testing are negative (like in triple-negative tumors)".
- Also MSI-H/dMMR and TMB-H (≥10 mut/Mb).
- Liquid biopsy (ctDNA) is an option, for example when tissue is exhausted.

### 6.2 PIK3CA / AKT1 / PTEN

- **Who:** HR+/HER2− advanced disease being considered for a PI3K/AKT-pathway drug.
- **Specimens (FDA labels)** [VERIFIED; L]:
  - **Alpelisib (Piqray**, label 2025-12-15): "one or more PIK3CA mutations in **tumor tissue or plasma**… If no mutation is detected in a plasma specimen, **test tumor tissue**." Indication: with fulvestrant after progression on or after an endocrine regimen.
  - **Inavolisib (Itovebi**, label 2026-04-21): PIK3CA mutations in **plasma**. Indication: with palbociclib + fulvestrant for **endocrine-resistant** disease that recurred on or after completing adjuvant endocrine therapy. In practice this means testing **at the first diagnosis of metastatic disease**.
  - **Capivasertib (Truqap**, label 2026-06-12): **one or more PIK3CA/AKT1/PTEN alterations in tumor tissue**. Indication: with fulvestrant after progression on ≥1 endocrine regimen in the metastatic setting, or recurrence on or within 12 months of adjuvant therapy.
- **Prevalence:** **40.8%** of CAPItello-291 patients had an AKT-pathway (PIK3CA/AKT1/PTEN) alteration (Turner 2023) [VERIFIED; A].
  - CAPItello-291 PFS: 7.2 vs 3.6 months overall (HR 0.60); 7.3 vs 3.1 months in altered tumours (HR 0.50).
  - Rash grade ≥3: 12.1%. Diarrhoea grade ≥3: 9.3%.
- **NCCN preferred 1st line (patient guide v3.2026)**, PIK3CA-mutated: fulvestrant + inavolisib + palbociclib, or alpelisib + fulvestrant. **2nd line and beyond**, PIK3CA/AKT1/PTEN-altered: capivasertib + fulvestrant [VERIFIED].
- **TFDA** [VERIFIED; TFDA]:
  - alpelisib 愛克利 (衛部藥輸字第027994–027996號, 2020-12-23);
  - capivasertib 泛抑癌 (028820/028821, **2024-11-06**; "具PIK3CA/AKT1/PTEN任一變異");
  - inavolisib 癌妥飛 (028944/028945, **2025-06-02**).

### 6.3 ESR1 (acquired resistance mutation): ctDNA

- **Why ctDNA, and why at progression.** ESR1 mutations are acquired under endocrine (mainly aromatase-inhibitor) pressure and are usually absent from the primary tumour. A fresh blood sample therefore detects them better than archival tissue.
- **ASCO rapid recommendation update 2023** (Burstein 2023) [PARTIAL; wording from ASCO Post summary]:
  - "Testing for the emergence of ESR1 mutations should be **routine at disease recurrence or progression**" on endocrine therapy, with or without a CDK4/6 inhibitor.
  - "The **preferred testing method is blood-based ctDNA**" (greater sensitivity).
  - Patients who remain ESR1 wild-type "may warrant **retesting at subsequent disease progression**".
  - The abstract itself is a template and gives no recommendation text.
- **FDA labels: all use plasma** [VERIFIED; L].
  - **Elacestrant (Orserdu)**: ER+/HER2− ESR1-mutated, after ≥1 endocrine line; postmenopausal women or adult men.
  - **Imlunestrant (Inluriyo)**: ESR1-mutated, after ≥1 endocrine line; adults.
  - **Vepdegestrant (Veppanu**, a PROTAC degrader): ESR1-mutated, after ≥1 endocrine line.
  - **Camizestrant (Etcamah**, accelerated approval, label effective **2026-09-04**): with a CDK4/6 inhibitor, "upon **detection of ESR1 mutation during aromatase inhibitor and CDK4/6 inhibitor therapy**".
    - Select patients who have had ≥6 months of AI + CDK4/6i, "using an FDA-authorized test performed **every 3 months until an ESR1 mutation has been detected**."
    - Approval date 2026-09-04 per news reports [PARTIAL]. The companion test is reported as Guardant360 CDx [PARTIAL].
- **Trial anchors** [VERIFIED; A]
  - **EMERALD** (elacestrant): ESR1 mutation detected in **47.8%**. PFS HR 0.70 overall and **0.55 in ESR1-mutated** disease.
  - **SERENA-6** (camizestrant):
    - ctDNA tested every 2–3 months during first-line AI + CDK4/6i (after ≥6 months).
    - 3,256 tested; **315** with an emergent ESR1 mutation and no radiological progression were randomized (about 10%; computed).
    - Switching to camizestrant gave median PFS **16.0 vs 9.2 months** (HR 0.44).
- **NCCN (patient guide v3.2026)** [VERIFIED]: for an ESR1 mutation after prior endocrine therapy ± CDK4/6i, use **elacestrant, imlunestrant or vepdegestrant**. Imlunestrant + abemaciclib is listed among other options.
- **TFDA** [VERIFIED; TFDA]: **imlunestrant 盈乳樂 衛部藥輸字第029131號, 2026-05-15**. **Elacestrant, vepdegestrant and camizestrant were not found** in the TFDA licence dataset.
- **Nursing summary of timing:**
  - Test **PIK3CA** at first diagnosis of metastatic disease (tissue or plasma).
  - Test **ESR1 by ctDNA at each progression** on endocrine therapy.
  - With camizestrant-style surveillance, test ESR1 by ctDNA **every 3 months** during first-line AI + CDK4/6i (US label).
  - Test **germline BRCA1/2 and PALB2** in all metastatic patients.

### 6.4 PD-L1 for TNBC: 22C3, combined positive score (CPS)

- **CPS** = (PD-L1-stained tumour cells + lymphocytes + macrophages) ÷ viable tumour cells × 100 (Cortes 2022 abstract) [VERIFIED; A].
- **KEYNOTE-355** (first-line metastatic TNBC; pembrolizumab + nab-paclitaxel, paclitaxel or gemcitabine-carboplatin) [VERIFIED; A]:
  - PD-L1 was measured centrally with **PD-L1 IHC 22C3 pharmDx**; randomization was stratified by CPS ≥1 vs <1 [L].
  - **CPS ≥10:** median OS **23.0 vs 16.1 months**, HR **0.73** (significant).
  - CPS ≥1: 17.6 vs 16.0 months (HR 0.86; not significant).
  - ITT: 17.2 vs 15.5 months.
  - → **The CPS ≥10 cut-off defines the indication.**
- **FDA Keytruda label** (2026-07-10) [VERIFIED; L]:
  - with chemotherapy for locally recurrent unresectable or metastatic TNBC with **CPS ≥10**;
  - **new:** with **sacituzumab govitecan** first-line for CPS ≥10;
  - early-stage high-risk TNBC (KEYNOTE-522) **regardless of PD-L1**.
- **TFDA Keytruda** (衛部菌疫輸字第001025號) [VERIFIED; TFDA]: high-risk early TNBC (neoadjuvant then adjuvant), and metastatic TNBC with chemotherapy when 「PD-L1表現(綜合陽性分數[CPS]≥10)」. The sacituzumab combination is not in the TFDA text.
- **NCCN (patient guide v3.2026)** [VERIFIED]:
  - CPS ≥10: chemotherapy + pembrolizumab, or sacituzumab govitecan + pembrolizumab, preferred first line.
  - CPS <10: sacituzumab govitecan, datopotamab deruxtecan, or chemotherapy.
  - gBRCA: PARP inhibitor or platinum.

---

## 7. AJCC 8th edition: anatomic vs prognostic stage

- **Edition in force:** breast is still **AJCC 8th edition** (AJCC "Current Staging System 2026" chart lists Breast = 8; no Version 9 protocol) [VERIFIED; https://www.facs.org/media/c5ik5tkr/ajcc-current-staging-system-2026.pdf].
- **Concept** (Giuliano 2017; NCCN patient guide 2026) [VERIFIED; A]:
  - **Anatomic stage** = T, N and M only. It is kept so that staging works worldwide where biomarkers are not available.
  - **Prognostic stage** = anatomic TNM **plus grade, ER, PR and HER2**. For eligible cancers, a **low Oncotype DX RS** can also lower the stage.
  - The prognostic stage assumes standard-of-care treatment.
  - There are **clinical** (cTNM, before treatment) and **pathological** (pTNM, after surgery) prognostic stage groups; "y" marks staging after neoadjuvant therapy.
- **Oncotype rule:** for HR+/HER2−, node-negative tumours <5 cm, an RS **<11** places the cancer in the most favourable prognostic group (pathological prognostic **stage IA**) [PARTIAL: <11 threshold and N0/<5 cm condition from Łukasiewicz 2021; "IA" from secondary knowledge].
- **Size of the effect:** in a Chinese series of luminal B-like HER2− cancers (n = 407), the prognostic stage moved **52.8%** of patients to a different group (25.1% down, 27.8% up) [PARTIAL; secondary validation study, abstract and full text read but not a Taiwanese cohort].
- **Teaching example of direction:** a triple-negative or grade 3 tumour is upstaged; an ER+/PR+/HER2+ or low-grade ER+ tumour is downstaged relative to the anatomic stage. Use the AJCC tables for exact cells; I did not reproduce the full table [UNVERIFIED cell-level grid].
- **LCIS** is not staged as Tis in the 8th edition (Tis = DCIS, Paget) [PARTIAL; consistent with the Taiwan LF counts above].

---

## 8. NCCN versions (nccn.org category pages, read 2026-10-29) [VERIFIED]

| Guideline | Version on 2026-10-29 |
|---|---|
| **Breast Cancer** | **Version 9.2026** |
| Breast Cancer Screening and Diagnosis | Version 1.2026 |
| Breast Cancer Risk Reduction | Version 1.2027 |
| Genetic/Familial High-Risk Assessment: Breast, Ovarian, Pancreatic, and Prostate | **Version 1.2027** |

- Recent JNCCN publications:
  - "Breast Cancer, Version 4.2026" (Gradishar 2026, JNCCN 24(7); metastatic-disease focus);
  - "NCCN Guidelines Insights: Breast Cancer, Version 5.2025" (early-stage updates);
  - "Insights: Genetic/Familial High-Risk Assessment: BOPP, Version 2.2026" (Cheng 2026; prostate and pancreas screening, non-epithelial ovarian testing criteria).
  I read only the abstracts [A].
- The NCCN Guidelines for Patients cited here lag behind the professional versions: Invasive 2026 is based on v2.2026 (2026-02-27); Metastatic 2026 on v3.2026 (2026-05-08); Genetic Testing 2026 on BOPP v3.2026 (2026-02-19).

---

## 9. Items not verified (do not print without checking)

1. National 2023 in-situ (DCIS) count (all hospitals); HPA annual report not reachable.
2. Nationwide Taiwanese subtype distribution for all stages, and for years after 2017.
3. NHI payment criteria for BRCA (breast indications), PIK3CA and ESR1 testing (nhi.gov.tw unreachable).
4. NCCN professional v9.2026 algorithm text for Oncotype/MammaPrint thresholds and for biomarker timing; NCCN BOPP v1.2027 changes versus v3.2026.
5. Nottingham grade cut-offs (3–5 / 6–7 / 8–9) in a primary source; full AJCC 8th prognostic-stage grid.
6. HER2 IHC 0/1+/3+ wording directly from ASCO/CAP 2018 full text (two peer-reviewed reproductions agree).
7. TP53 carriers' predominance of HER2+ breast cancer.
8. Whether the Taiwan Cancer Registry stores anatomic or prognostic stage for breast.
9. TFDA status of elacestrant, vepdegestrant, camizestrant (not found in the 2026-10-29 dataset copy; a pending application cannot be excluded).

---

## 10. References (APA 7)

### Official and registry sources
- 衛生福利部. (2025, December 30; updated 2026, January 5). *公布112年國人癌症登記資料分析結果 守護健康未來 從癌症篩檢開始* [Press release, with 附表 and 附圖]. https://mohw.gov.tw/cp-2704-84987-1.html ; attachment https://www.mohw.gov.tw/dl-98499-cd0fe70e-8e08-42cc-be15-3860b40d7f4d.html
- 衛生福利部統計處. (2026, June 22). *國人死亡人數連續3年下降 十大死因中6項死因人數、死亡率都減少* [Press release]; *114年死因統計結果分析* [PDF]; *114年死因統計結果摘要表* [Data set]. https://mohw.gov.tw/cp-16-86970-1.html ; https://www.mohw.gov.tw/dl-100915-0a572340-fabe-4a89-a8a0-199640a9053d.html ; https://www.mohw.gov.tw/dl-100920-e5938c74-aa2a-4994-a15c-054787318303.html
- 衛生福利部國民健康署. (2024, September 5). *乳影隨行健康相隨，粉紅十月健康相挺* [Press release]. https://mohw.gov.tw/cp-2704-79842-1.html
- 衛生福利部國民健康署. (2025, March 3). *乳癌篩檢年齡擴大至40-74歲婦女* [Press release]. https://mohw.gov.tw/cp-16-81672-1.html
- 衛生福利部國民健康署. (2025, June 6). *定期篩檢防乳癌 2年1次免費又安心* [Press release]. https://mohw.gov.tw/cp-16-82698-1.html
- 衛生福利部國民健康署. (2025, September 30; updated 2025, October 15). *粉紅十月！乳癌篩檢突破百萬人次 40開始乳攝篩檢護健康* [Press release]. https://mohw.gov.tw/cp-16-84098-1.html
- 衛生福利部國民健康署. (2026, March 2). *婦女節乳篩顧健康 愛家人也要護自己* [Press release]. https://mohw.gov.tw/cp-16-85674-1.html
- 衛生福利部國民健康署. (2026, September 17). *乳房X光攝影檢查兩年一篩 給自己15分鐘 「乳」此心安* [Press release]. https://www.mohw.gov.tw/cp-16-88006-1.html
- 衛生福利部中央健康保險署. (2024, April 19; updated 2024, June 13). *健保5月1日起給付癌症精準醫療「實體癌/血癌次世代基因定序檢測(NGS)」2萬多名癌友受惠* [Press release]. https://mohw.gov.tw/cp-16-78416-1.html
- Taiwan Cancer Registry Center. (2026, January). *Year_Breast_2023* and *Period_Breast_2023* [Data sets]. https://twcr.tw/wp-content/uploads/2026/01/Year_Breast_2023.xlsx ; https://twcr.tw/wp-content/uploads/2026/01/Period_Breast_2023.xlsx
- Taiwan Cancer Registry Center. (2025, December). *112年癌症登記長表報告* (CA17_LF112.pdf). https://twcr.tw/wp-content/uploads/2025/12/CA17_LF112.pdf
- Taiwan Cancer Registry Center. (2025, December). *台灣10大癌症108-112年新發個案存活率（追蹤至113年）* (Survival_108_112.pdf). https://twcr.tw/wp-content/uploads/2025/12/Survival_108_112.pdf
- Taiwan Food and Drug Administration. (2026). *全部藥品許可證資料集* [Data set, InfoId 36; copy downloaded 2026-10-29]. https://data.fda.gov.tw/opendata/exportDataList.do?method=ExportData&InfoId=36&logType=2
- American Joint Committee on Cancer. (2026). *AJCC current staging system* [Chart]. https://www.facs.org/media/c5ik5tkr/ajcc-current-staging-system-2026.pdf
- National Comprehensive Cancer Network. (2026). *NCCN Guidelines: Category pages* (Breast Cancer v9.2026; Breast Cancer Screening and Diagnosis v1.2026; Breast Cancer Risk Reduction v1.2027; Genetic/Familial High-Risk Assessment: BOPP v1.2027). Retrieved October 29, 2026, from https://www.nccn.org/guidelines/category_1 and https://www.nccn.org/guidelines/category_2
- National Comprehensive Cancer Network. (2026). *NCCN Guidelines for Patients: Invasive breast cancer* (based on NCCN Guidelines for Breast Cancer v2.2026). https://www.nccn.org/patients/guidelines/content/PDF/breast-invasive-patient.pdf
- National Comprehensive Cancer Network. (2026). *NCCN Guidelines for Patients: Metastatic breast cancer* (based on v3.2026). https://www.nccn.org/patients/guidelines/content/PDF/stage_iv_breast-patient.pdf
- National Comprehensive Cancer Network. (2026). *NCCN Guidelines for Patients: Genetic testing for hereditary breast, ovarian, pancreatic, and prostate cancers* (based on Genetic/Familial High-Risk Assessment: BOPP v3.2026). https://www.nccn.org/patients/guidelines/content/PDF/genetics-patient.pdf
- U.S. Food and Drug Administration labels via openFDA (effective dates): ORSERDU (elacestrant) 2026-06-24; PIQRAY (alpelisib) 2025-12-15; ITOVEBI (inavolisib) 2026-04-21; TRUQAP (capivasertib) 2026-06-12; INLURIYO (imlunestrant) 2026-06-04; VEPPANU (vepdegestrant) 2026-06-12; ETCAMAH (camizestrant) 2026-09-04; KEYTRUDA (pembrolizumab) 2026-07-10; ENHERTU (fam-trastuzumab deruxtecan-nxki) 2026-05-15. https://api.fda.gov/drug/label.json
- The ASCO Post. (2023, June 25). *Guideline update provides new testing and treatment recommendations for patients with ER-positive, HER2-negative metastatic breast cancer with ESR1 mutations*. https://ascopost.com/issues/june-25-2023/guideline-update-provides-new-testing-and-treatment-recommendations-for-patients-with-er-positive-her2-negative-metastatic-breast-cancer-with-esr1-mutations

### Journal articles
- Ahn, S., Woo, J. W., Lee, K., & Park, S. Y. (2020). HER2 status in breast cancer: Changes in guidelines and complicating factors for interpretation. *Journal of Pathology and Translational Medicine, 54*(1), 34–44. https://doi.org/10.4132/jptm.2019.11.03 (PMID 31693827; PMCID PMC6986968)
- Allison, K. H., Hammond, M. E. H., Dowsett, M., McKernin, S. E., Carey, L. A., Fitzgibbons, P. L., Hayes, D. F., Lakhani, S. R., Chavez-MacGregor, M., Perlmutter, J., Perou, C. M., Regan, M. M., Rimm, D. L., Symmans, W. F., Torlakovic, E. E., Varella, L., Viale, G., Weisberg, T. F., McShane, L. M., & Wolff, A. C. (2020). Estrogen and progesterone receptor testing in breast cancer: ASCO/CAP guideline update. *Journal of Clinical Oncology, 38*(12), 1346–1366. https://doi.org/10.1200/JCO.19.02309 (PMID 31928404)
- Andre, F., Ismaila, N., Allison, K. H., Barlow, W. E., Collyar, D. E., Damodaran, S., Henry, N. L., Jhaveri, K., Kalinsky, K., Kuderer, N. M., Litvak, A., Mayer, E. L., Pusztai, L., Raab, R., Wolff, A. C., & Stearns, V. (2022). Biomarkers for adjuvant endocrine and chemotherapy in early-stage breast cancer: ASCO guideline update. *Journal of Clinical Oncology, 40*(16), 1816–1837. https://doi.org/10.1200/JCO.22.00069 (PMID 35439025; erratum 40(22), 2514)
- Bardia, A., Hu, X., Dent, R., Yonemori, K., Barrios, C. H., O'Shaughnessy, J. A., Wildiers, H., Pierga, J.-Y., Zhang, Q., Saura, C., Biganzoli, L., Sohn, J., Im, S.-A., Lévy, C., Jacot, W., Begbie, N., Ke, J., Patel, G., & Curigliano, G. (2024). Trastuzumab deruxtecan after endocrine therapy in metastatic breast cancer. *The New England Journal of Medicine, 391*(22), 2110–2122. https://doi.org/10.1056/NEJMoa2407086 (PMID 39282896)
- Bedrosian, I., Somerfield, M. R., Achatz, M. I., Boughey, J. C., Curigliano, G., Friedman, S., Kohlmann, W. K., Kurian, A. W., Laronga, C., Lynce, F., Norquist, B. S., Plichta, J. K., Rodriguez, P., Shah, P. D., Tischkowitz, M., Wood, M., Yadav, S., Yao, K., & Robson, M. E. (2024). Germline testing in patients with breast cancer: ASCO–Society of Surgical Oncology guideline. *Journal of Clinical Oncology, 42*(5), 584–604. https://doi.org/10.1200/JCO.23.02225 (PMID 38175972)
- Bidard, F.-C., Kaklamani, V. G., Neven, P., Streich, G., Montero, A. J., Forget, F., Mouret-Reynier, M.-A., Sohn, J. H., Taylor, D., Harnden, K. K., Khong, H., Kocsis, J., Dalenc, F., Dillon, P. M., Babu, S., Waters, S., Deleu, I., García Sáenz, J. A., Bria, E., . . . Bardia, A. (2022). Elacestrant (oral selective estrogen receptor degrader) versus standard endocrine therapy for estrogen receptor–positive, human epidermal growth factor receptor 2–negative advanced breast cancer: Results from the randomized phase III EMERALD trial. *Journal of Clinical Oncology, 40*(28), 3246–3256. https://doi.org/10.1200/JCO.22.00338 (PMID 35584336; PMCID PMC9553388)
- Bidard, F.-C., Mayer, E. L., Park, Y. H., Janni, W., Ma, C., Cristofanilli, M., Bianchini, G., Kalinsky, K., Iwata, H., Chia, S., Fasching, P. A., Brufsky, A., Nowecki, Z., Pascual, J., Moreau, L., Chen, S.-C., Karadurmus, N., Gal-Yam, E. N., Jung, K. H., . . . Turner, N. C. (2025). First-line camizestrant for emerging ESR1-mutated advanced breast cancer. *The New England Journal of Medicine, 393*(6), 569–580. https://doi.org/10.1056/NEJMoa2502929 (PMID 40454637)
- Burstein, H. J., DeMichele, A., Somerfield, M. R., & Henry, N. L. (2023). Testing for ESR1 mutations to guide therapy for hormone receptor–positive, human epidermal growth factor receptor 2–negative metastatic breast cancer: ASCO guideline rapid recommendation update. *Journal of Clinical Oncology, 41*(18), 3423–3425. https://doi.org/10.1200/JCO.23.00638 (PMID 37196213)
- Cardoso, F., van't Veer, L. J., Bogaerts, J., Slaets, L., Viale, G., Delaloge, S., Pierga, J.-Y., Brain, E., Causeret, S., DeLorenzi, M., Glas, A. M., Golfinopoulos, V., Goulioti, T., Knox, S., Matos, E., Meulemans, B., Neijenhuis, P. A., Nitz, U., Passalacqua, R., . . . Piccart, M. (2016). 70-gene signature as an aid to treatment decisions in early-stage breast cancer. *The New England Journal of Medicine, 375*(8), 717–729. https://doi.org/10.1056/NEJMoa1602253 (PMID 27557300)
- Chen, B.-F., Tsai, Y.-F., Lien, P.-J., Lin, Y.-S., Feng, C.-J., Chen, Y.-J., Cheng, H.-F., Tseng, L.-M., & Huang, C.-C. (2023). Clinical characteristics and treatment outcomes of invasive ductal and lobular carcinoma: Analyses of 54,832 Taiwan Cancer Registry index cases. *Breast Cancer Research and Treatment, 201*(3), 547–560. https://doi.org/10.1007/s10549-023-07044-5 (PMID 37470893)
- Chen, Y.-J. G., Lien, P.-J., Tseng, L.-M., & Huang, C.-C. (2026). Clinical presentations and prognostication of HER2-low and HER2-zero early breast cancer in Taiwan. *Journal of the Chinese Medical Association, 89*(5), 354–363. https://doi.org/10.1097/JCMA.0000000000001376 (PMID 41968415; PMCID PMC13193289)
- Cheng, H. H., Giri, V. N., Goggins, M., Yurgelun, M. B., Karlan, B. Y., Norquist, B. S., Daly, M. B., Pal, T., AlHilli, Z., Arun, B., Churpek, J., Colonna, S., Domchek, S. M., Escobar, M. R., Fejerman, L., Friedman, S., Hagemann, A., Hendrix, A., Huo, D., . . . Dwyer, M. (2026). NCCN Guidelines® Insights: Genetic/familial high-risk assessment: Breast, ovarian, pancreatic, and prostate, version 2.2026. *Journal of the National Comprehensive Cancer Network, 24*(2), 2–10. https://doi.org/10.6004/jnccn.2026.0007 (PMID 41671423)
- Cheng, H.-F., Tsai, Y.-F., Liu, C.-Y., Hsu, C.-Y., Lien, P.-J., Lin, Y.-S., Chao, T.-C., Lai, J.-I., Feng, C.-J., Chen, Y.-J., Chen, B.-F., Chiu, J.-H., Tseng, L.-M., & Huang, C.-C. (2023). Prevalence of BRCA1, BRCA2, and PALB2 genomic alterations among 924 Taiwanese breast cancer assays with tumor-only targeted sequencing: Extended data analysis from the VGH-TAYLOR study. *Breast Cancer Research, 25*(1), Article 152. https://doi.org/10.1186/s13058-023-01751-z (PMID 38098088; PMCID PMC10722686)
- Cortes, J., Cescon, D. W., Rugo, H. S., Nowecki, Z., Im, S.-A., Yusof, M. M., Gallardo, C., Lipatov, O., Barrios, C. H., Holgado, E., Iwata, H., Masuda, N., Otero, M. T., Gokmen, E., Loi, S., Guo, Z., Zhao, J., Aktan, G., Karantza, V., & Schmid, P. (2020). Pembrolizumab plus chemotherapy versus placebo plus chemotherapy for previously untreated locally recurrent inoperable or metastatic triple-negative breast cancer (KEYNOTE-355): A randomised, placebo-controlled, double-blind, phase 3 clinical trial. *The Lancet, 396*(10265), 1817–1828. https://doi.org/10.1016/S0140-6736(20)32531-9 (PMID 33278935)
- Cortes, J., Rugo, H. S., Cescon, D. W., Im, S.-A., Yusof, M. M., Gallardo, C., Lipatov, O., Barrios, C. H., Perez-Garcia, J., Iwata, H., Masuda, N., Torregroza Otero, M., Gokmen, E., Loi, S., Guo, Z., Zhou, X., Karantza, V., Pan, W., & Schmid, P. (2022). Pembrolizumab plus chemotherapy in advanced triple-negative breast cancer. *The New England Journal of Medicine, 387*(3), 217–226. https://doi.org/10.1056/NEJMoa2202809 (PMID 35857659)
- Daly, M. B., Pal, T., Maxwell, K. N., Churpek, J., Kohlmann, W., AlHilli, Z., Arun, B., Buys, S. S., Cheng, H., Domchek, S. M., Friedman, S., Giri, V., Goggins, M., Hagemann, A., Hendrix, A., Hutton, M. L., Karlan, B. Y., Kassem, N., Khan, S., . . . Darlow, S. D. (2023). NCCN Guidelines® Insights: Genetic/familial high-risk assessment: Breast, ovarian, and pancreatic, version 2.2024. *Journal of the National Comprehensive Cancer Network, 21*(10), 1000–1010. https://doi.org/10.6004/jnccn.2023.0051 (PMID 37856201)
- de Andrade, K. C., Khincha, P. P., Hatton, J. N., Frone, M. N., Wegman-Ostrosky, T., Mai, P. L., Best, A. F., & Savage, S. A. (2021). Cancer incidence, patterns, and genotype–phenotype associations in individuals with pathogenic or likely pathogenic germline TP53 variants: An observational cohort study. *The Lancet Oncology, 22*(12), 1787–1798. https://doi.org/10.1016/S1470-2045(21)00580-5 (PMID 34780712; PMCID PMC8915249)
- Dorling, L., Carvalho, S., Allen, J., González-Neira, A., Luccarini, C., Wahlström, C., Pooley, K. A., Parsons, M. T., Fortuno, C., Wang, Q., Bolla, M. K., Dennis, J., Keeman, R., Alonso, M. R., Álvarez, N., Herraez, B., Fernandez, V., Núñez-Torres, R., Osorio, A., . . . Easton, D. F. (2021). Breast cancer risk genes—Association analysis in more than 113,000 women. *The New England Journal of Medicine, 384*(5), 428–439. https://doi.org/10.1056/NEJMoa1913948 (PMID 33471991; PMCID PMC7611105) [Breast Cancer Association Consortium]
- Elston, C. W., & Ellis, I. O. (1991). Pathological prognostic factors in breast cancer. I. The value of histological grade in breast cancer: Experience from a large study with long-term follow-up. *Histopathology, 19*(5), 403–410. https://doi.org/10.1111/j.1365-2559.1991.tb00229.x (PMID 1757079)
- Giuliano, A. E., Connolly, J. L., Edge, S. B., Mittendorf, E. A., Rugo, H. S., Solin, L. J., Weaver, D. L., Winchester, D. J., & Hortobagyi, G. N. (2017). Breast cancer—Major changes in the American Joint Committee on Cancer eighth edition cancer staging manual. *CA: A Cancer Journal for Clinicians, 67*(4), 290–303. https://doi.org/10.3322/caac.21393 (PMID 28294295; erratum 67(4), 345)
- Gradishar, W. J., Moran, M. S., Abraham, J., Abramson, V., Aft, R., Agnese, D., Allison, K. H., Anderson, B., Bailey, J., Burstein, H. J., Chen, N., Chew, H., Dang, C., Elias, A. D., Giordano, S. H., Goetz, M. P., Jankowitz, R. C., Javid, S. H., Krishnamurthy, J., . . . Kumar, R. (2025). NCCN Guidelines® Insights: Breast cancer, version 5.2025. *Journal of the National Comprehensive Cancer Network, 23*(11), 426–436. https://doi.org/10.6004/jnccn.2025.0053 (PMID 41213254)
- Gradishar, W. J., Moran, M. S., Abraham, J., Abramson, V., Aft, R., Agnese, D., Allison, K. H., Anderson, B., Bailey, J., Burstein, H. J., Chen, N., Chew, H., Dang, C., Elias, A. D., Giordano, S. H., Goetz, M. P., Jankowitz, R. C., Javid, S. H., Leitch, A. M., . . . Kumar, R. (2026). Breast cancer, version 4.2026, NCCN Clinical Practice Guidelines in Oncology. *Journal of the National Comprehensive Cancer Network, 24*(7). https://doi.org/10.6004/jnccn.2026.0033 (PMID 42425164)
- Hu, C., Hart, S. N., Gnanaolivu, R., Huang, H., Lee, K. Y., Na, J., Gao, C., Lilyquist, J., Yadav, S., Boddicker, N. J., Samara, R., Klebba, J., Ambrosone, C. B., Anton-Culver, H., Auer, P., Bandera, E. V., Bernstein, L., Bertrand, K. A., Burnside, E. S., . . . Couch, F. J. (2021). A population-based study of genes previously implicated in breast cancer. *The New England Journal of Medicine, 384*(5), 440–451. https://doi.org/10.1056/NEJMoa2005936 (PMID 33471974; PMCID PMC8127622)
- Huang, C.-C., Lu, T.-P., Wang, Y.-J., Chen, B.-F., Yang, H.-T., Chang, W.-P., & Tseng, L.-M. (2025). Identifying breast cancer risk factors and evaluating biennial mammography screening efficacy using big data analysis in Taiwan. *Scientific Reports, 15*(1), Article 16250. https://doi.org/10.1038/s41598-025-00984-6 (PMID 40346112; PMCID PMC12064733)
- Huang, C.-C., & Tseng, L.-M. (2025). Treatment patterns and outcomes of young female early breast cancer in Taiwan. *Journal of Breast Cancer, 28*(1), 37–45. https://doi.org/10.4048/jbc.2024.0188 (PMID 40047089; PMCID PMC11885852)
- Kalinsky, K., Barlow, W. E., Gralow, J. R., Meric-Bernstam, F., Albain, K. S., Hayes, D. F., Lin, N. U., Perez, E. A., Goldstein, L. J., Chia, S. K. L., Dhesy-Thind, S., Rastogi, P., Alba, E., Delaloge, S., Martin, M., Kelly, C. M., Ruiz-Borrego, M., Gil-Gil, M., Arce-Salinas, C. H., . . . Hortobagyi, G. N. (2021). 21-gene assay to inform chemotherapy benefit in node-positive breast cancer. *The New England Journal of Medicine, 385*(25), 2336–2347. https://doi.org/10.1056/NEJMoa2108873 (PMID 34914339; PMCID PMC9096864)
- Kalinsky, K., Barlow, W. E., Pathak, H. B., Puri, R. V., Mitra, A., Home, T., Gralow, J., Albain, K. S., Hayes, D. F., Delaloge, S., Lin, N. U., Perez, E. A., Goldstein, L. J., Chia, S. K. L., Rastogi, P., Schott, A. F., Brain, E., Pierga, J.-Y., Ferrero, J.-M., . . . Godwin, A. K. (2026). Ovarian reserve as a measure of adjuvant chemotherapy benefit in hormone receptor positive (HR-positive), HER2-negative, node-positive breast cancer in SWOG S1007 (RxPONDER). *Annals of Oncology, 37*(9), 1220–1229. https://doi.org/10.1016/j.annonc.2026.05.697 (PMID 42613139; PMCID PMC13488494; erratum published 2026-10-20)
- Koh, J., & Im, S.-A. (2026). Redefining HER2 in breast cancer: From conventional positivity to low and ultralow in the new era of antibody–drug conjugates. *Cancer Research and Treatment, 58*(1), 15–25. https://doi.org/10.4143/crt.2025.1182 (PMID 41414806; PMCID PMC12800947)
- Kuchenbaecker, K. B., Hopper, J. L., Barnes, D. R., Phillips, K.-A., Mooij, T. M., Roos-Blom, M.-J., Jervis, S., van Leeuwen, F. E., Milne, R. L., Andrieu, N., Goldgar, D. E., Terry, M. B., Rookus, M. A., Easton, D. F., Antoniou, A. C., McGuffog, L., Evans, D. G., Barrowdale, D., Frost, D., . . . Olsson, H. (2017). Risks of breast, ovarian, and contralateral breast cancer for BRCA1 and BRCA2 mutation carriers. *JAMA, 317*(23), 2402–2416. https://doi.org/10.1001/jama.2017.7112 (PMID 28632866)
- Lee, K.-T., Huang, P.-H., Hsu, C.-Y., Lee, Y.-H., Chen, H.-W., Lu, Y.-S., Lai, J.-I., Chao, T.-C., Liu, C.-Y., Huang, C.-C., Tsai, Y.-F., Tseng, L.-M., Yang, W.-C., Huang, Y.-T., Huang, C.-Y., & Lin, Y.-C. (2025). A retrospective study to investigate the prevalence and describe the clinicopathological characteristics, treatments, and outcomes of HER2-low breast cancer in Taiwan. *Cancer Treatment and Research Communications, 43*, Article 100893. https://doi.org/10.1016/j.ctarc.2025.100893 (PMID 40139140)
- Lin, C.-H., Liau, J.-Y., Lu, Y.-S., Huang, C.-S., Lee, W.-C., Kuo, K.-T., Shen, Y.-C., Kuo, S.-H., Lan, C., Liu, J. M., Kuo, W.-H., Chang, K.-J., & Cheng, A.-L. (2009). Molecular subtypes of breast cancer emerging in young women in Taiwan: Evidence for more than just westernization as a reason for the disease in Asia. *Cancer Epidemiology, Biomarkers & Prevention, 18*(6), 1807–1814. https://doi.org/10.1158/1055-9965.EPI-09-0096 (PMID 19505913)
- Lin, P.-H., Kuo, W.-H., Huang, A.-C., Lu, Y.-S., Lin, C.-H., Kuo, S.-H., Wang, M.-Y., Liu, C.-Y., Cheng, F. T.-F., Yeh, M.-H., Li, H.-Y., Yang, Y.-H., Hsu, Y.-H., Fan, S.-C., Li, L.-Y., Yu, S.-L., Chang, K.-J., Chen, P.-L., Ni, Y.-H., & Huang, C.-S. (2016). Multiple gene sequencing for risk assessment in patients with early-onset or familial breast cancer. *Oncotarget, 7*(7), 8310–8320. https://doi.org/10.18632/oncotarget.7027 (PMID 26824983; PMCID PMC4884994)
- Lin, P.-H., Tien, Y.-W., Cheng, W.-F., Chiang, Y.-C., Wu, C.-H., Yang, K., & Huang, C.-S. (2023). Diverse genetic spectrum among patients who met the criteria of hereditary breast, ovarian and pancreatic cancer syndrome. *Journal of Gynecologic Oncology, 34*(5), Article e66. https://doi.org/10.3802/jgo.2023.34.e66 (PMID 37170728; PMCID PMC10482589)
- Lo, C., Chang, D.-Y., Lu, Y.-S., Wang, M.-Y., Tsai, L.-W., Huang, C.-S., Tang, C.-H., & Lin, C.-H. (2025). Benefit of adjuvant chemotherapy for T1cN0M0 and selected T1bN0M0 triple-negative breast cancer: A nationwide cancer registry-based study. *The Oncologist, 30*(2), Article oyae346. https://doi.org/10.1093/oncolo/oyae346 (PMID 40042201; PMCID PMC11880992)
- Łukasiewicz, S., Czeczelewski, M., Forma, A., Baj, J., Sitarz, R., & Stanisławek, A. (2021). Breast cancer—Epidemiology, risk factors, classification, prognostic markers, and current treatment strategies—An updated review. *Cancers, 13*(17), Article 4287. https://doi.org/10.3390/cancers13174287 (PMID 34503097; PMCID PMC8428369)
- Mai, P. L., Best, A. F., Peters, J. A., DeCastro, R. M., Khincha, P. P., Loud, J. T., Bremer, R. C., Rosenberg, P. S., & Savage, S. A. (2016). Risks of first and subsequent cancers among TP53 mutation carriers in the National Cancer Institute Li-Fraumeni syndrome cohort. *Cancer, 122*(23), 3673–3681. https://doi.org/10.1002/cncr.30248 (PMID 27496084; PMCID PMC5115949)
- Nielsen, T. O., Leung, S. C. Y., Rimm, D. L., Dodson, A., Acs, B., Badve, S., Denkert, C., Ellis, M. J., Fineberg, S., Flowers, M., Kreipe, H. H., Laenkholm, A.-V., Pan, H., Penault-Llorca, F. M., Polley, M.-Y., Salgado, R., Smith, I. E., Sugie, T., Bartlett, J. M. S., . . . Hayes, D. F. (2021). Assessment of Ki67 in breast cancer: Updated recommendations from the International Ki67 in Breast Cancer Working Group. *Journal of the National Cancer Institute, 113*(7), 808–819. https://doi.org/10.1093/jnci/djaa201 (PMID 33369635; PMCID PMC8487652)
- Piccart, M., van 't Veer, L. J., Poncet, C., Lopes Cardozo, J. M. N., Delaloge, S., Pierga, J.-Y., Vuylsteke, P., Brain, E., Vrijaldenhoven, S., Neijenhuis, P. A., Causeret, S., Smilde, T. J., Viale, G., Glas, A. M., Delorenzi, M., Sotiriou, C., Rubio, I. T., Kümmel, S., Zoppoli, G., . . . Rutgers, E. J. T. (2021). 70-gene signature as an aid for treatment decisions in early breast cancer: Updated results of the phase 3 randomised MINDACT trial with an exploratory analysis by age. *The Lancet Oncology, 22*(4), 476–488. https://doi.org/10.1016/S1470-2045(21)00007-3 (PMID 33721561)
- Schmid, P., Cortes, J., Pusztai, L., McArthur, H., Kümmel, S., Bergh, J., Denkert, C., Park, Y. H., Hui, R., Harbeck, N., Takahashi, M., Foukakis, T., Fasching, P. A., Cardoso, F., Untch, M., Jia, L., Karantza, V., Zhao, J., Aktan, G., . . . O'Shaughnessy, J. (2020). Pembrolizumab for early triple-negative breast cancer. *The New England Journal of Medicine, 382*(9), 810–821. https://doi.org/10.1056/NEJMoa1910549 (PMID 32101663)
- Sparano, J. A., Gray, R. J., Makower, D. F., Pritchard, K. I., Albain, K. S., Hayes, D. F., Geyer, C. E., Dees, E. C., Perez, E. A., Olson, J. A., Zujewski, J., Lively, T., Badve, S. S., Saphner, T. J., Wagner, L. I., Whelan, T. J., Ellis, M. J., Paik, S., Wood, W. C., . . . Sledge, G. W. (2015). Prospective validation of a 21-gene expression assay in breast cancer. *The New England Journal of Medicine, 373*(21), 2005–2014. https://doi.org/10.1056/NEJMoa1510764 (PMID 26412349; PMCID PMC4701034)
- Sparano, J. A., Gray, R. J., Makower, D. F., Pritchard, K. I., Albain, K. S., Hayes, D. F., Geyer, C. E., Dees, E. C., Goetz, M. P., Olson, J. A., Lively, T., Badve, S. S., Saphner, T. J., Wagner, L. I., Whelan, T. J., Ellis, M. J., Paik, S., Wood, W. C., Ravdin, P. M., . . . Sledge, G. W. (2018). Adjuvant chemotherapy guided by a 21-gene expression assay in breast cancer. *The New England Journal of Medicine, 379*(2), 111–121. https://doi.org/10.1056/NEJMoa1804710 (PMID 29860917; PMCID PMC6172658)
- Sparano, J. A., Gray, R. J., Ravdin, P. M., Makower, D. F., Pritchard, K. I., Albain, K. S., Hayes, D. F., Geyer, C. E., Dees, E. C., Goetz, M. P., Olson, J. A., Lively, T., Badve, S. S., Saphner, T. J., Wagner, L. I., Whelan, T. J., Ellis, M. J., Paik, S., Wood, W. C., . . . Sledge, G. W. (2019). Clinical and genomic risk to guide the use of adjuvant therapy for breast cancer. *The New England Journal of Medicine, 380*(25), 2395–2405. https://doi.org/10.1056/NEJMoa1904819 (PMID 31157962; PMCID PMC6709671)
- Sung, P.-L., Wen, K.-C., Chen, Y.-J., Chao, T.-C., Tsai, Y.-F., Tseng, L.-M., Qiu, J.-T. T., Chao, K.-C., Wu, H.-H., Chuang, C.-M., Wang, P.-H., & Huang, C.-Y. F. (2017). The frequency of cancer predisposition gene mutations in hereditary breast and ovarian cancer patients in Taiwan: From BRCA1/2 to multi-gene panels. *PLoS ONE, 12*(9), Article e0185615. https://doi.org/10.1371/journal.pone.0185615 (PMID 28961279; PMCID PMC5621677)
- Tang, C.-H., Newson, R. S., Lin, C.-H., Chan, B. H.-F., Wang, B. C., Shen, S.-P., & Shao, S. Y.-J. (2024). The epidemiology, treatments and outcomes of patients with hormone receptor positive, human epidermal growth factor receptor 2 negative, node-positive early breast cancer in Taiwan. *Future Oncology, 20*(37), 2983–2992. https://doi.org/10.1080/14796694.2024.2407282 (PMID 39365110; PMCID PMC11572189)
- Turner, N. C., Oliveira, M., Howell, S. J., Dalenc, F., Cortes, J., Gomez Moreno, H. L., Hu, X., Jhaveri, K., Krivorotko, P., Loibl, S., Morales Murillo, S., Okera, M., Park, Y. H., Sohn, J., Toi, M., Tokunaga, E., Yousef, S., Zhukova, L., de Bruin, E. C., . . . Rugo, H. S. (2023). Capivasertib in hormone receptor–positive advanced breast cancer. *The New England Journal of Medicine, 388*(22), 2058–2070. https://doi.org/10.1056/NEJMoa2214131 (PMID 37256976; PMCID PMC11335038)
- Wolff, A. C., Hammond, M. E. H., Allison, K. H., Harvey, B. E., Mangu, P. B., Bartlett, J. M. S., Bilous, M., Ellis, I. O., Fitzgibbons, P., Hanna, W., Jenkins, R. B., Press, M. F., Spears, P. A., Vance, G. H., Viale, G., McShane, L. M., & Dowsett, M. (2018). Human epidermal growth factor receptor 2 testing in breast cancer: American Society of Clinical Oncology/College of American Pathologists clinical practice guideline focused update. *Journal of Clinical Oncology, 36*(20), 2105–2122. https://doi.org/10.1200/JCO.2018.77.8738 (PMID 29846122)
- Wolff, A. C., Somerfield, M. R., Dowsett, M., Hammond, M. E. H., Hayes, D. F., McShane, L. M., Saphner, T. J., Spears, P. A., & Allison, K. H. (2023). Human epidermal growth factor receptor 2 testing in breast cancer: ASCO–College of American Pathologists guideline update. *Journal of Clinical Oncology, 41*(22), 3867–3872. https://doi.org/10.1200/JCO.22.02864 (PMID 37284804)
- Yang, X., Leslie, G., Doroszuk, A., Schneider, S., Allen, J., Decker, B., Dunning, A. M., Redman, J., Scarth, J., Plaskocinska, I., Luccarini, C., Shah, M., Pooley, K., Dorling, L., Lee, A., Adank, M. A., Adlard, J., Aittomäki, K., Andrulis, I. L., . . . Tischkowitz, M. (2020). Cancer risks associated with germline PALB2 pathogenic variants: An international study of 524 families. *Journal of Clinical Oncology, 38*(7), 674–685. https://doi.org/10.1200/JCO.19.01907 (PMID 31841383; PMCID PMC7049229)
- Yao, M. M.-S., Vy, V. P. T., Chen, T. H.-H., Hsu, H.-H., Hsu, G.-C., Lee, C. S., Lin, L.-J., Chia, S.-L., Wu, C.-C., Chan, W. P., & Yen, A. M.-F. (2023). Performance measures of 8,169,869 examinations in the National Breast Cancer Screening Program in Taiwan, 2004–2020. *BMC Medicine, 21*(1), Article 497. https://doi.org/10.1186/s12916-023-03217-7 (PMID 38102671; PMCID PMC10724902)
- Yen, A. M.-F., Tsau, H.-S., Fann, J. C.-Y., Chen, S. L.-S., Chiu, S. Y.-H., Lee, Y.-C., Pan, S.-L., Chiu, H.-M., Kuo, W.-H., Chang, K.-J., Wu, Y.-Y., Chuang, S.-L., Hsu, C.-Y., Chang, D.-C., Koong, S.-L., Wu, C.-Y., Chia, S.-L., Chen, M.-J., Chen, H.-H., & Chiou, S.-T. (2016). Population-based breast cancer screening with risk-based and universal mammography screening compared with clinical breast examination: A propensity score analysis of 1 429 890 Taiwanese women. *JAMA Oncology, 2*(7), 915–921. https://doi.org/10.1001/jamaoncol.2016.0447 (PMID 27030951)

Secondary source used only for one AJCC illustration (Chinese luminal B-like validation, n = 407): Cancer Management and Research, 2022, PMCID PMC8881011. Full APA reference not built: [UNVERIFIED citation details].

---

## Critic additions

Added 2026-10-29 by the completeness critic (append only; nothing above was changed). Additions for other chapter sections are in the "Critic additions" sections of breast_2 (local therapy, HER2 adjuvant foundations, pCR), breast_3 (ABC definitions, brain metastases, breast-specific emergencies, everolimus, eribulin) and breast_4 (re-check of high-stakes numbers, Taiwan licences).

### CA1.1 AJCC 8th edition TNM: the actual definitions (gap: the notes had only the anatomic/prognostic concept) [VERIFIED]

Source: NCI PDQ "Breast Cancer Treatment – Health Professional Version", page updated 2025-04-25, Tables 2–8, which are "reprinted with permission from AJCC: Breast, revised version … AJCC Cancer Staging Manual, 8th ed., 2017". Downloaded from cancer.gov 2026-10-29. This is the official NCI reproduction of the AJCC tables; the AJCC manual itself was not opened.

**Primary tumour (T), clinical and pathological**

| T | Definition |
|---|---|
| Tis (DCIS) | Ductal carcinoma in situ. **LCIS is a benign entity and is removed from TNM staging in the 8th edition** (table footnote) — this upgrades the [PARTIAL] note in §7 to [VERIFIED] |
| Tis (Paget) | Paget disease of the nipple **not** associated with invasive carcinoma and/or DCIS in the underlying parenchyma |
| T1 | ≤20 mm. T1mi ≤1 mm; T1a >1–5 mm (round any measurement >1.0–1.9 mm up to 2 mm); T1b >5–10 mm; T1c >10–20 mm |
| T2 | >20 mm but ≤50 mm |
| T3 | >50 mm |
| T4 | Any size with direct extension to the chest wall and/or skin (ulceration or macroscopic nodules). **Invasion of the dermis alone does not qualify as T4** |
| T4a | Extension to the chest wall. **Invasion or adherence to pectoralis muscle alone does not qualify** |
| T4b | Ulceration and/or ipsilateral macroscopic satellite nodules and/or skin oedema (including peau d'orange) not meeting the criteria for inflammatory carcinoma |
| T4c | T4a + T4b |
| T4d | Inflammatory carcinoma |

- The clinical criteria for inflammatory carcinoma (extent of erythema/oedema) are in an AJCC rule that the PDQ page does not reproduce; the IBC consensus paper (Dawood 2011, PMC3105293) was available as abstract only. **The "≥1/3 of the breast skin" criterion therefore remains [UNVERIFIED].**

**Regional nodes, clinical (cN)**

| cN | Definition |
|---|---|
| cN0 | No regional nodal metastasis (imaging or clinical examination) |
| cN1 | Movable ipsilateral level I–II axillary node(s). cN1mi (rarely used): micrometastasis, about 200 cells, >0.2 mm but ≤2.0 mm |
| cN2a | Ipsilateral level I–II axillary nodes fixed to one another (matted) or to other structures |
| cN2b | Ipsilateral internal mammary nodes only, without axillary metastasis |
| cN3a | Ipsilateral infraclavicular (level III) node(s) |
| cN3b | Ipsilateral internal mammary **and** axillary node(s) |
| cN3c | Ipsilateral supraclavicular node(s) |

- Suffixes: (sn) = confirmed by sentinel node biopsy; (f) = confirmed by FNA or core biopsy. A node proven by FNA/core before neoadjuvant therapy is cN1(f) regardless of the size of the deposit later found.

**Regional nodes, pathological (pN)**

| pN | Definition |
|---|---|
| pN0 | No metastasis, or isolated tumour cells (ITCs) only. pN0(i+): ITCs ≤0.2 mm. pN0(mol+): RT-PCR positive, no ITCs |
| pN1mi | Micrometastases (~200 cells, >0.2 mm but ≤2.0 mm) |
| pN1a | 1–3 axillary nodes, at least one metastasis >2.0 mm |
| pN1b | Ipsilateral internal mammary sentinel nodes (excluding ITCs) |
| pN1c | pN1a + pN1b |
| pN2a | 4–9 axillary nodes (at least one deposit >2.0 mm) |
| pN2b | Clinically detected internal mammary nodes, with pathologically negative axillary nodes |
| pN3a | ≥10 axillary nodes, or infraclavicular (level III) nodes |
| pN3b | pN1a or pN2a with cN2b (internal mammary positive by imaging), or pN2a with pN1b |
| pN3c | Ipsilateral supraclavicular nodes |

**Distant metastasis (M)**
- M0: no clinical or radiographic evidence. **Imaging is not required to assign cM0.**
- cM0(i+): tumour cells or deposits ≤0.2 mm in blood, marrow or non-regional nodal tissue, without symptoms or signs.
- cM1: clinical/radiographic distant metastasis. pM1: histologically proven, or non-regional node metastasis >0.2 mm.

**Histological grade (Nottingham modification of Scarff-Bloom-Richardson)** — **upgrades §4.4 from [PARTIAL] to [VERIFIED]**
- G1: SBR score **3–5**; G2: **6–7**; G3: **8–9**.
- DCIS uses **nuclear grade** (G1 low, G2 intermediate, G3 high), not the SBR score.

**Anatomic stage groups (AJCC 8th, Table 8)**

| Stage | TNM |
|---|---|
| 0 | Tis N0 M0 |
| IA | T1 N0 M0 |
| IB | T0 N1mi M0; T1 N1mi M0 |
| IIA | T0 N1 M0; T1 N1 M0; T2 N0 M0 |
| IIB | T2 N1 M0; T3 N0 M0 |
| IIIA | T0 N2; T1 N2; T2 N2; T3 N1; T3 N2 (all M0) |
| IIIB | T4 N0; T4 N1; T4 N2 (all M0) |
| IIIC | Any T, N3, M0 |
| IV | Any T, any N, M1 |

Staging rules printed with the table (useful for MCQs):
- T1 includes T1mi. T0/T1 with N1mi = IB; T2–T4 with N1mi are staged with the N1 category.
- **pM0 is not a valid designation; any M0 is clinical.**
- M1 before neoadjuvant therapy = stage IV, and stays IV regardless of response.
- Stage may be changed if post-surgical imaging within **4 months** of diagnosis shows distant metastasis (no progression, no neoadjuvant therapy).
- After neoadjuvant therapy, use yc/yp prefixes. **No anatomic stage group is assigned after pCR (ypT0 ypN0 cM0).** Neoadjuvant therapy does not change the clinical (pretreatment) stage.
- In the US, registries must report the **clinical and pathological prognostic** stage groups; the anatomic table is for regions without routine grade/ER/PR/HER2. Patients given neoadjuvant therapy get a clinical prognostic stage, not a pathological prognostic stage.

Caveat: the same PDQ page summarises HER2 ISH with an "equivocal" category (2013-style wording). That conflicts with the 2018/2023 ASCO/CAP groups in §4.2. **Do not copy the PDQ HER2 block; use §4.2.** The Oncotype RS <11 → stage IA rule (§7) is not in the PDQ tables I read and stays [PARTIAL].

### CA1.2 Survivorship follow-up after curative treatment (gap) [VERIFIED; A]

ASCO 2013 update (Khatcheressian 2013; no change from 2006):
- History and physical examination every **3–6 months for years 1–3**, every **6–12 months for years 4–5**, then **annually**.
- After breast-conserving surgery: first post-treatment mammogram **1 year after the initial mammogram and at least 6 months after radiotherapy**, then yearly.
- **Not recommended** for routine follow-up of an asymptomatic patient with a normal examination: CBC, chemistry panels, bone scan, chest radiograph, liver or pelvic ultrasound, CT, FDG-PET, MRI, and tumour markers (CEA, CA 15-3, CA 27.29).

### CA1.3 Male breast cancer (gap: Taiwan had 67 male cases in 2023, §1.1) [VERIFIED; A]

ASCO 2020 (Hassett 2020):
- Adjuvant endocrine therapy: **tamoxifen** for an initial 5 years. If tamoxifen is contraindicated: **GnRH agonist/antagonist + AI**. Another 5 years may be offered if still high risk and tolerated.
- No adjuvant bone-modifying agents to prevent recurrence in men (may be used for osteoporosis).
- Advanced disease: endocrine therapy first line unless visceral crisis or rapidly progressive disease. Targeted therapies as in women.
- Imaging: annual **ipsilateral** mammogram after lumpectomy; contralateral annual mammogram may be offered to carriers of a predisposing variant. Routine breast MRI not recommended.
- **Genetic counselling and germline testing should be offered to all men with breast cancer** (consistent with NCCN in §3.4).
- ABC 5 (Cardoso 2020) [VERIFIED; FT]: for ER-positive male ABC, tamoxifen is the preferred endocrine option; if an AI is needed, give it with an LHRH agonist or orchiectomy.

### CA1.4 Still not verified after this pass
1. IBC clinical diagnostic criteria (erythema/oedema extent, duration).
2. The AJCC Oncotype-based prognostic stage rule (RS <11).
3. The cell-level clinical and pathological prognostic stage grids (PDQ Tables 9–10 exist but were not transcribed here; transcribe from PDQ if the chapter needs them).

### CA1 references (APA 7)
- PDQ® Adult Treatment Editorial Board. (2025, April 25). *Breast cancer treatment (PDQ®): Health professional version* (Tables 2–8 reprinted from the AJCC Cancer Staging Manual, 8th ed.). National Cancer Institute. Retrieved October 29, 2026, from https://www.cancer.gov/types/breast/hp/breast-treatment-pdq
- Cardoso, F., Paluch-Shimon, S., Senkus, E., Curigliano, G., Aapro, M. S., André, F., Barrios, C. H., Bergh, J., Bhattacharyya, G. S., Biganzoli, L., Boyle, F., Cardoso, M.-J., Carey, L. A., Cortés, J., El Saghir, N. S., Elzayat, M., Eniu, A., Fallowfield, L., Francis, P. A., . . . Winer, E. P. (2020). 5th ESO-ESMO international consensus guidelines for advanced breast cancer (ABC 5). *Annals of Oncology, 31*(12), 1623–1649. https://doi.org/10.1016/j.annonc.2020.09.010 (PMID 32979513; PMCID PMC7510449)
- Hassett, M. J., Somerfield, M. R., Baker, E. R., Cardoso, F., Kansal, K. J., Kwait, D. C., Plichta, J. K., Ricker, C., Roshal, A., Ruddy, K. J., Safer, J. D., Van Poznak, C., Yung, R. L., & Giordano, S. H. (2020). Management of male breast cancer: ASCO guideline. *Journal of Clinical Oncology, 38*(16), 1849–1863. https://doi.org/10.1200/JCO.19.03120 (PMID 32058842)
- Khatcheressian, J. L., Hurley, P., Bantug, E., Esserman, L. J., Grunfeld, E., Halberg, F., Hantel, A., Henry, N. L., Muss, H. B., Smith, T. J., Vogel, V. G., Wolff, A. C., Somerfield, M. R., & Davidson, N. E. (2013). Breast cancer follow-up and management after primary treatment: American Society of Clinical Oncology clinical practice guideline update. *Journal of Clinical Oncology, 31*(7), 961–965. https://doi.org/10.1200/JCO.2012.45.9859 (PMID 23129741)
