# Eliza · Run 5 Benchmark (Selective Lenses · GPT-5.4 · Blind)

**Run 5** · Selective lenses · Model: GPT-5.4 · **Blind rerun (Jul 2026)**  
**Evidence:** `E-Data.md` · **Lenses:** `E-Lenses.md` (2 per question)  
**Actual:** `Cohort-based questions.md` (Interview 2, held-out)  
**Method:** Predictions were regenerated in a fresh blind subagent using only calibration files after this chat had already opened scored benchmark files; held-out actuals were used only afterward for scoring.

---

## Summary

| # | Question | Score |
|---|----------|------:|
| 1 | How do alternative packaging materials c… | **80** |
| 2 | What are your views on the environmental… | **49** |
| 3 | How confident are you that you know the … | **81** |
| 4 | How does food waste or freshness affect … | **91** |
| 5 | Does packaging influence what you buy? | **52** |
| **Mean** | | **70.6** |
| **Mean (excl. Q5)** | | **75.3** |

| Metric | Run 5 (blind) | Run 4 | Δ |
|--------|--------------:|------:|--:|
| Mean | **70.6** | 70.2 | +0.4 |
| Mean (excl. Q5) | **75.3** | 76.8 | -1.5 |

---

## Question 1 · How do alternative packaging materials compare to plastic for you?

**Question type:** OPEN-ENDED · **Actual turn:** Eliza #75  
**Lenses:** `Category beliefs` · `Media and cultural signals`

### Actual response

> Again this is awful to say but just this information never gets to us. People just say it is better to have paper and I always believe that it is because that's what I've been hearing since I was little. I've never got the information why is it better. Because now you're asking me this and I was like yeah, I mean paper is better, but why is it better and I have no idea because I don't understand the science behind it or what happens to the paper after, I have no idea. I don't know why is it better. I think its better because people say its better. And they always say something like, yeah use paper, lets save the turtles. Why? Why, because I mean obviously if you throw plastic to the sea its going to be worse than throwing paper but its just as bad as throwing paper. So I don't understand why its that bad, but I don't think that information comes to us either way.
>
> They always talk about the big things but they never go to the actual, yeah you should do this because this happens, which sometimes that happens is [53:58] for example. At least in [home country].

### Predicted response

> So I feel like people say the paper one or the non-plastic one is probably better, and I kind of agree with that, but I do not really know enough to explain why properly, to be honest. For me the only thing is paper sometimes feels more fragile and like it will not last as long, so then I just trust plastic more if I need the food to keep.

### Score: **80**

**matchRationale:** Open-ended. The clean blind rerun now leads with the held-out thread's central hearsay and information-gap stance ("people say the non-plastic one is better, but I don't really know why") before adding calibration-backed fragility and shelf-life concerns. It still misses the stronger "information never gets to us" and "save the turtles" / sea-pollution examples, but the main point is aligned.

---

## Question 2 · What are your views on the environmental impact of plastic food packaging?

**Question type:** OPEN-ENDED · **Actual turn:** Eliza #71  
**Lenses:** `Tensions & contradictions` · `Needs, motivations, emotional states`

### Actual response

> I think its definitely something that is changing because I do see a lot of things just being like with paper and things like, so I think its changing and I'm glad it is. I am glad is it. Yeah I don't know what to say.

### Predicted response

> Yeah, I do think plastic food packaging is bad for the environment and I do not love how much of it there is. But to be honest I am also the person who still buys it because it is cheaper and easier, so I 100% agree with using less of it, I just do not always feel like I can choose that.

### Score: **49**

**matchRationale:** Open-ended. The blind prediction captures real anti-plastic sentiment and the budget-driven contradiction that are both present in calibration, but the actual answer is much briefer and more outward-looking: she mainly notices that industry seems to be shifting toward paper and says she is glad about that. Related topic, but the focal insight is still only partially matched.

---

## Question 3 · How confident are you that you know the "right" packaging choice?

**Question type:** OPEN-ENDED · **Actual turn:** Eliza #75  
**Lenses:** `Media and cultural signals` · `Barriers & frictions`

### Actual response

> *(See Question 1 actual response.)*

### Predicted response

> Not very confident, to be honest, because I feel like the rules are not that clear and people say different things. If it is really obvious, like cardboard or a thick plastic tray with the recycle symbol, then fine, but the small thin plastics are the ones where I am just like I do not know what I am supposed to do.

### Score: **81**

**matchRationale:** Open-ended. The rerun strongly captures low confidence, unclear rules, conflicting advice, and thin-film ambiguity, which are all calibration-consistent expressions of her uncertainty. The actual thread is slightly more about not understanding why paper is better than plastic, rather than about bin-sorting rules specifically, so this is strong but not exact.

---

## Question 4 · How does food waste or freshness affect your packaging/shopping choices?

