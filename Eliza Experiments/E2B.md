# Eliza · Run 2 Benchmark (Raw)

**Run 2** · Raw transcript only · `E-Data.md`  
**Actual:** `Cohort-based questions.md` (Interview 2, held-out)

---

## Question 1 · How do alternative packaging materials compare to plastic for you?

**Question type:** OPEN-ENDED  
**Actual turn:** Eliza #75

### Actual response

> Again this is awful to say but just this information never gets to us. People just say it is better to have paper and I always believe that it is because that's what I've been hearing since I was little. I've never got the information why is it better... I think its better because people say its better. And they always say something like, yeah use paper, lets save the turtles... if you throw plastic to the sea its going to be worse than throwing paper but its just as bad as throwing paper... I don't think that information comes to us either way.

### Predicted response (Raw)

> So plastic for me is just cheap and easy... People always say paper is better for the environment and I kind of believe that because I've always heard it, but I couldn't tell you why — no one really explains the science to us. Glass is different... milk cartons... fajita kits or pizza boxes...

### Score: **65**

**matchRationale:** Open-ended. Both convey paper believed better on hearsay without scientific understanding, but the actual centres on missing education ("save the turtles," sea pollution, information never reaching them) while the raw prediction still leads with practical shopping tradeoffs (cheap plastic, fragile paper, shelf life) before the hearsay line — partially aligned, improved over prior run on the "people say / don't know why" thread but still missing turtles/sea framing.

---

## Question 2 · What are your views on the environmental impact of plastic food packaging?

**Question type:** OPEN-ENDED  
**Actual turn:** Eliza #71

### Actual response

> I think its definitely something that is changing because I do see a lot of things just being like with paper and things like, so I think its changing and I'm glad it is. I am glad is it. Yeah I don't know what to say.

### Predicted response (Raw)

> I do care about the environment... I know plastic food packaging is bad... don't understand the science... since this study I've noticed... budget... I don't even know what happens to recycling... Yeah I don't know what to say beyond that.

### Score: **42**

**matchRationale:** Open-ended. The actual is brief and optimistic about industry packaging shifting to paper; the raw prediction shares the closing "I don't know what to say" hedging but otherwise elaborates personal climate concern, scientific ignorance, budget constraint, and recycling skepticism — partially related topic, but the focal insight (glad things are changing to paper) is absent.

---

## Question 3 · How confident are you that you know the "right" packaging choice?

**Question type:** OPEN-ENDED  
**Actual turn:** Eliza #75 (same as Q1)

### Actual response

> *(See Q1 actual — paper better because people say so; no science; save the turtles; information gap.)*

### Predicted response (Raw)

> Not that confident... People say paper is better and I believe that because I've always heard it, but why is it better? I have no idea... flatmates... thin plastics... green arrows... milk cartons...

### Score: **78**

**matchRationale:** Open-ended. Both express low confidence and reliance on hearsay without understanding why paper is better; the raw prediction now foregrounds the environmental-knowledge gap before recycling heuristics, aligning better with the actual's core stance, though it still adds bin-sorting detail (thick vs thin, green arrows) not present in the actual thread.

---

## Question 4 · How does food waste or freshness affect your packaging/shopping choices?

**Question type:** OPEN-ENDED  
**Actual turn:** Eliza #112

### Actual response

> ...food waste more present in my life than plastic waste... I would prefer to buy something in plastic that can make food longer, than just buy something in paper and then the food goes bad... I don't know the science behind plastic that much.

### Predicted response (Raw)

> Food waste is a big thing... freeze quiche... chicken leftovers... paper won't last as long... if something keeps food fresh longer that's better for me, even if it means more plastic... I don't know the science behind plastic, but food waste I understand...

### Score: **92**

**matchRationale:** Open-ended. Same core tradeoff — food waste more salient and understood than plastic harm, plastic preferred when it extends freshness over paper spoilage, plastic science unknown — with the prediction adding calibration meal-planning examples that supplement rather than contradict the actual stance.

