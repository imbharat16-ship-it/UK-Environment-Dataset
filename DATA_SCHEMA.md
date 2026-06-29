# Consumer Insights: Micro Insights — Data Schema

**UK Data Service study ID:** 857315  
**Project:** Plastic Packaging in People's Lives (PPiPL)  
**Data location:** `857315_data/`  
**Documentation source:** `857315_documentation/` (ReadMe, SUPPOR_1.DOC, participant materials)

---

## Overview

This dataset contains qualitative ethnographic research on UK consumers' everyday experiences with food plastic packaging. It is part of a broader three-year project examining the food packaging supply chain (production, consumption, post-consumption, and waste disposal) to help policymakers and industry bridge the attitude–behaviour gap in plastic packaging reduction.

The **Consumer Insights: Micro Insights** sub-study aimed to develop an in-depth understanding of consumers' everyday experiences of food plastic packaging across personal and social contexts, including disposal, reuse, and recycling behaviours.

**Citation:** Piacentini, M.G., Stowell, A.F., Hadley, C., Mumford, C., Cronin, J., Ferri, M., Hardy, J., Hendry, L., Kaloudis, H., Mumford, C., Razak, G., Skandalis, A., and Verma, S. (2024). *Plastic Packaging in People's Lives*.

---

## Dataset Summary

| Property | Value |
|---|---|
| **Format** | Microsoft Word (`.docx`) |
| **Total files** | 190 |
| **Total size** | ~79 MB (506 MB as originally deposited per UKDS documentation) |
| **Participants** | 27 households (pseudonymised) |
| **Collection period** | October 2021 – September 2022 |
| **Geography** | United Kingdom |
| **Data type** | Qualitative text (transcripts, diary entries, field notes) |

### File counts by type

| Data type | Count | Description |
|---|---|---|
| In-depth interview transcripts | 52 | Opening and closing interviews with each participant |
| Follow-up interview transcripts/notes | 50 | Shorter photo-elicitation interviews based on diary entries |
| Participant diary entries | 87 | Weekly participant-produced reflections on food and packaging |
| Researcher field diary | 1 | Consolidated field notes from home visits and shopping trips |
| **Total** | **190** | |

---

## Directory Structure

```
857315_data/
├── FieldDiary/
│   └── FieldDiary.docx              # Researcher field notes (all participants)
├── Households1_10/                  # Participants 01–10
│   ├── Household01Evie/
│   ├── Household02Emilia/
│   ├── ...
│   └── Household10John/
├── Households11_20/                 # Participants 11–20
│   ├── Household11Sarah/
│   ├── ...
│   └── Household20Josie/
└── Households21_27/                 # Participants 21–27
    ├── Household21Francesca/
    ├── ...
    └── Household27Hannah/
```

Each household folder contains all data files for one participant, linked by pseudonym.

---

## Data Entity Schema

This is a document-based qualitative dataset, not a tabular database. The schema below describes the logical entities, their attributes, and relationships.

### Entity relationship diagram

```
┌─────────────────┐
│   Participant   │  (27 households, pseudonymised)
│  Household01–27 │
└────────┬────────┘
         │ 1:N
         ├──────────────────────────────────────────┐
         │                                          │
         ▼                                          ▼
┌─────────────────────┐              ┌──────────────────────────┐
│  InDepthInterview   │              │     DiaryEntries         │
│  (Interview 1 & 2)  │              │  (weekly, 4–5 weeks)     │
└────────┬────────────┘              └────────────┬─────────────┘
         │                                        │
         │              ┌─────────────────────────┘
         │              │ triggers
         │              ▼
         │    ┌─────────────────────┐
         └────│  FollowUpInterview  │
              │  (photo-elicitation)│
              └─────────────────────┘

┌─────────────────────┐
│    FieldDiary       │  (researcher notes, cross-participant)
└─────────────────────┘
```

---

## Entity Definitions

### 1. Participant (Household)

| Attribute | Type | Description |
|---|---|---|
| `household_id` | string | Folder name, e.g. `Household01Evie` |
| `pseudonym` | string | First name only, e.g. `Evie`, `Anthony` |
| `household_number` | integer | 01–27 |

**Linking key:** The pseudonym in the folder name and file name ties all records for one participant together.

---

### 2. In-Depth Interview

| Attribute | Type | Description |
|---|---|---|
| `file_name` | string | e.g. `20211013_Interview_1_Evie.docx` |
| `date` | date | Prefix `YYYYMMDD` in filename |
| `interview_number` | integer | `1` (opening) or `2` (closing/final) |
| `participant_pseudonym` | string | From filename |
| `format` | string | `.docx` |
| `content_type` | enum | `interview_transcript` |

**Internal structure (observed):**
- Speaker-labelled dialogue (e.g. `A:` = interviewer, `B:` = participant, `C:` = second interviewer)
- Semi-structured conversational format (not a fixed survey)
- Topics span household context, food habits, shopping, routines, plastic packaging, disposal, recycling, and reuse

**Typical count per participant:** 2 (opening + closing), except partial-data cases

---

### 3. Follow-Up Interview

