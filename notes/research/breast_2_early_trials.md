# Breast 2. Early breast cancer key trials: citation and data verification

Handbook: Taiwanese oncology NP handbook (專科護理師), breast cancer chapter, early-disease section
Verification date: 2026-10-29
Method: Every PMID was pulled from PubMed (NCBI E-utilities esearch/efetch, the same database the PubMed MCP tools query). Numbers come from the PubMed abstract unless another source is named. Where the abstract lacked a requested number, I checked the PMC open-access full text, then the current US FDA prescribing information (openFDA; DailyMed for Verzenio), then the ClinicalTrials.gov registry record. Taiwan licence status comes from the TFDA open-data licence file (dataset 36, downloaded 2026-10-29; file timestamp 2026-10-27). Nothing was filled from memory. Anything still missing is marked **[UNVERIFIED]**.

**Source tags used inline**
- [A] = PubMed abstract of the cited paper
- [FT] = PMC full text of the cited paper (results or methods, not discussion, unless stated)
- [L-xxx] = current US FDA prescribing information (effective date given in Section G)
- [CT] = ClinicalTrials.gov record (API v2)
- [TFDA] = TFDA licence dataset 36
- [SR] = secondary source (review) indexed in PubMed with PMC full text; used only when no primary source was reachable
- **[UNVERIFIED]** = not found in any source checked; do not print without checking the full paper

**Section status tags**
- **[VERIFIED]** = citation confirmed on PubMed, and the primary-endpoint result (rate, HR, 95% CI where reported) confirmed from [A], [FT] or [L]
- **[PARTIAL]** = citation confirmed, but part of the requested content (usually a dose or a toxicity rate) comes only from a secondary source or is missing
- **[UNVERIFIED]** = paper not found

**APA 7 notes.** Author lists follow APA 7: all authors up to 20; for 21 or more, the first 19, an ellipsis, then the final author. Study-group bylines ("for the … Investigators") are left out; EBCTCG papers have the group as sole author. Titles are converted to sentence case. The year is the year of the journal issue, which can differ from the e-pub year (monarchE OS, PALLAS 5-year, DESTINY-Breast05, DESTINY-Breast11 and SOFT/TEXT final were all e-published 2025 or early 2026). Generational suffixes are written as in APA (Jr., II, III).

---

## 0. Corrections and flags for the editor (read first)

1. **SOFT/TEXT has a final 15-year report** (Francis et al., *Ann Oncol 37*(10), 2026; PMID 42229584). It supersedes the 2023 JCO 12/13-year updates. Key change: the **8-year SOFT OS benefit of adding OFS to tamoxifen (P = 0.01) is no longer significant at 15 years** (HR 0.87, 95% CI 0.68–1.10). In the combined analysis exemestane + OFS still improves DFS (HR 0.82) and distant recurrence (HR 0.83) but **not OS (HR 0.94, 0.80–1.11)**. OS gains are confined to high-risk subgroups (age < 35, prior chemotherapy, grade 3, HER2-negative).
2. **monarchE OS is now positive**: HR 0.842 (95% CI 0.722–0.981), P = 0.027, 7-year OS 86.8% vs 85.0% (Johnston et al., *Ann Oncol 37*(2), 2026; e-pub 2025). Older handbooks that say "OS immature/no difference (HR 0.929)" quote the 2023 interim.
3. **NATALEE OS is still not significant**: 5-year analysis HR 0.800 (0.637–1.003), nominal one-sided P = 0.026 (Crown et al., *ESMO Open* 2025). Do not write "ribociclib improves OS".
4. **KEYNOTE-522 pCR: two different numbers circulate.** 64.8% vs 51.2% (Δ13.6) is the first interim analysis of the first 602 patients. The **full ITT (n = 1174) pCR is 63.0% vs 55.6% (Δ7.5, 95% CI 1.6–13.4)** [L-Keytruda]. Use the ITT figure in the handbook. The OS HR (0.66, 0.50–0.87) is not in the NEJM 2024 abstract; it is confirmed from the FDA label.
5. **DESTINY-Breast05 and DESTINY-Breast11 are both published.** DB-05: Loibl et al., *NEJM 394*(9), 845–857, 2026 (erratum PMID 41931063, not reviewed). DB-11: Harbeck et al., *Ann Oncol 37*(2), 166–179, 2026. The T-DXd-monotherapy arm of DB-11 was **closed early** on IDMC advice (pCR 43.0%). DB-05 drug-related ILD 9.6% vs 1.6%, with 2 ILD deaths.
6. **Taiwan licence gap (TFDA, 2026-10-27 file):** Enhertu (優赫得) carries the **DB-11 neoadjuvant indication but not the DB-05 post-neoadjuvant indication**, which the US label already has. Kadcyla remains the only TFDA-licensed post-neoadjuvant ADC for residual HER2-positive disease.
7. **OlympiA has a third (6.1-year) update** (Garber et al., *Ann Oncol* 2026, ahead of print, PMID 42636977): OS HR 0.72 (0.56–0.93), 6-year OS 87.5% vs 83.2%. MDS/AML 0.4% vs 0.7% (no excess).
8. **APHINITY has no significant OS benefit** at 8.4 years (HR 0.83, 0.68–1.02, P = .078; threshold 0.006). No final OS paper was found on PubMed as of 2026-10-29.
9. **ExteNET final OS is null**: 8-year OS 90.1% vs 90.2%, HR 0.95 (0.75–1.21). Benefit claims rest on iDFS in the HR-positive, ≤1 year from trastuzumab subgroup (exploratory).
10. **KATHERINE OS (Geyer et al., NEJM 2025)**: HR 0.66 (0.51–0.87), P = 0.003; 7-year OS 89.1% vs 84.4%. The HR is **unstratified**.
11. **NSABP B-42 at 7 years was formally negative** (HR 0.85, 95% CI 0.73–0.999, P = 0.048 against a significance threshold of 0.0418). The **10-year update** reached significance for DFS (HR 0.85, 0.74–0.96, P = .01) but not OS (HR 0.97).
12. **New key meta-analysis on extended endocrine therapy:** EBCTCG, *Lancet 406*, 603–614 (2025), 12 trials, 22,031 women. Extended AI reduced recurrence by 27% (RR 0.73); breast cancer mortality reduction not significant (RR 0.90, 0.70–1.15). Erratum PMID 40812341 (not reviewed).
13. **NeoSphere** is a **phase 2** trial whose primary endpoint was **breast pCR (ypT0/is)**, not total pCR. Its 5-year PFS comparisons were descriptive and not powered.
14. **CALGB 9741 doses**: the JCO 2003 full text is paywalled (HTTP 403). Doses were confirmed from the ClinicalTrials.gov record (NCT00003088), not from the paper.
15. **CREATE-X capecitabine dose** (1,250 mg/m² twice daily, days 1–14 q3w, 6–8 cycles) is confirmed only from a secondary review in PMC [SR]. The NEJM paper is not open access. Note that the dose is **higher than the 1,000 mg/m² twice daily** used in the later EA1131 trial (same review).
16. **Errata exist; check them before quoting a number:** APHINITY NEJM 2017 (2 errata), SOFT 12-year JCO 2023 (PMID 37450784), EBCTCG premenopausal AI 2022 (PMID 35358463), EBCTCG extended AI 2025 (PMID 40812341), ATLAS (2013 erratum, plus PMID 28457627 on exclusion of 1 of 402 centres), NSABP B-42 2019 (PMID 30614468) and 2023 (PMID 37766422), APT NEJM 2015 (PMID 26559595), EBCTCG bisphosphonates 2015 (2 errata), CALGB 9741 JCO 2003 (erratum), DESTINY-Breast05 (PMID 41931063). I did not check what each erratum changes.
17. **Not found on PubMed as of 2026-10-29:** a published RxPONDER update beyond the 2021 primary report (only secondary analyses); APHINITY final OS; NATALEE final OS; DESTINY-Breast05 OS (immature, not in abstract or label); a full-text paper for KEYNOTE-522 OS with an OS HR in the abstract.

---

# A. Endocrine therapy

## 1. SOFT and TEXT (ovarian function suppression; exemestane vs tamoxifen) — [VERIFIED]

**References**
- (TEXT + SOFT combined primary) Pagani, O., Regan, M. M., Walley, B. A., Fleming, G. F., Colleoni, M., Láng, I., Gomez, H. L., Tondini, C., Burstein, H. J., Perez, E. A., Ciruelos, E., Stearns, V., Bonnefoi, H. R., Martino, S., Geyer, C. E., Jr., Pinotti, G., Puglisi, F., Crivellari, D., Ruhstaller, T., . . . Francis, P. A. (2014). Adjuvant exemestane with ovarian suppression in premenopausal breast cancer. *The New England Journal of Medicine*, *371*(2), 107–118. https://doi.org/10.1056/NEJMoa1404037 — PMID 24881463
- (SOFT primary) Francis, P. A., Regan, M. M., Fleming, G. F., Láng, I., Ciruelos, E., Bellet, M., Bonnefoi, H. R., Climent, M. A., Da Prada, G. A., Burstein, H. J., Martino, S., Davidson, N. E., Geyer, C. E., Jr., Walley, B. A., Coleman, R., Kerbrat, P., Buchholz, S., Ingle, J. N., Winer, E. P., . . . Gelber, R. D. (2015). Adjuvant ovarian suppression in premenopausal breast cancer. *The New England Journal of Medicine*, *372*(5), 436–446. https://doi.org/10.1056/NEJMoa1412379 — PMID 25495490
- (8-year) Francis, P. A., Pagani, O., Fleming, G. F., Walley, B. A., Colleoni, M., Láng, I., Gómez, H. L., Tondini, C., Ciruelos, E., Burstein, H. J., Bonnefoi, H. R., Bellet, M., Martino, S., Geyer, C. E., Jr., Goetz, M. P., Stearns, V., Pinotti, G., Puglisi, F., Spazzapan, S., . . . Regan, M. M. (2018). Tailoring adjuvant endocrine therapy for premenopausal breast cancer. *The New England Journal of Medicine*, *379*(2), 122–137. https://doi.org/10.1056/NEJMoa1803164 — PMID 29863451
- (12-year SOFT) Francis, P. A., Fleming, G. F., Láng, I., Ciruelos, E. M., Bonnefoi, H. R., Bellet, M., Bernardo, A., Climent, M. A., Martino, S., Bermejo, B., Burstein, H. J., Davidson, N. E., Geyer, C. E., Jr., Walley, B. A., Ingle, J. N., Coleman, R. E., Müller, B., Le Du, F., Loibl, S., . . . Regan, M. M. (2023). Adjuvant endocrine therapy in premenopausal breast cancer: 12-year results from SOFT. *Journal of Clinical Oncology*, *41*(7), 1370–1375. https://doi.org/10.1200/JCO.22.01065 — PMID 36493334. **Erratum:** PMID 37450784 (not reviewed).
- (13-year combined) Pagani, O., Walley, B. A., Fleming, G. F., Colleoni, M., Láng, I., Gomez, H. L., Tondini, C., Burstein, H. J., Goetz, M. P., Ciruelos, E. M., Stearns, V., Bonnefoi, H. R., Martino, S., Geyer, C. E., Jr., Chini, C., Puglisi, F., Spazzapan, S., Ruhstaller, T., Winer, E. P., . . . Francis, P. A. (2023). Adjuvant exemestane with ovarian suppression in premenopausal breast cancer: Long-term follow-up of the combined TEXT and SOFT trials. *Journal of Clinical Oncology*, *41*(7), 1376–1382. https://doi.org/10.1200/JCO.22.01064 — PMID 36521078
- **(Final, latest) Francis, P. A., Pagani, O., Fleming, G. F., Walley, B. A., Colleoni, M., Rubovszky, G., Tondini, C., Ciruelos, E. M., Gomez, H. L., Bonnefoi, H. R., Burstein, H. J., Chini, C., Puglisi, F., Spazzapan, S., Bernardo, A., Climent, M. A., Bellet, M., Ruhstaller, T., Bermejo, B., . . . Regan, M. M. (2026). Final outcomes of the SOFT and TEXT phase III trials in premenopausal hormone receptor-positive early breast cancer. *Annals of Oncology*, *37*(10), 1367–1385. https://doi.org/10.1016/j.annonc.2026.05.704 — PMID 42229584 (PMC13484932)**

**Design:** Two phase 3, open-label, randomized trials (IBCSG) [A].
**Population:** Premenopausal women with HR-positive early breast cancer. Final ITT: SOFT 3,047, TEXT 2,660 [A, final].
- SOFT: women still premenopausal after (neo)adjuvant chemotherapy, or for whom tamoxifen alone was reasonable. Stratified by prior chemotherapy [A].
- TEXT: OFS from the start; optional chemotherapy given concurrently with triptorelin [A, FT 2014].

**Arms (all 5 years)** [FT 2014]:
- Exemestane 25 mg orally daily + OFS.
- Tamoxifen 20 mg orally daily + OFS.
- SOFT only: tamoxifen 20 mg daily alone.
- OFS = triptorelin 3.75 mg IM every 28 days; bilateral oophorectomy or ovarian irradiation allowed (in TEXT after ≥6 months of triptorelin).
- TEXT without chemotherapy: oral endocrine therapy started 6–8 weeks after the first triptorelin dose [FT 2014].

**Primary endpoint:** DFS.

**Results by analysis**
- 2014 combined (median FU 68 months): 5-year DFS 91.1% (E+OFS) vs 87.3% (T+OFS); HR 0.72 (0.60–0.85), P < 0.001. OS HR 1.14 (0.86–1.51), NS [A].
- 2015 SOFT primary (median FU 67 months): 5-year DFS 86.6% (T+OFS) vs 84.7% (T); HR 0.83 (0.66–1.04), P = 0.10. **Not significant overall.** Prior-chemotherapy cohort freedom from breast cancer 82.5% vs 78.0%, HR 0.78 (0.60–1.02) [A].
- 2018 (8-year SOFT): DFS 78.9% (T), 83.2% (T+OFS), 85.9% (E+OFS); P = 0.009 for T vs T+OFS. OS 91.5%, 93.3%, 92.1%; P = 0.01 for T vs T+OFS [A].
- 2023 combined (median FU 13 years): 12-year DFS HR 0.79 (0.70–0.90); DRFI HR 0.83 (0.70–0.98); OS 90.1% vs 89.1%, HR 0.93 (0.78–1.11) [A].

**Final 15-year results (Francis 2026)** [A, FT]
| Comparison | Endpoint | HR (95% CI) | 15-year rates |
|---|---|---|---|
| SOFT: T+OFS vs T | DFS | 0.85 (0.72–1.00), P = 0.05 | E+OFS 73.5% / T+OFS 70.5% / T 67.0% |
| SOFT: E+OFS vs T | DFS | 0.73 (0.61–0.86) | — |
| SOFT: T+OFS vs T | BCFI | 0.82 (0.69–0.98), P = 0.03 | 78.6% / 75.7% / 72.1% |
| SOFT: T+OFS vs T | DRFI | 0.93 (0.75–1.17), P = 0.56 | 86.4% / 83.6% / 83.5% |
| SOFT: T+OFS vs T | OS | **0.87 (0.68–1.10)** | 86.9% / 86.7% / 85.3% |
| SOFT: E+OFS vs T | OS | 0.85 (0.67–1.08) | — |
| SOFT+TEXT: E+OFS vs T+OFS | DFS | 0.82 (0.73–0.92), P < 0.01 | 74.9% vs 71.3% |
| SOFT+TEXT: E+OFS vs T+OFS | DRFI | 0.83 (0.71–0.97), P = 0.02 | 86.5% vs 83.9% |
| SOFT+TEXT: E+OFS vs T+OFS | OS | **0.94 (0.80–1.11), P = 0.48** | 87.8% vs 87.0% |
| SOFT+TEXT, HER2-negative (n = 4,035) | DRFI | 0.75 (0.63–0.90) | 87.6% vs 83.7% |
| SOFT+TEXT, HER2-negative | OS | 0.89 (0.74–1.06) | 88.5% vs 86.9% |

**High-risk subgroups (final)** [A, FT]
- SOFT, prior chemotherapy, HER2-negative (n = 1,257): 15-year OS 81.0% (E+OFS), 77.1% (T+OFS), 76.8% (T).
- SOFT, age < 35, HER2-negative (n = 241): 15-year OS 82.5%, 77.9%, 68.1%. Only 51.3% of those on tamoxifen alone were free of breast cancer at 15 years.
- SOFT no-chemotherapy cohort: 15-year DRFI > 94% and OS > 94% in all arms.
- Combined, grade 3 HER2-negative: absolute 15-year benefit of E+OFS over T+OFS of 12.1% (BCFI), 9.7% (DRFI), 5.8% (OS) [FT, discussion; supplementary figure].

