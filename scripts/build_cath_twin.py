#!/usr/bin/env python3
"""Generate Cath Twin.md from extracted transcripts and P0 summaries."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
I2_PATH = ROOT / ".extracted/cath/20220531_Interview_2_Cath.txt"
OUT_PATH = ROOT / "Cath Twin.md"

FILLER = re.compile(
    r"^(ok|yeah|right|sure|no|oh|well|so|thanks|thank you|that's ok|that's okay|i see|great|perfect|absolutely|mm|hmm|sorry|yes|are you sure)\.?$",
    re.I,
)

# turn_num (1–69 consecutive substantive A turns) -> (type, patterns)
TURN_META: dict[int, tuple[str, str]] = {
    1: ("R+B", "`identity_green`, `garden_grow`"),
    2: ("B", "`activism_social`, `identity_green`"),
    3: ("B", "`activism_social`, `occasion_travel`"),
    4: ("B", "`occasion_travel`, `attgap_plastic`"),
    5: ("R+B", "`reuse_garden`, `attgap_plastic`, `garden_grow`"),
    6: ("C", "(inherits 5)"),
    7: ("B", "`identity_green`, `attgap_plastic`"),
    8: ("C", "(comfort — skip simulation)"),
    9: ("C", "(comfort break)"),
    10: ("B", "`recycling_high`, `attgap_plastic`"),
    11: ("B", "`recycling_high`, `attgap_plastic`"),
    12: ("B", "`recycling_high`, `reuse_garden`"),
    13: ("C", "(inherits 12)"),
    14: ("B", "`activism_social`, `recycling_high`"),
    15: ("B", "`meal_plan`, NEW nutrition lens"),
    16: ("B", "`meal_plan`, `foodwaste_chain`"),
    17: ("R+P", "`reuse_garden`, `recycling_high`"),
    18: ("B", "`reuse_garden`"),
    19: ("R+B", "`reuse_garden`, `pricing_split`, `attgap_plastic`"),
    20: ("B", "`reuse_garden`, `pricing_split`"),
    21: ("C", "(inherits 19)"),
    22: ("R", "`reuse_garden`"),
    23: ("C", "(inherits 22)"),
    24: ("B", "`recycling_high`, `identity_green`"),
    25: ("B", "`recycling_high`, NEW household_driver"),
    26: ("C", "(inherits 25)"),
    27: ("R", "`occasion_travel`, `meal_plan`"),
    28: ("R+B", "`recycling_high`, `meal_plan`, `attgap_plastic`"),
    29: ("B", "`foodwaste_chain`, `meal_plan`"),
    30: ("B", "`foodwaste_chain`, `attgap_plastic`"),
    31: ("B", "`identity_green`, `activism_social`"),
    32: ("C", "(inherits 31)"),
    33: ("R", "(transition to diaries)"),
    34: ("C", "(comfort check)"),
    35: ("R", "`occasion_travel`"),
    36: ("C", "(inherits 35)"),
    37: ("C", "(inherits 35)"),
    38: ("R", "`occasion_travel`"),
    39: ("C", "(inherits 38)"),
    40: ("R+B", "`recycling_high`, `occasion_travel`"),
    41: ("B", "`occasion_travel`, `recycling_high`"),
    42: ("C", "(inherits 41)"),
    43: ("R+B", "`reuse_garden`, `recycling_high`"),
    44: ("C", "(inherits 43)"),
    45: ("R", "`occasion_monday`, `foodwaste_chain`"),
    46: ("B", "`foodwaste_chain`, `meal_plan`"),
    47: ("R", "`occasion_travel`"),
    48: ("P", "`occasion_travel`, `attgap_plastic`"),
    49: ("B", "`occasion_travel`, `attgap_plastic`"),
    50: ("C", "(inherits 49)"),
    51: ("R", "`reuse_garden`, `occasion_travel`"),
    52: ("R", "`reuse_garden`, `occasion_travel`"),
    53: ("R", "`occasion_travel`, `attgap_plastic`"),
    54: ("R+P", "`reuse_garden`, `occasion_travel`"),
    55: ("B", "`reuse_garden`"),
    56: ("R+B", "`occasion_travel`, `recycling_high`"),
    57: ("R+B", "`occasion_travel`, `attgap_plastic`, `pricing_split`"),
    58: ("B", "`recycling_high`, `attgap_plastic`"),
    59: ("C", "(inherits 58)"),
    60: ("C", "(inherits 57)"),
    61: ("R+P", "`occasion_monday`, `meal_plan`, `foodwaste_chain`"),
    62: ("R", "`occasion_monday`, NEW friday_ritual"),
    63: ("C", "(inherits 62)"),
    64: ("R", "`occasion_travel`"),
    65: ("B", "`occasion_travel`, `meal_plan`"),
    66: ("P", "`pricing_split`, `attgap_plastic`, `meal_plan`"),
    67: ("C", "(inherits 66)"),
    68: ("C", "(inherits 66)"),
    69: ("C", "(closing)"),
}

TURN_PARAPHRASE: dict[int, str] = {
    1: "Going back to Interview 1, why are you anti-pesticide and pro wildlife gardening?",
    2: "Do you also campaign on Twitter about plastic and food packaging?",
    3: "What do you mean by taking a break from environmental pressure on weekends and bank holidays?",
    4: "Does taking a step back from Twitter also extend to packaging choices when travelling?",
    5: "You reuse yoghurt pots for garden labels — why don't you make your own bread, cakes, or yoghurt?",
    6: "When you say you make it difficult, do you mean making bread and cakes yourself?",
    7: "Can you say more about how deeply you feel about environmental issues?",
    8: "I don't want you to get too upset — shall we pause this line of questioning?",
    9: "Would you like a five-minute comfort break before we continue?",
    10: "How do cardboard, glass, and paper packaging compare to plastic for you?",
    11: "Why do you sometimes steer toward cardboard rather than plastic or paper?",
    12: "How do you handle soft plastics and compost bags that go to Tesco?",
    13: "That's good — shall we continue?",
    14: "Do you try to tell friends and family about peat-free compost and plastic packaging?",
    15: "You once considered a career in nutrition — can you tell me about that interest?",
    16: "How do you apply your nutrition knowledge in everyday meal planning?",
    17: "In your week-one kitchen video, what plastic did you reuse for seedlings?",
    18: "Do certain plastics need a 'junk' quality to be worth reusing in the garden?",
    19: "When we shopped at Waitrose together, what changed with the Yeo Valley yoghurt packaging?",
    20: "Is the Yeo Valley lid/token offer still running at Waitrose?",
    21: "Thank you for explaining the Yeo Valley packaging change.",
    22: "You had kept Yeo Valley lids as plant-pot stands — tell me more.",
    23: "So you've brought those lids back into the kitchen for reuse?",
    24: "How did you get on with Greenpeace's Big Plastic Count?",
    25: "What is your husband's view on recycling and reuse compared with yours?",
    26: "Does he support your habits in practice?",
    27: "When you went to London for the day, what happened to packaging at home?",
    28: "If you leave a Charlie Bigham meal for your husband, what happens to the packaging?",
    29: "How does your meal planning relate to both food waste and plastic waste?",
    30: "On a scale, which feels worse environmentally: food waste or plastic waste?",
    31: "How do you respond to documentaries and media about plastic pollution?",
    32: "Does avoiding distressing documentaries work for you?",
    33: "Shall we take a break before moving on to diary entries?",
    34: "You've been talking for about an hour — are you still ok to continue?",
    35: "Let's move to week three diary entries — the week I visited, starting the 9th?",
    36: "Does that week still feel recent given everything in between?",
    37: "I remember you saying that.",
    38: "Actually week three was the week before my visit — the bank holiday week commencing the 2nd?",
    39: "So that's the bank holiday weekend week commencing 2nd May?",
    40: "In that week you were away for the bank holiday — what soft plastics did you set aside?",
    41: "Tell me about the Falmouth apartment bin room and its recycling facilities.",
    42: "That's interesting — I hadn't heard of that setup before.",
    43: "Before you travelled, you colour-coded packaging destinations — why did some bread bags go to reuse?",
    44: "What is the difference between bread bags you reuse versus recycle?",
    45: "On Monday 2nd bank holiday, before you went away — tell me about that day.",
    46: "You had feta for lunch and kept half in the freezer — how does that work?",
    47: "When you were away, you hand-wrote diary entries — tell me about that.",
    48: "Tell me about National Trust brunch packaging waste from your photos.",
    49: "What did you think of vegetable-protein knives and milk containers?",
    50: "Let me know if you remember more about those disposables.",
    51: "On Thursday 5th May away, you ate hot cross buns — what happened to the film bag?",
    52: "I didn't expect the hot-cross-bun bag to be that type of reuse.",
    53: "Your children bought water bottles on Thursday — tell me about those.",
    54: "We touched on this when I visited — you had bottles in the kitchen.",
    55: "You cut a bottle in half for raised-bed irrigation — tell me more.",
    56: "On Sunday you brought crisp bags, bread bags, and foil home — why?",
    57: "Tell me about the M&S service-station sandwiches you brought home.",
    58: "Why did you try to separate the M&S sandwich box plastic lining?",
    59: "The box said recyclable — were you unsure about the lining?",
    60: "Was that sandwich packaging from Marks & Spencer?",
    61: "In week four you planned prawn and avocado salad as a Friday treat — tell me more.",
    62: "What did you mean by preparing ahead for Friday evening drinks?",
    63: "Eurovision isn't too far away now.",
    64: "On Saturday 14th you had a quick lunch before cinema — tell me more.",
    65: "Why is having a quick, healthy meal significant before going out?",
    66: "In your shop video you bought four different cheeses — why so many?",
    67: "That's fantastic!",
    68: "You're eating some of your favourite foods while we talk.",
    69: "That's all my questions — end of interview.",
}

ARC_TURNS: list[tuple[str, str, str, list[int]]] = [
    (
        "A",
        "Gardening philosophy & activism",
        "Parents' wildlife gardening; Twitter campaigning; stepping back on holidays; travel packaging concessions in Falmouth.",
        [1, 2, 3, 4],
    ),
    (
        "B",
        "Yoghurt pots, DIY limits & environmental distress",
        "Yoghurt pot reuse; guilt about not making bread/yoghurt; deep feelings on climate; comfort break.",
        [5, 6, 7, 8, 9],
    ),
    (
        "C",
        "Packaging materials: glass, cardboard vs plastic",
        "Compares glass/cardboard/paper to plastic; confusion about which is truly better.",
        [10, 11],
    ),
    (
        "D",
        "Soft plastics, compost bags & social evangelism",
        "Soft plastics to Tesco; compost sacks; peat compost; telling friends about recycling.",
        [12, 13, 14],
    ),
    (
        "E",
        "Nutrition, whole foods & meal planning",
        "Nutrition interest; ultra-processed foods; Sunday meal planning from scratch.",
        [15, 16],
    ),
    (
        "F",
        "Reuse, Yeo Valley yoghurt & household recycling",
        "Seedling plastic junk; sturdy vs flimsy plastic; Yeo Valley lids; Greenpeace count; husband as supporter.",
        list(range(17, 26)),
    ),
    (
        "G",
        "Food waste vs plastic, media & Charlie Bigham",
        "London trip ready meal; food waste vs plastic tradeoff; documentary distress; transition to diaries.",
        list(range(26, 35)),
    ),
    (
        "H",
        "Week 3 diary: bank holiday & Falmouth travel",
        "Soft plastics; Falmouth bin room; bread bag reuse; feta freezer; National Trust brunch; water bottles; M&S sandwiches.",
        list(range(35, 61)),
    ),
    (
        "I",
        "Week 4 diary: Friday treats & cheese shop",
        "Prawn Friday salad; prepare-ahead for drinks; quick Saturday lunch; four cheeses video.",
        list(range(61, 70)),
    ),
]


def parse_transcript(text: str) -> list[dict]:
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    turns: list[dict] = []
    current = None
    for line in lines:
        if line.startswith("A:"):
            if current:
                turns.append(current)
            current = {"speaker": "A", "text": line[2:].strip()}
        elif line.startswith("B:"):
            if current:
                turns.append(current)
            current = {"speaker": "B", "text": line[2:].strip()}
        elif current:
            current["text"] += " " + line
    if current:
        turns.append(current)
    return turns


def pairs_from_turns(turns: list[dict]) -> list[tuple[dict, dict | None]]:
    pairs: list[tuple[dict, dict | None]] = []
    i = 0
    while i < len(turns):
        if turns[i]["speaker"] == "A":
            a = turns[i]
            b = turns[i + 1] if i + 1 < len(turns) and turns[i + 1]["speaker"] == "B" else None
            pairs.append((a, b))
            i += 2 if b else 1
        else:
            i += 1
    return pairs


def classify_a(text: str) -> str:
    t = text.lower()
    if any(x in t for x in ["picture", "photo", "video", "look at this", "image", "photograph"]):
        return "P"
    if any(
        x in t
        for x in [
            "going back to your first interview",
            "going back to your interview",
            "earlier videos",
            "week three diary",
            "week four diary",
            "diary entry",
            "when i came to visit",
            "when i visited",
            "touched upon i think when i visited",
        ]
    ):
        return "R"
    if len(text) < 25 or FILLER.match(text.strip()):
        return "C"
    return "B"


def paraphrase(text: str) -> str:
    q = text.strip()
    q = re.sub(r"^(so |and |well |ok |yeah )", "", q, flags=re.I)
    if not q.endswith("?"):
        q = q.rstrip(".") + "?"
    if len(q) > 130:
        q = q[:127] + "..."
    return q[0].upper() + q[1:] if q else q


def verbatim_snippet(text: str, limit: int = 95) -> str:
    s = re.sub(r"\s+", " ", text.strip())
    if len(s) > limit:
        return s[: limit - 3] + "..."
    return s


def header_section() -> str:
    return """# Cath Twin

