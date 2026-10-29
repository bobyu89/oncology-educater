# Sarcoma 2. Bone sarcoma trials, regimens, HD-MTX safety and cisplatin ototoxicity: verified research notes

Handbook: Taiwanese oncology NP handbook (專科護理師), bone sarcoma chapter (ward practice + 專師甄審 exam)
Verification date: 2026-10-29
Scope: osteosarcoma (MAP, EURAMOS-1, histologic response, mifamurtide, relapse regimens, TKIs), Ewing sarcoma (VDC/IE interval compression, EE2012, Euro-EWING 99 BuMel, relapse regimens incl. rEECur), chondrosarcoma (surgery, IDH1/ivosidenib), high-dose methotrexate (HD-MTX) safety protocol, glucarpidase, cisplatin ototoxicity and sodium thiosulfate (STS).

**Method.** Every PMID was pulled from PubMed (NCBI E-utilities efetch, same database as the PubMed MCP tools). Numbers come from the PubMed abstract unless another source is named. When the abstract lacked a number, I checked the PMC full text, then the current US FDA label (openFDA `drug/label`, effective date given), the EMA EPAR / SmPC, ClinicalTrials.gov API v2, and the TFDA licence open-data file (InfoId=36; the CSV inside the zip is dated **2026-10-27**, downloaded 2026-10-29). NCCN Bone Cancer guideline page read 2026-10-29 shows **Version 1.2027** (content behind login; not read). Nothing was filled from memory. Anything still missing is **[UNVERIFIED]**.

**Source tags used inline**
- [A] = PubMed abstract of the cited paper
- [FT] = PMC full text of the cited paper (methods/results unless stated)
- [L-xxx] = current US FDA prescribing information via openFDA (effective date given at first use)
- [EMA] = EMA EPAR web page / SmPC PDF (ema.europa.eu), read 2026-10-29
- [TFDA] = TFDA licence open-data file (InfoId=36, CSV dated 2026-10-27)
- [CT] = ClinicalTrials.gov API v2 record (read 2026-10-29)
- [ASCO-A] = ASCO meeting abstract text (retrieved via Crossref metadata; not in PubMed)
- [PDQ] = NCI PDQ health-professional summary (secondary source; only where flagged)
- **[UNVERIFIED]** = not found in any source I read; do not print without checking

**Section status tags**
- **[VERIFIED]** = citation confirmed on PubMed and the primary-endpoint result (or the dose/fact) confirmed from a primary or official source I opened
- **[PARTIAL]** = citation confirmed, but part of the data is missing from the primary source or comes only from a secondary source
- **[UNVERIFIED]** = could not confirm

**APA 7 notes.** All authors up to 20; for 21 or more, first 19, ". . .", final author. Study-group bylines are omitted. Titles are sentence case from the PubMed record. Year = journal-issue year. Where PubMed shows only an e-locator, pages come from Crossref (stated).

---

## 0. Corrections and flags for the editor (read first)

1. **Mifamurtide (MEPACT) is NO LONGER licensed in Taiwan.** TFDA licence 衛部藥輸字第026319號 (秘配得 凍晶注射劑 4 mg, 台灣武田藥品工業) was issued 2015-02-13 and **cancelled 2023-10-17, reason 自請註銷 (voluntary withdrawal by the licence holder)** [TFDA]. EU: authorised 6 March 2009, renewed 20 Feb 2019; holder is now **Esteve Pharmaceuticals (Barcelona)**, not Takeda [EMA]. USA: **never FDA-approved** (no Drugs@FDA or label record in openFDA; "not been approved for use in the USA" [Marina 2016, FT]; "investigational agent that holds orphan drug status" in the US [Frampton 2010, A]). Do not write that mifamurtide is available in Taiwan.
2. **Two different INT-0133 hazard ratios circulate.** Meyers 2008 JCO: OS HR **0.71** (95% CI 0.52–0.96), 6-year OS 70% → 78%, P = .03 (n = 662) [A]. The EU SmPC: HR **0.72** (0.53–0.97), p = 0.0313 (n = 678) [EMA]. Both are "correct" for their datasets; cite the one you reference. Prescrire (2011) argued the same trial showed **no** OS gain and flagged severe hearing loss 12% vs 7% with mifamurtide [A] — the drug remains controversial.
3. **"Good response" means < 10% viable tumour (= ≥ 90% necrosis).** EURAMOS-1 dichotomised exactly this way, and ~**50%** of patients were good responders [Whelan 2015, A/FT]. Changing post-operative chemotherapy for poor responders (MAPIE) **did not help and added toxicity**; adding pegylated interferon for good responders **did not help** either. **MAP remains standard for both groups** [Marina 2016; Bielack 2015, A].
4. **The cisplatin schedule in "MAP" differed by group inside EURAMOS-1.** COG sites gave cisplatin 60 mg/m²/day as a **4-h infusion on 2 days**; other sites gave **120 mg/m² as a continuous 72-h infusion** [Marina 2016, FT]. Doxorubicin 37.5 mg/m²/day × 2 days was preferably a **48-h continuous infusion** [Whelan 2015, FT; CT]. This matters for STS: **PEDMARK is not established after cisplatin infusions longer than 6 h** [L-PEDMARK].
5. **Single-day cisplatin 120 mg/m² is much more ototoxic than 60 mg/m² × 2 days** in osteosarcoma: any hearing loss 78% (7/9) vs 30% (8/27), P = .019 [Lewis 2009, A].
6. **The US leucovorin label contains TWO different rescue algorithms** with different stop targets: (a) the HD-MTX Table 2 nomogram (stop when MTX < **0.05 µM**; delayed-early → 150 mg IV q3h) and (b) the "impaired elimination / overdose" paragraph (10 mg/m² q6h until MTX < **0.01 µM**; escalate to 100 mg/m² IV q3h) [L-LEUCOVORIN Sagent 2026-06-16]. EURAMOS-1 used 15 mg/m² until MTX < 0.1 µM [Marina 2016, FT]. Tell readers to follow the **protocol in use**, not to mix algorithms.
7. **Glucarpidase is NOT licensed in Taiwan** (no Voraxaze/glucarpidase entry in the TFDA file) [TFDA]; FDA-approved 2012-01-17 (BLA125327) and EU-authorised 11 Jan 2022 [openFDA drugsfda; EMA]. Availability in Taiwan by special import (專案進口) is **[UNVERIFIED]**. Also absent from the TFDA file: **sodium thiosulfate for otoprotection (PEDMARK/Pedmarqsi)**, **dexrazoxane**, **levoleucovorin** [TFDA]. Earlier sodium thiosulfate injections (DETOXOL) were cancelled in 1985 and 2010.
8. **FDA label re-analysis of ACCL0431 is weaker than the Lancet Oncology paper.** Paper (all randomised, assessable): hearing loss 28.6% vs 56.4%, OR 0.31 [A]. FDA label (localised-disease ITT, missing = hearing loss): 44% vs 58%, **RR 0.75 (0.48–1.18), adjusted 0.84 (0.53–1.35)** — not significant [L-PEDMARK 2025-10-27]. SIOPEL-6 also differs: paper 33% vs 63% (RR 0.52) vs label ITT 39% vs 68% (RR 0.58). Quote the source you use.
9. **STS safety signal in metastatic disease.** ACCL0431 disseminated-disease subgroup: 3-year OS **45% vs 84%**, RHR 4.10 (1.30–12.97), log-rank p = 0.009 [Freyer 2017, FT]. This is why the FDA and EU indications are restricted to **localised, non-metastatic** tumours and why the 2020 guideline makes a weak recommendation **against** routine STS in metastatic disease [L-PEDMARK; EMA; Freyer 2020, A].
10. **AYA gap for STS.** The EU indication is 1 month to < 18 years [EMA]; the US label says "pediatric patients 1 month of age and older" [L-PEDMARK]; both trials enrolled ≤ 18 years. Most osteosarcoma patients are 10–19 years (EURAMOS-1 median age 14) [Whelan 2015, FT], but use in 18–39-year-olds is **off-label**. In ACCL0431 the STS effect in the germ cell tumour/osteosarcoma group was OR 0.32 (0.06–1.25), **not significant** [Ohlsen 2025, A].
11. **EE2012 PubMed abstract wording is misleading.** The abstract reads "adjusted HR 0·71 [95% credible interval 0·55–0·92 in favour of group 1)", but group 1 is VIDE and the conclusion is that **group 2 (VDC/IE) is superior** (3-year EFS 67% vs 61%) [A]. Print it as "HR 0.71 favouring VDC/IE".
12. **Womer 2012 abstract unit typo.** The abstract reads "filgrastim (5 mg/kg per day; maximum, 300 mg)". Filgrastim is dosed in **µg**/kg; this is a µ→m rendering error. An erratum exists (J Clin Oncol 2015;33(7):814, PMID 25721580) whose content I could not open. Do not copy the abstract's units.
13. **Euro-EWING 99 R2Loc numbers differ between the paper and PDQ.** Whelan 2018 abstract: 3-year EFS **69.0% vs 56.7%** (BuMel vs VAI) [A]. PDQ quotes 66.9% vs 53.1% [PDQ]. Use the paper.
14. **rEECur has no full peer-reviewed paper on PubMed as of 2026-10-29.** Data exist only as ASCO abstracts (2019, 2020, 2022 LBA2) and reviews. The 2022 abstract gives median EFS **TC 3.7 mo vs high-dose ifosfamide 5.7 mo** [ASCO-A]; the Strauss 2024 review table prints TC 3.5 mo (2.1–5.1) [FT]. Flag as conference data.
15. **Ivosidenib has no chondrosarcoma indication anywhere I checked** (FDA label 2025-12-22: AML, MDS, cholangiocarcinoma; TFDA licence 衛部藥輸字第028815號 issued 2024-10-23: AML, MDS, cholangiocarcinoma). The phase 3 **CHONQUER** (NCT06127407, ivosidenib vs placebo) is **recruiting** (est. primary completion 2028-02) [CT].
16. **Regorafenib and cabozantinib are off-label for bone sarcoma in Taiwan** (TFDA indications: regorafenib = CRC, GIST, HCC; cabozantinib = RCC, HCC, DTC, NET) [TFDA]. Topotecan, irinotecan and temozolomide also have **no sarcoma indication** in Taiwan; ifosfamide **does** list 骨肉瘤 and 軟骨肉瘤 [TFDA].
17. **Errata exist:** Bielack 2015 JCO (Figure 1 printed cisplatin "120 g/m²" and doxorubicin "75 g/m²"; should be mg/m²) [erratum FT, PMID 29236598]; Womer 2012 JCO (PMID 25721580, content not read); Freyer 2017 Lancet Oncol (PMID 28593857, content not read).

---

# A. OSTEOSARCOMA

## 1. MAP backbone (EURAMOS-1 schedule) — [VERIFIED]

**Sources:** Marina 2016 [FT]; Whelan 2015 [A/FT]; Smeland 2019 [FT]; ClinicalTrials.gov NCT00134030 [CT]; methotrexate label [L-METHOTREXATE Accord 2026-09-04].

