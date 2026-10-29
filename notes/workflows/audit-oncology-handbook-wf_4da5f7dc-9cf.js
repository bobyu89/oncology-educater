export const meta = {
  name: 'audit-oncology-handbook',
  description: 'Adversarially audit lung + shared chapters for clinical accuracy, verify each finding with two lenses, apply confirmed fixes',
  phases: [
    { title: 'Review', detail: 'section reviewers + cross-file consistency + gap critics' },
    { title: 'Verify', detail: 'two independent lenses per finding' },
    { title: 'Fix', detail: 'one fixer per file applies confirmed fixes' },
  ],
}

const ROOT = '/home/user/oncology-educater'
const RESEARCH = '/tmp/claude-0/-home-user-oncology-educater/6a66dc7f-55e5-547a-b95f-33d6978992bf/scratchpad/research'
const LUNG = 'handbook/01-lung-cancer.md'
const S1 = 'handbook/00-shared/01-chemo-basics.md'
const S2 = 'handbook/00-shared/02-oncologic-emergencies.md'
const S3 = 'handbook/00-shared/03-supportive-care.md'
const S4 = 'handbook/00-shared/04-irae.md'

const UNITS = [
  { file: LUNG, lines: '1-88', label: 'lung: header, 0 速查卡, 1 流病與篩檢' },
  { file: LUNG, lines: '89-205', label: 'lung: 2 病理與分子標記, 3 診斷與分期' },
  { file: LUNG, lines: '206-252', label: 'lung: 4.1 I–II 期, 4.2 III 期' },
  { file: LUNG, lines: '253-326', label: 'lung: 4.3 IV 期 NSCLC' },
  { file: LUNG, lines: '327-381', label: 'lung: 4.4 SCLC, 4.5 台灣藥證' },
  { file: LUNG, lines: '382-468', label: 'lung: 5 常用處方' },
  { file: LUNG, lines: '469-547', label: 'lung: 6 副作用處置' },
  { file: LUNG, lines: '548-705', label: 'lung: 7 專師實務, 8 腫瘤急症, 9 健保架構' },
  { file: LUNG, lines: '706-936', label: 'lung: 10 個案, 11 自我測驗' },
  { file: S1, lines: '1-206', label: 'chemo-basics: 1–6' },
  { file: S1, lines: '207-443', label: 'chemo-basics: 7–11' },
  { file: S2, lines: '1-225', label: 'emergencies: FN, TLS, SVC' },
  { file: S2, lines: '226-530', label: 'emergencies: MSCC 到 CRS/ICANS 與測驗' },
  { file: S3, lines: '1-239', label: 'supportive: CINV, G-CSF, 疼痛, 黏膜炎, 腹瀉, 便秘' },
  { file: S3, lines: '240-421', label: 'supportive: VTE, 骨保護劑, 緩和照護, 測驗' },
  { file: S4, lines: '1-109', label: 'irAE: 機轉, 基線, 通用分級, 類固醇配套' },
  { file: S4, lines: '110-376', label: 'irAE: 各器官, 二線免疫抑制, rechallenge, 衛教, 測驗' },
]

const CONTEXT = `Context: ${ROOT} is a Traditional-Chinese study handbook for a Taiwanese oncology nurse practitioner (專科護理師) trainee, used both on the ward and for the 專師甄審 exam. Medical terms stay in English. Today is 2026-10-29. docs/STYLE_GUIDE.md defines conventions (GitHub alert callouts with a bold topic first line, APA 7 citations, no emoji). The NHI (健保) section 9 of the lung chapter is intentionally a pending skeleton; do not report it as missing content.
Verified research notes you may reuse as sources (each fact there was checked against PubMed / FDA labels / official Taiwan sources, with PMIDs): ${RESEARCH}/A_taiwan_guidelines_staging.md (staging, NCCN versions, CTCAE, Taiwan epidemiology, LDCT, FDA/TFDA approvals), ${RESEARCH}/B1_nsclc_targeted_trials.md and ${RESEARCH}/B2_nsclc_io_sclc_trials.md (trial data).
Tools: load PubMed tools with ToolSearch (query "pubmed"); WebSearch and WebFetch are available (openFDA / DailyMed labels, guideline papers). www.nhi.gov.tw and www.hpa.gov.tw are not reachable. Do not edit any file.`

