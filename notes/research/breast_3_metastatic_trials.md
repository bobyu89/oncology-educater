# Breast 3. Metastatic breast cancer key trials: citation and data verification

Handbook: Taiwanese oncology NP (專科護理師) handbook, breast cancer chapter (ward practice and 專師甄審)
Verification date: 2026-10-29
Method: Every PMID was pulled from PubMed through NCBI E-utilities (efetch/esearch; same database as the PubMed MCP tools). Numbers come from the PubMed abstract unless another source is named. Where an abstract lacked a requested number, I checked the PMC full text, then the current US FDA label (openFDA JSON, effective date given), then ClinicalTrials.gov (API v2) for trial phase. Taiwan licence status comes from the TFDA licence dataset (InfoId=36, CSV dated 2026-10-27, downloaded 2026-10-29). Nothing was filled from memory. Anything still missing is marked **[UNVERIFIED]**.

**Source tags used inline**
- [A] = PubMed abstract of the cited paper
- [FT] = PMC full text of the cited paper (results section or tables)
- [L-Brand YYYY-MM-DD] = current US FDA prescribing information via openFDA, with label effective date
- [CT.gov] = ClinicalTrials.gov registry record (API v2)
- [TFDA] = TFDA drug-licence dataset (InfoId=36), active licences only
- [SS] = secondary source (conference summary, review, regulatory commentary); never enough on its own for [VERIFIED]
- (computed) = arithmetic I did from verified numbers
- **[UNVERIFIED]** = not stated in any source checked; do not print without checking the full paper

**Section status tags**
- **[VERIFIED]** = citation confirmed on PubMed, and the primary-endpoint result (median, HR, 95% CI where reported) confirmed from [A], [FT] or [L]
- **[PARTIAL]** = citation confirmed, but part of the requested result is missing from the primary sources or comes only from [SS]
- **[UNVERIFIED]** = paper not found

**APA 7 notes.** Author lists follow APA 7: all authors up to 20; for 21 or more, the first 19, an ellipsis, then the final author. Study-group bylines (e.g., "SOLAR-1 Study Group") are left out. Titles are converted to sentence case from the PubMed title. The year is the journal-issue year, which can differ from the e-pub year. Article-number journals (BMJ, ESMO Open, npj Breast Cancer) are cited as "Article xxx". Two PubMed author records contain data errors; see flag 19.

**Abbreviations:** AI, aromatase inhibitor; BICR, blinded independent central review; CDK4/6i, CDK4/6 inhibitor; ET, endocrine therapy; FN, febrile neutropenia; ICC/TPC, investigator's/physician's choice chemotherapy; ILD, interstitial lung disease/pneumonitis; ORR, objective response rate; T-DXd, trastuzumab deruxtecan; Dato-DXd, datopotamab deruxtecan; SG, sacituzumab govitecan.

---

## 0. Corrections and flags for the editor (read first)

1. **HER2CLIMB is a randomized phase 2 trial, not phase 3.** ClinicalTrials.gov NCT02614794 lists phase "PHASE2", actual enrolment 612 [CT.gov]. It was registrational (tucatinib approval), but the handbook should not call it "phase III".
2. **Only ribociclib has a statistically significant first-line OS benefit among CDK4/6 inhibitors in this brief.**
   - MONALEESA-2: HR 0.76 (0.63–0.93), P = 0.008 [A].
   - MONALEESA-7: HR 0.71 (0.54–0.95), P = 0.00973 [A].
   - PALOMA-2 OS **not significant**: HR 0.96 (0.78–1.18) [A].
   - MONARCH 3 final OS **not significant**: HR 0.804 (0.637–1.015), P = 0.0664 [A].
   - PALOMA-3 OS **not significant** overall: HR 0.81 (0.64–1.03), P = 0.09 [A].
   - Do not write "CDK4/6 inhibitors all prolong survival".
3. **Most new oral ER degraders won only in ESR1-mutant disease.**
   - EMBER-3 all-comers: HR 0.87 (0.72–1.04), P = 0.12 [A].
   - VERITAC-2 all-comers: HR 0.83 (0.69–1.01), P = 0.07 [A].
   - EMERALD: benefit in the ITT was "primarily attributed" to ESR1-mutant patients; non-ESR1 HR 0.86 (0.63–1.19) [L-Orserdu 2026-06-24].
   - All three US labels (elacestrant, imlunestrant, vepdegestrant) are restricted to **ESR1-mutated** disease.
4. **EMERALD OS changed between paper and label.** The JCO interim OS in ESR1-mutant patients was HR 0.59 (0.36–0.96), "nonsignificant" [FT]. The current FDA label gives OS HR **0.90 (0.63–1.30), not significant**, in ESR1-mutant patients (53% events in each arm) [L-Orserdu]. Quote the label figure as the more mature one.
5. **Elacestrant dose: 400 mg in the paper = 345 mg on the label.** The 345 mg tablet "contains 400 mg of elacestrant hydrochloride (approximately 345 mg of elacestrant free base)" [L-Orserdu description field]. Same drug, same dose; different salt convention.
6. **Small numeric disagreements between paper and label (both correct for their own analysis):**
   - EMERALD randomized n: 477 (JCO) vs 478 enrolled, 239 vs 239 (label).
   - VERITAC-2 ESR1-mutant PFS HR: 0.58 (0.43–0.78) (NEJM) vs 0.57 (0.42–0.77) (label).
   - DESTINY-Breast09 ORR: 85.1% vs 78.6% (NEJM abstract) vs 87% vs 81% in patients with measurable disease (label).
7. **Typo in the DESTINY-Breast04 long-term paper.** Nature Medicine 2025 text says "577 patients" were randomized, but its own arms add up to 373 + 184 = **557**, matching NEJM 2022 [FT] (computed).
8. **Dato-DXd: no OS benefit in HR+ disease, but an OS benefit in first-line TNBC.**
   - TROPION-Breast01 final OS: HR **1.01** (0.83–1.22), P = 0.9445. Subsequent ADC use was imbalanced: 12.3% vs 24.0% [A].
   - TROPION-Breast02 OS: HR 0.79 (95.01% CI 0.64–0.98), P = 0.029 [A].
9. **T-DXd ILD rates rise with follow-up.**
   - DESTINY-Breast03: 10.5% (NEJM 2022) → 15% (Lancet 2023) → 16.7% (Nat Med 2024) [A].
   - DESTINY-Breast04: grade 5 rose from 0.8% to 1.1% [A, FT].
   - Pooled 9 early-phase studies: 15.4%, grade 5 2.2% [A].
   - FDA label (all 5.4 mg/kg monotherapy): 12%, fatal 0.9%; with pertuzumab 12%, fatal 0.5% [L-Enhertu 2026-05-15].
10. **Hyperglycemia rates depend on the definition.** AE-term rates are lower than lab-based "increased fasting glucose" rates in the labels. Compare like with like:
    - Capivasertib: hyperglycemia AE 16.3% [FT] vs increased fasting glucose 37% [L-Truqap 2026-06-12].
    - Inavolisib: AE 63.4% [FT] vs lab 85% [L-Itovebi 2026-04-21].
    - Alpelisib: 65% [L-Piqray 2025-12-15].
11. **Atezolizumab TNBC story.**
    - IMpassion130 ITT OS was never significant (final HR 0.87, P = 0.077) [A].
    - IMpassion131 (paclitaxel partner) failed: PFS HR 0.82, P = 0.20; OS HR 1.11 [A].
    - IMpassion132 (early relapse) failed: OS HR 0.93 [A].
    - The FDA ODAC (April 2021) initially voted to *retain* the PD-L1+ TNBC indication [A/FT, Lemery & Pazdur 2022]. The US indication was later withdrawn [SS, Hakariya 2025; exact date **[UNVERIFIED]**].
    - **The TFDA licence for Tecentriq still lists atezolizumab + nab-paclitaxel for PD-L1 IC ≥1% mTNBC** (licences 衛部菌疫輸字第001050號 and 001258號) [TFDA]. Japan also retained it [SS].
12. **Taiwan licence gaps (TFDA dataset, 2026-10-27)** [TFDA]:
    - **No active licence:** elacestrant, camizestrant, vepdegestrant, pyrotinib.
    - **Imlunestrant licensed 2026-05-15** (Inluriyo, ESR1-mutated).
    - **Tucatinib licensed 2026-03-02.**
    - **Trodelvy's Taiwan licence has no first-line TNBC indication** (only ≥2 prior systemic therapies for TNBC, and HR+/HER2−). ASCENT-03/-04 first-line indications are US-only so far.
    - **Datroway's Taiwan licence is HR+/HER2− only**; there is no TNBC indication (US label has one).
13. **CAPItello-291: the US/TFDA indication is the altered subgroup only.**
    - FDA label: PIK3CA/AKT1/PTEN-altered disease, tumour tissue NGS. Non-altered exploratory HR 0.79 (0.61–1.02) [L-Truqap].
    - TFDA wording is the same: 具PIK3CA/AKT1/PTEN任一變異 [TFDA].
    - **No final CAPItello-291 OS paper found on PubMed.**
14. **SERENA-6 / camizestrant.**
    - FDA approval (Etcamah, label effective 2026-09-04) is **accelerated approval**, based on PFS.
    - PFS2 is now significant: HR 0.63 (0.46–0.86), p = 0.0037 (Lancet Oncol 2026) [A]. OS is immature (12% maturity) [L-Etcamah].
    - **Boxed warning:** arrhythmia risk with ribociclib or other QTc-prolonging drugs [L].
15. **postMONARCH final OS (Ann Oncol, e-pub 2026-10-24) is not significant:** 32.1 vs 24.6 months, HR 0.80 (0.60–1.06), P = 0.11 [A].
16. **PHOEBE OS is available only as a conference summary** (Oncologist 2022 supplement, ASCO 2022) [SS]: HR 0.69 (0.48–0.98). That summary's PFS table **swaps the arms** (it prints pyrotinib 5.6 vs lapatinib 12.5 months; the Lancet Oncol primary paper gives pyrotinib 12.5 vs lapatinib 6.8 months). Do not copy that table.
17. **Newer data beyond the brief that the chapter may want:**
    - PHILA long-term OS (BMJ 2026): pyrotinib + trastuzumab + docetaxel, first line, China.
    - EMBER-3 updated OS (Ann Oncol 2026).
    - SERENA-6 extended analysis (Lancet Oncol 2026).
    - IMpassion132 (Ann Oncol 2024).
    - The Ibrance label now includes **PATINA** (palbociclib + anti-HER2 + ET maintenance in HR+/HER2+) [L-Ibrance 2026-07-06]. Not reviewed further.
18. **Not found on PubMed as of 2026-10-29:**
    - CAPItello-291 final OS.
    - DESTINY-Breast06 final OS.
    - DESTINY-Breast09 T-DXd + placebo arm results and OS.
    - ASCENT-03 and ASCENT-04 OS. The label says both are immature (51% and 46% deaths).
    - VERITAC-2 OS.
    - A stand-alone EMERALD OS paper; the final OS is in the label only.
    - TROPION-Breast01 median OS values; the final-OS abstract gives only the HR.
19. **PubMed author-record errors (corrected or flagged in references):**
    - ASCENT final (JCO 2024): PubMed lists "Shaughnessy, Joyce O'". I corrected it to O'Shaughnessy, J.
    - EMBER-3 update (Ann Oncol 2026): PubMed lists the surname "Qingyuan" (forename "Z"), which is probably Zhang Qingyuan. Left as PubMed has it, marked [sic].
    - INAVO120 primary (NEJM 2024): PubMed publication type says "Phase II", but the paper is phase 3.
    - TROPiCS-02 primary (JCO 2022): PubMed splits "Gómez Pardo" as surname "Pardo". I corrected it to Gómez Pardo, P., matching the Lancet 2023 record.
20. **Errata exist; check before quoting** (contents not reviewed):
    - MONALEESA-2 NEJM 2016 (erratum 2018, PMID 30586508).
    - MONALEESA-2 Ann Oncol 2018 (erratum 2019, PMID 31407010).
    - PALOMA-3 Lancet Oncol 2016 (two errata, PMIDs 27300673, 27733295).
    - EMERALD JCO 2022 (erratum 2023, PMID 37364222).
    - MONARCH 3 final OS (corrigendum 2025, PMID 41093689).
    - DESTINY-Breast03 Lancet 2023 (erratum, PMID 36803433).
    - HER2CLIMB NEJM 2020 (erratum, PMID 31881136) and final OS (corrigendum 2023, PMID 36564285).
    - IMpassion130 final OS (two corrigenda, PMIDs 34353668, 34740469).
    - OlympiAD NEJM 2017 (erratum, PMID 28792849).
    - PHILA BMJ 2023 (erratum, PMID 37973164).
    - ASCENT safety npj 2022 (erratum 2024, PMID 38844800).
21. **NCCN version:** the nccn.org category page (read 2026-10-29) lists **NCCN Breast Cancer Version 9.2026**. The professional PDF needs a login; I did not check preferred-regimen wording.

---

## Quick-reference table (for the handbook's summary page)

| Trial | Setting | Experimental vs control | Primary endpoint result | OS | Tag |
|---|---|---|---|---|---|
| PALOMA-2 | 1L HR+/HER2−, postmenopausal | Palbociclib + letrozole vs placebo + letrozole | PFS 24.8 vs 14.5 mo, HR 0.58 | 53.9 vs 51.2 mo, HR 0.96 (NS) | VERIFIED |
| MONALEESA-2 | 1L, postmenopausal | Ribociclib + letrozole vs placebo + letrozole | PFS HR 0.56 (interim); 25.3 vs 16.0 mo (update) | 63.9 vs 51.4 mo, HR 0.76 (sig) | VERIFIED |
| MONALEESA-7 | 1L, premenopausal | Ribociclib + goserelin + NSAI/tamoxifen vs placebo | PFS 23.8 vs 13.0 mo, HR 0.55 | 42-mo OS 70.2% vs 46.0%, HR 0.71 (sig) | VERIFIED (median OS UNVERIFIED) |
| MONARCH 3 | 1L, postmenopausal | Abemaciclib + NSAI vs placebo + NSAI | PFS 28.18 vs 14.76 mo, HR 0.540 | 66.8 vs 53.7 mo, HR 0.804 (NS) | VERIFIED |
| PALOMA-3 | After ET progression | Palbociclib + fulvestrant vs placebo + fulvestrant | PFS 9.5 vs 4.6 mo, HR 0.46 | 34.9 vs 28.0 mo, HR 0.81 (NS) | VERIFIED |
| SOLAR-1 | PIK3CA-mut, after AI | Alpelisib + fulvestrant vs placebo + fulvestrant | PFS 11.0 vs 5.7 mo, HR 0.65 | 39.3 vs 31.4 mo, HR 0.86 (NS) | VERIFIED |
| CAPItello-291 | After AI ± CDK4/6i | Capivasertib + fulvestrant vs placebo + fulvestrant | PFS 7.2 vs 3.6 mo, HR 0.60 (all); 7.3 vs 3.1, HR 0.50 (altered) | Immature | VERIFIED |
| EMERALD | 2L/3L after CDK4/6i | Elacestrant vs fulvestrant/AI | PFS HR 0.70 (all); ESR1m 3.8 vs 1.9 mo, HR 0.55 | ESR1m HR 0.90 (NS, label) | VERIFIED |
| INAVO120 | 1L, endocrine-resistant, PIK3CA-mut | Inavolisib + palbociclib + fulvestrant vs placebo + palbo + fulv | PFS 15.0 vs 7.3 mo, HR 0.43 | 34.0 vs 27.0 mo, HR 0.67 (sig) | VERIFIED |
| SERENA-6 | 1L, ESR1m emerging on AI + CDK4/6i | Switch to camizestrant + CDK4/6i vs continue AI + CDK4/6i | PFS 16.0 vs 9.2 mo, HR 0.44 | Immature; PFS2 HR 0.63 | VERIFIED |
| EMBER-3 | After AI ± CDK4/6i | Imlunestrant vs SOC ET vs imlunestrant + abemaciclib | ESR1m PFS 5.5 vs 3.8 mo; all-comers HR 0.87 (NS); combo vs imlu HR 0.57 | ESR1m HR 0.60 (boundary not reached) | VERIFIED |
| VERITAC-2 | After 1 CDK4/6i + ET | Vepdegestrant vs fulvestrant | ESR1m PFS 5.0 vs 2.1 mo, HR 0.58; all HR 0.83 (NS) | Not reported | VERIFIED |
| postMONARCH | After CDK4/6i + AI | Abemaciclib + fulvestrant vs placebo + fulvestrant | PFS 6.0 vs 5.3 mo, HR 0.73 | 32.1 vs 24.6 mo, HR 0.80 (NS) | VERIFIED |
| DESTINY-Breast04 | HER2-low, 1–2 prior chemo | T-DXd vs TPC | HR+ PFS 10.1 vs 5.4 mo, HR 0.51 | HR+ 23.9 vs 17.5 mo, HR 0.64 | VERIFIED |
| DESTINY-Breast06 | HR+, HER2-low/ultralow, chemo-naive for MBC | T-DXd vs TPC | HER2-low PFS 13.2 vs 8.1 mo, HR 0.62 | Immature | VERIFIED |
| TROPION-Breast01 | HR+/HER2−, 1–2 prior chemo | Dato-DXd vs ICC | PFS 6.9 vs 4.9 mo, HR 0.63 | HR 1.01 (NS) | VERIFIED (OS medians UNVERIFIED) |
| TROPiCS-02 | HR+/HER2−, 2–4 prior chemo | SG vs TPC | PFS 5.5 vs 4.0 mo, HR 0.66 | 14.4 vs 11.2 mo, HR 0.79 (sig) | VERIFIED |
| CLEOPATRA | 1L HER2+ | Pertuzumab + trastuzumab + docetaxel vs placebo + T + D | PFS 18.5 vs 12.4 mo, HR 0.62 | 57.1 vs 40.8 mo, HR 0.69 (end of study) | VERIFIED |
| DESTINY-Breast03 | 2L HER2+ | T-DXd vs T-DM1 | PFS 28.8 vs 6.8 mo, HR 0.33 (updated) | 52.6 vs 42.7 mo, HR 0.73 | VERIFIED |
| DESTINY-Breast09 | 1L HER2+ | T-DXd + pertuzumab vs THP | PFS 40.7 vs 26.9 mo, HR 0.56 | Immature | VERIFIED |
| HER2CLIMB (phase 2) | ≥2 prior anti-HER2 incl. T-DM1 | Tucatinib + trastuzumab + capecitabine vs placebo + T + C | PFS 7.8 vs 5.6 mo, HR 0.54 | 24.7 vs 19.2 mo, HR 0.73 (final) | VERIFIED |
| PHOEBE | HER2+, after trastuzumab + taxane (China) | Pyrotinib + capecitabine vs lapatinib + capecitabine | PFS 12.5 vs 6.8 mo, HR 0.39 | HR 0.69 (conference only) | PARTIAL |
| PHILA | 1L HER2+ (China) | Pyrotinib + trastuzumab + docetaxel vs placebo + T + D | PFS 24.3 vs 10.4 mo, HR 0.41 | HR 0.64, medians NR | VERIFIED |
| KEYNOTE-355 | 1L TNBC | Pembrolizumab + chemo vs placebo + chemo | CPS≥10 PFS 9.7 vs 5.6 mo, HR 0.65 | CPS≥10 23.0 vs 16.1 mo, HR 0.73 (sig) | VERIFIED |
| IMpassion130 | 1L TNBC | Atezolizumab + nab-paclitaxel vs placebo + nab-P | ITT PFS 7.2 vs 5.5 mo, HR 0.80; PD-L1+ 7.5 vs 5.0, HR 0.62 | ITT HR 0.87 (NS); PD-L1+ 25.4 vs 17.9 (exploratory) | VERIFIED |
| IMpassion131 | 1L TNBC | Atezolizumab + paclitaxel vs placebo + paclitaxel | PD-L1+ PFS 6.0 vs 5.7 mo, HR 0.82 (NS) | PD-L1+ 22.1 vs 28.3 mo, HR 1.11 | VERIFIED |
| ASCENT | ≥2L TNBC | SG vs TPC | PFS 5.6 vs 1.7 mo, HR 0.41 | 12.1 vs 6.7 mo, HR 0.48 | VERIFIED |
| ASCENT-03 | 1L TNBC, not PD-(L)1 candidates | SG vs chemo | PFS 9.7 vs 6.9 mo, HR 0.62 | Immature | VERIFIED |
| ASCENT-04 | 1L PD-L1+ TNBC | SG + pembrolizumab vs chemo + pembrolizumab | PFS 11.2 vs 7.8 mo, HR 0.65 | Immature | VERIFIED |
| TROPION-Breast02 | 1L TNBC, IO not an option | Dato-DXd vs ICC | PFS 10.8 vs 5.6 mo, HR 0.57 | 23.7 vs 18.7 mo, HR 0.79 (sig) | VERIFIED |
| OlympiAD | gBRCAm HER2−, ≤2 prior chemo | Olaparib vs TPC | PFS 7.0 vs 4.2 mo, HR 0.58 | 19.3 vs 17.1 mo, HR 0.90 (NS) | VERIFIED |
| EMBRACA | gBRCAm HER2− | Talazoparib vs TPC | PFS 8.6 vs 5.6 mo, HR 0.54 | 19.3 vs 19.5 mo, HR 0.848 (NS) | VERIFIED |