**Toxicity**
- Grade 3–4 targeted AEs (2014): 30.6% (E+OFS) vs 29.4% (T+OFS). Commonest grade 3–4: hot flushes, musculoskeletal symptoms, hypertension. Depression any grade 50.2%, grade 3–4 4.1% [FT 2014].
- Osteoporosis (T-score < −2.5): 13.2% (E+OFS) vs 6.4% (T+OFS) [FT 2014].
- More with exemestane: fractures, musculoskeletal symptoms, vaginal dryness, decreased libido, dyspareunia. More with tamoxifen: thromboembolism, hot flushes, sweating, urinary incontinence [FT 2014].
- Grade ≥3 AEs (2018, SOFT): 24.6% (T), 31.0% (T+OFS), 32.3% (E+OFS) [A].
- Late (after year 6) cumulative fracture incidence: 4.2% (T), 6.6% (T+OFS), 6.8% (E+OFS) [FT final].

---

## 2. EBCTCG: aromatase inhibitor vs tamoxifen — [VERIFIED]

**References**
- Early Breast Cancer Trialists' Collaborative Group. (2015). Aromatase inhibitors versus tamoxifen in early breast cancer: Patient-level meta-analysis of the randomised trials. *The Lancet*, *386*(10001), 1341–1352. https://doi.org/10.1016/S0140-6736(15)61074-1 — PMID 26211827
- (Premenopausal with OFS) Early Breast Cancer Trialists' Collaborative Group. (2022). Aromatase inhibitors versus tamoxifen in premenopausal women with oestrogen receptor-positive early-stage breast cancer treated with ovarian suppression: A patient-level meta-analysis of 7030 women from four randomised trials. *The Lancet Oncology*, *23*(3), 382–392. https://doi.org/10.1016/S1470-2045(21)00758-0 — PMID 35123662. **Erratum:** PMID 35358463 (not reviewed).

**2015 postmenopausal meta-analysis** [A]
- Individual data on 31,920 postmenopausal women with ER-positive disease. Three comparisons: AI 5 y vs tamoxifen 5 y; AI 5 y vs tamoxifen 2–3 y → AI; tamoxifen 2–3 y → AI vs tamoxifen 5 y.
- **AI 5 y vs tamoxifen 5 y:** recurrence RR 0.64 (0.52–0.78) in years 0–1 and 0.80 (0.68–0.93) in years 2–4; not significant afterwards. 10-year breast cancer mortality 12.1% vs 14.2%, RR 0.85 (0.75–0.96), 2p = 0.009.
- AI 5 y vs tamoxifen → AI: recurrence RR 0.90 (0.81–0.99), 2p = 0.045; breast cancer mortality RR 0.89 (0.78–1.03), NS.
- Switch (tamoxifen → AI) vs tamoxifen 5 y: 10-year breast cancer mortality 8.7% vs 10.1%, 2p = 0.015.
- All comparisons pooled: recurrence RR 0.70 (0.64–0.77) while treatments differed; breast cancer mortality RR 0.86 (0.80–0.94); all-cause mortality RR 0.88 (0.82–0.94).
- Take-home: AI reduces recurrence by about 30% while treatments differ; 5 years of AI cuts 10-year breast cancer mortality by about 15% vs tamoxifen and by about 40% vs no endocrine therapy.
- Toxicity: endometrial cancer 10-year 0.4% vs 1.2% (RR 0.33, 0.21–0.51); **fractures 5-year 8.2% vs 5.5% (RR 1.42, 1.28–1.57)**; non-breast-cancer mortality similar.

**2022 premenopausal (with OFS) meta-analysis** [A]
- 4 trials (ABCSG XII, SOFT, TEXT, HOBOE), 7,030 women, median FU 8.0 years.
- Recurrence RR 0.79 (0.69–0.90), P = 0.0005. Benefit concentrated in years 0–4: RR 0.68 (99% CI 0.55–0.85); 5-year recurrence 6.9% vs 10.1% (absolute 3.2%).
- Distant recurrence RR 0.83 (0.71–0.97).
- **No difference in breast cancer mortality** (RR 1.01, 0.82–1.24) or all-cause mortality (RR 1.04, 0.86–1.27).
- Fractures 6.4% vs 5.1%, RR 1.27 (1.04–1.54).

---

## 3. Extended endocrine therapy — [VERIFIED]

**References**
- Davies, C., Pan, H., Godwin, J., Gray, R., Arriagada, R., Raina, V., Abraham, M., Medeiros Alencar, V. H., Badran, A., Bonfill, X., Bradbury, J., Clarke, M., Collins, R., Davis, S. R., Delmestri, A., Forbes, J. F., Haddad, P., Hou, M.-F., Inbar, M., . . . Peto, R. (2013). Long-term effects of continuing adjuvant tamoxifen to 10 years versus stopping at 5 years after diagnosis of oestrogen receptor-positive breast cancer: ATLAS, a randomised trial. *The Lancet*, *381*(9869), 805–816. https://doi.org/10.1016/S0140-6736(12)61963-1 — PMID 23219286. **Errata:** 2013 (no PMID) and PMID 28457627 (exclusion of 1 of 402 centres).
- Goss, P. E., Ingle, J. N., Martino, S., Robert, N. J., Muss, H. B., Piccart, M. J., Castiglione, M., Tu, D., Shepherd, L. E., Pritchard, K. I., Livingston, R. B., Davidson, N. E., Norton, L., Perez, E. A., Abrams, J. S., Therasse, P., Palmer, M. J., & Pater, J. L. (2003). A randomized trial of letrozole in postmenopausal women after five years of tamoxifen therapy for early-stage breast cancer. *The New England Journal of Medicine*, *349*(19), 1793–1802. https://doi.org/10.1056/NEJMoa032312 — PMID 14551341
- Goss, P. E., Ingle, J. N., Pritchard, K. I., Robert, N. J., Muss, H., Gralow, J., Gelmon, K., Whelan, T., Strasser-Weippl, K., Rubin, S., Sturtz, K., Wolff, A. C., Winer, E., Hudis, C., Stopeck, A., Beck, J. T., Kaur, J. S., Whelan, K., Tu, D., & Parulekar, W. R. (2016). Extending aromatase-inhibitor adjuvant therapy to 10 years. *The New England Journal of Medicine*, *375*(3), 209–219. https://doi.org/10.1056/NEJMoa1604700 — PMID 27264120
- Mamounas, E. P., Bandos, H., Lembersky, B. C., Jeong, J.-H., Geyer, C. E., Jr., Rastogi, P., Fehrenbacher, L., Graham, M. L., Chia, S. K., Brufsky, A. M., Walshe, J. M., Soori, G. S., Dakhil, S. R., Seay, T. E., Wade, J. L., III, McCarron, E. C., Paik, S., Swain, S. M., Wickerham, D. L., & Wolmark, N. (2019). Use of letrozole after aromatase inhibitor-based therapy in postmenopausal breast cancer (NRG Oncology/NSABP B-42): A randomised, double-blind, placebo-controlled, phase 3 trial. *The Lancet Oncology*, *20*(1), 88–99. https://doi.org/10.1016/S1470-2045(18)30621-1 — PMID 30509771. **Erratum:** PMID 30614468.
- Mamounas, E. P., Bandos, H., Rastogi, P., Lembersky, B. C., Jeong, J.-H., Geyer, C. E., Jr., Fehrenbacher, L., Chia, S. K., Brufsky, A. M., Walshe, J. M., Soori, G. S., Dakhil, S. R., Wade, J. L., III, McCarron, E. C., Swain, S. M., & Wolmark, N. (2023). Ten-year update: NRG Oncology/National Surgical Adjuvant Breast and Bowel Project B-42 randomized trial: Extended letrozole therapy in early-stage breast cancer. *Journal of the National Cancer Institute*, *115*(11), 1302–1309. https://doi.org/10.1093/jnci/djad078 — PMID 37184928. **Erratum:** PMID 37766422.
- Gnant, M., Fitzal, F., Rinnerthaler, G., Steger, G. G., Greil-Ressler, S., Balic, M., Heck, D., Jakesz, R., Thaler, J., Egle, D., Manfreda, D., Bjelic-Radisic, V., Wieder, U., Singer, C. F., Melbinger-Zeinitzer, E., Haslbauer, F., Sevelda, P., Trapl, H., Wette, V., . . . Greil, R. (2021). Duration of adjuvant aromatase-inhibitor therapy in postmenopausal breast cancer. *The New England Journal of Medicine*, *385*(5), 395–405. https://doi.org/10.1056/NEJMoa2104162 — PMID 34320285
- Early Breast Cancer Trialists' Collaborative Group. (2025). Extending the duration of endocrine treatment for early breast cancer: Patient-level meta-analysis of 12 randomised trials of aromatase inhibitors in 22 031 postmenopausal women already treated with at least 5 years of endocrine therapy. *The Lancet*, *406*(10503), 603–614. https://doi.org/10.1016/S0140-6736(25)01013-X — PMID 40783288. **Erratum:** PMID 40812341.
- Pan, H., Gray, R., Braybrooke, J., Davies, C., Taylor, C., McGale, P., Peto, R., Pritchard, K. I., Bergh, J., Dowsett, M., & Hayes, D. F. (2017). 20-year risks of breast-cancer recurrence after stopping endocrine therapy at 5 years. *The New England Journal of Medicine*, *377*(19), 1836–1846. https://doi.org/10.1056/NEJMoa1701830 — PMID 29117498

**Why extend: late-recurrence risk (Pan 2017, EBCTCG, 88 trials, 62,923 women)** [A]
- Recurrence continued at a steady rate from year 5 to year 20 after stopping 5 years of endocrine therapy.
- 5–20-year distant recurrence risk by original TN status: T1N0 13%, T1N1–3 20%, T1N4–9 34%; T2N0 19%, T2N1–3 26%, T2N4–9 41%.
- T1N0 by grade: low 10%, moderate 13%, high 17%.

**ATLAS (tamoxifen 10 vs 5 years)** [A, FT]
- 12,894 women randomized after 5 years of tamoxifen; outcomes reported for 6,846 with ER-positive disease. Tamoxifen was almost always 20 mg/day [FT].
- Recurrence 617 vs 711 events, P = 0.002. Breast cancer deaths 331 vs 397, P = 0.01. All deaths 639 vs 722, P = 0.01.
- Effect larger after year 10: recurrence RR 0.90 (0.79–1.02) in years 5–9 and 0.75 (0.62–0.90) later.
- Cumulative years 5–14: recurrence 21.4% vs 25.1%; breast cancer mortality 12.2% vs 15.0% (absolute 2.8%).
- Toxicity: pulmonary embolus RR 1.87 (1.13–3.07); endometrial cancer RR 1.74 (1.30–2.34), cumulative 3.1% vs 1.6% (mortality 0.4% vs 0.2%); ischaemic heart disease RR 0.76 (0.60–0.95); stroke RR 1.06 (0.83–1.36).

**MA.17 (letrozole after 5 years tamoxifen)** [A]
- Double-blind, placebo-controlled; 5,187 women; median FU 2.4 years at the first interim analysis, which stopped the trial.
- 4-year DFS 93% vs 87%, P ≤ 0.001. Deaths 31 vs 42, P = 0.25.
- Osteoporosis 5.8% vs 4.5%, P = 0.07; fracture rates similar. More hot flushes, arthralgia and myalgia; less vaginal bleeding.

**MA.17R (letrozole to 10 years of AI)** [A, FT]
- Double-blind, placebo-controlled; 1,918 women after 4.5–6 years of AI (most also had prior tamoxifen). Letrozole 2.5 mg daily for 5 more years [FT].
- Median FU 6.3 years. 5-year DFS 95% (93–96) vs 91% (89–93); HR 0.66, P = 0.01.
- OS 93% vs 94%, HR 0.97, P = 0.83.
- Contralateral breast cancer annual rate 0.21% vs 0.49%, HR 0.42, P = 0.007.
- More bone pain, fractures and new osteoporosis with letrozole; QoL similar.

**NSABP B-42 (letrozole after 5 years AI-based therapy)** [A]
- Phase 3, double-blind; 3,966 postmenopausal women, stage I–IIIA; letrozole 2.5 mg daily vs placebo for 5 years.
- 7-year: DFS 84.7% vs 81.3%; HR 0.85 (0.73–0.999), P = 0.048. **Not significant** (threshold 0.0418).
- 10-year (median FU 10.3 years): DFS 75.9% vs 72.6%, HR 0.85 (0.74–0.96), P = .01. BCFI HR 0.75 (0.62–0.91). Distant recurrence HR 0.72 (0.55–0.92). OS HR 0.97 (0.82–1.15), NS. Osteoporotic fractures and arterial thrombotic events did not differ.

**ABCSG-16/SALSA (anastrozole 2 vs 5 extra years)** [A]
- Phase 3; 3,484 enrolled after 5 years of endocrine therapy; primary analysis in 3,208 recurrence-free at 2 years.
- DFS: 335 events in each arm; HR 0.99 (0.85–1.15), P = 0.90.
- Clinical bone fracture HR 1.35 (1.00–1.84) with 5 extra years.
- Take-home: 7 years total was as good as 10 years.

**EBCTCG 2025 extended-AI meta-analysis** [A]
- 12 trials, 22,031 postmenopausal women recurrence-free after ≥5 years of endocrine therapy.
- AI vs no further therapy: recurrence RR 0.73 (0.67–0.80).
- After some previous AI, 5 more years of AI: recurrence RR 0.71 (0.61–0.81), years 5–15 risk 11.6% vs 15.2%; distant recurrence RR 0.73 (0.61–0.88), 6.6% vs 8.6%; **breast cancer mortality RR 0.90 (0.70–1.15), NS**.
- Absolute benefit larger in node-positive (16.3% vs 20.1%) than node-negative disease (9.1% vs 11.8%).
- Fracture 5-year risk 4.6% vs 3.4%, RR 1.35 (1.13–1.61).
- Non-adherence was common: 39.0% (AI) vs 37.6% (placebo) in placebo-controlled trials.

---

# B. CDK4/6 inhibitors (HR-positive/HER2-negative)

## 4. monarchE (adjuvant abemaciclib) — [VERIFIED]

**References**
- Johnston, S. R. D., Harbeck, N., Hegg, R., Toi, M., Martin, M., Shao, Z. M., Zhang, Q. Y., Martinez Rodriguez, J. L., Campone, M., Hamilton, E., Sohn, J., Guarneri, V., Okada, M., Boyle, F., Neven, P., Cortés, J., Huober, J., Wardley, A., Tolaney, S. M., . . . Rastogi, P. (2020). Abemaciclib combined with endocrine therapy for the adjuvant treatment of HR+, HER2−, node-positive, high-risk, early breast cancer (monarchE). *Journal of Clinical Oncology*, *38*(34), 3987–3998. https://doi.org/10.1200/JCO.20.02514 — PMID 32954927
- Harbeck, N., Rastogi, P., Martin, M., Tolaney, S. M., Shao, Z. M., Fasching, P. A., Huang, C. S., Jaliffe, G. G., Tryakin, A., Goetz, M. P., Rugo, H. S., Senkus, E., Testa, L., Andersson, M., Tamura, K., Del Mastro, L., Steger, G. G., Kreipe, H., Hegg, R., . . . O'Shaughnessy, J. (2021). Adjuvant abemaciclib combined with endocrine therapy for high-risk early breast cancer: Updated efficacy and Ki-67 analysis from the monarchE study. *Annals of Oncology*, *32*(12), 1571–1581. https://doi.org/10.1016/j.annonc.2021.09.015 — PMID 34656740
- Johnston, S. R. D., Toi, M., O'Shaughnessy, J., Rastogi, P., Campone, M., Neven, P., Huang, C.-S., Huober, J., Jaliffe, G. G., Cicin, I., Tolaney, S. M., Goetz, M. P., Rugo, H. S., Senkus, E., Testa, L., Del Mastro, L., Shimizu, C., Wei, R., Shahir, A., . . . Martin, M. (2023). Abemaciclib plus endocrine therapy for hormone receptor-positive, HER2-negative, node-positive, high-risk early breast cancer (monarchE): Results from a preplanned interim analysis of a randomised, open-label, phase 3 trial. *The Lancet Oncology*, *24*(1), 77–90. https://doi.org/10.1016/S1470-2045(22)00694-5 — PMID 36493792
- (Safety/PRO) Rugo, H. S., O'Shaughnessy, J., Boyle, F., Toi, M., Broom, R., Blancas, I., Gumus, M., Yamashita, T., Im, Y.-H., Rastogi, P., Zagouri, F., Song, C., Campone, M., San Antonio, B., Shahir, A., Hulstijn, M., Brown, J., Zimmermann, A., Wei, R., . . . Tolaney, S. M. (2022). Adjuvant abemaciclib combined with endocrine therapy for high-risk early breast cancer: Safety and patient-reported outcomes from the monarchE study. *Annals of Oncology*, *33*(6), 616–627. https://doi.org/10.1016/j.annonc.2022.03.006 — PMID 35337972
- **(OS, latest) Johnston, S., Martin, M., O'Shaughnessy, J., Hegg, R., Tolaney, S. M., Guarneri, V., Del Mastro, L., Campone, M., Sohn, J., Boyle, F., Cortes, J., Rugo, H. S., Goetz, M. P., Hamilton, E. P., Huang, C.-S., Senkus, E., Cicin, I., Testa, L., Neven, P., . . . Harbeck, N. (2026). Overall survival with abemaciclib in early breast cancer. *Annals of Oncology*, *37*(2), 155–165. https://doi.org/10.1016/j.annonc.2025.10.005 — PMID 41110697** (e-pub 2025)

