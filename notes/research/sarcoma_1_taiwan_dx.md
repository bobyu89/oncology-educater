# Sarcoma 1. Bone sarcoma and soft tissue sarcoma (including GIST): Taiwan epidemiology, age patterns, risk factors, diagnostic principles, grading and molecular hallmarks, staging and GIST risk stratification — fact-check report

Fact-check date: 2026-10-29. Prepared for the Taiwanese oncology NP (專科護理師) handbook, sarcoma chapter (ward practice and 專師甄審).

Confidence tags:
- **[VERIFIED]**: confirmed in a primary or official source that I opened (journal abstract or PMC full text, official registry workbook or report, nccn.org page or NCCN Guidelines for Patients PDF, NCI PDQ page, official registry staging sheet).
- **[PARTIAL]**: confirmed only in a secondary source, or only part of the claim could be confirmed.
- **[UNVERIFIED]**: could not be confirmed. Do not print without checking.

Values I calculated myself are marked "(computed)". Source tags inline:
- [A] = PubMed abstract (pulled through NCBI E-utilities, same database as the PubMed MCP tools)
- [FT] = PMC full text
- [DS] = official dataset or report I downloaded and parsed (twcr.tw workbooks, TCR long-form report, MOHW cause-of-death workbook)
- [PDQ] = NCI PDQ Health Professional summary on cancer.gov (reproduces AJCC 8th tables "with permission")
- [PG] = NCCN Guidelines for Patients PDF (public; the professional PDFs need a login)
- [REG] = cancer-registry staging material reproducing UICC TNM 8 (NHS England NDRS staging sheet; ICCR dataset; ENCR/UICC training slides)
- [ACS] = American Cancer Society staging page citing AJCC 8th (secondary)

Method and access notes:
- Taiwan numbers come from the Taiwan Cancer Registry (TCR) yearly and period workbooks for "Bones" and "Soft-tissue" (data year 2023, posted 2026-01), and from the 112年 long-form report (CA17_LF112.pdf) already downloaded in this project.
- The ESMO–EURACAN–GENTURIS guideline full texts (annalsofoncology.org), the Tanaka & Ozaki AJCC review (academic.oup.com) and documents.cap.org all returned HTTP 403/502. AJCC 8th tables were therefore checked against NCI PDQ (which reprints AJCC tables), the ACS staging pages, the NHS England NDRS staging sheets (UICC TNM 8) and the ICCR bone dataset (UICC TNM 8 reproduced with permission). The AJCC manual itself was not opened.
- The TFDA licence dataset was not needed: this chapter covers diagnosis and staging, not drugs.
- www.nhi.gov.tw and www.hpa.gov.tw were not used (unreachable).

---

## 0. Corrections and flags for the editor (read first)

1. **The TCR "soft tissue" figure is not "all soft tissue sarcomas".**
   - The TCR site category 結締組織軟組織癌 is topography-based (ICD-O-3 **C47 + C49**). In 2023 it had **774 cases** (ASR 2.21/10⁵).
   - By histology across all sites, Taiwan STS incidence (2007–2013) was **ASIR 5.62/10⁵**, and only about **30%** of STS arose in C47/C49 tissues; about **70%** arose in other organs (stomach 15.9%, skin 14.3%, small intestine 10.5%) (Hung 2019) [VERIFIED; A].
   - **GIST was the most common STS subtype in Taiwan (29.2%; ASIR 1.55/10⁵)**, but GIST is registered under its organ (stomach, small bowel, etc.), not under C47/C49.
   - Do not print "774 soft tissue sarcomas per year" as the national sarcoma burden.
2. **Primary bone cancer is not rising in Taiwan.** Annual cases have stayed at about 150–190 since 2005. The 2023 ASR was **0.56/10⁵** (152 cases), down from 0.63 in 2022 [VERIFIED; DS]. Hung 2014 reported a +4.8%/year rise for 2003–2010 [VERIFIED; A]; the later TCR series does not show it continuing (computed from the workbook).
3. **The bone-cancer age curve in Taiwan is bimodal, and the older peak is as high as the adolescent one.**
   - 2019–2023 age-specific rates: 10–14 years **1.11/10⁵**; 75–79 years **1.24/10⁵** [VERIFIED; DS].
   - Girls peak at 10–14 (1.14), boys at 15–19 (1.13) [VERIFIED; DS].
   - In Taiwanese patients aged ≥60, osteosarcoma (24%) and chondrosarcoma (23%) are almost equal, and chordoma is 11% (Hung 2014) [VERIFIED; FT]. Do not teach "elderly bone sarcoma = Paget osteosarcoma" for Taiwan.
4. **AJCC 8th bone staging has no stage groups for spine or pelvis** (T categories only) [VERIFIED; REG + ATM review].
5. **AJCC and UICC disagree on node-positive STS of the trunk/extremity.**
   - AJCC 8th: any T **N1** M0 = **stage IV** for trunk/extremity, but **IIIB** for retroperitoneum [VERIFIED; PDQ; Tanaka & Ozaki abstract].
   - UICC TNM 8: N1 = IIIB at both sites; the NDRS sheet notes "AJCC classifies N1 as stage IV for extremity and superficial trunk" [VERIFIED; REG].
   - State which system the handbook uses (Taiwan registry: AJCC 8th).
6. **Error in an open-access teaching source.** Petriceks & Salmi 2019 (*Academic Pathology* educational case) stages an appendicular T2 N0 M0 G2 osteosarcoma as **IIA** and misprints T2 as "≤8 cm". The correct AJCC 8th group is **IIB**, and T2 is **>8 cm** (ACS; NDRS/UICC) [VERIFIED]. Do not copy that case.
7. **GIST risk schemes are not interchangeable.**
   - The 2025 updated Asian consensus (Japan, Korea, China, **Taiwan**) **recommends the modified NIH (Joensuu) criteria** to select patients for adjuvant imatinib [VERIFIED; FT].
   - It also asks for mitoses per **5 mm²** (≈ "50 HPF") [VERIFIED; FT].
   - Risk schemes **do not apply to SDH-deficient GIST** (Sbaraglia 2021, WHO 2020 review) [VERIFIED; FT].
8. **KIT/PDGFRA frequencies depend on the population studied.**
   - Population-based localized GIST (MolecGIST, France): KIT 71%, PDGFRA 15%.
   - Advanced GIST (MetaGIST): KIT 82.8%, PDGFRA 2.1% [VERIFIED; A].
   - Taiwan advanced/recurrent GIST on TKIs (n≈177 genotyped): KIT exon 11 **76.8%**, exon 9 **10.2%**, PDGFRA **1.7%**, wild-type **9.6%** [VERIFIED; FT].
   - Always state which population a percentage comes from.
9. **NCCN has a separate GIST guideline.** On 2026-10-29 nccn.org listed the following [VERIFIED]:
   - Gastrointestinal Stromal Tumors **Version 1.2026**
   - Soft Tissue Sarcoma **Version 5.2026**
   - Bone Cancer **Version 1.2027**
   - Pediatric Bone Sarcoma Version 1.2027
   - Pediatric Soft Tissue Sarcoma Version 1.2026
   - The STS keyword list on nccn.org still shows "GIST", so cite the GIST guideline for GIST.
   - The patient guides lag behind: the bone guide is based on v1.2026 (11 Sep 2025), the STS guide on v1.2025 (2 May 2025), and the GIST guide on v1.2026 (13 Jan 2026).
10. **The NF1 sarcoma risk differs by source.**
    - NCCN patient guide (STS 2025): "about 5 out of 100" people with NF1 develop STS (MPNST) [VERIFIED; PG].
    - Evans 2002, population-based: **lifetime MPNST risk 8–13%**; median age 26 vs 62 years for sporadic MPNST [VERIFIED; A].
    - Quote the range with both sources.
11. **Paget sarcoma risk.**
    - Malignant transformation is **<1%** (Hansen 2006) and **~0.3%** and falling (Mangham 2009) [VERIFIED; A].
    - One teaching article claims 5–10% for polyostotic disease. Mangham found polyostotic disease **not** a significant risk factor. Do not print 5–10%.
12. **PubMed DOI error for Tzen 2007 (Taiwan GIST incidence).** PubMed's ELocationID 10.1007/BF03033708 belongs to a different paper (*Pathology Oncology Research* 9:13–19). The correct DOI is **10.1007/s10620-006-9480-y** (checked on Crossref) [VERIFIED].
13. **Registry coding change ahead.** TCR notice 癌登第115004號 (2026-04-15): ICD-O-4 coding will be introduced **from 116年 (2027) for cases newly diagnosed in 115年 (2026)** [VERIFIED; twcr.tw]. Sarcoma/GIST morphology and behaviour codes may change; future TCR tables may not be comparable with ICD-O-3 years.
14. **Not found or not openable (marked [UNVERIFIED] below):**
    - a national (short-form, all-hospital) GIST count for 2023
    - a 2023 histology breakdown of Taiwanese bone cancers (latest published is 2003–2010)
    - the ESMO guideline full texts (403)
    - the AJCC 8th manual itself
    - the original Joensuu 2008 table
    - exact population percentages for SS18::SSX and FUS::DDIT3 positivity
    - Enneking's benign stage 1–3 wording

---

## 1. Taiwan epidemiology

### 1.1 Primary bone and joint cancer (骨癌; ICD-O-3 C40–C41), TCR data year 2023 [VERIFIED; DS]

Source: Taiwan Cancer Registry, Year_Bones_2023.xlsx (sheet 170_YEAR_data), https://twcr.tw/wp-content/uploads/2026/01/Year_Bones_2023.xlsx. Invasive cancers, mid-year population, age-standardised to the 2000 WHO world standard. Topography C40–C41 for TCR "primary bone cancer" is stated in Hung 2014, which used TCR data [VERIFIED; FT].

| Year | Cases (both sexes) | ASR /10⁵ | Male cases (ASR) | Female cases (ASR) |
|---|---|---|---|---|
| 2000 | 157 | 0.71 | 82 (0.72) | 75 (0.70) |
| 2005 | 187 | 0.81 | 113 (0.96) | 74 (0.65) |
| 2010 | 172 | 0.75 | 95 (0.83) | 77 (0.66) |
| 2015 | 151 | 0.65 | 84 (0.71) | 67 (0.59) |
| 2019 | 185 | 0.79 | 106 (0.92) | 79 (0.65) |
| 2020 | 168 | 0.69 | 102 (0.79) | 66 (0.60) |
| 2021 | 168 | 0.69 | 89 (0.72) | 79 (0.66) |
| 2022 | 162 | 0.63 | 102 (0.80) | 60 (0.46) |
| **2023** | **152** | **0.56** | **92 (0.64)** | **60 (0.49)** |

- Crude rate 2023: 0.65/10⁵ [DS].
- Male:female ratio 2023: 1.53 (computed).
- Share of all 138,051 new invasive cancers in 2023 (MOHW 112年 total, see breast notes): **0.11%** (computed).
- Bone cancer is not in the MOHW top-15 cancer death lists [VERIFIED; DS, 114年死因統計摘要表].

### 1.2 Connective and soft tissue cancer (結締組織軟組織癌; ICD-O-3 C47, C49), TCR 2023 [VERIFIED; DS]

Source: Year_Soft-tissue_2023.xlsx (sheet 171_YEAR_data), https://twcr.tw/wp-content/uploads/2026/01/Year_Soft-tissue_2023.xlsx. The C47 + C49 definition (connective, subcutaneous and other soft tissues, including peripheral nerves) is stated in Hung 2015, which used TCR data [VERIFIED; FT].

| Year | Cases | ASR /10⁵ | Male (ASR) | Female (ASR) |
|---|---|---|---|---|
| 1990 | 151 | 0.82 | 93 (0.96) | 58 (0.65) |
| 2000 | 366 | 1.61 | 204 (1.76) | 162 (1.46) |
| 2010 | 542 | 1.92 | 299 (2.11) | 243 (1.73) |
| 2015 | 657 | 2.21 | 360 (2.42) | 297 (2.02) |
| 2020 | 689 | 2.11 | 355 (2.20) | 334 (2.05) |
| 2022 | 728 | 2.15 | 402 (2.40) | 326 (1.95) |
| **2023** | **774** | **2.21** | **443 (2.65)** | **331 (1.80)** |

