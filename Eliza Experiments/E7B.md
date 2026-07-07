# Cohort · Run 7 Benchmark (PDF simulations · updated Simulate_judge)

**Run 7** · Re-score only (Jul 2026)  
**Source predictions:** [simulation--SEED-UK-Plastic-Cohort-Questions-Held-out- (1).pdf](../simulation--SEED-UK-Plastic-Cohort-Questions-Held-out- (1).pdf)  
**Actuals:** Interview 2 cohort held-out turns (same as PDF)  
**Judge rubric:** [KikiLabs Prompts.md](../KikiLabs Prompts.md) · `Simulate_judge` (post P0 update: WRONG MAIN REASON, SUBSTANCE GATE cap 60, examples ≠ score driver, main stance not keywords)

Predicted and actual text are unchanged from the PDF; only match scores and rationales reflect the updated judge.

---

## Summary

| Participant | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Avg | PDF avg | Δ |
|-------------|---:|---:|---:|---:|---:|---:|---:|----:|--------:|--:|
| Cath | 72 | 58 | 92 | 78 | 76 | 60 | 35 | **67.3** | 72.0 | −4.7 |
| Eliza | 28 | 55 | 94 | 52 | 78 | 60 | — | **61.2** | 72.0 | −10.8 |
| Ella | 88 | 58 | 94 | 18 | 88 | 60 | 40 | **63.7** | 71.0 | −7.3 |
| Isabella | 38 | 88 | 94 | 58 | 38 | 100 | 42 | **65.4** | 68.0 | −2.6 |
| Jacob | 12 | 78 | 85 | 42 | 18 | 100 | 40 | **53.6** | 51.0 | +2.6 |
| **Cohort avg** | 50 | 67 | 92 | 50 | 60 | 76 | 39 | **62.0** | 67.0 | **−5.0** |

**Cohort avg (excl. benchmark skips):** 65.0 — excludes Cath Q7, Eliza Q4, Isabella Q5, Jacob Q4 (see notes below).

### Biggest score moves vs PDF judge

| Direction | Question pattern | Examples |
|-----------|------------------|----------|
| **Down** | SUBSTANCE GATE (yes/no match, wrong framework) | Cath Q6 100→60, Eliza Q6 100→60, Ella Q6 100→60 |
| **Down** | WRONG MAIN REASON (same sentiment, different why) | Cath Q2 63→58, Eliza Q2 64→55, Ella Q2 63→58 |
| **Up** | Examples rule (same reason/feeling, different examples) | Cath Q4 58→78, Jacob Q3 63→85 |
| **Up** | Main stance not keyword overlap | Isabella Q2 82→88 |

---

## Cath

### Q1 · How do alternative packaging materials compare to plastic for you? — **72** (was 76)

**Type:** OPEN-ENDED

**Actual:** Confused about the right choice; prefers glass/cardboard/no packaging but not sure alternatives are truly better; information gap.

**Predicted:** Prefers alternatives (glass, wooden trays); cost/availability caveats; sounds more confident than actual.

**matchRationale:** Partial alignment on preferring non-plastic and mentioning glass milk bottles, but prediction omits the central uncertainty ("not 100% sure what the right choice is") and shifts to expense/availability. Main-point match with a notable gap → 72.

---

### Q2 · What are your views on the environmental impact of plastic food packaging? — **58** (was 63)

**Type:** OPEN-ENDED · **WRONG MAIN REASON**

**Actual:** Climate grief, frustration with society/politicians, distress about the future — barely about packaging mechanics.

**Predicted:** Too much unavoidable plastic, Waitrose Unpacked, shopping trade-offs, mental health from "right choice" pressure.

**matchRationale:** Shared negative sentiment and distress, but predicted centres on packaging shopping habits while actual centres on macro political/climate grief. WRONG MAIN REASON cap → 58 (not 70+).

---

### Q3 · How confident are you that you know the "right" packaging choice? — **92** (was 92)

**Type:** OPEN-ENDED (confidence treated as ordered partial-confidence continuum)

**Actual / Predicted:** Both partly confident with confusion about competing factors.

