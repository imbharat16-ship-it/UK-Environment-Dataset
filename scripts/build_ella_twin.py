#!/usr/bin/env python3
"""Generate Ella Twin.md from extracted transcripts and P0 summaries."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from ella_data import ARC_TURNS, CAN_SIMULATE_TURNS, TURN_META, TURN_PARAPHRASE
from twin_common import (
    behavior_tagged_section,
    full_transcript_section,
    pairs_from_turns,
    parse_transcript,
    verbatim_snippet,
)

I2_PATH = ROOT / ".extracted/ella/interview_2.txt"
I2_DOCX = "857315_data/Households11_20/Household14Ella/20220401_Final_interview_Ella.docx"
OUT_PATH = ROOT / "Ella Twin.md"


CLARIFICATION_B = re.compile(r"^(sorry|yeah|yes|no|ok|what)\.?\??$", re.I)


def _substantive_turn_index(pairs: list) -> dict[int, int]:
    """Map substantive turn number -> index in pairs list."""
    mapping: dict[int, int] = {}
    turn_num = 0
    for i, (a, _) in enumerate(pairs):
        if len(a["text"]) >= 15:
            turn_num += 1
            mapping[turn_num] = i
    return mapping


def _thread_segments(pairs: list, turn_num: int) -> list[tuple[str, str, str]]:
    """Return (role_label, speaker, text) segments for a CAN SIMULATE thread."""
    idx_map = _substantive_turn_index(pairs)
    if turn_num not in idx_map:
        return []
    start = idx_map[turn_num]
    segments: list[tuple[str, str, str]] = []
    i = start
    a, b = pairs[i]
    segments.append(("A · CAN SIMULATE", "A", a["text"]))
    if b:
        segments.append(("B · First turn", "B", b["text"]))
    i += 1
    follow = 1
    while i < len(pairs):
        a2, b2 = pairs[i]
        if len(a2["text"]) >= 15:
            if (
                b
                and len(b["text"]) < 40
                and CLARIFICATION_B.match(b["text"].strip())
                and follow == 1
            ):
                segments.append((f"A · #{turn_num + follow}", "A", a2["text"]))
                if b2:
                    segments.append(("B · Follow-up", "B", b2["text"]))
                break
            break
        if b2:
            segments.append((f"A · #{turn_num + follow}", "A", a2["text"]))
            segments.append(("B · Follow-up", "B", b2["text"]))
            follow += 1
        i += 1
    return segments


def can_simulate_threads_section(pairs: list) -> str:
    lines = [
        "Full verbatim threads below. *First turn = first **B:** on the topic · Full thread = all **B:** on the same topic, including follow-ups.*",
        "",
    ]
    for n in CAN_SIMULATE_TURNS:
        segments = _thread_segments(pairs, n)
        if not segments:
            continue
        lines.append(f"#### #{n} · {TURN_PARAPHRASE[n]}")
        lines.append("")
        b_count = sum(1 for label, _, _ in segments if label.startswith("B"))
        if b_count <= 1:
            thread_note = "*First turn only (no follow-ups on this thread)*"
        elif b_count == 2 and any("Follow-up" in s[0] for s in segments):
            thread_note = "*First turn = first **B:** below · Full thread = both **B:** turns*"
        else:
            thread_note = "*First turn = first **B:** below · Full thread = all **B:** on this topic*"
        lines.append(f"**Transcript (actual)** · {thread_note}")
        lines.append("")
        for label, speaker, text in segments:
            lines.append(f"**{label} (#{n}):** {text}")
            lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines)


def can_simulate_header() -> str:
    rows = []
    for n in CAN_SIMULATE_TURNS:
        typ, patterns = TURN_META[n]
        typ_display = typ.replace("+", " + ")
        rows.append(
            f"| {n} | {typ_display} | {TURN_PARAPHRASE[n]} | {patterns} |"
        )
    table = "\n".join(rows)
    return f"""### Interview 2: Can simulate (selected turns)

Questions marked **CAN SIMULATE** in the arc tables and full transcript below. Type uses full names (not encoded letters).

| # | Type | Paraphrased question | Behavioral patterns |
|---|------|---------------------|---------------------|
{table}

"""


def header_section(pairs: list) -> str:
    return f"""# Ella Twin

