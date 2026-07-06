#!/usr/bin/env python3
"""Generate Jacob Twin.md from extracted transcripts and P0 summaries."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from jacob_data import ARC_TURNS, TURN_META, TURN_PARAPHRASE
from twin_common import (
    CAN_SIMULATE_HEADER,
    behavior_tagged_section,
    full_transcript_section,
    pairs_from_turns,
    parse_transcript,
)

I2_PATH = ROOT / ".extracted/jacob/interview_2.txt"
I2_DOCX = "857315_data/Households11_20/Household15Jacob/20220601_Final_interview_Jacob.docx"
OUT_PATH = ROOT / "Jacob Twin.md"


def header_section(substantive: int) -> str:
    return f"""# Jacob Twin

**Source:** Jacob (Phase 1) · extracted from `P0_PARTICIPANT_SUMMARIES.md`  
**Scope:** Step summaries · Behavioral lens summary · I2 callback map · Behavior-tagged I2 ({substantive} turns) · Full I2 transcript  
**Archetype:** A · Student / shared household  
**Profile:** International postgraduate student, seven months in UK; from large family (10 siblings), now lives alone in shared student flat (five rooms, one kitchen). Shops Lidl, Nigerian supermarket, Eat India takeaway; batch-cooks stews stored in reused takeaway bowls.

{CAN_SIMULATE_HEADER}
"""


def step_summaries() -> str:
    return """### Step summaries

#### Interview 1 (Step 0) · Jacob — 13,184 words · 64,239 characters

**Themes:**

- **Household/home:** From [home country], family of ten; lives alone in UK; shared student flat (five rooms, one communal kitchen).
- **Routines:** Busy university schedule; uses Eat India when too tight to cook and does not want to spend time shopping for food.
- **Shopping:** Initially ate from Indian shop/restaurant; later discovered Nigerian supermarket; also shops Aldi/Lidl for cabbage and other stew ingredients; combines items from multiple stores for curry/cabbage stew.
- **Food/preparation:** UK diet very different from first months; adapted from Indian food toward Nigerian/local ingredients; batch-prepares cabbage-based stew as mainstay.
- **Plastic packaging:** Eat India serves rice and vegetables in separate small white plastic containers.
- **Disposal/recycling:** Three containers/bins in kitchen including plastics and general rubbish.
- **Reuse:** Retains takeaway bowls because he needs bowls and did not bring any from home; washes and keeps them rather than discarding after one use.

**Behavioral lenses:** Identity (international postgraduate), Culture/social (Indian then Nigerian food adaptation), Convenience tradeoff (Eat India when schedule tight), Reuse tendency (takeaway bowls as kitchenware), Pricing/value (multi-store ingredient sourcing), Attitude-behavior gap (disposable bowls kept for utility).

---

#### Diary 1 (Step 1) — 346 words · 1,875 characters

**Themes:**

- Routine-day diary across Tue/Wed/Fri (03–06/05/22).
- **Tuesday (03/05):** Busiest day of week; day starts ~8:00 after morning exercise and devotion; checks email and social media.
- **Wednesday (04/05) and Friday (06/05):** Logged as additional routine days in batch.

**Behavioral lenses:** Occasion (busy Tuesday), Culture/social (morning devotion routine), Identity (structured student week).

---

#### Diary 2 (Step 2) — 187 words · 1,063 characters

**Themes:**

- Routine-day entries: Monday (09/05), Wednesday (11/05), Friday (11/05).
- Short mid-study batch continuing day-of-week logging format.

**Behavioral lenses:** Occasion (weekday rhythm), Food waste sensitivity (implicit via planned batch-cooking lifestyle).

---

#### Follow-up interview 1 (Step 3) · Jacob — 624 words · 3,570 characters

**Themes:**

- **Routines:** Gym at least twice weekly when university schedule allows.
- **Takeaway day:** Did not want to cook; described cooking that day as a "waste of time"; bought takeaway instead.
- **Disposal:** Pepsi can from takeaway placed in kitchen plastics bin; chips packaging photographed (possibly polystyrene).
- **Shopping/cooking:** Diary documents a food-shopping trip; buys ingredients specifically to prepare [home country] stew all at once.
- **Fridge photo:** Communal fridge interior photographed (flat storage context).