| Drug | Dose per cycle | How given in EURAMOS-1 | Weeks (pre-op) |
|---|---|---|---|
| Cisplatin (P) | **120 mg/m²** | COG: **60 mg/m²/day, 4-h infusion, days 1–2**; other groups: **continuous 72-h infusion** [FT]; "either 72-h infusion or two 4-h infusions on separate days" [Whelan FT] | 1 and 6 |
| Doxorubicin (A) | **75 mg/m²** | **37.5 mg/m²/day on days 1–2**; preferred **48-h infusion** [Marina FT; Whelan FT; CT] | 1 and 6 |
| HD methotrexate (M) | **12 g/m²** (COG max **20 g**) | **IV over 4 h**, with hyperhydration, alkalinisation, leucovorin [Marina FT] | 4, 5, 9, 10 |

- **Pre-operative:** two 5-week MAP cycles (10 weeks), then surgery (median 82 days from start of chemo) [Whelan FT]. Pre-op targets: doxorubicin 150 mg/m², cisplatin 240 mg/m², MTX 48 g/m² [Whelan FT].
- **Post-operative MAP:** two more MAP cycles + two MA cycles (cisplatin stops at **cumulative 480 mg/m²**); total **29 weeks** [Marina FT]. Post-op targets: MTX 96 g/m², doxorubicin 300 mg/m², cisplatin 240 mg/m² [Marina FT table]. So whole-course cumulative: **cisplatin 480 mg/m², doxorubicin 450 mg/m², MTX 144 g/m²** (sum of pre- and post-op targets) [FT].
- **Count thresholds to start a cycle:** myelosuppressive cycles (AP) ANC ≥ 750/µL and platelets ≥ 75,000/µL; **HD-MTX only needs ANC ≥ 250/µL and platelets ≥ 50,000/µL** [Marina FT]. Registration needed GFR ≥ 70 mL/min/1.73 m², LVEF ≥ 50% or SF ≥ 28% [Whelan FT].
- **Leucovorin in EURAMOS-1:** 15 mg/m², started at 24 h (Whelan) / "24–48 h" (Marina) from the MTX start, continued until MTX < 0.1 µM, adjusted by nomogram [FT].
- **Dexrazoxane:** allowed at investigator discretion; "withdrawn by the European Medicines Agency in 2011" for this use in Europe [Whelan FT]. Not licensed in Taiwan [TFDA].
- **US label:** "typically 12 g/m² (maximum 20 g/dose) as an IV infusion over 4 hours" for osteosarcoma [L-METHOTREXATE].
- **Pre-op toxicity (2260 patients):** grade 3–4 neutropenia 83%, infective complications 58%, thrombocytopenia 50%, mucositis 27%; 3 treatment-related deaths (2 infection, **1 toxic epidermal necrolysis from MTX**) [Whelan FT]. Amputation/rotationplasty 17% [FT].

## 2. EURAMOS-1 — design and pre-randomisation results — [VERIFIED]

**Reference**
- Whelan, J. S., Bielack, S. S., Marina, N., Smeland, S., Jovic, G., Hook, J. M., Krailo, M., Anninga, J., Butterfass-Bahloul, T., Böhling, T., Calaminus, G., Capra, M., Deffenbaugh, C., Dhooge, C., Eriksson, M., Flanagan, A. M., Gelderblom, H., Goorin, A., Gorlick, R., . . . Bernstein, M. (2015). EURAMOS-1, an international randomised study for osteosarcoma: Results from pre-randomisation treatment. *Annals of Oncology*, *26*(2), 407–414. https://doi.org/10.1093/annonc/mdu526 — PMID 25421877

**Design:** International collaboration of COG, COSS, EOI and SSG; registration at diagnosis, age ≤ 40, resectable localised or metastatic high-grade osteosarcoma; post-surgery randomisation by histologic response (NCT00134030, ISRCTN 67613327) [A].
**Numbers:** 2260 patients, 326 centres, 17 countries, April 2005–June 2011; 1334 (59%) randomised; 94% completed pre-op chemo; **50% had ≥ 90% necrosis** [A]. (Marina 2016 says 325 sites — minor discrepancy.)
**Why randomisation was low:** absent consent (18%), progression before surgery (8%), late histology (4%) [FT].

## 3. EURAMOS-1 Good Response: MAP ± pegylated interferon alfa-2b — [VERIFIED]

**Reference**
- Bielack, S. S., Smeland, S., Whelan, J. S., Marina, N., Jovic, G., Hook, J. M., Krailo, M. D., Gebhardt, M., Pápai, Z., Meyer, J., Nadel, H., Randall, R. L., Deffenbaugh, C., Nagarajan, R., Brennan, B., Letson, G. D., Teot, L. A., Goorin, A., Baumhoer, D., . . . Bernstein, M. (2015). Methotrexate, doxorubicin, and cisplatin (MAP) plus maintenance pegylated interferon alfa-2b versus MAP alone in patients with resectable high-grade osteosarcoma and good histologic response to preoperative MAP: First results of the EURAMOS-1 good response randomized controlled trial. *Journal of Clinical Oncology*, *33*(20), 2279–2287. https://doi.org/10.1200/JCO.2014.60.0734 — PMID 26033801. **Erratum:** *J Clin Oncol 34*(33), 4059 (2016), PMID 29236598 (dose-unit typos in Figure 1 only).

**Design:** Phase 3, open-label, randomised 1:1 [PubMed type; A].
**Population:** Good responders (< 10% viable tumour), age ≥ 5 (interferon toxicity concern) [A; Whelan FT].
**Arms:** 4 post-op MAP cycles (n = 359) vs same + **pegylated IFN-α-2b 0.5 µg/kg/week SC (max 50 µg) × 4 weeks, then 1.0 µg/kg/week (max 100 µg)**, weeks 30–104 (n = 357) [A/FT].
**Primary endpoint (EFS):** median follow-up 44 months; 3-year EFS 74% (MAP) vs 77% (MAP + IFN); **HR 0.83 (95% CI 0.61–1.12), P = .214** [A/FT].
**OS:** 84 deaths; HR 0.77 (0.50–1.19); 5-year OS 81% vs 84% [FT].
**Adherence problem:** 23% never started IFN (mostly refusal); of 271 who started, 105 stopped early (toxicity 45% of these); median IFN duration 67 weeks; grade ≥ 3 toxicity in 133/268 [A/FT].
**Teaching point:** a negative trial; MAP alone stays standard for good responders.

## 4. EURAMOS-1 Poor Response: MAP vs MAPIE — [VERIFIED]

**Reference**
- Marina, N. M., Smeland, S., Bielack, S. S., Bernstein, M., Jovic, G., Krailo, M. D., Hook, J. M., Arndt, C., van den Berg, H., Brennan, B., Brichard, B., Brown, K. L. B., Butterfass-Bahloul, T., Calaminus, G., Daldrup-Link, H. E., Eriksson, M., Gebhardt, M. C., Gelderblom, H., Gerss, J., . . . Whelan, J. S. (2016). Comparison of MAPIE versus MAP in patients with a poor response to preoperative chemotherapy for newly diagnosed high-grade osteosarcoma (EURAMOS-1): An open-label, international, randomised controlled trial. *The Lancet Oncology*, *17*(10), 1396–1408. https://doi.org/10.1016/S1470-2045(16)30214-5 — PMID 27569442

**Design:** Phase 3, open-label, randomised 1:1; stratified by group, site, metastases [A].
**Population:** Poor responders (≥ 10% viable tumour), age ≤ 40 [A].
**Arms:** MAP (n = 310) vs **MAPIE** (n = 308) = MAP + **high-dose ifosfamide 14 g/m² (2.8 g/m²/day × 5, equidose mesna) + etoposide 100 mg/m²/day × 5** (3 post-op IE cycles), plus 2 "Ai" cycles of ifosfamide 3 g/m²/day × 3 (9 g/m²) with doxorubicin [A/FT]. Treatment length 40 vs 29 weeks [FT].
**Primary endpoint (EFS):** median follow-up 62.1 months; 307 events; **HR 0.98 (95% CI 0.78–1.23)**, hazards non-proportional (p = 0.0003); 3-year EFS **55% vs 53%**; RMST difference 0.8 months (p = 0.69) [A/FT].
**OS:** 193 deaths; HR 0.97 (0.73–1.29); 3-year OS 72% vs 77% (immature) [FT].
**Toxicity (MAP vs MAPIE):** grade 4 non-haematological 12% vs **24%**; febrile neutropenia without documented infection 50% vs **73%**; thrombocytopenia 78% vs 83%; discontinued for toxicity 3 vs 16 patients; **second malignancies 3 vs 10** (mostly MDS/AML; cause-specific HR 3.24, p = 0.079) [A/FT]. One MAP SUSAR: **bone-marrow infarction due to methotrexate** [A].
**Teaching point:** intensifying post-op chemo for poor responders adds toxicity and secondary leukaemia risk without benefit — continue MAP.

## 5. Histologic response (≥ 90% necrosis) as a prognostic factor — [VERIFIED]

**References**
- Smeland, S., Bielack, S. S., Whelan, J., Bernstein, M., Hogendoorn, P., Krailo, M. D., Gorlick, R., Janeway, K. A., Ingleby, F. C., Anninga, J., Antal, I., Arndt, C., Brown, K. L. B., Butterfass-Bahloul, T., Calaminus, G., Capra, M., Dhooge, C., Eriksson, M., Flanagan, A. M., . . . Marina, N. (2019). Survival and prognosis with osteosarcoma: Outcomes in more than 2000 patients in the EURAMOS-1 (European and American Osteosarcoma Study) cohort. *European Journal of Cancer*, *109*, 36–50. https://doi.org/10.1016/j.ejca.2018.11.027 — PMID 30685685
- Bielack, S. S., Kempf-Bielack, B., Delling, G., Exner, G. U., Flege, S., Helmke, K., Kotz, R., Salzer-Kuntschik, M., Werner, M., Winkelmann, W., Zoubek, A., Jürgens, H., & Winkler, K. (2002). Prognostic factors in high-grade osteosarcoma of the extremities or trunk: An analysis of 1,702 patients treated on neoadjuvant Cooperative Osteosarcoma Study Group protocols. *Journal of Clinical Oncology*, *20*(3), 776–790. https://doi.org/10.1200/JCO.2002.20.3.776 — PMID 11821461
- Bacci, G., Mercuri, M., Longhi, A., Ferrari, S., Bertoni, F., Versari, M., & Picci, P. (2005). Grade of chemotherapy-induced necrosis as a predictor of local and systemic control in 881 patients with non-metastatic osteosarcoma of the extremities treated with neoadjuvant chemotherapy in a single institution. *European Journal of Cancer*, *41*(14), 2079–2085. https://doi.org/10.1016/j.ejca.2005.03.036 — PMID 16115755

| Study | n | Good vs poor responders |
|---|---|---|
| COSS (Bielack 2002) | 1,702 | Actuarial **10-year OS 73.4% vs 47.2%** (P < .0001); histologic response and surgical remission were the key independent factors [A] |
| Rizzoli (Bacci 2005) | 881 (M0 extremity) | **5-year DFS 67.9% vs 51.3%; 5-year OS 78.4% vs 63.7%** (both P < .0001); prognostic value seen only in osteoblastic and telangiectatic subtypes [A] |
| EURAMOS-1 (Smeland 2019) | 1,395 (M0, complete surgical remission) | Poor response **EFS HR 2.13 (95% CI 1.76–2.58)** after surgery [A/FT] |

