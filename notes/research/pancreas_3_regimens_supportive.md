# Pancreas 3. Regimens, exact dosing, toxicity management and supportive care: verified nursing notes

Handbook: Taiwanese oncology NP handbook (專科護理師), pancreatic cancer chapter — ward practice + 專師甄審 exam
Verification date: 2026-10-29
Companion files: this file assumes the **trial-level efficacy data** (PFS/OS/HR) are in `pancreas_2_trials.md`; here the focus is **exact doses/schedules, toxicity management, UGT1A1/DPYD pharmacogenetics, supportive care and Taiwan licence status**. Where a regimen's efficacy is needed, I cite the pancreas_2 section rather than repeat it.

Method: Doses and schedules come from the **current US FDA label** (openFDA `drug/label`, effective date given) or the **trial paper** (PubMed abstract / PMC full text), never from memory. Taiwan doses/indications come from the **TFDA drug-insert platform** (mcp.fda.gov.tw, the official 仿單查詢平台) and the **TFDA licence open-data file** (InfoId=36, the CSV inside is dated **2026-10-27**). Guidelines come from the society paper (PubMed/PMC). Anything not found in a source I read is **[UNVERIFIED]**.

**Source tags used inline**
- [L-xxx] = current US FDA prescribing information via openFDA (label effective date given)
- [L-TW] = Taiwan drug insert (仿單) on mcp.fda.gov.tw (official TFDA platform)
- [TFDA] = TFDA licence open-data file (InfoId=36, CSV dated 2026-10-27)
- [A] = PubMed abstract of the cited paper
- [FT] = PMC full text (results/methods)
- [G] = society guideline (paper read on PubMed/PMC)
- **[UNVERIFIED]** = not found in any source I read; do not print without checking

**Section status tags**
- **[VERIFIED]** = dose/fact confirmed in a primary or official source I opened
- **[PARTIAL]** = confirmed in a secondary source only, or only partly confirmed
- **[UNVERIFIED]** = could not confirm

**APA 7 notes.** Author lists follow APA 7: all authors up to 20; 21+ → first 19, ". . .", final author. Study-group bylines (e.g. "for the CASSINI Investigators") are omitted. Titles are sentence case from the PubMed record. Year = journal-issue year.

---

## 0. Corrections and flags for the editor (read first)

1. **DPYD testing is now a BOXED WARNING on US 5-FU and capecitabine labels (October 2025 revision).** The current fluorouracil and XELODA (capecitabine) labels carry a boxed warning headed "SERIOUS ADVERSE REACTIONS OR DEATH IN PATIENTS WITH COMPLETE DPD DEFICIENCY" and a new section 2.1 "Evaluation and Testing for DPD Deficiency Before Initiating": *"test patients for genetic variants of the DPYD gene unless immediate treatment is necessary"* [L-FLUOROURACIL 2026-07-15, recent major changes 10/2025; L-XELODA 2026-02-05, recent major changes 10/2025]. The FDA announcement page is "Content current as of 02/05/2026." **This is a strengthening** of the March-2024 fluorouracil / December-2022 capecitabine "Warnings and Precautions" language (older generic labels, e.g. Xiromed 2026-02-19, still show only the W&P wording, no boxed warning). The label does **not name specific variants** and notes **no FDA-authorized DPYD test currently exists**.
2. **The FDA label does NOT require DPYD testing for Taiwanese patients specifically, and the classic Western DPYD variants are rare in East Asians.** The four CPIC/Western variants (DPYD*2A c.1905+1G>A, c.2846A>T, c.1679T>G/DPYD*13, c.1236G>A/HapB3) are essentially the European panel; a Japanese study of 301 East-Asian patients found these common Western variants were **not** the drivers — instead **rare, population-specific loss-of-function DPYD variants** (allele frequency <0.01%) carried the toxicity signal [Yokoi 2020, A]. Teaching point: a negative "standard" DPYD panel does not exclude DPD deficiency in a Taiwanese patient; clinical vigilance for early severe toxicity still applies.
3. **Onivyde (liposomal irinotecan) did originate from a Taiwanese company — confirmed.** The TFDA licence holder is **智擎生技製藥股份有限公司 (PharmaEngine, Inc.), Taipei** [TFDA, licence 衛部藥輸字第026655號]. The drug began as **PEP02 / MM-398**: PharmaEngine licensed Asian + European rights from **Hermes Biosciences** (South San Francisco; Hermes was acquired by **Merrimack** in 2009); the first-in-human and key phase 1/2 trials were **Taiwan-led** (Chang 2015, Ko 2013, Chiang 2016 — all with L.-T. Chen / NHRI and PharmaEngine employees as authors); NAPOLI-1 (the registration trial) had Taiwanese first/senior authors (Wang-Gillam … Chen L.-T.) [PubMed affiliations; PMC full texts name PharmaEngine as sponsor]. Note the nuance: the liposome *technology* was Hermes/US; the *clinical development and the product licence in Taiwan* are PharmaEngine's.
4. **UGT1A1 dosing: the Western label reduces for `*28/*28`, but in Taiwanese/East Asians `*6` matters at least as much.** The US Onivyde and Camptosar labels key dose reduction to **UGT1A1*28 homozygosity** [L]. Camptosar's label adds that *"*6/*6, or *6/*28"* genotypes are also at risk and that **~2% of East Asians are homozygous *28, and ~2–6% homozygous *6** [L-CAMPTOSAR]. The Taiwan Onivyde insert carries **only the *28 wording** (no *6 reduction), so the label and the East-Asian literature diverge — flag this for the chapter [L-TW Onivyde]. For NALIRIFOX (first-line), **no *28 reduction is made — the 50 mg/m² dose is the same regardless of *28 genotype** [L].
5. **The NALIRIFOX and nal-IRI doses are quoted differently (free base vs salt) and are a classic exam trap.** NALIRIFOX = liposomal irinotecan **50 mg/m² (as irinotecan free base)**; NAPOLI-1 second-line = **70 mg/m² free base = 80 mg/m² of the hydrochloride trihydrate salt** [L-ONIVYDE]. Do not add a 5-FU bolus to either.
6. **"No 5-FU bolus" is specific to the ADJUVANT (PRODIGE 24) mFOLFIRINOX and to NALIRIFOX; the METASTATIC FOLFIRINOX (PRODIGE 4) DOES include a 400 mg/m² 5-FU bolus.** See §1. This is the single most common dosing error.
7. **Taiwan licence facts that contradict common assumptions** (all from TFDA 2026-10-27 file + insert): TS-1 (S-1) has **no adjuvant-pancreas indication** in Taiwan (locally advanced/metastatic only) — adjuvant S-1 (JASPAC 01) is off-label; **erlotinib has no pancreatic indication** in Taiwan (NSCLC only), though it is still FDA-approved with gemcitabine; **zenocutuzumab and daraxonrasib are not licensed** in Taiwan; pembrolizumab's only pancreas-relevant Taiwan indication is **tissue-agnostic MSI-H/dMMR after prior therapy**.
8. **Oxaliplatin now carries a US boxed warning for hypersensitivity/anaphylaxis** (not only neuropathy) [L-OXALIPLATIN]. Capecitabine's boxed warning also includes **bleeding with vitamin-K antagonists (warfarin)** in addition to DPD [L-XELODA].
9. **Olanzapine is now an ASCO option for cancer anorexia/cachexia (2023 rapid update)** — a change from the 2020 guideline, which recommended no specific agent. Low-dose (2.5 mg/day) [G].
10. **Anamorelin is approved for cancer cachexia (incl. pancreatic) in Japan (Dec 2020) but NOT in the US/EU and NOT in Taiwan** [Wakabayashi 2021, A; no TFDA entry]. Do not imply Taiwan availability.

---

# A. CHEMOTHERAPY REGIMENS — EXACT DOSES AND SCHEDULES

> Efficacy (median OS/PFS, HR) for each regimen is in `pancreas_2_trials.md` (PRODIGE 24 §3, APACT §4, JASPAC 01 §5, PRODIGE 4 §15, MPACT §16, NAPOLI 3 §17, NAPOLI-1 §18, PA.3 §19, GEST §20, POLO §21). This section gives the **administration detail a nurse needs**.

## 1. FOLFIRINOX family — [VERIFIED]

**mFOLFIRINOX, ADJUVANT (PRODIGE 24 / CCTG PA.6 schedule), every 2 weeks** [A, Conroy 2018]:
- Oxaliplatin **85 mg/m²** IV (over 2 h)
- Irinotecan **180 mg/m²**, **reduced to 150 mg/m²** after a protocol safety amendment
- Leucovorin **400 mg/m²**
- 5-FU **2400 mg/m² continuous infusion over 46 h** — **NO 5-FU bolus**
- 12 cycles (24 weeks) [see pancreas_2 §3 for DFS 21.4 vs 12.8 mo, OS 53.5 vs 35.5 mo, HR 0.66/0.68]

**FOLFIRINOX, METASTATIC (PRODIGE 4 / ACCORD 11 schedule), every 2 weeks** [A, Conroy 2011]:
- Oxaliplatin **85 mg/m²**
- Irinotecan **180 mg/m²**
- Leucovorin **400 mg/m²**
- 5-FU **400 mg/m² IV bolus, THEN 2400 mg/m² over 46 h** — **bolus IS given** [see pancreas_2 §15 for OS 11.1 vs 6.8 mo, HR 0.57]
- Eligibility was ECOG 0–1; modern practice uses mFOLFIRINOX (bolus dropped, irinotecan 150) for tolerability, but PRODIGE 4 as published used the bolus.

**Reference (adjuvant):** Conroy, T., Hammel, P., Hebbar, M., Ben Abdelghani, M., Wei, A. C., Raoul, J. L., Choné, L., Francois, E., Artru, P., Biagi, J. J., Lecomte, T., Assenat, E., Faroux, R., Ychou, M., Volet, J., Sauvanet, A., Breysacher, G., Di Fiore, F., Cripps, C., . . . Bachet, J. B. (2018). FOLFIRINOX or gemcitabine as adjuvant therapy for pancreatic cancer. *The New England Journal of Medicine, 379*(25), 2395–2406. https://doi.org/10.1056/NEJMoa1809775 — PMID 30575490
**Reference (metastatic):** Conroy, T., Desseigne, F., Ychou, M., Bouché, O., Guimbaud, R., Bécouarn, Y., Adenis, A., Raoul, J. L., Gourgou-Bourgade, S., de la Fouchardière, C., Bennouna, J., Bachet, J. B., Khemissa-Akouz, F., Péré-Vergé, D., Delbaldo, C., Assenat, E., Chauffert, B., Michel, P., Montoto-Grillot, C., & Ducreux, M. (2011). FOLFIRINOX versus gemcitabine for metastatic pancreatic cancer. *The New England Journal of Medicine, 364*(19), 1817–1825. https://doi.org/10.1056/NEJMoa1011923 — PMID 21561347

## 2. NALIRIFOX (first-line metastatic; NAPOLI 3) — [VERIFIED]

Days 1 and 15 of a 28-day cycle, **in this order** [L-ONIVYDE 2025-03-03, Clinical Studies 14; matches NAPOLI 3]:
1. **Liposomal irinotecan (Onivyde) 50 mg/m²** (as irinotecan free base) IV over **90 min**
2. **Oxaliplatin 60 mg/m²** IV over 120 min
3. **Leucovorin 400 mg/m²** IV over 30 min
4. **5-FU 2400 mg/m²** IV over **46 h**
- **UGT1A1*28 homozygotes: same 50 mg/m² — no reduction** [L].
- Premedicate with a **corticosteroid + antiemetic 30 min before** [L].
- This is the full NALIRIFOX regimen; the Onivyde dose is **not** interchangeable with conventional irinotecan ("DO NOT SUBSTITUTE ONIVYDE for other drugs containing irinotecan HCl" [L]).

