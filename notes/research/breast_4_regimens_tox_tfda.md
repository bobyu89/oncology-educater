# Breast 4. Regimens, exact doses, toxicity management and TFDA licence status: fact-check report

Handbook: Taiwanese oncology NP (專科護理師) handbook, breast cancer chapter (ward practice and 專師甄審 exam)
Verification date: 2026-10-29
Method: Doses, schedules, hold rules and monitoring schedules come from the current US prescribing information (openFDA drug-label API; effective date and SPL set ID listed in section 9). Trial regimens come from the PubMed abstract, PMC full text, ClinicalTrials.gov registry record, or the trial description inside the FDA label. Taiwan licence status comes from my own download of the TFDA licence dataset (InfoId 36; file `36_2.csv`, timestamp 2026-10-27, downloaded 2026-10-29). Nothing was filled from memory. Anything I could not confirm is marked **[UNVERIFIED]**.

**Source tags used inline**
- [A] = PubMed abstract of the cited paper
- [FT] = PMC full text (methods or results section)
- [CT] = ClinicalTrials.gov registry record (API v2, read 2026-10-29)
- [L-xxx] = US prescribing information (openFDA), e.g. [L-Enhertu]; dates in section 9
- [TFDA] = TFDA licence dataset 36 (my download, 2026-10-29)
- [CTCAE] = NCI CTCAE v5.0 spreadsheet downloaded from dctd.cancer.gov
- [FDA-DDI] = FDA web table "Examples of drugs that interact with CYP enzymes and transporter systems" (read 2026-10-29)
- [ED] = editorial written by the trial's own authors (secondary)
- [WEB] = news or society web page (secondary)

**Status tags**
- **[VERIFIED]** = confirmed in a primary or official source that I opened
- **[PARTIAL]** = confirmed only in a secondary source, or only part of the statement confirmed
- **[UNVERIFIED]** = not confirmed; do not print without checking

**APA 7 notes.** All authors up to 20; for 21 or more, the first 19, an ellipsis, then the final author. Study-group bylines are left out. Titles in sentence case. Full reference list in section 10.

Cross-references: trial efficacy data for monarchE, NATALEE, OlympiA, KATHERINE, KEYNOTE-522, CREATE-X, CALGB 9741, APT, DESTINY-Breast05/-11 are in `breast_2_early_trials.md`. Biomarker testing (HER2-low/ultralow, ESR1, PIK3CA) is in `breast_1_taiwan_dx.md`.

---

## 0. Corrections and flags for the editor (read first)

