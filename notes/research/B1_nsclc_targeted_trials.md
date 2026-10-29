# B1. NSCLC targeted-therapy trials: citation and data verification

Handbook: Taiwanese oncology NP handbook, lung cancer chapter
Verification date: 2026-10-29
Method: Every PMID was pulled from PubMed (NCBI E-utilities efetch/esearch, same database as the PubMed MCP tools). Numbers come from the PubMed abstract unless another source is named. Where the abstract lacked a requested number, I checked the PMC open-access full text, then the current US FDA label (openFDA), then an author-written plain-language summary in PMC. Nothing was filled from memory. Anything still missing is marked **[UNVERIFIED]**.

**Source tags used inline**
- [A] = PubMed abstract of the cited paper
- [FT] = PMC full text of the cited paper (results section, not discussion, unless stated)
- [L-xxx] = current US FDA prescribing information via openFDA (label effective date given)
- [PLS] = author plain-language summary indexed in PubMed with PMC full text
- **[UNVERIFIED]** = not stated in any source checked; do not print without checking the full paper

**Section status tags**
- **[VERIFIED]** = citation confirmed on PubMed, and the primary-endpoint result (median, HR, 95% CI where the trial reports them) confirmed from [A] or [FT]
- **[PARTIAL]** = citation confirmed, but part of the primary-endpoint result is missing from the primary source or comes only from a secondary source
- **[UNVERIFIED]** = paper not found

**APA 7 notes.** Author lists follow APA 7: all authors up to 20; for 21 or more, the first 19, an ellipsis, then the final author. Study-group bylines (for example "for the FLAURA Investigators") are left out. Titles are converted to sentence case from the PubMed title. The year is the year of the journal issue, which can differ from the e-pub year (see FLAURA, FLAURA2 OS, ALEX final OS).

---

## 0. Corrections and flags for the editor (read first)

1. **KRYSTAL-12 citation is wrong in the brief.** The Lancet paper is **Barlesi et al., 2025**, *Lancet 406*, 615–626 (PMID 40783289). Mok is the last author, not the first. No "Mok 2024 Lancet" KRYSTAL-12 paper exists on PubMed.
2. **ALEX "final OS" is not Mok 2020.** Mok 2020 (*Ann Oncol*) is an *updated* OS analysis with *final PFS*; its OS was immature (37% of events), HR 0.67. The **true final OS** is **Peters et al., 2026**, *Ann Oncol 37*(1), 92–103: median OS **81.1 vs 54.2 months, HR 0.78 (95% CI 0.56–1.08)**. The CI crosses 1, so the final OS difference is not statistically significant.
3. **Dabrafenib + trametinib: Planchard 2016 is the *pretreated* cohort (B).** The *untreated* cohort (C) is Planchard **2017**.
4. **FLAURA2 final OS is published** (Jänne et al., NEJM, issue dated **2026**, vol 394(1); e-pub 2025): 47.5 vs 37.6 months, HR 0.77 (0.61–0.96). Grade ≥3 AEs 70% vs 34%. The FLAURA2 primary abstract gives no median PFS. The 25.5 vs 16.7 months figure is confirmed only by the FDA label.
5. **MARIPOSA OS is published** (Yang et al., NEJM 2025): HR 0.75 (0.61–0.92). The abstract gives no median OS. The FDA label gives NR vs 36.7 months.
6. **LIBRETTO-431 OS signal.** The NEJM interim OS HRs were 0.96 and 1.04 (immature). An FDA reviewer commentary (Duke et al., JCO 2026) reports a later immature OS HR of **1.26, numerically favouring chemo-immunotherapy**, which it attributes partly to crossover. Worth a sentence in the handbook.
7. **Several "positive" trials had non-significant OS**, which is easy to overstate: IPASS (EGFR+ HR 1.00), AURA3 (HR 0.87), PROFILE 1014 (HR 0.760, P = .098), ALTA-1L (HR 0.81), ALEX final (HR 0.78), TROPION-Lung01 (HR 0.94).
8. **Newer papers beyond the brief that the chapter may want:** sunvozertinib phase 3 **WU-KONG28** (Zhou et al., NEJM 2026); zongertinib **first-line** cohort (Heymach et al., NEJM 2026); CROWN **7-year** update (Shaw et al., Ann Oncol 2026); PHAROS updated OS (Johnson et al., JCO 2025).
9. **Not found on PubMed as of 2026-10-29:** MARIPOSA-2 final OS; PAPILLON final OS; LAURA final OS; KRYSTAL-12 OS (not in the Lancet abstract); a stand-alone TRUST-II paper (TRUST-II is pooled with TRUST-I in Pérol et al., 2025).
10. **Errata exist; check them before quoting a number:** PROFILE 1014 (NEJM 2015), ARCHER 1050 OS (JCO 2020), ALTA-1L final (JTO 2022), entrectinib Lancet Oncol (2 errata, 2020), ARROW (2021), VISION long-term (2023), PHAROS (2024), GEOMETRY final (2024), DESTINY-Lung02 (2 errata, 2024). I did not check what each erratum changes.
11. **ARCHER 1050 excluded patients with brain metastases**, per the 2021 *Drugs* abstract ("no history of central nervous system metastases"). Dacomitinib has no CNS efficacy data from this trial.

---

# EGFR

## 1. IPASS (gefitinib vs carboplatin–paclitaxel) — [PARTIAL]

**References**
- Mok, T. S., Wu, Y.-L., Thongprasert, S., Yang, C.-H., Chu, D.-T., Saijo, N., Sunpaweravong, P., Han, B., Margono, B., Ichinose, Y., Nishiwaki, Y., Ohe, Y., Yang, J.-J., Chewaskulyong, B., Jiang, H., Duffield, E. L., Watkins, C. L., Armour, A. A., & Fukuoka, M. (2009). Gefitinib or carboplatin-paclitaxel in pulmonary adenocarcinoma. *The New England Journal of Medicine*, *361*(10), 947–957. https://doi.org/10.1056/NEJMoa0810699 — PMID 19692680
- (Final OS) Fukuoka, M., Wu, Y.-L., Thongprasert, S., Sunpaweravong, P., Leong, S.-S., Sriuranpong, V., Chao, T.-Y., Nakagawa, K., Chu, D.-T., Saijo, N., Duffield, E. L., Rukazenkov, Y., Speake, G., Jiang, H., Armour, A. A., To, K.-F., Yang, J. C.-H., & Mok, T. S. K. (2011). Biomarker analyses and final overall survival results from a phase III, randomized, open-label, first-line study of gefitinib versus carboplatin/paclitaxel in clinically selected patients with advanced non-small-cell lung cancer in Asia (IPASS). *Journal of Clinical Oncology*, *29*(21), 2866–2874. https://doi.org/10.1200/JCO.2010.33.4235 — PMID 21670455

**Design:** Phase 3, open-label, randomized, East Asia [A].
**Population:** Untreated advanced pulmonary adenocarcinoma in nonsmokers or former light smokers. Patients were *clinically* selected, not EGFR-selected [A].
**Arms:** Gefitinib 250 mg/day (n = 609) vs carboplatin AUC 5 or 6 + paclitaxel 200 mg/m² (n = 608) [A].
**Primary endpoint (PFS):** Noninferiority met and superiority shown. ITT HR 0.74 (95% CI 0.65–0.85), P < 0.001. 12-month PFS 24.9% vs 6.7% [A].
- Median PFS per arm: **[UNVERIFIED]**. Not in the abstract, and NEJM 2009 is not in PMC.

**Key subgroups:**
- EGFR mutation-positive (n = 261): PFS HR 0.48 (0.36–0.64) favouring gefitinib.
- EGFR mutation-negative (n = 176): PFS HR 2.85 (2.05–3.98), favouring chemotherapy [A].
- This is the teaching point: test before using a TKI.

**Final OS (Fukuoka 2011):** 954 deaths, 78% maturity. Overall HR 0.90 (0.79–1.02), P = .109. EGFR+ HR 1.00 (0.76–1.33). EGFR− HR 1.18 (0.86–1.63). 64.3% of EGFR+ patients in the chemotherapy arm received a later EGFR-TKI [A]. Median OS values: **[UNVERIFIED]**.
**Toxicity:**
- Gefitinib: rash/acne 66.2%, diarrhoea 46.6%.
- Chemotherapy: neurotoxicity 69.9%, neutropenia 67.1%, alopecia 58.4% [A].
- ILD rate: **[UNVERIFIED]**.

---

## 2. ARCHER 1050 (dacomitinib vs gefitinib) — [VERIFIED]

**References**
- Wu, Y.-L., Cheng, Y., Zhou, X., Lee, K. H., Nakagawa, K., Niho, S., Tsuji, F., Linke, R., Rosell, R., Corral, J., Migliorino, M. R., Pluzanski, A., Sbar, E. I., Wang, T., White, J. L., Nadanaciva, S., Sandin, R., & Mok, T. S. (2017). Dacomitinib versus gefitinib as first-line treatment for patients with EGFR-mutation-positive non-small-cell lung cancer (ARCHER 1050): A randomised, open-label, phase 3 trial. *The Lancet Oncology*, *18*(11), 1454–1466. https://doi.org/10.1016/S1470-2045(17)30608-3 — PMID 28958502
- (OS) Mok, T. S., Cheng, Y., Zhou, X., Lee, K. H., Nakagawa, K., Niho, S., Lee, M., Linke, R., Rosell, R., Corral, J., Migliorino, M. R., Pluzanski, A., Sbar, E. I., Wang, T., White, J. L., & Wu, Y.-L. (2018). Improvement in overall survival in a randomized study that compared dacomitinib with gefitinib in patients with advanced non-small-cell lung cancer and EGFR-activating mutations. *Journal of Clinical Oncology*, *36*(22), 2244–2250. https://doi.org/10.1200/JCO.2018.78.7994 — PMID 29864379. **Erratum:** *J Clin Oncol 38*(31), 3725 (2020), PMID 33113342. Content not reviewed.
- (Updated OS) Mok, T. S., Cheng, Y., Zhou, X., Lee, K. H., Nakagawa, K., Niho, S., Chawla, A., Rosell, R., Corral, J., Migliorino, M. R., Pluzanski, A., Noonan, K., Tang, Y., Pastel, M., Wilner, K. D., & Wu, Y.-L. (2021). Updated overall survival in a randomized study comparing dacomitinib with gefitinib as first-line treatment in patients with advanced non-small-cell lung cancer and EGFR-activating mutations. *Drugs*, *81*(2), 257–266. https://doi.org/10.1007/s40265-020-01441-6 — PMID 33331989

**Design:** Phase 3, open-label, randomized 1:1, 71 centres in 7 countries/regions [A].
**Population:** Newly diagnosed advanced NSCLC with EGFR exon 19 deletion or L858R. Patients with a history of CNS metastases were **excluded** [A, Drugs 2021].
**Arms:** Dacomitinib 45 mg/day (n = 227) vs gefitinib 250 mg/day (n = 225) [A].
**Primary endpoint (PFS by masked independent review):** 14.7 months (95% CI 11.1–16.6) vs 9.2 months (9.1–11.0). HR 0.59 (0.47–0.74), p < 0.0001. Median PFS follow-up 22.1 months [A].
**OS:**
- 2018: HR 0.760 (0.582–0.993), P = .044. Median 34.1 vs 26.8 months (CIs not in abstract). 30-month OS 56.2% vs 46.3%. Median follow-up 31.3 months [A].
- 2021 ad hoc update (median follow-up 47.9 months): HR 0.748 (0.591–0.947), P = 0.0155. Median 34.1 vs 27.0 months. Patients with a dose reduction on dacomitinib (n = 154): median OS 42.5 months [A].

**CNS:** Not evaluable; brain metastases were excluded.
**Toxicity:**
- Grade 3–4 (primary paper): dermatitis acneiform 14% vs 0%; diarrhoea 8% vs 1%; ALT increase 1% vs 8%.
- Treatment-related SAEs 9% vs 4%. Two treatment-related deaths with dacomitinib [A].
- All-grade with dacomitinib (2021): diarrhoea 87.7%, paronychia 61.7%, dermatitis acneiform 49.3%, stomatitis 43.6% [A].

---

## 3. FLAURA (osimertinib vs gefitinib/erlotinib) — [VERIFIED]

