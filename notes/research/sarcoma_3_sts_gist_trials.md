# Sarcoma 3. Soft tissue sarcoma and GIST trials: local therapy, first-line and later-line systemic therapy, histology-specific agents, GIST adjuvant and advanced lines — fact-check report

Handbook: Taiwanese oncology NP (專科護理師) handbook, sarcoma chapter (ward practice and 專師甄審)
Verification date: 2026-10-29
Method: every PMID was pulled from PubMed (NCBI E-utilities efetch/esearch, the same database as the PubMed MCP tools). Numbers come from the PubMed abstract unless another source is named. Where the abstract lacked a requested number I checked the PMC open-access full text, then the current US prescribing information through openFDA (DailyMed set IDs given), then a secondary source. Nothing was filled from memory. Anything still missing is marked **[UNVERIFIED]**.

**Source tags used inline**
- [A] = PubMed abstract of the cited paper
- [FT] = PMC full text of the cited paper (results section unless stated)
- [L-xxx] = current US FDA prescribing information via openFDA (effective date in section 9)
- [TFDA] = TFDA drug licence open dataset (InfoId=36, file downloaded 2026-10-29; latest 異動日期 in file 2026/10/22; 72,096 rows)
- [CBER] = FDA "Approved Cellular and Gene Therapy Products" page (content current as of 2026-09-17)
- [PG] = NCCN Guidelines for Patients PDF (public); NCCN category page lists professional versions (STS **v5.2026**, GIST **v1.2026**) but the professional PDFs need a login and were not opened
- [NEWS] = trade press or company release (secondary)
- "(computed)" = arithmetic I did from verified numbers

**Section status tags**
- **[VERIFIED]** = citation confirmed on PubMed, and the primary-endpoint result (with HR/95% CI where the trial reports one) confirmed from [A], [FT] or [L]
- **[PARTIAL]** = citation confirmed, but part of the requested information comes only from a secondary source or is missing
- **[UNVERIFIED]** = not found in any primary source checked

**APA 7 notes.** All authors up to 20; for 21 or more, the first 19, an ellipsis, then the final author. Study-group bylines are left out. Titles are in sentence case (Lancet journals already publish in sentence case). Year = journal issue year. Papers without an issue yet are marked "Advance online publication".

---

## 0. Corrections and flags for the editor (read first)

1. **Late fibrosis after post-op RT was a trend, not a significant result.** Davis 2005: grade ≥2 fibrosis was 48.2% (post-op 66 Gy) vs 31.5% (pre-op 50 Gy), **P = 0.07**. Do not print "significantly more fibrosis". Field size, not timing, was the significant predictor (P = 0.002) [A].
2. **O'Sullivan 2002 wound-complication result is a per-protocol analysis** (31/88 = 35% vs 16/94 = 17%, difference 18%, 95% CI 5–30, p = 0.01). The pre-op boost dose for positive margins and the trial acronym "SR2" are **not in the abstract** and were not verified [UNVERIFIED].
3. **STRASS was negative overall** (abdominal recurrence-free survival HR 1.01, 95% CI 0.71–1.44). The "liposarcoma benefit" comes from an exploratory pooled analysis with off-trial patients (STRASS + STREXIT; HR 0.61, 0.42–0.89), not from the randomised comparison. The liposarcoma subgroup numbers inside the Lancet Oncology paper are not in its abstract [UNVERIFIED]. A 2026 post hoc analysis found **no excess major post-op complications** with pre-op RT (19.5% vs 20.2%).
4. **EORTC 62012 OS uses a 95.5% CI** (HR 0.83, 95.5% CI 0.67–1.03), and the trial enrolled **ages 18–60 only**.
5. **LMS-04 overall survival is published** (Pautier et al., NEJM 2024): OS 33 vs 24 months, adjusted HR 0.65 (95% CI 0.44–0.95). The Lancet Oncology 2022 abstract has a typo, "15 (201%)" for serious adverse events with doxorubicin + trabectedin (15/74 = 20.3%, computed).
6. **Doxorubicin + trabectedin first-line is not a labelled indication** in Taiwan or the US. Yondelis 友待 (衛部藥輸字第027370號) is licensed only for unresectable/metastatic liposarcoma or leiomyosarcoma after an anthracycline [TFDA; L-Yondelis].
7. **GeDDiS PFS CI typo.** The gemcitabine–docetaxel median PFS is printed as "23.7 weeks (95% CI 18.1–20.0)" in both abstract and full text. The CI cannot exclude its own median; do not reproduce it.
8. **Trabectedin did not improve OS.** Final OS 13.7 vs 13.1 months, HR 0.93 (0.75–1.15), P = .49 [FT; L].
9. **Eribulin: two slightly different OS results exist.** Lancet: 13.5 vs 11.5 months, HR 0.77 (0.62–0.95). US label (one site with 6 patients excluded): 13.5 vs 11.3 months, HR 0.75 (0.61–0.94). Benefit was confined to **liposarcoma** (OS HR 0.51); leiomyosarcoma stratum OS HR 0.90 (0.69–1.18), PFS HR 1.05. Both US and Taiwan labels cover **liposarcoma only** [L; TFDA]. The JCO 2017 liposarcoma paper has an erratum (PMID 29378157), content not checked.
10. **PALETTE: two PFS HRs.** Lancet: 0.31 (0.24–0.40). US label (independent review): 0.35 (0.26–0.48). Name the source when printing. Pneumothorax 8/240 (3.3%) in the STS trial [L-Votrient].
11. **Afami-cel (Tecelra) label changed in 06/2026** [L-Tecelra, recent major changes]: accelerated-approval statement **removed**, age extended to **≥12 years**, dose range now **1.62–10 × 10⁹** TCR⁺ T cells (approval-era range was 2.68–10 × 10⁹ per the FDA approval summary), ICANS warning added. The labeller is now **USWM CT, LLC**. Response durability differs by source: Lancet cohort 1 synovial sarcoma median DOR 11.6 months; FDA re-review median DOR 6.0 months; current label (cohorts 1–3, n = 137) ORR 43.8%, median DOR 5.3 months.
12. **Letetresgene autoleucel (lete-cel) is not FDA-approved.** It is absent from the FDA CBER approved list (current 2026-09-17), there is no openFDA label, and there is no TFDA licence. The pivotal IGNYTE-ESO results are **not on PubMed**; only a pilot MRCLS study (JCO 2025) is. IGNYTE-ESO numbers are [NEWS] only.
13. **Pexidartinib is no longer licensed in Taiwan.** TFDA licence 衛部藥輸字第028293號 (圖拉留膠囊 TURALIO 200 mg, issued 2022-05-27) was **self-cancelled on 2026-02-03** [TFDA]. The 2025 *Oncologist* statement "approved in … Taiwan" is out of date. The US dose is now **250 mg twice daily with a low-fat meal** (ENLIVEN used 1000 mg/day × 2 weeks, then 800 mg/day). Boxed hepatotoxicity warning and REMS [L-Turalio].
14. **Olaratumab (Lartruvo 樂除瘤)**: TFDA licence 衛部菌疫輸字第001075號 issued 2018-03-28, **self-cancelled 2019-09-04** [TFDA]. Global market withdrawal after ANNOUNCE (April 2019) is [NEWS/PARTIAL].
15. **No TFDA licence (active or cancelled) exists** for tazemetostat, nirogacestat, vimseltinib, nab-sirolimus (Fyarro) or afamitresgene autoleucel [TFDA]. Ripretinib (期樂錠) and avapritinib (泰時維) are licensed.
16. **INVICTUS OS is descriptive only.** The key secondary endpoint, ORR, failed (9.4% vs 0%, P = 0.0504), so under the hierarchy OS (15.1 vs 6.6 months, HR 0.36) was **not formally tested** [L-Qinlock; FT].
17. **GRID OS: no difference.** Label final OS 17.4 vs 17.4 months, HR 0.91 (0.65–1.27), with 88% crossover [L-Stivarga].
18. **Avapritinib: label wording differs.** US: PDGFRA **exon 18** mutations, including D842V. Taiwan: PDGFRA **D842V** only [L; TFDA]. VOYAGER (avapritinib vs regorafenib, 3L+ unselected) was **negative**.
19. **INTRIGUE: the KIT exon 9 subgroup favoured sunitinib** (PFS HR 2.85, 1.48–5.48). A ctDNA analysis found exon 11 + 17/18 favoured ripretinib, and the confirmatory INSIGHT trial (NCT05734105) is ongoing.
20. **Imatinib 800 mg for KIT exon 9 is a PFS-only benefit** (MetaGIST: no OS difference). The exon 9 medians were not verified because the MetaGIST full text was unreachable. The US label starts at 400 mg and allows escalation to 800 mg on progression; it does not mention exon 9 [L-Gleevec].
21. **Newer papers beyond the brief that the chapter may want:** SSG XVIII 10-year update (JAMA Oncol 2020); EORTC 62024 final (Ann Oncol 2021); KIT exon 9 adjuvant cohort (Napolitano, JAMA Oncol 2026); INTRIGUE final OS (JCO 2025); DeFi long-term (JCO 2025); ENLIVEN final (Oncologist 2025); MOTION long-term (Oncologist 2026, advance online); AMPECT final (JCO 2024); STRASS complications post hoc (Ann Surg 2026, advance online).
22. **PubMed indexing quirks:** tazemetostat (Gounder 2020) is single-arm but indexed as "Randomized Controlled Trial"; LMS-04 (2022) is a superiority trial but indexed as "Equivalence Trial".
23. **NHI (健保) reimbursement status for any of these drugs was not verified.** nhi.gov.tw was unreachable and no MOHW release was found.

---

## Quick-reference table

| # | Trial | Phase | N | Comparison | Primary endpoint result | Tag |
|---|---|---|---|---|---|---|
| 1 | O'Sullivan 2002 (NCIC) | RCT | 190 | Pre-op 50 Gy/25 vs post-op 66 Gy/33 | Wound complications 35% vs 17% (diff 18%, 95% CI 5–30; p=0.01) | VERIFIED |
| 2 | Davis 2005 (same trial) | Ph 3 late tox | 129 eval | same | G≥2 fibrosis 31.5% (pre) vs 48.2% (post), P=0.07 | VERIFIED |
| 3 | STRASS (EORTC 62092) | 3 | 266 | Pre-op RT 50.4 Gy + surgery vs surgery | ARFS HR 1.01 (0.71–1.44); p=0.95 | VERIFIED |
| 4 | EORTC 62012 | 3 | 455 | Dox vs intensified Dox+Ifos | OS 12.8 vs 14.3 mo, HR 0.83 (95.5% CI 0.67–1.03); p=0.076 | VERIFIED |
| 5 | ANNOUNCE | 3 | 509 | Dox+olaratumab vs Dox+placebo | OS 20.4 vs 19.7 mo, HR 1.05 (0.84–1.30) — negative | VERIFIED |
| 6 | LMS-04 | 3 | 150 | Dox+trabectedin → trab maint vs Dox | PFS 12.2 vs 6.2 mo, HR 0.41 (0.29–0.58); OS 33 vs 24 mo, HR 0.65 (0.44–0.95) | VERIFIED |
| 7 | GeDDiS | 3 | 257 | Gem-Doc vs Dox | 24-wk PFS 46.4% vs 46.3% — no difference | VERIFIED |
| 8 | ET743-SAR-3007 | 3 | 518 (577 final) | Trabectedin vs dacarbazine | OS final HR 0.93 (0.75–1.15); PFS 4.2 vs 1.5 mo, HR 0.55 (0.44–0.70) | VERIFIED |
| 9 | Eribulin 309 | 3 | 452 | Eribulin vs dacarbazine | OS 13.5 vs 11.5 mo, HR 0.77 (0.62–0.95); LPS HR 0.51 | VERIFIED |
| 10 | PALETTE | 3 | 369 | Pazopanib vs placebo | PFS 4.6 vs 1.6 mo, HR 0.31 (0.24–0.40) | VERIFIED |
| 11 | EZH-202 cohort 5 | 2 | 62 | Tazemetostat | ORR 15% (7–26) | VERIFIED |
| 12 | SPEARHEAD-1 | 2 | 52 (cohort 1) | Afami-cel | ORR 37% overall; 39% synovial sarcoma | VERIFIED |
| 13 | Lete-cel pilot / IGNYTE-ESO | pilot / 2 | 20 / 64 | Lete-cel | Pilot ORR 20% and 40%; IGNYTE-ESO 42% [NEWS] | PARTIAL |
| 14 | DeFi | 3 | 142 | Nirogacestat vs placebo | PFS HR 0.29 (0.15–0.55) | VERIFIED |
| 15 | ENLIVEN | 3 | 120 | Pexidartinib vs placebo | ORR wk 25 39% vs 0% | VERIFIED |
| 16 | MOTION | 3 | 123 | Vimseltinib vs placebo | ORR wk 25 40% vs 0% | VERIFIED |
| 17 | AMPECT | 2 | 34 (31 eval) | nab-sirolimus | ORR 39% (22–58) | VERIFIED |
| 18 | SSG XVIII/AIO | 3 | 400 | Imatinib 3 y vs 1 y | RFS HR 0.46 (0.32–0.65); OS HR 0.45 (0.22–0.89); 10-y OS HR 0.55 (0.37–0.83) | VERIFIED |
| 19 | MetaGIST / EORTC 62005 | meta / 3 | 1,640 / 377 | Imatinib 400 vs 800 mg | Small PFS gain with 800 mg, mainly KIT exon 9; no OS gain | PARTIAL |
| 20 | Sunitinib (A6181004) | 3 | 312 | Sunitinib vs placebo | TTP 27.3 vs 6.4 wk, HR 0.33 | VERIFIED |
| 21 | GRID | 3 | 199 | Regorafenib vs placebo | PFS 4.8 vs 0.9 mo, HR 0.27 (0.19–0.39) | VERIFIED |
| 22 | INVICTUS | 3 | 129 | Ripretinib vs placebo (4L+) | PFS 6.3 vs 1.0 mo, HR 0.15 (0.09–0.25) | VERIFIED |
| 23 | INTRIGUE | 3 | 453 | Ripretinib vs sunitinib (2L) | Exon 11 PFS HR 0.88 (0.66–1.16) — negative | VERIFIED |
| 24 | NAVIGATOR | 1 | 56 D842V | Avapritinib | ORR 88% (76–95); long-term 91% | VERIFIED |
| 25 | VOYAGER | 3 | 476 | Avapritinib vs regorafenib (3L+) | PFS 4.2 vs 5.6 mo, HR 1.25 (0.99–1.57) — negative | VERIFIED |

---

# A. Local therapy

## 1. Pre-operative vs post-operative RT for limb STS (O'Sullivan 2002) — [VERIFIED]

**Reference**
- O'Sullivan, B., Davis, A. M., Turcotte, R., Bell, R., Catton, C., Chabot, P., Wunder, J., Kandel, R., Goddard, K., Sadura, A., Pater, J., & Zee, B. (2002). Preoperative versus postoperative radiotherapy in soft-tissue sarcoma of the limbs: A randomised trial. *The Lancet*, *359*(9325), 2235–2241. https://doi.org/10.1016/S0140-6736(02)09292-9 — PMID 12103287

**Design:** Randomised trial, stratified by tumour size (≤10 cm vs >10 cm) [A]. PubMed lists it as a multicentre RCT. It is commonly called NCIC CTG SR2, but that name is not in the abstract [UNVERIFIED].
**Arms:** Pre-op RT **50 Gy in 25 fractions** (n = 94) vs post-op RT **66 Gy in 33 fractions** (n = 96) [A]. The pre-op boost for positive margins is not stated in the abstract [UNVERIFIED].
**Primary endpoint:** Wound complications within **120 days** of surgery, analysed per protocol [A].
**Result:**
- Wound complications **31/88 (35%) pre-op vs 16/94 (17%) post-op**; difference 18% (95% CI 5–30), **p = 0.01** [A].
- Four pre-op patients had no protocol surgery and were not evaluable [A].
- On multivariate analysis, tumour size and anatomical site were also significant risk factors [A].
- Median follow-up was 3.3 years. OS was "slightly better" with pre-op RT (p = 0.0481, secondary, ITT) [A].

**Authors' conclusion:** The choice of sequence should weigh surgical timing, tumour size and site [A].

**NP practice note:** Pre-op RT roughly doubles the early wound-complication rate (35% vs 17%) but uses a lower dose (50 vs 66 Gy). Large and lower-limb tumours need the closest post-op wound surveillance. "Lower limb" specifically is not in the abstract; the abstract says "anatomical site" [A].

## 2. Late radiation morbidity from the same trial (Davis 2005) — [VERIFIED]

**Reference**
- Davis, A. M., O'Sullivan, B., Turcotte, R., Bell, R., Catton, C., Chabot, P., Wunder, J., Hammond, A., Benk, V., Kandel, R., Goddard, K., Freeman, C., Sadura, A., Zee, B., Day, A., Tu, D., & Pater, J. (2005). Late radiation morbidity following randomization to preoperative versus postoperative radiotherapy in extremity soft tissue sarcoma. *Radiotherapy and Oncology*, *75*(1), 48–53. https://doi.org/10.1016/j.radonc.2004.12.020 — PMID 15948265

