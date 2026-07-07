# Eliza Twin · Prediction Benchmark (Team Summary)

**Participant:** Eliza (Household 12) · **July 2026**  
**Ground truth:** `Cohort-based questions.md` (Interview 2, held out)  
**Calibration:** `E-Data.md` (Interview 1, Diaries 1–4, Follow-up 1–2)

### File naming


| Code          | Meaning                                                    |
| ------------- | ---------------------------------------------------------- |
| `E`           | Eliza (participant)                                        |
| `1`–`8`       | Run number                                                 |
| `B`           | Scored run (actual vs predicted + match score + rationale) |
| `EB.md`       | Team summary (this file)                                   |
| `E-Data.md`   | Calibration transcript                                     |
| `E-Lenses.md` | Lens-encoded context + tone                                |


---

## Headline

Eight run configurations on held-out packaging questions. **Best Eliza prediction mean: 70.6/100** (Run 5: selective lenses, GPT-5.4, blind). **Runs 7–8** re-score existing predictions with the updated `Simulate_judge` rubric (no new predictions).


| Run                         | Configuration                              | Mean     | Mean (excl. Q5) |
| --------------------------- | ------------------------------------------ | -------- | --------------- |
| 1 · Prior                   | `E-Data.md` (first pass)                   | 60.6     | 64.8            |
| 2 · Raw                     | `E-Data.md` verbatim re-read               | 64.2     | 69.3            |
| 3 · Raw + Tone              | `E-Data.md` + tone register                | 67.8     | 73.8            |
| 4 · Selective Lenses        | `E-Data.md` + **2 lenses/question** + tone | **75.8** | **83.8**            |
| **5 · Selective (GPT-5.4)** | Same as Run 4 · **GPT-5.4** · **blind**    | **70.6** | **75.3**        |
| 6 · KikiLabs prompts        | Same as Run 4 · **`simulate_*` workflow**  | 70.2     | 76.8            |
| 7 · Updated judge (cohort)  | PDF sims · **`Simulate_judge` P0 rubric** · 5 participants | — (Eliza **61.2**) | — |
| 8 · Updated judge (Run 4)  | `E4B.md` sims · **`Simulate_judge` P0 rubric** · Eliza only | **75.8** | **83.8** |


---

## Run 7 · Cohort re-judge (updated Simulate_judge)

**Method:** Same predicted + actual text as [simulation PDF](../simulation--SEED-UK-Plastic-Cohort-Questions-Held-out- (1).pdf); scores recomputed using [KikiLabs Prompts.md](../KikiLabs Prompts.md) `Simulate_judge` after P0 updates (WRONG MAIN REASON, SUBSTANCE GATE cap 60, examples ≠ score driver, main stance not keywords).

**Full scored file:** `E7B.md`

### Cohort summary (all 5 participants · 7 questions)

| Participant | Run 7 avg | PDF avg | Δ |
|-------------|----------:|--------:|--:|
| Cath | **67.3** | 72.0 | −4.7 |
| Eliza | **61.2** | 72.0 | −10.8 |
| Ella | **63.7** | 71.0 | −7.3 |
| Isabella | **65.4** | 68.0 | −2.6 |
| Jacob | **53.6** | 51.0 | +2.6 |
| **All** | **62.0** | 67.0 | **−5.0** |

*Eliza avg is over 6 scored questions (no Q7 in PDF). Cohort avg (excl. benchmark skips): **65.0** — Cath Q7, Eliza Q4, Isabella Q5, Jacob Q4.*

### Eliza · Run 7 per question (PDF predictions)

| # | Question | PDF score | Run 7 | Δ | Rule applied |
|---|----------|----------:|------:|--:|--------------|
| 1 | Alternative materials vs plastic | 28 | **28** | 0 | — |
| 2 | Environmental impact of plastic | 64 | **55** | −9 | WRONG MAIN REASON |
| 3 | Confidence in "right" choice | 94 | **94** | 0 | Ordered scale |
| 4 | When do you compromise? | 58 | **52** | −6 | Wrong benchmark mapping (skip) |
| 5 | Food waste / freshness | 86 | **78** | −8 | Missing key why |
| 6 | Does packaging influence buying? | 100 | **60** | −40 | SUBSTANCE GATE |

