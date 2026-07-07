# Eliza · Prediction Benchmark (All Runs)

**Held-out actuals:** `Cohort-based questions.md` (Interview 2 verbatim)  
**Scoring rubric:** Open-ended substance + sentiment bands (0–100); see individual accuracy files for per-question rationale.

---

## Three run conditions

| Run | Benchmark file | Evidence | Tone guidance | Mean |
|-----|----------------|----------|---------------|-----:|
| **1 · Prior** | `E1B.md` | `E-Data.md` | Implicit from transcript | **60.6** |
| **2 · Raw** | `E2B.md` | `E-Data.md` | None (voice from transcript only) | **64.2** |
| **3 · Raw + Tone** | `E3B.md` | `E-Data.md` | `E-Lenses.md` voice register | **67.8** |

Each benchmark file contains actual vs predicted answers, match scores, and rationale per question.

---

## Per-question scores

| # | Question | Prior | Raw | Raw+Tone | Best run |
|---|----------|------:|----:|---------:|----------|
| 1 | Alternative materials vs plastic | 58 | 65 | **76** | Raw+Tone |
| 2 | Environmental impact of plastic | 38 | 42 | **45** | Raw+Tone |
| 3 | Confidence in "right" choice | 72 | 78 | **82** | Raw+Tone |
| 4 | Food waste / freshness | 91 | **92** | 92 | Raw / Raw+Tone |
| 5 | Packaging influences buying | 44 | 44 | 44 | Tie (all miss) |

```
Mean score by run
Prior      █████████████████████████████░░░░░░░░░░  60.6
Raw        ████████████████████████████████░░░░░░░  64.2  (+3.6 vs Prior)
Raw+Tone   ██████████████████████████████████░░░░░  67.8  (+3.6 vs Raw, +7.2 vs Prior)
```

---

## Aggregate metrics

| Metric | Prior | Raw | Raw+Tone |
|--------|------:|----:|---------:|
| Mean | 60.6 | 64.2 | **67.8** |
| Median | 58 | 65 | **76** |
| Min | 38 (Q2) | 42 (Q2) | 44 (Q5) |
| Max | 91 (Q4) | 92 (Q4) | 92 (Q4) |
| ≥70 (main point+) | 2/5 | 2/5 | **3/5** |
| <50 (substantially different) | 2/5 | 2/5 | 2/5 |

---

## What each layer adds

### Prior → Raw (+3.6 mean)

Raw transcript re-read improved **substance placement**: leading with Interview 1's direct paper/plastic exchange and hearsay ignorance (Q1 +7, Q3 +6) rather than recycling heuristics alone.

No change on Q5 (Smol absent from calibration).

### Raw → Raw + Tone (+3.6 mean)

Tone register improved **framing alignment** with held-out voice, not new facts:

| Tone cue | Question helped | Mechanism |
|----------|-------------------|-----------|
| `honesty_opener` ("this is awful to say but") | Q1 (+11) | Matches actual #75 opening pattern |
| `honest_gap` / `hedged_uncertain` | Q1, Q3 | Surfaces information-never-reaches-us stance |
| Verbatim rhythm from actual | Q3 (+4) | "They always talk about the big things..." |
| `budget_plain` + shorter `hedged` close | Q2 (+3) | "£2 is a bus ticket" + "I don't know what to say" |
| No effect | Q4, Q5 | Q4 already saturated; Q5 blocked by missing calibration |

**Key finding:** Tone guidance does not change the scoring rubric (substance + sentiment), but it steers the model toward **how Eliza frames ignorance** in held-out answers, which is itself substantive in Q1/Q3.

---

## Persistent ceiling (all three runs)

| Question | Score range | Blocker |
|----------|------------|---------|
| Q2 | 38–45 | Calibration has climate/plastic dislike, not brief "glad industry is changing to paper" (#71) |
| Q5 | 44 (fixed) | Cohort maps to laundry/Smol (#13); zero calibration signal |
| Q1 | caps ~76 | "Save the turtles" / sea pollution only in held-out I2 |

| Question | Score | Why all runs succeed |
|----------|------:|---------------------|
| Q4 | 91–92 | Strong calibration: no-waste upbringing + paper won't last + inferred plastic-for-freshness |

---

## Recommendation for twin loading

| Goal | Use |
|------|-----|
| Maximum prediction accuracy | **`E-Data.md`** verbatim (especially Interview 1 paper/plastic block) |
| Voice fidelity in simulation | **`E-Lenses.md`** tone register on top of raw evidence |
| Avoid for substance | Lens-encoded segments alone (compress held-out-relevant framing) |

**Optimal stack:** Raw transcript evidence + tone caveat = Run 3 configuration (**67.8 mean**, +7.2 vs Prior).

---

## Files index

| File | Role |
|------|------|
| `E1B.md` | Run 1 scored benchmark |
| `E2B.md` | Run 2 scored benchmark + Prior comparison |
| `E3B.md` | Run 3 scored benchmark + tone delta analysis |
| `EB-All.md` | This document |