**Population:** 129 evaluable patients assessed at **2 years** [A].
**Results (post-op 66 Gy vs pre-op 50 Gy)** [A]:
- Grade ≥2 subcutaneous fibrosis **48.2% (27/56) vs 31.5% (23/73), P = 0.07 (not significant)**
- Oedema 23.2% vs 15.5%, and joint stiffness 23.2% vs 17.8% (not significant)
- Patients with significant fibrosis, stiffness or oedema had lower MSTS and TESS function scores (all P < 0.01)
- **Field size** predicted fibrosis (P = 0.002) and joint stiffness (P = 0.006), and marginally predicted oedema (P = 0.06)

**Bottom line for teaching:** Pre-op RT means more early wound problems. Post-op RT means a trend to more late fibrosis, oedema and stiffness, and those late effects reduce limb function [A].

## 3. STRASS (EORTC 62092): pre-op RT for primary retroperitoneal sarcoma — [VERIFIED]

**References**
- Bonvalot, S., Gronchi, A., Le Péchoux, C., Swallow, C. J., Strauss, D., Meeus, P., van Coevorden, F., Stoldt, S., Stoeckle, E., Rutkowski, P., Rastrelli, M., Raut, C. P., Hompes, D., De Paoli, A., Sangalli, C., Honoré, C., Chung, P., Miah, A., Blay, J. Y., . . . Haas, R. L. (2020). Preoperative radiotherapy plus surgery versus surgery alone for patients with primary retroperitoneal sarcoma (EORTC-62092: STRASS): A multicentre, open-label, randomised, phase 3 trial. *The Lancet Oncology*, *21*(10), 1366–1377. https://doi.org/10.1016/S1470-2045(20)30446-0 — PMID 32941794
- (Pooled with off-trial patients) Callegaro, D., Raut, C. P., Ajayi, T., Strauss, D., Bonvalot, S., Ng, D., Stoeckle, E., Fairweather, M., Rutkowski, P., van Houdt, W. J., Gelderblom, H., Sangalli, C., Hayes, A., Honoré, C., Gladdy, R. A., Fau, M., Haas, R., Tzanis, D., Miah, A. B., . . . Gronchi, A. (2023). Preoperative radiotherapy in patients with primary retroperitoneal sarcoma: EORTC-62092 trial (STRASS) versus off-trial (STREXIT) results. *Annals of Surgery*, *278*(1), 127–134. https://doi.org/10.1097/SLA.0000000000005492 — PMID 35833413
- (Complications post hoc) Tirotta, F., Champezou, L., Fiore, M., Swallow, C. J., Strauss, D., Raut, C. P., van Houdt, W. J., Marreaud, S., Haas, R., Oppong, F. B., Gronchi, A., Bonvalot, S., & Ford, S. J. (2026). Preoperative radiotherapy and postoperative complications among patients with primary retroperitoneal sarcoma: A post hoc analysis of the EORTC-62092 (STRASS) phase 3 randomized clinical trial. *Annals of Surgery*. Advance online publication. https://doi.org/10.1097/SLA.0000000000007067 — PMID 41983724

**Design:** Phase 3, open-label, 31 centres in 13 countries (Europe and North America). Patients had localised primary operable RPS, WHO PS and ASA ≤2, and no prior treatment [A].
**Arms:** Surgery alone vs pre-op RT **50.4 Gy in 28 fractions of 1.8 Gy** (3D-CRT or IMRT) followed by surgery [A].
**Primary endpoint:** Abdominal recurrence-free survival (ARFS), investigator-assessed, ITT [A].
**Results:** 266 randomised (133 per arm); median follow-up 43.1 months [A].
- 96% of the surgery-alone arm had surgery; 89% of the RT arm had both RT and surgery.
- Median ARFS 4.5 years (95% CI 3.9–NE) with RT + surgery vs 5.0 years (3.4–NE) with surgery alone; **HR 1.01 (0.71–1.44), p = 0.95**.

**Toxicity (RT + surgery vs surgery alone)** [A]:
- Grade 3–4 lymphopenia 77% vs 1%, anaemia 12% vs 8%, hypoalbuminaemia 12% vs 4%
- Serious adverse events 24% vs 10%
- One treatment-related death with RT (gastropleural fistula)

**Authors' conclusion:** Pre-op RT "should not be considered as standard of care" for RPS [A].

**STREXIT pooled analysis (exploratory, not randomised)** [A]:
- Liposarcoma (n = 321): ARFS **HR 0.61 (0.42–0.89)** with RT
- Well-differentiated plus grade 1–2 dedifferentiated liposarcoma (n = 266): HR 0.63 (0.40–0.97)
- No benefit in G3 dedifferentiated liposarcoma or leiomyosarcoma; no association with OS or distant metastasis-free survival

**2026 post hoc analysis of complications** [A]:
- 242 patients; major complications (Clavien-Dindo ≥3 within 60 days) 19.5% with surgery alone vs 20.2% with pre-op RT, P = 0.90
- Adjusted OR 0.95 (0.48–1.87); consistent in the WDLPS/G1–2 DDLPS subgroup (OR 1.57, 0.56–4.41)

---

# B. First-line advanced/metastatic STS

## 4. EORTC 62012: doxorubicin vs intensified doxorubicin + ifosfamide — [VERIFIED]

**Reference**
- Judson, I., Verweij, J., Gelderblom, H., Hartmann, J. T., Schöffski, P., Blay, J.-Y., Kerst, J. M., Sufliarsky, J., Whelan, J., Hohenberger, P., Krarup-Hansen, A., Alcindor, T., Marreaud, S., Litière, S., Hermans, C., Fisher, C., Hogendoorn, P. C. W., dei Tos, A. P., & van der Graaf, W. T. A. (2014). Doxorubicin alone versus intensified doxorubicin plus ifosfamide for first-line treatment of advanced or metastatic soft-tissue sarcoma: A randomised controlled phase 3 trial. *The Lancet Oncology*, *15*(4), 415–423. https://doi.org/10.1016/S1470-2045(14)70063-4 — PMID 24618336

**Design:** Phase 3, 38 hospitals in 10 countries [A].
**Population:** High-grade (grade 2–3) locally advanced or metastatic STS, **age 18–60**, WHO PS 0–1 [A].
**Arms (every 3 weeks, up to 6 cycles)** [A]:
- Doxorubicin 75 mg/m² (IV bolus on day 1, or 72-h continuous infusion), vs
- Doxorubicin 75 mg/m² (25 mg/m²/day, days 1–3) **plus ifosfamide 10 g/m² over 4 days** with mesna and pegfilgrastim

**Primary endpoint:** OS (ITT) [A].
**Results:** 455 randomised (228 vs 227); median follow-up 56 and 59 months [A].

| Endpoint | Doxorubicin | Doxorubicin + ifosfamide | Effect |
|---|---|---|---|
| Median OS | 12.8 mo (95.5% CI 10.5–14.3) | 14.3 mo (12.5–16.5) | **HR 0.83 (95.5% CI 0.67–1.03); p = 0.076** |
| Median PFS | 4.6 mo (2.9–5.6) | 7.4 mo (6.6–8.3) | HR 0.74 (0.60–0.90); p = 0.003 |
| ORR | 14% (31/228) | 26% (60/227) | p < 0.0006 |

**Grade 3–4 toxicity (combination vs doxorubicin)** [A]:
- Febrile neutropenia 46% vs 13%
- Leucopenia 43% vs 18%; neutropenia 42% vs 37%
- Anaemia 35% vs 5%; thrombocytopenia 33% vs <1%

**Conclusion:** The combination is not supported for palliation "unless the specific goal is tumour shrinkage" [A].
**NP note:** Ifosfamide needs mesna, and growth-factor support was mandated (pegfilgrastim). Expect febrile neutropenia in about half of patients [A].

## 5. ANNOUNCE: doxorubicin ± olaratumab (negative confirmatory trial) — [VERIFIED]

**Reference**
- Tap, W. D., Wagner, A. J., Schöffski, P., Martin-Broto, J., Krarup-Hansen, A., Ganjoo, K. N., Yen, C.-C., Abdul Razak, A. R., Spira, A., Kawai, A., Le Cesne, A., Van Tine, B. A., Naito, Y., Park, S. H., Fedenko, A., Pápai, Z., Soldatenkova, V., Shahir, A., Mo, G., . . . Jones, R. L. (2020). Effect of doxorubicin plus olaratumab vs doxorubicin plus placebo on survival in patients with advanced soft tissue sarcomas: The ANNOUNCE randomized clinical trial. *JAMA*, *323*(13), 1266–1276. https://doi.org/10.1001/jama.2020.1707 — PMID 32259228

**Design:** Phase 3, double-blind, 110 sites in 25 countries, September 2015 – December 2018 [A].
**Population:** Anthracycline-naive adults with advanced STS, ECOG 0–1, LVEF ≥50% [A].
**Arms:** Doxorubicin 75 mg/m² on day 1 plus olaratumab (20 mg/kg in cycle 1, then 15 mg/kg) or placebo, on days 1 and 8. Up to 8 cycles of 21 days, then olaratumab or placebo alone [A].
**Dual primary endpoint:** OS in all STS and in leiomyosarcoma [A].
**Results:** 509 randomised (258 vs 251); 46.0% leiomyosarcoma; median follow-up 31 months [A].
- All STS: OS **20.4 vs 19.7 months, HR 1.05 (0.84–1.30), P = .69**
- Leiomyosarcoma: OS 21.6 vs 21.9 months, HR 0.95 (0.69–1.31), P = .76

**Grade ≥3 AEs (olaratumab vs placebo arm)** [A]: neutropenia 46.3% vs 49.0%; leukopenia 23.3% vs 23.7%; febrile neutropenia 17.5% vs 16.5%.
**Regulatory consequence:**
- TFDA: Lartruvo 樂除瘤 licence 衛部菌疫輸字第001075號, issued 2018-03-28 for use with doxorubicin; **self-cancelled 2019-09-04** [TFDA].
- Global withdrawal announced by Lilly in April 2019; FDA accelerated approval had been granted in October 2016 [NEWS: pharmaphorum; UK DHPC] [PARTIAL].

**Teaching point:** A classic example of a phase 2 OS signal that a phase 3 trial did not confirm [A].

## 6. LMS-04: doxorubicin + trabectedin → trabectedin maintenance in leiomyosarcoma — [VERIFIED]

**References**
- Pautier, P., Italiano, A., Piperno-Neumann, S., Chevreau, C., Penel, N., Firmin, N., Boudou-Rouquette, P., Bertucci, F., Balleyguier, C., Lebrun-Ly, V., Ray-Coquard, I., Kalbacher, E., Bardet, A., Bompas, E., Collard, O., Isambert, N., Guillemet, C., Rios, M., Archambaud, B., & Duffaud, F. (2022). Doxorubicin alone versus doxorubicin with trabectedin followed by trabectedin alone as first-line therapy for metastatic or unresectable leiomyosarcoma (LMS-04): A randomised, multicentre, open-label phase 3 trial. *The Lancet Oncology*, *23*(8), 1044–1054. https://doi.org/10.1016/S1470-2045(22)00380-1 — PMID 35835135
- (OS update) Pautier, P., Italiano, A., Piperno-Neumann, S., Chevreau, C., Penel, N., Firmin, N., Boudou-Rouquette, P., Bertucci, F., Lebrun-Ly, V., Ray-Coquard, I., Kalbacher, E., Bompas, E., Collard, O., Isambert, N., Guillemet, C., Rios, M., Le Cesne, A., Balleyguier, C., Archambaud, B., & Duffaud, F. (2024). Doxorubicin-trabectedin with trabectedin maintenance in leiomyosarcoma. *The New England Journal of Medicine*, *391*(9), 789–799. https://doi.org/10.1056/NEJMoa2403394 — PMID 39231341

**Design:** Phase 3, open-label, superiority; 20 French Sarcoma Group centres [A].
**Population:** Chemo-naive metastatic or unresectable uterine (n = 67) or soft-tissue (n = 83) leiomyosarcoma, ECOG 0–1 [A].
**Arms** [A]:
- Doxorubicin **75 mg/m²** every 3 weeks × 6 (n = 76), vs
- Doxorubicin **60 mg/m² + trabectedin 1.1 mg/m²** every 3 weeks × 6, then trabectedin maintenance (n = 74)
- Surgery for residual disease was allowed after 6 cycles in both arms

**Primary endpoint:** PFS by blinded independent central review (RECIST 1.1) [A].

| Endpoint | Doxorubicin | Dox + trabectedin | Effect | Source |
|---|---|---|---|---|
| PFS (2022) | 6.2 mo (4.1–7.1) | 12.2 mo (10.1–15.6) | **adj. HR 0.41 (0.29–0.58); p < 0.0001** | [A] Lancet Oncol |
| PFS (2024 update) | 6 mo (4–7) | 12 mo (10–16) | adj. HR 0.37 (0.26–0.53) | [A] NEJM |
| OS (2024; median FU 55 mo; 107 deaths) | 24 mo (19–31) | **33 mo (26–48)** | **adj. HR 0.65 (0.44–0.95)** | [A] NEJM |

**Grade 3–4 AEs (dox alone vs combination)** [A]:
- Neutropenia 13% vs **80%**
- Thrombocytopenia 0 vs **47%**
- Anaemia 5% vs 31%
- Febrile neutropenia 9% vs 28%
- Serious AEs 12% vs 20% (computed 15/74; the abstract misprints "201%")
- One treatment-related death, in the doxorubicin arm (cardiac failure)

**Regulatory status:** Not a labelled indication in Taiwan or the US (see flag 6). For trabectedin handling, see section 8.

## 7. GeDDiS: gemcitabine–docetaxel vs doxorubicin first line — [VERIFIED]

**Reference**
- Seddon, B., Strauss, S. J., Whelan, J., Leahy, M., Woll, P. J., Cowie, F., Rothermundt, C., Wood, Z., Benson, C., Ali, N., Marples, M., Veal, G. J., Jamieson, D., Küver, K., Tirabosco, R., Forsyth, S., Nash, S., Dehbi, H.-M., & Beare, S. (2017). Gemcitabine and docetaxel versus doxorubicin as first-line treatment in previously untreated advanced unresectable or metastatic soft-tissue sarcomas (GeDDiS): A randomised controlled phase 3 trial. *The Lancet Oncology*, *18*(10), 1397–1410. https://doi.org/10.1016/S1470-2045(17)30622-8 — PMID 28882536

**Design:** Phase 3; 24 UK hospitals and 1 SAKK (Switzerland) hospital [A].
**Population:** Trojani grade 2–3 STS with progression before enrolment and no prior chemotherapy [A].
**Arms (every 3 weeks × 6)** [A; FT]:
- Doxorubicin 75 mg/m² on day 1, vs
- Gemcitabine **675 mg/m² on days 1 and 8** (over 90 min) + docetaxel **75 mg/m² on day 8** (over 60 min)
- This is a deliberately lower dose than the Maki 900/100 schedule [FT discussion].

**Primary endpoint:** Proportion alive and progression-free at 24 weeks [A].
**Results:** 257 randomised (129 doxorubicin vs 128 gem–doc) [A; FT].
- 24-week PFS **46.3% (37.5–54.6) vs 46.4% (37.5–54.8)**
- Median PFS 23.3 vs 23.7 weeks; HR 1.28 (0.99–1.65), p = 0.06 (HR >1 favours doxorubicin)
- Median OS 76.3 vs 67.3 weeks; HR 1.14 (0.83–1.57), p = 0.41 [FT]

**Grade 3–4 AEs (doxorubicin vs gem–doc)** [A]:
- Neutropenia 25% vs 20%; febrile neutropenia 20% vs 12%
- Fatigue 6% vs 14%; oral mucositis 14% vs 2%; pain 8% vs 10%

**Conclusion:** Doxorubicin remains standard first line [A]. Gem–doc was harder to deliver (more delays, lower dose intensity) and had numerically worse global QoL [FT].

---

# C. Later-line STS

## 8. Trabectedin vs dacarbazine (ET743-SAR-3007) in liposarcoma/leiomyosarcoma — [VERIFIED]

**References**
- Demetri, G. D., von Mehren, M., Jones, R. L., Hensley, M. L., Schuetze, S. M., Staddon, A., Milhem, M., Elias, A., Ganjoo, K., Tawbi, H., Van Tine, B. A., Spira, A., Dean, A., Khokhar, N. Z., Park, Y. C., Knoblauch, R. E., Parekh, T. V., Maki, R. G., & Patel, S. R. (2016). Efficacy and safety of trabectedin or dacarbazine for metastatic liposarcoma or leiomyosarcoma after failure of conventional chemotherapy: Results of a phase III randomized multicenter clinical trial. *Journal of Clinical Oncology*, *34*(8), 786–793. https://doi.org/10.1200/JCO.2015.62.4734 — PMID 26371143
- (Final OS) Patel, S., von Mehren, M., Reed, D. R., Kaiser, P., Charlson, J., Ryan, C. W., Rushing, D., Livingston, M., Singh, A., Seth, R., Forscher, C., D'Amato, G., Chawla, S. P., McCarthy, S., Wang, G., Parekh, T., Knoblauch, R., Hensley, M. L., Maki, R. G., & Demetri, G. D. (2019). Overall survival and histology-specific subgroup analyses from a phase 3, randomized controlled study of trabectedin or dacarbazine in patients with advanced liposarcoma or leiomyosarcoma. *Cancer*, *125*(15), 2610–2620. https://doi.org/10.1002/cncr.32117 — PMID 31173362

