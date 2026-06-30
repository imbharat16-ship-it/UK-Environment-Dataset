#!/usr/bin/env python3
"""Classify P0 participant files, extract text, and compute volume counts."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "857315_data"

P0_PARTICIPANTS: dict[str, dict] = {
    "Eliza": {"household": "Household12Eliza", "phase": 1, "diaries": 4},
    "Isabella": {"household": "Household13Isabella", "phase": 1, "diaries": 4},
    "Ella": {"household": "Household14Ella", "phase": 1, "diaries": 4},
    "Jacob": {"household": "Household15Jacob", "phase": 1, "diaries": 4},
    "Cath": {"household": "Household16Cath", "phase": 1, "diaries": 4},
    "Marina": {"household": "Household17Marina", "phase": 1, "diaries": 4},
    "Stephen": {"household": "Household18Stephen", "phase": 1, "diaries": 5},
    "Josie": {"household": "Household20Josie", "phase": 1, "diaries": 4},
    "Francesca": {"household": "Household21Francesca", "phase": 2, "diaries": 4},
    "Amy": {"household": "Household22Amy", "phase": 2, "diaries": 5},
    "Gemma": {"household": "Household23Gemma", "phase": 2, "diaries": 4},
    "Laura": {"household": "Household26Laura", "phase": 2, "diaries": 4},
    "Hannah": {"household": "Household27Hannah", "phase": 2, "diaries": 4},
    "Naomi": {"household": "Household03Naomi", "phase": 3, "diaries": 4},
    "Sophia": {"household": "Household07Sophia", "phase": 3, "diaries": 4},
    "Katie": {"household": "Household09Katie", "phase": 3, "diaries": 5},
    "John": {"household": "Household10John", "phase": 3, "diaries": 4},
}

CANONICAL_ORDER = [
    "interview_1",
    "diary_1",
    "diary_2",
    "followup_1",
    "diary_3",
    "diary_4",
    "diary_5",
    "followup_2",
    "interview_2",
]

STEP_LABELS = {
    "interview_1": ("0", "Interview 1"),
    "diary_1": ("1", "Diary 1"),
    "diary_2": ("2", "Diary 2"),
    "followup_1": ("3", "Follow-up interview 1"),
    "diary_3": ("4", "Diary 3"),
    "diary_4": ("5", "Diary 4"),
    "diary_5": ("6", "Diary 5"),
    "followup_2": ("7", "Follow-up interview 2"),
    "interview_2": ("—", "Interview 2 (held out)"),
}


@dataclass
class FileRecord:
    step_key: str
    step_num: str
    step_label: str
    filename: str
    date_prefix: str  # DD/MM/YY display date
    words: int
    characters: int
    notes: str = ""


def find_household_dir(household: str) -> Path:
    for group in ("Households1_10", "Households11_20", "Households21_27"):
        candidate = DATA_DIR / group / household
        if candidate.is_dir():
            return candidate
    raise FileNotFoundError(f"Household folder not found: {household}")


def classify_file(filename: str) -> str | None:
    f = filename.lower().strip()

    if re.search(r"interview[\s_]*1|first[\s_]*interview", f):
        return "interview_1"
    if re.search(r"interview[\s_]*2|final[\s_]*interview", f):
        return "interview_2"
    if "follow" in f:
        return "followup_1" if re.search(r"follow[\s_]*up[\s_]*1|follow up_1", f) else "followup_2"

    diary_match = re.search(r"(?:diary|entries|entry)[\s_]*(\d+)", f)
    if diary_match:
        return f"diary_{diary_match.group(1)}"

    entries_match = re.search(r"entries[_\s]*(\d+)", f)
    if entries_match:
        return f"diary_{entries_match.group(1)}"

    return None


def extract_text(docx_path: Path) -> str:
    result = subprocess.run(
        ["textutil", "-convert", "txt", "-stdout", str(docx_path)],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.replace("\r\n", "\n").replace("\r", "\n")


def count_text(text: str) -> tuple[int, int]:
    words = len(text.split())
    characters = len(text)
    return words, characters


def date_from_filename(filename: str) -> str:
    """Return filename date as DD/MM/YY, or empty string if not parseable."""
    match = re.match(r"(\d{4})(\d{2})(\d{2})", filename)
    if not match:
        return ""
    year, month, day = match.group(1), match.group(2), match.group(3)
    return f"{day}/{month}/{year[2:]}"


def ordering_anomaly(step_key: str, filename: str, all_records: list[FileRecord]) -> str:
    notes: list[str] = []
    if step_key == "diary_5":
        i2 = next((r for r in all_records if r.step_key == "interview_2"), None)
        raw = re.match(r"(\d{8})", filename)
        i2_raw = re.match(r"(\d{8})", i2.filename) if i2 else None
        if raw and i2_raw and raw.group(1) > i2_raw.group(1):
            notes.append("Submission date after Interview 2; ordered at Step 6 by batch number")
    return "; ".join(notes)


def process_participant(name: str, extract_body: bool = False) -> dict:
    meta = P0_PARTICIPANTS[name]
    household_dir = find_household_dir(meta["household"])
    files = sorted(p.name for p in household_dir.glob("*.docx"))

    classified: list[tuple[str, str]] = []
    for fname in files:
        key = classify_file(fname)
        if key:
            classified.append((key, fname))

    classified.sort(key=lambda x: CANONICAL_ORDER.index(x[0]))

    records: list[FileRecord] = []
    texts: dict[str, str] = {}

    for step_key, fname in classified:
        path = household_dir / fname
        text = extract_text(path)
        words, chars = count_text(text)
        if extract_body:
            texts[step_key] = text

        step_num, step_label = STEP_LABELS[step_key]
        record = FileRecord(
            step_key=step_key,
            step_num=step_num,
            step_label=step_label,
            filename=fname,
            date_prefix=date_from_filename(fname),
            words=words,
            characters=chars,
        )
        records.append(record)

    for record in records:
        record.notes = ordering_anomaly(record.step_key, record.filename, records)

    total_words = sum(r.words for r in records)
    total_chars = sum(r.characters for r in records)

    result = {
        "name": name,
        "phase": meta["phase"],
        "diaries": meta["diaries"],
        "household": meta["household"],
        "household_path": str(household_dir.relative_to(ROOT)),
        "files": [asdict(r) for r in records],
        "totals": {
            "words": total_words,
            "characters": total_chars,
            "file_count": len(records),
        },
    }
    if extract_body:
        result["texts"] = texts
    return result


def markdown_table(data: dict) -> str:
    lines = [
        "| Step | Calibration step | File | Date | Words | Characters |",
        "|------|------------------|------|------|-------|------------|",
    ]
    for f in data["files"]:
        lines.append(
            f"| {f['step_num']} | {f['step_label']} | `{f['filename']}` | {f['date_prefix']} "
            f"| {f['words']:,} | {f['characters']:,} |"
        )
    t = data["totals"]
    lines.append("")
    lines.append(
        f"**Participant totals:** {t['words']:,} words · {t['characters']:,} characters · {t['file_count']} files"
    )
    return "\n".join(lines)


def main() -> None:
    args = sys.argv[1:]
    extract_body = "--extract" in args
    emit_json = "--json" in args
    args = [a for a in args if a not in ("--extract", "--json")]

    names = args if args else list(P0_PARTICIPANTS)
    results = [process_participant(n, extract_body=extract_body) for n in names]

    if emit_json:
        print(json.dumps(results, indent=2))
        return

    for data in results:
        print(f"## {data['name']} (Phase {data['phase']})")
        print(markdown_table(data))
        print()


if __name__ == "__main__":
    main()
