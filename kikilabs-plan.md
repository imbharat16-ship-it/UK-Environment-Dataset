# KikiLabs Plan — UK Environment Dataset Digital Twin Experiment

**Project:** Plastic Packaging in People's Lives (PPiPL) · Consumer Insights: Micro Insights  
**Dataset:** UK Data Service study 857315 · [`857315_data/`](857315_data/)  
**Schema reference:** [`DATA_SCHEMA.md`](DATA_SCHEMA.md)  
**Date:** June 2026

---

## Executive summary

This document defines how KikiLabs validates its **interview-grounded digital twin** workflow on real UK ethnographic research data.

**Primary simulation target:** Interview 2 (the closing interview). Interview 1 seeds the twin; diary batches and follow-ups are added **in study order**, one at a time. After each addition we re-run the twin against Interview 2 and measure simulation accuracy. The question is whether observed behaviour and mid-study conversations make the twin better at predicting what the participant actually said at the end.

Twins that pass release criteria can then run follow-on packaging scenarios on the same cohort without new fieldwork.

- **Working set:** 17 P0 participants (complete records only)
- **Phased execution:** Pilot (8) → Confirm (5) → Extend (4)
- **Primary metric:** Interview 2 simulation accuracy (BERTScore F1) at each calibration step
- **Out of scope (v1):** Scenario simulation with no ground truth in the dataset

**Research question:** As we sequentially add diary entries and follow-ups to the twin in the order they were collected, does Interview 2 simulation accuracy improve — and at which step does observed behaviour start to matter?

---

## About the source study

**Plastic Packaging in People's Lives (PPiPL)** is a UKRI-funded programme to help policymakers and industry close the gap between what consumers *say* about plastic packaging and what they *actually do*.

This deposit (**Consumer Insights: Micro Insights**, study 857315) is the consumer ethnography slice: 27 UK households tracked over 5–6 weeks (Oct 2021 – Sep 2022) via two in-depth interviews, weekly diaries, photo-elicitation follow-ups, and optional home/shopping visits. It captures the everyday lifecycle of food plastic packaging as qualitative text in Word documents.

We use **17 P0 participants** with complete file sets. Full inventory: [`DATA_SCHEMA.md`](DATA_SCHEMA.md).

---

## 1. Objective