**Design:** Phase 3, randomised **2:1**, open-label [A; L].
**Population:** LPS (dedifferentiated, myxoid/round cell or pleomorphic) or LMS after an anthracycline plus ifosfamide, or after an anthracycline plus ≥1 other cytotoxic regimen [L].
**Arms:** Trabectedin **1.5 mg/m² as a 24-h IV infusion every 3 weeks** (central line, dexamethasone 20 mg IV premedication) vs dacarbazine **1000 mg/m²** every 3 weeks [L-Yondelis].
**Primary endpoint:** OS [A].

| Endpoint | Trabectedin | Dacarbazine | Effect | Source |
|---|---|---|---|---|
| PFS (investigator) | 4.2 mo (3.0–4.8) | 1.5 mo (1.5–2.6) | **HR 0.55 (0.44–0.70); P < .001** | [A; L] |
| OS interim (64% censored) | 12.4 mo | 12.9 mo | HR 0.87; P = .37 | [A] |
| **OS final** (n = 577; 381 deaths) | 13.7 mo (12.2–16.0) | 13.1 mo (9.1–16.2) | **HR 0.93 (0.75–1.15); P = .49** | [FT; L] |
| ORR | 7% | 6% | — | [L] |
| Median DOR | 6.9 mo | 4.2 mo | — | [L] |

**Subgroups (final paper)** [FT]:
- PFS benefit in both LMS (4.3 vs 1.6 months) and LPS (3.0 vs 1.5 months)
- ≥6 cycles received: 42% vs 22%
- Post-study therapy (71% vs 69%) may have confounded OS

**Toxicity** [A; FT; L]:
- Grade 3–4 neutropenia 43% (lab-based)
- Transient transaminase rises
- Febrile neutropenia 4–7% vs 2%
- **Treatment-related deaths 9 (2%) vs 0**, mainly infection, rhabdomyolysis and renal failure

**Label warnings and handling (US)** [L-Yondelis]:
- Neutropenic sepsis: withhold if ANC <1,500/µL
- **Rhabdomyolysis: check CPK before each dose**; withhold if >2.5 × ULN
- Hepatotoxicity: moderate hepatic impairment dose is 0.9 mg/m²; do not give in severe impairment
- Cardiomyopathy, capillary leak syndrome, embryo-fetal toxicity
- **Central venous line required**
**Taiwan:** 友待 Yondelis 1 mg, 衛部藥輸字第027370號; indication LPS/LMS after an anthracycline-containing regimen [TFDA].

## 9. Eribulin vs dacarbazine (Study 309), with the liposarcoma subgroup — [VERIFIED]

**References**
- Schöffski, P., Chawla, S., Maki, R. G., Italiano, A., Gelderblom, H., Choy, E., Grignani, G., Camargo, V., Bauer, S., Rha, S. Y., Blay, J.-Y., Hohenberger, P., D'Adamo, D., Guo, M., Chmielowski, B., Le Cesne, A., Demetri, G. D., & Patel, S. R. (2016). Eribulin versus dacarbazine in previously treated patients with advanced liposarcoma or leiomyosarcoma: A randomised, open-label, multicentre, phase 3 trial. *The Lancet*, *387*(10028), 1629–1637. https://doi.org/10.1016/S0140-6736(15)01283-0 — PMID 26874885
- (Liposarcoma subgroup) Demetri, G. D., Schöffski, P., Grignani, G., Blay, J.-Y., Maki, R. G., Van Tine, B. A., Alcindor, T., Jones, R. L., D'Adamo, D. R., Guo, M., & Chawla, S. (2017). Activity of eribulin in patients with advanced liposarcoma demonstrated in a subgroup analysis from a randomized phase III study of eribulin versus dacarbazine. *Journal of Clinical Oncology*, *35*(30), 3433–3439. https://doi.org/10.1200/JCO.2016.71.6605 — PMID 28854066 (erratum PMID 29378157, not checked)

**Design:** Phase 3, open-label, 1:1, 110 sites in 22 countries [A].
**Population:** Intermediate- or high-grade LPS or LMS after ≥2 prior systemic regimens including an anthracycline [A].
**Arms (every 21 days)** [A]:
- Eribulin **1.4 mg/m² IV on days 1 and 8**, vs
- Dacarbazine 850, 1000 or 1200 mg/m² IV on day 1

**Primary endpoint:** OS [A].

| Population | Eribulin | Dacarbazine | Effect | Source |
|---|---|---|---|---|
| All (n = 228 vs 224) | OS 13.5 mo (10.9–15.6) | 11.5 mo (9.6–13.0) | **HR 0.77 (0.62–0.95); p = 0.0169** | [A] |
| All (label analysis, n = 225 vs 221) | OS 13.5 mo | 11.3 mo | HR 0.75 (0.61–0.94); PFS 2.6 vs 2.6 mo, HR 0.86 (0.69–1.06) | [L] |
| **Liposarcoma** (n = 71 vs 72) | **OS 15.6 mo** | 8.4 mo | **HR 0.51 (0.35–0.75); P < .001** | [A JCO; L] |
| Liposarcoma PFS | 2.9 mo | 1.7 mo | HR 0.52 (0.35–0.78); P = .0015 | [A JCO; L] |
| Leiomyosarcoma (n = 154 vs 149) | OS 12.8 mo | 12.3 mo | HR 0.90 (0.69–1.18); PFS HR 1.05 (0.81–1.35) | [L] |

ORR was very low: 1.4% vs 0% in LPS; 4.0% vs 5.0% overall [L].
**Safety:** Grade ≥3 AEs 67% vs 56%; deaths 4% vs 1% (one treatment-related, eribulin arm) [A].
**Label dosing** [L-eribulin generic label, which reproduces the Halaven text; the openFDA Halaven record is a stub]:
- Mild hepatic impairment (Child-Pugh A): 1.1 mg/m²; moderate (Child-Pugh B): 0.7 mg/m²
- CrCl 15–49 mL/min: 1.1 mg/m²
- Hold the dose for ANC <1,000/mm³, platelets <75,000/mm³ or grade 3–4 non-haematological toxicity; assess neuropathy before each dose
- Give IV over 2–5 min; do not dilute in dextrose
**Taiwan:** Halaven 賀樂維 0.5 mg/mL (衛部藥輸字第026140號) and generics; indication **liposarcoma only** (unresectable or metastatic, after an anthracycline) [TFDA].

## 10. PALETTE: pazopanib vs placebo in non-adipocytic STS — [VERIFIED]

**Reference**
- van der Graaf, W. T. A., Blay, J.-Y., Chawla, S. P., Kim, D.-W., Bui-Nguyen, B., Casali, P. G., Schöffski, P., Aglietta, M., Staddon, A. P., Beppu, Y., Le Cesne, A., Gelderblom, H., Judson, I. R., Araki, N., Ouali, M., Marreaud, S., Hodge, R., Dewji, M. R., Coens, C., . . . Hohenberger, P. (2012). Pazopanib for metastatic soft-tissue sarcoma (PALETTE): A randomised, double-blind, placebo-controlled phase 3 trial. *The Lancet*, *379*(9829), 1879–1886. https://doi.org/10.1016/S0140-6736(12)60651-5 — PMID 22595799

**Design:** Phase 3, double-blind, **2:1**, 72 institutions in 13 countries, no crossover [A].
**Population:** Angiogenesis-inhibitor-naive metastatic **non-adipocytic** STS after chemotherapy [A]. GIST and adipocytic sarcoma were excluded [L].
**Arms:** Pazopanib **800 mg once daily** vs placebo [A].
**Primary endpoint:** PFS [A].
**Results:** 369 randomised (246 vs 123) [A].
- PFS **4.6 (3.7–4.8) vs 1.6 (0.9–1.8) months, HR 0.31 (0.24–0.40), p < 0.0001**
- OS 12.5 vs 10.7 months, HR 0.86 (0.67–1.11), p = 0.25

**US label table (independent review)** [L]:
- PFS HR 0.35 (0.26–0.48)
- Leiomyosarcoma HR 0.37; synovial sarcoma HR 0.43; other STS HR 0.39
- ORR 4%

**AEs (pazopanib vs placebo)** [A]:
- Fatigue 65% vs 49%; diarrhoea 58% vs 16%; nausea 54% vs 28%
- Weight loss 48% vs 20%; hypertension 41% vs 7%

**Label** [L-Votrient]:
- **Boxed warning: hepatotoxicity**
- Take without food (≥1 h before or 2 h after a meal); do not crush
- STS first dose reduction is to 600 mg; moderate hepatic impairment 200 mg
- Pneumothorax 3.3% in the STS trial
- Limitation of use: efficacy **not demonstrated in adipocytic STS or GIST**

**Taiwan:** Votrient 福退癌 200 mg (衛署藥輸字第025433號) and generics; the same STS indication and the same adipocytic/GIST limitation [TFDA].

---

# D. Histology-specific agents

## 11. Tazemetostat in INI1-deficient epithelioid sarcoma (EZH-202 cohort 5) — [VERIFIED]

**Reference**
- Gounder, M., Schöffski, P., Jones, R. L., Agulnik, M., Cote, G. M., Villalobos, V. M., Attia, S., Chugh, R., Chen, T. W.-W., Jahan, T., Loggers, E. T., Gupta, A., Italiano, A., Demetri, G. D., Ratan, R., Davis, L. E., Mir, O., Dileo, P., Van Tine, B. A., . . . Stacchiotti, S. (2020). Tazemetostat in advanced epithelioid sarcoma with loss of INI1/SMARCB1: An international, open-label, phase 2 basket study. *The Lancet Oncology*, *21*(11), 1423–1432. https://doi.org/10.1016/S1470-2045(20)30451-4 — PMID 33035459

**Design:** Phase 2 basket study, single-arm cohort 5. Sites were in 9 countries, **including Taiwan** [A].
**Population:** Epithelioid sarcoma, age ≥16, with INI1 loss on IHC and/or biallelic SMARCB1 alteration, ECOG 0–2 [A].
**Dose:** Tazemetostat (oral EZH2 inhibitor) **800 mg twice daily**, continuous 28-day cycles [A; L].
**Primary endpoint:** Investigator-assessed ORR [A].
**Results (n = 62)** [A]:
- ORR **15% (95% CI 7–26)**; median DOR not reached (9.2–NE)
- Disease control at 32 weeks 26% (16–39); time to response 3.9 months
- PFS 5.5 months (3.4–5.9); OS 19.0 months (11.0–NE)
**Safety:** Grade ≥3 treatment-related AEs: anaemia 6%, weight loss 3%. Two treatment-related SAEs (seizure, haemoptysis). No treatment-related deaths [A].
**US label** [L-Tazverik]:
- **Accelerated approval** (still in place) for age ≥16 with ES not eligible for complete resection
- ORR by BICR 15% (7–26); CR 1.6%
- **Secondary malignancies** (MDS, AML, B-ALL) in 1.7% of 758 adults; T-cell lymphoblastic lymphoma in one child
- Dose reductions: 600 mg, then 400 mg BID
- Confirmatory phase 1b/3 trial of tazemetostat + doxorubicin first line, NCT04204941 [A]
**Taiwan:** No TFDA licence (active or cancelled) [TFDA].

## 12. Afamitresgene autoleucel (afami-cel; Tecelra), SPEARHEAD-1 — [VERIFIED]

**References**
- D'Angelo, S. P., Araujo, D. M., Abdul Razak, A. R., Agulnik, M., Attia, S., Blay, J.-Y., Carrasco Garcia, I., Charlson, J. A., Choy, E., Demetri, G. D., Druta, M., Forcade, E., Ganjoo, K. N., Glod, J., Keedy, V. L., Le Cesne, A., Liebner, D. A., Moreno, V., Pollack, S. M., . . . Van Tine, B. A. (2024). Afamitresgene autoleucel for advanced synovial sarcoma and myxoid round cell liposarcoma (SPEARHEAD-1): An international, open-label, phase 2 trial. *The Lancet*, *403*(10435), 1460–1471. https://doi.org/10.1016/S0140-6736(24)00319-2 — PMID 38554725
- (FDA review) Barnett, K. K., Johnson, A. R., Das, A., Lee, C.-H. J., Wang, C., Wang, X., Cho, E. S., Kluetz, P. G., & Fashoyin-Aje, L. A. (2025). FDA approval summary: Afamitresgene autoleucel for adults with HLA-restricted, MAGE-A4-positive unresectable or metastatic synovial sarcoma after prior chemotherapy. *Clinical Cancer Research*, *31*(15), 3112–3117. https://doi.org/10.1158/1078-0432.CCR-25-0595 — PMID 40423661

**Mechanism:** Autologous CD4⁺/CD8⁺ T cells with a lentiviral, affinity-enhanced **MAGE-A4-specific TCR** [FT]. Patients must be HLA-A*02 positive and MAGE-A4 positive.
**Design:** Phase 2, open-label, non-randomised, 23 sites; cohort 1 reported [A].
**Population:** Age 16–75; HLA-A*02; MAGE-A4-expressing synovial sarcoma (n = 44) or MRCLS (n = 8); ≥1 prior anthracycline- or ifosfamide-containing line; median 3 prior lines [A].
**Treatment:** Lymphodepletion with fludarabine 30 mg/m²/day (day −7 to −4) and cyclophosphamide 600 mg/m²/day (day −7 to −5), then a single infusion [L; FT FDA summary].
**Primary endpoint:** ORR by masked independent review [A].

| Source | Population | ORR (95% CI) | Median DOR |
|---|---|---|---|
| Lancet 2024 [A; FT] | All cohort 1 (n = 52) | 37% (24–51) | — |
| Lancet 2024 [A; FT] | Synovial sarcoma (n = 44) | **39% (24–55)** | **11.6 mo** (4.4–18.0) |
| Lancet 2024 [A; FT] | MRCLS (n = 8) | 25% (3–65) | 4.2 mo |
| FDA re-review [A; FT] | Synovial sarcoma (n = 44) | 43.2% (28.4–59.0); 2 CR | **6.0 mo** (4.6–NR) |
| Current US label [L] | Cohorts 1–3 efficacy-evaluable (n = 137) | 43.8% (35.3–52.5); 5 CR | 5.3 mo (4.5–8.2) |

- Median OS (Lancet, all cohort 1) was 15.4 months (10.9–28.7). OS was not reached in synovial sarcoma responders (70% alive at 24 months) [FT].
- During review the FDA found data-quality and study-conduct problems and ordered an independent imaging re-review; approval was based on the re-review [A FDA summary].

**Toxicity (Lancet)** [A; FT]:
- CRS in 71% (one grade 3), median onset day 2
- Grade ≥3 cytopenias: lymphopenia 96%, neutropenia 85%, leukopenia 81%
- No treatment-related deaths

**FDA summary safety** [A]: CRS 75% (grade ≥3 in 2%); grade ≥3 infections 14%; prolonged cytopenias; one EBV-positive lymphoproliferative disorder.
**US label (effective 2026-07-15)** [L-Tecelra]:
- **Boxed warning: CRS**
- Indication now **adults and children ≥12 years**; HLA-A*02:01P/02:02P/02:03P/02:06P positive (A*02:05P excluded); MAGE-A4 positive by companion diagnostic
- Dose range **1.62–10 × 10⁹** MAGE-A4 TCR⁺ T cells
- Premedicate with acetaminophen and an H1-antihistamine; **no prophylactic systemic steroids; no leukodepleting filter**
- Recent major changes (06/2026): indication, **accelerated-approval statement removed**, dose, ICANS warning added
**Taiwan:** No TFDA licence [TFDA].

## 13. Letetresgene autoleucel (lete-cel; NY-ESO-1 TCR-T) — [PARTIAL; not approved]

**Reference (only peer-reviewed sarcoma efficacy paper found)**
- D'Angelo, S. P., Druta, M., Van Tine, B. A., Liebner, D., Schuetze, S. M., Tap, W. D., Preston, J., Goodison, S., D'Souza, J. W., Kapoor, G. S., Suchindran, S., Zajic, S., Bhaskar, A., Kaczynski, H., Kim, J., Klohe, E., Corigliano, E., Eleftheriadou, I., Nathenson, M. J., & Somaiah, N. (2025). Letetresgene autoleucel in advanced/metastatic myxoid/round cell liposarcoma. *Journal of Clinical Oncology*, *43*(15), 1777–1788. https://doi.org/10.1200/JCO-24-01466 — PMID 39836945

**Pilot study (NCT02992743), MRCLS** [A; FT]:
- Eligibility: HLA-A*02:01, *02:05 and/or *02:06; NY-ESO-1 ≥30% of cells 2+/3+
- Cohort 1: reduced lymphodepletion (fludarabine 30 mg/m² × 3 days + cyclophosphamide 600 mg/m² × 3 days)
- Cohort 2: standard lymphodepletion (fludarabine 30 mg/m² × 4 days)
- ORR 20% (2.5–55.6) in cohort 1 vs 40% (12.2–73.8) in cohort 2 (n = 10 each)
- PFS 5.4 vs 8.7 months
- CRS 60% vs 100%; grade ≥3 CRS in 1 and 3 patients
- One potentially treatment-related death (cardiac arrest, day 161)

