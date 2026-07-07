#!/usr/bin/env python3
"""Merge Eliza E*P.md predictions into E*B.md benchmark files."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1] / "Eliza Experiments"

ACTUALS = {
    1: (
        "Eliza #75",
        """Again this is awful to say but just this information never gets to us. People just say it is better to have paper and I always believe that it is because that's what I've been hearing since I was little. I've never got the information why is it better. Because now you're asking me this and I was like yeah, I mean paper is better, but why is it better and I have no idea because I don't understand the science behind it or what happens to the paper after, I have no idea. I don't know why is it better. I think its better because people say its better. And they always say something like, yeah use paper, lets save the turtles. Why? Why, because I mean obviously if you throw plastic to the sea its going to be worse than throwing paper but its just as bad as throwing paper. So I don't understand why its that bad, but I don't think that information comes to us either way.

They always talk about the big things but they never go to the actual, yeah you should do this because this happens, which sometimes that happens is [53:58] for example. At least in [home country].""",
    ),
    2: (
        "Eliza #71",
        """I think its definitely something that is changing because I do see a lot of things just being like with paper and things like, so I think its changing and I'm glad it is. I am glad is it. Yeah I don't know what to say.""",
    ),
    3: (
        "Eliza #75",
        "*(Same thread as Question 1.)*",
    ),
    4: (
        "Eliza #112",
        """Yeah I don't know because again its not that I can't be impartial because I don't know the science behind the plastic in terms of yes I know its bad for the environment because I saw that it is but I don't understand why. Like specifically what is the thing that is so bad about plastic? Ok yeah assuming that the plastic is not going to go in, throwing at the sea and polluting, but what is the thing about plastic that is so bad, I don't understand that. While with food I understand what is so bad about wasting food. I've seen the damaging in the, the people that don't have access to food and stuff like that and I know how much it costs to buy food because obviously I pay for food so, its something that I have more present in my life than what plastic waste actually is. So I think I would prefer to buy something in plastic that can make, yeah that can make food longer, that just buy something in paper and then the food goes bad. Because I think maybe its just because its something that is more present in my life because I know how bad it is to just, I mean I've seen how bad it is to not get food. I know there are people that cannot have food. I know how much it costs to get money and then to buy food. So yeah it's a bit like that. I think I just don't know the science behind plastic that much.""",
    ),
    5: (
        "Eliza #13 (laundry / Smol)",
        """The first time I started using capsules was this year. Because last year obviously we were on those laundries on campus and to be fair I do have a lot of clothes so I don't have to do laundry every week. And to be fair I think when you're on campus it's a lot different because every time you go and do laundry on campus be there like once a week to twice a week, every time you go there its like £6. So it something that like for a student I had flat mates going and like yeah I have to go twice a week where that's almost £10. It is a lot. So you start managing that. And in terms of, I don't know because, yeah last year I bought a liquid for example, its like a whole litre of liquid and it lasted forever. And then, but then obviously I started realising how frequently I need to do my washing and everything, which is not that frequently because I have enough clothes. So yeah and it depends because sometimes you have trials, for example these last capsules that I bought was because I was part of a trial or something.

Yeah its kind of a trial of a student discount, its like ok we'll give you all a box with like 10 capsules and then if you want you can continue and buy it or you don't. So obviously there is some things and then a lot of promotions that are related to students, so it depends. I don't know which one I prefer to be honest. I think they're basically the same. I think if you do washing more frequently the definitely liquid.

So I mean basically I just, I think I just found it randomly on Instagram I think. Because there's a student at uni and she was promoting this.

Yeah. I think there is a student at university and she was promoting this because like washing capsules like made out of recycling, it was something like that and I don't know these are really directed to students and I don't know I was just curious and I was like ok yeah sure. Yeah and then basically they offer the first 10 and then you can continue or you just stop. And I was like ok why not. Because I never tried capsules and to be fair I prefer to pay like £1-2 for those capsules than go to an actual grocery shop and spend like £5 on capsules that I don't know if I'm going to like. I don't know its just, and it's a good way, yeah you're going to have things to wash for the next month, one month, to months and yeah for like, it's a trial. I don't know.

