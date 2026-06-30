#!/usr/bin/env python3
"""Assemble P0_PARTICIPANT_SUMMARIES.md from header + section files."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = ROOT / "sections"
OUT = ROOT / "P0_PARTICIPANT_SUMMARIES.md"

PHASE_ORDER = [
    ("Phase 1 · Pilot", 1, ["Eliza", "Isabella", "Ella", "Jacob", "Cath", "Marina", "Stephen", "Josie"]),
    ("Phase 2 · Confirm", 2, ["Francesca", "Amy", "Gemma", "Laura", "Hannah"]),
    ("Phase 3 · Extend", 3, ["Naomi", "Sophia", "Katie", "John"]),
]

ALL_NAMES = [n for _, _, names in PHASE_ORDER for n in names]


def load_totals() -> dict[str, dict]:
    totals: dict[str, dict] = {}
    for name in ALL_NAMES:
        meta_path = ROOT / ".extracted" / name.lower() / "meta.json"
        if meta_path.exists():
            data = json.loads(meta_path.read_text())
        else:
            out = subprocess.run(
                [sys.executable, str(ROOT / "scripts/classify_p0_files.py"), name, "--json"],
                capture_output=True,
                text=True,
                check=True,
            )
            data = json.loads(out.stdout)[0]
        totals[name] = {
            "phase": data["phase"],
            "diaries": data["diaries"],
            "files": data["totals"]["file_count"],
            "words": data["totals"]["words"],
            "characters": data["totals"]["characters"],
            "path": data["household_path"],
        }
    return totals


def phase_label(phase: int) -> str:
    return {1: "1 · Pilot", 2: "2 · Confirm", 3: "3 · Extend"}[phase]


def header(totals: dict[str, dict]) -> str:
    total_files = sum(t["files"] for t in totals.values())
    total_words = sum(t["words"] for t in totals.values())
    total_chars = sum(t["characters"] for t in totals.values())

    index_rows = []
    for name in ALL_NAMES:
        t = totals[name]
        index_rows.append(
            f"| {name} | {phase_label(t['phase'])} | {t['diaries']} | {t['files']} | "
            f"{t['words']:,} | {t['characters']:,} | `{t['path']}/` |"
        )

    return f"""# P0 Participant Summaries — UK Environment Dataset (857315)

> 17 P0 participants · calibration order · text volume · themes · interview questions · behavioral lenses  
> Reference: [kikilabs-plan.md](kikilabs-plan.md) · [DATA_SCHEMA.md](DATA_SCHEMA.md)

---

## How to read this document

**Data order** follows the twin calibration sequence from kikilabs-plan.md (batch-number based, not filename date):

`Interview 1 → Diary 1 → Diary 2 → Follow-up interview 1 → Diary 3 → Diary 4 [→ Diary 5] → Follow-up interview 2 → Interview 2`

**Step types:**
- **Interview 1 / Interview 2:** Opening and closing in-depth semi-structured interviews.
- **Diary 1–5:** Weekly participant diary batches (packaging, meals, shopping, disposal).
- **Follow-up interview 1 / 2:** Shorter mid-study **photo-elicitation interviews** (not diary entries). The researcher probes specific diary moments and photos the participant shared. Added at calibration Steps 3 and 7.

**Word/character counts** are computed from extracted plain text (`len(text)` for characters; whitespace-split tokens for words). Speaker labels and timestamps are included.

**Study domains** (from Appendix B): (1) household/home, (2) relationship with food, (3) food preparation, (4) shopping, (5) routines, (6) plastic packaging, (7) disposal/recycling, (8) packaging generally, (9) reuse.

**Behavioral lenses** (KikiLabs): Occasion · Pricing/value · Identity · Culture/social · Convenience tradeoff · Recycling diligence · Reuse tendency · Food waste sensitivity · Attitude-behavior gap.

---

## Dataset volume rollup

| Metric | Value |
|--------|-------|
| Participants summarised | 17 of 17 |
| Total files | {total_files} |
| Total words | {total_words:,} |
| Total characters | {total_chars:,} |

---

## Participant index

| Pseudonym | Phase | Diaries | Files | Total words | Total characters | Household path |
|-----------|-------|---------|-------|-------------|------------------|----------------|
{chr(10).join(index_rows)}

---
"""


def main() -> None:
    totals = load_totals()
    missing = [n for n in ALL_NAMES if not (SECTIONS / f"{n.lower()}.md").exists()]
    if missing:
        print("Missing section files:", ", ".join(missing), file=sys.stderr)
        sys.exit(1)

    parts = [header(totals)]
    for phase_title, _, names in PHASE_ORDER:
        parts.append(f"## {phase_title}\n")
        for name in names:
            content = (SECTIONS / f"{name.lower()}.md").read_text().rstrip()
            parts.append(content)
            parts.append("\n---\n")

    parts.append(
        "\n*Generated from `scripts/classify_p0_files.py` + qualitative synthesis.*\n"
    )
    OUT.write_text("\n".join(parts))
    print(f"Wrote {OUT} ({len(OUT.read_text().splitlines())} lines)")


if __name__ == "__main__":
    main()