**Other EURAMOS-1 cohort numbers (Smeland 2019):** all registered: 3-/5-year EFS 59%/54%, 5-year OS 71%; localised 5-year EFS 60%, OS 76%; metastatic 5-year EFS 28%, OS 45%. Adverse factors at diagnosis: pulmonary metastases HR 2.34, non-pulmonary metastases HR 1.94, axial site HR 1.53 [A/FT].
**Other notes:** the old COSS analysis also found 10-year survival of patients ≥ 40 years 41.6% vs 60.2% [A]. Huvos grading (grade III/IV = ≥ 90% necrosis) is the common pathology vocabulary, but I did **not** verify the grade definitions here — **[UNVERIFIED]**.

## 6. Mifamurtide (L-MTP-PE) and INT-0133 — [VERIFIED trial]; regulatory status [VERIFIED EU/Taiwan; PARTIAL USA]

**References**
- Meyers, P. A., Schwartz, C. L., Krailo, M., Kleinerman, E. S., Betcher, D., Bernstein, M. L., Conrad, E., Ferguson, W., Gebhardt, M., Goorin, A. M., Harris, M. B., Healey, J., Huvos, A., Link, M., Montebello, J., Nadel, H., Nieder, M., Sato, J., Siegal, G., . . . Grier, H. (2005). Osteosarcoma: A randomized, prospective trial of the addition of ifosfamide and/or muramyl tripeptide to cisplatin, doxorubicin, and high-dose methotrexate. *Journal of Clinical Oncology*, *23*(9), 2004–2011. https://doi.org/10.1200/JCO.2005.06.031 — PMID 15774791
- Meyers, P. A., Schwartz, C. L., Krailo, M. D., Healey, J. H., Bernstein, M. L., Betcher, D., Ferguson, W. S., Gebhardt, M. C., Goorin, A. M., Harris, M., Kleinerman, E., Link, M. P., Nadel, H., Nieder, M., Siegal, G. P., Weiner, M. A., Wells, R. J., Womer, R. B., & Grier, H. E. (2008). Osteosarcoma: The addition of muramyl tripeptide to chemotherapy improves overall survival--a report from the Children's Oncology Group. *Journal of Clinical Oncology*, *26*(4), 633–638. https://doi.org/10.1200/JCO.2008.14.0095 — PMID 18235123
- Palmerini, E., Meazza, C., Tamburini, A., Márquez-Vega, C., Bisogno, G., Fagioli, F., Ferraresi, V., Milano, G. M., Coccoli, L., Rubio-San-Simón, A., Gallego, O., Llinares Riestra, M. E., Manzitti, C., Mora, J., Vaz-Salgado, M. Á., Luksch, R., Mata, C., Pierini, M., Carretta, E., . . . Broto, J. M. (2025). Is there a role for mifamurtide in nonmetastatic high-grade osteosarcoma? Results from the Italian Sarcoma Group (ISG/OS-2) and Spanish Sarcoma Group (GEIS-33) trials. *Journal of Clinical Oncology*, *43*(28), 3113–3122. https://doi.org/10.1200/JCO-25-00210 — PMID 40825172
- Frampton, J. E. (2010). Mifamurtide: A review of its use in the treatment of osteosarcoma. *Paediatric Drugs*, *12*(3), 141–153. https://doi.org/10.2165/11204910-000000000-00000 — PMID 20481644
- Mifamurtide: Osteosarcoma: Ineffective and harmful. (2011). *Prescrire International*, *20*(115), 89. — PMID 21648206 (no DOI; unsigned editorial)

**INT-0133 design:** Phase 3, COG, 2 × 2 factorial: MAP ± ifosfamide (pre/post-op) × ± MTP post-op; identical cumulative cisplatin/doxorubicin/HD-MTX in all arms; non-metastatic resectable osteosarcoma [A].
**2005 report (n = 677):** factorial analysis not possible because of an **interaction** between ifosfamide and MTP; 3-year EFS: standard 71%, +MTP 68%, +ifosfamide 61%, +both 78% [A].
**2008 report (n = 662):** no interaction on longer follow-up; ifosfamide added nothing; **MTP improved 6-year OS 70% → 78% (P = .03), HR 0.71 (0.52–0.96)**; EFS trend only (P = .08) [A].
**Dose (EU SmPC):** **2 mg/m² IV over 1 hour, twice weekly (≥ 3 days apart) × 12 weeks, then weekly × 24 weeks = 48 infusions in 36 weeks**, after resection, with post-op multi-agent chemo [EMA SmPC]. Not to be given as a bolus [EMA].
**Interactions/contraindications (SmPC):** contraindicated with **ciclosporin/calcineurin inhibitors** and **high-dose NSAIDs** (block macrophage activation); separate administration times from **doxorubicin or other lipophilic drugs** [EMA SmPC].
**Common reactions:** chills 89%, fever 85%, fatigue 53% (manage with paracetamol) [EMA SmPC].
**Regulatory status:**
- **EU:** indicated for high-grade resectable non-metastatic osteosarcoma after macroscopically complete resection, ages 2–30 at diagnosis; orphan designation 21 June 2004; authorised **6 March 2009**; latest renewal 20 Feb 2019; holder **Esteve Pharmaceuticals, S.A.** [EMA]. — [VERIFIED]
- **USA:** not approved [Marina 2016 FT; Frampton 2010 A; no openFDA label/Drugs@FDA record]. The 2007 FDA advisory-committee history is **[UNVERIFIED]** (not read). — [PARTIAL]
- **Taiwan:** licence 衛部藥輸字第026319號 issued 2015-02-13, **cancelled 2023-10-17 (自請註銷)** [TFDA]. — [VERIFIED]

**Newer data (Palmerini 2025, ISG/OS-2 + GEIS-33, merged, 398 patients):** mifamurtide given only to **P-glycoprotein-positive** patients (53% of tumours); 5-year EFS 71.4% with mifamurtide vs 58.3% without (P = .0139), **not confirmed on multivariable analysis (P = .0593)**; overall 5-year EFS 65.2%, OS 74.8% [A]. Observational/non-randomised comparison.

## 7. Relapsed / refractory osteosarcoma

### 7a. Ifosfamide + etoposide — [VERIFIED trial; PARTIAL as relapse evidence]

- Goorin, A. M., Harris, M. B., Bernstein, M., Ferguson, W., Devidas, M., Siegal, G. P., Gebhardt, M. C., Schwartz, C. L., Link, M., & Grier, H. E. (2002). Phase II/III trial of etoposide and high-dose ifosfamide in newly diagnosed metastatic osteosarcoma: A Pediatric Oncology Group trial. *Journal of Clinical Oncology*, *20*(2), 426–433. https://doi.org/10.1200/JCO.2002.20.2.426 — PMID 11786570

**Caution:** this is the standard dose reference for IE, but the population was **newly diagnosed metastatic** (window therapy), not relapsed [A].
**Regimen:** **ifosfamide 3.5 g/m²/day + etoposide 100 mg/m²/day × 5 days**, G-CSF from day 6, repeated at 3 weeks [A].
**Results:** 43 patients; ORR **59%** (CR 10%, PR 49%); 2-year PFS 39% (lung-only) and 58% (bone ± lung) [A].
**Toxicity:** grade 4 neutropenia 83%, grade 4 thrombocytopenia 29%, sepsis 24%, **Fanconi syndrome in 5 patients**, 2 toxic deaths [A].

### 7b. Gemcitabine + docetaxel — [VERIFIED]

- Navid, F., Willert, J. R., McCarville, M. B., Furman, W., Watkins, A., Roberts, W., & Daw, N. C. (2008). Combination of gemcitabine and docetaxel in the treatment of children and young adults with refractory bone sarcoma. *Cancer*, *113*(2), 419–425. https://doi.org/10.1002/cncr.23586 — PMID 18484657
- Palmerini, E., Jones, R. L., Marchesi, E., Paioli, A., Cesari, M., Longhi, A., Meazza, C., Coccoli, L., Fagioli, F., Asaftei, S., Grignani, G., Tamburini, A., Pollack, S. M., Picci, P., & Ferrari, S. (2016). Gemcitabine and docetaxel in relapsed and unresectable high-grade osteosarcoma and spindle cell sarcoma of bone. *BMC Cancer*, *16*, Article 280. https://doi.org/10.1186/s12885-016-2312-3 — PMID 27098543

| Series | Regimen | Result |
|---|---|---|
| Navid 2008 (St Jude, retrospective, 22 pts, 17 osteosarcoma) | **Gemcitabine 675 mg/m² IV d1 + d8; docetaxel 75–100 mg/m² IV d8** | ORR 29% (of 14 evaluable); 3 PR in osteosarcoma; median duration of response/SD 4.8 mo; toxicity mainly thrombocytopenia/neutropenia [A] |
| Palmerini 2016 (Rizzoli, retrospective, 51 pts) | **Gemcitabine 900 mg/m² d1 + d8; docetaxel 75 mg/m² d8; q21d** | 4-month PFS 46% (primary end-point); PR 13%, SD 43%; median PFS 3.5 mo; 1-year OS 30%; 4-month PFS 56% in osteosarcoma vs 18% in spindle-cell sarcoma of bone; grade 4 neutropenia 21% [A/FT] |

### 7c. Regorafenib — REGOBONE (osteosarcoma cohort) — [VERIFIED]

- Duffaud, F., Mir, O., Boudou-Rouquette, P., Piperno-Neumann, S., Penel, N., Bompas, E., Delcambre, C., Kalbacher, E., Italiano, A., Collard, O., Chevreau, C., Saada, E., Isambert, N., Delaye, J., Schiffler, C., Bouvier, C., Vidal, V., Chabaud, S., & Blay, J.-Y. (2019). Efficacy and safety of regorafenib in adult patients with metastatic osteosarcoma: A non-comparative, randomised, double-blind, placebo-controlled, phase 2 study. *The Lancet Oncology*, *20*(1), 120–133. https://doi.org/10.1016/S1470-2045(18)30742-3 — PMID 30477937

**Design:** Phase 2, non-comparative, randomised 2:1, double-blind, placebo-controlled; French Sarcoma Group; crossover allowed (NCT02389244) [A].
**Population:** Age ≥ 10 (enrolled 43 adults), progression after 1–2 lines for metastatic disease, ECOG 0–1 [A].
**Arms:** **Regorafenib 160 mg/day, days 1–21 of 28** + BSC vs placebo + BSC [A]. (Children ≥ 10 y with BSA ≥ 1.30 m²: 82 mg/m²/day per registry [CT].)
**Primary endpoint (non-progression at 8 weeks):** **17/26 (65%; one-sided 95% CI lower bound 47%) vs 0/12** [A].
**Toxicity (regorafenib):** grade ≥ 3 hypertension 24%, hand-foot skin reaction 10%, fatigue 10%, hypophosphataemia 10%, chest pain 10%; treatment-related SAEs in 24% [A]. Median PFS: **[UNVERIFIED]** (not in abstract; no PMC full text).

### 7d. Regorafenib — SARC024 (osteosarcoma cohort) — [VERIFIED]

- Davis, L. E., Bolejack, V., Ryan, C. W., Ganjoo, K. N., Loggers, E. T., Chawla, S., Agulnik, M., Livingston, M. B., Reed, D., Keedy, V., Rushing, D., Okuno, S., Reinke, D. K., Riedel, R. F., Attia, S., Mascarenhas, L., & Maki, R. G. (2019). Randomized double-blind phase II study of regorafenib in patients with metastatic osteosarcoma. *Journal of Clinical Oncology*, *37*(16), 1424–1431. https://doi.org/10.1200/JCO.18.02374 — PMID 31013172

