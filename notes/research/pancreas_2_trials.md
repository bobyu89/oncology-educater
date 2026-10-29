# Pancreas 2. Pancreatic adenocarcinoma key trials: citation and data verification

Handbook: Taiwanese oncology NP handbook (專科護理師), pancreatic cancer chapter
Verification date: 2026-10-29
Method: Every PMID, author list, volume, page range and DOI was pulled from PubMed (NCBI E-utilities efetch/esearch, the same database the PubMed MCP tools use). Numbers come from the PubMed abstract unless another source is named. Where the abstract lacked a requested number, I checked the PMC full text, then the current US FDA label (openFDA), and only then an open-access secondary source (review or guideline in PMC), which I tag separately. Taiwan licensing comes from the TFDA open-data drug-licence file (InfoId=36; the zip inside is dated 2026-10-27). Nothing was filled from memory. Anything still missing is marked **[UNVERIFIED]**.

**Source tags used inline**
- [A] = PubMed abstract of the cited paper
- [FT] = PMC full text of the cited paper (results or methods section)
- [L-xxx] = current US FDA prescribing information via openFDA (label effective date given)
- [S-xxx] = secondary source (review or guideline) that quotes the trial; the trial paper itself was not readable
- [TFDA] = TFDA licence open data (file dated 2026-10-27)
- **[UNVERIFIED]** = not stated in any source I could read; do not print without checking the paper

**Section status tags**
- **[VERIFIED]** = citation confirmed on PubMed, and the primary-endpoint result (median, HR, 95% CI where the trial reports them) confirmed from [A], [FT] or [L]
- **[PARTIAL]** = citation confirmed, but part of the primary-endpoint result or key toxicity data rests on a secondary source or is missing
- **[UNVERIFIED]** = paper not found

**APA 7 notes.** Author lists follow APA 7: all authors up to 20; for 21 or more, the first 19, an ellipsis, then the final author. Study-group bylines (for example "for the APACT Investigators") are left out. Titles are converted to sentence case from the PubMed title, with proper nouns kept (Dutch, Japan, Taiwan, S-1). The year is the journal-issue year, which can differ from the e-pub year (Prep-02/JSAP-05: e-pub 2025, issue 2026). MASTERPLAN has no volume or pages yet (advance online publication).

**Secondary sources used** (cited inline as [S-xxx]):
- [S-deJesus] de Jesus, V. H. F., & Riechelmann, R. P. (2021). Comparative efficacy of modified FOLFIRINOX, gemcitabine plus capecitabine and gemcitabine plus nab-paclitaxel as adjuvant treatment for resected pancreatic cancer: A Bayesian network meta-analysis. *Ecancermedicalscience*, *15*, 1276. https://doi.org/10.3332/ecancer.2021.1276 — PMID 34567261 (Table 5 reproduces the ESPAC-4, PRODIGE 24 and APACT toxicity tables)
- [S-Ei] Ei, S., Takahashi, S., Ogasawara, T., Mashiko, T., Masuoka, Y., & Nakagohri, T. (2023). Neoadjuvant and adjuvant treatments for resectable and borderline resectable pancreatic ductal adenocarcinoma: The current status of pancreatic ductal adenocarcinoma treatment in Japan. *Gut and Liver*, *17*(5), 698–710. https://doi.org/10.5009/gnl220311 — PMID 36843421
- [S-PanAsia] Tai, D., Conroy, T., Lee, J. J. X., Chee, C. E., Hao, C. Y., Wijaya, I., Aggarwal, S., Ueno, M., Jeung, H. C., Hashim, N. M., Tan Chun Bing, J., Chen, L. T., Korphaisarn, K., Tanasanvimon, S., Chou, W. C., Cargullo, E., Muin, N. F. A., Lee, M. A., Ohba, A., . . . Ducreux, M. (2025). Pan-Asian adapted ESMO Clinical Practice Guidelines for the diagnosis, treatment and follow-up of patients with pancreatic cancer. *ESMO Open*, *10*(10), Article 105826. https://doi.org/10.1016/j.esmoop.2025.105826 — PMID 41067164 (Taiwan Oncology Society voted; has a Taiwan drug-access paragraph)
- [S-Fivaz] Fivaz, M., Bornand, A., Corro, C., Koessler, T., & Genoud, V. (2025). Actionable mutations in pancreatic cancer: Where targeted therapies are making a difference. *BMJ Open Gastroenterology*, *12*(1), Article e001925. https://doi.org/10.1136/bmjgast-2025-001925 — PMID 41309265
- [S-NAPOLI3] The NAPOLI 3 Lancet discussion (PMID 37708904, PMC full text) quotes PRODIGE 4 toxicity rates.
- [S-ESPAC4LT] The ESPAC-4 long-term paper (Palmer 2025, PMID 39637340, PMC full text) lists the PRODIGE 24 eligibility criteria.

---

## 0. Corrections and flags for the editor (read first)