---

## Question 5 · Does packaging influence what you buy?

**Question type:** OPEN-ENDED  
**Actual turn:** Eliza #13 (laundry / Smol trial)

### Actual response

> ...capsules that I bought was because I was part of a trial... Instagram student promo... recycled-plastic capsules... smaller amounts = less waste... Smol.

### Predicted response (Raw)

> A little bit, but not as much as price and meals... Aldi chicken... wouldn't pay £2-3 more for paper... reusable bags... milk carton familiar... hasn't really changed what I buy.

### Score: **44**

**matchRationale:** Open-ended. Both reflect student budget consciousness, but the actual shows eco-packaging (recycled capsules, less waste) actively drove a laundry purchase via student trial, while the raw prediction — limited to food-shopping calibration with no Smol content — concludes packaging is secondary and has not changed buying behaviour.

---

## Summary

| # | Question | Type | Raw score | Prior score | Δ |
|---|----------|------|----------:|------------:|--:|
| 1 | Alternative materials vs plastic | Open-ended | **65** | 58 | +7 |
| 2 | Environmental impact of plastic packaging | Open-ended | **42** | 38 | +4 |
| 3 | Confidence in "right" packaging choice | Open-ended | **78** | 72 | +6 |
| 4 | Food waste / freshness and packaging | Open-ended | **92** | 91 | +1 |
| 5 | Does packaging influence what you buy? | Open-ended | **44** | 44 | 0 |

| Metric | Raw (`E-Data.md`) | Prior (`E1B.md`) |
|--------|----------------------:|-------------------------------:|
| **Mean score** | **64.2** | **60.6** |
| **Median** | 65 | 58 |
| **≥70 (main point+)** | 2 / 5 | 2 / 5 |
| **<50 (substantially different)** | 2 / 5 | 2 / 5 |

---

## Benchmark analysis

### What improved (Raw vs Prior)

**Q1 (+7) and Q3 (+6):** Leading with verbatim Interview 1 content on paper believed better by hearsay ("I've always heard it" / "why is it better? I have no idea") better matches held-out #75 than leading with practical shopping alone.

**Q2 (+4):** Closing with "I don't know what to say" mirrors actual brevity, but the substantive miss (industry shifting to paper) remains because calibration data does not contain that optimism.

**Q4 (+1):** Already strong; raw pass adds explicit "I pay for food" line closer to actual's cost salience.

**Q5 (0):** No change. Smol laundry trial exists only in held-out Interview 2; neither raw nor prior calibration can predict it.

### Persistent blind spots (calibration data limits)

| Topic in held-out I2 | Signal in `E-Data.md` | Impact |
|---------------------|---------------------------|--------|
| "Save the turtles" / sea pollution framing | Absent | Q1 caps ~65 |
| Industry shifting to paper (glad it's changing) | Absent | Q2 caps ~42 |
| Smol / laundry packaging trial | Absent | Q5 caps ~44 |
| Plastic keeps food fresher (explicit tradeoff) | Inferred only | Q4 still scores ~92 |

### Raw vs Lenses note

This benchmark uses **`E-Data.md` verbatim** only. `E-Lenses.md` was not used for predictions or scoring. The prior `E1B.md` run was also calibration-based (not held-out I2); the +3.6 mean improvement comes from tighter alignment to Interview 1's direct paper/plastic exchange and Q75's environmental-ignorance framing, not from a different evidence base.

### Recommendation

For twin prediction tasks where held-out questions overlap Interview 2 #75 (paper vs plastic environmentally) or #71 (brief industry-change observation), raw transcript access to Interview 1's paper/plastic block is high-value. Lens encoding adds tone fidelity but does not surface held-out content absent from calibration. Q5 accuracy requires either a better cohort question mapping (food-shopping turn) or accepting that non-food purchase drivers are unpredictable from food-focused calibration.