**Pivotal IGNYTE-ESO (NCT03967223)** [NEWS: Targeted Oncology, 2025-01-13]:
- ORR by independent review 42% (27/64; 6 CR, 21 PR); synovial sarcoma 41%, MRCLS 43%
- Median DOR 12.2 months (6.8–19.5)
- FDA Breakthrough Therapy designation for MRCLS (January 2025)
- **No peer-reviewed IGNYTE-ESO paper on PubMed as of 2026-10-29.**

**Regulatory status:**
- **Not on FDA's approved cell and gene therapy list** (content current 2026-09-17) [CBER]; no openFDA label; no TFDA licence.
- The company planned a rolling BLA starting late 2025 [NEWS]; the outcome was not found.
- Do not describe lete-cel as approved.

## 14. DeFi: nirogacestat for progressing desmoid tumours — [VERIFIED]

**References**
- Gounder, M., Ratan, R., Alcindor, T., Schöffski, P., van der Graaf, W. T., Wilky, B. A., Riedel, R. F., Lim, A., Smith, L. M., Moody, S., Attia, S., Chawla, S., D'Amato, G., Federman, N., Merriam, P., Van Tine, B. A., Vincenzi, B., Benson, C., Bui, N. Q., . . . Kasper, B. (2023). Nirogacestat, a γ-secretase inhibitor for desmoid tumors. *The New England Journal of Medicine*, *388*(10), 898–912. https://doi.org/10.1056/NEJMoa2210140 — PMID 36884323
- (Long-term) Ratan, R., Kasper, B., Alcindor, T., Schöffski, P., van der Graaf, W. T. A., Federman, N., Bui, N. Q., D'Amato, G., Riedel, R. F., Attia, S., Chawla, S., Lim, A., Tumminello, B., Oton, A. B., Chu, Y., Zhou, S., & Gounder, M. (2025). Efficacy and safety of long-term continuous nirogacestat treatment in adults with desmoid tumors: Results from the DeFi trial. *Journal of Clinical Oncology*, *43*(34), 3646–3651. https://doi.org/10.1200/JCO-25-00582 — PMID 41115259

**Design:** Phase 3, double-blind, 1:1 [A]. 37 sites in the US, Canada and Europe; median age 34 [FT].
**Arms:** Nirogacestat **150 mg twice daily** vs placebo [A].
**Primary endpoint:** PFS (imaging-based or clinical progression) [A; FT].
**Results:** 142 randomised (70 vs 72) [A; FT].
- PFS **HR 0.29 (0.15–0.55), P < 0.001**. Median not reached vs 15.1 months (8.4–NE) [FT]
- Event-free at 2 years: 76% vs 44%
- ORR **41% vs 8%** (CR 7% vs 0%); median time to response 5.6 vs 11.1 months
- Long-term: ORR 45.7% (32/70) with up to 4 years of treatment; median exposure 33.6 months [A JCO 2025]

**Toxicity** [A; FT]:
- Diarrhoea 84%, nausea 54%, fatigue 51%, hypophosphataemia 42%, maculopapular rash 32%
- 95% of AEs were grade 1–2; dose reductions 42%; discontinuation for AEs 20%
- **Ovarian dysfunction in 27/36 (75%) women of childbearing potential**, resolved in 20 (74%); median onset 8.9 weeks

**US label** [L-Ogsiveo]:
- Grade 3 diarrhoea 16%
- Warnings: ovarian toxicity, hepatotoxicity, **non-melanoma skin cancers** (skin exams), hypophosphataemia/hypokalaemia monitoring, hypersensitivity, embryo-fetal toxicity
- Reduced dose 100 mg BID
**Taiwan:** No TFDA licence [TFDA].

## 15. ENLIVEN: pexidartinib for tenosynovial giant cell tumour (TGCT) — [VERIFIED]

**References**
- Tap, W. D., Gelderblom, H., Palmerini, E., Desai, J., Bauer, S., Blay, J.-Y., Alcindor, T., Ganjoo, K., Martín-Broto, J., Ryan, C. W., Thomas, D. M., Peterfy, C., Healey, J. H., van de Sande, M., Gelhorn, H. L., Shuster, D. E., Wang, Q., Yver, A., Hsu, H. H., . . . Wagner, A. J. (2019). Pexidartinib versus placebo for advanced tenosynovial giant cell tumour (ENLIVEN): A randomised phase 3 trial. *The Lancet*, *394*(10197), 478–487. https://doi.org/10.1016/S0140-6736(19)30764-0 — PMID 31229240
- (Final) Wagner, A. J., Tap, W. D., Bauer, S., Blay, J.-Y., Desai, J., Gelderblom, H., Palmerini, E., Ryan, C. W., Peterfy, C., Healey, J. H., van de Sande, M., Qian, M., Shuster, D. E., Rajper, A., Ye, X., Tecson, K., Wooddell, M. J., & Stacchiotti, S. (2025). Long-term efficacy and safety of pexidartinib in patients with tenosynovial giant cell tumor: Final results of the ENLIVEN study. *The Oncologist*, *30*(7), Article oyae345. https://doi.org/10.1093/oncolo/oyae345 — PMID 40613752

**Design:** Phase 3, two parts (part 1 double-blind, 1:1) [A].
**Dose in the trial:** **1000 mg/day for 2 weeks** (400 mg morning, 600 mg evening), then **800 mg/day** (400 mg BID) for 22 weeks [A].
**Primary endpoint:** ORR at week 25 by RECIST (central review) [A].
**Results:** 120 randomised (61 vs 59) [A; FT].
- Enrolment stopped 6 patients short of target because of mixed or cholestatic hepatotoxicity [A]
- ORR **39% vs 0%** (difference 39%, 95% CI 27–53), p < 0.0001
- TVS ORR 56% vs 0% [FT]
- Final analysis (91 patients ever treated, median follow-up 31.2 months): ORR 60.4% by RECIST and 68.1% by TVS [A Oncologist]

**Toxicity** [A; FT]:
- Hair colour change 67%, fatigue 54%, AST rise 39%, nausea 38%, ALT rise 28%, dysgeusia 25%
- **3 patients had mixed or cholestatic hepatotoxicity**; one lasted about 7 months and was biopsy-confirmed
- Grade 3–4 AEs 44% vs 12%
- Final analysis: AST or ALT ≥3 × ULN in 31%, ≥5 × ULN in 19% [A Oncologist]

**Current US label (effective 2025-01-16)** [L-Turalio]:
- **250 mg twice daily with a low-fat meal** (about 11–14 g fat); a high-fat meal raises exposure
- **Boxed warning: hepatotoxicity, including vanishing bile duct syndrome**
- REMS-restricted distribution
- Dose reductions: 375 mg/day, then 250 mg/day
**Taiwan:** TURALIO 圖拉留 licence **cancelled 2026-02-03** (self-requested) [TFDA] (see flag 13).

## 16. MOTION: vimseltinib for TGCT — [VERIFIED]

**References**
- Gelderblom, H., Bhadri, V., Stacchiotti, S., Bauer, S., Wagner, A. J., van de Sande, M., Bernthal, N. M., López Pousa, A., Razak, A. A., Italiano, A., Ahmed, M., Le Cesne, A., Tinoco, G., Boye, K., Martín-Broto, J., Palmerini, E., Tafuto, S., Pratap, S., Powers, B. C., . . . Tap, W. D. (2024). Vimseltinib versus placebo for tenosynovial giant cell tumour (MOTION): A multicentre, randomised, double-blind, placebo-controlled, phase 3 trial. *The Lancet*, *403*(10445), 2709–2719. https://doi.org/10.1016/S0140-6736(24)00885-7 — PMID 38843860
- (Long-term) Bhadri, V., Gelderblom, H., Stacchiotti, S., Bauer, S., Wagner, A. J., van de Sande, M., Bernthal, N. M., López Pousa, A., Abdul Razak, A., Italiano, A., Ahmed, M., Le Cesne, A., Tinoco, G., Boye, K., Martín-Broto, J., Palmerini, E., Tafuto, S., Pratap, S., Powers, B. C., . . . Tap, W. D. (2026). Long-term efficacy, clinical outcomes, and safety of vimseltinib in patients with tenosynovial giant cell tumor: Results from the MOTION phase 3 trial. *The Oncologist*. Advance online publication. https://doi.org/10.1093/oncolo/oyag421 — PMID 42898002

**Design:** Phase 3, double-blind, **2:1**, 35 hospitals in 13 countries [A].
**Arms:** Vimseltinib (switch-control CSF1R TKI) **30 mg orally twice weekly** vs placebo, for 24 weeks [A].
**Primary endpoint:** ORR at week 25 by independent review (RECIST 1.1) [A].
**Results:** 123 randomised (83 vs 40) [A; FT].
- ORR **40% vs 0%** (difference 40%, 95% CI 29–51), p < 0.0001
- TVS ORR 67% vs 0%
- Active range of motion improved 18.4% vs 3.8% [FT]
- Long-term ORR on study: 48% (40/83) for those randomised to vimseltinib; 54% (19/35) after crossover [A Oncologist 2026]

**Toxicity** [A; FT]:
- Grade 3–4 TEAEs 37% vs 10%; the only grade 3–4 TEAE in >5% was **CPK increase (10%)**
- Periorbital oedema 45%, fatigue 33%, face oedema 31%
- **No cholestatic hepatotoxicity or drug-induced liver injury**

**US label** [L-Romvimza]:
- 30 mg twice weekly with **≥72 h between doses** (blister pack schedule)
- Hepatotoxicity warning (class effect of another CSF1R inhibitor; grade 3 AST 2%, ALT 1%)
- Serum creatinine can rise without a real fall in renal function
- Tartrazine and sunset yellow dye allergy warning
**Taiwan:** No TFDA licence [TFDA].

## 17. AMPECT: nab-sirolimus (Fyarro) for malignant PEComa — [VERIFIED]

**References**
- Wagner, A. J., Ravi, V., Riedel, R. F., Ganjoo, K., Van Tine, B. A., Chugh, R., Cranmer, L., Gordon, E. M., Hornick, J. L., Du, H., Grigorian, B., Schmid, A. N., Hou, S., Harris, K., Kwiatkowski, D. J., Desai, N. P., & Dickson, M. A. (2021). nab-Sirolimus for patients with malignant perivascular epithelioid cell tumors. *Journal of Clinical Oncology*, *39*(33), 3660–3670. https://doi.org/10.1200/JCO.21.01728 — PMID 34637337 (erratum PMID 37890128, not checked)
- (Final) Wagner, A. J., Ravi, V., Riedel, R. F., Ganjoo, K., Van Tine, B. A., Chugh, R., Cranmer, L., Gordon, E. M., Hornick, J. L., Du, H., Ding, L., Schmid, A. N., Navarro, W. H., Kwiatkowski, D. J., & Dickson, M. A. (2024). Phase II trial of nab-sirolimus in patients with advanced malignant perivascular epithelioid cell tumors (AMPECT): Long-term efficacy and safety update. *Journal of Clinical Oncology*, *42*(13), 1472–1476. https://doi.org/10.1200/JCO.23.02266 — PMID 38427923

**Design:** Phase 2, single-arm registration trial [A].
**Dose:** **100 mg/m² IV on days 1 and 8 of a 21-day cycle** [A; L].
**Primary endpoint:** ORR by independent radiology review [A].
**Results:** 34 treated, 31 evaluable for efficacy [A].
- Primary analysis: ORR **39% (12/31; 95% CI 22–58)**, 1 CR; 67% of responses by week 6
- PFS 10.6 months (5.5–NR); OS 40.8 months
- **TSC2-mutant tumours: 8/9 (89%) responded vs 2/16 (13%)** without TSC2 mutation
- Final analysis: ORR 38.7% (21.8–57.8); **median DOR 39.7 months**; PFS 10.6 months (5.5–41.2); OS 53.1 months (22.2–NR)

**Toxicity** [FT; A]:
- Mucositis/stomatitis 79–82%, fatigue 59–62%, rash 56–62%
- Anaemia 47%, thrombocytopenia 32%
- **Non-infectious pneumonitis 18% (grade 1–2)**
- No grade ≥4 treatment-related AEs; dose reductions 34%

**US label** [L-Fyarro]:
- Infuse over 30 min
- Dose reductions: 75, then 56, then 45 mg/m²
- Warnings: stomatitis, myelosuppression, infections, hypokalaemia and hyperglycaemia, ILD/pneumonitis
**Taiwan:** No TFDA licence for Fyarro [TFDA].

---

# E. GIST

## 18. Adjuvant imatinib 3 years vs 1 year (SSG XVIII/AIO) with updates — [VERIFIED]

**References**
- Joensuu, H., Eriksson, M., Sundby Hall, K., Hartmann, J. T., Pink, D., Schütte, J., Ramadori, G., Hohenberger, P., Duyster, J., Al-Batran, S.-E., Schlemmer, M., Bauer, S., Wardelmann, E., Sarlomo-Rikala, M., Nilsson, B., Sihto, H., Monge, O. R., Bono, P., Kallio, R., . . . Reichardt, P. (2012). One vs three years of adjuvant imatinib for operable gastrointestinal stromal tumor: A randomized trial. *JAMA*, *307*(12), 1265–1272. https://doi.org/10.1001/jama.2012.347 — PMID 22453568
- Joensuu, H., Eriksson, M., Sundby Hall, K., Reichardt, A., Hartmann, J. T., Pink, D., Ramadori, G., Hohenberger, P., Al-Batran, S.-E., Schlemmer, M., Bauer, S., Wardelmann, E., Nilsson, B., Sihto, H., Bono, P., Kallio, R., Junnila, J., Alvegård, T., & Reichardt, P. (2016). Adjuvant imatinib for high-risk GI stromal tumor: Analysis of a randomized trial. *Journal of Clinical Oncology*, *34*(3), 244–250. https://doi.org/10.1200/JCO.2015.62.9170 — PMID 26527782
- Joensuu, H., Eriksson, M., Sundby Hall, K., Reichardt, A., Hermes, B., Schütte, J., Cameron, S., Hohenberger, P., Jost, P. J., Al-Batran, S.-E., Lindner, L. H., Bauer, S., Wardelmann, E., Nilsson, B., Kallio, R., Jaakkola, P., Junnila, J., Alvegård, T., & Reichardt, P. (2020). Survival outcomes associated with 3 years vs 1 year of adjuvant imatinib for patients with high-risk gastrointestinal stromal tumors: An analysis of a randomized clinical trial after 10-year follow-up. *JAMA Oncology*, *6*(8), 1241–1246. https://doi.org/10.1001/jamaoncol.2020.2091 — PMID 32469385

**Design:** Phase 3, open-label, 1:1; 24 hospitals in Finland, Germany, Norway and Sweden; enrolled 2004–2008 [A].
**Population:** KIT-positive GIST after macroscopically complete surgery, at **high risk by modified NIH criteria** [A].
**Arms:** Imatinib **400 mg/day** for 12 vs 36 months, started within 12 weeks of surgery [A].
**Primary endpoint:** RFS [A].

| Analysis | Median FU | RFS (36 vs 12 mo) | OS (36 vs 12 mo) |
|---|---|---|---|
| JAMA 2012 | 54 mo | 5-y RFS 65.6% vs 47.9%; **HR 0.46 (0.32–0.65); P < .001** | 5-y OS 92.0% vs 81.7%; **HR 0.45 (0.22–0.89); P = .02** |
| JCO 2016 | 90 mo | 5-y RFS 71.1% vs 52.3%; HR 0.60 (0.44–0.81) | 5-y OS 91.9% vs 85.3%; HR 0.60 (0.37–0.97); P = .036 |
| JAMA Oncol 2020 | 119 mo | 10-y RFS 52.5% vs 41.8%; HR 0.66 (0.49–0.87); P = .003 | **10-y OS 79.0% vs 65.3%; HR 0.55 (0.37–0.83); P = .004** |

- Central pathology confirmed GIST in 96%; KIT or PDGFRA mutation found in 91% [A 2012]
- Discontinuation for reasons other than recurrence: 12.6% (12-month arm) vs 25.8% (36-month arm) [A 2012]
- The authors estimate that about 50% of deaths in the first 10 years could be avoided with longer adjuvant treatment [A 2020]

**US label** [L-Gleevec]: adjuvant dose 400 mg/day; "three years of Gleevec is recommended" in the Study 2 population; optimal duration unknown.
**Taiwan** [TFDA]: Glivec 基利克 indication includes adjuvant treatment of adult KIT (CD117)-positive GIST after complete gross resection.
**NCCN Patients (GIST 2026)** [PG]: for high-risk disease, imatinib "may be given for at least 3 years after surgery".

**Related adjuvant evidence**
- **EORTC 62024 final** (2 years of imatinib vs observation; n = 908; median follow-up 9.1 years) [A]:
  - Primary endpoint, imatinib failure-free survival: HR 0.87 (95.7% CI 0.65–1.15), P = 0.31 (not significant)
  - RFS HR 0.71 (0.57–0.89); OS HR 0.88 (0.65–1.21)
  - Casali, P. G., Le Cesne, A., Velasco, A. P., Kotasek, D., Rutkowski, P., Hohenberger, P., Fumagalli, E., Judson, I. R., Italiano, A., Gelderblom, H., Penel, N., Hartmann, J. T., Duffaud, F., Goldstein, D., Martin-Broto, J., Gronchi, A., Wardelmann, E., Marréaud, S., Zalcberg, J. R., . . . Blay, J.-Y. (2021). Final analysis of the randomized trial on imatinib as an adjuvant in localized gastrointestinal stromal tumors (GIST) from the EORTC Soft Tissue and Bone Sarcoma Group (STBSG), the Australasian Gastro-Intestinal Trials Group (AGITG), UNICANCER, French Sarcoma Group (FSG), Italian Sarcoma Group (ISG), and Spanish Group for Research on Sarcomas (GEIS). *Annals of Oncology*, *32*(4), 533–541. https://doi.org/10.1016/j.annonc.2021.01.004 — PMID 33482247