const FINDINGS = {
  type: 'object',
  properties: {
    findings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          file: { type: 'string', description: 'repo-relative path' },
          quote: { type: 'string', description: 'verbatim text copied from the file that contains the problem; short but unique in the file' },
          problem: { type: 'string' },
          category: { type: 'string', enum: ['factual_error', 'outdated', 'unsupported_claim', 'unsafe_or_ambiguous', 'calculation_error', 'internal_inconsistency', 'citation_error', 'taiwan_context'] },
          severity: { type: 'string', enum: ['critical', 'major', 'minor'] },
          evidence: { type: 'string', description: 'source(s) with PMID/DOI/URL and what they actually say' },
          proposed_fix: { type: 'string', description: 'full replacement text for quote, same language/style, keeping Markdown table/callout syntax intact' },
          confidence: { type: 'string', enum: ['high', 'medium', 'low'] },
        },
        required: ['file', 'quote', 'problem', 'category', 'severity', 'evidence', 'proposed_fix', 'confidence'],
      },
    },
    claims_checked: { type: 'number' },
    notes: { type: 'string' },
  },
  required: ['findings', 'claims_checked', 'notes'],
}

const VERDICT = {
  type: 'object',
  properties: {
    is_error: { type: 'boolean', description: 'true only if the ORIGINAL text is actually wrong, outdated, unsafe or misleading' },
    fix_correct: { type: 'boolean', description: 'true if the proposed fix is itself accurate and safe as written' },
    revised_fix: { type: 'string', description: 'a corrected replacement for the original quote if the proposed fix is not right; empty string otherwise' },
    reasoning: { type: 'string' },
    sources: { type: 'string' },
  },
  required: ['is_error', 'fix_correct', 'revised_fix', 'reasoning', 'sources'],
}

const GAPS = {
  type: 'object',
  properties: {
    gaps: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          file: { type: 'string' },
          section: { type: 'string' },
          gap: { type: 'string' },
          why_it_matters: { type: 'string' },
          suggested_content: { type: 'string', description: 'concrete outline of what to add, with sources' },
          priority: { type: 'string', enum: ['high', 'medium', 'low'] },
        },
        required: ['file', 'section', 'gap', 'why_it_matters', 'suggested_content', 'priority'],
      },
    },
  },
  required: ['gaps'],
}

function reviewPrompt(u) {
  return `${CONTEXT}

Your unit: ${u.file}, lines ${u.lines} (${u.label}). Read those lines (and the surrounding file if needed for context).

Task: act as a meticulous clinical fact-checker. Extract every checkable clinical claim in your unit — drug doses and schedules, thresholds (lab cut-offs, grades, timings), recommendations and their conditions, trial results (medians, HRs, percentages), staging rules, epidemiology numbers, guideline/label statements, quiz answers and their explanations, and worked calculations (recompute every calculation). Check each against primary sources (drug labels, guideline papers, PubMed abstracts, the verified research notes).

Report ONLY substantive problems: wrong or outdated facts, numbers that disagree with the source, unsafe or ambiguous dosing/management advice, quiz items whose keyed answer or explanation is wrong or arguable, calculation errors, claims stated as fact without support, and Taiwan-context errors. Do not report style, wording preferences, or things that are correct but could be phrased differently. Severity: critical = could plausibly harm a patient if followed (dose, contraindication, missed emergency step); major = a wrong fact or number a learner would memorize or be tested on; minor = imprecise statement, missing important caveat, small numeric drift.

For each finding: quote must be copied verbatim from the file (unique within the file), proposed_fix must be a drop-in replacement for that exact quote in Traditional Chinese with English medical terms, preserving Markdown table pipes / callout '> ' prefixes. Cite the evidence precisely. If everything in your unit is correct, return an empty findings array — an empty result is a valid, useful answer.`
}