**References**
- Soria, J.-C., Ohe, Y., Vansteenkiste, J., Reungwetwattana, T., Chewaskulyong, B., Lee, K. H., Dechaphunkul, A., Imamura, F., Nogami, N., Kurata, T., Okamoto, I., Zhou, C., Cho, B. C., Cheng, Y., Cho, E. K., Voon, P. J., Planchard, D., Su, W.-C., Gray, J. E., . . . Ramalingam, S. S. (2018). Osimertinib in untreated EGFR-mutated advanced non-small-cell lung cancer. *The New England Journal of Medicine*, *378*(2), 113–125. https://doi.org/10.1056/NEJMoa1713137 — PMID 29151359 (e-pub 2017, print 2018)
- (OS) Ramalingam, S. S., Vansteenkiste, J., Planchard, D., Cho, B. C., Gray, J. E., Ohe, Y., Zhou, C., Reungwetwattana, T., Cheng, Y., Chewaskulyong, B., Shah, R., Cobo, M., Lee, K. H., Cheema, P., Tiseo, M., John, T., Lin, M.-C., Imamura, F., Kurata, T., . . . Soria, J.-C. (2020). Overall survival with osimertinib in untreated, EGFR-mutated advanced NSCLC. *The New England Journal of Medicine*, *382*(1), 41–50. https://doi.org/10.1056/NEJMoa1913662 — PMID 31751012
- (CNS) Reungwetwattana, T., Nakagawa, K., Cho, B. C., Cobo, M., Cho, E. K., Bertolini, A., Bohnet, S., Zhou, C., Lee, K. H., Nogami, N., Okamoto, I., Leighl, N., Hodge, R., McKeown, A., Brown, A. P., Rukazenkov, Y., Ramalingam, S. S., & Vansteenkiste, J. (2018). CNS response to osimertinib versus standard epidermal growth factor receptor tyrosine kinase inhibitors in patients with untreated EGFR-mutated advanced non-small-cell lung cancer. *Journal of Clinical Oncology*, *36*(33), 3290–3297. https://doi.org/10.1200/JCO.2018.78.3118 — PMID 30153097. The PubMed record has only the ahead-of-print locator; volume, issue and pages come from Crossref.

**Design:** Phase 3, double-blind, randomized 1:1 [A].
**Population:** 556 patients, previously untreated advanced NSCLC with EGFR exon 19 deletion or L858R [A].
**Arms:** Osimertinib 80 mg once daily vs standard EGFR-TKI (gefitinib 250 mg once daily or erlotinib 150 mg once daily) [A].
**Primary endpoint (investigator PFS):** 18.9 vs 10.2 months. HR 0.46 (0.37–0.57), P < 0.001 [A]. Median CIs: 18.9 (15.2–21.4) vs 10.2 (9.6–11.1) [L-Tagrisso, 2024-09-25].
**Secondary:**
- ORR 80% vs 76% (OR 1.27, P = 0.24).
- DoR 17.2 (13.8–22.0) vs 8.5 (7.3–9.8) months [A].

**Final OS (Ramalingam 2020):** 38.6 (34.5–41.8) vs 31.8 (26.6–36.0) months. HR 0.80 (95.05% CI 0.64–1.00), P = 0.046. At 3 years, 28% vs 9% were still on trial treatment [A].
**CNS (Reungwetwattana 2018):**
- 128 patients with CNS lesions at baseline.
- CNS PFS not reached (16.5–NC) vs 13.9 months; HR 0.48 (0.26–0.86), P = .014 (nominal).
- CNS ORR 91% vs 68% in patients with ≥1 measurable lesion (n = 41).
- CNS ORR 66% vs 43% in patients with measurable and/or non-measurable lesions [A].

**Toxicity:**
- Grade ≥3 AEs 34% vs 45% (primary analysis); 42% vs 47% (OS analysis) [A].
- ILD and QTc rates: **[UNVERIFIED]**; not in the abstracts.

---

## 4. FLAURA2 (osimertinib ± platinum–pemetrexed) — [PARTIAL]

**References**
- Planchard, D., Jänne, P. A., Cheng, Y., Yang, J. C.-H., Yanagitani, N., Kim, S.-W., Sugawara, S., Yu, Y., Fan, Y., Geater, S. L., Laktionov, K., Lee, C. K., Valdiviezo, N., Ahmed, S., Maurel, J.-M., Andrasina, I., Goldman, J., Ghiorghiu, D., Rukazenkov, Y., . . . Kobayashi, K. (2023). Osimertinib with or without chemotherapy in EGFR-mutated advanced NSCLC. *The New England Journal of Medicine*, *389*(21), 1935–1948. https://doi.org/10.1056/NEJMoa2306434 — PMID 37937763
- (Final OS) Jänne, P. A., Planchard, D., Kobayashi, K., Yang, J. C.-H., Liu, Y., Valdiviezo, N., Kim, T. M., Jiang, L., Kagamu, H., Yanagitani, N., Wang, J., Biswas, B., Poltoratskiy, A., Neron, Y., Rojas, C., Koubkova, L., Escriu, C., Ezeife, D. A., Mann, H., . . . Lee, C. K. (2026). Survival with osimertinib plus chemotherapy in EGFR-mutated advanced NSCLC. *The New England Journal of Medicine*, *394*(1), 27–38. https://doi.org/10.1056/NEJMoa2510308 — PMID 41104938. The brief says "2025": the paper was e-published in 2025, but the issue is dated 2026.

**Design:** Phase 3, international, open-label, randomized 1:1 [A].
**Population:** 557 patients with untreated advanced NSCLC with EGFR exon 19 deletion or L858R [A].
**Arms:**
- Osimertinib 80 mg once daily + pemetrexed 500 mg/m² + cisplatin 75 mg/m² or carboplatin (pharmacologically guided dose) [A]. The label specifies carboplatin AUC 5, given for 4 cycles, followed by osimertinib + pemetrexed maintenance q3w [L-Tagrisso].
- vs osimertinib 80 mg once daily [A].

**Primary endpoint (investigator PFS):**
- HR 0.62 (0.49–0.79), P < 0.001. 24-month PFS 57% vs 41%. BICR HR 0.62 (0.48–0.80) [A].
- Median PFS is not in the abstract. The FDA label gives **25.5 (24.7–NE) vs 16.7 (14.1–21.3) months** [L-Tagrisso, 2024-09-25]. This is the only source checked.

**Secondary (primary paper):** ORR 83% vs 76%. DoR 24.0 (20.9–27.8) vs 15.3 (12.7–19.4) months [A].
**Final OS (Jänne 2026):** 47.5 vs 37.6 months. HR 0.77 (95% CI 0.61–0.96), P = 0.02 [A]. CIs for the medians are not in the abstract.
**CNS:** Exploratory BICR analysis, measurable CNS lesions: CNS ORR 80% (64–91) vs 76% (60–89); CNS CR 48% vs 16% [L-Tagrisso].
**Toxicity:**
- Grade ≥3 AEs from any cause: 70% vs 34%.
- Osimertinib discontinued for AEs: 12% vs 7% [A, OS paper].
- The primary paper attributes the excess mainly to known chemotherapy toxicities [A].

---

## 5. MARIPOSA (amivantamab + lazertinib vs osimertinib) — [VERIFIED]

**References**
- Cho, B. C., Lu, S., Felip, E., Spira, A. I., Girard, N., Lee, J.-S., Lee, S.-H., Ostapenko, Y., Danchaivijitr, P., Liu, B., Alip, A., Korbenfeld, E., Mourão Dias, J., Besse, B., Lee, K.-H., Xiong, H., How, S.-H., Cheng, Y., Chang, G.-C., . . . Hayashi, H. (2024). Amivantamab plus lazertinib in previously untreated EGFR-mutated advanced NSCLC. *The New England Journal of Medicine*, *391*(16), 1486–1498. https://doi.org/10.1056/NEJMoa2403614 — PMID 38924756
- (OS) Yang, J. C.-H., Lu, S., Hayashi, H., Felip, E., Spira, A. I., Girard, N., Kim, Y. J., Lee, S.-H., Ostapenko, Y., Danchaivijitr, P., Liu, B., Alip, A., Korbenfeld, E., Mourão Dias, J., Besse, B., Passaro, A., Lee, K.-H., Xiong, H., How, S.-H., . . . Cho, B. C. (2025). Overall survival with amivantamab-lazertinib in EGFR-mutated advanced NSCLC. *The New England Journal of Medicine*, *393*(17), 1681–1693. https://doi.org/10.1056/NEJMoa2503001 — PMID 40923797

**Design:** Phase 3, randomized 2:2:1. Amivantamab–lazertinib was open-label; osimertinib and lazertinib alone were blinded [A].
**Population:** 1,074 patients with untreated locally advanced or metastatic NSCLC with EGFR exon 19 deletion or L858R. Randomized: 429 amivantamab–lazertinib, 429 osimertinib, 216 lazertinib [A].
**Arms (doses are not in the abstract; taken from the label):**
- Amivantamab IV 1,050 mg (<80 kg) or 1,400 mg (≥80 kg) weekly for 4 weeks, then every 2 weeks from week 5, plus lazertinib 240 mg PO once daily.
- vs osimertinib 80 mg once daily [L-Rybrevant, 2025-11-11].

**Primary endpoint (BICR PFS):** 23.7 vs 16.6 months. HR 0.70 (0.58–0.85), P < 0.001 [A]. Median CIs: 23.7 (19.1–27.7) vs 16.6 (14.8–18.5) [L-Rybrevant].
**Secondary:**
- ORR 86% vs 85%.
- DoR 25.8 vs 16.8 months [A].
- Interim OS HR 0.80 (0.61–1.05) [A].

**OS (Yang 2025):** Median follow-up 37.8 months. HR 0.75 (0.61–0.92), P = 0.005. 3-year OS 60% vs 51% [A]. Median OS: not reached (42.9–NE) vs 36.7 (33.4–41.0) months [L-Rybrevant]. At cutoff, 38% vs 28% were still on assigned treatment [A].
**CNS:** Exploratory intracranial ORR 68% vs 69%; intracranial CR 55% vs 52% [L-Rybrevant].
**Toxicity:**
- From the trial abstracts:
  - Grade ≥3 AEs 80% vs 52%, mainly skin, VTE and infusion-related [A, OS paper].
  - Discontinuation of all agents for treatment-related AEs: 10% vs 3% [A].
- From the FDA label, amivantamab–lazertinib arm [L-Rybrevant]:
  - **Infusion-related reactions 63%** (grade 3 5%, grade 4 1%); 4.5% discontinued amivantamab.
  - **VTE 36%** (grade 3 10%, grade 4 0.5%, 2 fatal); median onset 84 days. **Prophylactic anticoagulation is recommended for the first 4 months.**
  - **Rash 86%** (grade 3 26%).
  - **ILD/pneumonitis 3.1%** (1 fatal).

---

## 6. MARIPOSA-2 (amivantamab + chemo ± lazertinib after osimertinib) — [PARTIAL]

**Reference**
- Passaro, A., Wang, J., Wang, Y., Lee, S.-H., Melosky, B., Shih, J.-Y., Wang, J., Azuma, K., Juan-Vidal, O., Cobo, M., Felip, E., Girard, N., Cortot, A. B., Califano, R., Cappuzzo, F., Owen, S., Popat, S., Tan, J.-L., Salinas, J., . . . Cho, B. C. (2024). Amivantamab plus chemotherapy with and without lazertinib in EGFR-mutant advanced NSCLC after disease progression on osimertinib: Primary results from the phase III MARIPOSA-2 study. *Annals of Oncology*, *35*(1), 77–90. https://doi.org/10.1016/j.annonc.2023.10.117 — PMID 37879444

**Design:** Phase 3, randomized 2:2:1 to amivantamab–lazertinib–chemotherapy (LACP), chemotherapy (CP), or amivantamab–chemotherapy (ACP). Dual primary endpoint: BICR PFS for each amivantamab arm vs chemotherapy [A].
**Population:** 657 patients with EGFR exon 19 deletion or L858R locally advanced or metastatic NSCLC that progressed on osimertinib [A].
**Arms (doses are not in the abstract; taken from the label):**
- Amivantamab 1,400 mg (<80 kg) or 1,750 mg (≥80 kg) weekly for 4 weeks, then 1,750 or 2,100 mg every 3 weeks from week 7.
- Carboplatin AUC 5 every 3 weeks for up to 12 weeks, plus pemetrexed [L-Rybrevant].
- Because of haematologic toxicity, the LACP regimen was changed mid-study so that lazertinib starts after carboplatin is finished [A].

**Primary endpoint (BICR PFS):**
- ACP vs CP: median 6.3 vs 4.2 months, HR 0.48, P < 0.001 [A]. CIs: HR 0.48 (0.36–0.64); medians 6.3 (5.6–8.4) vs 4.2 (4.0–4.4) [L-Rybrevant].
- LACP vs CP: median 8.3 vs 4.2 months, HR 0.44, P < 0.001 [A]. 95% CI **[UNVERIFIED]**.
- Investigator-assessed PFS: HR 0.41 (ACP) and 0.38 (LACP) [A].

**Secondary:** ORR 64% (ACP) and 63% (LACP) vs 36% [A].
**CNS:** Intracranial PFS 12.5 (ACP) and 12.8 (LACP) vs 8.3 months; HR 0.55 and 0.58 [A].
**OS:** Final OS **[UNVERIFIED]**; no OS publication found on PubMed (searched 2026-10-29).
**Toxicity:**
- Mainly haematologic, EGFR-related and MET-related AEs. ACP caused fewer haematologic AEs than LACP [A].
- Label, pooled amivantamab + carboplatin–pemetrexed: IRR 50% (grade 3 3.2%); rash 82% (grade 3 15%); ILD 2.1% [L-Rybrevant].

---

## 7. PAPILLON (amivantamab + chemo, EGFR exon 20 insertion) — [VERIFIED]