(NS = not statistically significant; sig = met prespecified significance; NR = not reached.)

---

# A. HR-positive / HER2-negative

## A1. PALOMA-2 (palbociclib + letrozole, first line) — [VERIFIED]

**References**
- Finn, R. S., Martin, M., Rugo, H. S., Jones, S., Im, S.-A., Gelmon, K., Harbeck, N., Lipatov, O. N., Walshe, J. M., Moulder, S., Gauthier, E., Lu, D. R., Randolph, S., Diéras, V., & Slamon, D. J. (2016). Palbociclib and letrozole in advanced breast cancer. *The New England Journal of Medicine*, *375*(20), 1925–1936. https://doi.org/10.1056/NEJMoa1607303 — PMID 27959613
- (OS) Slamon, D. J., Diéras, V., Rugo, H. S., Harbeck, N., Im, S.-A., Gelmon, K. A., Lipatov, O. N., Walshe, J. M., Martin, M., Chavez-MacGregor, M., Bananis, E., Gauthier, E., Lu, D. R., Kim, S., & Finn, R. S. (2024). Overall survival with palbociclib plus letrozole in advanced breast cancer. *Journal of Clinical Oncology*, *42*(9), 994–1000. https://doi.org/10.1200/JCO.23.00137 — PMID 38252901 (PMC10950136)
- (Asian subgroup) Im, S.-A., Mukai, H., Park, I. H., Masuda, N., Shimizu, C., Kim, S.-B., Im, Y.-H., Ohtani, S., Huang Bartlett, C., Lu, D. R., Iyer, S., Mori, Y., Mori, A., Gauthier, E., Finn, R. S., & Toi, M. (2019). Palbociclib plus letrozole as first-line therapy in postmenopausal Asian women with metastatic breast cancer: Results from the phase III, randomized PALOMA-2 study. *Journal of Global Oncology*, *5*, 1–19. https://doi.org/10.1200/JGO.18.00173 — PMID 31125276 (PMC6550032)

**Design:** Phase 3, double-blind, randomized 2:1 [A].
**Population:** 666 postmenopausal women, ER+/HER2− advanced breast cancer, no prior treatment for advanced disease [A].
**Arms:** Palbociclib + letrozole vs placebo + letrozole [A]. Label dose: palbociclib 125 mg once daily, 21 days on / 7 days off [L-Ibrance 2026-07-06].
**Primary endpoint (investigator PFS):** 24.8 months (95% CI 22.1–NE) vs 14.5 (12.9–17.1). HR 0.58 (0.46–0.72), P < 0.001 [A].
**OS (Slamon 2024, secondary endpoint):**
- Median follow-up 90.1 months; 405 deaths.
- 53.9 (49.8–60.8) vs 51.2 (43.7–58.9) months. HR 0.96 (0.78–1.18), one-sided P = .34. **Not significant.**
- More patients had unknown survival in the placebo arm (13.3% vs 21.2%). With recovered survival data: 53.8 vs 49.8 months, HR 0.92 (0.76–1.12) [A].
**Toxicity:**
- Grade 3–4 neutropenia 66.4% vs 1.4%; leukopenia 24.8% vs 0%.
- FN 1.8% vs 0%.
- Discontinuation for AEs 9.7% vs 5.9% [A].
**Asian subgroup (n = 95; relevant to Taiwan):**
- PFS 25.7 vs 13.9 months, HR 0.49 (0.27–0.87).
- Neutropenia more frequent in Asians: grade 3–4 89.2% vs 62.5% in non-Asians. No FN in Asians.
- Palbociclib trough concentration 93.8 vs 61.7 ng/mL [A].
- Teaching point: early dose modification, not discontinuation.

---

## A2. MONALEESA-2 (ribociclib + letrozole, first line; OS) — [VERIFIED]

**References**
- Hortobagyi, G. N., Stemmer, S. M., Burris, H. A., Yap, Y.-S., Sonke, G. S., Paluch-Shimon, S., Campone, M., Blackwell, K. L., André, F., Winer, E. P., Janni, W., Verma, S., Conte, P., Arteaga, C. L., Cameron, D. A., Petrakova, K., Hart, L. L., Villanueva, C., Chan, A., . . . O'Shaughnessy, J. (2016). Ribociclib as first-line therapy for HR-positive, advanced breast cancer. *The New England Journal of Medicine*, *375*(18), 1738–1748. https://doi.org/10.1056/NEJMoa1609709 — PMID 27717303 **Erratum:** *N Engl J Med 379*(26), 2582 (2018), PMID 30586508.
- (Updated PFS) Hortobagyi, G. N., Stemmer, S. M., Burris, H. A., Yap, Y. S., Sonke, G. S., Paluch-Shimon, S., Campone, M., Petrakova, K., Blackwell, K. L., Winer, E. P., Janni, W., Verma, S., Conte, P., Arteaga, C. L., Cameron, D. A., Mondal, S., Su, F., Miller, M., Elmeliegy, M., . . . O'Shaughnessy, J. (2018). Updated results from MONALEESA-2, a phase III trial of first-line ribociclib plus letrozole versus placebo plus letrozole in hormone receptor-positive, HER2-negative advanced breast cancer. *Annals of Oncology*, *29*(7), 1541–1547. https://doi.org/10.1093/annonc/mdy155 — PMID 29718092 **Erratum:** PMID 31407010.
- (Final OS) Hortobagyi, G. N., Stemmer, S. M., Burris, H. A., Yap, Y.-S., Sonke, G. S., Hart, L., Campone, M., Petrakova, K., Winer, E. P., Janni, W., Conte, P., Cameron, D. A., André, F., Arteaga, C. L., Zarate, J. P., Chakravartty, A., Taran, T., Le Gac, F., Serra, P., & O'Shaughnessy, J. (2022). Overall survival with ribociclib plus letrozole in advanced breast cancer. *The New England Journal of Medicine*, *386*(10), 942–950. https://doi.org/10.1056/NEJMoa2114663 — PMID 35263519

**Design:** Phase 3, randomized, placebo-controlled; 1:1 [A].
**Population:** 668 postmenopausal women, HR+/HER2− recurrent or metastatic, no prior systemic therapy for advanced disease [A].
**Arms:** Ribociclib 600 mg/day (3 weeks on / 1 week off) + letrozole 2.5 mg/day vs placebo + letrozole [A].
**Primary endpoint (investigator PFS):**
- Interim analysis: HR 0.56 (0.43–0.72), P = 3.29 × 10⁻⁶. 18-month PFS 63.0% vs 42.2%. ORR (measurable disease) 52.7% vs 37.1% [A].
- Updated analysis: median 25.3 (23.0–30.3) vs 16.0 (13.4–18.2) months, HR 0.568 (0.457–0.704) [A].
**Final OS (Hortobagyi 2022):**
- Median follow-up 6.6 years.
- **63.9 (52.4–71.0) vs 51.4 (47.2–59.7) months, HR 0.76 (0.63–0.93), two-sided P = 0.008** [A].
- Difference 12.5 months (computed). The abstract says "more than 12 months".
**Toxicity (primary paper):**
- Grade 3–4 neutropenia 59.3% vs 0.9%; leukopenia 21.0% vs 0.6%.
- Discontinuation for AEs 7.5% vs 2.1% [A].
- QTc and hepatotoxicity: see section F3.

---

## A3. MONALEESA-7 (ribociclib, premenopausal; OS) — [VERIFIED] (median OS [UNVERIFIED])

**References**
- Tripathy, D., Im, S.-A., Colleoni, M., Franke, F., Bardia, A., Harbeck, N., Hurvitz, S. A., Chow, L., Sohn, J., Lee, K. S., Campos-Gomez, S., Villanueva Vazquez, R., Jung, K. H., Babu, K. G., Wheatley-Price, P., De Laurentiis, M., Im, Y.-H., Kuemmel, S., El-Saghir, N., . . . Lu, Y.-S. (2018). Ribociclib plus endocrine therapy for premenopausal women with hormone-receptor-positive, advanced breast cancer (MONALEESA-7): A randomised phase 3 trial. *The Lancet Oncology*, *19*(7), 904–915. https://doi.org/10.1016/S1470-2045(18)30292-4 — PMID 29804902
- (OS) Im, S.-A., Lu, Y.-S., Bardia, A., Harbeck, N., Colleoni, M., Franke, F., Chow, L., Sohn, J., Lee, K.-S., Campos-Gomez, S., Villanueva-Vazquez, R., Jung, K.-H., Chakravartty, A., Hughes, G., Gounaris, I., Rodriguez-Lorenc, K., Taran, T., Hurvitz, S., & Tripathy, D. (2019). Overall survival with ribociclib plus endocrine therapy in breast cancer. *The New England Journal of Medicine*, *381*(4), 307–316. https://doi.org/10.1056/NEJMoa1903765 — PMID 31166679

**Design:** Phase 3, randomized, double-blind, placebo-controlled; 188 centres, 30 countries [A].
**Population:** 672 premenopausal or perimenopausal women aged 18–59 years, HR+/HER2− advanced breast cancer, no prior CDK4/6i. Up to one prior chemotherapy line for advanced disease was allowed [A].
**Arms:** Ribociclib 600 mg (3 weeks on / 1 off) or placebo, **plus goserelin 3.6 mg every 28 days**, plus tamoxifen 20 mg or an NSAI (letrozole 2.5 mg or anastrozole 1 mg) [A].
**Primary endpoint (investigator PFS):** 23.8 (19.2–NR) vs 13.0 (11.0–16.4) months. HR 0.55 (0.44–0.69), p < 0.0001 [A].
**OS (Im 2019, protocol-specified interim):**
- Deaths: 83/335 (24.8%) vs 109/337 (32.3%).
- **Estimated 42-month OS 70.2% vs 46.0%, HR 0.71 (0.54–0.95), P = 0.00973.**
- AI subgroup (n = 495): HR 0.70 (0.50–0.98) [A].
- Median OS: **[UNVERIFIED]**; not in the abstract, and the NEJM paper is not in PMC.
**Toxicity:**
- Grade 3–4 neutropenia 61% vs 4%; leukopenia 14% vs 1%.
- SAEs 18% vs 12%. No treatment-related deaths [A].
- **Tamoxifen + ribociclib increases QTc.** QTcF rose >60 ms from baseline in 16% (14/87) with ribociclib + tamoxifen vs 7% (18/245) with ribociclib + NSAI. The label now says ribociclib is **not indicated with tamoxifen** [L-Kisqali 2026-07-01].
- Nursing point: in premenopausal patients, ribociclib is paired with **ovarian suppression + an AI**, not tamoxifen.

---

## A4. MONARCH 3 (abemaciclib + NSAI, first line; final OS) — [VERIFIED]

**References**
- Goetz, M. P., Toi, M., Campone, M., Sohn, J., Paluch-Shimon, S., Huober, J., Park, I. H., Trédan, O., Chen, S.-C., Manso, L., Freedman, O. C., Garnica Jaliffe, G., Forrester, T., Frenzel, M., Barriga, S., Smith, I. C., Bourayou, N., & Di Leo, A. (2017). MONARCH 3: Abemaciclib as initial therapy for advanced breast cancer. *Journal of Clinical Oncology*, *35*(32), 3638–3646. https://doi.org/10.1200/JCO.2017.75.6155 — PMID 28968163
- (Final PFS) Johnston, S., Martin, M., Di Leo, A., Im, S.-A., Awada, A., Forrester, T., Frenzel, M., Hardebeck, M. C., Cox, J., Barriga, S., Toi, M., Iwata, H., & Goetz, M. P. (2019). MONARCH 3 final PFS: A randomized study of abemaciclib as initial therapy for advanced breast cancer. *npj Breast Cancer*, *5*, Article 5. https://doi.org/10.1038/s41523-018-0097-z — PMID 30675515 (PMC6336880)
- (Final OS) Goetz, M. P., Toi, M., Huober, J., Sohn, J., Trédan, O., Park, I. H., Campone, M., Chen, S.-C., Manso, L. M., Paluch-Shimon, S., Freedman, O. C., O'Shaughnessy, J., Pivot, X., Tolaney, S. M., Hurvitz, S. A., Llombart-Cussac, A., André, V., Saha, A., van Hal, G., . . . Johnston, S. R. D. (2024). Abemaciclib plus a nonsteroidal aromatase inhibitor as initial therapy for HR+, HER2- advanced breast cancer: Final overall survival results of MONARCH 3. *Annals of Oncology*, *35*(8), 718–727. https://doi.org/10.1016/j.annonc.2024.04.013 — PMID 38729566 **Corrigendum:** *Ann Oncol 36*(12), 1556 (2025), PMID 41093689; content not reviewed.

**Design:** Phase 3, double-blind; randomized 2:1 [A].
**Population:** 493 postmenopausal women, HR+/HER2− advanced breast cancer, no prior systemic therapy in the advanced setting [A].
**Arms:** Abemaciclib 150 mg twice daily (continuous) or placebo, plus anastrozole 1 mg or letrozole 2.5 mg daily. n = 328 vs 165 [A].
**Primary endpoint (investigator PFS):**
- Interim: HR 0.54 (0.41–0.72), P = .000021. Median NR vs 14.7 months [A].
- **Final PFS: 28.18 vs 14.76 months, HR 0.540 (0.418–0.698).** ORR 61.0% vs 45.5% [A].
**Final OS (Goetz 2024):**
- Median follow-up 8.1 years.
- 66.8 vs 53.7 months, HR 0.804 (0.637–1.015), P = 0.0664. **Not significant.**
- Visceral-disease subgroup: 63.7 vs 48.8 months, HR 0.758 (0.558–1.030) [A].
**Toxicity:**
- Diarrhea 81.3% (mostly grade 1, 44.6%).
- Grade 3–4 neutropenia 21.1% vs 1.2%; diarrhea 9.5% vs 1.2%; leukopenia 7.6% vs 0.6% [A, interim].
- Label (pooled abemaciclib trials):
  - Diarrhea 81–90%, grade 3 8–20%; median onset 6–8 days.
  - VTE 2–5%.
  - ILD 3.3% in MBC (0.4% fatal).
  - Grade ≥3 ALT 2–6% [L-Verzenio 2026-07-13].