| Attribute | Type | Description |
|---|---|---|
| `file_name` | string | e.g. `20211103_Follow_up_1_Evie.docx` |
| `date` | date | Prefix `YYYYMMDD` in filename |
| `follow_up_number` | integer | `1` or `2` |
| `participant_pseudonym` | string | From filename |
| `format` | string | `.docx` |
| `content_type` | enum | `follow_up_interview_transcript_or_notes` |
| `method` | string | Photo-elicitation based on participant diary entries |

**Internal structure (observed):**
- Header with household number, pseudonym, follow-up number, and date
- Shorter, targeted questions referencing specific diary entries
- May include descriptions of photos or objects shown during the session

**Typical count per participant:** 2 (mid-study intervals)

---

### 4. Diary Entries

| Attribute | Type | Description |
|---|---|---|
| `file_name` | string | e.g. `20211019_Evie_diary_entries_1.docx` |
| `date_submitted` | date | Prefix `YYYYMMDD` in filename (submission date, not entry date) |
| `batch_number` | integer | Sequential batch, e.g. `_1`, `_2`, `_3` |
| `participant_pseudonym` | string | From filename |
| `format` | string | `.docx` |
| `content_type` | enum | `participant_diary_entries` |

**Internal structure (observed):**
- Dated bullet-point entries (e.g. `13th Oct 2021:`)
- Free-text reflections on daily food and packaging experiences
- May include embedded photographs of food, packaging, bins, or meals
- Content covers meals, shopping, unpacking, disposal/recycling, thoughts, and observations

**Typical count per participant:** 4–5 weekly batches over 4–5 weeks

---

### 5. Field Diary

| Attribute | Type | Description |
|---|---|---|
| `file_name` | string | `FieldDiary.docx` |
| `location` | string | `FieldDiary/` |
| `format` | string | `.docx` |
| `content_type` | enum | `researcher_field_notes` |

**Internal structure (observed):**
- Dated narrative entries (e.g. `3rd October 2021 – Introductory meeting with Evie`)
- Researcher observations from home visits, shopping trips, and informal "hanging out" sessions
- Reflective notes on participant behaviour, home environments, and packaging in context
- Cross-references participants by pseudonym

---

## File Naming Convention

```
{YYYYMMDD}_{DocumentType}_{Details}_{Pseudonym}.docx
```

| Component | Examples |
|---|---|
| Date | `20211013`, `20220224` |
| Document type | `Interview_1`, `Interview_2`, `Final_Interview`, `Follow_up_1`, `Follow_up_2`, `diary_entries_1`, `diary_entry_2` |
| Pseudonym | `Evie`, `Anthony`, `Sophia` |

**Notes:**
- Naming is mostly consistent but has minor variations (e.g. `First_Interview` vs `Interview_1`, `Final_Interview` vs `Interview_2`, apostrophe placement, occasional spaces).
- Some diary batches combine multiple weeks (e.g. `Anthony_diary_entries_1_3`).

---

## Research Methodology (Data Collection Design)

| Stage | Method | Frequency |
|---|---|---|
| Opening interview | In-depth semi-structured interview | Once, at study start |
| Diary keeping | Participant-produced weekly diary entries | 4–5 weeks |
| Follow-up interviews | Short photo-elicitation interviews | ~2 intervals during diary period |
| Closing interview | In-depth semi-structured interview | Once, at study end |
| Fieldwork | Researcher observations at home, work, and shopping | Throughout study period |

**Fieldwork settings:** Participants' homes, workplaces, and food shopping environments (supermarkets, etc.).

---

## Thematic Content (What the Data Contains)

Interview and diary topics documented in the study materials:

- Household, home, and neighbourhood context
- Relationship with food
- Food preparation and consumption
- Food shopping behaviours and habits
- Everyday routines
- Food plastic packaging (awareness, choices, frustrations)
- Food plastic packaging disposal and recycling
- Food packaging more generally (cardboard, glass, etc.)
- Reuse behaviours

**Diary entry content examples:**
- Specific meals and food choices
- Grocery shopping and unpacking at home
- Packaging disposed of in general waste or recycling bins
- Observations about others' recycling behaviour
- Reuse of containers and takeaway tubs
- Reflections on food waste

**Field diary content examples:**
- Home pantry and fridge observations
- Supermarket shopping trip shadowing
- Local council bin setups and recycling infrastructure
- Participant attitudes toward plastic and sustainability

---

## Data Completeness and Exceptions

Not all 27 participants have a full set of all four data types. Documented exceptions:

| Participant | Missing / partial data | Reason |
|---|---|---|
| **Tom** | No diary entries | Not provided or provided in non-anonymisable format (video, PDF) |
| **Lisa** | No diary entries | Same |
| **Grace** | No diary entries; only opening interview | Same |
| **Nathan** | No diary entries | Same |
| **Evie** | Partial diary data | Incomplete or alternate format (anonymisation not possible) |
| **Emilia** | Partial diary data | Same |
| **Anthony** | Partial diary data | Same |
| **Alan** | Partial data (1 diary batch, no closing interview) | Same |
| **Maria** | Partial data | Referenced in documentation; not present in current folder structure |
| **Sarah** | Missing 1 follow-up interview | Not documented as anonymisation-related |
| **Zoe** | Missing 1 diary batch | Not documented as anonymisation-related |