### What changed vs PDF judge

| Rule | Effect |
|------|--------|
| **SUBSTANCE GATE** (yes/no + wrong framework → cap 60) | Cath Q6, Eliza Q6, Ella Q6 drop from 100 |
| **WRONG MAIN REASON** (same sentiment, different why → cap 50–69) | Cath Q2, Eliza Q2, Ella Q2 lower |
| **Examples rule** (same reason/feeling, different examples OK) | Cath Q4 +20, Jacob Q3 +22 |
| **Main stance not keywords** | Isabella Q2 +6 |

Run 7 is **not comparable** to Runs 1–6 means: it re-scores different (PDF) predictions on a 7-question cohort grid, not Eliza Run 4/5/6 blind predictions on the 5-question Eliza benchmark.

---

## Run 8 · Run 4 re-judge (updated Simulate_judge)

**Method:** Same predicted + actual text as `E4B.md` (Run 4 · Selective lenses); scores recomputed using [KikiLabs Prompts.md](../KikiLabs Prompts.md) `Simulate_judge` after P0 updates.

**Full scored file:** `E8B.md`

**Scope:** Run 4 selective-lens **predictions exist for Eliza only** in this repo (5 questions). No Run 4 prediction files for Cath, Ella, Isabella, or Jacob.

### Eliza · Run 8 summary

| # | Question | Run 4 | Run 8 | Δ |
|---|----------|------:|------:|--:|
| 1 | Alternative materials vs plastic | 79 | **86** | +7 |
| 2 | Environmental impact of plastic | 52 | **65** | +13 |
| 3 | Confidence in "right" choice | 84 | **88** | +4 |
| 4 | Food waste / freshness | 92 | **96** | +4 |
| 5 | Packaging influences buying | 44 | **44** | 0 |
| **Mean** | | **70.2** | **75.8** | **+5.6** |
| **Mean (excl. Q5)** | | **76.8** | **83.8** | **+7.0** |

Run 8 shows the updated judge **raises** Run 4 Eliza scores (+5.6 mean) because predictions already capture main stance and key reasoning better than the cohort PDF sims (Run 7). Q5 unchanged (Smol/laundry outside calibration).

---

## Per-question scores (all runs)


| #   | Question                         | Prior | Raw    | Raw+Tone | Selective | Selective (GPT-5.4) | KikiLabs |
| --- | -------------------------------- | ----- | ------ | -------- | --------- | ------------------- | -------- |
| 1   | Alternative materials vs plastic | 58    | 65     | 76       | 79        | **80**              | 79       |
| 2   | Environmental impact of plastic  | 38    | 42     | 45       | **52**    | 49                  | **52**   |
| 3   | Confidence in "right" choice     | 72    | 78     | 82       | **84**    | 81                  | **84**   |
| 4   | Food waste / freshness           | 91    | **92** | **92**   | **92**    | 91                  | **92**   |
| 5   | Packaging influences buying      | 44    | 44     | 44       | 44        | **52**              | 44       |



| Metric                        | Prior | Raw  | Raw+Tone | Selective | Selective (GPT-5.4) | KikiLabs |
| ----------------------------- | ----- | ---- | -------- | --------- | ------------------- | -------- |
| Mean                          | 60.6  | 64.2 | 67.8     | 70.2      | **70.6**            | 70.2     |
| Mean (excl. Q5)               | 64.8  | 69.3 | 73.8     | **76.8**  | 75.3                | **76.8** |
| ≥70 (main point+)             | 2/5   | 2/5  | 3/5      | **4/5**   | 3/5                 | **4/5**  |
| <50 (substantially different) | 2/5   | 2/5  | 2/5      | 2/5       | **1/5**             | 2/5      |