---

## A5. PALOMA-3 (palbociclib + fulvestrant after ET progression) — [VERIFIED]

**References**
- Turner, N. C., Ro, J., André, F., Loi, S., Verma, S., Iwata, H., Harbeck, N., Loibl, S., Huang Bartlett, C., Zhang, K., Giorgetti, C., Randolph, S., Koehler, M., & Cristofanilli, M. (2015). Palbociclib in hormone-receptor-positive advanced breast cancer. *The New England Journal of Medicine*, *373*(3), 209–219. https://doi.org/10.1056/NEJMoa1505270 — PMID 26030518
- (Final PFS) Cristofanilli, M., Turner, N. C., Bondarenko, I., Ro, J., Im, S.-A., Masuda, N., Colleoni, M., DeMichele, A., Loi, S., Verma, S., Iwata, H., Harbeck, N., Zhang, K., Theall, K. P., Jiang, Y., Bartlett, C. H., Koehler, M., & Slamon, D. (2016). Fulvestrant plus palbociclib versus fulvestrant plus placebo for treatment of hormone-receptor-positive, HER2-negative metastatic breast cancer that progressed on previous endocrine therapy (PALOMA-3): Final analysis of the multicentre, double-blind, phase 3 randomised controlled trial. *The Lancet Oncology*, *17*(4), 425–439. https://doi.org/10.1016/S1470-2045(15)00613-0 — PMID 26947331 **Errata:** PMIDs 27300673, 27733295.
- (OS) Turner, N. C., Slamon, D. J., Ro, J., Bondarenko, I., Im, S.-A., Masuda, N., Colleoni, M., DeMichele, A., Loi, S., Verma, S., Iwata, H., Harbeck, N., Loibl, S., André, F., Puyana Theall, K., Huang, X., Giorgetti, C., Huang Bartlett, C., & Cristofanilli, M. (2018). Overall survival with palbociclib and fulvestrant in advanced breast cancer. *The New England Journal of Medicine*, *379*(20), 1926–1936. https://doi.org/10.1056/NEJMoa1810527 — PMID 30345905
- (Updated OS) Cristofanilli, M., Rugo, H. S., Im, S.-A., Slamon, D. J., Harbeck, N., Bondarenko, I., Masuda, N., Colleoni, M., DeMichele, A., Loi, S., Iwata, H., O'Leary, B., André, F., Loibl, S., Bananis, E., Liu, Y., Huang, X., Kim, S., Lechuga Frean, M. J., & Turner, N. C. (2022). Overall survival with palbociclib and fulvestrant in women with HR+/HER2- ABC: Updated exploratory analyses of PALOMA-3, a double-blind, phase III randomized study. *Clinical Cancer Research*, *28*(16), 3433–3442. https://doi.org/10.1158/1078-0432.CCR-22-0305 — PMID 35552673 (PMC9662922)

**Design:** Phase 3, double-blind, randomized 2:1; 144 centres in 17 countries [A].
**Population:** 521 women of any menopausal status with HR+/HER2− MBC that had relapsed or progressed on prior ET. Premenopausal and perimenopausal women also received goserelin [A].
**Arms:** Palbociclib 125 mg daily (3 weeks on / 1 off) + fulvestrant 500 mg (days 1 and 15 of cycle 1, then every 28 days) vs placebo + fulvestrant [A].
**Primary endpoint (investigator PFS):**
- Interim: 9.2 (7.5–NE) vs 3.8 (3.5–5.5) months, HR 0.42 (0.32–0.56) [A].
- Final: **9.5 (9.2–11.0) vs 4.6 (3.5–5.6), HR 0.46 (0.36–0.59)** [A].
- Benefit did not depend on PIK3CA status or HR expression level [A].
**OS:**
- 2018: 34.9 (28.8–40.0) vs 28.0 (23.6–34.6) months, HR 0.81 (0.64–1.03), **P = 0.09, not significant**.
- Endocrine-sensitive subgroup (n = 410): 39.7 vs 29.7 months, HR 0.72 (0.55–0.94).
- Time to chemotherapy 17.6 vs 8.8 months [A].
- 2022 exploratory update (73.3 months of follow-up): 34.8 vs 28.0 months, HR 0.81 (0.65–0.99); 6-year OS 19.1% vs 12.9% [A].
**Toxicity:**
- Grade 3–4 neutropenia 65% vs 1%; leukopenia 28% vs 1% [A, final].
- FN 0.6% in both arms [A, primary].

---

## A6. SOLAR-1 (alpelisib + fulvestrant, PIK3CA-mutated) — [VERIFIED]

**References**
- André, F., Ciruelos, E., Rubovszky, G., Campone, M., Loibl, S., Rugo, H. S., Iwata, H., Conte, P., Mayer, I. A., Kaufman, B., Yamashita, T., Lu, Y.-S., Inoue, K., Takahashi, M., Pápai, Z., Longin, A.-S., Mills, D., Wilke, C., Hirawat, S., & Juric, D. (2019). Alpelisib for PIK3CA-mutated, hormone receptor-positive advanced breast cancer. *The New England Journal of Medicine*, *380*(20), 1929–1940. https://doi.org/10.1056/NEJMoa1813904 — PMID 31091374
- (Final OS) André, F., Ciruelos, E. M., Juric, D., Loibl, S., Campone, M., Mayer, I. A., Rubovszky, G., Yamashita, T., Kaufman, B., Lu, Y.-S., Inoue, K., Pápai, Z., Takahashi, M., Ghaznawi, F., Mills, D., Kaper, M., Miller, M., Conte, P. F., Iwata, H., & Rugo, H. S. (2021). Alpelisib plus fulvestrant for PIK3CA-mutated, hormone receptor-positive, human epidermal growth factor receptor-2-negative advanced breast cancer: Final overall survival results from SOLAR-1. *Annals of Oncology*, *32*(2), 208–217. https://doi.org/10.1016/j.annonc.2020.11.011 — PMID 33246021
- (AE management) Rugo, H. S., André, F., Yamashita, T., Cerda, H., Toledano, I., Stemmer, S. M., Jurado, J. C., Juric, D., Mayer, I., Ciruelos, E. M., Iwata, H., Conte, P., Campone, M., Wilke, C., Mills, D., Lteif, A., Miller, M., Gaudenzi, F., & Loibl, S. (2020). Time course and management of key adverse events during the randomized phase III SOLAR-1 study of PI3K inhibitor alpelisib plus fulvestrant in patients with HR-positive advanced breast cancer. *Annals of Oncology*, *31*(8), 1001–1010. https://doi.org/10.1016/j.annonc.2020.05.001 — PMID 32416251

**Design:** Phase 3, randomized 1:1. There were two cohorts by tumour-tissue PIK3CA status [A].
**Population:** 572 men and postmenopausal women with HR+/HER2− ABC after ET (after an AI, per the OS paper). 341 had tissue-confirmed PIK3CA mutations [A].
**Arms:** Alpelisib 300 mg/day + fulvestrant 500 mg vs placebo + fulvestrant [A].
**Primary endpoint (investigator PFS, PIK3CA-mutant cohort):**
- **11.0 (7.5–14.5) vs 5.7 (3.7–7.4) months, HR 0.65 (0.50–0.85), P < 0.001.**
- PIK3CA-non-mutant cohort: HR 0.85 (0.58–1.25); proof-of-concept only [A].
**Final OS (André 2021):**
- 39.3 (34.1–44.9) vs 31.4 (26.8–41.3) months, HR 0.86 (0.64–1.15), P = 0.15. **Did not cross the boundary (P ≤ 0.0161).**
- Lung and/or liver metastases: 37.2 vs 22.8 months, HR 0.68 (0.46–1.00) [A].
**Toxicity:**
- Grade 3–4 hyperglycemia 36.6% vs 0.7% (grade 3 32.7%, grade 4 3.9%).
- Grade 3 rash 9.9%; grade 3 diarrhea 6.7%.
- Discontinuation 25.0% vs 4.2% [A].
- Timing: median time to grade ≥3 hyperglycemia 15 days, rash 13 days, diarrhea 139 days [A, Rugo 2020].
- Prevention: metformin was used in 87.1% of patients with hyperglycemia. Prophylactic anti-rash medication cut any-grade rash from 64.1% to 26.7% [A, Rugo 2020].
- Label:
  - Hyperglycemia 65%; ketoacidosis 0.7%. Fatal ketoacidosis has been reported post-marketing.
  - Diarrhea 58% (grade 3 7%).
  - Pneumonitis 1.8%; SJS 0.4%; EM 1.1% [L-Piqray 2025-12-15].
- Testing: tissue or plasma; if plasma is negative, test tissue [L].

---

## A7. CAPItello-291 (capivasertib + fulvestrant) — [VERIFIED] (final OS not found)

**References**
- Turner, N. C., Oliveira, M., Howell, S. J., Dalenc, F., Cortes, J., Gomez Moreno, H. L., Hu, X., Jhaveri, K., Krivorotko, P., Loibl, S., Morales Murillo, S., Okera, M., Park, Y. H., Sohn, J., Toi, M., Tokunaga, E., Yousef, S., Zhukova, L., de Bruin, E. C., . . . Rugo, H. S. (2023). Capivasertib in hormone receptor-positive advanced breast cancer. *The New England Journal of Medicine*, *388*(22), 2058–2070. https://doi.org/10.1056/NEJMoa2214131 — PMID 37256976 (PMC11335038)
- (AE characterization) Rugo, H. S., Oliveira, M., Howell, S. J., Dalenc, F., Cortes, J., Gomez, H. L., Hu, X., Jhaveri, K. L., Krivorotko, P., Loibl, S., Morales Murillo, S., Nowecki, Z., Okera, M., Park, Y. H., Sohn, J., Toi, M., Iwata, H., Yousef, S., Zhukova, L., . . . Turner, N. C. (2024). Capivasertib and fulvestrant for patients with hormone receptor-positive advanced breast cancer: Characterization, time course, and management of frequent adverse events from the phase III CAPItello-291 study. *ESMO Open*, *9*(9), Article 103697. https://doi.org/10.1016/j.esmoop.2024.103697 — PMID 39241495 (PMC11406080)

**Design:** Phase 3, double-blind, randomized 1:1 [A].
**Population:** 708 pre-, peri- and postmenopausal women and men with HR+/HER2− ABC. Disease had relapsed or progressed during or after an AI, with or without a prior CDK4/6i.
- 69.1% had a prior CDK4/6i for advanced disease.
- 40.8% (289) had AKT-pathway-altered tumours (PIK3CA, AKT1 or PTEN) [A].
- Excluded: type 1 diabetes, type 2 diabetes requiring insulin, or HbA1c ≥8% [L-Truqap 2026-06-12].
**Arms:** Capivasertib 400 mg twice daily, **4 days on / 3 days off**, + fulvestrant vs placebo + fulvestrant [A, AE paper].
**Dual primary endpoint (investigator PFS):**
- Overall: **7.2 vs 3.6 months, HR 0.60 (0.51–0.71)**.
- AKT-altered: **7.3 (5.5–9.0) vs 3.1 (2.0–3.7), HR 0.50 (0.38–0.65)** [A; median CIs from L].
- Non-altered (exploratory): HR 0.79 (0.61–1.02) [L].
**OS:** Immature at the primary analysis.
- 18-month OS 73.9% vs 65.0%, HR 0.74 (0.56–0.98) overall.
- Altered subgroup HR 0.69 (0.45–1.05) [FT].
- **Final OS: not found on PubMed [UNVERIFIED].**
**Toxicity:**
- Any grade: diarrhea 72.4%; rash (grouped) 38.0%; nausea 34.6%; hyperglycemia (AE term) 16.3% [FT].
- Grade ≥3: rash 12.1%; diarrhea 9.3%; hyperglycemia 2.3% [A].
- Median onset: diarrhea 8 days; rash 12 days; hyperglycemia 15 days [A, AE paper].
- Discontinuation for AEs 13.0% vs 2.3% [A].
- Label, lab-based: increased fasting glucose 37% (grade 2 11%, grade 3 2%, grade 4 1.1%). DKA 0.3%. Cutaneous reactions 58% (grade 3–4 17%); EM 1.7%; DRESS 0.3% [L].
- Monitoring [L]:
  - Fasting glucose on day 3 or 4 of the dosing week at weeks 1, 2, 4, 6 and 8, then monthly.
  - HbA1c every 3 months.
- Testing: tumour tissue only [L].

---

## A8. EMERALD (elacestrant, ESR1-mutant) — [VERIFIED]

**References**
- Bidard, F.-C., Kaklamani, V. G., Neven, P., Streich, G., Montero, A. J., Forget, F., Mouret-Reynier, M.-A., Sohn, J. H., Taylor, D., Harnden, K. K., Khong, H., Kocsis, J., Dalenc, F., Dillon, P. M., Babu, S., Waters, S., Deleu, I., García Sáenz, J. A., Bria, E., . . . Bardia, A. (2022). Elacestrant (oral selective estrogen receptor degrader) versus standard endocrine therapy for estrogen receptor-positive, human epidermal growth factor receptor 2-negative advanced breast cancer: Results from the randomized phase III EMERALD trial. *Journal of Clinical Oncology*, *40*(28), 3246–3256. https://doi.org/10.1200/JCO.22.00338 — PMID 35584336 (PMC9553388) **Erratum:** *J Clin Oncol 41*(23), 3962 (2023), PMID 37364222.

**Design:** Phase 3, open-label, randomized [A].
**Population:** 477 patients with ER+/HER2− ABC (label: 478 enrolled) [A, L].
- Inclusion: 1–2 prior lines of ET; **prior CDK4/6i required**; ≤1 prior chemotherapy line.
- ESR1 mutation detected in 47.8% (228) by ctDNA (Guardant360 CDx).
- 43.4% had 2 prior ET lines [A, L].
**Arms:** Elacestrant 400 mg once daily (= 345 mg free base; see flag 5) vs standard-of-care ET: fulvestrant (n = 166) or an AI (n = 73) [A, L].
**Primary endpoints (BICR PFS):**
- All patients: HR 0.70 (0.55–0.88), P = .002.
- **ESR1-mutant: 3.8 (2.2–7.3) vs 1.9 (1.9–2.1) months, HR 0.55 (0.39–0.77), P = .0005** [A; medians from L-Orserdu 2026-06-24].
- 12-month PFS: 22.3% vs 9.4% (all); 26.8% vs 8.2% (ESR1-mutant) [FT].
- All-patient median PFS 2.8 vs 1.9 months is reported only in a sensitivity analysis [FT]. The main all-patient medians are **[UNVERIFIED]**.
**OS:**
- Interim, ESR1-mutant: HR 0.59 (0.36–0.96), not significant [FT].
- **Label (later analysis), ESR1-mutant: HR 0.90 (0.63–1.30), NS** [L].
**Toxicity:**
- Nausea 35.0% vs 18.8% (grade 3–4 2.5% vs 0.9%); vomiting 19.0% vs 8.3%.
- Treatment-related grade 3–4 AEs 7.2% vs 3.1% [A, FT].
- Label: hypercholesterolemia 30%, hypertriglyceridemia 27%; check lipids at baseline and periodically [L].
**Taiwan:** no active TFDA licence [TFDA].

---

## A9. INAVO120 (inavolisib + palbociclib + fulvestrant; OS) — [VERIFIED]

**References**
- Turner, N. C., Im, S.-A., Saura, C., Juric, D., Loibl, S., Kalinsky, K., Schmid, P., Loi, S., Sunpaweravong, P., Musolino, A., Li, H., Zhang, Q., Nowecki, Z., Leung, R., Thanopoulou, E., Shankar, N., Lei, G., Stout, T. J., Hutchinson, K. E., . . . Jhaveri, K. L. (2024). Inavolisib-based therapy in PIK3CA-mutated advanced breast cancer. *The New England Journal of Medicine*, *391*(17), 1584–1596. https://doi.org/10.1056/NEJMoa2404625 — PMID 39476340
- (Final OS) Jhaveri, K. L., Im, S.-A., Saura, C., Loibl, S., Kalinsky, K., Schmid, P., Loi, S., Thanopoulou, E., Shankar, N., Jin, Y., Stout, T. J., Clark, T. D., Song, C., Juric, D., & Turner, N. C. (2025). Overall survival with inavolisib in PIK3CA-mutated advanced breast cancer. *The New England Journal of Medicine*, *393*(2), 151–161. https://doi.org/10.1056/NEJMoa2501796 — PMID 40454641 (PMC13496148)
- (Safety) Im, S.-A., Kalinsky, K., Jhaveri, K. L., Loibl, S., Turner, N., Saura, C., Schmid, P., Loi, S., Hamilton, E., Karadurmus, N., Wang, S., Awan, A. A., Ciruelos, E. M., Chung, C.-F., Thanopoulou, E., Shankar, N., Lim, S., Jin, Y., Song, C., & Juric, D. (2026). Safety analyses of the INAVO120 randomised phase III trial of inavolisib or placebo with palbociclib-fulvestrant in patients with PIK3CA-mutated, hormone receptor-positive, HER2-negative, endocrine-resistant advanced breast cancer. *ESMO Open*, *11*(6), Article 107735. https://doi.org/10.1016/j.esmoop.2026.107735 — PMID 42202490 (PMC13235453)

