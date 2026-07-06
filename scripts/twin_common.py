"""Shared utilities for participant Twin document generation."""

from __future__ import annotations

import re

FILLER = re.compile(
    r"^(ok|yeah|right|sure|no|oh|well|so|thanks|thank you|that's ok|that's okay|i see|great|perfect|absolutely|mm|hmm|sorry|yes|are you sure)\.?$",
    re.I,
)


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
            "going back to your previous",
            "going back to your fist year",
            "going back to the recycling",
            "going back to your diary",
            "earlier videos",
            "week three diary",
            "week four diary",
            "diary entry",
            "diary entries",
            "when i came to visit",
            "when i visited",
            "first interview when",
            "first interview again",
            "first interview that",
            "in your first interview",
            "in the past at you",
        ]
    ):
        return "R"
    if len(text) < 25 or FILLER.match(text.strip()):
        return "C"
    return "B"


def paraphrase_fallback(text: str) -> str:
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


CAN_SIMULATE_HEADER = """### Interview 2: Can simulate (selected turns)

_Add manually after tagging turns in the arc tables below (append ` · CAN SIMULATE` to turn numbers). Copy type, paraphrase, and patterns from tagged rows._

| # | Type | Paraphrased question | Behavioral patterns |
|---|------|---------------------|---------------------|

"""


def behavior_tagged_section(
    pairs: list[tuple[dict, dict | None]],
    *,
    participant: str,
    i2_path: str,
    substantive_count: int,
    arc_turns: list[tuple[str, str, str, list[int]]],
    turn_meta: dict,
    turn_paraphrase: dict,
    pattern_library_md: str,
    situation_table_md: str,
    arc_summary_table_md: str,
    p0_question_count: int = 20,
    subject_pronoun: str = "they",
) -> str:
    lines = [
        "## Interview 2: Behavior-Tagged Questions (Full Transcript)",
        "",
        "### Core reframing: simulate behavior, not lived experience",
        "",
        f"The summarized question list in `P0_PARTICIPANT_SUMMARIES.md` has **~{p0_question_count} paraphrased questions**. The actual transcript (`{i2_path}`) has **{substantive_count} substantive interviewer turns**.",
        "",
        f"For a twin, the goal is **not** to reproduce whether {participant} remembers a specific diary day. That is fact recall / lived experience.",
        "",
        f"The goal **is** to reproduce **how {subject_pronoun} behaves** when a situation arises:",
        "",
        situation_table_md,
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
        pattern_library_md,
        "",
        f"### Full transcript: {substantive_count} tagged turns in {len(arc_turns)} conversational arcs",
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
        turn_lookup[turn_num] = (a, b, turn_paraphrase.get(turn_num, paraphrase_fallback(a["text"])))

    for arc_id, title, summary, turn_nums in arc_turns:
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
            typ, patterns = turn_meta.get(n, (classify_a(a["text"]), "`identity_veg`"))
            lines.append(
                f"| {n} | {typ} | {para} | {verbatim_snippet(a['text'])} | {patterns} |"
            )
        lines.append("")

    lines.extend(
        [
            "### Summary: what the twin loads for each arc",
            "",
            arc_summary_table_md,
            "",
            "### Turns that are weak for behavior simulation",
            "",
            "- **Fact recall:** specific diary dates, brand names without behavioral generalization",
            "- **Comfort / logistics:** break offers, \"are you ok\", end-of-interview closings",
            "- **Pure photo ID without pattern:** \"what is this picture\" when no prior food-type pattern exists",
            "",
            f"### How this differs from the ~{p0_question_count}-question summary",
            "",
            f"P0 lists ~{p0_question_count} paraphrased I2 questions grouped by theme. The transcript has **{substantive_count} substantive turns** because the interviewer probes follow-ups. A twin must handle the **conversation thread**, not just the headline question.",
            "",
        ]
    )
    return "\n".join(lines)


def full_transcript_section(
    pairs: list[tuple[dict, dict | None]],
    arc_turns: list[tuple[str, str, str, list[int]]],
) -> str:
    lines = ["## Interview 2 transcript (full)", ""]
    turn_num = 0
    arc_by_turn: dict[int, str] = {}
    for arc_id, _, _, nums in arc_turns:
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
        lines.append(f"**A · #{turn_num}{arc_note}:** {a['text']}")
        lines.append("")
        if b:
            lines.append(f"**B:** {b['text']}")
            lines.append("")
    lines.append("End of interview")
    return "\n".join(lines)