**Design:** Phase 3, open-label, randomized 1:1; 603 sites in 38 countries [A 2023].
**Population:** 5,637 patients with HR+/HER2− node-positive high-risk EBC [A].
- Cohort 1: ≥4 positive axillary nodes, or 1–3 nodes plus grade 3 or tumour ≥5 cm.
- Cohort 2: 1–3 nodes plus central Ki-67 ≥20% [A 2021].

**Arms:** Abemaciclib 150 mg orally twice daily for 2 years + standard ET (≥5 years, up to 10) vs ET alone [A 2020, 2023].

**Primary endpoint (IDFS)**
| Analysis | Median FU | IDFS HR (95% CI) | Rates |
|---|---|---|---|
| 2020 interim | — | 0.75 (0.60–0.93), P = .01 | 2-year 92.2% vs 88.7% |
| 2021 primary outcome | 19 months | 0.71 (0.58–0.87) | — |
| 2021 additional FU | 27 months | 0.70 (0.59–0.82); DRFS 0.69 (0.57–0.83) | 3-year Δ IDFS 5.4%, Δ DRFS 4.2% |
| 2023 OS interim | 42 months | 0.664 (0.578–0.762) | 4-year 85.8% vs 79.4% |
| **2026 primary OS** | **76.2 months** | **0.734 (0.657–0.820); DRFS 0.746 (0.662–0.840)** | **7-year IDFS 77.4% vs 70.9%; DRFS 80.0% vs 74.9%** |

**OS:**
- 2023 interim: HR 0.929 (0.748–1.153), P = 0.50 [A].
- **2026 primary OS: 661 deaths; HR 0.842 (0.722–0.981), P = 0.027 (met the boundary). 7-year OS 86.8% vs 85.0% (Δ1.8%).** Living with metastatic disease: 6.4% vs 9.4% [A].

**Toxicity**
- Grade 3–4 (2023): neutropenia 19.6% vs 0.9%, leukopenia 11.4% vs 0.4%, diarrhoea 7.8% vs 0.2%. SAEs 15.5% vs 9.1%. Two treatment-related deaths (diarrhoea, pneumonitis) [A].
- Grade ≥3 AEs 49.7% vs 16.3%. Discontinuation due to AEs 18.5%. Dose holds 61.7%, dose reductions 43.4% [A, Rugo 2022].
- Diarrhoea: all grades **84%** (grade 3 8%) vs 9% [L-Verzenio]. Mostly grade 1–2 (76%); grade 2–3 peaks in month 1 (20.5%) [A, Rugo 2022].
- **VTE 2.5% vs 0.6%; with tamoxifen 4.3% vs with AI 1.8%** [A, Rugo 2022].
- ILD/pneumonitis 3% (grade 3–4 0.4%; 1 death, 0.1%) [L-Verzenio].
- Label monitoring: LFTs before start, every 2 weeks for 2 months, monthly for 2 months [L-Verzenio].

---

## 5. NATALEE (adjuvant ribociclib) — [VERIFIED]

**References**
- Slamon, D., Lipatov, O., Nowecki, Z., McAndrew, N., Kukielka-Budny, B., Stroyakovskiy, D., Yardley, D. A., Huang, C.-S., Fasching, P. A., Crown, J., Bardia, A., Chia, S., Im, S.-A., Ruiz-Borrego, M., Loi, S., Xu, B., Hurvitz, S., Barrios, C., Untch, M., . . . Hortobagyi, G. (2024). Ribociclib plus endocrine therapy in early breast cancer. *The New England Journal of Medicine*, *390*(12), 1080–1091. https://doi.org/10.1056/NEJMoa2305488 — PMID 38507751
- Hortobagyi, G. N., Lacko, A., Sohn, J., Cruz, F., Ruiz Borrego, M., Manikhas, A., Hee Park, Y., Stroyakovskiy, D., Yardley, D. A., Huang, C.-S., Fasching, P. A., Crown, J., Bardia, A., Chia, S., Im, S.-A., Martin, M., Loi, S., Xu, B., Hurvitz, S., . . . Slamon, D. (2025). A phase III trial of adjuvant ribociclib plus endocrine therapy versus endocrine therapy alone in patients with HR-positive/HER2-negative early breast cancer: Final invasive disease-free survival results from the NATALEE trial. *Annals of Oncology*, *36*(2), 149–157. https://doi.org/10.1016/j.annonc.2024.10.015 — PMID 39442617
- Fasching, P. A., Stroyakovskiy, D., Yardley, D. A., Huang, C.-S., Crown, J., Bardia, A., Chia, S., Im, S.-A., Martin, M., Xu, B., Loi, S., Barrios, C., Untch, M., Moroose, R., Visco, F., Hortobagyi, G. N., Slamon, D. J., Fresco, R., Zarate, J. P., . . . Hurvitz, S. A. (2025). Ribociclib plus endocrine therapy in hormone receptor-positive/ERBB2-negative early breast cancer: 4-year outcomes from the NATALEE randomized clinical trial. *JAMA Oncology*, *11*(11), 1364–1372. https://doi.org/10.1001/jamaoncol.2025.3700 — PMID 40996773
- **(5-year, latest) Crown, J., Stroyakovskii, D., Yardley, D. A., Huang, C.-S., Fasching, P. A., Bardia, A., Chia, S., Im, S.-A., Martin, M., Xu, B., Barrios, C. H., Untch, M., Moroose, R., Hurvitz, S. A., Hortobagyi, G. N., Slamon, D. J., Visco, F., Spera, G., Zarate, J. P., . . . Loi, S. (2025). Adjuvant ribociclib plus nonsteroidal aromatase inhibitor therapy in patients with HR-positive/HER2-negative early breast cancer: 5-year follow-up of NATALEE efficacy outcomes and updated overall survival. *ESMO Open*, *10*(11), Article 105858. https://doi.org/10.1016/j.esmoop.2025.105858 — PMID 41320342**

**Design:** Phase 3, international, open-label, randomized 1:1 [A].
**Population:** 5,101 pre/postmenopausal women and men with HR+/HER2− EBC, AJCC 8th anatomic stage IIA (N1, or N0 with grade 3, or grade 2 with Ki-67 ≥20% or high genomic risk), IIB or III [A, FT 4-year].
**Arms:**
- Ribociclib 400 mg once daily, days 1–21 of a 28-day cycle, for 36 months + NSAI (letrozole 2.5 mg or anastrozole 1 mg daily for 60 months).
- vs NSAI alone.
- Premenopausal women and men also received goserelin 3.6 mg every 28 days [A].
- The early-breast dose (400 mg) is lower than the metastatic dose (600 mg) [L-Kisqali].

**Primary endpoint (iDFS)**
| Analysis | Median FU | HR (95% CI) | Rates |
|---|---|---|---|
| NEJM 2024 interim | — | 0.75 (0.62–0.91), P = 0.003 | 3-year 90.4% vs 87.1% |
| Final iDFS (2025) | 33.3 months | 0.749 (0.628–0.892), P = 0.0012 | 3-year 90.7% vs 87.6% |
| 4-year exploratory | 44.2 months | 0.72 (0.61–0.84) | 4-year 88.5% vs 83.6% |
| **5-year prespecified** | **55.4 months** | **0.716 (0.618–0.829)** | **Δ4.5% at 5 years** (absolute 5-year rates not in text: **[UNVERIFIED]**) |

- N0 subgroup (5-year): HR 0.606 (0.372–0.986) [A].
- Distant recurrences 8.1% vs 11.4% [FT 5-year].

**OS (immature, not significant):**
- 4-year: HR 0.83 (0.64–1.07) [A].
- **5-year: HR 0.800 (0.637–1.003), nominal one-sided P = 0.026.** Deaths 5.4% vs 6.7% [A, FT].

**Toxicity (4-year analysis, safety set 2,526 vs 2,441)** [FT]
- Neutropenia 62.8% (grade 3 42.2%, grade 4 2.2%) vs 4.5%.
- ALT increase 19.7% (grade 3 6.4%, grade 4 1.3%); AST increase 17.2% (grade 3 4.0%).
- **QT prolongation 5.4% vs 1.6%**; grade ≥3 1.0% vs 0.7%.
- Arthralgia 38.8% vs 44.4%; nausea 23.5%; fatigue 22.8%; alopecia 15.3%.
- Discontinuation of ribociclib for AEs 20.0%, mainly ALT (7.2%) and AST (2.7%) increases. Dose reduction 27.2%.
- ILD/pneumonitis 1.5% (grade 1–2) [L-Kisqali].

---

## 6. PALLAS (adjuvant palbociclib) — NEGATIVE — [VERIFIED]

**References**
- Mayer, E. L., Dueck, A. C., Martin, M., Rubovszky, G., Burstein, H. J., Bellet-Ezquerra, M., Miller, K. D., Zdenkowski, N., Winer, E. P., Pfeiler, G., Goetz, M., Ruiz-Borrego, M., Anderson, D., Nowecki, Z., Loibl, S., Moulder, S., Ring, A., Fitzal, F., Traina, T., . . . Gnant, M. (2021). Palbociclib with adjuvant endocrine therapy in early breast cancer (PALLAS): Interim analysis of a multicentre, open-label, randomised, phase 3 study. *The Lancet Oncology*, *22*(2), 212–222. https://doi.org/10.1016/S1470-2045(20)30642-2 — PMID 33460574
- Gnant, M., Dueck, A. C., Frantal, S., Martin, M., Burstein, H. J., Greil, R., Fox, P., Wolff, A. C., Chan, A., Winer, E. P., Pfeiler, G., Miller, K. D., Colleoni, M., Suga, J. M., Rubovsky, G., Bliss, J. M., Mayer, I. A., Singer, C. F., Nowecki, Z., . . . Mayer, E. L. (2022). Adjuvant palbociclib for early breast cancer: The PALLAS trial results (ABCSG-42/AFT-05/BIG-14-03). *Journal of Clinical Oncology*, *40*(3), 282–293. https://doi.org/10.1200/JCO.21.02554 — PMID 34874182
- **(5-year, latest) Mayer, E. L., Hlauschek, D., Gnant, M., O'Brien, P. J., Bellet-Ezquerra, M., Goetz, M. P., Ruiz-Borrego, M., Chan, A., Clifton, K., Egle, D., Lake, D., Cabrera, P., Mamounas, T., Pristauz-Telsnigg, G., Dayao, Z., Gil Gil, M., Cameron, D., Traina, T., Morris, P. G., . . . DeMichele, A. (2026). Palbociclib with adjuvant endocrine therapy in early breast cancer: 5-year follow-up analysis of the global multicenter, open-label, randomized phase III PALLAS trial (ABCSG-42/AFT-05/PrE0109/BIG-14-13). *Annals of Oncology*, *37*(2), 271–277. https://doi.org/10.1016/j.annonc.2025.10.003 — PMID 41110701**

**Design:** Phase 3, open-label, randomized 1:1; 406 centres, 21 countries [A].
**Population:** 5,760 randomized (5,761 ITT in the final analysis), stage II–III HR+/HER2− EBC within 12 months of diagnosis [A].
**Arms:** Palbociclib 125 mg once daily, days 1–21 of 28, for 2 years + ET (≥5 years) vs ET alone [A].
**Primary endpoint (iDFS):**
- Interim (median FU 23.7 months): 3-year 88.2% vs 88.5%; HR 0.93 (0.76–1.15), P = 0.51. **Crossed the futility boundary**; IDMC recommended stopping palbociclib [A].
- Final (median FU 31 months): 4-year 84.2% vs 84.5%; HR 0.96 (0.81–1.14), P = .65 [A].
- **5-year (median FU 59.8 months): 84.2% vs 82.4%; HR 0.88 (0.77–1.01), P = 0.0614.** No benefit in any subgroup [A].
**OS (5-year):** 92.6% vs 93.2%; HR 1.09 (0.89–1.33), P = 0.4051 [A].
**Toxicity:** Grade 3–4 neutropenia 61.3% vs 0.3%; leukopenia 30.2%; fatigue 2.1%. SAEs 12.4% vs 7.6%. No treatment-related deaths [A, 2021].

---

## 7. PENELOPE-B (post-neoadjuvant palbociclib) — NEGATIVE — [VERIFIED]

**References**
- Loibl, S., Marmé, F., Martin, M., Untch, M., Bonnefoi, H., Kim, S.-B., Bear, H., McCarthy, N., Melé Olivé, M., Gelmon, K., García-Sáenz, J., Kelly, C. M., Reimer, T., Toi, M., Rugo, H. S., Denkert, C., Gnant, M., Makris, A., Koehler, M., . . . von Minckwitz, G. (2021). Palbociclib for residual high-risk invasive HR-positive and HER2-negative early breast cancer—The Penelope-B trial. *Journal of Clinical Oncology*, *39*(14), 1518–1530. https://doi.org/10.1200/JCO.20.03639 — PMID 33793299
- **(Final OS) Loibl, S., Martin, M., Bonnefoi, H., Untch, M., Kim, S.-B., Bear, H. D., García-Sáenz, J. A., Melé Olivé, M., Mc Carthy, N., Gelmon, K., Kelly, C. M., Im, S.-A., Reimer, T., Martinez-Janez, M., Zhang, Z., Toi, M., Provencher, L., Rugo, H. S., Gnant, M., . . . Marmé, F. (2025). Final survival results from the PENELOPE-B trial investigating palbociclib versus placebo for patients with high-risk HR+/HER2− breast cancer and residual disease after neoadjuvant chemotherapy. *Annals of Oncology*, *36*(7), 832–837. https://doi.org/10.1016/j.annonc.2025.03.010 — PMID 40139460**

**Design:** Phase 3, double-blind, placebo-controlled [A].
**Population:** 1,250 women, HR+/HER2−, no pCR after taxane-containing neoadjuvant chemotherapy, high relapse risk (CPS-EG score ≥3, or 2 with ypN+) [A].
**Arms:** Palbociclib 125 mg once daily, days 1–21 of 28, for 13 cycles (about 1 year) + ET vs placebo + ET [A].
**Primary endpoint (iDFS):** Median FU 42.8 months; stratified HR 0.93 (95% repeated CI 0.74–1.17), P = .525 [A].
**Final OS:** Median FU 77.8 months; 6-year OS 82.4% vs 80.3%; HR 0.87 (0.67–1.14), P = 0.31. Exploratory lobular subgroup: iDFS HR 0.52 (0.28–0.97), OS HR 0.45 (0.19–1.07); post hoc, hypothesis-generating only [A].
**Toxicity:** Related serious AEs (mostly infections and vascular disorders) 9.1%, no difference between arms; 8 fatal SAEs (2 palbociclib, 6 placebo) [A]. Grade 3–4 neutropenia rate: **[UNVERIFIED]** (not in abstract).

**Teaching point:** Among the three adjuvant CDK4/6 inhibitors, only abemaciclib (monarchE) and ribociclib (NATALEE) are positive; palbociclib failed twice (PALLAS, PENELOPE-B).

---

# C. PARP inhibitor

## 8. OlympiA (adjuvant olaparib, germline BRCA1/2) — [VERIFIED]

