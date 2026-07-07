# Eliza · Run 6 Predictions (Selective Lenses · KikiLabs Workflow)

**Run 6** · Selective lenses (2 per question) + tone  
**Evidence:** `E-Data.md` · **Lenses:** `E-Lenses.md` (2 per question)  
**Method:** Blind · `simulate_prediction` → `simulate_check` (Jul 2026)  
**Model:** Claude (Cursor agent)  
**Held-out actuals not used until scoring (`E6B.md`).**

---

## Question 1 · How do alternative packaging materials compare to plastic for you?

**Lenses:** `Category beliefs` · `Media and cultural signals`

### Predicted response

> Yeah so, this is awful to say but like, this information never really gets to us. People just say yeah use paper, paper is better, and I always believe that because that's what I've been hearing since I was little, but I've never got the information of why is it better. I don't understand the science or what happens to the paper after. They always talk about the big things but they never go to the actual yeah you should do this because this happens.
>
> In terms of how I actually think about them — plastic is just cheap and easy, that's honestly the first thing. Paper I think is a lot more fragile? Like it needs more care, and I have this feeling it won't last as much, so the food goes off sooner and I have to come back to the shop sooner. I don't have the time or money for that with uni and work.
>
> Glass I would never put in the same place as paper or plastic. At home we had the yellow plastic, green glass, blue paper bins and I thought that scheme was everywhere, and when I came here the boxes had no colours so I was really confused at the beginning. Thick plastic like the chicken tray obviously recycles; thin film I usually just bin because it's so small and our boxes are outside. Milk cartons I'm lost — cardboard outside but I don't know if there's plastic inside, and it doesn't say where it goes. So yeah, if that makes sense.

**Confidence:** high (direct I1 paper/plastic exchange, Portugal bin colours, thick vs thin heuristic, milk carton ambiguity)

**Reasoning:** Category beliefs (I1-19, I1-20) and Media/cultural signals (I1-15, I1-28, FU1 milk carton) support hearsay paper-better framing before material tradeoffs; tone register uses `honesty_opener`, `hedged_uncertain`, `budget_plain`.

### simulate_check

| Dimension | Score | Notes |
|-----------|------:|-------|
| grounded | 88 | All claims trace to calibration; no invented events |
| authenticVoice | 85 | Eliza fillers, hedges, check-in close |
| consistentWithTranscript | 90 | No contradictions |
| consistentWithPrevious | — | First question |

**Believability (avg 1–2):** 87 · **Consistency (avg 3–4):** 90  
**Critique:** Strong. Optional: could add one more oral stumble on glass/carton confusion.

---

## Question 2 · What are your views on the environmental impact of plastic food packaging?

**Lenses:** `Tensions & contradictions` · `Needs, motivations, emotional states`

### Predicted response

> Yeah I mean, I do care about the environment — I'm very aware we should be doing things for climate change and I agree with that. And I know plastic food packaging is bad, like I would prefer to buy less of it, I hate that so much stuff comes in plastic.
>
> But to be fair there's a tension there because when I go shopping I'm a uni student on a budget, and there are just way more options in plastic than not. So I end up buying plastic even though I know I shouldn't, which I don't love.
>
> Since this study I've been paying more attention — like oh everything in my fridge is plastic, and I notice when the thick plastic is different from the thin crunchy stuff. I think I do see more things in paper now as well, which is good. But it hasn't really changed what I buy because I still can't spend £2-3 more just for paper — like £2 is a bus ticket. Yeah I don't know what to say.

**Confidence:** high (I1-19 contradiction, study-awareness FU1, budget anchor)

**Reasoning:** Tensions lens foregrounds attitude–behavior gap; Needs lens adds quiet climate agreement; study reflection (E-Data FU1) supports "see more paper now"; closes with actual-typical hedge.

### simulate_check

| Dimension | Score | Notes |
|-----------|------:|-------|
| grounded | 86 | Study-awareness and budget tension are calibration-backed |
| authenticVoice | 84 | Contradiction framing matches Eliza |
| consistentWithTranscript | 88 | Aligns with prior plastic=cheap stance |
| consistentWithPrevious | 85 | Q1 paper hearsay compatible with Q2 plastic dislike |

**Believability:** 85 · **Consistency:** 87  
**Critique:** May be longer than Eliza's briefest answers; "see more paper now" is right frame but could be one sentence only.

---

## Question 3 · How confident are you that you know the "right" packaging choice?

**Lenses:** `Media and cultural signals` · `Barriers & frictions`

### Predicted response

> Not that confident, to be honest.
>
> For the environment side, people say paper is better and I believe that because I've always heard it, but why is it better? I have no idea. This information never really gets to us properly. They always talk about the big things but they never go to the actual yeah you should do this because this happens.
>
> For recycling it's also confusing. Growing up we had the colour scheme — yellow plastic, green glass, blue paper — and I thought that was everywhere. Here the boxes don't have colours and I had to ask my flatmates. I've heard people saying yeah recycle this and then others saying no you shouldn't. If there's that green thing with the arrows that helps, but a lot of things don't say anything. Milk cartons — I know they can be recycled but I don't know if it's paper or plastic or both. Thin plastics are the worst — am I supposed to recycle all plastics? I probably should know but I don't. And our recycling boxes are outside so for something really small and thin I'm like, is it even worth going out for that, while the chicken tray obviously makes sense. Yeah I kind of go with what people say, if that makes sense.