**Design:** Phase 2, randomised 1:1, double-blind, placebo-controlled, crossover at progression; stopped early after DSMB review [A].
**Population:** 42 patients, progressive metastatic osteosarcoma, measurable disease, ≥ 1 prior line (mean 2.3), median age 37 [A].
**Dose:** 160 mg PO days 1–21 of 28 — stated for the SARC024 Ewing cohort (Attia 2023, A); the osteosarcoma abstract does not state it — [PARTIAL].
**Primary endpoint (PFS):** **3.6 mo (95% CI 2.0–7.6) vs 1.7 mo (1.2–1.8); HR 0.42 (0.21–0.85), P = .017** [A]. OS: no significant difference (crossover) [A].
**Toxicity:** 14/22 (64%) grade 3–4 treatment-related events, including one grade 4 colonic perforation [A].

### 7e. Cabozantinib — CABONE — [VERIFIED]

- Italiano, A., Mir, O., Mathoulin-Pelissier, S., Penel, N., Piperno-Neumann, S., Bompas, E., Chevreau, C., Duffaud, F., Entz-Werlé, N., Saada, E., Ray-Coquard, I., Lervat, C., Gaspar, N., Marec-Berard, P., Pacquement, H., Wright, J., Toulmonde, M., Bessede, A., Crombe, A., . . . Blay, J.-Y. (2020). Cabozantinib in patients with advanced Ewing sarcoma or osteosarcoma (CABONE): A multicentre, single-arm, phase 2 trial. *The Lancet Oncology*, *21*(3), 446–455. https://doi.org/10.1016/S1470-2045(19)30825-3 — PMID 32078813

**Design:** Phase 2, single-arm, two-stage, French Sarcoma Group (NCT02243605) [A].
**Dose:** **Adults 60 mg PO daily; children < 16 y 40 mg/m² daily**, 28-day cycles [A].
**Population:** 90 patients (45 Ewing, 45 osteosarcoma), age ≥ 12, ECOG 0–1, documented progression [A].
**Primary endpoints:**
- Osteosarcoma (dual): **6-month ORR 12% (5/42; 95% CI 4–26), 6-month non-progression 33% (14/42; 20–50)** [A].
- Ewing: **6-month ORR 26% (10/39; 13–42)**, all PR [A].
**Toxicity:** grade 3–4 hypophosphataemia (11% Ewing, 7% osteosarcoma), AST rise, palmar-plantar syndrome, **pneumothorax (2% Ewing, 9% osteosarcoma)**, neutropenia; SAEs in 68%; no drug-related deaths [A].
**Nursing point:** pneumothorax with anti-angiogenic TKIs in patients with lung metastases — teach chest pain/dyspnoea reporting.

---

# B. EWING SARCOMA

## 8. INT-0091: adding IE to VDC-A (background) — [VERIFIED]

- Grier, H. E., Krailo, M. D., Tarbell, N. J., Link, M. P., Fryer, C. J. H., Pritchard, D. J., Gebhardt, M. C., Dickman, P. S., Perlman, E. J., Meyers, P. A., Donaldson, S. S., Moore, S., Rausen, A. R., Vietti, T. J., & Miser, J. S. (2003). Addition of ifosfamide and etoposide to standard chemotherapy for Ewing's sarcoma and primitive neuroectodermal tumor of bone. *The New England Journal of Medicine*, *348*(8), 694–701. https://doi.org/10.1056/NEJMoa020890 — PMID 12594313

**Arms:** 49 weeks of doxorubicin, vincristine, cyclophosphamide, dactinomycin vs the same alternating with ifosfamide + etoposide; age ≤ 30 [A].
**Result:** Non-metastatic (n = 398): **5-year EFS 69% vs 54% (P = .005); OS 72% vs 61% (P = .01)**. Metastatic (n = 120): no difference (P = .81) [A].

## 9. AEWS0031: interval-compressed VDC/IE (every 2 vs every 3 weeks) — [VERIFIED]

- Womer, R. B., West, D. C., Krailo, M. D., Dickman, P. S., Pawel, B. R., Grier, H. E., Marcus, K., Sailer, S., Healey, J. H., Dormans, J. P., & Weiss, A. R. (2012). Randomized controlled trial of interval-compressed chemotherapy for the treatment of localized Ewing sarcoma: A report from the Children's Oncology Group. *Journal of Clinical Oncology*, *30*(33), 4148–4154. https://doi.org/10.1200/JCO.2011.41.5703 — PMID 23091096. **Erratum:** *J Clin Oncol 33*(7), 814 (2015), PMID 25721580 (content not read).
- (Long-term) Cash, T., Krailo, M. D., Buxton, A. B., Pawel, B. R., Healey, J. H., Binitie, O., Marcus, K. J., Grier, H. E., Grohar, P. J., Reed, D. R., Weiss, A. R., Gorlick, R., Janeway, K. A., DuBois, S. G., & Womer, R. B. (2023). Long-term outcomes in patients with localized Ewing sarcoma treated with interval-compressed chemotherapy on Children's Oncology Group study AEWS0031. *Journal of Clinical Oncology*, *41*(30), 4724–4728. https://doi.org/10.1200/JCO.23.00053 — PMID 37651654

**Design:** Phase 3 (registry: PHASE3), randomised; age < 50, localised extradural Ewing sarcoma (NCT00006734) [A; CT].
**Arms:** Same drugs, cycles started every **14 days (intensified)** vs **21 days (standard)** if ANC > 750/µL and platelets > 75,000/µL; 14 cycles; local control at week 13 (after 6 vs 4 cycles) [A].
**Per-cycle doses (abstract):** **VDC = vincristine 2 mg/m², doxorubicin 75 mg/m², cyclophosphamide 1.2 g/m²; IE = ifosfamide 9 g/m², etoposide 500 mg/m²** per cycle; filgrastim between cycles (abstract units garbled — see flag 12) [A].
- Per-day split (ifosfamide **1.8 g/m²/day × 5**) is stated by [PDQ] only — [PARTIAL]. Etoposide 100 mg/m²/day × 5, vincristine 2-mg cap and doxorubicin → dactinomycin switch after a cumulative doxorubicin limit: **[UNVERIFIED]** (JCO full text not available in PMC).
**Primary endpoint (EFS):** n = 568 eligible (284 per arm); actual median interval 15 vs 21 days; **5-year EFS 73% vs 65% (P = .048)**; toxicity similar [A].
**Long-term (Cash 2023):** **10-year EFS 70% vs 61% (P = .03); 10-year OS 76% vs 69% (P = .04)**; no increase in second malignancies; greater benefit when tumour volume ≥ 200 mL [A].

## 10. EURO EWING 2012 (EE2012): VDC/IE vs VIDE — [VERIFIED for EFS; PARTIAL for OS]

- Brennan, B., Kirton, L., Marec-Bérard, P., Gaspar, N., Laurence, V., Martín-Broto, J., Sastre, A., Gelderblom, H., Owens, C., Fenwick, N., Strauss, S., Moroz, V., Whelan, J., & Wheatley, K. (2022). Comparison of two chemotherapy regimens in patients with newly diagnosed Ewing sarcoma (EE2012): An open-label, randomised, phase 3 trial. *The Lancet*, *400*(10362), 1513–1521. https://doi.org/10.1016/S0140-6736(22)01790-1 — PMID 36522207
- (R2, zoledronic acid) Brennan, B., Kirton, L., Marec-Bérard, P., Gaspar, N., Laurence, V., Martín-Broto, J., Gelderblom, H., Owens, C., Anderton, J., Strauss, S. J., Wingrove, J., Moroz, V., Whelan, J., Hjalgrim, L. L., Wheatley, K., & Gaunt, P. (2026). Addition of zoledronic acid to consolidation chemotherapy in Ewing sarcoma-EURO EWING 2012 (EE2012): An international, open-label, randomised controlled phase III trial. *British Journal of Cancer*, *134*(10), 1393–1402. https://doi.org/10.1038/s41416-026-03367-4 — PMID 41832299 (PubMed lists the first author as "Bernadette B"; name order corrected here.)

**Design:** Phase 3, open-label, randomised 1:1, Bayesian design, 10 countries; age 2–49, any stage (extrapulmonary metastases allowed from protocol v3.0, Sept 2016) [A].
**Arms:**
- Group 1 (European): **VIDE** induction (vincristine, ifosfamide, doxorubicin, etoposide) → consolidation VAI/VAC or busulfan-melphalan [A].
- Group 2 (US): **interval-compressed VDC/IE** induction → consolidation VC/IE or VAI, or busulfan-melphalan [A].
- Per-day VIDE doses: **[UNVERIFIED]** (Lancet not in PMC).
**Primary endpoint (EFS):** 640 patients (320 per arm), median follow-up 47 months; **3-year EFS 61% (VIDE) vs 67% (VDC/IE); adjusted HR 0.71 (95% credible interval 0.55–0.92)**; probability true HR < 1 > 0.99 [A] (see flag 11).
**OS:** HR 0.62 favouring VDC/IE per [PDQ] only — [PARTIAL].
**Toxicity (VIDE vs VDC/IE):** grade 3–5 febrile neutropenia **74% vs 58%**; ≥ 1 platelet transfusion 64% vs 43%; red-cell transfusion 87% vs 89% [A].
**Conclusion:** VDC/IE is "more effective, less toxic, and shorter" and the new standard for all stages [A].
**R2 (zoledronic acid):** 272 patients; 3-year EFS 59% vs 57%, HR 0.92 (0.64–1.31); 3-year OS 75% both — **no benefit** [A].

## 11. Euro-EWING 99 R2Loc: busulfan-melphalan (BuMel) vs VAI — [VERIFIED]

- Whelan, J., Le Deley, M.-C., Dirksen, U., Le Teuff, G., Brennan, B., Gaspar, N., Hawkins, D. S., Amler, S., Bauer, S., Bielack, S., Blay, J.-Y., Burdach, S., Castex, M.-P., Dilloo, D., Eggert, A., Gelderblom, H., Gentet, J.-C., Hartmann, W., Hassenpflug, W.-A., . . . Oberlin, O. (2018). High-dose chemotherapy and blood autologous stem-cell rescue compared with standard chemotherapy in localized high-risk Ewing sarcoma: Results of Euro-E.W.I.N.G.99 and Ewing-2008. *Journal of Clinical Oncology*, *36*(31), 3110–3119. https://doi.org/10.1200/JCO.2018.78.2516 — PMID 30188789 (pages from Crossref; PubMed shows e-locator only)
- (R2Pulm) Dirksen, U., Brennan, B., Le Deley, M.-C., Cozic, N., van den Berg, H., Bhadri, V., Brichard, B., Claude, L., Craft, A., Amler, S., Gaspar, N., Gelderblom, H., Goldsby, R., Gorlick, R., Grier, H. E., Guinbretiere, J.-M., Hauser, P., Hjorth, L., Janeway, K., . . . Hawkins, D. S. (2019). High-dose chemotherapy compared with standard chemotherapy and lung radiation in Ewing sarcoma with pulmonary metastases: Results of the European Ewing Tumour Working Initiative of National Groups, 99 trial and EWING 2008. *Journal of Clinical Oncology*, *37*(34), 3192–3202. https://doi.org/10.1200/JCO.19.00915 — PMID 31553693
- (Whole cohort) Valentin, T., Winter, S., Dirksen, U., Hawkins, D. S., Gelderblom, H., Risbourg, S., Berlanga, P., Gaspar, N., Janeway, K. A., Juergens, H., Kirchberg, I. E., Ladenstein, R., Laurence, V., Le Deley, M.-C., McCabe, M. G., Merks, H., Ranft, A., Strauss, S., Van De Sande, M. A. J., . . . Brennan, B. (2026). Long-term analysis of patients with Ewing sarcoma included in the Euro-EWING99 study. *Journal of Clinical Oncology*. Advance online publication. https://doi.org/10.1200/JCO-25-02516 — PMID 42537000