**References**
- Tutt, A. N. J., Garber, J. E., Kaufman, B., Viale, G., Fumagalli, D., Rastogi, P., Gelber, R. D., de Azambuja, E., Fielding, A., Balmaña, J., Domchek, S. M., Gelmon, K. A., Hollingsworth, S. J., Korde, L. A., Linderholm, B., Bandos, H., Senkus, E., Suga, J. M., Shao, Z., . . . Geyer, C. E., Jr. (2021). Adjuvant olaparib for patients with *BRCA1*- or *BRCA2*-mutated breast cancer. *The New England Journal of Medicine*, *384*(25), 2394–2405. https://doi.org/10.1056/NEJMoa2105215 — PMID 34081848 (PMC9126186)
- (OS, 2nd interim) Geyer, C. E., Jr., Garber, J. E., Gelber, R. D., Yothers, G., Taboada, M., Ross, L., Rastogi, P., Cui, K., Arahmani, A., Aktan, G., Armstrong, A. C., Arnedos, M., Balmaña, J., Bergh, J., Bliss, J., Delaloge, S., Domchek, S. M., Eisen, A., Elsafy, F., . . . Tutt, A. N. J. (2022). Overall survival in the OlympiA phase III trial of adjuvant olaparib in patients with germline pathogenic variants in *BRCA1/2* and high-risk, early breast cancer. *Annals of Oncology*, *33*(12), 1250–1268. https://doi.org/10.1016/j.annonc.2022.09.159 — PMID 36228963
- **(6.1-year, latest) Garber, J. E., Cameron, D., Campbell, C., Yothers, G., Taboada, M., El-Abed, S., Rastogi, P., McConnell, R., Correa, A., Delaloge, S., Liu, W. T., Sharma, P., Bergh, J., Janni, W., Balmaña, J., Loman, N., Španić, T., Friedman, S., Freeman, T., . . . Tutt, A. N. J. (2026). Sustained benefit of adjuvant olaparib in women with germline *BRCA1*- and *BRCA2*-associated high-risk HER2-negative early breast cancer: Updated results from the OlympiA phase III trial. *Annals of Oncology*. Advance online publication. https://doi.org/10.1016/j.annonc.2026.08.002 — PMID 42636977**

**Design:** Phase 3, double-blind, placebo-controlled, randomized 1:1 [A].
**Population:** 1,836 patients with germline BRCA1/2 pathogenic or likely pathogenic variants and high-risk HER2-negative EBC, after local therapy and ≥6 cycles of (neo)adjuvant anthracycline and/or taxane chemotherapy (platinum allowed) [A, FT].
- TNBC, adjuvant chemotherapy: node-positive or invasive tumour ≥2 cm.
- TNBC, neoadjuvant chemotherapy: no pCR.
- HR-positive, adjuvant: ≥4 positive nodes.
- HR-positive, neoadjuvant: no pCR and CPS+EG score ≥3 [FT].
- Endocrine therapy given concurrently for HR-positive disease [A, 2022].

**Arms:** Olaparib 300 mg orally twice daily vs placebo for 52 weeks [FT].

**Results**
| Analysis | Median FU | IDFS | DDFS | OS |
|---|---|---|---|---|
| 1st interim (NEJM 2021) | 2.5 y | 3-year 85.9% vs 77.1%; HR 0.58 (99.5% CI 0.41–0.82), P < 0.001 | 3-year 87.5% vs 80.4%; HR 0.57 (99.5% CI 0.39–0.83) | 59 vs 86 deaths; HR 0.68 (99% CI 0.44–1.05), not significant at that interim |
| 2nd interim (2022) | 3.5 y | 4-year 82.7% vs 75.4% | 4-year 86.5% vs 79.1% | **HR 0.68 (98.5% CI 0.47–0.97), P = 0.009**; 4-year 89.8% vs 86.4% |
| **3rd interim (2026)** | **6.1 y** | **HR 0.65 (0.53–0.78)** | **HR 0.65 (0.53–0.81)** | **HR 0.72 (0.56–0.93); 6-year 87.5% vs 83.2%** |

**Toxicity** [FT 2021 unless noted]
- Grade ≥3 AEs >1%: **anaemia 8.7%**, decreased neutrophils 4.8%, decreased WBC 3.0%, fatigue 1.8%, lymphopenia 1.2%.
- Nausea all grades 56.9% vs 23.3%.
- Transfusion 5.8% vs 0.9%. Dose reduction 25.0%. Discontinuation for AEs 9.9% vs 4.2%.
- **MDS/AML 0.4% vs 0.7%; AESI 6.3% vs 9.3%** at 6.1 years [A 2026].

---

# D. Genomic assays (21-gene Recurrence Score)

## 9. TAILORx (node-negative) — [VERIFIED]

**Reference**
- Sparano, J. A., Gray, R. J., Makower, D. F., Pritchard, K. I., Albain, K. S., Hayes, D. F., Geyer, C. E., Jr., Dees, E. C., Goetz, M. P., Olson, J. A., Jr., Lively, T., Badve, S. S., Saphner, T. J., Wagner, L. I., Whelan, T. J., Ellis, M. J., Paik, S., Wood, W. C., Ravdin, P. M., . . . Sledge, G. W., Jr. (2018). Adjuvant chemotherapy guided by a 21-gene expression assay in breast cancer. *The New England Journal of Medicine*, *379*(2), 111–121. https://doi.org/10.1056/NEJMoa1804710 — PMID 29860917 (PMC6172658)

**Design:** Prospective trial with randomized non-inferiority comparison in the mid-range RS group [A].
**Population:** 10,273 women aged 18–75 with HR+/HER2−, axillary node-negative EBC; 9,719 eligible with follow-up [A, FT].
**Assignment:**
- RS ≤10: endocrine therapy alone (17%).
- RS 11–25: **randomized** to ET vs chemo + ET (n = 6,711; 69%).
- RS ≥26: chemo + ET (14%) [FT].
- Chemotherapy used: docetaxel–cyclophosphamide 56%, anthracycline-containing 36% [FT].

**Primary endpoint (iDFS, RS 11–25):** ET non-inferior to chemo + ET; HR 1.08 (0.94–1.24), P = 0.26. 9-year iDFS 83.3% vs 84.3%; distant recurrence-free 94.5% vs 95.0%; OS 93.9% vs 93.8% [A].

**Other cohorts (9-year)** [FT, Table 2]
| Group | iDFS | Freedom from distant recurrence | OS |
|---|---|---|---|
| RS ≤10, ET | 84.0% | 96.8% | 93.7% |
| RS ≥26, chemo + ET | 75.7% | 86.8% | 89.3% |

**Age ≤50 (exploratory):** Chemotherapy lowered distant recurrence by 1.6 points at 9 years for RS 16–20 and 6.5 points for RS 21–25, with similar OS. For RS 0–15 in this age group, 9-year distant recurrence was about 2% on ET alone [FT].
**Take-home:** About 85% of node-negative patients can skip chemotherapy (age >50 with RS ≤25, or age ≤50 with RS ≤15) [FT, discussion].
**Toxicity:** Not an endpoint of this report.

---

## 10. RxPONDER (SWOG S1007, 1–3 positive nodes) — [VERIFIED]

**Reference**
- Kalinsky, K., Barlow, W. E., Gralow, J. R., Meric-Bernstam, F., Albain, K. S., Hayes, D. F., Lin, N. U., Perez, E. A., Goldstein, L. J., Chia, S. K. L., Dhesy-Thind, S., Rastogi, P., Alba, E., Delaloge, S., Martin, M., Kelly, C. M., Ruiz-Borrego, M., Gil-Gil, M., Arce-Salinas, C. H., . . . Hortobagyi, G. N. (2021). 21-gene assay to inform chemotherapy benefit in node-positive breast cancer. *The New England Journal of Medicine*, *385*(25), 2336–2347. https://doi.org/10.1056/NEJMoa2108873 — PMID 34914339 (PMC9096864)

**Design:** Phase 3, randomized [A].
**Population:** 5,083 women (33.2% premenopausal) with HR+/HER2−, 1–3 positive nodes, RS ≤25 [A].
**Arms:** ET alone vs chemo + ET. Preferred chemotherapy: anthracycline + taxane in premenopausal women (54%); taxane + cyclophosphamide in postmenopausal women (57%). Ovarian suppression was used in only 12.7% of premenopausal women within 12 months [FT].
**Primary endpoint (iDFS), prespecified third interim, median FU 5.3 years** [A, FT]
| Group | 5-year iDFS (ET vs chemo + ET) | HR (95% CI) |
|---|---|---|
| Postmenopausal | 91.9% vs 91.3% | 1.02 (0.82–1.26), P = 0.89 |
| Premenopausal | 89.0% vs 93.9% | **0.60 (0.43–0.83), P = 0.002** |
| Premenopausal, DRFS | Δ3.3 points at 5 years | 0.58 (0.39–0.87), P = 0.009 |

- Interaction with menopausal status: P = 0.008 [A].
- The relative chemotherapy benefit did not rise with RS within 0–25 [A].
- Premenopausal age ≥50: HR 0.98; age <50: HR 0.48 (0.32–0.72) [FT].
- OS: "not mature" in the 2021 paper [FT]. **No later primary update found on PubMed.**
**Caveat for teaching:** It is unclear whether the premenopausal benefit is cytotoxic or due to chemotherapy-induced menopause, because OFS was underused [FT, discussion; also noted in the SOFT/TEXT final paper].

---

# E. HER2-positive disease

## 11. APHINITY (adjuvant pertuzumab) — [VERIFIED]

**References**
- von Minckwitz, G., Procter, M., de Azambuja, E., Zardavas, D., Benyunes, M., Viale, G., Suter, T., Arahmani, A., Rouchet, N., Clark, E., Knott, A., Lang, I., Levy, C., Yardley, D. A., Bines, J., Gelber, R. D., Piccart, M., & Baselga, J. (2017). Adjuvant pertuzumab and trastuzumab in early HER2-positive breast cancer. *The New England Journal of Medicine*, *377*(2), 122–131. https://doi.org/10.1056/NEJMoa1703643 — PMID 28581356 (PMC5538020). **Errata:** PMID 28700263 and 30338958 (not reviewed).
- Piccart, M., Procter, M., Fumagalli, D., de Azambuja, E., Clark, E., Ewer, M. S., Restuccia, E., Jerusalem, G., Dent, S., Reaby, L., Bonnefoi, H., Krop, I., Liu, T.-W., Pieńkowski, T., Toi, M., Wilcken, N., Andersson, M., Im, Y.-H., Tseng, L. M., . . . Thomssen, C. (2021). Adjuvant pertuzumab and trastuzumab in early HER2-positive breast cancer in the APHINITY trial: 6 years' follow-up. *Journal of Clinical Oncology*, *39*(13), 1448–1457. https://doi.org/10.1200/JCO.20.01204 — PMID 33539215
- **(Latest OS) Loibl, S., Jassem, J., Sonnenblick, A., Parlier, D., Winer, E., Bergh, J., Gelber, R. D., Restuccia, E., Im, Y.-H., Huang, C.-S., Dalenc, F., Calvo, I., Procter, M., Caballero, C., Clark, E., Raimbault, A., McConnell, R., Monturus, E., de Azambuja, E., . . . Piccart, M. (2024). Adjuvant pertuzumab and trastuzumab in early human epidermal growth factor receptor 2-positive breast cancer in the APHINITY trial: Third interim overall survival analysis with efficacy update. *Journal of Clinical Oncology*, *42*(31), 3643–3651. https://doi.org/10.1200/JCO.23.02505 — PMID 39259927**

**Design:** Phase 3, double-blind, placebo-controlled, randomized 1:1 [A].
**Population:** 4,805 patients (4,804 ITT in 2024) with operable HER2-positive EBC, node-positive or high-risk node-negative; 63% node-positive, 36% HR-negative [A].
**Arms** [FT, L-Perjeta]:
- Pertuzumab 840 mg IV loading, then 420 mg IV q3w, or placebo.
- Plus trastuzumab 8 mg/kg loading, then 6 mg/kg q3w.
- Both started with the first taxane cycle; maximum 18 cycles within 1 year.
- Chemotherapy: anthracycline-based (FEC/FAC or AC/EC, q3w or q2w with G-CSF, then docetaxel or weekly paclitaxel 80 mg/m² ×12) or non-anthracycline (docetaxel–carboplatin).

**Primary endpoint (iDFS)**
| Analysis | Median FU | ITT HR (95% CI) | Rates | Node-positive |
|---|---|---|---|---|
| 2017 primary | 45 months | 0.81 (0.66–1.00), P = 0.045 | 3-year 94.1% vs 93.2% | HR 0.77 (0.62–0.96); 3-year 92.0% vs 90.2% |
| 2021 | 74 months | 0.76 (0.64–0.91) | 6-year 91% vs 88% | HR 0.72 (0.59–0.87); 88% vs 83% |
| 2024 | 8.4 years | — | — | **8-year 86.1% vs 81.2%; HR 0.72 (0.60–0.87)** |

- Node-negative: no benefit. 2017 HR 1.13 (0.68–1.86); 8-year placebo iDFS 93.3%, OS 96.4% [A].
- HR subsets (2024): HR-negative 0.82 (0.64–1.06); HR-positive 0.75 (0.61–0.92) [A].

**OS (not significant):**
- 2021: HR 0.85, P = .17 (threshold .0012); 6-year 95% vs 94% [A].
- **2024: 8-year 92.7% vs 92.0%; HR 0.83 (0.68–1.02), P = .078 (threshold 0.006).** Node-positive HR 0.80 (0.63–1.00); node-negative HR 0.99 (0.64–1.55) [A].

**Toxicity**
- **Grade ≥3 diarrhoea 9.8% vs 3.7%**, almost all during chemotherapy [A].
- Primary cardiac events 0.7% vs 0.3% (0.8% with anthracycline vs 0.4% without, in the pertuzumab arm) [FT]. Primary cardiac events remained <1% at 6 years [A 2021].

---

## 12. KATHERINE (T-DM1 for residual disease) — [VERIFIED]

**References**
- von Minckwitz, G., Huang, C.-S., Mano, M. S., Loibl, S., Mamounas, E. P., Untch, M., Wolmark, N., Rastogi, P., Schneeweiss, A., Redondo, A., Fischer, H. H., Jacot, W., Conlin, A. K., Arce-Salinas, C., Wapnir, I. L., Jackisch, C., DiGiovanna, M. P., Fasching, P. A., Crown, J. P., . . . Geyer, C. E., Jr. (2019). Trastuzumab emtansine for residual invasive HER2-positive breast cancer. *The New England Journal of Medicine*, *380*(7), 617–628. https://doi.org/10.1056/NEJMoa1814017 — PMID 30516102
- **(OS 2025) Geyer, C. E., Jr., Untch, M., Huang, C.-S., Mano, M. S., Mamounas, E. P., Wolmark, N., Rastogi, P., Schneeweiss, A., Redondo, A., Fischer, H. H., D'Hondt, V., Conlin, A. K., Guarneri, V., Wapnir, I. L., Jackisch, C., Arce-Salinas, C., Fasching, P. A., DiGiovanna, M. P., Crown, J. P., . . . Loibl, S. (2025). Survival with trastuzumab emtansine in residual HER2-positive breast cancer. *The New England Journal of Medicine*, *392*(3), 249–257. https://doi.org/10.1056/NEJMoa2406070 — PMID 39813643**

**Design:** Phase 3, open-label, randomized 1:1 [A].
**Population:** 1,486 patients with HER2-positive EBC and residual invasive disease in breast or axilla after neoadjuvant taxane (± anthracycline) + trastuzumab [A].
**Arms:** T-DM1 3.6 mg/kg IV q3w vs trastuzumab 6 mg/kg IV q3w, both for 14 cycles. Radiotherapy and endocrine therapy given concurrently per local guidelines [L-Kadcyla].

**Primary endpoint (iDFS)**
- 2019 interim: events 12.2% vs 22.2%; **3-year iDFS 88.3% vs 77.0%; HR 0.50 (0.39–0.64), P < 0.001.** Distant recurrence as first event 10.5% vs 15.9% [A].
- **2025 final iDFS (median FU 8.4 years): HR 0.54 (0.44–0.66); 7-year 80.8% vs 67.1% (Δ13.7)** [A].

**OS (2nd interim, 2025):** **HR 0.66 (0.51–0.87), P = 0.003 (unstratified); 7-year OS 89.1% vs 84.4% (Δ4.7)** [A].