**Source:** Ella (Phase 1) · extracted from `P0_PARTICIPANT_SUMMARIES.md`  
**Scope:** Step summaries · Behavioral lens summary · I2 callback map · Behavior-tagged I2 (132 turns) · Full I2 transcript  
**Archetype:** B · Environmental systems / student  
**Profile:** Third-year environmental science student; part-time supermarket checkout worker (four years, home store and university branch). Coastal hometown; pescetarian since New Year resolution; shared student house with rotating group meals. Main household shopper via staff discount online orders.

{can_simulate_header()}
{can_simulate_threads_section(pairs)}
"""


def step_summaries() -> str:
    return """### Step summaries

#### Interview 1 (Step 0) · Ella — 11,205 words · 56,707 characters

**Themes:**

- **Household/home:** Third-year environmental science student; grew up on the coast; lives with same flatmates since first year (~three years); responsible for household shop via supermarket staff discount online orders.
- **Routines:** Four-year checkout job (since age 17) at home store and casual university hours; dad is a baker with very early work start, so family ate earlier at home.
- **Shopping:** Weekly shop from large supermarket; choices driven by affordability; transitioned from free Sainsbury's bus to employer store; Mob Kitchen online recipes for group meals.
- **Food/preparation:** Became pescetarian as New Year resolution after failed vegetarian attempts in first year; shared cooking rotation (~two vegetarian meals/week); still relies on microwave rice packets despite knowing plastic cost; at least one takeaway/week across house.
- **Plastic packaging:** Plastic central to degree and checkout work; sees packaging volume on conveyor belt; notices shift toward loose fruit/veg and reusable bags over four years; associates plastic with wildlife harm (turtles, six-pack rings).
- **Disposal/recycling:** Influenced parents at home to think about plastic; home council introduced mixed blue bin plus separate food and garden bins; parents now ask her what is recyclable.
- **Reuse:** Observes customers avoiding veg bags and bringing own carriers; some motivated by environment, others by avoiding 10p–20p bag charge.

**Behavioral lenses:** Identity (environment student, pescetarian), Culture/social (influencing family recycling, course peer norms), Pricing/value (staff discount shop, sale packs, bag charge), Convenience tradeoff (microwave rice, jar sauces early on), Recycling diligence (family bin coaching), Food waste sensitivity (group meal planning), Attitude-behavior gap (knows rice packets are bad, buys them anyway).

---

#### Diary 1 (Step 1) — 1,291 words · 6,873 characters

**Themes:**

- First full diary batch; photo-led weekly shop and group meal planning.
- **Onions:** Usually buys loose but chose 3-pack on sale to lower bill (student budget tradeoff).
- **Group meal:** Chickpea curry planned for house; chose flatbreads instead of multiple rice packets to reduce packaging.
- **Shop photos:** Rest of weekly shop documented (Images 6–7); packaging visible across staples and fresh items.

**Behavioral lenses:** Pricing/value (sale pack over loose), Convenience tradeoff (flatbreads vs rice packets), Identity (environment-aware student shopper), Attitude-behavior gap (sale plastic pack when loose is norm).

---

#### Diary 2 (Step 2) — 928 words · 4,994 characters

**Themes:**

- Themed entry: full day of meals and their plastic packaging (11/03/22).
- **Breakfast:** Tea, strawberries, yogurt, fruit toast; notes hidden plastics in tea supply chain.
- **Lunch:** Studying at home; cupboard meal of tuna and couscous; tins feel plastic-free but couscous packaging noted.
- **Dinner:** Her turn for group meal; vegetarian Thai green curry; deliberately chose veg with minimal packaging where possible (Images 3–6).

**Behavioral lenses:** Occasion (study-from-home day), Convenience tradeoff (cupboard lunch), Recycling diligence (packaging audit mindset), Identity (vegetarian group cooking).

---

#### Follow-up interview 1 (Step 3) · Ella — 2,382 words · 13,177 characters

**Themes:**

- **Study reflexivity:** Participation made her think more about plastic; diary writing slows her down to notice packaging in daily use.
- **Deadline week:** Laptop broke over weekend; lost coursework; spent days on campus computers ahead of Tuesday deadline.
- **Monday dinner:** No time to cook; pulled frozen chips and vegetables from freezer after work + deadline pressure.
- **Routine shift:** Campus-heavy days changed where and how she eats compared with home cooking weeks.

**Behavioral lenses:** Occasion (deadline crisis), Convenience tradeoff (freezer meal), Identity (heightened packaging awareness through study), Attitude-behavior gap (reflects more, still defaults to convenience under stress).

---

#### Diary 3 (Step 4) — 1,255 words · 6,756 characters

**Themes:**