I think, in terms of the brand I think they sell more things, they sell like dishwasher machines, type of thing, but we don't have one so there was no point. But I think its just cleaning products honestly.

I think so. I can give you the brand if you want. I can give you the name of the brand if you want to search.

Its just, yeah I think their thing is they do, the plastic around the liquid basically, that involves the liquid, its made out of recycling plastics. I think its something like that. I think its something like that. And then they make it in smaller amounts so they don't have to waste as much. Like enough liquid to do a washing, but in small amounts so you don't have to waste as much plastic. I think its something like that.

Its called Smol.""",
    ),
}

QUESTIONS = {
    1: "How do alternative packaging materials compare to plastic for you?",
    2: "What are your views on the environmental impact of plastic food packaging?",
    3: 'How confident are you that you know the "right" packaging choice?',
    4: "How does food waste or freshness affect your packaging/shopping choices?",
    5: "Does packaging influence what you buy?",
}


def extract_predictions(path: Path) -> dict[int, str]:
    text = path.read_text()
    preds: dict[int, str] = {}
    for m in re.finditer(
        r"## Question (\d+) ·[^\n]*\n(?:.*?\n)*?### Predicted response\n\n(.*?)(?=\n---|\n## Question |\Z)",
        text,
        re.DOTALL,
    ):
        preds[int(m.group(1))] = m.group(2).strip()
    return preds


def extract_rationales(path: Path) -> dict[int, tuple[int, str]]:
    text = path.read_text(encoding="utf-8")
    out: dict[int, tuple[int, str]] = {}
    for m in re.finditer(
        r"### Q(\d+) · Score (\d+)\n\n\*\*matchRationale:\*\* (.*?)(?=\n\n### |\n---|\n## |\Z)",
        text,
        re.DOTALL,
    ):
        out[int(m.group(1))] = (int(m.group(2)), m.group(3).strip())
    if not out:
        for m in re.finditer(
            r"## Question (\d+) ·[^\n]*\n(?:.*?\n)*?### Score: \*\*(\d+)\*\*\n\n\*\*matchRationale:\*\* (.*?)(?=\n\n---|\n## Question |\Z)",
            text,
            re.DOTALL,
        ):
            out[int(m.group(1))] = (int(m.group(2)), m.group(3).strip())
    return out


def blockquote(text: str) -> str:
    return "\n".join(f"> {line}" if line else ">" for line in text.splitlines())


def build_question_section(qnum: int, predicted: str, score: int, rationale: str) -> str:
    turn, actual = ACTUALS[qnum]
    if qnum == 3:
        actual_display = "> *(See Question 1 actual response.)*"
    else:
        actual_display = blockquote(actual)
    return f"""## Question {qnum} · {QUESTIONS[qnum]}

**Question type:** OPEN-ENDED · **Actual turn:** {turn}

### Actual response

{actual_display}

### Predicted response

{blockquote(predicted)}

### Score: **{score}**

**matchRationale:** {rationale}
"""


RUNS = {
    "E3": {
        "title": "Eliza · Run 3 Benchmark (Raw + Tone)",
        "meta": """**Run 3** · Raw transcript + tone register  
**Evidence:** `E-Data.md` · **Tone:** `E-Lenses.md` voice register  
**Actual:** `Cohort-based questions.md` (Interview 2, held-out)""",
        "summary_extra": """| Metric | Raw+Tone | Raw |
|--------|----------:|----:|
| Mean | **67.8** | 64.2 |
| Mean (excl. Q5) | **73.8** | 69.3 |""",
    },
    "E4": {
        "title": "Eliza · Run 4 Benchmark (Selective Lenses)",
        "meta": """**Run 4** · Selective lenses (2 per question) + tone  