**Toxicity**
- Grade ≥3 AEs 26.1% vs 15.7% [A 2025]. Discontinuation of T-DM1 for AEs 18% [L-Kadcyla].
- **Thrombocytopenia 29% vs 2.4%; grade ≥3 6% vs 0.3%; in Asian patients grade ≥3 19% vs 0%** (relevant for Taiwan) [L-Kadcyla].
- **Peripheral neuropathy 32% vs 17%** (grade ≥3 1.6%); 30% unresolved at the primary analysis [L-Kadcyla].
- AST increase 79% (lab); haemorrhage 29% vs 10% (grade ≥3 0.4%, one fatal intracranial haemorrhage) [L-Kadcyla].
- Pneumonitis 1.1%; radiation pneumonitis 1.8% of irradiated patients; LV dysfunction 0.4% vs 0.6%; nodular regenerative hyperplasia 2 cases [L-Kadcyla].

---

## 13. ExteNET (extended adjuvant neratinib) — [VERIFIED]

**References**
- Chan, A., Delaloge, S., Holmes, F. A., Moy, B., Iwata, H., Harvey, V. J., Robert, N. J., Silovski, T., Gokmen, E., von Minckwitz, G., Ejlertsen, B., Chia, S. K. L., Mansi, J., Barrios, C. H., Gnant, M., Buyse, M., Gore, I., Smith, J., II, Harker, G., . . . Martin, M. (2016). Neratinib after trastuzumab-based adjuvant therapy in patients with HER2-positive breast cancer (ExteNET): A multicentre, randomised, double-blind, placebo-controlled, phase 3 trial. *The Lancet Oncology*, *17*(3), 367–377. https://doi.org/10.1016/S1470-2045(15)00551-3 — PMID 26874901
- Martin, M., Holmes, F. A., Ejlertsen, B., Delaloge, S., Moy, B., Iwata, H., von Minckwitz, G., Chia, S. K. L., Mansi, J., Barrios, C. H., Gnant, M., Tomašević, Z., Denduluri, N., Šeparović, R., Gokmen, E., Bashford, A., Ruiz Borrego, M., Kim, S.-B., Jakobsen, E. H., . . . Chan, A. (2017). Neratinib after trastuzumab-based adjuvant therapy in HER2-positive breast cancer (ExteNET): 5-year analysis of a randomised, double-blind, placebo-controlled, phase 3 trial. *The Lancet Oncology*, *18*(12), 1688–1700. https://doi.org/10.1016/S1470-2045(17)30717-9 — PMID 29146401
- Chan, A., Moy, B., Mansi, J., Ejlertsen, B., Holmes, F. A., Chia, S., Iwata, H., Gnant, M., Loibl, S., Barrios, C. H., Somali, I., Smichkoska, S., Martinez, N., Alonso, M. G., Link, J. S., Mayer, I. A., Cold, S., Murillo, S. M., Senecal, F., . . . Martin, M. (2021). Final efficacy results of neratinib in HER2-positive hormone receptor-positive early-stage breast cancer from the phase III ExteNET trial. *Clinical Breast Cancer*, *21*(1), 80–91.e7. https://doi.org/10.1016/j.clbc.2020.09.014 — PMID 33183970
- **(Final OS) Holmes, F. A., Moy, B., Delaloge, S., Chia, S. K. L., Ejlertsen, B., Mansi, J., Iwata, H., Gnant, M., Buyse, M., Barrios, C. H., Silovski, T., Šeparović, R., Bashford, A., Zotano, A. G., Denduluri, N., Patt, D., Gokmen, E., Gore, I., Smith, J. W., II, . . . Chan, A. (2023). Overall survival with neratinib after trastuzumab-based adjuvant therapy in HER2-positive breast cancer (ExteNET): A randomised, double-blind, placebo-controlled, phase 3 trial. *European Journal of Cancer*, *184*, 48–59. https://doi.org/10.1016/j.ejca.2023.02.002 — PMID 36898233**

**Design:** Phase 3, double-blind, placebo-controlled; 495 centres [A].
**Population:** 2,840 women with stage 1–3 HER2-positive EBC (amended in 2010 to stage 2–3 and ≤1 year from completing trastuzumab) [A].
**Arms:** Neratinib 240 mg orally once daily vs placebo for 1 year. No diarrhoea prophylaxis was used in the trial [A].
**Primary endpoint (iDFS):**
- 2-year: 93.9% vs 91.6%; HR 0.67 (0.50–0.91), P = 0.0091 [A].
- 5-year: 90.2% vs 87.7%; HR 0.73 (0.57–0.92), P = 0.0083 [A].
- HR+/≤1 year from trastuzumab (exploratory, n = 1,334): 5-year Δ5.1%, HR 0.58 (0.41–0.82). Residual disease after neoadjuvant therapy (n = 295): 8-year OS Δ9.1%, HR 0.47 (0.23–0.92) [A, Chan 2021].
**Final OS (median FU 8.1 years):** **8-year 90.1% vs 90.2%; HR 0.95 (0.75–1.21), P = 0.6914** [A].
**Toxicity:**
- **Grade 3 diarrhoea 40%** (grade 4 <1%) vs 2% without prophylaxis. Vomiting grade 3 3%; nausea grade 3 2% [A].
- 93% had diarrhoea in month 1; median onset of grade ≥3 diarrhoea day 8 [L-Nerlynx].
- No long-term toxicity excess [A 2017].
- **Label now mandates loperamide prophylaxis for the first 56 days:** 4 mg three times daily for weeks 1–2, 4 mg twice daily for weeks 3–8, then as needed (≤16 mg/day). A 2-week dose escalation start is an alternative [L-Nerlynx].

---

## 14. NeoSphere (neoadjuvant pertuzumab) — [VERIFIED]

**References**
- Gianni, L., Pienkowski, T., Im, Y.-H., Roman, L., Tseng, L.-M., Liu, M.-C., Lluch, A., Staroslawska, E., de la Haba-Rodriguez, J., Im, S.-A., Pedrini, J. L., Poirier, B., Morandi, P., Semiglazov, V., Srimuninnimit, V., Bianchi, G., Szado, T., Ratnayake, J., Ross, G., & Valagussa, P. (2012). Efficacy and safety of neoadjuvant pertuzumab and trastuzumab in women with locally advanced, inflammatory, or early HER2-positive breast cancer (NeoSphere): A randomised multicentre, open-label, phase 2 trial. *The Lancet Oncology*, *13*(1), 25–32. https://doi.org/10.1016/S1470-2045(11)70336-9 — PMID 22153890
- Gianni, L., Pienkowski, T., Im, Y.-H., Tseng, L.-M., Liu, M.-C., Lluch, A., Starosławska, E., de la Haba-Rodriguez, J., Im, S.-A., Pedrini, J. L., Poirier, B., Morandi, P., Semiglazov, V., Srimuninnimit, V., Bianchi, G. V., Magazzù, D., McNally, V., Douthwaite, H., Ross, G., & Valagussa, P. (2016). 5-year analysis of neoadjuvant pertuzumab and trastuzumab in patients with locally advanced, inflammatory, or early-stage HER2-positive breast cancer (NeoSphere): A multicentre, open-label, phase 2 randomised trial. *The Lancet Oncology*, *17*(6), 791–800. https://doi.org/10.1016/S1470-2045(16)00163-7 — PMID 27179402

**Design:** **Phase 2**, open-label, randomized 1:1:1:1 (PubMed tags the 2016 paper "Phase III"; the title and abstract say phase 2) [A].
**Population:** 417 treatment-naive women with operable, locally advanced or inflammatory HER2-positive breast cancer [A].
**Arms (4 neoadjuvant cycles q3w)** [A]
- A: trastuzumab (8 mg/kg loading, then 6 mg/kg) + docetaxel (75 mg/m², escalating to 100 mg/m² if tolerated).
- B: pertuzumab (840 mg loading, then 420 mg) + trastuzumab + docetaxel.
- C: pertuzumab + trastuzumab (no chemotherapy).
- D: pertuzumab + docetaxel.
- After surgery: FEC ×3 (5-FU 600, epirubicin 90, cyclophosphamide 600 mg/m²) and trastuzumab to complete 1 year (arm C got docetaxel ×4 before FEC) [A 2016].

**Primary endpoint: breast pCR (ypT0/is)** [A]
| Arm | pCR |
|---|---|
| A (TH) | 29.0% (20.6–38.5) |
| **B (THP)** | **45.8% (36.1–55.7)**, P = 0.0141 vs A |
| C (HP) | 16.8% (10.3–25.3) |
| D (TP) | 24.0% (15.8–33.7) |

**5-year (descriptive)** [A 2016]
- PFS: A 81%, B 86%, C 73%, D 73%; HR B vs A 0.69 (0.34–1.40), not powered.
- tpCR (all arms) vs no tpCR: PFS 85% vs 76%, HR 0.54 (0.29–1.00).

**Toxicity:** Grade ≥3 neutropenia (whole treatment period) A 66%, B 55%, C 37%, D 64%; febrile neutropenia 9%, 11%, 5%, 16% [A 2016].

---

## 15. TRYPHAENA (neoadjuvant pertuzumab, cardiac safety) — [VERIFIED]

**References**
- Schneeweiss, A., Chia, S., Hickish, T., Harvey, V., Eniu, A., Hegg, R., Tausch, C., Seo, J. H., Tsai, Y.-F., Ratnayake, J., McNally, V., Ross, G., & Cortés, J. (2013). Pertuzumab plus trastuzumab in combination with standard neoadjuvant anthracycline-containing and anthracycline-free chemotherapy regimens in patients with HER2-positive early breast cancer: A randomized phase II cardiac safety study (TRYPHAENA). *Annals of Oncology*, *24*(9), 2278–2284. https://doi.org/10.1093/annonc/mdt182 — PMID 23704196
- Schneeweiss, A., Chia, S., Hickish, T., Harvey, V., Eniu, A., Waldron-Lynch, M., Eng-Wong, J., Kirk, S., & Cortés, J. (2018). Long-term efficacy analysis of the randomised, phase II TRYPHAENA cardiac safety study: Evaluating pertuzumab and trastuzumab plus standard neoadjuvant anthracycline-containing and anthracycline-free chemotherapy regimens in patients with HER2-positive early breast cancer. *European Journal of Cancer*, *89*, 27–35. https://doi.org/10.1016/j.ejca.2017.10.021 — PMID 29223479

**Design:** Phase 2, open-label, randomized 1:1:1; primary endpoint cardiac safety [A].
**Population:** 225 patients with operable, locally advanced or inflammatory HER2-positive breast cancer [A].
**Arms (6 neoadjuvant cycles q3w)** [A 2013, 2018]
- A: FEC (5-FU 500, epirubicin 100, cyclophosphamide 600 mg/m²) + H + P ×3 → docetaxel (75→100 mg/m²) + H + P ×3.
- B: FEC ×3 → docetaxel + H + P ×3.
- C: docetaxel 75 mg/m² + carboplatin AUC 6 + H + P ×6 (TCHP).
- H = trastuzumab 8 → 6 mg/kg; P = pertuzumab 840 → 420 mg.

**Cardiac safety (neoadjuvant phase)** [A 2013]
- Symptomatic LVSD: 2 patients (2.7%, arm B).
- LVEF decline ≥10 points to <50%: A 5.6%, B 5.3%, C 3.9%.
**pCR (ypT0/is, breast):** A 61.6%, B 57.3%, C 66.2% [A 2013].
**Long-term:** 3-year DFS 87%, 88%, 90%. DFS HR for tpCR vs no tpCR 0.27 (0.11–0.64). Post-treatment LVEF decline ≥10 points to <50%: 11.1%, 16.0%, 11.8% [A 2018].
**Other toxicity:** Diarrhoea was the most common AE [A 2013]; rates **[UNVERIFIED]**.

---

## 16. DESTINY-Breast05 (post-neoadjuvant T-DXd vs T-DM1) — [VERIFIED]

**Reference**
- Loibl, S., Park, Y. H., Shao, Z., Huang, C.-S., Barrios, C., Abraham, J., Prat, A., Niikura, N., Im, S.-A., Li, W., Li, H., Wang, Y., Yao, H., Kim, S.-B., Geng, C.-Z., Rodriguez Pantigoso, W., Ramírez Godinez, F. J., Song, C., Ching Chang, Y., . . . Geyer, C. E., Jr. (2026). Trastuzumab deruxtecan in residual HER2-positive early breast cancer. *The New England Journal of Medicine*, *394*(9), 845–857. https://doi.org/10.1056/NEJMoa2514661 — PMID 41370739. **Erratum:** PMID 41931063 (not reviewed).

**Design:** Phase 3, open-label, randomized 1:1, international [A].
**Population:** 1,635 patients with HER2-positive EBC, residual invasive disease after neoadjuvant therapy, **and high risk**: node-positive at surgery (ypN+) or inoperable at diagnosis [A].
- Per the label: 48% Asian; 71% HR-positive; 52% inoperable at presentation; 81% ypN1–3; 79% had dual HER2 blockade before surgery [L-Enhertu].
- Excluded: prior ILD/pneumonitis requiring steroids [L-Enhertu].
**Arms:** T-DXd 5.4 mg/kg IV q3w vs T-DM1 3.6 mg/kg IV q3w, maximum 14 cycles. Radiotherapy concurrent or sequential [A, L-Enhertu].

**Primary endpoint (iDFS), interim, median FU about 30 months** [A, L-Enhertu]
- Events 6.2% vs 12.5%; **HR 0.47 (0.34–0.66), P < 0.001**.
- **3-year iDFS 92.4% (89.7–94.4) vs 83.7% (80.2–86.7).**
- DFS HR 0.47 (0.34–0.66); 3-year 92.3% vs 83.5%.
**OS:** Not reported in the abstract or the label: **[UNVERIFIED] / immature**.

**Toxicity**
- T-DXd: nausea 71.3%, constipation 32.0%, neutrophil decrease 31.6%, vomiting 31.0%.
- T-DM1: AST increase 50.2%, ALT increase 45.3%, platelet decrease 49.8% [A].
- **Adjudicated drug-related ILD 9.6% vs 1.6%; 2 ILD deaths with T-DXd** [A]. Label: ILD 10% (grade 3–4 0.9%) vs 1.6% [L-Enhertu].
- **Radiation pneumonitis 31% in both arms** among irradiated patients (all grade 1–2); higher with sequential than concurrent RT [L-Enhertu].
- Serious ARs 17%; discontinuation 18%; dose reduction 26% [L-Enhertu].
- All patients had baseline chest CT; patients receiving RT had regular chest CT during and after treatment [L-Enhertu].

**Regulatory:**
- US: adjuvant indication on the current label (effective 2026-05-15) [L-Enhertu].
- **Taiwan: not on the TFDA licence (file dated 2026-10-27)** [TFDA].

---

## 17. DESTINY-Breast11 (neoadjuvant T-DXd → THP) — [VERIFIED]

**Reference**
- Harbeck, N., Modi, S., Pusztai, L., Ohno, S., Wu, J., Kim, S.-B., Yoshida, A., Fabi, A., Cao, X., Joseph, R., Li, R., Żurawski, B., Escrivá-de-Romaní, S., Meneguetti, R., Supavavej, A., Chen, S.-C., Liu, Z., Kelly, C., Curigliano, G., . . . Boileau, J.-F. (2026). Neoadjuvant trastuzumab deruxtecan alone or followed by paclitaxel, trastuzumab, and pertuzumab for high-risk HER2-positive early breast cancer (DESTINY-Breast11): A randomised, open-label, multicentre, phase III trial. *Annals of Oncology*, *37*(2), 166–179. https://doi.org/10.1016/j.annonc.2025.10.019 — PMID 41130363

**Design:** Phase 3, open-label, randomized 1:1:1; 147 sites, 18 countries [A].
**Population:** 927 patients with high-risk HER2-positive EBC (≥cT3 N0, or cT0–4 N1–3, or inflammatory) [A, L-Enhertu].
**Arms (8 neoadjuvant cycles)** [A, L-Enhertu]
- T-DXd 5.4 mg/kg q3w ×8. **Enrolment closed early on IDMC advice.**
- T-DXd 5.4 mg/kg q3w ×4 → THP ×4.
- ddAC (doxorubicin 60 + cyclophosphamide 600 mg/m² q2w) ×4 → THP ×4.
- THP = paclitaxel 80 mg/m² weekly + trastuzumab (8 → 6 mg/kg q3w) + pertuzumab (840 → 420 mg q3w).

**Primary endpoint: pCR (ypT0/is ypN0)** [A, L-Enhertu]
| Arm | pCR |
|---|---|
| T-DXd ×8 (n = 123 evaluable at closure) | 43.0% |
| **T-DXd → THP** | **67.3% (61.9–72.4)** |
| ddAC → THP | 56.3% (50.6–61.8) |

- Difference 11.2% (95% CI 4.0–18.3), P = 0.003 (label CI 3.9–18.3).
- HR-positive: 61.4% vs 52.3% (Δ9.1, 0.2–17.9). HR-negative: 83.1% vs 67.1% (Δ16.1, 3.0–28.8).
- EFS immature (4.5% maturity): HR 0.56 (0.26–1.17) [A].