**Behavioral lenses:** Convenience tradeoff (takeaway vs cook), Recycling diligence (Pepsi can sorted to plastics), Culture/social (home-country stew), Occasion (time-pressed day), Attitude-behavior gap (aware of packaging, prioritises time).

---

#### Diary 3 (Step 4) — 434 words · 2,355 characters

**Themes:**

- Routine days: Tuesday (17/05), Thursday (19/05), Sunday (22/05).
- Mid-study batch spanning the follow-up 2 period.

**Behavioral lenses:** Occasion (Sunday vs weekday), Convenience tradeoff, Reuse tendency (ongoing bowl storage from batch cooks).

---

#### Diary 4 (Step 5) — 319 words · 1,754 characters

**Themes:**

- Final diary batch: Monday (23/05), Wednesday (25/05), Friday (27/05).
- Closing week of routine-day entries before final interview.

**Behavioral lenses:** Occasion (end-of-study week), Food waste sensitivity, Reuse tendency.

---

#### Follow-up interview 2 (Step 7) · Jacob — 677 words · 3,932 characters

**Themes:**

- **Study reflexivity:** Recording daily habits is interesting; makes him think about things he normally would not notice.
- **Shopping planning:** Realised he must buy food before running out, even when very busy; normally buys in bulk and plans cooking ahead.
- **Batch stew:** After cooking, transfers most stew into plastic takeaway bowls stored in fridge; refers to containers as "plastic bowls."
- **Disposal:** Discusses what counts as plastic waste and how it is disposed of after use.

**Behavioral lenses:** Identity (reflective participant), Convenience tradeoff (bulk cook vs daily prep), Reuse tendency (bowl storage), Recycling diligence (plastic waste sorting), Attitude-behavior gap (diary raises awareness, habits change slowly).

---

#### Interview 2 (held out) · Jacob — 11,392 words · 58,384 characters

**Themes:**

- **Home country environment:** Plastic waste in gutters contributes to flooding and erosion when not properly managed; compares dropping plastic at home to broader environmental harm.
- **Labelling and behaviour:** In [home country] bottles lack on-pack recycling prompts seen in UK; believes company encouragement of recycling shapes whether customers take it seriously.
- **Reuse contrast:** Does not normally reuse plastic containers at home; in UK washes robust takeaway plastic after eating rather than dumping carelessly; paper packaging must go in bin (e.g. after library snack).
- **Campus/library meals:** Buys lunch on campus; pepperoni pizza in paper packaging placed in general bin; orange juice packaging debated between plastic and paper bin; orange packaging to general waste.
- **Research and policy:** Recently read report citing ~£2 billion cost of plastic and food/beverage waste; asks himself questions about materials and correct disposal; discusses waste hierarchy (reduce, reuse, recycle).
- **Infrastructure:** Library has general bin and bottle bin; connects keeping environment safe to church-related community activities.

**Behavioral lenses:** Culture/social (home vs UK systems, church community), Recycling diligence (bin choice on campus/library), Identity (international student comparing infrastructure), Pricing/value (litter cost report), Attitude-behavior gap (knows hierarchy, still uses general bin for some paper), Convenience tradeoff (campus-bought lunch).

---

"""


def lens_and_callbacks() -> str:
    return """### Behavioral lens summary across steps

| Step | Primary lenses |
| ---- | -------------- |
| Interview 1 | Identity, Culture/social, Convenience tradeoff, Reuse tendency |
| Diary 1 | Occasion, Culture/social, Identity |
| Diary 2 | Occasion, Food waste sensitivity |
| Follow-up 1 | Convenience tradeoff, Culture/social, Recycling diligence, Occasion |
| Diary 3 | Occasion, Convenience tradeoff, Reuse tendency |
| Diary 4 | Occasion, Food waste sensitivity, Reuse tendency |
| Follow-up 2 | Identity, Reuse tendency, Convenience tradeoff, Attitude-behavior gap |
| Interview 2 | Culture/social, Recycling diligence, Attitude-behavior gap, Pricing/value |