**Design:** Phase 3, double-blind, randomized [A].
**Population:** 325 patients (161 vs 164) with PIK3CA-mutated HR+/HER2− ABC that relapsed during or within 12 months of completing adjuvant ET (endocrine-resistant). This was first-line therapy for advanced disease [A].
- Eligibility required fasting glucose <126 mg/dL and HbA1c <6.0%; the cut-off was amended from <5.7% [FT, safety paper].
- PIK3CA tested on plasma [L-Itovebi 2026-04-21].
**Arms:** Inavolisib 9 mg once daily + palbociclib 125 mg (days 1–21) + fulvestrant 500 mg vs placebo + palbociclib + fulvestrant [A, safety paper].
**Primary endpoint (investigator PFS):** **15.0 (11.3–20.5) vs 7.3 (5.6–9.3) months, HR 0.43 (0.32–0.59), P < 0.001.** ORR 58.4% vs 25.0% [A].
**Final OS (Jhaveri 2025):**
- **34.0 (28.4–44.8) vs 27.0 (22.8–38.7) months, HR 0.67 (0.48–0.94), P = 0.02** (boundary P < 0.0469). Significant [A].
- Updated PFS HR 0.42 (0.32–0.55); ORR 62.7% vs 28.0% [A].
- Second-line chemotherapy after progression: 55% vs 72% [FT].
**Toxicity:**
- Any grade (OS paper): hyperglycemia 63.4% vs 13.5% (grade 3–4 6.8%); stomatitis/mucositis 55.3% vs 28.8%; diarrhea 52.2% vs 16.0%; rash 26.7% vs 19.6%; ocular toxicity 29.2% vs 16.0% [FT].
- Grade 3–4 neutropenia ~80% in both arms (palbociclib effect) [A].
- Discontinuation of inavolisib 6.8% vs 0.6% [A].
- Safety paper:
  - Median time to hyperglycemia onset 7 days.
  - Metformin was the most common treatment.
  - No DKA.
  - No prediabetic patient stopped for hyperglycemia [A, FT].
- Label (lab-based): increased fasting glucose 85% (grade 3 12%, grade 4 0.6%); 46% received oral antihyperglycemics and 7% insulin [L].

---

## A10. SERENA-6 (camizestrant switch at ESR1 emergence; 2025) — [VERIFIED]

**References**
- Bidard, F.-C., Mayer, E. L., Park, Y. H., Janni, W., Ma, C., Cristofanilli, M., Bianchini, G., Kalinsky, K., Iwata, H., Chia, S., Fasching, P. A., Brufsky, A., Nowecki, Z., Pascual, J., Moreau, L., Chen, S.-C., Karadurmus, N., Gal-Yam, E. N., Jung, K. H., . . . Turner, N. C. (2025). First-line camizestrant for emerging ESR1-mutated advanced breast cancer. *The New England Journal of Medicine*, *393*(6), 569–580. https://doi.org/10.1056/NEJMoa2502929 — PMID 40454637
- (Extended analysis) Turner, N. C., Mayer, E. L., Park, Y. H., Janni, W., Ma, C., Cristofanilli, M., Bianchini, G., Kalinsky, K., Iwata, H., Chia, S., Brufsky, A. M., Fasching, P. A., Nowecki, Z., Pascual, J., Karadurmus, N., Gal-Yam, E., Chung, W.-P., Im, S.-A., Zambelli, A., . . . Bidard, F.-C. (2026). Switching to camizestrant at ESR1 mutation emergence before disease progression during first-line treatment of hormone receptor-positive advanced breast cancer (SERENA-6): Extended analysis of a double-blind, placebo-controlled, randomised, phase 3 trial. *The Lancet Oncology*, *27*(8), 941–958. https://doi.org/10.1016/S1470-2045(26)00287-1 — PMID 42442380

**Design:** Phase 3, double-blind, placebo-controlled (double-dummy); 264 centres in 23 countries [A].
**Population:**
- Patients on first-line AI + CDK4/6i (palbociclib, ribociclib or abemaciclib) for ≥6 months had ctDNA ESR1 testing every 2–3 months (Guardant360 CDx).
- 3256 were tested and 548 had an ESR1 mutation.
- **315 with ESR1 mutation and no radiological progression were randomized (157 vs 158).** 23% were Asian [A].
**Arms:** Switch to camizestrant 75 mg daily + continue the same CDK4/6i vs continue AI + CDK4/6i [A].
**Primary endpoint (investigator PFS), interim (12.6 months of follow-up):**
- **16.0 (12.7–18.2) vs 9.2 (7.2–9.5) months, HR 0.44 (0.31–0.60), P < 0.0001.**
- Time to deterioration of global QoL: 21.0 vs 6.4 months, HR 0.54 (0.34–0.84) [A].
**Extended analysis (cutoff 2026-01-02, median follow-up 23.5 months):**
- PFS 16.8 (14.7–19.4) vs 9.2 (7.2–9.7) months, HR 0.45 (0.34–0.59) (descriptive).
- **PFS2 25.7 (20.4–30.3) vs 19.1 (16.8–21.0) months, HR 0.63 (0.46–0.86), p = 0.0037** [A].
- OS immature (12% maturity) [L-Etcamah 2026-09-04].
**Toxicity:**
- Discontinuation for AEs 1.3% vs 1.9% [A].
- Grade 3–4 neutropenia 27% vs 17% [A, extended].
- One sudden death, possibly related to camizestrant [A, extended].
- Label:
  - **Bradycardia 8%** (mean HR fall ~13 bpm, maximum at day 15).
  - QTc prolongation 2.6%.
  - **Visual disturbances (photopsia, blurred vision, etc.) 34% vs 16%** (grade 3–4 0.6% vs 0).
  - **Boxed warning:** Torsades/sudden-death risk with ribociclib or other QTc-prolonging drugs. ECG at baseline, then weekly for 2 weeks [L].
**Regulatory:**
- US: accelerated approval, combined with abemaciclib, palbociclib or ribociclib [L].
- Taiwan: no TFDA licence [TFDA].

---

## A11. EMBER-3 (imlunestrant ± abemaciclib) — [VERIFIED]

**References**
- Jhaveri, K. L., Neven, P., Casalnuovo, M. L., Kim, S.-B., Tokunaga, E., Aftimos, P., Saura, C., O'Shaughnessy, J., Harbeck, N., Carey, L. A., Curigliano, G., Llombart-Cussac, A., Lim, E., García Tinoco, M. D. L. L., Sohn, J., Mattar, A., Zhang, Q., Huang, C.-S., Hung, C.-C., . . . Bidard, F.-C. (2025). Imlunestrant with or without abemaciclib in advanced breast cancer. *The New England Journal of Medicine*, *392*(12), 1189–1202. https://doi.org/10.1056/NEJMoa2410858 — PMID 39660834 (PMC13674379)
- (Updated efficacy, interim OS) Jhaveri, K. L., Neven, P., Casalnuovo, M. L., Kim, S.-B., Tokunaga, E., Aftimos, P., Saura, C., O'Shaughnessy, J., Harbeck, N., Carey, L. A., Curigliano, G., Watanabe, J., Lim, E., Huang, J., Qingyuan, Z. [sic], Llombart-Cussac, A., Huang, C., Desai, B., Limay, Y., . . . Bidard, F. C. (2026). Imlunestrant with or without abemaciclib in advanced breast cancer: Updated efficacy results from the phase III EMBER-3 trial. *Annals of Oncology*, *37*(4), 532–543. https://doi.org/10.1016/j.annonc.2025.11.018 — PMID 41391667 (PMC13485152)

**Design:** Phase 3, open-label. Randomization was 1:1, then amended to 1:1:1 [A, FT].
**Population:** 874 patients with ER+/HER2− ABC that recurred or progressed during or after an AI ± CDK4/6i [A].
- 59.8% had a prior CDK4/6i.
- ESR1 mutation in 256 patients (38.7% of the imlunestrant + SOC arms) [FT].
**Arms:** n = 331 vs 330 vs 213 [A, FT].
- Imlunestrant 400 mg daily.
- SOC: exemestane 25 mg or fulvestrant 500 mg.
- Imlunestrant + abemaciclib 150 mg twice daily.
**Primary endpoints (investigator PFS):**
- **ESR1-mutant, imlunestrant vs SOC: 5.5 (3.9–7.4) vs 3.8 (3.7–5.5) months.** The hazards were non-proportional, so the paper uses RMST at 19.4 months: 7.9 vs 5.4 months (difference 2.6), P < 0.001 [A, FT]. The label gives **HR 0.62 (0.46–0.82)**, p = 0.0008 [L-Inluriyo 2026-06-04].
- All patients, imlunestrant vs SOC: 5.6 vs 5.5 months, HR 0.87 (0.72–1.04), P = 0.12. **Not met** [A].
- Imlunestrant + abemaciclib vs imlunestrant (all concurrently randomized, n = 426): **9.4 (7.5–11.9) vs 5.5 (3.8–5.6) months, HR 0.57 (0.44–0.73)**, regardless of ESR1 status [A, FT].
**Updated analysis (cutoff 2025-08-18, 28.5 months of follow-up):**
- ESR1-mutant OS: 34.5 vs 23.1 months, HR 0.60 (0.43–0.86), P = 0.0043. The significance boundary was **not reached** [A].
- Combination vs imlunestrant: PFS 10.9 vs 5.5 months, HR 0.59 (0.47–0.74); OS NR vs 34.4 months, HR 0.82 (0.59–1.16) [A].
**Toxicity:**
- Grade ≥3 AEs: imlunestrant 17.1%; SOC 20.7%; combination 48.6% [A].
- Imlunestrant: fatigue 22.6%, diarrhea 21.4%, nausea 17.1% (mostly grade 1); bradycardia 2.1%; no photopsia [FT].
- Combination: diarrhea 86.1% (grade ≥3 8.2%); grade ≥3 neutropenia 19.7% [FT].
- Post hoc: 12-month CNS progression 1.5% vs 6.7% in ESR1-mutant patients [FT].
**Regulatory:**
- US: monotherapy for ESR1-mutated disease, 400 mg on an empty stomach [L].
- **Taiwan: Inluriyo 200 mg licensed 2026-05-15** (衛部藥輸字第029131號), for ESR1-mutated disease after ≥1 line of ET [TFDA].

---

## A12. VERITAC-2 (vepdegestrant, a PROTAC ER degrader) — [VERIFIED]

**References**
- Campone, M., De Laurentiis, M., Jhaveri, K., Hu, X., Ladoire, S., Patsouris, A., Zamagni, C., Cui, J., Cazzaniga, M., Cil, T., Jerzak, K. J., Fuentes, C., Yoshinami, T., Rodriguez-Lescure, A., Sezer, A., Fontana, A., Guarneri, V., Molckovsky, A., Mouret-Reynier, M.-A., . . . Hamilton, E. P. (2025). Vepdegestrant, a PROTAC estrogen receptor degrader, in advanced breast cancer. *The New England Journal of Medicine*, *393*(6), 556–568. https://doi.org/10.1056/NEJMoa2505725 — PMID 40454645

**Design:** Phase 3, open-label, randomized 1:1, stratified by ESR1 status and visceral disease [A].
**Population:** 624 patients with ER+/HER2− ABC after **one prior CDK4/6i + ET line** (up to one more ET line allowed). 270 were ESR1-mutant [A].
**Arms:** Vepdegestrant 200 mg once daily vs fulvestrant 500 mg (n = 313 vs 311) [A].
**Primary endpoints (BICR PFS):**
- **ESR1-mutant: 5.0 (3.7–7.4) vs 2.1 (1.9–3.5) months, HR 0.58 (0.43–0.78), P < 0.001.** The label gives HR 0.57 (0.42–0.77); ORR 19% vs 4% [A, L-Veppanu 2026-06-12].
- All patients: 3.8 vs 3.6 months, HR 0.83 (0.69–1.01), P = 0.07. **Not met** [A].
**OS:** Not reported **[UNVERIFIED]**.
**Toxicity:**
- Grade ≥3 AEs 23.4% vs 17.6%; discontinuation 2.9% vs 0.7% [A].
- Label: **QTc prolongation 10%** (grade 3 1.6%; QTcF >500 ms 1.6%). Do an ECG and check electrolytes before starting [L].
**Taiwan:** no TFDA licence [TFDA].

---

## A13. postMONARCH (abemaciclib + fulvestrant after a CDK4/6i) — [VERIFIED]

**References**
- Kalinsky, K., Bianchini, G., Hamilton, E., Graff, S. L., Park, K. H., Jeselsohn, R., Demirci, U., Martin, M., Layman, R. M., Hurvitz, S. A., Sammons, S., Kaufman, P. A., Muñoz, M., Lai, J.-I., Knoderer, H., Sandoval, C., Chawla, A. R., Nguyen, B., Zhou, Y., . . . Wander, S. A. (2025). Abemaciclib plus fulvestrant in advanced breast cancer after progression on CDK4/6 inhibition: Results from the phase III postMONARCH trial. *Journal of Clinical Oncology*, *43*(9), 1101–1112. https://doi.org/10.1200/JCO-24-02086 — PMID 39693591 (PMC11936477)
- (Final OS) Kalinsky, K., Wander, S. A., Hamilton, E., Graff, S. L., Jeselsohn, R., Park, K. H., Demirci, U., Martin, M., Layman, R. M., Hurvitz, S. A., Sammons, S., Kaufman, P. A., Ravenberg, E., Amdur, S., Litchfield, L. M., & Bianchini, G. (2026). Overall survival from the phase III postMONARCH trial of abemaciclib plus fulvestrant versus placebo plus fulvestrant for HR+, HER2- advanced breast cancer following progression on a prior CDK4/6 inhibitor plus endocrine therapy. *Annals of Oncology*. Advance online publication. https://doi.org/10.1016/j.annonc.2026.10.1283 — PMID 42926108

**Design:** Phase 3, double-blind, randomized 1:1 [A].
**Population:** 368 patients [A, FT].
- Progression on first-line CDK4/6i + AI, or recurrence on or after adjuvant CDK4/6i + ET.
- Prior CDK4/6i: palbociclib 59%, ribociclib 33%, abemaciclib 7.6%.
**Arms:** Abemaciclib 150 mg twice daily + fulvestrant 500 mg vs placebo + fulvestrant (n = 182 vs 186) [A, FT].
**Primary endpoint (investigator PFS):**
- **HR 0.73 (0.57–0.95); median 6.0 (5.6–8.6) vs 5.3 (3.7–5.6) months.**
- 6-month PFS 50% vs 37%. BICR HR 0.55 (0.39–0.77). ORR 17% vs 7% [A].
**Final OS (Ann Oncol, e-pub October 2026):** 32.1 vs 24.6 months, HR 0.80 (0.60–1.06), P = 0.11. **Not significant** (boundary HR 0.753). Updated PFS HR 0.78 (0.62–0.99) [A].
**Toxicity:**
- Grade ≥3 AEs 55% vs 20%.
- Diarrhea 74.6% (grade ≥3 3.9%).
- Neutropenia 40.9% (grade ≥3 24.9%).
- Dose reductions 30% vs 3% [FT].

---

# B. Antibody–drug conjugates

## B1. DESTINY-Breast04 (T-DXd, HER2-low) — [VERIFIED]

**References**
- Modi, S., Jacot, W., Yamashita, T., Sohn, J., Vidal, M., Tokunaga, E., Tsurutani, J., Ueno, N. T., Prat, A., Chae, Y. S., Lee, K. S., Niikura, N., Park, Y. H., Xu, B., Wang, X., Gil-Gil, M., Li, W., Pierga, J.-Y., Im, S.-A., . . . Cameron, D. A. (2022). Trastuzumab deruxtecan in previously treated HER2-low advanced breast cancer. *The New England Journal of Medicine*, *387*(1), 9–20. https://doi.org/10.1056/NEJMoa2203690 — PMID 35665782 (PMC10561652)
- (Long-term survival) Modi, S., Jacot, W., Iwata, H., Park, Y. H., Vidal Losada, M., Li, W., Tsurutani, J., Ueno, N. T., Zaman, K., Prat, A., Papazisis, K., Rugo, H. S., Yamashita, T., Harbeck, N., Im, S.-A., De Laurentiis, M., Pierga, J.-Y., Wang, X., Gombos, A., . . . Cameron, D. (2025). Trastuzumab deruxtecan in HER2-low metastatic breast cancer: Long-term survival analysis of the randomized, phase 3 DESTINY-Breast04 trial. *Nature Medicine*, *31*(12), 4205–4213. https://doi.org/10.1038/s41591-025-03981-4 — PMID 41062831 (PMC12705423)