- **KIT exon 9 adjuvant cohort** (observational, n = 367, 35 centres) [A]:
  - Adjuvant imatinib associated with lower early recurrence or death (HR 0.19, 0.10–0.36), with the effect fading over time, and better OS (HR 0.37, 0.17–0.83)
  - No difference between 400 and 800 mg in 257 high-risk patients
  - Napolitano, A., Joensuu, H., Rothschild, S., Evans, D., Heinrich, M. C., Sutton, T. L., Mayo, S. C., Boye, K., Falkenhorst, J., Le Cesne, A., Hohenberger, P., Rutkowski, P., van Houdt, W. J., Steeghs, N., Gelderblom, H., Desar, I. M. E., Pantaleo, M. A., Nishida, T., Reichardt, P., . . . Vincenzi, B. (2026). Adjuvant imatinib or observation in patients with gastrointestinal stromal tumors with KIT exon 9 mutations. *JAMA Oncology*, *12*(4), 407–412. https://doi.org/10.1001/jamaoncol.2026.0007 — PMID 41746633
- **SSG XXII (3 vs 5 years):** no results found on PubMed [UNVERIFIED].

## 19. Imatinib 400 vs 800 mg and KIT exon 9 — [PARTIAL]

**References**
- Gastrointestinal Stromal Tumor Meta-Analysis Group (MetaGIST). (2010). Comparison of two doses of imatinib for the treatment of unresectable or metastatic gastrointestinal stromal tumors: A meta-analysis of 1,640 patients. *Journal of Clinical Oncology*, *28*(7), 1247–1253. https://doi.org/10.1200/JCO.2009.24.2099 — PMID 20124181
- Debiec-Rychter, M., Sciot, R., Le Cesne, A., Schlemmer, M., Hohenberger, P., van Oosterom, A. T., Blay, J.-Y., Leyvraz, S., Stul, M., Casali, P. G., Zalcberg, J., Verweij, J., Van Glabbeke, M., Hagemeijer, A., & Judson, I. (2006). KIT mutations and dose selection for imatinib in patients with advanced gastrointestinal stromal tumours. *European Journal of Cancer*, *42*(8), 1093–1103. https://doi.org/10.1016/j.ejca.2006.01.030 — PMID 16624552

**MetaGIST** (2 randomised trials, 400 mg daily vs 400 mg twice daily; median follow-up 45 months) [A]:
- Small but significant PFS advantage with high dose; **OS identical**
- Mutation status was the only predictive factor: the PFS (and ORR) benefit of high dose was confined to **KIT exon 9**
- Exon 9, wild-type and "other" mutations all had worse prognosis than exon 11
**EORTC 62005 mutation analysis (n = 377)** [A]:
- KIT exon 9 raised the relative risk of progression by 171% and of death by 190% vs exon 11
- In exon 9 tumours, high dose improved PFS (P = 0.0013; relative risk reduction 61%)

**Not verified:** median PFS by dose within exon 9, and the absolute ORR difference (MetaGIST full text unreachable; PMC/Europe PMC blocked) [UNVERIFIED].
**Label and guideline wording:**
- US label: start 400 mg/day; escalation to 800 mg (400 mg BID) "may be considered" on progression; no exon 9 wording [L-Gleevec]
- NCCN Patients GIST 2026: escalating imatinib "may work best in people with KIT exon 9 mutations" [PG]
- INTRIGUE: exon 9 patients did better on sunitinib than ripretinib in second line (section 23)

## 20. Sunitinib after imatinib failure (Demetri 2006) — [VERIFIED]

**References**
- Demetri, G. D., van Oosterom, A. T., Garrett, C. R., Blackstein, M. E., Shah, M. H., Verweij, J., McArthur, G., Judson, I. R., Heinrich, M. C., Morgan, J. A., Desai, J., Fletcher, C. D., George, S., Bello, C. L., Huang, X., Baum, C. M., & Casali, P. G. (2006). Efficacy and safety of sunitinib in patients with advanced gastrointestinal stromal tumour after failure of imatinib: A randomised controlled trial. *The Lancet*, *368*(9544), 1329–1338. https://doi.org/10.1016/S0140-6736(06)69446-4 — PMID 17046465
- (Final OS) Demetri, G. D., Garrett, C. R., Schöffski, P., Shah, M. H., Verweij, J., Leyvraz, S., Hurwitz, H. I., Pousa, A. L., Le Cesne, A., Goldstein, D., Paz-Ares, L., Blay, J.-Y., McArthur, G. A., Xu, Q. C., Huang, X., Harmon, C. S., Tassell, V., Cohen, D. P., & Casali, P. G. (2012). Complete longitudinal analyses of the randomized, placebo-controlled, phase III trial of sunitinib in patients with gastrointestinal stromal tumor following imatinib failure. *Clinical Cancer Research*, *18*(11), 3170–3179. https://doi.org/10.1158/1078-0432.CCR-11-3005 — PMID 22661587

**Design:** Phase 3, double-blind, **2:1**; unblinded early at the interim analysis [A].
**Arms:** Sunitinib **50 mg once daily, 4 weeks on / 2 weeks off** (6-week cycles) vs placebo [A].
**Primary endpoint:** Time to tumour progression (TTP) [A].
**Results:** 312 randomised (207 vs 105) at the interim analysis [A].
- TTP **27.3 weeks (16.0–32.1) vs 6.4 weeks (4.4–10.0); HR 0.33 (0.23–0.47); p < 0.0001** [A; CI from L]
- PFS 24.1 vs 6.0 weeks, HR 0.33 (0.24–0.47) [L]
- ORR 6.8% vs 0 [L]
- Final OS (243 vs 118 randomised; 103 of the placebo patients crossed over): **72.7 vs 64.9 weeks, HR 0.876 (0.679–1.129)** [A CCR; L]. RPSFT crossover-adjusted placebo median OS 39.0 weeks.

**Toxicity:** Fatigue, diarrhoea, skin discolouration and nausea were the most common [A]. US label carries a **boxed warning for hepatotoxicity** [L-Sutent].
**Taiwan:** Sutent 紓癌特; indication GIST after progression on, or intolerance to, imatinib [TFDA].

## 21. GRID: regorafenib third line — [VERIFIED]

**Reference**
- Demetri, G. D., Reichardt, P., Kang, Y.-K., Blay, J.-Y., Rutkowski, P., Gelderblom, H., Hohenberger, P., Leahy, M., von Mehren, M., Joensuu, H., Badalamenti, G., Blackstein, M., Le Cesne, A., Schöffski, P., Maki, R. G., Bauer, S., Nguyen, B. B., Xu, J., Nishida, T., . . . Casali, P. G. (2013). Efficacy and safety of regorafenib for advanced gastrointestinal stromal tumours after failure of imatinib and sunitinib (GRID): An international, multicentre, randomised, placebo-controlled, phase 3 trial. *The Lancet*, *381*(9863), 295–302. https://doi.org/10.1016/S0140-6736(12)61857-1 — PMID 23177515

**Design:** Phase 3, double-blind, **2:1**, 57 hospitals in 17 countries; crossover allowed on progression [A].
**Arms:** Regorafenib **160 mg once daily, 3 weeks on / 1 week off**, vs placebo, both with best supportive care [A].
**Primary endpoint:** PFS by central review [A].
**Results:** 199 randomised (133 vs 66) [A; FT; L].
- PFS **4.8 vs 0.9 months; HR 0.27 (0.19–0.39); p < 0.0001**
- DCR 52.6% vs 9.1%; ORR 4.5% vs 1.5%
- Benefit seen in both KIT exon 11 (HR 0.21) and exon 9 (HR 0.24, n = 15)
- OS interim: HR 0.77 (0.42–1.41), p = 0.199 [FT]
- **OS final: 17.4 vs 17.4 months, HR 0.91 (0.65–1.27)**, after 88% crossover [L]

**Toxicity:** Drug-related grade ≥3 AEs 61.4% [FT].
- Hypertension 23%, **hand–foot skin reaction 20%**, diarrhoea 5%
- Dose modifications 72%
**US label:** **Boxed warning: hepatotoxicity** [L-Stivarga].
**Taiwan:** Stivarga 癌瑞格 40 mg; GIST after imatinib and sunitinib; dose 160 mg on days 1–21 of a 28-day cycle [TFDA].

## 22. INVICTUS: ripretinib fourth line or later — [VERIFIED]

**Reference**
- Blay, J.-Y., Serrano, C., Heinrich, M. C., Zalcberg, J., Bauer, S., Gelderblom, H., Schöffski, P., Jones, R. L., Attia, S., D'Amato, G., Chi, P., Reichardt, P., Meade, J., Shi, K., Ruiz-Soto, R., George, S., & von Mehren, M. (2020). Ripretinib in patients with advanced gastrointestinal stromal tumours (INVICTUS): A double-blind, randomised, placebo-controlled, phase 3 trial. *The Lancet Oncology*, *21*(7), 923–934. https://doi.org/10.1016/S1470-2045(20)30168-6 — PMID 32511981 (erratum PMID 32615117, not checked)

**Design:** Phase 3, double-blind, **2:1**, 29 hospitals in 12 countries; crossover at progression [A].
**Population:** Progression on, or intolerance to, imatinib, sunitinib and regorafenib; ECOG 0–2 [A].
**Arms:** Ripretinib **150 mg once daily** vs placebo [A].
**Primary endpoint:** PFS by BICR (modified RECIST) [A].
**Results:** 129 randomised (85 vs 44) [A; FT; L].
- PFS **6.3 (4.6–6.9) vs 1.0 (0.9–1.7) months; HR 0.15 (0.09–0.25); p < 0.0001**
- ORR 9.4% vs 0%, **P = 0.0504 (not significant)**
- OS 15.1 vs 6.6 months, HR 0.36 (0.21–0.62): **descriptive only, because the testing hierarchy stopped at ORR** [L]

**Toxicity:** Grade 3–4 treatment-related AEs: lipase rise 5%, hypertension 4%, fatigue 2%, hypophosphataemia 2% [A].
**US label warnings** [L-Qinlock]:
- Palmar-plantar erythrodysesthesia
- **New primary cutaneous malignancies** (dermatological exams)
- Hypertension; cardiac dysfunction (check LVEF)
- Wound healing: hold ≥1 week before surgery
- Photosensitivity
- Dose reduction to 100 mg
**Taiwan:** Qinlock 期樂錠 50 mg (衛部藥輸字第028106號); GIST after ≥3 kinase inhibitors including imatinib [TFDA].

## 23. INTRIGUE: ripretinib vs sunitinib second line (negative) — [VERIFIED]

**References**
- Bauer, S., Jones, R. L., Blay, J.-Y., Gelderblom, H., George, S., Schöffski, P., von Mehren, M., Zalcberg, J. R., Kang, Y.-K., Razak, A. A., Trent, J., Attia, S., Le Cesne, A., Su, Y., Meade, J., Wang, T., Sherman, M. L., Ruiz-Soto, R., & Heinrich, M. C. (2022). Ripretinib versus sunitinib in patients with advanced gastrointestinal stromal tumor after treatment with imatinib (INTRIGUE): A randomized, open-label, phase III trial. *Journal of Clinical Oncology*, *40*(34), 3918–3928. https://doi.org/10.1200/JCO.22.00294 — PMID 35947817
- (Final OS) Heinrich, M. C., Blay, J.-Y., Gelderblom, H., George, S., Schöffski, P., von Mehren, M., Zalcberg, J. R., Jones, R. L., Kang, Y.-K., Razak, A. A., Trent, J., Attia, S., Le Cesne, A., Boye, K., Goldstein, D., Sánchez, C., Siontis, B. L., Cox, P., Davis, E., . . . Bauer, S. (2025). Updated overall survival and long-term safety with ripretinib versus sunitinib in patients with GI stromal tumor: Final overall survival analysis from INTRIGUE. *Journal of Clinical Oncology*, *43*(20), 2239–2244. https://doi.org/10.1200/JCO-24-02818 — PMID 40408605
- (ctDNA) Heinrich, M. C., Jones, R. L., George, S., Gelderblom, H., Schöffski, P., von Mehren, M., Zalcberg, J. R., Kang, Y.-K., Razak, A. A., Trent, J., Attia, S., Le Cesne, A., Siontis, B. L., Goldstein, D., Boye, K., Sanchez, C., Steeghs, N., Rutkowski, P., Druta, M., . . . Bauer, S. (2024). Ripretinib versus sunitinib in gastrointestinal stromal tumor: ctDNA biomarker analysis of the phase 3 INTRIGUE trial. *Nature Medicine*, *30*(2), 498–506. https://doi.org/10.1038/s41591-023-02734-5 — PMID 38182785

**Design:** Phase 3, open-label, 1:1 [A].
**Arms:** Ripretinib 150 mg daily vs sunitinib 50 mg daily (4 weeks on / 2 weeks off) [A].
**Primary endpoint:** PFS by independent review, in the KIT exon 11 ITT population and then all ITT [A].
**Results:** 453 randomised (226 vs 227) [A; FT].
- KIT exon 11: PFS 8.3 vs 7.0 months, **HR 0.88 (0.66–1.16), P = .36**
- All patients: 8.0 vs 8.3 months, HR 1.05 (0.82–1.33)
- ORR in exon 11: 23.9% vs 14.6% (nominal P = .03)
- **KIT exon 9 (n = 60): PFS favoured sunitinib, 13.8 vs 5.5 months, HR 2.85 (1.48–5.48)** [FT]
- Final OS: 35.5 vs 31.5 months, HR 0.86 (0.65–1.13); exon 11 HR 0.98 (0.71–1.34) [FT JCO 2025]

**Safety:** Grade 3–4 TEAEs 41.3% vs 65.6% [A; FT].
- Ripretinib: alopecia 64.1%, fatigue 37.7%, myalgia 36.3%
- Sunitinib: PPES 51.1%, diarrhoea 48.0%, hypertension 47.1%
**ctDNA (exploratory)** [A]:
- KIT exon 11 + 13/14 only: PFS favoured **sunitinib** (15.0 vs 4.0 months)
- KIT exon 11 + 17/18 only: PFS favoured **ripretinib** (14.2 vs 1.5 months)
- This led to the phase 3 **INSIGHT** trial (NCT05734105), which is ongoing [A protocol paper PMID 39229786]

## 24. NAVIGATOR: avapritinib for PDGFRA D842V GIST — [VERIFIED]

**References**
- Heinrich, M. C., Jones, R. L., von Mehren, M., Schöffski, P., Serrano, C., Kang, Y.-K., Cassier, P. A., Mir, O., Eskens, F., Tap, W. D., Rutkowski, P., Chawla, S. P., Trent, J., Tugnait, M., Evans, E. K., Lauz, T., Zhou, T., Roche, M., Wolf, B. B., . . . George, S. (2020). Avapritinib in advanced PDGFRA D842V-mutant gastrointestinal stromal tumour (NAVIGATOR): A multicentre, open-label, phase 1 trial. *The Lancet Oncology*, *21*(7), 935–946. https://doi.org/10.1016/S1470-2045(20)30269-2 — PMID 32615108 (erratum PMID 32888469, not checked)
- (Long-term) Jones, R. L., Serrano, C., von Mehren, M., George, S., Heinrich, M. C., Kang, Y.-K., Schöffski, P., Cassier, P. A., Mir, O., Chawla, S. P., Eskens, F. A. L. M., Rutkowski, P., Tap, W. D., Zhou, T., Roche, M., & Bauer, S. (2021). Avapritinib in unresectable or metastatic PDGFRA D842V-mutant gastrointestinal stromal tumours: Long-term efficacy and safety data from the NAVIGATOR phase I trial. *European Journal of Cancer*, *145*, 132–142. https://doi.org/10.1016/j.ejca.2020.12.008 — PMID 33465704

**Design:** Phase 1, dose escalation and expansion [A]. MTD 400 mg; **recommended phase 2 dose 300 mg once daily** [A].
**Primary endpoints:** Safety, MTD and recommended dose; ORR in expansion [A].
**Results (PDGFRA D842V, n = 56)** [A; FT]:
- ORR **88% (95% CI 76–95)**; CR 9%, PR 79%
- Long-term (median follow-up 27.5 months): ORR 91%, clinical benefit rate 98%, median DOR 27.6 months, **median PFS 34.0 months**, OS not reached
**Toxicity** [A; FT]:
- Treatment-related grade 3–4 AEs 57% (anaemia 17%)
- Nausea 68%, diarrhoea 66%
- **Cognitive effects 57%**; intracranial bleeding 5% (3/56)
- Discontinuation for AEs 34%, mainly nervous system and psychiatric