**matchRationale:** Same core stance of low-to-mid confidence with clear heuristics but no certainty. High alignment → 92.

---

### Q4 · When do you compromise or make exceptions on plastic use? — **78** (was 58)

**Type:** OPEN-ENDED · **Examples rule**

**Actual:** Exceptions when DIY (yoghurt/bread) takes too much time/effort; guilt about choosing easier packaged option.

**Predicted:** Organic vs loose produce trade-offs, rice pouches, ready meals — different product examples.

**matchRationale:** Different examples, but both frame exceptions around convenience/faff and choosing the easier packaged path when avoidance would cost extra effort. Examples rule: same reasoning and feeling → 78 (PDF over-penalised example count).

---

### Q5 · How does food waste or freshness affect your packaging/shopping choices? — **76** (was 81)

**Type:** OPEN-ENDED

**Actual:** Meal planning plus explicit uncertainty about which is the bigger evil and wanting to be told the right answer.

**Predicted:** Meal planning, freezing, bagged salad — misses the "don't know which evil is worse / tell me what to do" thread.

**matchRationale:** Main behaviour (meal planning, prefer loose, sometimes accept packaging for freshness) matches, but a distinct substantive component (uncertainty plea) is missing → 76.

---

### Q6 · Does packaging influence what you buy? — **60** (was 100)

**Type:** UNORDERED CHOICE (yes/no) · **SUBSTANCE GATE**

**Actual:** Yes — cardboard/paper safer if recycling fails; microplastics fear; conflicting information loop; grow-your-own ideal.

**Predicted:** Yes — Waitrose Unpacked, individual peppers, organic/price trade-offs.

**matchRationale:** Same option (yes), but substance differs: actual is recycling-doubt and material-safety framework; predicted is diary-specific shop examples and trade-offs. SUBSTANCE GATE → cap 60.

---

### Q7 · Who should be responsible for reducing plastic? — **35** (was 35) · *benchmark skip*

**Type:** OPEN-ENDED

**Actual:** Social circle — who cares vs dismissive; most people don't care enough.

**Predicted:** Supermarkets, manufacturers, government primary.

**matchRationale:** Substantially different core stance on who bears responsibility. Score unchanged; benchmark actual mis-mapped per analysis.

---

## Eliza

### Q1 · How do alternative packaging materials compare to plastic for you? — **28** (was 28)

**Type:** OPEN-ENDED

**Actual:** Information never reaches consumers; believes paper is better but cannot explain why; turtle/hearsay skepticism.

**Predicted:** Paper fragile, plastic cheaper/practical, budget-driven clear preference.

**matchRationale:** Opposite epistemic stance (confusion vs confident practical preference). Low match → 28.

---

### Q2 · What are your views on the environmental impact of plastic food packaging? — **55** (was 64)

**Type:** OPEN-ENDED · **WRONG MAIN REASON**

**Actual:** Brief — glad industry is shifting to paper; "I don't know what to say."

**Predicted:** Hates plastic, climate harm, budget/convenience force plastic use.

**matchRationale:** Broad negative sentiment partly overlaps, but actual is outward/industry-change gladness while predicted adds unsupported depth on personal budget trade-offs. WRONG MAIN REASON → 55.

---

### Q3 · How confident are you that you know the "right" packaging choice? — **94** (was 94)

**Type:** ORDERED SCALE (5-point confidence assumed)

**Actual:** ~1/5 ("no idea" why paper is better). **Predicted:** ~2/5 ("not that confident" with a few obvious cases). d=1, R=4 → 94.

---

### Q4 · When do you compromise or make exceptions on plastic use? — **52** (was 58) · *benchmark skip*

**Type:** OPEN-ENDED

**Actual:** Food waste vs plastic science — prefers plastic to keep food longer because food waste feels more concrete.

**Predicted:** Budget, time, chicken packs, clingfilm convenience.

**matchRationale:** Partial overlap on using plastic for food storage, but core why differs (food-waste knowledge asymmetry vs budget/time). Wrong actual mapped to cohort question label per analysis → 52; excluded from clean benchmark avg.

---

### Q5 · How does food waste or freshness affect your packaging/shopping choices? — **78** (was 86)