**Design:** Phase 3, open-label, randomized 2:1 [A].
**Population:** 557 patients with HER2-low MBC (IHC 1+, or IHC 2+/ISH−): 494 HR+ and 63 HR− [A].
- 1–2 prior chemotherapy lines for MBC, or recurrence ≤6 months after adjuvant chemotherapy.
- HR+ patients had to have had ≥1 ET line [FT].
**Arms:** T-DXd 5.4 mg/kg every 3 weeks vs physician's choice (capecitabine, eribulin, gemcitabine, paclitaxel or nab-paclitaxel; eribulin 51.1%) [FT].
**Primary endpoint (BICR PFS, HR+ cohort):** **10.1 (9.5–11.5) vs 5.4 (4.4–7.1) months, HR 0.51 (0.40–0.64), P < 0.001** [FT].
**Key secondary endpoints:**
- All patients: PFS 9.9 vs 5.1 months, HR 0.50 (0.40–0.63).
- OS, HR+ cohort: **23.9 (20.8–24.8) vs 17.5 (15.2–22.4) months, HR 0.64 (0.48–0.86), P = 0.003.**
- OS, all patients: 23.4 vs 16.8 months, HR 0.64 (0.49–0.84) [A, FT].
- HR− cohort (exploratory): PFS 8.5 vs 2.9 months, HR 0.46 (0.24–0.89); OS 18.2 vs 8.3 months [FT].
- ORR (HR+): 52.6% vs 16.3% [FT].
**Long-term analysis (Modi 2025; median follow-up 32.0 months):**
- OS, all patients: 22.9 (21.2–24.5) vs 16.8 (14.1–19.5) months, HR 0.69 (0.55–0.86).
- OS, HR+: 23.9 vs 17.6 months, HR 0.69 (0.55–0.87).
- OS, HR−: 17.1 vs 8.3 months, HR 0.58 (0.31–1.08) [A, FT].
**Toxicity:**
- Grade ≥3 AEs 52.6% vs 67.4%.
- **Adjudicated drug-related ILD 12.1%** (grade 1 3.5%, grade 2 6.5%, grade 3 1.3%, grade 5 0.8%) [A, FT].
- Long-term: no new ILD cases. Grade 5 now 4 patients (1.1%); median onset 129 days [FT].
- Left ventricular dysfunction 4.6% (5.1% long-term) [FT].
- Nausea 73–76% (drug-related) [FT]. T-DXd is classed as **highly emetogenic** in the paper's discussion, citing NCCN antiemesis [FT].

---

## B2. DESTINY-Breast06 (T-DXd, HER2-low and HER2-ultralow, chemo-naive) — [VERIFIED] (OS immature)

**References**
- Bardia, A., Hu, X., Dent, R., Yonemori, K., Barrios, C. H., O'Shaughnessy, J. A., Wildiers, H., Pierga, J.-Y., Zhang, Q., Saura, C., Biganzoli, L., Sohn, J., Im, S.-A., Lévy, C., Jacot, W., Begbie, N., Ke, J., Patel, G., & Curigliano, G. (2024). Trastuzumab deruxtecan after endocrine therapy in metastatic breast cancer. *The New England Journal of Medicine*, *391*(22), 2110–2122. https://doi.org/10.1056/NEJMoa2407086 — PMID 39282896
- (Subgroups by time to progression on first-line ET + CDK4/6i) Curigliano, G., Hu, X., Dent, R., Yonemori, K., Barrios, C. H., Pierga, J.-Y., Puglisi, F., Ferrero, J.-M., Jung, K. H., Bagegni, N. A., Collignon, J., Gil-Gil, M., Wu, X., Andrzejuk-Ćwik, A., Schwaederle, M., Anand, S., & Bardia, A. (2026). Trastuzumab deruxtecan in hormone receptor-positive, HER2-low/-ultralow metastatic breast cancer (DESTINY-Breast06): Outcome analyses by time to progression on prior first-line endocrine therapy with CDK4/6 inhibitor and baseline burden of disease. *Annals of Oncology*, *37*(6), 849–860. https://doi.org/10.1016/j.annonc.2026.02.015 — PMID 41780642

**Design:** Phase 3, multicentre, open-label, randomized 1:1 [A].
**Population:** 866 patients with HR+ MBC: 713 HER2-low and 153 **HER2-ultralow** (IHC 0 with membrane staining in >0 and ≤10% of cells) [A, L].
- ≥1 line of endocrine-based therapy and **no prior chemotherapy for MBC**.
- Label eligibility: ≥2 ET lines, or 1 line plus either progression within 24 months of starting adjuvant ET or progression within 6 months of first-line ET + CDK4/6i.
- 89% had a prior CDK4/6i in the metastatic setting [L-Enhertu 2026-05-15].
**Arms:** T-DXd 5.4 mg/kg every 3 weeks vs chemotherapy (capecitabine 60%, nab-paclitaxel 24%, paclitaxel 16%) [L].
**Primary endpoint (BICR PFS, HER2-low):**
- **13.2 (11.4–15.2) vs 8.1 (7.0–9.0) months, HR 0.62 (0.52–0.75), P < 0.001** [A].
- ITT: 13.2 vs 8.1 months, HR 0.64 (0.54–0.76) [L].
- HER2-ultralow (exploratory): 15.1 vs 8.3 months, HR 0.76 (0.49–1.17) [L].
- ORR (HER2-low): 62.0% vs 35.2% [L].
- Benefit held regardless of time to progression on first-line ET + CDK4/6i (<6, 6–12 and >12 months) [A, Curigliano 2026].
**OS:** Immature (39% of patients had died at the final PFS analysis) [L]. **No final OS paper on PubMed.**
**Toxicity:**
- Grade ≥3 AEs 52.8% vs 44.4%.
- **Adjudicated ILD 11.3% (49 patients; 3 grade 5) vs 0.2%** [A].
**Taiwan:** the TFDA Enhertu licence includes HER2弱陽性 (low) and HER2微陽性 (ultralow) HR+ MBC after ≥1 ET [TFDA].

---

## B3. TROPION-Breast01 (Dato-DXd, HR+/HER2−) — [VERIFIED] (OS medians [UNVERIFIED])

**References**
- Bardia, A., Jhaveri, K., Im, S.-A., Pernas, S., De Laurentiis, M., Wang, S., Martínez Jañez, N., Borges, G., Cescon, D. W., Hattori, M., Lu, Y.-S., Hamilton, E., Zhang, Q., Tsurutani, J., Kalinsky, K., Rubini Liedke, P. E., Xu, L., Fairhurst, R. M., Khan, S., . . . Pistilli, B. (2025). Datopotamab deruxtecan versus chemotherapy in previously treated inoperable/metastatic hormone receptor-positive human epidermal growth factor receptor 2-negative breast cancer: Primary results from TROPION-Breast01. *Journal of Clinical Oncology*, *43*(3), 285–296. https://doi.org/10.1200/JCO.24.00920 — PMID 39265124 (PMC11771365)
- (Final OS) Pistilli, B., Jhaveri, K., Im, S.-A., Pernas, S., De Laurentiis, M., Wang, S., Martínez Jañez, N., Borges, G., Cescon, D. W., Hattori, M., Lu, Y.-S., Hamilton, E., Tsurutani, J., Kalinsky, K., Rubini Liedke, P. E., Carroll, D., Khan, S., Rugo, H. S., Xu, B., & Bardia, A. (2026). Datopotamab deruxtecan versus chemotherapy in previously treated inoperable/metastatic hormone receptor-positive, HER2-negative breast cancer: Final overall survival analysis of the phase III TROPION-Breast01 study. *Annals of Oncology*, *37*(5), 663–674. https://doi.org/10.1016/j.annonc.2025.12.017 — PMID 41448362

**Design:** Phase 3, global, open-label, randomized 1:1. **Dual primary endpoints: BICR PFS and OS** [A].
**Population:** 732 patients with inoperable or metastatic HR+/HER2− breast cancer that had progressed on ET, for whom ET was unsuitable, and who had 1–2 prior chemotherapy lines [A].
**Arms:** Dato-DXd 6 mg/kg every 3 weeks vs ICC (eribulin, vinorelbine, capecitabine or gemcitabine); n = 365 vs 367 [A].
**PFS (BICR):** **6.9 (5.7–7.4) vs 4.9 (4.2–5.5) months, HR 0.63 (0.52–0.76), P < .0001.** ORR 36.4% vs 22.9% [A, FT].
**Final OS (Pistilli 2026):**
- **HR 1.01 (0.83–1.22), P = 0.9445. Not significant.**
- Subsequent ADC use was imbalanced: 12.3% vs 24.0% [A].
- Median OS values **[UNVERIFIED]** (not in the abstract; paper not in PMC).
**Toxicity:**
- Grade ≥3 treatment-related AEs 20.8% vs 44.7% [A].
- Nausea 51.1%.
- **Stomatitis 50% (grade ≥3 6.4%)** [A, FT].
- Dry eye 21.7%; keratitis 14.4%; any ocular surface event 40% (mostly grade 1) [FT].
- **Adjudicated ILD 3.3%** (12 patients; 1 grade 5) [FT].
- Label (pooled breast cancer, n = 841): ILD 3.0%, fatal 0.2% [L-Datroway 2026-05-27].
- Prevention [L]:
  - Steroid mouthwash prophylaxis; ice chips during the infusion.
  - Artificial tears; avoid contact lenses [FT].
**Taiwan:** the TFDA Datroway licence (2025-11-10) covers HR+/HER2− after ET and chemotherapy [TFDA].

---

## B4. TROPiCS-02 (sacituzumab govitecan, HR+/HER2−) — [VERIFIED]

**References**
- Rugo, H. S., Bardia, A., Marmé, F., Cortes, J., Schmid, P., Loirat, D., Trédan, O., Ciruelos, E., Dalenc, F., Gómez Pardo, P., Jhaveri, K. L., Delaney, R., Fu, O., Lin, L., Verret, W., & Tolaney, S. M. (2022). Sacituzumab govitecan in hormone receptor-positive/human epidermal growth factor receptor 2-negative metastatic breast cancer. *Journal of Clinical Oncology*, *40*(29), 3365–3376. https://doi.org/10.1200/JCO.22.01002 — PMID 36027558
- (OS) Rugo, H. S., Bardia, A., Marmé, F., Cortés, J., Schmid, P., Loirat, D., Trédan, O., Ciruelos, E., Dalenc, F., Gómez Pardo, P., Jhaveri, K. L., Delaney, R., Valdez, T., Wang, H., Motwani, M., Yoon, O. K., Verret, W., & Tolaney, S. M. (2023). Overall survival with sacituzumab govitecan in hormone receptor-positive and human epidermal growth factor receptor 2-negative metastatic breast cancer (TROPiCS-02): A randomised, open-label, multicentre, phase 3 trial. *The Lancet*, *402*(10411), 1423–1433. https://doi.org/10.1016/S0140-6736(23)01245-X — PMID 37633306

**Design:** Phase 3, global, open-label, randomized 1:1; 91 centres in North America and Europe [A].
**Population:** 543 patients with endocrine-resistant HR+/HER2− MBC [A].
- Prior ET, taxane and CDK4/6i, plus 2–4 prior chemotherapy lines for MBC.
- Median 3 prior chemotherapy lines; 95% had visceral metastases; 99% had a prior CDK4/6i.
**Arms:** SG 10 mg/kg on days 1 and 8 every 21 days [L-Trodelvy 2026-06-24] vs chemotherapy (eribulin, vinorelbine, capecitabine or gemcitabine); n = 272 vs 271 [A].
**Primary endpoint (BICR PFS):** **5.5 (4.2–7.0) vs 4.0 (3.1–4.4) months, HR 0.66 (0.53–0.83), P = .0003.** 12-month PFS 21% vs 7% [A].
**OS (protocol-specified final analysis; label calls it "second interim"):** **14.4 (13.0–15.7) vs 11.2 (10.1–12.7) months, HR 0.79 (0.65–0.96), p = 0.020.** ORR 21% vs 14% [A, L].
**Toxicity:**
- Grade ≥3 neutropenia 51% vs 38%; diarrhea 9% vs 1% [A].
- One fatal septic shock from neutropenic colitis [A].
- See F2 for SG nursing management.

---

# C. HER2-positive

## C1. CLEOPATRA (pertuzumab + trastuzumab + docetaxel, first line; final OS) — [VERIFIED]

**References**
- Baselga, J., Cortés, J., Kim, S.-B., Im, S.-A., Hegg, R., Im, Y.-H., Roman, L., Pedrini, J. L., Pienkowski, T., Knott, A., Clark, E., Benyunes, M. C., Ross, G., & Swain, S. M. (2012). Pertuzumab plus trastuzumab plus docetaxel for metastatic breast cancer. *The New England Journal of Medicine*, *366*(2), 109–119. https://doi.org/10.1056/NEJMoa1113216 — PMID 22149875 (PMC5705202)
- (Final OS) Swain, S. M., Baselga, J., Kim, S.-B., Ro, J., Semiglazov, V., Campone, M., Ciruelos, E., Ferrero, J.-M., Schneeweiss, A., Heeson, S., Clark, E., Ross, G., Benyunes, M. C., & Cortés, J. (2015). Pertuzumab, trastuzumab, and docetaxel in HER2-positive metastatic breast cancer. *The New England Journal of Medicine*, *372*(8), 724–734. https://doi.org/10.1056/NEJMoa1413513 — PMID 25693012 (PMC5584549)
- (End of study) Swain, S. M., Miles, D., Kim, S.-B., Im, Y.-H., Im, S.-A., Semiglazov, V., Ciruelos, E., Schneeweiss, A., Loi, S., Monturus, E., Clark, E., Knott, A., Restuccia, E., Benyunes, M. C., & Cortés, J. (2020). Pertuzumab, trastuzumab, and docetaxel for HER2-positive metastatic breast cancer (CLEOPATRA): End-of-study results from a double-blind, randomised, placebo-controlled, phase 3 study. *The Lancet Oncology*, *21*(4), 519–530. https://doi.org/10.1016/S1470-2045(19)30863-0 — PMID 32171426

**Design:** Phase 3, double-blind, randomized 1:1, placebo-controlled; 204 centres in 25 countries [A].
**Population:** 808 patients with HER2+ MBC, no prior chemotherapy or anti-HER2 therapy for metastatic disease [A].
**Arms:** Every 3 weeks, IV [A]:
- Pertuzumab 840 mg loading, then 420 mg (or placebo).
- Trastuzumab 8 mg/kg loading, then 6 mg/kg.
- Docetaxel 75 mg/m², escalated to 100 mg/m² if tolerated; ≥6 cycles.
**Primary endpoint (independent-review PFS):** **18.5 vs 12.4 months, HR 0.62 (0.51–0.75), P < 0.001** [A].
**OS:**
- 2015 final prespecified analysis: **56.5 (49.3–NR) vs 40.8 (35.8–48.3) months, HR 0.68 (0.56–0.84), P < 0.001.** Difference 15.7 months [A].
- End of study (2020; median follow-up 99.9 months): **57.1 (50–72) vs 40.8 (36–48) months, HR 0.69 (0.58–0.82); 8-year OS 37% vs 23%.** 50 patients crossed over (analysis not adjusted, so conservative) [A].
**Toxicity:**
- No increase in LV systolic dysfunction [A].
- Febrile neutropenia 13.8% vs 7.6%; grade ≥3 diarrhea 7.9% vs 5.0%; any-grade diarrhea 66.8% vs 46.3% [FT].
- Grade 3–4 neutropenia 49% vs 46%; treatment-related deaths 1% vs 2% [A, 2020].
- Perjeta boxed warning: LV dysfunction and embryo-fetal toxicity [L-Perjeta 2026-04-30].

---

## C2. DESTINY-Breast03 (T-DXd vs T-DM1; OS) — [VERIFIED]

**References**
- Cortés, J., Kim, S.-B., Chung, W.-P., Im, S.-A., Park, Y. H., Hegg, R., Kim, M. H., Tseng, L.-M., Petry, V., Chung, C.-F., Iwata, H., Hamilton, E., Curigliano, G., Xu, B., Huang, C.-S., Kim, J. H., Chiu, J. W. Y., Pedrini, J. L., Lee, C., . . . Hurvitz, S. A. (2022). Trastuzumab deruxtecan versus trastuzumab emtansine for breast cancer. *The New England Journal of Medicine*, *386*(12), 1143–1154. https://doi.org/10.1056/NEJMoa2115022 — PMID 35320644
- (Updated, OS) Hurvitz, S. A., Hegg, R., Chung, W.-P., Im, S.-A., Jacot, W., Ganju, V., Chiu, J. W. Y., Xu, B., Hamilton, E., Madhusudan, S., Iwata, H., Altintas, S., Henning, J.-W., Curigliano, G., Perez-Garcia, J. M., Kim, S.-B., Petry, V., Huang, C.-S., Li, W., . . . Cortés, J. (2023). Trastuzumab deruxtecan versus trastuzumab emtansine in patients with HER2-positive metastatic breast cancer: Updated results from DESTINY-Breast03, a randomised, open-label, phase 3 trial. *The Lancet*, *401*(10371), 105–117. https://doi.org/10.1016/S0140-6736(22)02420-5 — PMID 36495879 **Erratum:** PMID 36803433.
- (Long-term) Cortés, J., Hurvitz, S. A., Im, S.-A., Iwata, H., Curigliano, G., Kim, S.-B., Chiu, J. W. Y., Pedrini, J. L., Li, W., Yonemori, K., Bianchini, G., Loi, S., Borges, G. S., Wang, X., Bachelot, T., Nakatani, S., Ashfaque, S., Liang, Z., Egorov, A., & Hamilton, E. (2024). Trastuzumab deruxtecan versus trastuzumab emtansine in HER2-positive metastatic breast cancer: Long-term survival analysis of the DESTINY-Breast03 trial. *Nature Medicine*, *30*(8), 2208–2215. https://doi.org/10.1038/s41591-024-03021-7 — PMID 38825627 (PMC11333275)