**US label** [L-Ayvakit, effective 2026-08-05]:
- GIST with **PDGFRA exon 18 mutation including D842V**; dose 300 mg once daily on an empty stomach
- Exon 18 ORR 84% (n = 43); D842V ORR 89% (n = 38)
- **Intracranial haemorrhage: stop permanently at any grade** (2.9% of 749 GIST/AdvSM patients)
- Cognitive effects; photosensitivity
**Taiwan:** AYVAKIT 泰時維 100/200/300 mg (衛部藥輸字第028029–028031號); indication **PDGFRA D842V** unresectable/metastatic GIST [TFDA].
**NCCN Patients GIST 2026** [PG]: avapritinib is preferred for PDGFRA exon 18 mutations that do not respond to imatinib, including D842V.

## 25. VOYAGER: avapritinib vs regorafenib third line or later (negative) — [VERIFIED]

**Reference**
- Kang, Y.-K., George, S., Jones, R. L., Rutkowski, P., Shen, L., Mir, O., Patel, S., Zhou, Y., von Mehren, M., Hohenberger, P., Villalobos, V., Brahmi, M., Tap, W. D., Trent, J., Pantaleo, M. A., Schöffski, P., He, K., Hew, P., Newberry, K., . . . Bauer, S. (2021). Avapritinib versus regorafenib in locally advanced unresectable or metastatic GI stromal tumor: A randomized, open-label phase III study. *Journal of Clinical Oncology*, *39*(28), 3128–3139. https://doi.org/10.1200/JCO.21.00217 — PMID 34343033

**Arms:** Avapritinib 300 mg daily vs regorafenib 160 mg (3 weeks on / 1 week off); crossover from regorafenib allowed [A].
**Results:** 476 randomised [A].
- PFS 4.2 vs 5.6 months, **HR 1.25 (0.99–1.57), P = .055 (not met)**
- ORR 17.1% vs 7.2%; DCR 41.7% vs 46.2%
- Treatment-related AEs: any grade 92.5% vs 96.2%; grade ≥3 55.2% vs 57.7%
**Lesson:** Avapritinib is for **PDGFRA exon 18/D842V**, not for unselected late-line KIT-mutant GIST [A].

---

# F. Taiwan licence snapshot (TFDA dataset, latest change date 2026-10-22) — [VERIFIED]

| Drug | Taiwan product (licence no.) | Status | Taiwan indication relevant here |
|---|---|---|---|
| Trabectedin | 友待 Yondelis 1 mg (衛部藥輸字第027370號) | Active | LPS/LMS after an anthracycline-containing regimen |
| Eribulin | 賀樂維 Halaven (衛部藥輸字第026140號) + generics | Active | Liposarcoma (and breast cancer) |
| Pazopanib | 福退癌 Votrient (衛署藥輸字第025433號) + generics | Active | STS after chemo; not adipocytic STS or GIST |
| Olaratumab | 樂除瘤 Lartruvo (衛部菌疫輸字第001075號) | **Cancelled 2019-09-04** | (was: with doxorubicin, 1L STS) |
| Pexidartinib | 圖拉留 TURALIO 200 mg (衛部藥輸字第028293號) | **Cancelled 2026-02-03** | (was: TGCT) |
| Tazemetostat, nirogacestat, vimseltinib, nab-sirolimus (Fyarro), afamitresgene, lete-cel | — | **No licence found** | — |
| Imatinib | 基利克 Glivec (衛署藥輸字第024027號) | Active | Unresectable/metastatic GIST; adjuvant after complete resection of KIT⁺ GIST |
| Sunitinib | 紓癌特 Sutent | Active | GIST after progression on, or intolerance to, imatinib |
| Regorafenib | 癌瑞格 Stivarga (衛部藥輸字第026168號) | Active | GIST after imatinib and sunitinib |
| Ripretinib | 期樂錠 Qinlock 50 mg (衛部藥輸字第028106號) | Active | GIST after ≥3 kinase inhibitors including imatinib |
| Avapritinib | 泰時維 AYVAKIT (衛部藥輸字第028029/028030/028031號) | Active | PDGFRA D842V GIST |

NHI (健保) reimbursement conditions: **[UNVERIFIED]** (nhi.gov.tw unreachable; no MOHW release found).

# G. Guideline context checked

- NCCN professional versions on the category page: **STS v5.2026, GIST v1.2026** (PDFs not opened).
- NCCN Guidelines for Patients, STS 2025 [PG]:
  - Preferred next-line options: eribulin ("especially for liposarcoma"), gemcitabine + docetaxel, pazopanib, trabectedin ("especially for liposarcoma and leiomyosarcoma")
  - Histology-specific preferred options: albumin-bound sirolimus for PEComa; pexidartinib or vimseltinib for TGCT
  - The preferred first-line list shows anthracycline-based regimens. Doxorubicin + trabectedin was not in the "preferred" table of the patient version (other categories not checked)
- NCCN Patients, GIST 2026 [PG]:
  - Imatinib is preferred first line for imatinib-sensitive mutations; avapritinib for PDGFRA exon 18/D842V
  - Sequence: imatinib → sunitinib → regorafenib → ripretinib
  - Imatinib dose increase is an option, "may work best" for KIT exon 9
  - Adjuvant imatinib "at least 3 years" for high risk
- ESMO–EURACAN–GENTURIS full texts were not reachable in this project (HTTP 403 in the sarcoma 1 notes). Not used.

# H. Label and dataset sources (accessed 2026-10-29)