- Prompted by follow-up 1 question on "unnecessary" packaging; kitchen audit (17/03/22).
- **Cupboard rice:** Risotto rice, orzo, paella rice flagged as unnecessarily plastic-wrapped; could be cardboard boxes (Image 1).
- **Noodles:** Thick udon bought only because reduced; not a usual purchase (Image 3).
- **Beauty products:** Separate entry (20/03/22) on plastic in toiletries/cosmetics beyond food.

**Behavioral lenses:** Recycling diligence (post-interview audit), Pricing/value (reduced udon), Attitude-behavior gap (knows rice could be cardboard, still owns plastic packs), Identity (environment student applying lens to own kitchen).

---

#### Diary 4 (Step 5) — 995 words · 5,360 characters

**Themes:**

- Sunny day BBQ with housemates (24/03/22); Mother's Day card bought from card shop en route.
- **BBQ shop:** Multiple packaging photos; quiche ingredients for her evening group meal (spinach and caramelised onion).
- **Packaging split:** Eggs and glass balsamic vinegar only items without plastic in front of her; meat trays and cream pot rinsed for recycling; soft plastics to general waste (not accepted kerbside).

**Behavioral lenses:** Occasion (BBQ, Mother's Day), Convenience tradeoff (one-trip shop for social meal), Recycling diligence (rinses rigid plastics, bins films), Pricing/value (student group catering), Attitude-behavior gap (social BBQ generates unavoidable soft plastic).

---

#### Follow-up interview 2 (Step 7) · Ella — 5,646 words · 28,193 characters

**Themes:**

- **Household change:** Now four housemates with chest freezer (previously seven people with two fridge-freezers); more capacity to freeze bread and batch items.
- **Bread strategy:** Freezes whole loaves on purchase; defrosts slices as needed; lasts ~one month vs mould in cupboard.
- **Campus vs home eating:** On campus = packed food, bought food, or staying home; different packaging footprint by location.
- **Breakfast plastics:** Strawberries and yogurt pots; porridge in cardboard; cereal boxes with inner film; yoghurt pot recycling debated (material ambiguity).
- **Health week:** Bad cold prior week; bought more fruit; reflecting on eating better when unwell.
- **Soft plastics:** Knows soft films not accepted in home kerbside bins; some packaging on verge between cardboard and plastic.

**Behavioral lenses:** Reuse tendency (bread freezing), Convenience tradeoff (freezer as backup when plans change), Recycling diligence (sorts yoghurt/cereal fractions), Occasion (campus days), Food waste sensitivity (bread freezing anti-mould).

---

#### Interview 2 (held out) · Ella — 12,923 words · 65,936 characters

**Themes:**

- **Checkout employee view:** Four years observing customer packaging choices; gradual shift to loose produce, reusable bags, and resistance to 20p carrier charge.
- **Store changes:** Veg bags moved from plastic to paper; bag levy rose from 5p to 20p; delivery orders separate cleaning products from food to contain leaks.
- **Early university diet:** Wraps, chicken, jar curry sauce repeatedly; basically "chicken all the time"; later broadened recipes and soup batching.
- **Beach cleans:** Joined litter-picking group; smoothie phase in first year (frozen + fresh mix); soups frozen in Tupperware over winter.
- **Recycling infrastructure:** Wants more public recycling along beaches; bins overflow so litter misses collection; read about microplastics in human body.
- **Employee monitoring:** Checkout scan-rate monitoring; colleagues' views on packaging complaints (paper veg bags vs customer expectations).
- **Geography:** University town within few hours of Liverpool, Manchester, Birmingham by train.

**Behavioral lenses:** Identity (environment student + checkout insider), Culture/social (beach clean community), Pricing/value (bag charge behaviour change), Convenience tradeoff (early jar-sauce diet), Recycling diligence (infrastructure frustration), Attitude-behavior gap (sees consumer shift, still uses convenience foods), Occasion (smoothies, soups, beach litter).

---

"""


def lens_and_callbacks() -> str:
    return """### Behavioral lens summary across steps

| Step | Primary lenses |
| ---- | -------------- |
| Interview 1 | Identity, Culture/social, Pricing/value, Convenience tradeoff, Attitude-behavior gap |
| Diary 1 | Pricing/value, Convenience tradeoff, Identity, Attitude-behavior gap |
| Diary 2 | Occasion, Convenience tradeoff, Recycling diligence, Identity |
| Follow-up 1 | Occasion, Convenience tradeoff, Identity, Attitude-behavior gap |
| Diary 3 | Recycling diligence, Pricing/value, Attitude-behavior gap, Identity |
| Diary 4 | Occasion, Recycling diligence, Convenience tradeoff, Attitude-behavior gap |
| Follow-up 2 | Reuse tendency, Convenience tradeoff, Recycling diligence, Occasion |
| Interview 2 | Identity, Culture/social, Pricing/value, Recycling diligence, Attitude-behavior gap |

---

### Where Interview 2 draws from (human summary)

Interview 2 is a closing conversation. The interviewer often **looks back** at what Ella said or did earlier in the study. When she answers, she is usually pulling from one of these earlier layers:

| Earlier material | What Ella goes back to |
| ---------------- | ---------------------- |
| **Interview 1** | Checkout job; coastal upbringing; pescetarian shift; microwave rice guilt; staff discount shop; Mob Kitchen group meals; parents' recycling coaching; veg bag and carrier-bag trends on belt |
| **Diary 1–2** | Sale onion pack; flatbreads vs rice packets; full-day packaging audit; Thai curry minimal-packaging shop |
| **Follow-up 1** | Deadline week frozen chips dinner; study making her notice packaging more |
| **Diary 3** | Unnecessary rice/noodle audit; beauty product swaps; loose tea leaves; spice jars from plastic-free shop |
| **Diary 4** | BBQ shop hard vs soft plastic split; Mother's Day balloon recycle stand; spa hotel plastics |
| **Follow-up 2** | Chest freezer and bread freezing; breakfast yoghurt/cereal fractions; soft plastics not kerbside |

Two kinds of look-back happen:

1. **She (or the interviewer) says it out loud** — e.g. "going back to your first interview…", "week three diary entry", "you mentioned on Thursday 24th".
2. **She doesn't name it, but the answer only makes sense with earlier context** — e.g. checkout packing logic draws on FU2 delivery red-bag discussion even when the question is general.

**Topics that mostly stand alone in Interview 2** (little prior material): scan-rate monitoring feelings; microplastics toxicity depth; Attenborough documentary accessibility; biodegradable bag scepticism; Olio app mechanics; hotel breakfast portion design.

#### By Interview 2 theme

**Checkout insider**

- Goes back to **Interview 1 + FU2**: four years on belt; paper veg bags; 5p-to-20p bag charge; delivery meat/cleaning separation
- **I2 new depth**: customer packing norms; loose produce weighing; scan monitoring for queue management

**Degree & microplastics**

- **Interview 1 + D4**: environmental science identity; microplastics in blood paper from beauty diary entry
- **I2 new depth**: no dedicated plastic modules; consumer-led change theory; media awareness loop

**Coastal tourism & beach cleans**

- **Interview 1**: coastal hometown; turtle/six-pack ring associations
- **I2 new depth**: post-COVID staycation litter; overflowing bins; Facebook beach-clean group

**First-year diet & pescetarian guilt**

- **Interview 1**: chicken wraps, jar sauces, microwave rice; course vegetarian norms
- **I2 new depth**: lecturer headcount moment; budget vs peers who can afford vegan diet

**Blender, smoothies, soups**

- **Interview 1 + FU2**: freezer capacity; batch cooking
- **I2 new depth**: smoothie laziness; frozen fruit logic; soup Tupperware vs takeaway tubs

**Diary callbacks (weeks 3–4)**

- **D3**: unnecessary packaging audit (44–48); tea/spice photos (49–57); beauty swaps (58–74)
- **D4**: enchiladas and cake (75–97); BBQ packaging (98–104); spa plastics (105–118)
- **FU1 implicit**: deadline freezer chips; flatbreads vs rice packets

**End of term & food waste**

- **D4 + I1**: packaged snacks vs fruit; carton recycling idea from I1
- **I2 new depth**: Costa cup rinse; Olio tofu via store food champions; carton washing barrier

#### The short version

If you imagine Ella's "memory" for Interview 2, it is weighted toward:

1. **Interview 1** — checkout insider view, pescetarian identity, coastal upbringing, microwave rice gap
2. **Diary 3** — unnecessary packaging audit, beauty swaps, tea/spice photos
3. **Diary 4** — BBQ hard/soft plastic split, spa hotel plastics, birthday cake
4. **Follow-up 2** — chest freezer, bread freezing, breakfast fractions
5. **Follow-up 1** — deadline week convenience defaults

About **6 topics** in Interview 2 are genuinely new depth (scan monitoring, microplastics toxicity detail, documentary reach, biodegradable bag science, Olio mechanics, hotel breakfast design). Everything else revisits something she already said, photographed, or observed on the checkout belt.

---

"""


PATTERN_LIBRARY = """| Pattern ID | Source | What to simulate |
| ---------- | ------ | ---------------- |
| `identity_systems` | I1, D3, I2 | Environmental science student; applies course lens to own kitchen and media |
| `checkout_insider` | I1, FU2, I2 | Four years on belt; sees packaging trends; scan monitoring; delivery vs till packing |
| `professional_lens` | I1, I2 | Employee view on customer bag choices, loose produce, and store policy changes |
| `community_infra` | I1, I2 | Beach cleans; wants public recycling on coast; Olio food-waste community |
| `recycling_diligence` | I1, D4, FU2, I2 | Rinses rigid plastics; bins soft films; council leaflet from memory; campus carton idea |
| `attgap_plastic` | I1, D1–D4, I2 | Knows rice packets and hotel bottles are bad; still buys convenience and reduced items |
| `meal_plan` | I1, D1–D4, I2 | Mob Kitchen group rotation; stir fries; enchiladas; batch soups |
| `freezing_chain` | FU2, I2 | Chest freezer bread; soup Tupperware batches; bar soap drying on windowsill |
| `convenience_default` | I1, FU1, I2 | Microwave rice; jar sauces; takeaways during deadlines; packaged snacks |
| `budget_student` | I1, D1, D3, I2 | Staff discount shop; sale onion pack; reduced udon; £15 split BBQ |
| `pescetarian_identity` | I1, I2 | New Year resolution; course vegetarian guilt; fish cost barrier |
| `beauty_swaps` | D3, I2 | Shampoo bars; Lush pot returns; geography A-level influence; DIY exfoliator fail |
| `plastic_free_shop` | D3, I2 | Local refill shop; pasta in jar; spice refill; loose tea leaves |
| `occasion_social` | D4, I2 | BBQ, spa, birthday cake, GBBO/Apprentice takeaway nights |
| `foodwaste_chain` | D1, FU2, I2 | Stir-fry leftovers; Olio tofu; restaurant leftovers; full spinach bag |"""

SITUATION_TABLE = """| Situation type | Behavioral pattern to simulate |
| -------------- | ------------------------------ |
| On checkout belt | Insider view on bags, loose produce, customer feedback |
| Student budget shop | Sale packs, reduced section, staff discount priorities |
| Group house cooking | Mob Kitchen rotation; vegetarian meals; takeaway under deadline pressure |
| Coastal / tourism litter | Beach cleans; bin overflow; infrastructure frustration |
| Kitchen audit moment | Flags unnecessary rice plastic; still owns plastic packs |
| Beauty / refill habits | Shampoo bars, Lush returns, plastic-free shop visits |
| Away from home (spa, campus) | Hotel bottle defaults; Costa cup rinse; carton recycling intention |
| Food waste apps | Olio pickup; supermarket food champions |"""

ARC_SUMMARY_TABLE = """| Arc | Twin loads | Weak for simulation |
| --- | ---------- | ------------------- |
| A | Checkout insider, bag charge, loose produce | Scan-rate score detail |
| B | Degree knowledge gaps, microplastics, consumer change | Module names |
| C | Staycation litter, beach cleans | Facebook group dates |
| D | First-year chicken diet, vegetarian guilt | Lecturer name |
| E | Smoothie/soup batching, freezer Tupperware | Blender brand |
| F | Documentary framing (beef/fish industry) | Exact Netflix titles |
| G | Unnecessary packaging audit, reduced udon | Diary photo IDs |
| H | Loose tea, spice jars, photo elicitation | Photo left/right |
| I | Beauty swaps, shampoo bars, Lush pots | My Little Eco Shop URL |
| J | Enchiladas, stir fries, takeaway TV nights | Takeaway vendor names |
| K | Birthday cake burn, restaurant leftovers, pasta jar | Cake recipe detail |
| L | BBQ packaging split, council memory | Mother's Day date |
| M | Spa hotel plastics, biodegradable scepticism | Hotel name |
| N | Costa cup, supplement, Olio tofu | Supplement brand |
| O | Packaged snacks vs fruit, carton recycling | Campus bin location |"""


def _format_turn_num(n: int) -> str:
    if n in CAN_SIMULATE_TURNS:
        return f"{n} - CAN SIMULATE"
    return str(n)


def behavior_tagged_section_ella(
    pairs,
    *,
    substantive_count: int,
) -> str:
    """Like twin_common.behavior_tagged_section but marks CAN SIMULATE turns."""
    from twin_common import classify_a, paraphrase_fallback

    lines = [
        "## Interview 2: Behavior-Tagged Questions (Full Transcript)",
        "",
        "### Core reframing: simulate behavior, not lived experience",
        "",
        f"The summarized question list in `P0_PARTICIPANT_SUMMARIES.md` has **~25 paraphrased questions**. The actual transcript (`{I2_DOCX}`) has **{substantive_count} substantive interviewer turns**.",
        "",
        "For a twin, the goal is **not** to reproduce whether Ella remembers a specific diary day. That is fact recall / lived experience.",
        "",
        "The goal **is** to reproduce **how she behaves** when a situation arises:",
        "",
        SITUATION_TABLE,
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
        PATTERN_LIBRARY,
        "",
        f"### Full transcript: {substantive_count} tagged turns in {len(ARC_TURNS)} conversational arcs",
        "",
        "Each turn has three question layers:",
        "",
        "1. **Paraphrased question** — clean, standalone question for twin prompting/evaluation",
        "2. **Verbatim turn** — what the interviewer actually said",
        "3. **Behavioral patterns** — which calibrated patterns to activate (not factual recall)",
        "",
    ]

    turn_lookup: dict[int, tuple] = {}
    turn_num = 0
    for a, b in pairs:
        if len(a["text"]) < 15:
            continue
        turn_num += 1
        turn_lookup[turn_num] = (a, b, TURN_PARAPHRASE.get(turn_num, paraphrase_fallback(a["text"])))

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
            typ, patterns = TURN_META.get(n, (classify_a(a["text"]), "`identity_systems`"))
            lines.append(
                f"| {_format_turn_num(n)} | {typ} | {para} | {verbatim_snippet(a['text'])} | {patterns} |"
            )
        lines.append("")

    lines.extend(
        [
            "### Summary: what the twin loads for each arc",
            "",
            ARC_SUMMARY_TABLE,
            "",
            "### Turns that are weak for behavior simulation",
            "",
            "- **Fact recall:** specific diary dates, spa hotel name, Mother's Day timing",
            "- **Comfort / logistics:** sister relationship small talk, end-of-interview closings",
            "- **Pure photo ID without pattern:** \"what is in this photograph\" when no prior food-type pattern exists",
            "",
            "### How this differs from the ~25-question summary",
            "",
            f"P0 lists ~25 paraphrased I2 questions grouped by theme. The transcript has **{substantive_count} substantive turns** because the interviewer probes follow-ups. A twin must handle the **conversation thread**, not just the headline question.",
            "",
        ]
    )
    return "\n".join(lines)


def full_transcript_section_ella(pairs) -> str:
    """Full transcript with CAN SIMULATE markers on selected turns."""
    lines = ["## Interview 2 transcript (full)", ""]
    turn_num = 0
    arc_by_turn: dict[int, str] = {}
    for arc_id, _, _, nums in ARC_TURNS:
        for n in nums:
            arc_by_turn[n] = arc_id

    for a, b in pairs:
        if len(a["text"]) < 15:
            lines.append(f"**A:** {a['text']}")
            lines.append("")
            if b:
                lines.append(f"**B:** {b['text']}")
                lines.append("")
            continue
        turn_num += 1
        arc = arc_by_turn.get(turn_num, "")
        arc_note = f" · Arc {arc}" if arc else ""
        sim_note = " · CAN SIMULATE" if turn_num in CAN_SIMULATE_TURNS else ""
        lines.append(f"**A · #{turn_num}{arc_note}{sim_note}:** {a['text']}")
        lines.append("")
        if b:
            lines.append(f"**B:** {b['text']}")
            lines.append("")
    lines.append("End of interview")
    return "\n".join(lines)


def main() -> None:
    text = I2_PATH.read_text()
    pairs = pairs_from_turns(parse_transcript(text))
    substantive = sum(1 for a, _ in pairs if len(a["text"]) >= 15)

    doc = (
        header_section(pairs)
        + step_summaries()
        + lens_and_callbacks()
        + behavior_tagged_section_ella(pairs, substantive_count=substantive)
        + full_transcript_section_ella(pairs)
    )

    OUT_PATH.write_text(doc)
    print(f"Wrote {OUT_PATH} ({len(doc.splitlines())} lines)")
    print(f"Substantive turns: {substantive}")
    print(f"CAN SIMULATE turns: {len(CAN_SIMULATE_TURNS)}")


if __name__ == "__main__":
    main()