**References**
- Zhou, C., Tang, K.-J., Cho, B. C., Liu, B., Paz-Ares, L., Cheng, S., Kitazono, S., Thiagarajan, M., Goldman, J. W., Sabari, J. K., Sanborn, R. E., Mansfield, A. S., Hung, J.-Y., Boyer, M., Popat, S., Mourão Dias, J., Felip, E., Majem, M., Gumus, M., . . . Girard, N. (2023). Amivantamab plus chemotherapy in NSCLC with EGFR exon 20 insertions. *The New England Journal of Medicine*, *389*(22), 2039–2051. https://doi.org/10.1056/NEJMoa2306441 — PMID 37870976
- (Asia subgroup, optional) Zhou, C., Tang, K.-J., Liu, B., Kim, S.-W., Kitazono, S., Ono, A., Thiagarajan, M., Hung, J.-Y., Boyer, M., Çİl, T., Yao, Y., Nagarkar, R., Xie, J., Bhattacharya, A., Wortman-Vayn, H., Baig, M., Agrawal, T., Lorenzini, P., Lee, S.-H., & Cho, B. C. (2026). Amivantamab plus chemotherapy versus chemotherapy for first-line treatment of participants with EGFR exon 20 insertion-mutated advanced non-small cell lung cancer: PAPILLON Asia subgroup analysis. *Lung Cancer*, *213*, 109302. https://doi.org/10.1016/j.lungcan.2026.109302 — PMID 41671628

**Design:** Phase 3, international, randomized 1:1. Patients in the chemotherapy arm could cross over to amivantamab monotherapy at progression [A].
**Population:** 308 patients with untreated advanced NSCLC with EGFR exon 20 insertion: 153 amivantamab–chemotherapy, 155 chemotherapy [A].
**Arms:**
- Amivantamab IV 1,400 or 1,750 mg weekly for 4 weeks, then 1,750 or 2,100 mg every 3 weeks from week 7 (weight cut-off 80 kg), plus carboplatin AUC 5 and pemetrexed [L-Rybrevant].
- vs carboplatin + pemetrexed.

**Primary endpoint (BICR PFS):** 11.4 vs 6.7 months. HR 0.40 (0.30–0.53), P < 0.001. 18-month PFS 31% vs 3% [A]. Median CIs: 11.4 (9.8–13.7) vs 6.7 (5.6–7.3) [L-Rybrevant].
**Secondary:**
- ORR 73% vs 47% (rate ratio 1.50) [A].
- Interim OS (33% maturity): HR 0.67 (0.42–1.09), P = 0.11 [A].
- Final OS: **[UNVERIFIED]**; not found on PubMed.

**Asia subgroup (n = 186):**
- PFS 11.5 vs 5.6 months, HR 0.34 (0.23–0.49).
- Interim OS not estimable vs 24.4 months, HR 0.65 (0.34–1.24).
- 73% crossover [A, Lung Cancer 2026].

**Toxicity:**
- Reversible haematologic and EGFR-related toxicities; 7% discontinued amivantamab for adverse reactions [A].
- IRR rate in PAPILLON alone: **[UNVERIFIED]**. The label gives a pooled amivantamab + chemotherapy IRR rate of 50%.

---

## 8. AURA3 (osimertinib vs platinum–pemetrexed, T790M) — [VERIFIED]

**References**
- Mok, T. S., Wu, Y.-L., Ahn, M.-J., Garassino, M. C., Kim, H. R., Ramalingam, S. S., Shepherd, F. A., He, Y., Akamatsu, H., Theelen, W. S. M. E., Lee, C. K., Sebastian, M., Templeton, A., Mann, H., Marotti, M., Ghiorghiu, S., & Papadimitrakopoulou, V. A. (2017). Osimertinib or platinum-pemetrexed in EGFR T790M-positive lung cancer. *The New England Journal of Medicine*, *376*(7), 629–640. https://doi.org/10.1056/NEJMoa1612674 — PMID 27959700 (PMC6762027)
- (CNS) Wu, Y.-L., Ahn, M.-J., Garassino, M. C., Han, J.-Y., Katakami, N., Kim, H. R., Hodge, R., Kaur, P., Brown, A. P., Ghiorghiu, D., Papadimitrakopoulou, V. A., & Mok, T. S. K. (2018). CNS efficacy of osimertinib in patients with T790M-positive advanced non-small-cell lung cancer: Data from a randomized phase III trial (AURA3). *Journal of Clinical Oncology*, *36*(26), 2702–2709. https://doi.org/10.1200/JCO.2018.77.9363 — PMID 30059262
- (OS) Papadimitrakopoulou, V. A., Mok, T. S., Han, J.-Y., Ahn, M.-J., Delmonte, A., Ramalingam, S. S., Kim, S. W., Shepherd, F. A., Laskin, J., He, Y., Akamatsu, H., Theelen, W. S. M. E., Su, W.-C., John, T., Sebastian, M., Mann, H., Miranda, M., Laus, G., Rukazenkov, Y., & Wu, Y.-L. (2020). Osimertinib versus platinum-pemetrexed for patients with EGFR T790M advanced NSCLC and progression on a prior EGFR-tyrosine kinase inhibitor: AURA3 overall survival analysis. *Annals of Oncology*, *31*(11), 1536–1544. https://doi.org/10.1016/j.annonc.2020.08.2100 — PMID 32861806

**Design:** Phase 3, international, open-label, randomized 2:1 [A].
**Population:** 419 patients with T790M-positive advanced NSCLC that progressed during first-line EGFR-TKI therapy [A].
**Arms:**
- Osimertinib 80 mg once daily.
- vs pemetrexed 500 mg/m² + carboplatin AUC 5 or cisplatin 75 mg/m² every 3 weeks for up to 6 cycles; maintenance pemetrexed allowed [A].

**Primary endpoint (investigator PFS):** 10.1 vs 4.4 months. HR 0.30 (0.23–0.41), P < 0.001 [A].
**Secondary:** ORR 71% (65–76) vs 31% (24–40) [A].
**CNS:**
- 144 patients with CNS metastases: PFS 8.5 vs 4.2 months, HR 0.32 (0.21–0.49) [A].
- CNS paper: CNS ORR (measurable lesions) 70% vs 31%; CNS PFS 11.7 vs 5.6 months, HR 0.32 (0.15–0.69) [A, Wu 2018].

**OS (2020):**
- HR **0.87 (0.67–1.12), P = 0.277; not significant**.
- Median 26.8 (23.5–31.5) vs 22.5 (20.2–28.8) months.
- 73% of the chemotherapy arm (99/136) crossed over; crossover-adjusted HR 0.54 (0.18–1.6) [A].

**Toxicity:**
- Grade ≥3 AEs 23% vs 47% [A].
- **ILD-like events 4%** (10 patients: 9 grade 1–2, 1 death) vs 1%.
- **QT prolongation 4%** vs 1% [FT].

---

## 9. COCOON (dermatologic prophylaxis with amivantamab + lazertinib) — [VERIFIED]

**Reference**
- Cho, B. C., Li, W., Spira, A. I., Sauder, M., Feldman, J., Bozorgmehr, F., Mak, M., Smith, J., Voon, P. J., Liu, B., Tian, P., Tan, J.-L., Yang, C.-T., Shih, J.-Y., Karadurmus, N., Cundom, J. E., Bertollo, G., Cicin, I., Nieva, J., . . . Girard, N. (2025). Enhanced versus standard dermatologic management with amivantamab-lazertinib in EGFR-mutated advanced NSCLC: The COCOON global randomized controlled trial. *Journal of Thoracic Oncology*, *20*(10), 1517–1530. https://doi.org/10.1016/j.jtho.2025.07.117 — PMID 40923969

**Design:** Phase 2, randomized 1:1 (NCT06120140) [A].
**Population:** 201 patients with previously untreated EGFR-mutant locally advanced or metastatic NSCLC starting IV amivantamab + oral lazertinib: 99 COCOON management, 102 standard-of-care management [A]. Amivantamab/lazertinib doses are not stated in the abstract **[UNVERIFIED]**.
**COCOON regimen (nursing-relevant) [A]:**
- Oral doxycycline or minocycline 100 mg twice daily, weeks 1–12.
- Clindamycin 1% applied to the scalp daily, weeks 13–52.
- Chlorhexidine 4% applied to fingernails and toenails daily.
- Ceramide-based moisturizer on body and face at least daily.

**Primary endpoint (grade ≥2 dermatologic AEs of interest by week 12):** 42% vs 75%. OR 0.24 (95% CI 0.13–0.45), p < 0.0001. Median follow-up 7.1 months [A].
**Secondary:**
- Face/body events, excluding paronychia: 26% vs 60%.
- Scalp events: 10% vs 26% (p = 0.0049).
- Benefit maintained at 6 months. Patient-reported outcomes favoured COCOON [A].

**Note:** The abstract does not report paronychia rates **[UNVERIFIED]**. A 2026 commentary (Furuya, *J Thorac Dis*, PMID 42583437) is titled "the unresolved challenge of paronychia in the COCOON trial", which suggests paronychia was not well prevented. Check the full text before writing patient-education material.

---

## 10. ADAURA (adjuvant osimertinib) — [VERIFIED]

**References**
- Wu, Y.-L., Tsuboi, M., He, J., John, T., Grohe, C., Majem, M., Goldman, J. W., Laktionov, K., Kim, S.-W., Kato, T., Vu, H.-V., Lu, S., Lee, K.-Y., Akewanlop, C., Yu, C.-J., de Marinis, F., Bonanno, L., Domine, M., Shepherd, F. A., . . . Herbst, R. S. (2020). Osimertinib in resected EGFR-mutated non-small-cell lung cancer. *The New England Journal of Medicine*, *383*(18), 1711–1723. https://doi.org/10.1056/NEJMoa2027071 — PMID 32955177
- (OS) Tsuboi, M., Herbst, R. S., John, T., Kato, T., Majem, M., Grohé, C., Wang, J., Goldman, J. W., Lu, S., Su, W.-C., de Marinis, F., Shepherd, F. A., Lee, K. H., Le, N. T., Dechaphunkul, A., Kowalski, D., Poole, L., Bolanos, A., Rukazenkov, Y., & Wu, Y.-L. (2023). Overall survival with osimertinib in resected EGFR-mutated NSCLC. *The New England Journal of Medicine*, *389*(2), 137–147. https://doi.org/10.1056/NEJMoa2304594 — PMID 37272535

**Design:** Phase 3, double-blind, placebo-controlled [A].
**Population:** 682 patients with completely resected stage IB–IIIA EGFR mutation-positive NSCLC: 339 osimertinib, 343 placebo [A]. Whether adjuvant chemotherapy was allowed is not stated in the abstract.
**Arms:** Osimertinib 80 mg once daily vs placebo, for up to 3 years [A].
**Primary endpoint (investigator DFS, stage II–IIIA):** 24-month DFS 90% (84–93) vs 44% (37–51). HR 0.17 (99.06% CI 0.11–0.26), P < 0.001 [A]. Median DFS: **[UNVERIFIED]**; not in the abstract.
**Secondary:**
- Stage IB–IIIA: 24-month DFS 89% vs 52%, HR 0.20 (99.12% CI 0.14–0.30).
- CNS: 24-month CNS DFS 98% vs 85%, HR 0.18 (95% CI 0.10–0.33) [A].

**OS (Tsuboi 2023):**
- Stage II–IIIA: 5-year OS 85% vs 73%, HR 0.49 (95.03% CI 0.33–0.73), P < 0.001.
- Stage IB–IIIA: 88% vs 78%, HR 0.49 (95.03% CI 0.34–0.70) [A].

**Toxicity:** No new safety concerns [A]. ILD rate: **[UNVERIFIED]**.

---

## 11. LAURA (osimertinib after chemoradiotherapy, stage III) — [VERIFIED]

**References**
- Lu, S., Kato, T., Dong, X., Ahn, M.-J., Quang, L.-V., Soparattanapaisarn, N., Inoue, T., Wang, C.-L., Huang, M., Yang, J. C.-H., Cobo, M., Özgüroğlu, M., Casarini, I., Khiem, D.-V., Sriuranpong, V., Cronemberger, E., Takahashi, T., Runglodvatana, Y., Chen, M., . . . Ramalingam, S. S. (2024). Osimertinib after chemoradiotherapy in stage III EGFR-mutated NSCLC. *The New England Journal of Medicine*, *391*(7), 585–597. https://doi.org/10.1056/NEJMoa2402614 — PMID 38828946
- (CNS) Lu, S., Ahn, M.-J., Reungwetwattana, T., Özgüroğlu, M., Kato, T., Yang, J. C.-H., Huang, M., Fujiki, F., Inoue, T., Quang, L.-V., Sriuranpong, V., Vicente, D., Fuentes, C., Chaudhry, A. A., Poole, L., Armenteros Monterroso, E., Rukazenkov, Y., van der Gronde, T., & Ramalingam, S. S. (2024). Osimertinib after definitive chemoradiotherapy in unresectable stage III epidermal growth factor receptor-mutated non-small-cell lung cancer: Analyses of central nervous system efficacy and distant progression from the phase III LAURA study. *Annals of Oncology*, *35*(12), 1116–1125. https://doi.org/10.1016/j.annonc.2024.08.2243 — PMID 39289145