Each item gives the labeller, the product, the label effective date and the DailyMed set ID. All were read through openFDA (https://api.fda.gov/drug/label.json).

- Janssen Products, LP. *YONDELIS (trabectedin)*. Effective 2026-01-06. Set ID 472bd78e-be17-4b9d-90f4-9482c3aec9ff.
- BluePoint Laboratories. *Eribulin mesylate injection* (generic; reproduces the Halaven efficacy text). Effective 2026-03-25. Set ID 1a1a9cff-d5da-4232-b98f-26f55208dfc4.
- Novartis Pharmaceuticals Corporation. *VOTRIENT (pazopanib)*. Effective 2025-12-16. Set ID eeaaaf38-fb86-4d9f-a19d-0f61daac2fd7.
- Epizyme, Inc. *TAZVERIK (tazemetostat)*. Effective 2026-04-29. Set ID 7db07b5f-4e22-467c-9c0a-f830b08dbb1d.
- USWM CT, LLC. *TECELRA (afamitresgene autoleucel)*. Effective 2026-07-15. Set ID ab24631f-3364-46e1-8074-7244863bcbab.
- SpringWorks Therapeutics, Inc. *OGSIVEO (nirogacestat)*. Effective 2026-09-01. Set ID f172e6ff-3190-41b0-b95a-58a7ef9e9e1e.
- Daiichi Sankyo Inc. *TURALIO (pexidartinib)*. Effective 2025-01-16. Set ID 7b0ec4bf-b2ac-49ee-96af-7740ad3f2e16.
- Deciphera Pharmaceuticals, LLC. *ROMVIMZA (vimseltinib)*. Effective 2026-06-26. Set ID f73c7a62-9601-4df0-810f-100f515d79ea.
- *FYARRO (sirolimus protein-bound particles)*, NDC 80803 (labeller field empty in openFDA). Effective 2026-05-19. Set ID 0f9bb784-53e2-46f9-a65d-1c6c2a230eaf.
- Novartis Pharmaceuticals Corporation. *Gleevec (imatinib)*. Effective 2026-07-13. Set ID 211ef2da-2868-4a77-8055-1cb2cd78e24b.
- Pfizer Laboratories Div Pfizer Inc. *SUTENT (sunitinib)*. Effective 2026-02-20. Set ID 43a4d7f8-48ae-4a63-9108-2fa8e3ea9d9c.
- Bayer HealthCare Pharmaceuticals Inc. *Stivarga (regorafenib)*. Effective 2026-02-09. Set ID 824f19c9-0546-4a8a-8d8f-c4055c04f7c7.
- Deciphera Pharmaceuticals, LLC. *QINLOCK (ripretinib)*. Effective 2025-05-12. Set ID 9f18e462-03dd-4296-a02a-a0577e3ee78d.
- *AYVAKIT (avapritinib)*, NDC 72064 (labeller field empty in openFDA). Effective 2026-08-05. Set ID 645c887c-8cd4-4623-8da9-ac223d71a8b9.
- Not found in openFDA: lete-cel, olaratumab (withdrawn).

Other sources:
- U.S. Food and Drug Administration. (2026). *Approved cellular and gene therapy products* (content current as of 2026-09-17). https://www.fda.gov/vaccines-blood-biologics/cellular-gene-therapy-products/approved-cellular-and-gene-therapy-products
- Taiwan Food and Drug Administration. (2026). *全部藥品許可證資料集* [Open data, InfoId=36]. https://data.fda.gov.tw/opendata/exportDataList.do?method=ExportData&InfoId=36&logType=2
- [NEWS] Targeted Oncology. (2025, January 13). FDA grants lete-cel BTD in myxoid/round cell liposarcoma. https://www.targetedonc.com/view/fda-grants-lete-cel-btd-in-myxoid-round-cell-liposarcoma
- [NEWS] pharmaphorum. Eli Lilly withdraws cancer drug Lartruvo from all markets. https://pharmaphorum.com/news/eli-lilly-withdraws-cancer-drug-lartruvo-from-all-markets/
- NCCN Guidelines for Patients: Soft Tissue Sarcoma (2025) and Gastrointestinal Stromal Tumors (2026), PDFs from nccn.org (copies in scratchpad `sarc_dl/`).

---

## Critic additions

Completeness critique of all four sarcoma notes files (sarcoma_1 to sarcoma_4), done 2026-10-29 against the 13-section chapter plan (exemplar: handbook/01-lung-cancer.md). This section covers the whole chapter, not only this file. Its sources follow the same rules: [A] = PubMed abstract (NCBI E-utilities efetch); [FT] = PMC full text; [L] = openFDA label (effective date given); [TFDA] = TFDA licence file `36_2.csv` dated 2026-10-27; [GL-UK] = UK guideline full text in PMC. Tags are [VERIFIED], [PARTIAL] and [UNVERIFIED].

### CA-0. Corrections and consistency fixes (read first)

1. **NCCN STS version is wrong in sarcoma_4 §F.** That file says "Soft Tissue Sarcoma **1.2026**". When I re-read https://www.nccn.org/guidelines/category_1 on 2026-10-29, it showed **Soft Tissue Sarcoma Version 5.2026** [VERIFIED].
   - The other versions on the page match the notes: GIST 1.2026; Bone Cancer 1.2027; Pediatric Bone Sarcoma 1.2027; Pediatric STS 1.2026; Kaposi Sarcoma 1.2027.
   - Category 3/4 pages also match: Hematopoietic Growth Factors 1.2027; Antiemesis 2.2026; Survivorship 3.2026; CAR T-Cell and Lymphocyte Engager-Related Toxicities 2.2026; Cancer-Related Infections 1.2026; Cancer-Associated VTE 1.2026; AYA Oncology 2.2027 [VERIFIED].
   - Use **v5.2026** in the chapter header.
2. **Atezolizumab in ASPS: the paper and the US label give different response rates.**
   - NEJM paper: ORR **37% (19/52; 1 CR, 18 PR)**, investigator-assessed [A].
   - US label (study ML39345): ORR **24% (95% CI 13–39; 12/49 PR, 0 CR)** by independent review committee [L-Tecentriq 2026-05-20].
   - State which source you quote. The exam-safe figure is the label's 24% (IRC).
3. **Huvos grades: [UNVERIFIED] in sarcoma_2 §5 is now [PARTIAL].**
   - Grade I: no chemotherapy effect. Grade II: partial response, >50% necrosis. Grade III: >90% necrosis with viable tumour present. Grade IV: no viable tumour.
   - Good responder = >90% necrosis (Rosen criterion).
   - Source: Bispo Júnior & Camargo 2011, quoting Huvos 1977 [FT; secondary citation; Huvos 1977 original not opened].
   - Rosen 1982 abstract confirms the ">90% tumor necrosis" response criterion [A].
4. **Pathological fracture management: one ward rule is missing from the notes.** For an impending or completed pathological fracture from a suspected primary bone tumour, use external splintage or immobilisation and pain control until imaging and biopsy are done. **"Internal fixation is contraindicated"** [GL-UK bone 2025; VERIFIED]. Teach it explicitly: an intramedullary nail through an undiagnosed sarcoma contaminates the whole bone.
5. **The notes had no adjuvant-chemotherapy evidence for localised STS.** The largest RCT (EORTC 62931) was **negative**. Added in CA-3.
6. **Not covered anywhere in the four files until now:**
   - immunotherapy in sarcoma
   - desmoid sorafenib
   - denosumab for giant cell tumour of bone (GCTB)
   - angiosarcoma paclitaxel (relevant because Taiwan has more angiosarcoma; see sarcoma_1 §1.4)
   - imatinib interruption trials
   - follow-up schedules
   - referral criteria
   - Li-Fraumeni surveillance
   - sarcoma-specific emergencies (pathological fracture, pneumothorax, Doege–Potter hypoglycaemia, hypercalcaemia after stopping denosumab)

   All are added below.

### CA-1. Re-check of high-stakes numbers already in the notes (against current primary labels)

| # | Number in notes (file) | Primary source re-read 2026-10-29 | Result |
|---|---|---|---|
| 1 | HD-MTX osteosarcoma **12 g/m² (max 20 g/dose) IV over 4 h** (s2 §1, §17) | Methotrexate Injection label, Hospira, effective 2025-06-10, set 0d63ba29: "typically 12 g/m² (maximum 20 g/dose) as an intravenous infusion over 4 hours" | **Confirmed** [VERIFIED] |
| 2 | Leucovorin nomogram: 15 mg q6h × 10 from 24 h; normal ≈10/1/<0.2 µM at 24/48/72 h; delayed early = **≥50 µM at 24 h or ≥5 µM at 48 h or ≥100% creatinine rise** → 150 mg IV q3h until <1 µM, then 15 mg IV q3h until <0.05 µM (s2 §18a) | Leucovorin Calcium Injection, Sagent, effective 2026-06-16, set c0cbcbf6, Table 2 | **Confirmed word for word** [VERIFIED] |
| 3 | Glucarpidase **50 U/kg IV over 5 min**; leucovorin ≥2 h before or after; same leucovorin dose for 48 h; continue until MTX below threshold ≥3 days (s2 §19) | VORAXAZE, BTG, effective 2024-11-27, set acaef5a6 | **Confirmed** [VERIFIED] |
| 4 | Mesna IV **20% w/w at 0, 4, 8 h (240 mg/m² each for ifosfamide 1.2 g/m²; total 60%)**; IV+PO = 240 mg/m² IV at 0 h + **480 mg/m² PO at 2 and 6 h** (s4 §6b) | MESNEX, effective 2025-12-10, set 1dd69e84 | **Confirmed** [VERIFIED] |
| 5 | Trabectedin **1.5 mg/m² 24-h IV q3w via central line; dexamethasone 20 mg IV 30 min before**; moderate hepatic impairment 0.9 mg/m²; CPK delay >2.5 × ULN, reduce >5 × ULN (s3 §8, s4 §9) | YONDELIS, Janssen, effective 2026-01-06, set 472bd78e | **Confirmed** [VERIFIED] |
| 6 | PEDMARK by actual weight **<5 kg 10 g/m²; 5–10 kg 15 g/m²; >10 kg 20 g/m²**, over 15 min, 6 h after the end of cisplatin, ≥10 h before the next cisplatin; only after 1–6-h cisplatin infusions (s2 §23) | PEDMARK, Fennec, effective 2025-10-27, set f98c7076 | **Confirmed** [VERIFIED] |
| 7 | NCCN STS version (s4 §F "1.2026") | nccn.org category_1 | **Wrong; current is 5.2026** (CA-0 item 1) |

No dose corrections were needed. All six re-checked doses and thresholds match the current US labels.

### CA-2. Screening, early detection and referral (chapter section 2)

**No population screening exists for sarcoma or GIST.**
- Taiwan's government-subsidised programmes do not include sarcoma. MOHW (2025-01-10) describes LDCT lung screening as **「第五癌篩檢」**, the fifth national cancer screening [VERIFIED; https://mohw.gov.tw/cp-16-81184-1.html].
- The release does not list the other four programmes. "Sarcoma is not among them" is an inference [PARTIAL].

**Referral triggers for a soft-tissue lump** (UK guidelines 2025, quoting NICE 2015) [GL-UK STS; VERIFIED]:
- Consider an urgent direct-access **ultrasound within 2 weeks** for an adult with an unexplained lump that is **increasing in size**.
- Use a suspected-cancer referral (appointment within 2 weeks) if ultrasound suggests sarcoma, or if it is uncertain and concern persists.
- Any retroperitoneal or intra-abdominal mass that looks like sarcoma on CT/MRI goes to a specialist sarcoma MDT **before biopsy or surgery**.
- The older NICE criteria (size **>5 cm**, increasing size, deep site, pain) "failed to discriminate" from lipomas and cysts. The UK has moved to ultrasound triage.
- Median size at diagnosis is still **>9 cm**.
- This upgrades the [PARTIAL] ">5 cm / deep / growing" point in sarcoma_1 §4.3 to [VERIFIED as UK/NICE history]. ESMO wording was still not opened.

**Red flags for a primary bone tumour** (UK bone guideline 2025) [GL-UK bone; VERIFIED]:
- Most common symptoms: pain and/or a lump; some patients present with a pathological fracture.
- **Night pain is a "red flag"**. Spinal tumours may present with **spinal cord compression**.
- Average symptom duration is 3 months. **A history of recent injury does not exclude a primary bone tumour.**
- Get an **urgent X-ray**. Investigate further if it shows bone destruction, new bone formation, periosteal swelling or soft-tissue swelling. **A normal X-ray does not exclude** a primary bone tumour; persistent pain needs urgent MRI or referral.
- **Patients under 40 with a suspected primary bone tumour should be referred urgently to a bone sarcoma centre**, before biopsy.
- Pre-referral bloods: FBC, ESR, biochemistry with ALP.

**Li-Fraumeni (germline TP53) surveillance ("Toronto protocol")**
- Villani 2016, prospective observational study, n = 89 carriers [A] [VERIFIED]:
  - Protocol: physical exam, biochemistry, **whole-body MRI**, brain MRI, breast MRI, mammography, abdominal/pelvic ultrasound and colonoscopy.
  - 40 asymptomatic tumours were found in 19 of 59 surveilled patients.
  - **5-year OS 88.8% (surveillance) vs 59.6% (no surveillance), p = 0.0132.**
- Ballinger 2017 meta-analysis (578 carriers): baseline WB-MRI detected new localised cancers in **7% (95% CI 5–9%)** [A] [VERIFIED].
- UK bone guideline: patients with osteosarcoma in the setting of LFS should follow appropriate surveillance programmes [GL-UK bone].

### CA-3. Localised STS: adjuvant/neoadjuvant chemotherapy and RT doses (chapter section 5)

**EORTC 62931 (Woll 2012)** [A] [VERIFIED]
- Design: resected grade II–III STS at any site; age 16–70; **doxorubicin 75 mg/m² + ifosfamide 5 g/m² + lenograstim q3w × 5** vs no chemotherapy; n = 351.
- OS **HR 0.94 (0.68–1.31), p = 0.72**; RFS HR 0.91 (0.67–1.22).
- 5-year OS 66.5% vs 67.8%.
- 80% completed 5 cycles; grade 3–4 fever/infection 10%; no toxic deaths.
- **No benefit.**

**Meta-analysis (Pervaiz 2008; 18 RCTs, n = 1,953)** [A] [VERIFIED]
- Local recurrence OR 0.73 (0.56–0.94); distant/overall recurrence OR 0.67 (0.56–0.82).
- Survival: **doxorubicin alone OR 0.84 (0.68–1.03), not significant**; **doxorubicin + ifosfamide OR 0.56 (0.36–0.85)**.
- Conclusion: "marginal efficacy".

**UK guideline 2025 position** [GL-UK STS; VERIFIED]
- "Neoadjuvant or adjuvant chemotherapy is **not routinely recommended**". It should be considered where local control is likely to be compromised or prognosis is poor, especially in chemo-sensitive subtypes.
- EORTC 62931 was criticised for a low ifosfamide dose and inclusion of intermediate-grade tumours.
- Sarculator re-analysis: patients with predicted **10-year OS <51%** benefited (HR 0.46).
- ISG-STS 1001 high-risk subgroup (Sarculator predicted 5-year OS <60%): 3 cycles of neoadjuvant AI gave 5-year OS 0.66 vs 0.55 for histotype-tailored therapy.
- **No RCT has tested neoadjuvant chemotherapy against immediate surgery.**

**RT dose** [GL-UK STS; VERIFIED]
- Post-op **60–66 Gy** in 1.8–2 Gy fractions; pre-op **50–50.4 Gy**.
- Pre-op RT: better long-term function and equivalent control, but more acute wound complications. This matches O'Sullivan and Davis (§1–2 above).
- Hypofractionated pre-op **25–30 Gy in 5 fractions** "appear to achieve equivalent local control" (non-randomised data; flagged as emerging).

**Follow-up after primary STS** [GL-UK STS, citing ESMO; VERIFIED]
- **Intermediate/high grade:** every **3–4 months for 2–3 years**, then twice yearly to year 5, then annually for a total of **8–10 years**.
- **Low grade:** every 6 months for 5 years, then annually.
- Visit content: history, examination of the local site (MRI/CT only if suspicious or the site is hard to examine) and **chest X-ray**, with CT chest for abnormalities.
- Patient-initiated follow-up (PIFU) is acceptable for selected low-grade tumours.
- Supporting RCT, **Puri 2014** (n = 500, extremity sarcoma) [A] [VERIFIED]:
  - 3-year OS **67% with chest X-ray vs 66% with CT** (HR 0.9). Non-inferiority of 6-monthly vs 3-monthly visits was **not** shown (OS 64% vs 69%; HR 1.2; upper 90% CI 1.47).
  - **"Almost 90% of local recurrences were identified by patients themselves."** This supports NP teaching on self-examination.

### CA-4. Advanced STS: immunotherapy and angiosarcoma (chapter section 5)

| Trial | Design / dose | Key result | Tag |
|---|---|---|---|
| **SARC028** (Tawbi 2017) | Phase 2, 2 cohorts; **pembrolizumab 200 mg IV q3w**; STS n = 40 evaluable, bone n = 40 | STS ORR **18%**: **UPS 4/10 (40%)**, liposarcoma 2/10 (20%; dedifferentiated), synovial 1/10, **LMS 0/10**. Bone ORR 5%: osteosarcoma 1/22, chondrosarcoma 1/5, **Ewing 0/13**. **Primary endpoint not met in either cohort.** Immune-related SAEs included adrenal insufficiency, pneumonitis and nephritis | [A] VERIFIED |
| **Alliance A091401** (D'Angelo 2018) | Non-comparative randomised phase 2; nivolumab 3 mg/kg q2w vs nivolumab 3 mg/kg + ipilimumab 1 mg/kg q3w × 4, then nivolumab | Confirmed ORR **5% (2/38) nivolumab alone vs 16% (6/38) combination**. Combination met its endpoint; nivolumab alone "does not warrant further study" | [A] VERIFIED |
| **Atezolizumab in ASPS** (Chen 2023, NEJM; NCT03141684) | Single-arm phase 2; **1200 mg IV q3w (adult); 15 mg/kg, max 1200 mg (<18 y)** | ORR **37% (19/52)**; median time to response 3.6 months; **median DOR 24.7 months**; median PFS 20.8 months; no treatment-related grade 4–5 AEs. JCO 2026 update exists (PMID 41999612), not read | [A] VERIFIED |
| Atezolizumab label | US: adults **840 mg q2w, 1200 mg q3w or 1680 mg q4w**; paediatric ≥2 y **15 mg/kg (max 1200 mg) q3w**; IRC ORR **24%** (n = 49) | — | [L-Tecentriq 2026-05-20, set 6fa682c9] VERIFIED |
| **Atezolizumab in Taiwan** | 癌自禦 衛部菌疫輸字第001050號 (IV, issued 2017-07-17) and 第001258號 (SC 癌自禦皮下注射劑, 2024-05-29) list 「肺泡狀軟組織肉瘤：單獨使用，適用於治療**2歲以上**無法切除或轉移性肺泡狀軟組織肉瘤」 | **ASPS is an on-label indication in Taiwan** | [TFDA] VERIFIED |
| Pembrolizumab / nivolumab / ipilimumab in Taiwan | No sarcoma wording found in any active TFDA indication | Off-label for sarcoma | [TFDA] VERIFIED |
| **ANGIOTAX** (Penel 2008) | **Weekly paclitaxel 80 mg/m² IV over 60 min, D1, 8, 15 q4w**; n = 30, unresectable angiosarcoma | Non-progression at 2 months **74%**, at 4 months 45%; median TTP 4 months; median OS 8 months; 3 PR in breast angiosarcoma led to curative surgery; 1 toxic death (thrombocytopenia) | [A] VERIFIED |

Teaching points:
- Immunotherapy in sarcoma is **histotype-specific**. It works in ASPS, UPS and dedifferentiated liposarcoma, but **not LMS or Ewing** in SARC028.
- ASPS is the one sarcoma with an on-label checkpoint inhibitor in Taiwan.
- NCCN-recommended immunotherapy regimens and categories were not read (login) [UNVERIFIED].

### CA-5. Desmoid tumour: sorafenib (complements DeFi, §14)

**Gounder 2018 (NEJM)** [A] [VERIFIED]
- Design: phase 3, double-blind; **sorafenib 400 mg once daily** vs placebo; n = 87; crossover allowed.
- 2-year PFS **81% vs 36%; HR 0.13 (0.05–0.31)**.
- ORR 33% vs **20% on placebo**. The placebo responses are themselves a teaching point: desmoids can regress spontaneously.
- AEs (grade 1–2): rash 73%, fatigue 67%, hypertension 55%, diarrhoea 51%.

**Regulatory**
- **Taiwan:** sorafenib licences (e.g., 蕾莎瓦 衛署藥輸字第024727號) cover HCC, RCC and others; **no desmoid indication**, so use for desmoid is off-label [TFDA; VERIFIED].
- **UK guideline:** "Initial standard treatment for fibromatosis is clinical and radiologic surveillance"; systemic therapy only for symptomatic progression [GL-UK STS; VERIFIED].

### CA-6. Giant cell tumour of bone: denosumab (chapter sections 5–6)

**Chawla 2019 (Lancet Oncol; phase 2, n = 532, age ≥12 and ≥45 kg)** [A] [VERIFIED]
- Dose: **120 mg SC every 4 weeks with loading doses on days 8 and 15.**
- Unsalvageable cohort: progression or recurrence in 11%.
- Salvageable cohort: **92% had no surgery at 6 months**.
- Safety:
  - grade ≥3 hypophosphataemia 5%
  - **osteonecrosis of the jaw 5% (adjudicated)**
  - atypical femur fracture 1%
  - **hypercalcaemia 1%, occurring after stopping denosumab**
  - sarcomatous transformation 1%

**US label** [L-Xgeva, Amgen, effective 2026-06-23, set 628f0998] [VERIFIED]
- 120 mg q4w plus 120 mg on days 8 and 15 of month 1.
- Give calcium and vitamin D as needed to treat or prevent hypocalcaemia.

**Taiwan** [TFDA] [VERIFIED]
- Xgeva 癌骨瓦 衛署菌疫輸字第000924號 includes 骨巨細胞瘤 「無法以手術切除或手術切除可能導致重症的成人和骨骼發育成熟之青少年」.
- Denosumab 120-mg biosimilars licensed 2025–2026 carry the same GCTB indication: 衛部菌疫輸字第001288、001296、001301、001313、001324、001331號.

**UK guideline** [GL-UK bone] [VERIFIED]
- Denosumab is for unresectable or unacceptably morbid surgery, or metastatic disease.
- **Curettage after denosumab carries a higher local-recurrence risk**, so complete resection is preferred after denosumab.
- Main toxicities: hypocalcaemia, ONJ, atypical fractures.

**NP actions**
- Dental review before the first dose, and calcium/vitamin D. The dental-review point is an ONJ precaution consistent with the label warnings; the exact label wording was not extracted [PARTIAL].
- Check calcium after stopping denosumab (rebound hypercalcaemia, Chawla 2019).

### CA-7. Bone sarcoma practice points from the UK 2025 guideline (complements sarcoma_2) [GL-UK bone; VERIFIED unless marked]

**Osteosarcoma**
- MAP is recommended for resectable osteosarcoma **up to 40 years**. Over 40, or if MTX is not tolerated: **doxorubicin + cisplatin (AP)**.
- Mifamurtide is "approved in the UK for osteosarcoma patients <30 years with localised, completely resected disease". The Taiwan licence was cancelled in 2023 (sarcoma_2 flag 1).
- Neoadjuvant chemotherapy has practical advantages, but its "survival benefit over postoperative chemotherapy alone is unproven".
- Combined treatment raises survival from **10–20% (surgery alone) to ~60%**.
- With **>90% necrosis**, a closer surgical margin "can be considered safe".
- For older patients, surgery first is reasonable.
- Adverse factors: metastases, axial or proximal site, large volume, high ALP or LDH, older age, high BMI, poor histological response, **pathological fracture**.

**Ewing sarcoma**
- **Interval-compressed VDC/IE × 14 is the preferred first-line regimen** for all fit patients.
- BuMel is for poor response after VIDE or volume >200 mL; its value after VDC/IE "is not defined".
- **Do not give BuMel if the RT fields include gut, spinal cord, brain or large lung volumes** (fatal toxicity reported).
- About **26% are metastatic at presentation** (10% lung, 10% bone/marrow, 6% combinations).
- RT doses [PDQ Ewing, updated 2024-11-27; PARTIAL, secondary]:
  - definitive RT ≈ **55.8 Gy** (45 Gy + 10.8 Gy boost)
  - post-op microscopic residual **50.4 Gy** (INT-0091: 45 + 5.4 Gy)
  - gross residual 45 + 10.8 Gy
  - no RT after complete resection with no microscopic residual (INT-0091)
- Whole-lung irradiation dose: **[UNVERIFIED]**.

**Chondrosarcoma**
- Atypical cartilaginous tumours of the extremity can be **observed**. If progressive or symptomatic, curettage ± adjuvants (high-speed burr, cryotherapy).
- Higher-grade, clear-cell, and **all pelvic/axial chondrosarcomas need wide margins**. In the pelvis a 2-mm margin is associated with lower local recurrence.
- Skull-base chondrosarcoma: surgery + high-dose RT gives 80–90% local control.
- Ollier/Maffucci and multiple osteochondromas: counsel about secondary chondrosarcoma and follow up.
- This fills the [UNVERIFIED] surgical-margin item in sarcoma_2 §13.

**Bone sarcoma follow-up**
- High grade: every **2–4 months for years 1–3**, every 6 months for years 4–5, then annually.
- Low grade: every 4–6 months for 2 years, then annually.
- Standard visit: **chest X-ray + X-ray of the local site + clinical review**.
- **Chordoma:** local MRI at 6 months, 1 year, then annually to 10 years.
- There is "no universally accepted stopping point". Late metastases and failed reconstructions occur after more than 10 years.
- Secondary AML can appear 2–5 years after chemotherapy.

### CA-8. GIST additions (chapter sections 5 and 8)

**Do not interrupt imatinib in advanced GIST** (BFR14, French Sarcoma Group) [A] [VERIFIED]
- Stop after 1 year (Blay 2007): progression in **26/32 interrupted vs 8/26 continued** (P < .0001). 24/26 responded when imatinib was restarted. No OS difference.
- Stop after 3 years (Le Cesne 2010): 2-year PFS **80% continued vs 16% interrupted** (p < 0.0001).
- Conclusion: discontinuation is not recommended outside trials unless toxicity is significant.
- This is a core NP adherence teaching point; patients often ask for a "drug holiday".

**Neoadjuvant imatinib** (Asian consensus 2025) [FT; VERIFIED]
- Consider for large (e.g., >10 cm) or hard-to-resect GIST.
- **Surgery generally after 6–12 months** of treatment, to balance shrinkage against secondary resistance.
- Genotype first, to exclude imatinib-insensitive tumours (PDGFRA D842V, wild-type).
- **Post-neoadjuvant specimens cannot be risk-classified.**

**Unified definition of tumour rupture** (Asian consensus 2025, Fig. 3) [FT; VERIFIED]
- Tumour fracture, spillage of tumour contents, blood-stained ascites, perforation at the tumour site, adjacent organ infiltration, **piecemeal resection, and incisional biopsy**.
- Ruptured GIST = very high risk; often prolonged or lifelong adjuvant imatinib.

**Follow-up after resection** (Asian consensus 2025) [FT; VERIFIED]
- Surveillance is "weakly recommended" and should be individualised.
- Intermediate/high risk: more intensive **contrast-enhanced CT** in the first years. PET is not established.
- Exact intervals are **[UNVERIFIED]**; the consensus cites Joensuu 2015 but gives no schedule in the text read.

### CA-9. Oncologic emergencies specific to sarcoma (chapter section 9; new)

| Emergency | Sarcoma context and numbers | Immediate action | Source / tag |
|---|---|---|---|
| **Pathological fracture** (bone sarcoma) | Occurs in **5–10%** of osteosarcoma; pooled 12% (885/7,604). Worse 3-year OS (**RR 1.53**), 5-year OS (RR 1.27) and metastasis (RR 1.33); local recurrence not significantly higher. Limb salvage not associated with more local recurrence (RR 1.58, 0.88–2.85) | Splint/immobilise, analgesia, **no internal fixation before diagnosis**, refer to bone sarcoma centre; fractures often heal during neoadjuvant chemotherapy | Gonzalez 2023 [A] VERIFIED; GL-UK bone VERIFIED |
| **Spinal cord compression** | Spinal primary bone tumours "may present with spinal cord compression"; Ewing, chordoma and metastatic sarcoma | Standard MSCC pathway (see shared emergencies chapter); MDT before surgery, because biopsy and tract matter | GL-UK bone VERIFIED (statement only, no incidence) |
| **Spontaneous pneumothorax** | Osteosarcoma lung metastases: 31/123 (**25%**) in one Chinese centre; associated with **cavitation (OR 12.4)** and **pleural involvement (OR 15.5)**. Also a TKI effect: pazopanib 3.3% (s3 §10), cabozantinib 9% in osteosarcoma (s2 §7e) | Teach patients that sudden chest pain/dyspnoea needs urgent assessment; CXR; drainage per size | Li 2024 [A] VERIFIED (single-centre) |
| **GI bleeding / tumour haemorrhage (GIST)** | Common presenting symptom; in resected GIST, bleeding was **not** an independent prognostic factor (pooled HR 1.45, 0.73–2.86). GI/intra-abdominal haemorrhage ~5% on imatinib (B2222, s4 §4). EUS biopsy preferred over percutaneous biopsy because of haemorrhage and seeding risk (s1 §4.1) | Resuscitate, endoscopy/IR; tumour perforation or bleed may meet the rupture definition (CA-8) | Shi 2023 [A] VERIFIED |
| **HD-MTX delayed clearance / AKI** | See s2 §15–19 (now re-checked, CA-1) | Leucovorin per nomogram; glucarpidase **not licensed in Taiwan** | VERIFIED |
| **Ifosfamide encephalopathy** | 11% in a Taiwan cohort (s4 §5) | Stop ifosfamide, hydrate; methylene blue (watch serotonin syndrome with opioids/SSRIs) | VERIFIED |
| **Rhabdomyolysis** (trabectedin) | 0.7% (fatal 0.3%), mostly cycle 2 (s4 §9) | CPK before each dose | VERIFIED |
| **CRS / ICANS** (afami-cel) | CRS 71–75% (s3 §12); not licensed in Taiwan | — | VERIFIED |
| **Hypercalcaemia after stopping denosumab** (GCTB) | 1% (4/526) of patients | Check calcium after stopping | Chawla 2019 [A] VERIFIED |
| **Hypoglycaemia (Doege–Potter syndrome)** | Non-islet-cell tumour hypoglycaemia from **IGF-2** secretion by solitary fibrous tumour, in about **5–10% of SFTs**; hypokalaemia is a clue; raised IGF-2:IGF-1 ratio; resolves after resection; steroids are a bridge | Check glucose in confused patients with a large pleural/pelvic mass | Kiely 2021 [FT, case report + review] PARTIAL; Crowley 2022 [A] PARTIAL |

### CA-10. Still missing or [UNVERIFIED] after this critique

- **NHI (健保) reimbursement:** chapter section skipped (pending).
- **Rhabdomyosarcoma (VAC-based) is not covered** in any file. Decide whether the adult NP chapter needs it; if so, verify the COG/EpSSG regimens.
- **Kaposi sarcoma** (separate NCCN guideline v1.2027), **DFSP** (imatinib on the TFDA label, per sarcoma_4 §E) and **chordoma** systemic therapy are not covered.
- National all-hospital GIST count for 2023; SS18::SSX and FUS::DDIT3 positivity percentages; the original Joensuu 2008 table; ESMO guideline full texts (403); exact GIST follow-up intervals; Ewing whole-lung RT dose; NCCN professional content (login).
- Huvos grade definitions remain [PARTIAL] (secondary citation only).
- Doege–Potter frequency (5–10%) is from a case report with review, so [PARTIAL].
- Taiwan fertility-preservation subsidy and psychosocial resources (HPA unreachable).

### CA-11. References for the critic additions (APA 7)

**Journal articles**
- Woll, P. J., Reichardt, P., Le Cesne, A., Bonvalot, S., Azzarelli, A., Hoekstra, H. J., Leahy, M., Van Coevorden, F., Verweij, J., Hogendoorn, P. C. W., Ouali, M., Marreaud, S., Bramwell, V. H. C., & Hohenberger, P. (2012). Adjuvant chemotherapy with doxorubicin, ifosfamide, and lenograstim for resected soft-tissue sarcoma (EORTC 62931): A multicentre randomised controlled trial. *The Lancet Oncology*, *13*(10), 1045–1054. https://doi.org/10.1016/S1470-2045(12)70346-7 — PMID 22954508
- Pervaiz, N., Colterjohn, N., Farrokhyar, F., Tozer, R., Figueredo, A., & Ghert, M. (2008). A systematic meta-analysis of randomized controlled trials of adjuvant chemotherapy for localized resectable soft-tissue sarcoma. *Cancer*, *113*(3), 573–581. https://doi.org/10.1002/cncr.23592 — PMID 18521899
- Tawbi, H. A., Burgess, M., Bolejack, V., Van Tine, B. A., Schuetze, S. M., Hu, J., D'Angelo, S., Attia, S., Riedel, R. F., Priebat, D. A., Movva, S., Davis, L. E., Okuno, S. H., Reed, D. R., Crowley, J., Butterfield, L. H., Salazar, R., Rodriguez-Canales, J., Lazar, A. J., . . . Patel, S. (2017). Pembrolizumab in advanced soft-tissue sarcoma and bone sarcoma (SARC028): A multicentre, two-cohort, single-arm, open-label, phase 2 trial. *The Lancet Oncology*, *18*(11), 1493–1501. https://doi.org/10.1016/S1470-2045(17)30624-1 — PMID 28988646; PMC7939029
- D'Angelo, S. P., Mahoney, M. R., Van Tine, B. A., Atkins, J., Milhem, M. M., Jahagirdar, B. N., Antonescu, C. R., Horvath, E., Tap, W. D., Schwartz, G. K., & Streicher, H. (2018). Nivolumab with or without ipilimumab treatment for metastatic sarcoma (Alliance A091401): Two open-label, non-comparative, randomised, phase 2 trials. *The Lancet Oncology*, *19*(3), 416–426. https://doi.org/10.1016/S1470-2045(18)30006-8 — PMID 29370992; PMC6126546
- Chen, A. P., Sharon, E., O'Sullivan-Coyne, G., Moore, N., Foster, J. C., Hu, J. S., Van Tine, B. A., Conley, A. P., Read, W. L., Riedel, R. F., Burgess, M. A., Glod, J., Davis, E. J., Merriam, P., Naqash, A. R., Fino, K. K., Miller, B. L., Wilsker, D. F., Begum, A., . . . Doroshow, J. H. (2023). Atezolizumab for advanced alveolar soft part sarcoma. *The New England Journal of Medicine*, *389*(10), 911–921. https://doi.org/10.1056/NEJMoa2303383 — PMID 37672694; PMC10729808
- Chen, A. P., Rosenberger, C. L., Moore, N., Foster, J. C., Naqash, A. R., Sharon, E., O'Sullivan Coyne, G., Schwartz, G. K., Riedel, R. F., Glod, J., Hu, J. S., Conley, A. P., Read, W. L., Burgess, M. A., Davis, E. J., Merriam, P., Deshpande, H. A., Ladle, B. H., Okuno, S. H., . . . Doroshow, J. H. (2026). Atezolizumab for alveolar soft part sarcoma: A clinical trial update. *Journal of Clinical Oncology*, *44*(16), 1490–1497. https://doi.org/10.1200/JCO-25-02811 — PMID 41999612 *(cited only; no abstract read)*
- Penel, N., Bui, B. N., Bay, J.-O., Cupissol, D., Ray-Coquard, I., Piperno-Neumann, S., Kerbrat, P., Fournier, C., Taieb, S., Jimenez, M., Isambert, N., Peyrade, F., Chevreau, C., Bompas, E., Brain, E. G. C., & Blay, J.-Y. (2008). Phase II trial of weekly paclitaxel for unresectable angiosarcoma: The ANGIOTAX Study. *Journal of Clinical Oncology*, *26*(32), 5269–5274. https://doi.org/10.1200/JCO.2008.17.3146 — PMID 18809609
- Gounder, M. M., Mahoney, M. R., Van Tine, B. A., Ravi, V., Attia, S., Deshpande, H. A., Gupta, A. A., Milhem, M. M., Conry, R. M., Movva, S., Pishvaian, M. J., Riedel, R. F., Sabagh, T., Tap, W. D., Horvat, N., Basch, E., Schwartz, L. H., Maki, R. G., Agaram, N. P., . . . Schwartz, G. K. (2018). Sorafenib for advanced and refractory desmoid tumors. *The New England Journal of Medicine*, *379*(25), 2417–2428. https://doi.org/10.1056/NEJMoa1805052 — PMID 30575484; PMC6447029
- Chawla, S., Blay, J.-Y., Rutkowski, P., Le Cesne, A., Reichardt, P., Gelderblom, H., Grimer, R. J., Choy, E., Skubitz, K., Seeger, L., Schuetze, S. M., Henshaw, R., Dai, T., Jandial, D., & Palmerini, E. (2019). Denosumab in patients with giant-cell tumour of bone: A multicentre, open-label, phase 2 study. *The Lancet Oncology*, *20*(12), 1719–1729. https://doi.org/10.1016/S1470-2045(19)30663-1 — PMID 31704134
- Villani, A., Shore, A., Wasserman, J. D., Stephens, D., Kim, R. H., Druker, H., Gallinger, B., Naumer, A., Kohlmann, W., Novokmet, A., Tabori, U., Tijerin, M., Greer, M.-L. C., Finlay, J. L., Schiffman, J. D., & Malkin, D. (2016). Biochemical and imaging surveillance in germline TP53 mutation carriers with Li-Fraumeni syndrome: 11 year follow-up of a prospective observational study. *The Lancet Oncology*, *17*(9), 1295–1305. https://doi.org/10.1016/S1470-2045(16)30249-2 — PMID 27501770
- Ballinger, M. L., Best, A., Mai, P. L., Khincha, P. P., Loud, J. T., Peters, J. A., Achatz, M. I., Chojniak, R., Balieiro da Costa, A., Santiago, K. M., Garber, J., O'Neill, A. F., Eeles, R. A., Evans, D. G., Bleiker, E., Sonke, G. S., Ruijs, M., Loo, C., Schiffman, J., . . . Savage, S. A. (2017). Baseline surveillance in Li-Fraumeni syndrome using whole-body magnetic resonance imaging: A meta-analysis. *JAMA Oncology*, *3*(12), 1634–1639. https://doi.org/10.1001/jamaoncol.2017.1968 — PMID 28772291; PMC5824277
- Puri, A., Gulia, A., Hawaldar, R., Ranganathan, P., & Badwe, R. A. (2014). Does intensity of surveillance affect survival after surgery for sarcomas? Results of a randomized noninferiority trial. *Clinical Orthopaedics and Related Research*, *472*(5), 1568–1575. https://doi.org/10.1007/s11999-013-3385-9 — PMID 24249538; PMC3971232
- Blay, J.-Y., Le Cesne, A., Ray-Coquard, I., Bui, B., Duffaud, F., Delbaldo, C., Adenis, A., Viens, P., Rios, M., Bompas, E., Cupissol, D., Guillemet, C., Kerbrat, P., Fayette, J., Chabaud, S., Berthaud, P., & Perol, D. (2007). Prospective multicentric randomized phase III study of imatinib in patients with advanced gastrointestinal stromal tumors comparing interruption versus continuation of treatment beyond 1 year: The French Sarcoma Group. *Journal of Clinical Oncology*, *25*(9), 1107–1113. https://doi.org/10.1200/JCO.2006.09.0183 — PMID 17369574
- Le Cesne, A., Ray-Coquard, I., Bui, B. N., Adenis, A., Rios, M., Bertucci, F., Duffaud, F., Chevreau, C., Cupissol, D., Cioffi, A., Emile, J.-F., Chabaud, S., Pérol, D., & Blay, J.-Y. (2010). Discontinuation of imatinib in patients with advanced gastrointestinal stromal tumours after 3 years of treatment: An open-label multicentre randomised phase 3 trial. *The Lancet Oncology*, *11*(10), 942–949. https://doi.org/10.1016/S1470-2045(10)70222-9 — PMID 20864406
- Gonzalez, M. R., Bedi, A., Karczewski, D., & Lozano-Calderon, S. A. (2023). Are pathologic fractures in patients with osteosarcoma associated with worse survival outcomes? A systematic review and meta-analysis. *Clinical Orthopaedics and Related Research*, *481*(12), 2433–2443. https://doi.org/10.1097/CORR.0000000000002687 — PMID 37184541; PMC10642876
- Li, J., Deng, C., Yuan, J., Jia, H., & Peng, L. (2024). Association of CT characteristics of osteosarcoma lung metastases with spontaneous pneumothorax: A retrospective analysis. *Journal of Thoracic Disease*, *16*(12), 8417–8423. https://doi.org/10.21037/jtd-24-1015 — PMID 39831258; PMC11740071
- Shi, X., Chen, Z., Shou, C., Bai, H., Yang, W., Zhang, Q., Liu, X., & Yu, J. (2023). The prognostic role of gastrointestinal bleeding in patients with a primary gastrointestinal stromal tumor: A long-term follow-up study. *Journal of Gastrointestinal Oncology*, *14*(5), 2028–2038. https://doi.org/10.21037/jgo-22-1240 — PMID 37969844; PMC10643578
- Kiely, N. P., Sinha, R., Tang, K., & Wan, K. M. (2021). Doege-Potter syndrome: A systematic review of the literature and case presentation of a rare pelvic malignant solitary fibrous tumour. *BMJ Case Reports*, *14*(8), Article e242447. https://doi.org/10.1136/bcr-2021-242447 — PMID 34413033; PMC8378376
- Crowley, M. T., Lonergan, E., O'Callaghan, P., Joyce, C. M., Morita, M., Conlon, N., & O'Halloran, D. J. (2022). IGF-2 mediated hypoglycemia and the paradox of an apparently benign lesion: A case report & review of the literature. *BMC Endocrine Disorders*, *22*(1), Article 262. https://doi.org/10.1186/s12902-022-01175-4 — PMID 36303203; PMC9615362
- Bispo Júnior, R. Z., & Camargo, O. P. de. (2011). Is there any difference in the prognosis for patients with primary osteosarcoma with a poor response to neoadjuvant chemotherapy between Huvos grades I and II? *Revista Brasileira de Ortopedia*, *46*(4), 420–423. https://doi.org/10.1016/S2255-4971(15)30256-1 — PMID 27027032; PMC4799283
- Rosen, G., Caparros, B., Huvos, A. G., Kosloff, C., Nirenberg, A., Cacavio, A., Marcove, R. C., Lane, J. M., Mehta, B., & Urban, C. (1982). Preoperative chemotherapy for osteogenic sarcoma: Selection of postoperative adjuvant chemotherapy based on the response of the primary tumor to preoperative chemotherapy. *Cancer*, *49*(6), 1221–1230. https://doi.org/10.1002/1097-0142(19820315)49:6<1221::aid-cncr2820490625>3.0.co;2-e — PMID 6174200

**Guidelines**
- Hayes, A. J., Nixon, I. F., Strauss, D. C., Seddon, B. M., Desai, A., Benson, C., Judson, I. R., & Dangoor, A. (2025). UK guidelines for the management of soft tissue sarcomas. *British Journal of Cancer*, *132*(1), 11–31. https://doi.org/10.1038/s41416-024-02674-y — PMID 38734790; PMC11724041
- Gerrand, C., Amary, F., Anwar, H. A., Brennan, B., Dileo, P., Kalkat, M. S., McCabe, M. G., McCullough, A. L., Parry, M. C., Patel, A., Seddon, B. M., Sherriff, J. M., Tirabosco, R., & Strauss, S. J. (2025). UK guidelines for the management of bone sarcomas. *British Journal of Cancer*, *132*(1), 32–48. https://doi.org/10.1038/s41416-024-02868-4 — PMID 39550489; PMC11723950

**Labels, registries and web pages**
- Labels re-read through openFDA on 2026-10-29:
  - Methotrexate Injection (Hospira, 2025-06-10, set 0d63ba29-b692-41b4-87e8-351265c8273f)
  - Leucovorin Calcium Injection (Sagent, 2026-06-16, set c0cbcbf6-6fd2-4cf3-877a-bb0fe3df4e59)
  - VORAXAZE (BTG, 2024-11-27, set acaef5a6-b740-40e3-8ffe-74a75c74745c)
  - MESNEX (2025-12-10, set 1dd69e84-616d-fb77-e063-6394a90af2f4)
  - YONDELIS (Janssen, 2026-01-06, set 472bd78e-be17-4b9d-90f4-9482c3aec9ff)
  - PEDMARK (Fennec, 2025-10-27, set f98c7076-2a7b-4fd7-ab90-eed5e9137bae)
  - TECENTRIQ (2026-05-20, set 6fa682c9-a312-4932-9831-f286908660ee)
  - XGEVA (Amgen, 2026-06-23, set 628f0998-1206-4001-aeee-18133aa9f3bf)
- National Comprehensive Cancer Network. (2026). *NCCN guidelines* [Category 1, 3 and 4 listings]. Retrieved October 29, 2026, from https://www.nccn.org/guidelines/category_1
- PDQ Pediatric Treatment Editorial Board. (2024, November 27). *Ewing sarcoma and undifferentiated small round cell sarcomas of bone and soft tissue treatment (PDQ®)–Health professional version*. National Cancer Institute. https://www.cancer.gov/types/bone/hp/ewing-treatment-pdq
- 衛生福利部. (2025, January 10). *114年擴大肺癌篩檢服務 新年從健康開始*. https://mohw.gov.tw/cp-16-81184-1.html

**Working files:** abstracts, PMC XML and label JSON are in /tmp/claude-0/-home-user-oncology-educater/6a66dc7f-55e5-547a-b95f-33d6978992bf/scratchpad/critic/.