**Source:** Cath (Phase 1) · extracted from `P0_PARTICIPANT_SUMMARIES.md`  
**Scope:** Step summaries · Behavioral lens summary · I2 callback map · Behavior-tagged I2 (69 turns) · Full I2 transcript  
**Archetype:** C · High-practice homeowner  
**Profile:** 57, semi-retired former teacher / casual exam invigilator; Green Party member; four-bed semi with garden, wildlife pond, and extensive home growing. Meal planner; shops Waitrose on foot, Aldi/Tesco by car.

### Interview 2: Can simulate (selected turns)

_Add manually after tagging turns in the arc tables below (append ` · CAN SIMULATE` to turn numbers). Copy type, paraphrase, and patterns from tagged rows._

| # | Type | Paraphrased question | Behavioral patterns |
|---|------|---------------------|---------------------|

"""


def step_summaries() -> str:
    return """### Step summaries

#### Interview 1 (Step 0) · Cath — 18,237 words · 92,437 characters

**Themes:**

- **Household/home:** Lives with husband; two grown-up children living elsewhere; four-bed semi with garden used for summer growing (tomatoes, salad, etc.); wildlife pond and wildlife-friendly garden.
- **Routines:** Casual exam invigilation with flexible volunteer schedule; spends significant time gardening; Sunday morning meal planning.
- **Shopping:** Shops Waitrose on foot (~twice weekly); Aldi/Tesco by car for bulk/cheaper items; sister's household nearly self-sufficient in home-grown veg by comparison.
- **Food/preparation:** Eats seasonally; home-grown chillies chopped and frozen for year-round use; cooks from scratch with meal plans; roast chicken example stretched across wraps, lunches, and later pasta.
- **Plastic packaging:** Uses far less plastic packaging in summer when growing; in winter buys more wrapped produce (e.g. bagged salad often wasted and composted).
- **Disposal/recycling:** Heavy recycler; soft plastics collected in pantry bag for supermarket drop-off; compost sacks with recycling symbol (number 4); reuses many trays and pots in garden until they fall apart.
- **Reuse:** Waste plastic reused for garden seedlings; mushroom/dessert trays for seedlings; stopped clingfilm in favour of bread bags; Tupperware for leftovers and freezing; freezer storage discussed in interview.