- Crude rate 2023: 3.32/10⁵. Share of all new cancers: 0.56% (computed). Male:female ratio 1.34 (computed).
- Case numbers keep rising, but the ASR has been flat at about 2.0–2.2 since 2013. The rise in counts mostly reflects population ageing (computed from the table).
- **This category excludes visceral sarcomas, GIST, uterine sarcomas, retroperitoneal (C48) sarcomas, skin angiosarcoma, and similar tumours** (see flag 1).

### 1.3 Age-specific incidence, 2019–2023 (per 10⁵ person-years) [VERIFIED; DS]

Sources: Period_Bones_2023.xlsx (sheet 170_AGE_data) and Period_Soft-tissue_2023.xlsx (sheet 171_AGE_data), https://twcr.tw/wp-content/uploads/2026/01/Period_Bones_2023.xlsx and …/Period_Soft-tissue_2023.xlsx.

| Age (years) | Bone, both sexes | Bone, male | Bone, female | Soft tissue (C47/C49), both sexes |
|---|---|---|---|---|
| 0–4 | 0.16 | 0.13 | 0.19 | 0.76 |
| 5–9 | 0.62 | 0.71 | 0.52 | 0.44 |
| **10–14** | **1.11** | 1.08 | **1.14** | 0.69 |
| **15–19** | 0.89 | **1.13** | 0.62 | 1.10 |
| 20–24 | 0.78 | 0.80 | 0.75 | 1.01 |
| 25–29 | 0.43 | 0.41 | 0.44 | 1.34 |
| 30–39 | 0.54 / 0.54 | 0.59 / 0.70 | 0.49 / 0.37 | 1.50 / 1.83 |
| 40–49 | 0.55 / 0.51 | 0.63 / 0.57 | 0.48 / 0.46 | 2.21 / 2.50 |
| 50–59 | 0.66 / 0.80 | 0.89 / 1.02 | 0.44 / 0.58 | 3.08 / 3.72 |
| 60–69 | 0.87 / 1.07 | 1.28 / 1.29 | 0.48 / 0.87 | 4.66 / 5.80 |
| 70–74 | 1.10 | 1.16 | 1.05 | 7.11 |
| **75–79** | **1.24** | **1.73** | 0.84 | 9.30 |
| 80–84 | 0.67 | 0.75 | 0.61 | 9.35 |
| 85+ | 1.03 | 1.42 | 0.76 | **10.53** |

(For the 10-year rows, the two numbers are the two 5-year bands, e.g. 30–34 / 35–39.)

Teaching reading:
- **Bone: bimodal.** One peak at 10–19 (girls earlier than boys, consistent with earlier puberty), a trough at 25–49, and a second rise after 60.
- **Soft tissue (C47/C49): rises steadily with age**, from a trough at 5–9 to more than 10/10⁵ at 85+.

### 1.4 Histology mix in Taiwan (published TCR analyses)

**Primary bone cancer, 2003–2010** (Hung 2014; n = 1,238; ASR 6.70 per million) [VERIFIED; A + FT]:
- All ages: osteosarcoma **45%**, chondrosarcoma **18%**, Ewing sarcoma **8%**. Median age at diagnosis 39 years.
- Ages 0–24 (Group I): osteosarcoma about two-thirds, Ewing 13%, chondrosarcoma 6%.
- Ages 25–59 (Group II): osteosarcoma 30%, chondrosarcoma 29%; chordoma third.
- Ages ≥60 (Group III): osteosarcoma 24%, chondrosarcoma 23%, chordoma 11%. ASR in Group III was **10.28 per million**, higher than Group I (7.00).
- Osteosarcoma peaked at 10–19 years in both sexes. Ewing sarcoma peaked earlier (girls 5–9 years). Chondrosarcoma rose steadily with age.
- Male predominance overall (M/F SRR 1.22), and strongest for chondrosarcoma, chordoma and malignant ameloblastoma.

**Soft tissue sarcoma of the extremities and trunk wall, 2003–2011** (Hung 2015; n = 3,843; ASR 1.63/10⁵) [VERIFIED; A + FT]:
- Liposarcoma 23%, undifferentiated pleomorphic sarcoma (UPS) 18.9%, leiomyosarcoma 7.6%.
- Median age 51 years (2003) and 56 years (2011).
- Peripheral PNET (Ewing family) highest in children. Rhabdomyosarcoma bimodal.

**All-site STS by histology, 2007–2013** (Hung 2019; n = 11,393; ASIR **5.62/10⁵**) [VERIFIED; A]:
- GIST **29.2%** (ASIR 1.55), liposarcoma 11.5% (0.63), leiomyosarcoma 9.7% (0.53).
- Incidence rises with age and peaks after 75. Male:female SRR 1.2.
- Taiwan has **more angiosarcoma**, and less leiomyosarcoma and Kaposi sarcoma, than Western registries.
- GIST cases ≈ 3,327 (computed: 29.2% × 11,393).

**Taiwan vs France, 2013–2016** (Chen 2022) [VERIFIED; A]:
- Angiosarcoma (5.4 vs 2.8 per million) and MPNST (2.0 vs 1.0) were higher in Taiwan.
- Liposarcoma, leiomyosarcoma and synovial sarcoma were higher in France.
- Taiwanese patients had more **liver angiosarcoma** (OR 10.72) and **uterine leiomyosarcoma** (OR 3.21).

**Ultrarare sarcomas, TCR 2002–2019** (Lee 2026) [VERIFIED; A]:
- Ultrarare sarcomas were 0.23% of all cancers (n = 3,690). The commonest were conventional chordoma and extraskeletal Ewing sarcoma.
- Overall survival was worse than for other sarcomas (HR 1.86).

### 1.5 GIST in Taiwan

**TCR 112年 long-form database, gastric GIST (表八之二)** [VERIFIED; DS]
- Source: CA17_LF112.pdf, pp. 50–51, https://twcr.tw/wp-content/uploads/2025/12/CA17_LF112.pdf.
- Long-form data cover the 106 long-form reporting hospitals, not the whole nation.

| Item, 2023 gastric GIST | Value |
|---|---|
| Cases | **915** (441 male, 474 female) |
| Age | none under 25; 60–64: 16.8%, 65–69: 17.2%, 70–74: 16.0%. **72.1% aged ≥60** (computed) |
| Combined stage (整併期別, AJCC 8th) | I **71.8%**, II 10.3%, III 7.7%, IV 3.9%, unknown 6.3% |
| First-course treatment | surgery alone **74.9%**; surgery + targeted therapy **16.5%**; targeted therapy alone 6.5%; palliative 0.4% |

- GIST rows in other long-form site tables (2023) [VERIFIED; DS]: oesophagus 9 (0.34% of oesophageal cancers), colon 11 (0.11%), rectum 49 (0.76%).
- Small intestine is not a long-form site, so no small-bowel GIST figure exists in this report.
- Long-form GIST total for these four sites: 984 (computed; excludes small bowel and other sites).
- **National all-hospital GIST count for 2023: [UNVERIFIED]** (not published in the MOHW release or the TCR workbooks).

**Other Taiwan GIST data**
- Tzen 2007 (single-centre extrapolation, 1998–2004): an estimated **13.74 per million** per year (≈304 cases/year). About 35% of GISTs were misdiagnosed without CD117 IHC, and about 15% without mutation testing [VERIFIED; A]. Hung 2019's population ASIR of 1.55/10⁵ (= 15.5 per million) is of the same order (computed comparison).
- Asian consensus 2025: GIST annual incidence about **1–2 per 100,000** [VERIFIED; FT].
- PDQ: geographically, GIST is most prevalent in China (Shanghai), **Taiwan**, Korea and Norway [VERIFIED; PDQ].

**Advanced/recurrent GIST on TKIs, TCOG registry 2010–2020** (Tsai 2024; n = 224) [VERIFIED; A + FT]:
- Median age 57.8 years. Stomach 37.9%, small intestine 43.3%.
- Genotype (≈177 tested): KIT exon 11 76.8%, exon 9 10.2% (17/18 were the 502–503 duplication), PDGFRA 1.7% (2 of 3 were D842V), wild-type 9.6%.
- 48-month PFS and OS on imatinib: 50.5% and 79.5%.
- KIT exon 9 and PDGFRA mutations were adverse for PFS.
- Taiwan reimbursement start dates: imatinib 2002, sunitinib 2010, regorafenib 2016 (as stated in the paper) [VERIFIED; FT].

### 1.6 Mortality (MOHW 114年 / 2025 cause-of-death statistics) [VERIFIED; DS]

- Among women, **間皮和軟組織癌 (ICD-10 C45–C49)** ranked **15th** among cancer deaths: **305 deaths**, crude rate 2.57/10⁵, age-standardised 1.25/10⁵ (2024: 284).
- Source: 114年死因統計結果摘要表, 表13 and 表30, https://www.mohw.gov.tw/dl-100920-e5938c74-aa2a-4994-a15c-054787318303.html.
- Caveat: C45–C49 includes mesothelioma (C45), Kaposi sarcoma (C46) and retroperitoneum/peritoneum (C48). It is not the same as TCR C47/C49 incidence.
- Bone (C40–C41) and male C45–C49 deaths were not in the top-15 lists.

### 1.7 Taiwan osteosarcoma outcomes (context) [VERIFIED; A]

Chu 2026 (TCR 2013–2022; n = 371):
- High AJCC stage (III–IV vs I–II): HR 1.94 for death.
- Low-grade histology: HR 0.31. Limb-salvage surgery: HR 0.38.
- Older age: worse survival.
- Patients diagnosed from 2018 were staged with the AJCC 8th edition.

---

## 2. Age patterns by histotype (international comparators)

| Tumour | Age pattern | Source |
|---|---|---|
| **Osteosarcoma** | Bimodal. Primary peak at 0–24 years, plateau at 25–59, **second peak at ≥60**. The adolescent peak is earlier in girls (age 12) than boys (age 16). Elderly peak at 77–79 years. In patients ≥60, Paget-associated or post-cancer (secondary) osteosarcoma made up about **34%** of cases (SEER 1973–2004). | Mirabello 2009 [VERIFIED; A + FT] |
| Osteosarcoma, children | 5.4 per million per year at ages 0–19 (US NCCR). More than 50% arise around the knee. | PDQ osteosarcoma [VERIFIED; PDQ] |
| **Ewing sarcoma** | US ages <20: 3.0 per million. Age-specific: 5–9 years 2.3, **10–14 years 4.3, 15–19 years 4.5** per million. About 9-fold more common in White than Black people, intermediate in Asian people. Male 58–59%. Sites: pelvis 18%, extraosseous/soft tissue 19%, rib 11%, femur 11%. About 25% are metastatic at diagnosis. | PDQ Ewing [VERIFIED; PDQ]; Jawad 2009 (race-specific incidence) [VERIFIED; A] |
| **Chondrosarcoma** | Adult disease; incidence rises steadily with age (Taiwan). Only 6% of bone cancers at ages 0–24, vs 29% at 25–59 and 23% at ≥60. Male predominance (M/F SRR 2.33 in Group II). Japan national registry 2016–2019: 1,015 cases, age-adjusted incidence 0.159/10⁵. Commonest sites: thigh bone, arm, pelvis. | Hung 2014 [VERIFIED; FT]; Kondo 2025 [VERIFIED; A]; NCCN patient guide [VERIFIED; PG] |
| Giant cell tumour of bone (usually benign, locally aggressive) | Ages 20–40, after skeletal maturity. Knee most common. | NCCN patient guide [VERIFIED; PG] |
| **Adult STS** | Incidence rises with age (Taiwan peak at >75). Adult distribution: extremities 45%, intra-abdominal 38%, trunk 10%, head and neck 5%. | Hung 2019 [VERIFIED; A]; PDQ STS [VERIFIED; PDQ] |
| **GIST** | Usually >50 years; <1% in children (almost all gastric). Site distribution: stomach 60%, jejunum/ileum 30%, duodenum 4–5%, rectum 4%, colon/appendix 1–2%, oesophagus <1%. | Miettinen & Lasota 2006 [VERIFIED; A]; PDQ GIST [VERIFIED; PDQ] |
| SDH-deficient GIST | Children and young adults, female predominance (>2:1). Nearly all gastric GISTs in patients <20 years are SDH-deficient. | Miettinen 2011 [VERIFIED; A] |