**Design:** Phase 3, double-blind, placebo-controlled, randomized 2:1 [A].
**Population:** 216 patients with unresectable stage III EGFR-mutated NSCLC without progression during or after definitive platinum-based chemoradiotherapy: 143 osimertinib, 73 placebo [A].
**Arms:** Osimertinib 80 mg daily vs placebo, until BICR-confirmed progression [A, Ann Oncol].
**Primary endpoint (BICR PFS):** 39.1 vs 5.6 months. HR 0.16 (0.10–0.24), P < 0.001. 12-month PFS 74% vs 22% [A].
**OS (interim, 20% maturity):** 36-month OS 84% vs 74%. HR 0.81 (0.42–1.56), P = 0.53 [A]. Final OS: **[UNVERIFIED]**; not found.
**CNS:**
- CNS PFS not reached vs 14.9 months, HR 0.17 (0.09–0.32).
- 12-month CNS progression 9% vs 36%.
- Time to distant metastasis HR 0.21 (0.11–0.38) [A, Ann Oncol].

**Toxicity:**
- Grade ≥3 AEs 35% vs 12%.
- **Radiation pneumonitis 48% vs 38%**, mostly grade 1–2 [A]. Useful for NP monitoring.

---

## 12. Sunvozertinib for EGFR exon 20 insertion — [VERIFIED]

**References**
- (Phase 3, first-line) Zhou, C., Greillier, L., Liu, G., John, T., Xing, L., Kowalski, D., Memmott, R. M., Yazici, O., Sun, M., Shu, C. A., Pons-Tostivint, E., Fan, Y., Fernandez-Hinojal, G., Shum, E., Wang, M., Bertolini, F., Camidge, D. R., Zhou, C., Doucet, L., . . . Heymach, J. V. (2026). First-line sunvozertinib in NSCLC with EGFR exon 20 insertion mutations. *The New England Journal of Medicine*, *395*(8), 765–775. https://doi.org/10.1056/NEJMoa2604461 — PMID 42212913 (WU-KONG28)
- (WU-KONG1B) Yang, J. C.-H., Wang, M., Doucet, L., Fan, Y., Lv, D., Sun, M., Huang, D., Greillier, L., Planchard, D., Hong, Q., Mazieres, J., Felip, E., Li, X., Hu, Y., Fang, J., Bazhenova, L., Ghiringhelli, F., Cobo Dols, M. A., Rodriguez, L. P.-A., . . . Jänne, P. A. (2025). Phase II dose-randomized study of sunvozertinib in platinum-pretreated non-small cell lung cancer with epidermal growth factor receptor exon 20 insertion mutations (WU-KONG1B). *Journal of Clinical Oncology*, *43*(29), 3198–3208. https://doi.org/10.1200/JCO-25-00788 — PMID 40923280
- (WU-KONG6) Wang, M., Fan, Y., Sun, M., Wang, Y., Zhao, Y., Jin, B., Hu, Y., Han, Z., Song, X., Liu, A., Tang, K., Ding, C., Liang, L., Wu, L., Gao, J., Wang, J., Cheng, Y., Zhou, J., He, Y., . . . Shi, Y. (2024). Sunvozertinib for patients in China with platinum-pretreated locally advanced or metastatic non-small-cell lung cancer and EGFR exon 20 insertion mutation (WU-KONG6): Single-arm, open-label, multicentre, phase 2 trial. *The Lancet Respiratory Medicine*, *12*(3), 217–224. https://doi.org/10.1016/S2213-2600(23)00379-X — PMID 38101437

**WU-KONG28 (phase 3, first line) [A]:**
- Design and population: international, randomized 1:1; advanced nonsquamous NSCLC with EGFR exon 20 insertion; 324 patients (163 sunvozertinib vs 161 carboplatin–pemetrexed); crossover allowed.
- Sunvozertinib dose: not stated in the abstract **[UNVERIFIED]**.
- Primary BICR PFS: 10.3 vs 7.5 months, HR 0.65 (0.50–0.85), P < 0.001. 12-month PFS 46.1% vs 26.7%.
- OS immature (38.9% maturity).
- ORR 58.9% vs 31.1%; DoR 11.2 vs 7.1 months.
- Grade ≥3 AEs 75.5% vs 56.7%. Most common grade ≥3 with sunvozertinib: CK increase, diarrhoea, anaemia. No treatment-related deaths.

**WU-KONG1B (phase 2, platinum-pretreated, randomized 200 vs 300 mg once daily) [A]:**
- Confirmed ORR by IRC: 45.9% (200 mg randomized, n = 85); 47.2% (300 mg randomized, n = 89); 45.8% (all 300 mg, n = 107). 97.5% CIs reported.
- 300 vs 200 mg, patients with baseline brain metastases: ORR 52.4% vs 28.6%.
- 300 vs 200 mg, patients with prior amivantamab: ORR 41.7% vs 25%.
- DoR 13.8 vs 11.1 months.
- Grade ≥3 TRAEs, 200 vs 300 mg: diarrhoea 2.2% vs 18%; CPK increase 6.6% vs 12.6%; anaemia 4.4% vs 6.3%. Safety was more favourable at 200 mg.

**WU-KONG6 (China, phase 2, 300 mg once daily, n = 104) [A]:**
- ORR 61% (50–71); all responses were partial.
- Grade ≥3 TRAEs: CPK increase 17%, diarrhoea 8%, anaemia 6%.
- **Serious treatment-related ILD 5%** (5/104).

---

## 13. TROPION-Lung01 and pooled EGFR-mutant Dato-DXd analysis (TROPION-Lung05) — [VERIFIED]

**References**
- Ahn, M.-J., Tanaka, K., Paz-Ares, L., Cornelissen, R., Girard, N., Pons-Tostivint, E., Vicente Baz, D., Sugawara, S., Cobo, M., Pérol, M., Mascaux, C., Poddubskaya, E., Kitazono, S., Hayashi, H., Hong, M. H., Felip, E., Hall, R., Juan-Vidal, O., Brungs, D., . . . Sands, J. (2025). Datopotamab deruxtecan versus docetaxel for previously treated advanced or metastatic non-small cell lung cancer: The randomized, open-label phase III TROPION-Lung01 study. *Journal of Clinical Oncology*, *43*(3), 260–272. https://doi.org/10.1200/JCO-24-01544 — PMID 39250535 (PMC11771353)
- (TROPION-Lung05) Sands, J., Ahn, M.-J., Lisberg, A., Cho, B. C., Blumenschein, G., Shum, E., Pons Tostivint, E., Goto, Y., Yoh, K., Heist, R., Shimizu, J., Lee, J.-S., Baas, P., Planchard, D., Pérol, M., Felip, E., Su, W.-C., Zebger-Gong, H., Lan, L., . . . Paz-Ares, L. (2025). Datopotamab deruxtecan in advanced or metastatic non-small cell lung cancer with actionable genomic alterations: Results from the phase II TROPION-Lung05 study. *Journal of Clinical Oncology*, *43*(10), 1254–1265. https://doi.org/10.1200/JCO-24-01349 — PMID 39761483
- (Pooled EGFR) Ahn, M.-J., Lisberg, A., Goto, Y., Sands, J., Hong, M. H., Paz-Ares, L., Pons-Tostivint, E., Pérol, M., Felip, E., Sugawara, S., Hayashi, H., Cho, B. C., Blumenschein, G., Shum, E., Lee, J.-S., Heist, R. S., Cornelissen, R., Chang, W.-C., Kowalski, D., . . . Okamoto, I. (2025). A pooled analysis of datopotamab deruxtecan in patients with EGFR-mutated NSCLC. *Journal of Thoracic Oncology*, *20*(11), 1669–1682. https://doi.org/10.1016/j.jtho.2025.06.002 — PMID 40516821

**TROPION-Lung01 [A]:**
- Design: phase 3, open-label, randomized; previously treated advanced or metastatic NSCLC; 299 Dato-DXd vs 305 docetaxel. Dual primary endpoints: PFS and OS.
- Arms: Dato-DXd 6 mg/kg vs docetaxel 75 mg/m², both every 3 weeks.
- PFS: 4.4 (4.2–5.6) vs 3.7 (2.9–4.2) months, HR 0.75 (0.62–0.91), P = .004.
- OS: 12.9 (11.0–13.9) vs 11.8 (10.1–12.8) months, HR 0.94 (0.78–1.14), P = .530. **Not significant.**
- Nonsquamous: PFS 5.5 vs 3.6 months, HR 0.63 (0.51–0.79); OS 14.6 vs 12.3 months, HR 0.84 (0.68–1.05).
- Squamous: PFS 2.8 vs 3.9 months, HR 1.41 (0.95–2.08); OS 7.6 vs 9.4 months, HR 1.32 (0.91–1.92). Numerically worse.
- Grade ≥3 TRAEs 25.6% vs 42.1%.
- **Adjudicated drug-related ILD/pneumonitis 8.8% vs 4.1%.**

**TROPION-Lung05 [A]:**
- Phase 2, single-arm; NSCLC with actionable genomic alterations; 137 patients (56.9% EGFR, 24.8% ALK); 71.5% had ≥3 prior lines.
- Confirmed ORR 35.8% overall; EGFR 43.6% (32.4–55.3); ALK 23.5% (10.7–41.2). DoR 7.0 months.
- Grade ≥3 TRAEs 28.5%.
- **Stomatitis 56.2%** (grade ≥3 9.5%).
- Adjudicated treatment-related ILD 3.6% (5 patients), including 1 grade 5 (0.7%).

**Pooled EGFR-mutant analysis (TL05 + TL01, n = 117) [A]:**
- Heavily pretreated (median 3 prior lines); 69% Asian.
- Confirmed ORR 43% (34–52); 5 CRs (4%).
- DoR 7.0 (4.2–9.8) months; PFS 5.8 (5.4–8.2) months; OS 15.6 (13.1–19.0) months.
- Grade ≥3 TRAEs 23%; SAEs 6%.
- ILD rate in the EGFR pool: **[UNVERIFIED]**; not in the abstract.

**Regulatory/safety context [L-Datroway, 2026-05-27]:**
- US accelerated approval for EGFR-mutated NSCLC after EGFR-directed therapy and platinum-based chemotherapy, based on ORR and DoR.
- Pooled NSCLC safety (n = 484): ILD/pneumonitis 7% (grade 3 0.6%, grade 4 0.4%), 8 fatal (1.7%); median onset 1.4 months.

---

# ALK

## 14. PROFILE 1014 (crizotinib vs chemotherapy) — [VERIFIED]

**References**
- Solomon, B. J., Mok, T., Kim, D.-W., Wu, Y.-L., Nakagawa, K., Mekhail, T., Felip, E., Cappuzzo, F., Paolini, J., Usari, T., Iyer, S., Reisman, A., Wilner, K. D., Tursi, J., & Blackhall, F. (2014). First-line crizotinib versus chemotherapy in ALK-positive lung cancer. *The New England Journal of Medicine*, *371*(23), 2167–2177. https://doi.org/10.1056/NEJMoa1408440 — PMID 25470694. **Erratum:** *N Engl J Med 373*(16), 1582 (2015), PMID 26466011.
- (Final OS) Solomon, B. J., Kim, D.-W., Wu, Y.-L., Nakagawa, K., Mekhail, T., Felip, E., Cappuzzo, F., Paolini, J., Usari, T., Tang, Y., Wilner, K. D., Blackhall, F., & Mok, T. S. (2018). Final overall survival analysis from a study comparing first-line crizotinib versus chemotherapy in ALK-mutation-positive non-small-cell lung cancer. *Journal of Clinical Oncology*, *36*(22), 2251–2258. https://doi.org/10.1200/JCO.2017.77.4794 — PMID 29768118

**Design:** Phase 3, open-label; crossover to crizotinib allowed [A].
**Population:** 343 patients with untreated advanced ALK-positive **nonsquamous** NSCLC [A].
**Arms:**
- Crizotinib 250 mg twice daily.
- vs pemetrexed 500 mg/m² + cisplatin 75 mg/m² or carboplatin AUC 5–6, every 3 weeks for up to 6 cycles [A].

**Primary endpoint (PFS by independent review):** 10.9 vs 7.0 months. HR 0.45 (0.35–0.60), P < 0.001 [A].
**Secondary:** ORR 74% vs 45% [A].
**Final OS:**
- HR **0.760 (0.548–1.053), P = .0978; not significant**.
- Median not reached (45.8–NR) vs 47.5 (32.2–NR) months. 4-year OS 56.6% vs 49.1%.
- 84.2% crossover; crossover-adjusted HR 0.346 (bootstrap 95% CI 0.081–0.718) [A].

**Toxicity:** Most common with crizotinib: vision disorders, diarrhoea, nausea, oedema [A].

---

## 15. ALEX (alectinib vs crizotinib) — [VERIFIED]

