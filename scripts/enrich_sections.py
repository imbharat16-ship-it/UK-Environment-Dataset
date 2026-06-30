#!/usr/bin/env python3
"""Patch section files with curated profiles and unique anchor suffixes."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = ROOT / "sections"
PROFILES = json.loads((ROOT / "scripts/participant_profiles.json").read_text())

NAMES = [
    "Eliza", "Isabella", "Ella", "Jacob", "Cath", "Marina", "Stephen", "Josie",
    "Francesca", "Amy", "Gemma", "Laura", "Hannah", "Naomi", "Sophia", "Katie", "John",
]


def slug(name: str) -> str:
    return name.lower()


def patch_profile(text: str, name: str) -> str:
    profile = PROFILES.get(name)
    if not profile:
        return text
    return re.sub(r"\*\*Profile:\*\*[^\n]*", profile, text, count=1)


def patch_anchors(text: str, name: str) -> str:
    s = slug(name)
    replacements = [
        ("Follow-up interview 1 (Step 3)", f"follow-up-interview-1-step-3-{s}"),
        ("Follow-up interview 2 (Step 7)", f"follow-up-interview-2-step-7-{s}"),
        ("Interview 2 (held out)", f"interview-2-held-out-{s}"),
        ("Follow-up 1 (Step 3)", f"follow-up-1-step-3-{s}"),
        ("Follow-up 2 (Step 7)", f"follow-up-2-step-7-{s}"),
        ("Interview 1 (Step 0)", f"interview-1-step-0-{s}"),
    ]
    for label, anchor in replacements:
        text = text.replace(f"[{label}](#{label.lower().replace(' ', '-').replace('(', '').replace(')', '')})", f"[{label}](#{anchor})")
        text = text.replace(f"(#{label.lower().replace(' ', '-').replace('(', '').replace(')', '')})", f"(#{anchor})")
        # normalize common auto anchors
        for variant in [
            label.lower().replace(" ", "-").replace("(", "").replace(")", ""),
            label.lower().replace(" ", "-"),
        ]:
            text = text.replace(f"](#{variant})", f"](#{anchor})")
        heading = f"#### {label}"
        unique_heading = f"#### {label} · {name}"
        text = text.replace(heading, unique_heading)
    return text


def main() -> None:
    for name in NAMES:
        path = SECTIONS / f"{slug(name)}.md"
        if not path.exists():
            print(f"Skip missing {path}")
            continue
        text = patch_anchors(patch_profile(path.read_text(), name), name)
        path.write_text(text)
        print(f"Patched {path.name} ({len(text.splitlines())} lines)")


if __name__ == "__main__":
    main()