**R2Loc design:** randomised; age < 50, localised high-risk: **poor histologic response (≥ 10% viable cells) after 6 VIDE**, or tumour volume ≥ 200 mL (unresected / initially resected / resected after RT) [A].
**Arms:** **BuMel + autologous stem-cell rescue (n = 122) vs 7 courses VAI (vincristine, dactinomycin, ifosfamide) (n = 118)**; 78% entered for poor histologic response; median age 17.1; median follow-up 7.8 years [A]. Bu/Mel doses: **[UNVERIFIED]** (full text not in PMC).
**Primary endpoint (EFS):** **HR 0.64 (95% CI 0.43–0.95), P = .026; 3-year EFS 69.0% vs 56.7%; 8-year 60.7% vs 47.1%** [A].
**OS:** HR 0.63 (0.41–0.95), P = .028; 3-year 78.0% vs 72.2%; 8-year 64.5% vs 55.6% [A].
**Toxicity:** 2 BuMel-related deaths vs 1 after standard chemo; more severe acute toxicity with BuMel [A].
**R2Pulm (Dirksen 2019, lung/pleural metastases only, n = 287):** BuMel vs VAI + whole-lung irradiation: 3-year EFS 56.6% vs 50.6%; **HR 0.79 (0.56–1.10), P = .16; OS HR 1.00**; 4 BuMel toxic deaths — **no clear benefit** [A].
**Whole-cohort (Valentin 2026, n = 3,395):** 5-year PFS 66.7% (localised), 42.0% (pleuropulmonary metastases), 21.8% (extrapulmonary metastases); 5-year OS 64.6% overall; histologic response remains prognostic — vs complete necrosis, PFS HR 1.69 (1–9% viable), 2.76 (10–29%), **3.59 (≥ 30%)** [A/FT]. 75% of resected patients after ≥ 4 VIDE had good response (< 10% viable cells) [FT].
**Teaching point:** BuMel benefit was shown on a **VIDE** backbone; how it applies after VDC/IE is not settled (EE2012 kept BuMel as a consolidation option in both arms [A]).

## 12. Relapsed / refractory Ewing sarcoma

### 12a. rEECur (multi-arm, multi-stage, Bayesian) — [PARTIAL: conference abstract + review only]

- McCabe, M., Kirton, L., Khan, M., Fenwick, N., Strauss, S. J., Valverde, C., Mata, C., Gaspar, N., Luksch, R., Longhi, A., Dirksen, U., Phillips, M., Safwat, A., Gelderblom, H., Kuehne, T., Kanerva, J., Westwood, A. J., Ferrari, S., Whelan, J., & Wheatley, K. (2022). Phase III assessment of topotecan and cyclophosphamide and high-dose ifosfamide in rEECur: An international randomized controlled trial of chemotherapy for the treatment of recurrent and primary refractory Ewing sarcoma (RR-ES) [Abstract]. *Journal of Clinical Oncology*, *40*(17_suppl), LBA2. https://doi.org/10.1200/JCO.2022.40.17_suppl.LBA2 — **no PMID** (ASCO abstract)
- Strauss, S. J., Berlanga, P., & McCabe, M. G. (2024). Emerging therapies in Ewing sarcoma. *Current Opinion in Oncology*, *36*(4), 297–304. https://doi.org/10.1097/CCO.0000000000001048 — PMID 38775200

**Design:** Age 4–50, recurrent or primary refractory Ewing; randomised to **topotecan + cyclophosphamide (TC), irinotecan + temozolomide (IT), gemcitabine + docetaxel (GD), or high-dose ifosfamide (IFOS)**; Bayesian pairwise comparisons; primary outcome EFS [ASCO-A]. Registry ISRCTN36453794 [Strauss FT].
**Sequence:** GD dropped at first interim (2019), IT at second interim (2020) for worse response/EFS [ASCO-A].
**Phase 3 TC vs IFOS (73 each; 451 randomised overall; median follow-up 40 mo):**
- **Median EFS 3.7 mo (2.1–6.2) TC vs 5.7 mo (3.8–7.0) IFOS**
- **Median OS 10.4 mo (7.5–15.5) vs 16.8 mo (11.1–25.8)**
- Posterior probability IFOS better: 95% for both EFS and OS; larger benefit in age < 14 [ASCO-A].
**Toxicity TC vs IFOS (grade 3/4):** febrile neutropenia 26% vs 25%; infection 8% vs 14%; **encephalopathy 0% vs 7%; renal toxicity 0% vs 8%** [ASCO-A].
**Pairwise EFS HRs (Strauss 2024 Table 1):** IT/TC 1.12; IFOS/TC 0.69 (0.48–0.99); GD/TC 1.60; GD/IT 1.40; IFOS/IT 1.00; IFOS/GD 0.55 [FT].
**Current arms (per review):** IFOS vs carboplatin-etoposide vs IFOS + lenvatinib; > 570 recruited [Strauss FT].
**Doses used in rEECur arms:** **[UNVERIFIED]** (registry page not retrievable). High-dose ifosfamide "3 g/m²/day × 5 = 15 g/m²" appears in [PDQ] only.

### 12b. Irinotecan + temozolomide (± vincristine) — [VERIFIED]

- Wagner, L. M., McAllister, N., Goldsby, R. E., Rausen, A. R., McNall-Knapp, R. Y., McCarville, M. B., & Albritton, K. (2007). Temozolomide and intravenous irinotecan for treatment of advanced Ewing sarcoma. *Pediatric Blood & Cancer*, *48*(2), 132–139. https://doi.org/10.1002/pbc.20697 — PMID 16317751
- Casey, D. A., Wexler, L. H., Merchant, M. S., Chou, A. J., Merola, P. R., Price, A. P., & Meyers, P. A. (2009). Irinotecan and temozolomide for Ewing sarcoma: The Memorial Sloan-Kettering experience. *Pediatric Blood & Cancer*, *53*(6), 1029–1034. https://doi.org/10.1002/pbc.22206 — PMID 19637327
- Xu, J., Xie, L., Sun, X., Liu, K., Liang, X., Cai, Z., Tang, X., & Guo, W. (2023). Longer versus shorter schedules of vincristine, irinotecan, and temozolomide (VIT) for relapsed or refractory Ewing sarcoma: A randomized controlled phase 2 trial. *Clinical Cancer Research*, *29*(6), 1040–1046. https://doi.org/10.1158/1078-0432.CCR-22-3546 — PMID 36622702

| Study | Regimen | Result |
|---|---|---|
| Wagner 2007 (4 centres, 16 pts) | **Temozolomide 100 mg/m²/day PO d1–5 + irinotecan 10–20 mg/m²/day IV d1–5 and d8–12**, q21–28d | 1 CR, 3 PR, 3 minor of 14; grade 3–4 diarrhoea 11% of courses (higher irinotecan doses); home irinotecan feasible [A] |
| Casey 2009 (MSKCC, 20 pts) | **Irinotecan 20 mg/m²/day × 5 × 2 weeks + temozolomide 100 mg/m²/day × 5** | ORR 63% (5 CR, 7 PR of 19); median TTP 8.3 mo (16.2 mo for recurrent) [A] |
| Xu 2023 (RCT phase 2, 46 pts, China) | **Protracted d×5×2: irinotecan 20 mg/m² d1–5, 8–12 + vincristine 1.4 mg/m² d1, 8** vs **short d×5: irinotecan 50 mg/m² d1–5 + vincristine 1.4 mg/m² d1**; temozolomide 100 mg/m² d1–5 both; q3w | **12-week ORR 54.5% vs 20.8% (P = .019)**; median PFS 4.3 vs 2.3 mo, OS 12.8 vs 14.8 mo (n.s.); more grade 3–4 diarrhoea/abdominal pain and nausea/vomiting with d×5 [A] |

**Nursing point:** the 10-day (d×5×2) irinotecan schedule is both more active and better tolerated; diarrhoea teaching (early loperamide) — loperamide protocol itself **[UNVERIFIED]** here.

### 12c. Cyclophosphamide + topotecan — [VERIFIED]

- Saylors, R. L., Stine, K. C., Sullivan, J., Kepner, J. L., Wall, D. A., Bernstein, M. L., Harris, M. B., Hayashi, R., & Vietti, T. J. (2001). Cyclophosphamide plus topotecan in children with recurrent or refractory solid tumors: A Pediatric Oncology Group phase II study. *Journal of Clinical Oncology*, *19*(15), 3463–3469. https://doi.org/10.1200/JCO.2001.19.15.3463 — PMID 11481351
- Hunold, A., Weddeling, N., Paulussen, M., Ranft, A., Liebscher, C., & Jürgens, H. (2006). Topotecan and cyclophosphamide in patients with refractory or relapsed Ewing tumors. *Pediatric Blood & Cancer*, *47*(6), 795–800. https://doi.org/10.1002/pbc.20719 — PMID 16411206

**Regimen (both):** **cyclophosphamide 250 mg/m²/day + topotecan 0.75 mg/m²/day, 30-min infusions, days 1–5**; filgrastim 5 µg/kg/day after (Saylors) [A].
**Saylors 2001 (POG phase 2, 83 assessable):** responses in Ewing 6/17, rhabdomyosarcoma 10/15, neuroblastoma 6/13; osteosarcoma 2/18 PR; grade 3–4 neutropenia 53%, thrombocytopenia 44% of courses [A].
**Hunold 2006 (German, 54 pts):** PR 32.6%, SD 26.5%; 1-year OS 0.61 (0.47–0.74) [A].

### 12d. TKIs in relapsed Ewing — [VERIFIED]

- Duffaud, F., Blay, J.-Y., Le Cesne, A., Chevreau, C., Boudou-Rouquette, P., Kalbacher, E., Penel, N., Perrin, C., Laurence, V., Bompas, E., Saada-Bouzid, E., Delcambre, C., Bertucci, F., Cancel, M., Schiffler, C., Monard, L., Bouvier, C., Vidal, V., Gaspar, N., & Chabaud, S. (2023). Regorafenib in patients with advanced Ewing sarcoma: Results of a non-comparative, randomised, double-blind, placebo-controlled, multicentre phase II study. *British Journal of Cancer*, *129*(12), 1940–1948. https://doi.org/10.1038/s41416-023-02413-9 — PMID 37914801
- Attia, S., Bolejack, V., Ganjoo, K. N., George, S., Agulnik, M., Rushing, D., Loggers, E. T., Livingston, M. B., Wright, J., Chawla, S. P., Okuno, S. H., Reinke, D. K., Riedel, R. F., Davis, L. E., Ryan, C. W., & Maki, R. G. (2023). A phase II trial of regorafenib in patients with advanced Ewing sarcoma and related tumors of soft tissue and bone: SARC024 trial results. *Cancer Medicine*, *12*(2), 1532–1539. https://doi.org/10.1002/cam4.5044 — PMID 35950293