---

### Where Interview 2 draws from (human summary)

Interview 2 is a closing conversation. The interviewer often **looks back** at what Jacob said or did earlier in the study. When he answers, he is usually pulling from one of these earlier layers:

| Earlier material | What Jacob goes back to |
| ---------------- | ----------------------- |
| **Interview 1** | Gutter dumping and flooding at home; Eat India takeaway bowls; Nigerian/Lidl multi-store shopping; three kitchen bins; reusing bowls for need not ideology |
| **Diary 1–2** | Busy Tuesday routine; morning devotion and exercise rhythm |
| **Follow-up 1** | Takeaway day when cooking felt wasteful; Pepsi can to plastics bin; bulk stew shopping trip; communal fridge photo |
| **Diary 3** | Tuesday campus dissertation day (pizza + OJ); Thursday "dumping" language; Sunday church and chores |
| **Diary 4** | Manchester all-nighter with OJ; devotion/exercise; egg stew with carrots; Friday Nigerian shop haul |
| **Follow-up 2** | Batch stew into plastic bowls; plastic waste sorting; diary reflexivity on planning ahead |
| **Home visit** | Shop with researcher; muffins/fruit to room; week 3 shopping table photo |

Two kinds of look-back happen:

1. **He (or the interviewer) says it out loud** — e.g. "going back to your first interview…", "week three diary entry", "when I visited".
2. **He doesn't name it, but the answer only makes sense with earlier context** — e.g. carrot packaging disposal draws on the shopping photo even when discussing general bin logic.

**Topics that mostly stand alone in Interview 2** (little prior material): World Bank report and reverse-logistics dissertation idea; clothing label curiosity (sustainable cotton); palm nut soup and wache local foods depth.

#### By Interview 2 theme

**Home country vs UK environment**

- Goes back to **Interview 1**: gutter dumping, flooding, erosion
- **I2 new depth**: ocean harm framing; UK label discipline vs home; visitors adopt UK norms

**Dissertation / policy lens**

- **I2 mostly new**: World Bank £2bn spend; reverse logistics as solution; producer-not-consumer reduce priority

**Reuse and packaging**

- **Interview 1 + FU2**: Eat India bowls; doesn't reuse at home; washes robust UK takeaway plastic
- **Home visit + D3 photo**: muffins/fruit wrappers to correct kitchen bin

**Campus / library meals**

- **Diary 3**: Tuesday five-hour library day; pizza paper to general bin; OJ to bottle bin
- **Diary 4**: Manchester trip then all-night proposal; OJ instead of food to stay awake

**Faith and kitchen**

- **Diary 3 Sunday entry**: church devotion; laundry; communal kitchen cleanliness responsibility

**Multi-store shopping**

- **Interview 1**: Indian → Nigerian → Lidl/Aldi adaptation
- **Diary 4 Friday**: opportunistic Manchester Nigerian shop with friend’s car

#### The short version

If you imagine Jacob's "memory" for Interview 2, it is weighted toward:

1. **Interview 1** — home flooding/gutter harm; Eat India bowls; multi-store food adaptation
2. **Follow-up 1–2** — takeaway vs cook; batch stew in bowls; plastics bin sorting
3. **Diary 3** — campus lunch bins; Sunday church; dumping language
4. **Diary 4** — Manchester trips; egg stew; Nigerian shop photos
5. **Home visit** — shop table photo (carrots, OJ, oranges)

About **4 topics** in Interview 2 are genuinely new depth (World Bank report, reverse logistics proposal, clothing label questions, wache/palm nut soup detail). Everything else revisits something he already said, photographed, or showed the researcher.

---