## 3. nal-IRI + 5-FU/LV (second-line, post-gemcitabine; NAPOLI-1) — [VERIFIED]

Every 2 weeks [L-ONIVYDE; A Wang-Gillam 2016]:
- **Liposomal irinotecan 70 mg/m² (free base) = 80 mg/m² of the hydrochloride trihydrate salt**, IV over 90 min
- Leucovorin 400 mg/m² over 30 min
- 5-FU 2400 mg/m² over 46 h
- **UGT1A1*28 homozygotes: start at 50 mg/m², escalate to 70 as tolerated** [L — and Taiwan insert, which uses the same wording] [L-TW].
- Premedicate with corticosteroid + antiemetic 30 min before [L].
- Taiwan real-world (Yu 2022, Taipei VGH, n=67): median starting dose only **36.8 mg/m²**, median dose intensity 40.4 mg/m²; grade 3–4 neutropenia 21.5%, anaemia 18.5%, diarrhoea 15.4% — i.e. Taiwanese practice often starts below label [A/FT].

## 4. Gemcitabine + nab-paclitaxel (MPACT) — [VERIFIED]

Days 1, 8, 15 of a 28-day cycle [L-ABRAXANE 2022-10-31 §2.4; L-TW Abraxane §3.1.3]:
- **Nab-paclitaxel 125 mg/m²** IV over 30–40 min, **THEN**
- **Gemcitabine 1000 mg/m²** IV over 30–40 min, immediately after
- **Dose-reduction ladder (pancreas):** full 125/1000 → 100/800 → 75/600 → discontinue [L-ABRAXANE Table 3].
- Grade 3–4 peripheral neuropathy → **withhold until ≤ grade 1, resume one dose level lower** (nab-P reduced; gemcitabine **not** reduced for neuropathy) [L Table 5].
- Label warning specific to this combination: **sepsis** (5%; biliary obstruction or a biliary stent are risk factors) and **pneumonitis** (4%, can be fatal) [L §5.3, §5.4].

**Reference:** Von Hoff, D. D., Ervin, T., Arena, F. P., Chiorean, E. G., Infante, J., Moore, M., Seay, T., Tjulandin, S. A., Ma, W. W., Saleh, M. N., Harris, M., Reni, M., Dowden, S., Laheru, D., Bahary, N., Ramanathan, R. K., Tabernero, J., Hidalgo, M., Goldstein, D., . . . Renschler, M. F. (2013). Increased survival in pancreatic cancer with nab-paclitaxel plus gemcitabine. *The New England Journal of Medicine, 369*(18), 1691–1703. https://doi.org/10.1056/NEJMoa1304369 — PMID 24131140

## 5. Gemcitabine + capecitabine (GemCap; ESPAC-4 adjuvant / advanced) — [VERIFIED]

Capecitabine label, pancreatic indication (adjuvant) [L-XELODA 2026-02-05 §2.5]:
- **Capecitabine 830 mg/m² orally twice daily, days 1–21 of a 28-day cycle, max 6 cycles**, with
- **Gemcitabine 1000 mg/m² IV on days 1, 8, 15** of each 28-day cycle
- (Note: the ESPAC-4 trial protocol used capecitabine 1660 mg/m²/day in two divided doses for days 1–21 — i.e. ~830 mg/m² BID — matching the label. See pancreas_2 §2 for OS 28.0 vs 25.5 mo, HR 0.82.)
- Capecitabine: take **within 30 min after a meal**, swallow whole, doses ~12 h apart; round to nearest 150 mg [L §2.8].
- DPD testing before starting (boxed warning, §0 flag 1).

## 6. Gemcitabine (single agent; CONKO-001 adjuvant, backbone) — [VERIFIED]

- **1000 mg/m² IV over 30 min**, days 1, 8, 15 of a 28-day cycle (pancreas) [L-GEMCITABINE 2026-04-27 §2.4]. First cycle in metastatic MPACT control arm was weekly ×7 then 1 week off, then days 1/8/15 q28d [pancreas_2 §16].
- **Schedule-dependent toxicity:** infusion >60 min or more-than-weekly dosing increases toxicity (hypotension, flu-like symptoms, myelosuppression) — **keep the infusion ≤30–60 min** [L §5.1].
- Watch for: myelosuppression, **haemolytic uraemic syndrome / thrombotic microangiopathy**, pulmonary toxicity (pneumonitis up to 2 weeks after last dose), capillary leak, PRES, radiation recall [L §5].

## 7. S-1 (TS-1; JASPAC 01 dosing by BSA) — [VERIFIED, Taiwan insert]

S-1 is tegafur/gimeracil/oteracil. Dose is by **body-surface area**, taken **twice daily after meals**. The **adjuvant JASPAC 01 schedule** (28 days on, 14 days off = 6-week cycle, ×4) used the standard BSA table [A Uesaka 2016; dose table from Taiwan TS-1 insert §3.1, licence 衛署藥輸字第025242/025243號]:

| BSA (m²) | Initial dose (as tegafur) |
|---|---|
| < 1.25 | **40 mg twice daily (80 mg/day)** |
| 1.25 to < 1.5 | **50 mg twice daily (100 mg/day)** |
| ≥ 1.5 | **60 mg twice daily (120 mg/day)** |

- Dose levels for titration: 40 / 50 / 60 / **75** mg per dose; max 75 mg/dose, min 40 mg/dose [L-TW §3.1].
- **Taiwan indication is locally advanced/metastatic pancreas only — NOT adjuvant** (JASPAC 01 adjuvant use is off-label in Taiwan) [TFDA; see §0 flag 7].
- **Contraindicated** in: severe renal impairment (gimeracil accumulation → ↑5-FU), severe marrow suppression, severe hepatic impairment, pregnancy, concurrent other fluoropyrimidine or flucytosine, and **known complete DPD deficiency** [L-TW §4].
- **≥7-day washout** required between S-1 and any other fluoropyrimidine (or flucytosine), in either direction [L-TW §5.1.1, §7]; ≥4-week gap from brivudine/sorivudine [L-TW §7].
- S-1 pancreatic-trial toxicity (GEST/TTYTG0702 single-agent arm, Taiwan insert): grade ≥3 neutropenia 8.5%, anaemia 7.0%, leucopenia 3.7%; non-haem anorexia 6.3%, diarrhoea 4.4%, fatigue 3.7%. With gemcitabine: grade ≥3 neutropenia **61.8%**, leucopenia 37.5%, anaemia 14.2% [L-TW §8.2].
- S-1 signature toxicities vs 5-FU: **more stomatitis, diarrhoea, lacrimation/tear-duct obstruction, skin pigmentation**; less myelosuppression than gemcitabine [A; L-TW].

**Reference:** Uesaka, K., Boku, N., Fukutomi, A., Okamura, Y., Konishi, M., Matsumoto, I., Kaneoka, Y., Shimizu, Y., Nakamori, S., Sakamoto, H., Morinaga, S., Kainuma, O., Imai, K., Sata, N., Hishinuma, S., Ojima, H., Yamaguchi, R., Hirano, S., Sudo, T., & Ohashi, Y. (2016). Adjuvant chemotherapy of S-1 versus gemcitabine for resected pancreatic cancer: A phase 3, open-label, randomised, non-inferiority trial (JASPAC 01). *The Lancet, 388*(10041), 248–257. https://doi.org/10.1016/S0140-6736(16)30583-9 — PMID 27265347

## 8. Olaparib maintenance (POLO; germline BRCA1/2) — [VERIFIED]

