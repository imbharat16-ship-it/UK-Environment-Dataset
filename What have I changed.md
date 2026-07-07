# Twin simulation methodology (Run 4 · selective lenses)

Operational guide for predicting held-out interview answers: what calibration is, how to add lenses and tone, and which prompts to use for simulate and judge.

**Reference implementation (Eliza):** [`E-Data.md`](Eliza Experiments/E-Data.md) · [`E-Lenses.md`](Eliza Experiments/E-Lenses.md) · [`KikiLabs Prompts.md`](KikiLabs Prompts.md)

---

## Evidence stack

```
┌─────────────────────────────────────────────────────────┐
│  {{TRANSCRIPT}}     E-Data.md (verbatim calibration)    │
├─────────────────────────────────────────────────────────┤
│  {{EXPERT_ANALYSIS}}                                    │
│    · 2 lens profile paragraphs (cross-step)             │
│    · Relevant encoded segments for those lenses         │
│    · Tone register (voice section)                      │
│    · Per-question: lead with lens frame first           │
├─────────────────────────────────────────────────────────┤
│  {{QUESTION_TEXT}}   Held-out question (no I2 answer)   │
└─────────────────────────────────────────────────────────┘
         │
         ▼
   simulate_prediction  →  simulate_check  →  (write actual)  →  simulate_judge
```

**Blind rule:** Build predictions from calibration only. Do not read held-out actuals (`Cohort-based questions.md`, Interview 2, or twin I2 turns) until after predictions are written.

---

## 1. Calibration data

### What it is

**Calibration data** is everything the twin is allowed to know before predicting a held-out answer. For Eliza this is [`E-Data.md`](Eliza Experiments/E-Data.md): full verbatim transcripts from the calibration phase.

| Included | Excluded |
|----------|----------|
| Interview 1 | Final interview (Interview 2) |
| Diaries 1–4 | |
| Follow-up interviews 1–2 | |

**Source files** (per participant) live under `.extracted/<name>/`. The markdown twin file concatenates them in calibration order with `A:` / `B:` speaker turns preserved.

### What goes in `{{TRANSCRIPT}}`