**Toxicity (T-DXd → THP vs ddAC → THP)** [A]
- Grade ≥3 AEs 37.5% vs 55.8%; SAEs 10.6% vs 20.2%.
- LV dysfunction 1.3% vs 6.1%.
- Adjudicated ILD 4.4% vs 5.1% (T-DXd alone 4.9%). One fatal ILD with T-DXd → THP (0.3%) [L-Enhertu].
- Treatment-related deaths: 1 (T-DXd → THP) vs 2 (ddAC → THP) [A].
- Neutrophil decrease 58%, grade 3–4 17%; febrile neutropenia 0.9% [L-Enhertu].

**Regulatory:**
- US label (2026-05-15): neoadjuvant indication, stage II–III [L-Enhertu].
- **Taiwan: TFDA licence 衛部菌疫輸字第001179號 lists the neoadjuvant T-DXd → THP indication for stage II–III HER2-positive breast cancer** [TFDA].

---

## 18. APT (adjuvant paclitaxel–trastuzumab for small node-negative tumours) — [VERIFIED]

**References**
- Tolaney, S. M., Barry, W. T., Dang, C. T., Yardley, D. A., Moy, B., Marcom, P. K., Albain, K. S., Rugo, H. S., Ellis, M., Shapira, I., Wolff, A. C., Carey, L. A., Overmoyer, B. A., Partridge, A. H., Guo, H., Hudis, C. A., Krop, I. E., Burstein, H. J., & Winer, E. P. (2015). Adjuvant paclitaxel and trastuzumab for node-negative, HER2-positive breast cancer. *The New England Journal of Medicine*, *372*(2), 134–141. https://doi.org/10.1056/NEJMoa1406281 — PMID 25564897. **Erratum:** PMID 26559595.
- Tolaney, S. M., Guo, H., Pernas, S., Barry, W. T., Dillon, D. A., Ritterhouse, L., Schneider, B. P., Shen, F., Fuhrman, K., Baltay, M., Dang, C. T., Yardley, D. A., Moy, B., Marcom, P. K., Albain, K. S., Rugo, H. S., Ellis, M. J., Shapira, I., Wolff, A. C., . . . Winer, E. P. (2019). Seven-year follow-up analysis of adjuvant paclitaxel and trastuzumab trial for node-negative, human epidermal growth factor receptor 2-positive breast cancer. *Journal of Clinical Oncology*, *37*(22), 1868–1875. https://doi.org/10.1200/JCO.19.00066 — PMID 30939096
- **(Final 10-year) Tolaney, S. M., Tarantino, P., Graham, N., Tayob, N., Parè, L., Villacampa, G., Dang, C. T., Yardley, D. A., Moy, B., Marcom, P. K., Albain, K. S., Rugo, H. S., Ellis, M. J., Shapira, I., Wolff, A. C., Carey, L. A., Barroso-Sousa, R., Villagrasa, P., DeMeo, M., . . . Winer, E. P. (2023). Adjuvant paclitaxel and trastuzumab for node-negative, HER2-positive breast cancer: Final 10-year analysis of the open-label, single-arm, phase 2 APT trial. *The Lancet Oncology*, *24*(3), 273–285. https://doi.org/10.1016/S1470-2045(23)00051-7 — PMID 36858723**

**Design:** **Single-arm** phase 2, 16 US institutions; no control arm [A].
**Population:** 410 enrolled, 406 treated; HER2-positive, node-negative, tumour ≤3 cm; 67% HR-positive [A].
**Regimen:** Paclitaxel 80 mg/m² IV weekly + trastuzumab (4 mg/kg loading, then 2 mg/kg) weekly ×12 weeks, then trastuzumab (2 mg/kg weekly or 6 mg/kg q3w) for 40 weeks to complete 1 year [A 2023].
**Primary endpoint (3-year iDFS):** 98.7% (97.6–99.8) [A 2015].
**Updates:**
- 7-year: DFS 93%; OS 95%; RFI 97.5%; distant recurrence 1.0% [A 2019].
- **10-year (median FU 10.8 years): iDFS 91.3% (88.3–94.4); RFI 96.3%; OS 94.3%; breast cancer-specific survival 98.8%.** Of 31 iDFS events: 6 distant recurrences, 9 contralateral cancers, 10 deaths [A 2023].
**Toxicity:** Grade 3 neuropathy 3.2%; symptomatic CHF 0.5% (2 patients; both recovered LVEF); significant asymptomatic LVEF decline 3.2%. 6% withdrew for protocol-specified AEs [A 2015].

---

# F. Triple-negative disease and chemotherapy backbone

## 19. KEYNOTE-522 (neoadjuvant + adjuvant pembrolizumab) — [VERIFIED]

**References**
- Schmid, P., Cortes, J., Pusztai, L., McArthur, H., Kümmel, S., Bergh, J., Denkert, C., Park, Y. H., Hui, R., Harbeck, N., Takahashi, M., Foukakis, T., Fasching, P. A., Cardoso, F., Untch, M., Jia, L., Karantza, V., Zhao, J., Aktan, G., . . . O'Shaughnessy, J. (2020). Pembrolizumab for early triple-negative breast cancer. *The New England Journal of Medicine*, *382*(9), 810–821. https://doi.org/10.1056/NEJMoa1910549 — PMID 32101663
- Schmid, P., Cortes, J., Dent, R., Pusztai, L., McArthur, H., Kümmel, S., Bergh, J., Denkert, C., Park, Y. H., Hui, R., Harbeck, N., Takahashi, M., Untch, M., Fasching, P. A., Cardoso, F., Andersen, J., Patt, D., Danso, M., Ferreira, M., . . . O'Shaughnessy, J. (2022). Event-free survival with pembrolizumab in early triple-negative breast cancer. *The New England Journal of Medicine*, *386*(6), 556–567. https://doi.org/10.1056/NEJMoa2112651 — PMID 35139274
- **(OS) Schmid, P., Cortes, J., Dent, R., McArthur, H., Pusztai, L., Kümmel, S., Denkert, C., Park, Y. H., Hui, R., Harbeck, N., Takahashi, M., Im, S.-A., Untch, M., Fasching, P. A., Mouret-Reynier, M.-A., Foukakis, T., Ferreira, M., Cardoso, F., Zhou, X., . . . O'Shaughnessy, J. (2024). Overall survival with pembrolizumab in early-stage triple-negative breast cancer. *The New England Journal of Medicine*, *391*(21), 1981–1991. https://doi.org/10.1056/NEJMoa2409932 — PMID 39282906**

**Design:** Phase 3, double-blind, placebo-controlled, randomized 2:1 [A].
**Population:** 1,174 patients with untreated stage II–III TNBC (tumour >1–2 cm with nodal involvement, or >2 cm regardless of nodes), enrolled regardless of PD-L1 [A, L-Keytruda].
**Arms** [L-Keytruda]
- Neoadjuvant cycles 1–4 (q3w): pembrolizumab 200 mg or placebo + paclitaxel 80 mg/m² weekly + carboplatin AUC 5 q3w (or AUC 1.5 weekly).
- Neoadjuvant cycles 5–8 (q3w): pembrolizumab or placebo + doxorubicin 60 mg/m² (or epirubicin 90 mg/m²) + cyclophosphamide 600 mg/m².
- After surgery: pembrolizumab 200 mg or placebo q3w for up to 9 cycles.
- The trial cannot separate the neoadjuvant and adjuvant contributions of pembrolizumab [L-Keytruda].

**Dual primary endpoints: pCR (ypT0/Tis ypN0) and EFS**
| Endpoint | Pembro + chemo | Placebo + chemo | Effect |
|---|---|---|---|
| pCR, first 602 patients (interim) | 64.8% | 51.2% | Δ13.6 (5.4–21.8), P < 0.001 [A] |
| **pCR, full ITT n = 1,174** | **63.0% (59.5–66.4)** | **55.6% (50.6–60.6)** | **Δ7.5 (1.6–13.4)** [L-Keytruda] |
| **EFS** (4th interim, median FU 39.1 months) | 36-month 84.5% | 76.8% | **HR 0.63 (0.48–0.82), P < 0.001** [A] |
| **OS** (median FU 75.1 months) | 60-month 86.6% (84.0–88.8) | 81.7% (77.5–85.2) | P = 0.002 [A]; **HR 0.66 (0.50–0.87)**; deaths 15% vs 22% [L-Keytruda] |

**Toxicity**
- Treatment-related grade ≥3 AEs 78.0% vs 73.0%; deaths 0.4% vs 0.3% [A 2020].
- From the label (pembrolizumab arm, n = 778) [L-Keytruda]:
  - Fatal ARs 0.9% (including adrenal crisis, autoimmune encephalitis, hepatitis, pneumonitis).
  - Serious ARs 44%, mainly febrile neutropenia 15%.
  - Pembrolizumab discontinued for ARs in 20%: ALT increase 2.7%, AST increase 1.5%, rash 1%.
- Immune-related endocrinopathy rates specific to KEYNOTE-522 (hypothyroidism, adrenal insufficiency): **[UNVERIFIED]** from the trial paper. The label gives only pooled pembrolizumab rates (hypothyroidism 8%, all indications).

---

## 20. CREATE-X (adjuvant capecitabine after neoadjuvant chemotherapy) — [PARTIAL]

**References**
- Masuda, N., Lee, S.-J., Ohtani, S., Im, Y.-H., Lee, E.-S., Yokota, I., Kuroi, K., Im, S.-A., Park, B.-W., Kim, S.-B., Yanagita, Y., Ohno, S., Takao, S., Aogi, K., Iwata, H., Jeong, J., Kim, A., Park, K.-H., Sasano, H., . . . Toi, M. (2017). Adjuvant capecitabine for breast cancer after preoperative chemotherapy. *The New England Journal of Medicine*, *376*(22), 2147–2159. https://doi.org/10.1056/NEJMoa1612645 — PMID 28564564
- (Dose source [SR]) Abahssain, H., Souadka, A., Alem, R., Santoni, M., Battelli, N., Amela, E., Lemaire, A., Rodriguez, J., & Errihani, H. (2024). Shifting paradigms in TNBC treatment: Emerging alternatives to capecitabine in the post-neoadjuvant setting. *Current Oncology*, *31*(7), 3771–3782. https://doi.org/10.3390/curroncol31070278 — PMID 39057150 (PMC11276086)

**Design:** Phase 3, randomized, Japan and Korea (directly relevant to East Asian patients) [A].
**Population:** 910 patients with HER2-negative residual invasive disease after neoadjuvant anthracycline and/or taxane chemotherapy; TNBC 32.2% [A, SR].
**Arms:** Standard post-surgical therapy (ET if HR-positive) ± capecitabine. Capecitabine 1,250 mg/m² twice daily, days 1–14 q3w, 6–8 cycles [SR; not confirmed from the primary paper].
**Primary endpoint (DFS):** Stopped early after meeting the endpoint at interim. 5-year DFS 74.1% vs 67.6%; **HR 0.70 (0.53–0.92), P = 0.01** [A].
**OS:** 5-year 89.2% vs 83.6%; HR 0.59 (0.39–0.90), P = 0.01 [A].
**TNBC subgroup:** DFS 69.8% vs 56.1%, HR 0.58 (0.39–0.87); OS 78.8% vs 70.3%, HR 0.52 (0.30–0.90) [A].
**Toxicity:** **Hand-foot syndrome 73.4%** [A]. Grade ≥3 HFS, diarrhoea and neutropenia rates: **[UNVERIFIED]** (NEJM full text not open).

---

## 21. EBCTCG 2015: adjuvant bisphosphonates — [VERIFIED]

**Reference**
- Early Breast Cancer Trialists' Collaborative Group. (2015). Adjuvant bisphosphonate treatment in early breast cancer: Meta-analyses of individual patient data from randomised trials. *The Lancet*, *386*(10001), 1353–1361. https://doi.org/10.1016/S0140-6736(15)60908-4 — PMID 26211824. **Errata:** 2016 (no PMID) and PMID 28656899 (not reviewed).

**Design:** Individual-patient-data meta-analysis of all unconfounded trials of bisphosphonate vs control [A].
**Population:** 18,766 women (97% in trials of 2–5 years of bisphosphonate); median FU 5.6 woman-years [A].
**Agents:** Aminobisphosphonates (zoledronic acid, ibandronate, pamidronate) and clodronate. No difference in benefit by class or schedule [A].

**Results (RR, 95% CI)** [A]
| Endpoint | All women | Postmenopausal (n = 11,767) |
|---|---|---|
| Any recurrence | 0.94 (0.87–1.01), 2p = 0.08 | **0.86 (0.78–0.94)**, 2p = 0.002 |
| Distant recurrence | 0.92 (0.85–0.99) | **0.82 (0.74–0.92)** |
| Bone recurrence | 0.83 (0.73–0.94) | **0.72 (0.60–0.86)** |
| Breast cancer mortality | 0.91 (0.83–0.99) | **0.82 (0.73–0.93)** |

- **Premenopausal women: no apparent effect on any outcome.** "Postmenopausal" combined natural and artificial (OFS-induced) menopause.
- Fractures reduced: RR 0.85 (0.75–0.97). No difference in non-breast-cancer mortality.
- Specific toxicity (osteonecrosis of the jaw, renal) is not reported in the abstract: **[UNVERIFIED]**.

---

## 22. CALGB 9741 (dose-dense AC→T) and EBCTCG dose-intensity meta-analysis — [VERIFIED]

**References**
- Citron, M. L., Berry, D. A., Cirrincione, C., Hudis, C., Winer, E. P., Gradishar, W. J., Davidson, N. E., Martino, S., Livingston, R., Ingle, J. N., Perez, E. A., Carpenter, J., Hurd, D., Holland, J. F., Smith, B. L., Sartor, C. I., Leung, E. H., Abrams, J., Schilsky, R. L., . . . Norton, L. (2003). Randomized trial of dose-dense versus conventionally scheduled and sequential versus concurrent combination chemotherapy as postoperative adjuvant treatment of node-positive primary breast cancer: First report of Intergroup Trial C9741/Cancer and Leukemia Group B Trial 9741. *Journal of Clinical Oncology*, *21*(8), 1431–1439. https://doi.org/10.1200/JCO.2003.09.081 — PMID 12668651. **Erratum:** J Clin Oncol 21(11):2226 (no PMID; not reviewed).
- (12.3-year outcomes, reported within a correlative paper) Liu, M. C., Pitcher, B. N., Mardis, E. R., Davies, S. R., Friedman, P. N., Snider, J. E., Vickery, T. L., Reed, J. P., DeSchryver, K., Singh, B., Gradishar, W. J., Perez, E. A., Martino, S., Citron, M. L., Norton, L., Winer, E. P., Hudis, C. A., Carey, L. A., Bernard, P. S., . . . Barry, W. T. (2016). PAM50 gene signatures and breast cancer prognosis with adjuvant anthracycline- and taxane-based chemotherapy: Correlative analysis of C9741 (Alliance). *npj Breast Cancer*, *2*, Article 15023. https://doi.org/10.1038/npjbcancer.2015.23 — PMID 28691057 (PMC5501351)
- Early Breast Cancer Trialists' Collaborative Group. (2019). Increasing the dose intensity of chemotherapy by more frequent administration or sequential scheduling: A patient-level meta-analysis of 37 298 women with early breast cancer in 26 randomised trials. *The Lancet*, *393*(10179), 1440–1452. https://doi.org/10.1016/S0140-6736(18)33137-4 — PMID 30739743

**CALGB 9741 design:** Phase 3, 2 × 2 factorial; 2,005 women with node-positive operable breast cancer [A].
**Arms** (the registry outline adds tamoxifen for 5 years after chemotherapy and radiotherapy 4–6 weeks after chemotherapy) [A, CT]
| Arm | Regimen |
|---|---|
| I | Sequential A ×4 → T ×4 → C ×4, every 3 weeks |
| II | Sequential A → T → C, every 2 weeks + filgrastim |
| III | Concurrent AC ×4 → T ×4, every 3 weeks |
| **IV (dose-dense AC→T)** | **AC ×4 → T ×4, every 2 weeks + filgrastim** |

- Doses: doxorubicin 60 mg/m², cyclophosphamide 600 mg/m², paclitaxel 175 mg/m² (3-hour infusion) [CT].
- Filgrastim 5 µg/kg SC on days 3–10 of each cycle [CT].