**Design:** Phase 3, multicentre, open-label, randomized 1:1; 169 centres [A].
**Population:** 524 patients with HER2+ MBC previously treated with trastuzumab and a taxane [A].
**Arms:** T-DXd 5.4 mg/kg vs T-DM1 3.6 mg/kg, both every 3 weeks (n = 261 vs 263) [A].
**Primary endpoint (BICR PFS):**
- Primary analysis: 12-month PFS 75.8% vs 34.1%, HR 0.28 (0.22–0.37), P < 0.001. ORR 79.7% vs 34.2% [A].
- Updated (28.4 months of follow-up): **median 28.8 (22.4–37.9) vs 6.8 (5.6–8.2) months, HR 0.33 (0.26–0.43)** [A].
**OS:**
- 2023: median NR in both arms; HR 0.64 (0.47–0.87), p = 0.0037, significant [A].
- Long-term (41 months of follow-up): **52.6 vs 42.7 months, HR 0.73 (0.56–0.94).** Investigator PFS 29.0 vs 7.2 months, HR 0.30 (0.24–0.38) [A].
**ILD, adjudicated drug-related:**
- 10.5% vs 1.9% (primary).
- 15% vs 3% (2023).
- **16.7% vs 3.4%** (2024).
- No grade 4–5 events in DB-03 at any cut-off [A].

---

## C3. DESTINY-Breast09 (T-DXd + pertuzumab, first line; 2025–2026) — [VERIFIED] (interim)

**References**
- Tolaney, S. M., Jiang, Z., Zhang, Q., Barroso-Sousa, R., Park, Y. H., Rimawi, M. F., Saura, C., Schneeweiss, A., Toi, M., Chae, Y. S., Kemal, Y., Chaudhari, M., Şendur, M. A. N., Yamashita, T., Casalnuovo, M., Danso, M. A., Liu, J., Shetty, J., Herbolsheimer, P., & Loibl, S. (2026). Trastuzumab deruxtecan plus pertuzumab for HER2-positive metastatic breast cancer. *The New England Journal of Medicine*, *394*(6), 551–562. https://doi.org/10.1056/NEJMoa2508668 — PMID 41160818

**Design:** Phase 3, three arms, randomized 1:1:1. 1157 enrolled [L, CT.gov].
**Population:** HER2+ advanced or metastatic breast cancer with no prior chemotherapy or HER2 therapy for metastatic disease [A, L].
- Prior (neo)adjuvant HER2 therapy allowed if completed >6 months before.
- One prior ET line allowed.
- 50% were Asian [L].
**Arms:** T-DXd 5.4 mg/kg + pertuzumab (840 mg, then 420 mg) vs THP (taxane, trastuzumab, pertuzumab) vs T-DXd + placebo. The third arm stays blinded until the final PFS analysis [A, L].
**Primary endpoint (BICR PFS, interim; cutoff 2025-02-26):**
- **40.7 (36.5–NE) vs 26.9 (21.8–NE) months, HR 0.56 (0.44–0.71), P < 0.00001.**
- Confirmed ORR 85.1% vs 78.6%; CR 15.1% vs 8.5%. Median DoR 39.2 vs 26.4 months [A].
**OS:** Immature (16% of patients had died) [L].
**Toxicity:**
- Grade ≥3 AEs 63.5% vs 62.3% [A].
- **Adjudicated drug-related ILD 12.1% (2 grade 5 deaths) vs 1.0%** [A].
- Label (with pertuzumab): ILD 12%, fatal 0.5%; median onset 8.0 months [L].
- Concurrent ET (HR+) was allowed after 6 cycles: used in 13.5% vs 38.3% [L].
**Regulatory:**
- US label: first-line with pertuzumab [L].
- **Taiwan:** the TFDA Enhertu licence already lists 與pertuzumab合併使用…第一線治療 [TFDA].

---

## C4. HER2CLIMB (tucatinib + trastuzumab + capecitabine) — [VERIFIED]; **randomized phase 2** [CT.gov]

**References**
- Murthy, R. K., Loi, S., Okines, A., Paplomata, E., Hamilton, E., Hurvitz, S. A., Lin, N. U., Borges, V., Abramson, V., Anders, C., Bedard, P. L., Oliveira, M., Jakobsen, E., Bachelot, T., Shachar, S. S., Müller, V., Braga, S., Duhoux, F. P., Greil, R., . . . Winer, E. P. (2020). Tucatinib, trastuzumab, and capecitabine for HER2-positive metastatic breast cancer. *The New England Journal of Medicine*, *382*(7), 597–609. https://doi.org/10.1056/NEJMoa1914609 — PMID 31825569 **Erratum:** PMID 31881136.
- (Final OS) Curigliano, G., Mueller, V., Borges, V., Hamilton, E., Hurvitz, S., Loi, S., Murthy, R., Okines, A., Paplomata, E., Cameron, D., Carey, L. A., Gelmon, K., Hortobagyi, G. N., Krop, I., Loibl, S., Pegram, M., Slamon, D., Ramos, J., Feng, W., & Winer, E. (2022). Tucatinib versus placebo added to trastuzumab and capecitabine for patients with pretreated HER2+ metastatic breast cancer with and without brain metastases (HER2CLIMB): Final overall survival analysis. *Annals of Oncology*, *33*(3), 321–329. https://doi.org/10.1016/j.annonc.2021.12.005 — PMID 34954044 **Corrigendum:** PMID 36564285.
- (Brain metastases) Lin, N. U., Borges, V., Anders, C., Murthy, R. K., Paplomata, E., Hamilton, E., Hurvitz, S., Loi, S., Okines, A., Abramson, V., Bedard, P. L., Oliveira, M., Mueller, V., Zelnak, A., DiGiovanna, M. P., Bachelot, T., Chien, A. J., O'Regan, R., Wardley, A., . . . Winer, E. P. (2020). Intracranial efficacy and survival with tucatinib plus trastuzumab and capecitabine for previously treated HER2-positive breast cancer with brain metastases in the HER2CLIMB trial. *Journal of Clinical Oncology*, *38*(23), 2610–2619. https://doi.org/10.1200/JCO.20.00775 — PMID 32468955 (PMC7403000)

**Design:** Randomized 2:1, double-blind, placebo-controlled; **phase 2** per ClinicalTrials.gov (NCT02614794) [A, CT.gov].
**Population:** 612 patients with HER2+ MBC previously treated with trastuzumab, pertuzumab and T-DM1. 48% had brain metastases, including untreated or progressing ("active") lesions [A, FT].
**Arms:** Tucatinib 300 mg twice daily or placebo, plus trastuzumab (8 mg/kg, then 6 mg/kg every 21 days) and capecitabine 1000 mg/m² twice daily on days 1–14 [L-Tukysa 2024-11-04].
**Primary endpoint (PFS, first 480 patients):** 1-year PFS 33.1% vs 12.3%; **median 7.8 vs 5.6 months, HR 0.54 (0.42–0.71), P < 0.001** [A].
**Secondary endpoints:**
- OS (primary analysis): 21.9 vs 17.4 months, HR 0.66 (0.50–0.88), P = 0.005.
- Brain metastases: PFS 7.6 vs 5.4 months, HR 0.48 (0.34–0.69) [A].
**Final OS (29.6 months of follow-up):** **24.7 vs 19.2 months, HR 0.73 (0.59–0.90), P = 0.004.** PFS 7.6 vs 4.9 months, HR 0.57 (0.47–0.70) [A].
**Brain metastases (n = 291):**
- CNS-PFS 9.9 vs 4.2 months, HR 0.32 (0.22–0.48).
- OS 18.1 vs 12.0 months, HR 0.58 (0.40–0.85).
- Intracranial ORR 47.3% vs 20.0% [A].
**Toxicity (label):**
- Diarrhea 81% (grade 3 12%, grade 4 0.5%; both grade 4 patients died).
- ALT >5×ULN 8%; AST >5×ULN 6%; bilirubin >3×ULN 1.5%. Check LFTs every 3 weeks [L].
**Taiwan:** TUKYSA licensed 2026-03-02 (衛部藥輸字第029081/029082號) [TFDA].

---

## C5. PHOEBE and PHILA (pyrotinib; China-only trials, relevant to Asia) — PHOEBE [PARTIAL], PHILA [VERIFIED]

**References**
- (PHOEBE) Xu, B., Yan, M., Ma, F., Hu, X., Feng, J., Ouyang, Q., Tong, Z., Li, H., Zhang, Q., Sun, T., Wang, X., Yin, Y., Cheng, Y., Li, W., Gu, Y., Chen, Q., Liu, J., Cheng, J., Geng, C., . . . Zou, J. (2021). Pyrotinib plus capecitabine versus lapatinib plus capecitabine for the treatment of HER2-positive metastatic breast cancer (PHOEBE): A multicentre, open-label, randomised, controlled, phase 3 trial. *The Lancet Oncology*, *22*(3), 351–360. https://doi.org/10.1016/S1470-2045(20)30702-6 — PMID 33581774
- (PHILA) Ma, F., Yan, M., Li, W., Ouyang, Q., Tong, Z., Teng, Y., Wang, Y., Wang, S., Geng, C., Luo, T., Zhong, J., Zhang, Q., Liu, Q., Zeng, X., Sun, T., Mo, Q., Liu, H., Cheng, Y., Cheng, J., . . . Xu, B. (2023). Pyrotinib versus placebo in combination with trastuzumab and docetaxel as first line treatment in patients with HER2 positive metastatic breast cancer (PHILA): Randomised, double blind, multicentre, phase 3 trial. *BMJ*, *383*, Article e076065. https://doi.org/10.1136/bmj-2023-076065 — PMID 37907210 (PMC10616786) **Erratum:** PMID 37973164.
- (PHILA long-term) Ma, F., Yan, M., Li, W., Ouyang, Q., Tong, Z., Teng, Y., Wang, Y., Wang, S., Geng, C., Luo, T., Zhong, J., Zhang, Q., Liu, Q., Zeng, X., Sun, T., Mo, Q., Zhou, S., Li, P., Cheng, J., . . . Xu, B. (2026). Pyrotinib or placebo in combination with trastuzumab and docetaxel for HER2 positive metastatic breast cancer: Long term survival results from randomised phase 3 PHILA trial. *BMJ*, *392*, Article e087259. https://doi.org/10.1136/bmj-2025-087259 — PMID 41839514 (PMC12990035)
- (PHOEBE OS, conference summary [SS]) Jacobson, A. (2022). Pyrotinib improves survival in previously treated HER2-positive metastatic breast cancer. *The Oncologist*, *27*(Suppl. 1), S5–S6. https://doi.org/10.1093/oncolo/oyac013 — PMID 35348780 (PMC8963278)

**PHOEBE:**
- Design: phase 3, open-label, 1:1; 29 hospitals in China [A].
- Population: 267 patients with HER2+ MBC after trastuzumab and a taxane, aged 18–70 years [A].
- Arms: pyrotinib 400 mg or lapatinib 1250 mg once daily, each with capecitabine 1000 mg/m² twice daily on days 1–14 every 21 days [A].
- Primary endpoint (independent central review PFS, interim): **12.5 (9.7–NR) vs 6.8 (5.4–8.1) months, HR 0.39 (0.27–0.56)** [A].
- Grade ≥3 diarrhea 31% vs 8%; hand-foot syndrome 16% vs 15% [A].
- OS (ASCO 2022 summary only, [SS]): NR vs 26.9 months, HR 0.69 (0.48–0.98), p = .02; 24-month OS 66.6% vs 58.8%. **Peer-reviewed OS paper not found.** The summary table swaps the PFS arms (flag 16).

**PHILA:**
- Design: phase 3, double-blind; 40 centres in China [A].
- Population: 590 women with untreated HER2+ MBC [A].
- Arms: pyrotinib 400 mg/day or placebo, plus trastuzumab (8 then 6 mg/kg) and docetaxel 75 mg/m² every 21 days [A].
- Primary endpoint (investigator PFS): **24.3 (19.1–33.0) vs 10.4 (9.3–12.3) months, HR 0.41 (0.32–0.53)**. Grade ≥3 treatment-related AEs 90% vs 76% [A].
- Long-term (BMJ 2026; ~35 months of follow-up): deaths 20% vs 30%; **OS HR 0.64 (0.46–0.89)**, nominal one-sided P = 0.004; medians NR. PFS 22.1 vs 10.5 months, HR 0.44 (0.36–0.53) [A].
- Diarrhoea (treatment-related) 99% vs 54% [FT].

**Taiwan:** pyrotinib has **no TFDA licence** [TFDA]. Teach it as Asian evidence context, not a Taiwan treatment option.

---

# D. Triple-negative

## D1. KEYNOTE-355 (pembrolizumab + chemotherapy; CPS ≥10 OS) — [VERIFIED]

**References**
- Cortes, J., Cescon, D. W., Rugo, H. S., Nowecki, Z., Im, S.-A., Yusof, M. M., Gallardo, C., Lipatov, O., Barrios, C. H., Holgado, E., Iwata, H., Masuda, N., Otero, M. T., Gokmen, E., Loi, S., Guo, Z., Zhao, J., Aktan, G., Karantza, V., & Schmid, P. (2020). Pembrolizumab plus chemotherapy versus placebo plus chemotherapy for previously untreated locally recurrent inoperable or metastatic triple-negative breast cancer (KEYNOTE-355): A randomised, placebo-controlled, double-blind, phase 3 clinical trial. *The Lancet*, *396*(10265), 1817–1828. https://doi.org/10.1016/S0140-6736(20)32531-9 — PMID 33278935
- (Final OS) Cortes, J., Rugo, H. S., Cescon, D. W., Im, S.-A., Yusof, M. M., Gallardo, C., Lipatov, O., Barrios, C. H., Perez-Garcia, J., Iwata, H., Masuda, N., Torregroza Otero, M., Gokmen, E., Loi, S., Guo, Z., Zhou, X., Karantza, V., Pan, W., & Schmid, P. (2022). Pembrolizumab plus chemotherapy in advanced triple-negative breast cancer. *The New England Journal of Medicine*, *387*(3), 217–226. https://doi.org/10.1056/NEJMoa2202809 — PMID 35857659

**Design:** Phase 3, double-blind, randomized 2:1; 209 sites in 29 countries [A].
**Population:** 847 patients with untreated locally recurrent inoperable or metastatic TNBC (566 vs 281). Stratified by chemotherapy type, PD-L1 CPS ≥1 vs <1, and prior same-class chemotherapy [A].
**Arms:** Pembrolizumab 200 mg every 3 weeks or placebo, plus nab-paclitaxel, paclitaxel or gemcitabine + carboplatin [A].
**PFS (dual primary):**
- **CPS ≥10: 9.7 vs 5.6 months, HR 0.65 (0.49–0.86), one-sided p = 0.0012 (met).**
- CPS ≥1: 7.6 vs 5.6 months, HR 0.74 (0.61–0.90); not significant.
- ITT: 7.5 vs 5.6 months, HR 0.82 (0.69–0.97); not tested [A].
**OS (final, 44.1 months of follow-up):**
- **CPS ≥10: 23.0 vs 16.1 months, HR 0.73 (0.55–0.95), P = 0.0185 (met).**
- CPS ≥1: 17.6 vs 16.0 months, HR 0.86 (0.72–1.04); not significant.
- ITT: 17.2 vs 15.5 months, HR 0.89 (0.76–1.05) [A].
**Toxicity:**
- Treatment-related grade 3–5 AEs 68.1% vs 66.9%; treatment-related deaths 0.4% vs 0 [A].
- Label: fatal adverse reactions 2.5%; pembrolizumab discontinued in 11% (ALT increase 2.2%, pneumonitis 1.2%) [L-Keytruda Qlex 2026-07-31].
**Teaching point:** the benefit is confined to CPS ≥10 (22C3 assay; assay name is **[UNVERIFIED]** in the sources read).
**Taiwan:** the TFDA Keytruda licence includes metastatic TNBC with CPS ≥10 [TFDA].

---

## D2. IMpassion130 / IMpassion131 / IMpassion132 (the atezolizumab story) — [VERIFIED]; US withdrawal [PARTIAL]

