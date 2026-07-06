#!/usr/bin/env python3
"""Generate scripts/jacob_data.py from extracted I2 transcript."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys_path = ROOT / "scripts"
import sys

sys.path.insert(0, str(sys_path))
from twin_common import classify_a, pairs_from_turns, parse_transcript

I2_PATH = ROOT / ".extracted/jacob/interview_2.txt"

# Manual overrides for cleaner standalone questions
OVERRIDES: dict[int, str] = {
    1: "Going back to Interview 1, what do you know about plastic waste dumped in gutters and its consequences?",
    2: "You also mentioned consequences for fish in the ocean — can you say more?",
    3: "What do you know about the consequences of plastic waste for life and the environment?",
    4: "What do you know about the consequences of plastic waste in the UK?",
    5: "Confirming the bottle label: made from 50% recycled plastic?",
    6: "What do you mean by making sure the environment is safe?",
    7: "Can you tell me more what you mean by keeping the environment safe?",
    8: "With food-industry arguments that plastic extends shelf life, how do you weigh food waste versus plastic waste?",
    9: "Is the two billion spent on waste by citizens or government?",
    10: "Do you want to share the World Bank report source later?",
    11: "Would you like to share the report link in chat?",
    12: "You can post the link in Teams chat or email — how would you share it?",
    13: "Is this a report you came across recently?",
    14: "Was the report about improving waste management infrastructure?",
    15: "Were you researching the environment in your home country when you found this report?",
    16: "Were you looking specifically for plastic implications, or general environmental data?",
    17: "Did you learn about the plastic-environment connection through your project work?",
    18: "Through your dissertation project, what have you learnt about plastic and the environment?",
    19: "The report mentions 3000 metric tons of plastic litter — what stands out to you?",
    20: "Going back to Interview 1, how do you manage plastic at home in your home country versus reusing Eat India bowls in the UK?",
    21: "You showed a red-lid container — is packaging like that common at home?",
    22: "How important is it to see recycling labels like '50% recycled plastic' on packaging?",
    23: "What kinds of questions do you ask yourself when reading packaging information?",
    24: "You mentioned sustainable cotton on a clothing label — what does that signal to you?",
    25: "Another label says minimum 30% recycled plastic — how do you interpret mixed claims?",
    26: "How does reusing takeaway containers in the UK compare with habits at home?",
    27: "How do cardboard, paper, glass, and traditional leaf packaging compare to plastic environmentally?",
    28: "In your UK flat, how practical is plastic versus paper and cardboard packaging?",
    29: "Do you prefer plastic, paper, cardboard, or glass when buying food?",
    30: "You said disposing in the appropriate bin matters — what do you mean?",
    31: "What counts as the appropriate bin for plastic versus paper waste?",
    32: "Have you come across the reduce, reuse, recycle waste hierarchy?",
    33: "Within the hierarchy, what do you think about reducing plastic food packaging as a consumer?",
    34: "Should waste reduction start with producers rather than consumers?",
    35: "In week 3 Tuesday entry, you spent five hours on campus — tell me about buying pepperoni pizza and orange juice.",
    36: "Was there a paper bin and a bottle bin in the library?",
    37: "Was there just a general bin and a bottle bin where you were sitting?",
    38: "What was the pepperoni pizza packaging made from?",
    39: "Did the paper wrapper go in the general bin?",
    40: "Library bins differ from home — how did you decide where paper and plastic went?",
    41: "Do you often buy lunch when you are out on campus?",
    42: "If the right bin is not available, would you keep packaging in your bag until you find one?",
    43: "Is carrying waste home only for certain types of packaging?",
    44: "When no bin was available for sweets, you held the wrapper — tell me more.",
    45: "In week 3 Thursday entry you use the word 'dumping' — what does dumping mean to you?",
    46: "Is 'dumping' the right word versus 'dropping' waste?",
    47: "In week 3 Sunday entry, tell me about Sundays devoted to God and chores.",
    48: "Give me general background on how you spend Sundays.",
    49: "Sundays are devoted to God — what does that involve for you?",
    50: "What church-related activities do you take part in?",
    51: "Why are Sundays also for household chores like laundry?",
    52: "Is there a particular reason laundry falls on Sunday?",
    53: "Does cleanliness in the shared kitchen relate to food hygiene for you?",
    54: "When I visited and you shopped, you took muffins and fruit to your room — what happens to the packaging?",
    55: "Can I show you a photograph from your diary?",
    56: "I'll find the photograph to share.",
    57: "This is the week three shopping photograph.",
    58: "Describe the week three food-shopping photo on the table.",
    59: "In the photo, describe the carrot packaging on the right and where it goes.",
    60: "Describe the orange juice packaging in the same photo and its disposal.",
    61: "Can you see the carrots on the right of the photograph?",
    62: "Where does the orange juice container packaging end up?",
    63: "Why does the orange juice packaging go in the plastic bin?",
    64: "Why do you prefer the plastic bin for the orange juice container?",
    65: "Why might the orange juice container go in plastic or paper bins?",
    66: "Describe the orange net/bag packaging and how you dispose of it.",
    67: "Why does orange packaging go in the general waste bin?",
    68: "In week 4 Monday entry you travelled to Manchester then worked all night — tell me about that day.",
    69: "Food-wise, what did you eat from Manchester through the library all-nighter?",
    70: "You avoided eating later to stay awake — why?",
    71: "Morning devotion and exercise appear often in diaries — are they daily routines?",
    72: "Are there particular foods you eat to maintain your body alongside exercise?",
    73: "Tell me about the egg stew and yam you mention in this entry.",
    74: "Can you tell me more about how you prepare egg stew?",
    75: "What ingredients go into the egg stew — peppers, carrots?",
    76: "Were the carrots from the previous week's shopping photo used in this stew?",
    77: "On Friday 27th you shopped at a Nigerian supermarket in Manchester — why then?",
    78: "Had you planned the Manchester grocery trip beforehand?",
    79: "What happened to the groceries while you visited museums with friends?",
    80: "In week four photos, you bought peanuts in a bottle-shaped container — why?",
    81: "Did you buy the groundnuts for a particular reason?",
    82: "Tell me about the evening meal photograph (rice and stew on a plate).",
    83: "Tell me about the palm nut soup in a takeaway-style container.",
    84: "Do you always add fish or vegetables to prepared palm nut soup?",
    85: "Describe the clear plastic container photo with rice, vegetables, and fish.",
    86: "Are we looking at the same container photograph?",
    87: "This photo is food in a container, not on a plate — is that the egg stew?",
    88: "Can you identify the food — salad with meat or fish on the right?",
    89: "Should I share my screen to confirm the photo?",
    90: "Can you see the screen with the wache rice photograph?",
    91: "Closing — any final points before end of interview?",
}

ARC_TURNS = [
    ("A", "Home country plastic harm", "Gutter dumping, flooding, erosion, ocean harm; look-back to Interview 1.", [1, 2, 3, 4]),
    ("B", "UK vs home recycling culture", "UK labels and discipline; visitors adopt local norms; environment must be kept safe.", [5, 6, 7]),
    ("C", "Food vs plastic waste and World Bank report", "Neither waste is better; £2bn government spend; dissertation reverse-logistics idea.", [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]),
    ("D", "Reuse bowls and packaging labels", "Eat India containers; home vs UK packaging; reads labels; asks why 50% not 100%.", [20, 21, 22, 23, 24, 25, 26]),
    ("E", "Materials comparison and UK flat bins", "Leaf packaging memory; glass/plastic hardness; follow kitchen bin instructions; appropriate bin logic.", [27, 28, 29, 30, 31]),
    ("F", "Waste hierarchy and producer responsibility", "Reduce-reuse-recycle known; reduction should start at production not consumer.", [32, 33, 34]),
    ("G", "Week 3: campus library lunch", "Tuesday dissertation day; pepperoni pizza + OJ; general vs bottle bins; carry waste home.", [35, 36, 37, 38, 39, 40, 41, 42, 43, 44]),
    ("H", "Week 3: dumping language", "Final destination of waste; dumping vs dropping.", [45, 46]),
    ("I", "Week 3: Sunday church and kitchen cleanliness", "Faith day; church participation; laundry; communal kitchen hygiene.", [47, 48, 49, 50, 51, 52, 53]),
    ("J", "Home visit shop and room snacks", "Muffins/fruit to room; packaging returned to kitchen bins.", [54, 55, 56, 57, 58, 59]),
    ("K", "Week 3 shopping photo elicitation", "Carrots, orange juice, orange net — plastic vs general bin reasoning.", [60, 61, 62, 63, 64, 65, 66, 67]),
    ("L", "Week 4: Manchester all-nighter", "Monday trip + library until 4am; tea/bread in Manchester; OJ to stay awake.", [68, 69, 70]),
    ("M", "Week 4: devotion, exercise, egg stew", "Daily devotion and gym; egg stew with carrots from prior shop.", [71, 72, 73, 74, 75, 76]),
    ("N", "Week 4: Manchester Nigerian shop", "Opportunistic bulk shop; car storage while sightseeing.", [77, 78, 79]),
    ("O", "Week 4 diary photos", "Groundnuts, palm nut soup, wache rice in containers; photo ID.", [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91]),
]

PATTERN_RULES: list[tuple[str, str]] = [
    ("first interview|gutter|flooding|erosion|ocean|fish", "`culture_home_uk`, `identity_intl`"),
    ("50% recycled|label|sustainable cotton|30% recycled|read on it|curiosity", "`recycling_learning`, `culture_home_uk`"),
    ("world bank|two billion|reverse logistic|project work|dissertation|report", "`professional_lens`, `culture_home_uk`"),
    ("food waste.*plastic|extend the life", "`foodwaste_chain`, `attgap_plastic`"),
    ("reuse|container|bowl|eat india", "`reuse_bowls`, `culture_home_uk`"),
    ("leaves|cardboard|glass|paper based", "`recycling_learning`, `attgap_plastic`"),
    ("appropriate bin|waste hierarchy|reduce", "`recycling_learning`, `attgap_plastic`"),
    ("pepperoni|orange juice|library|campus|bin", "`occasion_campus`, `recycling_learning`"),
    ("dumping", "`recycling_learning`"),
    ("sunday|church|god|cleanliness|kitchen", "`faith_community`, `identity_intl`"),
    ("photograph|photo|screen|carrot|orange", "`recycling_learning`, `multi_store`"),
    ("manchester|all night|proposal|deadline", "`occasion_campus`, `convenience_default`"),
    ("devotion|exercise|gym|egg stew|yam|carrot", "`foodwaste_chain`, `identity_intl`"),
    ("nigerian|groundnut|palm nut|wache", "`multi_store`, `culture_home_uk`"),
]


def patterns_for(text: str, typ: str) -> str:
    if typ == "C":
        return "(inherits prior)"
    if typ.endswith("+P") or typ == "P":
        return "`recycling_learning`, `multi_store`"
    t = text.lower()
    for needle, pat in PATTERN_RULES:
        if re.search(needle, t):
            return pat
    if typ.startswith("R"):
        return "`culture_home_uk`, `identity_intl`"
    return "`culture_home_uk`, `attgap_plastic`"


def main() -> None:
    text = I2_PATH.read_text()
    pairs = pairs_from_turns(parse_transcript(text))
    turn_num = 0
    paraphrase: dict[int, str] = {}
    meta: dict[int, tuple[str, str]] = {}
    for a, _ in pairs:
        if len(a["text"]) < 15:
            continue
        turn_num += 1
        typ = classify_a(a["text"])
        if turn_num in OVERRIDES:
            para = OVERRIDES[turn_num]
        else:
            para = a["text"][:120].rstrip() + ("..." if len(a["text"]) > 120 else "")
        paraphrase[turn_num] = para
        meta[turn_num] = (typ, patterns_for(a["text"], typ))

    out = ['"""Jacob I2 turn metadata."""', "", "TURN_PARAPHRASE = {"]
    for n in sorted(paraphrase):
        s = paraphrase[n].replace("'", "\\'")
        out.append(f"    {n}: '{s}',")
    out.append("}")
    out.append("")
    out.append("TURN_META = {")
    for n in sorted(meta):
        typ, pat = meta[n]
        out.append(f"    {n}: ('{typ}', '{pat}'),")
    out.append("}")
    out.append("")
    out.append("ARC_TURNS = [")
    for arc_id, title, summary, nums in ARC_TURNS:
        out.append(f"    ('{arc_id}', '{title}', '{summary}', {nums}),")
    out.append("]")
    out.append("")

    dest = ROOT / "scripts/jacob_data.py"
    dest.write_text("\n".join(out))
    print(f"Wrote {dest} ({turn_num} turns)")


if __name__ == "__main__":
    main()