- **REGOBONE Ewing (2:1, n = 36 evaluable):** progression-free at 8 weeks **56% vs 7.7%**; median PFS 11.4 vs 3.9 weeks; **primary endpoint not met statistically** [A].
- **SARC024 Ewing (single arm, n = 30):** regorafenib 160 mg d1–21/28; PFR at 8 weeks 63%; median PFS 14.8 weeks; ORR 10%; median OS 53 weeks; hypophosphataemia was the commonest reason for dose reduction [A].
- **CABONE Ewing:** ORR 26% (see §7e) [A].

---

# C. CHONDROSARCOMA

## 13. Surgery is the treatment; systemic options are investigational — [VERIFIED]

- Tap, W. D., Villalobos, V. M., Cote, G. M., Burris, H., Janku, F., Mir, O., Beeram, M., Wagner, A. J., Jiang, L., Wu, B., Choe, S., Yen, K., Gliser, C., Fan, B., Agresta, S., Pandya, S. S., & Trent, J. C. (2020). Phase I study of the mutant IDH1 inhibitor ivosidenib: Safety and clinical activity in patients with advanced chondrosarcoma. *Journal of Clinical Oncology*, *38*(15), 1693–1701. https://doi.org/10.1200/JCO.19.02492 — PMID 32208957
- Tap, W. D., Cote, G. M., Burris, H., Gore, L., Elias, A., Beeram, M., Conley, A. P., Gianolio, D. A., Qu, Z., Pandya, S., & Trent, J. C. (2025). Phase I study of the mutant IDH1 inhibitor ivosidenib: Long-term safety and clinical activity in patients with conventional chondrosarcoma. *Clinical Cancer Research*, *31*(11), 2108–2114. https://doi.org/10.1158/1078-0432.CCR-24-4128 — PMID 40100120
- Wood, G. E., Graves, L. A., Rubin, E. M., Reed, D. R., Riedel, R. F., & Strauss, S. J. (2023). Bad to the bone: Emerging approaches to aggressive bone sarcomas. *American Society of Clinical Oncology Educational Book*, *43*, Article e390306. https://doi.org/10.1200/EDBK_390306 — PMID 37220319
- Duffaud, F., Italiano, A., Bompas, E., Rios, M., Penel, N., Mir, O., Piperno-Neumann, S., Chevreau, C., Delcambre, C., Bertucci, F., Boudou-Rouquette, P., Cancel, M., Perrin, C., Saada-Bouzid, E., Monard, L., Schiffler, C., Chaigneau, L., Hervieu, A., Collard, O., . . . Blay, J.-Y. (2021). Efficacy and safety of regorafenib in patients with metastatic or locally advanced chondrosarcoma: Results of a non-comparative, randomised, double-blind, placebo controlled, multicentre phase II study. *European Journal of Cancer*, *150*, 108–118. https://doi.org/10.1016/j.ejca.2021.03.039 — PMID 33895682

**Key statements:**
- "Surgery is the primary therapy for localized chondrosarcoma; for locally advanced and/or metastatic disease, no known effective systemic therapy exists" [Tap 2020, A].
- "Conventional chondrosarcoma remains a surgical disease, with no defined role for cytotoxic therapy and no approved targeted systemic therapies" [Wood 2023, A].
- Conventional CS is resistant to chemotherapy and radiotherapy; local recurrence after surgery ≈ 25%; skull-base cases may get surgery and/or RT [Tap 2025, FT].
- IDH1/2 mutations in up to 65% of chondrosarcomas [Tap 2020, A]; IDH1 specifically in ≈ 40% of conventional CS [Tap 2025, FT].
- Specific surgical margin rules (curettage for low-grade/atypical cartilaginous tumour vs wide resection) and NCCN v1.2027 content: **[UNVERIFIED]** (NCCN PDF behind login).

## 14. Ivosidenib (mutant IDH1) — [VERIFIED]

**Phase 1 (Tap 2020, n = 21 CS: 12 escalation, 9 expansion):** dose range 100 mg BID–1,200 mg QD; mostly grade 1–2 AEs; 1 treatment-related grade ≥ 3 AE (hypophosphataemia); 2-HG fell 14%–94.2%; **median PFS 5.6 mo (95% CI 1.9–7.4); 6-month PFS 39.5%; SD 52%** [A].
**Long-term (Tap 2025, data lock 18 Mar 2024):** 13 conventional, 6 dedifferentiated, 2 unknown. Expansion dose **500 mg once daily** [A]. Conventional CS: **ORR 23.1% (95% CI 5.0–53.8; 1 CR at skull base + 2 PR), median DoR 53.5 mo, median PFS 7.4 mo (2.0–61.3)**; 3 patients treated > 7 years; no ivosidenib-related SAEs [A/FT].
**Phase 3 CHONQUER (NCT06127407):** ivosidenib vs placebo, locally advanced/metastatic conventional CS untreated or after 1–2 regimens; primary PFS by BICR in grade 1–2; est. n = 156; **recruiting**; start 2024-07-09; est. primary completion 2028-02-01 [CT].
**Regulatory:** FDA label (TIBSOVO, 2025-12-22): AML, MDS, cholangiocarcinoma — **no chondrosarcoma** [L-TIBSOVO]. Taiwan 拓舒沃膜衣錠 250 mg 衛部藥輸字第028815號 (2024-10-23): same indications — **chondrosarcoma off-label** [TFDA].
**Regorafenib in CS (REGOBONE, 2:1, 40 evaluable):** 12-week PFR 54.2% vs 31.3%; median PFS 19.9 vs 8.0 weeks; primary endpoint not met; one fatal liver dysfunction [A].

---

# D. HIGH-DOSE METHOTREXATE (HD-MTX) SAFETY PROTOCOL

**References**
- Howard, S. C., McCormick, J., Pui, C.-H., Buddington, R. K., & Harvey, R. D. (2016). Preventing and managing toxicities of high-dose methotrexate. *The Oncologist*, *21*(12), 1471–1482. https://doi.org/10.1634/theoncologist.2015-0164 — PMID 27496039
- Ramsey, L. B., Balis, F. M., O'Brien, M. M., Schmiegelow, K., Pauley, J. L., Bleyer, A., Widemann, B. C., Askenazi, D., Bergeron, S., Shirali, A., Schwartz, S., Vinks, A. A., & Heldrup, J. (2018). Consensus guideline for use of glucarpidase in patients with high-dose methotrexate induced acute kidney injury and delayed methotrexate clearance. *The Oncologist*, *23*(1), 52–61. https://doi.org/10.1634/theoncologist.2017-0243 — PMID 29079637
- Widemann, B. C., Schwartz, S., Jayaprakash, N., Christensen, R., Pui, C.-H., Chauhan, N., Daugherty, C., King, T. R., Rush, J. E., & Howard, S. C. (2014). Efficacy of glucarpidase (carboxypeptidase G2) in patients with acute kidney injury after high-dose methotrexate therapy. *Pharmacotherapy*, *34*(5), 427–439. https://doi.org/10.1002/phar.1360 — PMID 24132809
- Labels: methotrexate injection [L-METHOTREXATE, Accord, effective 2026-09-04, set_id dd035a9f-…]; leucovorin calcium injection [L-LEUCOVORIN, Sagent, 2026-06-16, set_id c0cbcbf6-…]; VORAXAZE (glucarpidase) [L-VORAXAZE, BTG, 2024-11-27].

## 15. Definitions and risk — [VERIFIED]

- **HD-MTX = ≥ 500 mg/m²** [Howard A; L-METHOTREXATE: leucovorin required at ≥ 500 mg/m², consider at 100–< 500 mg/m²].
- AKI after HD-MTX: 2%–12% overall [Howard A]; **1.5% of cycles in sarcoma** vs 9.1% in lymphoma [Howard FT]; **1.8% of courses of 12 g/m² over 4 h in osteosarcoma** [Ramsey FT].
- Mechanism: MTX and metabolites (7-OH-MTX, DAMPA) **precipitate in acidic urine (pH < 5.5)**; raising urine pH from 6.0 to 7.0 increases solubility **5–8-fold** [Howard FT]. Osteosarcoma regimen end-of-infusion plasma MTX ≈ **1,000 µM**, urine ≈ 10,000 µM — near the solubility limit at pH 7 [Ramsey FT].
- AKI is usually **non-oliguric** (urine output preserved, creatinine rises) — so do not rely on urine output alone [Ramsey FT].
- **Use preservative-free MTX for high-dose regimens** (benzyl-alcohol formulations can cause metabolic acidosis/CNS toxicity) — boxed warning [L-METHOTREXATE].

## 16. Before the infusion — [VERIFIED unless marked]

| Check | Target / action | Source |
|---|---|---|
| Counts (EURAMOS) | ANC ≥ 250/µL, platelets ≥ 50,000/µL for an HD-MTX dose | Marina FT |
| Renal function | Baseline creatinine/electrolytes; then at least daily | L-METHOTREXATE |
| Third-space fluid | **Drain significant effusions/ascites before MTX** (slow release → prolonged half-life, toxicity) | L-METHOTREXATE §5.17; Howard FT |
| Interacting drugs (stop or avoid; if unavoidable monitor closely) | **Penicillins; sulfonamide antibiotics (incl. TMP-SMX); PPIs; probenecid; aspirin/NSAIDs ("unexpectedly severe and fatal GI toxicity" with HD-MTX); other antifolates (dapsone, pemetrexed, pyrimethamine); highly protein-bound drugs; mercaptopurine; hepatotoxic/nephrotoxic drugs; nitrous oxide anaesthesia (avoid); folic acid** | L-METHOTREXATE §7.1 |
| TMP-SMX prophylaxis | Whether to hold it during HD-MTX is **controversial**; "no strong data" | Howard FT |
| Leucovorin already running | Stop it and **defer HD-MTX to the next day** | Howard FT |
| Hydration | Pediatric protocols: ≥ 2 h at ≥ 200 mL/m²/h, or 100–150 mL/m²/h from 12 h before, continued 24–48 h or longer; adults: 150–200 mL/h of bicarbonate fluid to 2 L before | Howard FT |
| Alkaline fluid | Fluids with **40 mEq/L sodium bicarbonate** during and after HD-MTX | Howard FT |
| Urine pH to start | **≥ 7** (Howard; label "7 or higher"); Ramsey "**above 7**" before start, maintained until MTX below solubility threshold | Howard FT; L-METHOTREXATE; Ramsey FT |
| Urine output | **≥ 2,500 mL/m²/day** before, during and after; < 2,000 mL/m²/day → higher risk of delayed clearance | Ramsey FT |

## 17. During the infusion — [VERIFIED]

- **Dose:** osteosarcoma **12 g/m² (max 20 g) IV over 4 h** [L-METHOTREXATE; Marina FT].
- **Urine pH with every void**; bicarbonate bolus **12.5 mEq/m² if pH 6.5, 25 mEq/m² if pH < 6.5**; hourly urine pH during infusion in that protocol [Howard FT].
- If systemic alkalosis but urine not alkaline: **acetazolamide 250–500 mg PO four times daily** [Howard FT].
- Strict intake/output [Howard FT].
- **Draw MTX levels from a different lumen/site**: samples from the infusion lumen can be falsely high; if MTX high but creatinine normal, repeat with a new sample [Ramsey FT].

## 18. Leucovorin rescue and level-guided adjustment

### 18a. US leucovorin label nomogram (based on MTX 12–15 g/m² IV over 4 h) — [VERIFIED, L-LEUCOVORIN]

