#!/usr/bin/env python3
"""Generate Isabella Twin.md from extracted transcripts and P0 summaries."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from isabella_data import ARC_TURNS, TURN_META, TURN_PARAPHRASE
from twin_common import (
    CAN_SIMULATE_HEADER,
    behavior_tagged_section,
    full_transcript_section,
    pairs_from_turns,
    parse_transcript,
)

I2_PATH = ROOT / ".extracted/isabella/interview_2.txt"
I2_DOCX = "857315_data/Households11_20/Household13Isabella/20220328_Final_interview_Isabella.docx"
OUT_PATH = ROOT / "Isabella Twin.md"


def header_section() -> str:
    return f"""# Isabella Twin

**Source:** Isabella (Phase 1) · extracted from `P0_PARTICIPANT_SUMMARIES.md`  
**Scope:** Step summaries · Behavioral lens summary · I2 callback map · Behavior-tagged I2 (94 turns) · Full I2 transcript  
**Archetype:** A · Student / shared household  
**Profile:** Spanish island student from Santa; third year; lives with five housemates including boyfriend Pablo (primary cook). Vegetarian (occasional chicken for gym). MBC pupil debates on plastics. Shops weekly at Aldi with wheeled caddy and reusable carriers.

{CAN_SIMULATE_HEADER}
"""


def step_summaries() -> str:
    return """### Step summaries

#### Interview 1 (Step 0) · Isabella — 13,503 words · 68,659 characters

**Themes:**

- **Household/home:** Mountain-town upbringing; family meat business; vegetarian since mid-teens despite parental opposition; complicated eating arrangements at home (grandmother, friends).
- **Routines:** Reading, films, walking; six-person house with three fridges; shared kitchen after COVID packing mix-up.
- **Shopping:** Year 1 university meal plan (parents insisted); year 2+ weekly Aldi trips with Pablo; list-based recipe planning.
- **Food/preparation:** Pablo leads cooking; batch lentil soup; breakfast wraps; occasional chicken for gym; split veg/meat versions of same meals.
- **Plastic packaging:** Strong frustration that Spain-recyclable plastics go to general waste in UK house.
- **Disposal/recycling:** Orange council bin bags only; recycling attempts failed years 1–2 (bins not collected); recycles on campus/streets but not at home.
- **Reuse:** Tupperware, clingfilm, original produce containers; accumulated thick Aldi reusable bags.

**Behavioral lenses:** Identity (vegetarian values), Culture/social (Spain vs UK recycling), Pricing/value (Aldi, frozen veg), Food waste sensitivity, Attitude-behavior gap (knows recycling, can't practice at home), Occasion (cinema, McDonald's).

---

#### Diary 1 (Step 1) — 215 words · 1,211 characters

**Themes:**

- **Tuesday:** Breakfast wraps; leftover black beans stored in original can with clingfilm.
- **Wednesday:** Pasta leftovers in Tupperware; half lemon wrapped in clingfilm.
- **Thursday:** Potato leftovers in Tupperware; ate prior pasta; quick Aldi shop (eggs, toast, frozen broccoli, nuggets, coconut milk, gum, milk); dinner = leftover potatoes + bean quesadillas.
- **Friday:** McDonald's nuggets in paper box; sauce sachets in plastic.
- **Saturday cinema:** Tap water in plastic cups; popcorn; no recycling bin (general waste only) for cups or paper holder.