const consistencyPrompt = `${CONTEXT}

Task: cross-file consistency check across ${LUNG}, ${S1}, ${S2}, ${S3}, ${S4}. Find places where two files (or two parts of one file) state different values or advice for the same thing — e.g. steroid doses for the same irAE grade, PJP prophylaxis thresholds, FN definitions and antibiotic timing, SIADH correction limits, dexamethasone doses for brain metastases, pemetrexed premedication, CTCAE version statements, carboplatin cap, antiemetic regimens, G-CSF thresholds, extravasation management, Schoenfeld osimertinib data. For each real contradiction decide which statement is correct per primary sources and report a finding against the WRONG location (quote verbatim from that file, proposed_fix aligned with the correct one). Only report genuine contradictions or a statement that is wrong; not mere differences in level of detail. Empty findings is a valid result.`

function gapPrompt(scope) {
  return `${CONTEXT}

Task: completeness critic for ${scope}. Read the chapter(s) in full. Identify the most important topics a Taiwanese oncology NP trainee would need on the ward or in the 專師甄審 exam that are missing or too thin — e.g. missing high-yield toxicities, missing nursing assessments, missing common orders, missing Taiwan-specific practice, missing exam-classic facts. Do not list the NHI section 9 (pending by design). Give at most 10 gaps, prioritized, each with a concrete outline of what to add and sources. Empty is acceptable if coverage is genuinely complete.`
}

function verifyPrompt(f, lens) {
  const lensText = lens === 'source'
    ? 'LENS: primary-source check. Independently find the primary source (drug label, guideline document, the trial paper on PubMed). Decide from the source itself whether the original text is wrong. Do not rely on the reviewer\'s evidence summary — re-check it.'
    : 'LENS: skeptical clinician. Your job is to try to REFUTE the reviewer: is the original statement actually acceptable under current guidelines (NCCN/ESMO/ASCO/MASCC), the drug label, or reasonable Taiwanese practice, perhaps with a different but valid convention? If after checking you are not convinced the original is wrong, set is_error=false. Also scrutinize the proposed fix for new errors.'
  return `${CONTEXT}

A reviewer flagged a possible problem in ${f.file}.
Original text (verbatim): """${f.quote}"""
Reviewer's problem statement: ${f.problem}
Category/severity: ${f.category} / ${f.severity}
Reviewer's evidence: ${f.evidence}
Proposed replacement: """${f.proposed_fix}"""

${lensText}

Read the surrounding lines in the file for context. Return is_error (is the ORIGINAL text really wrong/outdated/unsafe/misleading?), fix_correct (is the proposed replacement accurate and safe as written, and a valid drop-in for the quote?), and if the proposed fix is not right but the original is wrong, put a corrected drop-in replacement in revised_fix (Traditional Chinese, English medical terms, Markdown syntax preserved).`
}

phase('Review')
const reviewAndVerify = pipeline(
  UNITS,
  u => agent(reviewPrompt(u), { label: `review:${u.label}`, phase: 'Review', schema: FINDINGS }),
  (res, u) => parallel((res ? res.findings : []).map(f => () =>
    parallel([
      () => agent(verifyPrompt(f, 'source'), { label: `verify-src:${u.label}`, phase: 'Verify', schema: VERDICT }),
      () => agent(verifyPrompt(f, 'skeptic'), { label: `verify-skeptic:${u.label}`, phase: 'Verify', schema: VERDICT }),
    ]).then(vs => ({ f, vs }))
  )).then(items => ({ unit: u.label, checked: res ? res.claims_checked : 0, notes: res ? res.notes : 'reviewer failed', items }))
)