**References**
- Peters, S., Camidge, D. R., Shaw, A. T., Gadgeel, S., Ahn, J. S., Kim, D.-W., Ou, S.-H. I., Pérol, M., Dziadziuszko, R., Rosell, R., Zeaiter, A., Mitry, E., Golding, S., Balas, B., Noe, J., Morcos, P. N., & Mok, T. (2017). Alectinib versus crizotinib in untreated ALK-positive non-small-cell lung cancer. *The New England Journal of Medicine*, *377*(9), 829–838. https://doi.org/10.1056/NEJMoa1704795 — PMID 28586279
- (Updated OS and final PFS; **not** final OS) Mok, T., Camidge, D. R., Gadgeel, S. M., Rosell, R., Dziadziuszko, R., Kim, D.-W., Pérol, M., Ou, S.-H. I., Ahn, J. S., Shaw, A. T., Bordogna, W., Smoljanović, V., Hilton, M., Ruf, T., Noé, J., & Peters, S. (2020). Updated overall survival and final progression-free survival data for patients with treatment-naive advanced ALK-positive non-small-cell lung cancer in the ALEX study. *Annals of Oncology*, *31*(8), 1056–1064. https://doi.org/10.1016/j.annonc.2020.04.478 — PMID 32418886
- (**Final OS**) Peters, S., Camidge, R., Dziadziuszko, R., Gadgeel, S., Shaw, A. T., Kim, D.-W., Pérol, M., Rosell, D. R., Cheema, P., Wan-Teck Lim, D., Lin, J. J., Pavlakis, N., Ahn, J. S., Zhang, L., Henschel, V., Higgerson, A. A., McNally, V., Rooney, I., Scalori, A., . . . Mok, T. (2026). Alectinib versus crizotinib in previously untreated ALK-positive advanced non-small cell lung cancer: Final overall survival analysis of the phase III ALEX study. *Annals of Oncology*, *37*(1), 92–103. https://doi.org/10.1016/j.annonc.2025.09.018 — PMID 41110693. Author names are given exactly as PubMed and Crossref index them ("Camidge, R.", "Rosell, D. R.", "Wan-Teck Lim, D."). They are probably D. R. Camidge, R. Rosell and D. W.-T. Lim; check against the publisher PDF.

**Design:** Phase 3, open-label, randomized [A].
**Population:** 303 patients with untreated advanced (stage III/IV) ALK-positive NSCLC [A].
**Arms:** Alectinib 600 mg twice daily (n = 152) vs crizotinib 250 mg twice daily (n = 151) [A].
**Primary endpoint (investigator PFS):** 12-month event-free 68.4% vs 48.7%. HR 0.47 (0.34–0.65), P < 0.001. Median not reached with alectinib at the primary analysis [A].
**Secondary:**
- ORR 82.9% vs 75.5% (P = 0.09) [A].
- Mature PFS (2020): median 34.8 vs 10.9 months, HR 0.43 (0.32–0.58) [A].

**CNS:** CNS progression 12% vs 45%; cause-specific HR 0.16 (0.10–0.28), P < 0.001 [A].
**OS:**
- 2020 (immature, 37% of events): not reached vs 57.4 months, HR 0.67 (0.46–0.98). 5-year OS 62.5% vs 45.5% [A].
- **Final (data cutoff 28 April 2025):**
  - Median OS **81.1 (62.3–NE) vs 54.2 (34.6–75.6) months, HR 0.78 (0.56–1.08)**.
  - Baseline CNS metastases: 63.4 vs 30.9 months, HR 0.68 (0.40–1.15).
  - No baseline CNS metastases: 94.0 vs 69.8 months, HR 0.87 (0.58–1.32).
  - DoR 42.3 vs 11.1 months [A].

**Toxicity:**
- Grade 3–5 AEs 41% vs 50% [A].
- Median alectinib exposure 28.1 months; no new safety signals [A].
- Specific signals (myalgia/CK, bradycardia, hyperbilirubinaemia): **[UNVERIFIED]**; not in the abstracts.

---

## 16. ALTA-1L (brigatinib vs crizotinib) — [VERIFIED]

**References**
- Camidge, D. R., Kim, H. R., Ahn, M.-J., Yang, J. C.-H., Han, J.-Y., Lee, J.-S., Hochmair, M. J., Li, J. Y.-C., Chang, G.-C., Lee, K. H., Gridelli, C., Delmonte, A., Garcia Campelo, R., Kim, D.-W., Bearz, A., Griesinger, F., Morabito, A., Felip, E., Califano, R., . . . Popat, S. (2018). Brigatinib versus crizotinib in ALK-positive non-small-cell lung cancer. *The New England Journal of Medicine*, *379*(21), 2027–2039. https://doi.org/10.1056/NEJMoa1810171 — PMID 30280657
- (Final) Camidge, D. R., Kim, H. R., Ahn, M.-J., Yang, J. C. H., Han, J.-Y., Hochmair, M. J., Lee, K. H., Delmonte, A., Garcia Campelo, M. R., Kim, D.-W., Griesinger, F., Felip, E., Califano, R., Spira, A. I., Gettinger, S. N., Tiseo, M., Lin, H. M., Liu, Y., Vranceanu, F., . . . Popat, S. (2021). Brigatinib versus crizotinib in ALK inhibitor-naive advanced ALK-positive NSCLC: Final results of phase 3 ALTA-1L trial. *Journal of Thoracic Oncology*, *16*(12), 2091–2108. https://doi.org/10.1016/j.jtho.2021.07.035 — PMID 34537440. **Erratum:** PMID 36244926 (JTO 2022).

**Design:** Phase 3, open-label, randomized 1:1 [A].
**Population:** 275 patients with ALK-inhibitor-naive advanced ALK-positive NSCLC: 137 brigatinib, 138 crizotinib [A].
**Arms:** Brigatinib 180 mg once daily after a 7-day lead-in at 90 mg vs crizotinib 250 mg twice daily [A].
**Primary endpoint (BICR PFS, first interim analysis):** 12-month PFS 67% vs 43%. HR 0.49 (0.33–0.74), P < 0.001 [A].
**Secondary:** Confirmed ORR 71% vs 60%. Intracranial ORR (measurable lesions) 78% vs 29% [A].
**Final (median follow-up 40.4 months):**
- BICR PFS median **24.0 vs 11.1 months, HR 0.48 (0.35–0.66)**; 3-year PFS 43% vs 19%.
- OS not reached in either arm, HR 0.81 (0.53–1.22), not significant.
- Post hoc, baseline brain metastases: OS HR 0.43 (0.21–0.89) [A].

**Toxicity:**
- "No new safety concerns" [A].
- Early-onset pulmonary events and CPK elevation: **[UNVERIFIED]**; not in the abstracts.

---

## 17. CROWN (lorlatinib vs crizotinib) — [VERIFIED]

**References**
- Shaw, A. T., Bauer, T. M., de Marinis, F., Felip, E., Goto, Y., Liu, G., Mazieres, J., Kim, D.-W., Mok, T., Polli, A., Thurm, H., Calella, A. M., Peltz, G., & Solomon, B. J. (2020). First-line lorlatinib or crizotinib in advanced ALK-positive lung cancer. *The New England Journal of Medicine*, *383*(21), 2018–2029. https://doi.org/10.1056/NEJMoa2027187 — PMID 33207094
- (5-year) Solomon, B. J., Liu, G., Felip, E., Mok, T. S. K., Soo, R. A., Mazieres, J., Shaw, A. T., de Marinis, F., Goto, Y., Wu, Y.-L., Kim, D.-W., Martini, J.-F., Messina, R., Paolini, J., Polli, A., Thomaidou, D., Toffalorio, F., & Bauer, T. M. (2024). Lorlatinib versus crizotinib in patients with advanced ALK-positive non-small cell lung cancer: 5-year outcomes from the phase III CROWN study. *Journal of Clinical Oncology*, *42*(29), 3400–3409. https://doi.org/10.1200/JCO.24.00581 — PMID 38819031 (PMC11458101)
- (7-year, newer than the brief) Shaw, A. T., Solomon, B. J., Felip, E., Bauer, T. M., Liu, G., Goto, Y., Wu, Y.-L., Soo, R. A., Mazieres, J., Kim, D.-W., Wang, I.-M., Paolini, J., Polli, A., Rifi, N., Toffalorio, F., & Mok, T. S. K. (2026). Lorlatinib versus crizotinib as first-line treatment for advanced ALK-positive non-small-cell lung cancer: 7-year update from the phase III CROWN study. *Annals of Oncology*, *37*(9), 1242–1252. https://doi.org/10.1016/j.annonc.2026.05.692 — PMID 42217582

**Design:** Phase 3, global, randomized 1:1 [A].
**Population:** 296 patients with advanced ALK-positive NSCLC and no prior systemic therapy for metastatic disease [A].
**Arms:** Lorlatinib 100 mg once daily (n = 149) vs crizotinib 250 mg twice daily (n = 147) [A, 5-year paper].
**Primary endpoint (BICR PFS, interim analysis):** 12-month PFS 78% (70–84) vs 39% (30–48). HR 0.28 (0.19–0.41), P < 0.001 [A].
**Secondary:** ORR 76% vs 58% [A].
**CNS:** Intracranial ORR (measurable brain metastases) 82% vs 23%; 71% intracranial CR with lorlatinib [A].
**5-year update (post hoc, investigator-assessed):**
- Median PFS not reached (64.3–NR) vs 9.1 (7.4–10.9) months, HR 0.19 (0.13–0.27). 5-year PFS 60% vs 8%.
- Time to intracranial progression not reached vs 16.4 months, HR 0.06 (0.03–0.12) [A].

**7-year update:**
- PFS not reached (68.5–NR) vs 9.1 months, HR 0.19 (0.13–0.26). 7-year PFS 55% vs 3%.
- No new intracranial progression after month 30.
- OS: the number of events for the protocol analysis has not yet been reached [A].

**Toxicity:**
- Primary analysis [A]:
  - Hyperlipidaemia, oedema, weight gain, peripheral neuropathy, cognitive effects.
  - Grade 3–4 AEs 72% vs 56% (mainly lipids). Discontinuation 7% vs 9%.
- At 5 years [FT]:
  - Grade 3/4 AEs 77% vs 57%.
  - Grade 3/4 hypertriglyceridaemia 25%, hypercholesterolaemia 21%, weight gain 23%, hypertension 12%.
  - **CNS AEs 42%** (86% grade 1–2).

---

## 18. ALINA (adjuvant alectinib) — [VERIFIED]

**Reference**
- Wu, Y.-L., Dziadziuszko, R., Ahn, J. S., Barlesi, F., Nishio, M., Lee, D. H., Lee, J.-S., Zhong, W., Horinouchi, H., Mao, W., Hochmair, M., de Marinis, F., Migliorino, M. R., Bondarenko, I., Lu, S., Wang, Q., Ochi Lohmann, T., Xu, T., Cardona, A., . . . Solomon, B. J. (2024). Alectinib in resected ALK-positive non-small-cell lung cancer. *The New England Journal of Medicine*, *390*(14), 1265–1276. https://doi.org/10.1056/NEJMoa2310532 — PMID 38598794

**Design:** Phase 3, global, open-label, randomized 1:1 [A].
**Population:** 257 patients with completely resected ALK-positive NSCLC, stage IB (≥4 cm) to IIIA (AJCC 7th edition): 130 alectinib, 127 chemotherapy [A].
**Arms:** Alectinib 600 mg twice daily for 24 months vs IV platinum-based chemotherapy, 4 cycles of 21 days [A].
**Primary endpoint (DFS, tested hierarchically):**
- Stage II–IIIA: 2-year DFS 93.8% vs 63.0%, HR 0.24 (0.13–0.45), P < 0.001.
- ITT: 93.6% vs 63.7%, HR 0.24 (0.13–0.43), P < 0.001 [A].

**Secondary:**
- CNS DFS HR 0.22 (0.08–0.58) [A].
- OS immature [A].

**Toxicity:** No unexpected safety findings [A].

---

# ROS1

## 19. PROFILE 1001 ROS1 cohort (crizotinib) — [VERIFIED]

**References**
- Shaw, A. T., Ou, S.-H. I., Bang, Y.-J., Camidge, D. R., Solomon, B. J., Salgia, R., Riely, G. J., Varella-Garcia, M., Shapiro, G. I., Costa, D. B., Doebele, R. C., Le, L. P., Zheng, Z., Tan, W., Stephenson, P., Shreeve, S. M., Tye, L. M., Christensen, J. G., Wilner, K. D., . . . Iafrate, A. J. (2014). Crizotinib in ROS1-rearranged non-small-cell lung cancer. *The New England Journal of Medicine*, *371*(21), 1963–1971. https://doi.org/10.1056/NEJMoa1406766 — PMID 25264305 (PMC4264527)
- (Updated incl. OS) Shaw, A. T., Riely, G. J., Bang, Y.-J., Kim, D.-W., Camidge, D. R., Solomon, B. J., Varella-Garcia, M., Iafrate, A. J., Shapiro, G. I., Usari, T., Wang, S. C., Wilner, K. D., Clark, J. W., & Ou, S.-H. I. (2019). Crizotinib in ROS1-rearranged advanced non-small-cell lung cancer (NSCLC): Updated results, including overall survival, from PROFILE 1001. *Annals of Oncology*, *30*(7), 1121–1126. https://doi.org/10.1093/annonc/mdz131 — PMID 30980071

**Design:** Expansion cohort of a phase 1 study [A].
**Population:** Advanced ROS1-rearranged NSCLC; n = 50 (2014), n = 53 (2019) [A].
**Arm:** Crizotinib 250 mg twice daily [A].
**Primary result (ORR; single-arm):**
- 2014: ORR 72% (58–84), 3 CR and 33 PR. DoR 17.6 months. PFS 19.2 (14.4–NR) months [A].
- 2019: ORR 72% (58–83). DoR 24.7 (15.2–45.3) months. PFS 19.3 (15.2–39.1) months [A].