- **300 mg (two 150 mg tablets) orally twice daily**, with or without food; continue to progression/toxicity [L-LYNPARZA 2025-07-10 §2.2; L-TW §3.1].
- 100 mg tablet is **for dose reduction only** — do not make up 300 mg from 100 mg tablets [L-TW].
- Moderate renal impairment (CrCl 31–50): **reduce to 200 mg BID** [L §2.5].
- Patient selection by an FDA-approved companion diagnostic for **germline BRCA** [L §1.6/2.1]; indication = maintenance after ≥16 weeks of first-line platinum without progression, metastatic [L; TFDA indication #5].
- See pancreas_2 §21: PFS 7.4 vs 3.8 mo (HR 0.53); OS not significant.

## 9. Erlotinib + gemcitabine (PA.3) — [VERIFIED, but not Taiwan-licensed for pancreas]

- **Erlotinib 100 mg orally once daily, on an empty stomach** (1 h before / 2 h after food), with gemcitabine [L-ERLOTINIB §2.3]. (NSCLC dose is 150 mg; pancreas is 100 mg.)
- US label warnings relevant to pancreas: **increased risk of CVA and of microangiopathic haemolytic anaemia (MAHA) in pancreatic-cancer patients**; GI perforation; bullous skin disorders [L §5].
- **Taiwan: erlotinib has NO pancreatic indication (NSCLC only)** [TFDA — all Tarceva/generic licences read EGFR-mutant NSCLC]. The marginal benefit (OS 6.24 vs 5.91 mo) means it is rarely used anyway.

---

# B. TOXICITY MANAGEMENT (nursing-critical)

## 10. Irinotecan / liposomal irinotecan — acute cholinergic syndrome and delayed diarrhoea — [VERIFIED]

Both the conventional irinotecan (Camptosar) and liposomal irinotecan (Onivyde) labels describe **two distinct diarrhoeas** [L-CAMPTOSAR 2026-05-12 §5.1; L-ONIVYDE §5.2]:

- **EARLY / acute (during or within 24 h of infusion): cholinergic syndrome.** Rhinitis, lacrimation, salivation, miosis, diaphoresis, flushing, abdominal cramping, **bradycardia**, intestinal hyperperistalsis. → **Atropine 0.25–1 mg IV or SC** (unless contraindicated), prophylactically or therapeutically [L-CAMPTOSAR §5.1, §2.4; L-ONIVYDE §5.2 "administer atropine for early diarrhea of any severity"]. More frequent at higher irinotecan doses.
- **LATE (>24 h, median onset ~5 days [3-week schedule] or ~11 days [weekly]): life-threatening secretory diarrhoea.** → **high-dose loperamide**: *"4 mg at the first onset of late diarrhea, then 2 mg every 2 hours until diarrhea-free for ≥12 hours"* (4 mg every 4 h at night). **Do not exceed 48 consecutive hours** at this dose (paralytic ileus risk) [L-CAMPTOSAR §5.1, patient counseling]. For Onivyde: "administer loperamide for late diarrhea of any severity" [L-ONIVYDE §5.2].
- Escalate (add fluoroquinolone antibiotic, octreotide, hospitalise) if: diarrhoea not improving within 24–48 h, fever/neutropenia, bloody stools, dehydration, or ileus [L; Benson 2004 guideline §16].
- In NAPOLI-1, **34% received loperamide for late and 26% atropine for early diarrhoea** on nal-IRI/5-FU/LV [L-ONIVYDE §5.2] — expect to use both agents routinely.
- Hold irinotecan/Onivyde for grade 2–4 diarrhoea; do not give to patients with **bowel obstruction** [L].

## 11. Irinotecan — UGT1A1 pharmacogenetics — [VERIFIED]

- SN-38 (active metabolite) is glucuronidated by **UGT1A1**; reduced-function alleles → ↑SN-38 → neutropenia and diarrhoea [L-CAMPTOSAR §12.5].
- **Western label rule:** reduce starting dose by ≥1 level for `*28/*28`, `*6/*6`, or `*6/*28` [L-CAMPTOSAR §2.3]. Onivyde (US + Taiwan): `*28/*28` → start 50 mg/m² in the second-line 70-regimen; **NALIRIFOX first-line = 50 mg/m² for all genotypes** [L; L-TW].
- **Population frequencies (from the Camptosar label itself):** homozygous *28 in **~20% Black, ~10% White, ~2% East Asian**; homozygous *6 in **~2–6% East Asian** (uncommon in White/Black) [L-CAMPTOSAR §12.5].
- **Teaching point for Taiwan:** in East Asians the *28 allele is less common but **the *6 allele is much more common** and is the clinically important one — testing only *28 (as some labels/assays do) misses East-Asian risk. See §12.

## 12. UGT1A1 *6 and *28 — frequencies and the Taiwanese/East-Asian picture — [VERIFIED]

- **Allele-frequency contrast (Taiwan PEP02 phase 1, Chang 2015, FT):** *"the Asian population is known to have a lower frequency of UGT1A1*28 (13.9% vs 33.4% in Caucasians) but a significantly higher frequency of UGT1A1*6 (13.0% vs 0.5% in Caucasians)."* The single treatment-related death in that Taiwanese PEP02 trial was a **UGT1A1 *6/*28 compound heterozygote** [A/FT].
- **Healthy Taiwanese (Huang 2000, n=290):** the A(TA)7TAA (*28) allele was "relatively rare" and the coding-region (incl. *6, c.211G>A) variation rate was "much higher … compared to Caucasians" [A].
- **Taiwanese mCRC (Liu 2008, n=128):** ~20% carried *28 (15.6% TA6/7, 4.7% TA7/7); carriers had markedly more grade 3–4 neutropenia (53.8% vs 4.9%) and diarrhoea (26.9% vs 5.9%) on irinotecan + 5-FU/LV [A].
- **Asian meta-analyses:** combined *6 + *28 testing predicts irinotecan neutropenia (Chen 2014: OR 2.55; Atasilp 2022: neutropenia OR 2.89, diarrhoea OR 2.26; homozygotes OR ~6.2 for neutropenia) [A].
- **Taiwan dose-escalation model (Lu 2015 / PURE-FIST Tsai 2020):** `*1/*1` and `*1/*28` start irinotecan **180 mg/m²** and may escalate; `*28/*28` starts **120 mg/m²**. Genotype-guided escalation improved response/PFS without more grade ≥3 AEs [A/FT].

**References (UGT1A1):**
- Huang, C. S., Luo, G. A., Huang, M. L., Yu, S. C., & Yang, S. S. (2000). Variations of the bilirubin uridine-diphosphoglucuronosyl transferase 1A1 gene in healthy Taiwanese. *Pharmacogenetics, 10*(6), 539–544. https://doi.org/10.1097/00008571-200008000-00007 — PMID 10975608
- Liu, C.-Y., Chen, P.-M., Chiou, T.-J., Liu, J.-H., Lin, J.-K., Lin, T.-C., Chen, W.-S., Jiang, J.-K., Wang, H.-S., & Wang, W.-S. (2008). UGT1A1*28 polymorphism predicts irinotecan-induced severe toxicities without affecting treatment outcome and survival in patients with metastatic colorectal carcinoma. *Cancer, 112*(9), 1932–1940. https://doi.org/10.1002/cncr.23370 — PMID 18300238
- Chang, T. C., Shiah, H. S., Yang, C. H., Yeh, K. H., Cheng, A. L., Shen, B. N., Wang, Y. W., Yeh, C. G., Chiang, N. J., Chang, J. Y., & Chen, L. T. (2015). Phase I study of nanoliposomal irinotecan (PEP02) in advanced solid tumor patients. *Cancer Chemotherapy and Pharmacology, 75*(3), 579–586. https://doi.org/10.1007/s00280-014-2671-x — PMID 25577133
- Chen, Y.-J., Hu, F., Li, C.-Y., Fang, J.-M., Chu, L., Zhang, X., & Xu, Q. (2014). The association of UGT1A1*6 and UGT1A1*28 with irinotecan-induced neutropenia in Asians: A meta-analysis. *Biomarkers, 19*(1), 56–62. https://doi.org/10.3109/1354750X.2013.867534 — PMID 24308720
- Atasilp, C., Biswas, M., Jinda, P., Nuntharadthanaphong, N., Rachanakul, J., Hongkaew, Y., Vanwong, N., Saokaew, S., & Sukasem, C. (2022). Association of UGT1A1*6, UGT1A1*28, or ABCC2 c.3972C>T genetic polymorphisms with irinotecan-induced toxicity in Asian cancer patients: Meta-analysis. *Clinical and Translational Science, 15*(7), 1613–1633. https://doi.org/10.1111/cts.13277 — PMID 35506159
- Tsai, H.-L., Huang, C.-W., Lin, Y.-W., Wang, J.-H., Wu, C.-C., Sung, Y.-C., Chen, T.-L., Wang, H.-M., Tang, H.-C., Chen, J.-B., Ke, T.-W., Tsai, C.-S., Huang, H.-Y., & Wang, J.-Y. (2020). Determination of the UGT1A1 polymorphism as guidance for irinotecan dose escalation in metastatic colorectal cancer treated with first-line bevacizumab and FOLFIRI (PURE FIST). *European Journal of Cancer, 138*, 19–29. https://doi.org/10.1016/j.ejca.2020.05.031 — PMID 32829105
- Lu, C.-Y., Huang, C.-W., Wu, I.-C., Tsai, H.-L., Ma, C.-J., Yeh, Y.-S., Chang, S.-F., Huang, M.-L., & Wang, J.-Y. (2015). Clinical implication of UGT1A1 promoter polymorphism for irinotecan dose escalation in metastatic colorectal cancer patients treated with bevacizumab combined with FOLFIRI in the first-line setting. *Translational Oncology, 8*(6), 474–479. https://doi.org/10.1016/j.tranon.2015.11.002 — PMID 26692528

## 13. Oxaliplatin — acute cold-induced dysesthesia, cumulative neuropathy, hypersensitivity — [VERIFIED]

Current US label; boxed warning is now **hypersensitivity/anaphylaxis** [L-OXALIPLATIN 2026-08-07, Hospira; boxed warning from Gland label 2026-08-24]:
- **Acute neuropathy** (within hours–2 days, ~56% of patients): transient paraesthesia/dysaesthesia of hands, feet, perioral area, throat; **precipitated/worsened by cold**; can include **pharyngolaryngeal dysaesthesia** (subjective dyspnoea/dysphagia with no stridor), jaw spasm. **Avoid cold drinks, ice, cold objects, cold air**; **do NOT use ice (oral cryotherapy) for mucositis** with oxaliplatin — cold worsens the syndrome [L §5.2, patient counseling].
- Prolonging the infusion from **2 h to 6 h** can mitigate acute toxicity / infusion reactions [L §2.2].
- **Delayed/cumulative sensory neuropathy** (>14 days, dose-dependent): paraesthesia, proprioceptive loss interfering with writing/buttoning/walking; 48% overall. Partially reversible after stopping (at 18 months ~21% still have some grade). Reduce dose or discontinue for persistent neurosensory toxicity [L §5.2].
- **Hypersensitivity/anaphylaxis** (boxed warning): can occur within minutes, any cycle; grade 3–4 in 2–3%. **Contraindicated** in prior platinum hypersensitivity; **discontinue permanently** for a hypersensitivity reaction [L boxed warning, §4, §5.1]. In Japanese mCRC data, grade 3/4 HSR incidence ~9.3%, correlated with **cumulative cycles** [Seki 2011, A].
- **Desensitisation** is feasible for selected patients who must continue a platinum (standardised 12-step protocol; 94% of 413 desensitisations had mild/no reaction) [Castells 2008, A] — a specialist allergy/oncology procedure, not routine.
- No agent prevents CIPN; **duloxetine** is the only agent with evidence for established painful CIPN; avoid acetyl-L-carnitine (may worsen) [ASCO CIPN guideline, Loprinzi 2020, G].

**References:**
- Seki, K., Senzaki, K., Tsuduki, Y., Ioroi, T., Fujii, M., Yamauchi, H., Shiraishi, Y., Nakata, I., Nishiguchi, K., Matsubayashi, T., Takakubo, Y., Okamura, N., Yamamori, M., Tamura, T., & Sakaeda, T. (2011). Risk factors for oxaliplatin-induced hypersensitivity reactions in Japanese patients with advanced colorectal cancer. *International Journal of Medical Sciences, 8*(3), 210–215. https://doi.org/10.7150/ijms.8.210 — PMID 21448307
- Castells, M. C., Tennant, N. M., Sloane, D. E., Hsu, F. I., Barrett, N. A., Hong, D. I., Laidlaw, T. M., Legere, H. J., Nallamshetty, S. N., Palis, R. I., Rao, J. J., Berlin, S. T., Campos, S. M., & Matulonis, U. A. (2008). Hypersensitivity reactions to chemotherapy: Outcomes and safety of rapid desensitization in 413 cases. *The Journal of Allergy and Clinical Immunology, 122*(3), 574–580. https://doi.org/10.1016/j.jaci.2008.02.044 — PMID 18502492
- Loprinzi, C. L., Lacchetti, C., Bleeker, J., Cavaletti, G., Chauhan, C., Hertz, D. L., Kelley, M. R., Lavino, A., Lustberg, M. B., Paice, J. A., Schneider, B. P., Lavoie Smith, E. M., Smith, M. L., Smith, T. J., Wagner-Johnston, N., & Hershman, D. L. (2020). Prevention and management of chemotherapy-induced peripheral neuropathy in survivors of adult cancers: ASCO guideline update. *Journal of Clinical Oncology, 38*(28), 3325–3348. https://doi.org/10.1200/JCO.20.01399 — PMID 32663120

## 14. 5-FU / capecitabine — DPYD (DPD) deficiency — [VERIFIED]

- **Current US boxed warning (both drugs, Oct 2025):** serious/fatal toxicity in complete DPD deficiency; **test for DPYD variants before starting unless treatment cannot wait**; **avoid** in complete-deficiency homozygotes/compound heterozygotes (no safe dose); **individualise** in partial deficiency [L-FLUOROURACIL 2026-07-15 boxed warning + §2.1, §5.1; L-XELODA 2026-02-05]. The FDA announcement is current as of 2026-02-05. No FDA-authorized test and no specific variants named in the label.
- Capecitabine boxed warning **also** covers **bleeding with vitamin-K antagonists** (↑INR, monitor closely) [L-XELODA].
- **CPIC 2017 dosing by activity score (AS):** AS 1 (one no-function allele, e.g. *2A or c.1679T>G heterozygote) → **reduce starting dose ~50%**; AS 1.5 (one decreased-function allele, e.g. c.2846A>T or c.1236G>A/HapB3) → ~25–50% reduction, individualise; AS 0 (complete deficiency) → **avoid** [Amstutz 2018, G]. Prospective Dutch data: upfront genotyping + a 50% reduction for *2A and c.1679T>G made their toxicity rate comparable to non-carriers [Henricks 2018, A].
- **East-Asian caveat (see §0 flag 2):** the four Western variants are rare in East Asians; Japanese data implicate **rare population-specific loss-of-function DPYD variants** (allele freq <0.01%) instead [Yokoi 2020]. A standard DPYD panel can be falsely reassuring in a Taiwanese patient — maintain clinical vigilance for early-onset severe mucositis/diarrhoea/neutropenia. Taiwan TS-1 insert lists **known complete DPD deficiency as an absolute contraindication** [L-TW].
- Early management if severe toxicity despite negative/absent testing: withhold/discontinue; **uridine triacetate** is the 5-FU/capecitabine overdose/early-severe-toxicity antidote (not in these label sections but standard of care; [UNVERIFIED] here — confirm local availability).

**References:**
- Amstutz, U., Henricks, L. M., Offer, S. M., Barbarino, J., Schellens, J. H. M., Swen, J. J., Klein, T. E., McLeod, H. L., Caudle, K. E., Diasio, R. B., & Schwab, M. (2018). Clinical Pharmacogenetics Implementation Consortium (CPIC) guideline for dihydropyrimidine dehydrogenase genotype and fluoropyrimidine dosing: 2017 update. *Clinical Pharmacology and Therapeutics, 103*(2), 210–216. https://doi.org/10.1002/cpt.911 — PMID 29152729
- Henricks, L. M., Lunenburg, C. A. T. C., de Man, F. M., Meulendijks, D., Frederix, G. W. J., Kienhuis, E., Creemers, G.-J., Baars, A., Dezentjé, V. O., Imholz, A. L. T., Jeurissen, F. J. F., Portielje, J. E. A., Jansen, R. L. H., Hamberg, P., Ten Tije, A. J., Droogendijk, H. J., Koopman, M., Nieboer, P., van de Poel, M. H. W., . . . Schellens, J. H. M. (2018). DPYD genotype-guided dose individualisation of fluoropyrimidine therapy in patients with cancer: A prospective safety analysis. *The Lancet Oncology, 19*(11), 1459–1467. https://doi.org/10.1016/S1470-2045(18)30686-7 — PMID 30348537
- Yokoi, K., Nakajima, Y., Matsuoka, H., Shinkai, Y., Ishihara, T., Maeda, Y., Kato, T., Katsuno, H., Masumori, K., Kawada, K., Yoshikawa, T., Ito, T., & Kurahashi, H. (2020). Impact of DPYD, DPYS, and UPB1 gene variations on severe drug-related toxicity in patients with cancer. *Cancer Science, 111*(9), 3359–3366. https://doi.org/10.1111/cas.14553 — PMID 32619063

## 15. Capecitabine — hand-foot syndrome (palmar-plantar erythrodysaesthesia) — [VERIFIED]

- Label: withhold capecitabine for **grade 2–3 HFS**, then resume at same/reduced dose per Table 1 (grade 2: 100% → 75% → 50% → discontinue over recurrences; grade 3: 75% → 50% → discontinue) [L-XELODA §2.5, §5.8].
- **Prophylaxis:** best evidence is **10% urea cream** — in the AIO phase 3 trial, 10% urea cream was **superior** to a newer antioxidant ointment (HFS 22.4% vs 39.5% over 6 weeks) [Hofheinz 2015, A]. Supportive: emollients, avoid friction/heat/pressure, cotton gloves/socks.
- 5-FU can also cause HFS (continuous-infusion schedules); withhold for grade 2–3 [L-FLUOROURACIL §2.7].

**Reference:** Hofheinz, R.-D., Gencer, D., Schulz, H., Stahl, M., Hegewisch-Becker, S., Loeffler, L. M., Kronawitter, U., Bolz, G., Potenberg, J., Tauchert, F., Al-Batran, S.-E., & Schneeweiss, A. (2015). Mapisal versus urea cream as prophylaxis for capecitabine-associated hand-foot syndrome: A randomized phase III trial of the AIO Quality of Life Working Group. *Journal of Clinical Oncology, 33*(22), 2444–2449. https://doi.org/10.1200/JCO.2014.60.4587 — PMID 26124485

## 16. nab-paclitaxel — neuropathy and sepsis — [VERIFIED]

- Grade 3–4 sensory neuropathy on nab-P/gemcitabine in MPACT: **17% vs 1%**; median time to improve to ≤grade 1 was **29 days** [pancreas_2 §16, A]. Management: **withhold until ≤ grade 1, resume one dose level lower** (nab-P only; gemcitabine not reduced for neuropathy) [L-ABRAXANE §2.6 Table 5].
- **Do NOT substitute nab-paclitaxel for or with other paclitaxel formulations** — different dosing [L §2.1].
- Infusion over 30–40 min; limiting to 30 min lowers infusion-reaction risk [L §2.1]. Severe hypersensitivity → do not rechallenge; cross-reactivity with other taxanes reported [L §5.5].
- **Sepsis** (5%; biliary obstruction/stent are risk factors) and **pneumonitis** (4%) are combination-specific label warnings [L §5.3–5.4].

## 17. Gemcitabine — key safety points — [VERIFIED]
Covered in §6: schedule-dependent toxicity (keep infusion ≤30–60 min), myelosuppression, HUS/TMA, pneumonitis, capillary leak, radiation recall, SCARs [L-GEMCITABINE §5].

---

# C. SUPPORTIVE / PROCEDURAL CARE

## 18. Biliary obstruction — stents and cholangitis — [VERIFIED]

- **Preoperative drainage is NOT routine.** van der Gaag 2010 RCT: routine preop biliary drainage before pancreatic-head surgery **increased** serious complications (74% vs 39% with early surgery, RR 0.54) [A]. ESGE: reserve preop drainage for **cholangitis, severe symptomatic jaundice (e.g. intense pruritus), delayed surgery, or before neoadjuvant chemotherapy in jaundiced patients** [G, Dumonceau 2018].
- **Metal vs plastic stent:** for a malignant distal obstruction expected to be managed non-operatively, a **self-expandable metal stent (SEMS)** is preferred — lower occlusion, fewer reinterventions, **less cholangitis** (8% vs 21%) than plastic [Sawas 2015 meta-analysis, A]. ESGE: **10-mm SEMS** for preop drainage; SEMS for palliative distal malignant obstruction (strong, high-quality); for **unconfirmed** aetiology use a covered SEMS or plastic, not an uncovered SEMS [G]. Plastic stents clog at ~3 months, so they suit only very short bridges or undiagnosed strictures.
- **Cholangitis — Tokyo Guidelines 2018 (TG18):** diagnosis needs (A) systemic inflammation + (B) cholestasis + (C) imaging of biliary dilatation/cause; severity grading (I mild / II moderate / III severe with organ dysfunction) guides timing of drainage. **Grade II benefits from early/urgent biliary drainage** [G, Kiriyama 2018]. Blood cultures should be drawn. Nursing: watch for Charcot's triad (fever, RUQ pain, jaundice) and Reynolds' pentad (+hypotension, confusion → Grade III).

**References:**
- van der Gaag, N. A., Rauws, E. A. J., van Eijck, C. H. J., Bruno, M. J., van der Harst, E., Kubben, F. J. G. M., Gerritsen, J. J. G. M., Greve, J. W., Gerhards, M. F., de Hingh, I. H. J. T., Klinkenbijl, J. H., Nio, C. Y., de Castro, S. M. M., Busch, O. R. C., van Gulik, T. M., Bossuyt, P. M. M., & Gouma, D. J. (2010). Preoperative biliary drainage for cancer of the head of the pancreas. *The New England Journal of Medicine, 362*(2), 129–137. https://doi.org/10.1056/NEJMoa0903230 — PMID 20071702
- Dumonceau, J.-M., Tringali, A., Papanikolaou, I. S., Blero, D., Mangiavillano, B., Schmidt, A., Vanbiervliet, G., Costamagna, G., Devière, J., García-Cano, J., Gyökeres, T., Hassan, C., Prat, F., Siersema, P. D., & van Hooft, J. E. (2018). Endoscopic biliary stenting: Indications, choice of stents, and results: European Society of Gastrointestinal Endoscopy (ESGE) Clinical Guideline — updated October 2017. *Endoscopy, 50*(9), 910–930. https://doi.org/10.1055/a-0659-9864 — PMID 30086596
- Sawas, T., Al Halabi, S., Parsi, M. A., & Vargo, J. J. (2015). Self-expandable metal stents versus plastic stents for malignant biliary obstruction: A meta-analysis. *Gastrointestinal Endoscopy, 82*(2), 256–267.e7. https://doi.org/10.1016/j.gie.2015.03.1980 — PMID 25982849
- Kiriyama, S., Kozaka, K., Takada, T., Strasberg, S. M., Pitt, H. A., Gabata, T., Hata, J., Liau, K.-H., Miura, F., Horiguchi, A., Liu, K.-H., Su, C.-H., Wada, K., Jagannath, P., Itoi, T., Gouma, D. J., Mori, Y., Mukai, S., Giménez, M. E., . . . Yamamoto, M. (2018). Tokyo Guidelines 2018: Diagnostic criteria and severity grading of acute cholangitis (with videos). *Journal of Hepato-Biliary-Pancreatic Sciences, 25*(1), 17–30. https://doi.org/10.1002/jhbp.512 — PMID 29032610

## 19. Gastric outlet obstruction (GOO) — [VERIFIED]

- **Enteral (duodenal) SEMS vs surgical gastrojejunostomy (SUSTENT RCT):** stent gives **faster** symptom relief (median 5 vs 8 days) but **more late recurrent obstruction/reinterventions**; gastrojejunostomy gives better **long-term** relief. Choose **stent if life expectancy < 2 months, surgical GJ if ≥ 2 months** [Jeurnink 2010, A].
- **EUS-guided gastroenterostomy (EUS-GE)** is now an option in expert centres (ESGE: alternative to enteral stenting or surgery) [G, van der Merwe 2022]. DRA-GOO RCT (Teoh 2025): EUS-GE had far **fewer 6-month reinterventions than duodenal stenting (4% vs 29%)** and better eating, with similar survival/adverse events [A].

**References:**
- Jeurnink, S. M., Steyerberg, E. W., van Hooft, J. E., van Eijck, C. H. J., Schwartz, M. P., Vleggaar, F. P., Kuipers, E. J., & Siersema, P. D. (2010). Surgical gastrojejunostomy or endoscopic stent placement for the palliation of malignant gastric outlet obstruction (SUSTENT study): A multicenter randomized trial. *Gastrointestinal Endoscopy, 71*(3), 490–499. https://doi.org/10.1016/j.gie.2009.09.042 — PMID 20003966
- van der Merwe, S. W., van Wanrooij, R. L. J., Bronswijk, M., Everett, S., Lakhtakia, S., Rimbas, M., Hucl, T., Kunda, R., Badaoui, A., Law, R., Arcidiacono, P. G., Larghi, A., Giovannini, M., Khashab, M. A., Binmoeller, K. F., Barthet, M., Perez-Miranda, M., & van Hooft, J. E. (2022). Therapeutic endoscopic ultrasound: European Society of Gastrointestinal Endoscopy (ESGE) guideline. *Endoscopy, 54*(2), 185–205. https://doi.org/10.1055/a-1717-1391 — PMID 34937098
- Teoh, A. Y. B., Lakhtakia, S., Tarantino, I., Perez-Miranda, M., Kunda, R., Maluf-Filho, F., Dhir, V., Basha, J., Chan, S. M., Ligresti, D., Ma, M. T. W., de la Serna-Higuera, C., Yip, H. C., Ng, E. K. W., Chiu, P. W. Y., & Itoi, T. (2025). Endoscopic ultrasonography-guided gastroenterostomy versus uncovered duodenal metal stenting for unresectable malignant gastric outlet obstruction (DRA-GOO): A multicentre randomised controlled trial. *The Lancet Gastroenterology & Hepatology, 10*(6), e8–e16. https://doi.org/10.1016/S2468-1253(25)00136-0 — PMID 40347959

## 20. Pancreatic exocrine insufficiency (PEI) and PERT dosing — [VERIFIED]

- **PEI occurs in ~70% of pancreatic-cancer patients** (higher with head tumours and advanced disease; pooled prevalence in advanced disease ~72%) [European PEI guideline, Dominguez-Muñoz 2025, FT, Statement 6.1.1–6.1.2].
- **PERT dose (adults):** **40,000–50,000 units of lipase (PhEur/USP) with each main meal, and half that (20,000–25,000 units) with snacks**, taken **with/throughout meals and snacks** [G, 2025 European PEI guideline, FT]. This matches the ESPEN pancreatitis guideline [Arvanitakis 2024]. Doses below 40,000 units/meal have scarce evidence; **severe PEI (pancreatic cancer, post-pancreatoduodenectomy/total pancreatectomy) often needs higher doses**.
- **Non-response →** confirm adherence and correct timing (taken with food), **escalate the dose, and add a proton-pump inhibitor** (acid lowers enteric-coating dissolution) before testing for other causes [G, Statement 3.7].
- **Taiwan products:** **Creon 25000 and Creon 40000** (pancreatin; 卡利消腸溶微粒膠囊) are licensed for PEI due to cystic fibrosis, chronic pancreatitis or pancreatic surgery; **"Creon 10000" is licensed only as a digestive aid (幫助消化)** [TFDA 衛部藥輸字第027421/027422/027423號]. The licence wording does not list pancreatic *cancer* explicitly, so PERT in cancer-related PEI is by extension of the "pancreatic surgery/chronic pancreatitis" indication [TFDA]. Count units by **lipase**, not capsule number.
- PERT improves symptoms and nutritional status (level 1) and **may improve overall survival** in PEI secondary to pancreatic cancer (level 2) [G, Statement 6.6.1–6.6.3]; a UK population study found adjusted median survival ~2.6× longer in PERT-treated patients [Roberts 2019, A].

**References:**
- Dominguez-Muñoz, J. E., Vujasinovic, M., de la Iglesia, D., Cahen, D., Capurso, G., Gubergrits, N., Hegyi, P., Hungin, P., Ockenga, J., Paiella, S., Perkhofer, L., Rebours, V., Rosendahl, J., Salvia, R., Scheers, I., Szentesi, A., Bonovas, S., Piovani, D., & Löhr, J. M. (2025). European guidelines for the diagnosis and treatment of pancreatic exocrine insufficiency: UEG, EPC, EDS, ESPEN, ESPGHAN, ESDO, and ESPCG evidence-based recommendations. *United European Gastroenterology Journal, 13*(1), 125–172. https://doi.org/10.1002/ueg2.12674 — PMID 39639485
- Arvanitakis, M., Ockenga, J., Bezmarevic, M., Gianotti, L., Krznarić, Ž., Lobo, D. N., Löser, C., Madl, C., Meier, R., Phillips, M., Rasmussen, H. H., Van Hooft, J. E., & Bischoff, S. C. (2024). ESPEN practical guideline on clinical nutrition in acute and chronic pancreatitis. *Clinical Nutrition, 43*(2), 395–412. https://doi.org/10.1016/j.clnu.2023.12.019 — PMID 38169174
- Roberts, K. J., Bannister, C. A., & Schrem, H. (2019). Enzyme replacement improves survival among patients with pancreatic cancer: Results of a population based study. *Pancreatology, 19*(1), 114–121. https://doi.org/10.1016/j.pan.2018.10.010 — PMID 30385188

## 21. Cachexia / anorexia — [VERIFIED]

- **ASCO 2020** found no agent strong enough to recommend as standard; dietary counselling may be offered; progesterone analogues and short-term corticosteroids may be used for appetite/weight; **do not routinely use enteral/parenteral feeding** [G, Roeland 2020].
- **ASCO 2023 rapid update:** clinicians **may offer low-dose olanzapine (2.5 mg once daily)** to improve appetite/weight (evidence quality intermediate, strength moderate; most evidence in lung/GI cancers) [G, Roeland 2023]. Basis: Sandhya 2023 RCT (incl. hepatopancreaticobiliary) — olanzapine 2.5 mg/day gave weight gain >5% in 60% vs 9% and better appetite/QoL with minimal side effects [A].
- **Anamorelin** (oral ghrelin-receptor agonist) is **approved in Japan (Dec 2020) for cachexia in NSCLC, gastric, pancreatic, colorectal cancer**; **not approved in US/EU; not in Taiwan** [Wakabayashi 2021, A; no TFDA entry — §0 flag 10].

**References:**
- Roeland, E. J., Bohlke, K., Baracos, V. E., Bruera, E., Del Fabbro, E., Dixon, S., Fallon, M., Herrstedt, J., Lau, H., Platek, M., Rugo, H. S., Schnipper, H. H., Smith, T. J., Tan, W., & Loprinzi, C. L. (2020). Management of cancer cachexia: ASCO guideline. *Journal of Clinical Oncology, 38*(21), 2438–2453. https://doi.org/10.1200/JCO.20.00611 — PMID 32432946
- Roeland, E. J., Bohlke, K., Baracos, V. E., Smith, T. J., & Loprinzi, C. L. (2023). Cancer cachexia: ASCO guideline rapid recommendation update. *Journal of Clinical Oncology, 41*(25), 4178–4179. https://doi.org/10.1200/JCO.23.01280 — PMID 37467399
- Sandhya, L., Devi Sreenivasan, N., Goenka, L., Dubashi, B., Kayal, S., Solaiappan, M., Govindarajalou, R., Kt, H., & Ganesan, P. (2023). Randomized double-blind placebo-controlled study of olanzapine for chemotherapy-related anorexia in patients with locally advanced or metastatic gastric, hepatopancreaticobiliary, and lung cancer. *Journal of Clinical Oncology, 41*(14), 2617–2627. https://doi.org/10.1200/JCO.22.01997 — PMID 36977285
- Wakabayashi, H., Arai, H., & Inui, A. (2021). The regulatory approval of anamorelin for treatment of cachexia in patients with non-small cell lung cancer, gastric cancer, pancreatic cancer, and colorectal cancer in Japan: Facts and numbers. *Journal of Cachexia, Sarcopenia and Muscle, 12*(1), 14–16. https://doi.org/10.1002/jcsm.12675 — PMID 33382205

## 22. Venous thromboembolism (VTE) — [VERIFIED]

- **Pancreatic cancer is a "very high-risk" site in the Khorana score (2 points for the tumour site alone).** Khorana score components (1 point each unless noted): **site — 2 points for very-high-risk (stomach, pancreas), 1 point for high-risk (lung, gynaecologic, bladder, testicular, lymphoma)**; platelets ≥350×10⁹/L; Hb <10 g/dL or ESA use; leukocytes >11×10⁹/L; BMI ≥35. Score ≥3 ≈ 7% short-term VTE [Khorana 2008, FT; site definitions confirmed in Mulder 2019 and a 2021 review]. A pancreatic-cancer patient therefore starts at 2 and crosses the ≥2 prophylaxis threshold with almost any second factor.
- **CASSINI (rivaroxaban 10 mg/day):** primary endpoint (to day 180) not significant (HR 0.66, p=0.10) because of off-treatment events, but **during the on-treatment intervention period, substantially fewer VTE (2.6% vs 6.4%, HR 0.40)** with low major bleeding [Khorana 2019, A]. **Pancreatic subgroup (n=273):** on-treatment VTE 3.7% vs 10.1%, HR 0.35, no excess major bleeding — supports prophylaxis in this group [Vadhan-Raj 2020, A].
- **AVERT (apixaban 2.5 mg BID):** VTE 4.2% vs 10.2% (HR 0.41, p<0.001); more major bleeding (3.5% vs 1.8%) [Carrier 2019, A].
- **ASCO 2023 VTE guideline:** apixaban, rivaroxaban or LMWH may be offered for thromboprophylaxis to selected high-risk ambulatory patients (Khorana ≥2) starting chemo, after bleeding-risk assessment; apixaban is now a strong option for VTE treatment [Key 2023, G].

**References:**
- Khorana, A. A., Kuderer, N. M., Culakova, E., Lyman, G. H., & Francis, C. W. (2008). Development and validation of a predictive model for chemotherapy-associated thrombosis. *Blood, 111*(10), 4902–4907. https://doi.org/10.1182/blood-2007-10-116327 — PMID 18216292
- Khorana, A. A., Soff, G. A., Kakkar, A. K., Vadhan-Raj, S., Riess, H., Wun, T., Streiff, M. B., Garcia, D. A., Liebman, H. A., Belani, C. P., O'Reilly, E. M., Patel, J. N., Yimer, H. A., Wildgoose, P., Burton, P., Vijapurkar, U., Kaul, S., Eikelboom, J., McBane, R., . . . Lyman, G. H. (2019). Rivaroxaban for thromboprophylaxis in high-risk ambulatory patients with cancer. *The New England Journal of Medicine, 380*(8), 720–728. https://doi.org/10.1056/NEJMoa1814630 — PMID 30786186
- Carrier, M., Abou-Nassar, K., Mallick, R., Tagalakis, V., Shivakumar, S., Schattner, A., Kuruvilla, P., Hill, D., Spadafora, S., Marquis, K., Trinkaus, M., Tomiak, A., Lee, A. Y. Y., Gross, P. L., Lazo-Langner, A., El-Maraghi, R., Goss, G., Le Gal, G., Stewart, D., . . . Wells, P. S. (2019). Apixaban to prevent venous thromboembolism in patients with cancer. *The New England Journal of Medicine, 380*(8), 711–719. https://doi.org/10.1056/NEJMoa1814468 — PMID 30511879
- Vadhan-Raj, S., McNamara, M. G., Venerito, M., Riess, H., O'Reilly, E. M., Overman, M. J., Zhou, X., Vijapurkar, U., Kaul, S., Wildgoose, P., & Khorana, A. A. (2020). Rivaroxaban thromboprophylaxis in ambulatory patients with pancreatic cancer: Results from a pre-specified subgroup analysis of the randomized CASSINI study. *Cancer Medicine, 9*(17), 6196–6204. https://doi.org/10.1002/cam4.3269 — PMID 32663379
- Mulder, F. I., Candeloro, M., Kamphuisen, P. W., Di Nisio, M., Bossuyt, P. M., Guman, N., Smit, K., Büller, H. R., & van Es, N. (2019). The Khorana score for prediction of venous thromboembolism in cancer patients: A systematic review and meta-analysis. *Haematologica, 104*(6), 1277–1287. https://doi.org/10.3324/haematol.2018.209114 — PMID 30606788
- Key, N. S., Khorana, A. A., Kuderer, N. M., Bohlke, K., Lee, A. Y. Y., Arcelus, J. I., Wong, S. L., Balaban, E. P., Flowers, C. R., Gates, L. E., Kakkar, A. K., Tempero, M. A., Gupta, S., Lyman, G. H., & Falanga, A. (2023). Venous thromboembolism prophylaxis and treatment in patients with cancer: ASCO guideline update. *Journal of Clinical Oncology, 41*(16), 3063–3071. https://doi.org/10.1200/JCO.23.00294 — PMID 37075273

## 23. Celiac plexus neurolysis (CPN) — [VERIFIED]

- **Wong 2004 (percutaneous NCPB RCT, n=100):** NCPB improved pain vs opioids alone (fewer with moderate/severe pain at 6 weeks, 14% vs 40%) **but did not reduce opioid consumption, improve QoL, or prolong survival** [A].
- **Wyse 2011 (early EUS-CPN RCT, n=96):** early EUS-CPN at diagnostic EUS reduced pain at 3 months and tended to lower morphine use; **no QoL or survival benefit** [A].
- **Cochrane (Arcidiacono 2011):** small but significant pain reduction and **significantly lower opioid consumption**, with **fewer adverse effects than opioids** [A].
- Nursing: CPN is an **adjunct** to reduce opioid burden and opioid side effects (constipation, sedation), not a cure for pain; expect transient post-procedure hypotension and diarrhoea.

**References:**
- Wong, G. Y., Schroeder, D. R., Carns, P. E., Wilson, J. L., Martin, D. P., Kinney, M. O., Mantilla, C. B., & Warner, D. O. (2004). Effect of neurolytic celiac plexus block on pain relief, quality of life, and survival in patients with unresectable pancreatic cancer: A randomized controlled trial. *JAMA, 291*(9), 1092–1099. https://doi.org/10.1001/jama.291.9.1092 — PMID 14996778
- Wyse, J. M., Carone, M., Paquin, S. C., Usatii, M., & Sahai, A. V. (2011). Randomized, double-blind, controlled trial of early endoscopic ultrasound-guided celiac plexus neurolysis to prevent pain progression in patients with newly diagnosed, painful, inoperable pancreatic cancer. *Journal of Clinical Oncology, 29*(26), 3541–3546. https://doi.org/10.1200/JCO.2010.32.2750 — PMID 21844506
- Arcidiacono, P. G., Calori, G., Carrara, S., McNicol, E. D., & Testoni, P. A. (2011). Celiac plexus block for pancreatic cancer pain in adults. *Cochrane Database of Systematic Reviews, 2011*(3), CD007519. https://doi.org/10.1002/14651858.CD007519.pub2 — PMID 21412903

## 24. Diabetes (pancreatogenic / type 3c and new-onset) — [VERIFIED]

- **Pancreatic cancer is a diabetogenic state:** DM is far more prevalent in pancreatic-cancer patients than controls (47% vs 7%), and is predominantly **new-onset (<2 years)**; it often **resolves after pancreaticoduodenectomy** when new-onset — evidence the tumour induces it [Pannala 2008, A]. New-onset DM after age 50 can be an early marker of pancreatic cancer.
- **Type 3c (pancreatogenic) diabetes:** caused by exocrine-pancreas disease (chronic pancreatitis, PDAC, post-pancreatectomy). Not simple type 2 — there is concurrent **loss of glucagon and PP**, so it is **"brittle" with high hypoglycaemia risk**, and **coexisting PEI** is usual. Insulin is often required, especially after resection; metformin is reasonable where feasible [Hart 2016, A]. Nursing: PERT and diabetes management go together in type 3c.

**References:**
- Pannala, R., Leirness, J. B., Bamlet, W. R., Basu, A., Petersen, G. M., & Chari, S. T. (2008). Prevalence and clinical profile of pancreatic cancer-associated diabetes mellitus. *Gastroenterology, 134*(4), 981–987. https://doi.org/10.1053/j.gastro.2008.01.039 — PMID 18395079
- Hart, P. A., Bellin, M. D., Andersen, D. K., Bradley, D., Cruz-Monserrate, Z., Forsmark, C. E., Goodarzi, M. O., Habtezion, A., Korc, M., Kudva, Y. C., Pandol, S. J., Yadav, D., & Chari, S. T. (2016). Type 3c (pancreatogenic) diabetes mellitus secondary to chronic pancreatitis and pancreatic cancer. *The Lancet Gastroenterology & Hepatology, 1*(3), 226–237. https://doi.org/10.1016/S2468-1253(16)30106-6 — PMID 28404095

---

# D. TAIWAN LICENCE STATUS (TFDA open-data file InfoId=36, CSV dated 2026-10-27; indications cross-checked on the mcp.fda.gov.tw insert platform) — [VERIFIED]

| Drug (brand) | TFDA licence(s) | Status / last change | Pancreatic indication in Taiwan (abridged, as written) |
|---|---|---|---|
| **Liposomal irinotecan** (Onivyde 安能得微脂體注射劑) | 衛部藥輸字第026655號 | Active; issued 2015-12-07; last changed **2026-02-25**; valid to 2030-12-07. Holder **智擎生技製藥 (PharmaEngine)** | (1) **First-line** metastatic, with oxaliplatin + 5-FU + LV (NALIRIFOX); (2) with 5-FU + LV after gemcitabine |
| **Nab-paclitaxel** (Abraxane 亞伯杉) | 衛部藥輸字第026484號 | Active; 2015-03-19; last changed 2025-03-07 | With gemcitabine, first-line metastatic. (No albumin-bound generic found under nab/protein-bound search as of 2026-10-27) |
| **S-1 / TS-1** (愛斯萬; also "剋伏" Golfer generic) | 衛署藥輸字第025242/025243號 (TS-1); 衛部藥製字第060480/060482號 (Golfer) | Active; TS-1 2010-08-05, last changed 2025-04-23 | **Locally advanced or metastatic pancreas only — NO adjuvant indication** |
| **Olaparib** (Lynparza 令癌莎 100/150 mg) | 衛部藥輸字第027445/027446號 | Active; 2018-06-05; last changed 2025-11-01 | Indication #5: single-agent **maintenance, germline BRCA metastatic pancreas, no progression after ≥16 wk first-line platinum** |
| **Erlotinib** (Tarceva 得舒緩 + many generics) | 衛署藥輸字第025071號 etc. | Active | **NONE for pancreas** — all licences read EGFR-mutant NSCLC first-line/maintenance + 2nd-line lung adenocarcinoma |
| **Larotrectinib** (Vitrakvi 維泰凱) | 衛部藥輸字第027746–027748號 | Active; 2019-12-03; last changed 2026-02-10 | Tissue-agnostic **NTRK fusion** solid tumour (adult + paediatric), with the 3 standard conditions |
| **Entrectinib** (Rozlytrek 羅思克) | 衛部藥輸字第027864/027865號 | Active; 2020-05-21; last changed 2026-09-18 | ROS1+ NSCLC; **NTRK fusion** solid tumour (≥1 month old) — tissue-agnostic |
| **Pembrolizumab** (Keytruda 吉舒達) | 衛部菌疫輸字第001025號 | Active; current licence 2024-10-28; last changed 2026-09-10 | Pancreas-relevant: indication #9 **tissue-agnostic MSI-H/dMMR** unresectable/metastatic solid tumour after prior therapy with no suitable alternative |
| **Zenocutuzumab** (NRG1-fusion) | — | **Not found in TFDA file (0 results)** | **Not licensed in Taiwan** |

Notes:
- **Oxaliplatin, irinotecan (conventional), gemcitabine, 5-FU, tegafur** all have active Taiwan licences with pancreatic indications; FOLFIRINOX is written into the oxaliplatin and irinotecan labels as *"與5-fluorouracil、leucovorin…合併治療(FOLFIRINOX)，作為轉移性胰臟癌之第一線治療"* [TFDA]. **Capecitabine licences active in the file carry no pancreatic indication** (colorectal/breast/gastric only) — GemCap for pancreas would be off-label in Taiwan [TFDA; **[PARTIAL]** — I searched the active capecitabine records, found 0 with "胰"].
- **Daraxonrasib** (RASONQUE) and anamorelin: **not in the TFDA file** — not licensed in Taiwan.
- **Creon 25000/40000** (pancreatin): active, PEI from CF / chronic pancreatitis / pancreatic surgery [衛部藥輸字第027421/027422號].
- NHI reimbursement status **not verifiable** (www.nhi.gov.tw unreachable). The Pan-Asian ESMO guideline (pancreas_2 [S-PanAsia]) notes new drugs take 1–2 years post-FDA/EMA to reach Taiwan, then 1–2 more for NHI cover; KRAS PCR self-paid, MSI IHC reimbursed. **[UNVERIFIED]** for specifics.

---

# E. Quick-reference dosing card (for the handbook)

| Regimen | Agent | Dose | Schedule | Bolus 5-FU? |
|---|---|---|---|---|
| mFOLFIRINOX (adjuvant) | oxali / irino / LV / 5-FU | 85 / 150(→from 180) / 400 / 2400 over 46 h mg/m² | q2w ×12 | **NO** |
| FOLFIRINOX (metastatic) | oxali / irino / LV / 5-FU | 85 / 180 / 400 / **400 bolus + 2400/46h** mg/m² | q2w | **YES** |
| NALIRIFOX (1L met.) | nal-IRI / oxali / LV / 5-FU | **50 (free base)** / 60 / 400 / 2400/46h mg/m² | d1,15 q28d | NO |
| nal-IRI/5-FU/LV (2L) | nal-IRI / LV / 5-FU | **70 free base (=80 salt)** / 400 / 2400/46h | q2w | NO |
| Gem + nab-P | nab-P then gem | 125 then 1000 mg/m² | d1,8,15 q28d | – |
| GemCap | capecitabine + gem | **830 mg/m² BID d1–21** + gem 1000 d1,8,15 | q28d ×6 | – |
| Gemcitabine | gemcitabine | 1000 mg/m² over ≤30 min | d1,8,15 q28d | – |
| S-1 (by BSA) | S-1 | 40/50/60 mg BID (<1.25 / 1.25–<1.5 / ≥1.5 m²) | 28 on/14 off | – |
| Olaparib | olaparib | 300 mg BID | continuous | – |
| Erlotinib (not TW) | erlotinib + gem | 100 mg/day PO empty stomach | daily | – |
| PERT | lipase | **40,000–50,000 u/main meal; 20,000–25,000 u/snack** | with food | – |

Antidotes/rules to memorise: **irinotecan early diarrhoea → atropine 0.25–1 mg; late diarrhoea → loperamide 4 mg then 2 mg q2h, ≤48 h**; **oxaliplatin → no cold, no ice-chip mucositis prophylaxis**; **5-FU/capecitabine → DPYD boxed warning (test before, avoid in complete deficiency)**; **capecitabine HFS → 10% urea cream**; pancreas = **Khorana 2 points (very-high-risk site)**.

---

# F. Still missing / to verify before print

- **Capecitabine pancreatic indication in Taiwan:** I found no active capecitabine licence with a pancreatic indication in the 2026-10-27 file, but I searched by generic name only — confirm no brand (e.g. Xeloda) carries it before stating GemCap is off-label in Taiwan.
- **Named DPYD variants on the 2025 US boxed-warning label:** the label deliberately names none, and no FDA-authorized test exists — do not imply a specific panel is mandated.
- **Taiwan-specific DPYD allele frequencies:** no clean Taiwanese DPYD population-frequency paper found; East-Asian data are extrapolated (Japanese: rare private LoF variants). Mark as [PARTIAL] if quoted.
- **Uridine triacetate (5-FU antidote) availability in Taiwan:** [UNVERIFIED] — not in the drug file search I ran; confirm separately.
- **NHI reimbursement criteria** for any drug above: unreachable (nhi.gov.tw down).
- **Onivyde "2003 Hermes licence" date:** press sources confirm PharmaEngine licensed from Hermes and that Merrimack acquired Hermes in 2009, but the exact original licensing year is not confirmed in a source I read — state "early 2000s" or omit the year.
- NCCN Pancreatic Adenocarcinoma is **Version 4.2026** (nccn.org reachable) and twcr.tw is reachable if the chapter later needs Taiwan incidence/NCCN category cross-checks.

---

## Critic additions

Completeness critic pass, 2026-10-29. Append only; nothing above was changed. Same tag conventions as this file. Labels were re-pulled from openFDA today (effective dates given). TFDA = licence open-data file InfoId=36 (CSV dated 2026-10-27).

### CA-0. Re-check of high-stakes numbers already in this file

| # | Item in this file | Primary source re-read | Verdict |
|---|---|---|---|
| 1 | NALIRIFOX Onivyde 50 mg/m², same dose for UGT1A1*28/*28; corticosteroid + antiemetic 30 min before | ONIVYDE USPI (openFDA effective 2025-03-03) §2.2 | **Confirmed** [VERIFIED] |
| 2 | nal-IRI 70 mg/m² free base = 80 mg/m² hydrochloride trihydrate | ONIVYDE §14 ("based on irinotecan free base (equivalent to 80 mg/m² of irinotecan as the hydrochloride trihydrate)") | **Confirmed** [VERIFIED] |
| 3 | Gem + nab-P ladder 125/1000 → 100/800 → 75/600 → stop | ABRAXANE USPI (2022-10-31) §2.6 Table 3 | **Confirmed** [VERIFIED] |
| 4 | Atropine 0.25–1 mg IV/SC; loperamide 4 mg then 2 mg q2h until diarrhoea-free ≥12 h, 4 mg q4h at night, not >48 consecutive h | CAMPTOSAR USPI (2026-05-12) §5.1 and §17 | **Confirmed** word for word [VERIFIED] |
| 5 | Capecitabine 830 mg/m² BID d1–21 q28d, max 6 cycles, with gemcitabine 1000 mg/m² d1, 8, 15 | XELODA USPI (2026-02-05) §2.5 | **Confirmed** [VERIFIED] |
| 6 | Olaparib 300 mg BID; CrCl 31–50 mL/min → 200 mg BID | LYNPARZA USPI (2025-07-10) §2.5 | **Confirmed** [VERIFIED] |
| 7 | PERT 40,000–50,000 lipase units per main meal, half with snacks | Dominguez-Muñoz 2025 [FT] | **Confirmed.** The guideline calls this a "minimum dose", and says evidence for doses below 40,000 is scarce [VERIFIED]. Computed: Creon 25000 → 2 capsules per main meal, 1 per snack. |
| 8 | mFOLFIRINOX irinotecan 180 → 150 mg/m²; no 5-FU bolus | PRODIGE 24 abstract (PMID 30575490); NCCN Guidelines for Patients 2026 ("a slow drip of fluorouracil instead of a fast injection") | **Confirmed** [VERIFIED] |
| 9 | Khorana: site 2/1 points; platelets ≥350 ×10⁹/L; Hb <10 g/dL or ESA; WBC >11 ×10⁹/L; BMI ≥35; VTE 7.1%/6.7% at score ≥3 | Khorana 2008 abstract | **Confirmed** [VERIFIED]. "Very high-risk = stomach, pancreas" is still sourced only from Mulder 2019 [PARTIAL]. |
| 10 | CASSINI pancreatic subgroup "on-treatment VTE 3.7% vs 10.1%, HR 0.35" | Vadhan-Raj 2020 abstract | **Numbers correct but incomplete.** See correction CA-1a. |
| 11 | Gemcitabine "1000 mg/m², days 1, 8, 15 of a 28-day cycle (pancreas) [L §2.4]" | Gemcitabine USPI (Avgemsi, openFDA 2026-07-27) §2.4 | **Imprecise.** See correction CA-1b. |

### CA-1. Corrections

**CA-1a. CASSINI pancreatic subgroup: primary endpoint was NOT significant** [VERIFIED; A, Vadhan-Raj 2020]
- Primary efficacy endpoint (up to day 180): **9.6% (13/135) vs 13.0% (18/138), HR 0.70 (0.34–1.43), P = .328**, which is not significant.
- On-treatment (intervention) period: 3.7% vs 10.1%, HR 0.35 (0.13–0.97), P = .034. This is the figure §22 quotes.
- Major bleeding: 1.5% vs 2.3%.
- At screening, 6.6% (24/362) of pancreatic patients **already had VTE** and were not randomised. This supports baseline imaging review before starting prophylaxis.
- Suggested handbook wording: "In CASSINI, rivaroxaban did not significantly reduce VTE in pancreatic cancer over 180 days. Benefit was seen only while patients were taking the drug."

**CA-1b. Gemcitabine single-agent label schedule** [VERIFIED; L, gemcitabine (Avgemsi) 2026-07-27 §2.4]
- The label's pancreatic schedule is **1000 mg/m² over 30 min weekly for 7 weeks, then 1 week of rest; after week 8, days 1, 8 and 15 of each 28-day cycle.**
- The days 1, 8, 15 q28d schedule from cycle 1 is the adjuvant schedule (CONKO-001, PRODIGE 24 control arm) and the gem + nab-P schedule. It is not the label's metastatic single-agent schedule. §6 should say this.
- Myelosuppression table for pancreatic cancer (label Table 4):
  - ANC ≥1,000 **and** platelets ≥100,000 → full dose
  - ANC 500–999 **or** platelets 50,000–99,999 → 75% of the dose
  - ANC <500 **or** platelets <50,000 → hold
- Permanent discontinuation: SCAR, unexplained dyspnoea or severe pulmonary toxicity, HUS or severe renal impairment, severe hepatotoxicity, capillary leak, PRES.

**CA-1c. Thromboprophylaxis in Taiwan: optional, not routine** [VERIFIED; A Chen 2018; FT Pan-Asian 2025]
- Taiwanese 4-centre cohort (Chen 2018; 838 patients on palliative chemotherapy, 2010–2016):
  - VTE occurred in **8.0% (67/838)** over a median follow-up of 7.7 months.
  - Independent predictors were **WBC >11,000/µL** and **liver metastases**.
  - VTE overall did not shorten survival, but **early-onset VTE (within 1.5 months of starting chemotherapy) was an independent negative prognostic factor**.
- The Pan-Asian ESMO guideline (2025; Taiwan Oncology Society voted) **downgraded** primary prophylaxis to "can be considered … in the absence of contraindications **[I, C]**", because VTE rates are lower in Asian patients and there is no OS benefit.
- Practical consequence: §22 should not present rivaroxaban or apixaban prophylaxis as standard for Taiwanese patients.
- NCCN Guidelines for Patients 2026 (anticoagulant choice) [VERIFIED]:
  - LMWH is preferred over warfarin for VTE treatment.
  - A DOAC "may be used if the pancreatic tumor is not growing inside of the stomach or intestine", because of the GI bleeding risk.
  - Ward check: endoscopic or CT evidence of duodenal or gastric invasion before choosing a DOAC.

### CA-2. Organ-function dosing for jaundiced, elderly or renally impaired patients (order-set ready)

Pancreatic-head cancer patients are often jaundiced, so these thresholds decide whether chemotherapy can start before biliary drainage.

| Drug | Hepatic rule (label wording) | Renal rule | Source / tag |
|---|---|---|---|
| **Liposomal irinotecan (Onivyde)** | **"There is no recommended dosage of ONIVYDE for patients with serum bilirubin above the upper limit of normal."** Applies to both NALIRIFOX and NAPOLI-1 regimens. | — | L-ONIVYDE §2.2 [VERIFIED] |
| **Irinotecan (Camptosar; in FOLFIRINOX)** | Consider a one-level starting-dose reduction for raised bilirubin; **no dose can be recommended for bilirubin >2 mg/dL**. Trials excluded bilirubin >2.0 mg/dL or transaminases >3× ULN (>5× with liver metastases). With the weekly schedule, bilirubin 1.0–2.0 mg/dL raised grade 3–4 neutropenia risk. | Use caution; **do not use in patients on dialysis** | L-CAMPTOSAR §2, §5.10, §8 [VERIFIED] |
| **Nab-paclitaxel (pancreas)** | **Not recommended** if bilirubin >1.5× ULN (moderate or severe impairment) or AST >10× ULN. Patients with bilirubin above ULN were excluded from the pancreatic trial. | — | L-ABRAXANE §2.5 Table 1 [VERIFIED] |
| **Gemcitabine** | No numeric hepatic dose rule. Check LFTs before and during treatment. Liver metastases, hepatitis, alcoholism or cirrhosis can worsen hepatic insufficiency. Stop permanently for severe hepatotoxicity. | Stop for HUS or severe renal impairment | L-gemcitabine §5.5–5.6 [VERIFIED] |
| **Oxaliplatin** | Check LFTs at baseline and before each cycle (hepatic vascular disorders). | **CrCl <30 mL/min → 65 mg/m²** | L-oxaliplatin (Gland, 2026-08-24) §2.3, §5.6 [VERIFIED] |
| **Capecitabine** | Grade 3–4 hyperbilirubinaemia: hold, and resume when ≤ grade 2 (<3× ULN) at the Table 1 dose | **CrCl 30–50 → reduce by 25%**; no dosage established for CrCl <30 | L-XELODA §2.6–2.7 [VERIFIED] |
| **Olaparib** | — | CrCl 31–50 → 200 mg BID | L-LYNPARZA §2.5 [VERIFIED] |
| FOLFIRINOX trial entry (PRODIGE 4; PRODIGE 24) | Bilirubin ≤1.5× ULN (biliary drainage allowed in PRODIGE 4) | Creatinine <120 µmol/L (PRODIGE 4) or <130 µmol/L (PRODIGE 24) | ClinicalTrials.gov NCT00112658, NCT01526135 [VERIFIED registry]; see pancreas_2 Critic additions |

Teaching sentence (derived from the rows above): "Drain the bile duct first. Onivyde needs a normal bilirubin; nab-paclitaxel is not recommended above 1.5× ULN; and the FOLFIRINOX trials required ≤1.5× ULN."

### CA-3. Onivyde administration and dose modification detail (missing from §2–3) [VERIFIED; L-ONIVYDE 2025-03-03]

- **Boxed warning** (severe neutropenia and severe diarrhoea):
  - Withhold for ANC <1,500/mm³ or neutropenic fever.
  - Do not give with bowel obstruction.
  - Withhold for grade 2–4 diarrhoea.
  - Give loperamide for late diarrhoea and atropine for early diarrhoea, of any severity.
- **NALIRIFOX (Table 1):**
  - After a grade 3–4 adverse reaction, do not resume until **ANC ≥2,000/mm³** and platelets ≥100,000/mm³. Note that this is stricter than the 1,500 threshold used elsewhere.
  - Onivyde dose steps: **50 → 40 → 32.5 → 25 mg/m² → discontinue**.
  - With each Onivyde reduction, reduce 5-FU and oxaliplatin to **80%, then 65%, then 50%** of the original dose. Leucovorin stays at the original dose.
  - Oxaliplatin may be dropped while Onivyde + 5-FU/LV continues.
  - Discontinue Onivyde for grade 3–4 hand-foot syndrome, any neurocerebellar toxicity, grade ≥2 cardiac toxicity, ILD or anaphylaxis.
- **NAPOLI-1 regimen (Table 2):** 70 → 50 → 43 mg/m² → discontinue. For *28/*28 patients not escalated: 50 → 43 → 35 → discontinue.
- **Preparation:**
  - Vial: 43 mg/10 mL (irinotecan free base).
  - Dilute in **500 mL D5W or NS** and protect from light.
  - Use within 4 h at room temperature or 24 h refrigerated.
  - Infuse over **90 min**.
  - Give Onivyde **before** oxaliplatin, leucovorin and 5-FU.
- **Nab-paclitaxel premedication** [VERIFIED; L-ABRAXANE §2.1]: no routine premedication. "Consider premedication" only after a prior hypersensitivity reaction, and do not rechallenge after a severe reaction. This contrasts with conventional paclitaxel.

### CA-4. Gem + nab-P within-cycle rules (missing from §4) [VERIFIED; L-ABRAXANE Tables 4–5]

**Day 1**
- ANC <1,500 or platelets <100,000 → delay until recovery.

**Day 8**
- ANC 500–<1,000 or platelets 50,000–<75,000 → reduce one dose level.
- ANC <500 or platelets <50,000 → withhold.

**Day 15, if day 8 doses were reduced or given in full**
- ANC 500–<1,000 or platelets 50,000–<75,000 → one level below day 8.
- ANC <500 or platelets <50,000 → withhold.

**Day 15, if day 8 doses were withheld**
- ANC ≥1,000 or platelets ≥75,000 → one level below day 1.
- ANC 500–<1,000 or platelets 50,000–<75,000 → two levels below day 1.
- ANC <500 or platelets <50,000 → withhold.

**Other adverse reactions**
- Grade 3–4 febrile neutropenia: withhold both drugs until fever resolves and ANC ≥1,500, then resume one level lower.
- Grade 2–3 cutaneous toxicity: one level lower; stop if it persists.
- Grade 3 mucositis or diarrhoea: withhold until ≤ grade 1, then one level lower.

### CA-5. Post-pancreatectomy complications (ISGPS definitions; ward-critical, previously absent)

| Complication | Definition and grading | Tag |
|---|---|---|
| **Postoperative pancreatic fistula (POPF), ISGPS 2016** | Drain output of **any measurable volume** with **amylase >3× the institutional upper limit of normal serum amylase**, *plus* a clinically relevant condition. The old "grade A" is now a **biochemical leak** and is no longer counted as a fistula. **Grade B**: change in postoperative management, with drains left in place for >3 weeks or repositioned endoscopically or percutaneously. **Grade C**: reoperation, single or multiple organ failure, and/or death attributable to the POPF. | [VERIFIED; A Bassi 2017] |
| | "On or after postoperative day 3" timing: stated in secondary sources, not in the abstract | [PARTIAL] |
| | A 2024 corrigendum exists (Surgery 176(3):988–989, PMID 38926000); content not read | — |
| **Delayed gastric emptying (DGE), ISGPS 2007** | Inability to return to a standard diet by the end of the first postoperative week, including prolonged nasogastric intubation; grades A, B and C by clinical impact. | [VERIFIED; A Wente 2007] |
| | Grade cut-offs: **A**, unable to tolerate solid oral intake by POD 7; **B**, by POD 14; **C**, by POD 21. Grade A is not clinically relevant. Another series quotes the B threshold as NGT >7 days or reinsertion after POD 7. | [PARTIAL; secondary: Jiménez-Romero 2025 FT and others] |
| **Post-pancreatectomy haemorrhage (PPH), ISGPS 2007** | Defined by **onset** (early ≤24 h vs late >24 h after the end of surgery), **location** (intraluminal vs extraluminal) and **severity** (mild vs severe); graded A–C by onset, site, severity and clinical impact. | [VERIFIED; A Wente 2007] |
| | Grade C involves embolisation, endoscopy or relaparotomy | [PARTIAL; secondary] |
| **Chyle leak, ISGPS 2017** | **Milky fluid** from a drain, drain site or wound **on or after POD 3**, with **triglycerides ≥110 mg/dL (≥1.2 mmol/L)**. Occurs in up to 10% of resections. **A**: oral dietary restriction only. **B**: longer stay, nasoenteral nutrition with dietary restriction, TPN, octreotide, drains kept or new percutaneous drains. **C**: more invasive in-hospital treatment, ICU or death. | [VERIFIED; A Besselink 2017] |
| **Pasireotide for POPF prevention** | Single-centre RCT, n = 300. Pasireotide 900 µg SC BID from the morning of surgery for 7 days (14 doses). Grade ≥3 fistula, leak or abscess **9% vs 21%, RR 0.44 (0.24–0.78), P = .006**. Benefit was seen after both PD and distal pancreatectomy. | [VERIFIED; A Allen 2014] |
| **Taiwan licence status** | Pasireotide (Signifor 欣瘤伏, 衛署藥輸字第026093–026095號) is licensed for **Cushing's disease only**, so POPF use is off-label. **Octreotide** (Sandostatin 善得定 衛署藥輸字第017873號 and generics, e.g. 霖肽 衛部藥製字第061437號) has a Taiwan indication that explicitly includes **「預防胰臟手術後的併發症」**. | [VERIFIED; TFDA] |

Nursing cue (editorial, not sourced): drain colour and amylase on schedule; milky output → send triglycerides; a "sentinel" bleed from a drain or the GI tract after the first post-op day → escalate for urgent CT angiography.

### CA-6. TFDA look-ups that close items in §F (file dated 2026-10-27) [VERIFIED; TFDA]

- **Uridine triacetate (Vistogard): 0 records**, so it is not licensed in Taiwan. Special-import availability is [UNVERIFIED].
- **Capecitabine:** 5 active licences, **including Xeloda 衛署藥輸字第022409號**; none mention 胰. Xeloda's Taiwan indications are breast, colorectal and gastric only. **GemCap for pancreatic cancer is off-label in Taiwan.** This closes the first bullet of §F.
- **Creon 25000 / 40000** (衛部藥輸字第027421/027422號) re-confirmed for PEI (CF, chronic pancreatitis, pancreatic surgery); Creon 10000 (027423) is licensed as a digestive aid only.

### CA-7. Still unverified after this pass

- **Emetogenic classification of FOLFIRINOX / NALIRIFOX: [UNVERIFIED].**
  - The ASCO 2020 antiemetic update abstract does not classify these regimens, and the NCCN Antiemesis PDF was not opened.
  - A Japanese FOLFIRINOX/FOLFOXIRI series (Tokushima, 2026) used "standard triple antiemetic prophylaxis" (NK1 + 5-HT3 + dexamethasone) [PARTIAL; practice only].
  - The Onivyde label requires a corticosteroid + antiemetic before each dose.
- G-CSF primary prophylaxis rules for FOLFIRINOX: not checked.
- Post-ERCP pancreatitis prophylaxis (rectal NSAID): not checked.

### CA-8. References for these additions (APA 7)

- Allen, P. J., Gönen, M., Brennan, M. F., Bucknor, A. A., Robinson, L. M., Pappas, M. M., Carlucci, K. E., D'Angelica, M. I., DeMatteo, R. P., Kingham, T. P., Fong, Y., & Jarnagin, W. R. (2014). Pasireotide for postoperative pancreatic fistula. *The New England Journal of Medicine, 370*(21), 2014–2022. https://doi.org/10.1056/NEJMoa1313688 — PMID 24849084
- Bassi, C., Marchegiani, G., Dervenis, C., Sarr, M., Abu Hilal, M., Adham, M., Allen, P., Andersson, R., Asbun, H. J., Besselink, M. G., Conlon, K., Del Chiaro, M., Falconi, M., Fernandez-Cruz, L., Fernandez-Del Castillo, C., Fingerhut, A., Friess, H., Gouma, D. J., Hackert, T., . . . Buchler, M. (2017). The 2016 update of the International Study Group (ISGPS) definition and grading of postoperative pancreatic fistula: 11 years after. *Surgery, 161*(3), 584–591. https://doi.org/10.1016/j.surg.2016.11.014 — PMID 28040257 (corrigendum: *Surgery*, 2024, *176*(3), 988–989, https://doi.org/10.1016/j.surg.2024.05.043, PMID 38926000; not read)
- Besselink, M. G., van Rijssen, L. B., Bassi, C., Dervenis, C., Montorsi, M., Adham, M., Asbun, H. J., Bockhorn, M., Strobel, O., Büchler, M. W., Busch, O. R., Charnley, R. M., Conlon, K. C., Fernández-Cruz, L., Fingerhut, A., Friess, H., Izbicki, J. R., Lillemoe, K. D., Neoptolemos, J. P., . . . Gouma, D. J. (2017). Definition and classification of chyle leak after pancreatic operation: A consensus statement by the International Study Group on Pancreatic Surgery. *Surgery, 161*(2), 365–372. https://doi.org/10.1016/j.surg.2016.06.058 — PMID 27692778
- Chen, J.-S., Hung, C.-Y., Chang, H., Liu, C.-T., Chen, Y.-Y., Lu, C.-H., Chang, P.-H., Hung, Y.-S., & Chou, W.-C. (2018). Venous thromboembolism in Asian patients with pancreatic cancer following palliative chemotherapy: Low incidence but a negative prognosticator for those with early onset. *Cancers, 10*(12), Article 501. https://doi.org/10.3390/cancers10120501 — PMID 30544670; PMCID PMC6315992
- Jiménez-Romero, C., de Juan Lerma, A., Marcacuzco Quinto, A., Caso Maestro, O., Alonso Murillo, L., Rioja Conde, P., & Justo Alonso, I. (2025). Risk factors for delayed gastric emptying after pancreatoduodenectomy: A 10-year retrospective study. *Annals of Medicine, 57*(1), Article 2453076. https://doi.org/10.1080/07853890.2025.2453076 — PMID 39817563; PMCID PMC11740295 (secondary source for DGE grade cut-offs)
- Tai, D., Conroy, T., Lee, J. J. X., Chee, C. E., Hao, C. Y., Wijaya, I., Aggarwal, S., Ueno, M., Jeung, H. C., Hashim, N. M., Tan Chun Bing, J., Chen, L. T., Korphaisarn, K., Tanasanvimon, S., Chou, W. C., Cargullo, E., Muin, N. F. A., Lee, M. A., Ohba, A., . . . Ducreux, M. (2025). Pan-Asian adapted ESMO Clinical Practice Guidelines for the diagnosis, treatment and follow-up of patients with pancreatic cancer. *ESMO Open, 10*(10), Article 105826. https://doi.org/10.1016/j.esmoop.2025.105826 — PMID 41067164; PMCID PMC12546840
- Vadhan-Raj, S., et al. (2020) and Dominguez-Muñoz, J. E., et al. (2025): full references in §22 and §20 above.
- Wente, M. N., Bassi, C., Dervenis, C., Fingerhut, A., Gouma, D. J., Izbicki, J. R., Neoptolemos, J. P., Padbury, R. T., Sarr, M. G., Traverso, L. W., Yeo, C. J., & Büchler, M. W. (2007). Delayed gastric emptying (DGE) after pancreatic surgery: A suggested definition by the International Study Group of Pancreatic Surgery (ISGPS). *Surgery, 142*(5), 761–768. https://doi.org/10.1016/j.surg.2007.05.005 — PMID 17981197
- Wente, M. N., Veit, J. A., Bassi, C., Dervenis, C., Fingerhut, A., Gouma, D. J., Izbicki, J. R., Neoptolemos, J. P., Padbury, R. T., Sarr, M. G., Yeo, C. J., & Büchler, M. W. (2007). Postpancreatectomy hemorrhage (PPH): An International Study Group of Pancreatic Surgery (ISGPS) definition. *Surgery, 142*(1), 20–25. https://doi.org/10.1016/j.surg.2007.02.001 — PMID 17629996
- US FDA prescribing information read via openFDA `drug/label`, 2026-10-29:
  - ONIVYDE (Ipsen; effective 2025-03-03)
  - ABRAXANE (Abraxis; 2022-10-31)
  - CAMPTOSAR (Pharmacia & Upjohn; 2026-05-12)
  - XELODA (H2-Pharma; 2026-02-05)
  - LYNPARZA (AstraZeneca; 2025-07-10)
  - gemcitabine injection AVGEMSI (Avyxa; 2026-07-27)
  - oxaliplatin injection (Gland; 2026-08-24)
- National Comprehensive Cancer Network. (2026). *NCCN Guidelines for Patients: Pancreatic cancer* (based on NCCN Guidelines v2.2026, April 22, 2026). https://www.nccn.org/patients/guidelines/content/PDF/pancreatic-patient.pdf