**References**
- (IMpassion130) Schmid, P., Adams, S., Rugo, H. S., Schneeweiss, A., Barrios, C. H., Iwata, H., Diéras, V., Hegg, R., Im, S.-A., Shaw Wright, G., Henschel, V., Molinero, L., Chui, S. Y., Funke, R., Husain, A., Winer, E. P., Loi, S., & Emens, L. A. (2018). Atezolizumab and nab-paclitaxel in advanced triple-negative breast cancer. *The New England Journal of Medicine*, *379*(22), 2108–2121. https://doi.org/10.1056/NEJMoa1809615 — PMID 30345906
- (IMpassion130, 2nd interim OS) Schmid, P., Rugo, H. S., Adams, S., Schneeweiss, A., Barrios, C. H., Iwata, H., Diéras, V., Henschel, V., Molinero, L., Chui, S. Y., Maiya, V., Husain, A., Winer, E. P., Loi, S., & Emens, L. A. (2020). Atezolizumab plus nab-paclitaxel as first-line treatment for unresectable, locally advanced or metastatic triple-negative breast cancer (IMpassion130): Updated efficacy results from a randomised, double-blind, placebo-controlled, phase 3 trial. *The Lancet Oncology*, *21*(1), 44–59. https://doi.org/10.1016/S1470-2045(19)30689-8 — PMID 31786121
- (IMpassion130, final OS) Emens, L. A., Adams, S., Barrios, C. H., Diéras, V., Iwata, H., Loi, S., Rugo, H. S., Schneeweiss, A., Winer, E. P., Patel, S., Henschel, V., Swat, A., Kaul, M., Molinero, L., Patel, S., Chui, S. Y., & Schmid, P. (2021). First-line atezolizumab plus nab-paclitaxel for unresectable, locally advanced, or metastatic triple-negative breast cancer: IMpassion130 final overall survival analysis. *Annals of Oncology*, *32*(8), 983–993. https://doi.org/10.1016/j.annonc.2021.05.355 — PMID 34272041 **Corrigenda:** PMIDs 34353668, 34740469.
- (IMpassion131) Miles, D., Gligorov, J., André, F., Cameron, D., Schneeweiss, A., Barrios, C., Xu, B., Wardley, A., Kaen, D., Andrade, L., Semiglazov, V., Reinisch, M., Patel, S., Patre, M., Morales, L., Patel, S. L., Kaul, M., Barata, T., & O'Shaughnessy, J. (2021). Primary results from IMpassion131, a double-blind, placebo-controlled, randomised phase III trial of first-line paclitaxel with or without atezolizumab for unresectable locally advanced/metastatic triple-negative breast cancer. *Annals of Oncology*, *32*(8), 994–1004. https://doi.org/10.1016/j.annonc.2021.05.801 — PMID 34219000
- (IMpassion132) Dent, R., André, F., Gonçalves, A., Martin, M., Schmid, P., Schütz, F., Kümmel, S., Swain, S. M., Bilici, A., Loirat, D., Villalobos Valencia, R., Im, S.-A., Park, Y. H., De Laurentis, M., Colleoni, M., Guarneri, V., Bianchini, G., Li, H., Kirchmayer Machackova, Z., . . . Cortés, J. (2024). IMpassion132 double-blind randomised phase III trial of chemotherapy with or without atezolizumab for early relapsing unresectable locally advanced or metastatic triple-negative breast cancer. *Annals of Oncology*, *35*(7), 630–642. https://doi.org/10.1016/j.annonc.2024.04.001 — PMID 38755096
- (FDA review of "dangling" approvals) Lemery, S., & Pazdur, R. (2022). Approvals in 2021: Dangling accelerated approvals, drug dosing, new approvals and beyond. *Nature Reviews Clinical Oncology*, *19*(4), 217–218. https://doi.org/10.1038/s41571-022-00605-5 — PMID 35136230 (PMC8824437)
- (FDA perspective on "dangling" approvals; PubMed has no abstract and I did not read the text, so cite only as background) Beaver, J. A., & Pazdur, R. (2021). "Dangling" accelerated approvals in oncology. *The New England Journal of Medicine*, *384*(18), e68. https://doi.org/10.1056/NEJMp2104846 — PMID 33882220
- (US withdrawal and Japan, [SS]) Hakariya, H., Ozaki, A., & Tanimoto, T. (2025). US FDA-accelerated approvals and subsequent withdrawals: Influence on Japanese clinical oncology practice guidelines. *Investigational New Drugs*, *43*(2), 311–317. https://doi.org/10.1007/s10637-025-01524-9 — PMID 40178688 (PMC12048449)

**IMpassion130:**
- Design: phase 3, double-blind, 1:1 [A].
- Population: 902 patients with untreated metastatic TNBC (451 per arm) [A].
- Arms: atezolizumab 840 mg (days 1 and 15) + nab-paclitaxel 100 mg/m² (days 1, 8, 15) every 28 days vs placebo + nab-paclitaxel [A].
- PFS (co-primary): ITT 7.2 vs 5.5 months, HR 0.80 (0.69–0.92), P = 0.002; **PD-L1+ (SP142 IC ≥1%): 7.5 vs 5.0 months, HR 0.62 (0.49–0.78)** [A].
- OS (hierarchical; ITT first):
  - 1st interim: ITT 21.3 vs 17.6 months, HR 0.84 (0.69–1.02), P = 0.08.
  - 2nd interim: ITT 21.0 vs 18.7 months, HR 0.86 (0.72–1.02).
  - **Final: ITT 21.0 vs 18.7 months, HR 0.87 (0.75–1.02), P = 0.077, not significant.** PD-L1+ OS 25.4 vs 17.9 months, HR 0.67 (0.53–0.86), which **could not be formally tested** [A].
- Immune-mediated AEs of special interest 58.7% vs 41.6% [A].

**IMpassion131:**
- Design: phase 3, double-blind, 2:1 [A].
- Population: 651 patients; 45% PD-L1+ [A].
- Arms: atezolizumab 840 mg (days 1, 15) + **paclitaxel 90 mg/m²** (days 1, 8, 15) every 28 days vs placebo + paclitaxel [A].
- PD-L1+ PFS: 6.0 vs 5.7 months, HR 0.82 (0.60–1.12), P = 0.20. **Negative** [A].
- Final OS (PD-L1+): 22.1 vs 28.3 months, HR 1.11 (0.76–1.64) [A].

**IMpassion132:**
- Population: rapidly relapsing TNBC (<12 months after early-stage treatment); 354 PD-L1+ patients [A].
- Arms: atezolizumab 1200 mg every 21 days + carboplatin/gemcitabine or capecitabine vs placebo + chemotherapy [A].
- OS: 12.1 vs 11.2 months, HR 0.93 (0.73–1.20), P = 0.59. **Negative** [A].

**Regulatory history:**
- In April 2021 the FDA Advisory Committee reviewed "dangling" accelerated approvals and voted to **retain** atezolizumab for PD-L1+ TNBC, pending further data [FT, Lemery & Pazdur 2022].
- A 2025 analysis states the US indication was withdrawn on the basis of IMpassion131. Japan kept it, and the Japanese Breast Cancer Society rates it "highly preferred" [SS, Hakariya 2025]. Exact US withdrawal date **[UNVERIFIED]**.
- **Taiwan:** both active Tecentriq licences still list 與nab-paclitaxel併用…三陰性乳癌，且腫瘤具PD-L1表現 (IC ≥1%) [TFDA].

**Teaching points:**
- The taxane partner matters: nab-paclitaxel was positive in IMpassion130; paclitaxel was negative in IMpassion131.
- The PD-L1 assay and cut-off differ between drugs: SP142 IC ≥1% for atezolizumab vs CPS ≥10 for pembrolizumab.

---

## D3. ASCENT (sacituzumab govitecan, ≥2nd line TNBC) — [VERIFIED]

**References**
- Bardia, A., Hurvitz, S. A., Tolaney, S. M., Loirat, D., Punie, K., Oliveira, M., Brufsky, A., Sardesai, S. D., Kalinsky, K., Zelnak, A. B., Weaver, R., Traina, T., Dalenc, F., Aftimos, P., Lynce, F., Diab, S., Cortés, J., O'Shaughnessy, J., Diéras, V., . . . Rugo, H. S. (2021). Sacituzumab govitecan in metastatic triple-negative breast cancer. *The New England Journal of Medicine*, *384*(16), 1529–1541. https://doi.org/10.1056/NEJMoa2028485 — PMID 33882206
- (Final) Bardia, A., Rugo, H. S., Tolaney, S. M., Loirat, D., Punie, K., Oliveira, M., Brufsky, A., Kalinsky, K., Cortés, J., O'Shaughnessy, J., Diéras, V., Carey, L. A., Gianni, L., Piccart-Gebhart, M., Loibl, S., Yoon, O. K., Pan, Y., Hofsess, S., Phan, S.-C., & Hurvitz, S. A. (2024). Final results from the randomized phase III ASCENT clinical trial in metastatic triple-negative breast cancer and association of outcomes by human epidermal growth factor receptor 2 and trophoblast cell surface antigen 2 expression. *Journal of Clinical Oncology*, *42*(15), 1738–1744. https://doi.org/10.1200/JCO.23.01409 — PMID 38422473 (PMC11107894) PubMed misrecords the author O'Shaughnessy (corrected here).
- (Safety, UGT1A1) Rugo, H. S., Tolaney, S. M., Loirat, D., Punie, K., Bardia, A., Hurvitz, S. A., O'Shaughnessy, J., Cortés, J., Diéras, V., Carey, L. A., Gianni, L., Piccart, M. J., Loibl, S., Goldenberg, D. M., Hong, Q., Olivo, M., Itri, L. M., & Kalinsky, K. (2022). Safety analyses from the phase 3 ASCENT trial of sacituzumab govitecan in metastatic triple-negative breast cancer. *npj Breast Cancer*, *8*(1), Article 98. https://doi.org/10.1038/s41523-022-00467-1 — PMID 36038616 (PMC9424318) **Erratum:** PMID 38844800.

