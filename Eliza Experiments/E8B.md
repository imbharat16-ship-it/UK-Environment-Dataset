# Eliza · Run 8 Benchmark (Run 4 predictions · updated Simulate_judge)

**Run 8** · Re-score only (Jul 2026)  
**Source predictions:** `E4B.md` (Run 4 · Selective lenses · 2 lenses/question + tone)  
**Actuals:** `Cohort-based questions.md` (Interview 2, held-out)  
**Judge rubric:** [KikiLabs Prompts.md](../KikiLabs Prompts.md) · `Simulate_judge` (post P0 update)

Predicted and actual text unchanged from Run 4; only match scores and rationales reflect the updated judge.

**Scope note:** Run 4 selective-lens predictions and post P0 re-judges exist for Cath (`C4B.md`), Eliza (`E4B.md`), Isabella (`I4B.md`), and Jacob (`J4B.md`). For cohort-wide re-scores of platform PDF simulations, see Run 7 (`E7B.md`).

---

## Summary

| # | Question | Run 4 | Run 8 | Δ | Rule applied |
|---|----------|------:|------:|--:|--------------|
| 1 | Alternative materials vs plastic | 79 | **86** | +7 | Main stance match |
| 2 | Environmental impact of plastic | 52 | **65** | +13 | WRONG MAIN REASON (partial industry-shift alignment) |
| 3 | Confidence in "right" choice | 84 | **88** | +4 | — |
| 4 | Food waste / freshness | 92 | **96** | +4 | Captures food-waste vs plastic-science why |
| 5 | Packaging influences buying | 44 | **44** | 0 | Calibration ceiling (food shop vs Smol #13) |
| **Mean** | | **70.2** | **75.8** | **+5.6** | |
| **Mean (excl. Q5)** | | **76.8** | **83.8** | **+7.0** | |

---

## Question 1 · How do alternative packaging materials compare to plastic for you? — **86** (was 79)

**Type:** OPEN-ENDED · **Actual turn:** Eliza #75

### Actual response

> Again this is awful to say but just this information never gets to us. People just say it is better to have paper and I always believe that it is because that's what I've been hearing since I was little. I've never got the information why is it better. Because now you're asking me this and I was like yeah, I mean paper is better, but why is it better and I have no idea because I don't understand the science behind it or what happens to the paper after, I have no idea. I don't know why is it better. I think its better because people say its better. And they always say something like, yeah use paper, lets save the turtles. Why? Why, because I mean obviously if you throw plastic to the sea its going to be worse than throwing paper but its just as bad as throwing paper. So I don't understand why its that bad, but I don't think that information comes to us either way.
>
> They always talk about the big things but they never go to the actual, yeah you should do this because this happens, which sometimes that happens is [53:58] for example. At least in [home country].

### Predicted response (Run 4)

> Yeah so, this is awful to say but like, this information never really gets to us. People just say yeah use paper, paper is better, and I always believe that because that's what I've been hearing since I was little, but I've never got the information of why is it better. I don't understand the science or what happens to the paper after. They always talk about the big things but they never go to the actual yeah you should do this because this happens.
>
> In terms of how I actually think about them — plastic is just cheap and easy, that's honestly the first thing. Paper I think is a lot more fragile? Like it needs more care, and I have this feeling it won't last as much, so the food goes off sooner and I have to come back to the shop sooner. I don't have the time or money for that with uni and work.
>
> Glass I would never put in the same place as paper or plastic. At home we had the yellow plastic, green glass, blue paper bins and I thought that scheme was everywhere, and when I came here the boxes had no colours so I was really confused at the beginning. Thick plastic like the chicken tray obviously recycles; thin film I usually just bin because it's so small and our boxes are outside. Milk cartons I'm lost — cardboard outside but I don't know if there's plastic inside, and it doesn't say where it goes. So yeah, if that makes sense.

**matchRationale:** OPEN-ENDED. Prediction opens with the actual's core hearsay and information-gap stance verbatim in spirit; adds practical material comparisons from calibration. Omits "save the turtles" and sea-pollution examples but main substance and sentiment align strongly → 86.

---

## Question 2 · What are your views on the environmental impact of plastic food packaging? — **65** (was 52)

**Type:** OPEN-ENDED · **WRONG MAIN REASON (partial)** · **Actual turn:** Eliza #71

### Actual response

> I think its definitely something that is changing because I do see a lot of things just being like with paper and things like, so I think its changing and I'm glad it is. I am glad is it. Yeah I don't know what to say.

### Predicted response (Run 4)

> Yeah I mean, I do care about the environment — I'm very aware we should be doing things for climate change and I agree with that. And I know plastic food packaging is bad, like I would prefer to buy less of it, I hate that so much stuff comes in plastic.
>
> But to be fair there's a tension there because when I go shopping I'm a uni student on a budget, and there are just way more options in plastic than not. So I end up buying plastic even though I know I shouldn't, which I don't love.
>
> Since this study I've been paying more attention — like oh everything in my fridge is plastic, and I notice when the thick plastic is different from the thin crunchy stuff. I think I do see more things in paper now as well, which is good. But it hasn't really changed what I buy because I still can't spend £2-3 more just for paper — like £2 is a bus ticket. Yeah I don't know what to say.

**matchRationale:** OPEN-ENDED. Prediction includes actual's key thread ("see more things in paper now, which is good") and closes with the same "I don't know what to say," but still centres budget/tension more than actual's brief industry-shift gladness. WRONG MAIN REASON cap applies but partial alignment is stronger than Run 4 scored → 65.

---

## Question 3 · How confident are you that you know the "right" packaging choice? — **88** (was 84)

**Type:** OPEN-ENDED (confidence) · **Actual turn:** Eliza #75

### Actual response

> *(See Question 1 actual response.)*

### Predicted response (Run 4)

> Not that confident, to be honest.
>
> For the environment side, people say paper is better and I believe that because I've always heard it, but why is it better? I have no idea. This information never really gets to us properly. They always talk about the big things but they never go to the actual yeah you should do this because this happens.
>
> For recycling it's also confusing. Growing up we had the colour scheme — yellow plastic, green glass, blue paper — and I thought that was everywhere. Here the boxes don't have colours and I had to ask my flatmates. I've heard people saying yeah recycle this and then others saying no you shouldn't. If there's that green thing with the arrows that helps, but a lot of things don't say anything. Milk cartons — I know they can be recycled but I don't know if it's paper or plastic or both. Thin plastics are the worst — am I supposed to recycle all plastics? I probably should know but I don't. And our recycling boxes are outside so for something really small and thin I'm like, is it even worth going out for that, while the chicken tray obviously makes sense. Yeah I kind of go with what people say, if that makes sense.

**matchRationale:** OPEN-ENDED. Core low-confidence stance and "people say paper better / don't know why" match strongly. Adds recycling logistics beyond held-out thread but does not contradict. Main point with minor gaps → 88.

---

## Question 4 · How does food waste or freshness affect your packaging/shopping choices? — **96** (was 92)

**Type:** OPEN-ENDED · **Actual turn:** Eliza #112

### Actual response

> Yeah I don't know because again its not that I can't be impartial because I don't know the science behind the plastic in terms of yes I know its bad for the environment because I saw that it is but I don't understand why. Like specifically what is the thing that is so bad about plastic? Ok yeah assuming that the plastic is not going to go in, throwing at the sea and polluting, but what is the thing about plastic that is so bad, I don't understand that. While with food I understand what is so bad about wasting food. I've seen the damaging in the, the people that don't have access to food and stuff like that and I know how much it costs to buy food because obviously I pay for food so, its something that I have more present in my life than what plastic waste actually is. So I think I would prefer to buy something in plastic that can make, yeah that can make food longer, that just buy something in paper and then the food goes bad. Because I think maybe its just because its something that is more present in my life because I know how bad it is to just, I mean I've seen how bad it is to not get food. I know there are people that cannot have food. I know how much it costs to get money and then to buy food. So yeah it's a bit like that. I think I just don't know the science behind plastic that much.

### Predicted response (Run 4)

> Yeah so food waste is a big thing — that's the only thing in my house we don't waste food. My mum always taught me you can always do something with it unless it's gone off. So I hate throwing food away because it's wasting money.
>
> That affects how I shop. Before I travel I buy things in jars or frozen stuff and fewer vegetables because I know I won't use them in time. Like I had a quiche and froze it because it was going to go off. I stretch meals too — kilo of chicken for curry and enchiladas, then leftovers for noodles. At the end of term I batch cook curry into freezer boxes because I won't have time to cook every day.
>
> There's a tension with packaging because I want less plastic but paper feels like it won't last as long, so the food might go bad sooner and that's more waste and another shop. So if something keeps food fresh longer that's better for me, even if it means more plastic — wasting the actual food feels worse than the packaging. I don't know the science behind plastic, but food waste I understand because I pay for food and I know how much it costs, if that makes sense.

**matchRationale:** OPEN-ENDED. Prediction captures the actual's core tradeoff and explicitly includes the key why: food waste is more present/understood than plastic science ("I don't know the science behind plastic, but food waste I understand"). Same substance and sentiment → 96.

---

## Question 5 · Does packaging influence what you buy? — **44** (was 44)

**Type:** OPEN-ENDED · **Actual turn:** Eliza #13 (laundry / Smol)

### Actual response

> The first time I started using capsules was this year. Because last year obviously we were on those laundries on campus and to be fair I do have a lot of clothes so I don't have to do laundry every week. And to be fair I think when you're on campus it's a lot different because every time you go and do laundry on campus be there like once a week to twice a week, every time you go there its like £6. So it something that like for a student I had flat mates going and like yeah I have to go twice a week where that's almost £10. It is a lot. So you start managing that. And in terms of, I don't know because, yeah last year I bought a liquid for example, its like a whole litre of liquid and it lasted forever. And then, but then obviously I started realising how frequently I need to do my washing and everything, which is not that frequently because I have enough clothes. So yeah and it depends because sometimes you have trials, for example these last capsules that I bought was because I was part of a trial or something.
>
> *(Full Smol trial thread — see E4B.md.)*
>
> Its called Smol.

### Predicted response (Run 4)

> I mean, a little bit, but not as much as price and whether it fits my meals. When I'm at Aldi I'm doing the maths in my head — like if I buy the kilo chicken that's cheaper and it'll give me four meals if I do it right, and if I have two work shifts that's four meals I don't need to worry about. I'm comparing prices and weights, not walking around looking for the least packaging.
>
> Plastic influences it a bit because I know I hate how much stuff is in plastic and if I could I'd buy less. But there aren't that many options that aren't in plastic, and I'm on a budget, so I usually buy what's cheaper even if it's plastic. I wouldn't pay £2-3 more for paper — like £2 is a bus ticket.
>
> The only times I really notice are carrier bags — I never buy the 10p ones, we have reusable bags — or milk, I prefer the cardboard carton because it's what I'm used to from home. Since this study I've noticed packaging more but it hasn't changed what I buy. So yeah, budget and meals come first, if that makes sense.

**matchRationale:** OPEN-ENDED. Actual centres on laundry/Smol trial where recycled-plastic packaging influenced the try; predicted centres on food-shopping budget logic with no Smol thread. Substantially different substance despite both touching "packaging a little bit" → 44 unchanged (calibration ceiling).

---

## Run 8 vs Run 4 judge delta

| Rule | Effect on Run 4 Eliza scores |
|------|------------------------------|
| **Main stance not keywords** | Q2 +13 (industry-shift line now credited) |
| **WRONG MAIN REASON** | Q2 capped but less harsh than pure miss |
| **Examples / key-why emphasis** | Q4 +4 (plastic-science ignorance explicit in prediction) |
| **SUBSTANCE GATE** | N/A — Run 4 Q5 scored as open-ended, not yes/no |

Run 8 mean **75.8** vs Run 4 **70.2** (+5.6) under updated judge; prediction quality unchanged.