1. **Goserelin (諾雷德 Zoladex) is no longer licensed in Taiwan.** Both licences were cancelled on **2026-10-07** with the reason 「自請註銷」 (cancelled at the holder's request): 3.6 mg 衛署藥輸字第022137號 and 10.8 mg LA 衛署藥輸字第022233號 (holder 臺灣阿斯特捷利康) [VERIFIED; TFDA]. The dataset has **no active goserelin licence**. Any handbook text saying "goserelin 3.6 mg q28d" or "POEMS goserelin" must say that the product is no longer licensed in Taiwan. Context: AstraZeneca is withdrawing monthly Zoladex 3.6 mg in Australia from 2026-11-01 for "commercial reasons" [PARTIAL; WEB, Australian sources only]. I found no Taiwanese announcement. Confirm current supply with the hospital pharmacy.
   - GnRH agonists still licensed in Taiwan **with a breast indication** [VERIFIED; TFDA]:
     - Leuplin Depot 3.75 mg 柳菩林 (衛署藥輸字第019493號 and 第025934號): 「停經前乳癌」.
     - Leuplin Depot 3M 11.25 mg (衛署藥輸字第025193號): 「停經前乳癌，作為術後輔助療法」.
     - Diphereline P.R. 3.75 mg 達菲林 (衛署藥輸字第024382號): 「停經前早期乳癌」.
     - Pamorelin 3.75 mg 帕摩霖 (衛部藥輸字第026704號): with tamoxifen or an AI as adjuvant therapy for premenopausal, HR-positive, high-recurrence-risk early breast cancer after chemotherapy.
   - **None of these licences lists ovarian protection during chemotherapy.** POEMS-style use is off-label in Taiwan [VERIFIED; TFDA, by absence in the 適應症 text].
2. **Dexrazoxane has no Taiwan licence**, active or cancelled. Searches for DEXRAZOXANE, ZINECARD, CARDIOXANE, SAVENE and 右雷佐 all returned nothing [VERIFIED; TFDA]. The US label limits dexrazoxane to women with **metastatic** breast cancer who have **already received 300 mg/m² of doxorubicin** and will continue it [VERIFIED; L-dexrazoxane].
3. **Capecitabine US label now carries a boxed warning: test for DPYD variants before starting**, unless treatment is urgent [VERIFIED; L-Xeloda 2026-02-05]. Other current points:
   - Metastatic breast dose: **1,000 or 1,250 mg/m² twice daily, days 1–14 of a 21-day cycle**.
   - Renal: reduce the dose by 25% for CLcr 30–50 mL/min. For CLcr <30 mL/min the label now says only "a dosage has not been established". Older teaching said "contraindicated".
4. **Ribociclib (Kisqali) ECG schedule is shorter than older teaching** [VERIFIED; L-Kisqali 2026-07-01]:
   - ECG before starting, then again at about **Day 14 of cycle 1**, then as clinically indicated. The label no longer calls for a routine ECG at the start of cycle 2.
   - Electrolytes (K, Ca, P, Mg) at the start of each of the **first 6 cycles**.
   - "**KISQALI is not indicated for concomitant use with tamoxifen**" (QT).
5. **Sacituzumab govitecan (Trodelvy) US label has changed** [VERIFIED; L-Trodelvy 2026-06-24]:
   - New first-line TNBC indications: single agent if not a PD-1/PD-L1 candidate; with pembrolizumab if PD-L1 CPS ≥10.
   - Dose reductions are now written as **10 → 7.5 → 5 mg/kg**. Discontinue if 5 mg/kg is not tolerated.
   - **Primary G-CSF prophylaxis is recommended from cycle 1** for patients at increased risk of febrile neutropenia.
   - **UGT1A1 genotyping is not required.** The label warns that *28/*28 homozygotes are at higher risk.
   - **The TFDA licence has none of the first-line indications** (section 8).
6. **T-DXd (Enhertu)**:
   - US label now includes the post-neoadjuvant indication (DESTINY-Breast05: 5.4 mg/kg q3w ×14 cycles), the neoadjuvant indication (4 cycles, then THP ×4) and first-line therapy with pertuzumab [VERIFIED; L-Enhertu 2026-05-15].
   - **TFDA has the neoadjuvant and first-line-with-pertuzumab indications but not the post-neoadjuvant indication** [VERIFIED; TFDA].
   - Note the odd TFDA dates: issued (發證) 2026-04-23, expiry (有效) 2026-12-07 (licence presumably re-issued; reason not in the dataset).
7. **Talazoparib in Taiwan.** The 1 mg capsule licence (衛部藥輸字第027802號) was cancelled on 2024-06-18. Only the **0.25 mg** capsule (衛部藥輸字第027801號) carries the breast indication; the 0.1 mg capsule is prostate-only [VERIFIED; TFDA]. The breast dose of 1 mg daily [VERIFIED; L-Talzenna] therefore means **four 0.25 mg capsules** (computed).
8. **Palbociclib's TFDA licence now includes HER2-positive maintenance (PATINA)**: with trastuzumab ± pertuzumab and endocrine therapy after induction, for HR+/HER2+ advanced disease. Licence updated (異動) 2026-09-29 [VERIFIED; TFDA].
9. **Not licensed in Taiwan** (2026-10-27 file): elacestrant, camizestrant, pyrotinib (also searched as 吡咯 and 艾瑞妮), vepdegestrant [VERIFIED; TFDA].
   - **Licensed:** imlunestrant (2026-05-15), tucatinib (2026-03-02), datopotamab deruxtecan (2025-11-10), inavolisib (2025-06-02), capivasertib (2024-11-06).
10. **Tamoxifen label typo risk.** Every current US tamoxifen label I opened prints uterine sarcoma as "0.17 for tamoxifen vs. **0.4** for placebo per 1,000 women-years" in the boxed warning [L-tamoxifen]. Read literally, that is *lower* risk on tamoxifen, which contradicts the warning itself. The placebo figure is probably 0.04, but I could not confirm this from a primary source **[UNVERIFIED]**. Do not print the sarcoma figures. Use the endometrial cancer RRs instead (section 6.5).
11. **Cardiac hold rules differ by drug.** Do not teach a single "LVEF <50% hold" rule (section 6.2).
    - Trastuzumab: hold for a ≥16-point absolute fall, or for LVEF below LLN with a ≥10-point fall.
    - T-DM1 and T-DXd: different thresholds.
    - Pertuzumab in **early** breast cancer: baseline LVEF ≥55% required (≥50% after an anthracycline).
12. **Hyperglycaemia grading.** CTCAE v5.0 grades hyperglycaemia by the intervention needed, not by glucose value [VERIFIED; CTCAE]. The PI3K/AKT labels give **fasting-glucose thresholds** (alpelisib uses CTCAE v4.03 values). Teach the mg/dL thresholds, not "grade 3" (section 6.9).
13. **Long contraception windows are easy to miss** [VERIFIED; labels]:
    - Fulvestrant: **1 year** after the last dose.
    - Cyclophosphamide: up to **1 year** (females).
    - Trastuzumab, pertuzumab, T-DM1, T-DXd, Dato-DXd: **7 months**.
    - Full table in section 6.12.
14. **CREATE-X capecitabine dose** (1,250 mg/m² BID, days 1–14 q3w, 8 cycles) is confirmed only by an editorial written by the CREATE-X authors (2,500 mg/m²/day, 8 cycles) [PARTIAL; ED]. The NEJM full text is not open access.
15. **New US indications not licensed in Taiwan:**
    - Dato-DXd: first-line TNBC (US label 2026-05-27).
    - Capivasertib: PTEN-deficient metastatic hormone-sensitive prostate cancer (US label 2026-06-12).
    - These do not change breast dosing.

---

# A. Chemotherapy and HER2 backbones

## 1. Regimen table (exact doses as verified)

| Regimen | Doses and schedule | Source | Status |
|---|---|---|---|
| **AC** (adjuvant) | Doxorubicin **60 mg/m²** IV bolus + cyclophosphamide **600 mg/m²**, day 1 **q21d ×4** | L-doxorubicin §2.1; Jones 2006 [A] | [VERIFIED] |
| **EC** (in KEYNOTE-522) | Epirubicin **90 mg/m²** + cyclophosphamide **600 mg/m²** q3w ×4 | L-Keytruda §14 | [VERIFIED] |
| **ddAC → ddT** (CALGB 9741 arm IV) | AC 60/600 **q2w ×4** → paclitaxel **175 mg/m²** (3-h infusion) **q2w ×4**; filgrastim **5 µg/kg SC days 3–10** of each cycle (rounded to 300 or 480 µg) | Citron 2003 [A]; NCT00003088 [CT] | [VERIFIED] |
| **AC → weekly paclitaxel** (E1199 arm II) | AC 60/600 q3w ×4 → paclitaxel **80 mg/m² over 1 h weekly ×12** | Sparano 2008 [FT, PMC HTML] | [VERIFIED] |
| AC → q3w paclitaxel (E1199 standard arm; US label adjuvant dose) | Paclitaxel **175 mg/m² over 3 h q3w ×4** | Sparano 2008 [FT]; L-paclitaxel | [VERIFIED] |
| AC → docetaxel (E1199 arms III and IV) | Docetaxel 100 mg/m² q3w ×4, or 35 mg/m² weekly ×12 | Sparano 2008 [FT] | [VERIFIED] |
| **TC** (US Oncology 9735) | Docetaxel **75 mg/m²** + cyclophosphamide **600 mg/m²** IV **q3w ×4** | Jones 2006 [A] | [VERIFIED] |
| **TCH** (BCIRG 006) | Docetaxel **75 mg/m²** + carboplatin **AUC 6** q3w **×6**, with trastuzumab, then trastuzumab to complete 1 year | Slamon 2011 [FT] | [VERIFIED] |
| **TCHP** (TRYPHAENA arm C) | Docetaxel 75 mg/m² (**no escalation**) + carboplatin AUC 6 + trastuzumab + pertuzumab **q3w ×6** preoperatively; trastuzumab to 1 year after surgery | L-Perjeta §2.3, §14; Schneeweiss 2013 [A] | [VERIFIED] |
| **THP** (CLEOPATRA, metastatic) | Docetaxel **75 mg/m²** q3w (escalate to 100 mg/m² if tolerated) + trastuzumab 8 → 6 mg/kg + pertuzumab 840 → 420 mg q3w | Baselga 2012 [FT]; L-Perjeta | [VERIFIED] |
| **ddAC → THP (paclitaxel)** | ddAC ×4 → pertuzumab + trastuzumab + paclitaxel ×4 cycles (one of the label's neoadjuvant options) | L-Perjeta §2.3 | [VERIFIED] (weekly paclitaxel 80 mg/m² ×12 is listed in the label's APHINITY description) |
| **Weekly paclitaxel + trastuzumab** (APT) | Paclitaxel **80 mg/m² weekly ×12** + trastuzumab 4 mg/kg load → 2 mg/kg weekly, then trastuzumab to complete 1 year (APT: 9 months of trastuzumab monotherapy) | Tolaney 2015 [FT], [A] | [VERIFIED] |
| **KEYNOTE-522** (stage II–III TNBC) | Cycles 1–4 (q3w): pembrolizumab **200 mg** day 1 + paclitaxel **80 mg/m² days 1, 8, 15** + carboplatin **AUC 5 q3w** *or* **AUC 1.5 days 1, 8, 15**. Cycles 5–8 (q3w): pembrolizumab 200 mg + doxorubicin 60 mg/m² *or* epirubicin 90 mg/m² + cyclophosphamide 600 mg/m². After surgery: pembrolizumab 200 mg q3w **×9**. Label alternative: 400 mg q6w (4 doses neoadjuvant, 5 doses adjuvant) | L-Keytruda §2.2, §14; Schmid 2020 [A] | [VERIFIED] |
| **Capecitabine** (CREATE-X, residual HER2-negative disease) | **1,250 mg/m² BID days 1–14 q3w, 8 cycles** | Toi 2017 [ED]; Masuda 2017 [A] (dose not in abstract) | [PARTIAL] |
| Capecitabine (metastatic, US label) | 1,000 or 1,250 mg/m² BID days 1–14 q21d; with docetaxel 75 mg/m² day 1 | L-Xeloda §2.3 | [VERIFIED] |
| Docetaxel (US label adjuvant) | TAC: docetaxel 75 mg/m² 1 h after doxorubicin 50 mg/m² + cyclophosphamide 500 mg/m², q3w ×6 | L-docetaxel §2.1 | [VERIFIED] |
| Epirubicin (US label) | FEC-100: 5-FU 500 + epirubicin 100 + cyclophosphamide 500 mg/m² day 1 q21d ×6. CEF-120: oral cyclophosphamide 75 mg/m² days 1–14 + epirubicin 60 mg/m² and 5-FU 500 mg/m² days 1 and 8, q28d ×6. Patients on the 120 mg/m² regimen should receive prophylactic antibiotics | L-Ellence §2.1–2.2 | [VERIFIED] |

Not verified:
- "Dose-dense paclitaxel 80 mg/m² weekly after ddAC" as a separate named trial regimen: not checked **[UNVERIFIED]**.
- Neutrophil and platelet thresholds for starting each cycle: institutional; not checked **[UNVERIFIED]**.

## 2. Premedication and administration notes (taxanes, platinum)

- **Paclitaxel** (US label) [VERIFIED; L-paclitaxel 2026-09-09]:
  - Premedicate all patients: **dexamethasone 20 mg PO about 12 h and 6 h before**, diphenhydramine 50 mg IV 30–60 min before, and cimetidine 300 mg *or* ranitidine 50 mg IV 30–60 min before.
  - Use non-PVC containers and polyethylene-lined sets.
  - Do not give if baseline neutrophils are <1,500/mm³ (solid tumours).
  - Hypersensitivity: anaphylaxis/severe reactions in 2–4% in trials; fatal reactions occurred despite premedication; do not rechallenge after a severe reaction.
  - The label gives no reduced-premedication scheme for weekly 80 mg/m². Institutional dexamethasone tapering for weekly paclitaxel **[UNVERIFIED]**.
- **Docetaxel** [VERIFIED; L-docetaxel]:
  - Oral corticosteroid premedication, e.g. **dexamethasone 16 mg/day (8 mg BID) for 3 days starting 1 day before**, to reduce fluid retention and hypersensitivity.
  - Boxed warning: avoid if bilirubin >ULN, or if AST/ALT >1.5×ULN together with ALP >2.5×ULN.
  - Infuse over 1 h q3w.
- **Weekly paclitaxel neuropathy (E1199)**: grade 2–4 neuropathy in **27%** with weekly paclitaxel vs **20%** with q3w paclitaxel; grade 3–4 in 4–8% across arms [VERIFIED; FT]. In APT, grade 3 neuropathy occurred in 3.2% [VERIFIED; A].

## 3. Trastuzumab and pertuzumab dosing

**Trastuzumab IV** [VERIFIED; L-Herceptin 2026-05-29]
- Adjuvant, 52 weeks in total. Either:
  - **4 mg/kg over 90 min, then 2 mg/kg over 30 min weekly** during paclitaxel or docetaxel (12 weeks) or docetaxel/carboplatin (18 weeks); one week after the last weekly dose, **6 mg/kg q3w over 30–90 min**; or
  - **8 mg/kg over 90 min, then 6 mg/kg q3w**.
- "Extending adjuvant treatment beyond one year is not recommended."
- **Missed dose:**
  - Missed by ≤1 week: give the usual maintenance dose (2 or 6 mg/kg) as soon as possible.
  - Missed by >1 week: give a **re-loading dose** (4 mg/kg weekly schedule, or 8 mg/kg q3w schedule) over about 90 min, then resume maintenance.
- The label warns: do not substitute Herceptin for or with T-DM1 or T-DXd (look-alike names).

**Pertuzumab IV** [VERIFIED; L-Perjeta 2026-04-30]
- **840 mg over 60 min, then 420 mg over 30–60 min q3w.**
- Order: pertuzumab and trastuzumab in either order, then the taxane.
- **Observe 30–60 min after each pertuzumab infusion** before starting the next drug.
- Neoadjuvant: 3–6 cycles. Adjuvant: to complete 1 year (up to 18 cycles).
- With an anthracycline regimen, give pertuzumab and trastuzumab **after** the anthracycline is finished.

**Subcutaneous products**
- **Phesgo** (pertuzumab/trastuzumab/hyaluronidase) [VERIFIED; L-Phesgo 2026-05-21]:
  - **Thigh only.**
  - Loading dose 1,200 mg pertuzumab / 600 mg trastuzumab / 30,000 units hyaluronidase over about 8 min.
  - Then 600/600 mg / 20,000 units q3w over about 5 min.
- Trastuzumab-hyaluronidase-oysk with Perjeta: 600 mg/10,000 units SC over 2–5 min q3w, fixed dose regardless of weight [VERIFIED; L-Perjeta].
- Taiwan licence for Phesgo (賀雙妥, 衛部菌疫輸字第001172號): see `breast_2_early_trials.md` section G.

---

# B. Antibody–drug conjugates

## 4. ADC dosing and administration

| Drug | Dose | Infusion | Dose reductions | Key monitoring | Source |
|---|---|---|---|---|---|
| **T-DM1** (Kadcyla 賀癌寧) | **3.6 mg/kg q3w**; never exceed 3.6 mg/kg; early breast cancer **14 cycles** | First infusion 90 min, observe ≥90 min; later infusions 30 min, observe ≥30 min; do not use 5% dextrose | 3.6 → **3.0** → **2.4** mg/kg → stop | Transaminases and bilirubin **before each dose** (boxed warning); platelets before each dose; LVEF before and during | L-Kadcyla 2026-04-01 [VERIFIED] |
| **T-DXd** (Enhertu 優赫得) | **5.4 mg/kg q3w** (all breast indications). Gastric: 6.4 mg/kg | First infusion 90 min; later infusions 30 min if tolerated; dilute in **5% dextrose; do NOT use normal saline** | 5.4 → **4.4** → **3.2** mg/kg → stop; **no re-escalation** | **Highly emetogenic, including delayed nausea**: prophylactic antiemetics. CBC before each dose; LVEF at baseline and regularly; ILD surveillance (section 6.7) | L-Enhertu 2026-05-15 [VERIFIED] |
| T-DXd + pertuzumab (first-line HER2+ metastatic) | Cycle 1: T-DXd 5.4 mg/kg, then pertuzumab **840 mg 30 min after**; later cycles: pertuzumab 420 mg | as above | as above | as above | L-Enhertu [VERIFIED] |
| T-DXd neoadjuvant (DESTINY-Breast11) | 5.4 mg/kg q3w **×4**, then THP ×4 (trastuzumab 6 mg/kg q3w; pertuzumab 840 → 420 mg) | — | — | — | L-Enhertu [VERIFIED] |
| T-DXd post-neoadjuvant (DESTINY-Breast05) | 5.4 mg/kg q3w **×14 cycles** | — | — | Not licensed for this use in Taiwan | L-Enhertu [VERIFIED]; TFDA |
| **Sacituzumab govitecan** (Trodelvy 拓達維) | **10 mg/kg on days 1 and 8 of a 21-day cycle**; never exceed 10 mg/kg | **First infusion over 3 h**; later infusions **1–2 h**; observe during and **≥30 min after** each infusion; cover the bag from light (tubing need not be covered); **normal saline only**; flush with 20 mL saline | 10 → **7.5** → **5** mg/kg → stop | See section 6.8 | L-Trodelvy 2026-06-24 [VERIFIED] |
| **Datopotamab deruxtecan** (Datroway 達卓優) | **6 mg/kg q3w**, maximum **540 mg** (patients ≥90 kg) | Reconstitute with sterile water; **dilute in 5% dextrose; no normal saline** | — | **Stomatitis prophylaxis**: steroid-containing mouthwash (dexamethasone oral solution 0.1 mg/mL **four times daily**) from the start of treatment; ice chips or ice water in the mouth during the infusion. **Eyes**: preservative-free lubricating drops; no contact lenses. Ocular adverse reactions 38%. Premedication: antihistamine (diphenhydramine 25–50 mg) and antipyretic (acetaminophen 650–1,000 mg) 30–60 min before | L-Datroway 2026-05-27 [VERIFIED] |

**T-DXd neutropenia and LVEF holds** [VERIFIED; L-Enhertu Table 3]
- Neutropenia:
  - Grade 3 (ANC 0.5 to <1.0 ×10⁹/L): hold until grade ≤2, then same dose.
  - Grade 4: hold until grade ≤2, then reduce one level.
  - Febrile neutropenia: hold until resolved, then reduce one level.
- Thrombocytopenia:
  - Grade 3: hold until grade ≤1, then same dose.
  - Grade 4: hold until grade ≤1, then reduce one level.
- LVEF rules: see section 6.2.

**T-DM1 liver rules (early breast cancer)** [VERIFIED; L-Kadcyla Table 2]
- ALT:
  - Grade 2–3 (>3 to ≤20×ULN): hold until grade ≤1, then reduce one level.
  - Grade 4: stop.
- Total bilirubin:
  - >1.0 to 2.0×ULN on the day of treatment: hold until ≤1.0×ULN, then reduce one level.
  - >2×ULN at any time: stop.
- Nodular regenerative hyperplasia (any grade): stop permanently.
- ILD or pneumonitis: stop permanently.

---

# C. Endocrine therapy and targeted oral agents

## 5. Doses at a glance

### 5.1 Endocrine agents [VERIFIED unless marked]

| Drug | Dose | Notes | Source |
|---|---|---|---|
| **Tamoxifen** | **20 mg daily** (label range 20–40 mg; doses >20 mg split morning and evening); DCIS and risk reduction 20 mg daily ×5 years | Adjuvant duration in label: 5 years. Extended therapy evidence is in breast_2 | L-tamoxifen 2026-03-19 |
| **Letrozole** | **2.5 mg daily**, with or without food | Cirrhosis or severe hepatic impairment: 2.5 mg **every other day** | L-Femara 2026-06-11 |
| **Anastrozole** | **1 mg daily** | ATAC used 5 years | L-Arimidex 2026-03-02 |
| **Exemestane** | **25 mg daily after a meal** | Label: check **25-hydroxy vitamin D before starting an AI** | L-Aromasin 2025-12-24 |
| **Fulvestrant** | **500 mg IM** as **two 5 mL injections, one per buttock, 1–2 min each**, on **days 1, 15, 29, then monthly** | Moderate hepatic impairment: 250 mg. Bleeding risk (anticoagulants, thrombocytopenia); sciatic nerve near the dorsogluteal site. 500 mg beat 250 mg in CONFIRM (Di Leo 2010) | L-Faslodex 2020-09-25; Di Leo 2010 [A] |
| **Goserelin** | **3.6 mg SC every 28 days** into the anterior abdominal wall below the navel | US breast indication is the 3.6 mg depot only (palliative, pre-/perimenopausal advanced breast cancer). **Not licensed in Taiwan since 2026-10-07** (flag 1) | L-Zoladex 2026-03-24; TFDA |
| Leuprorelin / triptorelin | Taiwan licences with a breast indication are listed in flag 1 | US leuprolide labels have no breast indication. Taiwan monthly vs 3-monthly dosing for breast: from the Taiwan package inserts, not read **[UNVERIFIED]** | TFDA |
| **Elacestrant** (Orserdu) | **345 mg daily with food** (reduces nausea); reductions 258 → 172 mg → stop | ESR1-mutated (plasma) ER+/HER2− advanced disease. **Monitor lipids** (hypercholesterolaemia 30%, hypertriglyceridaemia 27%). **Not licensed in Taiwan** | L-Orserdu 2026-06-24; TFDA |
| **Imlunestrant** (Inluriyo 盈乳樂) | **400 mg daily on an empty stomach** (≥2 h before or 1 h after food) | Pre-/perimenopausal women and men: add a GnRH agonist. Reduce in moderate or severe hepatic impairment. Taiwan: licensed 2026-05-15 | L-Inluriyo 2026-06-04; TFDA |
| **Camizestrant** (Etcamah) | **75 mg daily**, with or without food, **added to the CDK4/6 inhibitor already in use** (abemaciclib, palbociclib or ribociclib) once ESR1 is detected on ctDNA (tested every 3 months after ≥6 months of AI + CDK4/6 inhibitor) | **ECG before start, then weekly for 2 weeks**. Bradycardia: monitor heart rate more often in the first 30 days. QTc risk greatest with ribociclib. **No dose reductions.** Accelerated approval. **Not licensed in Taiwan** | L-Etcamah 2026-09-04; TFDA |

### 5.2 CDK4/6 inhibitors [VERIFIED]

| | **Palbociclib** (Ibrance 愛乳適) | **Ribociclib** (Kisqali 擊癌利) | **Abemaciclib** (Verzenio 捷癌寧) |
|---|---|---|---|
| Start dose | **125 mg daily, 21 days on / 7 off** (28-day cycle). Tablets with or without food; capsules **with food** | Metastatic: **600 mg daily, 21/7**. **Adjuvant: 400 mg daily, 21/7, for 3 years** (with an AI) | **150 mg BID continuous** (with fulvestrant, tamoxifen or an AI); **200 mg BID** as monotherapy. Adjuvant: **2 years** |
| Dose levels | 125 → 100 → 75 mg → stop | Metastatic 600 → 400 → 200 mg → stop; adjuvant 400 → 200 mg → stop | Combination 150 → 100 → 50 mg BID → stop; monotherapy 200 → 150 → 100 → 50 mg BID |
| CBC | Before start; **day 1 and day 15 of cycles 1–2**; then each cycle. If max grade 1–2 neutropenia in the first 6 cycles: every 3 months | Before start; **every 2 weeks for 2 cycles**, then at the start of each of the next 4 cycles | Before start; **every 2 weeks for 2 months**, monthly for the next 2 months |
| Neutropenia rule | G3 on day 1: hold, repeat CBC within 1 week, resume at the same dose when ≤G2. G3 on day 15 of cycles 1–2: continue and recheck on day 22. **G3 with fever ≥38.5 °C and/or infection, or G4: hold, then next lower dose** | G3: hold until ≤G2, same dose; if it recurs, lower dose. G3 febrile or G4: hold, then lower dose | G3: hold until ≤G2, no reduction. Recurrent G3 or G4: hold, then lower dose. **If G-CSF is used, hold abemaciclib ≥48 h after the last G-CSF dose** |
| Liver | — | **LFTs every 2 weeks for 2 cycles, at the start of each of the next 4 cycles**. ALT/AST >3×ULN **with** bilirubin >2×ULN (no cholestasis): stop | **ALT, AST, bilirubin every 2 weeks for 2 months, monthly for 2 months**. ALT/AST >3×ULN with bilirubin >2×ULN, or G4: stop |
| ECG / QT | Not required | **ECG at baseline and about day 14 of cycle 1**; electrolytes at the start of the first 6 cycles. QTcF >480 ms: hold until ≤480 ms (adjuvant: same dose; metastatic: lower dose). QTcF >500 ms: hold, then lower dose. Stop for TdP, polymorphic VT or syncope. **Not with tamoxifen** | Not required |
| Signature AE | Neutropenia 80% (PALOMA-2) and 83% (PALOMA-3); grade ≥3 66% | Adjuvant (NATALEE): neutrophil decrease 94% (grade 3–4 45%); febrile neutropenia 0.3%. QTcF >500 ms in 0.3%; >60 ms increase in 2% | **Diarrhoea 81–90%; grade 3 8–20%; median onset 6–8 days** (section 6.4). VTE: in early breast cancer **hold for any-grade VTE** |
| Strong CYP3A inhibitor | Avoid; if unavoidable, **75 mg daily** | Avoid; if unavoidable, adjuvant **200 mg**, metastatic **400 mg** | Avoid ketoconazole; other strong inhibitors: reduce to **100 mg BID** (or 50 mg BID if already at 100 mg) |
| GnRH agonist | Pre-/perimenopausal women; consider in men | Pre-/perimenopausal women **and men** | Pre-/perimenopausal women; men with an AI |
| ILD/pneumonitis | Permanently stop for severe ILD | G2: hold, then lower dose; recurrent G2 or G3–4: stop | Persistent G2: hold, then lower dose; G3–4: stop |
| Contraception (females) | ≥3 weeks after the last dose (males 3 months) | ≥3 weeks | 3 weeks |
| Source | L-Ibrance tablets and capsules 2026-07-02 | L-Kisqali 2026-07-01 | L-Verzenio 2026-07-13 |

### 5.3 PI3K/AKT inhibitors, PARP inhibitors and HER2 TKIs [VERIFIED]

| Drug | Dose | Dose levels | Key points | Source |
|---|---|---|---|---|
| **Alpelisib** (Piqray 愛克利) | **300 mg daily with food** + fulvestrant 500 mg | 300 → 250 → 200 mg → stop (only one reduction for pancreatitis) | Missed dose: take within 9 h with food. **Antihistamine before rash onset** lowered rash incidence. Severe cutaneous reactions: stop permanently | L-Piqray 2025-12-15 |
| **Capivasertib** (Truqap 泛抑癌) | **400 mg BID (about 12 h apart), 4 days on / 3 days off**, with or without food, + fulvestrant | 400 → **320** → **200** mg BID, 4 on/3 off → stop | Weekly calendar: days 1–4 morning and evening 2×200 mg; **no dosing days 5–7**. Missed dose: take if ≤4 h late, otherwise skip | L-Truqap 2026-06-12 |
| **Inavolisib** (Itovebi 癌妥飛) | **9 mg daily** + palbociclib 125 mg 21/7 + fulvestrant | 9 → 6 → 3 mg → stop | PIK3CA mutation in **plasma**. Reduce the starting dose in moderate or severe renal impairment | L-Itovebi 2026-04-21 |
| **Olaparib** (Lynparza 令癌莎) | **300 mg BID** tablets, with or without food. **Adjuvant: 1 year** (OlympiA) | 300 → **250** → **200** mg BID | CLcr 31–50 mL/min: 200 mg BID. Avoid strong or moderate CYP3A inhibitors. **CBC at baseline and monthly**. MDS/AML in about 1.2% across indications; pneumonitis 1.0% | L-Lynparza 2025-07-10; Tutt 2021 [A, FT] |
| **Talazoparib** (Talzenna 達勝癌) | **1 mg daily** (breast) | — | Taiwan: 4 × 0.25 mg capsules (flag 7) | L-Talzenna 2026-04-10; TFDA |
| **Tucatinib** (Tukysa 杜凱莎) | **300 mg BID** + trastuzumab + capecitabine **1,000 mg/m² BID days 1–14 q21d** (within 30 min after a meal; can be taken at the same time as tucatinib) | Severe hepatic impairment: 200 mg BID | HER2CLIMB also allowed trastuzumab 600 mg SC day 1 q21d | L-Tukysa 2024-11-04 |
| **Neratinib** (Nerlynx 賀儷安) | **240 mg (6 × 40 mg) daily with food**. Extended adjuvant: up to 1 year. Metastatic: days 1–21 q21d + capecitabine 750 mg/m² BID days 1–14 | Severe hepatic impairment: 80 mg | **Loperamide from the first dose for the first 56 days** (unless using the 2-week dose escalation); after day 56, titrate to 1–2 stools/day | L-Nerlynx 2026-07-02 |

---

# D. Toxicity management

## 6.1 Anthracycline cumulative dose, cardiotoxicity and dexrazoxane

**Doxorubicin** [VERIFIED; L-doxorubicin (Pfizer) 2026-05-05]
- Boxed warning: estimated cardiomyopathy risk by cumulative dose (given q3w):

  | Cumulative dose | Cardiomyopathy risk |
  |---|---|
  | 300 mg/m² | 1–2% |
  | 400 mg/m² | 3–5% |
  | 450 mg/m² | 5–8% |
  | 500 mg/m² | 6–20% |

- "Cumulative doses **above 550 mg/m²** are associated with an increased risk of cardiomyopathy."
- **Count prior anthracyclines and anthracenediones** in the cumulative total.
- Risk is additive with mediastinal radiotherapy, cyclophosphamide and trastuzumab.
- LVEF (MUGA or echo; same method each time): before, during and after treatment, **more often above 300 mg/m²**.
- Stop for signs or symptoms of cardiomyopathy.
- Hepatic dosing. The label's Table 1 column is headed "Dosage Modification" and gives **50%** for bilirubin 1.2–3 mg/dL and **75%** for 3.1–5 mg/dL. The text says "reduce the dose", so these are read as **reductions** (i.e. give 50% and 25% of the dose). That reading is my interpretation: [PARTIAL].

  | Bilirubin | Label "dosage modification" | Dose given (interpretation) |
  |---|---|---|
  | 1.2–3 mg/dL | 50% | 50% of dose |
  | 3.1–5 mg/dL | 75% | 25% of dose |
  | >5 mg/dL, or Child-Pugh C | Do not start; discontinue (contraindicated) | — |

- Extravasation: stop the infusion and apply **ice**.
- Secondary AML/MDS warning.
- Swain 2003 retrospective analysis: estimated doxorubicin-related CHF **26% at 550 mg/m²**, more frequent in patients >65 years after 400 mg/m² [VERIFIED; A]. This is higher than the older 7% estimate cited in that paper.

**Epirubicin** [VERIFIED; L-Ellence 2026-07-24]
- Boxed warning: cardiomyopathy incidence **0.9% at 550 mg/m², 1.6% at 700 mg/m², 3.3% at 900 mg/m²**.
- "Cumulative doses of **900 mg/m²** ELLENCE should generally be avoided."
- After trastuzumab (long half-life), delay epirubicin until trastuzumab has cleared, where possible.
- An epirubicin-to-doxorubicin conversion factor (for combined cumulative dose) was not found in the sources I opened **[UNVERIFIED]**.

**Dexrazoxane** [VERIFIED; L-dexrazoxane 2026-08-10]
- Indication: reduce doxorubicin cardiomyopathy in **metastatic breast cancer** after a **cumulative 300 mg/m²**, when doxorubicin will continue. "Do not use with the initiation of doxorubicin therapy."
- Dose: **10:1 ratio** (e.g. 500 mg/m² dexrazoxane for 50 mg/m² doxorubicin).
- **Give doxorubicin within 30 min after the dexrazoxane infusion ends**; never give doxorubicin first.
- CLcr <40 mL/min: halve the dose (5:1).
- **Not licensed in Taiwan** (flag 2).

**ESC 2022 cardio-oncology guideline (Lyon 2022)** [PARTIAL; I could read only the text portions, not the recommendation tables, which are images]
- Asymptomatic cancer therapy-related cardiac dysfunction (CTRCD), Table 3:

  | Severity | Definition |
  |---|---|
  | Severe | New LVEF fall to **<40%** |
  | Moderate | New LVEF fall by **≥10 points to 40–49%**; or by <10 points to 40–49% **plus** either a new relative GLS decline >15% or a new rise in cardiac biomarkers |
  | Mild | LVEF ≥50% **plus** a new relative GLS decline >15% and/or a new biomarker rise |

- Anthracyclines: in moderate-risk patients, "TTE should be considered after a cumulative dose of ≥250 mg/m² of doxorubicin or equivalent". Troponin and natriuretic peptide **every two cycles** during anthracycline therapy and within 3 months after (Class IIa, Level C, in moderate risk).
- Dexrazoxane "should be considered (at least 30 min prior to each anthracycline cycle)" in high-risk patients or those planned for high cumulative doses.
- ASCO 2017 (Armenian): high-risk survivors may warrant routine cardiac imaging surveillance after therapy. The abstract gives no intervals [VERIFIED; A]; specific intervals **[UNVERIFIED]**.

## 6.2 HER2-directed therapy: LVEF monitoring and hold rules (per label)

| Drug | Baseline and schedule | Hold | Resume / stop | Source |
|---|---|---|---|---|
| **Trastuzumab** | LVEF **immediately before** starting; **every 3 months during and at completion**; **every 6 months for ≥2 years after** adjuvant therapy; **every 4 weeks** while held | Hold **≥4 weeks** for **≥16-point absolute LVEF fall**, *or* **LVEF below LLN with a ≥10-point fall** | Resume if **within 4–8 weeks** LVEF is back within normal limits and the absolute fall is **≤15 points**. **Stop for a persistent (>8 weeks) decline, or after >3 holds** for cardiomyopathy | L-Herceptin 2026-05-29 [VERIFIED] |
| **Pertuzumab** (+ trastuzumab) | Metastatic: baseline **≥50%**; recheck about **every 12 weeks**. Early breast cancer: baseline **≥55%** (≥50% after anthracycline); about every 12 weeks (**once during neoadjuvant**) | Hold both ≥3 weeks. Metastatic: **<40%**, or **40–45% with a ≥10-point fall**. Early: **<50% with a ≥10-point fall** | Resume after 3 weeks if: metastatic **>45%**, or 40–45% with a <10-point fall; early **≥50%** or <10 points below baseline | L-Perjeta [VERIFIED] |
| **T-DM1**, metastatic | Before and during | LVEF **<40%**: hold, repeat within 3 weeks; stop if confirmed. **40–45% with a ≥10-point fall**: hold, repeat within 3 weeks; stop if not back within 10 points | 40–45% with a <10-point fall: continue, repeat within 3 weeks. >45%: continue. Symptomatic CHF: stop | L-Kadcyla [VERIFIED] |
| **T-DM1**, early breast cancer | Before and during | **<45%**: hold, repeat within 3 weeks; stop if confirmed. **45% to <50% with a ≥10-point fall**: hold, repeat within 3 weeks; stop if still <50% and not recovered | 45% to <50% with a <10-point fall: continue, repeat within 3 weeks. Stop for symptomatic CHF, grade 3–4 LVSD or heart failure, or grade 2 heart failure with LVEF <45% | L-Kadcyla [VERIFIED] |
| **T-DXd** | LVEF before starting and "at regular intervals"; **not studied with baseline LVEF <50%** | **40–45% with a 10–20-point fall**: hold, repeat within 3 weeks; stop if not back within 10 points. **<40%, or >20-point fall**: hold, repeat within 3 weeks; stop if confirmed | >45% with a 10–20-point fall: continue. 40–45% with a <10-point fall: continue, repeat within 3 weeks. **Symptomatic CHF: stop** | L-Enhertu [VERIFIED] |

Background figures (Herceptin label) [VERIFIED]:
- Symptomatic myocardial dysfunction is 4–6-fold higher with trastuzumab; highest with an anthracycline.
- Discontinuation for cardiac toxicity:

  | Trial | Rate |
  |---|---|
  | NSABP B-31, AC→TH arm (median follow-up 8.7 years) | 15% |
  | HERA (1 year of trastuzumab) | 2.6% |
  | BCIRG 006, TCH | 2.9% |
  | BCIRG 006, AC→TH | 5.7% |

- In BCIRG 006, CHF and cardiac dysfunction were significantly more frequent with AC-T plus trastuzumab than with TCH (P < 0.001) [VERIFIED; Slamon 2011 A].
- TRYPHAENA: symptomatic LVSD 2.7% in arm B only; LVEF fall ≥10 points to <50% in 5.6% / 5.3% / 3.9% (arms A / B / C) [VERIFIED; A].

## 6.3 CDK4/6 inhibitors: neutropenia, ECG, LFT

- Schedules and rules: table in section 5.2 [VERIFIED; labels].
- Nursing teaching points (from the labels):
  - Palbociclib and ribociclib neutropenia is concentration-dependent and usually managed by holds or lower doses, not G-CSF. G-CSF is not mentioned in the Ibrance or Kisqali neutropenia tables; Verzenio says to hold the drug for ≥48 h after any G-CSF [VERIFIED; L-Verzenio].
  - Ribociclib: correct electrolytes before starting. Avoid other QT-prolonging drugs and strong CYP3A inhibitors.
  - Abemaciclib and ribociclib need LFT schedules; palbociclib does not.
  - ILD/pneumonitis is a class warning. Ribociclib, metastatic trials: 1.6% any grade, 0.1% fatal [VERIFIED; L-Kisqali].

## 6.4 Abemaciclib diarrhoea [VERIFIED; L-Verzenio 2026-07-13]

- Incidence 81–90% (4 trials, n = 3,691); grade 3 in 8–20%; median onset **6–8 days**; most in month 1.
- Median duration: grade 2, 6–11 days; grade 3, 5–8 days.
- 19–26% needed a dose interruption and 13–23% a reduction.
- **Patient instruction: at the first loose stool, start an antidiarrhoeal (e.g. loperamide), increase oral fluids, and call the team.**
- Dose rules:

  | Diarrhoea | Action |
  |---|---|
  | G1 | No change |
  | G2 not resolved to ≤G1 within 24 h | Hold until resolved; no reduction |
  | G2 persisting or recurring at the same dose despite maximal support | Hold until ≤G1, then lower dose |
  | G3–4, or hospitalisation | Hold until ≤G1, then lower dose |

- Loperamide doses for abemaciclib are not specified in the Verzenio label. The SG label regimen (4 mg, then 2 mg per loose stool, maximum 16 mg/day) is SG-specific; do not transfer it without a source **[UNVERIFIED for abemaciclib]**.

## 6.5 Tamoxifen: VTE, endometrial cancer, CYP2D6 and SSRIs

**Label** [VERIFIED; L-tamoxifen 2026-03-19]
- Boxed warning (risk-reduction and DCIS settings): uterine malignancies, stroke and pulmonary embolism, some fatal.
  - Endometrial adenocarcinoma: 2.20 vs 0.71 per 1,000 woman-years.
  - Stroke: 1.43 vs 1.00.
  - PE: 0.75 vs 0.25.
  - Sarcoma figure: see flag 10.
  - "The benefits … outweigh its risks in women already diagnosed with breast cancer."
- NSABP P-1 invasive endometrial cancer:

  | Group | Tamoxifen vs placebo | RR (95% CI) |
  |---|---|---|
  | All | 33 vs 14 cases | **2.48 (1.27–4.92)** |
  | Age ≥50 at randomisation | — | **4.50 (1.78–13.16)** |
  | Age ≤49 at randomisation | — | 0.94 (0.28–2.89) |

  All tamoxifen-arm cases were FIGO stage I.
- Instructions:
  - Promptly evaluate abnormal vaginal bleeding.
  - **Annual gynaecological examination.**
  - Report menstrual irregularity, bleeding, pelvic pain or pressure.
- VTE: risk rises further when given together with chemotherapy. Weigh risk in women with prior VTE. In a P-1 sub-study (n = 81), screening for factor V Leiden / prothrombin mutation showed no apparent benefit.

**NSABP P-1** (Fisher 1998) [VERIFIED; A]
- Endometrial cancer RR **2.53 (1.35–4.97)**, mainly in women ≥50 years.
- Stroke, PE and DVT increased, also mainly in women ≥50.

**CYP2D6 and antidepressants**
- **CPIC 2018** (Goetz 2018) [VERIFIED; FT]:
  - For normal and ultrarapid metabolisers: "**Avoid moderate and strong CYP2D6 inhibitors**" and start the standard 20 mg/day.
  - "In general, prolonged overlap of tamoxifen with strong and moderate CYP2D6 inhibitors should be avoided."
  - Poor metabolisers: consider an AI (with OFS if premenopausal). 40 mg/day raises but does not normalise endoxifen.
- **FDA inhibitor classification** [VERIFIED; FDA-DDI]:

  | Class | Drugs |
  |---|---|
  | **Strong** CYP2D6 inhibitors | **paroxetine, fluoxetine, bupropion**, quinidine, terbinafine |
  | **Moderate** | **duloxetine**, mirabegron, cinacalcet, abiraterone |
  | **Weak** | **sertraline, escitalopram**, celecoxib, cimetidine |
  | Not listed as a CYP2D6 inhibitor (listed only as a substrate) | Venlafaxine |

- **Kelly 2010** (Ontario cohort, n = 2,430 women ≥66 years on tamoxifen plus one SSRI) [VERIFIED; A]:
  - Absolute increases of 25%, 50% and 75% in the share of tamoxifen time overlapping with **paroxetine** were linked to 24%, 54% and 91% higher breast cancer mortality.
  - No such risk with other antidepressants.
  - One extra breast cancer death per 19.7 patients at the median 41% overlap.
- Practical implication for hot-flush treatment on tamoxifen: avoid paroxetine, fluoxetine and bupropion; duloxetine is a moderate inhibitor (also avoid per CPIC). Venlafaxine is not an inhibitor on the FDA list. The handbook may present venlafaxine as the usual choice, but **"preferred" status from a guideline: [UNVERIFIED]**.

## 6.6 Aromatase inhibitors: arthralgia and bone health

**Label data** [VERIFIED]
- **ATAC** (anastrozole vs tamoxifen): arthritis 17% vs 14%; arthralgia 15% vs 11%; osteoporosis 11% vs 7%; fractures 10% vs 7% (OR 1.57; spine, hip or wrist 4% vs 3%) [L-Arimidex].
  - Ischaemic cardiovascular events in women with pre-existing ischaemic heart disease: 17% vs 10%.
  - Labels say "consider BMD monitoring" and "consider cholesterol monitoring".
- **BIG 1-98** (letrozole vs tamoxifen): arthralgia/arthritis 25.4% vs 20.6%; fractures 14.7% vs 11.4%; hypercholesterolaemia 52.3% vs 28.6% [L-Femara].
  - Lumbar spine BMD at 24 months: median −4.1% with letrozole vs +0.3% with tamoxifen.
- **Exemestane**: lumbar spine BMD −3.1% to −3.5% at 24 months.
  - Women with, or at risk of, osteoporosis should have BMD "formally assessed by bone densitometry at the commencement of treatment".
  - **Check 25-OH vitamin D before starting an AI** [L-Aromasin].

**Arthralgia management trials** [VERIFIED; A]
- **SWOG S1200** (Hershman 2018, JAMA; n = 226):
  - True acupuncture: 12 sessions over 6 weeks, then weekly for 6 weeks.
  - 6-week worst-pain score fell by 2.05 points, vs 1.07 (sham) and 0.99 (waitlist).
- **SWOG S1202** (Henry 2018, JCO; n = 299):
  - Duloxetine for 13 weeks lowered average joint pain by 0.82 points vs placebo at 12 weeks (95% CI −1.24 to −0.40).
  - More low-grade adverse events (78% vs 50%).
  - Duloxetine is a moderate CYP2D6 inhibitor: fine with an AI, avoid with tamoxifen (section 6.5).

**Bone-modifying agents** [VERIFIED; A]
- **ASCO 2019 osteoporosis guideline** (Shapiro): assess fracture risk with established tools. Order a BMD test when risk is substantial. When a drug is needed, **bisphosphonates or denosumab at osteoporosis doses** are preferred.
  - The repeat-DXA interval is not in the abstract **[UNVERIFIED]**.
- **ABCSG-18** (Gnant 2015): **denosumab 60 mg SC every 6 months** in postmenopausal women on an AI (n = 3,420). Time to first clinical fracture HR **0.50 (0.39–0.65)**.
- **EBCTCG 2015 bisphosphonate meta-analysis**: benefit in postmenopausal women only. Details in breast_2 §21.
- Adjuvant zoledronic acid dose and schedule: not verified here **[UNVERIFIED]**.

## 6.7 T-DXd interstitial lung disease (label) [VERIFIED; L-Enhertu 2026-05-15]

**Boxed warning:** ILD/pneumonitis, including fatal cases. **Permanently stop for grade ≥2 ILD.**

**Incidence**

| Setting | ILD | Median onset | Fatal |
|---|---|---|---|
| 5.4 mg/kg monotherapy | **12%** | 5.5 months (0.9–31.5) | 0.9% |
| With pertuzumab | 12% | 8.0 months | 0.5% |
| T-DXd → THP (DESTINY-Breast11) | 4.4% | 2.7 months | 1 patient (0.3%) |

- ILD grade 1–2 is more frequent with **moderate renal impairment**.

**CTCAE v5.0 pneumonitis grades** [VERIFIED; CTCAE]

| Grade | Definition |
|---|---|
| 1 | Asymptomatic; clinical or diagnostic observations only; intervention not indicated |
| 2 | Symptomatic; medical intervention indicated; limiting instrumental ADL |
| 3 | Severe symptoms; limiting self-care ADL; oxygen indicated |
| 4 | Life-threatening respiratory compromise; urgent intervention indicated |

**Management (label)**

| ILD grade | Action |
|---|---|
| **Grade 1** (asymptomatic) | **Interrupt** until resolved to grade 0. Resolved **≤28 days** from onset: same dose. Resolved **>28 days**: reduce one level. **Consider corticosteroids (e.g. ≥0.5 mg/kg/day prednisolone or equivalent)** as soon as ILD is suspected |
| **Grade ≥2** (symptomatic) | **Permanently stop.** Start corticosteroids promptly (**≥1 mg/kg/day prednisolone or equivalent**) for **≥14 days**, then taper over **≥4 weeks** |

- All patients: report cough, dyspnoea, fever or new respiratory symptoms immediately. Investigate suspected ILD with imaging; consider pulmonology referral.
- **Adjuvant setting:** rule out radiotherapy-related pneumonitis. If only radiation pneumonitis is suspected: consider interruption for grade 2; stop permanently for grade ≥3.
- **Retreatment after grade 1 ILD** (Rugo 2025, pooled 9 trials, n = 2,145) [VERIFIED; A]:
  - 9% had grade 1 ILD; 45 of those 193 were retreated.
  - ILD recurred in 33.3% (15/45); all recurrences grade 1–2; none grade ≥3 or fatal.
  - Median time to recurrence 64 days.
  - Erratum to this paper published 2026 (not reviewed).
- **Baseline and routine chest CT schedules are not stated in the US label** **[UNVERIFIED as a label requirement]**. For DESTINY-Breast05 CT practice, see breast_2.

## 6.8 Sacituzumab govitecan: neutropenia, diarrhoea, premedication, UGT1A1

[VERIFIED; L-Trodelvy 2026-06-24 unless marked]

**Boxed warning:** neutropenia and diarrhoea.

**Premedication before each dose**
- Antipyretic, plus **H1 and H2 blockers**. Corticosteroids may be used if there was a prior infusion reaction.
- Antiemetics: **2- or 3-drug** regimen, e.g. dexamethasone + 5-HT3 antagonist or NK1 antagonist. Give take-home antiemetics.

**Neutropenia**
- Incidence: any grade 64%; grade 3–4 48%; febrile 6%; median onset 19 days; neutropenic colitis 1.4%.
- **Primary G-CSF from cycle 1** for patients at increased FN risk: older age, previous neutropenia, poor PS, organ dysfunction, comorbidities.
- **Hold: ANC <1,500/mm³ on day 1, <1,000/mm³ on day 8, or neutropenic fever.**
- Reduce one level for each febrile neutropenia or prolonged grade 3–4 neutropenia.

**Diarrhoea**
- Incidence: any grade 62%; grade 3–4 10%; AKI from dehydration 0.6%.
- At onset, exclude infection, then start **loperamide 4 mg, then 2 mg after each episode, maximum 16 mg/day**. Stop loperamide **12 h after diarrhoea resolves**.
- Hold for grade 3–4 diarrhoea at the time of a scheduled dose; resume at ≤G1 with one dose level lower.
- **Cholinergic syndrome** (cramping, diarrhoea, salivation): **atropine** premedication for later doses.

**Hypersensitivity**
- Hypersensitivity reactions 28% (13% within 24 h); grade 3–4 1.5%; anaphylaxis <0.1%.
- Stop permanently for grade 4 infusion reactions.

**UGT1A1**

| Genotype | Grade 3–4 neutropenia | Median time to neutropenia | Grade 3–4 anaemia |
|---|---|---|---|
| *28/*28 (n = 138) | 57% | 9 days | 17% |
| *1/*28 (n = 531) | 48% | 19 days | 9% |
| *1/*1 (n = 533) | 41% | 21 days | 8% |

- **The label gives no genotype-based starting dose.** Monitor homozygotes closely.
- ASCENT safety analysis (Rugo 2022) [VERIFIED; A]: *28/*28 vs *1/*28 and *1/*1:

  | Event | *28/*28 | *1/*28 | *1/*1 |
  |---|---|---|---|
  | Grade ≥3 SG-related neutropenia | 59% | 47% | 53% |
  | Febrile neutropenia | 18% | 5% | 3% |
  | Diarrhoea | 15% | 9% | 10% |

- Relevance of UGT1A1*6 (common in East Asians) to SG toxicity: not checked **[UNVERIFIED]**.

**Contraception:** females 6 months after the last dose; males 3 months.

## 6.9 Hyperglycaemia with PI3K/AKT inhibitors

**Grading.** CTCAE v5.0 grades hyperglycaemia by intervention [VERIFIED; CTCAE]:
- G1: abnormal glucose, no intervention.
- G2: oral agent started or diabetic regimen changed.
- G3: insulin started or hospitalisation.
- G4: life-threatening.

The labels act on **fasting glucose (FG) values**.

**Baseline (all three drugs):** fasting glucose and HbA1c; optimise glucose before starting [VERIFIED; labels].

| Fasting glucose | **Alpelisib** (L-Piqray, v4.03 grading) | **Capivasertib** (L-Truqap) | **Inavolisib** (L-Itovebi) |
|---|---|---|---|
| >ULN–160 mg/dL (≤8.9 mmol/L) | No dose change; start or intensify anti-hyperglycaemics | Consider starting or intensifying oral agents (also if HbA1c >7%) | No change; diet and hydration; oral agents if risk factors |
| 161–250 mg/dL | No dose change; intensify. If not ≤160 within **21 days**, reduce one level | **Hold** until ≤160. Recovery ≤28 days: same dose; >28 days: lower dose | **Hold** until ≤160, then same dose. If >200–250 persists 7 days on treatment: consult a diabetes specialist |
| 251–500 mg/dL | **Hold**; IV fluids. ≤160 within **3–5 days**: resume one level lower. Not within 3–5 days: consult. Not within **21 days**: stop | **Hold** until ≤160. ≤28 days: one level lower; >28 days: **stop** | **Hold**. ≤160 within 7 days: same dose; ≥8 days: one level lower. Recurrence within 30 days: lower dose |
| >500 mg/dL | Hold; recheck within 24 h. If confirmed >500: **stop** | Hold. Life-threatening sequelae, or ≥500 after 24 h: **stop** | Hold; assess volume and ketosis. When ≤160: one level lower (full text truncated in my read) |
| **Monitoring schedule** | FG **≥ weekly for 2 weeks, then ≥ every 4 weeks**; HbA1c every 3 months | FG on **day 3 or 4 of the dosing week in weeks 1, 2, 4, 6 and 8**, then monthly. **At least twice weekly** (on and off days) during hyperglycaemia. On anti-diabetic drugs: weekly for 2 months, then every 2 weeks. HbA1c every 3 months | FG **every 3 days in week 1**, weekly for weeks 2–4, **every 2 weeks for the next 8 weeks**, then every 4 weeks; HbA1c every 3 months |
| Drug choice | **Metformin** (SOLAR-1 titration: 500 mg daily → 500 mg BID → 500 mg with breakfast + 1,000 mg with dinner → 1,000 mg BID). SGLT2 inhibitors, TZDs or DPP-4 inhibitors per label. Insulin 1–2 days if needed. **Consider metformin premedication** in patients at risk | Withhold in situations raising DKA risk (serious infection, acute illness). **Withhold at once if ketoacidosis is suspected; stop if confirmed** | Ketoacidosis with a fatal outcome reported post-marketing |
| Incidence | SOLAR-1: grade 3 32.7%, grade 4 3.9%; median onset of grade ≥3 15 days; metformin used by 87.1% of affected patients (Rugo 2020 [A]) | — | FG rise 85%; G3 12%; G4 0.6%; median onset 7 days; 7% needed insulin |

- **SGLT2-inhibitor caution** (euglycaemic DKA) with these drugs: not stated in the label passages I read **[UNVERIFIED]**.
- **SOLAR-1 rash:** preventive anti-rash medication lowered any-grade rash from 64.1% to 26.7% and grade 3 from 22.7% to 11.6%. Stopping for grade ≥3 AEs fell from 18.1% to 7.9% once the detailed AE guidance was added [VERIFIED; Rugo 2020 A].

## 6.10 Lymphoedema risk reduction

- **Asdourian 2016** (systematic review, 31 studies) [VERIFIED; A]:
  - Evidence that air travel, ipsilateral blood-pressure cuffs, skin puncture or extreme temperatures cause breast cancer-related lymphoedema is mostly low-level (levels 3–5) or inconclusive; only four level-2 studies showed a significant association.
  - **Skin infection, and previous infection or inflammation of the ipsilateral arm, are the most clearly established risk factors.**
  - The authors call for a risk-adjusted approach rather than blanket precautions.
- **PAL trials** (Schmitz) [VERIFIED; A]:
  - **At risk (2010, JAMA; n = 154, ≥2 nodes removed):** 1 year of slowly progressive weight lifting did not increase lymphoedema onset (11% vs 17%; equivalence met). With ≥5 nodes removed: 7% vs 22%.
  - **Existing lymphoedema (2009, NEJM; n = 141):** twice-weekly progressive weight lifting, **with a well-fitted compression garment during exercise**, did not increase swelling (≥5% increase: 11% vs 12%). Fewer exacerbations (14% vs 29%) and better strength.
- Handbook implications (from these sources):
  - Prioritise skin care and early treatment of arm infection.
  - Supervised progressive resistance exercise is safe.
  - Avoiding BP cuffs and venepuncture on the operated side is a precaution with weak evidence. Many units keep it; flag it as institutional policy.
- CTCAE v5.0 lymphoedema grades [VERIFIED; CTCAE]:
  - G1: trace thickening or faint discoloration.
  - G2: marked discoloration, leathery skin, papillary formation; limiting instrumental ADL.
  - G3: severe symptoms; limiting self-care ADL.
- McLaughlin 2017 expert panel (Part 2): cited for completeness. PubMed has no abstract for it; content not reviewed **[UNVERIFIED]**.

## 6.11 Scalp cooling

- **SCALP RCT** (Nangia 2017, JAMA; interim analysis, n = 142 evaluable) [VERIFIED; A]:
  - Hair preservation (CTCAE grade 0–1 at the end of 4 cycles): **50.5% with cooling vs 0%** with control.
  - Regimens: 36% anthracycline-based, 64% taxane-based.
- **Prospective cohort** (Rugo 2017, JAMA; n = 122; **no anthracyclines** in the cooling group) [VERIFIED; A]:
  - Hair loss ≤50% (Dean 0–2) in 66.3%.
  - Protocol: cooling from **30 min before** each cycle, scalp held at **3 °C** during chemotherapy and for **90–120 min after**.
- **Scalp metastasis safety** (Rugo 2017, BCRT meta-analysis) [VERIFIED; A]: incidence 0.61% with cooling vs 0.41% without (P = 0.43).
- Device availability and cost in Taiwanese hospitals: not checked **[UNVERIFIED]**.

## 6.12 Fertility, pregnancy and contraception

**Counselling**
- **ASCO 2018** (Oktay) [VERIFIED; A]:
  - Discuss infertility risk as early as possible, and document the discussion.
  - Sperm, oocyte and embryo cryopreservation are standard.
  - Evidence on GnRH agonists for fertility preservation is conflicting. In young women with breast cancer, a GnRHa **may be offered** to reduce chemotherapy-induced ovarian insufficiency, but **not in place of proven methods**.
- ESMO 2020 (Lambertini): cited for completeness; PubMed has no abstract; content not reviewed **[UNVERIFIED]**.

**POEMS / S0230**
- Methods [VERIFIED; FT]: premenopausal women with **HR-negative** stage I–IIIA disease on cyclophosphamide-containing chemotherapy. **Goserelin 3.6 mg SC every 4 weeks, starting 1 week before the first chemotherapy dose**, continued to within 2 weeks before or after the last dose.
- 2015 results [VERIFIED; A]: ovarian failure at 2 years **8% vs 22%** (OR 0.30, 0.09–0.97). Pregnancy 21% vs 11%.
- Final analysis 2019 [VERIFIED; A]: 5-year pregnancy incidence 23.1% vs 12.2% (OR 2.34). DFS HR 0.55 (0.27–1.10) and OS HR 0.45 (0.19–1.04), not significant.
- **Taiwan:** goserelin is no longer licensed, and no Taiwan GnRHa licence lists this use (flag 1).

**POSITIVE** (Partridge 2023) [VERIFIED; A, FT]
- Women ≤42 years, stage I–III HR+ disease, after **18–30 months** of adjuvant endocrine therapy.
- **3-month washout** before attempting pregnancy. Interruption allowed for up to 2 years.
- 74.0% had ≥1 pregnancy; 63.8% had a live birth.
- 3-year breast cancer events: **8.9% vs 9.2%** in an external control cohort.

**Contraception after the last dose (US labels)** [VERIFIED]

| Drug | Females | Males |
|---|---|---|
| Trastuzumab / pertuzumab (with trastuzumab) | 7 months | — |
| T-DM1 | 7 months | 4 months |
| T-DXd | 7 months | 4 months |
| Dato-DXd | 7 months | 4 months |
| Sacituzumab govitecan | 6 months | 3 months |
| Doxorubicin | 6 months (highly effective) | 3 months |
| Epirubicin | 6 months | 3 months (condoms for 7 days if the partner is pregnant) |
| Cyclophosphamide | **up to 1 year** | 4 months |
| Docetaxel | 2 months | 4 months |
| Capecitabine | 6 months | 3 months |
| Pembrolizumab | 4 months | — |
| Olaparib | 6 months | 3 months (no sperm donation for 3 months) |
| Palbociclib | ≥3 weeks | 3 months |
| Ribociclib / abemaciclib | 3 weeks | — |
| Alpelisib | 1 week | 1 week (condoms) |
| Capivasertib | 1 month | 4 months |
| Inavolisib | 1 week (**non-hormonal**) | 1 week |
| Elacestrant / imlunestrant | 1 week | 1 week |
| Camizestrant | 4 weeks (**non-hormonal**) | 1 week |
| Letrozole / anastrozole | ≥3 weeks | — |
| Exemestane | 1 month | — |
| **Fulvestrant** | **1 year** | — |
| **Tamoxifen** | **Barrier or non-hormonal** contraception during treatment and for **about 2 months** after stopping. "Tamoxifen does not cause infertility, even in the presence of menstrual irregularity" | — |
| **Goserelin** | **Non-hormonal** contraception during therapy and for **12 weeks** after. Ovulation is usually suppressed, but pregnancy prevention is not ensured | — |

---

# E. Taiwan licence status

## 8. TFDA licence dataset (InfoId 36; file dated 2026-10-27; my download 2026-10-29)

All rows [VERIFIED; TFDA]. Indication wording is paraphrased from the 適應症 field. "Not found" means no row, active or cancelled, matched the English ingredient or product name (and the Chinese name where one is known).

| Drug | Taiwan brand / licence no. | Issued (發證) | Breast indication on the Taiwan licence (summary) | Gap vs US label |
|---|---|---|---|---|
| **Trastuzumab deruxtecan** | 優赫得 Enhertu 100 mg, 衛部菌疫輸字第001179號 | 2026/04/23 (expiry 2026/12/07; updated 2026/05/20) | (1) Neoadjuvant T-DXd → THP, HER2+ stage II–III. (2) HER2+ mBC: first-line with pertuzumab; monotherapy after prior anti-HER2 therapy (metastatic, or recurrence during or ≤6 months after neo/adjuvant). (3) HR+ HER2-low or **ultralow** mBC after ≥1 ET and unsuitable for further ET. (4) HER2-low after chemotherapy for metastatic disease, or recurrence ≤6 months after adjuvant chemotherapy | **No post-neoadjuvant (DESTINY-Breast05) indication** |
| **Sacituzumab govitecan** | 拓達維 Trodelvy, 衛部菌疫輸字第001206號 | 2022/11/15 | TNBC after ≥2 prior systemic therapies (≥1 for advanced disease). HR+/HER2− (IHC 0, 1+, 2+/ISH−) after ≥2 prior systemic therapies for metastatic disease (HR+ patients must have had ET unless unsuitable) | No first-line TNBC (alone or with pembrolizumab) |
| **Datopotamab deruxtecan** | 達卓優 Datroway 100 mg, 衛部菌疫輸字第001302號 | 2025/11/10 | HR+/HER2− unresectable or metastatic disease after ET **and** chemotherapy for advanced disease | No TNBC; no EGFR-mutant NSCLC |
| **Capivasertib** | 泛抑癌 Truqap 160 mg 衛部藥輸字第028821號; 200 mg 第028820號 | 2024/11/06 (updated 2026/10/22) | With fulvestrant, HR+/HER2− advanced disease with **any PIK3CA/AKT1/PTEN alteration**, relapse or progression after ET | No prostate indication |
| **Alpelisib** | 愛克利 Piqray 50 mg 第027994號, 150 mg 第027995號, 200 mg 第027996號 | 2020/12/23 | With fulvestrant, postmenopausal women and men, HR+/HER2− PIK3CA-mutated advanced disease after ET progression | — |
| **Inavolisib** | 癌妥飛 Itovebi 3 mg 第028944號, 9 mg 第028945號 | 2025/06/02 (updated 2026/08/14) | With palbociclib + fulvestrant: PIK3CA-mutated HR+/HER2− locally advanced or metastatic disease, **endocrine-resistant, recurring during or after adjuvant ET** | — |
| **Elacestrant** | **Not found** | — | — | Not licensed |
| **Camizestrant** | **Not found** | — | — | Not licensed |
| **Imlunestrant** | 盈乳樂 Inluriyo 200 mg, 衛部藥輸字第029131號 | 2026/05/15 | ESR1-mutated ER+/HER2− advanced disease after ≥1 line of ET | — |
| **Ribociclib** | 擊癌利 Kisqali 200 mg, 衛部藥輸字第027320號 (only strength) | 2017/11/22 (updated 2026/04/30) | **Adjuvant: with an AI for HR+/HER2− high-recurrence-risk stage II–III early breast cancer.** Advanced: with an AI as initial ET (men; pre-, peri- or postmenopausal women); with fulvestrant as initial or later ET (men, postmenopausal women) | — |
| **Abemaciclib** | 捷癌寧 Verzenio 50/100/150/200 mg, 第027643/027642/027641/027640號 | 2019/05/14 (updated 2024/11/04) | Adjuvant with ET (tamoxifen or AI) for HR+/HER2− **node-positive** high-risk early breast cancer. Advanced: with an AI first-line (postmenopausal women, men); with fulvestrant after ET; monotherapy after ET and chemotherapy | — |
| **Tucatinib** | 杜凱莎 Tukysa 50 mg 第029081號, 150 mg 第029082號 | 2026/03/02 | With trastuzumab + capecitabine, HER2+ advanced disease **including brain metastases**, after ≥1–2 anti-HER2 regimens in the metastatic setting | No colorectal indication |
| **Pyrotinib** | **Not found** | — | — | — |
| **Neratinib** | 賀儷安 Nerlynx 40 mg, 衛部藥輸字第027901號 | 2020/06/30 | Extended adjuvant after trastuzumab-based adjuvant therapy (HER2+ early breast cancer; no HR restriction in the wording). With capecitabine after ≥2 anti-HER2 regimens for metastatic disease | — |
| **Olaparib** | 令癌莎 Lynparza 100 mg 第027445號, 150 mg 第027446號 | 2018/06/05 (updated 2025/11/01) | Adjuvant: gBRCA1/2, HER2−, high-risk early breast cancer after neo/adjuvant chemotherapy. Metastatic: gBRCA HER2− after chemotherapy (HR+: after ET or unsuitable) | — |
| **Talazoparib** | 達勝癌 Talzenna **0.25 mg** 衛部藥輸字第027801號 (breast + prostate); 1 mg 第027802號 **cancelled 2024/06/18**; 0.1 mg 第028865號 (prostate only) | 2020/02/03 | gBRCA1/2 HER2− locally advanced or metastatic disease after neo/adjuvant or metastatic chemotherapy, or unable to receive chemotherapy | Use 4 × 0.25 mg for 1 mg |

**Related rows** [VERIFIED; TFDA]
- **Palbociclib** 愛乳適:
  - Licences: tablets 75/100/125 mg 衛部藥輸字第028005/028006/028007號; capsules 第027102/027103/027104號.
  - Indications: HR+/HER2− with an AI, or with fulvestrant after ET. **New: HR+/HER2+ maintenance with trastuzumab ± pertuzumab + ET after induction** (updated 2026/09/29).
  - Pre-/perimenopausal women need an LHRH agonist.
- **Kadcyla** 賀癌寧: 衛部菌疫輸字第000949號 (active).
- **Goserelin**: all licences cancelled (flag 1).
- **Dexrazoxane**: none (flag 2).
- **Fulvestrant**: originator Faslodex 法洛德 (衛署藥輸字第024369號) plus several generics, including locally made products (e.g. 台灣神隆, 霖揚, 台灣東洋).

Not checked: NHI (健保) reimbursement criteria for any of these drugs **[UNVERIFIED]** (www.nhi.gov.tw not reachable).

---

## 9. Label and official sources used (versions)

US prescribing information, read through openFDA (`https://api.fda.gov/drug/label.json?search=set_id:<set ID>`) on 2026-10-29 [VERIFIED]:

| Product | Holder (label) | Effective date | SPL set ID |
|---|---|---|---|
| Enhertu (fam-trastuzumab deruxtecan-nxki) | Daiichi Sankyo, Inc. | 2026-05-15 | 7e67e73e-ddf4-4e4d-8b50-09d7514910b6 |
| Trodelvy (sacituzumab govitecan-hziy) | Gilead Sciences, Inc. | 2026-06-24 | 57a597d2-03f0-472e-b148-016d7169169d |
| Kadcyla (ado-trastuzumab emtansine) | Genentech, Inc. | 2026-04-01 | 23f3c1f4-0fc8-4804-a9e3-04cf25dd302e |
| Datroway (datopotamab deruxtecan-dlnk) | Daiichi Sankyo, Inc. | 2026-05-27 | 2950227c-6230-4ca4-a135-46e44d9424a0 |
| Herceptin (trastuzumab) | Genentech, Inc. | 2026-05-29 | 492dbdb2-077e-4064-bff3-372d6af0a7a2 |
| Perjeta (pertuzumab) | Genentech, Inc. | 2026-04-30 | 17f85d17-ab71-4f5b-9fe3-0b8c822f69ff |
| Phesgo | Genentech, Inc. | 2026-05-21 | 27dd5e6b-72cd-458d-a015-cf4dab5800da |
| Keytruda (pembrolizumab) | Merck Sharp & Dohme LLC | 2026-07-10 | 9333c79b-d487-4538-a9f0-71b91a02b287 |
| Xeloda (capecitabine) | H2-Pharma, LLC | 2026-02-05 | e702d84d-7162-4751-bf37-d724cc7e45a5 |
| Doxorubicin HCl injection | Pfizer | 2026-05-05 | 1fd148fb-0fbc-4b6f-b790-23546fb46a71 |
| Ellence (epirubicin) | Pharmacia & Upjohn (Pfizer) | 2026-07-24 | 0a03c798-a652-4895-b29c-3b521a89ba42 |
| Paclitaxel injection | Teva Parenteral | 2026-09-09 | e4be6cbf-72b9-4f7f-9b1b-459b2d35961a |
| Docetaxel injection | Mylan Institutional | 2026-04-15 | 2992d633-08fa-44f3-b14d-41700f24686b |
| Cyclophosphamide injection | Nexus Pharmaceuticals | 2026-09-03 | c961a1ac-6705-4756-9abc-9d84a6fcb5c8 |
| Dexrazoxane for injection | Eugia US | 2026-08-10 | cb72203a-0b09-42d5-bf51-7f479feb3adb |
| Tamoxifen citrate tablets | (repackager label, Bryant Ranch Prepack) | 2026-03-19 | 8c0eb763-420a-4106-ba56-526b53a7f72b |
| Femara (letrozole) | Novartis | 2026-06-11 | 82b77d74-085f-45ac-a7dd-1f5c038bf406 |
| Arimidex (anastrozole) | ANI Pharmaceuticals | 2026-03-02 | acbfaaa9-503c-4691-9828-76a7146ed6de |
| Aromasin (exemestane) | Pharmacia & Upjohn | 2025-12-24 | cf066b7a-032a-416c-8d40-15ba581423e3 |
| Faslodex (fulvestrant) | AstraZeneca | 2020-09-25 | 83d7a440-e904-4e36-afb5-cb02b1c919f7 |
| Zoladex (goserelin) | TerSera Therapeutics | 2026-03-24 | 294b168b-6e5f-4db9-bf70-d599271458b3 |
| Ibrance tablets (palbociclib) | Pfizer | 2026-07-02 | fecbdd7d-b729-41b5-9872-231b8fe104ce (capsules: e0e6412f-50b4-4fd4-9364-62818d121a07) |
| Kisqali (ribociclib) | Novartis | 2026-07-01 | aaeaef94-f3f5-4367-8ea2-b181d7be2da8 |
| Verzenio (abemaciclib) | Lilly USA | 2026-07-13 | be4bc0de-0fdc-4d46-8d25-be43c79e6a06 |
| Piqray (alpelisib) | Novartis | 2025-12-15 | b20b4e18-7a4b-4500-a08f-06c6dab0ee5b |
| Truqap (capivasertib) | AstraZeneca | 2026-06-12 | d698c106-2322-401e-b738-cbd83c843ecf |
| Itovebi (inavolisib) | Genentech, Inc. | 2026-04-21 | 5de59f5b-e5db-410f-b692-658686ef4107 |
| Orserdu (elacestrant) | Stemline Therapeutics | 2026-06-24 | aa66ae5c-2bd2-4444-8178-b55651e054ef |
| Inluriyo (imlunestrant) | Lilly USA | 2026-06-04 | 5bc172e4-e8a2-441a-be52-279a7f890196 |
| Etcamah (camizestrant) | AstraZeneca | 2026-09-04 | c54223d3-f3c7-4186-afa0-429d84805826 |
| Lynparza (olaparib) | AstraZeneca | 2025-07-10 | 741ff3e3-dc1a-45a6-84e5-2481b27131aa |
| Talzenna (talazoparib) | Pfizer | 2026-04-10 | c6fd147f-a77e-4a0b-9280-e82ecc41b4be |
| Tukysa (tucatinib) | Seagen | 2024-11-04 | f27eb1b9-b7fc-424e-988f-84dd7bb195a3 |
| Nerlynx (neratinib) | Puma Biotechnology | 2026-07-02 | d1e41dcf-e82a-47c2-a0ad-6c6eef621834 |

Other official sources [VERIFIED]:
- NCCN Guidelines, Breast Cancer: **Version 9.2026** on the nccn.org category page (read 2026-10-29). This note does not quote NCCN regimen pages (login-gated).
- ClinicalTrials.gov: NCT00003088 (CALGB 9741 arms and doses); NCT00004125 (E1199; no doses in the record).
- NCI CTCAE v5.0 (`ctcae-v5.0.xlsx`, dctd.cancer.gov).
- FDA "Examples of drugs that interact with CYP enzymes and transporter systems" web table.
- TFDA dataset 36.

---

## 9b. Items not verified (do not print without checking)

1. Taiwan package-insert (仿單) dosing for any drug. The TFDA dataset 用法用量 field says only 「詳見仿單」 or 「詳如仿單」.
2. Leuprorelin/triptorelin monthly vs 3-monthly schedules for breast cancer in Taiwan.
3. The reason Zoladex was withdrawn in Taiwan, and whether supply continues under another route.
4. The CREATE-X capecitabine dose from the primary NEJM paper (confirmed only by the authors' editorial).
5. Reduced dexamethasone premedication for weekly paclitaxel.
6. Epirubicin-to-doxorubicin conversion factor for combined cumulative dose.
7. Repeat-DXA interval and adjuvant zoledronic acid schedule.
8. UGT1A1*6 and SG toxicity in East Asian patients.
9. Loperamide regimen specific to abemaciclib.
10. SGLT2-inhibitor/DKA caution in the PI3K/AKT labels.
11. ESC 2022 recommendation tables (images): 12-month post-treatment echocardiography and HER2-therapy CTRCD management.
12. Tamoxifen label uterine sarcoma placebo rate (0.4 vs probable 0.04 per 1,000 woman-years).
13. ESMO 2020 fertility guideline content; McLaughlin 2017 lymphoedema panel content.
14. NHI reimbursement criteria.
15. Errata exist for several cited papers and were not reviewed:
    - Citron 2003; Sparano 2008 (two); Jones 2006; Tolaney 2015.
    - EBCTCG 2015 (two); Hortobagyi 2016; Robson 2017; Bidard 2022.
    - Lyon 2022; Rugo 2022; Rugo 2025.

---

## 10. References (APA 7)

### Journal articles and guidelines

- André, F., Ciruelos, E., Rubovszky, G., Campone, M., Loibl, S., Rugo, H. S., Iwata, H., Conte, P., Mayer, I. A., Kaufman, B., Yamashita, T., Lu, Y.-S., Inoue, K., Takahashi, M., Pápai, Z., Longin, A.-S., Mills, D., Wilke, C., Hirawat, S., & Juric, D. (2019). Alpelisib for *PIK3CA*-mutated, hormone receptor-positive advanced breast cancer. *The New England Journal of Medicine*, *380*(20), 1929–1940. https://doi.org/10.1056/NEJMoa1813904 — PMID 31091374
- Armenian, S. H., Lacchetti, C., Barac, A., Carver, J., Constine, L. S., Denduluri, N., Dent, S., Douglas, P. S., Durand, J.-B., Ewer, M., Fabian, C., Hudson, M., Jessup, M., Jones, L. W., Ky, B., Mayer, E. L., Moslehi, J., Oeffinger, K., Ray, K., . . . Lenihan, D. (2017). Prevention and monitoring of cardiac dysfunction in survivors of adult cancers: American Society of Clinical Oncology clinical practice guideline. *Journal of Clinical Oncology*, *35*(8), 893–911. https://doi.org/10.1200/JCO.2016.70.5400 — PMID 27918725
- Asdourian, M. S., Skolny, M. N., Brunelle, C., Seward, C. E., Salama, L., & Taghian, A. G. (2016). Precautions for breast cancer-related lymphoedema: Risk from air travel, ipsilateral arm blood pressure measurements, skin puncture, extreme temperatures, and cellulitis. *The Lancet Oncology*, *17*(9), e392–e405. https://doi.org/10.1016/S1470-2045(16)30204-2 — PMID 27599144
- Bardia, A., Hurvitz, S. A., Tolaney, S. M., Loirat, D., Punie, K., Oliveira, M., Brufsky, A., Sardesai, S. D., Kalinsky, K., Zelnak, A. B., Weaver, R., Traina, T., Dalenc, F., Aftimos, P., Lynce, F., Diab, S., Cortés, J., O'Shaughnessy, J., Diéras, V., . . . Rugo, H. S. (2021). Sacituzumab govitecan in metastatic triple-negative breast cancer. *The New England Journal of Medicine*, *384*(16), 1529–1541. https://doi.org/10.1056/NEJMoa2028485 — PMID 33882206
- Baselga, J., Cortés, J., Kim, S.-B., Im, S.-A., Hegg, R., Im, Y.-H., Roman, L., Pedrini, J. L., Pienkowski, T., Knott, A., Clark, E., Benyunes, M. C., Ross, G., & Swain, S. M. (2012). Pertuzumab plus trastuzumab plus docetaxel for metastatic breast cancer. *The New England Journal of Medicine*, *366*(2), 109–119. https://doi.org/10.1056/NEJMoa1113216 — PMID 22149875 (PMC5705202)
- Bidard, F.-C., Kaklamani, V. G., Neven, P., Streich, G., Montero, A. J., Forget, F., Mouret-Reynier, M.-A., Sohn, J. H., Taylor, D., Harnden, K. K., Khong, H., Kocsis, J., Dalenc, F., Dillon, P. M., Babu, S., Waters, S., Deleu, I., García Sáenz, J. A., Bria, E., . . . Bardia, A. (2022). Elacestrant (oral selective estrogen receptor degrader) versus standard endocrine therapy for estrogen receptor-positive, human epidermal growth factor receptor 2-negative advanced breast cancer: Results from the randomized phase III EMERALD trial. *Journal of Clinical Oncology*, *40*(28), 3246–3256. https://doi.org/10.1200/JCO.22.00338 — PMID 35584336 (PMC9553388)
- Citron, M. L., Berry, D. A., Cirrincione, C., Hudis, C., Winer, E. P., Gradishar, W. J., Davidson, N. E., Martino, S., Livingston, R., Ingle, J. N., Perez, E. A., Carpenter, J., Hurd, D., Holland, J. F., Smith, B. L., Sartor, C. I., Leung, E. H., Abrams, J., Schilsky, R. L., . . . Norton, L. (2003). Randomized trial of dose-dense versus conventionally scheduled and sequential versus concurrent combination chemotherapy as postoperative adjuvant treatment of node-positive primary breast cancer: First report of Intergroup Trial C9741/Cancer and Leukemia Group B Trial 9741. *Journal of Clinical Oncology*, *21*(8), 1431–1439. https://doi.org/10.1200/JCO.2003.09.081 — PMID 12668651
- Cortés, J., Kim, S.-B., Chung, W.-P., Im, S.-A., Park, Y. H., Hegg, R., Kim, M. H., Tseng, L.-M., Petry, V., Chung, C.-F., Iwata, H., Hamilton, E., Curigliano, G., Xu, B., Huang, C.-S., Kim, J. H., Chiu, J. W. Y., Pedrini, J. L., Lee, C., . . . Hurvitz, S. A. (2022). Trastuzumab deruxtecan versus trastuzumab emtansine for breast cancer. *The New England Journal of Medicine*, *386*(12), 1143–1154. https://doi.org/10.1056/NEJMoa2115022 — PMID 35320644
- Di Leo, A., Jerusalem, G., Petruzelka, L., Torres, R., Bondarenko, I. N., Khasanov, R., Verhoeven, D., Pedrini, J. L., Smirnova, I., Lichinitser, M. R., Pendergrass, K., Garnett, S., Lindemann, J. P. O., Sapunar, F., & Martin, M. (2010). Results of the CONFIRM phase III trial comparing fulvestrant 250 mg with fulvestrant 500 mg in postmenopausal women with estrogen receptor-positive advanced breast cancer. *Journal of Clinical Oncology*, *28*(30), 4594–4600. https://doi.org/10.1200/JCO.2010.28.8415 — PMID 20855825
- Early Breast Cancer Trialists' Collaborative Group. (2015). Adjuvant bisphosphonate treatment in early breast cancer: Meta-analyses of individual patient data from randomised trials. *The Lancet*, *386*(10001), 1353–1361. https://doi.org/10.1016/S0140-6736(15)60908-4 — PMID 26211824
- Finn, R. S., Martin, M., Rugo, H. S., Jones, S., Im, S.-A., Gelmon, K., Harbeck, N., Lipatov, O. N., Walshe, J. M., Moulder, S., Gauthier, E., Lu, D. R., Randolph, S., Diéras, V., & Slamon, D. J. (2016). Palbociclib and letrozole in advanced breast cancer. *The New England Journal of Medicine*, *375*(20), 1925–1936. https://doi.org/10.1056/NEJMoa1607303 — PMID 27959613
- Fisher, B., Costantino, J. P., Wickerham, D. L., Redmond, C. K., Kavanah, M., Cronin, W. M., Vogel, V., Robidoux, A., Dimitrov, N., Atkins, J., Daly, M., Wieand, S., Tan-Chiu, E., Ford, L., & Wolmark, N. (1998). Tamoxifen for prevention of breast cancer: Report of the National Surgical Adjuvant Breast and Bowel Project P-1 Study. *Journal of the National Cancer Institute*, *90*(18), 1371–1388. https://doi.org/10.1093/jnci/90.18.1371 — PMID 9747868
- Gnant, M., Pfeiler, G., Dubsky, P. C., Hubalek, M., Greil, R., Jakesz, R., Wette, V., Balic, M., Haslbauer, F., Melbinger, E., Bjelic-Radisic, V., Artner-Matuschek, S., Fitzal, F., Marth, C., Sevelda, P., Mlineritsch, B., Steger, G. G., Manfreda, D., Exner, R., . . . Singer, C. F. (2015). Adjuvant denosumab in breast cancer (ABCSG-18): A multicentre, randomised, double-blind, placebo-controlled trial. *The Lancet*, *386*(9992), 433–443. https://doi.org/10.1016/S0140-6736(15)60995-3 — PMID 26040499
- Goetz, M. P., Sangkuhl, K., Guchelaar, H.-J., Schwab, M., Province, M., Whirl-Carrillo, M., Symmans, W. F., McLeod, H. L., Ratain, M. J., Zembutsu, H., Gaedigk, A., van Schaik, R. H., Ingle, J. N., Caudle, K. E., & Klein, T. E. (2018). Clinical Pharmacogenetics Implementation Consortium (CPIC) guideline for *CYP2D6* and tamoxifen therapy. *Clinical Pharmacology & Therapeutics*, *103*(5), 770–777. https://doi.org/10.1002/cpt.1007 — PMID 29385237 (PMC5931215)
- Henry, N. L., Unger, J. M., Schott, A. F., Fehrenbacher, L., Flynn, P. J., Prow, D. M., Sharer, C. W., Burton, G. V., Kuzma, C. S., Moseley, A., Lew, D. L., Fisch, M. J., Moinpour, C. M., Hershman, D. L., & Wade, J. L. (2018). Randomized, multicenter, placebo-controlled clinical trial of duloxetine versus placebo for aromatase inhibitor-associated arthralgias in early-stage breast cancer: SWOG S1202. *Journal of Clinical Oncology*, *36*(4), 326–332. https://doi.org/10.1200/JCO.2017.74.6651 — PMID 29136387 (PMC5805479)
- Hershman, D. L., Unger, J. M., Greenlee, H., Capodice, J. L., Lew, D. L., Darke, A. K., Kengla, A. T., Melnik, M. K., Jorgensen, C. W., Kreisle, W. H., Minasian, L. M., Fisch, M. J., Henry, N. L., & Crew, K. D. (2018). Effect of acupuncture vs sham acupuncture or waitlist control on joint pain related to aromatase inhibitors among women with early-stage breast cancer: A randomized clinical trial. *JAMA*, *320*(2), 167–176. https://doi.org/10.1001/jama.2018.8907 — PMID 29998338 (PMC6583520)
- Hortobagyi, G. N., Stemmer, S. M., Burris, H. A., Yap, Y.-S., Sonke, G. S., Paluch-Shimon, S., Campone, M., Blackwell, K. L., André, F., Winer, E. P., Janni, W., Verma, S., Conte, P., Arteaga, C. L., Cameron, D. A., Petrakova, K., Hart, L. L., Villanueva, C., Chan, A., . . . O'Shaughnessy, J. (2016). Ribociclib as first-line therapy for HR-positive, advanced breast cancer. *The New England Journal of Medicine*, *375*(18), 1738–1748. https://doi.org/10.1056/NEJMoa1609709 — PMID 27717303
- Johnston, S. R. D., Harbeck, N., Hegg, R., Toi, M., Martin, M., Shao, Z. M., Zhang, Q. Y., Martinez Rodriguez, J. L., Campone, M., Hamilton, E., Sohn, J., Guarneri, V., Okada, M., Boyle, F., Neven, P., Cortés, J., Huober, J., Wardley, A., Tolaney, S. M., . . . Rastogi, P. (2020). Abemaciclib combined with endocrine therapy for the adjuvant treatment of HR+, HER2−, node-positive, high-risk, early breast cancer (monarchE). *Journal of Clinical Oncology*, *38*(34), 3987–3998. https://doi.org/10.1200/JCO.20.02514 — PMID 32954927 (PMC7768339)
- Jones, S. E., Savin, M. A., Holmes, F. A., O'Shaughnessy, J. A., Blum, J. L., Vukelja, S., McIntyre, K. J., Pippen, J. E., Bordelon, J. H., Kirby, R., Sandbach, J., Hyman, W. J., Khandelwal, P., Negron, A. G., Richards, D. A., Anthony, S. P., Mennel, R. G., Boehm, K. A., Meyer, W. G., & Asmar, L. (2006). Phase III trial comparing doxorubicin plus cyclophosphamide with docetaxel plus cyclophosphamide as adjuvant therapy for operable breast cancer. *Journal of Clinical Oncology*, *24*(34), 5381–5387. https://doi.org/10.1200/JCO.2006.06.5391 — PMID 17135639
- Kelly, C. M., Juurlink, D. N., Gomes, T., Duong-Hua, M., Pritchard, K. I., Austin, P. C., & Paszat, L. F. (2010). Selective serotonin reuptake inhibitors and breast cancer mortality in women receiving tamoxifen: A population based cohort study. *BMJ*, *340*, Article c693. https://doi.org/10.1136/bmj.c693 — PMID 20142325 (PMC2817754)
- Lambertini, M., Peccatori, F. A., Demeestere, I., Amant, F., Wyns, C., Stukenborg, J.-B., Paluch-Shimon, S., Halaska, M. J., Uzan, C., Meissner, J., von Wolff, M., Anderson, R. A., & Jordan, K. (2020). Fertility preservation and post-treatment pregnancies in post-pubertal cancer patients: ESMO clinical practice guidelines. *Annals of Oncology*, *31*(12), 1664–1678. https://doi.org/10.1016/j.annonc.2020.09.006 — PMID 32976936
- Lyon, A. R., López-Fernández, T., Couch, L. S., Asteggiano, R., Aznar, M. C., Bergler-Klein, J., Boriani, G., Cardinale, D., Cordoba, R., Cosyns, B., Cutter, D. J., de Azambuja, E., de Boer, R. A., Dent, S. F., Farmakis, D., Gevaert, S. A., Gorog, D. A., Herrmann, J., Lenihan, D., . . . van der Pal, H. J. H. (2022). 2022 ESC guidelines on cardio-oncology developed in collaboration with the European Hematology Association (EHA), the European Society for Therapeutic Radiology and Oncology (ESTRO) and the International Cardio-Oncology Society (IC-OS). *European Heart Journal*, *43*(41), 4229–4361. https://doi.org/10.1093/eurheartj/ehac244 — PMID 36017568
- Masuda, N., Lee, S.-J., Ohtani, S., Im, Y.-H., Lee, E.-S., Yokota, I., Kuroi, K., Im, S.-A., Park, B.-W., Kim, S.-B., Yanagita, Y., Ohno, S., Takao, S., Aogi, K., Iwata, H., Jeong, J., Kim, A., Park, K.-H., Sasano, H., . . . Toi, M. (2017). Adjuvant capecitabine for breast cancer after preoperative chemotherapy. *The New England Journal of Medicine*, *376*(22), 2147–2159. https://doi.org/10.1056/NEJMoa1612645 — PMID 28564564
- McLaughlin, S. A., DeSnyder, S. M., Klimberg, S., Alatriste, M., Boccardo, F., Smith, M. L., Staley, A. C., Thiruchelvam, P. T. R., Hutchison, N. A., Mendez, J., MacNeill, F., Vicini, F., Rockson, S. G., & Feldman, S. M. (2017). Considerations for clinicians in the diagnosis, prevention, and treatment of breast cancer-related lymphedema, recommendations from an expert panel: Part 2: Preventive and therapeutic options. *Annals of Surgical Oncology*, *24*(10), 2827–2835. https://doi.org/10.1245/s10434-017-5964-6 — PMID 28766218
- Modi, S., Jacot, W., Yamashita, T., Sohn, J., Vidal, M., Tokunaga, E., Tsurutani, J., Ueno, N. T., Prat, A., Chae, Y. S., Lee, K. S., Niikura, N., Park, Y. H., Xu, B., Wang, X., Gil-Gil, M., Li, W., Pierga, J.-Y., Im, S.-A., . . . Cameron, D. A. (2022). Trastuzumab deruxtecan in previously treated HER2-low advanced breast cancer. *The New England Journal of Medicine*, *387*(1), 9–20. https://doi.org/10.1056/NEJMoa2203690 — PMID 35665782 (PMC10561652)
- Moore, H. C. F., Unger, J. M., Phillips, K.-A., Boyle, F., Hitre, E., Porter, D., Francis, P. A., Goldstein, L. J., Gomez, H. L., Vallejos, C. S., Partridge, A. H., Dakhil, S. R., Garcia, A. A., Gralow, J., Lombard, J. M., Forbes, J. F., Martino, S., Barlow, W. E., Fabian, C. J., . . . Albain, K. S. (2015). Goserelin for ovarian protection during breast-cancer adjuvant chemotherapy. *The New England Journal of Medicine*, *372*(10), 923–932. https://doi.org/10.1056/NEJMoa1413204 — PMID 25738668 (PMC4405231)
- Moore, H. C. F., Unger, J. M., Phillips, K.-A., Boyle, F., Hitre, E., Moseley, A., Porter, D. J., Francis, P. A., Goldstein, L. J., Gomez, H. L., Vallejos, C. S., Partridge, A. H., Dakhil, S. R., Garcia, A. A., Gralow, J. R., Lombard, J. M., Forbes, J. F., Martino, S., Barlow, W. E., . . . Albain, K. S. (2019). Final analysis of the Prevention of Early Menopause Study (POEMS)/SWOG Intergroup S0230. *Journal of the National Cancer Institute*, *111*(2), 210–213. https://doi.org/10.1093/jnci/djy185 — PMID 30371800 (PMC6657277)
- Nangia, J., Wang, T., Osborne, C., Niravath, P., Otte, K., Papish, S., Holmes, F., Abraham, J., Lacouture, M., Courtright, J., Paxman, R., Rude, M., Hilsenbeck, S., Osborne, C. K., & Rimawi, M. (2017). Effect of a scalp cooling device on alopecia in women undergoing chemotherapy for breast cancer: The SCALP randomized clinical trial. *JAMA*, *317*(6), 596–605. https://doi.org/10.1001/jama.2016.20939 — PMID 28196254
- Oktay, K., Harvey, B. E., Partridge, A. H., Quinn, G. P., Reinecke, J., Taylor, H. S., Wallace, W. H., Wang, E. T., & Loren, A. W. (2018). Fertility preservation in patients with cancer: ASCO clinical practice guideline update. *Journal of Clinical Oncology*, *36*(19), 1994–2001. https://doi.org/10.1200/JCO.2018.78.1914 — PMID 29620997
- Partridge, A. H., Niman, S. M., Ruggeri, M., Peccatori, F. A., Azim, H. A., Colleoni, M., Saura, C., Shimizu, C., Sætersdal, A. B., Kroep, J. R., Mailliez, A., Warner, E., Borges, V. F., Amant, F., Gombos, A., Kataoka, A., Rousset-Jablonski, C., Borstnar, S., Takei, J., . . . Pagani, O. (2023). Interrupting endocrine therapy to attempt pregnancy after breast cancer. *The New England Journal of Medicine*, *388*(18), 1645–1656. https://doi.org/10.1056/NEJMoa2212856 — PMID 37133584 (PMC10358451)
- Robson, M., Im, S.-A., Senkus, E., Xu, B., Domchek, S. M., Masuda, N., Delaloge, S., Li, W., Tung, N., Armstrong, A., Wu, W., Goessl, C., Runswick, S., & Conte, P. (2017). Olaparib for metastatic breast cancer in patients with a germline *BRCA* mutation. *The New England Journal of Medicine*, *377*(6), 523–533. https://doi.org/10.1056/NEJMoa1706450 — PMID 28578601
- Rugo, H. S., André, F., Yamashita, T., Cerda, H., Toledano, I., Stemmer, S. M., Jurado, J. C., Juric, D., Mayer, I., Ciruelos, E. M., Iwata, H., Conte, P., Campone, M., Wilke, C., Mills, D., Lteif, A., Miller, M., Gaudenzi, F., & Loibl, S. (2020). Time course and management of key adverse events during the randomized phase III SOLAR-1 study of PI3K inhibitor alpelisib plus fulvestrant in patients with HR-positive advanced breast cancer. *Annals of Oncology*, *31*(8), 1001–1010. https://doi.org/10.1016/j.annonc.2020.05.001 — PMID 32416251
- Rugo, H. S., Bardia, A., Marmé, F., Cortés, J., Schmid, P., Loirat, D., Trédan, O., Ciruelos, E., Dalenc, F., Gómez Pardo, P., Jhaveri, K. L., Delaney, R., Valdez, T., Wang, H., Motwani, M., Yoon, O. K., Verret, W., & Tolaney, S. M. (2023). Overall survival with sacituzumab govitecan in hormone receptor-positive and human epidermal growth factor receptor 2-negative metastatic breast cancer (TROPiCS-02): A randomised, open-label, multicentre, phase 3 trial. *The Lancet*, *402*(10411), 1423–1433. https://doi.org/10.1016/S0140-6736(23)01245-X — PMID 37633306
- Rugo, H. S., Klein, P., Melin, S. A., Hurvitz, S. A., Melisko, M. E., Moore, A., Park, G., Mitchel, J., Bågeman, E., D'Agostino, R. B., Ver Hoeve, E. S., Esserman, L., & Cigler, T. (2017). Association between use of a scalp cooling device and alopecia after chemotherapy for breast cancer. *JAMA*, *317*(6), 606–614. https://doi.org/10.1001/jama.2016.21038 — PMID 28196257 (PMC5639721)
- Rugo, H. S., Melin, S. A., & Voigt, J. (2017). Scalp cooling with adjuvant/neoadjuvant chemotherapy for breast cancer and the risk of scalp metastases: Systematic review and meta-analysis. *Breast Cancer Research and Treatment*, *163*(2), 199–205. https://doi.org/10.1007/s10549-017-4185-9 — PMID 28275922 (PMC5410200)
- Rugo, H. S., Tokunaga, E., Iwata, H., Petry, V., Smit, E. F., Goto, Y., Kim, D.-W., Shitara, K., Gruden, J. F., Modi, S., Cortés, J., Krop, I., Jänne, P. A., Cheng, Y., Taitt, C., Cheng, F.-C., & Powell, C. A. (2025). Pooled analysis of trastuzumab deruxtecan retreatment after recovery from grade 1 interstitial lung disease/pneumonitis. *Annals of Oncology*, *36*(11), 1389–1399. https://doi.org/10.1016/j.annonc.2025.07.015 — PMID 40769277. Erratum: *Annals of Oncology*, *37*(9), 1308 (2026), not reviewed.
- Rugo, H. S., Tolaney, S. M., Loirat, D., Punie, K., Bardia, A., Hurvitz, S. A., O'Shaughnessy, J., Cortés, J., Diéras, V., Carey, L. A., Gianni, L., Piccart, M. J., Loibl, S., Goldenberg, D. M., Hong, Q., Olivo, M., Itri, L. M., & Kalinsky, K. (2022). Safety analyses from the phase 3 ASCENT trial of sacituzumab govitecan in metastatic triple-negative breast cancer. *npj Breast Cancer*, *8*, Article 98. https://doi.org/10.1038/s41523-022-00467-1 — PMID 36038616 (PMC9424318)
- Schmid, P., Cortes, J., Pusztai, L., McArthur, H., Kümmel, S., Bergh, J., Denkert, C., Park, Y. H., Hui, R., Harbeck, N., Takahashi, M., Foukakis, T., Fasching, P. A., Cardoso, F., Untch, M., Jia, L., Karantza, V., Zhao, J., Aktan, G., . . . O'Shaughnessy, J. (2020). Pembrolizumab for early triple-negative breast cancer. *The New England Journal of Medicine*, *382*(9), 810–821. https://doi.org/10.1056/NEJMoa1910549 — PMID 32101663
- Schmitz, K. H., Ahmed, R. L., Troxel, A., Cheville, A., Smith, R., Lewis-Grant, L., Bryan, C. J., Williams-Smith, C. T., & Greene, Q. P. (2009). Weight lifting in women with breast-cancer-related lymphedema. *The New England Journal of Medicine*, *361*(7), 664–673. https://doi.org/10.1056/NEJMoa0810118 — PMID 19675330
- Schmitz, K. H., Ahmed, R. L., Troxel, A. B., Cheville, A., Lewis-Grant, L., Smith, R., Bryan, C. J., Williams-Smith, C. T., & Chittams, J. (2010). Weight lifting for women at risk for breast cancer-related lymphedema: A randomized trial. *JAMA*, *304*(24), 2699–2705. https://doi.org/10.1001/jama.2010.1837 — PMID 21148134
- Schneeweiss, A., Chia, S., Hickish, T., Harvey, V., Eniu, A., Hegg, R., Tausch, C., Seo, J. H., Tsai, Y.-F., Ratnayake, J., McNally, V., Ross, G., & Cortés, J. (2013). Pertuzumab plus trastuzumab in combination with standard neoadjuvant anthracycline-containing and anthracycline-free chemotherapy regimens in patients with HER2-positive early breast cancer: A randomized phase II cardiac safety study (TRYPHAENA). *Annals of Oncology*, *24*(9), 2278–2284. https://doi.org/10.1093/annonc/mdt182 — PMID 23704196
- Shapiro, C. L., Van Poznak, C., Lacchetti, C., Kirshner, J., Eastell, R., Gagel, R., Smith, S., Edwards, B. J., Frank, E., Lyman, G. H., Smith, M. R., Mhaskar, R., Henderson, T., & Neuner, J. (2019). Management of osteoporosis in survivors of adult cancers with nonmetastatic disease: ASCO clinical practice guideline. *Journal of Clinical Oncology*, *37*(31), 2916–2946. https://doi.org/10.1200/JCO.19.01696 — PMID 31532726
- Slamon, D., Eiermann, W., Robert, N., Pienkowski, T., Martin, M., Press, M., Mackey, J., Glaspy, J., Chan, A., Pawlicki, M., Pinter, T., Valero, V., Liu, M.-C., Sauter, G., von Minckwitz, G., Visco, F., Bee, V., Buyse, M., Bendahmane, B., . . . Crown, J. (2011). Adjuvant trastuzumab in HER2-positive breast cancer. *The New England Journal of Medicine*, *365*(14), 1273–1283. https://doi.org/10.1056/NEJMoa0910383 — PMID 21991949 (PMC3268553)
- Slamon, D., Lipatov, O., Nowecki, Z., McAndrew, N., Kukielka-Budny, B., Stroyakovskiy, D., Yardley, D. A., Huang, C.-S., Fasching, P. A., Crown, J., Bardia, A., Chia, S., Im, S.-A., Ruiz-Borrego, M., Loi, S., Xu, B., Hurvitz, S., Barrios, C., Untch, M., . . . Hortobagyi, G. (2024). Ribociclib plus endocrine therapy in early breast cancer. *The New England Journal of Medicine*, *390*(12), 1080–1091. https://doi.org/10.1056/NEJMoa2305488 — PMID 38507751
- Sparano, J. A., Wang, M., Martino, S., Jones, V., Perez, E. A., Saphner, T., Wolff, A. C., Sledge, G. W., Wood, W. C., & Davidson, N. E. (2008). Weekly paclitaxel in the adjuvant treatment of breast cancer. *The New England Journal of Medicine*, *358*(16), 1663–1671. https://doi.org/10.1056/NEJMoa0707056 — PMID 18420499 (PMC2743943)
- Sparano, J. A., Zhao, F., Martino, S., Ligibel, J. A., Perez, E. A., Saphner, T., Wolff, A. C., Sledge, G. W., Wood, W. C., & Davidson, N. E. (2015). Long-term follow-up of the E1199 phase III trial evaluating the role of taxane and schedule in operable breast cancer. *Journal of Clinical Oncology*, *33*(21), 2353–2360. https://doi.org/10.1200/JCO.2015.60.9271 — PMID 26077235 (PMC4500829)
- Swain, S. M., Baselga, J., Kim, S.-B., Ro, J., Semiglazov, V., Campone, M., Ciruelos, E., Ferrero, J.-M., Schneeweiss, A., Heeson, S., Clark, E., Ross, G., Benyunes, M. C., & Cortés, J. (2015). Pertuzumab, trastuzumab, and docetaxel in HER2-positive metastatic breast cancer. *The New England Journal of Medicine*, *372*(8), 724–734. https://doi.org/10.1056/NEJMoa1413513 — PMID 25693012 (PMC5584549)
- Swain, S. M., Whaley, F. S., & Ewer, M. S. (2003). Congestive heart failure in patients treated with doxorubicin: A retrospective analysis of three trials. *Cancer*, *97*(11), 2869–2879. https://doi.org/10.1002/cncr.11407 — PMID 12767102
- Toi, M., Masuda, N., & Lee, S.-J. (2017). Capecitabine for primary breast cancer. *Oncotarget*, *8*(67), 110739–110740. https://doi.org/10.18632/oncotarget.22990 — PMID 29340011 (PMC5762279)
- Tolaney, S. M., Barry, W. T., Dang, C. T., Yardley, D. A., Moy, B., Marcom, P. K., Albain, K. S., Rugo, H. S., Ellis, M., Shapira, I., Wolff, A. C., Carey, L. A., Overmoyer, B. A., Partridge, A. H., Guo, H., Hudis, C. A., Krop, I. E., Burstein, H. J., & Winer, E. P. (2015). Adjuvant paclitaxel and trastuzumab for node-negative, HER2-positive breast cancer. *The New England Journal of Medicine*, *372*(2), 134–141. https://doi.org/10.1056/NEJMoa1406281 — PMID 25564897 (PMC4313867)
- Tolaney, S. M., Sonpavde, G. P., Tarantino, P., Lustberg, M. B., & Rugo, H. S. (2025). Clinical perspective on management of key adverse events with sacituzumab govitecan. *The Oncologist*, *30*(11), Article oyaf311. https://doi.org/10.1093/oncolo/oyaf311 — PMID 41006069 (PMC12619999). Consulted for context only (pooled SG adverse-event incidence: neutropenia 61%, diarrhoea 64%) [A].
- Turner, N. C., Oliveira, M., Howell, S. J., Dalenc, F., Cortes, J., Gomez Moreno, H. L., Hu, X., Jhaveri, K., Krivorotko, P., Loibl, S., Morales Murillo, S., Okera, M., Park, Y. H., Sohn, J., Toi, M., Tokunaga, E., Yousef, S., Zhukova, L., de Bruin, E. C., . . . Rugo, H. S. (2023). Capivasertib in hormone receptor-positive advanced breast cancer. *The New England Journal of Medicine*, *388*(22), 2058–2070. https://doi.org/10.1056/NEJMoa2214131 — PMID 37256976 (PMC11335038)
- Tutt, A. N. J., Garber, J. E., Kaufman, B., Viale, G., Fumagalli, D., Rastogi, P., Gelber, R. D., de Azambuja, E., Fielding, A., Balmaña, J., Domchek, S. M., Gelmon, K. A., Hollingsworth, S. J., Korde, L. A., Linderholm, B., Bandos, H., Senkus, E., Suga, J. M., Shao, Z., . . . Geyer, C. E. (2021). Adjuvant olaparib for patients with *BRCA1*- or *BRCA2*-mutated breast cancer. *The New England Journal of Medicine*, *384*(25), 2394–2405. https://doi.org/10.1056/NEJMoa2105215 — PMID 34081848 (PMC9126186)
- von Minckwitz, G., Huang, C.-S., Mano, M. S., Loibl, S., Mamounas, E. P., Untch, M., Wolmark, N., Rastogi, P., Schneeweiss, A., Redondo, A., Fischer, H. H., Jacot, W., Conlin, A. K., Arce-Salinas, C., Wapnir, I. L., Jackisch, C., DiGiovanna, M. P., Fasching, P. A., Crown, J. P., . . . Geyer, C. E. (2019). Trastuzumab emtansine for residual invasive HER2-positive breast cancer. *The New England Journal of Medicine*, *380*(7), 617–628. https://doi.org/10.1056/NEJMoa1814017 — PMID 30516102

### Official sources and datasets

- European Society of Cardiology guideline: see Lyon et al. (2022) above.
- National Cancer Institute. (2017). *Common terminology criteria for adverse events (CTCAE)* (Version 5.0) [Data set]. U.S. Department of Health and Human Services. https://dctd.cancer.gov/research/ctep-trials/trial-development/ctcae-v5.0.xlsx
- National Comprehensive Cancer Network. (2026). *NCCN clinical practice guidelines in oncology: Breast cancer* (Version 9.2026). https://www.nccn.org/guidelines/category_1 (version read from the category page on 2026-10-29)
- Taiwan Food and Drug Administration. (2026). *全部藥品許可證資料集* [All drug licences data set; InfoId 36; file dated 2026-10-27; downloaded 2026-10-29] [Data set]. https://data.fda.gov.tw/opendata/exportDataList.do?method=ExportData&InfoId=36&logType=2
- U.S. Food and Drug Administration. (n.d.). *For healthcare professionals: FDA's examples of drugs that interact with CYP enzymes and transporter systems*. Retrieved October 29, 2026, from https://www.fda.gov/drugs/drug-interactions-labeling/healthcare-professionals-fdas-examples-drugs-interact-cyp-enzymes-and-transporter-systems
- U.S. National Library of Medicine. (2026). *Combination chemotherapy in treating patients with breast cancer* (ClinicalTrials.gov Identifier NCT00003088) [CALGB 9741 registry record]. https://clinicaltrials.gov/study/NCT00003088
- U.S. prescribing information: one entry per product in the format "[Holder]. ([year of effective date]). *[Brand] ([generic]) prescribing information* [SPL set ID …]. openFDA. https://api.fda.gov/drug/label.json?search=set_id:[set ID]". All holders, dates and set IDs are in the section 9 table.
- Australian context for the Zoladex withdrawal (secondary, [WEB]): Breast Cancer Network Australia, "Update on access to Zoladex treatment" (last updated 14 May 2026), https://www.bcna.org.au/latest-news/bcna-news/update-on-access-to-zoladex-treatment/; healthed.com.au, "AZ pulling Zoladex 3.6mg from Australian market", https://www.healthed.com.au/clinical_articles/az-pulling-zoladex-3-6mg-from-australian-market/

## Appendix: PMID index

12668651 Citron 2003 (CALGB 9741) · 12767102 Swain 2003 · 17135639 Jones 2006 (TC) · 18420499 Sparano 2008 (E1199) · 26077235 Sparano 2015 · 21991949 Slamon 2011 (BCIRG 006) · 23704196 Schneeweiss 2013 (TRYPHAENA) · 22149875 Baselga 2012 and 25693012 Swain 2015 (CLEOPATRA) · 25564897 Tolaney 2015 (APT) · 32101663 Schmid 2020 (KEYNOTE-522) · 28564564 Masuda 2017 (CREATE-X) · 29340011 Toi 2017 (editorial) · 30516102 von Minckwitz 2019 (KATHERINE) · 35320644 Cortés 2022 (DB-03) · 35665782 Modi 2022 (DB-04) · 40769277 Rugo 2025 (T-DXd ILD retreatment) · 33882206 Bardia 2021 (ASCENT) · 36038616 Rugo 2022 (ASCENT safety/UGT1A1) · 37633306 Rugo 2023 (TROPiCS-02) · 41006069 Tolaney 2025 · 27959613 Finn 2016 (PALOMA-2) · 27717303 Hortobagyi 2016 (MONALEESA-2) · 38507751 Slamon 2024 (NATALEE) · 32954927 Johnston 2020 (monarchE) · 31091374 André 2019 (SOLAR-1) · 32416251 Rugo 2020 (SOLAR-1 AE) · 37256976 Turner 2023 (CAPItello-291) · 35584336 Bidard 2022 (EMERALD) · 28578601 Robson 2017 (OlympiAD) · 34081848 Tutt 2021 (OlympiA) · 20855825 Di Leo 2010 (CONFIRM) · 9747868 Fisher 1998 (P-1) · 20142325 Kelly 2010 · 29385237 Goetz 2018 (CPIC) · 31532726 Shapiro 2019 · 26040499 Gnant 2015 (ABCSG-18) · 26211824 EBCTCG 2015 · 29998338 Hershman 2018 · 29136387 Henry 2018 · 27599144 Asdourian 2016 · 28766218 McLaughlin 2017 · 19675330 Schmitz 2009 · 21148134 Schmitz 2010 · 28196254 Nangia 2017 · 28196257 Rugo 2017 (JAMA) · 28275922 Rugo 2017 (BCRT) · 25738668 Moore 2015 (POEMS) · 30371800 Moore 2019 · 37133584 Partridge 2023 (POSITIVE) · 29620997 Oktay 2018 · 32976936 Lambertini 2020 · 27918725 Armenian 2017 · 36017568 Lyon 2022
