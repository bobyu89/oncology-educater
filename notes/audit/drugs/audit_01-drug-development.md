# Audit log: handbook/05-drugs/01-drug-development.md

Auditor run 2026-11-11. Only this chapter file was edited. Lint after edits: `0 error, 0 warn`.

## Fixes (section | what was wrong | what it is now | source)

1. §1 timeline, 1942 row | "第一次證明全身性藥物能讓腫瘤縮小，也第一次看到骨髓抑制與復發": an unsupported "first systemic drug" claim (the source only claims proof of concept for intravenous chemotherapy; marrow suppression from mustard was already described in 1919, as the chapter itself says) | "第一次用靜脈化療讓腫瘤縮小，同時看到骨髓抑制與復發後抗藥" | Christakis 2011 full text (PMC3117414): "proof of concept that intravenous chemotherapy resulted in tumor regression, but that resistance occurred after multiple dosages".
2. §1.1 Nitrogen mustard paragraph | The Bari sentence was cited only to Falzone 2018, which never names Bari or Italy (it says "in December 1943, the John Harvey ship ... was bombed", bone marrow aplasia in those exposed) | Sentence reworded ("義大利巴里港（Bari）遭空襲，船上載運的芥子氣外洩") and co-cited to Turner & Sapp 2026; reference entry added | Falzone 2018 full text (PMC6243123); Turner & Sapp 2026, PubMed PMID 41223052 (abstract: 1943 air raid on Bari, Italy, release of mustard gas).
3. §2.3 accelerated approval | CodeBreaK 200 was presented only as "PFS 優於 docetaxel", which reads as a successful confirmation in a section about confirmatory trials | Added: OS not significantly different, and ODAC (October 2023) recommended against conversion to regular approval; cited Wei et al. 2026; reference entry added | de Langen 2023 abstract (PFS 5.6 vs 4.5, HR 0.66 confirmed); Wei et al. 2026, PubMed PMID 41665865 abstract.
4. §3.1 endpoint table, pCR row | KEYNOTE-522 "64.8% 對 51.2%" given without saying it is the first interim analysis of the first 602 patients; the breast chapter (4.6, line 749) uses the all-ITT 63.0% vs 55.6% and explicitly warns not to mix the two | Labelled "第一次期中分析（前 602 人）" and linked to breast chapter 4.6 for the all-population figure | Schmid 2020 abstract (PMID 32101663); handbook/03-breast-cancer.md §4.6.
5. §4.2 closing paragraph (protein degraders) | "蛋白降解劑的命名方式 WHO 還在制定" and "-deg- 提示它是降解劑" were attributed to Stem Book 2024, which contains neither statement (it only lists vepdegestrant under -estrant and bavdegalutamide under -lutamide) | Reworded: no formal stem in Stem Book 2024; the WHO pre-stem working document (March 2024) gives the scheme "-deg- (+ vowel) + target stem" (-deg-estrant, -dega-lutamide); cited and reference entry added | WHO Stem Book 2024 PDF (lines for -estrant, -lutamide); WHO INN Working Document 23.574 rev., 8 March 2024, "Bifunctional proteolysis-targeting substances concept".
6. §7.1 third bullet (Sequist) | "所有腫瘤都保留原本的 EGFR 突變，另外多了抗藥的變化" implies every tumour had an added resistance alteration; 15 of 37 had none identified | "部分另外出現已知的抗藥變化（例如 T790M、MET 放大）" | Sequist 2011 abstract and full text (PMC3132801).
7. §8.1 WARNING box | "多數嚴重的給藥錯誤，在「處方」這一步就看得出來": unsourced quantitative claim | "許多嚴重的給藥錯誤…" | no source supports "most"; softened.
8. §11 Sartor et al. 2021 | 20 named authors were written as 19 + ellipsis + last (APA 7 uses the ellipsis only from 21 authors; nobody was actually omitted) | All 20 listed with "&" before Krause | PubMed PMID 34161051 (20 named authors + VISION Investigators).
9. §11 Rosenberg et al. 1965 | Issue number missing | "*Nature, 205*(4972), 698–699" | Crossref DOI 10.1038/205698a0.
10. §11 new entries (needed by fixes 2, 3, 5) | — | Programme on International Nonproprietary Names (2024, March 8); Turner & Sapp (2026); Wei et al. (2026) | WHO PDF fetched; PubMed metadata for PMID 41223052 and 41665865.

## Writer's flagged items: outcome