**OS (2019):** Median **51.4 (29.3–NR) months**. Survival at 12/24/36/48 months: 79%/67%/53%/51%. Median follow-up 62.6 months [A].
**CNS:** **[UNVERIFIED]**; not in the abstracts.
**Toxicity:** Mainly grade 1–2. No grade ≥4 TRAEs and no permanent discontinuations for TRAEs [A, 2019].

---

## 20. Entrectinib integrated analysis (ROS1) — [VERIFIED]

**References**
- Drilon, A., Siena, S., Dziadziuszko, R., Barlesi, F., Krebs, M. G., Shaw, A. T., de Braud, F., Rolfo, C., Ahn, M.-J., Wolf, J., Seto, T., Cho, B. C., Patel, M. R., Chiu, C.-H., John, T., Goto, K., Karapetis, C. S., Arkenau, H.-T., Kim, S.-W., . . . Doebele, R. C. (2020). Entrectinib in ROS1 fusion-positive non-small-cell lung cancer: Integrated analysis of three phase 1–2 trials. *The Lancet Oncology*, *21*(2), 261–270. https://doi.org/10.1016/S1470-2045(19)30690-4 — PMID 31838015 (PMC7811790). **Errata:** PMIDs 32007206 and 32615113.
- (Long-term) Drilon, A., Chiu, C.-H., Fan, Y., Cho, B. C., Lu, S., Ahn, M.-J., Krebs, M. G., Liu, S. V., John, T., Otterson, G. A., Tan, D. S. W., Patil, T., Dziadziuszko, R., Massarelli, E., Seto, T., Doebele, R. C., Pitcher, B., Kurtsikidze, N., Heinzmann, S., & Siena, S. (2022). Long-term efficacy and safety of entrectinib in ROS1 fusion-positive NSCLC. *JTO Clinical and Research Reports*, *3*(6), 100332. https://doi.org/10.1016/j.jtocrr.2022.100332 — PMID 35663414

**Design:** Integrated analysis of three phase 1–2 trials: ALKA-372-001, STARTRK-1, STARTRK-2 [A].
**Population:** ROS1 inhibitor-naive, ROS1 fusion-positive NSCLC with ≥12 months of follow-up; ECOG 0–2 [A].
**Arm:** Entrectinib ≥600 mg once daily [A].
**Primary result (ORR and DoR by BICR):** ORR 77% (64–88) in 53 patients. DoR 24.6 (11.4–34.8) months [A].
**Secondary:**
- PFS 19.0 (12.2–36.6) months [FT].
- OS not estimable at the 2020 analysis [FT].

**CNS:** Intracranial ORR **55% (11/20; 95% CI 32–77)** in patients with BICR-confirmed baseline CNS metastases [FT].
**2022 update (n = 168):**
- ORR 68% (60.2–74.8). DoR 20.5 months. PFS 15.7 months. OS 47.8 months.
- Intracranial ORR 80% (59.3–93.2) in 25 patients with measurable CNS disease; intracranial PFS 8.8 months.
- CNS-only progression after crizotinib: 11% PR [A].

**Toxicity (n = 134):**
- Grade 3–4 TRAEs 34%; most common were weight increase (8%) and neutropenia (4%).
- Serious TRAEs 11% (nervous system 3%, cardiac 2%). No treatment-related deaths [A].

---

## 21. TRIDENT-1 (repotrectinib, ROS1) — [VERIFIED]

**Reference**
- Drilon, A., Camidge, D. R., Lin, J. J., Kim, S.-W., Solomon, B. J., Dziadziuszko, R., Besse, B., Goto, K., de Langen, A. J., Wolf, J., Lee, K. H., Popat, S., Springfeld, C., Nagasaka, M., Felip, E., Yang, N., Velcheti, V., Lu, S., Kao, S., . . . Cho, B. C. (2024). Repotrectinib in ROS1 fusion-positive non-small-cell lung cancer. *The New England Journal of Medicine*, *390*(2), 118–131. https://doi.org/10.1056/NEJMoa2302299 — PMID 38197815 (PMC11702311)

**Design:** Registrational phase 1–2 trial [A].
**Population:** Advanced ROS1 fusion-positive NSCLC [A].
**Arm:** Repotrectinib 160 mg once daily for 14 days, then 160 mg twice daily (recommended phase 2 dose) [A].
**Primary result (confirmed ORR):**
- TKI-naive (n = 71): ORR 79% (68–88). DoR 34.1 (25.6–NE) months. PFS 35.7 (27.4–NE) months [A].
- One prior TKI, chemotherapy-naive (n = 56): ORR 38% (25–52). DoR 14.8 months. PFS 9.0 (6.8–19.6) months [A].
- ROS1 G2032R: 10/17 responded (59%) [A].

**OS [FT]:** TKI-naive not estimable (44.4–NE); one prior TKI 25.1 (17.8–NE) months.
**CNS [FT]:** Intracranial ORR 89% (8/9; 52–100) in TKI-naive patients and 38% (5/13; 14–68) after one TKI.
**Toxicity (n = 426):** **Dizziness 58%, dysgeusia 50%, paraesthesia 30%**. 3% discontinued for TRAEs [A].

---

## 22. Taletrectinib (TRUST-I / TRUST-II) — [VERIFIED]

**References**
- (Pooled TRUST-I + TRUST-II) Pérol, M., Li, W., Pennell, N. A., Liu, G., Ohe, Y., De Braud, F., Nagasaka, M., Felip, E., Xiong, A., Zhang, Y., Fan, H., Wang, X., Li, S., Lai, R. K., Ran, F., Zhang, X., Chen, W., Bazhenova, L., & Zhou, C. (2025). Taletrectinib in ROS1+ non-small cell lung cancer: TRUST. *Journal of Clinical Oncology*, *43*(16), 1920–1929. https://doi.org/10.1200/JCO-25-00275 — PMID 40179330 (PMC12118623)
- (TRUST-I) Li, W., Xiong, A., Yang, N., Fan, H., Yu, Q., Zhao, Y., Wang, Y., Meng, X., Wu, J., Wang, Z., Liu, Y., Wang, X., Qin, X., Lu, K., Zhuang, W., Ren, Y., Zhang, X., Yan, B., Lovly, C. M., & Zhou, C. (2024). Efficacy and safety of taletrectinib in Chinese patients with ROS1+ non-small cell lung cancer: The phase II TRUST-I study. *Journal of Clinical Oncology*, *42*(22), 2660–2670. https://doi.org/10.1200/JCO.24.00731 — PMID 38822758

**Design:** Phase 2, single-arm, open-label. Efficacy is pooled from the pivotal TRUST-I and TRUST-II cohorts [A]. No stand-alone TRUST-II results paper was found on PubMed.
**Arm:** Taletrectinib 600 mg once daily [A].
**Pooled efficacy (n = 273):**
- TKI-naive (n = 160): confirmed ORR **88.8%**; intracranial ORR 76.5% [A]. DoR 44.2 (30.4–NR) months. **PFS 45.6 (29.0–NR) months**. 36-month OS 66.3% [FT].
- TKI-pretreated (n = 113): ORR 55.8%; intracranial ORR 65.6% [A]. DoR 16.6 (10.6–27.3) months. PFS 9.7 (7.4–12.0) months [FT].
- G2032R: 61.5% (8/13) [A].

**TRUST-I (China, n = 173) [A]:**
- TKI-naive: ORR 91%; intracranial ORR 88%; PFS not reached.
- Crizotinib-pretreated: ORR 52%; intracranial ORR 73%; PFS 7.6 (5.5–12.0) months.

**Toxicity (pooled, n = 352):**
- GI events 88%, AST increase 72%, ALT increase 68%, mostly grade 1.
- Dizziness 21%, dysgeusia 15%.
- Discontinuation 6.5% [A].
- NP note: liver enzymes and GI toxicity dominate, with less neurotoxicity than repotrectinib.

---

# BRAF V600E

## 23. Dabrafenib + trametinib (BRF113928) — [VERIFIED]

**References**
- (Pretreated cohort B) Planchard, D., Besse, B., Groen, H. J. M., Souquet, P.-J., Quoix, E., Baik, C. S., Barlesi, F., Kim, T. M., Mazieres, J., Novello, S., Rigas, J. R., Upalawanna, A., D'Amelio, A. M., Zhang, P., Mookerjee, B., & Johnson, B. E. (2016). Dabrafenib plus trametinib in patients with previously treated BRAF(V600E)-mutant metastatic non-small cell lung cancer: An open-label, multicentre phase 2 trial. *The Lancet Oncology*, *17*(7), 984–993. https://doi.org/10.1016/S1470-2045(16)30146-2 — PMID 27283860
- (**Untreated** cohort C) Planchard, D., Smit, E. F., Groen, H. J. M., Mazieres, J., Besse, B., Helland, Å., Giannone, V., D'Amelio, A. M., Zhang, P., Mookerjee, B., & Johnson, B. E. (2017). Dabrafenib plus trametinib in patients with previously untreated BRAFV600E-mutant metastatic non-small-cell lung cancer: An open-label, phase 2 trial. *The Lancet Oncology*, *18*(10), 1307–1316. https://doi.org/10.1016/S1470-2045(17)30679-4 — PMID 28919011
- (5-year OS) Planchard, D., Besse, B., Groen, H. J. M., Hashemi, S. M. S., Mazieres, J., Kim, T. M., Quoix, E., Souquet, P.-J., Barlesi, F., Baik, C., Villaruz, L. C., Kelly, R. J., Zhang, S., Tan, M., Gasal, E., Santarpia, L., & Johnson, B. E. (2022). Phase 2 study of dabrafenib plus trametinib in patients with BRAF V600E-mutant metastatic NSCLC: Updated 5-year survival rates and genomic analysis. *Journal of Thoracic Oncology*, *17*(1), 103–115. https://doi.org/10.1016/j.jtho.2021.08.011 — PMID 34455067

**Design:** Phase 2, multicohort, non-randomized, open-label (NCT01336634) [A].
**Arm:** Dabrafenib 150 mg twice daily + trametinib 2 mg once daily [A].
**Primary endpoint (investigator ORR):**
- Untreated (n = 36): ORR 64% (46–79); 2 CRs (6%). Median follow-up 15.9 months [A].
- Pretreated (n = 57): ORR 63.2% (49.3–75.6) [A].

**5-year update (pretreated B vs untreated C):**
- ORR 68.4% vs 63.9%.
- PFS 10.2 (6.9–16.7) vs 10.8 (7.0–14.5) months.
- OS 18.2 (14.3–28.6) vs 17.3 (12.3–40.2) months.
- 5-year OS 19% vs 22% [A].

**Toxicity:**
- Untreated cohort: grade 3–4 AEs 69%, including pyrexia 11%, ALT increase 11%, hypertension 11%, vomiting 8%. SAEs included **ejection fraction decrease 8%** [A].
- Pretreated cohort: SAEs 56%, including pyrexia 16% and cutaneous SCC 4% [A].
- Pooled 5-year: **pyrexia 56%** [A].

---

## 24. PHAROS (encorafenib + binimetinib) — [VERIFIED]

**References**
- Riely, G. J., Smit, E. F., Ahn, M.-J., Felip, E., Ramalingam, S. S., Tsao, A., Johnson, M., Gelsomino, F., Esper, R., Nadal, E., Offin, M., Provencio, M., Clarke, J., Hussain, M., Otterson, G. A., Dagogo-Jack, I., Goldman, J. W., Morgensztern, D., Alcasid, A., . . . Johnson, B. E. (2023). Phase II, open-label study of encorafenib plus binimetinib in patients with BRAFV600-mutant metastatic non-small-cell lung cancer. *Journal of Clinical Oncology*, *41*(21), 3700–3711. https://doi.org/10.1200/JCO.23.00774 — PMID 37270692. **Erratum:** *J Clin Oncol 42*(2), 245 (2024), PMID 38051975.
- (Updated OS) Johnson, M. L., Smit, E. F., Felip, E., Ramalingam, S. S., Ahn, M.-J., Tsao, A., Johnson, B. E., Offin, M., Hussein, M., Dagogo-Jack, I., Goldman, J. W., Clarke, J. M., Negrao, M. V., Sanborn, R. E., Morgensztern, D., Usari, T., Wilner, K., Alejandro, L., Rifi, N., . . . Riely, G. J. (2025). Updated overall survival analysis from the phase II PHAROS study of encorafenib plus binimetinib in patients with BRAF V600E-mutant metastatic non-small cell lung cancer. *Journal of Clinical Oncology*, *43*(35), 3706–3713. https://doi.org/10.1200/JCO-25-02023 — PMID 41109959

**Design:** Phase 2, single-arm, open-label [A].
**Population:** 98 patients with BRAF V600E metastatic NSCLC (59 treatment-naive, 39 previously treated) [A]. The title says "BRAFV600"; the enrolled population was V600E.
**Arm:** Encorafenib 450 mg once daily + binimetinib 45 mg twice daily, 28-day cycles [A].
**Primary endpoint (ORR by IRR):** Naive 75% (62–85); pretreated 46% (30–63) [A].
**Secondary (2023):**
- DoR not estimable (23.1–NE) vs 16.7 (7.4–NE) months.
- PFS not estimable (15.7–NE) vs 9.3 (6.2–NE) months [A].