---

## 3. Risk factors

Most sarcomas are sporadic (PDQ STS) [VERIFIED; PDQ].

| Risk factor | Key verified facts | Source |
|---|---|---|
| **Li-Fraumeni syndrome (germline TP53)** | Core cancers: STS, **osteosarcoma**, adrenocortical carcinoma, CNS tumours, very-early-onset breast cancer (<31 years). | Frebourg 2020 (ERN GENTURIS guideline) [VERIFIED; FT] |
| | Modified Chompret criteria for testing: (a) familial: proband with a core tumour <46 years plus a first/second-degree relative with a core tumour <56 years; (b) multiple primaries; (c) rare tumours (adrenocortical carcinoma, choroid plexus carcinoma, anaplastic embryonal rhabdomyosarcoma) regardless of family history; (d) breast cancer <31 years. Also test: **jaw osteosarcoma**, and a second primary inside the radiotherapy field of a first core tumour diagnosed <46 years. | Frebourg 2020 [VERIFIED; FT] |
| | Cumulative incidence by age 70 in TP53 carriers (NCI LFS cohort). Females: breast 54%, STS **15%**, brain 6%, osteosarcoma **5%**. Males: STS **22%**, brain 19%, osteosarcoma **11%**. Osteosarcoma hazard is highest before age 10 to adolescence. | Mai 2016 [VERIFIED; A + FT] |
| | Germline TP53 found in 3–9.5% of young osteosarcoma patients across studies. Osteosarcoma is the most common sarcoma in LFS at ages 6–19; rhabdomyosarcoma at ≤5 years. | PDQ osteosarcoma [VERIFIED; PDQ] |
| **Hereditary retinoblastoma (germline RB1, 13q14)** | Subsequent cancer risk: hereditary SIR **19** vs non-hereditary 1.2. Radiotherapy raises it a further **3.1-fold**. Cumulative incidence of a new cancer 50 years after Rb diagnosis: **36%** (hereditary) vs 5.7%. Sarcomas are among the persisting excess cancers. | Kleinerman 2005 [VERIFIED; A] |
| | The hereditary form increases the risk of leiomyosarcoma and bone sarcoma. | NCCN patient guide STS 2025 [VERIFIED; PG]; PDQ osteosarcoma Table 2 [VERIFIED; PDQ] |
| **Neurofibromatosis type 1 (NF1)** | MPNST lifetime risk **8–13%**; median age 26 years (vs 62 sporadic); 5-year survival 21% vs 42% sporadic. | Evans 2002 [VERIFIED; A] |
| | "About 5 out of 100" people with NF1 develop STS (mostly MPNST). | NCCN patient guide [VERIFIED; PG] (see flag 10) |
| | NF1 also predisposes to (multiple) **small-intestinal GISTs**, which are KIT/PDGFRA wild-type. | Miettinen & Lasota 2006 [VERIFIED; A]; PDQ GIST [VERIFIED; PDQ] |
| **Prior radiotherapy** | Radiation-associated STS (MSKCC, 130 of 7,649 STS): 83% high grade, 87% deep, 61.5% truncal. **Median latency 10 years (1.3–74).** Worse disease-specific survival than sporadic STS (HR 1.7). | Gladdy 2010 [VERIFIED; A] |
| | Listed as a risk factor for STS. | PDQ STS [VERIFIED; PDQ] |
| | Radiation-associated osteosarcoma "approximately 3%" of osteosarcomas. | Petriceks 2019 [PARTIAL; teaching article] |
| **Paget disease of bone** | Osteosarcoma complicates **<1%** of PDB, mostly in long-standing polyostotic disease, in the 7th decade. The late osteosarcoma peak is absent where Paget's is rare. | Hansen 2006 [VERIFIED; A] |
| | Pagetic sarcoma now about **0.3%** of PDB. Mean age 73.8 years; 42% had known Paget's beforehand. Median survival 0.66 years. Polyostotic disease is not an independent risk factor. Fell from 23% to 8% of bone-sarcoma referrals aged >50 (1986–95 vs 1996–2005). | Mangham 2009 [VERIFIED; A] |
| | SEER: osteosarcoma with Paget's was 2% of all osteosarcomas; 5-year survival 18.9%. | Mirabello 2009 [VERIFIED; FT] |
| | Taiwan relevance: Paget disease is rarely reported in Taiwan. The Taiwanese elderly bone-cancer peak is mostly chondrosarcoma/chordoma/osteosarcoma, not pagetic sarcoma. | [PARTIAL; inference from Hansen 2006 + Hung 2014] |
| Other osteosarcoma syndromes | Rothmund-Thomson (RECQL4), Bloom (BLM), Werner (WRN), Diamond-Blackfan anaemia (ribosomal protein genes). | PDQ osteosarcoma Table 2 [VERIFIED; PDQ] |
| | **28.0%** of 1,004 osteosarcoma patients unselected for family history carried a P/LP cancer-susceptibility variant; about three-quarters were in autosomal-dominant genes. | Mirabello 2020 [VERIFIED; A] |
| | PDQ quotes this study as 18% in autosomal-dominant genes. | [VERIFIED; PDQ] |
| Other STS syndromes and exposures | Gardner/FAP (APC; desmoid), Gorlin (PTCH1), tuberous sclerosis, Werner. Chronic lymphoedema (lymphangiosarcoma; Stewart–Treves). Thorotrast, vinyl chloride, arsenic (hepatic angiosarcoma). HIV/HHV-8 (Kaposi). | PDQ STS [VERIFIED; PDQ] |
| | Carney–Stratakis syndrome (SDHx germline: gastric GIST + paraganglioma); Lynch syndrome (small STS risk). | NCCN patient guide [VERIFIED; PG] |
| Germline burden in adult sarcoma | International Sarcoma Kindred Study (n = 1,162, including a Korean cohort): 55% of probands carried an excess of pathogenic germline variants. Pathogenic variants were linked to earlier onset (TP53, ATM, ATR, BRCA2, ERCC2). | Ballinger 2016 [VERIFIED; A] |

---

## 4. Diagnostic principles

### 4.1 Imaging

**STS**
- Imaging is usually done **before** biopsy.
- CT vs MRI depends on site; **MRI is preferred for extremities** (and brain, spine, liver). PET is usually combined with CT [VERIFIED; PG STS 2025].
- PDQ STS staging work-up [VERIFIED; PDQ]:
  - MRI and/or CT of the primary site
  - **chest CT for high-grade sarcomas** (lung is the commonest metastatic site)
  - abdominal/pelvic CT
  - PET
  - **CT abdomen/pelvis plus whole-spine MRI for myxoid/round-cell liposarcoma** (extrapulmonary spread to unusual sites)
  - brain imaging for angiosarcoma, epithelioid sarcoma and alveolar soft-part sarcoma
- PDQ also says PET is particularly useful for subtypes prone to nodal spread: synovial, clear cell, angiosarcoma, rhabdomyosarcoma, epithelioid sarcoma.
- Nodal metastasis overall is **<3%** [VERIFIED; PDQ].
- **Intra- vs extracompartmental extension** of extremity sarcoma matters for surgical planning [VERIFIED; PDQ].

**Bone (Ewing work-up, PDQ)** [VERIFIED; PDQ]:
- MRI of the primary site; chest CT; PET; bone scan (PET may replace it); bone-marrow aspirate/biopsy; plain films; CBC; LDH.
- **Imaging of the entire involved bone is standard because of skip metastases (15.8% in one series).**
- Marrow biopsy may be omitted when FDG-PET is used in otherwise localized disease. Pooled marrow involvement: 4.8% overall, and only 1.2% as the sole metastatic site.

**Osteosarcoma**
- Restaging tests listed include chest CT, MRI ± CT of the primary, and FDG-PET/CT or bone scan.
- Baseline ALP and LDH: elevated LDH correlates with poorer outcome.
- Sources: NCCN patient guide bone 2026 [VERIFIED; PG]; PDQ [VERIFIED; PDQ].
- "Whole-bone MRI to exclude skip lesions" for osteosarcoma specifically: [PARTIAL]. It is supported by the AJCC T3 "discontinuous tumours in the primary bone" category and by the PDQ skip-lesion discussion, but I could not open the ESMO text.

**GIST** [VERIFIED; PDQ]:
- CT, MRI, PET and endoscopy.
- **EUS-guided FNA/biopsy is preferred over percutaneous biopsy** because of the risk of haemorrhage and peritoneal seeding.
- For a resectable GIST with classic imaging findings, some surgeons proceed without biopsy.
- Asian consensus 2025 [VERIFIED; FT]:
  - Histological diagnosis is generally required before preoperative or systemic therapy.
  - A small gastric GIST **<2 cm without high-risk features** may be managed by active surveillance.
  - Mutational analysis is recommended when the diagnosis is uncertain or TKIs are planned.

### 4.2 Biopsy

**Preferred technique**
- **Core needle biopsy is preferred** for both bone and soft tissue sarcoma. Incisional (open) biopsy is the alternative [VERIFIED; PG bone 2026 and STS 2025].
- Bone guide: "The biopsy should be performed by an experienced surgeon **at the center where you'll receive treatment**" [VERIFIED; PG].
- STS guide: deep tumours need image guidance (ultrasound or CT); tests should be reviewed at an experienced centre [VERIFIED; PG].
- PDQ STS [VERIFIED; PDQ]:
  - Use image-guided core needle biopsy, or planned incisional biopsy for select cases.
  - An experienced sarcoma pathologist should review the samples.
  - **Careful planning of the initial biopsy, with consultation among surgeon, radiation oncologist and interventional radiologist, avoids compromising curative resection.**
  - Incisional biopsy is reserved for non-diagnostic cores or anatomically unsafe sites.
- PDQ osteosarcoma [VERIFIED; PDQ]: biopsy preferably by a surgeon skilled in limb sparing. "The original biopsy incision placement is crucial. Inappropriate alignment of the biopsy or inadvertent contamination of soft tissues can render subsequent limb-preserving reconstructive surgery impossible."

**Evidence that the biopsy site matters**
- MSTS "hazards of biopsy" (Mankin 1996; 597 patients) [VERIFIED; A]:
  - diagnostic error rate 17.8%
  - a biopsy problem forced a different or more complex treatment in 19.3%
  - outcome changed in 10.1%
  - 18 unnecessary amputations
  - errors and complications were **2–12 times more frequent when the biopsy was done at a referring institution rather than a treatment centre**
- Biopsy-tract seeding (Barrientos-Ruiz 2017; n = 180) [VERIFIED; A]:
  - tract contaminated in **32% of open** vs **0.8% of percutaneous core** biopsies (OR 56)
  - contamination was associated with much shorter local-recurrence-free survival
  - the authors excised the tract with the definitive resection whenever possible
- **Teaching point:** place the needle tract inside the planned resection field so it can be removed en bloc. This rationale is consistent with PDQ and the MSTS data above. The exact ESMO wording ("biopsy tract … should be removed during definitive surgery") could not be opened: [PARTIAL].

**Grading on cores**
- Current grading is **not suitable for core needle biopsies** (risk of under-grading) (Coindre 2006) [VERIFIED; A].

### 4.3 Unplanned excision (the "whoops" operation)

**Definition**
- Unplanned excision = excisional biopsy or resection "without benefit of preoperative imaging and without regard for the necessity to resect the lesion with a margin of normal tissue" (Noria 1996) [VERIFIED; A].
- The colloquial name "whoops" operation is used in the literature (Grignol & Lopez-Aguiar 2022, *Surgical Clinics of North America*) [VERIFIED; A].

**How common, and residual tumour**
- Noria 1996 (65 extremity STS, no gross residual on exam or imaging): residual sarcoma found on re-excision in **35%** [VERIFIED; A].
- Qureshi 2012 [VERIFIED; A]:
  - unplanned excision accounts for **up to 40%** of initial STS operations
  - residual tumour in **48%** of re-excisions
  - local recurrence 23.8% vs 11% in stage-matched planned controls
  - for stage 3 tumours: 37.5% vs 14.2%