"""


PATTERN_LIBRARY = """| Pattern ID | Source | What to simulate |
| ---------- | ------ | ---------------- |
| `identity_intl` | I1, D1, I2 | International PG student; large family background; solo in shared flat |
| `culture_home_uk` | I1, I2 | Home flooding/gutter harm vs UK labels and bin discipline; adopts UK norms |
| `budget_student` | I1, D4, I2 | Lidl/Aldi + Nigerian shop; opportunistic Manchester bulk buy |
| `convenience_default` | I1, FU1, D3–D4, I2 | Eat India when time-tight; campus lunch on long library days |
| `reuse_bowls` | I1, FU2, I2 | Keeps Eat India bowls as kitchenware; batch stew storage; washes not dumps |
| `recycling_learning` | I1, FU1, D3, I2 | Three kitchen bins; library general vs bottle bins; reads packaging labels |
| `attgap_plastic` | I1, I2 | Knows hierarchy and harm; paper sometimes to general bin; producer responsibility |
| `foodwaste_chain` | I1, FU1–2, D4, I2 | Batch cabbage/egg stew; carrots from shop photo; light food on all-nighters |
| `faith_community` | D1, D3, I2 | Sunday church; devotion; cleanliness in shared kitchen |
| `occasion_campus` | D3–D4, I2 | Dissertation deadlines; Manchester trips; library meals |
| `professional_lens` | I2 | Dissertation reverse logistics; World Bank waste cost data |
| `multi_store` | I1, D4, I2 | Indian → Nigerian → UK supermarkets; Manchester shop haul |"""

SITUATION_TABLE = """| Situation type | Behavioral pattern to simulate |
| -------------- | ------------------------------ |
| Time-pressed student | Eat India takeaway; campus lunch on long library days |
| Home vs UK infrastructure | Gutter flooding memory; UK label reading; adopts local bin rules |
| Shared flat kitchen | Three labelled bins; cleans after self; communal friction |
| Batch cooking | Stew into reused takeaway bowls; bulk shop before run-out |
| Dissertation/policy mode | Cites World Bank data; reverse logistics; producer-first reduce |
| Faith Sunday | Church activities; laundry; cleanliness as godliness |
| Photo/diary callback | Shopping table photo bin choices; Manchester food photos |"""

ARC_SUMMARY_TABLE = """| Arc | Twin loads | Weak for simulation |
| --- | ---------- | ------------------- |
| A | Home-country harm narrative (flooding, erosion) | — |
| B | UK label culture; discipline when visiting | Short clarifiers |
| C | Food vs plastic parity; policy/research depth | Report source logistics |
| D | Bowl reuse; label curiosity | Clothing label detail |
| E | Materials hierarchy; appropriate bin logic | — |
| F | Waste hierarchy; producer responsibility | — |
| G | Campus lunch bin mismatch | Diary date IDs |
| H | Dumping vs dropping language | — |
| I | Church, Sunday chores, kitchen hygiene | — |
| J | Room snacks → kitchen bins | — |
| K | Photo elicitation bin reasoning | Screen-share logistics |
| L | All-nighter fuel (OJ not food) | — |
| M | Devotion, gym, egg stew chain | — |
| N | Opportunistic Manchester shop | — |
| O | Local food photos (wache, palm nut) | Photo ID confusion |"""


def main() -> None:
    text = I2_PATH.read_text()
    pairs = pairs_from_turns(parse_transcript(text))
    substantive = sum(1 for a, _ in pairs if len(a["text"]) >= 15)

    doc = (
        header_section(substantive)
        + step_summaries()
        + lens_and_callbacks()
        + behavior_tagged_section(
            pairs,
            participant="Jacob",
            i2_path=I2_DOCX,
            substantive_count=substantive,
            arc_turns=ARC_TURNS,
            turn_meta=TURN_META,
            turn_paraphrase=TURN_PARAPHRASE,
            pattern_library_md=PATTERN_LIBRARY,
            situation_table_md=SITUATION_TABLE,
            arc_summary_table_md=ARC_SUMMARY_TABLE,
            p0_question_count=20,
            subject_pronoun="he",
        )
        + full_transcript_section(pairs, ARC_TURNS)
    )

    OUT_PATH.write_text(doc)
    print(f"Wrote {OUT_PATH} ({len(doc.splitlines())} lines)")
    print(f"Substantive turns: {substantive}")


if __name__ == "__main__":
    main()