**Design:** Phase 3, open-label, randomized 1:1 [A].
**Population:** Relapsed or refractory mTNBC after ≥2 prior chemotherapy regimens, ≥1 of them in the metastatic setting [A, safety paper]. 529 randomized; 468 without brain metastases formed the primary-analysis population [A, L].
**Arms:** SG 10 mg/kg on days 1 and 8 every 21 days vs TPC (eribulin, vinorelbine, capecitabine or gemcitabine) [A, L].
**Primary endpoint (BICR PFS, no brain metastases):** **5.6 (4.3–6.3) vs 1.7 (1.5–2.6) months, HR 0.41 (0.32–0.52), P < 0.001** [A].
**OS:**
- Primary analysis: **12.1 (10.7–14.0) vs 6.7 (5.8–7.7) months, HR 0.48 (0.38–0.59)**. ORR 35% vs 5% [A].
- Final analysis (all randomized, including brain metastases; 267 vs 262): PFS 4.8 vs 1.7 months, HR 0.41 (0.33–0.52); OS 11.8 vs 6.9 months, HR 0.51 (0.42–0.63) [A]. The label gives the same medians with HR 0.51 (0.41–0.62) and 67% vs 79% deaths [L-Trodelvy].
**Toxicity:**
- Grade ≥3 (primary): neutropenia 51% vs 33%; leukopenia 10% vs 5%; diarrhea 10% vs <1%; anemia 8% vs 5%; FN 6% vs 2%. No SG-related deaths [A].
- Final paper: grade ≥3 neutropenia 52%, diarrhea 12% [FT].
- **UGT1A1 *28/*28 vs *1/*28 vs *1/*1** [A, safety paper]:
  - Grade ≥3 neutropenia 59% vs 47% vs 53%.
  - **FN 18% vs 5% vs 3%.**
  - Diarrhea 15% vs 9% vs 10%.

---

## D4. ASCENT-03 (SG, first line, not PD-(L)1 candidates; 2025) — [VERIFIED]

**References**
- Cortés, J., Punie, K., Barrios, C., Hurvitz, S. A., Schneeweiss, A., Sohn, J., Tokunaga, E., Brufsky, A., Park, Y. H., Xu, B., Hegg, R., Oliveira, M., Fabi, A., Vaksman, N., Valdez, T., Zhang, X., Lai, C., & Tolaney, S. M. (2025). Sacituzumab govitecan in untreated, advanced triple-negative breast cancer. *The New England Journal of Medicine*, *393*(19), 1912–1925. https://doi.org/10.1056/NEJMoa2511734 — PMID 41124233

**Design:** Phase 3, international, open-label, randomized 1:1 [A]. ClinicalTrials.gov actual enrolment is 623 vs 558 analysed in the NEJM paper; the reason was not checked [CT.gov].
**Population:** 558 patients with untreated advanced TNBC who were not candidates for PD-(L)1 inhibitors [A].
- Either PD-L1 CPS <10, or CPS ≥10 with prior PD-(L)1 exposure or a comorbidity.
- 99.5% had CPS <10 [L].
**Arms:** SG 10 mg/kg (days 1 and 8 every 21 days) vs paclitaxel, nab-paclitaxel or gemcitabine + carboplatin. Crossover to SG was allowed at progression [A, L].
**Primary endpoint (BICR PFS):** **9.7 (8.1–11.1) vs 6.9 (5.6–8.2) months, HR 0.62 (0.50–0.77), P < 0.001.** ORR 48% vs 46%; DoR 12.2 vs 7.2 months [A].
**OS:** Immature (51% had died) [L].
**Toxicity:**
- Grade ≥3 AEs 66% vs 62%: neutropenia 43%, diarrhea 9%, leukopenia 7% with SG.
- Discontinuation 4% vs 12% [A].
- Label: fatal adverse reactions 2.5% (sepsis 1.1%) [L].

---

## D5. ASCENT-04 / KEYNOTE-D19 (SG + pembrolizumab, first line, PD-L1+; 2026) — [VERIFIED]

**References**
- Tolaney, S. M., de Azambuja, E., Kalinsky, K., Loi, S., Kim, S.-B., Yam, C., Rapoport, B., Im, S.-A., Pistilli, B., Mchayleh, W., Cescon, D. W., Watanabe, J., Bañuelas, M. A. L., Freitas-Junior, R., Salvador Bofill, J., Afshari, M., Gary, D., Wang, L., Lai, C., & Schmid, P. (2026). Sacituzumab govitecan plus pembrolizumab for advanced triple-negative breast cancer. *The New England Journal of Medicine*, *394*(4), 354–366. https://doi.org/10.1056/NEJMoa2508959 — PMID 41564397

**Design:** Phase 3, international, open-label, randomized 1:1 [A, CT.gov].
**Population:** 443 patients with untreated PD-L1-positive advanced TNBC (US indication: CPS ≥10) [A, L].
**Arms:** SG 10 mg/kg (days 1 and 8) + pembrolizumab 200 mg every 21 days vs TPC (nab-paclitaxel, paclitaxel or gemcitabine + carboplatin) + pembrolizumab; n = 221 vs 222 [A, L].
**Primary endpoint (BICR PFS):** **11.2 (9.3–16.7) vs 7.8 (7.3–9.3) months, HR 0.65 (0.51–0.84), P < 0.001.** ORR 60% vs 53%; DoR 16.5 vs 9.2 months [A].
**OS:** Immature (46% had died) [A, L].
**Toxicity:**
- Grade ≥3 AEs 71% vs 70%.
- Discontinuation for AEs 12% vs 31%; deaths from AEs 3% in each arm [A].
- Label: decreased neutrophils 86%; diarrhea 72% [L].
**Taiwan:** the Trodelvy licence has **no** first-line indication [TFDA].

---

## D6. TROPION-Breast02 (Dato-DXd, first line, IO not an option; 2026) — [VERIFIED]

**References**
- Dent, R., Shao, Z., Schmid, P., Cortes, J., Cescon, D. W., Saji, S., Jung, K. H., Bachelot, T., Wang, S., Ramírez, E. M., Basaran, G., Stradella, A., Mathiba, R., Chen, S.-C., Shen, K., Wéber, Á., Battelli, N., Niikura, N., Luo, T., . . . Traina, T. (2026). Datopotamab deruxtecan in patients with untreated, advanced triple-negative breast cancer (TROPION-Breast02): A randomised, open-label, international, phase III trial. *Annals of Oncology*, *37*(8), 1066–1080. https://doi.org/10.1016/j.annonc.2026.03.008 — PMID 41937088

**Design:** Phase 3, open-label, international, randomized 1:1. **Dual primary endpoints PFS (BICR) and OS** [A].
**Population:** 644 patients with untreated locally recurrent inoperable or metastatic TNBC for whom immunotherapy was not an option (323 vs 321) [A].
**Arms:** Dato-DXd 6 mg/kg every 3 weeks vs ICC [A].
**Results:**
- **PFS 10.8 (8.6–13.0) vs 5.6 (5.0–7.0) months, HR 0.57 (99% CI 0.44–0.73), P < 0.0001.**
- **OS 23.7 (19.8–25.6) vs 18.7 (16.0–21.8) months, HR 0.79 (95.01% CI 0.64–0.98), P = 0.029.** Both dual primary endpoints were met [A].
**Toxicity:**
- Grade ≥3 treatment-related AEs 33% vs 29%; discontinuation 4% vs 7%; no treatment-related deaths [A].
- Label (pooled breast cancer): ILD 3.0%; stomatitis 63% (grade 3 8%); ocular adverse reactions 38% [L-Datroway].
**Regulatory:** the US label has a TNBC indication; **Taiwan does not** [L, TFDA].

---

# E. Germline BRCA

## E1. OlympiAD (olaparib) — [VERIFIED]

**References**
- Robson, M., Im, S.-A., Senkus, E., Xu, B., Domchek, S. M., Masuda, N., Delaloge, S., Li, W., Tung, N., Armstrong, A., Wu, W., Goessl, C., Runswick, S., & Conte, P. (2017). Olaparib for metastatic breast cancer in patients with a germline BRCA mutation. *The New England Journal of Medicine*, *377*(6), 523–533. https://doi.org/10.1056/NEJMoa1706450 — PMID 28578601 **Erratum:** PMID 28792849.
- (Final OS) Robson, M. E., Tung, N., Conte, P., Im, S.-A., Senkus, E., Xu, B., Masuda, N., Delaloge, S., Li, W., Armstrong, A., Wu, W., Goessl, C., Runswick, S., & Domchek, S. M. (2019). OlympiAD final overall survival and tolerability results: Olaparib versus chemotherapy treatment of physician's choice in patients with a germline BRCA mutation and HER2-negative metastatic breast cancer. *Annals of Oncology*, *30*(4), 558–566. https://doi.org/10.1093/annonc/mdz012 — PMID 30689707 (PMC6503629)
- (Extended follow-up) Robson, M. E., Im, S.-A., Senkus, E., Xu, B., Domchek, S. M., Masuda, N., Delaloge, S., Tung, N., Armstrong, A., Dymond, M., Fielding, A., Allen, A., & Conte, P. (2023). OlympiAD extended follow-up for overall survival and safety: Olaparib versus chemotherapy treatment of physician's choice in patients with a germline BRCA mutation and HER2-negative metastatic breast cancer. *European Journal of Cancer*, *184*, 39–47. https://doi.org/10.1016/j.ejca.2023.01.031 — PMID 36893711 (PMC10585240)

**Design:** Phase 3, open-label, randomized 2:1 [A].
**Population:** 302 patients with germline BRCA-mutated HER2− MBC and ≤2 prior chemotherapy lines for MBC (205 vs 97) [A].
**Arms:** Olaparib tablets 300 mg twice daily vs TPC (capecitabine, eribulin or vinorelbine) [A].
**Primary endpoint (BICR PFS):** **7.0 vs 4.2 months, HR 0.58 (0.43–0.80), P < 0.001.** ORR 59.9% vs 28.8% [A].
**OS:**
- Final (64% maturity): 19.3 vs 17.1 months, HR 0.90 (0.66–1.23), P = 0.513. **Not significant.**
- First-line (no prior chemotherapy for MBC) subgroup: HR 0.51 (0.29–0.90) [A].
- Extended follow-up (76.8% maturity): HR 0.89 (0.67–1.18). First-line: 22.6 vs 14.7 months, HR 0.55 (0.33–0.95); 3-year OS 40.8% vs 12.8% [A].
**Toxicity:**
- Grade ≥3 AEs 36.6% vs 50.5% [A, primary].
- Anemia any grade 40.0% (grade ≥3 16.1%) vs 26.4% (4.4%); nausea 58.0% [FT].
- Label: MDS/AML ~1.2% (26/2219), with 54% of those fatal [L-Lynparza 2025-07-10].
**Taiwan:** Lynparza is licensed for gBRCA HER2− MBC after (neo)adjuvant or metastatic chemotherapy [TFDA].

---

## E2. EMBRACA (talazoparib) — [VERIFIED]

**References**
- Litton, J. K., Rugo, H. S., Ettl, J., Hurvitz, S. A., Gonçalves, A., Lee, K.-H., Fehrenbacher, L., Yerushalmi, R., Mina, L. A., Martin, M., Roché, H., Im, Y.-H., Quek, R. G. W., Markova, D., Tudor, I. C., Hannah, A. L., Eiermann, W., & Blum, J. L. (2018). Talazoparib in patients with advanced breast cancer and a germline BRCA mutation. *The New England Journal of Medicine*, *379*(8), 753–763. https://doi.org/10.1056/NEJMoa1802905 — PMID 30110579 (PMC10600918)
- (Final OS) Litton, J. K., Hurvitz, S. A., Mina, L. A., Rugo, H. S., Lee, K.-H., Gonçalves, A., Diab, S., Woodward, N., Goodwin, A., Yerushalmi, R., Roché, H., Im, Y.-H., Eiermann, W., Quek, R. G. W., Usari, T., Lanzalone, S., Czibere, A., Blum, J. L., Martin, M., & Ettl, J. (2020). Talazoparib versus chemotherapy in patients with germline BRCA1/2-mutated HER2-negative advanced breast cancer: Final overall survival results from the EMBRACA trial. *Annals of Oncology*, *31*(11), 1526–1535. https://doi.org/10.1016/j.annonc.2020.08.2098 — PMID 32828825 (PMC10649377)

**Design:** Phase 3, open-label, randomized 2:1 [A].
**Population:** 431 patients with advanced breast cancer and a germline BRCA1/2 mutation; HER2− per the OS paper (287 vs 144) [A].
**Arms:** Talazoparib 1 mg once daily vs TPC (capecitabine, eribulin, gemcitabine or vinorelbine) [A].
**Primary endpoint (BICR PFS):** **8.6 vs 5.6 months, HR 0.54 (0.41–0.71), P < 0.001.** ORR 62.6% vs 27.2% [A].
**Final OS:**
- **19.3 (16.6–22.5) vs 19.5 (17.4–22.4) months, HR 0.848 (0.670–1.073), P = 0.17. Not significant.**
- Subsequent PARP inhibitor 4.5% vs 32.6%; platinum 46.3% vs 41.7%.
- Adjusted for subsequent PARPi/platinum: HR 0.756 [A].
**Toxicity:**
- Hematologic grade 3–4 AEs 55% vs 38% [A].
- Grade 3 anemia 38.5% vs 4.0% [FT].
- Label (monotherapy pooled): grade ≥3 anemia 39%, neutropenia 21%, thrombocytopenia 15%; MDS/AML 0.4% [L-Talzenna 2026-06-01].

---

# F. Toxicity cross-reference for nursing (numbers from the sources above)

## F1. Trastuzumab deruxtecan ILD (boxed warning) — [VERIFIED]

| Source | Any-grade adjudicated drug-related ILD | Grade 5 |
|---|---|---|
| DESTINY-Breast03 primary / 2023 / 2024 | 10.5% / 15% / 16.7% | 0 |
| DESTINY-Breast04 primary → long-term | 12.1% → 12.1% (no new cases) | 0.8% → 1.1% |
| DESTINY-Breast06 | 11.3% | 3 patients (~0.7%, computed) |
| DESTINY-Breast09 (with pertuzumab) | 12.1% | 2 patients |
| Pooled 9 phase 1/2 studies (n = 1150) | 15.4% | 2.2% |
| FDA label, 5.4 mg/kg monotherapy | 12% (median onset 5.5 months) | 0.9% |

**Pooled-analysis risk factors** [A, Powell 2022]:
- Age <65 years.
- **Enrolment in Japan.**
- Dose >6.4 mg/kg.
- SpO₂ <95%.
- Moderate or severe renal impairment.
- Lung comorbidity.
- >4 years since diagnosis.
- 87% of first events occurred within 12 months.
**Label management** [L-Enhertu]:
- Grade 1: withhold; consider steroids (≥0.5 mg/kg/day prednisolone).
- **Grade ≥2: permanently discontinue**; give ≥1 mg/kg/day prednisolone for ≥14 days, then taper over ≥4 weeks.

**Pooled reference**
- Powell, C. A., Modi, S., Iwata, H., Takahashi, S., Smit, E. F., Siena, S., Chang, D.-Y., Macpherson, E., Qin, A., Singh, J., Taitt, C., Shire, N., & Camidge, D. R. (2022). Pooled analysis of drug-related interstitial lung disease and/or pneumonitis in nine trastuzumab deruxtecan monotherapy studies. *ESMO Open*, *7*(4), Article 100554. https://doi.org/10.1016/j.esmoop.2022.100554 — PMID 35963179 (PMC9434416)

## F2. Sacituzumab govitecan: neutropenia and diarrhea (boxed warning) — [VERIFIED]

- Label: neutropenia 64% (grade 3–4 48%); FN 6%; neutropenic colitis 1.4%; diarrhea 62% (grade 3–4 10%) [L-Trodelvy].
- UGT1A1 genotype, pooled n = 1202, grade 3–4 neutropenia [L]:
  - *28/*28: 57%
  - *1/*28: 48%
  - wild type: 41%
- Anemia: 17% / 9% / 8% in the same genotype groups [L].
- **Hold rules:** ANC <1500/mm³ on day 1 or <1000/mm³ on day 8, or neutropenic fever [L].
- **Primary G-CSF prophylaxis** is recommended for patients at high FN risk [L].
- Premedication [L]:
  - Antipyretic + H1 and H2 blockers.
  - Two- or three-drug antiemetic.
- Diarrhea [L]:
  - Exclude infection, then loperamide 4 mg, then 2 mg after each loose stool (maximum 16 mg/day).
  - Atropine for a cholinergic syndrome.
- Do not substitute for or combine with irinotecan or SN-38 products [L].

## F3. CDK4/6 inhibitors — [VERIFIED]

**Ribociclib** [L-Kisqali 2026-07-01]:
- MBC (600 mg): QTcF >500 ms in 1.4%; >60 ms increase in 6%; most within the first 4 weeks.
- Start only if QTcF <450 ms. ECG at baseline and about day 14 of cycle 1. Electrolytes at the start of each of the first 6 cycles.
- **Not indicated with tamoxifen.**
- Grade 3–4 ALT 11% and AST 8% (MBC); median onset 92 days; Hy's law 1%.
- LFTs every 2 weeks for 2 cycles, then at the start of each of the next 4 cycles.
- ILD and SCAR warnings.

**Abemaciclib:** see A4. Diarrhea starts at a median of 6–8 days. Start loperamide at the first loose stool [L-Verzenio].

**Palbociclib:** grade 3–4 neutropenia 62–66%. FN is rare (≤1.8%). Asians have more neutropenia (A1).

## F4. PI3K/AKT pathway inhibitors: hyperglycemia and rash — [VERIFIED]

| Drug (trial) | Hyperglycemia, any grade | Grade ≥3 | Median onset | Rash or skin, any / grade ≥3 |
|---|---|---|---|---|
| Alpelisib (SOLAR-1) | 65% [L] | 36.6% [A] | 15 days | rash grade 3 9.9% |
| Capivasertib (CAPItello-291) | 16.3% AE term [FT]; 37% fasting-glucose labs [L] | 2.3% [A] | 15 days | 38% / 12.1% [FT]; label cutaneous 58% / 17% |
| Inavolisib (INAVO120) | 63.4% AE term [FT]; 85% fasting-glucose labs [L] | 6.8% AE [FT]; 12.6% lab (computed) | 7 days | 26.7% / 0 [FT] |

**Teaching points:**
- Check FPG and HbA1c before starting.
- Monitor glucose closely in the first 2–4 weeks.
- Metformin is first-line.
- Hold the drug during acute illness (DKA risk).
- Eligibility cut-offs show which patients were excluded: CAPItello-291 HbA1c ≥8% or insulin-requiring T2DM; INAVO120 FPG ≥126 mg/dL or HbA1c ≥6.0% [L, FT].

## F5. Other new-agent signals — [VERIFIED]

- **Dato-DXd:**
  - Stomatitis 50% (TB01); pooled 63% (grade 3 8%).
  - Ocular 38–40%: dry eye and keratitis.
  - ILD ~3%.
  - Steroid mouthwash; ice chips during infusion; ophthalmology review [FT, L].
- **Camizestrant:**
  - Bradycardia 8%; QTc 2.6%; visual disturbances 34%.
  - **Boxed warning with ribociclib** [L].
- **Vepdegestrant:** QTc prolongation 10% [L].
- **Elacestrant:** nausea 35%; hypercholesterolemia 30%, hypertriglyceridemia 27% [FT, L].
- **Imlunestrant:** mostly grade 1 fatigue, diarrhea and nausea; bradycardia 2.1% [FT].
- **Tucatinib:** diarrhea 81% (grade ≥3 12.5%); ALT >5×ULN 8% [L].
- **Pyrotinib:**
  - PHOEBE: grade ≥3 diarrhea 31%.
  - PHILA: diarrhoea 99% [A, FT].
- **PARP inhibitors:** anemia (talazoparib grade 3 38.5%; olaparib grade ≥3 16.1%); MDS/AML [FT, L].

---

# G. Taiwan TFDA licence status (InfoId=36 dataset dated 2026-10-27; active licences only) — [VERIFIED]

| Drug | Brand (中文) | Licence no. | Issue date (dataset field) | Breast indication summary |
|---|---|---|---|---|
| Ribociclib | KISQALI 擊癌利 | 衛部藥輸字第027320號 | 2017/11/22 | eBC adjuvant; MBC with AI (men, pre-, peri- or postmenopausal women) or fulvestrant |
| Abemaciclib | VERZENIO 捷癌寧 | 027640–027643 | 2019/05/14 | eBC adjuvant; MBC with AI or fulvestrant; monotherapy |
| Palbociclib | IBRANCE 愛乳適 | 027102–027104 (capsules); 028005–028007 (tablets) | 2017/05/04; 2021/01 | HR+/HER2− MBC with AI or fulvestrant |
| Alpelisib | PIQRAY 愛克利 | 027994–027996 | 2020/12/23 | PIK3CA-mut, with fulvestrant, **postmenopausal women and men** |
| Capivasertib | Truqap 泛抑癌 | 028820–028821 | 2024/11/06 | PIK3CA/AKT1/PTEN-altered, with fulvestrant |
| Inavolisib | Itovebi 癌妥飛 | 028944–028945 | 2025/06/02 | PIK3CA-mut, endocrine-resistant, with palbociclib + fulvestrant |
| Imlunestrant | Inluriyo 盈乳樂 | 029131 | 2026/05/15 | ESR1-mut after ≥1 ET |
| Elacestrant / camizestrant / vepdegestrant | — | **none** | — | not licensed |
| T-DXd | ENHERTU 優赫得 | 衛部菌疫輸字第001179號 | 2026/04/23 (dataset field; may reflect re-issue) | HER2+ (first line with pertuzumab, later lines), HER2-low, HER2-ultralow, eBC neoadjuvant |
| Sacituzumab govitecan | TRODELVY 拓達維 | 001206 | 2022/11/15 | TNBC after ≥2 systemic therapies; HR+/HER2− after ≥2 metastatic therapies. **No first-line indication** |
| Dato-DXd | DATROWAY 達卓優 | 001302 | 2025/11/10 | HR+/HER2− after ET + chemotherapy. **No TNBC indication** |
| Tucatinib | TUKYSA 杜凱莎 | 029081–029082 | 2026/03/02 | With trastuzumab + capecitabine after 1–2 anti-HER2 lines (including brain metastases) |
| Pyrotinib | — | **none** | — | not licensed |
| Pertuzumab | Perjeta 賀疾妥; Phesgo 賀雙妥 | 000942; 001172–001173 | 2013/06/14; 2021/09/22 | (not reviewed) |
| Pembrolizumab | Keytruda 吉舒達 | 001025 | 2024/10/28 (dataset field) | Metastatic TNBC CPS ≥10; high-risk early TNBC |
| Atezolizumab | Tecentriq 癌自禦 | 001050; 001258 (SC) | 2017/07/17; 2024/05/29 | **Still lists** nab-paclitaxel combination for PD-L1 IC ≥1% mTNBC |
| Olaparib | Lynparza 令癌莎 | 027445–027446 | 2018/06/05 | gBRCA HER2− MBC after chemotherapy; HR+ after or unsuitable for ET |
| Talazoparib | Talzenna 達勝癌 | 027801 | 2020/02/03 | gBRCA HER2− LA/MBC |

NHI reimbursement was **not checked**: www.nhi.gov.tw is not reachable from this environment. Licensed does not mean reimbursed.

---

## Appendix: PMID index

| Trial | Primary PMID | Follow-up / OS / safety PMID(s) |
|---|---|---|
| PALOMA-2 | 27959613 | 38252901 (OS); 31125276 (Asian) |
| MONALEESA-2 | 27717303 (erratum 30586508) | 29718092 (erratum 31407010); 35263519 (OS) |
| MONALEESA-7 | 29804902 | 31166679 (OS) |
| MONARCH 3 | 28968163 | 30675515 (final PFS); 38729566 (OS; corrigendum 41093689) |
| PALOMA-3 | 26030518 | 26947331 (errata 27300673, 27733295); 30345905; 35552673 |
| SOLAR-1 | 31091374 | 33246021 (OS); 32416251 (AEs) |
| CAPItello-291 | 37256976 | 39241495 (AEs); final OS not found |
| EMERALD | 35584336 (erratum 37364222) | OS in FDA label only |
| INAVO120 | 39476340 | 40454641 (OS); 42202490 (safety) |
| SERENA-6 | 40454637 | 42442380 (extended, PFS2) |
| EMBER-3 | 39660834 | 41391667 (updated, interim OS) |
| VERITAC-2 | 40454645 | — |
| postMONARCH | 39693591 | 42926108 (OS) |
| DESTINY-Breast04 | 35665782 | 41062831 (long-term) |
| DESTINY-Breast06 | 39282896 | 41780642 (subgroups); OS not found |
| TROPION-Breast01 | 39265124 | 41448362 (final OS) |
| TROPiCS-02 | 36027558 | 37633306 (OS) |
| T-DXd ILD pooled | 35963179 | — |
| CLEOPATRA | 22149875 | 25693012 (OS); 32171426 (end of study) |
| DESTINY-Breast03 | 35320644 | 36495879 (erratum 36803433); 38825627 |
| DESTINY-Breast09 | 41160818 | — |
| HER2CLIMB | 31825569 (erratum 31881136) | 34954044 (corrigendum 36564285); 32468955 (CNS) |
| PHOEBE | 33581774 | 35348780 (OS conference summary, [SS]) |
| PHILA | 37907210 (erratum 37973164) | 41839514 (long-term OS) |
| KEYNOTE-355 | 33278935 | 35857659 (OS) |
| IMpassion130 | 30345906 | 31786121; 34272041 (corrigenda 34353668, 34740469) |
| IMpassion131 | 34219000 | — |
| IMpassion132 | 38755096 | — |
| ASCENT | 33882206 | 38422473 (final); 36038616 (safety; erratum 38844800) |
| ASCENT-03 | 41124233 | — |
| ASCENT-04 | 41564397 | — |
| TROPION-Breast02 | 41937088 | — |
| OlympiAD | 28578601 (erratum 28792849) | 30689707 (OS); 36893711 (extended) |
| EMBRACA | 30110579 | 32828825 (OS) |
| Regulatory | 35136230; 33882220 | 40178688 ([SS]) |

**FDA labels read (openFDA, effective dates):**
- Kisqali 2026-07-01; Verzenio 2026-07-13; Ibrance 2026-07-06.
- Piqray 2025-12-15; Truqap 2026-06-12; Itovebi 2026-04-21.
- Orserdu 2026-06-24; Inluriyo 2026-06-04; Veppanu 2026-06-12; Etcamah 2026-09-04.
- Enhertu 2026-05-15; Trodelvy 2026-06-24; Datroway 2026-05-27.
- Tukysa 2024-11-04; Perjeta 2026-04-30; Keytruda Qlex 2026-07-31.
- Lynparza 2025-07-10; Talzenna 2026-06-01.