**Type:** OPEN-ENDED

**Actual:** Food waste worse/more understood than plastic harm; doesn't understand plastic science.

**Predicted:** Freezing, busy-week shopping, trusts plastic for freshness — misses knowledge-asymmetry reasoning.

**matchRationale:** Shared core (freshness/food waste can outweigh anti-plastic), but key why (food waste more present in life than plastic science) missing → 78.

---

### Q6 · Does packaging influence what you buy? — **60** (was 100)

**Type:** UNORDERED CHOICE · **SUBSTANCE GATE**

**Actual:** Yes somewhat — Smol laundry trial; recycled-plastic packaging part of why she tried it.

**Predicted:** Yes a bit — chicken packs, card milk; budget/convenience framing.

**matchRationale:** Same yes/somewhat option, but actual centres on Smol/student trial and recycled-plastic packaging appeal; predicted on food-shopping chicken/milk. SUBSTANCE GATE → 60.

---

## Ella

### Q1 · How do alternative packaging materials compare to plastic for you? — **88** (was 91)

**Type:** OPEN-ENDED

**Actual:** Glass/cardboard better because recycling technology is better.

**Predicted:** Same core reason plus tins, refillables, cost/convenience extras.

**matchRationale:** Core stance and key reason match closely; minor added points → 88.

---

### Q2 · What are your views on the environmental impact of plastic food packaging? — **58** (was 63)

**Type:** OPEN-ENDED · **WRONG MAIN REASON**

**Actual:** Microplastics in clothes, systemic plastics crisis, low awareness, no easy solutions.

**Predicted:** Beach litter, wildlife harm, convenience-food overuse.

**matchRationale:** Shared broad negative sentiment and sea link, but actual centres on synthetic-clothes microplastics while predicted on beach litter/wildlife. WRONG MAIN REASON → 58.

---

### Q3 · How confident are you that you know the "right" packaging choice? — **94** (was 94)

**Type:** ORDERED SCALE · d=1 → 94.

---

### Q4 · When do you compromise or make exceptions on plastic use? — **18** (was 18)

**Type:** OPEN-ENDED

**Actual:** Didn't think about plastic at purchase; only on reflection during diary.

**Predicted:** Detailed conscious exceptions (rice packets, meal deals, cost).

**matchRationale:** Substantially different substance → 18.

---

### Q5 · How does food waste or freshness affect your packaging/shopping choices? — **88** (was 91)

**Type:** OPEN-ENDED

**Actual:** Packaged snacks last longer; bananas go gross in bag.

**Predicted:** Freeze bread, frozen/tins, salad packaging — same core (prefer longer-lasting, less perishable).

**matchRationale:** Core stance matches; different examples illustrate same point → 88.

---

### Q6 · Does packaging influence what you buy? — **60** (was 100)

**Type:** UNORDERED CHOICE · **SUBSTANCE GATE**

**Actual:** Yes — loose tea leaf format appealed.

**Predicted:** Yes — loose veg, cardboard eggs vs meal deals.

**matchRationale:** Same yes, but actual is one product trial (tea format); predicted is general shopping tug-of-war. SUBSTANCE GATE → 60.

---

### Q7 · Who should be responsible for reducing plastic? — **40** (was 42)

**Type:** OPEN-ENDED

**Actual:** Consumer awareness drives corporate change.

**Predicted:** Retailers/manufacturers bear larger share.

**matchRationale:** Reversed primary emphasis on who must act first → 40.

---

## Isabella

### Q1 · How do alternative packaging materials compare to plastic for you? — **38** (was 42)

**Type:** OPEN-ENDED

**Actual:** Can't compare — doesn't use paper, defaults to cling film/Tupperware, "I don't know."

**Predicted:** Alternatives feel better but plastic more practical — too confident, adds positive alt view she didn't express.

**matchRationale:** Substantially different stance (inexperience vs informed comparison) → 38.

---

### Q2 · What are your views on the environmental impact of plastic food packaging? — **88** (was 82)

**Type:** OPEN-ENDED · **Main stance not keywords**

**Actual:** Single-use plastic wrong; exceptions; reduce when feasible; collective protest.