**Behavioral lenses:** Identity (Green Party member, environmental gardener), Culture/social (family food norms, sister's home-growing contrast), Pricing/value (Waitrose vs Aldi/Tesco split), Convenience tradeoff (meal planning), Recycling diligence (soft-plastic collection, compost-sack schemes), Reuse tendency (garden trays, bread bags, Tupperware), Food waste sensitivity (meal planner, seasonal growing, bagged-salad caution).

---

#### Diary 1 (Step 1) — 590 words · 3,684 characters

**Themes:**

- Full week logged Monday 18th through Sunday 24th April; colour-coded disposal (red landfill, green kerbside, blue Tesco soft plastics, orange reuse).
- **Monday:** Home day; chicken/tray meals; wine box bag recycled; compost bag and water-butt kit reused in garden.
- **Tuesday:** Waitrose shop (video); mackerel tray, potato salad from loose potatoes; husband packed lunch with biscuits from big pack (no individual wrappers).
- **Wednesday:** Day out in London — coffee/lunch/dinner out, no takeaway packaging; Charlie Bigham curry in wooden boxes + film at home.
- **Thursday:** Waitrose trolley shop; fajita pasta from leftover defrosted chicken; cheese pack to Tesco soft plastics; afternoon potting tomatoes in reused plastic pots.
- **Friday–Sunday:** Mix of Charlie Bigham ready meals, gardening, homemade meals; soft plastics from crisp packs, ready-meal films, biscuit trays; Sunday heavier plastic day (covid test, bread/muesli/gnocchi bags, yogurt pot).

**Behavioral lenses:** Occasion (weekly rhythm, London day out), Identity (committed participant), Recycling diligence (Tesco soft plastics, tray recycling), Reuse tendency (garden pots, compost bag), Food waste sensitivity (leftover chicken chain).

---

#### Diary 2 (Step 2) — 747 words · 4,600 characters

**Themes:**

- Second week Monday 25th through Saturday 30th April; continued colour-coded logging.
- **Monday:** Deli wraps from Waitrose (film bag); nut burgers; hot cross bun plastic.
- **Tuesday:** Garden centre trip (plant pot stickers); falafel plastic bag; veggie kievs tray/film.
- **Wednesday:** Tesco shop + soft plastics drop-off at store; homemade spinach curry with shop-bought bhajis/naans (lots of trays/film).
- **Thursday:** Teabag film; Waitrose top-up; dinner out locally while husbands eat orzo/prawn pasta at home (prawn bag, cake film).
- **Friday:** Bin day — green bin nearly full of two weeks' recycling; heavy plastic day (yogurt pot, garden matting film, bird coconut film, biscuit tray).
- **Saturday–Sunday:** Craft market + Waitrose; concludes **majority of plastic waste is soft film/bags** not council-recycled; Charlie Bigham ready meal Sunday with £4.50 off.

**Behavioral lenses:** Occasion, Convenience tradeoff (ready meals, shop-bought sides), Recycling diligence (Tesco soft plastics, bin-day audit), Reuse tendency, Food waste sensitivity, Attitude-behavior gap (knows soft plastics problem, still accumulates film).

---

#### Follow-up interview 1 (Step 3) · Cath — 5,563 words · 28,485 characters

**Themes:**

- **Study reflexivity:** Really enjoying the diary; will miss it when finished; gives daily purpose; has always thought about packaging but now engages more deliberately.
- **Pantry video:** Packets of rice in pantry, including microwaveable pouches; feels guilty every time ("such a lot of packaging"); knows she should cook rice from scratch but is "absolutely terrible" at cooking rice.

**Behavioral lenses:** Identity (self-aware environmentalist), Convenience tradeoff (rice pouches), Attitude-behavior gap (guilt vs continued use), Culture/social (enjoys study participation).

---

#### Diary 3 (Step 4) — 326 words · 2,003 characters

**Themes:**

- **Bank holiday Monday (2nd May):** Veggie burgers + defrosted soup; feta half-block frozen; lemon/orange net bags; minimal waste day before travel.
- **Tuesday 3rd:** Packing/cleaning; Waitrose small shop; mushroom bake from scratch with garden chives/salad; notes from May onward buys less fruit/veg as garden produces.
- **Wednesday 4th–Sunday 8th May — Falmouth:** Handwritten diary; self-catering apartment; ate out heavily (four adults); brought soft plastics home; apartment bin room with sorted cardboard/glass; M&S service-station sandwiches (mixed-material packaging confusion); National Trust brunch with disposable packaging; children bought water bottles (reused in garden); hot cross bun giant Aldi bag saved for reuse.

**Behavioral lenses:** Occasion (bank holiday, travel, Falmouth), Convenience tradeoff (away-from-home eating), Recycling diligence (bin room praise, bring soft plastics home), Reuse tendency (bread bags, hot cross bun bag, water bottles), Attitude-behavior gap (travel packaging vs home standards).

---

#### Diary 4 (Step 5) — 772 words · 4,603 characters

**Themes:**

- **Monday 9th:** Post-Falmouth; quick soup + veggie burgers (typical Monday meal); extra burger frozen for plastic-free packed lunch; gardening priority.
- **Tuesday 10th:** Oxford brunch with friend; mackerel + garden herb potato salad; planned for leftovers.
- **Wednesday 11th:** Oxford bus trip; refilled hand soaps; bubble wrap reused for frost protection; meal out + cinema (no takeaway waste).
- **Thursday 12th:** Fajita pasta from freezer chicken; Thursday = more exciting scratch-cook night; leftovers for lunch.
- **Friday 13th:** Prawn and avocado salad (Friday treat); prepare-ahead for evening drinks/crisps/chat; haloumi/ciabatta asparagus meal.
- **Saturday 14th:** Quick feta/tomato/artichoke lunch before cinema; husband's frittata dinner; Eurovision evening.
- **Sunday 15th:** Tray-bake veggie curry; cauliflower/cucumber/spinach plastic despite garden glut approaching.

**Behavioral lenses:** Occasion (Monday quick vs Fri–Sun treats, cinema, post-holiday reset), Recycling diligence, Reuse tendency, Food waste sensitivity (freezer, leftovers, garden herbs), Pricing/value (Monday cheap meals).

---

#### Follow-up interview 2 (Step 7) · Cath — 4,276 words · 22,521 characters

**Themes:**

- **Leftovers and planning:** Some meals lend themselves to leftovers; plans midweek so husband has packed lunches; meal-planning video shared.
- **Weekly tempo:** Monday = quicker, lower-priority meal ("back to work vibe"); weekends more special; spends more on food toward end of week, bank holidays, and weekends.
- **Quick Monday meal:** Small folded deli wraps (pitta-like) with burger filling.
- **Freezer routine:** Two freezers (pantry fridge-freezer for peas, chips, etc.); each morning thinks about what to pull from freezer for dinner.
- **Shopping friction:** Heroes/Celebrations chocolates bought for husband's sailing event; she would object; competing concerns can spoil otherwise enjoyable shopping trips.
- **Packaging tradeoffs:** Buys larger cheese blocks when cheaper or less packaging; still troubled by "nasty" pouches.

**Behavioral lenses:** Occasion (Monday vs weekend, sailing gifts), Convenience tradeoff (frozen veg, deli wraps), Pricing/value (bulk cheese), Food waste sensitivity (leftover planning), Attitude-behavior gap (objects to celebration tins), Recycling diligence.

---

#### Interview 2 (held out) · Cath — 17,690 words · 89,592 characters

**Themes:**

- **Gardening philosophy:** Values inherited from parents; "live and let live" rather than spraying/killing garden pests; wants birds and hedgehogs in the garden; moves snails away from lettuces by hand.
- **Activism:** Uses Twitter to message supermarkets (e.g. plastic carrier bags, Waitrose coffee cups); signs petitions; takes breaks on weekends/holidays for mental health.
- **Material choices:** Prefers glass as better recycled but reads conflicting claims about glass weight/energy; feels confused; yoghurt pots reused yet still many accumulate.
- **Travel:** When travelling (Falmouth), must sometimes accept plastic packaging avoided at home; brings soft plastics home; impressed by apartment bin room.
- **Growing vs buying:** Satisfaction when home cucumbers and other produce reduce need to shop for wrapped equivalents.
- **Food vs plastic tradeoff:** Accepts plastic can extend shelf life (cucumbers) but gut feeling plastic worse; meal planning keeps both under control.
- **Diary callbacks:** Rice pouches guilt; Monday meals; freezer routine; celebration tins; cheese block; Falmouth travel; Yeo Valley lids; four-cheese shop video.

**Behavioral lenses:** Identity (lifelong environmental values), Culture/social (Twitter, petitions, husband as facilitator), Attitude-behavior gap (travel packaging, rice pouches, yoghurt volume), Recycling diligence (glass vs plastic confusion, soft plastics), Reuse tendency (yoghurt pots, garden trays, bread bags), Occasion (Falmouth, out-and-about meals), Food waste sensitivity (meal planning vs packaging tradeoff).

---

"""


def lens_and_callbacks() -> str:
    return """### Behavioral lens summary across steps

| Step | Primary lenses |
| ---- | -------------- |
| Interview 1 | Identity, Recycling diligence, Reuse tendency, Food waste sensitivity, Pricing/value |
| Diary 1 | Occasion, Identity, Recycling diligence, Reuse tendency |
| Diary 2 | Occasion, Recycling diligence, Reuse tendency, Attitude-behavior gap (soft plastics) |
| Follow-up 1 | Attitude-behavior gap, Convenience tradeoff, Identity |
| Diary 3 | Occasion (travel/Falmouth), Recycling diligence, Reuse tendency, Attitude-behavior gap |
| Diary 4 | Occasion (Monday vs weekend), Food waste sensitivity, Recycling diligence, Pricing/value |
| Follow-up 2 | Occasion, Food waste sensitivity, Attitude-behavior gap, Convenience tradeoff, Pricing/value |
| Interview 2 | Identity, Activism, Reuse tendency, Attitude-behavior gap, Occasion (travel), Food waste sensitivity |

---

### Where Interview 2 draws from (human summary)

Interview 2 is a closing conversation. The interviewer often **looks back** at what Cath said or did earlier in the study. When Cath answers, she is usually pulling from one of these earlier layers:

| Earlier material | What Cath goes back to |
| ---------------- | ---------------------- |
| **Interview 1** | Green Party identity, wildlife gardening, soft-plastics pantry bag, Waitrose vs Aldi/Tesco split, Sunday meal planning, roast-chicken leftover chain, garden reuse of trays/pots, summer vs winter packaging |
| **Diary 1–2** | Weekly Waitrose shops, Charlie Bigham ready meals, soft-plastic film accumulation, London day out, gardening + reused pots |
| **Follow-up 1** | Microwave rice pouches in pantry and guilt about using them |
| **Diary 3** | Bank holiday Monday feta-freezer habit; Falmouth travel; National Trust brunch packaging; M&S sandwiches; bin room; bringing soft plastics home |
| **Diary 4** | Monday quick soup/burgers; Friday prawn salad + prepare-ahead for drinks; Saturday cinema quick lunch; four-cheese shop video |
| **Follow-up 2** | Monday deli wraps; morning freezer check; Heroes/Celebrations for sailing; large cheese block tradeoff; leftover planning for husband |
| **Home visit (Step 7 fieldwork)** | Waitrose shop together; Yeo Valley yoghurt lids; children’s water bottles; garden bottle irrigation; bread-bag drawer |

Two kinds of look-back happen:

1. **She (or the interviewer) says it out loud** — e.g. "going back to your first interview…", "week three diary entry", "when I came to visit you and we went to Waitrose". These are the clearest callbacks.
2. **She doesn't name it, but the answer only makes sense with earlier context** — e.g. bread-bag reuse logic draws on Interview 1 clingfilm replacement, even when the question is about a rolls bag from Diary 3.

**Topics that mostly stand alone in Interview 2** (little prior material): parents' garden philosophy in depth, Greenpeace Big Plastic Count, nutrition book revelation (four cheeses), Eurovision/cinema evening, detailed Twitter activism mechanics.

#### By Interview 2 theme

**Gardening & identity**

- Goes back to **Interview 1**: wildlife pond, no pesticides, garden reuse, seasonal growing
- Adds **new depth**: snail-moving, fondness for "bad guys", parents as origin of values

**Activism & media**

- **Interview 1 / I2 new**: Twitter supermarket campaigns, petition signing, Waitrose coffee cup win
- **I2 new**: skips distressing documentaries; reads practical magazine articles instead

**Materials & recycling**

- **Interview 1**: soft plastics bag, compost sacks, glass milk bottles, tray reuse
- **Home visit / I2**: Yeo Valley lid change, bread-bag types, M&S mixed-material sandwich box
- **I2 new**: glass vs plastic confusion; vegetable-protein disposables scepticism

**Travel & away-from-home**

- **Diary 3**: Falmouth apartment, bin room, National Trust brunch, service-station sandwiches
- **Follow-up 2 / I2**: Charlie Bigham for husband when Cath in London; children’s water bottles

**Meal planning & food waste**

- **Interview 1 + Follow-up 2**: Sunday planning, Monday quick meals, freezer routine, leftovers for husband
- **Diary 4 / I2**: Friday prawn treat, prepare-ahead for drinks, Saturday quick lunch before cinema

**Attitude–behavior gaps**

- **Follow-up 1**: rice pouch guilt (implicit in nutrition/whole-food thread)
- **Follow-up 2**: celebration tins, "nasty" pouches
- **I2**: travel packaging concessions; not making own yoghurt/bread despite guilt

#### The short version

If you imagine Cath's "memory" for Interview 2, it is weighted toward:

1. **Interview 1** — baseline green identity, garden, recycling, meal planning
2. **Diary 3 (Falmouth week)** — the travel week the interviewer probes hardest
3. **Follow-up 2** — Monday tempo, freezer routine, celebration tins, cheese tradeoff
4. **Home visit + Diary 4** — Yeo Valley lids, Friday rituals, cheese shop video
5. **Follow-up 1** — rice pouches (lighter touch in I2)

About **4 topics** in Interview 2 are genuinely new depth (parents' philosophy, Big Plastic Count results, nutrition/diabetes book, documentary avoidance coping strategy). Everything else revisits something she already said, photographed, or showed on video.

---

"""


def behavior_tagged_section(pairs: list[tuple[dict, dict | None]]) -> str:
    lines = [
        "## Interview 2: Behavior-Tagged Questions (Full Transcript)",
        "",
        "### Core reframing: simulate behavior, not lived experience",
        "",
        "The summarized question list in `P0_PARTICIPANT_SUMMARIES.md` has **~20 paraphrased questions**. The actual transcript (`857315_data/Households11_20/Household16Cath/20220531_Interview_2_Cath.docx`) has **69 substantive interviewer turns** (77 total `A:` lines including short follow-ups).",
        "",
        "For a twin, the goal is **not** to reproduce whether Cath remembers \"on Thursday I ate hot cross buns in Falmouth.\" That is fact recall / lived experience.",
        "",
        "The goal **is** to reproduce **how she behaves** when a situation arises:",
        "",
        "| Situation type | Behavioral pattern to simulate |",
        "| -------------- | ------------------------------ |",
        "| High-practice homeowner | Sort soft plastics to Tesco; rinse trays; reuse bread bags and garden trays |",
        "| Seasonal growing | Buy less wrapped produce in summer; satisfaction when cucumbers/tomatoes ready |",
        "| Meal planning | Sunday folder planning; Monday quick meals; Friday treats; freezer for surplus cheese |",
        "| Activism | Twitter petitions; polite supermarket emails; weekend breaks from distressing news |",
        "| Travel occasion | Accept more packaging away from home; bring soft plastics home; prefer sit-down café cups |",
        "| Attitude–behavior gap | Guilt about rice pouches, yoghurt pots, travel disposables; still uses some |",
        "| Social evangelism | Tell friends about Tesco soft plastics; some dismiss her as \"funny like that\" |",
        "",
        "**Tagging logic:** Each I2 turn gets tagged with **which behavioral patterns from prior steps should activate** — not which diary photo to cite.",
        "",
        "### Question type legend",
        "",
        "| Type | Meaning | Twin approach |",
        "| ---- | ------- | ------------- |",
        "| **B** | Behavior probe | Simulate decision logic from calibrated patterns |",
        "| **F** | Fact recall | Weak for twin — dates, brands, specific diary days |",
        "| **P** | Photo elicitation | Needs photo/video context OR generalize to food-type behavior |",
        "| **C** | Clarification / follow-up | Continues prior turn; inherits parent tags |",
        "| **R** | Reflexive look-back | Interviewer names prior step; twin should **re-express known patterns** |",
        "",
        "### Behavioral pattern library (from prior steps)",
        "",
        "| Pattern ID | Source | What to simulate |",
        "| ---------- | ------ | ---------------- |",
        "| `identity_green` | I1, I2 | Green Party member; lifelong environmental values; distress at climate harm |",
        "| `garden_grow` | I1, D3, I2 | Home growing reduces wrapped produce; seasonal split; wildlife-friendly garden |",
        "| `meal_plan` | I1, FU2, D4 | Sunday planning; leftovers for husband; whole-food from-scratch cooking |",
        "| `occasion_monday` | FU2, D4 | Quick Monday meals vs weekend special food |",
        "| `occasion_travel` | D3, I2 | Falmouth / away-from-home packaging concessions; bring soft plastics home |",
        "| `recycling_high` | I1, D2 | Soft-plastics pantry bag; compost sacks; heavy sorting; rinse before recycle |",
        "| `reuse_garden` | I1, I2 | Trays/pots/yoghurt pots/bread bags/water bottles reused until discarded |",
        "| `attgap_plastic` | FU1, FU2, I2 | Rice pouch guilt; celebration tins; travel packaging; yoghurt volume |",
        "| `pricing_split` | I1 | Waitrose on foot vs Aldi/Tesco by car; Yeo Valley vs Aldi yoghurt |",
        "| `foodwaste_chain` | I1, FU2 | Roast chicken stretched; feta frozen; meal planning prevents waste |",
        "| `activism_social` | I2 | Twitter supermarket messaging; petitions; polite campaigning letters |",
        "",
        f"### Full transcript: {sum(len(a) for _, _, _, a in ARC_TURNS)} tagged turns in {len(ARC_TURNS)} conversational arcs",
        "",
        "Each turn has three question layers:",
        "",
        "1. **Paraphrased question** — clean, standalone question for twin prompting/evaluation",
        "2. **Verbatim turn** — what the interviewer actually said",
        "3. **Behavioral patterns** — which calibrated patterns to activate (not factual recall)",
        "",
    ]

    turn_lookup: dict[int, tuple[dict, dict | None, str]] = {}
    turn_num = 0
    for a, b in pairs:
        if len(a["text"]) < 15:
            continue
        turn_num += 1
        turn_lookup[turn_num] = (a, b, TURN_PARAPHRASE.get(turn_num, paraphrase(a["text"])))

    for arc_id, title, summary, turn_nums in ARC_TURNS:
        lines.append(f"#### Arc {arc_id}: {title} (turns {turn_nums[0]}–{turn_nums[-1]})")
        lines.append("")
        lines.append(f"**Arc summary (paraphrased):** {summary}")
        lines.append("")
        lines.append("| # | Type | Paraphrased question | Verbatim turn | Behavioral patterns |")
        lines.append("| - | ---- | -------------------- | ------------- | ------------------- |")
        for n in turn_nums:
            if n not in turn_lookup:
                continue
            a, _, para = turn_lookup[n]
            typ, patterns = TURN_META.get(n, (classify_a(a["text"]), "`identity_green`"))
            lines.append(
                f"| {n} | {typ} | {para} | {verbatim_snippet(a['text'])} | {patterns} |"
            )
        lines.append("")

    lines.extend(
        [
            "### Summary: what the twin loads for each arc",
            "",
            "| Arc | Twin loads | Weak for simulation |",
            "| --- | ---------- | ------------------- |",
            "| A | Green identity, live-and-let-live garden, Twitter activism, travel packaging guilt | — |",
            "| B | Reuse guilt loop, DIY limits, climate distress | Comfort-break turns |",
            "| C | Material preference hierarchy (none > cardboard/glass > plastic), confusion | — |",
            "| D | Soft-plastic hoarding, compost-bag schemes, social evangelism | — |",
            "| E | Whole-food meal planning, ultra-processed avoidance | — |",
            "| F | Garden reuse hierarchy, Yeo Valley tradeoff, husband as supporter | Token survey detail |",
            "| G | Food-waste vs plastic tradeoff, media avoidance, Charlie Bigham treat logic | — |",
            "| H | Falmouth travel behaviors, bin room, bread-bag types, National Trust mortification | Specific dates/diary day IDs |",
            "| I | Friday ritual, quick pre-cinema meals, cheese/nutrition tension | Eurovision detail |",
            "",
            "### Turns that are weak for behavior simulation",
            "",
            "- **Fact recall:** specific diary dates, \"was it Tuesday 3rd\", brand names without behavioral generalization",
            "- **Comfort / logistics:** break offers, \"are you ok\", end-of-interview closings",
            "- **Pure photo ID without pattern:** \"what is this picture\" when no prior food-type pattern exists",
            "",
            "### How this differs from the 20-question summary",
            "",
            "P0 lists ~20 paraphrased I2 questions grouped by theme (gardening, materials, travel, diary callbacks). The transcript has **69 substantive turns** because the interviewer probes follow-ups (bread-bag types, Yeo Valley lid survey, National Trust compostable cutlery scepticism, feta-freezer habit, M&S mixed-material sandwich). A twin must handle the **conversation thread**, not just the headline question.",
            "",
        ]
    )
    return "\n".join(lines)


def full_transcript_section(pairs: list[tuple[dict, dict | None]]) -> str:
    lines = ["## Interview 2 transcript (full)", ""]
    turn_num = 0
    arc_by_turn: dict[int, str] = {}
    for arc_id, _, _, nums in ARC_TURNS:
        for n in nums:
            arc_by_turn[n] = arc_id

    for a, b in pairs:
        if len(a["text"]) < 15:
            label = "**A:**"
            lines.append(f"{label} {a['text']}")
            lines.append("")
            if b:
                lines.append(f"**B:** {b['text']}")
                lines.append("")
            continue
        turn_num += 1
        arc = arc_by_turn.get(turn_num, "")
        arc_note = f" · Arc {arc}" if arc else ""
        lines.append(f"**A · #{turn_num}{arc_note}:** {a['text']}")
        lines.append("")
        if b:
            lines.append(f"**B:** {b['text']}")
            lines.append("")
    lines.append("End of interview")
    return "\n".join(lines)


def main() -> None:
    text = I2_PATH.read_text()
    turns = parse_transcript(text)
    pairs = pairs_from_turns(turns)

    substantive = sum(1 for a, _ in pairs if len(a["text"]) >= 15)

    doc = (
        header_section()
        + step_summaries()
        + lens_and_callbacks()
        + behavior_tagged_section(pairs)
        + full_transcript_section(pairs)
    )

    OUT_PATH.write_text(doc)
    print(f"Wrote {OUT_PATH} ({len(doc.splitlines())} lines)")
    print(f"Substantive turns: {substantive}")


if __name__ == "__main__":
    main()