**Behavioral lenses:** Reuse tendency (Tupperware, bean/can cycle), Recycling diligence (cinema frustration), Occasion (cinema, McDonald's), Culture/social (would recycle in Spain).

---

#### Diary 2 (Step 2) — 500 words · 2,674 characters

**Themes:**

- **Monday:** Weekly Aldi shop (photo); pasta sauce meal prep covered with clingfilm; half onion wrapped for later use; spinach kept in original plastic containers.
- **Wednesday:** Post-gym Aldi top-up; refused plastic bag, carried goods in tote, pockets, and hands; lunch = leftover pasta sauce; pineapple cut into Tupperware.
- **Disposal:** Chocolate brioche and almond packaging to general waste (would recycle in Spain).
- **Thursday:** Vegan/real meatball split with rice in oversized Tupperware; spare almond sauce frozen.
- **Friday:** Pasta leftovers; party with ubiquitous plastic cups.
- **Saturday–Sunday:** Banana-oat pancakes to use browning bananas; rice cake packaging to general waste (Spain-recyclable).

**Behavioral lenses:** Culture/social (Spain vs UK bins), Pricing/value (no plastic bag purchase), Food waste sensitivity (banana pancakes), Reuse tendency (containers, frozen sauce), Occasion (party, gym trip).

---

#### Follow-up interview 1 (Step 3) · Isabella — 3,511 words · 19,260 characters

**Themes:**

- **Party norms:** Pre-drinks before nightclub; plastic cups default, never ask for glass.
- **Breakfast wraps:** Eggs, beans, pepper, spinach, guacamole; weekly or fortnightly; leftover beans become quesadillas later.
- **Green goddess sauce:** Blender recipe from vegan YouTuber; Pablo adapts; batch stored for multiple pasta meals.
- **Cooking roles:** Pablo confident main cook; Isabella "sous chef," checks recipes due to poor memory.
- **Leftovers:** Lentil soup batches last 3–4 days; clingfilm preferred when Tupperware scarce (housemates' meal prep).
- **McDonald's:** Boyfriend started job there; paper nuggets box to general waste (greasy); sauce partly kept in fridge.
- **Cinema:** Tap water in plastic cup; believes Spanish cinemas sometimes recycle drinks packaging.
- **Frozen vs fresh:** Frozen broccoli/sweetcorn for specific recipes; fresh lemons non-negotiable; frozen bread to prevent waste.
- **Fridge storage:** Apples/carrots/tomatoes left in original plastic bags in fridge (no spare Tupperware).

**Behavioral lenses:** Occasion (party, cinema, McDonald's), Identity (healthy eating mindset), Reuse tendency (leftover beans), Culture/social (Spain recycling expectations), Convenience tradeoff (frozen veg/bread).

---

#### Diary 3 (Step 4) — 696 words · 3,788 characters

**Themes:**

- **Monday:** Lentil soup leftover in Tupperware.
- **Tuesday:** Bagel lunch; gym visit noting single-use plastic hydration bottles among gym-goers.
- **Wednesday (work):** Children's lunch all in plastic; MBC debate on banning plastics (reuse/recycle vs ocean harm); girl notes peers bin bottles beside recycle bin.
- **Thursday:** Greggs vegan sausage roll (paper wrapper recycled in library bin); quiche stored in glass dish with clingfilm (no Tupperware free).
- **Friday–Sunday:** Chopped tomatoes in original can + clingfilm; multiple Spain-recyclable plastics (apples, Ben & Jerry's paper, baby plum tomatoes, lettuce) to general waste; salad Tupperware wrapped in clingfilm for library day (lost reusable bag from prior term).

**Behavioral lenses:** Culture/social (school debate, Spain norms), Occasion (work, gym, library), Recycling diligence (Greggs paper at campus), Attitude-behavior gap (teaches plastic debate, house cannot recycle).

---

#### Diary 4 (Step 5) — 570 words · 3,051 characters

**Themes:**

- **Monday:** McDonald's nuggets (paper pack, extra sauce sachet wasted); lesson learned on sauce quantity.
- **Tuesday shop:** Frozen pizza with box + inner plastic wrap.
- **Wednesday:** Rice packaging to general waste (Spain-recyclable).
- **Thursday campus day:** Pasta and grapes in Tupperware; clingfilm wrap; bought Sainsbury's plastic bag to reuse instead of daily clingfilm.
- **Friday–Saturday:** M&M wrapper binned at campus (no recycling option); sunset outing litter-pick (plastic bottles left by others).
- **Sunday:** Finished Greek yogurt tub to general waste (Spain-recyclable); reused shopping bag to cover Tupperware for campus.

**Behavioral lenses:** Reuse tendency (Sainsbury's bag solution), Culture/social (Spain recycling expectations), Occasion (campus study days, castle outing), Pricing/value (small investment to reduce film waste), Food waste sensitivity (sauce portion learning).

---

#### Follow-up interview 2 (Step 7) · Isabella — 3,820 words · 20,625 characters

**Themes:**

- **MBC debates:** Primary-school plastic ban debates; "plastic should not be banned" side often wins; Isabella prompts deeper thinking (reusable bottles vs single-use).
- **Aldi routine:** Wheeled shopping caddy + thick reusable Aldi bags accumulated across six housemates; walk home, share carrying.
- **Shared kitchen:** Under-sink cupboard for carrier bags/cleaning products; communal Tupperware shelf; pans/devices shared after COVID repacking errors.
- **Photo-elicitation:** Weekly shop packaging mostly plastic; would recycle all in Spain except uncertain items (cocoa tin, lemon netting, greasy meatball tray).
- **Dirty packaging trauma:** Conference taught "dirty plastic ruins recycling"; won't touch boyfriend's meat packaging; butter tub grease uncertainty.
- **Margarine discovery:** Realised she had bought margarine for three years, not butter; switched to real butter in new packaging.
- **Post-gym shop:** Carried groceries without buying plastic bag (commonsense); interior coat pockets looked like shoplifting.

**Behavioral lenses:** Culture/social (educating children on plastics), Identity (vegetarian, won't handle meat packs), Recycling diligence (would recycle in Spain), Reuse tendency (accumulated carriers), Attitude-behavior gap (environment job vs home general waste).

---

#### Interview 2 (held out) · Isabella — 13,760 words · 70,602 characters

**Themes:**

- **Gym and diet:** Protein-focused eating; occasional chicken; frozen vegetables to reduce fresh spoilage.
- **Upbringing:** Santa mountain town; less control over food when visiting home on vacation.
- **University food journey:** Year 1 marketplace plan vs year 2+ shared cooking with Pablo.
- **End-of-term:** Deadline eating; campus days with Tupperware transport; clingfilm vs reusable bag workaround.
- **Recycling history:** Failed kerbside recycling both years; orange bags only; emotional "failure" vs Spain community norm.
- **Diary callbacks:** Gym plastic cups; McDonald's sauces; cinema waste; children's debate; Greggs paper; frozen pizza double wrap; litter picking; Sainsbury's bag; container reuse.

**Behavioral lenses:** Identity (health/fitness, vegetarian), Food waste sensitivity, Culture/social (UK recycling failure), Occasion (gym, campus, parties), Convenience tradeoff (frozen pizza, meal prep), Attitude-behavior gap.

---

"""


def lens_and_callbacks() -> str:
    return """### Behavioral lens summary across steps

| Step | Primary lenses |
| ---- | -------------- |
| Interview 1 | Identity, Culture/social, Attitude-behavior gap, Pricing/value, Food waste sensitivity |
| Diary 1 | Reuse tendency, Recycling diligence, Occasion, Culture/social |
| Diary 2 | Culture/social, Food waste sensitivity, Reuse tendency, Pricing/value, Occasion |
| Follow-up 1 | Occasion, Identity, Reuse tendency, Culture/social, Convenience tradeoff |
| Diary 3 | Culture/social, Attitude-behavior gap, Occasion, Recycling diligence |
| Diary 4 | Reuse tendency, Culture/social, Occasion, Pricing/value, Food waste sensitivity |
| Follow-up 2 | Culture/social, Identity, Recycling diligence, Reuse tendency, Attitude-behavior gap |
| Interview 2 | Identity, Culture/social, Food waste sensitivity, Occasion, Convenience tradeoff, Attitude-behavior gap |

---

### Where Interview 2 draws from (human summary)

Interview 2 is a closing conversation. The interviewer often **looks back** at what Isabella said or did earlier in the study. When she answers, she is usually pulling from one of these earlier layers:

| Earlier material | What Isabella goes back to |
| ---------------- | -------------------------- |
| **Interview 1** | Vegetarian identity; six-person shared house; Pablo as cook; Aldi weekly shop; orange bags only; failed recycling attempts; Spain vs UK bin norms; Tupperware vs thin containers |
| **Diary 1–2** | Breakfast wraps and bean quesadilla chain; cinema plastic cups; McDonald's packaging; party cups; post-gym shop without plastic bag; banana pancakes |
| **Follow-up 1** | Green goddess sauce batches; clingfilm when Tupperware scarce; frozen vs fresh veg; fridge storage in original bags; cinema/party norms |
| **Diary 3** | Gym plastic hydration bottles; MBC children's plastic debate; Greggs paper at library; quiche in glass dish with clingfilm |
| **Diary 4** | McDonald's sauce waste lesson; frozen pizza box + inner wrap; Sainsbury's bag instead of clingfilm; castle litter-pick; Greek yogurt tub |
| **Follow-up 2** | Aldi wheeled caddy and carrier accumulation; dirty-packaging trauma; margarine vs butter; weekly shop photo-elicitation; won't touch meat packs |

Two kinds of look-back happen:

1. **She (or the interviewer) says it out loud** — e.g. "going back to your first interview…", "week three diary entry", "you mentioned on Thursday 10th".
2. **She doesn't name it, but the answer only makes sense with earlier context** — e.g. gym cup frustration draws on D3 gym entry even when the question is general.

**Topics that mostly stand alone in Interview 2** (little prior material): canal walking benefits; Apple Music vs Spotify; Santa mountain-town childhood depth; Seaspiracy documentary reaction; leftover reheating psychology.

#### By Interview 2 theme

**Gym & diet**

- Goes back to **Interview 1 / D2–D3**: gym routine; occasional chicken for protein; frozen veg
- **I2 new depth**: morning gym rhythm; porridge pre-workout; eating enough after sessions

**Upbringing & university journey**

- **Interview 1 / I2**: Santa food norms; year 1 marketplace catering; year 2 shared cooking anxiety
- **D1–D2**: solo lunch waste → frozen veg; family-sized Aldi packs with Pablo

**Recycling failure**

- **Interview 1 + FU2**: orange bags; kerbside attempts; Spain community norm vs UK house
- **I2 new depth**: emotional "failure"; black/white bag experiments; student housing leaflet loop

**MBC work vs household**

- **Diary 3 + FU2**: children's plastic debates; teaches reuse while home bins everything
- **I2**: exceptions for single-use plastic; produce packaging choice logic

**Diary callbacks (weeks 3–4)**

- **D3**: gym cups (turns 55–60); MBC work (61–63); quiche/clingfilm (71–72); Greggs photo (73)
- **D4**: McDonald's (74–76); frozen pizza double wrap (77); Sainsbury's bag (81); litter pick (82–83)
- **FU1/FU2 implicit**: cinema cups, party cups, margarine/butter, dirty meat trays

**Reuse & leftovers**

- **Interview 1 + FU1**: Tupperware preference; clingfilm scarcity; cold-food aversion
- **D4 + I2 closing**: Sainsbury's bag hack; fruit-container reuse (Spain habit)

#### The short version

If you imagine Isabella's "memory" for Interview 2, it is weighted toward:

1. **Interview 1** — vegetarian identity, shared house, recycling blocked at home, Pablo cooking
2. **Follow-up 2** — Aldi routine, dirty plastic trauma, margarine discovery, MBC debates
3. **Diary 3** — gym cups, school debate, Greggs/quiche
4. **Diary 4** — McDonald's, frozen pizza, Sainsbury's bag, litter pick
5. **Follow-up 1** — party/cinema cups, breakfast wrap chain, clingfilm logic

About **5 topics** in Interview 2 are genuinely new depth (Seaspiracy, leftover psychology, brioche comparison, island litter attitudes, reheating brain categorization). Everything else revisits something she already said, photographed, or debated with children.

---

"""


PATTERN_LIBRARY = """| Pattern ID | Source | What to simulate |
| ---------- | ------ | ---------------- |
| `identity_veg` | I1, FU2, I2 | Vegetarian values; won't handle meat packaging; occasional gym chicken |
| `culture_spain_uk` | I1, D1–D4, FU1/FU2, I2 | Spain recycles community-wide; UK house orange bags only; emotional gap |
| `budget_student` | I1, D2, FU2, I2 | Aldi list shop; wheeled caddy; refuse paid plastic bags; family-sized packs |
| `recycling_blocked` | I1, D1–D4, I2 | Can't recycle at home; campus/library when available; teaches debate anyway |
| `attgap_plastic` | I1, D3–D4, FU2, I2 | Knows plastic harm; home general waste; MBC work vs own bins |
| `occasion_social` | D1–D4, FU1, I2 | Parties, cinema, McDonald's, gym — different packaging rules |
| `occasion_campus` | D3–D4, I2 | Library days, Tupperware transport, Greggs, study deadlines |
| `foodwaste_chain` | I1, D1–D4, FU1, I2 | Bean → quesadilla; batch soup; banana pancakes; sauce portion learning |
| `reuse_containers` | I1, D1–D4, FU2, I2 | Tupperware, clingfilm, Sainsbury's bag, fruit containers |
| `convenience_default` | I1, D2–D4, I2 | Frozen veg/pizza/bread; marketplace year 1; deadline eating |
| `partner_cook` | I1, FU1, I2 | Pablo leads; Isabella sous chef; shared Aldi shop |
| `mbc_work` | D3, FU2, I2 | Children's plastic debates; prompts reusable bottle thinking |
| `fitness_diet` | D2–D3, I2 | Gym mornings; protein planning; post-workout lunch |"""

SITUATION_TABLE = """| Situation type | Behavioral pattern to simulate |
| -------------- | ------------------------------ |
| Shared student house | Recycling blocked; orange bags; campus recycling workaround |
| Spain vs UK norms | Would recycle at home in Spain; general waste here; cultural frustration |
| Pablo-led cooking | Partner cooks; batch meals; veg/meat split versions |
| Social occasions | Party/cinema/gym cups to general waste; doesn't ask for glass |
| Aldi weekly shop | List planning; reusable carriers; no paid bag after gym |
| MBC plastic debates | Professional knowledge vs household inability to recycle |
| Food waste vs packaging | Frozen veg/pizza tradeoffs; bean leftover chain; sauce waste lesson |"""

ARC_SUMMARY_TABLE = """| Arc | Twin loads | Weak for simulation |
| --- | ---------- | ------------------- |
| A | Gym identity, protein planning, post-workout eating | — |
| B | Santa upbringing, broad hobbies, home food norms | Music platform detail |
| C | Year 1 catering, solo waste, frozen veg logic | Marketplace timetable |
| D | Anxious year-2 cooking, housemate meals | Specific empanada names |
| E | Recycling failure narrative, orange bags | Council contact details |
| F | Tupperware health, cold-food aversion | — |
| G | Gym cups, MBC debates, produce choice, documentaries | Specific debate dates |
| H | Quiche clingfilm, Greggs, McDonald's packaging | Diary day IDs |
| I | Frozen pizza wrap, Sainsbury bag hack, litter pick | Brioche brand detail |
| J | Leftover psychology, container reuse | Eurovision-adjacent closings |"""


def main() -> None:
    text = I2_PATH.read_text()
    pairs = pairs_from_turns(parse_transcript(text))
    substantive = sum(1 for a, _ in pairs if len(a["text"]) >= 15)

    doc = (
        header_section()
        + step_summaries()
        + lens_and_callbacks()
        + behavior_tagged_section(
            pairs,
            participant="Isabella",
            i2_path=I2_DOCX,
            substantive_count=substantive,
            arc_turns=ARC_TURNS,
            turn_meta=TURN_META,
            turn_paraphrase=TURN_PARAPHRASE,
            pattern_library_md=PATTERN_LIBRARY,
            situation_table_md=SITUATION_TABLE,
            arc_summary_table_md=ARC_SUMMARY_TABLE,
        )
        + full_transcript_section(pairs, ARC_TURNS)
    )

    OUT_PATH.write_text(doc)
    print(f"Wrote {OUT_PATH} ({len(doc.splitlines())} lines)")
    print(f"Substantive turns: {substantive}")


if __name__ == "__main__":
    main()