**Standard:** **leucovorin 15 mg (≈ 10 mg/m²) q6h × 10 doses, starting 24 h after the start of MTX.** Creatinine and MTX at least daily. Continue leucovorin, hydration and **urine alkalinisation (pH ≥ 7.0)** until MTX < **0.05 µM (5 × 10⁻⁸ M)**.

| Situation | MTX level / renal criterion | Leucovorin |
|---|---|---|
| Normal elimination | ≈ **10 µM at 24 h, ≈ 1 µM at 48 h, < 0.2 µM at 72 h** | 15 mg PO/IM/IV q6h for 60 h (10 doses from 24 h) |
| Delayed **late** elimination | > 0.2 µM at 72 h **and** > 0.05 µM at 96 h | Continue 15 mg q6h until < 0.05 µM |
| Delayed **early** elimination and/or AKI | **≥ 50 µM at 24 h, or ≥ 5 µM at 48 h, or ≥ 100% creatinine rise at 24 h** (e.g., 0.5 → ≥ 1.0 mg/dL) | **150 mg IV q3h until < 1 µM, then 15 mg IV q3h until < 0.05 µM** |

- If significant toxicity occurred with "less severe" abnormalities: extend rescue by 24 h (**14 doses over 84 h**) in later courses [L].
- **IV push no faster than 160 mg/min** (calcium content) [L]. Do not give intrathecally [L].
- Separate "impaired elimination/overdose" paragraph in the same label: 10 mg/m² q6h until MTX < 0.01 µM; if creatinine +50% at 24 h, or 24-h MTX > 5 µM, or 48-h > 0.9 µM → **100 mg/m² IV q3h**; hydration 3 L/day + bicarbonate to urine pH ≥ 7.0 [L] (see flag 6).

### 18b. Timing rules from the consensus papers — [VERIFIED]

- Leucovorin usually starts **24–42 h** after the start of HD-MTX and **must not be delayed beyond 42–48 h**; delay beyond 48 h significantly increases severe toxicity [Ramsey FT].
- Leucovorin is less effective when MTX is high (competition for the reduced folate carrier), especially MTX > 10 µM for ≥ 48 h [Ramsey FT].
- Doses > 200–500 mg (or BSA × 50) infused over 1–2 h because of calcium; levoleucovorin can replace racemic leucovorin at **50% of the dose** [Ramsey FT].
- "Over-rescue" (unnecessarily high leucovorin) has been linked with treatment failure in ALL and osteosarcoma — avoid [Ramsey FT].
- Some regimens calculate leucovorin (mg) = **plasma MTX (µM) × body weight (kg)** when MTX > 5 µM [Ramsey FT].

## 19. Delayed clearance and glucarpidase — [VERIFIED]

**Label (VORAXAZE):** indicated to reduce toxic plasma MTX (**> 1 µmol/L**) in adults and children with **delayed clearance (> 2 SD above the expected excretion curve) due to impaired renal function**; **not** for patients with expected clearance (risk of subtherapeutic MTX exposure) [L-VORAXAZE].
- **Dose: 50 units/kg IV over 5 minutes**, single dose; flush line before and after [L].
- **Leucovorin ≥ 2 h before or ≥ 2 h after glucarpidase** (glucarpidase also cleaves leucovorin) [L; Ramsey FT].
- First 48 h after glucarpidase: give the **same leucovorin dose as before**; after 48 h dose by measured MTX; continue until MTX below threshold for **≥ 3 days**; continue hydration/alkalinisation [L].
- **Measure MTX by a chromatographic method (HPLC) for 48 h** — DAMPA (half-life ≈ 9 h) cross-reacts with immunoassays and overestimates MTX [L; Howard FT; Ramsey FT].
- Registration study: 22 patients (50% osteosarcoma); rapid sustained reduction to ≤ 1 µM in **10/22 (45%)** [L]. Pooled compassionate use (Widemann 2014): 99% median MTX reduction within 15 min; RSCIR 59% (83/140); 64% of patients with ≥ grade 2 renal impairment recovered to grade 0–1, median 12.5 days [A].
- Serious hypersensitivity < 1% [L].
- **Approval:** FDA 2012-01-17 (BLA125327) [openFDA drugsfda]; EU 11 Jan 2022 (holder SERB SAS) [EMA]; **Taiwan: not in TFDA licence file** [TFDA].

**Ramsey 2018 consensus thresholds** (glucarpidase "may be indicated" when the level is above the threshold **and** serum creatinine is elevated vs baseline) [A/FT]:

| Regimen | Trigger for extra monitoring | Glucarpidase threshold (hours from start of MTX) |
|---|---|---|
| **8–12 g/m² over ≤ 6 h (osteosarcoma)** | End-of-infusion MTX > 1,500 µM | **24 h > 50 µM; 36 h > 30 µM; 42 h > 10 µM; 48 h > 5 µM** |
| 1–8 g/m² over 24 h | End-of-infusion > 120 µM or creatinine ≥ 50% rise | 36 h > 30 µM; 42 h > 10 µM; 48 h > 5 µM |
| 36–42-h infusion | — | 48 h > 5 µM |

- **Give glucarpidase optimally within 48–60 h** of the start of HD-MTX; life-threatening toxicity may not be preventable later [A].
- Glucarpidase is often not stocked — order as soon as need is anticipated; if less than 50 U/kg is available, give what is available [Ramsey FT].
- Rebound of plasma MTX can occur as tissue MTX redistributes; continue leucovorin ≥ 48 h after glucarpidase [Ramsey FT].
- Without glucarpidase: high-dose leucovorin is the best option; dialysis gives rebound and mixed results [Ramsey FT; Howard FT].
- With AKI: keep alkalinised fluids, add acetazolamide to keep urine pH > 7, and push fluids to **≥ 3 L/m²/day** if tolerated (watch for fluid overload) [Howard FT].

**Other HD-MTX toxicities to monitor:** transient transaminase rise in up to 60% and hyperbilirubinaemia in 25% of courses; transient CNS disturbance in up to 15% of courses; emesis 10%–30% [Howard FT]. Severe dermatologic reactions (TEN, SJS) and photosensitivity [L-METHOTREXATE §5.11]; one fatal TEN in EURAMOS-1 pre-op [Whelan FT].

---

# E. CISPLATIN OTOTOXICITY IN CHILDREN/AYA AND SODIUM THIOSULFATE

**References**
- Brock, P. R., Maibach, R., Childs, M., Rajput, K., Roebuck, D., Sullivan, M. J., Laithier, V., Ronghe, M., Dall'Igna, P., Hiyama, E., Brichard, B., Skeen, J., Mateos, M. E., Capra, M., Rangaswami, A. A., Ansari, M., Rechnitzer, C., Veal, G. J., Covezzoli, A., . . . Neuwelt, E. A. (2018). Sodium thiosulfate for protection from cisplatin-induced hearing loss. *The New England Journal of Medicine*, *378*(25), 2376–2385. https://doi.org/10.1056/NEJMoa1801109 — PMID 29924955
- Freyer, D. R., Chen, L., Krailo, M. D., Knight, K., Villaluna, D., Bliss, B., Pollock, B. H., Ramdas, J., Lange, B., Van Hoff, D., VanSoelen, M. L., Wiernikowski, J., Neuwelt, E. A., & Sung, L. (2017). Effects of sodium thiosulfate versus observation on development of cisplatin-induced hearing loss in children with cancer (ACCL0431): A multicentre, randomised, controlled, open-label, phase 3 trial. *The Lancet Oncology*, *18*(1), 63–74. https://doi.org/10.1016/S1470-2045(16)30625-8 — PMID 27914822. **Erratum:** *Lancet Oncol 18*(6), e301 (2017), PMID 28593857 (content not read).
- Ohlsen, T. J. D., Collier, W. H., Ramdas, J., Sung, L., & Freyer, D. R. (2025). Otoprotective effects of sodium thiosulfate by demographic and clinical characteristics: A report from Children's Oncology Group study ACCL0431. *Pediatric Blood & Cancer*, *72*(3), Article e31479. https://doi.org/10.1002/pbc.31479 — PMID 39654065
- Moke, D. J., Luo, C., Millstein, J., Knight, K. R., Rassekh, S. R., Brooks, B., Ross, C. J. D., Wright, M., Mena, V., Rushing, T., Esbenshade, A. J., Carleton, B. C., & Orgel, E. (2021). Prevalence and risk factors for cisplatin-induced hearing loss in children, adolescents, and young adults: A multi-institutional North American cohort study. *The Lancet Child & Adolescent Health*, *5*(4), 274–283. https://doi.org/10.1016/S2352-4642(21)00020-1 — PMID 33581749
- Lewis, M. J., DuBois, S. G., Fligor, B., Li, X., Goorin, A., & Grier, H. E. (2009). Ototoxicity in children treated for osteosarcoma. *Pediatric Blood & Cancer*, *52*(3), 387–391. https://doi.org/10.1002/pbc.21875 — PMID 19061216
- Freyer, D. R., Brock, P. R., Chang, K. W., Dupuis, L. L., Epelman, S., Knight, K., Mills, D., Phillips, R., Potter, E., Risby, D., Simpkin, P., Sullivan, M., Cabral, S., Robinson, P. D., & Sung, L. (2020). Prevention of cisplatin-induced ototoxicity in children and adolescents with cancer: A clinical practice guideline. *The Lancet Child & Adolescent Health*, *4*(2), 141–150. https://doi.org/10.1016/S2352-4642(19)30336-0 — PMID 31866182
- Ma, J., Foster, J. H., Rassekh, S. R., Malvar, J., Chi, Y.-Y., Sauer, H. E., Jeon, J., Freyer, D. R., Rushing, T., & Orgel, E. (2025). Real-world experience using sodium thiosulfate pentahydrate off-label for cisplatin otoprotection in children, adolescents, and young adults. *Pediatric Blood & Cancer*, *72*(5), Article e31631. https://doi.org/10.1002/pbc.31631 — PMID 40032793
- Streefkerk, N., Geller, J. I., Knight, K., Ansari, M., Papadakis, V., Calaminus, G., Masroor, A., Huitema, A. D. R., Pasqualini, C., Rutkowski, S., Bouffet, E., Am Zehnhoff-Dinnesen, A., Caniza, M., van de Wetering, M. D., Delano, P., Rajput, K. M., Weerdenburg, H., Frazier, A. L., Hoetink, A. E., . . . van den Heuvel-Eibrink, M. M. (2026). Avoiding cisplatin-related hearing loss, including implementing sodium thiosulfate as otoprotectant into daily pediatric clinical practice: Proceedings based on evidence and expert opinion from the Ototoxicity Taskforce of the SIOP Supportive Care Network. *Ear and Hearing*, *47*(6), 1573–1583. https://doi.org/10.1097/AUD.0000000000001856 — PMID 42370844
- Labels: cisplatin [L-CISPLATIN, WG Critical Care, 2026-06-24]; PEDMARK [L-PEDMARK, Fennec, 2025-10-27]; Pedmarqsi EPAR [EMA].

## 20. Burden of cisplatin-induced hearing loss (CIHL) — [VERIFIED]