**Updated OS (data cutoff 14 March 2025):**
- Naive: median OS **47.6 (31.3–NE) months**; 4-year OS 49%.
- Pretreated: 22.7 (14.1–32.6) months; 4-year OS 31% [A].

**Toxicity:**
- Nausea 50%, diarrhoea 43%, fatigue 32%.
- Dose reductions 24%; permanent discontinuation 15%.
- One grade 5 intracranial haemorrhage [A].

---

# MET exon 14

## 25. GEOMETRY mono-1 (capmatinib) — [PARTIAL]

**References**
- Wolf, J., Seto, T., Han, J.-Y., Reguart, N., Garon, E. B., Groen, H. J. M., Tan, D. S. W., Hida, T., de Jonge, M., Orlov, S. V., Smit, E. F., Souquet, P.-J., Vansteenkiste, J., Hochmair, M., Felip, E., Nishio, M., Thomas, M., Ohashi, K., Toyozawa, R., . . . Heist, R. S. (2020). Capmatinib in MET exon 14-mutated or MET-amplified non-small-cell lung cancer. *The New England Journal of Medicine*, *383*(10), 944–957. https://doi.org/10.1056/NEJMoa2002787 — PMID 32877583
- (Final) Wolf, J., Hochmair, M., Han, J.-Y., Reguart, N., Souquet, P.-J., Smit, E. F., Orlov, S. V., Vansteenkiste, J., Nishio, M., de Jonge, M., Akerley, W., Garon, E. B., Groen, H. J. M., Tan, D. S. W., Seto, T., Frampton, G. M., Robeva, A., Carbini, M., Le Mouhaer, S., . . . Heist, R. S. (2024). Capmatinib in MET exon 14-mutated non-small-cell lung cancer: Final results from the open-label, phase 2 GEOMETRY mono-1 trial. *The Lancet Oncology*, *25*(10), 1357–1370. https://doi.org/10.1016/S1470-2045(24)00441-8 — PMID 39362249. **Erratum:** PMID 39366396.

**Design:** Phase 2, multicohort, non-randomized [A].
**Population:** MET-dysregulated advanced NSCLC (METex14 or MET amplification); EGFR wild-type and ALK-negative per the final paper; n = 364 (2020) [A].
**Arm:** Capmatinib 400 mg tablet twice daily [A].
**Primary endpoint (ORR by IRC):**
- METex14, 1–2 prior lines (n = 69): ORR 41% (29–53); DoR 9.7 (5.6–13.0) months [A].
- METex14, treatment-naive (n = 28): ORR 68% (48–84); DoR 12.6 (5.6–NE) months [A].
- MET amplification, gene copy number ≥10: ORR 29% (pretreated) and 40% (naive). Copy number <10: 7–12% [A].
- Final analysis (160 METex14 patients): naive (n = 60) ORR 68% (55.0–79.7); pretreated (n = 100) 44% (34.1–54.3) [A].

**PFS:** **[UNVERIFIED]**. Not in either abstract, and NEJM 2020 is not in PMC. The VISION paper's discussion [FT] cites GEOMETRY median PFS of 5.4 months (pretreated) and 9.7 months (naive). This may reflect an earlier data cut and should not be quoted until checked against the GEOMETRY full text.
**CNS:** **[UNVERIFIED]**; not in the abstracts.
**Toxicity:**
- 2020: peripheral oedema 51%, nausea 45%, mostly grade 1–2 [A].
- Final (n = 373): oedema 47%, nausea 35%, creatinine increase 21%, vomiting 20%. Grade 3–4 SAEs 44%. 4 treatment-related deaths (1%), including **organising pneumonia and pneumonitis** [A].

---

## 26. VISION (tepotinib) — [VERIFIED]

**References**
- Paik, P. K., Felip, E., Veillon, R., Sakai, H., Cortot, A. B., Garassino, M. C., Mazieres, J., Viteri, S., Senellart, H., Van Meerbeeck, J., Raskin, J., Reinmuth, N., Conte, P., Kowalski, D., Cho, B. C., Patel, J. D., Horn, L., Griesinger, F., Han, J.-Y., . . . Le, X. (2020). Tepotinib in non-small-cell lung cancer with MET exon 14 skipping mutations. *The New England Journal of Medicine*, *383*(10), 931–943. https://doi.org/10.1056/NEJMoa2004407 — PMID 32469185 (PMC8422679)
- (Long-term) Mazieres, J., Paik, P. K., Garassino, M. C., Le, X., Sakai, H., Veillon, R., Smit, E. F., Cortot, A. B., Raskin, J., Viteri, S., Wu, Y.-L., Yang, J. C. H., Ahn, M.-J., Ma, R., Zhao, J., O'Brate, A., Berghoff, K., Bruns, R., Otto, G., . . . Thomas, M. (2023). Tepotinib treatment in patients with MET exon 14-skipping non-small cell lung cancer: Long-term follow-up of the VISION phase 2 nonrandomized clinical trial. *JAMA Oncology*, *9*(9), 1260–1266. https://doi.org/10.1001/jamaoncol.2023.1962 — PMID 37270698. **Erratum:** PMID 37471093.

**Design:** Phase 2, open-label [A].
**Population:** Advanced NSCLC with MET exon 14 skipping, detected by liquid or tissue biopsy. 152 patients treated; 99 with ≥9 months of follow-up [A].
**Arm:** Tepotinib 500 mg once daily, equal to 450 mg active moiety [A, 2023].
**Primary endpoint (ORR by independent review):** 46% (36–57). DoR 11.1 (7.2–NE) months. Liquid-biopsy group 48%, tissue-biopsy group 50% [A].
**Secondary:** PFS 8.5 (6.7–11.0) months in the combined-biopsy group [FT].
**Long-term (cohorts A + C, n = 313; median age 72):**
- Overall: ORR 51.4% (45.8–57.1); DoR 18.0 months.
- Treatment-naive (n = 164): ORR 57.3%; DoR 46.4 months.
- Pretreated (n = 149): ORR 45.0%; DoR 12.6 months [A].

**Toxicity:**
- 2020: grade ≥3 TRAEs 28%, including peripheral oedema 7%; discontinuation 11% [A].
- Long-term: **peripheral oedema 67.1%** (grade ≥3 11.2%) [A].

---

# RET

## 27. LIBRETTO-431 (selpercatinib vs chemo ± pembrolizumab) — [VERIFIED]

**References**
- Zhou, C., Solomon, B., Loong, H. H., Park, K., Pérol, M., Arriola, E., Novello, S., Han, B., Zhou, J., Ardizzoni, A., Mak, M. P., Santini, F. C., Elamin, Y. Y., Drilon, A., Wolf, J., Payakachat, N., Uh, M. K., Rajakumar, D., Han, H., . . . Goto, K. (2023). First-line selpercatinib or chemotherapy and pembrolizumab in RET fusion-positive NSCLC. *The New England Journal of Medicine*, *389*(20), 1839–1850. https://doi.org/10.1056/NEJMoa2309457 — PMID 37870973 (PMC10698285)
- (CNS) Pérol, M., Solomon, B. J., Goto, K., Park, K., Nadal, E., Bria, E., Martin, C., Bar, J., Williams, J. N., Puri, T., Li, J., Uh, M. K., Lin, B. K., & Zhou, C. (2024). CNS protective effect of selpercatinib in first-line RET fusion-positive advanced non-small cell lung cancer. *Journal of Clinical Oncology*, *42*(21), 2500–2505. https://doi.org/10.1200/JCO.24.00724 — PMID 38828957
- (FDA reviewer commentary on OS) Duke, E. S., Bradford, D., Sinha, A. K., Li, X., Mishra-Kalyani, P. S., de Claro, R. A., Larkins, E., & Drezner, N. (2026). Selpercatinib and the crossover conundrum: Potential impact of postprogression therapies on overall survival. *Journal of Clinical Oncology*, *44*(15), 1457–1464. https://doi.org/10.1200/JCO-25-02375 — PMID 41996652

**Design:** Phase 3, randomized; crossover to selpercatinib allowed after BICR-confirmed progression [A].
**Population:** Untreated advanced RET fusion-positive NSCLC. ITT-pembrolizumab population n = 212; overall ITT n = 261 [A].
**Arms:**
- Selpercatinib 160 mg twice daily [FT].
- vs pemetrexed 500 mg/m² + carboplatin AUC 5 or cisplatin 75 mg/m², with or without pembrolizumab at investigator's choice [FT].

**Primary endpoint (BICR PFS):**
- ITT-pembrolizumab: 24.8 (16.9–NE) vs 11.2 (8.8–16.8) months. HR 0.46 (0.31–0.70), P < 0.001 [A].
- Overall ITT: 24.8 (17.3–NE) vs 11.2 (8.8–16.8) months. HR 0.48 (0.33–0.70) [FT].

**Secondary:** ORR 84% vs 65% [A].
**OS:**
- Interim (information fraction 28.6%, 50 deaths): HR 0.96 (0.50–1.83) in ITT-pembrolizumab and 1.04 (0.58–1.87) in overall ITT [FT].
- **FDA reviewers (Duke 2026) report a later, still immature OS HR of 1.26, numerically favouring chemo-immunotherapy.** They attribute this partly to crossover and post-progression therapy. The CI is not stated in the abstract [A].

**CNS:**
- Time to CNS progression: cause-specific HR 0.28 (0.12–0.68) [A].
- Patients without baseline CNS metastases (n = 150): CNS progression cause-specific HR 0.17 (0.04–0.69) [A, Pérol 2024].

**Toxicity (selpercatinib arm) [FT]:**
- Grade ≥3: **ALT increase 22%**, AST increase 13%, **hypertension 20%**, **QTc prolongation 9%**.
- Any grade: ALT increase 60%, AST increase 61%, hypertension 48%.
- These events were more frequent in **East Asian** patients, which is relevant for Taiwan.

---

## 28. ARROW (pralsetinib) — [VERIFIED]

**Reference**
- Gainor, J. F., Curigliano, G., Kim, D.-W., Lee, D. H., Besse, B., Baik, C. S., Doebele, R. C., Cassier, P. A., Lopes, G., Tan, D. S. W., Garralda, E., Paz-Ares, L. G., Cho, B. C., Gadgeel, S. M., Thomas, M., Liu, S. V., Taylor, M. H., Mansfield, A. S., Zhu, V. W., . . . Subbiah, V. (2021). Pralsetinib for RET fusion-positive non-small-cell lung cancer (ARROW): A multi-cohort, open-label, phase 1/2 study. *The Lancet Oncology*, *22*(7), 959–969. https://doi.org/10.1016/S1470-2045(21)00247-3 — PMID 34118197. **Erratum:** PMID 34339651.

**Design:** Phase 1/2, multi-cohort, open-label; 71 sites in 13 countries, including **Taiwan** [A].
**Population:** 233 patients with RET fusion-positive NSCLC enrolled [A].
**Arm:** Pralsetinib 400 mg once daily [A].
**Primary endpoint (ORR by BICR):**
- After platinum (n = 87): ORR 61% (50–71), CR 6% [A].
- Treatment-naive (n = 27): ORR 70% (50–86), CR 11% [A].
- PFS and DoR: not in the abstract **[UNVERIFIED]**.

**Toxicity (n = 233):**
- Grade ≥3 TRAEs: neutropenia 18%, hypertension 11%, anaemia 10%. No treatment-related deaths [A].
- Pneumonitis rate: **[UNVERIFIED]**.

---

# KRAS G12C

## 29. CodeBreaK 200 (sotorasib vs docetaxel) — [VERIFIED]

**References**
- de Langen, A. J., Johnson, M. L., Mazieres, J., Dingemans, A.-M. C., Mountzios, G., Pless, M., Wolf, J., Schuler, M., Lena, H., Skoulidis, F., Yoneshima, Y., Kim, S.-W., Linardou, H., Novello, S., van der Wekken, A. J., Chen, Y., Peters, S., Felip, E., Solomon, B. J., . . . Paz-Ares, L. (2023). Sotorasib versus docetaxel for previously treated non-small-cell lung cancer with KRASG12C mutation: A randomised, open-label, phase 3 trial. *The Lancet*, *401*(10378), 733–746. https://doi.org/10.1016/S0140-6736(23)00221-0 — PMID 36764316
- (Plain-language summary, OS source) de Langen, A. J., Johnson, M. L., Mazieres, J., Dingemans, A.-M. C., Mountzios, G., Pless, M., Wolf, J., Schuler, M., Lena, H., Skoulidis, F., Yoneshima, Y., Kim, S.-W., Linardou, H., Novello, S., van der Wekken, A. J., Chen, Y., Peters, S., Felip, E., Solomon, B. J., . . . Paz-Ares, L. (2025). Sotorasib versus docetaxel for previously treated KRAS G12C-mutated non-small-cell lung cancer: A plain language summary. *Future Oncology*, *21*(9), 1033–1044. https://doi.org/10.1080/14796694.2025.2474789 — PMID 40129223 (PMC11988231)
- (CNS) Dingemans, A.-M. C., Syrigos, K., Livi, L., Paulus, A., Kim, S.-W., Chen, Y., Felip, E., Griesinger, F., Ohashi, K., Zalcman, G., Hughes, B. G. M., Sørensen, J. B., Blais, N., Ferreira, C. G. M., Lindsay, C. R., Dziadziuszko, R., Ward, P. J., Obiozor, C. C., Wang, Y., & Peters, S. (2025). Intracranial activity of sotorasib vs docetaxel in pretreated KRAS G12C-mutated advanced non-small cell lung cancer from a global, phase 3, randomized controlled trial. *Lung Cancer*, *207*, 108683. https://doi.org/10.1016/j.lungcan.2025.108683 — PMID 40774040