---

## Per-Participant File Inventory

`P3` = participant has missing or partial data (see [Data Completeness and Exceptions](#data-completeness-and-exceptions)).

`P0` = complete deposited file set with no missing or partial data.

`Anonym. excluded` = some data was withheld from deposit because anonymisation was not possible (e.g. video, PDF, or unanonymisable diary content), per UKDS documentation. None of the P0 participants are flagged.

| Household | Pseudonym | Interviews | Follow-ups | Diary batches | Total files | Priority | Anonym. excluded |
|---|---|---|---|---|---|---|---|
| Household01Evie | Evie | 2 | 2 | 2 | 6 | P3 | Yes |
| Household02Emilia | Emilia | 2 | 2 | 4 | 8 | P3 | Yes |
| Household03Naomi | Naomi | 2 | 2 | 4 | 8 | P0 | |
| Household04Tom | Tom | 2 | 2 | 0 | 4 | P3 | Yes |
| Household05Lisa | Lisa | 2 | 2 | 0 | 4 | P3 | Yes |
| Household06Anthony | Anthony | 2 | 2 | 2 | 6 | P3 | Yes |
| Household07Sophia | Sophia | 2 | 2 | 4 | 8 | P0 | |
| Household08Alan | Alan | 1 | 1 | 1 | 3 | P3 | Yes |
| Household09Katie | Katie | 2 | 2 | 5 | 9 | P0 | |
| Household10John | John | 2 | 2 | 4 | 8 | P0 | |
| Household11Sarah | Sarah | 2 | 1 | 4 | 7 | P3 | |
| Household12Eliza | Eliza | 2 | 2 | 4 | 8 | P0 | |
| Household13Isabella | Isabella | 2 | 2 | 4 | 8 | P0 | |
| Household14Ella | Ella | 2 | 2 | 4 | 8 | P0 | |
| Household15Jacob | Jacob | 2 | 2 | 4 | 8 | P0 | |
| Household16Cath | Cath | 2 | 2 | 4 | 8 | P0 | |
| Household17Marina | Marina | 2 | 2 | 4 | 8 | P0 | |
| Household18Stephen | Stephen | 2 | 2 | 5 | 9 | P0 | |
| Household19Grace | Grace | 1 | 0 | 0 | 1 | P3 | Yes |
| Household20Josie | Josie | 2 | 2 | 4 | 8 | P0 | |
| Household21Francesca | Francesca | 2 | 2 | 4 | 8 | P0 | |
| Household22Amy | Amy | 2 | 2 | 5 | 9 | P0 | |
| Household23Gemma | Gemma | 2 | 2 | 4 | 8 | P0 | |
| Household24Nathan | Nathan | 2 | 2 | 0 | 4 | P3 | Yes |
| Household25Zoe | Zoe | 2 | 2 | 3 | 7 | P3 | |
| Household26Laura | Laura | 2 | 2 | 4 | 8 | P0 | |
| Household27Hannah | Hannah | 2 | 2 | 4 | 8 | P0 | |

---

## Linking Records Across Files

All data for one participant links via:

1. **Pseudonym** in the household folder name and file name
2. **Chronological date prefix** (`YYYYMMDD`) for temporal ordering
3. **Cross-references in text** (follow-up interviews explicitly reference diary entry content; field diary entries reference participants by name)

There is no separate ID table or metadata CSV. Relationships must be inferred from folder structure and naming.

---

## Privacy and Anonymisation

- Participants are identified by first-name pseudonyms only
- Location names are redacted in transcripts (shown as `[x]`)
- Personal names of family/friends may appear as `[Friend 1]`, `[xxx]`, etc.
- Some data was excluded from deposit where anonymisation was not possible (video, PDF, or unanonymisable diary content)

---

## Related Documentation Files

| File | Purpose |
|---|---|
| `857315_documentation/ReadMe_File_for_ConsumerInsights_MicroInsights.docx` | Per-file catalogue with descriptions and linking notes |
| `857315_documentation/SUPPOR_1.DOC` | Full data documentation (methodology, file list, exceptions) |
| `857315_documentation/Participant_Information_Sheet.docx` | Study information provided to participants |
| `857315_documentation/Participant_consent_form.docx` | Consent form template |

---

## Suggested Usage Notes

- **Parsing:** Extract text from `.docx` files (e.g. via `python-docx`, Pandoc, or macOS `textutil`).
- **Analysis:** Suitable for thematic analysis, discourse analysis, or NLP on qualitative text. No structured fields beyond filename metadata.
- **Temporal analysis:** Use the `YYYYMMDD` filename prefix to order events within a participant's timeline.
- **Cross-participant analysis:** Field diary provides researcher perspective; participant data is in household folders.
- **Incomplete cases:** Filter or flag participants with missing diary data when analysing packaging behaviour from diaries specifically.