const consistency = agent(consistencyPrompt, { label: 'consistency', phase: 'Review', schema: FINDINGS })
  .then(res => parallel((res ? res.findings : []).map(f => () =>
    parallel([
      () => agent(verifyPrompt(f, 'source'), { label: 'verify-src:consistency', phase: 'Verify', schema: VERDICT }),
      () => agent(verifyPrompt(f, 'skeptic'), { label: 'verify-skeptic:consistency', phase: 'Verify', schema: VERDICT }),
    ]).then(vs => ({ f, vs }))
  )).then(items => ({ unit: 'consistency', checked: res ? res.claims_checked : 0, notes: res ? res.notes : 'failed', items })))

const gapsLung = agent(gapPrompt(`the lung cancer chapter ${LUNG}`), { label: 'gaps:lung', phase: 'Review', schema: GAPS })
const gapsShared = agent(gapPrompt(`the shared chapters ${S1}, ${S2}, ${S3}, ${S4}`), { label: 'gaps:shared', phase: 'Review', schema: GAPS })

const [unitResults, consResult, gl, gs] = await Promise.all([reviewAndVerify, consistency, gapsLung, gapsShared])
const allUnits = unitResults.filter(Boolean).concat(consResult ? [consResult] : [])

const confirmed = [], disputed = [], rejected = []
for (const u of allUnits) {
  for (const it of u.items.filter(Boolean)) {
    const [a, b] = it.vs
    if (!a || !b) { disputed.push({ ...it.f, why: 'a verifier failed', a, b }); continue }
    const votes = [a.is_error, b.is_error].filter(Boolean).length
    if (votes === 2) {
      let fix = null
      if (a.fix_correct) fix = it.f.proposed_fix
      else if (a.revised_fix) fix = a.revised_fix
      else if (b.fix_correct) fix = it.f.proposed_fix
      else if (b.revised_fix) fix = b.revised_fix
      if (fix) confirmed.push({ file: it.f.file, quote: it.f.quote, replacement: fix, problem: it.f.problem, severity: it.f.severity, evidence: it.f.evidence, src_reason: a.reasoning, skeptic_reason: b.reasoning })
      else disputed.push({ ...it.f, why: 'both agree error but no agreed fix', a, b })
    } else if (votes === 1) {
      disputed.push({ ...it.f, why: 'verifiers split', a, b })
    } else {
      rejected.push({ file: it.f.file, quote: it.f.quote, problem: it.f.problem })
    }
  }
}
log(`confirmed ${confirmed.length}, disputed ${disputed.length}, rejected ${rejected.length}`)

phase('Fix')
const byFile = {}
for (const c of confirmed) (byFile[c.file] = byFile[c.file] || []).push(c)
const fixResults = await parallel(Object.keys(byFile).map(file => () => agent(
  `You are applying verified corrections to ${ROOT}/${file}. Each item below was confirmed as an error by two independent verifiers. Apply every item with the Edit tool: replace the verbatim quote with the replacement. Rules: change nothing else; keep Markdown table pipes, callout '> ' prefixes and list structure valid; if a quote no longer matches exactly (e.g. an earlier item already changed nearby text, or whitespace differs), locate the same passage and apply the intended correction carefully; if two items overlap, merge them into one coherent edit. Do not run the site build. Do not commit.

Items (JSON):
${JSON.stringify(byFile[file].map(c => ({ quote: c.quote, replacement: c.replacement, problem: c.problem })), null, 1)}

Return a short report: for each item, applied / merged / not applied (with reason).`,
  { label: `fix:${file}`, phase: 'Fix' }
)))

return {
  confirmed,
  disputed,
  rejected,
  unit_notes: allUnits.map(u => ({ unit: u.unit, checked: u.checked, notes: u.notes })),
  fix_reports: Object.keys(byFile).map((f, i) => ({ file: f, report: fixResults[i] })),
  gaps: { lung: gl ? gl.gaps : null, shared: gs ? gs.gaps : null },
}