**Confidence:** high (I1-15, FU2-13/14, thin-film friction, environmental ignorance thread)

**Reasoning:** Media lens centres hearsay and missing education; Barriers lens adds UK box confusion, conflicting advice, outdoor-bin distance for thin film.

### simulate_check

| Dimension | Score | Notes |
|-----------|------:|-------|
| grounded | 90 | Recycling heuristics all from calibration |
| authenticVoice | 88 | Opens with direct low-confidence answer |
| consistentWithTranscript | 92 | Matches Q1 information-gap thread |
| consistentWithPrevious | 90 | Extends Q1/Q2 without contradicting |

**Believability:** 89 · **Consistency:** 91  
**Critique:** Recycling detail is richer than environmental-only confidence; acceptable given lens picks.

---

## Question 4 · How does food waste or freshness affect your packaging/shopping choices?

**Lenses:** `Tensions & contradictions` · `Routines & occasions`

### Predicted response

> Yeah so food waste is a big thing — that's the only thing in my house we don't waste food. My mum always taught me you can always do something with it unless it's gone off. So I hate throwing food away because it's wasting money.
>
> That affects how I shop. Before I travel I buy things in jars or frozen stuff and fewer vegetables because I know I won't use them in time. Like I had a quiche and froze it because it was going to go off. I stretch meals too — kilo of chicken for curry and enchiladas, then leftovers for noodles. At the end of term I batch cook curry into freezer boxes because I won't have time to cook every day.
>
> There's a tension with packaging because I want less plastic but paper feels like it won't last as long, so the food might go bad sooner and that's more waste and another shop. So if something keeps food fresh longer that's better for me, even if it means more plastic — wasting the actual food feels worse than the packaging. I don't know the science behind plastic, but food waste I understand because I pay for food and I know how much it costs, if that makes sense.

**Confidence:** high (I1-04 no-waste, I1-08 travel freezing, D3 batch curry, I1-20 paper shelf-life)

**Reasoning:** Routines lens supplies travel/term-phase examples; Tensions lens drives plastic-for-freshness over paper spoilage tradeoff.

### simulate_check

| Dimension | Score | Notes |
|-----------|------:|-------|
| grounded | 92 | Meal-stretching and freezing from multiple calibration steps |
| authenticVoice | 90 | Mum reference, budget anchor, check-in close |
| consistentWithTranscript | 94 | Consistent with paper-fragile belief |
| consistentWithPrevious | 91 | Q1–Q3 plastic/paper views align |

**Believability:** 91 · **Consistency:** 93  
**Critique:** None material. Strong believability pass.

---

## Question 5 · Does packaging influence what you buy?

**Lenses:** `Shopping & decisions` · `Price & value`

### Predicted response

> I mean, a little bit, but not as much as price and whether it fits my meals. When I'm at Aldi I'm doing the maths in my head — like if I buy the kilo chicken that's cheaper and it'll give me four meals if I do it right, and if I have two work shifts that's four meals I don't need to worry about. I'm comparing prices and weights, not walking around looking for the least packaging.
>
> Plastic influences it a bit because I know I hate how much stuff is in plastic and if I could I'd buy less. But there aren't that many options that aren't in plastic, and I'm on a budget, so I usually buy what's cheaper even if it's plastic. I wouldn't pay £2-3 more for paper — like £2 is a bus ticket.
>
> The only times I really notice are carrier bags — I never buy the 10p ones, we have reusable bags — or milk, I prefer the cardboard carton because it's what I'm used to from home. Since this study I've noticed packaging more but it hasn't changed what I buy. So yeah, budget and meals come first, if that makes sense.

**Confidence:** medium (food-shopping calibration strong; held-out turn mapping unknown at prediction time)

**Reasoning:** Shopping + Price lenses predict Aldi meal arithmetic and packaging as secondary to budget; carrier bags and milk carton are only packaging-notable purchase cues in calibration.

### simulate_check

| Dimension | Score | Notes |
|-----------|------:|-------|
| grounded | 88 | No Smol/laundry invented; food-shopping only |
| authenticVoice | 86 | Mental maths and bus-ticket anchor in character |
| consistentWithTranscript | 90 | Matches I1-22, I1-23, study awareness |
| consistentWithPrevious | 88 | Consistent with Q1–Q4 budget/plastic themes |

**Believability:** 87 · **Consistency:** 89  
**Critique:** Calibration ceiling — cannot reach non-food purchase drivers; prediction appropriately flags medium confidence.

---

## Workflow summary

| Step | Tool | Status |
|------|------|--------|
| 1 | `simulate_prediction` | 5/5 predictions written (blind) |
| 2 | `simulate_check` | 5/5 passed believability bar (≥70) |
| 3 | `simulate_judge` | See `E6B.md` |
