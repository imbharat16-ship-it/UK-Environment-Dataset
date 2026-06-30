#!/usr/bin/env python3
"""Generate Naomi-format participant section markdown from extracted transcripts."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXTRACTED = ROOT / ".extracted"
OUT = ROOT / "sections"

DOMAINS = [
    ("Household / home / neighbourhood", re.compile(
        r"house|home|flat|flatmate|neighbour|live|family|village|street|accommodation|room", re.I)),
    ("Food / preparation / shopping / routines", re.compile(
        r"food|cook|meal|eat|diet|shop|buy|aldi|supermarket|recipe|kitchen|fridge|freezer|routine|week|breakfast|lunch|dinner", re.I)),
    ("Disposal / recycling / packaging", re.compile(
        r"recycl|bin|waste|packag|plastic|cardboard|glass|film|cling|container|dispose|trash|rubbish", re.I)),
    ("Broader context", re.compile(r".")),  # catch-all last
]

LENS_KEYWORDS = {
    "Occasion": re.compile(r"party|pub|cinema|holiday|christmas|travel|restaurant|takeaway|club|work|campus|gym", re.I),
    "Pricing/value": re.compile(r"budget|cheap|price|cost|deal|offer|minimum|student|afford|save", re.I),
    "Identity": re.compile(r"vegetarian|vegan|disabled|student|independent|value|green|environment", re.I),
    "Culture/social": re.compile(r"home country|portugal|spain|parents|family|flatmate|norm|tradition", re.I),
    "Convenience tradeoff": re.compile(r"convenien|quick|frozen|ready|microwave|time|busy|easy|pre-?pack", re.I),
    "Recycling diligence": re.compile(r"recycl|sort|wash|rinse|bin|label|symbol|council", re.I),
    "Reuse tendency": re.compile(r"reuse|tupperware|container|bag|jar|leftover|freezer bag|carrier", re.I),
    "Food waste sensitivity": re.compile(r"waste|leftover|freeze|batch|use up|off|spoil|portion", re.I),
    "Attitude-behavior gap": re.compile(r"want|should|know|but|however|can't|fail|give up|contradict", re.I),
}

STEP_TITLES = {
    "interview_1": "Interview 1 (Step 0)",
    "diary_1": "Diary 1 (Step 1)",
    "diary_2": "Diary 2 (Step 2)",
    "followup_1": "Follow-up interview 1 (Step 3)",
    "diary_3": "Diary 3 (Step 4)",
    "diary_4": "Diary 4 (Step 5)",
    "diary_5": "Diary 5 (Step 6)",
    "followup_2": "Follow-up interview 2 (Step 7)",
    "interview_2": "Interview 2 (held out)",
}

FILLER = re.compile(
    r"^(ok|yeah|right|sure|no|oh|well|so|thanks|thank you|that\'s ok|that\'s okay|i see|great|perfect|absolutely|mm|hmm|sorry|yes)\.?$",
    re.I,
)


def phase_heading(name: str, phase: int) -> str:
    labels = {1: "Phase 1", 2: "Phase 2 · Confirm", 3: "Phase 3 · Extend"}
    return f"### {name} ({labels[phase]})"


def paraphrase_question(line: str) -> str:
    q = line.strip()
    q = re.sub(r"^(so |and |well |ok |yeah )", "", q, flags=re.I)
    if not q.endswith("?"):
        q = q.rstrip(".") + "?"
    if len(q) > 120:
        q = q[:117] + "..."
    return q[0].upper() + q[1:] if q else q


def extract_questions(text: str, limit: int = 28) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for line in text.splitlines():
        if not line.startswith("A:"):
            continue
        raw = line[2:].strip()
        if len(raw) < 20 or FILLER.match(raw):
            continue
        if "?" not in raw and not re.match(
            r"(tell me|describe|walk me|explain|can you|could you|would you|what|how|why|when|where|who|do you|did you|have you|is there|are there|i wondered|going back|just wondering)",
            raw,
            re.I,
        ):
            continue
        q = paraphrase_question(raw)
        key = q.lower()[:60]
        if key in seen:
            continue
        seen.add(key)
        out.append(q)
        if len(out) >= limit:
            break
    return out


def classify_question(q: str) -> str:
    for name, pat in DOMAINS[:-1]:
        if pat.search(q):
            return name
    return DOMAINS[-1][0]


def group_questions(questions: list[str]) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = {d[0]: [] for d in DOMAINS}
    for q in questions:
        groups[classify_question(q)].append(q)
    return {k: v for k, v in groups.items() if v}


def tag_lenses(text: str, max_tags: int = 6) -> list[str]:
    tags = [name for name, pat in LENS_KEYWORDS.items() if pat.search(text)]
    return tags[:max_tags]


def diary_themes(text: str) -> list[str]:
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    bullets: list[str] = []
    for ln in lines:
        if ln.startswith(("202", "-", "•", "*")) or re.match(r"^(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)", ln, re.I):
            cleaned = re.sub(r"^[-•*]\s*", "", ln)
            cleaned = re.sub(r"^\d{4}-\d{2}-\d{2}\s*[-–]?\s*", "", cleaned)
            if len(cleaned) > 15:
                bullets.append(cleaned[:200])
    if not bullets:
        for ln in lines[1:6]:
            if len(ln) > 20:
                bullets.append(ln[:200])
    return bullets[:8]


def interview_themes(text: str) -> dict[str, list[str]]:
    """Heuristic domain themes from participant (B:) utterances."""
    b_text = "\n".join(ln[2:] for ln in text.splitlines() if ln.startswith("B:"))
    themes: dict[str, list[str]] = {}
    domain_patterns = [
        ("Household/home", r"house|flat|live|family|home|room|flatmate"),
        ("Shopping", r"shop|buy|aldi|supermarket|budget|trolley"),
        ("Food/preparation", r"cook|meal|eat|recipe|fridge|freezer|chicken|vegetarian"),
        ("Plastic packaging", r"plastic|packag|film|pre-?pack|container"),
        ("Disposal/recycling", r"recycl|bin|waste|rubbish|cardboard|glass"),
        ("Reuse", r"reuse|tupperware|bag|jar|leftover|freeze"),
        ("Routines", r"week|day|campus|work|job|travel|routine|time"),
    ]
    sentences = re.split(r"(?<=[.!?])\s+", b_text)
    for domain, pat in domain_patterns:
        hits = [s.strip()[:160] for s in sentences if re.search(pat, s, re.I) and len(s.strip()) > 40]
        if hits:
            themes[domain] = hits[:2]
    return themes


def infer_profile(name: str, interview_1: str) -> str:
    b_lines = [ln[2:].strip() for ln in interview_1.splitlines() if ln.startswith("B:")][:40]
    snippet = " ".join(b_lines)[:1200]
    # lightweight signals
    signals = []
    if re.search(r"student|university|uni|degree|year", snippet, re.I):
        signals.append("university student")
    if re.search(r"vegetarian|vegan", snippet, re.I):
        signals.append("vegetarian/vegan")
    if re.search(r"wheelchair|disabled|assistance dog", snippet, re.I):
        signals.append("disabled; uses assistance dog")
    if re.search(r"flatmate|housemate|live with", snippet, re.I):
        m = re.search(r"live with (\w+|four|five|six|\d+)", snippet, re.I)
        signals.append("shared student house" if m else "shared accommodation")
    if re.search(r"aldi|tesco|asda|sainsbury", snippet, re.I):
        store = re.search(r"(Aldi|Tesco|Asda|Sainsbury)", snippet, re.I)
        if store:
            signals.append(f"shops at {store.group(1)}")
    base = f"**Profile:** P0 participant ({name}). "
    if signals:
        base += "; ".join(signals[:5]).capitalize() + ". "
    base += "See Interview 1 themes for household, food, and packaging context."
    return base


def questions_md(title: str, text: str, limit: int, callback_note: str = "") -> str:
    qs = extract_questions(text, limit=limit)
    groups = group_questions(qs)
    lines = [f"#### {title}", ""]
    if callback_note:
        lines.append(callback_note)
        lines.append("")
    for domain, items in groups.items():
        lines.append(f"**{domain}**")
        for q in items:
            lines.append(f"- {q}")
        lines.append("")
    return "\n".join(lines).rstrip()


def render_participant(name: str, data: dict, texts: dict[str, str]) -> str:
    phase = data["phase"]
    parts = [
        phase_heading(name, phase),
        "",
        infer_profile(name, texts.get("interview_1", "")),
        "",
        "### Data order and volume",
        "",
        "| Step | Calibration step | File | Date | Words | Characters |",
        "|------|------------------|------|------|-------|------------|",
    ]
    for f in data["files"]:
        parts.append(
            f"| {f['step_num']} | {f['step_label']} | `{f['filename']}` | {f['date_prefix']} "
            f"| {f['words']:,} | {f['characters']:,} |"
        )
    t = data["totals"]
    parts += [
        "",
        f"**Participant totals:** {t['words']:,} words · {t['characters']:,} characters · {t['file_count']} files",
        "",
        "---",
        "",
        "### Step summaries",
        "",
    ]

    lens_summary: list[tuple[str, list[str]]] = []

    for f in data["files"]:
        key = f["step_key"]
        text = texts.get(key, "")
        title = STEP_TITLES.get(key, key)
        parts.append(f"#### {title} — {f['words']:,} words · {f['characters']:,} characters")
        parts.append("")
        parts.append("**Themes:**")

        if key.startswith("diary"):
            bullets = diary_themes(text)
            if bullets:
                for b in bullets:
                    parts.append(f"- {b}")
            else:
                parts.append("- Short photo-led diary batch; see attached images referenced in source file.")
        elif key.startswith("followup") and not text.strip().startswith("A:"):
            # researcher notes
            notes = [ln.strip() for ln in text.splitlines() if len(ln.strip()) > 30][:8]
            for n in notes:
                parts.append(f"- {n[:200]}")
        else:
            themes = interview_themes(text)
            if themes:
                for domain, items in themes.items():
                    parts.append(f"- **{domain}:** " + "; ".join(items))
            else:
                parts.append("- See interview transcript for step coverage.")

        lenses = tag_lenses(text)
        parts.append("")
        parts.append(f"**Behavioral lenses:** {', '.join(lenses) if lenses else 'See themes above'}.")
        parts.append("")

        if key in ("followup_1", "followup_2", "interview_2"):
            anchor = title.lower().replace(" ", "-").replace("(", "").replace(")", "")
            anchor = re.sub(r"[^a-z0-9-]", "", anchor)
            parts.append(f"**Questions asked:** See [{title}](#{anchor}) below.")
            parts.append("")

        parts.append("---")
        parts.append("")
        lens_summary.append((title.split("—")[0].strip(), lenses))

    parts += ["### Interview questions", ""]

    parts.append(questions_md("Interview 1 (Step 0)", texts.get("interview_1", ""), 25))
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append(
        questions_md(
            "Interview 2 (held out)",
            texts.get("interview_2", ""),
            28,
            "**Diary callbacks (where applicable)**",
        )
    )
    parts.append("")
    parts.append("---")
    parts.append("")
    fu1_limit = 12 if texts.get("followup_1", "").startswith("A:") else 10
    fu1 = texts.get("followup_1", "")
    if not fu1.startswith("A:"):
        fu1_qs = [
            "Has participation changed how you notice packaging?",
            "Walk through key diary photos from this period. *(diary callback)*",
            "Tell me about meals or shopping moments flagged in the diary. *(diary callback)*",
            "What happened to the packaging from those items? *(diary callback)*",
            "How does disposal here compare with home or prior habits?",
        ]
        parts.append("#### Follow-up 1 (Step 3)")
        parts.append("")
        parts.append("**Diary callbacks / photo-elicitation**")
        for q in fu1_qs:
            parts.append(f"- {q}")
    else:
        parts.append(questions_md("Follow-up 1 (Step 3)", fu1, fu1_limit, "**Diary callbacks**"))
    parts.append("")
    parts.append("---")
    parts.append("")
    fu2 = texts.get("followup_2", "")
    if not fu2.startswith("A:"):
        parts.append("#### Follow-up 2 (Step 7)")
        parts.append("")
        parts.append("**Diary callbacks (researcher-led probes)**")
        for ln in [l.strip() for l in fu2.splitlines() if l.strip().startswith("[") or "?" in l][:12]:
            parts.append(f"- {ln.lstrip('[]0123456789.: ')[:180]} *(diary callback)*")
    else:
        parts.append(questions_md("Follow-up 2 (Step 7)", fu2, 12, "**Diary callbacks**"))

    parts += ["", "---", "", "### Behavioral lens summary across steps", "", "| Step | Primary lenses |", "|------|----------------|"]
    for step, lenses in lens_summary:
        parts.append(f"| {step} | {', '.join(lenses[:5]) if lenses else '—'} |")

    return "\n".join(parts)


def main() -> None:
    names = sys.argv[1:] if len(sys.argv) > 1 else [
        "Ella", "Jacob", "Cath", "Marina", "Stephen", "Josie",
        "Francesca", "Amy", "Gemma", "Laura", "Hannah", "Naomi", "Sophia", "Katie", "John",
    ]
    OUT.mkdir(exist_ok=True)
    for name in names:
        meta_path = EXTRACTED / name.lower() / "meta.json"
        data = json.loads(meta_path.read_text())
        texts = {}
        for f in data["files"]:
            p = EXTRACTED / name.lower() / f"{f['step_key']}.txt"
            if p.exists():
                texts[f["step_key"]] = p.read_text()
        md = render_participant(name, data, texts)
        out_path = OUT / f"{name.lower()}.md"
        out_path.write_text(md)
        print(f"Wrote {out_path} ({len(md.splitlines())} lines)")


if __name__ == "__main__":
    main()