**Primary endpoint (DFS), median FU 36 months** [A]
- Dose-dense vs conventional: **DFS RR 0.74, P = .010; OS RR 0.69, P = .013**. 4-year DFS 82% vs 75%.
- Sequential vs concurrent: no difference; no interaction between density and sequence.
**12.3-year update (in Liu 2016)** [FT]
- Dose-dense benefit persisted: conventional vs dose-dense HR 1.26 (1.08–1.47) for RFS and 1.21 (1.03–1.43) for OS.
- Sequential vs concurrent: still no difference (RFS HR 1.06, 0.91–1.24).
**Toxicity:** Severe neutropenia was **less** frequent with dose-dense regimens, because of G-CSF support [A]. Other rates (anaemia/transfusion, febrile neutropenia): **[UNVERIFIED]** (JCO full text inaccessible).

**EBCTCG 2019 (26 trials, 37,298 women)** [A]
- Dose-intense vs standard schedule: 10-year recurrence 28.0% vs 31.4%, **RR 0.86 (0.82–0.89)**.
- Breast cancer mortality 18.9% vs 21.3%, RR 0.87 (0.83–0.92). All-cause mortality 22.1% vs 24.8%, RR 0.87 (0.83–0.91).
- Death without recurrence 4.1% vs 4.6%, RR 0.88 (0.78–0.99): no excess non-cancer mortality.
- 2-weekly vs the same drugs 3-weekly (7 trials): recurrence 24.0% vs 28.3%, RR 0.83 (0.76–0.91). Similar effect in ER-positive and ER-negative disease.

---

# G. Taiwan regulatory snapshot and label sources

**TFDA licence file (dataset 36; file timestamp 2026-10-27; downloaded 2026-10-29)** [TFDA]. Only active licences listed; early-breast indication wording paraphrased from the 適應症 field.

| Drug (TW brand) | Licence no. (example strength) | Early-breast indication on TW licence |
|---|---|---|
| Abemaciclib 捷癌寧 VERZENIO | 衛部藥輸字第027641號 (150 mg) | Adjuvant with ET (tamoxifen or AI) for HR+/HER2−, **node-positive**, high-risk EBC (no Ki-67 requirement in the wording) |
| Ribociclib 擊癌利 KISQALI | 衛部藥輸字第027320號 (200 mg) | Adjuvant with AI for HR+/HER2− **stage II–III** high-risk EBC |
| Palbociclib 愛乳適 IBRANCE | 衛部藥輸字第028006號 (100 mg tab) | **None** (advanced disease only); consistent with PALLAS/PENELOPE-B |
| Olaparib 令癌莎 Lynparza | 衛部藥輸字第027446號 (150 mg) | Adjuvant for gBRCA1/2, HER2−, high-risk EBC after (neo)adjuvant chemotherapy |
| Pertuzumab 賀疾妥 Perjeta | 衛署菌疫輸字第000942號 | Neoadjuvant (>2 cm or N+) and adjuvant high-risk HER2+ EBC; the licence notes high risk = **node-positive per APHINITY** |
| Pertuzumab/trastuzumab SC 賀雙妥 Phesgo | 衛部菌疫輸字第001172號 | Neoadjuvant and adjuvant HER2+ EBC as for Perjeta |
| T-DM1 賀癌寧 Kadcyla | 衛部菌疫輸字第000949號 | Adjuvant for residual disease after taxane + trastuzumab neoadjuvant therapy |
| T-DXd 優赫得 Enhertu | 衛部菌疫輸字第001179號 | **Neoadjuvant T-DXd → THP, stage II–III HER2+ (DB-11). No post-neoadjuvant (DB-05) indication.** |
| Neratinib 賀儷安 NERLYNX | 衛部藥輸字第027901號 | Extended adjuvant after trastuzumab-based adjuvant therapy, HER2+ EBC (the TW wording has no HR+ restriction) |
| Pembrolizumab 吉舒達 Keytruda | 衛部菌疫輸字第001025號 | With chemotherapy as neoadjuvant, then adjuvant monotherapy, for high-risk early TNBC |

- **NHI (健保) reimbursement criteria for these drugs: [UNVERIFIED].** www.nhi.gov.tw was not reachable; no MOHW press release was checked for this note.

**US label versions used**
- openFDA: KEYTRUDA effective 2026-07-10; KADCYLA 2026-04-01; ENHERTU 2026-05-15; KISQALI 2026-07-01; LYNPARZA 2025-07-10; NERLYNX 2026-07-02; PERJETA 2026-04-30.
- DailyMed: VERZENIO SPL version 31, published 2026-10-01 (not in openFDA).

---

# H. Nursing quick reference: signature toxicities and monitoring (from sources above)

| Regimen | Signature toxicity (verified rate) | What the label or trial asks for |
|---|---|---|
| Exemestane/AI + OFS | Osteoporosis 13.2% vs 6.4% (vs tamoxifen + OFS); fractures; musculoskeletal symptoms | Bone health (BMD); EBCTCG AI vs tamoxifen fracture RR 1.42 |
| Tamoxifen (incl. 10 years) | Endometrial cancer RR 1.74 and PE RR 1.87 (ATLAS) | Report abnormal vaginal bleeding; VTE awareness |
| Abemaciclib | Diarrhoea 84% (grade 3 8%); neutropenia grade 3–4 19.6%; VTE 2.5% (4.3% with tamoxifen); ILD 3% | LFTs every 2 weeks ×2 months, then monthly ×2; antidiarrhoeals; VTE history not studied |
| Ribociclib (400 mg) | Neutropenia 62.8% (grade 3 42.2%); ALT increase 19.7%; QT prolongation 5.4% | ECG and electrolytes before start, ECG again about day 14 of cycle 1; LFTs every 2 weeks for 2 cycles, then at the start of the next 4 cycles; with a strong CYP3A inhibitor reduce to 200 mg [L-Kisqali] |
| Olaparib | Anaemia grade ≥3 8.7%; nausea 56.9%; transfusion 5.8% | CBC at baseline, then monthly [L-Lynparza]; MDS/AML not increased at 6.1 years |
| Pertuzumab (APHINITY) | Grade ≥3 diarrhoea 9.8% (during chemotherapy) | LVEF before start and at regular intervals [L-Perjeta]; primary cardiac events 0.7% |
| T-DM1 | Thrombocytopenia 29% (grade ≥3 19% in Asians); neuropathy 32%; AST increase 79% | Platelets, transaminases and bilirubin before each dose [L-Kadcyla]; bleeding precautions |
| T-DXd (post-neoadjuvant) | ILD 9.6–10% (2 deaths); nausea 71%; radiation pneumonitis 31% | Baseline chest CT; regular chest CT if receiving RT; antiemetics |
| Neratinib | Grade 3 diarrhoea 40% without prophylaxis | Loperamide prophylaxis for 56 days, or 2-week dose escalation |
| Pembrolizumab (KEYNOTE-522) | Serious febrile neutropenia 15%; fatal ARs 0.9% (incl. adrenal crisis, hepatitis, pneumonitis); ALT/AST rise the leading cause of discontinuation | Distinguish irAEs from chemotherapy toxicity; KEYNOTE-522-specific irAE monitoring schedule not verified from the label **[UNVERIFIED]** |
| Capecitabine (CREATE-X) | Hand-foot syndrome 73.4% | Skin care education; dose holds |
| Dose-dense AC→T | Less severe neutropenia with G-CSF support | Filgrastim days 3–10 (C9741 protocol) |

---

## Appendix: PMID index

| Trial / topic | Primary PMID | Follow-up / latest PMID(s) |
|---|---|---|
| SOFT/TEXT | 24881463 (combined), 25495490 (SOFT) | 29863451; 36493334 (erratum 37450784); 36521078; **42229584 (final 15-year, 2026)** |
| EBCTCG AI vs tamoxifen | 26211827 | 35123662 (premenopausal + OFS; erratum 35358463) |
| ATLAS | 23219286 | — |
| MA.17 / MA.17R | 14551341 / 27264120 | — |
| NSABP B-42 | 30509771 (erratum 30614468) | 37184928 (10-year; erratum 37766422) |
| ABCSG-16/SALSA | 34320285 | — |
| EBCTCG extended AI | 40783288 (erratum 40812341) | — |
| EBCTCG 20-year recurrence | 29117498 | — |
| monarchE | 32954927 | 34656740; 36493792; 35337972 (safety); **41110697 (OS)** |
| NATALEE | 38507751 | 39442617 (final iDFS); 40996773 (4-year); **41320342 (5-year)** |
| PALLAS | 33460574 | 34874182; **41110701 (5-year)** |
| PENELOPE-B | 33793299 | **40139460 (final OS)** |
| OlympiA | 34081848 | 36228963 (OS); **42636977 (6.1-year)** |
| TAILORx | 29860917 | — |
| RxPONDER | 34914339 | — |
| APHINITY | 28581356 | 33539215; **39259927 (8.4-year OS)** |
| KATHERINE | 30516102 | **39813643 (OS)** |
| ExteNET | 26874901 | 29146401; 33183970; **36898233 (final OS)** |
| NeoSphere | 22153890 | 27179402 |
| TRYPHAENA | 23704196 | 29223479 |
| DESTINY-Breast05 | **41370739** (erratum 41931063) | — |
| DESTINY-Breast11 | **41130363** | — |
| APT | 25564897 (erratum 26559595) | 30939096; **36858723 (10-year)** |
| KEYNOTE-522 | 32101663 | 35139274 (EFS); **39282906 (OS)** |
| CREATE-X | 28564564 | dose from review 39057150 |
| EBCTCG bisphosphonates | 26211824 | — |
| CALGB 9741 | 12668651 | 28691057 (12.3-year data); EBCTCG 2019: 30739743 |

---

## Critic additions

Added 2026-10-29 by the completeness critic (append only). Biggest gap found: **the early-disease notes had no local therapy at all** (surgery, margins, axilla, radiotherapy, DCIS) and no adjuvant-trastuzumab foundation trials. All numbers below are from the PubMed abstract [A] unless marked; every PMID was pulled through NCBI E-utilities on 2026-10-29.

### CA2.1 Surgery and margins [VERIFIED; A]

**NSABP B-06, 20-year (Fisher 2002)** — 1,851 women; total mastectomy vs lumpectomy vs lumpectomy + breast irradiation.
- Ipsilateral breast recurrence: **14.3%** (lumpectomy + RT) vs **39.2%** (lumpectomy alone), P < 0.001.
- No difference in DFS, distant DFS or OS. Death, lumpectomy + RT vs mastectomy: HR 0.97 (0.83–1.14).
- Teaching point: breast conservation **with** radiotherapy = mastectomy for survival, provided margins are tumour-free.

**Margins, invasive cancer (SSO–ASTRO 2014; Moran 2014)** — meta-analysis of 33 studies, 28,162 patients.
- Positive margin = **ink on invasive carcinoma or DCIS**; it doubles ipsilateral breast tumour recurrence (IBTR).
- **"No ink on tumour" is an adequate margin.** Wider margins do not lower IBTR further, including in young patients, unfavourable biology, lobular cancer or extensive intraductal component.

**Margins, pure DCIS (SSO–ASTRO–ASCO 2016; Morrow 2016)** — 20 studies, 7,883 patients; applies to DCIS treated with BCS **plus whole-breast irradiation**.
- **2 mm** is the standard adequate margin. Wider than 2 mm adds nothing.
- Negative margins <2 mm are **not** by themselves an indication for mastectomy; re-excision is a clinical judgement.
- Teaching contrast: invasive = no ink on tumour; DCIS = 2 mm.

### CA2.2 Axillary management [VERIFIED; A]

| Trial | Population | Comparison | Key result |
|---|---|---|---|
| **ACOSOG Z0011** (Giuliano 2017, 10-year) | cT1–T2, no palpable nodes, **1–2 positive sentinel nodes**, lumpectomy + **tangential whole-breast RT** (third field prohibited) + systemic therapy; n = 891 | SLNB alone vs ALND | 10-year OS **86.3% vs 83.6%**, HR 0.85, non-inferiority P = .02; DFS 80.2% vs 78.2%. Regional recurrence did not differ |
| **AMAROS** (Donker 2014; Bartels 2023) | cT1–2 cN0, positive SLN; 1,425 randomised node-positive | Axillary RT vs ALND | 5-year axillary recurrence 1.19% vs 0.43% (test underpowered). **10-year 1.82% vs 0.93%** (HR 1.71, 0.67–4.39); no OS or DFS difference. **Lymphoedema at 5 years 11.9% (RT) vs 24.5% (ALND)**, P < .001. In the ALND arm, 33% had additional positive nodes. Exploratory: 10-year second primary cancers 12.1% (RT) vs 8.3% (ALND) |
| **SOUND** (Gentilini 2023) | Tumour **≤2 cm**, **negative axillary ultrasound**; n = 1,405 ITT (87.8% ER+/HER2−; median age 60) | No axillary surgery vs SLNB | 5-year DDFS **98.0% vs 97.7%** (HR 0.84; non-inferior). 13.7% of the SLNB arm were node-positive |
| **INSEMA** (Reimer 2025) | cT1–T2 (≤5 cm), cN0, planned BCS; 5,502 randomised **1:4** | No axillary surgery vs SLNB | Per-protocol 5-year iDFS **91.9% vs 91.7%**, HR 0.91 (0.73–1.14), non-inferior. Axillary recurrence 1.0% vs 0.3%. Less lymphoedema and arm morbidity without surgery |
| **ACOSOG Z1071** (Boughey 2013) | Biopsy-proven **cN1**, after neoadjuvant chemotherapy; SLNB **and** ALND in all | False-negative rate of SLNB after NAC | With ≥2 SLNs: **FNR 12.6%**, which failed the ≤10% target. SLN not found in 7.1%; nodal pCR 41.0%. Dual-tracer mapping was encouraged |

- Nursing link: lymphoedema-risk teaching in breast_4 §6.10. AMAROS gives the cleanest head-to-head lymphoedema figure.
- The technical refinements that make post-NAC SLNB acceptable (≥3 SLNs, clipped-node retrieval/targeted axillary dissection) were **not verified** here [UNVERIFIED].

### CA2.3 Radiotherapy [VERIFIED; A]

- **EBCTCG 2011, RT after BCS** (17 trials, 10,801 women): 10-year any first recurrence **35.0% → 19.3%**; 15-year breast-cancer death **25.2% → 21.4%**. About **one breast-cancer death avoided by year 15 for every four recurrences avoided by year 10**. pN+ subgroup: recurrence 63.7% → 42.5%, death 51.3% → 42.8%.
- **EBCTCG 2014, post-mastectomy RT** (22 trials, 8,135 women; after mastectomy + axillary dissection):
  - pN0 (n = 700): no benefit (overall recurrence RR 1.06; breast-cancer mortality RR 1.18, NS).
  - **1–3 positive nodes** (n = 1,314): overall recurrence **RR 0.68** (0.57–0.82); breast-cancer mortality **RR 0.80** (0.67–0.95). Benefit held when systemic therapy was given.
  - ≥4 nodes (n = 1,772): recurrence RR 0.79; mortality RR 0.87.
  - Erratum: Lancet 2014;384:1848 (not reviewed).
- **FAST-Forward** (Murray Brunt 2020; 4,096 patients, pT1–3 pN0–1 after BCS or mastectomy; whole breast/chest wall):
  - 40 Gy/15 fractions (3 weeks) vs 27 Gy/5 vs **26 Gy/5 fractions (1 week)**.
  - 5-year IBTR after 40 Gy 2.1%; HR 0.67 (0.38–1.16) for 26 Gy, non-inferior.
  - Moderate/marked clinician-assessed normal-tissue effects at 5 years: 9.9% (40 Gy), **15.4% (27 Gy)**, 11.9% (26 Gy). **26 Gy/5 is non-inferior and as safe; 27 Gy/5 is more toxic.**
- **PRIME II** (Kunkler 2023; n = 1,326): age **≥65**, HR+, **node-negative**, T1–T2 **≤3 cm**, clear margins, on adjuvant endocrine therapy; WBI 40–50 Gy vs none.
  - 10-year local recurrence **9.5% (no RT) vs 0.9% (RT)**, HR 10.4.
  - Distant recurrence as first event 1.6% vs 3.0%; **10-year OS 80.8% vs 80.7%** (no difference).
  - Teaching point: omitting RT in low-risk older women raises local recurrence but not death; endocrine adherence becomes the safeguard.