- Larios 2024 meta-analysis (16,946 patients; 35.5% unplanned excision) [VERIFIED; A]:
  - worse 5-year local-recurrence-free survival (RR 1.35)
  - residual tumour in the bed (RR 2.59)
  - **no significant difference in 5-year overall survival** (RR 0.90), amputation or plastic reconstruction rates
  - tumour-bed re-excision remains standard

**NP practice points**
- Any deep mass, a mass >5 cm, or a growing mass should be imaged before excision and referred to a sarcoma centre.
- After a "whoops" excision, refer before any further surgery.
- These points restate the evidence above; the specific size/depth triggers are guideline content not opened here: [PARTIAL].

---

## 5. Pathology: grading and molecular hallmarks

### 5.1 FNCLCC histological grade for STS (used by AJCC 8th) [VERIFIED; PDQ reprinting AJCC 8th Tables 4–6; Guillou 1997 A; Coindre 2006 A]

Grade = differentiation score + mitotic count score + necrosis score.

| Parameter | Score |
|---|---|
| Differentiation | 1 = closely resembles normal adult mesenchymal tissue (e.g. well-differentiated liposarcoma / ALT). 2 = histological type certain (e.g. myxoid liposarcoma, myxofibrosarcoma, conventional leiomyosarcoma). 3 = embryonal or undifferentiated, type doubtful, synovial sarcoma, extraskeletal osteosarcoma, Ewing/PNET, UPS, dedifferentiated/pleomorphic/round-cell liposarcoma |
| Mitotic count (per 10 HPF) | 1 = 0–9; 2 = 10–19; 3 = ≥20 |
| Tumour necrosis | 0 = none; 1 = <50%; 2 = ≥50% |
| **Grade** | **G1 = total 2–3; G2 = 4–5; G3 = 6–8** (GX = cannot be assessed) |

- FNCLCC slightly outperformed the NCI system for predicting metastasis and death. Grade discordance between the two systems occurred in 34.6% of cases (Guillou 1997, n = 410) [VERIFIED; A].
- Grading is the best predictor of metastasis in adult STS. It should **not** be applied to tumours of intermediate malignancy or to some entities such as dedifferentiated liposarcoma, and it is not suited to core biopsies (Coindre 2006) [VERIFIED; A].
- **Exam trap:** FNCLCC is **not used for GIST**. GIST uses size, mitoses per 5 mm² (50 HPF), site and rupture (Section 6.4).

### 5.2 Bone tumour grade (WHO 2020, ICCR dataset) [VERIFIED; REG-ICCR]

- **Grade is mostly determined by histotype:**
  - G1: low-grade central osteosarcoma, parosteal osteosarcoma, clear-cell chondrosarcoma
  - G2: periosteal osteosarcoma
  - G3: conventional/telangiectatic/small-cell/secondary/high-grade surface osteosarcoma; UPS of bone; **Ewing sarcoma**; dedifferentiated and mesenchymal chondrosarcoma; dedifferentiated and poorly differentiated chordoma; angiosarcoma
  - Variable: conventional chondrosarcoma (grade 1–3)
  - Not applicable: adamantinoma, conventional chordoma
- **Atypical cartilaginous tumour (ATC) vs chondrosarcoma grade 1:** the same histology is called ATC in the appendicular skeleton (long and short tubular bones; locally aggressive, does not metastasize) but **chondrosarcoma grade 1 in the axial skeleton** (pelvis, scapula, skull base) [VERIFIED; REG-ICCR].
- AJCC 8th bone uses a **three-tier grade**: G1 well differentiated/low grade; G2 moderately differentiated/high grade; G3 poorly differentiated/high grade.
  - Sources: Tanaka & Ozaki 2019 (change to three grades) [VERIFIED; A]; definitions [VERIFIED; ACS + Petriceks FT].

### 5.3 Molecular hallmarks (diagnostic markers)

| Tumour | Hallmark | Notes | Source |
|---|---|---|---|
| **Atypical lipomatous tumour / well-differentiated liposarcoma (ALT/WDLPS) and dedifferentiated liposarcoma (DDLPS)** | **MDM2 amplification (12q13–15), with CDK4 co-amplification**; supernumerary ring/giant marker chromosomes | "Detected in virtually all cases" of ALT/WDLPS (PDQ). FISH (or qPCR) for MDM2/CDK4 is recommended when histology is equivocal: lipoma vs ALT, and undifferentiated sarcoma vs DDLPS. | Sirvent 2007 [VERIFIED; A]; PDQ childhood STS [VERIFIED; PDQ] |
| Pleomorphic liposarcoma | Lacks MDM2 amplification and DDIT3 rearrangement | Disease of older adults | PDQ [VERIFIED] |
| Parosteal (and low-grade central) osteosarcoma | MDM2/CDK4 amplification; absent in conventional osteosarcoma | Taiwan series (Taipei VGH): amplification level rises with dedifferentiation to high grade | Chen PC 2019 [VERIFIED; A]; PDQ (MDM2 amp in ~5% of osteosarcomas overall) |
| Conventional osteosarcoma | Complex karyotype. Biallelic TP53 loss in most cases; RB1 loss; CDKN2A deletion ~20%; MYC and CCNE1 gain ~10% each | No single diagnostic fusion | PDQ osteosarcoma [VERIFIED; PDQ] |
| **Synovial sarcoma** | **t(X;18)(p11.2;q11.2) → SS18::SSX1/SSX2/SSX4** (SS18 was formerly called SYT) | "Specific for synovial sarcoma and found in all morphological subtypes". In the discovery paper the SYT probe detected rearrangement in 10/13 tumours. A population positivity % was not found: [UNVERIFIED]. | Clark 1994 [VERIFIED; A]; PDQ childhood STS [VERIFIED; PDQ] |
| **Ewing sarcoma** | **t(11;22)(q24;q12) → EWSR1::FLI1 in 85–90%**; EWSR1::ERG ~10%; rare ETV1, ETV4, FEV, and FUS partners | **EWSR1 break-apart FISH is negative in FUS-rearranged cases.** WHO 2020 separates "undifferentiated small round cell sarcomas" (CIC-rearranged, BCOR-altered, EWSR1::non-ETS) from Ewing sarcoma. Fusion is somatic, not inherited. | Delattre 1992 [VERIFIED; A]; PDQ Ewing [VERIFIED; PDQ]; Sbaraglia 2021 [VERIFIED; FT]; NCCN patient guide bone [VERIFIED; PG] |
| **Myxoid (round-cell) liposarcoma** | **t(12;16)(q13;p11) → FUS::DDIT3** (FUS was formerly TLS; DDIT3 was formerly CHOP); a minority have **t(12;22) EWSR1::DDIT3** | Extrapulmonary spread to spine, bone and abdomen, hence whole-spine MRI (Section 4.1). An exact % is not stated in the sources opened: [UNVERIFIED]. | Crozat 1993 [VERIFIED; A]; PDQ [VERIFIED; PDQ] |
| Other fusions worth knowing | Solitary fibrous tumour NAB2::STAT6; mesenchymal chondrosarcoma HEY1::NCOA2; NTRK-rearranged spindle cell neoplasm (WHO 2020 emerging entity; NTRK inhibitors) | Table of fusions | PDQ childhood STS [VERIFIED]; Sbaraglia 2021 [VERIFIED; FT] |
| **GIST** | KIT or PDGFRA gain-of-function mutation (mutually exclusive), KIT (CD117) and DOG1 IHC | Detailed in Section 5.4 | Hirota 1998; Heinrich 2003 [VERIFIED; A] |

### 5.4 GIST molecular classes and exon frequencies

**Discovery**
- KIT gain-of-function mutations (Hirota 1998). The proposed cell of origin is the **interstitial cells of Cajal** [VERIFIED; A].
- About 35% of KIT-wild-type GISTs carry **PDGFRA** activating mutations; KIT and PDGFRA mutations are mutually exclusive (Heinrich 2003) [VERIFIED; A].

**IHC**
- About 95% of GISTs are CD117-positive. DOG1 helps for KIT-negative tumours [VERIFIED; PDQ].

**Frequencies (unselected/overall)**

| Class | PDQ (based on AJCC 8th and reviews) [VERIFIED; PDQ] | Asian consensus 2025 [VERIFIED; FT] |
|---|---|---|
| KIT, any | ~80% | 80–85% |
| — **exon 11** (juxtamembrane) | **67%**, all sites | **65–70%**. Deletions/delins involving codons 557–558 have a worse prognosis. |
| — **exon 9** (extracellular) | **10%**; small bowel and colon | ~10%; mostly duodenum, small intestine, rectum. **Imatinib 800 mg** may be considered (advanced setting). |
| — exons 13, 17 (and 8) | ~3% | rare |
| **PDGFRA** | 5–8%. Strong gastric predilection, epithelioid morphology. **Exon 18 in 80–90%, of which D842V is 62%** | D842V is the most common PDGFRA mutation; imatinib-resistant, avapritinib-sensitive |
| KIT/PDGFRA wild-type | 12–15%: SDH-deficient, NF1-related, BRAF V600E, NTRK fusions | — |
| Syndromic | <5% (NF1, Carney triad, familial KIT/PDGFRA) | — |

**Population matters** (see flag 8):
- MolecGIST population-based localized cohort (France, n = 492 genotyped): KIT 71%, PDGFRA 15% [VERIFIED; A].
- Advanced (MetaGIST): KIT 82.8%, PDGFRA 2.1% [VERIFIED; A].
- Taiwan advanced cohort: KIT11 76.8%, KIT9 10.2%, PDGFRA 1.7%, wild-type 9.6% [VERIFIED; FT].

**SDH-deficient GIST**
- 7.5% of unselected gastric GISTs (66/756). Female:male >2:1. Nearly all gastric GISTs in patients <20 years. Often multinodular or plexiform, epithelioid. KIT/DOG1-positive. **SDHB IHC loss.** Lymph-node metastases occur. A chronic course even with metastases. All 378 non-gastric GISTs were SDHB-positive (Miettinen 2011) [VERIFIED; A].
- NIH wild-type clinic (n = 95) (Boikos 2016) [VERIFIED; A]:
  - SDH-deficient in 84 of 95
  - of these, 67% had SDHx mutations (82% germline when tested) and 22% had **SDHC promoter epimutation** (almost all young females, median age 15)
  - SDH-deficient tumours occurred **only in the stomach**
- WHO 2020 review (Sbaraglia 2021) [VERIFIED; FT]:
  - **5–10% of all GIST**
  - SDHx mutation in ~60% (SDHA most often), SDHC methylation ~40%
  - **resistant to TKIs**
  - **conventional risk assessment is not applicable**
- Carney–Stratakis syndrome = germline SDHx (GIST + paraganglioma). Carney triad = SDHC epimutation (gastric GIST + paraganglioma + pulmonary chondroma) [VERIFIED; PDQ; Asian 2025 FT].
- **Practice point:** do SDHB IHC in young patients with epithelioid gastric GIST. Germline SDHx testing and genetic counselling follow if SDHB is lost (Asian 2025) [VERIFIED; FT].

---

## 6. Staging and risk stratification

### 6.1 AJCC 8th edition, bone (ICD-O-3 C40–C41; all primary malignant bone tumours except lymphoma and myeloma)

Sources: Tanaka & Ozaki 2019 abstract [VERIFIED; A]; NDRS staging sheet (UICC TNM 8) [VERIFIED; REG]; ACS staging page citing AJCC 8th [VERIFIED; ACS]; ICCR dataset (UICC TNM 8 reproduced with permission) [VERIFIED; REG]; Rose 2019 spine practice update [VERIFIED; web full text, *Annals of Translational Medicine*]. The AJCC manual itself was not opened.

The 8th edition splits primary bone sites into three groups:

**(a) Appendicular skeleton, trunk, skull and facial bones**

| T | Definition |
|---|---|
| T1 | ≤8 cm in greatest dimension |
| T2 | >8 cm |
| T3 | Discontinuous tumours in the primary bone site (skip lesions) |

- N1 = regional node metastasis (rare; when not assessed, N0 may be used).
- **M1a = lung**; **M1b = bone or other distant sites**.