**Evidence:** `E-Data.md` · **Lenses:** `E-Lenses.md` (2 per question)  
**Actual:** `Cohort-based questions.md` (Interview 2, held-out)""",
        "summary_extra": """| Metric | Selective | Raw+Tone |
|--------|----------:|---------:|
| Mean | **70.2** | 67.8 |
| Mean (excl. Q5) | **76.8** | 73.8 |""",
    },
    "E4c": {
        "title": "Eliza · Run 4c Benchmark (Selective Lenses · GPT-5.4)",
        "meta": """**Run 4c** · Selective lenses · Model: GPT-5.4 · Blind  
**Evidence:** `E-Data.md` · **Lenses:** `E-Lenses.md` (2 per question)  
**Actual:** `Cohort-based questions.md` (Interview 2, held-out)""",
        "summary_extra": """| Metric | Run 4c (blind) | Run 4 | Δ |
|--------|---------------:|------:|--:|
| Mean | **70.8** | 70.2 | +0.6 |
| Mean (excl. Q5) | **77.5** | 76.8 | +0.7 |""",
    },
}


def merge_run(prefix: str, cfg: dict) -> None:
    p_path = ROOT / f"{prefix}P.md"
    b_path = ROOT / f"{prefix}B.md"
    preds = extract_predictions(p_path)
    rationales = extract_rationales(b_path)

    scores = [rationales[i][0] for i in range(1, 6)]
    mean = round(sum(scores) / len(scores), 1)
    mean_excl = round(sum(scores[:4]) / 4, 1)

    summary_rows = "\n".join(
        f"| {i} | {QUESTIONS[i][:40]}{'…' if len(QUESTIONS[i]) > 40 else ''} | **{rationales[i][0]}** |"
        for i in range(1, 6)
    )

    sections = "\n---\n\n".join(
        build_question_section(i, preds[i], rationales[i][0], rationales[i][1])
        for i in range(1, 6)
    )

    content = f"""# {cfg['title']}

{cfg['meta']}

---

## Summary

| # | Question | Score |
|---|----------|------:|
{summary_rows}
| **Mean** | | **{mean}** |
| **Mean (excl. Q5)** | | **{mean_excl}** |

{cfg['summary_extra']}

---

{sections}
"""
    b_path.write_text(content)
    print(f"merged {prefix} -> {b_path.name}")


def patch_existing_headers() -> None:
    for prefix in ("E1", "E2"):
        path = ROOT / f"{prefix}B.md"
        text = path.read_text()
        text = re.sub(
            r"\*\*Predicted source:\*\* `E\d+P\.md`[^\n]*\n",
            "",
            text,
        )
        text = re.sub(
            r"\*\*Benchmark comparison:\*\* `E1B\.md`[^\n]*\n",
            "",
            text,
        )
        if prefix == "E1":
            text = text.replace(
                "# Eliza · Prediction Accuracy Evaluation",
                "# Eliza · Run 1 Benchmark (Prior)",
            )
            insert = "**Run 1** · Prior pass · `E-Data.md` calibration only  \n**Actual:** `Cohort-based questions.md` (Interview 2, held-out)\n\n"
            text = text.replace(
                "**Scoring rules:**",
                insert + "**Scoring rules:**",
                1,
            )
        if prefix == "E2":
            text = text.replace(
                "# Eliza · Prediction Accuracy (Raw Transcript)",
                "# Eliza · Run 2 Benchmark (Raw)",
            )
            insert = "**Run 2** · Raw transcript only · `E-Data.md`  \n**Actual:** `Cohort-based questions.md` (Interview 2, held-out)\n\n"
            text = text.replace(
                "**Actual source:**",
                insert + "**Actual source:**",
                1,
            )
        path.write_text(text)
        print(f"patched {path.name}")


def main() -> None:
    for prefix, cfg in RUNS.items():
        merge_run(prefix, cfg)
    patch_existing_headers()
    for p in ROOT.glob("E*P.md"):
        p.unlink()
        print(f"deleted {p.name}")


if __name__ == "__main__":
    main()