---

## What each layer added


| Step                                   | Δ mean | What changed                                                                             |
| -------------------------------------- | ------ | ---------------------------------------------------------------------------------------- |
| Prior → Raw                            | +3.6   | Verbatim Interview 1 paper/plastic block; hearsay ignorance foregrounded                 |
| Raw → Raw + Tone                       | +3.6   | `honesty_opener`, `hedged_uncertain` match held-out voice (Q1 +11)                       |
| Raw + Tone → Selective                 | +2.4   | 2 lenses/question prioritise right frame (Q2 +7 via Needs/Tensions)                      |
| Selective → Selective (GPT-5.4, blind) | +0.4   | Cleaner blind wording improved Q1 and Q5; shorter answers lost some specificity on Q2-Q4 |
| Selective → KikiLabs prompts (Run 6)     | 0.0    | Same evidence stack and scores; adds `simulate_prediction` → `simulate_check` → `simulate_judge` QA gate |


**Run 5 lens picks:**


| Q   | Lens 1                     | Lens 2                     |
| --- | -------------------------- | -------------------------- |
| 1   | Category beliefs           | Media and cultural signals |
| 2   | Tensions & contradictions  | Needs, motivations         |
| 3   | Media and cultural signals | Barriers & frictions       |
| 4   | Tensions & contradictions  | Routines & occasions       |
| 5   | Shopping & decisions       | Price & value              |


---

## Strong vs weak

**Strong (Q4, 92 best overall; 91 in Run 5):** Food-waste upbringing + paper shelf-life → plastic-for-freshness tradeoff.

**Weak (all runs):**


| Question | Best score | Blocker                                                                                                                        |
| -------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Q5       | 52         | Clean blind rerun now says packaging can influence buying, but laundry/Smol (#13) still sits outside food-shopping calibration |
| Q2       | 52         | Calibration has climate/plastic dislike, not brief "glad industry is changing to paper" (#71)                                  |


---

## Recommendation

**Optimal twin stack (Run 5):**

1. `E-Data.md` — verbatim evidence
2. **2 expert lenses per question** — from `E-Lenses.md` cross-step profile + tagged segments
3. Tone register — always on
4. **Lens-led answer ordering** — lead with the frame the lenses surface (e.g. Media → information gap; Needs/Tensions → climate care vs budget)
5. Prefer a **short answer first**, then only one small supporting example if needed
6. **Run blind** — do not consult held-out actuals during prediction (see `.cursor/rules/twin-benchmark-blind-runs.mdc`)

Do not load all 11 lenses or lens segments alone without raw transcript.

---

## Artifacts (`Eliza Experiments/`)


| Run                     | Scored benchmark |
| ----------------------- | ---------------- |
| 1 · Prior               | `E1B.md`         |
| 2 · Raw                 | `E2B.md`         |
| 3 · Raw + Tone          | `E3B.md`         |
| 4 · Selective           | `E4B.md`         |
| 5 · Selective (GPT-5.4) | `E5B.md`         |
| 6 · KikiLabs prompts    | `E6B.md` (`E6P.md` predictions + checks) |
| 7 · Updated judge (cohort PDF) | `E7B.md` (5 participants · 7 questions · re-score only) |
| 8 · Updated judge (Run 4) | `E8B.md` (Eliza · 5 questions · re-score only) |


Each `E*B.md` file contains the actual answer, predicted answer, match score, and rationale per question. Runs 7–8 use existing predictions unchanged; only judge scores differ.

**Also:** `EB-All.md` (extended benchmark notes) · `E-Data.md` · `E-Lenses.md`

---

## Open questions

1. Remap Q5 to food-shopping turn before cross-participant benchmarks?
2. Replicate five-run series for Cath, Ella, Isabella, Jacob?
3. Automate lens selection (segment count) vs researcher judgment?