1. **Daraxonrasib is now published, approved and practice-changing (2026).** RASolute 302 (O'Reilly et al., *NEJM* 2026; 395(4): 325–337; e-pub 2026-05-31): second-line metastatic PDAC, **OS 13.2 vs 6.7 months, HR 0.40 (95% CI 0.30–0.53)** in the overall population [A + L]. FDA approved RASONQUE (daraxonrasib) on **2026-08-26** (NDA 220910, priority review) [openFDA Drugs@FDA]. The FDA indication is **wider than the trial**: "received at least one prior systemic therapy **or who are not candidates for multiagent systemic therapy**" [L-2026-08-27]. RASolute 302 enrolled only second-line patients; a *Nat Rev Clin Oncol* commentary is titled "An imprecise label in the era of precision medicine" (Subbiah 2026, PMID 42869992; no abstract). **Not licensed in Taiwan** (no TFDA entry as of 2026-10-27).
2. **TS-1 (S-1) is not licensed in Taiwan for adjuvant pancreatic cancer.** The TFDA indication for pancreas reads 「適用於治療局部晚期或轉移性胰臟癌病人」 only [TFDA, licences 衛署藥輸字第025242/025243號]. Adjuvant S-1 (JASPAC 01) is therefore off-label in Taiwan, even though the 2025 Pan-Asian ESMO guideline, which Taiwan Oncology Society voted on, recommends "adjuvant mFOLFIRINOX or S-1 [I, A]" [S-PanAsia]. The Taiwan paragraph of that guideline says: "All available regimens are not approved or reimbursed for [the] adjuvant setting" [S-PanAsia].
3. **TFDA data contradict the Pan-Asian guideline's Taiwan paragraph on two drugs.** (a) Onivyde: the guideline says nal-IRI is "approved in the second-line setting", but the current TFDA indication also includes **first-line NALIRIFOX** (「與oxaliplatin、5-fluorouracil和leucovorin併用，作為轉移性胰腺癌成人病人的第一線治療」; licence last changed 2026-02-25). (b) Entrectinib: the guideline says "not approved" in Taiwan, but TFDA lists Rozlytrek (licensed 2020-05-21) with an NTRK-fusion solid-tumour indication. Use TFDA wording in the handbook.
4. **Onivyde's Taiwan licence holder is a Taiwanese company**: 智擎生技製藥股份有限公司 (PharmaEngine) [TFDA]. Taiwanese investigators were authors on NAPOLI-1 (Li C.-P., Taipei Veterans General Hospital; Shan Y.-S., National Cheng Kung University Hospital; Chiu C.-F., China Medical University Hospital; Chen L.-T., NHRI) and APACT (Li C.-P., Shan Y.-S.) [PubMed affiliations]. GEST (S-1 in advanced disease) was a Japan–Taiwan trial.
5. **PRODIGE 24 numbers changed between the 2018 and 2022 papers.** Use the 5-year paper: DFS **21.4 vs 12.8 months, HR 0.66 (0.54–0.82)**; OS **53.5 vs 35.5 months, HR 0.68 (0.54–0.85)**; 5-year OS 43.2% vs 31.4%. The often-quoted "54.4 vs 35.0 months, HR 0.64" is the 2018 interim. The 5-year paper has an erratum (*JAMA Oncol* 2023;9(1):151), which I did not read.
6. **Several famous trials were negative on the primary endpoint**, which is easy to overstate:
   - APACT: independent-review DFS **HR 0.88 (0.729–1.063), P = .18**. OS favoured nab-P + gem (5-year HR 0.80), but this was secondary.
   - PREOPANC (2020): OS HR 0.78 (0.58–1.05), P = .096. It became significant only at long-term follow-up: HR 0.73 (0.56–0.96), P = .025, with a **median gain of 1.4 months** (15.7 vs 14.3).
   - PREOPANC-2: neoadjuvant FOLFIRINOX **not better** than gemcitabine-based chemoradiotherapy (21.9 vs 21.3 months, HR 0.88, P = .32).
   - NORPACT-1: neoadjuvant FOLFIRINOX trended **worse** than upfront surgery (median OS 25.1 vs 38.5 months, HR 1.52 (1.00–2.33), P = .050).
   - S1505: neither perioperative arm beat the 40% two-year OS threshold.
   - LAP07: no OS benefit from chemoradiotherapy (HR 1.03) or erlotinib (HR 1.19).
   - CONKO-007: primary endpoint switched from OS to R0 rate, and it still failed (25% vs 18%, P = .113).
   - POLO: final OS not significant (19.0 vs 19.2 months, HR 0.83, P = .3487).
   - CONKO-001: OS was **not** significant in 2007 (P = .06). It became significant only in 2013 (HR 0.76).
7. **NAPOLI 3 HR differs between paper and label.** Lancet: OS HR **0.83** (0.70–0.99), P = .036; PFS HR 0.69 (0.58–0.83). FDA label: OS HR **0.84** (0.71–0.99), P = .0403; PFS HR 0.70 (0.59–0.85) [L-2025-03-03]. Cite one source consistently. The absolute OS gain is 1.9 months (11.1 vs 9.2).
8. **PA.3 (erlotinib) medians differ by source.** Abstract (all doses): 6.24 vs 5.91 months, HR 0.82 (0.69–0.99). FDA label (100 mg cohort only): 6.5 vs 6.0 months, HR 0.81 (0.68–0.97). *J Clin Oncol* 2023;41(30):4714–4720 (PMID 37847995) is a **reprint** of the 2007 paper, not new data. **Erlotinib has no pancreatic indication in Taiwan** [TFDA, Tarceva licences].
9. **JASPAC 01 median OS (46.5 vs 25.5 months) is not in the Lancet abstract.** It is confirmed only by two secondary sources [S-Ei; S-PanAsia]. The abstract gives HR 0.57 (0.44–0.72) and 5-year OS 44.1% vs 24.4%.
10. **CONKO-001 2013 abstract gives no median OS.** It gives HR 0.76 and 5- and 10-year rates only. Any "22.8 vs 20.2 months" figure is **[UNVERIFIED]** from my sources.
11. **KEYNOTE-158 pancreatic subgroup is weak and comes from a secondary source.** n = 22, ORR **18.2%**, median PFS 2.1 months, median OS 3.7 months [S-Fivaz]. The JCO 2020 Table 3 was not readable (image only; the journal site returned 403). Check before printing.
12. **New 2025–2026 data the chapter may want, beyond the brief:**
    - ESPAC-4 long-term (Palmer et al., *JCO* 2025): GemCap vs gem 31.6 vs 28.4 months, HR 0.83 (0.71–0.98).
    - Prep-02/JSAP-05 (Unno et al., *Ann Surg* 2026): neoadjuvant gemcitabine + S-1 improved OS, 37.0 vs 26.6 months, HR 0.73 (0.56–0.95). This is the positive Asian neoadjuvant trial.
    - MASTERPLAN (Oar et al., *Lancet Oncol* 2026, e-pub 2026-10-23): adding SBRT to chemotherapy reduced 12-month locoregional recurrence (20.2% vs 52.0%).
    - KRAS G12D agents: setidegrasib (*NEJM* 2026), GFH375 (*Nat Med* 2026), and HRS-4642 with chemotherapy (*Nat Med* 2026) or with adebrelimab (*Cancer Cell* 2026).
13. **Not found on PubMed as of 2026-10-29:**
    - Peer-reviewed **first-line** daraxonrasib results (a JCO 2026 commentary titled "…From Second-Line Breakthrough to First-Line Evidence", PMID 42691452, has no abstract).
    - Alliance A021806 results (only a 2024 protocol commentary).
    - PREOPANC-3 results (protocol only, 2023).
    - Peer-reviewed phase 3 data for elironrasib or zoldonrasib in PDAC.
14. **Errata exist. Check them before quoting a number:**
    - PRODIGE 24 5-year (*JAMA Oncol* 2023)
    - S1505 (*JAMA Oncol* 2024;10(4):541)
    - NAPOLI-1 (*Lancet* 2016;387(10018):536)
    - POLO OS (*JCO* 2024;42(17):2112)
    - CONKO-007 (*JCO* 2026;44(5):430; PMID 41505667)
    - Entrectinib NTRK pooled analysis (4 errata, 2020–2021)

    I did not read what any erratum changes (the publisher sites return 403).

---

# A. ADJUVANT (resected PDAC)

## 1. CONKO-001 (gemcitabine vs observation) — [VERIFIED]

**References**
- Oettle, H., Post, S., Neuhaus, P., Gellert, K., Langrehr, J., Ridwelski, K., Schramm, H., Fahlke, J., Zuelke, C., Burkart, C., Gutberlet, K., Kettner, E., Schmalenberg, H., Weigang-Koehler, K., Bechstein, W. O., Niedergethmann, M., Schmidt-Wolf, I., Roll, L., Doerken, B., & Riess, H. (2007). Adjuvant chemotherapy with gemcitabine vs observation in patients undergoing curative-intent resection of pancreatic cancer: A randomized controlled trial. *JAMA*, *297*(3), 267–277. https://doi.org/10.1001/jama.297.3.267 — PMID 17227978
- (Long-term) Oettle, H., Neuhaus, P., Hochhaus, A., Hartmann, J. T., Gellert, K., Ridwelski, K., Niedergethmann, M., Zülke, C., Fahlke, J., Arning, M. B., Sinn, M., Hinke, A., & Riess, H. (2013). Adjuvant chemotherapy with gemcitabine and long-term outcomes among patients with resected pancreatic cancer: The CONKO-001 randomized trial. *JAMA*, *310*(14), 1473–1481. https://doi.org/10.1001/jama.2013.279201 — PMID 24104372

**Design:** Phase 3, open-label, multicentre (88 centres, Germany and Austria), 1998–2004 [A].
**Population:** Gross complete (R0 or R1) resection of pancreatic cancer, no prior radiotherapy or chemotherapy. 368 randomized, 354 eligible for ITT. More than 80% had R0 resection [A].
**Arms:** Gemcitabine 1000 mg/m² on days 1, 8 and 15 every 4 weeks for 6 cycles (6 months), n = 179, vs observation, n = 175 [A 2007; dose from A 2013].
**Primary endpoint (DFS):**
- 2007: 13.4 months (95% CI 11.4–15.3) vs 6.9 months (6.1–7.8), P < .001 [A]
- 2013 (median follow-up 136 months): 13.4 (11.6–15.3) vs 6.7 (6.0–7.5), **HR 0.55 (0.44–0.69)**, P < .001 [A]

**OS:**
- 2007: 22.1 (18.4–25.8) vs 20.2 (17–23.4) months, **P = .06 (not significant)** [A]
- 2013: **HR 0.76 (0.61–0.95)**, P = .01. 5-year OS 20.7% vs 10.4%; 10-year OS 12.2% vs 7.7% [A]. The 2013 abstract gives no median OS (**[UNVERIFIED]**).

**Toxicity:** "Grade 3 or 4 toxicities rarely occurred", and quality of life did not differ (Spitzer index) [A 2007]. Exact rates **[UNVERIFIED]** (JAMA full text not in PMC).

## 2. ESPAC-4 (gemcitabine + capecitabine vs gemcitabine) — [VERIFIED] (toxicity [PARTIAL])

**References**
- Neoptolemos, J. P., Palmer, D. H., Ghaneh, P., Psarelli, E. E., Valle, J. W., Halloran, C. M., Faluyi, O., O'Reilly, D. A., Cunningham, D., Wadsley, J., Darby, S., Meyer, T., Gillmore, R., Anthoney, A., Lind, P., Glimelius, B., Falk, S., Izbicki, J. R., Middleton, G. W., . . . Büchler, M. W. (2017). Comparison of adjuvant gemcitabine and capecitabine with gemcitabine monotherapy in patients with resected pancreatic cancer (ESPAC-4): A multicentre, open-label, randomised, phase 3 trial. *The Lancet*, *389*(10073), 1011–1024. https://doi.org/10.1016/S0140-6736(16)32409-6 — PMID 28129987
- (Long-term) Palmer, D. H., Jackson, R., Springfeld, C., Ghaneh, P., Rawcliffe, C., Halloran, C. M., Faluyi, O., Cunningham, D., Wadsley, J., Darby, S., Meyer, T., Gillmore, R., Lind, P., Glimelius, B., Falk, S., Ma, Y. T., Middleton, G. W., Cummins, S., Ross, P. J., . . . Neoptolemos, J. P. (2025). Pancreatic adenocarcinoma: Long-term outcomes of adjuvant therapy in the ESPAC4 phase III trial. *Journal of Clinical Oncology*, *43*(10), 1240–1253. https://doi.org/10.1200/JCO.24.01118 — PMID 39637340

**Design:** Phase 3, open-label, 92 hospitals in the UK, Germany, France and Sweden [A].
**Population:** Age ≥18, macroscopic complete resection (R0 or R1) of PDAC, randomized within 12 weeks of surgery. 732 enrolled, 730 analysed (gemcitabine 366, GemCap 364) [A].
**Arms (6 cycles of 4 weeks):** Gemcitabine 1000 mg/m² weekly × 3 every 4 weeks, ± oral capecitabine 1660 mg/m²/day for 21 days then 7 days off [A].
**Primary endpoint (OS):** 28.0 months (95% CI 23.5–31.5) vs 25.5 (22.7–27.9), **HR 0.82 (0.68–0.98)**, P = .032. Reported at 458 deaths (95% of the 480 target) on the data monitoring committee's request [A].
**Long-term (median follow-up 104 months, 566 deaths):**
- OS 31.6 (26.5–38.0) vs 28.4 (25.2–32.0) months, **HR 0.83 (0.71–0.98)**, P = .031 [A 2025]
- R0 subgroup: 49.9 vs 32.2 months, HR 0.63 (0.47–0.84) [A 2025]
- In the 193 patients (26.4%) who would **not** have been eligible for PRODIGE 24, GemCap still helped: 25.9 vs 20.7 months, HR 0.71 (0.52–0.98) [A 2025]

**Toxicity:** 608 grade 3–4 events in 226 of 359 patients (GemCap) vs 481 events in 196 of 366 (gemcitabine) [A]. Grade 3–4 rates, GemCap vs gemcitabine [S-deJesus Table 5]:
- neutropenia 38.2% vs 24.3%
- diarrhoea 5.3% vs 1.6%
- hand-foot syndrome 7.2% vs 0%
- fatigue 5.6% vs 5.2%

## 3. PRODIGE 24 / CCTG PA.6 (modified FOLFIRINOX vs gemcitabine) — [VERIFIED] (toxicity detail [PARTIAL])

**References**
- Conroy, T., Hammel, P., Hebbar, M., Ben Abdelghani, M., Wei, A. C., Raoul, J. L., Choné, L., Francois, E., Artru, P., Biagi, J. J., Lecomte, T., Assenat, E., Faroux, R., Ychou, M., Volet, J., Sauvanet, A., Breysacher, G., Di Fiore, F., Cripps, C., . . . Bachet, J. B. (2018). FOLFIRINOX or gemcitabine as adjuvant therapy for pancreatic cancer. *The New England Journal of Medicine*, *379*(25), 2395–2406. https://doi.org/10.1056/NEJMoa1809775 — PMID 30575490
- (5-year) Conroy, T., Castan, F., Lopez, A., Turpin, A., Ben Abdelghani, M., Wei, A. C., Mitry, E., Biagi, J. J., Evesque, L., Artru, P., Lecomte, T., Assenat, E., Bauguion, L., Ychou, M., Bouché, O., Monard, L., Lambert, A., & Hammel, P. (2022). Five-year outcomes of FOLFIRINOX vs gemcitabine as adjuvant therapy for pancreatic cancer: A randomized clinical trial. *JAMA Oncology*, *8*(11), 1571–1578. https://doi.org/10.1001/jamaoncol.2022.3829 — PMID 36048453 (erratum: *JAMA Oncol* 2023;9(1):151)

**Design:** Phase 3, open-label, 77 hospitals in France and Canada, 2012–2016 [A 2022].
**Population:** Age 18–79, PDAC with R0 or R1 resection 3 to 12 weeks before randomization; n = 493 [A 2022]. Other entry criteria [S-ESPAC4LT]:
- postoperative CA19-9 ≤180 kU/L
- WHO PS 0–1
- platelets ≥100,000/mm³
- bilirubin ≤1.5 × ULN
- no significant cardiovascular disease

**Arms (24 weeks):**
- mFOLFIRINOX every 2 weeks: oxaliplatin 85 mg/m², irinotecan 180 mg/m² (reduced to **150 mg/m²** after a protocol safety analysis), leucovorin 400 mg/m², 5-FU 2400 mg/m² over 46 h, **with no 5-FU bolus** [A 2018]
- Gemcitabine 1000 mg/m² on days 1, 8 and 15 every 4 weeks [A 2018]

**Primary endpoint (DFS):**

| Analysis | DFS mFFX vs gem | HR (95% CI) | OS mFFX vs gem | HR (95% CI) |
|---|---|---|---|---|
| 2018 (median follow-up 33.6 months) [A] | 21.6 vs 12.8 months | 0.58 (0.46–0.73) | 54.4 vs 35.0 months | 0.64 (0.48–0.86) |
| **2022, 5-year (median follow-up 69.7 months)** [A] | **21.4 (17.5–26.7) vs 12.8 (11.6–15.2)** | **0.66 (0.54–0.82)** | **53.5 (43.5–58.4) vs 35.5 (30.1–40.3)** | **0.68 (0.54–0.85)** |

Other results:
- 2018: 3-year DFS 39.7% vs 21.4%; 3-year OS 63.4% vs 48.6% [A]
- 2022: 5-year DFS 26.1% vs 19.0%; 5-year OS 43.2% vs 31.4%; metastasis-free survival 29.4 vs 17.7 months (HR 0.64); cancer-specific survival 54.7 vs 36.3 months (HR 0.65) [A]

**Toxicity:** Grade 3–4 adverse events 75.9% vs 52.9%. One toxic death (interstitial pneumonitis) occurred, in the gemcitabine arm [A]. Grade 3–4 rates, mFFX vs gemcitabine [S-deJesus Table 5]:
- diarrhoea 18.6% vs 3.7%
- neutropenia 28.4% vs 26.0%
- fatigue 11.0% vs 4.6%
- peripheral neuropathy 9.3% vs 0%
- nausea 5.5% vs 0.8%
- vomiting 5.1% vs 1.2%
- mucositis 2.5% vs 0%

## 4. APACT (adjuvant nab-paclitaxel + gemcitabine vs gemcitabine) — [VERIFIED]

**Reference**
- Tempero, M. A., Pelzer, U., O'Reilly, E. M., Winter, J., Oh, D. Y., Li, C. P., Tortora, G., Chang, H. M., Lopez, C. D., Bekaii-Saab, T., Ko, A. H., Santoro, A., Park, J. O., Noel, M. S., Frassineti, G. L., Shan, Y. S., Dean, A., Riess, H., Van Cutsem, E., . . . Reni, M. (2023). Adjuvant nab-paclitaxel + gemcitabine in resected pancreatic ductal adenocarcinoma: Results from a randomized, open-label, phase III trial. *Journal of Clinical Oncology*, *41*(11), 2007–2019. https://doi.org/10.1200/JCO.22.01134 — PMID 36521097 (e-pub 2022-12-15)

**Design:** Phase 3, open-label, 160 sites in 21 countries, enrolled 2014–2016 [FT]. Patients came from Europe 47%, North America 35%, Asia 12% and Australia 6%. Investigators from Taiwan took part (Taipei Veterans General Hospital; National Cheng Kung University Hospital) [PubMed affiliations].
**Population:** 866 treatment-naive patients after macroscopic complete resection, ECOG ≤1 [FT]. Other criteria [FT]:
- **CA19-9 <100 U/mL**
- adjuvant therapy started ≤12 weeks after surgery
- stratified by R0/R1, node status and region

Baseline: R0 76%, node-positive 72% [FT].
**Arms:** Nab-paclitaxel 125 mg/m² + gemcitabine 1000 mg/m² (each given IV over 30–40 minutes) vs gemcitabine 1000 mg/m², on days 1, 8 and 15 of six 28-day cycles [FT].
**Primary endpoint (independently assessed DFS):** 19.4 vs 18.8 months, **HR 0.88 (0.729–1.063), P = .18 — NOT MET** [A].
**Secondary endpoints [A]:**
- Investigator-assessed DFS: 16.6 vs 13.7 months, HR 0.82 (0.694–0.965)
- OS, primary cut-off: 40.5 vs 36.2 months, HR 0.82 (0.680–0.996)
- OS, 5-year follow-up: 41.8 vs 37.7 months, HR 0.80 (0.678–0.947), P = .0091

**Toxicity:** Grade ≥3 treatment-emergent AEs 86% vs 68%; serious AEs 41% vs 23%; 2 treatment-related deaths per arm [FT]. Grade ≥3 rates, combination vs gemcitabine [FT]:
- neutropenia 49% vs 43%
- anaemia 15% vs 8%
- fatigue 10% vs 3%
- **peripheral neuropathy 15% vs 0%** (62% of episodes began in cycle 4 or later)
- febrile neutropenia 5% vs 1%

G-CSF was used in 35% vs 21% [FT].
**Handbook point:** APACT is often cited as "positive" because of OS. Its primary endpoint failed, and nab-P + gem is not a standard adjuvant regimen.

## 5. JASPAC 01 (S-1 vs gemcitabine, Japan) — [PARTIAL] (median OS secondary only)

**Reference**
- Uesaka, K., Boku, N., Fukutomi, A., Okamura, Y., Konishi, M., Matsumoto, I., Kaneoka, Y., Shimizu, Y., Nakamori, S., Sakamoto, H., Morinaga, S., Kainuma, O., Imai, K., Sata, N., Hishinuma, S., Ojima, H., Yamaguchi, R., Hirano, S., Sudo, T., & Ohashi, Y. (2016). Adjuvant chemotherapy of S-1 versus gemcitabine for resected pancreatic cancer: A phase 3, open-label, randomised, non-inferiority trial (JASPAC 01). *The Lancet*, *388*(10041), 248–257. https://doi.org/10.1016/S0140-6736(16)30583-9 — PMID 27265347

**Design:** Phase 3, open-label, **non-inferiority**, 33 hospitals in Japan, 2007–2010. Non-inferiority margin was HR 1.25 [A].
**Population:** Age ≥20, pathologic stage I–III invasive ductal carcinoma. The abstract says "no local residual or microscopic residual tumour", yet randomization balanced "residual tumour status". Whether R1 resection was eligible needs the full text (**[UNVERIFIED]**). 385 randomized (gemcitabine 193, S-1 192); per-protocol 190 vs 187 [A].
**Arms:**
- Gemcitabine 1000 mg/m² on days 1, 8 and 15 every 4 weeks, up to 6 cycles [A]
- **S-1 40, 50 or 60 mg by body-surface area, orally twice daily for 28 days, then 14 days off (6-week cycle), up to 4 cycles** [A]

**Primary endpoint (OS):** HR **0.57 (0.44–0.72)**; P < .0001 for non-inferiority and P < .0001 for superiority. 5-year OS 44.1% (36.9–51.1) with S-1 vs 24.4% (18.6–30.8) with gemcitabine [A]. **Median OS 46.5 vs 25.5 months** [S-Ei; S-PanAsia; not in the abstract].
**Toxicity:** Grade 3–4 leucopenia, neutropenia and raised AST/ALT were more frequent with gemcitabine; stomatitis and diarrhoea were more frequent with S-1 [A]. Early discontinuation was 42% (gemcitabine) vs 28% (S-1) [S-Ei].
**Taiwan:** The S-1 licence (TS-1 愛斯萬) covers locally advanced or metastatic pancreatic cancer only, not adjuvant use [TFDA]. See flag 2.

---

# B. NEOADJUVANT / PERIOPERATIVE (resectable and borderline resectable)

## 6. PREOPANC (gemcitabine-based chemoradiotherapy vs upfront surgery) — [VERIFIED]

**References**
- Versteijne, E., Suker, M., Groothuis, K., Akkermans-Vogelaar, J. M., Besselink, M. G., Bonsing, B. A., Buijsen, J., Busch, O. R., Creemers, G. M., van Dam, R. M., Eskens, F. A. L. M., Festen, S., de Groot, J. W. B., Groot Koerkamp, B., de Hingh, I. H., Homs, M. Y. V., van Hooft, J. E., Kerver, E. D., Luelmo, S. A. C., . . . van Tienhoven, G. (2020). Preoperative chemoradiotherapy versus immediate surgery for resectable and borderline resectable pancreatic cancer: Results of the Dutch randomized phase III PREOPANC trial. *Journal of Clinical Oncology*, *38*(16), 1763–1773. https://doi.org/10.1200/JCO.19.02274 — PMID 32105518
- (Long-term) Versteijne, E., van Dam, J. L., Suker, M., Janssen, Q. P., Groothuis, K., Akkermans-Vogelaar, J. M., Besselink, M. G., Bonsing, B. A., Buijsen, J., Busch, O. R., Creemers, G. M., van Dam, R. M., Eskens, F. A. L. M., Festen, S., de Groot, J. W. B., Groot Koerkamp, B., de Hingh, I. H., Homs, M. Y. V., van Hooft, J. E., . . . van Eijck, C. H. J. (2022). Neoadjuvant chemoradiotherapy versus upfront surgery for resectable and borderline resectable pancreatic cancer: Long-term results of the Dutch randomized PREOPANC trial. *Journal of Clinical Oncology*, *40*(11), 1220–1230. https://doi.org/10.1200/JCO.21.02233 — PMID 35084987

**Design:** Phase 3, 16 Dutch centres, 2013–2017 [A].
**Population:** Resectable or borderline resectable PDAC; 246 eligible (chemoradiotherapy 119, surgery 127) [A].
**Arms:**
- Neoadjuvant: 3 courses of gemcitabine, with **36 Gy in 15 fractions (2.4 Gy each)** during the second course, then surgery, then 4 courses of adjuvant gemcitabine [A]
- Control: immediate surgery, then 6 courses of adjuvant gemcitabine [A]

**Primary endpoint (OS by ITT):**
- 2020: 16.0 vs 14.3 months, **HR 0.78 (0.58–1.05), P = .096 — not significant** [A]
- 2022 (median follow-up 59 months): **HR 0.73 (0.56–0.96), P = .025**; median 15.7 vs 14.3 months; 5-year OS **20.5% (14.2–29.8) vs 6.5% (3.1–13.7)** [A]

**Secondary endpoints:** Resection rate 61% vs 72% (P = .058). R0 rate among resected patients 71% (51 of 72) vs 40% (37 of 92), P < .001 [A].
**Toxicity:** Serious AEs 52% vs 41% (P = .096) [A]. No safety data were collected after the first report [A 2022].

## 7. PREOPANC-2 (neoadjuvant FOLFIRINOX vs neoadjuvant gemcitabine-chemoradiotherapy) — [VERIFIED]

**Reference**
- Janssen, Q. P., van Dam, J. L., van Bekkum, M. L., Bonsing, B. A., Bos, H., Bosscha, K. P., Bouwense, S. A. W., Brouwer-Hol, L., Bruynzeel, A. M. E., Busch, O. R., Coene, P. L. O., van Eijck, C. H. J., de Groot, J. W. B., Haberkorn, B. C. M., de Hingh, I. H. J. T., Karsten, T. M., Kazemier, G., van der Kolk, M. B., Liem, M. S. L., . . . Groot Koerkamp, B. (2025). Neoadjuvant FOLFIRINOX versus neoadjuvant gemcitabine-based chemoradiotherapy in resectable and borderline resectable pancreatic cancer (PREOPANC-2): A multicentre, open-label, phase 3 randomised trial. *The Lancet Oncology*, *26*(10), 1346–1356. https://doi.org/10.1016/S1470-2045(25)00363-8 — PMID 40945523 (e-pub 2025-09-10). Correspondence was published in *Lancet Oncol* 2026;27:e3–e6.

**Design:** Phase 3, open-label, 19 Dutch centres, 2018–2021 [A].
**Population:** Resectable or borderline resectable PDAC, WHO PS 0–1. 375 randomized (FFX 188, CRT 187); 369 in the modified ITT analysis [A].
**Arms:**
- FFX arm: **8 cycles of full-dose FOLFIRINOX** every 14 days (oxaliplatin 85, irinotecan 180, leucovorin 400 mg/m², 5-FU 400 mg/m² bolus then 2400 mg/m² over 46 h), then surgery, **with no adjuvant therapy** [A]
- CRT arm: 3 cycles of gemcitabine 1000 mg/m² (days 1, 8 and 15; days 1 and 8 only in cycles 1 and 3) with 36 Gy in 15 fractions in cycle 2, then surgery, then 4 cycles of adjuvant gemcitabine [A]

**Primary endpoint (OS, median follow-up 42.3 months):** 21.9 (17.7–27.0) vs 21.3 (16.8–25.5) months, **HR 0.88 (0.69–1.13), P = .32 — negative** [A].
**Toxicity:**
- Grade ≥3 AEs 67% vs 60%; serious AEs 49% vs 43% [A]
- Grade 3–4 neutropenia 25% vs 22%; **diarrhoea 23% vs 1%**; leukopenia 8% vs 15% [A]
- Treatment-related deaths: 2 with FFX (multi-organ failure, intestinal mucositis) vs 1 with CRT (upper GI haemorrhage) [A]
- A separate thromboembolism analysis exists: Willems et al., *JCO* 2026;44:662–675, PMID 41610374 (not read)

## 8. Alliance A021501 (borderline resectable: mFOLFIRINOX ± hypofractionated RT) — [VERIFIED]

**References**
- Katz, M. H. G., Shi, Q., Meyers, J., Herman, J. M., Chuong, M., Wolpin, B. M., Ahmad, S., Marsh, R., Schwartz, L., Behr, S., Frankel, W. L., Collisson, E., Leenstra, J., Williams, T. M., Vaccaro, G., Venook, A., Meyerhardt, J. A., & O'Reilly, E. M. (2022). Efficacy of preoperative mFOLFIRINOX vs mFOLFIRINOX plus hypofractionated radiotherapy for borderline resectable adenocarcinoma of the pancreas: The A021501 phase 2 randomized clinical trial. *JAMA Oncology*, *8*(9), 1263–1270. https://doi.org/10.1001/jamaoncol.2022.2319 — PMID 35834226
- (Postoperative AEs) Snyder, R. A., Zemla, T. J., Shi, Q., Segovia, D., Ahmad, S. A., O'Reilly, E. M., Herman, J. M., & Katz, M. H. G. (2024). Postoperative adverse events following neoadjuvant therapy and surgery for borderline resectable pancreatic cancer in a phase 2 clinical trial (Alliance A021501). *Annals of Surgical Oncology*, *31*(10), 7033–7042. https://doi.org/10.1245/s10434-024-15670-6 — PMID 39008208

**Design:** Randomized phase 2 in the US National Clinical Trials Network, 2017–2019. Each arm was compared with a historical 18-month OS of 50% [A].
**Population:** Borderline resectable PDAC; 126 patients (arm 1: 70, of whom 54 randomized and 16 added after arm 2 closed; arm 2: 56) [A].
**Arms:**
- Arm 1: **8 cycles of mFOLFIRINOX** every 2 weeks (oxaliplatin 85, irinotecan 180, leucovorin 400 mg/m², infusional 5-FU 2400 mg/m² over 46 h) [A]
- Arm 2: 7 cycles of mFOLFIRINOX, then **SBRT 33–40 Gy in 5 fractions** or hypofractionated image-guided RT 25 Gy in 5 fractions [A]
- Both arms: pancreatectomy, then **4 cycles of mFOLFOX6** [A]

**Interim analysis:** R0 resection in the first 30 patients per arm was 57% (arm 1) vs 33% (arm 2), so **arm 2 was closed** [A].
**Primary endpoint (18-month OS):** Arm 1 **66.7% (56.1–79.4)** vs arm 2 47.3% (35.8–62.5). Median OS 29.8 (21.1–36.6) vs 17.1 (12.8–24.4) months [A].
**Toxicity / surgery:** 51 of 126 patients (40%) underwent pancreatectomy. Grade ≥3 postoperative AEs occurred in 56%, 90-day mortality was 2.0%, and readmission was 16% vs 42% [A Snyder 2024]. Chemotherapy-phase grade 3–4 rates **[UNVERIFIED]**: the PMC copy has only the abstract.

## 9. NORPACT-1 (neoadjuvant FOLFIRINOX vs upfront surgery, resectable pancreatic head) — [VERIFIED]

**Reference**
- Labori, K. J., Bratlie, S. O., Andersson, B., Angelsen, J. H., Biörserud, C., Björnsson, B., Bringeland, E. A., Elander, N., Garresori, H., Grønbech, J. E., Haux, J., Hemmingsson, O., Liljefors, M. G., Myklebust, T. Å., Nymo, L. S., Peltola, K., Pfeiffer, P., Sallinen, V., Sandström, P., . . . Lassen, K. (2024). Neoadjuvant FOLFIRINOX versus upfront surgery for resectable pancreatic head cancer (NORPACT-1): A multicentre, randomised, phase 2 trial. *The Lancet Gastroenterology & Hepatology*, *9*(3), 205–217. https://doi.org/10.1016/S2468-1253(23)00405-3 — PMID 38237621

**Design:** Phase 2, 12 hospitals in Denmark, Finland, Norway and Sweden, 2017–2021 [A].
**Population:** Resectable tumour of the pancreatic head, radiologically strongly suspected PDAC, WHO PS 0–1. 140 randomized (neoadjuvant 77, surgery 63), at a 3:2 ratio until October 2018 and 1:1 after [A].
**Arms:**
- Neoadjuvant: **4 cycles of FOLFIRINOX** (oxaliplatin 85, irinotecan 180, leucovorin 400 mg/m², 5-FU 400 mg/m² bolus then 2400 mg/m² over 46 h, every 14 days), then surgery and adjuvant chemotherapy [A]
- Upfront surgery, then adjuvant chemotherapy [A]
- Adjuvant therapy was GemCap at first, with modified FFX permitted after a protocol amendment [A]

**Primary endpoint (18-month OS, ITT):** **60% (49–71) vs 73% (62–84), P = .032 — favouring upfront surgery**. Median OS 25.1 (17.2–34.9) vs 38.5 (27.6–NR) months, **HR 1.52 (1.00–2.33)**, P = .050 [A].
**Other results:**
- Only 61 of 77 patients (79%) in the neoadjuvant arm actually received neoadjuvant therapy [A]
- Resection rate 82% vs 89% [A]

**Toxicity:**
- Grade ≥3 AEs 58% vs 40% [A]
- Two deaths after cycle 1 (one sudden death of unknown cause, one COVID-19) [A]
- During adjuvant therapy, grade ≥3 neutropenia occurred in 22% vs 11% [A]

## 10. Prep-02/JSAP-05 (neoadjuvant gemcitabine + S-1 vs upfront surgery, Japan) — [VERIFIED]

**Reference**
- Unno, M., Motoi, F., Matsuyama, Y., Satoi, S., Toyama, H., Matsumoto, I., Aosasa, S., Shirakawa, H., Wada, K., Fujii, T., Yoshitomi, H., Takahashi, S., Sho, M., Ueno, H., & Kosuge, T. (2026). Neoadjuvant chemotherapy with gemcitabine and S-1 versus upfront surgery for resectable pancreatic cancer: Results of the randomized phase II/III Prep-02/JSAP05 trial. *Annals of Surgery*, *283*(1), 57–64. https://doi.org/10.1097/SLA.0000000000006730 — PMID 40235447 (e-pub 2025-04-16; PMC12695294)
- (Protocol) Motoi et al., *Jpn J Clin Oncol* 2019;49:190–194, PMID 30608598 (citation only, not read)

**Design:** Randomized phase II/III in Japan. The phase II primary endpoint was resection rate; the phase III primary endpoint was OS [A].
**Population:** Resectable PDAC **without arterial abutment**, ECOG 0–1; 364 randomized (182 per arm) [A].
**Arms:**
- Neoadjuvant: **gemcitabine 1000 mg/m² on days 1 and 8 + S-1 40–60 mg orally twice daily on days 1–14, every 3 weeks for 2 cycles** [A], then surgery
- Control: upfront surgery
- Both arms were advised to take **adjuvant S-1 for 6 months**, starting within 10 weeks of surgery [FT]

**Primary endpoint (OS):** **37.0 (28.6–43.3) vs 26.6 (21.5–31.5) months, HR 0.73 (0.56–0.95), P = .018** [A]. RFS 14.3 vs 11.3 months, HR 0.77 (0.61–0.98) [A].
**Surgery:** 157 resected after neoadjuvant therapy vs 156 with upfront surgery [FT]. Neoadjuvant vs upfront surgery [FT]:
- R0 91.1% vs 85.9%
- **pN1 59.2% vs 81.4%** (P < .01)
- no operative deaths in either arm

**Toxicity (neoadjuvant arm):** Grade 3 AEs 48.8%, grade 4 AEs 23.8% (grade 4 neutropenia 22.7%). Grade 3 events seen in more than 5% of patients: neutropenia, leukopenia, rash, appetite loss, febrile neutropenia and stomatitis [FT].

## 11. SWOG S1505 (perioperative mFOLFIRINOX vs gemcitabine/nab-paclitaxel) — [VERIFIED] (doses [UNVERIFIED])

**References**
- Sohal, D. P. S., Duong, M., Ahmad, S. A., Gandhi, N. S., Beg, M. S., Wang-Gillam, A., Wade, J. L., Chiorean, E. G., Guthrie, K. A., Lowy, A. M., Philip, P. A., & Hochster, H. S. (2021). Efficacy of perioperative chemotherapy for resectable pancreatic adenocarcinoma: A phase 2 randomized clinical trial. *JAMA Oncology*, *7*(3), 421–427. https://doi.org/10.1001/jamaoncol.2020.7328 — PMID 33475684 (erratum: *JAMA Oncol* 2024;10(4):541)
- (Surgical outcomes) Ahmad, S. A., Duong, M., Sohal, D. P. S., Gandhi, N. S., Beg, M. S., Wang-Gillam, A., Wade, J. L., Chiorean, E. G., Guthrie, K. A., Lowy, A. M., Philip, P. A., & Hochster, H. S. (2020). Surgical outcome results from SWOG S1505: A randomized clinical trial of mFOLFIRINOX versus gemcitabine/nab-paclitaxel for perioperative treatment of resectable pancreatic ductal adenocarcinoma. *Annals of Surgery*, *272*(3), 481–486. https://doi.org/10.1097/SLA.0000000000004155 — PMID 32740235

**Design:** Randomized phase 2, "pick-the-winner" design [A].
**Population:** Resectable PDA by Intergroup criteria, Zubrod PS 0–1. 147 enrolled, but **43 (29%) were ineligible on central radiology review**. 102 were eligible and evaluable (mFFX 55, GnP 47) [A].
**Arms:** 12 weeks of chemotherapy before and 12 weeks after surgery, with either mFOLFIRINOX or gemcitabine/nab-paclitaxel. Doses are not in the abstract (**[UNVERIFIED]**).
**Primary endpoint (2-year OS):** 47% (31–61) vs 48% (31–63). **Neither arm beat the a priori threshold of 40%**. Median OS 23.2 (17.6–45.9) vs 23.6 (17.8–31.7) months [A].
**Other results:**
- Resection 73% vs 70%; all treatment completed by 49% vs 40%; DFS after resection 10.9 vs 14.2 months [A]
- Among 77 operated patients: R0 85%, complete or major pathologic response 33%, grade 3–5 postoperative complications 16% [A Ahmad 2020]

**Toxicity:** "Expected hematologic toxic effects, fatigue, and gastrointestinal toxicities." Rates **[UNVERIFIED]**.

## 12. MASTERPLAN (new, 2026; SBRT added to perioperative chemotherapy) — [VERIFIED]

**Reference**
- Oar, A., Kneebone, A., Sjoquist, K. M., Espinoza, D., Lee, M., Le, H., Gholamrezaei, L., Chu, J., Lynam, J., Mallesara, G., Lee, D., Vignarajah, D., Ward, I., Samra, J., Barbour, A., Whitehead, A., Brooks, S., Nicholson, A., Wang, T. W., . . . Goldstein, D. (2026). Perioperative chemotherapy and stereotactic body radiotherapy versus perioperative chemotherapy alone in patients with high-risk, localised pancreatic cancer (MASTERPLAN): An open-label, phase 2, multicentre, randomised trial of the Australasian Gastro-Intestinal Trials Group. *The Lancet Oncology*. Advance online publication. https://doi.org/10.1016/S1470-2045(26)00532-2 — PMID 42914998 (e-pub 2026-10-23)

**Design:** Phase 2, open-label, 14 hospitals in Australia and New Zealand, 2:1 randomization. It closed early (74 of the planned 120 patients) [A].
**Population:** Localised PDAC with at least one high-risk feature: tumour >4 cm, extrapancreatic extension, N+, borderline resectable or locally advanced [A].
**Arms:**
- Chemotherapy: mFOLFIRINOX (oxaliplatin 85, irinotecan 150 mg/m², leucovorin 50 mg, 5-FU 2400 mg/m² over 46 h, ×6) or GnP (×3), with or without **SBRT 40 Gy in 5 fractions** [A]
- Then surgery, followed by 12 more weeks of chemotherapy [A]

**Primary endpoint (12-month locoregional recurrence):** 20.2% (9.9–33.1) vs 52.0% (30.3–69.9), sub-distribution HR 0.44 (0.22–0.88), P = .022 [A].
**Toxicity:** Grade ≥3 AEs 70% vs 64%. SBRT-related serious AEs: one grade 2 small-bowel obstruction and one grade 3 pancreatitis [A]. This is a phase 2 trial with a locoregional endpoint, not OS.

---

# C. LOCALLY ADVANCED

## 13. LAP07 (chemoradiotherapy vs chemotherapy after 4 months of induction; erlotinib) — [VERIFIED]

**Reference**
- Hammel, P., Huguet, F., van Laethem, J. L., Goldstein, D., Glimelius, B., Artru, P., Borbath, I., Bouché, O., Shannon, J., André, T., Mineur, L., Chibaudel, B., Bonnetain, F., & Louvet, C. (2016). Effect of chemoradiotherapy vs chemotherapy on survival in patients with locally advanced pancreatic cancer controlled after 4 months of gemcitabine with or without erlotinib: The LAP07 randomized clinical trial. *JAMA*, *315*(17), 1844–1853. https://doi.org/10.1001/jama.2016.4324 — PMID 27139057

**Design:** Phase 3, international, open-label, two randomizations, 2008–2011 [A].
**Population:** Locally advanced PDAC; 449 enrolled, 442 in the first randomization, 269 in the second (progression-free after 4 months) [A].
**Arms:**
- First randomization: gemcitabine 1000 mg/m² weekly (n = 223) vs gemcitabine + **erlotinib 100 mg/day** (n = 219) [A]
- Second randomization: 2 more months of the same chemotherapy (n = 136) vs **chemoradiotherapy 54 Gy + capecitabine** (n = 133). The capecitabine dose is not in the abstract (**[UNVERIFIED]**) [A]

**Primary endpoint (OS from the first randomization):** The trial stopped at the interim analysis for futility [A].
- Chemotherapy 16.5 (14.5–18.5) vs chemoradiotherapy 15.2 (13.9–17.3) months, **HR 1.03 (0.79–1.34), P = .83** [A]
- Gemcitabine 13.6 vs gemcitabine + erlotinib 11.9 months, **HR 1.19 (0.97–1.45), P = .09** [A]

**Toxicity / other:** Chemoradiotherapy reduced local progression (32% vs 46%, P = .03). It did not increase grade 3–4 toxicity except nausea [A].

## 14. CONKO-007 (chemoradiotherapy vs chemotherapy after induction; published 2025) — [VERIFIED] (erratum unread)

**References**
- Fietkau, R., Ghadimi, M., Grützmann, R., Wittel, U. A., Jacobasch, L., Uhl, W., Croner, R. S., Bechstein, W. O., Neumann, U. P., Waldschmidt, D., Boeck, S., Moosmann, N., Reinacher-Schick, A. C., Golcher, H., Adler, W., Semrau, S., Lubgan, D., Kallies, A., Hecht, M., . . . Oettle, H. (2025). Benefit of chemoradiotherapy versus chemotherapy after induction therapy for conversion of unresectable into resectable pancreatic cancer: The randomized CONKO-007 trial. *Journal of Clinical Oncology*, *43*(30), 3266–3278. https://doi.org/10.1200/JCO-24-01502 — PMID 40802908
- (Erratum) Fietkau, R., Ghadimi, M., Grützmann, R., Wittel, U. A., Jacobasch, L., Uhl, W., Croner, R. S., Bechstein, W. O., Neumann, U. P., Waldschmidt, D., Boeck, S., Moosmann, N., Reinacher-Schick, A. C., Golcher, H., Adler, W., Semrau, S., Lubgan, D., Kallies, A., Hecht, M., . . . Oettle, H. (2026). Erratum: Benefit of chemoradiotherapy versus chemotherapy after induction therapy for conversion of unresectable into resectable pancreatic cancer: The randomized CONKO-007 trial. *Journal of Clinical Oncology*, *44*(5), 430. https://doi.org/10.1200/JCO-25-03004 — PMID 41505667 (**content not read**)

**Design:** Phase 3, investigator-initiated, open-label, multicentre (Germany). After an interim analysis, slow accrual led the investigators to **change the primary endpoint from OS to overall R0 resection rate** [A].
**Population:** 525 patients with unresectable tumours enrolled. 495 received 3 months of induction (FOLFIRINOX 402, gemcitabine 93). 336 without progression were randomized [A].
**Arms:** Continue the same chemotherapy (n = 167) vs **chemoradiotherapy 50.4 Gy with concurrent gemcitabine** (n = 169). A central surgical panel reassessed resectability [A].
**Primary endpoint (overall R0 rate):** **25% (43 of 169) vs 18% (30 of 167), P = .113 — not met** [A].
**Secondary endpoints [A]:**
- Surgery rate similar (P = .91)
- R0 among operated patients 69.4% vs 50.0% (P = .04)
- **OS HR 0.937 (0.747–1.174), P = .57**; median follow-up 76 months
- Surgery itself was associated with longer OS (HR 0.525) — non-randomized comparison

**Toxicity:** Not in the abstract (**[UNVERIFIED]**).

---

# D. METASTATIC — CHEMOTHERAPY BACKBONES

## 15. PRODIGE 4 / ACCORD 11 (FOLFIRINOX vs gemcitabine) — [VERIFIED] (toxicity detail [PARTIAL])

**Reference**
- Conroy, T., Desseigne, F., Ychou, M., Bouché, O., Guimbaud, R., Bécouarn, Y., Adenis, A., Raoul, J. L., Gourgou-Bourgade, S., de la Fouchardière, C., Bennouna, J., Bachet, J. B., Khemissa-Akouz, F., Péré-Vergé, D., Delbaldo, C., Assenat, E., Chauffert, B., Michel, P., Montoto-Grillot, C., & Ducreux, M. (2011). FOLFIRINOX versus gemcitabine for metastatic pancreatic cancer. *The New England Journal of Medicine*, *364*(19), 1817–1825. https://doi.org/10.1056/NEJMoa1011923 — PMID 21561347

**Design:** Phase 3 (phase 2–3 design per the trial name; the abstract says only "randomly assigned") [A].
**Population:** Metastatic PDAC, **ECOG 0–1**; n = 342 [A]. Age limit (≤75) and bilirubin criteria **[UNVERIFIED]** (NEJM full text not accessible).
**Arms:**
- FOLFIRINOX every 2 weeks: oxaliplatin 85, irinotecan 180, leucovorin 400 mg/m², **5-FU 400 mg/m² bolus + 2400 mg/m² over 46 h** [A]
- Gemcitabine 1000 mg/m² weekly for 7 of 8 weeks, then weekly for 3 of 4 weeks [A]
- Six months of chemotherapy were recommended for responders [A]

**Primary endpoint (OS):** **11.1 vs 6.8 months, HR 0.57 (0.45–0.73)**, P < .001 [A].
**Secondary endpoints [A]:**
- PFS 6.4 vs 3.3 months, HR 0.47 (0.37–0.59)
- ORR 31.6% vs 9.4%
- Definitive QoL deterioration at 6 months 31% vs 66% (HR 0.47)

**Toxicity:**
- Febrile neutropenia 5.4% with FOLFIRINOX [A]
- Grade 3–4 neutropenia **45.7%** and grade 3–4 peripheral sensory neuropathy **9.0%** with FOLFIRINOX [S-NAPOLI3, quoting PRODIGE 4]
- Diarrhoea, thrombocytopenia and other rates **[UNVERIFIED]**

## 16. MPACT (nab-paclitaxel + gemcitabine vs gemcitabine) — [VERIFIED]

**References**
- Von Hoff, D. D., Ervin, T., Arena, F. P., Chiorean, E. G., Infante, J., Moore, M., Seay, T., Tjulandin, S. A., Ma, W. W., Saleh, M. N., Harris, M., Reni, M., Dowden, S., Laheru, D., Bahary, N., Ramanathan, R. K., Tabernero, J., Hidalgo, M., Goldstein, D., . . . Renschler, M. F. (2013). Increased survival in pancreatic cancer with nab-paclitaxel plus gemcitabine. *The New England Journal of Medicine*, *369*(18), 1691–1703. https://doi.org/10.1056/NEJMoa1304369 — PMID 24131140
- (Long-term) Goldstein, D., El-Maraghi, R. H., Hammel, P., Heinemann, V., Kunzmann, V., Sastre, J., Scheithauer, W., Siena, S., Tabernero, J., Teixeira, L., Tortora, G., Van Laethem, J. L., Young, R., Penenberg, D. N., Lu, B., Romano, A., & Von Hoff, D. D. (2015). nab-Paclitaxel plus gemcitabine for metastatic pancreatic cancer: Long-term survival from a phase III trial. *Journal of the National Cancer Institute*, *107*(2), Article dju413. https://doi.org/10.1093/jnci/dju413 — PMID 25638248

**Design:** Phase 3 [A].
**Population:** Metastatic PDAC, **Karnofsky PS ≥70**; n = 861 (431 vs 430) [A].
**Arms:**
- Nab-paclitaxel 125 mg/m² then gemcitabine 1000 mg/m², days 1, 8 and 15 every 4 weeks [A]
- Gemcitabine 1000 mg/m² weekly for 7 of 8 weeks (cycle 1), then days 1, 8 and 15 every 4 weeks [A]

**Primary endpoint (OS):** **8.5 vs 6.7 months, HR 0.72 (0.62–0.83)**, P < .001 [A]. Survival at 1 year 35% vs 22%; at 2 years 9% vs 4% [A]. On updated follow-up: 8.7 vs 6.6 months, HR 0.72 (0.62–0.83). More-than-3-year survivors (4%) were seen only in the combination arm [A Goldstein 2015].
**Secondary endpoints:** PFS 5.5 vs 3.7 months, HR 0.69 (0.58–0.82); ORR (independent review) 23% vs 7% [A].
**Toxicity (grade ≥3):** neutropenia 38% vs 27%; fatigue 17% vs 7%; **neuropathy 17% vs 1%**; febrile neutropenia 3% vs 1%. Grade ≥3 neuropathy improved to grade ≤1 in a median of **29 days** [A].

## 17. NAPOLI 3 (NALIRIFOX vs nab-paclitaxel + gemcitabine) — [VERIFIED]

**Reference**
- Wainberg, Z. A., Melisi, D., Macarulla, T., Pazo Cid, R., Chandana, S. R., De La Fouchardière, C., Dean, A., Kiss, I., Lee, W. J., Goetze, T. O., Van Cutsem, E., Paulson, A. S., Bekaii-Saab, T., Pant, S., Hubner, R. A., Xiao, Z., Chen, H., Benzaghou, F., & O'Reilly, E. M. (2023). NALIRIFOX versus nab-paclitaxel and gemcitabine in treatment-naive patients with metastatic pancreatic ductal adenocarcinoma (NAPOLI 3): A randomised, open-label, phase 3 trial. *The Lancet*, *402*(10409), 1272–1281. https://doi.org/10.1016/S0140-6736(23)01366-1 — PMID 37708904

**Design:** Phase 3, open-label, 187 sites in 18 countries, 2020–2021 [A].
**Population:** Untreated metastatic PDAC, ECOG 0–1; n = 770 (383 vs 387) [A]. 80% had liver metastases; 4.9% were Asian [L].
**Arms:**
- NALIRIFOX on days 1 and 15 of a 28-day cycle: **liposomal irinotecan 50 mg/m² + oxaliplatin 60 mg/m² + leucovorin 400 mg/m² + 5-FU 2400 mg/m² over 46 h** [A]
- Nab-paclitaxel 125 + gemcitabine 1000 mg/m², days 1, 8 and 15 every 28 days [A]
- The NALIRIFOX dose was the same for UGT1A1*28 homozygous patients [L]

**Primary endpoint (OS, median follow-up 16.1 months):**
- Lancet: **11.1 (10.0–12.1) vs 9.2 (8.3–10.6) months, HR 0.83 (0.70–0.99)**, P = .036 [A]
- FDA label: HR **0.84 (0.71–0.99)**, P = .0403 [L-2025-03-03]

**Secondary endpoints:**
- PFS 7.4 (6.0–7.7) vs 5.6 (5.3–5.8) months, HR 0.69 (0.58–0.83) [FT]; label HR 0.70 (0.59–0.85)
- ORR 41.8% vs 36.2%, **not significant** (P = .11) [FT, L]
- 18-month OS 26.2% vs 19.3% [FT]

**Toxicity:** Grade ≥3 treatment-emergent AEs 87% vs 86%; treatment-related deaths 2% in each arm [A]. Grade 3–4 rates, NALIRIFOX vs GnP [FT Table 3]:
- **diarrhoea 20% vs 5%**
- nausea 12% vs 3%
- vomiting 7% vs 2%
- **hypokalaemia 15% vs 4%**
- neutropenia 14% vs 25% (plus "neutrophil count decreased" 10% vs 14%)
- anaemia 11% vs 17%
- peripheral neuropathy 3% vs 6%

**Taiwan:** The Onivyde TFDA indication now includes this first-line regimen [TFDA]. See flag 3.

## 18. NAPOLI-1 (nal-IRI + 5-FU/LV after gemcitabine) — [VERIFIED]

**References**
- Wang-Gillam, A., Li, C. P., Bodoky, G., Dean, A., Shan, Y. S., Jameson, G., Macarulla, T., Lee, K. H., Cunningham, D., Blanc, J. F., Hubner, R. A., Chiu, C. F., Schwartsmann, G., Siveke, J. T., Braiteh, F., Moyo, V., Belanger, B., Dhindsa, N., Bayever, E., . . . Chen, L. T. (2016). Nanoliposomal irinotecan with fluorouracil and folinic acid in metastatic pancreatic cancer after previous gemcitabine-based therapy (NAPOLI-1): A global, randomised, open-label, phase 3 trial. *The Lancet*, *387*(10018), 545–557. https://doi.org/10.1016/S0140-6736(15)00986-1 — PMID 26615328 (erratum: *Lancet* 2016;387(10018):536)
- (Final OS) Wang-Gillam, A., Hubner, R. A., Siveke, J. T., Von Hoff, D. D., Belanger, B., de Jong, F. A., Mirakhur, B., & Chen, L. T. (2019). NAPOLI-1 phase 3 study of liposomal irinotecan in metastatic pancreatic cancer: Final overall survival analysis and characteristics of long-term survivors. *European Journal of Cancer*, *108*, 78–87. https://doi.org/10.1016/j.ejca.2018.12.007 — PMID 30654298

**Design:** Phase 3, open-label, 76 sites in 14 countries. A third arm was added by amendment [A]. Taiwanese investigators were among the authors [PubMed affiliations].
**Population:** Metastatic PDAC after gemcitabine-based therapy; n = 417 [A]. KPS ≥70, normal bilirubin and albumin ≥3.0 g/dL were required [L].
**Arms:**
- **nal-IRI 70 mg/m² (as free base; = 80 mg/m² as hydrochloride salt) + leucovorin 400 mg/m² + 5-FU 2400 mg/m² over 46 h, every 2 weeks** [A for the nal-IRI dose; L for 5-FU/LV]; n = 117
- nal-IRI monotherapy 100 mg/m² (free base) every 3 weeks; n = 151 [A, L]
- 5-FU 2000 mg/m² over 24 h + leucovorin 200 mg/m², weekly for 4 of 6 weeks; n = 149 [L]

**Primary endpoint (OS):**
- nal-IRI + 5-FU/LV vs 5-FU/LV: **6.1 (4.8–8.9) vs 4.2 (3.3–5.3) months, HR 0.67 (0.49–0.92)**, P = .012 [A]
- Monotherapy was **no better**: 4.9 vs 4.2 months, HR 0.99 [A]
- Final analysis: 6.2 vs 4.2 months, HR 0.75 (0.57–0.99); 1-year OS 26% vs 16% [A 2019]

**Toxicity (grade 3–4, combination arm):** neutropenia 27%, fatigue 14%, diarrhoea 13%, vomiting 11% [A]. Premedication with a corticosteroid and an antiemetic is required [L].

## 19. NCIC CTG PA.3 (erlotinib + gemcitabine) — [VERIFIED]

**Reference**
- Moore, M. J., Goldstein, D., Hamm, J., Figer, A., Hecht, J. R., Gallinger, S., Au, H. J., Murawa, P., Walde, D., Wolff, R. A., Campos, D., Lim, R., Ding, K., Clark, G., Voskoglou-Nomikos, T., Ptasynski, M., & Parulekar, W. (2007). Erlotinib plus gemcitabine compared with gemcitabine alone in patients with advanced pancreatic cancer: A phase III trial of the National Cancer Institute of Canada Clinical Trials Group. *Journal of Clinical Oncology*, *25*(15), 1960–1966. https://doi.org/10.1200/JCO.2006.07.9525 — PMID 17452677 (reprinted unchanged in *JCO* 2023;41(30):4714–4720, PMID 37847995; PubMed tags it "ReprintOf". Do not cite the reprint as new data.)

**Design:** Phase 3, double-blind, placebo-controlled, international [A].
**Population:** Unresectable locally advanced or metastatic PDAC; n = 569 [A]. 76% metastatic; ECOG 0–2 (17% PS 2) [L].
**Arms:** Gemcitabine (1000 mg/m² weekly × 7 of 8 weeks, then 3 of 4 weeks [L]) + erlotinib **100 or 150 mg/day** vs + placebo [A].
**Primary endpoint (OS):**
- All doses: **HR 0.82 (0.69–0.99)**, P = .038; **median 6.24 vs 5.91 months**; 1-year OS 23% vs 17% [A]
- 100 mg cohort: 6.5 (6.0–7.4) vs 6.0 (5.1–6.7) months, HR 0.81 (0.68–0.97) [L-erlotinib generic, 2019-10-25]

**Secondary endpoint:** PFS HR 0.77 (0.64–0.92) [A].
**Toxicity (100 mg cohort, erlotinib vs placebo):** rash any grade 70% vs 30% (grade 3 5%); diarrhoea 48% vs 36% (grade 3 5%); infection grade 3 13% vs 9%. Interstitial lung disease, MAHA, MI and stroke were each <5% [L].
**Handbook point:** The 0.33-month gain is the classic example of "statistically significant but clinically trivial." **No pancreatic indication for Tarceva in Taiwan** [TFDA].

## 20. GEST (Japan–Taiwan; S-1 vs gemcitabine vs gemcitabine + S-1; advanced) — [VERIFIED] (extra, Taiwan-relevant)

**Reference**
- Ueno, H., Ioka, T., Ikeda, M., Ohkawa, S., Yanagimoto, H., Boku, N., Fukutomi, A., Sugimori, K., Baba, H., Yamao, K., Shimamura, T., Sho, M., Kitano, M., Cheng, A. L., Mizumoto, K., Chen, J. S., Furuse, J., Funakoshi, A., Hatori, T., . . . Tanaka, M. (2013). Randomized phase III study of gemcitabine plus S-1, S-1 alone, or gemcitabine alone in patients with locally advanced and metastatic pancreatic cancer in Japan and Taiwan: GEST study. *Journal of Clinical Oncology*, *31*(13), 1640–1648. https://doi.org/10.1200/JCO.2012.43.3680 — PMID 23547081

**Population:** Chemotherapy-naive locally advanced or metastatic PDAC; n = 834 [A].
**Arms:**
- Gemcitabine 1000 mg/m² on days 1, 8 and 15 every 28 days [A]
- S-1 80/100/120 mg/day (by BSA) on days 1–28 every 42 days [A]
- Gemcitabine 1000 mg/m² on days 1 and 8 + S-1 60/80/100 mg/day on days 1–14 every 21 days [A]

**Primary endpoint (OS):** gemcitabine 8.8, S-1 9.7, gemcitabine + S-1 10.1 months [A].
- **S-1 was non-inferior** to gemcitabine: HR 0.96 (97.5% CI 0.78–1.18) [A]
- Gemcitabine + S-1 was **not superior**: HR 0.88 (97.5% CI 0.71–1.08), P = .15 [A]

**Toxicity:** Haematologic and GI toxicity was worse with gemcitabine + S-1 [A].
This trial underpins the TFDA S-1 indication for advanced pancreatic cancer.

---

# E. METASTATIC — BIOMARKER-DIRECTED

## 21. POLO (maintenance olaparib, germline BRCA1/2) — [VERIFIED]

**References**
- Golan, T., Hammel, P., Reni, M., Van Cutsem, E., Macarulla, T., Hall, M. J., Park, J. O., Hochhauser, D., Arnold, D., Oh, D. Y., Reinacher-Schick, A., Tortora, G., Algül, H., O'Reilly, E. M., McGuinness, D., Cui, K. Y., Schlienger, K., Locker, G. Y., & Kindler, H. L. (2019). Maintenance olaparib for germline BRCA-mutated metastatic pancreatic cancer. *The New England Journal of Medicine*, *381*(4), 317–327. https://doi.org/10.1056/NEJMoa1903387 — PMID 31157963
- (Final OS) Kindler, H. L., Hammel, P., Reni, M., Van Cutsem, E., Macarulla, T., Hall, M. J., Park, J. O., Hochhauser, D., Arnold, D., Oh, D. Y., Reinacher-Schick, A., Tortora, G., Algül, H., O'Reilly, E. M., Bordia, S., McGuinness, D., Cui, K., Locker, G. Y., & Golan, T. (2022). Overall survival results from the POLO trial: A phase III study of active maintenance olaparib versus placebo for germline BRCA-mutated metastatic pancreatic cancer. *Journal of Clinical Oncology*, *40*(34), 3929–3939. https://doi.org/10.1200/JCO.21.01604 — PMID 35834777 (erratum: *JCO* 2024;42(17):2112)

**Design:** Phase 3, double-blind, placebo-controlled, 3:2 randomization [A].
**Population:** Germline BRCA1/2 mutation, metastatic PDAC, **no progression after ≥16 weeks of first-line platinum** chemotherapy. 3315 screened, 154 randomized (92 vs 62) [A].
**Arms:** Olaparib **300 mg tablets twice daily** vs placebo [A].
**Primary endpoint (PFS by blinded independent central review):** **7.4 vs 3.8 months, HR 0.53 (0.35–0.82)**, P = .004 [A].
**OS:**
- Interim: 18.9 vs 18.1 months, HR 0.91 [A 2019]
- Final: **19.0 vs 19.2 months, HR 0.83 (0.56–1.22), P = .3487 — not significant**; 3-year OS 33.9% vs 17.8% [A 2022]

Time to first subsequent therapy or death favoured olaparib (HR 0.44) [A 2022].
**Toxicity:** Grade ≥3 AEs 40% vs 23%; discontinuation for AEs 5% vs 2%; no QoL difference [A]. Olaparib vs placebo [FT]:
- fatigue/asthenia, any grade 60% vs 35% (grade ≥3 5% vs 2%)
- anaemia, any grade 27% vs 17% (**grade ≥3 11% vs 3%**)
- nausea 45% vs 23%; diarrhoea 29% vs 15%; decreased appetite 25% vs 7%

**Taiwan:** Lynparza TFDA indication 5 matches the POLO population (gBRCA, ≥16 weeks of platinum) [TFDA].

## 22. KEYNOTE-158 (pembrolizumab, MSI-H/dMMR non-colorectal) — [PARTIAL]

**References**
- Marabelle, A., Le, D. T., Ascierto, P. A., Di Giacomo, A. M., De Jesus-Acosta, A., Delord, J. P., Geva, R., Gottfried, M., Penel, N., Hansen, A. R., Piha-Paul, S. A., Doi, T., Gao, B., Chung, H. C., Lopez-Martin, J., Bang, Y. J., Frommer, R. S., Shah, M., Ghori, R., . . . Diaz, L. A. (2020). Efficacy of pembrolizumab in patients with noncolorectal high microsatellite instability/mismatch repair-deficient cancer: Results from the phase II KEYNOTE-158 study. *Journal of Clinical Oncology*, *38*(1), 1–10. https://doi.org/10.1200/JCO.19.02105 — PMID 31682550
- (Update) Maio, M., Ascierto, P. A., Manzyuk, L., Motola-Kuba, D., Penel, N., Cassier, P. A., Bariani, G. M., De Jesus Acosta, A., Doi, T., Longo, F., Miller, W. H., Oh, D. Y., Gottfried, M., Xu, L., Jin, F., Norwood, K., & Marabelle, A. (2022). Pembrolizumab in microsatellite instability high or mismatch repair deficient cancers: Updated analysis from the phase II KEYNOTE-158 study. *Annals of Oncology*, *33*(9), 929–938. https://doi.org/10.1016/j.annonc.2022.05.519 — PMID 35680043
- (Update) Marabelle, A., O'Malley, D. M., Hendifar, A. E., Ascierto, P. A., Motola-Kuba, D., Penel, N., Cassier, P. A., Bariani, G., De Jesus-Acosta, A., Doi, T., Longo, F., Miller, W. H., Oh, D. Y., Gottfried, M., Yao, L., Jin, F., Gozman, A., & Maio, M. (2025). Pembrolizumab in microsatellite-instability-high and mismatch-repair-deficient advanced solid tumors: Updated results of the KEYNOTE-158 trial. *Nature Cancer*, *6*(2), 253–258. https://doi.org/10.1038/s43018-024-00894-y — PMID 39979665

**Design:** Phase 2, multicohort basket [A].
**Population:** Previously treated, advanced MSI-H/dMMR non-colorectal cancer. Pancreatic cancer was one of the most common tumour types [A].
**Arm:** Pembrolizumab **200 mg every 3 weeks** for up to 2 years (35 cycles) [A].
**Primary endpoint (ORR, independent central review), all tumours [A]:**

| Report | n | ORR | Median PFS | Median OS | Grade 3–5 TRAEs |
|---|---|---|---|---|---|
| 2020 | 233 | 34.3% (28.3–40.8) | 4.1 months | 23.5 months | 14.6% |
| 2022 | 321 evaluable | 30.8% (25.8–36.2) | 3.5 months | 20.1 months | Grade 3–4: 11.1% |
| 2025 | 373 | 33.8% | 4.0 months | 19.8 months | Grade ≥3: 13% |

**Pancreatic subgroup:** n = 22, **ORR 18.2%, median PFS 2.1 months, median OS 3.7 months** [S-Fivaz]. Not confirmed from the primary Table 3 (**check before printing**).
**Toxicity:** Grade 3–5 TRAEs 14.6%, with one grade 5 pneumonia [A 2020]. Grade 5 events in the 2022 update: myocarditis, pneumonia and Guillain–Barré syndrome (one each) [A 2022].
**Taiwan:** The Keytruda TFDA indication 9 covers tissue-agnostic MSI-H/dMMR solid tumours after prior therapy [TFDA]. MSI immunohistochemistry is reimbursed in Taiwan; KRAS PCR is self-paid [S-PanAsia, TOS paragraph].

## 23. NTRK fusions (larotrectinib, entrectinib) — [VERIFIED] (pancreatic counts tiny)

**References**
- Hong, D. S., DuBois, S. G., Kummar, S., Farago, A. F., Albert, C. M., Rohrberg, K. S., van Tilburg, C. M., Nagasubramanian, R., Berlin, J. D., Federman, N., Mascarenhas, L., Geoerger, B., Dowlati, A., Pappo, A. S., Bielack, S., Doz, F., McDermott, R., Patel, J. D., Schilder, R. J., . . . Drilon, A. (2020). Larotrectinib in patients with TRK fusion-positive solid tumours: A pooled analysis of three phase 1/2 clinical trials. *The Lancet Oncology*, *21*(4), 531–540. https://doi.org/10.1016/S1470-2045(19)30856-3 — PMID 32105622
- Doebele, R. C., Drilon, A., Paz-Ares, L., Siena, S., Shaw, A. T., Farago, A. F., Blakely, C. M., Seto, T., Cho, B. C., Tosi, D., Besse, B., Chawla, S. P., Bazhenova, L., Krauss, J. C., Chae, Y. K., Barve, M., Garrido-Laguna, I., Liu, S. V., Conkling, P., . . . Demetri, G. D. (2020). Entrectinib in patients with advanced or metastatic NTRK fusion-positive solid tumours: Integrated analysis of three phase 1–2 trials. *The Lancet Oncology*, *21*(2), 271–282. https://doi.org/10.1016/S1470-2045(19)30691-6 — PMID 31838007 (4 errata, 2020–2021)

**Larotrectinib** (adults mostly 100 mg twice daily) [A]:
- 159 patients; ORR 79% (72–85) of 153 evaluable; CR 16% [A]
- **Pancreas: 2 patients, 1 response** [FT Table 3]
- Grade 3–4 related AEs were rare: ALT increase 3%, anaemia 2%, neutropenia 2% [A]

**Entrectinib** (≥600 mg once daily) [A]:
- 54 adults; ORR 57% (43.2–70.8); median DOR 10 months [A]
- **Pancreatic: 2 of 3 responded** [FT]
- Grade 3–4 related AEs: weight gain 10%, anaemia 12% in the NTRK safety population [A]

**Taiwan:** Vitrakvi (larotrectinib, 2019), Rozlytrek (entrectinib, 2020) and Augtyro (repotrectinib, 2025) are TFDA-licensed with NTRK-fusion solid-tumour indications [TFDA]. See flag 3 on the guideline discrepancy.

## 24. Zenocutuzumab (eNRGy; NRG1 fusion) — [VERIFIED]

**Reference**
- Schram, A. M., Goto, K., Kim, D. W., Macarulla, T., Hollebecque, A., O'Reilly, E. M., Ou, S. I., Rodon, J., Rha, S. Y., Nishino, K., Duruisseaux, M., Park, J. O., Neuzillet, C., Liu, S. V., Weinberg, B. A., Cleary, J. M., Calvo, E., Umemoto, K., Nagasaka, M., . . . Drilon, A. (2025). Efficacy of zenocutuzumab in NRG1 fusion-positive cancer. *The New England Journal of Medicine*, *392*(6), 566–576. https://doi.org/10.1056/NEJMoa2405008 — PMID 39908431

**Design:** Registrational phase 2 basket (phase 1/2 in PubMed indexing); 204 patients with 12 tumour types [A].
**Arm:** Zenocutuzumab (a HER2 × HER3 bispecific antibody) **750 mg IV every 2 weeks** [A].
**Primary endpoint (investigator-assessed ORR), all tumours:** 30% (23–37) in 158 patients; DOR 11.1 months; PFS 6.8 months [A].
**Pancreatic cohort:**
- **15 of 36 responded (42%, 95% CI 25–59)**; DOR 7.4 months (4.0–11.2); **PFS 9.2 months (5.5–11.2)** [FT]
- 24 of 31 had a ≥50% CA19-9 fall [FT]
- All 36 evaluable patients were **KRAS wild-type**; the commonest fusion partner was ATP1B1 (44%) [FT]
- FDA label, BICR, n = 30: ORR **40% (23–59)**, CR 3.3%, DOR range 3.7–16.6 months, DOR ≥6 months in 67% [L-2026-05-19]

**Toxicity:** Mostly grade 1–2. Related AEs: diarrhoea 18%, fatigue 12%, nausea 11%; infusion-related reactions 14% [A]. **Boxed warning: embryo-fetal toxicity.** Warnings and precautions also cover infusion reactions and anaphylaxis, ILD/pneumonitis (stop permanently for grade ≥2) and **LV dysfunction (check LVEF)** [L].
**Approval:** FDA accelerated approval on 2024-12-04 (BLA 761352) for NRG1+ NSCLC and pancreatic adenocarcinoma; a cholangiocarcinoma indication was added later [openFDA]. **Not TFDA-licensed** (no entry as of 2026-10-27).

---

# F. RAS-TARGETED THERAPY (2023–2026)

## 25. Daraxonrasib (RMC-6236; pan-RAS(ON) inhibitor)

### 25a. Phase 1/2 RMC-6236-001, PDAC cohort — [VERIFIED]
- Wolpin, B. M., Park, W., Garrido-Laguna, I., Spira, A., Starodub, A., Sommerhalder, D., Punekar, S. R., Barve, M., Pelster, M., Herzberg, B., Azad, N. S., Hecht, J. R., Ou, S. H. I., Lin, T., Kar, S., Tao, L., Vora, R., Hegde, A., Aung, K., & Hong, D. S. (2026). Daraxonrasib in previously treated advanced RAS-mutated pancreatic cancer. *The New England Journal of Medicine*, *394*(18), 1790–1802. https://doi.org/10.1056/NEJMoa2505783 — PMID 42090791

**Design and dosing:** Doses ranged from 10 to 400 mg once daily; **300 mg** was chosen as the phase 3 dose. The primary endpoint was safety; 168 patients had previously treated RAS-mutated PDAC [A].
**Toxicity:** Treatment-related AEs 96%; grade ≥3 30%. The commonest were rash, diarrhoea, nausea, stomatitis/mucositis, vomiting and fatigue [A].
**Activity in second-line RAS G12 patients at 300 mg (n = 26):** ORR 35% (17–56), DOR 8.2 months, PFS 8.5 months, OS 13.1 months [A].
**Activity in RAS G12/G13/Q61 patients (n = 38):** ORR 29% (15–46), PFS 8.1 months, OS 15.6 months [A].

### 25b. RASolute 302 (phase 3, second line) — [VERIFIED]
- O'Reilly, E. M., Wainberg, Z. A., Hendifar, A. E., Borad, M. J., Pietrantonio, F., Pant, S., Hammel, P., Cremolini, C., Manji, G. A., Oberstein, P. E., Garrido-Laguna, I., Springfeld, C., Azad, N. S., Ueno, M., Chui, S. Y., Zhang, Y., Patel, H., Lee, Y., Salman, Z., & Wolpin, B. M. (2026). Daraxonrasib or chemotherapy in previously treated metastatic pancreatic cancer. *The New England Journal of Medicine*, *395*(4), 325–337. https://doi.org/10.1056/NEJMoa2605555 — PMID 42223072 (e-pub 2026-05-31; correspondence *NEJM* 2026;395:1661–1662)

**Design:** Phase 3, international, open-label, randomized 1:1 [A].
**Population:** Metastatic PDAC that progressed after **one** prior line (fluoropyrimidine- or gemcitabine-based), ECOG 0–1, measurable disease, known RAS status. n = 500 (daraxonrasib 248, chemotherapy 252). 91.8% had RAS G12 mutations; 3% had no RAS mutation detected [A, L]. Baseline: median age 66 years, 11% Asian, 70% liver metastases [L].
**Arms:**
- **Daraxonrasib 300 mg orally once daily** [L]
- Investigator's-choice chemotherapy: mFOLFIRINOX, gemcitabine + nab-paclitaxel, FOLFOX or nal-IRI + 5-FU/LV [L]

**Dual primary endpoints (OS and BICR PFS in the RAS G12 population, n = 459):**
- OS **13.2 vs 6.6 months, HR 0.40 (0.30–0.54)** [A; CI from L]
- PFS **7.3 vs 3.5 months, HR 0.45 (0.34–0.59)** [A; CI from L]
- ORR 32% (26–38) vs 11% (7–16) [L]

**Overall population:**
- OS **13.2 (10.0–NE) vs 6.7 (5.8–8.0) months, HR 0.40 (0.30–0.53)**, P < .0001 [A, L]
- PFS 7.2 (5.7–7.5) vs 3.6 (2.9–4.2) months, HR 0.49 (0.38–0.64) [L]
- ORR 30% (25–36) vs 11% (7–15) [L]

**Toxicity:**
- Grade ≥3 AEs **61.8% vs 69.6%**; discontinuation for treatment-related AEs **1.2% vs 11.2%** [A]
- From the label: serious AEs 30%; dose interruption 69%; dose reduction 37% [L]

Adverse reactions in RASolute 302, daraxonrasib vs chemotherapy, any grade (grade 3–4) [L Table 3]:

| Adverse reaction | Daraxonrasib | Chemotherapy |
|---|---|---|
| Rash | **87% (13%)** | 9% (0%) |
| Diarrhoea | 67% (7%) | 44% (8%) |
| Stomatitis | **56% (12%)** | 19% (3%) |
| Nausea | 52% (3%) | 42% (2%) |
| Fatigue | 47% (5%) | 61% (10%) |
| Vomiting | 42% (1%) | 25% (1%) |
| Haemorrhage | 22% (3%) | 12% (4%) |
| Paronychia | 17% | 0% |
| Peripheral neuropathy | 10% | 29% |

- Pooled pancreatic safety data [L]: skin toxicity 86% (grade 3 10%; median onset **13 days**); stomatitis 57% (grade 3 9%; onset 22 days); diarrhoea 63% (grade 3 6%; onset **3 days**); **GI perforation 0.9%** (one fatal); **ILD/pneumonitis 2.4%** (one fatal); renal-limited thrombotic microangiopathy 0.4%

**Nursing-relevant label points [L-2026-08-27]:**
- **Start prophylaxis from day 1:** topical corticosteroid to face and chest, emollients, SPF ≥30 sunscreen, and consider oral doxycycline or minocycline
- Use a steroid-containing mouthwash for stomatitis
- Dose reductions: 300 → 200 → 150 mg; stop permanently if 150 mg is not tolerated
- **Drug interactions:** daraxonrasib is a CYP3A and P-gp substrate and a **P-gp inhibitor**. Give P-gp substrates ≥4 hours apart, and **avoid cyclosporine** (both bind cyclophilin A). One commentary flags opioid P-gp interactions (Davis 2026, *J Pain Symptom Manage*, PMID 42863589; title only).

**Status:** FDA approved 2026-08-26. **Not TFDA-licensed** as of 2026-10-27. First-line data have **not** been published in a peer-reviewed paper as of 2026-10-29.

## 26. KRAS G12C inhibitors (rare in PDAC, about 1–2%) — [VERIFIED]
- Strickler, J. H., Satake, H., George, T. J., Yaeger, R., Hollebecque, A., Garrido-Laguna, I., Schuler, M., Burns, T. F., Coveler, A. L., Falchook, G. S., Vincent, M., Sunakawa, Y., Dahan, L., Bajor, D., Rha, S. Y., Lemech, C., Juric, D., Rehn, M., Ngarmchamnanrith, G., . . . Hong, D. S. (2023). Sotorasib in KRAS p.G12C-mutated advanced pancreatic cancer. *The New England Journal of Medicine*, *388*(1), 33–43. https://doi.org/10.1056/NEJMoa2208470 — PMID 36546651
- Bekaii-Saab, T. S., Yaeger, R., Spira, A. I., Pelster, M. S., Sabari, J. K., Hafez, N., Barve, M., Velastegui, K., Yan, X., Shetty, A., Der-Torossian, H., & Pant, S. (2023). Adagrasib in advanced solid tumors harboring a KRAS^G12C^ mutation. *Journal of Clinical Oncology*, *41*(25), 4097–4106. https://doi.org/10.1200/JCO.23.00434 — PMID 37099736

**Sotorasib (CodeBreaK 100), 960 mg daily, n = 38** (median 2 prior lines) [A]:
- ORR 21% (10–37); PFS 4.0 months (2.8–5.6); OS 6.9 months (5.0–9.1) [A]
- Treatment-related AEs 42%; grade 3 16% (diarrhoea and fatigue, 5% each) [A, FT]

**Adagrasib (KRYSTAL-1), 600 mg twice daily** [A]:
- **Pancreatic: 7 of 21 responded (33.3%)**
- Whole non-lung, non-colorectal cohort: DOR 5.3 months, PFS 7.4 months; grade 3–4 TRAEs 27%

**Taiwan:** Lumakras and Krazati are TFDA-licensed, but neither licence includes a pancreatic indication [TFDA].

## 27. KRAS G12D-directed agents (all early phase; 2026 publications) — [VERIFIED]
- Park, W., Kasi, A., Spira, A. I., Paz-Ares Rodríguez, L., Herzberg, B. O., Pelster, M. S., Tolcher, A. W., Kuboki, Y., Kitano, S., Shoji, H., Wang, J. S., Berlin, J. D., Hollebecque, A., LoRusso, P., Fountzilas, C., Cassier, P. A., Nishina, T., Sakai, D., Inagaki, C., . . . Goldman, J. W. (2026). Setidegrasib in advanced non-small-cell lung cancer and pancreatic cancer. *The New England Journal of Medicine*, *394*(14), 1409–1420. https://doi.org/10.1056/NEJMoa2600752 — PMID 41879829
- Ai, X., Song, Z., Wu, L., Zhou, A., Cheng, D., Zong, H., Wu, H., Niu, Z., Sun, Y., Zhu, L., Li, Z., Deng, Y., Yuan, Y., Qu, X., Zhao, H., Du, Y., Li, Z., Wang, Y., Shen, H., . . . Lu, S. (2026). Oral KRAS G12D inhibitor GFH375 for previously treated advanced solid tumors with KRAS^G12D^ mutations: A phase 1 trial. *Nature Medicine*, *32*(9), 3302–3312. https://doi.org/10.1038/s41591-026-04559-4 — PMID 42745055
- Cui, J., Jiang, K., Li, W., Ni, S., Zong, H., Du, J., He, Y., Liu, Z., Kong, G., Zhang, Y., Li, X., Han, H., Yao, F., Chen, Y., Zhou, M., & Wang, L. (2026). KRAS-G12D inhibitor HRS-4642 plus chemotherapy in advanced KRAS^G12D^-mutant pancreatic cancer: A phase 1b/2 trial. *Nature Medicine*, *32*(9), 3294–3301. https://doi.org/10.1038/s41591-026-04538-9 — PMID 42426224
- Shi, S., Wei, M., Du, N., Li, J., Han, B., Wang, W., Hu, X., Luo, F., Xu, J., & Yu, X. (2026). Chemotherapy-free phase 1/2 trial of HRS-4642 plus adebrelimab in previously treated metastatic KRAS G12D-mutant pancreatic cancer. *Cancer Cell*, *44*(10), 2100–2107.e2. https://doi.org/10.1016/j.ccell.2026.08.012 — PMID 42748921

| Agent (trial) | Setting / dose | PDAC n | ORR | PFS / OS (months) | Key toxicity |
|---|---|---|---|---|---|
| Setidegrasib (ASP3082, KRAS G12D degrader) | 2L or 3L; 600 mg IV weekly | 21 | 24% (8–47) | 3.0 / 10.3 | Infusion reactions 80%; grade ≥3 AEs 42% (n = 76 at 600 mg) [A] |
| GFH375 (oral; ON + OFF state inhibitor) | Pretreated; RP2D 600 mg daily | 37 evaluable | 35.1% (13 of 37) | 5.5 / 9.9 (DOR 5.6) | Grade ≥3 TRAEs 36.5% (all tumours); 1 grade 5 septic shock [A] |
| HRS-4642 (liposomal IV) + nab-P/gem | **1L**, 30 treatment-naive | 30 | **63.3% (43.9–80.1)** | not in abstract | Grade ≥3 TRAEs 90.3% (mostly haematologic) [A] |
| HRS-4642 + adebrelimab (anti-PD-L1) | Pretreated; RP2D cohort | 37 | 43.2% (27.1–60.5) | 5.7 / 11.5 | Hypercholesterolaemia and anaemia 50% each [A] |

---

# G. Taiwan regulatory snapshot for this chapter (TFDA open data, file dated 2026-10-27) — [VERIFIED]

| Drug (brand) | TFDA licence | Pancreatic indication in Taiwan (quoted or abridged) |
|---|---|---|
| Liposomal irinotecan (Onivyde 安能得微脂體注射劑; holder 智擎生技) | 衛部藥輸字第026655號, issued 2015-12-07 | (1) With oxaliplatin/5-FU/LV, **first-line** metastatic; (2) with 5-FU/LV after gemcitabine |
| Nab-paclitaxel (Abraxane 亞伯杉) | 衛部藥輸字第026484號, 2015-03-19 | With gemcitabine, first-line metastatic |
| Olaparib (Lynparza 令癌莎) | 衛部藥輸字第027445/027446號, 2018-06-05 | Maintenance, germline BRCA, no progression after ≥16 weeks of first-line platinum, metastatic |
| S-1 (TS-1 愛斯萬; also generic Golfer 剋伏) | 衛署藥輸字第025242/025243號, 2010-08-05 | **Locally advanced or metastatic only (no adjuvant pancreatic indication)** |
| Erlotinib (Tarceva) | 衛署藥輸字第025071號 etc. | **None** (NSCLC only) |
| Pembrolizumab (Keytruda 吉舒達) | 衛部菌疫輸字第001025號 | Tissue-agnostic MSI-H/dMMR solid tumours after prior therapy |
| Larotrectinib / entrectinib / repotrectinib | 027746–027748 / 027864–027865 / 028909 | NTRK-fusion solid tumours (tissue-agnostic) |
| Sotorasib / adagrasib | 028291, 029167 / 028871 | None for pancreas |
| Daraxonrasib, zenocutuzumab | — | **Not licensed** |

NHI reimbursement status could not be checked (www.nhi.gov.tw is unreachable): **[UNVERIFIED]**. The Pan-Asian guideline's Taiwan paragraph says [S-PanAsia]:
- NHI covers reimbursed drugs at "nearly 100%"; non-covered drugs are fully self-paid
- MSI immunohistochemistry is reimbursed; KRAS PCR is self-paid
- Oxaliplatin and irinotecan are approved in Taiwan for pancreatic cancer only first-line, as part of FOLFIRINOX
- New drugs take 1–2 years after FDA/EMA approval to reach Taiwan, then another 1–2 years for NHI coverage

---

# H. Quick-reference table (primary-endpoint results for the handbook)

| Trial | Setting | Experimental vs control | Primary endpoint result | Verdict |
|---|---|---|---|---|
| CONKO-001 | Adjuvant | Gem ×6 vs observation | DFS 13.4 vs 6.7 months, HR 0.55; OS HR 0.76 (2013) | Positive |
| ESPAC-4 | Adjuvant | GemCap vs gem | OS 28.0 vs 25.5 months, HR 0.82 (0.68–0.98) | Positive |
| PRODIGE 24 | Adjuvant | mFFX vs gem | DFS 21.4 vs 12.8 months, HR 0.66; OS 53.5 vs 35.5, HR 0.68 (5-year) | Positive; standard if fit |
| APACT | Adjuvant | Nab-P + gem vs gem | Independent DFS 19.4 vs 18.8 months, HR 0.88 (P = .18) | **Negative** primary |
| JASPAC 01 | Adjuvant (Japan) | S-1 vs gem | OS HR 0.57 (0.44–0.72); 5-year OS 44.1% vs 24.4% | Positive (Asian) |
| PREOPANC | Neoadjuvant | Gem-CRT vs surgery | OS HR 0.78 (NS) → HR 0.73 long-term; 5-year 20.5% vs 6.5% | Positive on long-term follow-up |
| PREOPANC-2 | Neoadjuvant | FFX ×8 vs gem-CRT | OS 21.9 vs 21.3 months, HR 0.88 (P = .32) | **Negative** |
| A021501 | Borderline resectable, phase 2 | mFFX ± SBRT | 18-month OS 66.7% vs 47.3%; RT arm closed | mFFX alone = reference |
| NORPACT-1 | Neoadjuvant, phase 2 | FFX ×4 vs surgery | 18-month OS 60% vs 73%; HR 1.52 | **Negative** (trend to harm) |
| Prep-02/JSAP-05 | Neoadjuvant (Japan) | Gem + S-1 ×2 vs surgery | OS 37.0 vs 26.6 months, HR 0.73 (0.56–0.95) | Positive |
| S1505 | Perioperative, phase 2 | mFFX vs GnP | 2-year OS 47% vs 48% (threshold 40%) | **Negative** |
| LAP07 | Locally advanced | CRT vs chemo; erlotinib | OS HR 1.03; erlotinib HR 1.19 | **Negative** |
| CONKO-007 | Locally advanced | CRT vs chemo after induction | R0 25% vs 18% (P = .113); OS HR 0.937 | **Negative** |
| PRODIGE 4 | Metastatic 1L | FOLFIRINOX vs gem | OS 11.1 vs 6.8 months, HR 0.57 | Positive |
| MPACT | Metastatic 1L | Nab-P + gem vs gem | OS 8.5 vs 6.7 months, HR 0.72 | Positive |
| NAPOLI 3 | Metastatic 1L | NALIRIFOX vs GnP | OS 11.1 vs 9.2 months, HR 0.83 (label 0.84) | Positive |
| NAPOLI-1 | Metastatic 2L | nal-IRI + 5-FU/LV vs 5-FU/LV | OS 6.1 vs 4.2 months, HR 0.67 | Positive |
| PA.3 | Advanced 1L | Gem + erlotinib vs gem | OS 6.24 vs 5.91 months, HR 0.82 | Positive but trivial |
| POLO | gBRCA maintenance | Olaparib vs placebo | PFS 7.4 vs 3.8 months, HR 0.53; OS NS | PFS-positive |
| RASolute 302 | Metastatic 2L | Daraxonrasib vs chemo | OS 13.2 vs 6.6 months (G12), HR 0.40 | **Strongly positive** |

---

# I. Not verified, or still missing (do not print without checking)

- PRODIGE 4: age limit (≤75), and diarrhoea/thrombocytopenia rates. NEJM full text is not accessible (403).
- PRODIGE 24: the toxicity percentages come from a secondary reproduction [S-deJesus], not the NEJM paper itself.
- CONKO-001: median OS in the 2013 paper.
- JASPAC 01: median OS (secondary sources only), and whether R1 resection was eligible.
- KEYNOTE-158 pancreatic subgroup (secondary only, [S-Fivaz]).
- LAP07: capecitabine dose with radiotherapy. S1505: chemotherapy doses and grade 3–4 rates. A021501: chemotherapy-phase grade 3–4 rates. CONKO-007: toxicity, and what the erratum corrects.
- Contents of the errata listed in flag 14.
- NHI reimbursement criteria for any of these drugs (nhi.gov.tw unreachable).
- Peer-reviewed first-line daraxonrasib data; A021806 and PREOPANC-3 results: not published as of 2026-10-29.

---

## Critic additions

Completeness critic pass, 2026-10-29. Append only. Tags as above; [REG] = ClinicalTrials.gov registry record, read through the ClinicalTrials.gov API v2 tool.

### CA-1. Trial eligibility now verified from the registries (closes items in §I)

**PRODIGE 4 / ACCORD 11** (NCT00112658, UNICANCER; randomized phase II/III, 342 enrolled) [VERIFIED; REG]
- Inclusion:
  - age **18 to 75**
  - **WHO PS 0–1**
  - metastatic, measurable PDAC
  - **bilirubin ≤1.5× ULN (biliary drainage allowed)**
  - ANC ≥1,500/mm³ and platelets ≥100,000/mm³
  - creatinine <120 µmol/L
- Exclusion:
  - brain or meningeal metastases
  - prior MI, angina or uncompensated cardiac insufficiency
  - prior inflammatory bowel disease or chronic diarrhoea
  - unresolved bowel occlusion or sub-occlusion
- Registry arm description:
  - oxaliplatin over 2 h, irinotecan over 90 min, leucovorin over 2 h
  - 5-FU bolus over 5 min, then 46-h infusion, every 14 days
  - gemcitabine weekly ×7, then 3 of 4 weeks
- This closes "age ≤75 and bilirubin [UNVERIFIED]" in §15 and §I.

**PRODIGE 24 / CCTG PA.6** (NCT01526135) [VERIFIED; REG]
- Inclusion:
  - age **18 to 79**
  - WHO PS 0–1
  - R0/R1 resection, randomized **21–84 days after surgery**
  - oral intake ≥1,500 kcal/day
  - ANC ≥1,500 and platelets ≥100,000
  - haemoglobin ≥10 (the registry prints "g/L", an obvious slip for g/dL)
  - bilirubin ≤1.5× ULN
  - creatinine <130 µmol/L
  - IPMN with an invasive component was eligible
- Exclusion:
  - **CA19-9 >180 U/mL within 21 days of registration** (confirms the [S-ESPAC4LT] criterion in §3)
  - **pre-existing neuropathy, Gilbert's disease or UGT1A1*28/*28 genotype**
  - colorectal inflammatory disease, or bowel occlusion or sub-occlusion
  - uncontrolled diabetes
  - chronic HBV, HCV or HIV infection
- Teaching point: the adjuvant mFOLFIRINOX evidence excludes *28 homozygotes, Gilbert's syndrome and pre-existing neuropathy. Fit-for-mFOLFIRINOX is a narrower population than "resected PDAC".

### CA-2. Second-line oxaliplatin trials (missing; they conflict)

| Trial | Design / population | Result | Tag |
|---|---|---|---|
| **CONKO-003** (Oettle 2014) | Phase 3, 16 German institutions, 2004–2007. 168 patients progressing on first-line gemcitabine (160 analysed). **OFF** (oxaliplatin + folinic acid + 5-FU) vs FF. | OS **5.9 vs 3.3 months, HR 0.66 (0.48–0.91), P = .010**. TTP 2.9 vs 2.0 months, HR 0.68 (0.50–0.94). AE rates similar except grade 1–2 neurotoxicity, 38.2% vs 7.1%. | [VERIFIED; A] |
| **PANCREOX** (Gill 2016) | Phase 3, Canada. 108 patients after gemcitabine, ECOG 0–2. **mFOLFOX6** vs infusional 5-FU/LV. | PFS 3.1 vs 2.9 months (P = .99). **OS worse with mFOLFOX6: 6.1 vs 9.9 months (P = .02)**. Grade 3–4 AEs 63% vs 11%. Withdrawal for AEs 20% vs 2%. Post-progression therapy 7% vs 25%. | [VERIFIED; A] |

- Exam point: oxaliplatin after gemcitabine was positive in one trial (CONKO-003) and harmful in another (PANCREOX). NAPOLI-1 (§18) is the more robust second-line evidence.
- NCCN still lists FOLFOX, OFF and CAPEOX among second-line options after gemcitabine (see CA-3).

### CA-3. NCCN regimen preferences (NCCN Guidelines for Patients: Pancreatic Cancer 2026, based on professional v2.2026 dated 2026-04-22) [VERIFIED for the patient guide; professional v4.2026 PDF not readable, HTTP 403]

**First line, PS 0–1 (Guide 5)**
- Preferred, all patients:
  - gemcitabine + nab-paclitaxel
  - **FOLFIRINOX or mFOLFIRINOX**
  - **NALIRIFOX**
- Preferred, BRCA1/2 or PALB2:
  - **cisplatin + gemcitabine**
  - FOLFIRINOX or mFOLFIRINOX
- Other recommended:
  - GemCap
  - gemcitabine + erlotinib
  - gemcitabine
  - nab-paclitaxel + cisplatin + gemcitabine
  - CAPEOX
  - GTX
  - OFF
  - locally advanced only: capecitabine, 5-FU
- Certain cases (biomarker): dabrafenib + trametinib; entrectinib, larotrectinib or repotrectinib; pembrolizumab; selpercatinib.

**First line, PS 2 (Guide 6)**
- Preferred: gemcitabine + nab-paclitaxel, capecitabine, gemcitabine.
- Metastatic, also preferred: CAPEOX, FOLFIRI, FOLFOX.

**First line, PS 3 (Guide 7)**
- Locally advanced, preferred: gemcitabine, capecitabine, 5-FU.
- **No preferred therapy for metastatic disease.**

**Maintenance (Guide 8)**
- Preferred: **olaparib for germline BRCA1/2 after platinum**.
- Also listed for metastatic disease: CAPEOX, FOLFIRI, FOLFOX.
- Other recommended:
  - after FOLFIRINOX: capecitabine
  - after gem + nab-P: gem + nab-P on a modified schedule, or gemcitabine
- Certain cases:
  - after FOLFIRINOX: FOLFIRI, 5-FU/LV or FOLFOX
  - **rucaparib** for BRCA1/2 or PALB2 after platinum
- Maintenance is considered after **at least 4–6 months** of stable or responding disease.

**Second line, PS 0–1 (Guide 9)**
- After gemcitabine-based therapy:
  - 5-FU/LV/(liposomal) irinotecan
  - capecitabine
  - CAPEOX
  - 5-FU
  - 5-FU/LV
  - FOLFIRI
  - FOLFIRINOX or mFOLFIRINOX
  - FOLFOX
  - OFF
- After fluoropyrimidine-based therapy:
  - gemcitabine + nab-P
  - cisplatin + gemcitabine
  - erlotinib + gemcitabine
  - 5-FU/LV/liposomal irinotecan (only if no prior irinotecan)
  - gemcitabine
  - nab-P + cisplatin + gemcitabine
- Biomarker-directed:
  - adagrasib or sotorasib
  - dabrafenib + trametinib
  - NTRK inhibitors
  - erdafitinib
  - fam-trastuzumab deruxtecan
  - selpercatinib
  - zenocutuzumab
- Immunotherapy-naive: dostarlimab, pembrolizumab, ipilimumab + nivolumab.
- Rule: the prior regimen may be repeated if **≥6 months** have passed since it was completed; otherwise use a different regimen.

**Neoadjuvant (Guide 12)**
- Preferred:
  - FOLFIRINOX or mFOLFIRINOX (**PS 0–1 only**)
  - gemcitabine + nab-P
  - cisplatin + gemcitabine for BRCA or PALB2
- Certain cases: PAXG.
- Treat at, or with management from, a **high-volume centre**, for **up to 6 months**.
- Consolidation chemoradiation: preferred capecitabine or 5-FU; other recommended, gemcitabine.

**Adjuvant (Guide 13)**
- Preferred: **GemCap and mFOLFIRINOX**.
- Other recommended: 5-FU/LV, gemcitabine, 5-FU, capecitabine.
- Ideally start **within 12 weeks** of surgery.
- Total chemotherapy up to 6 months, including any neoadjuvant cycles.
- Before adjuvant therapy: contrast CT of chest, abdomen and pelvis, plus CA19-9.

**Interpretation notes**
- Guide 9 prints "Fluorouracil, Leucovorin, Irinotecan". The body text says this means "fluorouracil, leucovorin, and **liposomal** irinotecan … you must not have already had irinotecan" [PARTIAL interpretation].
- **Daraxonrasib is absent.** The patient guide predates the 2026-08-26 FDA approval, so check professional v4.2026 before printing.

### CA-4. KEYNOTE-158 pancreatic subgroup: ORR now verified from the FDA label (upgrades §22)

- KEYTRUDA USPI (openFDA, effective 2026-07-10), MSI-H/dMMR non-colorectal adult pool (KEYNOTE-158 and KEYNOTE-164):
  - **pancreatic cancer n = 22, ORR 4/22 = 18% (95% CI 5–40%)**
  - DOR range 8.1 to 24.3+ months
  - [VERIFIED; L]
- Median PFS 2.1 and OS 3.7 months still come only from [S-Fivaz]; they are not in the label.
- The same label section reports **local vs central MSI discordance** in KEYNOTE-158 cohort K:
  - of 104 tumours that were MSI-H/dMMR by local testing, **only 56.7%** were MSI-H on FoundationOne CDx
  - of 169, **62.1%** were dMMR on the VENTANA MMR RxDx panel
  - [VERIFIED; L]
  - Teaching point: confirm MSI-H/dMMR before immunotherapy.

### CA-5. Surveillance after resection (needed for §7 "follow-up")

- **NCCN Guidelines for Patients 2026:** surveillance consists of history and examination, **CA19-9**, **chest CT**, and **contrast CT or MRI of abdomen and pelvis**, "as needed". **Intervals are not given** in the patient guide, so any "every 3–6 months for 2 years" schedule is [UNVERIFIED] until the professional PDF is read.
- **Pan-Asian ESMO 2025, recommendation 6a:** "For patients with resected pancreatic cancer, regular follow-up is suggested **[III, B]**" (100% consensus). The panel upgraded the level of evidence after Andel 2025 [VERIFIED; FT].
- **Andel 2025** (E-AHPBA prospective cross-sectional study; 33 centres in 13 countries; 333 patients with recurrence after PDAC resection) [VERIFIED; A]:
  - **routine imaging** in 71%, symptomatic follow-up in 29%
  - OS **28 vs 23 months (P = .01)**
  - routine imaging associated with recurrence-focused treatment (adjusted OR 2.57, 1.22–5.41) and longer OS (adjusted HR 0.75, 0.56–0.99)
  - asymptomatic subgroup 30 vs 21 months (P = .03), as quoted by the Pan-Asian guideline [PARTIAL]
  - Observational, so it supports, but does not prove, routine CT surveillance.

### CA-6. References for these additions (APA 7)

- Andel, P. C. M., van Goor, I. W. J. M., Augustinus, S., Berrevoet, F., Besselink, M. G., Bhojwani, R., Boggi, U., Bouwense, S. A. W., Cirkel, G. A., van Dam, J. L., Djanani, A., Dorcaratto, D., Dreyer, S., den Dulk, M., Frigerio, I., Ghorbani, P., Goetz, M. R., Groot Koerkamp, B., Gryspeerdt, F., . . . van Santvoort, H. C. (2025). Routine imaging or symptomatic follow-up after resection of pancreatic adenocarcinoma. *JAMA Surgery, 160*(1), 74–84. https://doi.org/10.1001/jamasurg.2024.5024 — PMID 39504033; PMCID PMC11541741
- Gill, S., Ko, Y.-J., Cripps, C., Beaudoin, A., Dhesy-Thind, S., Zulfiqar, M., Zalewski, P., Do, T., Cano, P., Lam, W. Y. H., Dowden, S., Grassin, H., Stewart, J., & Moore, M. (2016). PANCREOX: A randomized phase III study of fluorouracil/leucovorin with or without oxaliplatin for second-line advanced pancreatic cancer in patients who have received gemcitabine-based chemotherapy. *Journal of Clinical Oncology, 34*(32), 3914–3920. https://doi.org/10.1200/JCO.2016.68.5776 — PMID 27621395
- Oettle, H., Riess, H., Stieler, J. M., Heil, G., Schwaner, I., Seraphin, J., Görner, M., Mölle, M., Greten, T. F., Lakner, V., Bischoff, S., Sinn, M., Dörken, B., & Pelzer, U. (2014). Second-line oxaliplatin, folinic acid, and fluorouracil versus folinic acid and fluorouracil alone for gemcitabine-refractory pancreatic cancer: Outcomes from the CONKO-003 trial. *Journal of Clinical Oncology, 32*(23), 2423–2429. https://doi.org/10.1200/JCO.2013.53.6995 — PMID 24982456
- UNICANCER. (n.d.). *Randomized phase II/III trial comparing Folfirinox association [oxaliplatin/irinotecan/LV5FU2] versus gemcitabine in first line of chemotherapy in metastatics pancreas cancers patients* (ClinicalTrials.gov Identifier NCT00112658). Retrieved October 29, 2026, from https://clinicaltrials.gov/study/NCT00112658
- UNICANCER. (n.d.). *Multicentric randomized phase III trial comparing adjuvant chemotherapy with gemcitabine versus 5-fluorouracil, leucovorin, irinotecan and oxaliplatin (mFolfirinox) in patients with resected pancreatic adenocarcinoma* (ClinicalTrials.gov Identifier NCT01526135). Retrieved October 29, 2026, from https://clinicaltrials.gov/study/NCT01526135
- Merck Sharp & Dohme LLC. (2026). *KEYTRUDA (pembrolizumab) injection: Prescribing information* [openFDA drug label, effective 2026-07-10]. https://api.fda.gov/drug/label.json
- National Comprehensive Cancer Network. (2026). *NCCN Guidelines for Patients: Pancreatic cancer* (based on NCCN Guidelines for Pancreatic Adenocarcinoma v2.2026, April 22, 2026). https://www.nccn.org/patients/guidelines/content/PDF/pancreatic-patient.pdf
- Tai et al. (2025), Pan-Asian ESMO guideline: full reference under [S-PanAsia] at the top of this file (PMCID PMC12546840).