- **Cisplatin label:** ototoxicity is cumulative, high-frequency (4,000–8,000 Hz) first, can be unilateral or bilateral, can occur after the first dose; **pediatric prevalence 40%–60%**, worse < 5 years; consider audiometric and vestibular monitoring in **all** pediatric patients; TPMT variants may contribute (inconsistent) [L-CISPLATIN].
- **Moke 2021 (North American cohort, n = 1,481, incl. AYA 15–39; osteosarcoma 20% of cohort):** moderate/severe CIHL (SIOP ≥ 2) **43.8%** at latest follow-up (mean 3.9 years); risk rises with **daily dose (aOR 1.15 per +10 mg/m²/day)** and **cycle dose (aOR 2.16 per +50 mg/m²/cycle)** after accounting for cumulative dose; **vincristine exposure aOR 3.55**; cumulative dose aOR 1.19 per +100 mg/m²; dose reductions were not associated with worse survival [A/FT]. Osteosarcoma-specific prevalence is shown only in a figure — **[UNVERIFIED]** as a number.
- **Osteosarcoma (Lewis 2009, 3–18 y):** cisplatin **120 mg/m² on 1 day → 78% hearing loss vs 60 mg/m²/day × 2 days → 30%** (P = .019); educationally significant loss only 4% with the 2-day split; age and cumulative dose also independent predictors [A].
- MAP cumulative cisplatin = **480 mg/m²** [Marina FT] — well above the 200 mg/m² threshold used for ACCL0431 eligibility [Freyer FT].
- Mifamurtide arm in INT-0133: severe hearing loss 12% vs 7% per Prescrire [A] — **[PARTIAL]** (secondary critique; not checked in the primary paper).

## 21. SIOPEL-6 (STS in standard-risk hepatoblastoma) — [VERIFIED]

**Design:** Phase 3, randomised; age > 1 month to < 18 years; standard-risk hepatoblastoma [A].
**Arms:** cisplatin **80 mg/m² over 6 h** alone vs + **STS 20 g/m² IV over 15 min, 6 h after the end of cisplatin**; 4 pre-op + 2 post-op courses [A].
**Primary endpoint (Brock grade ≥ 1 hearing loss, at ≥ 3.5 years of age):** **33% (18/55) vs 63% (29/46); RR 0.52 (95% CI 0.33–0.81), P = .002** [A].
**Survival (median 52 mo):** 3-year EFS 82% vs 79%; 3-year OS 98% vs 92% — no detriment [A].

## 22. ACCL0431 (STS across pediatric cancers, COG) — [VERIFIED]

**Design:** Phase 3, open-label, randomised 1:1; age 1–18; newly diagnosed cancer with planned cumulative cisplatin ≥ 200 mg/m² and infusion ≤ 6 h; 38 COG sites (NCT00716976) [A/FT].
**Arms:** **STS 16 g/m² IV over 15 min, 6 h after each cisplatin dose** vs observation [A]. Osteosarcoma was ≈ 23% of each arm (15 and 14 patients) [FT].
**Primary endpoint (hearing loss 4 weeks after last cisplatin, ASHA criteria):** **28.6% (14/49) vs 56.4% (31/55), p = 0.00022; adjusted OR 0.31 (0.13–0.73)** [A].
**Survival signal:** localised disease (n = 77) — no difference (3-year OS 83% STS vs 89% control; EFS RHR 1.14, OS RHR 1.09). **Disseminated disease — 3-year OS 45% (STS) vs 84% (control), RHR 4.10 (1.30–12.97), p = 0.009** (post hoc) [FT].
**Subgroups (Ohlsen 2025):** benefit largest in age < 5 (OR 0.08) and neuroblastoma/hepatoblastoma/medulloblastoma (OR 0.10); **germ cell tumour/osteosarcoma OR 0.32 (0.06–1.25), not significant** [A].

## 23. Labels, guidelines and practical STS rules — [VERIFIED]

- **US (PEDMARK, NDA212937, approved 2022-09-20):** to reduce ototoxicity with cisplatin in **pediatric patients ≥ 1 month with localized, non-metastatic solid tumors**. Dose by actual weight: **< 5 kg 10 g/m²; 5–10 kg 15 g/m²; > 10 kg 20 g/m²**, IV over 15 min **starting 6 h after the end of cisplatin**; for multi-day cisplatin, give after each dose and **≥ 10 h before the next cisplatin** (do not give if next cisplatin is < 10 h away). **Not established after cisplatin infusions > 6 h.** Not substitutable with other STS products. Pre-medicate with antiemetics; hypersensitivity 8%–13%; check sodium (withhold if > 145 mmol/L) and potassium; sodium load 162 mmol/m² at 20 g/m² [L-PEDMARK; openFDA drugsfda].
- **EU (Pedmarqsi, authorised 26 May 2023, Norgine):** 1 month to **< 18 years**, localised non-metastatic solid tumours; 15-min infusion exactly 6 h after cisplatin [EMA].
- **Guideline (Freyer 2020):** **strong** recommendation for STS in non-metastatic hepatoblastoma; **weak** recommendation **for** other non-metastatic cancers; **weak** recommendation **against** routine use in metastatic cancers; amifostine, sodium diethyldithiocarbamate and intratympanic therapy not routinely; **do not change cisplatin infusion duration** to reduce ototoxicity [A].
- **SIOP task force 2026:** cisplatin infusions **1–6 h** as standard of care, STS 6 h after the end; multi-day cisplatin = STS after each day, with ≥ 6 h after STS before the next cisplatin; consider a further **6-h gap after STS before an alkylating agent**; dose differs numerically between **pentahydrate and anhydrous** STS salts (equivalent active drug) [FT].
- **AYA real-world (Ma 2025, 59 patients, off-label STS pentahydrate 16 or 20 g/m²):** infusion reactions 14% (more at 20 g/m²); CIHL (SIOP ≥ 2) 30% at end of therapy [A].
- **Relevance to osteosarcoma in Taiwan:** (1) MAP uses cisplatin; the COG 2-day 4-h schedule fits the STS window, the 72-h continuous European schedule does not [Marina FT; L-PEDMARK]; (2) most patients are non-metastatic adolescents — on-label only < 18 (EU) / "pediatric" (US); (3) the metastatic-disease survival signal argues against STS when lung metastases are present [Freyer 2017 FT; Freyer 2020 A]; (4) **no STS otoprotectant is licensed in Taiwan** [TFDA]. Baseline and per-cycle audiology remains the main nursing action [L-CISPLATIN].

---

# F. TAIWAN LICENCE STATUS SNAPSHOT (TFDA open data, CSV dated 2026-10-27) — [VERIFIED]

| Drug | Taiwan status | Bone-sarcoma relevance |
|---|---|---|
| Mifamurtide (MEPACT 秘配得) | 衛部藥輸字第026319號, issued 2015-02-13, **cancelled 2023-10-17 (自請註銷)** | Not available as a licensed product |
| Glucarpidase (Voraxaze) | **No entry** | Special-import route **[UNVERIFIED]** |
| Sodium thiosulfate otoprotectant (PEDMARK/Pedmarqsi) | **No entry**; old STS injections (DETOXOL) cancelled 1985/2010 | — |
| Dexrazoxane | **No entry** | — |
| Levoleucovorin | **No entry** (racemic calcium folinate only; indication 葉酸拮抗劑(如 Methotrexate)過量之解毒劑) | — |
| Regorafenib (Stivarga 癌瑞格) | 衛部藥輸字第026168號; CRC, GIST, HCC | Osteosarcoma/Ewing/CS = off-label |
| Cabozantinib (Cabometyx 癌必定) | 衛部藥輸字第027511–027513號; RCC, HCC, DTC (≥ 12 y), pNET/epNET | Off-label |
| Ivosidenib (Tibsovo 拓舒沃) | 衛部藥輸字第028815號 (2024-10-23); AML, MDS, cholangiocarcinoma | Chondrosarcoma off-label |
| Ifosfamide (好克癌, 愛斯達) | 衛署藥輸字第018479–018481號; indication lists **骨肉瘤** and **軟骨肉瘤** among others | On-label for osteosarcoma |
| Topotecan, irinotecan, temozolomide | No sarcoma indication | Ewing relapse regimens = off-label |
| Methotrexate injection (e.g., 盈壽求得 1 g/10 mL, 衛署藥輸字第022132號) | Indication generic (抗腫瘍化學治療劑 etc.) | HD-MTX for osteosarcoma not explicitly listed |

NHI reimbursement status of any of these for bone sarcoma: **[UNVERIFIED]** (www.nhi.gov.tw not reachable).

---

# G. EXAM/WARD PEARLS (each tied to a verified source above)

1. MAP = cisplatin 120 mg/m² (60 × 2), doxorubicin 75 mg/m² (37.5 × 2), MTX 12 g/m² over 4 h (max 20 g); pre-op 10 weeks, post-op to week 29; cumulative cisplatin 480, doxorubicin 450 mg/m² [§1].
2. Good response = < 10% viable tumour (≥ 90% necrosis); about half of patients; poor response doubles post-surgery event risk (HR 2.13) [§5].
3. EURAMOS-1: MAPIE for poor responders — no EFS gain (HR 0.98), more toxicity and secondary leukaemia; IFN for good responders — no gain (HR 0.83) [§3–4].
4. HD-MTX: urine pH ≥ 7 before starting; urine output ≥ 2.5 L/m²/day; drain third-space fluid; stop PPIs, NSAIDs, penicillins, sulfonamides, probenecid; leucovorin at 24 h; levels 24/48/72 h; normal ≈ 10/1/< 0.2 µM [§16–18].
5. Glucarpidase 50 U/kg over 5 min; leucovorin ≥ 2 h apart; HPLC for 48 h; best within 48–60 h; osteosarcoma triggers 24 h > 50, 48 h > 5 µM with rising creatinine [§19].
6. Ewing: interval-compressed VDC/IE every 14 days beats every 21 days (5-year EFS 73% vs 65%; 10-year OS 76% vs 69%) and beats VIDE (3-year EFS 67% vs 61%) [§9–10].
7. BuMel helps localised high-risk Ewing after VIDE (EFS HR 0.64) but not lung-metastatic Ewing (HR 0.79, n.s.) [§11].
8. Relapsed Ewing: high-dose ifosfamide beat TC in rEECur (median OS 16.8 vs 10.4 mo, conference data); watch encephalopathy and nephrotoxicity [§12a].
9. Relapsed osteosarcoma: regorafenib (PFS 3.6 vs 1.7 mo; HR 0.42) and cabozantinib (ORR 12%) are options; both off-label in Taiwan [§7, §F].
10. Chondrosarcoma: surgery; chemo/RT-resistant; ivosidenib ORR 23% in IDH1-mutant conventional CS (phase 1), phase 3 pending [§13–14].
11. Cisplatin hearing loss: split 60 × 2 is less ototoxic than 120 × 1; STS 6 h after cisplatin halves hearing loss in localised disease but not for metastatic disease, and is not licensed in Taiwan [§20–23].

---

## H. Not verified / not found (as of 2026-10-29)

- Full rEECur peer-reviewed paper and its exact arm doses (only ASCO abstracts and reviews).
- Per-day doses of VIDE, VDC/IE dose caps (vincristine 2 mg max, doxorubicin → dactinomycin switch), BuMel doses — JCO/Lancet full texts not in PMC.
- REGOBONE osteosarcoma median PFS (not in abstract).
- FDA advisory-committee details for mifamurtide (2007).
- Osteosarcoma-specific CIHL prevalence in Moke 2021 (figure only).
- Huvos grade definitions; NCCN v1.2027 specific recommendations (PDF behind login).
- Taiwan special-import or NHI reimbursement status for glucarpidase, STS, regorafenib, cabozantinib, ivosidenib in bone sarcoma.
- Taiwan Cancer Registry incidence for bone sarcomas was outside this file's scope and not checked here.