**Question type:** OPEN-ENDED · **Actual turn:** Eliza #112  
**Lenses:** `Tensions & contradictions` · `Routines & occasions`

### Actual response

> Yeah I don't know because again its not that I can't be impartial because I don't know the science behind the plastic in terms of yes I know its bad for the environment because I saw that it is but I don't understand why. Like specifically what is the thing that is so bad about plastic? Ok yeah assuming that the plastic is not going to go in, throwing at the sea and polluting, but what is the thing about plastic that is so bad, I don't understand that. While with food I understand what is so bad about wasting food. I've seen the damaging in the, the people that don't have access to food and stuff like that and I know how much it costs to buy food because obviously I pay for food so, its something that I have more present in my life than what plastic waste actually is. So I think I would prefer to buy something in plastic that can make, yeah that can make food longer, that just buy something in paper and then the food goes bad. Because I think maybe its just because its something that is more present in my life because I know how bad it is to just, I mean I've seen how bad it is to not get food. I know there are people that cannot have food. I know how much it costs to get money and then to buy food. So yeah it's a bit like that. I think I just don't know the science behind plastic that much.

### Predicted response

> A lot, actually. I hate wasting food, so even if I do not love the packaging, I will choose whatever helps food last or makes it easier to store and freeze, especially when uni gets busy. If I know something will go off fast, that really puts me off.

### Score: **91**

**matchRationale:** Open-ended. Same underlying tradeoff as the actual: food waste is more immediate and concrete than abstract plastic harm, so freshness, longevity, and freezer-friendliness drive the choice even when packaging is not ideal. The rerun is shorter and drops the explicit "I don't know the science behind plastic" line, but the substance still matches closely.

---

## Question 5 · Does packaging influence what you buy?

**Question type:** OPEN-ENDED · **Actual turn:** Eliza #13 (laundry / Smol)  
**Lenses:** `Shopping & decisions` · `Price & value`

### Actual response

> The first time I started using capsules was this year. Because last year obviously we were on those laundries on campus and to be fair I do have a lot of clothes so I don't have to do laundry every week. And to be fair I think when you're on campus it's a lot different because every time you go and do laundry on campus be there like once a week to twice a week, every time you go there its like £6. So it something that like for a student I had flat mates going and like yeah I have to go twice a week where that's almost £10. It is a lot. So you start managing that. And in terms of, I don't know because, yeah last year I bought a liquid for example, its like a whole litre of liquid and it lasted forever. And then, but then obviously I started realising how frequently I need to do my washing and everything, which is not that frequently because I have enough clothes. So yeah and it depends because sometimes you have trials, for example these last capsules that I bought was because I was part of a trial or something.
>
> Yeah its kind of a trial of a student discount, its like ok we'll give you all a box with like 10 capsules and then if you want you can continue and buy it or you don't. So obviously there is some things and then a lot of promotions that are related to students, so it depends. I don't know which one I prefer to be honest. I think they're basically the same. I think if you do washing more frequently the definitely liquid.
>
> So I mean basically I just, I think I just found it randomly on Instagram I think. Because there's a student at uni and she was promoting this.
>
> Yeah. I think there is a student at university and she was promoting this because like washing capsules like made out of recycling, it was something like that and I don't know these are really directed to students and I don't know I was just curious and I was like ok yeah sure. Yeah and then basically they offer the first 10 and then you can continue or you just stop. And I was like ok why not. Because I never tried capsules and to be fair I prefer to pay like £1-2 for those capsules than go to an actual grocery shop and spend like £5 on capsules that I don't know if I'm going to like. I don't know its just, and it's a good way, yeah you're going to have things to wash for the next month, one month, to months and yeah for like, it's a trial. I don't know.
>
> I think, in terms of the brand I think they sell more things, they sell like dishwasher machines, type of thing, but we don't have one so there was no point. But I think its just cleaning products honestly.
>
> I think so. I can give you the brand if you want. I can give you the name of the brand if you want to search.
>
> Its just, yeah I think their thing is they do, the plastic around the liquid basically, that involves the liquid, its made out of recycling plastics. I think its something like that. I think its something like that. And then they make it in smaller amounts so they don't have to waste as much. Like enough liquid to do a washing, but in small amounts so you don't have to waste as much plastic. I think its something like that.
>
> Its called Smol.

### Predicted response

> Yeah, it does, but mostly because of practicality and price. If one option feels cheaper, easier to store, or like it will last longer, I will probably buy that one, even if the packaging is more plastic than I would ideally want.

### Score: **52**

**matchRationale:** Open-ended. This clean blind rerun improves over the earlier food-only "not really" answer by conceding that packaging can influence buying, which does move it closer to the held-out turn's yes-leaning direction. It still misses the laundry / Smol student-trial context and the eco-packaging specifics that actually drove the purchase, so it remains only a partial match.