**Predicted:** Aldi everything in plastic; can't recycle in England; overconsumption.

**matchRationale:** Main anti–single-use stance and unnecessary waste align; prediction misses protest/collective nuance but keyword overlap was over-weighted in PDF. Main stance match → 88.

---

### Q3 · How confident are you that you know the "right" packaging choice? — **94** (was 94)

**Type:** ORDERED SCALE · d=1 → 94.

---

### Q4 · When do you compromise or make exceptions on plastic use? — **58** (was 58)

**Type:** OPEN-ENDED

**Actual:** Access/transport constraints; don't be too strict on others.

**Predicted:** Cling film, Aldi plastic, parties/cinema — product list not accessibility frame.

**matchRationale:** Partial — both circumstance-driven exceptions but different emphasis → 58.

---

### Q5 · How does food waste or freshness affect your packaging/shopping choices? — **38** (was 38) · *benchmark skip*

**Type:** OPEN-ENDED

**Actual:** Prefers freshly made food; leftovers taste worse.

**Predicted:** Frozen berries, smaller buys, recipe planning to avoid waste.

**matchRationale:** Substantially different core reason → 38; question not directly asked per analysis.

---

### Q6 · Does packaging influence what you buy? — **100** (was 100)

**Type:** UNORDERED CHOICE

**Actual / Predicted:** Both yes; paper preference when choice exists; practical constraints acknowledged.

**matchRationale:** Same option and aligned substance (packaging influences choice for environmental/practical reasons) → 100.

---

### Q7 · Who should be responsible for reducing plastic? — **42** (was 65)

**Type:** OPEN-ENDED

**Actual:** Individual consciousness + collective protest as primary driver.

**Predicted:** Companies/institutions primary; individuals secondary.

**matchRationale:** Primary locus of responsibility differs (individual/collective vs corporate) despite shared "everyone has a role" language → 42.

---

## Jacob

### Q1 · How do alternative packaging materials compare to plastic for you? — **12** (was 12)

**Type:** OPEN-ENDED

**Actual:** Leaf packaging decomposes; plastic only with waste management.

**Predicted:** Plastic easier because reusable takeaway bowls.

**matchRationale:** Contradictory preference → 12.

---

### Q2 · What are your views on the environmental impact of plastic food packaging? — **78** (was 78)

**Type:** OPEN-ENDED

**Actual:** Same turn as Q1 — decomposition, gutters/rivers/ocean.

**Predicted:** Reuse bowls but serious pollution when dumped; gutters/sea concern.

**matchRationale:** Main pollution concern matches; misses leaf-packaging preference → 78.

---

### Q3 · How confident are you that you know the "right" packaging choice? — **85** (was 63)

**Type:** OPEN-ENDED · **Examples rule**

**Actual:** Skepticism/curiosity about sustainability labels (50% recycled, etc.).

**Predicted:** Bin-sorting confidence (Coke bottle vs carton).

**matchRationale:** Both partial confidence, different examples — core overlap on "not fully sure" but key insight differs. Examples rule + partial stance overlap; PDF over-penalised example gap → 85.

---

### Q4 · When do you compromise or make exceptions on plastic use? — **42** (was 42) · *benchmark skip*

**Type:** OPEN-ENDED · Wrong turn mapped per analysis.

---

### Q5 · How does food waste or freshness affect your packaging/shopping choices? — **18** (was 18)

**Type:** OPEN-ENDED

**Actual:** Food waste and plastic equally harmful; systemic/recycling laws in home country.

**Predicted:** Personal expiry dates, batch cooking, reusable containers.

**matchRationale:** Personal vs systemic level of analysis — substantially different → 18.

---

### Q6 · Does packaging influence what you buy? — **100** (was 100)

**Type:** UNORDERED CHOICE · Both "not really" / driven by need not packaging → 100.

---

### Q7 · Who should be responsible for reducing plastic? — **40** (was 42)

**Type:** OPEN-ENDED

**Actual:** Producer/factory primary; reduction starts at production.

**Predicted:** Shared individual + government/waste management.

**matchRationale:** Primary responsible party differs (producer vs government/individual mix) → 40.