- Approval years: confirmed against openFDA Drugs@FDA original-approval records: rituximab BLA103705 1997-11-26; trastuzumab BLA103792 1998-09-25; bevacizumab BLA125085 2004-02-26; ipilimumab BLA125377 2011-03-25. Also pembrolizumab 2014-09-04, larotrectinib 2018-11-26, sotorasib 2021-05-28, osimertinib 2015-11-13. No change needed.
- Farber 1948: five authors and "(aminopterin)" in title confirmed by Crossref. Goodman 1946: six authors confirmed by the PubMed record of the 1984 JAMA landmark reprint (PMID 6368885); volume 132(3), 126–132 by PubMed/Crossref. Gilman & Philips 1946 confirmed by PubMed and Crossref. Piaggio 2012 with CONSORT Group as collective author matches PubMed/Crossref.
- FDA 2018 entries: every "Food and Drug Administration, 2018" citation refers to the Step 3 page content (phase sizes, durations, percentages, IND contents, 30 days) and every "Oncology Center of Excellence et al., 2018" citation refers to the endpoints guidance (definitions, accelerated approval, NI trials). Both documents were fetched and matched. FDA 2023 page date and four one-line descriptions matched.
- INN stems (§4): all 25 stem definitions and all example drugs in 4.2, the old and new antibody schemes in 4.3, payload stems in 4.4 and "raludotatug deruxtecan" were found in the Stem Book 2024 text. There is no "-degrant" stem; vepdegestrant is under -estrant. 64th Consultation April 2017 (Parren 2017), 879 -mab INN and 73rd Consultation October 2021 (Guimaraes Koch 2022 abstract; WHO executive summary INN Working Doc. 21.533: 19–22 October 2021) confirmed.
- Worked-example trials: FLAURA, KEYNOTE-189, PACIFIC, MPACT, DESTINY-Breast04, KATHERINE, PERSEPHONE, AURA3, CodeBreaK 100/200 all match the abstracts and the lung, pancreatic and breast chapters. KEYNOTE-522 needed the label in fix 4. KATHERINE here is the 3-year result (2019); the breast chapter uses the 7-year update. Both are correctly labelled.
- RECIST 1.1 (checked against the guideline PDF from EORTC) and iRECIST (PMC5648544): all thresholds, the two worked calculations and Q6/Q7 are correct.

## Quiz

All 15 items solved independently; keys A/B/C/D as printed are the single best answers and the distractors are clearly wrong. No change. Format unchanged.

## Drug cards

None by design. Nothing added.

## Taiwan / NHI

No specific licence or reimbursement claim is made in this chapter; it only points to the cancer chapters. No 待核對 box needed.

## Problems seen in other files (not edited)

- handbook/05-drugs/02-cytotoxic-chemotherapy.md line 79: "Bari 港" is co-cited to Falzone 2018, which does not name Bari (it names the ship and December 1943) and calls the cargo "nitrogen mustard bombs". Turner & Sapp 2026 is also cited there, so the sentence stands, but Falzone should not be the support for the place name or the agent.
- handbook/05-drugs/02-cytotoxic-chemotherapy.md line 1018: Rosenberg 1965 reference lacks the issue number (4972). Cosmetic.
- handbook/01-lung-cancer.md line 416: CodeBreaK 200 is given as PFS only. Not an error, but the OS result (no significant difference) is absent.
- No factual disagreement found between this chapter and handbook/0[1-4]-*.md or handbook/00-shared/*.md for the shared trials and rules.

## Could not check, and why

- Full text not open-access, so the check was at abstract level (every cited number is in the abstract): Slamon 2001, Druker 2001, Hurwitz 2004, McLaughlin 1998, Kobayashi 2005, Soria 2018, Ramalingam 2020, Gandhi 2018, Antonia 2017, von Minckwitz 2019, Schmid 2020, Cortazar 2014, Prasad 2015, Assmann 2000, Temel 2010, Engelman 2007, Beaver 2018, de Langen 2023, Cohen 2002, Chuk 2017, O'Leary 2019, Marcus 2019, Scott 2019, Fourie Zirkelbach 2022, Neuss 2016, DeVita 1980, Fisher 1975, Bonadonna 1976, Einhorn 1977, Nowell 1976, Goldie & Coldman 1979, Gottesman 2002, DeVita & Chu 2008, Giobbie-Hurder 2013.
- No abstract and no full text reachable, so only bibliographic data were confirmed: Goodman 1946, Gilman & Philips 1946, Farber 1948, Rosenberg 1965 and 1969, DeVita 1970, Oken 1982. The chapter's statements that cite them are either their titles or are also supported by Christakis 2011, Falzone 2018 or DeVita 1980.
- CodeBreaK 200 overall-survival figures (HR and medians) were not read in the primary paper; the added sentence therefore states only "no significant difference", as in Wei et al. 2026. The regulatory status of sotorasib after October 2023 was not checked.
- Whether WHO has made "-deg-" an official stem after March 2024 (later pre-stem lists or a later Stem Book) was not checked; the text is dated to the 2024 documents.
- PubMed stores study-group names as an empty collective author, so group names (for example PACIFIC Investigators) could not be compared; the reference list follows the handbook's convention of omitting them.