| Stage | T | N | M | Grade |
|---|---|---|---|---|
| IA | T1 | N0 | M0 | G1/GX (low) |
| IB | T2 or T3 | N0 | M0 | G1/GX |
| IIA | T1 | N0 | M0 | G2/G3 (high) |
| **IIB** | **T2** | N0 | M0 | G2/G3 |
| III | T3 | N0 | M0 | G2/G3 |
| IVA | any T | N0 | **M1a** | any G |
| IVB | any T | **N1** | any M | any G |
| IVB | any T | any N | **M1b** | any G |

**(b) Spine.** Five vertebral segments: right pedicle, right body, left body, left pedicle, posterior element.

| T | Definition |
|---|---|
| T1 | 1 segment or 2 adjacent segments |
| T2 | 3 adjacent segments |
| T3 | 4 adjacent segments (UICC/ICCR wording). The ENCR/UICC slides say ">4 adjacent, or any non-adjacent segments" [PARTIAL: wording differs between sources; check against the AJCC manual] |
| T4a | Invades the spinal canal |
| T4b | Invades adjacent vessels or tumour thrombus in adjacent vessels |

**(c) Pelvis.** Four segments: sacrum lateral to the sacral foramen; iliac wing; acetabulum/periacetabulum; pubic rami, symphysis and ischium. Each T is split by size: **a = ≤8 cm, b = >8 cm**.

| T | Definition |
|---|---|
| T1 | 1 segment, no extraosseous extension |
| T2 | 1 segment with extraosseous extension, or 2 adjacent segments without extraosseous extension |
| T3 | 2 segments with extraosseous extension |
| T4a | 3 adjacent segments, or crossing the SI joint to the sacral neuroforamen |
| T4b | Encasing the external iliac vessels, or gross tumour thrombus in major pelvic vessels |

- **Spine and pelvis: no prognostic stage groups** (record TNM + G only) [VERIFIED; REG; Rose 2019].
- The AJCC 8th edition applies to cases diagnosed from 1 January 2018 [VERIFIED; Rose 2019]. The AJCC "Current Staging System 2026" chart lists Bone (ch. 38) as **still 8th edition**, with no Version 9 protocol [VERIFIED; AJCC chart].

### 6.2 AJCC 8th edition, soft tissue sarcoma [VERIFIED; PDQ Tables 1–7; Tanaka & Ozaki A; NDRS REG]

The 8th edition stages STS separately by site:
- trunk and extremities
- retroperitoneum
- head and neck
- abdomen and thoracic visceral organs
- unusual histologies/sites

Two other changes: **tumour depth (superficial vs deep) was removed**, and the size cut-offs became **5/10/15 cm**.

**T categories**

| T | Trunk/extremities and retroperitoneum | Head and neck | Abdominal/thoracic visceral organs |
|---|---|---|---|
| T1 | ≤5 cm | ≤2 cm | organ-confined |
| T2 | >5 to ≤10 cm | >2 to ≤4 cm | beyond the organ (T2a serosa/visceral peritoneum; T2b beyond serosa) |
| T3 | >10 to ≤15 cm | >4 cm | invades another organ |
| T4 | >15 cm | adjoining structures (T4a orbit, skull base, etc.; T4b brain, carotid encasement, prevertebral, perineural CNS) | multifocal (T4a 2 sites; T4b 3–5 sites; T4c >5 sites) |

**Stage groups (trunk/extremities and retroperitoneum)**

| Stage | T | N | M | G |
|---|---|---|---|---|
| IA | T1 | N0 | M0 | G1/GX |
| IB | T2–T4 | N0 | M0 | G1/GX |
| II | T1 | N0 | M0 | G2/G3 |
| IIIA | T2 | N0 | M0 | G2/G3 |
| IIIB | T3–T4 | N0 | M0 | G2/G3 |
| **N1** | any T | N1 | M0 | any G → **AJCC: stage IV (trunk/extremity) but IIIB (retroperitoneum)**. UICC TNM 8: IIIB for both. |
| IV | any T | any N | M1 | any G |

- Head and neck and visceral STS: **no stage grouping** [VERIFIED; PDQ; REG].
- Not staged with the STS chapters (UICC): Kaposi sarcoma, dermatofibrosarcoma protuberans, sarcomas of dura/brain, and angiosarcoma. Cystosarcoma phyllodes is staged as superficial-trunk STS [VERIFIED; REG-ENCR slides].
- PDQ notes that STS staging is used mainly for research; decisions rest on subtype, grade, site and extent [VERIFIED; PDQ].

### 6.3 AJCC 8th edition, GIST (unchanged from 7th edition) [VERIFIED; ACS (AJCC 8th, last revised 2026-03-10); Chen JH 2025 FT for "unchanged since 7th"; ENCR/UICC slides]

**Definitions**
- T1 ≤2 cm; T2 >2–5 cm; T3 >5–10 cm; T4 >10 cm. N1 = regional nodes (rare). M1 = distant.
- **Mitotic rate:** low = ≤5 per 5 mm² (50 HPF); high = >5 [VERIFIED; ENCR/UICC "5 or fewer per 50 hpf"; Asian 2025 "50 HPF ≈ 5 mm²"].
- Topography: C15–C20 and C48 [VERIFIED; ENCR].

**Stage groups**

| Stage | Gastric / omental GIST | Small intestine, oesophagus, colon, rectum, mesentery, peritoneum |
|---|---|---|
| I / IA | **IA:** T1–T2, low mitotic rate | **I:** T1–T2, low |
| IB | T3, low | — |
| II | T1–T2 high; **or** T4 low | T3 low |
| IIIA | T3 high | T1 high; **or** T4 low |
| IIIB | T4 high | T2–T4 high |
| IV | any T N1 M0, or any M1 | any T N1 M0, or any M1 |

- ACS: the TNM system is **not** meant for paediatric or syndromic GIST [VERIFIED; ACS].
- In practice, the modified NIH and AFIP risk schemes guide adjuvant therapy more than TNM does (Chen JH 2025; Asian 2025) [VERIFIED; FT].
- TCR reports GIST by AJCC 8th combined stage (Section 1.5).

### 6.4 GIST risk stratification

**NIH consensus (Fletcher 2002)** [VERIFIED; A]
- Uses size + mitotic count only.
- It advises avoiding the term "benign" for any GIST.

**AFIP / Miettinen & Lasota (2006)** [VERIFIED; A for the principle; PDQ and Asian 2025 for the tables]
- Adds **site**: gastric GISTs behave better than intestinal ones with the same size and mitoses.
- Abstract wording: gastric GISTs ≤10 cm with ≤5 mitoses/50 HPF are low risk; gastric GISTs >5 cm with >5 mitoses are high risk. All intestinal GISTs >5 cm are at least moderate risk, and all intestinal GISTs with >5 mitoses are high risk.

Metastasis/progression rates (PDQ, adapted from Miettinen & Lasota and the CAP protocol) [VERIFIED; PDQ]:

| Mitoses /50 HPF | Size | Gastric: % metastasis (risk) | Non-gastric: % (risk) |
|---|---|---|---|
| ≤5 | ≤2 cm | 0 (none) | 0 (none) |
| ≤5 | >2–5 | 1.9 (very low) | 1.9–8.5 (low) |
| ≤5 | >5–10 | 3.6 (low) | 24 (insufficient data–moderate) |
| ≤5 | >10 | 12 (moderate) | 34–52 (high) |
| >5 | ≤2 | 0 (none) | 50–54 (insufficient data–high) |
| >5 | >2–5 | 16 (moderate) | 50–73 (high) |
| >5 | >5–10 | 55 (high) | 85 (high) |
| >5 | >10 | 86 (high) | 71–90 (high) |

AFIP categories by site, as reproduced in the **2025 Asian consensus**, Table 2 [VERIFIED; FT]:

| Size (cm) | Mitoses /50 HPF | Stomach | Small intestine | Duodenum | Rectum |
|---|---|---|---|---|---|
| ≤2 | ≤5 | None | None | None | None |
| >2–5 | ≤5 | Very low | Low | Low | Low |
| >5–10 | ≤5 | Low | Moderate | High | High |
| >10 | ≤5 | Moderate | High | High | High |
| ≤2 | >5 | None | High | No data | High |
| >2–5 | >5 | Moderate | High | High | High |
| >5–10 | >5 | High | High | High | High |
| >10 | >5 | High | High | High | High |

**Modified NIH / Joensuu (2008)**
- Abstract [VERIFIED; A]:
  - adds **tumour rupture** and **non-gastric site**
  - non-gastric 2.1–5 cm with >5 mitoses, or 5.1–10 cm with ≤5 mitoses, and rupture → **high risk** (>15–20% recurrence)
  - gastric GISTs are about 58% of all GISTs
  - NIH high risk ≈44%, intermediate 24%, low/very low 32% of resected GIST
- Table as reproduced in the **2025 Asian consensus**, Table 3 [VERIFIED; FT]:

| Size (cm) | Mitoses /50 HPF | Stomach | Other sites |
|---|---|---|---|
| ≤2 (printed "<2") | ≤5 | Very low | Very low |
| >2–5 | ≤5 | Low | Low |
| >5–10 | ≤5 | Intermediate | **High** |
| ≤2 | >5–10 | Intermediate | High |
| >2–5 | >5–10 | Intermediate | High |
| >5–10 | >5–10 | High | High |
| >10 | any | High | High |
| any | >10 | High | High |
| **Tumour rupture** | any | **High** | **High** |

- Caveat [PARTIAL]: I could not open the original Joensuu 2008 table. The ≤2 cm row with 6–10 mitoses is the cell most often rendered differently, so check the original before printing that cell.
- The Asian consensus notes that "50 HPF" was not clearly defined in the original articles and **adopts 5 mm²** [VERIFIED; FT].
- **Use:** the Asian consensus 2025 recommends modified NIH to select patients for **3 years of adjuvant imatinib** in high-risk GIST (SSG XVIII/AIO), with genotyping first to identify imatinib-insensitive tumours (PDGFRA D842V, wild-type) [VERIFIED; FT].

**Pooled population cohorts (Joensuu 2012; n = 2,560, no adjuvant therapy)** [VERIFIED; A]
- 15-year recurrence-free survival 59.9%; few recurrences after 10 years.
- Adverse factors: large size, high mitoses, non-gastric site, rupture, male sex.
- AUC for 10-year RFS: NIH 0.79, modified NIH 0.78, AFIP 0.82, non-linear **prognostic contour maps 0.88**.
- Modified NIH is best for defining a single high-risk group; the contour maps are best for individual risk estimates.

**Note:** none of these schemes applies to SDH-deficient GIST (Section 5.4).

### 6.5 Enneking / MSTS surgical staging (concept)

**Stages** (Enneking, Spanier & Goodman 1980) [VERIFIED; A]
- Stratified by grade, anatomic setting and metastasis:
  - **I = low grade; II = high grade; III = metastasis (regional or distant)**
  - **A = intracompartmental** (within well-delineated surgical compartments); **B = extracompartmental**
- Examples: IIB = high grade, extracompartmental (the usual presentation of conventional osteosarcoma; see the Petriceks case [PARTIAL]).
- Surgical margins: **intralesional, marginal, wide, radical**, defined relative to the lesion, its reactive zone and the anatomic compartment.
- The system applies to bone and soft-tissue lesions of any histogenesis.

**Status and limits**
- Adopted by the MSTS. Enneking 1986 notes it was adapted by the AJCC bone task force [VERIFIED; A].
- ACS describes MSTS stages IA/IB (low grade, localized), IIA/IIB (high grade, localized) and III (metastatic); A = within bone, B = beyond bone [VERIFIED; ACS].
- Designed for extremity tumours; it is not suited to spine tumours, where the Weinstein–Boriani–Biagini system describes surgical anatomy (Rose 2019) [VERIFIED].
- Benign-lesion stages 1/2/3 (latent/active/aggressive) are often taught, but I did not see that wording in a source opened here: [UNVERIFIED].

**MSTS functional score** (Enneking 1993) [VERIFIED; A]
- Six categories each scored **0–5**:
  - all limbs: pain, function, emotional acceptance
  - lower limb: supports, walking, gait
  - upper limb: hand positioning, dexterity, lifting ability