### CA2.4 DCIS: adjuvant tamoxifen (NSABP B-24; Fisher 1999) [VERIFIED; A]
- 1,804 women with DCIS (positive margins allowed) after lumpectomy + RT (50 Gy); tamoxifen 20 mg daily × 5 years vs placebo.
- Breast-cancer events at 5 years **8.2% vs 13.4%** (P = 0.0009). Invasive events in the tamoxifen arm 4.1% (ipsilateral 2.1%, contralateral 1.8%).
- Benefit seen even with involved margins or comedonecrosis. The abstract does not mention ER status; any ER-restricted recommendation for DCIS needs a separate source [UNVERIFIED here].

### CA2.5 Adjuvant trastuzumab: the foundation trials (gap) [VERIFIED; A]

| Trial | Design | Result |
|---|---|---|
| **NSABP B-31 + NCCTG N9831 joint OS** (Perez 2014) | 4,046 patients; AC → paclitaxel ± trastuzumab; median 8.4 years on study | OS **HR 0.63** (0.54–0.73); 10-year OS **75.2% → 84.0%**. DFS HR 0.60; 10-year DFS 62.2% → 73.7%. All subgroups benefited |
| **HERA, final 11-year** (Cameron 2017) | 5,102 randomised after all primary therapy; trastuzumab 8 → 6 mg/kg q3w for 1 or 2 years vs observation | 1 year vs observation: DFS HR **0.76**, death HR **0.74** (despite 52% crossover from observation). **2 years vs 1 year: DFS HR 1.02 — no added benefit.** 10-year DFS 63% / 69% / 69%. Secondary cardiac end points 7.3% (2 years), 4.4% (1 year), 0.9% (observation). Erratum Lancet 2019;393:1100 |
| **PERSEPHONE** (Earl 2019) | 4,088 patients; 6 vs 12 months, IV (8 → 6 mg/kg) or SC 600 mg, with chemotherapy | 4-year DFS **89.4% (6 months) vs 89.8% (12 months)**, HR 1.07 (90% CI 0.93–1.24), non-inferior. Stopped early for cardiotoxicity **3% vs 8%**; severe AEs 19% vs 24% |

- Practice framing for the chapter: **1 year remains the label standard** (US Herceptin label: 52 weeks; "extending adjuvant treatment beyond one year is not recommended", breast_4 §3). PERSEPHONE supports *considering* 6 months for similar-risk patients, e.g. after cardiotoxicity. HERA explains why we never give 2 years.

### CA2.6 pCR definition and meaning (CTNeoBC; Cortazar 2014) [VERIFIED; A]
- 12 trials, 11,955 patients.
- pCR defined as **ypT0 ypN0 or ypT0/is ypN0** (breast **and** nodes) predicts survival better than breast-only ypT0/is. EFS HR 0.48 and OS HR 0.36 for ypT0/is ypN0.
- Prognostic value is strongest in **TNBC** (EFS HR 0.24; OS 0.16) and **HER2+/HR− treated with trastuzumab** (EFS 0.15; OS 0.08).
- **Trial-level surrogacy failed** (R² 0.03 for EFS, 0.24 for OS): a higher pCR rate in one arm does not by itself prove an EFS/OS gain. Useful when explaining why KEYNOTE-522's modest ITT pCR gain (63.0 vs 55.6%) still mattered only once EFS/OS read out.
- Erratum: Lancet 2019;393:986 (not reviewed).

### CA2.7 Re-check of high-stakes numbers already in this file (primary source re-opened 2026-10-29)

| Number in notes | Re-checked against | Result |
|---|---|---|
| KEYNOTE-522 ITT pCR **63.0% (59.5–66.4) vs 55.6% (50.6–60.6)** | Keytruda label (openFDA, effective 2026-07-10), Table 115 | **Confirmed** (494/784 vs 217/390; significance was shown at the 602-patient interim, p = 0.00055) |
| Ribociclib adjuvant **400 mg daily, 21/7, for 3 years**, with an AI | Kisqali label (2026-07-01) §2.1 | **Confirmed**. ECG before start and about day 14 of cycle 1. Below 200 mg/day: discontinue |
| Olaparib adjuvant **300 mg BID for 1 year** | Lynparza label (2025-07-10) §2 | **Confirmed**; concurrent endocrine therapy for HR+; CLcr 31–50 mL/min → 200 mg BID |
| Neratinib loperamide: **4 mg TID weeks 1–2, 4 mg BID weeks 3–8**, then PRN ≤16 mg/day; 240 mg daily with food up to 1 year | Nerlynx label (2026-07-02) Table 1, §2.2 | **Confirmed** |

No corrections were needed in this file.

### CA2.8 Still [PARTIAL] or [UNVERIFIED]
- **CREATE-X capecitabine dose**: the NEJM protocol supplement returned HTTP 403. Two secondary sources agree on 2,500 mg/m²/day in two divided doses (= 1,250 mg/m² BID), days 1–14 q3w, 8 cycles; the trial is registered as UMIN000000843 (secondary source; the UMIN record itself was not opened). Stays **[PARTIAL]**.
- Neoadjuvant indications, post-NAC SLNB technical criteria, regional nodal irradiation trials (MA.20, EORTC 22922) and partial-breast irradiation were not covered [UNVERIFIED].

### CA2 references (APA 7)
- Bartels, S. A. L., Donker, M., Poncet, C., Sauvé, N., Straver, M. E., van de Velde, C. J. H., Mansel, R. E., Blanken, C., Orzalesi, L., Klinkenbijl, J. H. G., van der Mijle, H. C. J., Nieuwenhuijzen, G. A. P., Veltkamp, S. C., van Dalen, T., Marinelli, A., Rijna, H., Snoj, M., Bundred, N. J., Merkus, J. W. S., . . . Rutgers, E. J. T. (2023). Radiotherapy or surgery of the axilla after a positive sentinel node in breast cancer: 10-year results of the randomized controlled EORTC 10981-22023 AMAROS trial. *Journal of Clinical Oncology, 41*(12), 2159–2165. https://doi.org/10.1200/JCO.22.01565 (PMID 36383926)
- Boughey, J. C., Suman, V. J., Mittendorf, E. A., Ahrendt, G. M., Wilke, L. G., Taback, B., Leitch, A. M., Kuerer, H. M., Bowling, M., Flippo-Morton, T. S., Byrd, D. R., Ollila, D. W., Julian, T. B., McLaughlin, S. A., McCall, L., Symmans, W. F., Le-Petross, H. T., Haffty, B. G., Buchholz, T. A., . . . Hunt, K. K. (2013). Sentinel lymph node surgery after neoadjuvant chemotherapy in patients with node-positive breast cancer: The ACOSOG Z1071 (Alliance) clinical trial. *JAMA, 310*(14), 1455–1461. https://doi.org/10.1001/jama.2013.278932 (PMID 24101169; PMCID PMC4075763)
- Cameron, D., Piccart-Gebhart, M. J., Gelber, R. D., Procter, M., Goldhirsch, A., de Azambuja, E., Castro, G., Untch, M., Smith, I., Gianni, L., Baselga, J., Al-Sakaff, N., Lauer, S., McFadden, E., Leyland-Jones, B., Bell, R., Dowsett, M., & Jackisch, C. (2017). 11 years' follow-up of trastuzumab after adjuvant chemotherapy in HER2-positive early breast cancer: Final analysis of the HERceptin Adjuvant (HERA) trial. *The Lancet, 389*(10075), 1195–1205. https://doi.org/10.1016/S0140-6736(16)32616-2 (PMID 28215665; PMCID PMC5465633)
- Cortazar, P., Zhang, L., Untch, M., Mehta, K., Costantino, J. P., Wolmark, N., Bonnefoi, H., Cameron, D., Gianni, L., Valagussa, P., Swain, S. M., Prowell, T., Loibl, S., Wickerham, D. L., Bogaerts, J., Baselga, J., Perou, C., Blumenthal, G., Blohmer, J., . . . von Minckwitz, G. (2014). Pathological complete response and long-term clinical benefit in breast cancer: The CTNeoBC pooled analysis. *The Lancet, 384*(9938), 164–172. https://doi.org/10.1016/S0140-6736(13)62422-8 (PMID 24529560)
- Donker, M., van Tienhoven, G., Straver, M. E., Meijnen, P., van de Velde, C. J. H., Mansel, R. E., Cataliotti, L., Westenberg, A. H., Klinkenbijl, J. H. G., Orzalesi, L., Bouma, W. H., van der Mijle, H. C. J., Nieuwenhuijzen, G. A. P., Veltkamp, S. C., Slaets, L., Duez, N. J., de Graaf, P. W., van Dalen, T., Marinelli, A., . . . Rutgers, E. J. T. (2014). Radiotherapy or surgery of the axilla after a positive sentinel node in breast cancer (EORTC 10981-22023 AMAROS): A randomised, multicentre, open-label, phase 3 non-inferiority trial. *The Lancet Oncology, 15*(12), 1303–1310. https://doi.org/10.1016/S1470-2045(14)70460-7 (PMID 25439688; PMCID PMC4291166)
- Earl, H. M., Hiller, L., Vallier, A.-L., Loi, S., McAdam, K., Hughes-Davies, L., Harnett, A. N., Ah-See, M.-L., Simcock, R., Rea, D., Raj, S., Woodings, P., Harries, M., Howe, D., Raynes, K., Higgins, H. B., Wilcox, M., Plummer, C., Mansi, J., . . . Dunn, J. A. (2019). 6 versus 12 months of adjuvant trastuzumab for HER2-positive early breast cancer (PERSEPHONE): 4-year disease-free survival results of a randomised phase 3 non-inferiority trial. *The Lancet, 393*(10191), 2599–2612. https://doi.org/10.1016/S0140-6736(19)30650-6 (PMID 31178152; PMCID PMC6615016)
- Early Breast Cancer Trialists' Collaborative Group. (2011). Effect of radiotherapy after breast-conserving surgery on 10-year recurrence and 15-year breast cancer death: Meta-analysis of individual patient data for 10,801 women in 17 randomised trials. *The Lancet, 378*(9804), 1707–1716. https://doi.org/10.1016/S0140-6736(11)61629-2 (PMID 22019144; PMCID PMC3254252)
- Early Breast Cancer Trialists' Collaborative Group. (2014). Effect of radiotherapy after mastectomy and axillary surgery on 10-year recurrence and 20-year breast cancer mortality: Meta-analysis of individual patient data for 8135 women in 22 randomised trials. *The Lancet, 383*(9935), 2127–2135. https://doi.org/10.1016/S0140-6736(14)60488-8 (PMID 24656685; PMCID PMC5015598)
- Fisher, B., Anderson, S., Bryant, J., Margolese, R. G., Deutsch, M., Fisher, E. R., Jeong, J.-H., & Wolmark, N. (2002). Twenty-year follow-up of a randomized trial comparing total mastectomy, lumpectomy, and lumpectomy plus irradiation for the treatment of invasive breast cancer. *The New England Journal of Medicine, 347*(16), 1233–1241. https://doi.org/10.1056/NEJMoa022152 (PMID 12393820)
- Fisher, B., Dignam, J., Wolmark, N., Wickerham, D. L., Fisher, E. R., Mamounas, E., Smith, R., Begovic, M., Dimitrov, N. V., Margolese, R. G., Kardinal, C. G., Kavanah, M. T., Fehrenbacher, L., & Oishi, R. H. (1999). Tamoxifen in treatment of intraductal breast cancer: National Surgical Adjuvant Breast and Bowel Project B-24 randomised controlled trial. *The Lancet, 353*(9169), 1993–2000. https://doi.org/10.1016/S0140-6736(99)05036-9 (PMID 10376613)
- Gentilini, O. D., Botteri, E., Sangalli, C., Galimberti, V., Porpiglia, M., Agresti, R., Luini, A., Viale, G., Cassano, E., Peradze, N., Toesca, A., Massari, G., Sacchini, V., Munzone, E., Leonardi, M. C., Cattadori, F., Di Micco, R., Esposito, E., Sgarella, A., . . . Veronesi, P. (2023). Sentinel lymph node biopsy vs no axillary surgery in patients with small breast cancer and negative results on ultrasonography of axillary lymph nodes: The SOUND randomized clinical trial. *JAMA Oncology, 9*(11), 1557–1564. https://doi.org/10.1001/jamaoncol.2023.3759 (PMID 37733364; PMCID PMC10514873)
- Giuliano, A. E., Ballman, K. V., McCall, L., Beitsch, P. D., Brennan, M. B., Kelemen, P. R., Ollila, D. W., Hansen, N. M., Whitworth, P. W., Blumencranz, P. W., Leitch, A. M., Saha, S., Hunt, K. K., & Morrow, M. (2017). Effect of axillary dissection vs no axillary dissection on 10-year overall survival among women with invasive breast cancer and sentinel node metastasis: The ACOSOG Z0011 (Alliance) randomized clinical trial. *JAMA, 318*(10), 918–926. https://doi.org/10.1001/jama.2017.11470 (PMID 28898379; PMCID PMC5672806)
- Kunkler, I. H., Williams, L. J., Jack, W. J. L., Cameron, D. A., & Dixon, J. M. (2023). Breast-conserving surgery with or without irradiation in early breast cancer. *The New England Journal of Medicine, 388*(7), 585–594. https://doi.org/10.1056/NEJMoa2207586 (PMID 36791159)
- Moran, M. S., Schnitt, S. J., Giuliano, A. E., Harris, J. R., Khan, S. A., Horton, J., Klimberg, S., Chavez-MacGregor, M., Freedman, G., Houssami, N., Johnson, P. L., & Morrow, M. (2014). Society of Surgical Oncology–American Society for Radiation Oncology consensus guideline on margins for breast-conserving surgery with whole-breast irradiation in stages I and II invasive breast cancer. *Journal of Clinical Oncology, 32*(14), 1507–1515. https://doi.org/10.1200/JCO.2013.53.3935 (PMID 24516019)
- Morrow, M., Van Zee, K. J., Solin, L. J., Houssami, N., Chavez-MacGregor, M., Harris, J. R., Horton, J., Hwang, S., Johnson, P. L., Marinovich, M. L., Schnitt, S. J., Wapnir, I., & Moran, M. S. (2016). Society of Surgical Oncology–American Society for Radiation Oncology–American Society of Clinical Oncology consensus guideline on margins for breast-conserving surgery with whole-breast irradiation in ductal carcinoma in situ. *Practical Radiation Oncology, 6*(5), 287–295. https://doi.org/10.1016/j.prro.2016.06.011 (PMID 27538810; PMCID PMC5070537)
- Murray Brunt, A., Haviland, J. S., Wheatley, D. A., Sydenham, M. A., Alhasso, A., Bloomfield, D. J., Chan, C., Churn, M., Cleator, S., Coles, C. E., Goodman, A., Harnett, A., Hopwood, P., Kirby, A. M., Kirwan, C. C., Morris, C., Nabi, Z., Sawyer, E., Somaiah, N., . . . Yarnold, J. R. (2020). Hypofractionated breast radiotherapy for 1 week versus 3 weeks (FAST-Forward): 5-year efficacy and late normal tissue effects results from a multicentre, non-inferiority, randomised, phase 3 trial. *The Lancet, 395*(10237), 1613–1626. https://doi.org/10.1016/S0140-6736(20)30932-6 (PMID 32580883; PMCID PMC7262592)
- Perez, E. A., Romond, E. H., Suman, V. J., Jeong, J.-H., Sledge, G., Geyer, C. E., Martino, S., Rastogi, P., Gralow, J., Swain, S. M., Winer, E. P., Colon-Otero, G., Davidson, N. E., Mamounas, E., Zujewski, J. A., & Wolmark, N. (2014). Trastuzumab plus adjuvant chemotherapy for human epidermal growth factor receptor 2-positive breast cancer: Planned joint analysis of overall survival from NSABP B-31 and NCCTG N9831. *Journal of Clinical Oncology, 32*(33), 3744–3752. https://doi.org/10.1200/JCO.2014.55.5730 (PMID 25332249; PMCID PMC4226805)
- Reimer, T., Stachs, A., Veselinovic, K., Kühn, T., Heil, J., Polata, S., Marmé, F., Müller, T., Hildebrandt, G., Krug, D., Ataseven, B., Reitsamer, R., Ruth, S., Denkert, C., Bekes, I., Zahm, D.-M., Thill, M., Golatta, M., Holtschmidt, J., . . . Gerber, B. (2025). Axillary surgery in breast cancer—Primary results of the INSEMA trial. *The New England Journal of Medicine, 392*(11), 1051–1064. https://doi.org/10.1056/NEJMoa2412063 (PMID 39665649)
- Labels re-opened via openFDA on 2026-10-29: KEYTRUDA (effective 2026-07-10), KISQALI (2026-07-01), LYNPARZA (2025-07-10), NERLYNX (2026-07-02). https://api.fda.gov/drug/label.json