[KikiLabs](https://trykikilabs.com/) calibrates twins from real research and simulates follow-on decisions on the same cohort. This experiment proves that pipeline on PPiPL data.

The study itself ran in a fixed temporal order: **Interview 1 → weekly diaries → follow-ups → Interview 2**. Our calibration mirrors that order. Interview 2 is always held out. Every sequential step asks: *given everything the twin knows so far, how accurately can it simulate the closing interview?*

**Ground rules:**

- Interview 2 is never seen during calibration
- Each calibration step adds exactly one new data source (one diary batch or one follow-up)
- Re-score Interview 2 simulation after every step; report lift vs previous step and vs generic baseline
- Follow-on packaging scenarios allowed only after release criteria pass

---

## 2. Design

### Simulation target: Interview 2

Interview 2 is the closing in-depth interview. It revisits packaging attitudes, probes the attitude–behaviour gap, references specific diary moments, and captures how the participant's views evolved over the study period. This is the closest ground truth we have to "what would this person say in a follow-on research conversation" — the same class of output KikiLabs twins must produce in production.

**What we simulate:** For each interviewer question in Interview 2, the twin generates a first-person answer. Ground truth is the participant's actual response.

**Primary scoring domains:** Packaging-heavy Q&A (domains 6–8: plastic packaging, disposal/recycling, packaging generally). Full interview also scored for completeness. Domain guide: [Appendix B](#appendix-b-interview-questionnaires).

### Sequential calibration (study order)

Calibration material is added **one piece at a time**, matching when it was collected in the field. After each addition, rebuild the twin and re-measure Interview 2 simulation accuracy.

```
Step 0   Interview 1                          → simulate Interview 2
Step 1   + Diary batch 1                        → simulate Interview 2
Step 2   + Diary batch 2                        → simulate Interview 2
Step 3   + Follow-up 1                          → simulate Interview 2
Step 4   + Diary batch 3                        → simulate Interview 2
Step 5   + Diary batch 4                        → simulate Interview 2
Step 6   + Diary batch 5  (Katie, Stephen, Amy) → simulate Interview 2
Step 7   + Follow-up 2                          → simulate Interview 2
Step 8   + Behavioral parameters (from Steps 0–7)→ simulate Interview 2
Step 9   + Field diary excerpts (date-filtered)  → simulate Interview 2
```

---

## 3. Scoring

### Primary: Interview 2 simulation accuracy

Measured at **every sequential step** (Steps 0–9).


| Metric | Notes |
|---|---|
| **BERTScore F1** | Semantic match to participant's actual answer, per question |
| **ROUGE-L** | Lexical overlap |
| **Fact consistency** | Zero contradictions of verifiable Interview 1 facts |
| **Topic coverage** | Twin addresses same sub-topics participant raised (producer responsibility, waste hierarchy, diary callbacks) |


Report a **lift curve**: accuracy at Step 0, 1, 2, … 9. The curve shows which data type (diaries vs follow-ups vs parameters) moves the needle on closing-interview simulation.

### Secondary tests (diagnostic)

Run at the **final calibration step** (Step 7 or 9) to validate twin quality beyond Interview 2 wording:


| Test                                  | Ground truth                                  | Purpose                                                                  |
| ------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------ |
| **T4** Attitude–behaviour consistency | Interview 1 stated attitudes vs diary actions | Validates "behave vs say" — explains why Interview 2 is hard to simulate |
| **T5** Behaviour classification       | Rule-based labels from diary batch N          | Checks twin encodes observed behaviour, not just interview rhetoric      |


Detail: [Appendix C](#appendix-c-scoring-detail).

---

## 4. Execution

### Phased rollout


| Phase           | Participants                                               | N   | Role                                           |
| --------------- | ---------------------------------------------------------- | --- | ---------------------------------------------- |
| **1 · Pilot**   | Eliza, Isabella, Ella, Jacob, Cath, Marina, Stephen, Josie | 8   | Build pipeline; tune prompts; plot lift curves |
| **2 · Confirm** | Francesca, Amy, Gemma, Laura, Hannah                       | 5   | Locked pipeline; check generalization          |
| **3 · Extend**  | Naomi, Sophia, Katie, John                                 | 4   | Final validation                               |


Do not tune on Phase 2/3 until Phase 1 meets release criteria. Participants: [Appendix A](#appendix-a-p0-participants).

Extraction pipeline must preserve **study chronology** (filename dates, batch order). See [Appendix D](#appendix-d-extraction-prerequisites).

---

## 5. Expected outcomes

### Release criteria

A twin is cleared for follow-on simulation when:


| Criterion                           | Threshold                                                              |
| ----------------------------------- | ---------------------------------------------------------------------- |
| **Final-step Interview 2 accuracy** | Step 7 (or 9) beats Step 0 and generic baseline on BERTScore F1        |
| **Sequential lift**                 | At least one diary or follow-up step shows measurable lift over Step 0 |
| **Fact consistency**                | Zero contradictions of Interview 1 verifiable facts                    |
| **T4 (secondary)**                  | Final step beats Step 0 on attitude–behaviour contradiction F1         |


Phase 1 must pass in aggregate before locking for Phase 2.

### What success looks like

| Finding | Implication |
|---|---|
| Step 0 → Step 1–2 lift | Early diary observations improve closing-interview simulation |
| Step 2 → Step 3 lift (Follow-up 1) | Photo-elicitation adds decision context interviews miss |
| Step 5 → Step 7 lift (Follow-up 2) | Late-stage probes capture evolved views before closing interview |
| Step 0 ≈ Step 7 | Interview-only twins are sufficient (unlikely given diary callbacks in Interview 2) |
| Phase 2 confirms Phase 1 curves | Pipeline generalizes across participants |

### After this experiment

Twins that pass simulate **follow-on packaging scenarios** on the same cohort. Trust inherits from Interview 2 simulation accuracy at the final calibration step.

Deliverables: [Appendix E](#appendix-e-team-deliverables). KikiLabs mapping: [Appendix F](#appendix-f-kikilabs-product-mapping).

---

## Appendix A · P0 participants


| Pseudonym | Household            | Diaries | Phase | Sequential steps |
| --------- | -------------------- | ------- | ----- | ---------------- |
| Eliza     | Household12Eliza     | 4       | 1     | 0–5, 7–9         |
| Isabella  | Household13Isabella  | 4       | 1     | 0–5, 7–9         |
| Ella      | Household14Ella      | 4       | 1     | 0–5, 7–9         |
| Jacob     | Household15Jacob     | 4       | 1     | 0–5, 7–9         |
| Cath      | Household16Cath      | 4       | 1     | 0–5, 7–9         |
| Marina    | Household17Marina    | 4       | 1     | 0–5, 7–9         |
| Stephen   | Household18Stephen   | 5       | 1     | 0–6, 7–9         |
| Josie     | Household20Josie     | 4       | 1     | 0–5, 7–9         |
| Francesca | Household21Francesca | 4       | 2     | 0–5, 7–9         |
| Amy       | Household22Amy       | 5       | 2     | 0–6, 7–9         |
| Gemma     | Household23Gemma     | 4       | 2     | 0–5, 7–9         |
| Laura     | Household26Laura     | 4       | 2     | 0–5, 7–9         |
| Hannah    | Household27Hannah    | 4       | 2     | 0–5, 7–9         |
| Naomi     | Household03Naomi     | 4       | 3     | 0–5, 7–9         |
| Sophia    | Household07Sophia    | 4       | 3     | 0–5, 7–9         |
| Katie     | Household09Katie     | 5       | 3     | 0–6, 7–9         |
| John      | Household10John      | 4       | 3     | 0–5, 7–9         |


**Data path:** `857315_data/{Household}/`

---

## Appendix B · Interview questionnaires

### Nine topic domains


| #   | Domain                                                     | In Interview 2 simulation                           |
| --- | ---------------------------------------------------------- | --------------------------------------------------- |
| 1–5 | Household, food, preparation, shopping, routines           | Context from Interview 1; Interview 2 may revisit   |
| 6–8 | Plastic packaging, disposal/recycling, packaging generally | **Primary scoring focus**                           |
| 9   | Reuse behaviours                                           | Often referenced with diary examples in Interview 2 |


### Study timeline per participant

```
Interview 1 → Diary 1 → Diary 2 → Follow-up 1 → Diary 3 → Diary 4 [→ Diary 5] → Follow-up 2 → Interview 2
     ↑              ↑ sequential calibration (Steps 0–7)              ↑
  Step 0         Steps 1–7                                    SIMULATION TARGET (held out)
```

### Follow-ups


| Follow-up   | After                    | Added at step |
| ----------- | ------------------------ | ------------- |
| Follow-up 1 | Diary batches 1–2        | Step 3        |
| Follow-up 2 | Diary batches 3–4 (or 5) | Step 7        |


### Diary prompt

Weekly records of packaging encounters, shopping, meal prep, disposal, thoughts/feelings. Optional photos (text-only in v1).

---

## Appendix C · Scoring detail

### Interview 2 simulation metrics (primary)

- **BERTScore F1** and **ROUGE-L** per Q&A pair
- **Fact consistency** vs Interview 1 (household size, diet, bin setup)
- **Diary callback recall** — when Interview 2 references a diary moment, does the twin's answer align with what diaries recorded?

### Lift curve (report per participant)

For each participant, plot **Interview 2 BERTScore F1** at Steps 0–9. Report per-step delta vs previous step, vs Step 0, and vs generic baseline. Steps: 0 = Interview 1; 1–2 = diaries; 3 = Follow-up 1; 4–6 = diaries; 7 = Follow-up 2; 8 = parameters; 9 = field diary.

### T4 · Attitude–behaviour consistency (secondary)

Ground-truth pairs from Interview 1 attitudes vs diary observations:

- Stated recycler → observed general-waste disposal
- Stated packaging concern → observed convenience packaging purchase
- Stated reuse intent → observed single-use disposal

Twin predicts **aligned** or **contradictory**. High contradiction rate explains low Step 0 accuracy on Interview 2.

### T5 · Behaviour classification (secondary)

Rule-based labels from final diary batch: plastic packaging mention, recycling, general waste, food waste, reuse, shopping trip, out-of-home eating.

### Behavioral parameters (Step 8)

Extracted after Steps 0–7: `recycling_diligence`, `producer_vs_consumer_responsibility`, `convenience_packaging_tradeoff`, `reuse_tendency`, `food_waste_sensitivity`, `attitude_behavior_contradiction`, `occasion_context`. Re-run Interview 2 simulation to test whether structured parameters beat raw text concatenation.

---

## Appendix D · Extraction prerequisites


| Deliverable                          | Purpose                                             |
| ------------------------------------ | --------------------------------------------------- |
| `extract/extract.py`                 | Parse P0 `.docx` → JSON per participant             |
| `CSVs/full_participant.csv`          | One row per participant with ordered arrays         |
| `CSVs/full_participant_timeline.csv` | Chronological events for sequential step assignment |


**Critical:** preserve batch order (`diary_1`, `diary_2`, …) and filename dates so Steps 1–7 map correctly per participant.

**Field diary (Step 9):** entries dated before Interview 2, excluding test-period leakage.

**v1 limitation:** diary photos not extracted.

---

## Appendix E · Team deliverables


| Deliverable                                             | Owner          | When           |
| ------------------------------------------------------- | -------------- | -------------- |
| Extraction pipeline with chronological ordering         | Eng            | Phase 1 start  |
| Per-participant step manifest (which file = which step) | Eng            | Phase 1 start  |
| Twin calibration prompts (per step)                     | Research / ML  | Phase 1        |
| Interview 2 simulation harness + lift curve report      | Eng / ML       | Phase 1        |
| Phase 1 lift curves (8 participants)                    | Research       | Phase 1 end    |
| Locked pipeline config                                  | Research + Eng | Before Phase 2 |
| Phase 2 + 3 confirmation report                         | Research       | Experiment end |


---

## Appendix F · KikiLabs product mapping


| KikiLabs capability              | This experiment                                                      |
| -------------------------------- | -------------------------------------------------------------------- |
| Interview-grounded digital twins | Interview 1 seeds twin; Interview 2 is simulation target             |
| Compounding consumer memory      | Each diary/follow-up step adds memory; lift curve proves compounding |
| Behavioral parameter extraction  | Step 8 tests whether parameters beat raw sequential text             |
| Held-out tested before scenarios | Interview 2 never in calibration                                     |
| Scenario simulation runtime      | After release criteria pass                                          |


---

## Appendix G · References

- [`DATA_SCHEMA.md`](DATA_SCHEMA.md)
- [`857315_documentation/SUPPOR_1.DOC`](857315_documentation/SUPPOR_1.DOC)
- [KikiLabs](https://trykikilabs.com/)
- Piacentini et al. (2024). *Plastic Packaging in People's Lives.*