- Reported as a numerical score and a percentage. Maximum 30 = 100% (computed).
- Used to report function after limb salvage or amputation.

---

## 7. NCCN guideline versions on nccn.org (read 2026-10-29) [VERIFIED]

Sources: https://www.nccn.org/guidelines/category_1 and the detail pages (id=1418 bone, 1464 STS, 1507 GIST, 1551 paediatric bone).

| Guideline | Current version | Patient guide available (and its basis) |
|---|---|---|
| **Bone Cancer** (sub-sections: chondrosarcoma, chordoma, Ewing sarcoma, GCTB, osteosarcoma) | **Version 1.2027** | Bone Cancer 2026 (based on v1.2026, 11 Sep 2025) |
| **Soft Tissue Sarcoma** (extremity/trunk/H&N, retroperitoneal/intra-abdominal, desmoid, rhabdomyosarcoma, many histotypes) | **Version 5.2026** | Soft Tissue Sarcoma 2025 (based on v1.2025, 2 May 2025) |
| **Gastrointestinal Stromal Tumors** | **Version 1.2026** | GIST 2026 (based on v1.2026, 13 Jan 2026) |
| Pediatric Bone Sarcoma | Version 1.2027 | none listed |
| Pediatric Soft Tissue Sarcoma | Version 1.2026 | — |

- The category pages show versions only, without posting dates. NCCN updates often, so recheck before printing.
- Bone Cancer 1.2027 and STS 5.2026 match the versions recorded earlier today in A_taiwan_guidelines_staging.md.

---

## 8. Exam-style pearls (each traceable to the sections above)

1. Taiwan 2023: bone cancer **152** new cases (ASR 0.56/10⁵); C47/C49 soft tissue **774** (ASR 2.21/10⁵). GIST is the commonest STS by histology but is registered under its organ [VERIFIED].
2. Bone sarcoma age curve: **bimodal**, adolescent (10–19) and ≥60–70s. Soft tissue sarcoma: **rises with age** [VERIFIED].
3. Osteosarcoma: commonest primary bone cancer; peaks in adolescence; knee region. Ewing: 10–19, pelvis/diaphysis, EWSR1::FLI1. Chondrosarcoma: adults; pelvis, femur, humerus [VERIFIED].
4. Diagnostic order: **imaging (MRI of the primary; for bone, the whole bone) and chest CT before biopsy → core needle biopsy at the treating sarcoma centre, along the future resection tract** [VERIFIED/PARTIAL as in Section 4].
5. "Whoops" excision raises local recurrence; residual tumour is found in about 35–48% at re-excision; overall survival is not clearly worse in the meta-analysis [VERIFIED].
6. FNCLCC = differentiation (1–3) + mitoses/10 HPF (1–3) + necrosis (0–2). **G1 2–3, G2 4–5, G3 6–8** [VERIFIED].
7. MDM2 → WD/DD liposarcoma (and parosteal osteosarcoma). SS18::SSX → synovial sarcoma. EWSR1::FLI1 → Ewing. FUS::DDIT3 → myxoid liposarcoma. KIT exon 11 > exon 9 > PDGFRA exon 18 → GIST. SDHB loss → young, gastric, TKI-resistant GIST [VERIFIED].
8. AJCC 8th: bone T cut-off **8 cm**; spine/pelvis have **no stage group**; STS T **5/10/15 cm** with depth removed; **extremity N1 = stage IV (AJCC)**, retroperitoneal N1 = IIIB [VERIFIED].
9. GIST: size + mitoses/5 mm² + site + rupture. Rupture = high risk (modified NIH). Mitotic cut-off **5 per 5 mm² (50 HPF)** [VERIFIED].

---

## 9. References (APA 7)

### Taiwan data and official sources
- Taiwan Cancer Registry Center. (2026, January). *Year_Bones_2023*, *Period_Bones_2023*, *Year_Soft-tissue_2023*, *Period_Soft-tissue_2023* [Data sets]. https://twcr.tw/wp-content/uploads/2026/01/Year_Bones_2023.xlsx ; https://twcr.tw/wp-content/uploads/2026/01/Period_Bones_2023.xlsx ; https://twcr.tw/wp-content/uploads/2026/01/Year_Soft-tissue_2023.xlsx ; https://twcr.tw/wp-content/uploads/2026/01/Period_Soft-tissue_2023.xlsx
- Taiwan Cancer Registry Center. (2025, December). *112年癌症登記長表報告* (CA17_LF112.pdf; 表八之二 胃部胃腸基質瘤). https://twcr.tw/wp-content/uploads/2025/12/CA17_LF112.pdf
- Taiwan Cancer Registry Center. (2026, April 15). *[癌登第115004號通知文] ICD-O-4最新訊息與修正AJCC Version 9 TNM、stage編碼對應與第8版差異處*. https://twcr.tw/?p=3529
- 衛生福利部統計處. (2026, June 22). *114年死因統計結果摘要表* [Data set]. https://www.mohw.gov.tw/dl-100920-e5938c74-aa2a-4994-a15c-054787318303.html

### Guidelines, staging and reference summaries (non-journal)
- National Comprehensive Cancer Network. (2026). *NCCN guidelines: Category 1 listing* (Bone Cancer v1.2027; Soft Tissue Sarcoma v5.2026; Gastrointestinal Stromal Tumors v1.2026; Pediatric Bone Sarcoma v1.2027; Pediatric Soft Tissue Sarcoma v1.2026). Retrieved October 29, 2026, from https://www.nccn.org/guidelines/category_1
- National Comprehensive Cancer Network. (2026). *NCCN Guidelines for Patients: Bone cancer* (based on NCCN Guidelines for Bone Cancer v1.2026). https://www.nccn.org/patients/guidelines/content/PDF/bone-patient.pdf
- National Comprehensive Cancer Network. (2025). *NCCN Guidelines for Patients: Soft tissue sarcoma* (based on v1.2025). https://www.nccn.org/patients/guidelines/content/PDF/sarcoma-patient.pdf
- National Comprehensive Cancer Network. (2026). *NCCN Guidelines for Patients: Gastrointestinal stromal tumors* (based on v1.2026). https://www.nccn.org/patients/guidelines/content/PDF/gist-patient.pdf
- PDQ Adult Treatment Editorial Board. (2025, February 21). *Soft tissue sarcoma treatment (PDQ®)–Health professional version*. National Cancer Institute. https://www.cancer.gov/types/soft-tissue-sarcoma/hp/adult-soft-tissue-treatment-pdq
- PDQ Adult Treatment Editorial Board. (2024, December 13). *Gastrointestinal stromal tumors treatment (PDQ®)–Health professional version*. National Cancer Institute. https://www.cancer.gov/types/soft-tissue-sarcoma/hp/gist-treatment-pdq
- PDQ Pediatric Treatment Editorial Board. (2024, December 2). *Osteosarcoma and undifferentiated pleomorphic sarcoma of bone treatment (PDQ®)–Health professional version*. National Cancer Institute. https://www.cancer.gov/types/bone/hp/osteosarcoma-treatment-pdq
- PDQ Pediatric Treatment Editorial Board. (2024, November 27). *Ewing sarcoma and undifferentiated small round cell sarcomas of bone and soft tissue treatment (PDQ®)–Health professional version*. National Cancer Institute. https://www.cancer.gov/types/bone/hp/ewing-treatment-pdq
- PDQ Pediatric Treatment Editorial Board. (2025, April 21). *Childhood soft tissue sarcoma treatment (PDQ®)–Health professional version*. National Cancer Institute. https://www.cancer.gov/types/soft-tissue-sarcoma/hp/child-soft-tissue-treatment-pdq
- American Cancer Society. (2026, March 10). *Gastrointestinal stromal tumor stages*. https://www.cancer.org/cancer/types/gastrointestinal-stromal-tumor/detection-diagnosis-staging/staging.html
- American Cancer Society. (2026, January 5). *Bone cancer stages*. https://www.cancer.org/cancer/types/bone-cancer/detection-diagnosis-staging/staging.html
- National Disease Registration Service, NHS England. (n.d.). *Staging sheets: Bone (ICD10 C40 & C41)* and *Soft tissues (ICD10 C38.1-2, C47-C49)* [TNM 8th edition]. Accessed via mirror https://nhsd-proxy.openprescribing.net/ndrs/data/cancer-data-training-materials/staging-sheets/bone and …/soft-tissue (canonical digital.nhs.uk returned 403).
- International Collaboration on Cancer Reporting. (2021). *Primary tumour in bone: Histopathology reporting guide—Resection specimens* (1st ed., v1.1). https://www.iccr-cancer.org/wp-content/uploads/2023/11/ICCR-Bone_Resection-1st-ed-v1.1-Bookmarked.pdf
- Van Eycken, L. (2019). *Coding sarcomas: UICC TNM 8th edition* [Training slides, ENCR]. https://www.encr.eu/sites/default/files/meetings/Training-Nov-2019/Session7_Eycken-Sarcoma-ENCR-Nov2019-TNM-website.pdf
- American Joint Committee on Cancer. (2026). *AJCC current staging system* [Chart]. https://www.facs.org/media/c5ik5tkr/ajcc-current-staging-system-2026.pdf
- Rose, P. S., Holt, G. E., & Kneisl, J. S. (2019). Changes to the American Joint Committee on Cancer staging system for spine tumors—practice update. *Annals of Translational Medicine*, *7*(10), 215. https://doi.org/10.21037/atm.2019.04.43 (PMID 31297380; PMC6595207)

### Clinical practice guidelines and consensus (journal)
- Strauss, S. J., Frezza, A. M., Abecassis, N., Bajpai, J., Bauer, S., Biagini, R., Bielack, S., Blay, J. Y., Bolle, S., Bonvalot, S., Boukovinas, I., Bovee, J. V. M. G., Boye, K., Brennan, B., Brodowicz, T., Buonadonna, A., de Álava, E., Dei Tos, A. P., Garcia Del Muro, X., . . . ESMO Guidelines Committee, EURACAN, GENTURIS and ERN PaedCan. (2021). Bone sarcomas: ESMO–EURACAN–GENTURIS–ERN PaedCan clinical practice guideline for diagnosis, treatment and follow-up. *Annals of Oncology*, *32*(12), 1520–1536. https://doi.org/10.1016/j.annonc.2021.08.1995 (PMID 34500044) — *citation verified; full text 403, not used for content*
- Gronchi, A., Miah, A. B., Dei Tos, A. P., Abecassis, N., Bajpai, J., Bauer, S., Biagini, R., Bielack, S., Blay, J. Y., Bolle, S., Bonvalot, S., Boukovinas, I., Bovee, J. V. M. G., Boye, K., Brennan, B., Brodowicz, T., Buonadonna, A., De Álava, E., Del Muro, X. G., . . . ESMO Guidelines Committee, EURACAN and GENTURIS. (2021). Soft tissue and visceral sarcomas: ESMO–EURACAN–GENTURIS clinical practice guidelines for diagnosis, treatment and follow-up. *Annals of Oncology*, *32*(11), 1348–1365. https://doi.org/10.1016/j.annonc.2021.07.006 (PMID 34303806) — *citation verified; full text 403*
- Casali, P. G., Blay, J. Y., Abecassis, N., Bajpai, J., Bauer, S., Biagini, R., Bielack, S., Bonvalot, S., Boukovinas, I., Bovee, J. V. M. G., Boye, K., Brodowicz, T., Buonadonna, A., De Álava, E., Dei Tos, A. P., Del Muro, X. G., Dufresne, A., Eriksson, M., Fedenko, A., . . . ESMO Guidelines Committee, EURACAN and GENTURIS. (2022). Gastrointestinal stromal tumours: ESMO–EURACAN–GENTURIS clinical practice guidelines for diagnosis, treatment and follow-up. *Annals of Oncology*, *33*(1), 20–33. https://doi.org/10.1016/j.annonc.2021.09.005 (PMID 34560242) — *citation verified; full text 403*
- Hirano, H., Naito, Y., Takahashi, T., Hirota, S., Kim, K.-M., Ryu, M.-H., Wang, J., Cao, H., Li, J., Li, C.-F., Yen, C.-C., Yang, H.-K., Jung, H.-Y., Yeh, C.-N., Wang, H.-P., Chen, L.-T., Shen, L., Kang, Y.-K., & Nishida, T. (2026). Updated Asian consensus guidelines for the diagnosis and management of gastrointestinal stromal tumor (2025). *Gastric Cancer*, *29*(5), 887–903. https://doi.org/10.1007/s10120-026-01773-4 (PMID 42455249; PMC13525072)
- Koo, D.-H., Ryu, M.-H., Kim, K.-M., Yang, H.-K., Sawaki, A., Hirota, S., Zheng, J., Zhang, B., Tzen, C.-Y., Yeh, C.-N., Nishida, T., Shen, L., Chen, L.-T., & Kang, Y.-K. (2016). Asian consensus guidelines for the diagnosis and management of gastrointestinal stromal tumor. *Cancer Research and Treatment*, *48*(4), 1155–1166. https://doi.org/10.4143/crt.2016.187 (PMID 27384163; PMC5080813)
- Frebourg, T., Bajalica Lagercrantz, S., Oliveira, C., Magenheim, R., Evans, D. G., & European Reference Network GENTURIS. (2020). Guidelines for the Li–Fraumeni and heritable TP53-related cancer syndromes. *European Journal of Human Genetics*, *28*(10), 1379–1386. https://doi.org/10.1038/s41431-020-0638-4 (PMID 32457520; PMC7609280)