Paste the full contents of `E-Data.md` (or the participant's `*-Data.md`), **minus** any held-out material. The model should see the participant's real words, not summaries.

### Building calibration for a new participant

1. Extract text from interview/diary docx into `.extracted/<name>/`.
2. Assemble verbatim markdown in step order (Interview 1 → diaries → follow-ups).
3. Add a short profile block (cohort, household, category context).
4. Exclude the evaluation interview from this file.

Eliza builder: [`scripts/build_eliza_data_lenses.py`](scripts/build_eliza_data_lenses.py) (reads `.extracted/eliza/`).

---

## 2. How to add lenses

### What lenses are

[`E-Lenses.md`](Eliza Experiments/E-Lenses.md) encodes the same calibration through **11 expert lenses**. Each lens is a interpretive frame (not a fact list):

| Lens | Interprets |
|------|------------|
| Identity & culture | Self, family, belonging |
| Needs, motivations, emotional states | Attitudes, motivations |
| Category beliefs | How the category works for them |
| Routines & occasions | When/where/how it fits life |
| Sensory experience | Taste, feel, smell |
| Shopping & decisions | Path to purchase |
| Competitive context | Brands across category |
| Price & value | Worth, trade-offs |
| Barriers & frictions | What blocks switching |
| Tensions & contradictions | Say vs do |
| Media and cultural signals | News, school, labels, norms |

Each **encoded segment** in `E-Lenses.md` has:

- **Lenses** — which frames apply
- **Encodes** — behavioral claim to reproduce (stance, not trivia)
- **Tone** — cue tags for how they say it
- **Quote** — verbatim anchor from calibration

### Selective lenses (Run 4)

Do **not** load all 11 lenses or all segments. Per held-out question, pick **exactly two lenses** using the **Cross-step lens profile** section (which lenses have the richest signal for that topic).

**Eliza lens picks (example):**

| Q | Topic | Lens 1 | Lens 2 |
|---|-------|--------|--------|
| 1 | Alternative materials vs plastic | Category beliefs | Media and cultural signals |
| 2 | Environmental impact of plastic | Tensions & contradictions | Needs, motivations |
| 3 | Confidence in "right" choice | Media and cultural signals | Barriers & frictions |
| 4 | Food waste / freshness | Tensions & contradictions | Routines & occasions |
| 5 | Packaging influences buying | Shopping & decisions | Price & value |

### What to paste into `{{EXPERT_ANALYSIS}}`

Assemble a block like this (before the question):

```markdown
## Expert analysis (selective lenses for this question)

### Lens: Category beliefs
[Cross-step profile paragraph from E-Lenses.md]

### Lens: Media and cultural signals
[Cross-step profile paragraph from E-Lenses.md]

### Relevant segments
[Pull 3–8 encoded segments tagged with either lens, prioritising packaging/food/shopping]

### Prediction instruction
Lead with the stance these two lenses surface (e.g. information gap / hearsay before shop examples).
State the overall decision framework before any diary or shop examples.
Use at most one illustrative example unless the participant habitually lists many.
```

**Selection heuristic:** Read the held-out question → choose lenses whose cross-step profile + segment tags best match the decision being asked → prefer segments from Interview 1 when the topic was discussed directly there.

**Do not use for substance:** lens segments alone without `E-Data.md`, or all lenses at once.

---

## 3. How to add tone

Tone is the **voice register** so the twin sounds like the participant, not just reasons like them.

### Where it lives

`E-Lenses.md` → section **Eliza's voice (tone register)**:

- Overall character (student register, hedges, budget pragmatism, etc.)
- Signature speech patterns (`honesty_opener`, `hedged_uncertain`, `budget_plain`, …)
- Sentence shape (direct answer → example → hedge → soft close)
- Avoid list (no polished research language, no activist tone)
- Wrong vs right examples

Per-segment **Tone** tags in encoded segments (e.g. `warm_casual`, `thinking_aloud`) map to the legend at the bottom of `E-Lenses.md`.

### What to paste

Include the full **voice register** section in `{{EXPERT_ANALYSIS}}` (or immediately after the transcript) on every prediction. Tone is always on for Run 4, not optional.

### What tone does

Tone does not add new facts. It steers **framing and phrasing** to match held-out voice: e.g. opening with "this is awful to say but…" when the participant does that in Interview 2, or closing with "if that makes sense" / "I don't know what to say."

---

## 4. Prompts (`KikiLabs Prompts.md`)

Replace `{{...}}` placeholders, then run in order: **prediction → check → judge** (judge only after you have the actual held-out answer).

### Placeholders

| Variable | Content |
|----------|---------|
| `{{TRANSCRIPT}}` | Full `E-Data.md` (calibration only) |
| `{{EXPERT_ANALYSIS}}` | Selective lenses + segments + tone + per-question instruction (see §2–3) |
| `{{QUESTION_TEXT}}` | Held-out question verbatim |
| `{{PREVIOUS_PREDICTIONS}}` | Prior Q&A pairs in the same session (optional; empty on Q1) |
| `{{REVISION_FEEDBACK}}` | Output from `simulate_check` critique if rewriting (optional) |
| `{{PREDICTED_RESPONSE}}` | Model output from `simulate_prediction` |
| `{{ACTUAL_RESPONSE}}` | Held-out answer (for judge only; never before prediction) |

---

### `Simulate_prediction`

```
You are working with a single 1-on-1 research interview. Below is the transcript of a completed interview with a participant, with certain questions removed. Read it carefully — your specific task is described after the transcript.

## Interview Transcript (with selected questions removed)
{{TRANSCRIPT}}

{{EXPERT_ANALYSIS}}## Your Task
You are an expert qualitative researcher. Predict what the participant would have answered to the question shown below, based on their personality, communication style, opinions, values, and patterns evident in the remaining transcript.

## Instructions
- Predict the participant's response as they would naturally speak, matching their vocabulary, sentence structure, level of detail, and emotional tone.
- Draw on concrete evidence from the transcript: opinions they expressed, experiences they shared, patterns in how they answer.
- For multiple-choice or ranking questions, predict which option(s) they would choose and explain why.
- Be specific and grounded — do not produce generic responses.
- In your reasoning, cite specific parts of the transcript that informed your prediction.
- Rate your confidence as high (strong, direct evidence in the transcript), medium (reasonable inference), or low (mostly speculative). Use low — not medium — whenever the prediction rests mostly on weak or indirect inference, e.g. near a scale's midpoint, on cognitive-reflection "trick" questions, or on near-indifferent binary choices where the transcript gives little signal.
- When the transcript shows confusion, repeated "I don't know," or that the participant is not sure what the right choice is, lead with that uncertainty in the predicted answer. Do not sound fully confident if their pattern is mid confidence at best.
- When the participant says they lack experience with an alternative (e.g. never uses paper, can't compare materials) or cannot answer, predict that directly — do not infer a polished comparison they did not express.
- State the participant's overall decision framework or stance (what packaging means to them, what tension they hold) before any shop or diary examples. Use at most one illustrative example unless they habitually list many; do not let a single vivid diary detail become the whole answer.

## Answering scale, rating, and multiple-choice questions
- When the options form an ordered scale (e.g. a Likert agree-disagree scale or a numeric 1-N rating), treat them as an ordered continuum: first describe who sits at each end, then place this participant at the specific point that matches the strength of their evidenced view, and explicitly include that exact option label in your predicted response — not just the direction.
- Watch for reverse-worded or negated statements. Decide whether agreeing with THIS sentence implies the same underlying trait as the participant's related answers or the opposite, and match the trait rather than the surface wording: someone high on a trait should disagree with a reverse-worded item about it.
- Do not default to agreement or to the positive/high end of a scale. Choose the side and the intensity strictly from this participant's evidenced stance; a lack of evidence is not evidence of agreement.
- For rating batteries that ask respondents to spread ratings across the full range, do not collapse every item to the extreme. Reserve the endpoints for the views this participant holds most strongly and use mid-range values for moderate ones, mirroring how widely they use the scale elsewhere in the transcript.

{{PREVIOUS_PREDICTIONS}}## Question to Predict
{{QUESTION_TEXT}}{{REVISION_FEEDBACK}}
```

---

### `Simulate_check`

Run on the predicted response before scoring. Use the critique to rewrite if believability or consistency falls below 70.

```
You are working with a single 1-on-1 research interview. Below is the transcript of a completed interview with a participant, with certain questions removed. Read it carefully — your specific task is described after the transcript.

## Interview Transcript (with selected questions removed)
{{TRANSCRIPT}}

{{EXPERT_ANALYSIS}}{{PREVIOUS_PREDICTIONS}}## Question
{{QUESTION_TEXT}}

## Predicted Response to Evaluate
{{PREDICTED_RESPONSE}}

## Your Task
You are a rigorous quality evaluator. A predicted response was generated to fill in the question above, which was removed from the participant's transcript. Judge whether the prediction is BELIEVABLE and CONSISTENT before it is scored.

## What to Evaluate
1. grounded — the prediction stays grounded in the transcript and the participant's demonstrated views. Reasonable inference is fine, but it must NOT invent specific facts, events, or strong opinions the participant never expressed.
2. authenticVoice — it reads like this participant speaking (their tone, vocabulary, level of detail), not generic or robotic prose.
3. consistentWithTranscript — it does not contradict anything in the transcript.
4. consistentWithPrevious — it does not contradict the participant's earlier predicted answers shown above (if any).
5. uncertaintyFraming — when the transcript shows the participant is confused or not sure what the "right" choice is, the prediction reflects that tentativeness rather than sounding 100% sure.

## Scoring
Score believability (dimensions 1-2) and consistency (dimensions 3-5) each from 0 to 100, where 100 is flawless and 70 is the minimum acceptable bar. List concrete issues and write a short, actionable critique the predictor could use to fix the problems on a rewrite.
```

---

### `Simulate_judge`

Run only after predictions are fixed. Compares predicted vs actual held-out answer.

```
You are a rigorous evaluator scoring how well a PREDICTED survey/interview response matches the participant's ACTUAL response, from 0 to 100. Pick the scoring rule that fits the question type — never award credit merely because the two responses are about the same topic.

## Question
{{QUESTION_TEXT}}

## Actual Response
{{ACTUAL_RESPONSE}}

## Predicted Response
{{PREDICTED_RESPONSE}}

## Step 1 — Classify the question
- ORDERED SCALE: answers come from an ordered set — a Likert agreement scale (Disagree strongly ... Agree strongly), a frequency or importance scale, or a numeric rating (e.g. 1-9). Adjacent points mean nearly the same thing; opposite ends mean opposite things.
- UNORDERED CHOICE: the answer is one or more options from a set with no inherent order (e.g. choosing a symptom or a product, yes/no, or a select-all list).
- OPEN-ENDED: a free-text answer with no fixed option set.

## Step 2 — Score by type
### Ordered scale
Locate both responses on the scale. If the question text does not make the scale explicit, infer the most standard scale for the item (e.g. a 5-point Likert agreement scale, or the numeric range named in the question) and state the scale you assumed in the rationale. Let d = the number of steps between them and R = the total number of steps from one end of the scale to the other. Score = round(100 * (1 - (d/R)^2)): an exact match is 100, a one-step gap is penalized only lightly, and the penalty grows quadratically as the gap widens. Two rules override this formula:
  - DIRECTION FLIP: if the two responses fall on opposite sides of the scale's midpoint (e.g. agree vs disagree, support vs oppose, important vs unimportant), that is a substantive error — score no higher than 40 even if they are only one or two steps apart.
  - Opposite extremes (e.g. Disagree strongly vs Agree strongly) score 0.
### Unordered choice
The same option selected scores 100. A different option scores 0 — do NOT give partial credit because two options share a theme; a wrong category is a miss. For select-all answers, score by Jaccard overlap: round(100 * (size of the intersection of the predicted and actual option sets / size of their union)).
  - SUBSTANCE GATE: for yes/no or single-select items that also invite explanation, if both responses select the same option (e.g. both "yes") but the open-ended substance clearly differs (different main reason, opposite framing, or unrelated examples), cap the score at 60 and state that the choice matched but the substance did not.
### Open-ended
Judge whether the prediction conveys the same core stance, key insights, and sentiment as the actual answer: different wording with the same substance scores high, the same keywords with a different point scores low. Score the main stance and reasoning, not keyword or topic overlap alone. Bands: 90-100 same substance and sentiment; 70-89 main point with minor gaps; 50-69 partially aligned; 30-49 substantially different or opposing; 0-29 contradictory or unrelated.
  - WRONG MAIN REASON: if both responses share the same broad sentiment direction (e.g. both negative on plastic) but the predicted answer centres on a different main reason than the actual (e.g. shopping trade-offs vs climate grief, or practical preference vs "I don't know"), cap the score at 50–69, not 70+.
- **Examples only — same point, not same count:** When the actual answer uses several illustrative examples (concrete reasons, anecdotes, or named instances), score whether the prediction captures what those examples *mean*, not whether it repeats every example or uses the same nouns. If multiple actual examples all support the same underlying point, treat them as one illustration — do not penalize the prediction for giving fewer examples, as long as its example(s) are grounded and convey that shared meaning. Do not let different examples lower the score when the reasoning and feeling match. Penalize only when a missing example carries a different substantive point, or when the prediction invents an example the participant never expressed.

## Step 3 — Rationale
In matchRationale, state the question type, where each response sits (for scales, give both positions and the step distance d/R), and the rule that set the score. When examples drove the score, say whether they illustrated the same point — not a checklist of every example or noun in the actual. Keep it to 1-3 sentences.
```

---

## Workflow checklist

1. Load `*-Data.md` into `{{TRANSCRIPT}}`.
2. Pick 2 lenses for the question; build `{{EXPERT_ANALYSIS}}` from cross-step profiles + segments + tone register.
3. Run **`Simulate_prediction`** with held-out question in `{{QUESTION_TEXT}}`.
4. Run **`Simulate_check`**; rewrite if below 70 on believability or consistency.
5. After all predictions are written, pull actuals from `Cohort-based questions.md`.
6. Run **`Simulate_judge`** per question; record score and `matchRationale` in `*B.md`.

**Scored output format:** See [`E4B.md`](Eliza Experiments/E4B.md) or [`E6B.md`](Eliza Experiments/E6B.md) for per-question actual, predicted, score, and rationale.