**Design:** Phase 3, open-label, randomized 1:1; 148 centres in 22 countries [A].
**Population:** KRAS G12C-mutated advanced NSCLC that progressed after platinum chemotherapy and a PD-1/PD-L1 inhibitor: 171 sotorasib, 174 docetaxel [A].
**Arms:** Sotorasib 960 mg once daily vs docetaxel 75 mg/m² every 3 weeks [A].
**Primary endpoint (BICR PFS):** 5.6 (4.3–7.8) vs 4.5 (3.0–5.7) months. HR 0.66 (0.51–0.86), p = 0.0017. Median follow-up 17.7 months [A].
**OS:**
- Not in the Lancet abstract.
- The author plain-language summary reports median OS **10.6 vs 11.3 months**, "similar" [PLS].
- OS HR and CI: **[UNVERIFIED]**.

**CNS:** Patients with baseline CNS metastases (40 vs 29): CNS PFS 9.6 vs 4.5 months, HR 0.43 (0.20–0.92) [A, Dingemans 2025].
**Toxicity:**
- Grade ≥3 TRAEs 33% vs 40%; serious TRAEs 11% vs 23% [A].
- Sotorasib grade ≥3: diarrhoea 12%, **ALT increase 8%, AST increase 5%** [A].

---

## 30. KRYSTAL-12 (adagrasib vs docetaxel) — [VERIFIED; CITATION CORRECTED]

**Reference**
- Barlesi, F., Yao, W., Duruisseaux, M., Doucet, L., Martínez, A. A., Gregorc, V., Juan-Vidal, O., Lu, S., De Bondt, C., de Marinis, F., Linardou, H., Kim, Y.-C., Jotte, R., Felip, E., Lo Russo, G., Reck, M., Michenzie, M. F., Yang, W., Meade, J. N., . . . Mok, T. S. K. (2025). Adagrasib versus docetaxel in KRASG12C-mutated non-small-cell lung cancer (KRYSTAL-12): A randomised, open-label, phase 3 trial. *The Lancet*, *406*(10503), 615–626. https://doi.org/10.1016/S0140-6736(25)00866-9 — PMID 40783289
  - **The brief's "Mok 2024 Lancet" is incorrect.** Mok is the last author, and the publication year is 2025. The second author's surname appears as "Martínez, A. A." in PubMed but as "Azkárate Martínez" in the 2026 plain-language summary; check against the publisher PDF.

**Design:** Phase 3, open-label, randomized 2:1; 230 centres in 22 countries [A].
**Population:** KRAS G12C-mutated locally advanced or metastatic NSCLC previously treated with platinum chemotherapy and anti-PD-(L)1. 453 patients: 301 adagrasib, 152 docetaxel [A].
**Arms:** Adagrasib 600 mg twice daily vs docetaxel 75 mg/m² every 3 weeks [A].
**Primary endpoint (BICR PFS, ITT):** 5.5 (4.5–6.7) vs 3.8 (2.7–4.7) months. HR 0.58 (0.45–0.76), p < 0.0001. Median follow-up 7.2 months [A].
**OS and ORR:** **[UNVERIFIED]**. OS is not reported in the abstract, and no OS paper was found on PubMed.
**Toxicity:**
- Grade ≥3 TRAEs 47% vs 46%.
- Treatment-related deaths: 4 (1%) vs 1 (1%) [A].

---

# HER2

## 31. DESTINY-Lung02 (trastuzumab deruxtecan) — [VERIFIED]

**Reference**
- Goto, K., Goto, Y., Kubo, T., Ninomiya, K., Kim, S.-W., Planchard, D., Ahn, M.-J., Smit, E. F., de Langen, A. J., Pérol, M., Pons-Tostivint, E., Novello, S., Hayashi, H., Shimizu, J., Kim, D.-W., Kuo, C.-H., Yang, J. C.-H., Pereira, K., Cheng, F.-C., . . . Jänne, P. A. (2023). Trastuzumab deruxtecan in patients with HER2-mutant metastatic non-small-cell lung cancer: Primary results from the randomized, phase II DESTINY-Lung02 trial. *Journal of Clinical Oncology*, *41*(31), 4852–4863. https://doi.org/10.1200/JCO.23.01361 — PMID 37694347 (PMC10617843). **Two errata:** PMIDs 38113428 (2024) and 39270141 (2024).

**Design:** Phase 2, blinded, multicentre; randomized 2:1 between two doses [A].
**Population:** 152 patients with HER2-mutant metastatic NSCLC previously treated with platinum-containing therapy [A].
**Arms:** T-DXd 5.4 mg/kg vs 6.4 mg/kg every 3 weeks [A].
**Primary endpoint (confirmed ORR by BICR):** 49.0% (39.0–59.1) vs 56.0% (41.3–70.0) [A].
**Secondary:**
- DoR 16.8 (6.4–NE) months vs not estimable [A].
- PFS 9.9 (7.4–NE) vs 15.4 (8.3–NE) months [FT].
- OS 19.5 (13.6–NE) months vs not estimable (12.1–NE) [FT].

**Toxicity:**
- Grade ≥3 drug-related TEAEs 38.6% vs 58.0% [A].
- **Adjudicated drug-related ILD 12.9% (13/101) at 5.4 mg/kg vs 28.0% (14/50) at 6.4 mg/kg**; grade ≥3 ILD 2.0% in each arm [A].
- The safety profile favours 5.4 mg/kg.

---

## 32. Beamion LUNG-1 (zongertinib) — [VERIFIED]

**References**
- Heymach, J. V., Ruiter, G., Ahn, M.-J., Girard, N., Smit, E. F., Planchard, D., Wu, Y.-L., Cho, B. C., Yamamoto, N., Sabari, J. K., Zhao, Y., Tu, H.-Y., Yoh, K., Nadal, E., Sadrolhefazi, B., Rohrbacher, M., von Wangenheim, U., Eigenbrod-Giese, S., & Zugazagoitia, J. (2025). Zongertinib in previously treated HER2-mutant non-small-cell lung cancer. *The New England Journal of Medicine*, *392*(23), 2321–2333. https://doi.org/10.1056/NEJMoa2503704 — PMID 40293180
- (First-line cohort, newer than the brief) Heymach, J. V., Yamamoto, N., Girard, N., Ruiter, G., Smit, E. F., Planchard, D., Nadal, E., Wu, Y.-L., Zugazagoitia, J., Tu, H.-Y., Baik, C. S., Yoh, K., Soo, R. A., Zhao, Y., Sabari, J. K., Wermke, M., Scheffler, M., Ahn, M.-J., Fernamberg, K., . . . Popat, S. (2026). First-line zongertinib in advanced HER2-mutant non-small-cell lung cancer. *The New England Journal of Medicine*, *394*(17), 1675–1684. https://doi.org/10.1056/NEJMoa2516969 — PMID 41985129

**Design:** Phase 1a–1b, multicohort [A].
**Arm:** Zongertinib 120 mg once daily. Cohort 1 initially randomized patients to 120 or 240 mg [A].
**Previously treated (2025) [A]:**
- Cohort 1, tyrosine-kinase-domain mutation (n = 75 at 120 mg): confirmed ORR **71% (60–80)**. DoR 14.1 (6.9–NE) months. PFS 12.4 (8.2–NE) months. Drug-related grade ≥3 AEs 17%.
- Cohort 5, prior HER2 ADC (n = 31): ORR 48% (32–65).
- Cohort 3, non-tyrosine-kinase-domain mutation (n = 20): ORR 30% (15–52).
- **No drug-related ILD in any of the three cohorts.**

**First line, cohort 2 (n = 74, 2026) [A]:**
- Confirmed ORR 76% (65–84). DoR 15.2 (9.8–NE) months. PFS 14.4 (11.1–NE) months.
- Grade ≥3 TRAEs 19%.

**CNS (cohort 4, active brain metastases, n = 30) [A]:**
- Intracranial ORR 47% (30–64) by RANO-BM.
- Grade ≥3 TRAEs 17%.

---

# NTRK

## 33. Larotrectinib — [VERIFIED]

**References**
- Drilon, A., Laetsch, T. W., Kummar, S., DuBois, S. G., Lassen, U. N., Demetri, G. D., Nathenson, M., Doebele, R. C., Farago, A. F., Pappo, A. S., Turpin, B., Dowlati, A., Brose, M. S., Mascarenhas, L., Federman, N., Berlin, J., El-Deiry, W. S., Baik, C., Deeken, J., . . . Hyman, D. M. (2018). Efficacy of larotrectinib in TRK fusion-positive cancers in adults and children. *The New England Journal of Medicine*, *378*(8), 731–739. https://doi.org/10.1056/NEJMoa1714448 — PMID 29466156 (PMC5857389)
- (Lung-specific) Drilon, A., Tan, D. S. W., Lassen, U. N., Leyvraz, S., Liu, Y., Patel, J. D., Rosen, L., Solomon, B., Norenberg, R., Dima, L., Brega, N., Shen, L., Moreno, V., Kummar, S., & Lin, J. J. (2022). Efficacy and safety of larotrectinib in patients with tropomyosin receptor kinase fusion-positive lung cancers. *JCO Precision Oncology*, *6*, e2100418. https://doi.org/10.1200/PO.21.00418 — PMID 35085007

**Design:** Combined analysis of three trials: phase 1 in adults, phase 1–2 in children, phase 2 basket in adolescents and adults [A].
**Population:** 55 patients aged 4 months to 76 years, with 17 TRK fusion-positive tumour types [A].
**Arm:** Larotrectinib 100 mg twice daily for adults and children with BSA ≥1 m²; 100 mg/m² twice daily if BSA <1 m² [FT].
**Primary endpoint (ORR):** 75% (61–85) by independent review; 80% by investigator [A].
**Secondary:**
- At 1 year, 71% of responses were ongoing and 55% of patients were progression-free [A].
- Median DoR and PFS not reached [A].

**Lung cancers (n = 20; 15 evaluable) [A, 2022]:**
- ORR 73% (45–92).
- DoR 33.9 months; PFS 35.4 months; OS 40.7 months.
- **Baseline CNS metastases: ORR 63% (25–91).**

**Toxicity:**
- Mostly grade 1.
- No drug-related grade 3–4 AE occurred in more than 5% of patients.
- No discontinuations for drug-related AEs [A].

---

## Appendix: PMID index

| Trial | Primary PMID | Follow-up / OS PMID(s) |
|---|---|---|
| IPASS | 19692680 | 21670455 |
| ARCHER 1050 | 28958502 | 29864379 (erratum 33113342), 33331989 |
| FLAURA | 29151359 | 31751012; CNS 30153097 |
| FLAURA2 | 37937763 | 41104938 |
| MARIPOSA | 38924756 | 40923797 |
| MARIPOSA-2 | 37879444 | none found |
| PAPILLON | 37870976 | 41671628 (Asia subgroup) |
| AURA3 | 27959700 | 32861806; CNS 30059262 |
| COCOON | 40923969 | — |
| ADAURA | 32955177 | 37272535 |
| LAURA | 38828946 | 39289145 (CNS) |
| Sunvozertinib | 42212913 (WU-KONG28) | 40923280 (WU-KONG1B), 38101437 (WU-KONG6) |
| TROPION-Lung01 / pooled | 39250535 | 39761483 (TL05), 40516821 (pooled EGFR) |
| PROFILE 1014 | 25470694 | 29768118 |
| ALEX | 28586279 | 32418886 (updated), 41110693 (final OS) |
| ALTA-1L | 30280657 | 34537440 |
| CROWN | 33207094 | 38819031 (5-y), 42217582 (7-y) |
| ALINA | 38598794 | — |
| PROFILE 1001 (ROS1) | 25264305 | 30980071 |
| Entrectinib ROS1 | 31838015 | 35663414 |
| TRIDENT-1 | 38197815 | — |
| Taletrectinib | 40179330 (pooled TRUST) | 38822758 (TRUST-I) |
| Dabrafenib + trametinib | 27283860 (pretreated), 28919011 (untreated) | 34455067 |
| PHAROS | 37270692 | 41109959 |
| GEOMETRY mono-1 | 32877583 | 39362249 |
| VISION | 32469185 | 37270698 |
| LIBRETTO-431 | 37870973 | 38828957 (CNS), 41996652 (FDA OS commentary) |
| ARROW | 34118197 | — |
| CodeBreaK 200 | 36764316 | 40129223 (PLS), 40774040 (CNS) |
| KRYSTAL-12 | 40783289 | — |
| DESTINY-Lung02 | 37694347 | — |
| Beamion LUNG-1 | 40293180 | 41985129 (first line) |
| Larotrectinib | 29466156 | 35085007 (lung) |