### Staging, grading and risk stratification
- Tanaka, K., & Ozaki, T. (2019). New TNM classification (AJCC eighth edition) of bone and soft tissue sarcomas: JCOG Bone and Soft Tissue Tumor Study Group. *Japanese Journal of Clinical Oncology*, *49*(2), 103–107. https://doi.org/10.1093/jjco/hyy157 (PMID 30423153)
- Coindre, J.-M. (2006). Grading of soft tissue sarcomas: Review and update. *Archives of Pathology & Laboratory Medicine*, *130*(10), 1448–1453. https://doi.org/10.5858/2006-130-1448-GOSTSR (PMID 17090186)
- Guillou, L., Coindre, J. M., Bonichon, F., Nguyen, B. B., Terrier, P., Collin, F., Vilain, M. O., Mandard, A. M., Le Doussal, V., Leroux, A., Jacquemier, J., Duplay, H., Sastre-Garau, X., & Costa, J. (1997). Comparative study of the National Cancer Institute and French Federation of Cancer Centers Sarcoma Group grading systems in a population of 410 adult patients with soft tissue sarcoma. *Journal of Clinical Oncology*, *15*(1), 350–362. https://doi.org/10.1200/JCO.1997.15.1.350 (PMID 8996162)
- Enneking, W. F., Spanier, S. S., & Goodman, M. A. (1980). A system for the surgical staging of musculoskeletal sarcoma. *Clinical Orthopaedics and Related Research*, (153), 106–120. (PMID 7449206; no DOI)
- Enneking, W. F. (1986). A system of staging musculoskeletal neoplasms. *Clinical Orthopaedics and Related Research*, (204), 9–24. (PMID 3456859; no DOI)
- Enneking, W. F., Dunham, W., Gebhardt, M. C., Malawar, M., & Pritchard, D. J. (1993). A system for the functional evaluation of reconstructive procedures after surgical treatment of tumors of the musculoskeletal system. *Clinical Orthopaedics and Related Research*, (286), 241–246. (PMID 8425352; no DOI)
- Fletcher, C. D. M., Berman, J. J., Corless, C., Gorstein, F., Lasota, J., Longley, B. J., Miettinen, M., O'Leary, T. J., Remotti, H., Rubin, B. P., Shmookler, B., Sobin, L. H., & Weiss, S. W. (2002). Diagnosis of gastrointestinal stromal tumors: A consensus approach. *Human Pathology*, *33*(5), 459–465. https://doi.org/10.1053/hupa.2002.123545 (PMID 12094370)
- Miettinen, M., & Lasota, J. (2006). Gastrointestinal stromal tumors: Pathology and prognosis at different sites. *Seminars in Diagnostic Pathology*, *23*(2), 70–83. https://doi.org/10.1053/j.semdp.2006.09.001 (PMID 17193820)
- Joensuu, H. (2008). Risk stratification of patients diagnosed with gastrointestinal stromal tumor. *Human Pathology*, *39*(10), 1411–1419. https://doi.org/10.1016/j.humpath.2008.06.025 (PMID 18774375)
- Joensuu, H., Vehtari, A., Riihimäki, J., Nishida, T., Steigen, S. E., Brabec, P., Plank, L., Nilsson, B., Cirilli, C., Braconi, C., Bordoni, A., Magnusson, M. K., Linke, Z., Sufliarsky, J., Federico, M., Jonasson, J. G., Dei Tos, A. P., & Rutkowski, P. (2012). Risk of recurrence of gastrointestinal stromal tumour after surgery: An analysis of pooled population-based cohorts. *The Lancet Oncology*, *13*(3), 265–274. https://doi.org/10.1016/S1470-2045(11)70299-6 (PMID 22153892)
- Chen, J.-H., Yang, Z.-R., Cai, Z.-M., Lin, T., Lin, R., Su, X.-C., Kang, R.-B., Lin, L., Ye, Z.-S., & Zhou, Y.-J. (2025). Comparative study of National Institute of Health criteria and TNM staging system in predicting the prognosis of gastrointestinal stromal tumours: A retrospective study. *Frontiers in Oncology*, *15*, Article 1622777. https://doi.org/10.3389/fonc.2025.1622777 (PMID 40904501; PMC12401700)
- Petriceks, A. H., & Salmi, D. (2019). Educational case: Primary osteosarcoma. *Academic Pathology*, *6*, Article 2374289518820337. https://doi.org/10.1177/2374289518820337 (PMID 30733995; PMC6343432) — *cited only to flag its stage-group error*

### Epidemiology
- Hung, G.-Y., Horng, J.-L., Yen, H.-J., Yen, C.-C., Chen, W.-M., Chen, P. C.-H., Wu, H.-T. H., & Chiou, H.-J. (2014). Incidence patterns of primary bone cancer in Taiwan (2003–2010): A population-based study. *Annals of Surgical Oncology*, *21*(8), 2490–2498. https://doi.org/10.1245/s10434-014-3697-3 (PMID 24723225; PMC4082651)
- Hung, G.-Y., Yen, C.-C., Horng, J.-L., Liu, C.-Y., Chen, W.-M., Chen, T.-H., & Liu, C.-L. (2015). Incidences of primary soft tissue sarcoma diagnosed on extremities and trunk wall: A population-based study in Taiwan. *Medicine*, *94*(41), e1696. https://doi.org/10.1097/MD.0000000000001696 (PMID 26469906; PMC4616812)
- Hung, G.-Y., Horng, J.-L., Chen, P. C.-H., Lin, L.-Y., Chen, J.-Y., Chuang, P.-H., Chao, T.-C., & Yen, C.-C. (2019). Incidence of soft tissue sarcoma in Taiwan: A nationwide population-based study (2007–2013). *Cancer Epidemiology*, *60*, 185–192. https://doi.org/10.1016/j.canep.2019.04.007 (PMID 31055220)
- Chen, T. W.-W., Chiang, R. C.-J., Le Cesne, A., Hsieh, Y.-C., Italiano, A., Yang, Y.-W., Penel, N., Lee, W.-C., Bompas, E., Valentin, T., Anract, P., Firmin, N., Duffaud, F., Cheng, A.-L., Ducimetiere, F., Chan, K. A., & Blay, J.-Y. (2022). Soft tissue sarcoma incidences and clinical characteristics are significantly different in France and Taiwan. *Cancer*, *128*(18), 3360–3369. https://doi.org/10.1002/cncr.34372 (PMID 35796499)
- Lee, M.-J., Chiang, C.-J., Yang, Y.-W., Zhuang, B.-Z., Lee, W.-C., Li, Z. C.-C., & Chen, T. W.-W. (2026). Age-related differences in outcomes and tumor characteristics of ultrarare sarcomas: A nationwide study. *Cancer Epidemiology, Biomarkers & Prevention*, *35*(9), 1654–1662. https://doi.org/10.1158/1055-9965.EPI-25-1790 (PMID 42089803)
- Chu, H.-Y., Shen, X.-H., Lin, C.-N., Lee, C.-C., Chen, Y.-C., Chen, Y.-J., Lin, Y.-C., & Chang, S.-H. (2026). Overall survival and prognostic factors in osteosarcoma: A nationwide cohort study from Taiwan. *Life*, *16*(2), Article 288. https://doi.org/10.3390/life16020288 (PMID 41752924; PMC12942422)
- Tzen, C.-Y., Wang, J.-H., Huang, Y.-J., Wang, M.-N., Lin, P.-C., Lai, G.-L., Wu, C.-Y., & Tzen, C.-Y. (2007). Incidence of gastrointestinal stromal tumor: A retrospective study based on immunohistochemical and mutational analyses. *Digestive Diseases and Sciences*, *52*(3), 792–797. https://doi.org/10.1007/s10620-006-9480-y (PMID 17253141; PMC7087581) — *DOI corrected; PubMed shows a wrong DOI*
- Tsai, H.-J., Shan, Y.-S., Yang, C.-Y., Hsiao, C.-F., Tsai, C.-H., Wang, C.-C., Lin, M.-T., Ting, C.-F., Chan, D.-C., Chen, T.-H., Yen, C.-C., Chen, Y.-Y., Lin, H.-Y., Yeh, T.-S., Ho, C.-L., Shieh, T.-Y., Bai, L.-Y., Hsu, J.-T., Chen, I.-S., . . . Taiwan Cooperative Oncology Group (TCOG) GIST Study Group. (2024). Survival of advanced/recurrent gastrointestinal stromal tumors treated with tyrosine kinase inhibitors in Taiwan: A nationwide registry study. *BMC Cancer*, *24*(1), Article 828. https://doi.org/10.1186/s12885-024-12567-1 (PMID 38992597; PMC11238460)
- Mirabello, L., Troisi, R. J., & Savage, S. A. (2009). Osteosarcoma incidence and survival rates from 1973 to 2004: Data from the Surveillance, Epidemiology, and End Results Program. *Cancer*, *115*(7), 1531–1543. https://doi.org/10.1002/cncr.24121 (PMID 19197972; PMC2813207)
- Jawad, M. U., Cheung, M. C., Min, E. S., Schneiderbauer, M. M., Koniaris, L. G., & Scully, S. P. (2009). Ewing sarcoma demonstrates racial disparities in incidence-related and sex-related differences in outcome: An analysis of 1631 cases from the SEER database, 1973–2005. *Cancer*, *115*(15), 3526–3536. https://doi.org/10.1002/cncr.24388 (PMID 19548262)
- Giuffrida, A. Y., Burgueno, J. E., Koniaris, L. G., Gutierrez, J. C., Duncan, R., & Scully, S. P. (2009). Chondrosarcoma in the United States (1973 to 2003): An analysis of 2890 cases from the SEER database. *The Journal of Bone and Joint Surgery. American Volume*, *91*(5), 1063–1072. https://doi.org/10.2106/JBJS.H.00416 (PMID 19411454)
- Kondo, H., Ogura, K., Morizane, C., Satake, T., Iwata, S., Toda, Y., Muramatsu, S., Takemori, T., Kobayashi, E., Higashi, T., & Kawai, A. (2025). Chondrosarcoma in Japan: An analytic study using population-based National Cancer Registry. *Japanese Journal of Clinical Oncology*, *55*(5), 490–497. https://doi.org/10.1093/jjco/hyaf024 (PMID 39893587)

### Risk factors and genetics
- Mai, P. L., Best, A. F., Peters, J. A., DeCastro, R. M., Khincha, P. P., Loud, J. T., Bremer, R. C., Rosenberg, P. S., & Savage, S. A. (2016). Risks of first and subsequent cancers among TP53 mutation carriers in the National Cancer Institute Li-Fraumeni syndrome cohort. *Cancer*, *122*(23), 3673–3681. https://doi.org/10.1002/cncr.30248 (PMID 27496084; PMC5115949)
- de Andrade, K. C., Khincha, P. P., Hatton, J. N., Frone, M. N., Wegman-Ostrosky, T., Mai, P. L., Best, A. F., & Savage, S. A. (2021). Cancer incidence, patterns, and genotype–phenotype associations in individuals with pathogenic or likely pathogenic germline TP53 variants: An observational cohort study. *The Lancet Oncology*, *22*(12), 1787–1798. https://doi.org/10.1016/S1470-2045(21)00580-5 (PMID 34780712; PMC8915249)
- Mirabello, L., Zhu, B., Koster, R., Karlins, E., Dean, M., Yeager, M., Gianferante, M., Spector, L. G., Morton, L. M., Karyadi, D., Robison, L. L., Armstrong, G. T., Bhatia, S., Song, L., Pankratz, N., Pinheiro, M., Gastier-Foster, J. M., Gorlick, R., de Toledo, S. R. C., . . . Savage, S. A. (2020). Frequency of pathogenic germline variants in cancer-susceptibility genes in patients with osteosarcoma. *JAMA Oncology*, *6*(5), 724–734. https://doi.org/10.1001/jamaoncol.2020.0197 (PMID 32191290; PMC7082769)
- Ballinger, M. L., Goode, D. L., Ray-Coquard, I., James, P. A., Mitchell, G., Niedermayr, E., Puri, A., Schiffman, J. D., Dite, G. S., Cipponi, A., Maki, R. G., Brohl, A. S., Myklebost, O., Stratford, E. W., Lorenz, S., Ahn, S.-M., Ahn, J.-H., Kim, J. E., Shanley, S., . . . International Sarcoma Kindred Study. (2016). Monogenic and polygenic determinants of sarcoma risk: An international genetic study. *The Lancet Oncology*, *17*(9), 1261–1271. https://doi.org/10.1016/S1470-2045(16)30147-4 (PMID 27498913)
- Kleinerman, R. A., Tucker, M. A., Tarone, R. E., Abramson, D. H., Seddon, J. M., Stovall, M., Li, F. P., & Fraumeni, J. F. (2005). Risk of new cancers after radiotherapy in long-term survivors of retinoblastoma: An extended follow-up. *Journal of Clinical Oncology*, *23*(10), 2272–2279. https://doi.org/10.1200/JCO.2005.05.054 (PMID 15800318)
- Evans, D. G. R., Baser, M. E., McGaughran, J., Sharif, S., Howard, E., & Moran, A. (2002). Malignant peripheral nerve sheath tumours in neurofibromatosis 1. *Journal of Medical Genetics*, *39*(5), 311–314. https://doi.org/10.1136/jmg.39.5.311 (PMID 12011145; PMC1735122)
- Gladdy, R. A., Qin, L.-X., Moraco, N., Edgar, M. A., Antonescu, C. R., Alektiar, K. M., Brennan, M. F., & Singer, S. (2010). Do radiation-associated soft tissue sarcomas have the same prognosis as sporadic soft tissue sarcomas? *Journal of Clinical Oncology*, *28*(12), 2064–2069. https://doi.org/10.1200/JCO.2009.25.1728 (PMID 20308666; PMC3651600)
- Hansen, M. F., Seton, M., & Merchant, A. (2006). Osteosarcoma in Paget's disease of bone. *Journal of Bone and Mineral Research*, *21*(Suppl. 2), P58–P63. https://doi.org/10.1359/jbmr.06s211 (PMID 17229010)
- Mangham, D. C., Davie, M. W., & Grimer, R. J. (2009). Sarcoma arising in Paget's disease of bone: Declining incidence and increasing age at presentation. *Bone*, *44*(3), 431–436. https://doi.org/10.1016/j.bone.2008.11.002 (PMID 19064007)

### Biopsy and unplanned excision
- Mankin, H. J., Mankin, C. J., & Simon, M. A. (1996). The hazards of the biopsy, revisited. Members of the Musculoskeletal Tumor Society. *The Journal of Bone and Joint Surgery. American Volume*, *78*(5), 656–663. https://doi.org/10.2106/00004623-199605000-00004 (PMID 8642021)
- Barrientos-Ruiz, I., Ortiz-Cruz, E. J., Serrano-Montilla, J., Bernabeu-Taboada, D., & Pozo-Kreilinger, J. J. (2017). Are biopsy tracts a concern for seeding and local recurrence in sarcomas? *Clinical Orthopaedics and Related Research*, *475*(2), 511–518. https://doi.org/10.1007/s11999-016-5090-y (PMID 27655183; PMC5213942)
- Noria, S., Davis, A., Kandel, R., Levesque, J., O'Sullivan, B., Wunder, J., & Bell, R. (1996). Residual disease following unplanned excision of soft-tissue sarcoma of an extremity. *The Journal of Bone and Joint Surgery. American Volume*, *78*(5), 650–655. https://doi.org/10.2106/00004623-199605000-00003 (PMID 8642020)
- Qureshi, Y. A., Huddy, J. R., Miller, J. D., Strauss, D. C., Thomas, J. M., & Hayes, A. J. (2012). Unplanned excision of soft tissue sarcoma results in increased rates of local recurrence despite full further oncological treatment. *Annals of Surgical Oncology*, *19*(3), 871–877. https://doi.org/10.1245/s10434-011-1876-z (PMID 21792512)
- Larios, F., Gonzalez, M. R., Ruiz-Arellanos, K., Aquilino E Silva, G., & Pretell-Mazzini, J. (2024). Is unplanned excision of soft tissue sarcomas associated with worse oncological outcomes? A systematic review and meta-analysis. *Cancers*, *16*(2), Article 443. https://doi.org/10.3390/cancers16020443 (PMID 38275885; PMC10814439)
- Grignol, V. P., & Lopez-Aguiar, A. G. (2022). The implications of an unplanned sarcoma excision (the "whoops" operation). *Surgical Clinics of North America*, *102*(4), 529–538. https://doi.org/10.1016/j.suc.2022.04.002 (PMID 35952685)

### Molecular pathology and classification
- Sbaraglia, M., Bellan, E., & Dei Tos, A. P. (2021). The 2020 WHO classification of soft tissue tumours: News and perspectives. *Pathologica*, *113*(2), 70–84. https://doi.org/10.32074/1591-951X-213 (PMID 33179614; PMC8167394)
- Sirvent, N., Coindre, J.-M., Maire, G., Hostein, I., Keslair, F., Guillou, L., Ranchere-Vince, D., Terrier, P., & Pedeutour, F. (2007). Detection of MDM2-CDK4 amplification by fluorescence in situ hybridization in 200 paraffin-embedded tumor samples: Utility in diagnosing adipocytic lesions and comparison with immunohistochemistry and real-time PCR. *The American Journal of Surgical Pathology*, *31*(10), 1476–1489. https://doi.org/10.1097/PAS.0b013e3180581fff (PMID 17895748)
- Chen, P. C.-H., Yen, C.-C., Hung, G.-Y., Pan, C.-C., & Chen, W.-M. (2019). Gene amplification and tumor grading in parosteal osteosarcoma. *Journal of the Chinese Medical Association*, *82*(12), 889–894. https://doi.org/10.1097/JCMA.0000000000000211 (PMID 31634336; PMC13048025)
- Clark, J., Rocques, P. J., Crew, A. J., Gill, S., Shipley, J., Chan, A. M., Gusterson, B. A., & Cooper, C. S. (1994). Identification of novel genes, SYT and SSX, involved in the t(X;18)(p11.2;q11.2) translocation found in human synovial sarcoma. *Nature Genetics*, *7*(4), 502–508. https://doi.org/10.1038/ng0894-502 (PMID 7951320)
- Delattre, O., Zucman, J., Plougastel, B., Desmaze, C., Melot, T., Peter, M., Kovar, H., Joubert, I., de Jong, P., & Rouleau, G. (1992). Gene fusion with an ETS DNA-binding domain caused by chromosome translocation in human tumours. *Nature*, *359*(6391), 162–165. https://doi.org/10.1038/359162a0 (PMID 1522903)
- Crozat, A., Aman, P., Mandahl, N., & Ron, D. (1993). Fusion of CHOP to a novel RNA-binding protein in human myxoid liposarcoma. *Nature*, *363*(6430), 640–644. https://doi.org/10.1038/363640a0 (PMID 8510758)
- Hirota, S., Isozaki, K., Moriyama, Y., Hashimoto, K., Nishida, T., Ishiguro, S., Kawano, K., Hanada, M., Kurata, A., Takeda, M., Muhammad Tunio, G., Matsuzawa, Y., Kanakura, Y., Shinomura, Y., & Kitamura, Y. (1998). Gain-of-function mutations of c-kit in human gastrointestinal stromal tumors. *Science*, *279*(5350), 577–580. https://doi.org/10.1126/science.279.5350.577 (PMID 9438854)
- Heinrich, M. C., Corless, C. L., Duensing, A., McGreevey, L., Chen, C.-J., Joseph, N., Singer, S., Griffith, D. J., Haley, A., Town, A., Demetri, G. D., Fletcher, C. D. M., & Fletcher, J. A. (2003). PDGFRA activating mutations in gastrointestinal stromal tumors. *Science*, *299*(5607), 708–710. https://doi.org/10.1126/science.1079666 (PMID 12522257)
- Emile, J. F., Brahimi, S., Coindre, J. M., Bringuier, P. P., Monges, G., Samb, P., Doucet, L., Hostein, I., Landi, B., Buisine, M. P., Neuville, A., Bouché, O., Cervera, P., Pretet, J. L., Tisserand, J., Gauthier, A., Le Cesne, A., Sabourin, J. C., Scoazec, J. Y., . . . Aegerter, P. (2012). Frequencies of KIT and PDGFRA mutations in the MolecGIST prospective population-based study differ from those of advanced GISTs. *Medical Oncology*, *29*(3), 1765–1772. https://doi.org/10.1007/s12032-011-0074-y (PMID 21953054)
- Miettinen, M., Wang, Z.-F., Sarlomo-Rikala, M., Osuch, C., Rutkowski, P., & Lasota, J. (2011). Succinate dehydrogenase-deficient GISTs: A clinicopathologic, immunohistochemical, and molecular genetic study of 66 gastric GISTs with predilection to young age. *The American Journal of Surgical Pathology*, *35*(11), 1712–1721. https://doi.org/10.1097/PAS.0b013e3182260752 (PMID 21997692; PMC3193596)
- Boikos, S. A., Pappo, A. S., Killian, J. K., LaQuaglia, M. P., Weldon, C. B., George, S., Trent, J. C., von Mehren, M., Wright, J. A., Schiffman, J. D., Raygada, M., Pacak, K., Meltzer, P. S., Miettinen, M. M., Stratakis, C., Janeway, K. A., & Helman, L. J. (2016). Molecular subtypes of KIT/PDGFRA wild-type gastrointestinal stromal tumors: A report from the National Institutes of Health Gastrointestinal Stromal Tumor Clinic. *JAMA Oncology*, *2*(7), 922–928. https://doi.org/10.1001/jamaoncol.2016.0256 (PMID 27011036; PMC5472100)
- Corless, C. L., Barnett, C. M., & Heinrich, M. C. (2011). Gastrointestinal stromal tumours: Origin and molecular oncology. *Nature Reviews Cancer*, *11*(12), 865–878. https://doi.org/10.1038/nrc3143 (PMID 22089421) — *background review; abstract only, no numbers taken from it*

---

### Local working files (for the editor)
- TCR workbooks: /tmp/claude-0/-home-user-oncology-educater/6a66dc7f-55e5-547a-b95f-33d6978992bf/scratchpad/sarc_dl/ (Year_/Period_/Cohort_ Bones and Soft-tissue .xlsx)
- NCCN patient guides (PDF + text), PDQ, ACS, NDRS, ICCR and ENCR extracts: same folder
- PubMed abstracts: /tmp/claude-0/-home-user-oncology-educater/6a66dc7f-55e5-547a-b95f-33d6978992bf/scratchpad/sarc_pm/ ; PMC full texts: …/sarc_pmc/ ; PubMed metadata JSON: …/sarc_data/meta.json
