# P0 Participant Summaries — UK Environment Dataset (857315)

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
| Total files | 139 |
| Total words | 641,248 |
| Total characters | 3,301,574 |

---

## Participant index

| Pseudonym | Phase | Diaries | Files | Total words | Total characters | Household path |
|-----------|-------|---------|-------|-------------|------------------|----------------|
| Eliza | 1 · Pilot | 4 | 8 | 42,308 | 212,093 | `857315_data/Households11_20/Household12Eliza/` |
| Isabella | 1 · Pilot | 4 | 8 | 36,575 | 189,870 | `857315_data/Households11_20/Household13Isabella/` |
| Ella | 1 · Pilot | 4 | 8 | 36,625 | 187,996 | `857315_data/Households11_20/Household14Ella/` |
| Jacob | 1 · Pilot | 4 | 8 | 27,163 | 137,172 | `857315_data/Households11_20/Household15Jacob/` |
| Cath | 1 · Pilot | 4 | 8 | 48,201 | 247,925 | `857315_data/Households11_20/Household16Cath/` |
| Marina | 1 · Pilot | 4 | 8 | 43,737 | 225,912 | `857315_data/Households11_20/Household17Marina/` |
| Stephen | 1 · Pilot | 5 | 9 | 27,883 | 146,060 | `857315_data/Households11_20/Household18Stephen/` |
| Josie | 1 · Pilot | 4 | 8 | 44,408 | 223,539 | `857315_data/Households11_20/Household20Josie/` |
| Francesca | 2 · Confirm | 4 | 8 | 43,752 | 228,271 | `857315_data/Households21_27/Household21Francesca/` |
| Amy | 2 · Confirm | 5 | 9 | 40,344 | 208,867 | `857315_data/Households21_27/Household22Amy/` |
| Gemma | 2 · Confirm | 4 | 8 | 23,936 | 120,462 | `857315_data/Households21_27/Household23Gemma/` |
| Laura | 2 · Confirm | 4 | 8 | 28,132 | 147,139 | `857315_data/Households21_27/Household26Laura/` |
| Hannah | 2 · Confirm | 4 | 8 | 44,397 | 230,545 | `857315_data/Households21_27/Household27Hannah/` |
| Naomi | 3 · Extend | 4 | 8 | 42,322 | 214,257 | `857315_data/Households1_10/Household03Naomi/` |
| Sophia | 3 · Extend | 4 | 8 | 34,113 | 178,922 | `857315_data/Households1_10/Household07Sophia/` |
| Katie | 3 · Extend | 5 | 9 | 34,837 | 181,025 | `857315_data/Households1_10/Household09Katie/` |
| John | 3 · Extend | 4 | 8 | 42,515 | 221,519 | `857315_data/Households1_10/Household10John/` |

---

## Phase 1 · Interview 1 theme clusters

> For cohort-based simulations. **Primary themes** = cohort-defining anchors from Interview 1 step summaries. **Secondary themes** = refiners for simulation variants. Source: Interview 1 themes and question domains in this document (Phase 1 pilot only).
>
> **Cohort rule:** Each cohort must have **≥2 members** for simulation. Singleton assignments are merged into the nearest thematic neighbor (see cohort notes for within-cohort variance).

| Participant | Profile anchor | Primary themes | Secondary themes | Suggested cohort |
|-------------|----------------|----------------|------------------|------------------|
| Eliza | International student, solo in UK flat | International transition (Portugal → UK); budget-led student shopping; learning UK kerbside recycling | Bulk freezing & batch cooking; origin vs UK packaging norms; mum-guided cooking by phone; attitude–behavior gap on plastic | A · Student / shared household |
| Isabella | Vegetarian student, 6-person house | Vegetarian identity & values; origin vs UK recycling (Spain → UK); shared-house recycling blocked | Partner-led cooking (Pablo); Aldi list-based shopping; campus/street recycling workaround; attitude–behavior gap at home | A · Student / shared household |
| Ella | Env-science student, checkout worker | Environmental science identity; retail / checkout insider view; group-house shared meals | Pescetarian diet shift; staff-discount supermarket shop; influencing family recycling; convenience rice packets (gap) | B · Environmental systems practice |
| Jacob | International PG, solo in shared flat | International food adaptation; ethnic / multi-store sourcing; takeaway containers as kitchenware | Busy-schedule convenience (Eat India); batch stew cooking; minimal recycling-infrastructure focus; UK vs home-country shopping | A · Student / shared household |
| Cath | Semi-retired gardener, Green Party | Home growing & seasonal eating; meal planning & leftovers; high recycling & garden reuse | Green Party / activist identity; summer vs winter plastic split; soft-plastics pantry collection; Waitrose vs Aldi/Tesco split | C · High-practice homeowner |
| Marina | Car-free parent, refill shopper | Refill / low-packaging shopping; Oxfordshire recycling diligence; car-free mobility constraints | Split-week custody routine; anti plastic-wrapped produce; takeaway-tub freezing; weekend vs midweek cooking | C · High-practice homeowner |
| Stephen | Community-larder founder, council worker | Community food rescue / larder; civic environmental identity; multi-stream home recycling | Values intensity fluctuation; heavy freezing & food waste; pet food plastic (pouches); CAG / county waste networks | B · Environmental systems practice |
| Josie | Waste-sector marketer, meal planner | Waste-sector professional knowledge; integrated kitchen recycling setup; meal planning & loose preference | Household dietary restrictions; scrunch test / soft plastics; dog-food packaging; pre-renovation vs post-renovation bins | B · Environmental systems practice |

### Suggested simulation cohorts

| Cohort | Members | Shared Interview 1 signal | Within-cohort variance |
|--------|---------|---------------------------|------------------------|
| **A · Student / shared household** | Eliza, Isabella, Jacob | University life, shared kitchens, budget or convenience pressure; recycling often learned, blocked, or secondary | International transition (Eliza, Jacob) vs UK-native student (Isabella); recycling blocked at home (Isabella) vs learning curve (Eliza) vs thin focus (Jacob) |
| **B · Environmental systems practice** | Ella, Stephen, Josie | Packaging and waste understood through a **systems** lens (coursework, industry, or community infrastructure), not only household habit | Retail/checkout view (Ella) vs community larder (Stephen) vs waste-sector home systems (Josie) |
| **C · High-practice homeowner** | Cath, Marina | Proactive packaging reduction (grow / refill) plus strong domestic sorting routines | Garden-growing (Cath) vs refill/car-free shopping (Marina); both high recycling diligence |

*Ella was previously a singleton under "env-professional student"; merged into B with Stephen and Josie on shared systems-level environmental framing. Josie merged from "waste-professional household" for the same reason.*

### Cross-cohort bridges

Useful if merging cohorts when Phase 2/3 participants are added:

- **Recycling diligence (high):** Marina, Cath, Josie, Stephen — vs Eliza/Isabella (learning or blocked) — vs Jacob (thin focus in Interview 1)
- **Attitude–behavior gap on plastic:** Eliza, Isabella, Ella, Cath, Marina, Stephen, Josie
- **Meal planning / freezing:** Cath, Josie, Stephen, Eliza

---

## Phase 1 · Pilot

### Eliza (Phase 1)

**Profile:** International student from Portugal/Lisbon area; 3rd-year university student in UK. Lives with four flatmates in a rented town house; works a campus catering job (~8 hrs/week, flexible). Travels home frequently for family events (previously lived in a household of 16). Developed cooking, budgeting, and recycling habits after a COVID-era solo arrival.

### Data order and volume

| Step | Calibration step | File | Date | Words | Characters |
|------|------------------|------|------|-------|------------|
| 0 | Interview 1 | `20220222_First_interview_Eliza.docx` | 22/02/22 | 19,159 | 94,642 |
| 1 | Diary 1 | `20220303_Eliza_entries_1.docx` | 03/03/22 | 263 | 1,331 |
| 2 | Diary 2 | `20220311_Eliza_diary_entry_2.docx` | 11/03/22 | 171 | 879 |
| 3 | Follow-up interview 1 | `20220308_Follow_up_1_Eliza.docx` | 08/03/22 | 4,632 | 24,948 |
| 4 | Diary 3 | `20220317_Eliza_diary_entries_3.docx` | 17/03/22 | 164 | 836 |
| 5 | Diary 4 | `20220324_Eliza_diary_entries_4.docx` | 24/03/22 | 145 | 726 |
| 7 | Follow-up interview 2 | `20220322_Follow_up_2_Eliza.docx` | 22/03/22 | 5,115 | 25,584 |
| — | Interview 2 (held out) | `20220325_Final_interview_Eliza.docx` | 25/03/22 | 12,659 | 63,147 |

**Participant totals:** 42,308 words · 212,093 characters · 8 files

**Note:** Diary batches are very short (photo-led); most volume is in interviews and follow-up interviews.

---

### Step summaries

#### Interview 1 (Step 0) · Eliza — 19,159 words · 94,642 characters

**Themes:**
- **Household/home:** Large Portuguese family; moved alone to UK pre-Brexit; cultural shock (more liberal social norms); rented house with four flatmates, very different food habits.
- **Routines:** Campus catering job (~8 hrs/week flexible); travels home for Christmas/Easter/summer; pre-trip shopping freezes food.
- **Shopping:** Weekly Aldi shop on student budget; mental meal arithmetic (chicken for curry + enchiladas + lasagne); avoids 10p plastic bags, uses reusable Aldi carriers.
- **Food/preparation:** Learned cooking from mum phone calls (defrosting, storage); bulk chicken in freezer bags; lasagne from leftover veg; clingfilm-covered bowls when no containers.
- **Plastic packaging:** Associates plastic with cheap/easy; would prefer less plastic but budget wins; paper feels more fragile and shorter-lived.
- **Disposal/recycling:** Home country uses street-side yellow/green/blue communal bins; UK kerbside boxes (green/black) confused her until flatmates corrected; rinses raw chicken trays, bins thin films.
- **Reuse:** Freezer bags, takeaway tubs aspiration; parents unpack and wash veg at home; she keeps produce in original packaging in UK flat.

**Behavioral lenses:** Identity (international student, becoming independent), Culture/social (Portugal vs UK packaging/shopping norms), Pricing/value (bulk chicken, student budget), Convenience tradeoff (microwave rice, ready pasta), Recycling diligence (learning from flatmates, inconsistent on thin plastics), Food waste sensitivity (mum recipes, no waste at home), Attitude-behavior gap (wants less plastic, buys pre-packed).

---

#### Diary 1 (Step 1) — 263 words · 1,331 characters

**Themes:**
- Week spent in home country; photo-first diary method still being calibrated.
- **Breakfast:** Yogurt with granola or cereal; quick, no time for relaxed mornings while visiting friends.
- **Lunch:** Mostly reheated leftovers; out meeting people, no time to cook fresh meals.
- **Dinner:** Chicken (photo of plastic bag in fridge) and salmon with vegetables on two nights; other nights eating out (burgers, sushi) at restaurants or friends'/family houses.
- **Packaging context:** Parents responsible for shopping; vegetables already unpacked in fridge, no packaging photos possible.
- **Disposal/recycling:** Photo of home-country street bins (yellow plastic, green glass, blue paper, black general) to explain colour-scheme confusion on arriving in UK.

**Behavioral lenses:** Occasion (travel, eating out), Culture/social (home vs UK bin systems), Identity (less control when at parents').

---

#### Diary 2 (Step 2) — 171 words · 879 characters

**Themes:**
- First full week back in UK after home trip; mostly food already in fridge/freezer before travel.
- **Chicken/fajitas:** Defrosted entire 1 kg pack (forgot to pre-divide); fajita kit yielded three meals across separate days.
- **Leftover chaining:** Remaining fajita tomato sauce + chicken made into packaged noodle meals (two portions).
- **Quiche:** Two meals; frozen when travel plans changed.
- **Work meals:** Two evening shifts; dinner at job plus packed leftovers covered four meals.
- **Pasta bake:** Three portions using glass-jar sauce; pepper and tomato packaging reused across multiple meals.
- **Staples:** Same milk packaging as prior week; crumpets, snacks, chocolate.

**Behavioral lenses:** Food waste sensitivity (sauce/chicken chaining), Convenience tradeoff (fajita kit, pre-done pasta), Reuse tendency (multi-meal ingredients), Pricing/value (bulk chicken economics).

---

#### Follow-up interview 1 (Step 3) · Eliza — 4,632 words · 24,948 characters

**Themes:**
- **Study reflexivity:** Participation raised awareness of plastic types (thin chicken film vs thick tray); flatmates noticed photo sessions.
- **Diary method:** Prefers photos over prose; same ingredients span multiple meals in one batch of images.
- **Chicken handling:** Divides 1 kg packs into freezer bags; washes thick tray before recycling, bins thin cover; jars rinsed before recycling.
- **Travel food:** Early Manchester flight = airport meal deal (all plastic); return from home = sandwich from leftovers, no airport purchase.
- **Home vs UK groceries:** Parents unpack/wash veg into dedicated drawer; Eliza keeps UK produce in original packs until use.
- **Portugal packaging:** Loose produce weighed in store-branded plastic bags with printed labels; different raw meat counter norms.
- **Photo callbacks:** Salmon defrosted in boiling water in packaging; home recycling bin colours; milk carton (cardboard + possible inner plastic); screw-cap lid collection for wheelchair charity on campus.

**Questions asked:** See [Follow-up 1 (Step 3)](#follow-up-1-step-3-eliza) below.

**Behavioral lenses:** Pricing/value (airport meal deals, budget), Culture/social (family fridge routines vs student flat), Recycling diligence (rinse chicken tray), Occasion (travel meals), Attitude-behavior gap (knows recycling matters, skips thin films).

---

#### Diary 3 (Step 4) — 164 words · 836 characters

**Themes:**
- Late submission; end-of-term workload dominated the week.
- **Skipped meals:** Long campus days with no lunch; biscuits only on some days.
- **Batch cooking:** Curry at start of week (three meals); two portions frozen in microwave-safe plastic boxes bought for the purpose.
- **Quick meals:** Ramen and pre-packaged pasta when no time to cook.
- **Breakfast:** Yogurt/oats some days; crumpets or nothing on others.
- **Work:** Friday shift; dinner at work and packed lunch for Saturday.

**Behavioral lenses:** Occasion (end-of-term chaos), Convenience tradeoff (frozen curry, ramen, packaged pasta), Food waste sensitivity (batch cooking), Identity (student time pressure).

---

#### Diary 4 (Step 5) — 145 words · 726 characters

**Themes:**
- Continued end-of-term time pressure; no main shop, mostly leftovers and frozen batches.
- **Frozen curry:** Ate two previously frozen curry boxes from prior week.
- **Work:** One shift; dinner at work plus two packed meals home.
- **Chicken/noodles:** One meal from remaining chicken and noodles.
- **Convenience:** Pre-done pasta package; quiche (two meals, one taken to campus in plastic box).
- **Pizza and pasta bake:** Pizza plus pasta bake (~2–3 portions).
- **Campus pattern:** Full days on campus without time to shop; eating whatever is fastest.

**Behavioral lenses:** Convenience tradeoff, Occasion (campus-heavy week), Reuse tendency (campus lunch box), Food waste sensitivity (using frozen batches).

---

#### Follow-up interview 2 (Step 7) · Eliza — 5,115 words · 25,584 characters

**Themes:**
- **Term rhythm:** Start-of-term = creative meal planning; end-of-term = bulk freeze-and-reheat (curry, lasagne in microwave boxes).
- **Diary callbacks:** Fajita kit (cardboard recycled, inner tortilla/sauce films not); chicken tray washing; pepper/tomato scrunchy plastic (sometimes recycled if remembered).
- **Recycling uncertainty:** Relies on green arrow symbol; thin films and ambiguous plastics often to general waste; flatmates recycle bottles and pizza boxes, not small films.
- **Storage:** Clingfilm over bowls when Tupperware forgotten; covers fridge items for flatmate preference.
- **Snacks:** Biscuits, crackers, oranges brought to campus; not literal "snacks" but quick portable foods.

**Questions asked:** See [Follow-up 2 (Step 7)](#follow-up-2-step-7-eliza) below.

**Behavioral lenses:** Convenience tradeoff (batch freeze vs cook daily), Recycling diligence (selective by plastic type/thickness), Occasion (campus study days), Pricing/value (won't buy £2 containers some weeks), Attitude-behavior gap (recycles chicken tray, skips fajita films).

---

#### Interview 2 (held out) · Eliza — 12,659 words · 63,147 characters

**Themes:**
- **COVID arrival:** Parents blocked by border closure; isolation kit with basic pasta; flatmate taught laundry; first real washing machine use in current house.
- **Early diet:** Packet pasta/noodles and frozen breaded chicken; deliberate shift away from pasta-only routine.
- **Organisation:** Now plans around budget, freezer space, and term phase; Smol laundry capsule trial via Instagram student promo.
- **Flatmate learning:** Freezer bags, batch curry/lasagne freezing, clingfilm fridge covers all picked up from housemates.
- **Mum recipes:** Leftover pasta + sauces + frozen chicken as "use everything" meals when too busy to shop.
- **Parties:** House parties and clubbing; plastic cups to single bin bag, not separated for recycling.
- **Diary callbacks (week 3–4):** Campus days without eating; quiche packed for campus; biscuits in bag; work shift Tuesday routine.
- **Environment views:** Knows plastic harms environment but lacks scientific detail; change seen via paper substitutions in shops.

**Questions asked:** See [Interview 2 (held out)](#interview-2-held-out-eliza) below.

**Behavioral lenses:** Identity (maturation abroad), Culture/social (habits from flatmates), Pricing/value (Smol trial, container cost), Reuse tendency (freezer bags, cardboard takeaway boxes), Attitude-behavior gap (party cups to general waste), Food waste sensitivity (mum leftover logic).

---

### Interview questions

#### Interview 1 (Step 0) · Eliza

**Household / home / neighbourhood**
- Tell me about yourself, your studies, and your move to the UK.
- Where were you living before, and did you come with anyone?
- How was moving alone, including around food and house tasks?
- What was the cultural shock like, and can you give examples?
- What was it like shifting from living with family to living independently?
- Describe your rented house, flatmates, and how food habits differ in the house.

**Food / preparation / shopping / routines**
- What did you cook early on, and how did your mum help by phone?
- How do you handle chicken defrosting, storage, and dividing into freezer bags?
- Can you give an example of using leftovers or a "mum recipe"?
- What was your role at home growing up compared to siblings?
- Tell me about your campus job: hours, tasks, and meals there.
- How often do you travel home, and how does that affect food planning and freezing?
- What foods do you freeze, and what do you not freeze (e.g. fresh vegetables)?
- How have your cooking skills and recipes changed since you arrived?
- Walk me through making lasagne and storing multi-meal portions.
- Describe your kitchen cupboards, fridge/freezer, and communal equipment.
- Do you cook for yourself or for others in the house?

**Disposal / recycling / packaging**
- What bin and recycling setup do you have, and how did you learn to use it?
- How did recycling work at home in Portugal compared with the UK?
- How do you decide whether plastic packaging is recyclable?
- When during cooking/cleaning do you recycle items?
- What comes to mind when you think about plastic food packaging?
- How do environmental concerns compare with budget when you shop?
- How does paper packaging compare with plastic in your experience?
- What happens to packaging from takeaways and ready meals?
- Why do you rinse some containers (e.g. raw chicken trays) but not others?
- What do you think happens to recycling after kerbside collection?
- How do you categorise glass vs plastic vs cardboard when disposing?

**Broader context**
- Describe your weekly routine, especially campus days and mealtimes.
- Walk through a recent day (e.g. yesterday): breakfast, lunch, dinner, snacks.
- Tell me about your last main food shop: planning, items bought, transport home.
- Why do you avoid buying single-use plastic carrier bags?
- How do you store fruit, veg, sauces, and opened items after shopping?
- How does your diet differ midweek vs weekends?
- Has your relationship with food changed over the past year?

---

#### Interview 2 (held out) · Eliza

**Life history / identity**
- Going back to your first interview: what changed since your solo COVID arrival?
- What was in the isolation kit, and what did you eat in the first weeks?
- How does your organisation around food, budget, and laundry compare with home?

**Food / preparation / routines**
- What ready-made pasta/frozen meals did you rely on at first, and what packaging did they come in?
- How did flatmates influence freezer bags, batch cooking, and fridge covering habits?
- What did you mean by "mum recipes," and can you give recent examples?
- How does meal planning differ at the start vs end of term?
- Describe batch curry/lasagne freezing in microwave boxes. *(diary callback)*
- What is your campus/work routine on busy days, and how does that affect eating?

**Disposal / recycling / packaging**
- What happens to plastic cups and other waste after house parties or club nights?
- Why are party cups not recycled while some kitchen plastics are?
- What are your views on plastic's environmental impact, and how much detail do you feel you have?
- How do you compare paper and plastic packaging environmentally?

**Diary callbacks (weeks 3–4)**
- Tell me about the week you ate almost nothing on campus except biscuits. *(diary callback)*
- Why did you pack quiche in a plastic box for campus? *(diary callback)*
- Describe your Tuesday work shift routine and meals that day. *(diary callback)*
- What snacks/crackers/oranges do you bring to campus and why?

**Broader context**
- Tell me about the Smol laundry capsule trial and why you joined.
- Do you have hobbies (ballet society, reading, travel) and how do they fit your routine?
- Easter plans and family food traditions when you travel home.

---

#### Follow-up 1 (Step 3) · Eliza

**Study participation / routines**
- Has taking part in the study changed how you notice packaging?
- How are you finding the diary method (photos vs writing)?

**Diary callbacks — travel and home**
- Describe food on your journey to vs from home country. *(diary callback)*
- Why buy an airport meal deal outbound but take a homemade sandwich inbound? *(diary callback)*
- Why is breakfast different at home vs in your university town?

**Diary callbacks — chicken and recycling**
- How do you separate and freeze chicken portions? *(diary callback)*
- What happens to the chicken tray, thin cover, and other packaging? *(diary callback)*
- Why wash raw chicken packaging before recycling?

**Diary callbacks — home vs UK food storage**
- Why do your parents unpack vegetables but you keep them in packaging in the UK? *(diary callback)*
- How is loose produce packaged and weighed in Portugal vs UK supermarkets? *(photo callback)*

**Diary callbacks — photos**
- Tell me about the salmon packaging and defrosting method. *(photo callback)*
- How do you dispose of milk cartons and collect screw caps for charity? *(photo callback)*

---

#### Follow-up 2 (Step 7) · Eliza

**Study participation / term rhythm**
- How has diary-keeping affected attention to what you eat?
- How do meals differ between beginning and end of term?

**Diary callbacks — batch cooking**
- Compare start-of-term lasagne planning with end-of-term curry freezing. *(diary callback)*
- Why buy microwave boxes now when you didn't earlier in the year? *(diary callback)*

**Diary callbacks — fajitas and chicken**
- Walk through the 1 kg chicken, fajitas, and noodle leftover chain. *(diary callback)*
- How did you store partial chicken between meals (clingfilm, bowls)? *(diary callback)*
- What happened to fajita kit packaging (cardboard vs thin plastics)? *(diary callback)*

**Disposal / recycling**
- Which plastics do you recycle vs bin, and why (thickness, symbols, convenience)?
- What does the green recycling arrow symbol mean to you?
- Do flatmates recycle differently from you?

**Diary callbacks — snacks and campus**
- What did you mean by "snacks" in the diary (biscuits, crackers, oranges)? *(diary callback)*

---

### Behavioral lens summary across steps

| Step | Primary lenses |
|------|----------------|
| Interview 1 | Identity, Culture/social, Pricing/value, Recycling diligence, Attitude-behavior gap |
| Diary 1 | Occasion, Culture/social, Identity |
| Diary 2 | Food waste sensitivity, Convenience tradeoff, Reuse tendency, Pricing/value |
| Follow-up 1 | Culture/social, Recycling diligence, Pricing/value, Occasion |
| Diary 3 | Occasion, Convenience tradeoff, Food waste sensitivity |
| Diary 4 | Convenience tradeoff, Occasion, Reuse tendency |
| Follow-up 2 | Convenience tradeoff, Recycling diligence, Attitude-behavior gap, Pricing/value |
| Interview 2 | Identity, Culture/social, Reuse tendency, Attitude-behavior gap, Convenience tradeoff |

---

---

### Isabella (Phase 1)

**Profile:** Spanish island student from mountain town Santa; third year (plans masters). Lives with five housemates including boyfriend Pablo (primary cook). Vegetarian since teens (environment, animal welfare; occasional chicken for gym protein). Works Morecambe Bay Curriculum pupil debates on plastics. Shops weekly at Aldi (5-minute walk) with wheeled bag and thick reusable carriers.

### Data order and volume

| Step | Calibration step | File | Date | Words | Characters |
|------|------------------|------|------|-------|------------|
| 0 | Interview 1 | `20220222_First_Interview_Isabella.docx` | 22/02/22 | 13,503 | 68,659 |
| 1 | Diary 1 | `20220228_Isabella_diary_entries_1.docx` | 28/02/22 | 215 | 1,211 |
| 2 | Diary 2 | `20220307_Isabella_diary_entries_2.docx` | 07/03/22 | 500 | 2,674 |
| 3 | Follow-up interview 1 | `20220307_Follow_up_1_Isabella.docx` | 07/03/22 | 3,511 | 19,260 |
| 4 | Diary 3 | `20220314_Isabella_diary_entries_3.docx` | 14/03/22 | 696 | 3,788 |
| 5 | Diary 4 | `20220321_Isabella_diary_entries_4.docx` | 21/03/22 | 570 | 3,051 |
| 7 | Follow-up interview 2 | `20220321_Follow_up_2_Isabella.docx` | 21/03/22 | 3,820 | 20,625 |
| — | Interview 2 (held out) | `20220328_Final_interview_Isabella.docx` | 28/03/22 | 13,760 | 70,602 |

**Participant totals:** 36,575 words · 189,870 characters · 8 files

---

### Step summaries

#### Interview 1 (Step 0) · Isabella — 13,503 words · 68,659 characters

**Themes:**
- **Household/home:** Mountain-town upbringing; family meat business; vegetarian since mid-teens despite parental opposition; complicated eating arrangements at home (grandmother, friends).
- **Routines:** Reading, films, walking; six-person house with three fridges; shared kitchen after COVID packing mix-up.
- **Shopping:** Year 1 university meal plan (parents insisted); year 2+ weekly Aldi trips with Pablo; list-based recipe planning.
- **Food/preparation:** Pablo leads cooking; batch lentil soup; breakfast wraps; occasional chicken for gym; split veg/meat versions of same meals.
- **Plastic packaging:** Strong frustration that Spain-recyclable plastics go to general waste in UK house.
- **Disposal/recycling:** Orange council bin bags only; recycling attempts failed years 1–2 (bins not collected); recycles on campus/streets but not at home.
- **Reuse:** Tupperware, clingfilm, original produce containers; accumulated thick Aldi reusable bags.

**Behavioral lenses:** Identity (vegetarian values), Culture/social (Spain vs UK recycling), Pricing/value (Aldi, frozen veg), Food waste sensitivity, Attitude-behavior gap (knows recycling, can't practice at home), Occasion (cinema, McDonald's).

---

#### Diary 1 (Step 1) — 215 words · 1,211 characters

**Themes:**
- **Tuesday:** Breakfast wraps; leftover black beans stored in original can with clingfilm.
- **Wednesday:** Pasta leftovers in Tupperware; half lemon wrapped in clingfilm.
- **Thursday:** Potato leftovers in Tupperware; ate prior pasta; quick Aldi shop (eggs, toast, frozen broccoli, nuggets, coconut milk, gum, milk); dinner = leftover potatoes + bean quesadillas.
- **Friday:** McDonald's nuggets in paper box; sauce sachets in plastic.
- **Saturday cinema:** Tap water in plastic cups; popcorn; no recycling bin (general waste only) for cups or paper holder.

**Behavioral lenses:** Reuse tendency (Tupperware, bean/can cycle), Recycling diligence (cinema frustration), Occasion (cinema, McDonald's), Culture/social (would recycle in Spain).

---

#### Diary 2 (Step 2) — 500 words · 2,674 characters

**Themes:**
- **Monday:** Weekly Aldi shop (photo); pasta sauce meal prep covered with clingfilm; half onion wrapped for later use; spinach photo example of keeping original plastic containers for produce.
- **Wednesday:** Post-gym Aldi top-up; refused plastic bag, carried goods in tote, pockets, and hands; lunch = leftover pasta sauce; pineapple cut into Tupperware.
- **Disposal:** Chocolate brioche and almond packaging to general waste (would recycle in Spain).
- **Thursday:** Vegan/real meatball split with rice in oversized Tupperware; spare almond sauce frozen.
- **Friday:** Pasta leftovers; party with ubiquitous plastic cups.
- **Saturday–Sunday:** Banana-oat pancakes to use browning bananas; rice cake packaging to general waste (Spain-recyclable).

**Behavioral lenses:** Culture/social (Spain vs UK bins), Pricing/value (no plastic bag purchase), Food waste sensitivity (banana pancakes), Reuse tendency (containers, frozen sauce), Occasion (party, gym trip).

---

#### Follow-up interview 1 (Step 3) · Isabella — 3,511 words · 19,260 characters

**Themes (researcher notes + participant quotes):**
- **Party norms:** Pre-drinks before nightclub; plastic cups default, never ask for glass.
- **Breakfast wraps:** Eggs, beans, pepper, spinach, guacamole; weekly or fortnightly; leftover beans become quesadillas later.
- **Green goddess sauce:** Blender recipe from vegan YouTuber; Pablo adapts; batch stored for multiple pasta meals.
- **Cooking roles:** Pablo confident main cook; Isabella "sous chef," checks recipes due to poor memory.
- **Leftovers:** Lentil soup batches last 3–4 days; clingfilm preferred when Tupperware scarce (housemates' meal prep).
- **McDonald's:** Boyfriend started job there; paper nuggets box to general waste (greasy); sauce partly kept in fridge.
- **Cinema:** Tap water in plastic cup; believes Spanish cinemas sometimes recycle drinks packaging.
- **Frozen vs fresh:** Frozen broccoli/sweetcorn for specific recipes; fresh lemons non-negotiable; frozen bread to prevent waste.
- **Fridge storage:** Apples/carrots/tomatoes left in original plastic bags in fridge (no spare Tupperware).

**Questions asked:** See [Follow-up 1 (Step 3)](#follow-up-1-step-3-1) below.

**Behavioral lenses:** Occasion (party, cinema, McDonald's), Identity (healthy eating mindset), Reuse tendency (leftover beans), Culture/social (Spain recycling expectations), Convenience tradeoff (frozen veg/bread).

---

#### Diary 3 (Step 4) — 696 words · 3,788 characters

**Themes:**
- **Monday:** Lentil soup leftover in Tupperware.
- **Tuesday:** Bagel lunch; gym visit noting single-use plastic hydration bottles among gym-goers.
- **Wednesday (work):** Children's lunch all in plastic; MBC debate on banning plastics (reuse/recycle vs ocean harm); girl notes peers bin bottles beside recycle bin.
- **Thursday:** Greggs vegan sausage roll (paper wrapper recycled in library bin); quiche stored in glass dish with clingfilm (no Tupperware free).
- **Friday–Sunday:** Chopped tomatoes in original can + clingfilm; multiple Spain-recyclable plastics (apples, Ben & Jerry's paper, baby plum tomatoes, lettuce) to general waste; salad Tupperware wrapped in clingfilm for library day (lost reusable bag from prior term).

**Behavioral lenses:** Culture/social (school debate, Spain norms), Occasion (work, gym, library), Recycling diligence (Greggs paper at campus), Attitude-behavior gap (teaches plastic debate, house cannot recycle).

---

#### Diary 4 (Step 5) — 570 words · 3,051 characters

**Themes:**
- **Monday:** McDonald's nuggets (paper pack, extra sauce sachet wasted); lesson learned on sauce quantity.
- **Tuesday shop:** Frozen pizza with box + inner plastic wrap.
- **Wednesday:** Rice packaging to general waste (Spain-recyclable).
- **Thursday campus day:** Pasta and grapes in Tupperware; clingfilm wrap; bought Sainsbury's plastic bag to reuse instead of daily clingfilm.
- **Friday–Saturday:** M&M wrapper binned at campus (no recycling option); sunset outing litter-pick (plastic bottles left by others).
- **Sunday:** Finished Greek yogurt tub to general waste (Spain-recyclable); reused shopping bag to cover Tupperware for campus.

**Behavioral lenses:** Reuse tendency (Sainsbury's bag solution), Culture/social (Spain recycling expectations), Occasion (campus study days, castle outing), Pricing/value (small investment to reduce film waste), Food waste sensitivity (sauce portion learning).

---

#### Follow-up interview 2 (Step 7) · Isabella — 3,820 words · 20,625 characters

**Themes (researcher notes + participant quotes):**
- **MBC debates:** Primary-school plastic ban debates; "plastic should not be banned" side often wins; Isabella prompts deeper thinking (reusable bottles vs single-use).
- **Aldi routine:** Wheeled shopping caddy + thick reusable Aldi bags accumulated across six housemates; walk home, share carrying.
- **Shared kitchen:** Under-sink cupboard for carrier bags/cleaning products; communal Tupperware shelf; pans/devices shared after COVID repacking errors.
- **Photo-elicitation:** Weekly shop packaging mostly plastic; would recycle all in Spain except uncertain items (cocoa tin, lemon netting, greasy meatball tray).
- **Dirty packaging trauma:** Conference taught "dirty plastic ruins recycling"; won't touch boyfriend's meat packaging; butter tub grease uncertainty.
- **Margarine discovery:** Realised she had bought margarine for three years, not butter; switched to real butter in new packaging.
- **Post-gym shop:** Carried groceries without buying plastic bag (commonsense, not discussed); interior coat pockets looked like shoplifting.

**Questions asked:** See [Follow-up 2 (Step 7)](#follow-up-2-step-7-1) below.

**Behavioral lenses:** Culture/social (educating children on plastics), Identity (vegetarian, won't handle meat packs), Recycling diligence (would recycle in Spain), Reuse tendency (accumulated carriers), Attitude-behavior gap (environment job vs home general waste).

---

#### Interview 2 (held out) · Isabella — 13,760 words · 70,602 characters

**Themes:**
- **Gym and diet:** Protein-focused eating; occasional chicken; frozen vegetables to reduce fresh spoilage.
- **Upbringing:** Santa mountain town; less control over food when visiting home on vacation.
- **University food journey:** Year 1 marketplace plan vs year 2+ shared cooking with Pablo.
- **End-of-term:** Deadline eating; campus days with Tupperware transport; clingfilm vs reusable bag workaround.
- **Recycling history:** Failed kerbside recycling both years; orange bags only; emotional "failure" vs Spain community norm.
- **Diary callbacks:** Gym plastic cups; McDonald's sauces; cinema waste; children's debate; Greggs paper; frozen pizza double wrap; litter picking.

**Questions asked:** See [Interview 2 (held out)](#interview-2-held-out-1) below.

**Behavioral lenses:** Identity (health/fitness, vegetarian), Food waste sensitivity, Culture/social (UK recycling failure), Occasion (gym, campus, parties), Convenience tradeoff (frozen pizza, meal prep), Attitude-behavior gap.

---

### Interview questions

#### Interview 1 (Step 0) · Isabella

**Household / home / neighbourhood**
- Tell me about yourself, your background, and where you grew up.
- What do you do outside studies, and what is your current living situation?
- What is it like living with five housemates, including your boyfriend?
- Where did you meet your partner, and how did you both end up at the same university?
- How was leaving home to study in the UK?

**Food / preparation / shopping / routines**
- Did you cook at home before university, given your vegetarianism?
- Why did you become vegetarian, and how did your family react (meat business background)?
- What did you eat in year 1 (meal plan) vs later years?
- Describe your kitchen, appliances, and how fridge/cupboard space is shared.
- Who decides what you and Pablo buy and cook each week?
- What meals do you eat now (breakfast wraps, soups, chicken occasionally)?
- Tell me about your last weekly Aldi shop: route, companions, and list planning.

**Disposal / recycling / packaging**
- Describe your bin setup (orange bags, collection day, where bags wait).
- Have you tried recycling at this house or last year, and what went wrong?
- How does recycling at home in Spain compare with England?
- What plastics did you recycle at home, and how did you store/separate them?
- What packaging do fruits and vegetables come in, and how does it feel/textures?
- Do you recycle when out (campus, street bins) even if not at home?

**Broader context**
- How do environmental and health reasons shape your food choices?
- What happens when packaging is "dirty" (meat, grease) in your view?

---

#### Interview 2 (held out) · Isabella

**Life history / identity**
- How does gym/fitness shape what you eat now compared with year 1?
- Tell me about growing up in Santa and food at home on visits.

**Food / preparation / routines**
- How did marketplace catering compare with cooking in the shared house?
- Why use frozen vegetables and bread, and when prefer fresh?
- Describe end-of-term eating when deadlines and campus days collide.

**Disposal / recycling**
- Retrace failed recycling attempts in years 1 and 2 (landlord, council, neighbours).
- How do orange council bags work, and how does that feel vs Spain?
- Why does household recycling feel like a "failure" when you care about the environment?

**Diary callbacks (weeks 1–4)**
- Tell me about plastic cups at the party and cinema. *(diary callback)*
- What happened to McDonald's and Greggs packaging? *(diary callback)*
- Describe the schoolchildren's plastic debate and bin behavior. *(diary callback)*
- Why buy a Sainsbury's bag instead of daily clingfilm for campus food? *(diary callback)*
- What packaging from your Aldi shop would you recycle in Spain but not here? *(diary callback)*

**Broader context**
- How does your MBC work on plastics relate to your own household waste?
- Margarine vs butter discovery: what changed in your shopping?

---

#### Follow-up 1 (Step 3) · Isabella

**Diary callbacks — social occasions**
- Why are plastic cups the default at house parties? *(diary callback)*
- Why couldn't you recycle cinema cups or popcorn packaging? *(diary callback)*

**Diary callbacks — meals and leftovers**
- Walk through breakfast wraps and the leftover bean → quesadilla cycle. *(diary callback)*
- Tell me about green goddess sauce: recipe source, ingredients, batch storage. *(diary callback)*
- Who leads cooking in the house, and how do you store leftovers (clingfilm vs Tupperware)? *(diary callback)*

**Diary callbacks — packaging choices**
- Why McDonald's that week, and what happened to the packaging? *(diary callback)*
- Why buy frozen broccoli/sweetcorn vs fresh, and frozen bread? *(photo callback)*
- Why keep apples/tomatoes in original plastic bags in the fridge? *(photo callback)*

**Disposal / recycling**
- Which items in your fridge/shopping photos would you recycle in Spain? *(photo callback)*
- What packaging types leave you unsure (cocoa tin, lemon netting)? *(photo callback)*

---

#### Follow-up 2 (Step 7) · Isabella

**Work / citizenship**
- Describe your role in MBC plastic debates with schoolchildren.
- What arguments do children use for and against banning plastics?

**Diary callbacks — shopping and kitchen**
- How do you shop at Aldi (wheeled bag, reusable carriers, walking home)? *(diary callback)*
- Walk through shared kitchen storage after COVID packing confusion. *(diary callback)*
- Photo-elicit weekly shop: what is recyclable from your perspective? *(photo callback)*

**Disposal / recycling**
- Which packaging would you refuse to recycle because it is too dirty (meatballs, butter)? *(diary callback)*
- How did the recycling conference affect your behavior? *(diary callback)*
- Real butter vs margarine: what did you learn about what you were buying?

**Diary callbacks — transport food**
- Why avoid buying a plastic bag after gym shopping, carrying in pockets instead? *(diary callback)*

---

### Behavioral lens summary across steps

| Step | Primary lenses |
|------|----------------|
| Interview 1 | Identity, Culture/social, Attitude-behavior gap, Pricing/value, Food waste sensitivity |
| Diary 1 | Reuse tendency, Recycling diligence, Occasion, Culture/social |
| Diary 2 | Culture/social, Food waste sensitivity, Reuse tendency, Pricing/value, Occasion |
| Follow-up 1 | Occasion, Identity, Reuse tendency, Culture/social, Convenience tradeoff |
| Diary 3 | Culture/social, Attitude-behavior gap, Occasion, Recycling diligence |
| Diary 4 | Reuse tendency, Culture/social, Occasion, Pricing/value, Food waste sensitivity |
| Follow-up 2 | Culture/social, Identity, Recycling diligence, Reuse tendency, Attitude-behavior gap |
| Interview 2 | Identity, Culture/social, Food waste sensitivity, Occasion, Convenience tradeoff |

---

---

### Ella (Phase 1)

**Profile:** Third-year environmental science student; part-time supermarket checkout worker (four years, home store and university branch). Coastal hometown; pescetarian since New Year resolution; shared student house with rotating group meals. Main household shopper via staff discount online orders.

### Data order and volume

| Step | Calibration step | File | Date | Words | Characters |
|------|------------------|------|------|-------|------------|
| 0 | Interview 1 | `20220301_First_Interview_Ella.docx` | 01/03/22 | 11,205 | 56,707 |
| 1 | Diary 1 | `20220309_Ella_diary_entries_1.docx` | 09/03/22 | 1,291 | 6,873 |
| 2 | Diary 2 | `20220316_Ella_diary_entries_2.docx` | 16/03/22 | 928 | 4,994 |
| 3 | Follow-up interview 1 | `20220316_Follow_up_1_Ella.docx` | 16/03/22 | 2,382 | 13,177 |
| 4 | Diary 3 | `20220323_Ella_diary_entries_3.docx` | 23/03/22 | 1,255 | 6,756 |
| 5 | Diary 4 | `20220331_Ella_diary_entries_4.docx` | 31/03/22 | 995 | 5,360 |
| 7 | Follow-up interview 2 | `20220322_Follow_up_2_Ella.docx` | 22/03/22 | 5,646 | 28,193 |
| — | Interview 2 (held out) | `20220401_Final_interview_Ella.docx` | 01/04/22 | 12,923 | 65,936 |

**Participant totals:** 36,625 words · 187,996 characters · 8 files

---

### Step summaries

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

**Questions asked:** See [Follow-up 1 (Step 3)](#follow-up-1-step-3-ella) below.

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

**Questions asked:** See [Follow-up 2 (Step 7)](#follow-up-2-step-7-ella) below.

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

**Questions asked:** See [Interview 2 (held out)](#interview-2-held-out-ella) below.

**Behavioral lenses:** Identity (environment student + checkout insider), Culture/social (beach clean community), Pricing/value (bag charge behaviour change), Convenience tradeoff (early jar-sauce diet), Recycling diligence (infrastructure frustration), Attitude-behavior gap (sees consumer shift, still uses convenience foods), Occasion (smoothies, soups, beach litter).

---

### Interview questions

#### Interview 1 (Step 0) · Ella

**Household / home / neighbourhood**
- Tell me about yourself, your degree, and why you joined the study.
- What role does plastic play in your environmental science course?
- Describe growing up on the coast and how that shaped your views on ocean pollution.
- What is home like, and how does it compare to where you live at university?
- Who do you live with, and how long have you shared a house?
- How did your family think about plastic before you started "nattering in their ear"?

**Food / preparation / shopping / routines**
- How did food and shopping work at home with your dad's bakery hours and your mum/sister cooking?
- What was the transition to university like for budgeting, cooking, and meals?
- Why did you become pescetarian, and how does shared cooking work in the house?
- Who is responsible for the household shop, and how does your staff discount shape orders?
- What meals have you cooked recently for the group, including successes and disasters?
- How often do takeaways happen, and what drives that choice?
- Where do you find recipes (e.g. Mob Kitchen), and what constraints matter (cost, time, washing up)?
- Why do you buy microwave rice packets despite knowing the plastic cost?
- How has your cooking changed from first year (frozen chicken, jar sauces) to now?

**Disposal / recycling / packaging**
- What comes to mind when you think about plastic food packaging and the environment?
- How did your parents' council recycling change, and what bins do they use now?
- What do you see on checkout about customers' packaging and bag choices over four years?
- How do reusable bags, loose produce, and the bag charge influence behaviour?
- What packaging from tea, yogurt, fruit, and ready meals do you notice most?

**Broader context**
- Tell me about your part-time supermarket job: hours, locations, and what you observe on the belt.
- How do course modules (water footprint, cattle methane, farm carbon project) affect your food choices?
- How did peer vegetarian/vegan norms on your course make you feel before changing diet?
- Describe guilt, nutrition, and cost tradeoffs around fish vs full vegetarianism.

---

#### Interview 2 (held out) · Ella

**Checkout / retail perspective**
- How have customer bag-buying habits changed as prices rose from 5p to 20p?
- What feedback have you heard about paper veg bags vs older plastic ones?
- How does scan-rate monitoring feel, and how do colleagues talk about it?
- Are there employee-side issues when customers buy loose produce or use own containers?
- How are delivery orders packed to separate cleaning products from food?

**Food / preparation / routines**
- Looking back at first year: what did you eat repeatedly, and what packaging came with it?
- Tell me about your smoothie phase: ingredients, frozen vs fresh, and blender access.
- How did you start batching soups in winter, and how do you freeze them?
- What Tupperware or containers do you use, and where do they come from?
- How does living with a chest freezer change what you store (bread, batch meals)?

**Environment / activism**
- How did you get involved in beach cleans and litter picking?
- What was it like finding litter on the beach during a clean?
- What do you know about microplastics in humans after reading recent coverage?
- Do you think change starts with consumers, retailers, or government?

**Disposal / recycling / packaging**
- What recycling facilities are missing locally (e.g. along beaches)?
- What happens when public bins overflow?
- How do you think about plastic toxicity beyond packaging waste?

**Diary callbacks**
- Reflect on diary weeks: unnecessary rice/noodle packaging audit. *(diary callback)*
- BBQ shop: which items had plastic vs not, and what was recycled? *(diary callback)*
- Freezer chips dinner during deadline week. *(diary callback)*

---

#### Follow-up 1 (Step 3) · Ella

**Study participation**
- Has taking part made you think more about plastic in daily life?
- How is the diary method working for you (photos vs writing)?

**Diary callbacks — deadline week**
- Walk through the broken-laptop week and campus computer days. *(diary callback)*
- What did you eat on Monday when you had no time to cook? *(diary callback)*
- What packaging came with the frozen chips/veg meal? *(diary callback)*

**Diary callbacks — shop and group meals**
- Why buy a 3-pack of onions on sale instead of loose? *(diary callback)*
- Why flatbreads for chickpea curry instead of rice packets? *(diary callback)*
- Talk through the full-day packaging audit (breakfast, lunch, Thai curry dinner). *(diary callback)*

---

#### Follow-up 2 (Step 7) · Ella

**Household / freezer**
- How many housemates now, and what changed about freezer space?
- Compare previous two fridge-freezers (seven people) with current chest freezer setup.
- What else do you freeze besides bread (backup meals, batch cooking)?

**Diary callbacks — breakfast packaging**
- Talk through the breakfast photo: strawberries, yogurt, cereal/porridge fractions. *(diary callback)*
- How do you decide whether the yogurt pot is recyclable? *(diary callback)*
- What do you do with cereal inner film vs cardboard box? *(diary callback)*

**Health and diet**
- You mentioned a bad cold and buying more fruit; did that change eating habits?
- Any other diet tweaks after feeling unwell?

**Disposal / recycling**
- Which soft plastics do you bin because kerbside won't take them?
- When packaging is part cardboard, part plastic, which bin wins?

---

### Behavioral lens summary across steps

| Step | Primary lenses |
|------|----------------|
| Interview 1 | Identity, Culture/social, Pricing/value, Convenience tradeoff, Attitude-behavior gap |
| Diary 1 | Pricing/value, Convenience tradeoff, Identity, Attitude-behavior gap |
| Diary 2 | Occasion, Convenience tradeoff, Recycling diligence, Identity |
| Follow-up 1 | Occasion, Convenience tradeoff, Identity, Attitude-behavior gap |
| Diary 3 | Recycling diligence, Pricing/value, Attitude-behavior gap, Identity |
| Diary 4 | Occasion, Recycling diligence, Convenience tradeoff, Attitude-behavior gap |
| Follow-up 2 | Reuse tendency, Convenience tradeoff, Recycling diligence, Occasion |
| Interview 2 | Identity, Culture/social, Pricing/value, Recycling diligence, Attitude-behavior gap |

---

---

### Jacob (Phase 1)

**Profile:** International postgraduate student, seven months in UK; from large family (10 siblings), now lives alone in shared student flat (five rooms, one kitchen). Shops Lidl, Nigerian supermarket, Eat India takeaway; batch-cooks stews stored in reused takeaway bowls.

### Data order and volume

| Step | Calibration step | File | Date | Words | Characters |
|------|------------------|------|------|-------|------------|
| 0 | Interview 1 | `20220503_First_interview_Jacob.docx` | 03/05/22 | 13,184 | 64,239 |
| 1 | Diary 1 | `20220509_Jacob_diary_entries_1.docx` | 09/05/22 | 346 | 1,875 |
| 2 | Diary 2 | `20220516_Jacob_diary_entries_2.docx` | 16/05/22 | 187 | 1,063 |
| 3 | Follow-up interview 1 | `20220512_Follow_up_1_Jacob.docx` | 12/05/22 | 624 | 3,570 |
| 4 | Diary 3 | `20220523_Jacob_diary_entries_3.docx` | 23/05/22 | 434 | 2,355 |
| 5 | Diary 4 | `20220530_Jacob_diary_entries_4.docx` | 30/05/22 | 319 | 1,754 |
| 7 | Follow-up interview 2 | `20220519_Follow_up_2_Jacob.docx` | 19/05/22 | 677 | 3,932 |
| — | Interview 2 (held out) | `20220601_Final_interview_Jacob.docx` | 01/06/22 | 11,392 | 58,384 |

**Participant totals:** 27,163 words · 137,172 characters · 8 files

**Note:** Diary batches are short (routine-day logs); most volume is in interviews.

---

### Step summaries

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

**Questions asked:** See [Follow-up 1 (Step 3)](#follow-up-1-step-3-jacob) below.

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

**Questions asked:** See [Follow-up 2 (Step 7)](#follow-up-2-step-7-jacob) below.

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

**Questions asked:** See [Interview 2 (held out)](#interview-2-held-out-jacob) below.

**Behavioral lenses:** Culture/social (home vs UK systems, church community), Recycling diligence (bin choice on campus/library), Identity (international student comparing infrastructure), Pricing/value (litter cost report), Attitude-behavior gap (knows hierarchy, still uses general bin for some paper), Convenience tradeoff (campus-bought lunch).

---

### Interview questions

#### Interview 1 (Step 0) · Jacob

**Household / home / neighbourhood**
- Tell me about yourself and your background.
- You live alone in the UK as well?
- Tell me about your large family and upbringing around food and cooking.
- Were you involved in cooking at home before you moved?
- How do you bring food home from the shops (bags, transport)?

**Food / preparation / shopping / routines**
- What foods did you buy from the Indian supermarket/restaurant when you first arrived?
- Tell me about Eat India: what kind of place it is, and whether you eat in or takeaway.
- How often do you go to Eat India when you do not want to cook?
- What packaging are those meals served in?
- What ingredients do you now buy from the Nigerian supermarket?
- What meals did you want to make when you first came to the UK?
- How available is your preferred home-country food here?
- How did cooking responsibilities shift when you left the family home?
- How does food shopping in the UK differ from buying food at home (choice vs sustenance)?
- How often do you go to the supermarket in the UK?
- Walk me through your last supermarket trip: list, substitutions, and what you bought.
- Do you buy items not on your list, and why?

**Disposal / recycling / packaging**
- What are the takeaway containers made of?
- What happens to packaging after you have used it?
- You said you need to dispose of containers but also retain them. What do you mean?

**Broader context**
- What was it like in your first few months before you found the Nigerian supermarket?
- What was your first experience shopping in a UK supermarket?

---

#### Interview 2 (held out) · Jacob

**Home country vs UK environment**
- Tell me more about environmental impacts of plastic waste in your home country (flooding, erosion, gutters).
- Did you learn about these connections in the UK or before you came?
- How do recycling labels on UK products compare with products at home?
- Why does company messaging about recycling matter for customer behaviour?

**Campus / library meals**
- Do you often buy lunch when you are out on campus?
- Walk through the library/campus meal photo: pepperoni pizza packaging and which bin you used.
- Why did the paper go in the general bin rather than a paper bin?
- Describe the orange juice packaging and which bin you chose.
- Why did the orange packaging go in general waste?

**Waste hierarchy and research**
- Have you come across the waste hierarchy (reduce, reuse, recycle)?
- Tell me about the recent report on litter costs and what you took from it.
- What questions do you ask yourself when deciding how to dispose of packaging?
- How important are recycling labels on bottles when you are shopping?

**Reuse and cleanliness**
- You said you do not normally reuse plastic containers at home. How is the UK different?
- Do thoughts about cleanliness affect how you use the kitchen or dispose of packaging?

**Community**
- What church or community activities do you take part in?
- What does "making sure the environment is safe" mean to you in that context?

**Diary callbacks**
- Bulk stew cooking and bowl storage in the communal fridge. *(diary callback)*
- Takeaway day when cooking felt like a "waste of time." *(diary callback)*
- Pepsi can and chips packaging disposal. *(diary callback)*

---

#### Follow-up 1 (Step 3) · Jacob

**Routines**
- How does gym/exercise fit around your university schedule (at least twice weekly)?

**Diary callbacks — takeaway day**
- Why did you not want to cook that day, and what did you eat instead? *(diary callback)*
- What packaging came with the meal (Pepsi can, chips tray)? *(diary callback)*
- Which kitchen bin did each item go in? *(diary callback)*

**Diary callbacks — shopping and stew**
- Walk through the shopping-trip diary: what was bought for the stew? *(diary callback)*
- How do you prepare food "all at once" after shopping? *(diary callback)*
- Describe the communal fridge photo. *(diary callback)*

**Study participation**
- Has participating changed how you notice packaging or daily routines?

---

#### Follow-up 2 (Step 7) · Jacob

**Study reflexivity**
- What is it like recording what you normally do on a daily basis?
- Has diary-keeping changed how you think about shopping before food runs out?

**Diary callbacks — batch cooking**
- Walk through planning and cooking the stew. *(diary callback)*
- Why transfer most stew into plastic takeaway bowls in the fridge? *(diary callback)*
- What do you call these containers ("plastic bowls"), and when do you discard them? *(diary callback)*

**Disposal / recycling**
- What counts as plastic waste for you, and how do you dispose of it? *(diary callback)*

---

### Behavioral lens summary across steps

| Step | Primary lenses |
|------|----------------|
| Interview 1 | Identity, Culture/social, Convenience tradeoff, Reuse tendency |
| Diary 1 | Occasion, Culture/social, Identity |
| Diary 2 | Occasion, Food waste sensitivity |
| Follow-up 1 | Convenience tradeoff, Culture/social, Recycling diligence, Occasion |
| Diary 3 | Occasion, Convenience tradeoff, Reuse tendency |
| Diary 4 | Occasion, Food waste sensitivity, Reuse tendency |
| Follow-up 2 | Identity, Reuse tendency, Convenience tradeoff, Attitude-behavior gap |
| Interview 2 | Culture/social, Recycling diligence, Attitude-behavior gap, Pricing/value |

---

---

### Cath (Phase 1)

**Profile:** 57, semi-retired former teacher now casual exam invigilator; Green Party member; lives with husband in four-bed semi with garden, wildlife pond, and extensive home growing. Meal planner; shops Waitrose on foot, Aldi/Tesco by car.

### Data order and volume

| Step | Calibration step | File | Date | Words | Characters |
|------|------------------|------|------|-------|------------|
| 0 | Interview 1 | `20220419_Interview_1_Cath.docx` | 19/04/22 | 18,237 | 92,437 |
| 1 | Diary 1 | `20220425_Cath_diary_entries_1.docx` | 25/04/22 | 590 | 3,684 |
| 2 | Diary 2 | `20220502_Cath_diary_entries_2.docx` | 02/05/22 | 747 | 4,600 |
| 3 | Follow-up interview 1 | `20220429_Follow_up_1_Cath.docx` | 29/04/22 | 5,563 | 28,485 |
| 4 | Diary 3 | `20220509_Cath_diary_entries_3.docx` | 09/05/22 | 326 | 2,003 |
| 5 | Diary 4 | `20220516_Cath_diary_entries_4.docx` | 16/05/22 | 772 | 4,603 |
| 7 | Follow-up interview 2 | `20220509_Follow_up_2_Cath.docx` | 09/05/22 | 4,276 | 22,521 |
| — | Interview 2 (held out) | `20220531_Interview_2_Cath.docx` | 31/05/22 | 17,690 | 89,592 |

**Participant totals:** 48,201 words · 247,925 characters · 8 files

---

### Step summaries

#### Interview 1 (Step 0) · Cath — 18,237 words · 92,437 characters

**Themes:**
- **Household/home:** Lives with husband; two grown-up children living elsewhere; four-bed semi with garden used for summer growing (tomatoes, salad, etc.); wildlife pond and wildlife-friendly garden.
- **Routines:** Casual exam invigilation with flexible volunteer schedule; spends significant time gardening; Sunday morning meal planning.
- **Shopping:** Shops Waitrose on foot (~twice weekly); Aldi/Tesco by car for bulk/cheaper items; sister's household nearly self-sufficient in home-grown veg by comparison.
- **Food/preparation:** Eats seasonally; home-grown chillies chopped and frozen for year-round use; cooks from scratch with meal plans; roast chicken example stretched across wraps, lunches, and later pasta.
- **Plastic packaging:** Uses far less plastic packaging in summer when growing; in winter buys more wrapped produce (e.g. bagged salad often wasted and composted).
- **Disposal/recycling:** Heavy recycler; soft plastics collected in pantry bag for supermarket drop-off; compost sacks with recycling symbol (number 4); reuses many trays and pots in garden until they fall apart.
- **Reuse:** Waste plastic reused for garden seedlings; mushroom/dessert trays for seedlings; stopped clingfilm in favour of bread bags; Tupperware for leftovers and freezing; freezer storage discussed in interview.

**Behavioral lenses:** Identity (Green Party member, environmental gardener), Culture/social (family food norms, sister's home-growing contrast), Pricing/value (Waitrose vs Aldi/Tesco split), Convenience tradeoff (meal planning), Recycling diligence (soft-plastic collection, compost-sack schemes), Reuse tendency (garden trays, bread bags, Tupperware), Food waste sensitivity (meal planner, seasonal growing, bagged-salad caution).

---

#### Diary 1 (Step 1) — 590 words · 3,684 characters

**Themes:**
- Full week logged Monday 18th through Sunday 24th April.
- Day-by-day diary covering meals, packaging, and disposal across the first study week.

**Behavioral lenses:** Occasion (weekly rhythm), Identity (committed participant), Recycling diligence, Food waste sensitivity.

---

#### Diary 2 (Step 2) — 747 words · 4,600 characters

**Themes:**
- Second week Monday 25th through Saturday 30th April.
- Continued daily logging; longer batch than Diary 1.

**Behavioral lenses:** Occasion, Convenience tradeoff, Recycling diligence, Reuse tendency, Food waste sensitivity.

---

#### Follow-up interview 1 (Step 3) · Cath — 5,563 words · 28,485 characters

**Themes:**
- **Study reflexivity:** Really enjoying the diary; will miss it when finished; gives daily purpose; has always thought about packaging but now engages more deliberately.
- **Pantry video:** Packets of rice in pantry, including microwaveable pouches; feels guilty every time ("such a lot of packaging"); knows she should cook rice from scratch but is "absolutely terrible" at cooking rice.

**Questions asked:** See [Follow-up 1 (Step 3)](#follow-up-1-step-3-cath) below.

**Behavioral lenses:** Identity (self-aware environmentalist), Convenience tradeoff (rice pouches), Attitude-behavior gap (guilt vs continued use), Culture/social (enjoys study participation).

---

#### Diary 3 (Step 4) — 326 words · 2,003 characters

**Themes:**
- **Bank holiday Monday (2nd May):** Short entry.
- **Falmouth trip (Wednesday 4th–Sunday 8th May):** Travel week away from home routine.

**Behavioral lenses:** Occasion (bank holiday, travel), Convenience tradeoff (away-from-home eating), Identity (diarising while travelling).

---

#### Diary 4 (Step 5) — 772 words · 4,603 characters

**Themes:**
- **Tuesday 10th May and Thursday 12th May:** Post-travel catch-up entries after Falmouth return.

**Behavioral lenses:** Occasion (return to home routine), Recycling diligence, Reuse tendency.

---

#### Follow-up interview 2 (Step 7) · Cath — 4,276 words · 22,521 characters

**Themes:**
- **Leftovers and planning:** Some meals lend themselves to leftovers; plans midweek so husband has packed lunches; meal-planning video shared.
- **Weekly tempo:** Monday = quicker, lower-priority meal ("back to work vibe"); weekends more special; spends more on food toward end of week, bank holidays, and weekends.
- **Quick Monday meal:** Small folded deli wraps (pitta-like) with burger filling.
- **Freezer routine:** Two freezers (pantry fridge-freezer for peas, chips, etc.); each morning thinks about what to pull from freezer for dinner.
- **Shopping friction:** Heroes/Celebrations chocolates bought for husband's sailing event; she would object; competing concerns can spoil otherwise enjoyable shopping trips.
- **Packaging tradeoffs:** Buys larger cheese blocks when cheaper or less packaging; still troubled by "nasty" pouches.

**Questions asked:** See [Follow-up 2 (Step 7)](#follow-up-2-step-7-cath) below.

**Behavioral lenses:** Occasion (Monday vs weekend, sailing gifts), Convenience tradeoff (frozen veg, deli wraps), Pricing/value (bulk cheese), Food waste sensitivity (leftover planning), Attitude-behavior gap (objects to celebration tins), Recycling diligence.

---

#### Interview 2 (held out) · Cath — 17,690 words · 89,592 characters

**Themes:**
- **Gardening philosophy:** Values inherited from parents; "live and let live" rather than spraying/killing garden pests; wants birds and hedgehogs in the garden; moves snails away from lettuces by hand.
- **Activism:** Uses Twitter to message supermarkets (e.g. plastic carrier bags); signs petitions; feels part of a wider community of like-minded people.
- **Material choices:** Prefers glass as better recycled but reads conflicting claims about glass weight/energy; feels confused; yoghurt pots reused in various ways yet still many thrown away.
- **Travel:** When travelling or out and about (e.g. Falmouth), must sometimes accept plastic packaging avoided at home.
- **Growing vs buying:** Satisfaction when home cucumbers and other produce reduce need to shop for wrapped equivalents.

**Questions asked:** See [Interview 2 (held out)](#interview-2-held-out-cath) below.

**Behavioral lenses:** Identity (lifelong environmental values), Culture/social (Twitter, petitions), Attitude-behavior gap (travel packaging, yoghurt-pot volume), Recycling diligence (glass vs plastic confusion), Reuse tendency (yoghurt pots, garden trays), Occasion (Falmouth, out-and-about meals).

---

### Interview questions

#### Interview 1 (Step 0) · Cath

**Household / home / neighbourhood**
- Tell me about yourself, your family, and your home.
- What does your casual invigilation schedule look like over the coming weeks?
- Describe your interest in gardening and how growing connects to food waste.
- Tell me about your wildlife pond and wildlife-friendly garden.

**Food / preparation / shopping / routines**
- How does growing your own food help prevent waste and reduce packaging?
- What are your concerns about bagged salad and bagged tomatoes?
- Walk through a recent shared meal (e.g. roast chicken) and how it was prepared and reused.
- Is the later pasta dish using leftover chicken on your meal plan?
- How do you shop: Waitrose on foot and Aldi/Tesco by car?
- How many freezers do you have, and what do you use them for?
- Who writes the weekly meal plan on Sunday mornings, and how are decisions shared?

**Disposal / recycling / packaging**
- Where do you store packaging reused in the garden (pots, trays, labels)?
- Describe the roast chicken packaging: tray, film, and what happened to each part.
- Why did you stop using clingfilm, and what do you use instead?
- Where do you keep the soft-plastics bag in the pantry before taking it to Tesco?
- Describe the recycling symbol on compost sacks (number 4).
- Do you get compost delivered?

**Broader context**
- Tell me about your Green Party membership and environmental priorities.
- How does plastic packaging use differ between summer (growing) and winter?

---

#### Interview 2 (held out) · Cath

**Gardening and activism**
- How did your parents influence your approach to the garden?
- Why avoid spraying/killing pests, and how do birds and hedgehogs fit in?
- How do you use Twitter to challenge supermarkets on packaging?
- What does "take a step back" mean for you?

**Materials and recycling**
- Why prefer glass, and what confuses you about glass vs plastic recycling?
- How do you reuse yoghurt pots, and what still gets thrown away?
- Did you try separating yoghurt lid materials, and why?

**Travel and away-from-home**
- Describe separated recycling bins seen while travelling (bin room).
- How does packaging choice change in Falmouth or when out and about?

**Household routines**
- Why leave a ready meal (Charlie Bigham) for your husband when you are away?
- How does growing produce reduce what you need to buy wrapped?

**Diary callbacks**
- Microwave rice pouches in the pantry and guilt about using them. *(diary callback)*
- Monday quick deli-wrap meals vs weekend special food. *(diary callback)*
- Heroes/Celebrations chocolates for sailing events. *(diary callback)*
- Morning freezer check before breakfast. *(diary callback)*
- Large cheese block: cost and packaging tradeoff. *(diary callback)*

---

#### Follow-up 1 (Step 3) · Cath

**Study participation**
- Are you enjoying the diary, and has it given you a sense of purpose?
- Has participation changed how you notice packaging?

**Diary callbacks — pantry**
- Walk through the pantry video: packets of rice on the shelf. *(diary callback)*
- Are these microwaveable rice pouches? *(diary callback)*
- Why do they make you feel guilty, and why do you still use them? *(diary callback)*

**Diary callbacks — weeks 1–2**
- Tell me about standout meals or packaging from the first two diary weeks. *(diary callback)*
- What was recycled, reused, or thrown away? *(diary callback)*

---

#### Follow-up 2 (Step 7) · Cath

**Meal planning and leftovers**
- How do you plan leftovers for lunches, especially for your husband? *(diary callback)*
- Which dishes lend themselves to leftovers vs which do not?

**Weekly tempo**
- Why is Monday a quicker, lower-priority cooking day? *(diary callback)*
- How do weekends and bank holidays differ for food spending? *(diary callback)*
- What makes the folded deli wraps a quick Monday meal? *(diary callback)*

**Freezer and shopping**
- Describe your two freezers and what you keep in each. *(diary callback)*
- What is your morning routine for pulling items from the freezer? *(diary callback)*
- How do you handle freezing part of a larger item (e.g. cheese block)? *(diary callback)*

**Packaging tradeoffs**
- Why buy a larger cheese block, and how does packaging factor in? *(diary callback)*
- Tell me about the "nasty" pouch you referenced. *(diary callback)*
- How do competing concerns affect otherwise enjoyable shopping trips? *(diary callback)*

---

### Behavioral lens summary across steps

| Step | Primary lenses |
|------|----------------|
| Interview 1 | Identity, Recycling diligence, Reuse tendency, Food waste sensitivity |
| Diary 1 | Occasion, Identity, Food waste sensitivity |
| Diary 2 | Occasion, Recycling diligence, Reuse tendency |
| Follow-up 1 | Attitude-behavior gap, Convenience tradeoff, Identity |
| Diary 3 | Occasion, Convenience tradeoff |
| Diary 4 | Occasion, Recycling diligence |
| Follow-up 2 | Occasion, Food waste sensitivity, Attitude-behavior gap, Convenience tradeoff |
| Interview 2 | Identity, Culture/social, Attitude-behavior gap, Reuse tendency |

---

### Marina (Phase 1)

**Profile:** Part-time exams officer (30 hrs, term-time); shared custody of eight-year-old (Thu–Fri). No car; cycles with panniers; veg box delivery Fridays; refill shopping at Regal (Wallingford) and Waitrose. Strong environmental values; Oxfordshire recycling.

### Data order and volume

| Step | Calibration step | File | Date | Words | Characters |
|------|------------------|------|------|-------|------------|
| 0 | Interview 1 | `20220428_Interview_1_Marina.docx` | 28/04/22 | 18,387 | 92,555 |
| 1 | Diary 1 | `20220502_Marina_diary_entries_1.docx` | 02/05/22 | 1,219 | 6,842 |
| 2 | Diary 2 | `20220511_Marina_diary_entries_2.docx` | 11/05/22 | 1,367 | 7,410 |
| 3 | Follow-up interview 1 | `20220505_Follow_up_1_Marina.docx` | 05/05/22 | 4,908 | 26,407 |
| 4 | Diary 3 | `20220515_Marina_diary_entries_3.docx` | 15/05/22 | 1,294 | 7,069 |
| 5 | Diary 4 | `20220516_Marina_diary_entries_4.docx` | 16/05/22 | 1,082 | 5,707 |
| 7 | Follow-up interview 2 | `20220511_Follow_up_2_Marina.docx` | 11/05/22 | 2,436 | 12,781 |
| — | Interview 2 (held out) | `20220530_Interview 2_Marina.docx` | 30/05/22 | 13,044 | 67,141 |

**Participant totals:** 43,737 words · 225,912 characters · 8 files

---

### Step summaries

#### Interview 1 (Step 0) · Marina — 18,387 words · 92,555 characters

**Themes:**
- **Household/home:** Son lives with his father but stays with her part of the week, splitting her time between childcare, work, and solo household routines; can take the train from her area for some trips.
- **Routines:** Split-week custody shapes when she shops, cooks, and cleans; often on her own, so cooking and household tasks compete with a demanding part-time work schedule.
- **Shopping:** No car; cycles with panniers, which limits where and how much she can carry; visits Regal refill shop in Wallingford (bus-accessible but slower than driving); tops up at Waitrose and local supermarkets; has always been puzzled by people who buy without thinking about what they consume.
- **Food/preparation:** Weekend vs midweek meals differ (better cooking on Saturdays and Sundays, per interview topics); often cooking and cleaning while on her own between work and custody days.
- **Plastic packaging:** Strong childhood awareness of packaging waste; misses Waitrose cheese, meat, and fish counters that closed during COVID; weighs packaging complexity when deciding what to buy.
- **Disposal/recycling:** Oxfordshire mixed recycling shapes daily decisions; even with local knowledge, some items have too many packaging components to feel worth sorting; flexible plastics collected separately (yoghurt pots kept near sink area).
- **Reuse:** Purpose-made refill bags (foldable, designed for loose weighing); weigh-and-fill routine at refill shops; reuses takeaway containers for meat storage and freezing before eventually recycling them when they break.

**Behavioral lenses:** Identity (lifelong environmental awareness), Convenience tradeoff (cycling limits, split-week routine), Pricing/value (refill vs packaged tradeoffs), Recycling diligence (Oxfordshire schemes, component-count fatigue), Attitude-behavior gap (values vs practical eating), Reuse tendency (refill bags, takeaway tubs), Culture/social (custody schedule, refill-shop ethics).

---

#### Diary 1 (Step 1) — 1,219 words · 6,842 characters

**Themes:**
- **Monday 25 April:** Shop trip; organic yoghurt past use-by date judged still fine for breakfast; items assessed for freezability and packaging recyclability before purchase.
- **Freezable vs use-now items:** Some purchases kept for later freezing; trays rinsed and recycled, with part of paper packaging also recyclable; other items earmarked for same-day dinner because they cannot freeze; notes packaging that has recently changed to reduce plastic with clearer recycling instructions.
- **Tuesday 26 April:** Continued logging (date header only in source).
- **Friday 29 April:** Loose fruit in a sturdy paper bag; non-recyclable label to rubbish; bag itself recyclable but sturdy enough to reuse first.

**Behavioral lenses:** Recycling diligence (label-checking, separation instructions), Food waste sensitivity (use-by judgement, freezability logic), Reuse tendency (paper fruit bag).

---

#### Diary 2 (Step 2) — 1,367 words · 7,410 characters

**Themes:**
- **Monday 2 May — veg box:** Loose veg with no packaging; food scraps to compost bin; compostable veg-box wrapping accumulated slowly (unsure how well it composts at home).
- **Cardboard packaging:** Veg and eggs in cardboard destined for recycling or compost once empty.
- **Loose Tesco veg:** Strong dislike of single-use plastic-wrapped produce when alternatives exist; still values eating a variety of food colours for nutrition.
- **Refill shopping:** Spices and dried goods in refill containers; spice pot refilled in-store rather than replaced; glass jar obtained second-hand.
- **Sauce jar:** Glass jar with cap recyclable when empty; possible reuse.
- **Meat storage:** Portion frozen in a reused takeaway container; containers reused several times before recycling; they tend to crack after repeated use.

**Behavioral lenses:** Identity (anti-plastic-wrap preference, refill ethos), Reuse tendency (takeaway tubs, second-hand jars, refilled spice pot), Recycling diligence (cardboard routing, compostable packaging caution), Convenience tradeoff (frozen meat portions), Food waste sensitivity (composting scraps).

---

#### Follow-up interview 1 (Step 3) · Marina — 4,908 words · 26,407 characters

**Themes:**
- **Study reflexivity:** Enjoying the diary; finds it interesting to write habits on paper and make implicit routines explicit; often topics she already thinks about.
- **Bin-cupboard photo:** Diary includes a photograph of home recycling bins; kitchen entrance has a small cupboard on each side (bin cupboard with water meter; opposite cupboard with electricity meter); bins kept in kitchen for easy sorting while cooking.

**Questions asked:** See [Follow-up 1 (Step 3)](#follow-up-1-step-3-marina) below.

**Behavioral lenses:** Identity (reflective environmental participant), Recycling diligence (in-kitchen bin setup), Culture/social (photo-elicitation of domestic infrastructure).

---

#### Diary 3 (Step 4) — 1,294 words · 7,069 characters

**Themes:**
- **Wednesday 11 May / Thursday 12 May:** Mix of shop-bought and home-prepared meals across two days.
- **Pastry preference:** Sweet pastry bought the evening before; prefers freshly baked goods over long-life pre-packaged pastries lacking crispy, flaky texture.
- **Breakfast routine:** Common breakfast of oats, dried fruit, and yoghurt; broken fridge at Tesco Express limited yoghurt choice on a targeted yoghurt run.
- **Cereal:** Supermarket own-brand cereal unless a special offer on branded options; aware of refill cereal in some shops.
- **Fish cakes:** Bought a couple of weeks earlier; recycling information only visible inside packaging once opened; tries to buy seafood selectively.
- **Freezing:** Green beans frozen in a reused takeaway container to prolong life; peas among the few vegetables bought frozen in a plastic bag for ease, with recyclable marking checked before purchase.

**Behavioral lenses:** Convenience tradeoff (frozen peas, broken-fridge shop), Recycling diligence (inside-label surprise, recyclable-mark check), Reuse tendency (takeaway tub for beans), Attitude-behavior gap (packaging info only after opening), Identity (fresh-bakery preference).

---

#### Diary 4 (Step 5) — 1,082 words · 5,707 characters

**Themes:**
- **Sunday 15 May through Friday 20 May:** Week logged across six dates (Mon–Fri plus Sunday).
- **Reduced-section treats:** Doughnuts from reduced section eaten on walk home (two consumed immediately); paper bag with thin plastic window and large label.
- **Reduced bakery items:** Muffins and ciabatta rolls in plastic wrapping, reduced to a fifth of original price; frozen until needed.

**Behavioral lenses:** Pricing/value (deep reductions, impulse treats), Convenience tradeoff (eat-while-walking doughnuts), Reuse tendency (freezing bakery for later), Recycling diligence (paper/plastic window separation implied by packaging description).

---

#### Follow-up interview 2 (Step 7) · Marina — 2,436 words · 12,781 characters

**Themes:**
- **Plastic-wrapped produce:** Hates buying fruit and vegetables in single-use plastic when alternatives exist; still loves variety of food colours for nutrition.
- **Refill containers:** Discusses practicalities of refilling rice and pasta; appreciates how refillable dried goods work in routine.
- **Meal-deal shopping:** Breaded chicken pieces bought as part of a pizza meal deal (pizza plus sides such as chicken or garlic bread).
- **Refill vs bulk plastic:** Buys pasta loose through refill stores but also purchases 3 kg plastic bags of pasta; framed as a practical transport or shopping-context compromise rather than a values reversal.

**Questions asked:** See [Follow-up 2 (Step 7)](#follow-up-2-step-7-marina) below.

**Behavioral lenses:** Identity (anti-plastic-wrap stance), Convenience tradeoff (meal deals, 3 kg pasta bags), Attitude-behavior gap (refill ideals vs plastic-bag practicality), Reuse tendency (refill-container routine), Pricing/value (meal-deal structure).

---

#### Interview 2 (held out) · Marina — 13,044 words · 67,141 characters

**Themes:**
- **Media awareness:** Recalls content about how much plastic households accumulate.
- **Work fatigue:** Long workdays often mean not getting home until around half past six; affects energy for cooking and packaging-conscious shopping.
- **Meat and refill phase:** Period of not buying meat unless she could refill her own container; extends to other products only available in plastic or without cardboard/refill alternatives.
- **On-the-go disposal:** When eating purchased food while still out, packaging often goes straight in a bin rather than coming home for sorting.
- **Easier meals for two:** Falls back on simpler shared meals when her son is with her.
- **Recycling expansion:** Recent increase in locally recyclable plastics reduces anxiety about some purchases.
- **Bag reuse:** Shakes crumbs out of bags and puts them back into use; paper bags reused until torn, dirty, or grease-stained.

**Questions asked:** See [Interview 2 (held out)](#interview-2-held-out-marina) below.

**Behavioral lenses:** Identity (pragmatic environmentalist), Attitude-behavior gap (past restriction phase vs current balance), Convenience tradeoff (late-home meals, on-the-go bins), Recycling diligence (expanded local acceptance), Reuse tendency (crumb-shaken bags, paper bags), Culture/social (son as co-eater, custody weekends).

---

### Interview questions

#### Interview 1 (Step 0) · Marina

**Household / home / neighbourhood**
- Tell me about yourself, your family, and how you spend spare time.
- How does shared custody shape your weekly routine?
- How does living without a car affect where you can shop?

**Food / preparation / shopping / routines**
- Walk through a typical working week: work hours, food shopping, and cleaning.
- Are particular days reserved for shopping or bigger cooking?
- What do you buy from Regal refill shop in Wallingford?
- How do you transport dried goods (nuts, pasta) home from refill shops?
- How do weekend meals compare with midweek meals?
- Why do you cook more ambitiously on Saturdays and Sundays?
- Which products have packaging you consider too difficult to manage?
- What do you do with meat packaging (hard plastic trays, films)?
- Describe your quick-cooking repertoire and how you add vegetables.

**Disposal / recycling / packaging**
- How does cycling everywhere shape packaging and shopping choices?
- Where do you keep the bag for flexible plastics?
- Describe your in-kitchen recycling bin setup.
- How do you decide whether a plastic goes in recycling vs rubbish?
- Give examples of hard plastics you recycle locally.
- How often do you get takeaways, and what happens to the containers?

**Broader context**
- What priorities outside work compete with environmental goals?
- Which packaging decisions make you anxious?
- How are you finding balance after a phase of saying no to plastic-packaged food?
- What does Oxfordshire's recycling system accept?
- What goes in the flexible-plastics collection (yoghurt pots, etc.)?
- Where are yoghurt pots kept before recycling (sink area)?

---

#### Interview 2 (held out) · Marina

**Packaging materials**
- Aside from environmental impact, how does plastic food packaging compare with other materials for you?
- Why did a yoghurt pot no longer have its plastic lid, and how did you adapt?
- Walk through recycling instructions on a milk/oat-milk carton (label placement).

**Recycling behaviour**
- Revisit the first-interview point about refusing plastic when alternatives exist.
- When labelling is unclear, what mental process do you use?
- How long do you typically keep yoghurt or similar products once opened?

**Diary callbacks**
- Thursday 12 May breakfast and packaging (yoghurt, cereal, oat milk). *(diary callback)*
- Fish cakes with recycling information inside the packaging. *(diary callback)*
- Green beans and peas freezing routines. *(diary callback)*
- Sweet pastry vs long-life packaged pastries. *(diary callback)*
- What do you do with packaging when travelling or away from home? *(diary callback)*

---

#### Follow-up 1 (Step 3) · Marina

**Study participation**
- Are you enjoying the diary, and has writing habits on paper changed how you see them?
- Has participation changed how you notice packaging?

**Bin-cupboard photo-elicitation**
- Walk through the photograph of your home recycling bins. *(diary callback)*
- Why are bins located in the kitchen entrance cupboards? *(diary callback)*
- What is in the bin cupboard vs the meter cupboard opposite? *(diary callback)*

**Diary callbacks — weeks 1–2**
- Monday 25 April: yoghurt use-by judgement and recyclability checks. *(diary callback)*
- Freezable vs same-day dinner items and packaging changes. *(diary callback)*
- Friday fruit bag: reusable paper vs non-recyclable label. *(diary callback)*
- Veg-box compostable wrapping and compost-bin caution. *(diary callback)*
- Refill spices, second-hand glass jar, and takeaway-container meat freezing. *(diary callback)*

---

#### Follow-up 2 (Step 7) · Marina

**Produce and refills**
- Why do you hate plastic-wrapped fruit and veg when alternatives exist? *(diary callback)*
- How do you balance food-colour variety with packaging preferences? *(diary callback)*
- Walk through refill-container practicalities for rice and pasta. *(diary callback)*
- Why buy both refill pasta and 3 kg plastic bags? *(diary callback)*

**Meal-deal shopping**
- Describe the pizza meal deal with breaded chicken sides. *(diary callback)*

**Packaging return / storage**
- How do you return or store reusable packaging during the week? *(diary callback)*
- Where is reusable packaging kept between shops? *(diary callback)*

---

### Behavioral lens summary across steps

| Step | Primary lenses |
|------|----------------|
| Interview 1 | Identity, Attitude-behavior gap, Recycling diligence, Convenience tradeoff |
| Diary 1 | Recycling diligence, Food waste sensitivity, Reuse tendency |
| Diary 2 | Identity, Reuse tendency, Recycling diligence, Food waste sensitivity |
| Follow-up 1 | Identity, Recycling diligence, Culture/social |
| Diary 3 | Convenience tradeoff, Recycling diligence, Reuse tendency, Attitude-behavior gap |
| Diary 4 | Pricing/value, Convenience tradeoff, Reuse tendency |
| Follow-up 2 | Identity, Attitude-behavior gap, Convenience tradeoff, Reuse tendency |
| Interview 2 | Identity, Attitude-behavior gap, Convenience tradeoff, Reuse tendency |

---

### Stephen (Phase 1)

**Profile:** Works in community grants/data/policy; founded local community fridge (now larder); environmental science graduate. Lives with partner and cat in hometown; cycles most days; volunteers weekly Waitrose food collection.

### Data order and volume

| Step | Calibration step | File | Date | Words | Characters |
|------|------------------|------|------|-------|------------|
| 0 | Interview 1 | `20220428_Interview_1_Stephen.docx` | 28/04/22 | 14,124 | 72,867 |
| 1 | Diary 1 | `20220501_Stephen_diary_entries_1.docx` | 01/05/22 | 184 | 1,036 |
| 2 | Diary 2 | `20220509_Stephen_diary_entries_2.docx` | 09/05/22 | 271 | 1,538 |
| 3 | Follow-up interview 1 | `20220506_Follow_up_1_Stephen.docx` | 06/05/22 | 3,263 | 17,605 |
| 4 | Diary 3 | `20220516_Stephen_diary_entries_3.docx` | 16/05/22 | 171 | 973 |
| 5 | Diary 4 | `20220522_Stephen_diary_entries_4.docx` | 22/05/22 | 127 | 760 |
| 6 | Diary 5 | `20220530_Stephen_diary_entries_5.docx` | 30/05/22 | 215 | 1,260 |
| 7 | Follow-up interview 2 | `20220512_Follow_up_2_Stephen.docx` | 12/05/22 | 2,131 | 11,722 |
| — | Interview 2 (held out) | `20220531_Interview_2_Stephen.docx` | 31/05/22 | 7,397 | 38,299 |

**Participant totals:** 27,883 words · 146,060 characters · 9 files

**Diary note:** Five diary files, all very short (127–271 words each); week-level headers dominate. Meal-level detail appears mainly in Diary 2 and Diary 3.

---

### Step summaries

#### Interview 1 (Step 0) · Stephen — 14,124 words · 72,867 characters

**Themes:**
- **Household/home:** Lives with partner and cat outside the main town; hometown community-food project is central to his civic identity.
- **Routines:** Varied council job (data, grants, policy); cycles most days; volunteers weekly collecting surplus food from Waitrose for the community larder.
- **Community larder:** Attended an intro session and founded a local community fridge, which evolved into a community larder focused on intercepting surplus food from the supply chain; volunteers collect supermarket end-of-day surplus; frustrated when some stores restrict what volunteers can take from donations.
- **Food/preparation:** Uses freezing heavily for leftovers, bread, and items at risk of spoiling; sweet tooth with snack intake varying by how the week is going (per interview topics).
- **Plastic packaging:** Feeds the cat with plastic pouches (unavoidable in practice); also buys large 20 kg dry-kibble bags; noticed Whiskers advertising a move toward cardboard cat-food packaging.
- **Disposal/recycling:** Connected to CAG (Community Action Groups), county-council-funded waste-reduction networks; cares deeply about recycling and waste reduction but describes ups and downs in how intensely he practices it; separate glass, mixed recycling, food caddy, and general waste systems discussed in interview (grey bin, council-provided caddy, bin put out infrequently every 8–10 weeks).
- **Reuse:** Reuses supermarket carrier bags; takeaway containers noted as useful freezer vessels (per interview topics and later steps).

**Behavioral lenses:** Identity (environmental science graduate, community-larder founder), Culture/social (CAG network, volunteer food collection), Convenience tradeoff (cat pouches, community-fridge rescued food), Recycling diligence (multi-stream sorting, label confusion), Attitude-behavior gap (strong values vs inconsistent intensity), Reuse tendency (freezing, bag reuse, takeaway tubs), Food waste sensitivity (larder mission, freezer habit).

---

#### Diary 1 (Step 1) — 184 words · 1,036 characters

**Themes:**
- **Week 1:** Diary batch logged under a single week header; no meal-level detail in source summary.

**Behavioral lenses:** Identity (study participation), Occasion (week 1 baseline).

---

#### Diary 2 (Step 2) — 271 words · 1,538 characters

**Themes:**
- **Saturday 7 May — lunch:** Pre-made potato salad and ready-to-eat edamame beans from M&S, sourced via the community larder; paired with a reduced Sainsbury's triple sandwich bought the day before.
- **Sunday 8 May — breakfast:** Planned oatcakes but found mould one day after best-before date; prompted reflection on whether plastic packaging actually extends shelf life as expected.

**Behavioral lenses:** Culture/social (community-larder food), Pricing/value (reduced sandwich), Food waste sensitivity (mould despite best-before), Attitude-behavior gap (packaging trust questioned), Convenience tradeoff (ready-to-eat larder items).

---

#### Follow-up interview 1 (Step 3) · Stephen — 3,263 words · 17,605 characters

**Themes:**
- **Study reflexivity:** Finds filming shopping and cupboard reflection interesting; participation makes implicit buying habits more visible.
- **Unrecorded reflection:** Raised raw chicken and other raw-meat packaging in a video not yet reviewed by researchers.
- **Plastic and diet:** Still does not see a realistic way to eat without plastic; reflects on this openly in diary video.
- **Chicken vs beef packaging:** Raw chicken feels disgusting to handle (salmonella anxiety) despite enjoying eating it; contrast drawn with raw beef packaging handling.

**Questions asked:** See [Follow-up 1 (Step 3)](#follow-up-1-step-3-stephen) below.

**Behavioral lenses:** Identity (reflective environmental practitioner), Attitude-behavior gap (plastic dependence acknowledged), Convenience tradeoff (packaged meat norms), Food waste sensitivity (hygiene concern driving packaging acceptance).

---

#### Diary 3 (Step 4) — 171 words · 973 characters

**Themes:**
- **Week 3:** Batch header only beyond one detailed entry.
- **Monday 9 May — freezer rummage and dinner:** Video of freezer search and cooking; notes substantial plastic in the meal; apart from leeks, judges most packaging warranted for product protection and food hygiene.

**Behavioral lenses:** Recycling diligence (plastic audit), Attitude-behavior gap (accepts "necessary" plastic), Food waste sensitivity (freezer rummage to use stored food), Reuse tendency (freezer as preservation tool).

---

#### Diary 4 (Step 5) — 127 words · 760 characters

**Themes:**
- **Week 4:** Diary batch logged under week header; no meal-level detail in source summary.

**Behavioral lenses:** Occasion (mid-study week), Identity (continued participation).

---

#### Diary 5 (Step 6) — 215 words · 1,260 characters

**Themes:**
- **Week 5:** Final diary batch under week header; no meal-level detail in source summary.

**Behavioral lenses:** Occasion (late study week), Recycling diligence (ongoing logging).

---

#### Follow-up interview 2 (Step 7) · Stephen — 2,131 words · 12,781 characters

**Themes:**
- **Lidl deluxe potatoes:** Bought "posh" potatoes in plastic packaging because they taste nicer than loose; loose option sometimes available, sometimes not; judges veg appearance a little but prioritises usability over looks.
- **Traditional milk bottle:** Diary reflection on childhood home next to a dairy (two-minute walk); nostalgia for glass milk-bottle delivery routine.
- **Cat treat pouches:** Compares materials across two different cat-treat pouch types; discusses disposal (pouches to rubbish bin).
- **Plastic pragmatism:** Argues plastic is not inherently evil and has legitimate uses, while supporting reduced use; acknowledges hypocrisy in when he calls packaging necessary vs wasteful.
- **Local authority guidance:** Council communications classify certain film lids as "flyaway" plastics; discusses plastic film used on specific products.
- **Manufacturer contact:** Diary mentioned querying a manufacturer (e.g. plastic vs cork on a bottle of fizz); photo review of reduced Sainsbury's triple sandwich led him to revise an earlier judgement.

**Questions asked:** See [Follow-up 2 (Step 7)](#follow-up-2-step-7-stephen) below.

**Behavioral lenses:** Identity (pragmatic environmentalist, self-described hypocrite), Pricing/value (deluxe potatoes, reduced sandwich), Convenience tradeoff (plastic-wrapped potatoes), Attitude-behavior gap (pro-plastic argument vs waste concerns), Culture/social (council recycling communications), Recycling diligence (flyaway-film rules, pouch disposal).

---

#### Interview 2 (held out) · Stephen — 7,397 words · 38,299 characters

**Themes:**
- **Compostable claims:** Skeptical that everything labelled compostable works in home or industrial composting; distinguishes "compostable" from "home compostable."
- **Fridge and freezer routines:** Periodic fridge rummages (especially end of week, before shopping); freezes items nearing spoilage; takeaway containers ideal freezer size and reused.
- **Community-larder packaging:** Most rescued-food packaging is low-grade non-recyclable plastic and goes to general waste; food contents (leaves, etc.) go in the food-recycling caddy; local rules allow some plastic in the food caddy.
- **Loose produce concern:** Worries about other shoppers handling loose fruit and vegetables in store.
- **Food-caddy liners:** Prefers not pouring liquids into an empty liner because of leak-through risk.
- **Travel/holiday:** Discusses packaging and disposal in accommodation away from home (per interview topics).

**Questions asked:** See [Interview 2 (held out)](#interview-2-held-out-stephen) below.

**Behavioral lenses:** Recycling diligence (caddy rules, non-recyclable larder plastics), Reuse tendency (takeaway tubs, freezing on the edge), Food waste sensitivity (fridge rummage, spoilage threshold), Attitude-behavior gap (compostable-label skepticism), Convenience tradeoff (rescued food packaging tradeoff), Culture/social (holiday accommodation, documentary/media callbacks from interview topics).

---

### Interview questions

#### Interview 1 (Step 0) · Stephen

**Household / home / neighbourhood**
- Tell me about yourself, your work, and living outside the main town.
- Describe ups and downs in how much you think about recycling and waste.

**Community larder / volunteering**
- How did you set up the community fridge, and how did it become a larder?
- What do volunteers collect from supermarkets, and what restrictions frustrate you?
- Give examples of rescued food and how freezing portions fits your routine.

**Food / preparation / shopping / routines**
- Describe your typical diet, meals, and cooking patterns.
- How does your sweet tooth affect snack buying across the week?
- How often do you put the bin out (every 8–10 weeks), and how does that work?
- What happens to packaging after a chippy takeaway?
- If you bought loose apples, potatoes, and carrots, how would you handle them?
- What goes in the kitchen food-waste caddy, and where does council waste go?

**Disposal / recycling / packaging**
- What happens to packaging for peas and similar frozen items?
- How do you reuse supermarket carrier bags?
- Describe the large grey recycling bin (without lid) and what goes in it.
- Why is glass kept separate from paper, cardboard, and plastic?
- Which plastic types do you routinely recycle?
- How do you handle spinach bags, potato/onion bags, and spray-bottle tops?
- How did the council communicate about label removal, and what examples were given?
- Why does your partner dislike keeping a bag on the door?

**Pet food / packaging**
- How do you feed the cat (pouches vs 20 kg kibble bag)?
- What did you make of Whiskers moving toward cardboard packaging?

---

#### Interview 2 (held out) · Stephen

**Compostable and biodegradable materials**
- Have you encountered packaging labelled home compostable?
- What is your view on biodegradable or compostable plastics?

**Community larder and disposal**
- Revisit community-fridge/larder packaging that goes straight to rubbish.
- Can plastic go in your food caddy, and why?
- Why reuse takeaway containers for freezing?

**Freezer and food waste**
- What forgotten leftovers have you since used from the back of the freezer?
- Which foods are you less willing to eat after freezing?
- Is there a point where something is too far gone to use?
- At what spoilage threshold would you still use a single piece vs normally discard?

**Recipes and routines**
- Do you repeat recipes from a favourite cookbook?
- Is the kitchen bin the one discussed in diary entries?

**Travel and away-from-home**
- Describe packaging in holiday accommodation you stayed at.
- What do you do when travelling and recycling options are unclear?
- Diary entry taken in the car: what was being disposed of?

**Media and values (callbacks)**
- Revisit first-interview discussion (e.g. documentary/media about plastic pollution).
- Would you freeze yoghurt or similar rather than discard?
- Besides cat pouches, which plastics feel hardest to avoid?

---

#### Follow-up 1 (Step 3) · Stephen

**Study participation**
- How has filming shopping and cupboard contents changed what you notice?
- Has participation changed how you think about packaging?

**Meat packaging**
- Expand on the raw chicken vs raw beef packaging reflection from your video. *(diary callback)*
- Why is raw chicken especially unpleasant to handle despite eating it? *(diary callback)*
- What relevant packaging thoughts have you had that are not yet in the diary? *(diary callback)*

**Plastic and diet**
- You said you still do not see how to eat without plastic; say more about that. *(diary callback)*

**Diary callbacks — weeks 1–2**
- Saturday lunch: community-larder M&S salad/edamame plus reduced Sainsbury's sandwich. *(diary callback)*
- Sunday oatcakes mouldy one day after best-before; what does that imply about packaging? *(diary callback)*

---

#### Follow-up 2 (Step 7) · Stephen

**Potatoes and produce**
- Why buy Lidl deluxe potatoes in plastic when loose may be available? *(diary callback)*
- How much do you judge vegetable appearance vs usability? *(diary callback)*

**Nostalgia and materials**
- Tell me about growing up next to a dairy and traditional milk bottles. *(diary callback)*
- Compare the two cat-treat pouch materials. *(diary callback)*
- What do you do with pouches afterward? *(diary callback)*

**Packaging pragmatism**
- You argued plastic is not evil and has legitimate uses; elaborate. *(diary callback)*
- Where do you feel hypocritical about necessary vs wasteful packaging? *(diary callback)*
- Council guidance on flyaway film lids and product wrapping. *(diary callback)*

**Diary callbacks — products**
- Bottle of fizz: plastic vs cork query and manufacturer contact. *(diary callback)*
- Reduced Sainsbury's triple sandwich photo: why change your mind? *(diary callback)*
- Rubbish-bin disposal for non-recyclable items. *(diary callback)*

---

### Behavioral lens summary across steps

| Step | Primary lenses |
|------|----------------|
| Interview 1 | Identity, Culture/social, Food waste sensitivity, Attitude-behavior gap |
| Diary 1 | Identity, Occasion |
| Diary 2 | Culture/social, Food waste sensitivity, Attitude-behavior gap, Pricing/value |
| Follow-up 1 | Identity, Attitude-behavior gap, Convenience tradeoff |
| Diary 3 | Attitude-behavior gap, Recycling diligence, Food waste sensitivity |
| Diary 4 | Occasion, Identity |
| Diary 5 | Occasion, Recycling diligence |
| Follow-up 2 | Identity, Attitude-behavior gap, Pricing/value, Culture/social |
| Interview 2 | Recycling diligence, Reuse tendency, Food waste sensitivity, Attitude-behavior gap |

---

### Josie (Phase 1)

**Profile:** Marketing at waste/recycling company; main household shopper; keen recycler (scrunch test). Married, pregnant (19 weeks); husband celiac/lactose intolerant; two dogs. Renovated 1960s kitchen; integrated recycling bin; meal planner.

### Data order and volume

| Step | Calibration step | File | Date | Words | Characters |
|------|------------------|------|------|-------|------------|
| 0 | Interview 1 | `20220524_Interview_1_Josie.docx` | 24/05/22 | 18,640 | 92,979 |
| 1 | Diary 1 | `20220523_Josie_diary_entries_1.docx` | 23/05/22 | 388 | 2,069 |
| 2 | Diary 2 | `20220530_Josie_diary_entries_2.docx` | 30/05/22 | 429 | 2,251 |
| 3 | Follow-up interview 1 | `20220527_Follow_up_1_Josie.docx` | 27/05/22 | 3,127 | 16,057 |
| 4 | Diary 3 | `20220606_Josie_diary_entries_3.docx` | 06/06/22 | 518 | 2,744 |
| 5 | Diary 4 | `20220613_Josie_diary_entries_4.docx` | 13/06/22 | 527 | 2,758 |
| 7 | Follow-up interview 2 | `20220530_Follow_up_2_Josie.docx` | 30/05/22 | 2,367 | 12,284 |
| — | Interview 2 (held out) | `20220627_Interview_2_Josie.docx` | 27/06/22 | 18,412 | 92,397 |

**Participant totals:** 44,408 words · 223,539 characters · 8 files

**Diary note:** Four diary files, all short (388–527 words each); most entries are week/date headers with limited meal-level detail in source summaries.

---

### Step summaries

#### Interview 1 (Step 0) · Josie — 18,640 words · 92,979 characters

**Themes:**
- **Household/home:** Lives in current home about five years; grew up elsewhere; married with husband (celiac and lactose intolerant per profile); two dogs; renovated a previously difficult 1960s kitchen with an integrated recycling bin replacing an old bin near the door.
- **Routines:** Main household shopper and meal planner; thinks deliberately before buying; set meal times discussed in interview; quick/simple meals when time is tight.
- **Shopping:** Prefers loose produce over packaged alternatives; examines packaging at point of purchase; reuses bags (dog-food bags and other carrier bags kept for reuse); offers surplus food to friends (per interview topics).
- **Food/preparation:** Food and packaging framed as an accessible starting point for environmental change (like carrier bags or choosing solar for electricity); dog food arrives heavily plastic-packaged including compost-bag products.
- **Plastic packaging:** Strong preference for less packaging and finite-resource awareness; diary reflection on individually wrapped sweets as especially wasteful; joined study because of keen recycling interest.
- **Disposal/recycling:** Uses scrunch test and professional waste-sector knowledge; discovered soft-plastics collection routes through a conference; compares old vs new kitchen recycling setup; meal planning used explicitly to avoid waste.
- **Broader context:** Watches TED talks (publicly available online); bakes in spare time; pregnancy shaping priorities (per interview topics).

**Behavioral lenses:** Identity (waste-sector marketer, environmental values), Recycling diligence (scrunch test, integrated bin, soft-plastics awareness), Food waste sensitivity (meal planner), Convenience tradeoff (quick meals, packaged dog food), Culture/social (offering food to friends, husband's dietary needs), Attitude-behavior gap (values vs packaged necessities).

---

#### Diary 1 (Step 1) — 388 words · 2,069 characters

**Themes:**
- **Week 1:** Batch logged with entries on Wednesday 18 May and Saturday 21 May; no meal-level detail in source summary.

**Behavioral lenses:** Occasion (week 1 rhythm), Identity (study participation), Recycling diligence.

---

#### Diary 2 (Step 2) — 429 words · 2,251 characters

**Themes:**
- **Week 2:** Entries on Wednesday 25 May and Thursday 26 May; no meal-level detail in source summary.

**Behavioral lenses:** Occasion, Convenience tradeoff, Recycling diligence, Reuse tendency.

---

#### Follow-up interview 1 (Step 3) · Josie — 3,127 words · 16,057 characters

**Themes:**
- **Study reflexivity:** Diaries and filming have made her think more about what she buys and how she uses things, especially meat packaging.
- **Household socialisation:** After sausages, husband held up packaging and asked "which bin?" having heard her complain about it repeatedly.
- **Meat-packaging routine:** Washes trays with a little washing-up liquid, soaks, rinses, and puts outside; still dislikes touching raw-meat packaging.
- **Holiday food shop:** Monday 16 May holiday shop discussed (video reference in source).

**Questions asked:** See [Follow-up 1 (Step 3)](#follow-up-1-step-3-josie) below.

**Behavioral lenses:** Identity (household recycling educator), Recycling diligence (meat-tray cleaning), Culture/social (husband learning bin rules), Convenience tradeoff (dislike of handling packaging), Food waste sensitivity.

---

#### Diary 3 (Step 4) — 518 words · 2,744 characters

**Themes:**
- **Week 3:** Entry on Thursday 2 June; no meal-level detail in source summary.

**Behavioral lenses:** Occasion, Recycling diligence, Reuse tendency, Food waste sensitivity.

---

#### Diary 4 (Step 5) — 527 words · 2,758 characters

**Themes:**
- **Week 4:** Entry on Thursday 9 June; no meal-level detail in source summary (later interview references additional June entries not expanded in step summary).

**Behavioral lenses:** Occasion, Convenience tradeoff, Recycling diligence, Food waste sensitivity.

---

#### Follow-up interview 2 (Step 7) · Josie — 2,367 words · 12,284 characters

**Themes:**
- **Using stocks down:** Little new food bought; running down fridge and freezer contents deliberately.
- **Rice cooking shift:** First time boiling rice instead of microwave packets; cooked too much; partner ate leftovers for lunch rather than waste food.
- **Container stash:** Showed stacked reusable containers stored with potatoes and onions; discussed whether there is a point of having too many.
- **Bag reuse:** Reuses clothing-delivery bags as small-room bin liners, prompted by the 10p carrier-bag charge.
- **Pizza-box separation:** Diary photos show pizza boxes separated for recycling; social negotiation when others bin incorrectly; sometimes takes packaging home from elsewhere; challenges behaviour that contradicts council leaflets and social-media guidance.

**Questions asked:** See [Follow-up 2 (Step 7)](#follow-up-2-step-7-josie) below.

**Behavioral lenses:** Food waste sensitivity (running down stocks, leftover rice), Reuse tendency (containers, delivery bags), Recycling diligence (pizza-box sorting, council-guidance enforcement), Culture/social (partner, friends/family bin habits), Convenience tradeoff (rice packets vs boiling), Pricing/value (10p bag charge prompting reuse).

---

#### Interview 2 (held out) · Josie — 18,412 words · 92,397 characters

**Themes:**
- **Pregnancy cravings:** Craves mushrooms and similar foods; unpackaged produce lasts longer at home and gets used up; torn between body cravings and packaging guilt when buying pre-packed items.
- **Sweets and treats:** Film-night Maoams with partner: sweets tipped from bag, eaten, then bag filled with many tiny individual wrappers destined for rubbish; knows this is wasteful; previously bought large share bags when pregnant before.
- **Packaging choices:** Tries to choose less packaging or recyclable/reusable formats; accepts some product types need specific packaging to prolong shelf life.
- **Meal planning:** Would not go back to unplanned shopping; feels she eats better at her peak when following the planner (per interview topics).
- **Freezing and storage:** Meat-freezing routine, separated freezer items, and set meal times revisited (per interview topics).
- **Tools and infrastructure:** Waste Wizard app vs council website for disposal queries; woven baskets, cereal bags, and apple bags collected for reuse; "magic bag" purchase and embarrassment about others seeing her recycling habits (per interview topics).

**Questions asked:** See [Interview 2 (held out)](#interview-2-held-out-josie) below.

**Behavioral lenses:** Identity (professional waste knowledge vs personal cravings), Attitude-behavior gap (Maoams wrappers, pre-packed cravings), Food waste sensitivity (unpacked mushrooms last longer), Convenience tradeoff (individually wrapped sweets), Recycling diligence (Waste Wizard, council guidance), Culture/social (friend's use-by-date attitudes, partner's loose pepper preference), Occasion (pregnancy cravings).

---

### Interview questions

#### Interview 1 (Step 0) · Josie

**Household / home / neighbourhood**
- Tell me about yourself, where you live, and how long you have been there.
- Describe your pregnancy and how it affects food choices.
- Tell me about your husband's celiac and lactose intolerance and how that shapes shopping.
- Describe your two dogs and dog-food packaging.

**Food / preparation / shopping / routines**
- How do you think about products before buying them?
- Why are you the main household shopper?
- What foods do you offer out to friends?
- Which bags do you keep for reuse besides dog-food bags?
- How do you reuse food packaging at home?
- What are your quick, simple meals?
- How did the kitchen renovation change cooking and recycling?

**Disposal / recycling / packaging**
- What did you learn at the conference about soft-plastics collection?
- How does meal planning help you avoid waste?
- Compare the old bin near the door with the new integrated recycling system.
- How does current recycling compare with before the renovation?
- Walk through checking packaging when food shopping.
- Why do you prefer loose over packaged goods?

**Broader context**
- Why did your keen recycling interest make you want to join the study?
- What TED talks do you watch, and on what themes?
- What do you do in spare time, and how often do you bake?
- Reflect on individually wrapped sweets mentioned in your diary.
- What worries you about finite resources and "one planet"?

---

#### Interview 2 (held out) · Josie

**Pregnancy and cravings**
- Why do unpackaged mushrooms last longer and get used up? *(diary callback)*
- When cravings conflict with packaging values, how do you decide? *(diary callback)*

**Sweets and treats**
- Describe film-night Maoams and the tiny wrapper waste. *(diary callback)*
- How does this compare with buying large share bags when pregnant before?

**Meal planning and freezing**
- Would you go back to shopping without a meal planner? *(diary callback)*
- How do set meal times fit your routine? *(diary callback)*
- How do you freeze meat, and what is separated in the freezer? *(diary callback)*
- How did first-time boiled rice go (week four, Monday 6 June entry)? *(diary callback)*

**Recycling tools and infrastructure**
- When abroad or in places with weaker waste infrastructure, what do you do? *(diary callback)*
- Does compostable packaging go in the garden bin separately? *(diary callback)*
- Do you use the Waste Wizard app or the council website? *(diary callback)*
- Does brand information on packaging change your disposal choice?

**Social and household norms**
- Why does your husband prefer loose peppers now? *(diary callback)*
- How does your friend's use-by-date attitude differ from yours on freezing? *(diary callback)*
- Why is a fully stocked freezer better for you? *(diary callback)*
- Woven baskets, cereal bags, apple bags: what do you collect and reuse? *(diary callback)*
- Tuesday 2 June entry: what were you collecting? *(diary callback)*
- What is a "magic bag" purchase? *(diary callback)*
- Were you embarrassed when others saw your recycling habits? *(diary callback)*
- Sunday 12 June last entry: what stood out? *(diary callback)*

**Reuse boundaries**
- Does it matter if a container previously held food before you reuse it in the bathroom?

---

#### Follow-up 1 (Step 3) · Josie

**Study participation**
- What has the project made you think about that is not in the diary?
- Has participation changed how you notice packaging?

**Meat packaging**
- Have you changed behaviour around meat packaging since the study? *(diary callback)*
- Walk through washing, soaking, and binning sausage packaging. *(diary callback)*
- How did your husband react when asking "which bin?" *(diary callback)*

**Diary callbacks**
- Monday 16 May holiday food shop. *(diary callback)*
- Walk through key diary photos from weeks 1–2. *(diary callback)*
- What happened to packaging from flagged meals? *(diary callback)*

---

#### Follow-up 2 (Step 7) · Josie

**Stock use-down**
- You bought little new food while running down fridge and freezer stocks. *(diary callback)*

**Rice and leftovers**
- Was boiling rice the first time instead of microwave packets? *(diary callback)*
- Why did you cook too much, and how were leftovers used? *(diary callback)*

**Containers and bags**
- Show the stacked containers stored with potatoes and onions. *(diary callback)*
- Is there a point when you have too many containers? *(diary callback)*
- How did the 10p carrier-bag charge prompt reusing clothing-delivery bags as bin liners? *(diary callback)*

**Pizza boxes and social sorting**
- Who separated pizza boxes in the diary photos? *(diary callback)*
- Did others throw packaging in the wrong bin? *(diary callback)*
- Did you take packaging home from elsewhere to recycle correctly? *(diary callback)*
- How do you respond when others' disposal goes against council guidance? *(diary callback)*

---

### Behavioral lens summary across steps

| Step | Primary lenses |
|------|----------------|
| Interview 1 | Identity, Recycling diligence, Food waste sensitivity, Attitude-behavior gap |
| Diary 1 | Occasion, Identity, Recycling diligence |
| Diary 2 | Occasion, Convenience tradeoff, Recycling diligence |
| Follow-up 1 | Identity, Recycling diligence, Culture/social |
| Diary 3 | Occasion, Recycling diligence, Reuse tendency |
| Diary 4 | Occasion, Convenience tradeoff, Food waste sensitivity |
| Follow-up 2 | Food waste sensitivity, Reuse tendency, Recycling diligence, Culture/social |
| Interview 2 | Identity, Attitude-behavior gap, Food waste sensitivity, Occasion |

---

## Phase 2 · Confirm

### Francesca (Phase 2 · Confirm)

**Profile:** Teaching assistant; vegetarian since age 14; husband in forces; two adult sons at university. Everyday Plastic participant; eco club lead; COP26 burnout; marches and environmental campaigns.

### Data order and volume

| Step | Calibration step | File | Date | Words | Characters |
|------|------------------|------|------|-------|------------|
| 0 | Interview 1 | `20220617_Interview_1_Francesca.docx` | 17/06/22 | 15,520 | 79,512 |
| 1 | Diary 1 | `20220620_Francesca_diary_entries_1.docx` | 20/06/22 | 1,301 | 7,300 |
| 2 | Diary 2 | `20220627_Francesca_diary_entries_2.docx` | 27/06/22 | 1,494 | 8,184 |
| 3 | Follow-up interview 1 | `20220623_Follow_up_1_Francesca.docx` | 23/06/22 | 4,132 | 22,848 |
| 4 | Diary 3 | `20220704_Francesca_diary_entries_3.docx` | 04/07/22 | 1,698 | 8,903 |
| 5 | Diary 4 | `20220711_Francesca_diary_entries_4.docx` | 11/07/22 | 1,460 | 7,874 |
| 7 | Follow-up interview 2 | `20220630_Follow_up_2_Francesca.docx` | 30/06/22 | 4,593 | 24,607 |
| — | Interview 2 (held out) | `20220721_Interview_2_Francesca.docx` | 21/07/22 | 13,554 | 69,043 |

**Participant totals:** 43,752 words · 228,271 characters · 8 files

---

### Step summaries

#### Interview 1 (Step 0) · Francesca — 15,520 words · 79,512 characters

**Themes:**
- **Household/home:** I live with my husband, he’s in the [x], so we live [x].; So they’re, one is home never and one is home at holiday time.
- **Shopping:** And so he runs little workshops where you, I did it over lock down, where you save everything for a week and then you spread it all over your living room floor ; Yeah I don’t buy, we do have a shop, I think once in the last eight years have I actually bought something from the shop because I don’t believe in, you know I’
- **Food/preparation:** And then at uni went to protests about nuclear power stations and things and was always interested in, well vegetarianism isn’t particularly, back then it wasn’; Well we are, like its an existential threat, climate change.
- **Plastic packaging:** I take part in lots of marches and studies and plastic things like, I took part in Everyday Plastic a few years ago where you had to, the man, Dan I think is hi; But that was good because you didn’t have to save all the plastic, you just noted it down when you used it and then you recycled or did whatever else with it.
- **Disposal/recycling:** But that was good because you didn’t have to save all the plastic, you just noted it down when you used it and then you recycled or did whatever else with it.; Like the other day, its not food packaging I know, but our school ordered loads of PE kit and tennis rackets and a big box, cardboard box, that’s fine.
- **Reuse:** I kind of burnt out before COP26 because I, we were working with the children, forest of promises was a thing that World Wildlife Fund did and so with the child; Yeah I don’t buy, we do have a shop, I think once in the last eight years have I actually bought something from the shop because I don’t believe in, you know I’
- **Routines:** So they’re, one is home never and one is home at holiday time.; So most of the time now its just my husband and I, this is the first year that its been like that.

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

---

#### Diary 1 (Step 1) — 1,301 words · 7,300 characters

**Themes:**
- week 1 – Francesca’s diary entries

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

---

#### Diary 2 (Step 2) — 1,494 words · 8,184 characters

**Themes:**
- week 2 - Francesca's diary entries

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

---

#### Follow-up interview 1 (Step 3) · Francesca — 4,132 words · 22,848 characters

**Themes:**
- 2022-06-23 - Follow up 1 – Francesca
- Firstly, I asked how Francesca is finding recording the diary entries
- Well I do everything and send it to you on the Sunday [laughs]. Because, my life is pretty simple, and the day-to-day is pretty much the same and er, the exciting thing happens on Saturday because I g
- Improvement = reduction of plastic for Francesca
- Emphasis on ‘improving’ herself when food shopping, which is connected to a reduction in the purchase and consumption of plastic here:
- Taken from Francesca’s week 1 diary entry: “I think this is pretty good, plastic-wise. I know where I could improve: always buy raisins from the self-fill in a paper bag, but my husband prefers the la
- As noted above Francesca talks about having a conversation with her husband about switching to the loose raisins as an alternative to the ‘juicier’ raisins in the plastic bag and once I asked her abou
- ‘Ah, no, he’s-, because his diet has changed and he’s eating raisins which he didn’t particularly eat very often, so he’s been trying different types of them because they do vary, some more moist than

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

**Questions asked:** See [Follow-up interview 1 (Step 3)](#follow-up-interview-1-step-3-francesca) below.

---

#### Diary 3 (Step 4) — 1,698 words · 8,903 characters

**Themes:**
- Week 3 - Francesca's diary entries

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

---

#### Diary 4 (Step 5) — 1,460 words · 7,874 characters

**Themes:**
- week 4 - Francesca's diary entries

**Behavioral lenses:** Occasion, Identity, Culture/social, Convenience tradeoff, Recycling diligence, Reuse tendency.

---

#### Follow-up interview 2 (Step 7) · Francesca — 4,593 words · 24,607 characters

**Themes:**
- 2022-06-30 - Follow up 2 – Francesca [pseudonym]
- Week 2 – photograph B – food storage
- Decanting tea from it’s original packaging
- After searching to find the photograph I’ve described to Fran, she states, ‘ah yes, I’m looking at it, it’s a mess [laughs]. It is a mess because, we usually only use the things in the front row and e
- [Francesca goes on to talk about the two tins in the bottom left of the photograph]… Oh, I’ve had them for decades. I think they both originally were gifts, filled with tea, loose tea bags and so we k
- [[Researcher] probes a little bit further about decanting the tea bags from their original packaging into glass jars...]
- [seemingly puzzled by the process herself] Yeah, I don’t know why we do that. At some point [the glass jars] sat don on the counter and they moved back up to the-, I honestly don’t know. We’ve been do
- [[Researcher] asks Fran to elaborate further on her point about only buying tea bags without plastic, that she wouldn’t necessarily choose]

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

**Questions asked:** See [Follow-up interview 2 (Step 7)](#follow-up-interview-2-step-7-francesca) below.

---

#### Interview 2 (held out) · Francesca — 13,554 words · 69,043 characters

**Themes:**
- **Household/home:** Because I live on an [X] base and so we don’t get anybody knocking on our door unless they live here.; But I haven’t, I did the training but I’m just, I certainly couldn’t do it where we live now, I’d have to go out.
- **Shopping:** And so on the bus back that day I was thinking should I join, should I not, because I’d also gone to another little workshop that same day and I was just thinki; But yeah people, its fantastic because you know rather than them just throwing it in the bin or having to take it to the dump people walk buy and see what they 
- **Food/preparation:** I’ve been really really busy with work and so I have, that’s definitely taken a second, a back seat.; And then there was one neighbour we had once and she said, with the green caddy, she said I don’t put meat or fish in it because then there are maggots and she 
- **Plastic packaging:** But if you can avoid having anything that’s the much better option obviously but we have to eat so packaging has to be happening.; So yeah I’ll always as you know go for the paper, cardboard if possible option or bring my own bags to get the fruit and, so I’m not using any more packaging I 
- **Disposal/recycling:** Although a few weeks ago, was it the recycling?; Because you know there’s recycling and there’s the kitchen waste and there’s the landfill bin, so three different types.
- **Reuse:** So yeah I’ll always as you know go for the paper, cardboard if possible option or bring my own bags to get the fruit and, so I’m not using any more packaging I ; But, also, I mean they say don’t put the compostable plastic in recycling, like even the, no I’m getting confused, when you have the kitchen caddy the home comp
- **Routines:** I’ve been really really busy with work and so I have, that’s definitely taken a second, a back seat.; I went to a local, a talk and I went, it was in our local museum in Oxford and it was like a day of things and XR had a few talks and the one I wanted was about

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

**Questions asked:** See [Interview 2 (held out)](#interview-2-held-out-francesca) below.

---

### Interview questions

#### Interview 1 (Step 0) · Francesca

**Household / home / neighbourhood**
- To begin with would you be able to tell me a little bit about yourself, your family?
- Is that for any particular reason then why you just choose to make up a Tupperware, make up a lunch yourself at home?
- And you mentioned as well your son there, so you mentioned you’ve got one son who comes home during the holidays. And...
- You mentioned there about using, filling up the home compostable bags with the frozen peas. How do you find that syst...
- What tends to happen then once you’ve brought the produce home with you, whatever that may be, if that’s the oats or ...

**Food / preparation / shopping / routines**
- So just out of curiosity then would you be able to tell me what the working week looks like in terms of the hours tha...
- Yeah. And so you mentioned there that you will be working during the weekend this weekend just to help out, help the ...
- So you mentioned just there that your husband is not eating in the evening then midweek. Is that for any particular r...
- What types of foods then are we talking about then, you mentioned long life for a minute there, you mentioned dried f...
- I was just thinking as well like in terms of the food shopping, so you mentioned earlier on that you tend to go food ...

**Disposal / recycling / packaging**
- Yeah, you mentioned just that about clingfilm there then so do you not use clingfilm then at all?
- Can I just ask you there, so you mentioned that it comes with, so the bread it comes with a plastic window but its re...

**Broader context**
- Yeah, and you mentioned there as well that you’re very interested, you’re very keen in environmental issues. Would yo...
- Yeah, so you mentioned there that you had high hopes for COP26 but it didn’t really pan out. Can you tell me a little...
- What role then do you think the government has in this country in terms of change or executing change?
- Just within this topic of the focus on environmental issues here, would you be able to tell me what you understand ab...
- And just to take a step back for minute there, just to go back to when we were talking about yourself earlier on and ...
- So is your job then full time at the minute then? Is that a Monday to Friday?
- I see. So when you say spare time there is that you working outside of work hours then in your own time?
- Is that something that just tends to happen then around the planning of the summer play?
- Is that for any particular reason?
- Yeah. And you mentioned just there as well about how your cupboards tend to be fuller than the cupboards of your Brit...
- Ok, would you be able to tell me a bit more about that?
- I see, ok. And I just wanted to ask you as well about your experiences of using the Waitrose, Waitrose Unpacked is it...
- Does that work then for you, that practicality wise?

---

#### Interview 2 (held out) · Francesca

**Diary callbacks (where applicable)**

**Household / home / neighbourhood**
- And just out of curiosity how long have you lived on the camp? I think you mentioned during your first interview that...

**Food / preparation / shopping / routines**
- Ok. I wanted to ask you again about the food shop as well, so you mention here, this was when your younger son had co...
- That’s a good idea. I mean just on that point are there any other food waste packaging that you do tend to reuse or r...

**Disposal / recycling / packaging**
- Is there any particular reason then why you would opt for more paper or cardboard based rather than say plastic?
- Yeah, I see. And did you have something then to decant them from these sturdy containers then into the paper bag?

**Broader context**
- For you what are these actions about? What’s the importance of getting involved in them for you?
- You mentioned as well that, you mentioned that COVID and the pandemic has kind of put a halt maybe to some of the pla...
- Had you moved to various different places before that?
- Does that get used quite regularly then? Is that something that a lot of people would ordinarily then engage with wit...
- Do you want me to read?
- Yeah, and just on a, practicality wise then, so you mentioned there that the nuts were in a sealed bag that you have ...

---

#### Follow-up 1 (Step 3) · Francesca

**Diary callbacks / photo-elicitation**
- Has participation changed how you notice packaging?
- Walk through key diary photos from this period. *(diary callback)*
- Tell me about meals or shopping moments flagged in the diary. *(diary callback)*
- What happened to the packaging from those items? *(diary callback)*
- How does disposal here compare with home or prior habits?

---

#### Follow-up 2 (Step 7) · Francesca

**Diary callbacks (researcher-led probes)**
- Francesca goes on to talk about the two tins in the bottom left of the photograph]… Oh, I’ve had them for decades. I think they both originally were gifts, filled with tea, loose t *(diary callback)*
- Researcher] probes a little bit further about decanting the tea bags from their original packaging into glass jars...] *(diary callback)*
- seemingly puzzled by the process herself] Yeah, I don’t know why we do that. At some point [the glass jars] sat don on the counter and they moved back up to the-, I honestly don’t  *(diary callback)*
- Researcher] asks Fran to elaborate further on her point about only buying tea bags without plastic, that she wouldn’t necessarily choose] *(diary callback)*
- After asking Fran to clarify her point about the tea bags she wouldn’t normally choose, she mentioned that here she was mainly referring to the gifts of tea that people buy, rather *(diary callback)*
- Researcher] asks Francesca about the paper bags on the top shelf storing dried foods such as pasta, rice, and lentils] *(diary callback)*
- Researcher] asks Fran to elaborate on her thoughts about the dog food purchased in plastic packaging, not just specifically for her dog’s diet, but also for the dog treats she buys *(diary callback)*
- Sighs] so, anything, unless you feed a dog tinned food only, I suppose, there’s going to be plastic. If you feed them these royal food diets, there’s plastic involved in that and I *(diary callback)*
- Researcher] asks Francesca to explain what she means by that last point... *(diary callback)*
- Researcher] first asks Francesca about the idea of taking treats in for her colleagues to celebrate her birthday... *(diary callback)*
- Researcher] asks about the labelling that Francesca had mentioned ‘cap on’ *(diary callback)*
- Researcher] asks about Francesca’s thoughts on the guidance for this bottle compared to the guidance for the pomegranate bottle juice that we talked about in the previous follow up *(diary callback)*

---

### Behavioral lens summary across steps

| Step | Primary lenses |
|------|----------------|
| Interview 1 (Step 0) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |
| Diary 1 (Step 1) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |
| Diary 2 (Step 2) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |
| Follow-up interview 1 (Step 3) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |
| Diary 3 (Step 4) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |
| Diary 4 (Step 5) | Occasion, Identity, Culture/social, Convenience tradeoff, Recycling diligence |
| Follow-up interview 2 (Step 7) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |
| Interview 2 (held out) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |

---

### Amy (Phase 2 · Confirm)

**Profile:** Originally from Eastern Europe; in UK 12 years; married, dog, no children. Works for Oxfordshire council; passionate about excessive fruit/veg plastic packaging; returns soft plastics to Tesco.

### Data order and volume

| Step | Calibration step | File | Date | Words | Characters |
|------|------------------|------|------|-------|------------|
| 0 | Interview 1 | `20220614_Interview_1_Amy.docx` | 14/06/22 | 17,371 | 88,174 |
| 1 | Diary 1 | `20220621_Amy_diary_entries_1.docx` | 21/06/22 | 560 | 3,072 |
| 2 | Diary 2 | `20220627_Amy_diary_entries_2.docx` | 27/06/22 | 1,266 | 7,018 |
| 3 | Follow-up interview 1 | `20220621_Follow_up_1_Amy.docx` | 21/06/22 | 4,601 | 24,573 |
| 4 | Diary 3 | `20220704_Amy_diary_entries_3.docx` | 04/07/22 | 620 | 3,345 |
| 5 | Diary 4 | `20220711_Amy_diary_entries_4.docx` | 11/07/22 | 205 | 1,094 |
| 6 | Diary 5 | `20220718_Amy_diary_entries_5.docx` | 18/07/22 | 424 | 2,285 |
| 7 | Follow-up interview 2 | `20220628_Follow up_2_Amy.docx` | 28/06/22 | 3,981 | 21,180 |
| — | Interview 2 (held out) | `20220720_Interview_2_Amy.docx` | 20/07/22 | 11,316 | 58,126 |

**Participant totals:** 40,344 words · 208,867 characters · 9 files

---

### Step summaries

#### Interview 1 (Step 0) · Amy — 17,371 words · 88,174 characters

**Themes:**
- **Household/home:** I lived in [x] afterwards as well for year and a half teaching English with no qualifications, that was fun!; Because like if one household produces so much plastic waste, I mean multiple it, I don’t know is it 60 million in the UK and more worldwide.
- **Shopping:** Sorry I don’t actually, I remember more that it would have said recycle with plastic bags at your local supermarket.; And what I’ve noticed recently is that if I buy fruit, like berries lets say or strawberries or blueberries or things like that, it does actually say or like ha
- **Food/preparation:** So I think they have started to do that, which is great, but yeah I used to just chuck a load of plastic wrappings back at them kind of thing into the, in the l; Yeah it was great because I just always loved the Spanish language.
- **Plastic packaging:** I work for[x] and I feel very passionately about the amount of plastic packaging we just see in stores and the fact that for example many fruits and vegetables ; Yeah I mean its just sad really, I think its just really really sad because if I, so I used to gather the little packages into like a plastic bag and I would th
- **Disposal/recycling:** Yeah I mean its just sad really, I think its just really really sad because if I, so I used to gather the little packages into like a plastic bag and I would th; I think now in some places they do because some of the packages do say you know recycle at your local store with plastic packaging.
- **Reuse:** Yeah I mean its just sad really, I think its just really really sad because if I, so I used to gather the little packages into like a plastic bag and I would th; Oh well obviously there are landfills, but I don’t know if they would go into landfill if they aren’t, don’t know, but yeah so they would go somewhere like a la
- **Routines:** Yeah and I work for the [x] in Oxfordshire at the moment.; I work for[x] and I feel very passionately about the amount of plastic packaging we just see in stores and the fact that for example many fruits and vegetables 

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

---

#### Diary 1 (Step 1) — 560 words · 3,072 characters

**Themes:**
- Fruit wrapped in film that’s “not yet recycled”
- Around 6 or 7 small tomatoes wrapped in packaging containing a tray which can luckily be recycled, and film which isn’t recyclable at home. The suggestion is to recycle this with bags at large superma
- 4 individual burger buns wrapping to be recycled at supermarkets
- A punnet of basil (really, just a handful) wrapped in film that’s “not yet recycled” – isn’t it outrageous? I just wonder why is this necessary and it makes me sad.
- Waitrose chocolate cake – I’m happy to learn that the whole packaging can be recycled. Although, it says “widely recycled” – does that mean it’ll definitely be recycled, or not necessarily everywhere?
- Lastly, a photo of the inside of my plastic food container cupboard. I always keep as many and reuse as many as possible, for storing foods in the fridge, taking food into the office with me, whatever

**Behavioral lenses:** Occasion, Pricing/value, Culture/social, Convenience tradeoff, Recycling diligence, Reuse tendency.

---

#### Diary 2 (Step 2) — 1,266 words · 7,018 characters

**Themes:**
- (2x, back and front) Lidl mini sweet peppers. No sign at all on the packaging to indicate as to what it’s being sold in (‘good’ or ‘bad’ plastic?)
- The compost bin I use to put food waste into, lined with compostable bags. These need to be transferred over to one singular bag such as a carrier bag or compostable bin liners ready for roadside coll
- A bag of chopped kale, wrapping can’t be recycled. My question initially was surrounding the cleanliness of the bag, if it was recyclable, we’d need to make sure the bag’s washed beforehand and it wou
- This company seems to be working on “alternative packaging”, which is great, and I hope is true also. I haven’t seen many of these yet.
- I went to donate blood and received a bag containing ONLY! 3 small rich tea biscuits, wrapped in a small wrapper that… surprise-surprise, can’t be recycled. What a waste of packaging.
- Shopping for vine tomatoes at Lidl. One of the few things there you can buy loose, I don’t understand why we couldn’t do that with other stuff? Tomatoes don’t have the most protective skin either, but
- Weekly food shop for 1 person as husband is away. Most wrapped in our favourite material, plastic.
- 35% less plastic packaging for cheddar… which is nice. But I’ve also heard that people are getting slightly confused with these sorts of stickers on food items, for example thinking it was 35% less fa

**Behavioral lenses:** Occasion, Pricing/value, Culture/social, Convenience tradeoff, Recycling diligence, Reuse tendency.

---

#### Follow-up interview 1 (Step 3) · Amy — 4,601 words · 24,573 characters

**Themes:**
- 2022-06-21 - Follow up 1 – Amy  [pseudonym]
- Reflections on recording the diary entries
- Amy mentioned that she has found recording the diary entries ‘easier’ to find things to record than she thought it would be, so I then asked, if she had initially thought it would be difficult to ‘fin
- Reflecting on her thoughts around what she would record in her diary entries
- ...i was sort of imagining in my head that I’m gonna go and do this normal shopping in Lidl and then I’m gonna show you guys how much plastic there is...and that was my idea, that there would be quite
- [Researcher] asks about Amy’s comment above about ‘learning a lot’ and ‘reading the labels’  - is this something that she would not ordinarily do?
- ‘I would do, but maybe not as much as-, like, you know, you kind of get into a routine and like I say, last time, we talked about the meat packaging. Like, if I buy a box of chicken breast, I did-, be
- So in that sense, yeah and then just reading the labels sort of more closely and things may have changed as well meanwhile and you don’t know that something that wasn’t recyclable before is now recycl

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

**Questions asked:** See [Follow-up interview 1 (Step 3)](#follow-up-interview-1-step-3-amy) below.

---

#### Diary 3 (Step 4) — 620 words · 3,345 characters

**Themes:**
- Noticed that the film was gone from the Danpack butter when I opened a new pack, usually there’s a film in between the lid and the butter. So that was a good surprise because usually the film isn’t re
- Packet of breadcrumbs, in a small pouch that isn’t recyclable, not even at large supermarkets. Unbelievable.
- Packet of kale not yet recycled.
- Bag of dog treats, bought from a new local pet shop, seemed like an independent one rather than a chain pet store, unfortunately it doesn’t even state whether packaging is recyclable.
- Olive oil bottle. I always put these in the normal bin because of some weird logic which I don’t even understand now that I think of it, but it goes something like this: you’re not meant to put oil an
- On the second photo with olive oil you can see a small ‘experiment’ where I Googled what’s the best way to clean a bottle of oil for recycling (or rather, it started with Googling “do I have to wash a
- My ODDBOX deliveries have resumed, this is a medium size fruit & veg box rescued from farms near and far, delivered overnight on a Sunday every 2 weeks.
- It all comes without any packaging apart rocket which was in its own plastic wrapping which cannot be recycled and brown paper bags for smaller fruit. Happy to pay slightly more for fruit and veg that

**Behavioral lenses:** Occasion, Identity, Culture/social, Recycling diligence, Reuse tendency, Food waste sensitivity.

---

#### Diary 4 (Step 5) — 205 words · 1,094 characters

**Themes:**
- The only thing that had a wrapping from the Oddbox delivery was wild rocket, and it doesn’t appear to have any markings, so it’s been discarded in the main bin
- Again no markings on the wrapping, so going to the normal bin…
- Bread from co-op, in an unrecycleable bag
- Ham from a polish shop, not sure if can be recycled so going to the bin (couldn’t see any markings)
- Blueberries, film to be discarded but tray can be recycled so it’s been rinsed and put in the recycling bin
- I usually bin the packages that meat comes in, just seems unhygienic with meat juices and so on so it usually finds its way to the bin really quick, but recently after realising these can be washed an
- Some deliveries come in plastic bags (normally online items/orders) which don’t seem recyclable so they end up in the normal bin unfortunately.
- Shocked to find out even the pasta packaging can’t be recycled

**Behavioral lenses:** Culture/social, Convenience tradeoff, Recycling diligence, Reuse tendency, Attitude-behavior gap.

---

#### Diary 5 (Step 6) — 424 words · 2,285 characters

**Themes:**
- Happened to spot this in the supermarket, SINGLE portion of herring wrapped in its own packaging! Terrible, but it’s all around I suppose, come to think of it. Single servings of cut up fruit in singu
- ‘Recycle this packaging with Terracycle’… well to be honest, if I wasn’t involved in this survey, I probably wouldn’t look it up. I would just bin it, because it seems like you have to go that extra m
- Unsmoked bacon rashers – I don’t think this packaging even states whether it could be recycled, I think that’s why I took a photo of it. At least I couldn’t see any markings.
- Sad to discover that the bag of nuts I get from Lidl isn’t even recyclable, it explicitly says DON’T recycle! To me, the packaging looks eco-friendly and sensible, probably just because of the colour 
- Something we buy weekly, cooked beetroot – also non-recyclable. I am starting to see a pattern here where I probably bin 2/3rds of packaging and only 1/3rd goes in the recycling bin, if even that.
- Bottle of mayo. Where do you even start… It looks to be recycleable purely because of the round arrow logo which I associate with all things recyclable, but I don’t even know for sure if it can be rec
- Bag of mozzarella – don’t recycle!
- Bag of noodles – not yet recycled!

**Behavioral lenses:** Convenience tradeoff, Recycling diligence, Reuse tendency, Food waste sensitivity, Attitude-behavior gap.

---

#### Follow-up interview 2 (Step 7) · Amy — 3,981 words · 21,180 characters

**Themes:**
- Looking at week 2 diary entries
- Mini sweet peppers – No information provided on the packaging
- Within her week two diary entries, Amy indicated that the packaging for her mini sweet peppers did not make a reference to what the packaging was made out of, making a reference to ‘good or bad plasti
- ‘Oh I should have maybe been clearer. Yeah, like whether it’s plastic that can be recycled or whether it’s bad plastic, as in, plastic that can’t be recycled. Because I think, you know, initially, I t
- Interviewer asks how Amy disposed of the packaging...
- ‘I just put it in the normal bin, because I didn’t know if it can be recycled.
- Interviewer then asks about other instances in which Amy is uncertain as to whether the packaging can be recycled
- ‘Yeah, I would normally, put it in the normal bin. But, now I’m thinking maybe I should switch and put it in the recycling, just in case, because I don’t know. It might be a better idea to do that ins

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

**Questions asked:** See [Follow-up interview 2 (Step 7)](#follow-up-interview-2-step-7-amy) below.

---

#### Interview 2 (held out) · Amy — 11,316 words · 58,126 characters

**Themes:**
- **Household/home:** But in terms of the kitchen I think, well I guess in general I would maybe choose a house that would suit my needs, like you know if I was, if we were to buy a ; I didn’t even know what the house looked like.
- **Shopping:** But in terms of the kitchen I think, well I guess in general I would maybe choose a house that would suit my needs, like you know if I was, if we were to buy a ; Oh yeah, so there is a camp shop, quite a small sort of like a supermarket, like a corner shop essentially but they actually now stock quite well, they do all s
- **Food/preparation:** So we decided obviously against to choose a house like that because kitchen is an important place for us and we like to cook food and things like that.; Like we usually just get a chicken, like chargrilled chicken in a, you know with salad in a pitta bread.
- **Plastic packaging:** But other than that I don’t know what happens with the plastic recycling or cardboard or anything like that.; And Essex yeah
 I think in the Midlands if I remember right, yeah we had a, like, it was like blue, I don’t know if it was fabric or like sort of plasticy box, 
- **Disposal/recycling:** But yeah in terms of other recycling stuff I don’t think so.; Lots of people sometimes post oh which week is it, is it the recycling week or is it the normal week.
- **Reuse:** I don’t know if they have a deal with Tesco or if they have access to like leftover food, but they then post it on the Olio app and people around here can go an; Sometimes its just things we don’t eat, like there’s a lot of baguettes or certain types of things that we don’t usually include in our diet, but if something d
- **Routines:** But at the same time community spirit here is quite good.; And then there is a restaurant type bar place as its not open every, well now they actually opened a place for families where they can go for lunch and weekends

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

**Questions asked:** See [Interview 2 (held out)](#interview-2-held-out-amy) below.

---

### Interview questions

#### Interview 1 (Step 0) · Amy

**Household / home / neighbourhood**
- And as well you mentioned that you lived in Spain in for a year too, teaching English. And would you be able to again...
- I see, ok. So all of your waste then went into this one bin then within the shared flat?
- What kind of happened then with in the household? Back at home sorry this is?

**Food / preparation / shopping / routines**
- Just out of curiosity then, so how do you determine then whether, if you came across some plastic food packaging, how...

**Disposal / recycling / packaging**
- And you mentioned a little bit there as well in terms of what happens once you have disposed of it. You mentioned tha...
- How does that make you feel knowing that first world countries as you say do ship some of their waste to other countr...
- So just out of curiosity then what happened then to your waste whilst you were living in Spain?
- I see, ok. So was this a separate collection then to these large bins that you were talking about?
- No, that’s ok. That’s perfectly fine. So in the situations then for example where it might state check or recycle at ...
- I see, ok. And so you were talking about the fruit, the packaging that fruit might come in like strawberries or other...
- Yeah, ok. And just go back to an earlier point you made as well when you were talking about disposing of plastic pack...

**Broader context**
- Just to begin with then would you be able to tell me a little bit about yourself?
- Just on that point you mentioned there, before I guess go back to all of the points that you made about yourself and ...
- And you mentioned as well that you studied humanities in the UK as well. Would you be able to tell me a little bit ab...
- Oh really, so was it more of a, within the residential area then rather than with in a centre perhaps?
- Did you tend to use these at all whilst you were there?
- Was this then just the responsibility or something that your mum did solely herself or is this anything that anybody ...
- Oh really? I mean would you be able to tell me a little bit more about that?
- What items would those be?
- I see. And so you mentioned as well there that you look at the labels. So is this something that you would do each ti...
- What kind of labels are you looking for then when you are checking something that’s new?
- I see, ok. And you just gave an example there of one particular label that might state to check with your local colle...
- I see, ok. And so you’ve just given me one example there, are there any other types of examples of the types of packa...
- I mean would you be able to tell me a little bit more about that as well. I think you mentioned earlier as well, yeah...
- You mentioned hygiene reasons a couple of times there. Is that something that’s important to you?

---

#### Interview 2 (held out) · Amy

**Diary callbacks (where applicable)**

**Household / home / neighbourhood**
- You’ve just mentioned there as well that you used to live in the Midlands and I think this is something you mention i...
- That’s ok, that’s been helpful. So just moving on to the olive oil bottle as well, so you’d mentioned a point about d...

**Food / preparation / shopping / routines**
- You mentioned about the corner shop there and about how they’ve increased perhaps what it is they’re selling there. T...
- And in terms of the types of I guess plastic food packaging that you recycle here, how does that compare to perhaps t...
- Just moving on a little bit now then, so at one point we were talking about dog food and you mentioned that at the ti...
- Just moving on a little bit, so you mentioned about the bag of dog treats as well that you bought from a local pet sh...
- Ok. Right I have one last question based on your week three diary entries before I move on to your week four. So this...
- And your views haven’t changed on that at all? I think you shared another photograph as well for week five which was ...

**Disposal / recycling / packaging**
- I see, ok. And do you know then what happens to the recycling once they take it away?
- What would happen to the containers that you do have at the moment?
- No no, that’s ok. Within your situation, so did you just have perhaps the one bin there, as far as you can remember, ...
- What are your thoughts as well on like biodegradable and compostable plastics as well?
- And is there any particular reason for that? I mean you mentioned that there’s no marking on the packaging at all?
- That’s fine. Ok so my next question was about the packaging there for, I think it was the beef mince. You’d taken a p...

**Broader context**
- You also mentioned as well that you have a Facebook group and I was just wondering in terms of the types of content. ...
- I see and this is just something that you’ve come across, not something that you’ve taken part in yourself?
- Ok. You just mentioned there that you rinse it so its clean and put it upside down to drain. How is it that you do de...
- Its something that you’re kind of avoiding then at the moment?
- Just hypothetically then if you did, after this interview read about it and it came across that perhaps there is a po...
- I mean based on the experiment that you did do you mentioned that you tried using flour to try and clean the inside. ...
- If you receive your, well previously when you received your box in the evening would you not kind of bring this into ...
- You also mentioned about the quality of the produce as well, you mentioned that its much nicer, would you be able to ...
- Because its only very small isn’t it?
- Should I move onto the next point?
- So those concerns originally about it being unhygienic, did that cross your mind at all when you were washing the pac...

---

#### Follow-up 1 (Step 3) · Amy

**Diary callbacks / photo-elicitation**
- Has participation changed how you notice packaging?
- Walk through key diary photos from this period. *(diary callback)*
- Tell me about meals or shopping moments flagged in the diary. *(diary callback)*
- What happened to the packaging from those items? *(diary callback)*
- How does disposal here compare with home or prior habits?

---

#### Follow-up 2 (Step 7) · Amy

**Diary callbacks (researcher-led probes)**
- looking back over Amy’s photograph showing her with the vine tomatoes in the supermarket] *(diary callback)*
- Photograph of all Amy’s food shopping – with plastic packaged cherry tomatoes next to the yoghurts *(diary callback)*
- Interviewer asks about Amy’s efforts to look for a specific variety of tomato for a recipe she is following] *(diary callback)*
- referring back to the photograph of Amy’s shopping] *(diary callback)*
- Interviewer asked about Amy’s decisions to purchase both loose and packaged avocadoes] *(diary callback)*
- Interviewer asks whether she has spoken to her mother about clingfilm] *(diary callback)*
- Interviewer asks Amy if removing that packaging is something that she has always done. ] *(diary callback)*
- Interviewer asks Amy about subscribing to Oddbox ] *(diary callback)*

---

### Behavioral lens summary across steps

| Step | Primary lenses |
|------|----------------|
| Interview 1 (Step 0) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |
| Diary 1 (Step 1) | Occasion, Pricing/value, Culture/social, Convenience tradeoff, Recycling diligence |
| Diary 2 (Step 2) | Occasion, Pricing/value, Culture/social, Convenience tradeoff, Recycling diligence |
| Follow-up interview 1 (Step 3) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |
| Diary 3 (Step 4) | Occasion, Identity, Culture/social, Recycling diligence, Reuse tendency |
| Diary 4 (Step 5) | Culture/social, Convenience tradeoff, Recycling diligence, Reuse tendency, Attitude-behavior gap |
| Diary 5 (Step 6) | Convenience tradeoff, Recycling diligence, Reuse tendency, Food waste sensitivity, Attitude-behavior gap |
| Follow-up interview 2 (Step 7) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |
| Interview 2 (held out) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |

---

### Gemma (Phase 2 · Confirm)

**Profile:** US-born, 10 years in UK; PhD completed; lodger in Oxford household (retired teachers + one other lodger). Part-time bookshop (Mon/Fri/Sat); walks/cycles to shop; small shared mini-fridge limits bulk buying.

### Data order and volume

| Step | Calibration step | File | Date | Words | Characters |
|------|------------------|------|------|-------|------------|
| 0 | Interview 1 | `20220607_Interview_1_Gemma.docx` | 07/06/22 | 9,260 | 45,994 |
| 1 | Diary 1 | `20220614_Gemma_diary_entries_1.docx` | 14/06/22 | 906 | 4,618 |
| 2 | Diary 2 | `20220620_ Gemma_diary_entries_2.docx` | 20/06/22 | 929 | 4,724 |
| 3 | Follow-up interview 1 | `20220616_Follow_up_1_Gemma.docx` | 16/06/22 | 1,165 | 6,207 |
| 4 | Diary 3 | `20220627_Gemma_diary_entries_3.docx` | 27/06/22 | 1,008 | 5,086 |
| 5 | Diary 4 | `20220704_Gemma_diary_entries_4.docx` | 04/07/22 | 774 | 3,982 |
| 7 | Follow-up interview 2 | `20220621_Follow_up_2_Gemma.docx` | 21/06/22 | 1,089 | 5,989 |
| — | Interview 2 (held out) | `20220711_Interview_2_Gemma.docx` | 11/07/22 | 8,805 | 43,862 |

**Participant totals:** 23,936 words · 120,462 characters · 8 files

---

### Step summaries

#### Interview 1 (Step 0) · Gemma — 9,260 words · 45,994 characters

**Themes:**
- **Household/home:** Yeah, so I’m 33, I’m from the States but I’ve been living in the UK for about 10 years next month and I just finished my PhD in [x] in the autumn at [x], but I ; And live in a house, I’m a lodger in a house with a couple who own the house.
- **Shopping:** And I’m currently working at a bookshop part time and the doing bits of other kinds of work, a little bit of teaching and a little bit of research and stuff lik; Yeah so I, lets see, right now I’m kind of working for the next, usually I work three days a week at the bookshop, so I work on Mondays, Fridays and Saturdays.
- **Food/preparation:** And then there’s like a little fridge that I share with the other lodger, little mini fridge and then cupboards we share, I’ve got a couple of cupboards.; And yeah, so just kind of very easy kind of dynamic and we don’t cook together all the time, but they often do invite me kind of to eat with them or if they hav
- **Plastic packaging:** Two, yeah for plastic and glass and things like that, there are two of those under the sink.; So its just mixed kind of cardboard, paper, glass, plastic and all that kind of thing.
- **Disposal/recycling:** Or things like that that won’t go, you know that I know I’ll eat and that won’t kind of go to waste or anything like that.; So we’ve got a bin for regular rubbish and then recycling stuff, under the sink we’ve got two like canisters for recycling and then we just take them round, its
- **Reuse:** It’s a little limiting with the mini fridge because its essentially like one shelf, half of the crisper drawer and then like one and half of the little things o; So I’m just always very aware of how heavy my bags are going to be.
- **Routines:** And I’m currently working at a bookshop part time and the doing bits of other kinds of work, a little bit of teaching and a little bit of research and stuff lik; Yeah so I, lets see, right now I’m kind of working for the next, usually I work three days a week at the bookshop, so I work on Mondays, Fridays and Saturdays.

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

---

#### Diary 1 (Step 1) — 906 words · 4,618 characters

**Themes:**
- Today’s grocery shopping was a bit more of a top-up than a proper shop (although that’s not unusual for me!). I bought bagged salad (easy because it is pre-washed), a bell pepper (single because I did
- Today wasn’t a bit grocery shopping day. I just stopped by the Co-op in the evening to pick up a loaf of bread. It isn’t the kind I normally buy––it’s a lot bigger––but it seemed like the best option 
- Here am I, claiming never to eat out and I’ve had dinner out twice in a week! I went to dinner at a tapas place with my friend. We had tapas and wine, and I took a little leftover food home in a dispo

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

---

#### Diary 2 (Step 2) — 929 words · 4,724 characters

**Themes:**
- Wednesday 15 June
- Thursday 16 June

**Behavioral lenses:** Occasion, Pricing/value, Identity, Convenience tradeoff, Recycling diligence, Reuse tendency.

---

#### Follow-up interview 1 (Step 3) · Gemma — 1,165 words · 6,207 characters

**Themes:**
- 2022-06-16 - First follow up with Gemma [pseudonym]
- Carrying her re-usable coffee cup can be a deterrent
- During the follow up, reflecting on Gemma’s week 1 diary entries, where she mentions the use of her re-usable Keepcup on a few occasions, she indicates that taking the cup with her as she is out and a
- Practicalities of carrying and using the keep cup whilst out
- ‘I usually carry a little bag, like a little linen, you know those bags that are everywhere, the cotton bags that you get from places so I usually carry something to put my keys and phone and that kin
- [Researcher] asks about why it can be a deterrent?
- ‘Just having something to carry, so if I’m not-, if it just so happens I’m not carrying a bag, which is not usually the case but for work, I often feel like I’m lugging a lot of stuff around, which I 
- Keepcup vs. Plastic cup from a store

**Behavioral lenses:** Occasion, Identity, Convenience tradeoff, Recycling diligence, Reuse tendency, Food waste sensitivity.

**Questions asked:** See [Follow-up interview 1 (Step 3)](#follow-up-interview-1-step-3-gemma) below.

---

#### Diary 3 (Step 4) — 1,008 words · 5,086 characters

**Themes:**
- Wednesday 22 June
- Thursday 23 June

**Behavioral lenses:** Occasion, Pricing/value, Convenience tradeoff, Recycling diligence, Reuse tendency, Food waste sensitivity.

---

#### Diary 4 (Step 5) — 774 words · 3,982 characters

**Themes:**
- I went for a big ‘ole shop today—a bit of a stock the fridge kind of shop. I like having some things in the freezer…and I have this feeling like I should have things in the house in case I come down w
- Unfortunately, I tested positive for Covid yesterday. Not fun! I had a feeling this might’ve been on its way….(!) I didn’t feel so good when I woke up this morning, so I made a bowl of porridge with c
- Still testing positive with Covid, so my friend did the food shop for me and brought it round. My housemate had offered to cook me some soup, so otherwise I would’ve asked my friend to bring me some. 

**Behavioral lenses:** Occasion, Pricing/value, Culture/social, Reuse tendency, Food waste sensitivity, Attitude-behavior gap.

---

#### Follow-up interview 2 (Step 7) · Gemma — 1,089 words · 5,989 characters

**Themes:**
- 2022-06-21 – Second follow up with Gemma [pseudonym]
- Re-using packaging and reusable packaging
- Reflecting on the first entry in Gemma’s week 1 diary entries, Gemma describes the two containers that she used to contain nuts and biscuits in...‘The container is kinda a reusable thing, with a plast
- ‘The pretzels and things, again I save bags [laughs], so I’d bought some nuts in a bag and so I used that’. Previously Gemma has told me about the bread bags that she saves to put food items into for 
- At one point during our follow up, Gemma mentioned that she would usually make a shopping list before she goes food shopping, and that she would think ‘a couple days ahead’ about the types of foods th
- Mum’s ‘nice gesture’ - sending favourite foods from the U.S
- Within Gemma’s week 2 diary entries, she mentioned that her mum (who lives in the U.S. - where Gemma is originally from) has sent some foods that are produced and sold in the U.S to her. When I asked 
- ‘How far do re-use practices go?’

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

**Questions asked:** See [Follow-up interview 2 (Step 7)](#follow-up-interview-2-step-7-gemma) below.

---

#### Interview 2 (held out) · Gemma — 8,805 words · 43,862 characters

**Themes:**
- **Household/home:** Yeah I did, so I lived there for my first two years and then I commuted, I’ve commuted after that subsequently to come up to teach and then meet with my supervi; So I would always, when I got there I would like get a boxed salad to have on the way home because I knew it would be like a healthy option that wasn’t very exp
- **Shopping:** But also just I like having a few things just, it makes it, I guess it means I don’t have to go to the shop as often or I can kind of get other things when I go; Yeah and if there’s certain shops I get certain things at different shops.
- **Food/preparation:** Because I knew I could just eat junk because I was travelling.; So I think I was just aware that where I knew, like I knew I could get something that was a bit healthier then I should probably go for that rather than like wa
- **Plastic packaging:** I mean generally I look on the package to see if it has any instructions about that.; And then I think, I don’t know that I’ve come across like film, plastic film as being recyclable so I usually just toss that.
- **Disposal/recycling:** And then I think, I don’t know that I’ve come across like film, plastic film as being recyclable so I usually just toss that.; But if it says something on the package or if its like a harder plastic then I generally assume that that’s recyclable.
- **Reuse:** We just, I mean we put our recycling in a carrier bag, we just like leave it on the side, on the counter.; Yeah
 Not usually just because we had the bag to take back up!
- **Routines:** So I guess the first year that I did it it was pretty intense because I was teaching every week.; I was coming up every week and I would say three out of the four weeks in a month I would do it in a day.

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

**Questions asked:** See [Interview 2 (held out)](#interview-2-held-out-gemma) below.

---

### Interview questions

#### Interview 1 (Step 0) · Gemma

**Household / home / neighbourhood**
- Sure, that’s perfect. And you mentioned as well that you’re a lodger in a house as well, living with a couple and the...
- And how long, just out of curiosity, how long have you lived there for?

**Food / preparation / shopping / routines**
- And would you be able to tell me a bit more about I guess the kitchen situation. So you mentioned there that you do s...
- Ok. And just going back to the kitchen space then again. So you mentioned that you have two cupboards there and a fri...
- You mentioned just then as well that when you do go food shopping you might buy multiple of the same because its chea...
- And whilst we’re on the subject of the different types of food that you are buying, I mean would you be able to tell ...
- And you just mentioned there as well that you do try to eat less meat than you used to. Would you be able to tell me ...
- I see, ok. And what types of things were those then that you bought for not kind eating immediately like the salad then?
- Yeah, I see. Ok. And you mentioned there as well, moving back onto cooking there that its easier not to do any elabor...
- And so you mentioned there that you have bin and then there are the recycling bins, so the food caddy or the food com...

**Disposal / recycling / packaging**
- I see ok. And the main or the bin for general waste whereabouts is that positioned?
- I see ok. And would you be able to tell me a little bit about the recycling there? So you mentioned that there’s one ...

**Broader context**
- Just to begin then will you be able to tell me a little bit about yourself?
- Would you be able to tell me then, it sounds like you’re involved in quite a few different things then if you’re work...
- Ok. Would you be able to tell me as well, do you have any hobbies or other things that you like to do in your spare t...
- Ok. And whereabouts where you before that then?
- I see, in terms of how much weight the basket can take?
- You mentioned as well then that whilst its mainly for environmental reasons there’s a part of you that just doesn’t f...
- Is that for any particular reason? I know you mentioned that yesterday you were working so you had a sandwich there?
- Ok. Can you tell me more about that, about the differences there between, that you can remember of course between [x]...
- I see. And so for you then, I mean you’ve given me a couple of examples of the different types specifically of plasti...
- Yeah, ok. And you just mentioned there as well that you reuse bread bags. Would you be able to tell me about that?
- Could you tell me more about, so this is the bees wax one you’re talking about? What do you mean then when you say it...
- I see. And when you were talking about the bread bags you mentioned that its good to reuse them. Could you tell me wh...
- Ok. And why bread bags?

---

#### Interview 2 (held out) · Gemma

**Diary callbacks (where applicable)**

**Household / home / neighbourhood**
- You’d take it back upstairs to the flat then?
- Ok. And were there any instances then where perhaps you wouldn’t be returning back to the flat and you would perhaps ...
- Yeah, well that’s ok. Actually one of the questions I was going to ask you is whether you do travel back home a lot. ...
- I see, ok. Do you have anything like that near to where you live?

**Food / preparation / shopping / routines**
- I see, so just out of curiosity then so what was that like within the context of the study, around food and food pack...
- Yeah. And you mentioned there as well that you could easily have eaten junk food as well but because you were travell...
- I see. So you are aware then of I guess the days of the week or the dates at which there’s different collections?
- Yeah, I see. And you mentioned there that on your journey there you stopped to buy some muesli along the way and you ...
- No that’s ok. No I appreciate it was a few weeks ago now. And you mention as well about taking a variety of different...
- Is that something that you have done before then? Is this a brand then that you would tend to buy quite regularly?

**Disposal / recycling / packaging**
- I see and when you say film what exactly do you mean there when you say film? Could you give me an example of what th...
- I see, ok. And then if you came across, I’m sorry just to backtrack to the film plastic as well, you mentioned there ...
- I see, yeah ok. And how did it work then in terms of taking stuff to the larger recycling communal bin downstairs then?
- Yeah, I see. And then the carrier bag then with all of the recyclable material in there, what happens to the carrier ...
- Yeah. And what about the waste disposal set up as well, would that change at all?
- Right, I see. And the type of packaging there?

**Broader context**
- I see, so is this something that you would tend to do quite regularly then if you’re, if you tend to, so you mentione...
- And is that for any particular reason then?
- Ok. Would you be able to tell me a little bit more about what that’s like in comparison to the set up that you have i...
- Ok. Was it a fairly large carrier bag then?
- I see, ok. And then you, again was there a similar pattern in terms of reusing the carrier bag or?
- I see, ok. So it’s a similar set up in terms of collecting all the materials in one as you do in Oxford?
- If there’s any, I mean you mentioned previously about how you would pay attention to the labelling as well on the pac...
- Yeah, ok. Just on that point actually, just going back to the labelling here then in terms of you mentioned that you ...
- I see, ok. And yeah there have been a couple of occasions during your interview and our previous follow ups as well w...
- I see. And is that important to you then in terms of cutting down on the decision making, spending less time in a sto...
- I see. And so you mentioned as well just then that this is the first time that you’ve bought this because it was on o...
- Right, I see, ok. And just one final question about this photograph, what would happen as well then to the yoghurt pot?

---

#### Follow-up 1 (Step 3) · Gemma

**Diary callbacks / photo-elicitation**
- Has participation changed how you notice packaging?
- Walk through key diary photos from this period. *(diary callback)*
- Tell me about meals or shopping moments flagged in the diary. *(diary callback)*
- What happened to the packaging from those items? *(diary callback)*
- How does disposal here compare with home or prior habits?

---

#### Follow-up 2 (Step 7) · Gemma

**Diary callbacks (researcher-led probes)**
- ‘How far do re-use practices go?’ *(diary callback)*

---

### Behavioral lens summary across steps

| Step | Primary lenses |
|------|----------------|
| Interview 1 (Step 0) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |
| Diary 1 (Step 1) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |
| Diary 2 (Step 2) | Occasion, Pricing/value, Identity, Convenience tradeoff, Recycling diligence |
| Follow-up interview 1 (Step 3) | Occasion, Identity, Convenience tradeoff, Recycling diligence, Reuse tendency |
| Diary 3 (Step 4) | Occasion, Pricing/value, Convenience tradeoff, Recycling diligence, Reuse tendency |
| Diary 4 (Step 5) | Occasion, Pricing/value, Culture/social, Reuse tendency, Food waste sensitivity |
| Follow-up interview 2 (Step 7) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |
| Interview 2 (held out) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |

---

### Laura (Phase 2 · Confirm)

**Profile:** NHS worker, 50; husband and two children (19, 16); pub and chickens; Aga cooking; meal planner; abhors food waste; Hello Fresh for recipe variety; tried Veganuary.

### Data order and volume

| Step | Calibration step | File | Date | Words | Characters |
|------|------------------|------|------|-------|------------|
| 0 | Interview 1 | `20220822_Interview_1_Laura.docx` | 22/08/22 | 14,095 | 72,493 |
| 1 | Diary 1 | `20220822_Laura_diary_entries_1.docx` | 22/08/22 | 124 | 693 |
| 2 | Diary 2 | `20220905_Laura_diary_entries_2.docx` | 05/09/22 | 93 | 509 |
| 3 | Follow-up interview 1 | `20220901_Follow_up_1_Laura.docx` | 01/09/22 | 3,324 | 17,882 |
| 4 | Diary 3 | `20220912_Laura_diary_entries_3.docx` | 12/09/22 | 45 | 234 |
| 5 | Diary 4 | `20220919_Laura_diary_entries_4.docx` | 19/09/22 | 38 | 194 |
| 7 | Follow-up interview 2 | `20220907_Follow_up_2_Laura.docx` | 07/09/22 | 1,964 | 10,649 |
| — | Interview 2 (held out) | `20220926_Interview_2_Laura.docx` | 26/09/22 | 8,449 | 44,485 |

**Participant totals:** 28,132 words · 147,139 characters · 8 files

---

### Step summaries

#### Interview 1 (Step 0) · Laura — 14,095 words · 72,493 characters

**Themes:**
- **Household/home:** I guess I was more referencing time for my own personal health and wellbeing versus the personal health and wellbeing of those that I live with.; At the weekends we always seem to be, oh we also have a big old house, so we’re often doing running repairs for that and trying to keep things under control.
- **Shopping:** We have a pub and [xxx], which is important and relevant to my shopping habits.; But it depends whether or not I’ve put any thought into it when I’ve been shopping or whether or not, sometimes things disappear out of the fridge that you were
- **Food/preparation:** I absolutely believe in cooking fresh food.; I don’t really like to compromise on what I eat.
- **Plastic packaging:** But you can normally freeze elderflower cordial if you put it in a plastic bottle and just don’t fill it up.; Well open packet, its made of plastic and not very good for storing items in, as you will be aware because when you open them they invariably split all over the
- **Disposal/recycling:** But because I absolutely abhor food waste I will always try and use stuff up and be innovative about what I’m cooking.; I keep all sorts of things, you know like I keep my ginger in the freezer because you can grate if straight from frozen and it doesn’t waste.
- **Reuse:** I would buy those, bring them home, put them in the freezer and then plan a meal around what I’ve got in the freezer.; So I will plan by what’s in the fridge, what’s in the freezer.
- **Routines:** Yeah, so my name’s Laura [pseudonym], I’m a [xxx] and I work for the NHS.; I guess I was more referencing time for my own personal health and wellbeing versus the personal health and wellbeing of those that I live with.

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

---

#### Diary 1 (Step 1) — 124 words · 693 characters

**Themes:**
- Entry B: And obviously the packet will go in my flyaway plastics bag for recycling
- Entry G: So, this morning I’ve collected up to recycle the tetra packs - they stink! This is a really put off for doing my bit…. Fruit punnet going to recycling bin

**Behavioral lenses:** Recycling diligence, Reuse tendency, Food waste sensitivity, Attitude-behavior gap.

---

#### Diary 2 (Step 2) — 93 words · 509 characters

**Themes:**
- Week 2 - Laura's diary entries

**Behavioral lenses:** Convenience tradeoff, Recycling diligence, Attitude-behavior gap.

---

#### Follow-up interview 1 (Step 3) · Laura — 3,324 words · 17,882 characters

**Themes:**
- 2022-09-01 - Follow up 1 – Laura
- Removing broccoli from its packaging after purchase
- Within her first entry, she mentioned that she would normally take broccoli out from its original plastic packaging that it came sold in and transferred it to alternative packaging to prevent condensa
- Well, when the project gets wet, it’s more likely to deteriorate in the fridge and the other thing about broccoli is [laughs] and this is going to sound pathetic, it just makes a lot of mess in the fr
- [Interviewer prompts Laura about who was helping her unpack the shopping on this occasion]
- That’ll be my husband [laughs] So, I-, yeah so he’d obviously just unpacked it and shoved it in the fridge, whereas I would have taken it out. I tend to take it out and just put it in a Tupperware so 
- Unpacking the food shop –routines
- [Reflecting on the previous point about the way Laura would unpack and store the broccoli after her food shop, the interviewer asks about whether Laura and her husband have different ideas about how t

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

**Questions asked:** See [Follow-up interview 1 (Step 3)](#follow-up-interview-1-step-3-laura) below.

---

#### Diary 3 (Step 4) — 45 words · 234 characters

**Themes:**
- Week 3 - Laura's diary entries

**Behavioral lenses:** Recycling diligence, Reuse tendency.

---

#### Diary 4 (Step 5) — 38 words · 194 characters

**Themes:**
- Week 4 - Laura's diary entries

**Behavioral lenses:** Recycling diligence, Reuse tendency.

---

#### Follow-up interview 2 (Step 7) · Laura — 1,964 words · 10,649 characters

**Themes:**
- 2022-09-07 - Follow up 2 – Laura
- Changes in packaging / less plastic / online food shopping / boundaries of responsibility – recycling /
- [Interviewer asks Laura what her thoughts are on this messaging on the packaging]
- Well, I thought it was good that they told me that there was less plastic packaging, but obviously I’d already noticed that, so I thought it was positive. Did it make me choose the ice cream in partic
- [interviewer asks Laura about whether packaging has an influence on other particular foods that she tends to buy – whether for environmental reasons or otherwise]
- Erm, if they are of a comparable price and quality, then I would probably choose something that wasn’t in a plastic packet. But, most of the time being on a budget, then I would choose the thing that 
- You’ll see from an entry that I’ve done today, that I haven’t shared with you yet, my online shopping came today and I’ve shared some of the things that I purchased from that. So, when I’m not choosin
- [Interviewer asks for clarification on what she means when she states, when she’s ‘not choosing the product’]

**Behavioral lenses:** Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence, Reuse tendency.

**Questions asked:** See [Follow-up interview 2 (Step 7)](#follow-up-interview-2-step-7-laura) below.

---

#### Interview 2 (held out) · Laura — 8,449 words · 44,485 characters

**Themes:**
- **Household/home:** Its often just because we’ve got a really busy home schedule.; And I think right from when I was a child I was probably quite privileged that our family was able to cook for us.
- **Shopping:** So sometimes I’ll buy an ingredient and think oh how am I going to use that and then I’ll find a recipe that will use it up.; So I guess sometimes you get in a bit of a food rut and you go shopping and you buy the same thing time and time again.
- **Food/preparation:** I don’t eat just because I have to eat, I like to eat nice food.; And as a result sometimes I probably over engineer our dinners and so we don’t really eat convenience food.
- **Plastic packaging:** So every time I’ve visited the place where I deposit these things I’ve tried to understand what it is that they say that they’re going with these plastics.; They’ve got those in the front of our local Tesco and I was really pleased that they were full to the rim of people having chucked their flyaway plastics in the
- **Disposal/recycling:** Especially if I’ve seen, I do like to reduce food waste, so these particular fish fillets I’ve noticed I bought in the reduced counter.; I actually don’t know whether or not they go off to be recycled and I’ve been thinking about that.
- **Reuse:** They’ve got those in the front of our local Tesco and I was really pleased that they were full to the rim of people having chucked their flyaway plastics in the; You’ve always been able to recycle plastic bags at the supermarket when they introduced all the bags for life and things like that.
- **Routines:** Yeah well obviously I work in healthcare and I recognise the importance of a balanced diet as the fundamentals for living well really.; And as a result sometimes I probably over engineer our dinners and so we don’t really eat convenience food.

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

**Questions asked:** See [Interview 2 (held out)](#interview-2-held-out-laura) below.

---

### Interview questions

#### Interview 1 (Step 0) · Laura

**Food / preparation / shopping / routines**
- Ok. And you mentioned there as well that food’s a very important part of your life and its something that you’re not ...
- I see. And do these meals that you’re cooking within a particular day, do they vary then across the three different s...
- Just to go back to the meal planner then, so how do you then determine what goes on the meal planner?
- How does that then balance with the meal plans that you already have in place and also your kind of efforts there to ...
- Can you tell me a little bit more about the importance of preventing food waste for you and you also mentioned its so...
- And you mentioned as well that sometimes you would buy some spices whilst you were abroad and these come in better pa...
- Yeah. And just going back to a point you made earlier after you showed me the pantry, you mentioned that cooking is o...
- How do you decide then whether the food packaging falls into or whether it can be taken to a supermarket then?

**Disposal / recycling / packaging**
- I mean I can see as well on the right-hand side there you had a lot of the like kilner style type glass containers th...
- I see. So what type of packaging have you got there?
- Ok, so I mean you’ve described to me a couple of different types of packaging in there that will go into the bag to g...

**Broader context**
- Just to begin with then would you be able to tell me a little bit about yourself?
- Fabulous, ok. Well, you mentioned there, a couple of times you alluded to that you don’t have much time there for ext...
- Ok, so when you say three different time schedules, what do you mean by that?
- Ok. You mentioned there that you decided to go vegan in January. Would you be able to tell me a bit more about the re...
- You’re talking about foraging here as well, is this something that you do yourself?
- Do you store, so once you have made blackberry liquor and the sloe gin and the jams, how do you store them then once ...
- So you have a dedicated space for those?
- Are they all spices there?
- Is that for any particular reason?
- You mentioned as well then, so you’ve got your various types of flours there and pulses. Apart from being able to tel...
- Oh no, not at all. And you mentioned as well that you spice share. So how does that work then because I can assume th...
- What kind of items then go into the cupboard of doom?
- Oh right, I see. So is that where the new rack will be going?
- I see, so is that door always locked into the garage?

---

#### Interview 2 (held out) · Laura

**Diary callbacks (where applicable)**

**Food / preparation / shopping / routines**
- Is there a reason why you’ve made that change to reduce how much processed meat that you have?
- I see so aside then from storing cooking apples then, so what other ways or how else do you use the freezers?

**Disposal / recycling / packaging**
- That is one of the points I wanted to talk to you about as well actually. But as well I mean these types of plastics ...
- I see ok. And have you ever come across packaging that you are unsure as to whether it can be recycled or not?
- Ok. So these black plastic trays, so what did you do in that instance then?
- Oh I see. So when you say the film which part are you referring to here?
- How much can you tell me about biodegradable plastics or packaging?
- You just mentioned there its contrary to what the packaging, what were you referring to?
- Oh it is like a drinks bottle? A really long glass bottle with a straw in?
- That’s ok. But you haven’t put them in the recycling though?
- Does it provide any packaging information?
- Ok. And I’m just curious so you rinsed the tray out but the flyaway or the film lid packaging is too dirty. But what’...

**Broader context**
- I see. So the photograph that you shared with me then of the lid is that what you tend to follow or do you go by any ...
- I also wanted to ask that, another point on clarification here as well. So when talking about the different types of ...
- Do you know why perhaps the yoghurt and margarine tubs weren’t accepted in [x]?
- How did you find out about that?
- Right I see and was that a recent situation?
- Can you tell me the reason for that?
- I wondered what your thoughts were on those two cups. So they were two slightly different cups that you shared the vi...
- What’s happened to these cups since?
- I see. And what kind of information does Ocado provide you on each particular item?
- I was just going to ask you what are your thoughts on that? So there’s differences there in terms of what the milk bo...

---

#### Follow-up 1 (Step 3) · Laura

**Diary callbacks / photo-elicitation**
- Has participation changed how you notice packaging?
- Walk through key diary photos from this period. *(diary callback)*
- Tell me about meals or shopping moments flagged in the diary. *(diary callback)*
- What happened to the packaging from those items? *(diary callback)*
- How does disposal here compare with home or prior habits?

---

#### Follow-up 2 (Step 7) · Laura

**Diary callbacks (researcher-led probes)**
- Interviewer asks Laura what her thoughts are on this messaging on the packaging] *(diary callback)*
- Well, I thought it was good that they told me that there was less plastic packaging, but obviously I’d already noticed that, so I thought it was positive. Did it make me choose the *(diary callback)*
- interviewer asks Laura about whether packaging has an influence on other particular foods that she tends to buy – whether for environmental reasons or otherwise] *(diary callback)*
- Interviewer asks for clarification on what she means when she states, when she’s ‘not choosing the product’] *(diary callback)*
- So, when you do online shopping, you can’t tell necessarily how it’s packaged. You can’t always tell how it’s going to arrive. Sometimes they will show the project out of the packa *(diary callback)*
- Reflecting on the ice cream that Laura had purchased which had come sold in cardboard-based packaging for the most part, the interviewer asks how plastic packaging compares to card *(diary callback)*
- Diary entry highlights Laura preparing lunch and only needed one bread roll from a multipack of bread rolls and the need to find alternative means to package them to preserve fresh *(diary callback)*
- Video entry that starts with looking at pitta breads. Within the video Laura mentions buying the large plastic 3kg bag of pasta and then decanting this into a Kilner jar] *(diary callback)*
- Well I guess they’re [pak choi], they’re harder to-, I guess if you’re buying them from a massive supermarket, a lot of those vegetables are put in packaging to make them easier to *(diary callback)*
- Video diary shared and a photograph] *(diary callback)*
- Interviewer asks Laura whether there are other types of foods besides fruits and vegetables that we’ve already discussed, where she would consider the packaging to be unnecessary] *(diary callback)*
- Interviewer  reminds Laura about her point in her diary entry about the food covers and how they are able to go in the dishwasher and asks about the circumstances in which she may  *(diary callback)*

---

### Behavioral lens summary across steps

| Step | Primary lenses |
|------|----------------|
| Interview 1 (Step 0) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |
| Diary 1 (Step 1) | Recycling diligence, Reuse tendency, Food waste sensitivity, Attitude-behavior gap |
| Diary 2 (Step 2) | Convenience tradeoff, Recycling diligence, Attitude-behavior gap |
| Follow-up interview 1 (Step 3) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |
| Diary 3 (Step 4) | Recycling diligence, Reuse tendency |
| Diary 4 (Step 5) | Recycling diligence, Reuse tendency |
| Follow-up interview 2 (Step 7) | Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence |
| Interview 2 (held out) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |

---

### Hannah (Phase 2 · Confirm)

**Profile:** [xxx] designer, hybrid office; vegan; lives with boyfriend in Oxfordshire. Mum modelled low-packaging shopping; zero-waste shops, greengrocer, Lidl; bread maker at home.

### Data order and volume

| Step | Calibration step | File | Date | Words | Characters |
|------|------------------|------|------|-------|------------|
| 0 | Interview 1 | `20220808_Interview_1_Hannah.docx` | 08/08/22 | 15,509 | 78,365 |
| 1 | Diary 1 | `20220830_Hannah_diary_entries_1.docx` | 30/08/22 | 2,369 | 12,953 |
| 2 | Diary 2 | `20220905_Hannah_diary_entries_2.docx` | 05/09/22 | 2,982 | 15,742 |
| 3 | Follow-up interview 1 | `20220902_Follow_up_1_Hannah.docx` | 02/09/22 | 4,106 | 21,480 |
| 4 | Diary 3 | `20220912_Hannah_diary_ entries_3.docx` | 12/09/22 | 2,752 | 14,590 |
| 5 | Diary 4 | `20220919_Hannah_diary_entries_4.docx` | 19/09/22 | 1,997 | 10,350 |
| 7 | Follow-up interview 2 | `20220908_Follow_up_2_Hannah.docx` | 08/09/22 | 3,291 | 17,987 |
| — | Interview 2 (held out) | `20220921_Interview_2_Hannah.docx` | 21/09/22 | 11,391 | 59,078 |

**Participant totals:** 44,397 words · 230,545 characters · 8 files

---

### Step summaries

#### Interview 1 (Step 0) · Hannah — 15,509 words · 78,365 characters

**Themes:**
- **Household/home:** I’m always shocked when I’m at someone else’s house and I see their shopping and there’s just so much, everything’s in packaging.; Yeah so if, like if we knew that we were going to be meeting up like at our family home we’d say like does anyone want anything from here.
- **Shopping:** So there is both, its in two buildings and in the one I’m in there’s kind of a coffee shop with some sandwiches and salads that are all in plastic.; So there is the opportunity to buy a meal without plastic packaging, at least that you can see.
- **Food/preparation:** No, I think the only engagement I would have with plastic at work is through what I eat and drink.; So there is the opportunity to buy a meal without plastic packaging, at least that you can see.
- **Plastic packaging:** So there’s company, I can’t think of the word, there’s things about trying to be green and be green by design, but I think that’s more of a wider carbon thing t; Yeah I think through my work I don’t really have a lot of scope to control plastic that’s used.
- **Disposal/recycling:** So she’s always been trying to reduce packaging, definitely reduce food waste and just do whatever she can basically.; I think, because if you’re, yeah I think it would have been at first because supermarkets are open generally wider hours than independent and zero waste shops.
- **Reuse:** When I was, so she would, she would buy loose fruit and veg and she would take Tupperware to the butchers in the village, possibly to the cheese counter in Wait; We definitely thought it was a bit weird that my mum was taking Tupperware, like we would have thought it was slightly embarrassing.
- **Routines:** Yeah, so my name is Hannah [pseudonym], I am a [xxx] that works for a[x] on [x] design.; I like running, that’s how I spend most of my non work time.

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

---

#### Diary 1 (Step 1) — 2,369 words · 12,953 characters

**Themes:**
- On holiday - for context, we (my partner [x] and I) got an overnight bus to Cologne from London Victoria on Thursday 18th. Germany offered a ticket for 9 euros the covered all travel expect fast train
- To make eating/drinking on the go less wasteful we had with us two keep cups (one squashable), two tupperwares that we'd had pasta in for dinner before the bus (one squashable), a small square tupperw
- Breakfast at parents house: homemade bread, homemade hummus.
- Vegan marg - plastic tub with foil lid. Some vegan cheese that came as a block in plastic. This was from a vegan section of the fridge in the supermarket. Large selection of fake meats and cheeses. Al
- Coffee from aluminium Nespresso pod.

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

---

#### Diary 2 (Step 2) — 2,982 words · 15,742 characters

**Themes:**
- Week 2 – Hannah's diary entries

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

---

#### Follow-up interview 1 (Step 3) · Hannah — 4,106 words · 21,480 characters

**Themes:**
- 2022-09-02 – Follow up 1 – Hannah
- Eating on-the-go requires more thought
- Conversation started prior to recording took place...
- [before recording, Hannah had mentioned whilst she was away last week, she feels that every decision that she made, in terms of the meals that she was having required more thought compared to being at
- Yeah, I guess, because I was starting from scratch with each meal...because I was on holiday, and also moving almost every day, travelling through Germany and into Austria, we didn’t have a cupboard w
- ...Yeah, so I was saying, it felt like there was more to say because there was something to think about with each meal whereas when I’m at home, well I’m not really at home, I’m staying with my sister
- Hannah mentioned in her diary entry that she and her partner had made a number of preparations before she went travelling. For instance, going to a zero-waste shop to re-fill hand sanitizers. Intervie
- I had lots of small travel, the kind of toiletries that you get from hotels. I don’t know why I had some many but yeah moving house, I was trying to declutter a bit before packing things away into box

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

**Questions asked:** See [Follow-up interview 1 (Step 3)](#follow-up-interview-1-step-3-hannah) below.

---

#### Diary 3 (Step 4) — 2,752 words · 14,590 characters

**Themes:**
- Week 3 – Hannah's diary entries

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

---

#### Diary 4 (Step 5) — 1,997 words · 10,350 characters

**Themes:**
- Week 4 - Hannah's diary entries

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

---

#### Follow-up interview 2 (Step 7) · Hannah — 3,291 words · 17,987 characters

**Themes:**
- 2022-09-08 - Follow up 2 – Hannah
- [Interviewer asks Hannah about her experiences around choosing to go without rather than purchase products due to the packaging involved]
- ‘I think I’m just used to it now. And I’m sure I must do it in other parts of life too, if you decide that that’s the way you do things, it just kind of becomes a habit. Like, I guess, when I was firs
- I think there have been times, when I’ve forgotten to take a coffee cup with me, for example, a re-usable coffee cup, then I would just not have one instead of one instead of buying and that’s sort of
- But, with things like filling up water, I just, [pffft], I think the only time I’ve ever paid for bottled water in recent years, is when our water went off in our flat and we didn’t know how long it w
- Mentioned staying over at a friend's house and going to Lidl before going to work and she needed to purchase food for all three meals [breakfast/lunch/evening meal] and mentioned in her entry about fe
- I think it’s because I felt like I didn’t have as much control as I usually have over the way I shop. So, the way you can use less on the go packaging is by making lunch, so not buying lunch at work f
- So, yeah, I guess I made unconventional meal choices [laughs] because I just wanted to reduce the amount of single use plastic, or just single use packaging. Stuff that’s not recyclable or packaging i

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

**Questions asked:** See [Follow-up interview 2 (Step 7)](#follow-up-interview-2-step-7-hannah) below.

---

#### Interview 2 (held out) · Hannah — 11,391 words · 59,078 characters

**Themes:**
- **Household/home:** And it must either, well a lot of its probably flown or alternatively if it is grown in the UK then its probably with a lot of energy, like in a warehouse or so; We weren’t allowed to put glass in bins through our flats.
- **Shopping:** But I think its because although the system is there for us to take it to a supermarket and potentially be recycled, I’m not sure if they are and I’m not sure w; I guess there’s the fact that shops are open like all day, from very early in the morning until very late at night, some of them even 24 hours.
- **Food/preparation:** So whilst its great for like food, like making it available and stuff, I think when it was probably introduced I would have thought that the lifecycle wasn’t th; Its probably not broken down or its going to get eaten by an animal or a bird, that’s not good for them.
- **Plastic packaging:** I mean things like crisp packets, biscuit wrappers, bread bags, yeah any kind of like plastic film.; Or maybe I’d sometimes use the term soft plastic or flyaway plastic.
- **Disposal/recycling:** So whilst its great for like food, like making it available and stuff, I think when it was probably introduced I would have thought that the lifecycle wasn’t th; I just said I think it’s a big contributor to the waste problem we have in the planet at the moment.
- **Reuse:** I mean things like crisp packets, biscuit wrappers, bread bags, yeah any kind of like plastic film.; Here everything goes, I’m in Cardiff at the moment, everything goes in one green bin bag essentially.
- **Routines:** Or maybe I’d sometimes use the term soft plastic or flyaway plastic.; I guess there’s the fact that shops are open like all day, from very early in the morning until very late at night, some of them even 24 hours.

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

**Questions asked:** See [Interview 2 (held out)](#interview-2-held-out-hannah) below.

---

### Interview questions

#### Interview 1 (Step 0) · Hannah

**Household / home / neighbourhood**
- To begin with then would you be able to tell me a little bit about yourself, what it is you do, who you live with?
- Would you be able to tell me your first experiences of using a zero waste shop, both in [x] and where you live curren...

**Food / preparation / shopping / routines**
- Ok. And would you be able to tell me a bit more about that then in terms of the food and drink that you eat? Is this ...
- You mentioned there that you focused largely on food shopping initially. Why was that?
- You mentioned as well there that when you were a student you don’t have the space to buy in bulk. So can you tell me ...
- You mentioned there as well that he’s not so keen on the way his parents shop at the moment. How does this compare to...
- Would you be able to tell me a little bit more about your diet? So you’ve mentioned there that you’re a vegan, how lo...
- Would you be able to tell me a little bit more about cooking in bulk then and then portioning the meals out. Is there...
- Could you tell me a little bit more about your routines then and what you tend to eat meal wise. Perhaps if we take t...
- When you mentioned as well that you would tend to cook in bulk and it could be maybe four or eight portions and then ...

**Disposal / recycling / packaging**
- I see and as part of your role there does plastic play a role there at all?
- Do you maybe not engage with plastic at all then as part of your role?
- You mentioned your mum there who made the decision to collect all of the single use plastic within given year. Was th...
- I see, so there’s no duplicates then in terms of having say one full container, like a kilner jar for pasta and the a...
- When you say compostable packaging can you tell me a little bit about that?
- Whereabouts do you store the vegetable peelings then and the compostable packaging then in between visits to your par...

**Broader context**
- Ok. So you mentioned there that you’re a [xxx]. Would you be able to tell me then a little bit more about what your w...
- Would you be able to tell me a bit more about that, about how it plays a big part in it?
- Is that something you would do quite often there? You just mentioned with your sister that she would bring some noodl...
- You mentioned as well that you were more aware but its not something that you felt like you could do. What is it exac...
- Was it important for you then to try and kind of maintain the consistency there in terms of what you were doing already?
- Can you tell me a little bit more about that, about your initial thoughts there of taking Tupperware in as something ...
- You mentioned there using the bread bags and the bagel bags, is that for any specific reason why you use those?
- Is that what you mean when you say approve of?
- How long ago was that? Was that something fairly recent or?

---

#### Interview 2 (held out) · Hannah

**Diary callbacks (where applicable)**

**Food / preparation / shopping / routines**
- Is there a reason then why you only kind of visit refill or zero waste shops with your containers to fill up then? Is...
- What do you think about the idea of more biodegradable packaging being introduced for food packaging?

**Disposal / recycling / packaging**
- Just out of curiosity you mentioned there that you would have to take your glass separately to a different collection...
- Packaging that’s labelled as biodegradable is that?
- What have you done then in that instance with packaging?
- Yeah. And so you mentioned there when referring to the sandwich packaging that it was perhaps like a traditional pack...
- Ok. And so how were they disposed of then?
- Does that bottle then go into the bag as it was sold in terms of all packaging there or does anything else happen in ...
- Yeah, so what, how would you define soft plastic then?

**Broader context**
- Ok. And I know we’ve had various discussions as well throughout the follow ups we’ve had but also referring back to f...
- Would you or how do you categorise these types of materials now knowing that they can be I guess collected and?
- Yeah, ok. And before I move onto the next point I wanted to ask you, so you mentioned there when we were talking abou...
- Yeah, ok. And I know you mentioned as well that you’re moving around quite a bit, but how about when were living in y...
- With the window was that?
- Did you mention it at all?
- Ok. So moving on to your entry for 9th September, so you mentioned here that when you would travel up to your partner...
- Ok. And moving on to your entry now for 17th September. So you mentioned, I think at this point you had moved back to...

---

#### Follow-up 1 (Step 3) · Hannah

**Diary callbacks / photo-elicitation**
- Has participation changed how you notice packaging?
- Walk through key diary photos from this period. *(diary callback)*
- Tell me about meals or shopping moments flagged in the diary. *(diary callback)*
- What happened to the packaging from those items? *(diary callback)*
- How does disposal here compare with home or prior habits?

---

#### Follow-up 2 (Step 7) · Hannah

**Diary callbacks (researcher-led probes)**
- Interviewer asks Hannah about her experiences around choosing to go without rather than purchase products due to the packaging involved] *(diary callback)*
- diary entry for 31st August] *(diary callback)*
- Interviewer asks Hannah about how her diet/meal choices compare when she is on-the-go compared to when she is at home] *(diary callback)*
- Interviewer asks about Hannah’s experience of having ‘failed’ if she purchases food in single-use packaging] *(diary callback)*
- Interviewer asks if there was someone in particular that she did want to set an example for, reflecting back on the situation we’ve just discussed] *(diary callback)*
- Hannah then briefly talks about recording her diary entries and how whilst she hasn’t done it yet, ‘these cupboards [in the kitchen] will be very different’ from her sister’s. ] *(diary callback)*
- Her diary entry includes photographs of her sister’s kitchen cupboards and Hannah mentions how  sister shares similar beliefs and values to her, regarding the amount of foods that  *(diary callback)*
- Interviewer asks about whether there’s a designated place where the containers are stored when they are not in use] *(diary callback)*
- Interviewer asks about the practicalities of using bagel bags as containers to fill up her pasta etc.] *(diary callback)*
- I think it’s easier with two people, yeah I think, [reflecting back] did I fill a bag this time? No, I filled a bag of couscous, but it wasn’t from a- [dispenser]. It wasn’t above, *(diary callback)*
- Interviewer prompts Hannah to talk about her experience in relation to the ‘community aspect’ that she referred to in her latest diary entry]. *(diary callback)*
- Interviewer asks Hannah what her thoughts are on compostable packaging] *(diary callback)*

---

### Behavioral lens summary across steps

| Step | Primary lenses |
|------|----------------|
| Interview 1 (Step 0) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |
| Diary 1 (Step 1) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |
| Diary 2 (Step 2) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |
| Follow-up interview 1 (Step 3) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |
| Diary 3 (Step 4) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |
| Diary 4 (Step 5) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |
| Follow-up interview 2 (Step 7) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |
| Interview 2 (held out) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |

---

## Phase 3 · Extend

### Naomi (Phase 3 · Extend)

**Profile:** Lives alone in a rural Lancashire village bungalow, adapted for wheelchair use. Assistance dog (springer spaniel). Disabled, does not work; active social life (Meet Up group, pub games nights, Lake District trips). Shops mainly at Asda using a basket on her knee (no carrier bags).

### Data order and volume

| Step | Calibration step | File | Date prefix | Words | Characters | Notes |
|------|------------------|------|-------------|-------|------------|-------|
| 0 | Interview 1 | `20211108_Interview_1_Naomi.docx` | 20211108 | 11,636 | 57,705 | |
| 1 | Diary 1 | `20211109_Naomi_diary_entries_1.docx` | 20211109 | 2,178 | 11,328 | |
| 2 | Diary 2 | `20211116_Naomi_ diary_entries_2.docx` | 20211116 | 2,053 | 10,672 | Space in filename |
| 3 | Follow-up 1 | `20211122_Follow_up_1_Naomi.docx` | 20211122 | 5,193 | 26,083 | Conducted after Diary 2 (holiday week) |
| 4 | Diary 3 | `20211123_Naomi_diary_entries_3.docx` | 20211123 | 2,115 | 10,941 | |
| 5 | Diary 4 | `20211130_Naomi_diary_entries_4.docx` | 20211130 | 2,122 | 11,071 | |
| 7 | Follow-up 2 | `20211210_Follow_up_2_Naomi.docx` | 20211210 | 2,001 | 10,783 | Researcher notes format |
| — | Interview 2 (held out) | `20220110_Interview_2_Naomi.docx` | 20220110 | 15,024 | 75,674 | |

**Participant totals:** 42,322 words · 214,257 characters · 8 files

---

### Step summaries

#### Interview 1 (Step 0) · Naomi — 11,636 words · 57,705 characters

**Themes:**
- **Household/home:** Semidetached adapted bungalow on quiet cul-de-sac; no village shop (3-mile drive to supermarket); strong community spirit, two village pubs.
- **Routines:** Daily dog walks (1–3×/day), weekly Lakes trips, Tuesday pub games night via Meet Up app; most days merge together as she does not work; rests frequently.
- **Shopping:** Weekly Asda shop (occasional Aldi, Co-op, farm shop); uses kept Asda basket on knee due to wheelchair + assistance dog; online shopping uneconomical alone (minimum order surcharge).
- **Food/preparation:** Eats healthily from fresh ingredients; adapted rise-and-fall cooker/sink; bulk-freezes vegetables in takeaway tubs; detailed fridge/freezer organisation; dysphagia affects food choices.
- **Plastic packaging:** Strong frustration with pre-packed ham, grape/tomato tubs, film lids; prefers paper bags and deli counters; horrified by packaging volume; sister sells catering disposables (conflict).
- **Disposal/recycling:** Morrisons basket under cooker for recycling staging; three council boxes (plastic/metal ×2, paper); council empties from drive; labels guide decisions.
- **Reuse:** Kilner jars for pasta; takeaway tubs for freezing veg/meat; dog food bags reused for garden waste.
- **Lockdown:** Sister shopped for her during shielding; healthier eating then, weight regain after; secretly ordered 48 Mars bars via Amazon.

**Behavioral lenses:** Identity (disabled independent shopper, environmentally conscious), Culture/social (village community, farming background referenced later), Pricing/value (online minimum order, switched dog food brand for cost), Convenience tradeoff (frozen pre-cut veg), Recycling diligence (label-checking, council collection), Reuse tendency (jars, tubs, basket), Food waste sensitivity (smaller packs for living alone), Attitude-behavior gap (wants less plastic, limited alternatives).

---

#### Diary 1 (Step 1) — 2,178 words · 11,328 characters

**Themes:**
- Use-up week: no main shop planned; saving money; medication blister pack waste noted.
- Detailed meal-by-meal packaging audit: ham film not recyclable, pasta cardboard with plastic window, clingfilm for leftovers.
- Family takeaway night: cooks own jerk chicken while others order Indian; microwave rice pouches despite annoyance (cannot lift boiling pans safely).
- Pub cake takeaway: greasy cardboard not recyclable per council rules.
- Pizza/garlic bread evening with friend; multipack chocolate wrapper frustration.
- Impulse Co-op shop (5 for £5 freezer fillers) when short on time.
- Closing reflection: wishes for deli counters, own containers, bigger pack sizes; basket shopping constraint.

**Behavioral lenses:** Pricing/value (use-up week, Co-op deal), Occasion (family takeaway, friend pizza night, pub cake), Convenience tradeoff (microwave rice, ready-sliced onions), Recycling diligence (film vs tray, clean cardboard rule), Reuse tendency (takeaway tubs, basket), Food waste sensitivity (bigger cheese blocks, half rice pouch), Attitude-behavior gap (wants paper bags, buys pre-packed), Culture/social (supermarkets blame consumers).

---

#### Diary 2 (Step 2) — 2,053 words · 10,672 characters

**Themes:**
- Holiday prep: 16 pre-weighed dog food bags in small plastic bags for van trip; medication packed.
- Pub Coke in cans (landlord says draft is less green); landlord permission for photo.
- Quick unhealthy meals when time-pressed: frozen dippers, onion rings.
- Big pre-holiday shop: Malibu stock-up, road-trip treats, dog food pouches; transferred biscuits to reusable container.
- Emotional eating binge (Twix, Fry's) before trip.
- McDonald's breakfast (paper packaging); parents' roast dinner (chicken-in-bag, veg plastic bags).
- Bins emptied early before week away; road trip begins (Premier Inn, hotel meals, serviettes/sachets).

**Behavioral lenses:** Occasion (holiday, McDonald's, parents' dinner, hotel meals), Pricing/value (Malibu offer, Home Bargains mentioned in FU2), Convenience tradeoff (pre-weighed dog portions, frozen convenience tea), Reuse tendency (food clips, biscuit transfer), Recycling diligence (early bin emptying), Food waste sensitivity (steak halved across two nights), Identity (organised holiday prep despite disability).

---

#### Follow-up 1 (Step 3) · Naomi — 5,193 words · 26,083 characters

**Themes:**
- Holiday reflection: far less packaging when eating out; still recycles in van, brings home to household bins.
- **Diary callbacks:** Ham packaging annoyance (producer vs consumer blame); microwave rice convenience vs disability; pasta film window; dirty cardboard recycling rules; mayo squeezy vs glass hygiene; washing containers before recycling; Morrisons basket as recycling staging; steak tray plastic layers.
- Shopping route optimisation in Asda basket (soft items protected, bread last).
- Kilner jar storage for pasta/spaghetti (mite prevention, internet article).
- Photo-elicitation of fridge, recycling basket, steak packaging, shopping.

**Questions asked:** See [Follow-up 1 questions](#follow-up-1-step-3-naomi) below.

**Behavioral lenses:** Occasion (holiday eating patterns), Culture/social (supermarkets save money, blame consumers), Convenience tradeoff (rice pouches, squeezy mayo), Recycling diligence (wash-before-recycle, council website, greasy cardboard), Reuse tendency (kilner jars, own containers aspiration), Attitude-behavior gap (wants paper, system prevents it), Identity (disability shapes kitchen safety).

---

#### Diary 3 (Step 3) — 2,115 words · 10,941 characters

**Themes:**
- Inverness hotel week: large breakfasts, meal deals, sachets (vinegar, mayo, ketchup, butter, jam).
- Dog won't eat dry food at hotel; tricks him with "treats" from pre-weighed bags; extra plastic bags for smell.
- Christmas shopping; pub condiment sachet frustration (plans to ask landlord about pots).
- Drive home (7 hours): road snacks, Wotsits, individually wrapped sweets; Lancaster restaurant stop.
- Post-holiday exhaustion: PJ day, pub burger, chocolate binge, frozen pizza.
- Recovery meals: sausage/mash from freezer tubs; wine poured away (too old).

**Behavioral lenses:** Occasion (hotel holiday, Christmas shopping, pub meals, drive snacks), Convenience tradeoff (hotel sachets, frozen pizza when exhausted), Recycling diligence (water bottle recycled, greasy cake box binned), Reuse tendency (takeaway tubs for sausage), Food waste sensitivity (wine discarded), Attitude-behavior gap (wants pot condiments, receives sachets).

---

#### Diary 4 (Step 4) — 2,122 words · 11,071 characters

**Themes:**
- Family funeral livestream; parents' spread (packaging not discussed).
- Games night pub; weight gain post-holiday (5 lbs); nachos/tea when tired.
- Date night at gastropub (minimal packaging, ceramic/metal serving).
- McDonald's drive-through (paper/cardboard mostly recyclable).
- Friend visit: roast at pub (paper salt/pepper sachets; plans sustainability chat with manager).
- Ferrero Rocher: foil-paper cases burned on open fire; foil recycled.
- Spaghetti bolognese from freezer tub; clingfilm for leftovers; Christmas stock-up shop with photos.

**Behavioral lenses:** Occasion (funeral, date, family birthday meal, pub Sunday dinner, games night), Identity (trying to lose weight), Recycling diligence (McDonald's cup rinsed, film lids binned), Reuse tendency (freezer tubs, Parmesan pre-grated and frozen), Culture/social (pub landlord relationship, family traditions), Food waste sensitivity (clingfilm leftovers for easy tea).

---

#### Follow-up 2 (Step 7) · Naomi — 2,001 words · 10,783 characters

**Themes (researcher notes + participant quotes):**
- Dog food portioning in plastic bags for travel (no room for tubs in van with wheelchairs).
- Washing tins/bottles before recycling; timing around cooking/photography for study.
- Clingfilm over leftovers for microwave convenience.
- Roast chicken-in-bag at parents': farming family, no waste, soup from carcass.
- Leftovers culture vs brother-in-law who won't reheat.
- Biscuits/cheese-onion rolls transferred to reusable containers to avoid van mess.
- Holiday checklist on phone (bins, recycling, dog food, pack case).
- Asda shopping list app; separate Home Bargains trip for road-trip sweets.
- Co-op for nachos/salsa/guacamole; 5 for £5 freezer fillers.
- Overstocking tendency reinforced by lockdown shielding (sister got COVID, couldn't shop).
- Hot chocolate sachets for Premier Inn breakfasts; travel cup vs bottled water on A9.

**Questions asked:** See [Follow-up 2 questions](#follow-up-2-step-7-naomi) below.

**Behavioral lenses:** Pricing/value (Home Bargains, Co-op deals, overstocking), Occasion (holiday prep, road trip), Reuse tendency (containers for flaky foods), Food waste sensitivity (farming family no-waste ethos), Recycling diligence (wash ritual), Identity (organised lists, memory support), Culture/social (family leftover norms).

---

#### Interview 2 (Step — held out) — 15,024 words · 75,674 characters

**Themes:**
- Life history: lifelong village resident (minus university years), agricultural college, equestrian career, own riding school 1999–2013.
- Functional neurological disorder and fibromyalgia: impacts cooking (one-pan meals, ready meals on bad days), shopping (Asda dog walks in extreme weather), rest-heavy routine.
- Recycling infrastructure: fortnightly collections; neighbours at Sunderland Point lack doorstep recycling; comparison to farm years (fought for grey bin, no green bin).
- **Christmas deep-dive:** Eve with friend, sister's lunch (agony, presents opened for her), New Year family meal (parents had COVID); extra ready-meal packaging from helpers; chocolate/biscuit packaging.
- **Diary callbacks:** Dog sachets at hotel; Christmas food gifts packaging; hotel breakfast sachets; pub garlic mayo in pot (positive); post-holiday exhaustion; tea cake foil-window box; medication blister packs; Ferrero Rocher on fire; week-4 shop photos with dog.
- Friends/sister shopped for her during sciatica; ready meals on list when unable to cook.

**Questions asked:** See [Interview 2 questions](#interview-2-held-out-naomi) below.

**Behavioral lenses:** Identity (disabled, farming roots, organised shopper), Occasion (Christmas traditions, hotel holiday), Culture/social (family food roles, producer responsibility), Convenience tradeoff (ready meals when unwell), Recycling diligence (fire for confidential/mixed materials), Reuse tendency (phone shopping lists), Food waste sensitivity (mum takes near-expiry food), Attitude-behavior gap (recycling vs blister packs to bin).

---

### Interview questions

#### Interview 1 (Step 0) · Naomi

**Household / home / neighbourhood**
- Tell me about yourself, your family, and what you like to do.
- How often do you visit the Lakes? What other hobbies do you have?
- Walk me through a typical week (e.g. last week).
- How does your midweek routine compare to weekends?
- Describe where you live: the house, street, and neighbourhood.
- When did the village shop close? How far do you travel for food?

**Food / preparation / shopping / routines**
- Where do you shop and how do you decide what to buy?
- Do you eat healthily? What did you eat last week?
- What food do you buy for your assistance dog?
- Talk me through bringing the shopping home and putting it away.
- How do you organise your fridge and freezers?
- If your kitchen were a person, how would you describe it?
- Describe your kitchen layout, cupboards, and storage systems.
- Why did you stop keeping vegetables in the cupboard?

**Disposal / recycling / packaging**
- Do you have a kitchen bin? Where does waste go?
- How do you decide what gets recycled?
- How often do you take recycling out, and why before visitors come?
- Where are your council bins kept?
- What comes to mind when you think about plastic food packaging?
- Why do businesses and consumers choose plastic over greener options?
- How do you define plastic food packaging?
- Describe all the packaging your food comes in and what happens to each type when you get home.

**Broader context**
- Has your relationship with food changed over the past 12 months?
- How did lockdown and your sister shopping for you affect your eating habits?
- Why is online shopping difficult when living alone?

---

#### Interview 2 (held out) · Naomi

**Life history / identity**
- How long have you lived in the village? Tell me about your education and career.
- Explain your functional neurological disorder and how it affects daily life.
- How does disability impact cooking, shopping, and kitchen use?
- Describe your rest-heavy daily routine and fibromyalgia.

**Disposal / recycling**
- How often are your bins collected? Does everyone on the street have the same setup?
- How do Sunderland Point residents handle recycling?
- How does your current bin setup compare to your previous farm and earlier homes?
- Did neighbouring farms recycle when you lived on the farm?

**Christmas / occasions**
- Where did you spend Christmas and was there travel involved?
- Is Christmas Eve with your friend an annual tradition?
- Tell me about preparing chocolate puddings for Christmas.
- What does Christmas mean to you and what are your traditions?
- What presents do you buy for your dog?
- What happened in the kitchen around Christmas dinner (packaging, cleanup)?

**Diary callbacks (weeks 3–4)**
- Why did you buy dog meat sachets and how does the packaging compare to dry food?
- Which hotel bin did you use for dog food waste?
- Tell me about Christmas food gifts you bought and how they were packaged.
- What happens to gift-wrapping paper after presents are opened?
- What happened to hotel breakfast/dinner packaging (butter, jam, sachets)?
- You wished pubs served condiments in pots rather than sachets — tell me more.
- Describe your exhausted PJ day after the drive home.
- Tell me about the tea cake box with recyclable plastic window.
- Why did you pour wine down the sink? Any other post-holiday food waste?
- What does "putting out medication in tubs" involve?
- Why do you burn some packaging on the open fire (Ferrero Rocher, medication boxes)?
- Does everything on your week-4 shop table fit in your basket?
- When friends or family shop for you, how does that work?

---

#### Follow-up 1 (Step 3) · Naomi

**Holiday / routines**
- Did you have a nice break? How does eating away differ from home?
- Do your recycling habits change when you are out and about?

**Diary callbacks — week 1**
- Why were you annoyed about pre-packed ham and not being able to buy loose? *(diary callback)*
- How would you prefer to buy grapes? Why paper over plastic?
- Do you follow a set route around Asda?
- Why do you use microwave rice pouches despite the plastic? *(diary callback)*
- Why is the pasta box plastic window annoying? Why transfer to kilner jars?
- Why couldn't the greasy cake box be recycled? Could it have been cleaned?
- Why the soup carton couldn't be recycled after microwaving.
- Why squeezy mayo over glass (hygiene with guests)?

**Diary callbacks — week 2**
- Why did you wash out the soured cream bottle before recycling?
- Are you happy with your under-counter recycling basket setup?
- Tell me about the steak packaging (cardboard tray + plastic layers). *(photo callback)*

---

#### Follow-up 2 (Step 7) · Naomi

**Diary callbacks (researcher-led probes)**
- Why weigh dog food into small plastic bags for holiday rather than tubs?
- When and why do you wash packaging before recycling?
- Why store leftover mash in a bowl with clingfilm? Do you microwave through clingfilm?
- What happened to the roast chicken packaging at your parents'?
- How were you taught about food waste growing up on a farm?
- Why transfer biscuits and cheese-onion rolls to reusable containers for the road trip?
- Tell me about your pre-holiday checklist (bins, recycling, packing).
- How does your phone shopping list work? Do you deviate for holiday stock-ups?
- Why shop at Co-op and Home Bargains separately from Asda?
- Tell me about overstocking, especially after lockdown shielding.
- Why take hot chocolate sachets and a travel cup to Premier Inn?

---

### Behavioral lens summary across steps

| Step | Primary lenses |
|------|----------------|
| Interview 1 | Identity, Recycling diligence, Attitude-behavior gap, Convenience tradeoff, Pricing/value |
| Diary 1 | Pricing/value, Convenience tradeoff, Recycling diligence, Occasion, Attitude-behavior gap |
| Diary 2 | Occasion, Convenience tradeoff, Food waste sensitivity, Reuse tendency |
| Follow-up 1 | Culture/social, Convenience tradeoff, Recycling diligence, Attitude-behavior gap |
| Diary 3 | Occasion, Convenience tradeoff, Attitude-behavior gap |
| Diary 4 | Occasion, Recycling diligence, Reuse tendency, Culture/social |
| Follow-up 2 | Pricing/value, Food waste sensitivity, Identity, Reuse tendency |
| Interview 2 | Identity, Occasion, Culture/social, Convenience tradeoff, Recycling diligence |

---

---

### Sophia (Phase 3 · Extend)

**Profile:** Part-time home worker; husband at university; eight-year-old son and puppy. Running family (parkrun, football); son has school lunches four days; lockdown improved shared evening meals.

### Data order and volume

| Step | Calibration step | File | Date | Words | Characters |
|------|------------------|------|------|-------|------------|
| 0 | Interview 1 | `20220113_Interview_1_Sophia.docx` | 13/01/22 | 13,007 | 66,747 |
| 1 | Diary 1 | `20220118_diary_entries_1_Sophia.docx` | 18/01/22 | 535 | 3,059 |
| 2 | Diary 2 | `20220124_diary_entries_2_Sophia.docx` | 24/01/22 | 1,920 | 10,234 |
| 3 | Follow-up interview 1 | `20220127_Follow_up_1_Sophia.docx` | 27/01/22 | 1,438 | 8,342 |
| 4 | Diary 3 | `20220201_diary_entries_3_Sophia.docx` | 01/02/22 | 2,351 | 12,350 |
| 5 | Diary 4 | `20220207_diary_entries_4_Sophia.docx` | 07/02/22 | 1,912 | 9,997 |
| 7 | Follow-up interview 2 | `20220217_Follow_up_2_Sophia.docx` | 17/02/22 | 2,607 | 14,784 |
| — | Interview 2 (held out) | `20220224_Final_Interview_Sophia.docx` | 24/02/22 | 10,343 | 53,409 |

**Participant totals:** 34,113 words · 178,922 characters · 8 files

---

### Step summaries

#### Interview 1 (Step 0) · Sophia — 13,007 words · 66,747 characters

**Themes:**
- **Household/home:** Yeah so live at home, so there’s me, my husband and we’ve got an eight year old son and we now have puppy.; So I work part time but pretty much 99% of it from home.
- **Shopping:** Doesn’t always, now that kind of life’s getting a bit more back to normal [Son's name] has got a few activities after school so there might be the odd day that ; Yeah
 Yeah so I very stupidly, because I normally do my food shopping on Thursday morning.
- **Food/preparation:** So in terms of food and meals, apart from the very abnormality I pretty much eat everything here.; He normally gets breakfast at the university if he’s there and in terms of lunch meals he, if we’ve got leftovers he might take that, if not goodness knows what
- **Plastic packaging:** There’s one day of the week that he doesn’t like the food, so he gets sent with a packed lunch that day but school send him his packaging, so we dispose of that; So that normally stays on the pan while we’re eating in case anyone wants a bit of extras kind of at tea time and then I’ll go and wash everything up and put wh
- **Disposal/recycling:** And likewise even things that come in cardboard packaging like sometimes I will get like a frozen pizza or a frozen garlic bread pizza, I take out of the cardbo; There is also a bit of storage under the bottom shelf, so I will sometimes, depending on upcoming meals and how quickly I think we’re going to go through it, I 
- **Reuse:** He normally gets breakfast at the university if he’s there and in terms of lunch meals he, if we’ve got leftovers he might take that, if not goodness knows what; Normally for lunch either salad or like scrambled egg on toast or leftovers from the night before.
- **Routines:** So I work part time but pretty much 99% of it from home.; [Son's name] is at primary school so has hot lunches four days of the week.

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

---

#### Diary 1 (Step 1) — 535 words · 3,059 characters

**Themes:**
- week one diary entries (Sophia)

**Behavioral lenses:** Occasion, Convenience tradeoff, Recycling diligence, Reuse tendency, Food waste sensitivity, Attitude-behavior gap.

---

#### Diary 2 (Step 2) — 1,920 words · 10,234 characters

**Themes:**
- Week two diary entries (Sophia)
- Monday – 17th January
- Tuesday – 18th January
- Wednesday – 19th January
- Thursday – 20th January
- Friday – 21st January
- Saturday – 22nd January
- Sunday – 23rd January

**Behavioral lenses:** Occasion, Pricing/value, Culture/social, Convenience tradeoff, Recycling diligence, Reuse tendency.

---

#### Follow-up interview 1 (Step 3) · Sophia — 1,438 words · 8,342 characters

**Themes:**
- 2022-01-27 – First follow up with Sophia
- Sophia explained to me that she has been spending some time home-schooling [son's name] this past week as he tested positive for Covid and she mentioned that whilst the school ‘have been fantastic’, [
- Reflecting on recording the diary entries for this study
- [1.30] Sophia explained that ‘it’s made me realise...how much you do eat during the day that you judt don’t think about and how much packaging there is and in some ways it has made me realise...as a f
- Reflecting back on our previous conversation during her first interview, Sophia explained that during the evening they try to eat the same meal, but a part of that they don’t; there are a lot of separ
- Different tastes: Making sure everyone has what they want
- [2.33] ‘My motivation has been making sure everyone has what they want and acknowledges that people have different tastes and want different things’ but on the flipside, she recognises that ‘requires 
- Sophia talks about dislike for sandwiches, explaining that sandwiches tend to be [son's name]’s preference

**Behavioral lenses:** Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence, Reuse tendency.

**Questions asked:** See [Follow-up interview 1 (Step 3)](#follow-up-interview-1-step-3-sophia) below.

---

#### Diary 3 (Step 4) — 2,351 words · 12,350 characters

**Themes:**
- Week 3 diary entries (Sophia)
- Monday – 24th January
- Tuesday – 25th January
- Wednesday - 26th January
- Thursday – 27th January
- Friday – 28th January
- Saturday - 29th January
- Sunday 30th January

**Behavioral lenses:** Occasion, Pricing/value, Culture/social, Convenience tradeoff, Recycling diligence, Reuse tendency.

---

#### Diary 4 (Step 5) — 1,912 words · 9,997 characters

**Themes:**
- Week 4 diary entries (Sophia)
- Monday - 31st January
- Tuesday - 1st February
- Wednesday - 2nd February
- Thursday - 3rd February
- Friday - 4th February
- Saturday- 5th February
- Sunday - 6th February

**Behavioral lenses:** Occasion, Culture/social, Convenience tradeoff, Recycling diligence, Reuse tendency, Food waste sensitivity.

---

#### Follow-up interview 2 (Step 7) · Sophia — 2,607 words · 14,784 characters

**Themes:**
- 2022-02-17 - Second follow up with Sophia
- Reflecting on her involvement in the study
- The following discussion was prompted by me asking Sophia, if she’s had any reflections about the study, now that she has shared the 4th and final set of diary entries with us.
- •	Coordinating ‘convenience’ meals vs. Cooking from scratch
- “Those days when I feel that I haven’t got the energy to kind of cook us all something from scratch, so I make us all something individually, actually that is probably a lot harder work...because I’d 
- [3.49] Sophia talks about what ‘cooking from scratch’ means to her... “pretty much, my go-to family meals for us would be, spaghetti bolognaise, chili with rice, a variety of different pasta bakes wit
- What is the difference between ‘convenience’-based meals and meals that are ‘cooked from scratch’ for Sophia
- Examples of the convenience meals include “breaded chicken burgers’ [5.40], chicken nuggets, chicken kievs, chips and veg, those kind of things.”

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

**Questions asked:** See [Follow-up interview 2 (Step 7)](#follow-up-interview-2-step-7-sophia) below.

---

#### Interview 2 (held out) · Sophia — 10,343 words · 53,409 characters

**Themes:**
- **Household/home:** I find a toy, you know I don’t buy him a new toy, I find something random from round the house.; For picnics, for things I would always try as much as possible to make as much of it from home and kind of use sustainable plastics, drinks bottles, Tupperwares
- **Shopping:** I normally do my food shop on a Thursday morning.; So normally on a Wednesday evening when I’m going through and making the shopping list of what we actually need I do try and do a rough plan of what we’re going
- **Food/preparation:** So normally on a Wednesday evening when I’m going through and making the shopping list of what we actually need I do try and do a rough plan of what we’re going; So kind of next to my shopping list will write the days of the week and try and correlate that with a meal.
- **Plastic packaging:** Know where things are, know what the packaging looks like, what I normally pick and kind of pick it up without really thinking and without really looking whethe; Yeah, like I say we are quite conscious and I think as well now we’ve got [dog's name] in terms of out walking I think that also makes you see again how much pl
- **Disposal/recycling:** Yeah, like I say we are quite conscious and I think as well now we’ve got [dog's name] in terms of out walking I think that also makes you see again how much pl; But this morning even I was just thinking like cereal, its in the plastic wrap, but then its in a cardboard box.
- **Reuse:** And if it was something like a spaghetti Bolognese and the mince was in the fridge I’d then just check the date on it and if I wasn’t going to be able to use it; So sometimes when I’m doing him a fakeaway I’ll go the whole hog, I will get him a brown paper bag that’s got McDonalds sign kind of drawn and coloured in on it
- **Routines:** I normally do my food shop on a Thursday morning.; So normally on a Wednesday evening when I’m going through and making the shopping list of what we actually need I do try and do a rough plan of what we’re going

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

**Questions asked:** See [Interview 2 (held out)](#interview-2-held-out-sophia) below.

---

### Interview questions

#### Interview 1 (Step 0) · Sophia

**Household / home / neighbourhood**
- Can you tell me a little bit more about what you like to do in your spare time? Yourself as a family?
- Ok. And you mentioned there that, earlier that the school sends [Son's name] home with the packaging. Are there any o...

**Food / preparation / shopping / routines**
- You mentioned that you tend to then have your lunches here obviously. So what types of foods do you tend to have for ...
- Can you tell me then what these meals tend to be, we’re on Thursday now, maybe just take this week as an example?
- What about the potatoes then as well? So you have two different types of potatoes, you have the mash that you buy rea...
- Would it be easier to go back and talk about the meals you’ve just had Monday, Tuesday, Wednesday?
- Is there much cooking involved there with these types of meals that you’re having?
- What happens then? So after you’ve eaten, so maybe once you’ve kind of got your meals that you’re going to be eating ...
- Would you be able to tell me a little bit more about the kitchen then? You say you’ve been here for about seven or ei...
- Yeah, so what other types of things then do you tend to have in the freezer? So you’ve mentioned that you’ve got the ...
- Right ok. And you mentioned earlier when you were talking about the types of meals that you have, you mentioned that ...
- And you mentioned before then so he tends to have hot dinners four days a week and then one day he’ll go in with a pa...
- Ok. And you mentioned before that you tend to do your main food shop on a Thursday morning first thing. And that you ...

**Disposal / recycling / packaging**
- Is there any particular reason for that, that combination of between the fresh and the frozen?

**Broader context**
- And so you mentioned there that you work part time as well. So what kind of days is that?
- Ok. And when you say a salad then is that, could you tell me a bit more about that?
- When you say a bit of a snack what does this tend to be?
- Can you tell me more about kind of the importance of running, of exercise and what it means I guess?
- What do you mean by that exactly?
- When you say laziness, what do you mean there?
- And can you tell me a little bit more about that, for example the pesto then, so you’ve got the pesto pasta, so how i...
- You mentioned earlier as well that sometimes you’ll have leftovers that you’ll have or is it [husband's name]?
- Ok. Just moving on slightly then, so could you, I mean its probably strange because I’m here but could you tell me a ...
- Ok. And can you tell me a little bit more about the appliances that you’ve got? What you use?
- Yeah, would you be able to tell me a bit about that?

---

#### Interview 2 (held out) · Sophia

**Diary callbacks (where applicable)**

**Household / home / neighbourhood**
- Ok. Moving on to the Monday now then, so on 31st you mentioned that you made a moussaka for tea with mince, mushrooms...

**Food / preparation / shopping / routines**
- Ok. And moving on to food shopping now. It’s a shame I wasn’t able to go with you but I was wondering whilst you are ...
- Ok. And just when you’re buying as well, particular items that are already on your list, is there anything there that...
- Ok. And kind of coming away from kind of meals now. I just wanted to ask you about when you think about plastic and p...
- What’s convenient then about Aldi?
- Ok. And just thinking I guess outside of maybe the food shopping situation, if somebody presented you with the same p...
- Right I see. That was something I was going to come back to actually because you mentioned in week four actually abou...
- Ok. And you mentioned just then about you wanting it to be a treat for everybody and you used inverted commas, what d...
- When you say deemed good there for each meal are there any, is there anything that’s kind of helping you come to that...
- And there was nothing on it at all, it was just kind of going in the fridge as it is?

**Disposal / recycling / packaging**
- Ok. And actually just thinking about, so you’re talking about the packaging there as well from the kind of fakeaway M...
- Ok. And you mentioned there that there is a lot of unnecessary and excessive packaging as well, plastic packaging. Co...
- You say just there then obviously with the Coke you would dispose of them after one use, is there any reason for that?
- Just thinking about the environmental kind of impact then of packaging, how do they compare then in terms of packagin...

**Broader context**
- And you mentioned just then about when you’re kind of sat down on Wednesday evenings and you’re thinking about the we...
- Ok. And going back to your first interview again, so you mentioned that at one point when we were talking about the t...
- Is there any particular reason why these are your staples?
- And when you were talking about kind of on days where you go out and you mentioned there that you like to use, or you...
- Right and I know again we’ve talked probably about this a couple of times but this is a question that I wanted to ask...
- Right, so what is it then?
- I can’t see a number though, can you see a number?
- What happened then, I mean you mentioned there that it would have involved cutting up the chicken, what happened then...
- Yeah. And will you take those on the walks with you?
- What kind of size bags are these that you would take, are they a lot smaller then?
- No, ok. And on this same day, so this is the day that you ordered a takeaway and you mentioned here that [Son's name]...
- The popcorn. The small bags of popcorn. You also mentioned like yourself having Greek yoghurt, hot chocolate, small b...
- Yeah. And is it just you then that has this vanilla protein?
- Oh right, ok. But you both have the protein scoops?

---

#### Follow-up 1 (Step 3) · Sophia

**Diary callbacks / photo-elicitation**
- Has participation changed how you notice packaging?
- Walk through key diary photos from this period. *(diary callback)*
- Tell me about meals or shopping moments flagged in the diary. *(diary callback)*
- What happened to the packaging from those items? *(diary callback)*
- How does disposal here compare with home or prior habits?

---

#### Follow-up 2 (Step 7) · Sophia

**Diary callbacks (researcher-led probes)**
- Sophia talks about what ‘cooking from scratch’ means to her... “pretty much, my go-to family meals for us would be, spaghetti bolognaise, chili with rice, a variety of different pa *(diary callback)*
- “In terms of convenience foods...with chicken kievs, [husband's name]s and [son's name] will eat the same...but then it’s slightly different convenience foods for [husband's name]  *(diary callback)*
- Sophia also talked about how she has changed the way she approaches lunch times (as the person who predominantly prepares meals in her home). She mentions how she has “always just  *(diary callback)*
- Sophia talks about the food she purchases on a regular basis and ‘knowing’ whether these are recyclable or not, this ‘knowing’ has formed a part of her habit. *(diary callback)*
- ‏Why wash and rinse? Sophia mentions that her ‘mum told [her] to’ - she explains that this is something that, reflecting back on when ‘recycling proper kicked off’ that ‘it has jus *(diary callback)*

---

### Behavioral lens summary across steps

| Step | Primary lenses |
|------|----------------|
| Interview 1 (Step 0) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |
| Diary 1 (Step 1) | Occasion, Convenience tradeoff, Recycling diligence, Reuse tendency, Food waste sensitivity |
| Diary 2 (Step 2) | Occasion, Pricing/value, Culture/social, Convenience tradeoff, Recycling diligence |
| Follow-up interview 1 (Step 3) | Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence |
| Diary 3 (Step 4) | Occasion, Pricing/value, Culture/social, Convenience tradeoff, Recycling diligence |
| Diary 4 (Step 5) | Occasion, Culture/social, Convenience tradeoff, Recycling diligence, Reuse tendency |
| Follow-up interview 2 (Step 7) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |
| Interview 2 (held out) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |

---

### Katie (Phase 3 · Extend)

**Profile:** 28; environmental health technical officer + part-time school role; lives with partner in small semidetached (no kitchen bin, dishwasher instead). Masters in environmental pollution; Brita filter vs tap water tension; cycles when possible.

### Data order and volume

| Step | Calibration step | File | Date | Words | Characters |
|------|------------------|------|------|-------|------------|
| 0 | Interview 1 | `20220117_Interview_1_Katie.docx` | 17/01/22 | 15,867 | 80,612 |
| 1 | Diary 1 | `20220120_diary_entries_1_Katie.docx` | 20/01/22 | 569 | 3,281 |
| 2 | Diary 2 | `20220126_diary_entries_2_Katie.docx` | 26/01/22 | 621 | 3,393 |
| 3 | Follow-up interview 1 | `20220125_Follow_up_1_Katie.docx` | 25/01/22 | 1,517 | 8,627 |
| 4 | Diary 3 | `20220202_diary_entries_3_Katie.docx` | 02/02/22 | 651 | 3,555 |
| 5 | Diary 4 | `20220207_diary_entries_4_Katie.docx` | 07/02/22 | 459 | 2,466 |
| 6 | Diary 5 | `20220224_diary_entries_5_Katie.docx` | 24/02/22 | 670 | 3,720 |
| 7 | Follow-up interview 2 | `20220217_Follow_up_2_Katie.docx` | 17/02/22 | 3,610 | 19,532 |
| — | Interview 2 (held out) | `20220221_Final_Interview_Katie.docx` | 21/02/22 | 10,873 | 55,839 |

**Participant totals:** 34,837 words · 181,025 characters · 9 files

---

### Step summaries

#### Interview 1 (Step 0) · Katie — 15,867 words · 80,612 characters

**Themes:**
- **Household/home:** What sort of detail do you need to know about where we live?; So [partner's name] my partner, its his house, he bought it.
- **Shopping:** Ideally I’d love to live off grid in a rural place but in reality I do buy plastic and I do drive a diesel car.; And then like I’d like to buy locally sourced food and avoid all the plastic packaging that comes with the supermarket food and that kind of thing but then its 
- **Food/preparation:** So I’d like to eat organic but I can’t always afford it.; But I did get my mum and dad an allotment and I did used to eat their food for as long as they had that but they don’t have it anymore sadly.
- **Plastic packaging:** And not use as much plastic and that kind of thing.; Ideally I’d love to live off grid in a rural place but in reality I do buy plastic and I do drive a diesel car.
- **Disposal/recycling:** We sort of have a bin bag on the door and we just have to keep taking that out every day.; It was either a bin in the cupboard or a dishwasher and we went with the dishwasher.
- **Reuse:** We sort of have a bin bag on the door and we just have to keep taking that out every day.; Well like Actimel or when you’re buying vegetables and they put them in unnecessary plastic bags and things.
- **Routines:** We sort of have a bin bag on the door and we just have to keep taking that out every day.; I work for the [x] and also at the [x] part time.

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

---

#### Diary 1 (Step 1) — 569 words · 3,281 characters

**Themes:**
- Taking part in this study has caused me to become quite aware of the plastic in my life. It’s everywhere! I always knew we were too reliant on plastic as a society but I am realising how ubiquitous pl
- I received a Tassimo coffee maker for Christmas from my boyfriend. I’d never invested in one myself before as I didn’t feel I needed one (I’m quite happy with instant coffee and my kettle), and I am a
- Tassimo coffee machine received as a Christmas present.

**Behavioral lenses:** Occasion, Pricing/value, Identity, Convenience tradeoff, Recycling diligence, Reuse tendency.

---

#### Diary 2 (Step 2) — 621 words · 3,393 characters

**Themes:**
- Went to the shop for cat food, water, and lunch.
- For the cat I got the Gourmet mousses (left of photo below). Each portion comes in a little white plastic pot. The food I usually get her comes in tins.
- The bottle of water I bought was a plastic 2L bottle.
- For lunch I picked up some bananas for my smoothie, plus a pot noodle as I just fancied one. However when I got home, I realised I had no other ingredients for my smoothie so just had the pot noodle.

**Behavioral lenses:** Occasion, Pricing/value, Identity, Convenience tradeoff, Recycling diligence, Reuse tendency.

---

#### Follow-up interview 1 (Step 3) · Katie — 1,517 words · 8,627 characters

**Themes:**
- 2022-01-25 – First follow up with Katie
- Reflecting on writing the diary entries – mentions that she sometimes forgets to record something that she thinks would be useful to include within her entries, only realising once she has gone to bed
- Refers to ‘making mental notes and thinking about plastic a lot more’ and makes a reference to unnecessary plastic at the supermarket. She mentions that she feels a ‘bit more guilty but still buy it a
- Gives an example of a salad bag that she has bought and also mentions that she is ‘trying’ to eat more organic foods too. Along these lines, she mentioned that she doesn't want to buy whole vegetables
- Despite living with her partner and often eating evening meals with him, Katie’s and [boyfriend's name]’s diet and the foods they eat often differ.
- Reflecting on the first interview and her awareness of the volume of plastic food packaging in her life [3.30] - plastics’ ‘disappearance’
- Mentions here that she was talking about the types of foods that she tends to buy that are packaged in plastic, but has since realised that there is a lot more plastic visible....she mentions ‘actuall
- Microwavable rice and stir fry (which is sometimes shop-bought, sometimes ‘made from scratch’ [4.40]

**Behavioral lenses:** Occasion, Identity, Convenience tradeoff, Recycling diligence, Reuse tendency, Food waste sensitivity.

**Questions asked:** See [Follow-up interview 1 (Step 3)](#follow-up-interview-1-step-3-katie) below.

---

#### Diary 3 (Step 4) — 651 words · 3,555 characters

**Themes:**
- Saturday 29th Jan

**Behavioral lenses:** Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence, Reuse tendency.

---

#### Diary 4 (Step 5) — 459 words · 2,466 characters

**Themes:**
- Thursday 3rd Feb
- Saturday 5th Feb

**Behavioral lenses:** Occasion, Culture/social, Convenience tradeoff, Recycling diligence, Reuse tendency, Food waste sensitivity.

---

#### Diary 5 (Step 6) — 670 words · 3,720 characters

**Themes:**
- Breakfast: Weetabix as above. Photo above showing the ingredients and packaging used.
- Lunch: Tinned tomato soup with seeded bread (as above)
- Tea: Duck legs with chips and salad

**Behavioral lenses:** Occasion, Pricing/value, Identity, Convenience tradeoff, Recycling diligence, Reuse tendency.

---

#### Follow-up interview 2 (Step 7) · Katie — 3,610 words · 19,532 characters

**Themes:**
- 2022-02-17 - Second follow up with Katie
- Reflections on taking part in the study
- More aware of the presence of plastic packaging
- “Well, I thought, when I first started, I thought that I was quite good [laughs] in terms of waste, I’m really not at all. But then, throughout the study, I’ve tried, well, it’s been on my mind, sort 
- [04.00] “I’m aware, it’s just literally everything that I buy is in plastic...it’s almost literally everything. I don’t know if it’s got worse over the years and I’ve just not noticed...yeah when I wa
- [5.15] Talks about the seafood sticks being ‘extra-packaged’.
- New scientist magazine article and limited capacity to make a change as a ‘little person’ [3.10]
- But, yeah, it’s just made me more aware really and actually I was reading an article yesterday in New Scientist and it was called ‘Material world’ or something like that and it was about that exact th

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

**Questions asked:** See [Follow-up interview 2 (Step 7)](#follow-up-interview-2-step-7-katie) below.

---

#### Interview 2 (held out) · Katie — 10,873 words · 55,839 characters

**Themes:**
- **Household/home:** Yeah, he’s getting better, we’re actually, we’re trying to clear the house to move house at the moment.; So like I said before we don’t have room for a proper bin so we just hang bags on the door.
- **Shopping:** Yeah so I mean I have been eating the same meals for evening really because we just keep buying the same stuff but less chicken, so I haven’t really eaten much ; And then we nip next door to Aldi sometimes to bulk up on the rest.
- **Food/preparation:** So I heard that around here its not a great proportion that actually gets recycled once its been taken away.; Yeah
 Yeah
 Yeah, its frustrating because I really do, I had all these grand ideas that I was going to eat organic and eat the rainbow and everything.
- **Plastic packaging:** Needles all come in, syringes all come in plastic for hygiene and then you rip it off and throw it away.; There’s a lot of disposable, everything’s disposable with that because everything’s wrapped in plastic for hygiene reasons.
- **Disposal/recycling:** And then we were recycling them but its just additional plastic waste and that’s like 14 little tubs a week.; I don’t know whether they are actually recycled.
- **Reuse:** I think I mentioned about like the blood samples coming in a plastic bag but then they double bagged them, pointlessly, because that would stop COVID or somethi; Then he has sort of like cereal bars and crisps and like KitKat type biscuits, just stuff that he can just keep in his bag and its just easy.
- **Routines:** Oh well I don’t have a clinical background but I know a bit, I worked in the lab, in the blood lab.; So I think if we were having them every day, like sometimes we do, we’re not at the moment because I feel a bit sickly and I just can’t be bothered with them.

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

**Questions asked:** See [Interview 2 (held out)](#interview-2-held-out-katie) below.

---

### Interview questions

#### Interview 1 (Step 0) · Katie

**Household / home / neighbourhood**
- Ok. Just going back a little bit then, you mentioned that you’d been in the house maybe four to five years or you mov...

**Food / preparation / shopping / routines**
- You just mentioned there that you don’t like creating unnecessary plastic waste. Could you give me like an example? C...
- Right I see so you’ve got the bag for life on the kitchen door and that’s what you use for, what tends to go in there...
- Ok, well just out of curiosity then, when you come across a piece of plastic food packaging then how do you determine...
- How do you manage then if you feel like you don’t really have much space, like in terms of food and food shopping, ho...
- Ok. And could you give me a few more examples of these types of foods then?
- I guess is the space that you’ve got in the freezer suitable? I mean you’re talking about things that you might have ...

**Disposal / recycling / packaging**
- And how does that compare as well to the fruit and veg you mentioned as well in terms of the unnecessary packaging?
- You mentioned there that you feel bad if you put it in the general waste, why is that?
- What types of plastics then do you put in there in recycling? I mean you’ve mentioned there that you put the lid in f...
- Right ok. So just out of curiosity then for you what types of plastic can you recycle?
- What happens then, do you, I mean once you’ve put it in the compost bin?
- Just out of curiosity why do you think they might not be recyclable?

**Broader context**
- You mentioned there that you’re quite environmentally aware, would you be able to tell me a little bit more about that?
- I mean I was just curious as to maybe if you could tell me then a little bit more about your degree. So you mentioned...
- It was just if you could tell me a little bit more about yourself. But yeah so this is, you haven’t gone off on a tan...
- No, what do they look like then? What are they made out of?
- Right ok. What makes you think you’ve got to send it to Brita?
- I mean you give me one instance there were you feel kind of conflicted then between the environment and also your hea...
- I think I know what they look, what are they made out of?
- What is it about its that unnecessary then? So you talked about the Actimel but you mentioned there about taking that...
- Oh I see, are these two carrier bags then?
- Can I just ask why is that then? If they’ve given you this leaflet with the additional information stating ‘don’t rec...
- So did you separate it beforehand?
- So what happens to that then?

---

#### Interview 2 (held out) · Katie

**Diary callbacks (where applicable)**

**Household / home / neighbourhood**
- And so what happens then mainly at your house then in terms of recycling then in the kitchen?

**Food / preparation / shopping / routines**
- Oh right, so when you do your weekly shop you go to both shops then?
- And these kind of special meats then that you’re talking about, I mean what kind of meats are these then?
- Right I see. So you buy the Granny Smiths and they are the ones that come sold in plastic?
- And so how, I mean just kind of thinking about this study again, how does food waste compare to kind of throwing plas...
- And you just mentioned again there that you don’t like food waste and kind of feel bad about throwing food away. So i...

**Disposal / recycling / packaging**
- Right I see, ok. And is there kind of, does plastic have a presence there as well in any of the modules that you’re i...
- What do you think happens to the rest of it then, the other percentage then that isn’t recycled?
- Yeah, ok. And how do these tend to come packaged then?
- Ok. And so what kind of happened to this packaging then after?
- And these normally go in the general waste?
- Ok. So just out of curiosity then, how does this packaging then compare with the packaging from Booths? Did you say i...
- Ok. And yeah I guess another point that I wanted to mention, going back to the recycling, so I mean you mentioned dur...
- I know which ones you mean. Yeah the relatively kind of large kind of containers aren’t they?
- Ok. And is there any reason why you didn’t think it was recyclable?

**Broader context**
- And you mentioned there so you’re involvement around their sessions which are based around problem based learning. So...
- In terms of equipment as well?
- Yeah, ok. And you mentioned there about the aseptic testing, did you say as well?
- And what’s the purpose of the aseptic technique then and what situation does that happen in?
- Ok. And you mentioned just there as well like you don’t feel like it fills you with much confidence when you are taki...
- Ok, yeah. And it just goes over the top to cover it?
- Right ok. So is that for any particular reason? It is mainly the contamination then that you’re talking about?
- Right ok. So this doesn’t kind of get rinsed then at all?
- Yeah, so why is it that you feel that it is better?
- Yeah. So when you mention as well that it, I mean coming together or living together was quite tricky just in terms o...
- So what do you think about that?
- And is there any particular reason why you go for the Granny Smith apples as well?
- Yeah. So what happened, what’s been happening then when you mentioned before about decluttering and you talked about ...

---

#### Follow-up 1 (Step 3) · Katie

**Diary callbacks / photo-elicitation**
- Has participation changed how you notice packaging?
- Walk through key diary photos from this period. *(diary callback)*
- Tell me about meals or shopping moments flagged in the diary. *(diary callback)*
- What happened to the packaging from those items? *(diary callback)*
- How does disposal here compare with home or prior habits?

---

#### Follow-up 2 (Step 7) · Katie

**Diary callbacks (researcher-led probes)**
- “Well, I thought, when I first started, I thought that I was quite good [laughs] in terms of waste, I’m really not at all. But then, throughout the study, I’ve tried, well, it’s be *(diary callback)*
- “I’m aware, it’s just literally everything that I buy is in plastic...it’s almost literally everything. I don’t know if it’s got worse over the years and I’ve just not noticed...ye *(diary callback)*
- Talks about the seafood sticks being ‘extra-packaged’. *(diary callback)*
- It was talking about a circular economy and a circular society as well and they interviewed somebody who was pushing for a more circular, is it circular economy? I don’t know, but  *(diary callback)*
- They didn’t have the usual food which comes in a metal tin, but I thought that those gourmet pots that are in the picture, I thought that they would be metal too, but they weren’t, *(diary callback)*
-  *(diary callback)*
- “I know it's probably overly cautious, but. It had, like I read that it has been known and chemicals do leach and. And. I just so I'm just looking at that. It was the kippers, wasn *(diary callback)*
- Evening meal will consist of ‘proper food’ *(diary callback)*
- What is convenience food for Katie? [23.11] *(diary callback)*
- We just sort of get a takeaway when it’s convenient or if we’re really tired and none of us can be bothered cooking or if we run out of food and we can’t be bothered doing a full s *(diary callback)*
- R: But these are foods that you have bought to eat together? *(diary callback)*
- Test tubes – stored in Katie’s fridge – the air pollution tubes that ‘need to be kept cool’. Katie explains that the tubes have a reagent in the top of them which reacts with nitro *(diary callback)*

---

### Behavioral lens summary across steps

| Step | Primary lenses |
|------|----------------|
| Interview 1 (Step 0) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |
| Diary 1 (Step 1) | Occasion, Pricing/value, Identity, Convenience tradeoff, Recycling diligence |
| Diary 2 (Step 2) | Occasion, Pricing/value, Identity, Convenience tradeoff, Recycling diligence |
| Follow-up interview 1 (Step 3) | Occasion, Identity, Convenience tradeoff, Recycling diligence, Reuse tendency |
| Diary 3 (Step 4) | Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence |
| Diary 4 (Step 5) | Occasion, Culture/social, Convenience tradeoff, Recycling diligence, Reuse tendency |
| Diary 5 (Step 6) | Occasion, Pricing/value, Identity, Convenience tradeoff, Recycling diligence |
| Follow-up interview 2 (Step 7) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |
| Interview 2 (held out) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |

---

### John (Phase 3 · Extend)

**Profile:** Father of two primary-age girls; married; lifelong [home town] resident; 13+ years charity/grant-making sector. Recycling awareness increasing through study participation; tetrapak/paper straw discoveries.

### Data order and volume

| Step | Calibration step | File | Date | Words | Characters |
|------|------------------|------|------|-------|------------|
| 0 | Interview 1 | `20220111_First_Interview_John.docx` | 11/01/22 | 20,989 | 107,100 |
| 1 | Diary 1 | `20220117_John's_diary_entry_1.docx` | 17/01/22 | 716 | 3,968 |
| 2 | Diary 2 | `20220124_John_diary_entry_2.docx` | 24/01/22 | 484 | 2,646 |
| 3 | Follow-up interview 1 | `20220127_Follow_up_1_John.docx` | 27/01/22 | 1,497 | 8,482 |
| 4 | Diary 3 | `20220131_John_diary_entry_3.docx` | 31/01/22 | 496 | 2,745 |
| 5 | Diary 4 | `20220207_John_diary_entry_4.docx` | 07/02/22 | 471 | 2,542 |
| 7 | Follow-up interview 2 | `20220218_Follow_up_2_John.docx` | 18/02/22 | 3,540 | 19,442 |
| — | Interview 2 (held out) | `20220222_Final_Interview_John.docx` | 22/02/22 | 14,322 | 74,594 |

**Participant totals:** 42,515 words · 221,519 characters · 8 files

---

### Step summaries

#### Interview 1 (Step 0) · John — 20,989 words · 107,100 characters

**Themes:**
- **Household/home:** Other than that been living, well lived in [home town] pretty much all my life.; Went off and studied elsewhere but [home town]’s always been home.
- **Shopping:** Yeah stuff that isn’t particularly good but its easy to just go in a shop and leave it in my drawer and know that if I’ve got five minutes to eat it I can liter; So yeah we’ve got cutlery for literally eating at your desk for when you’ve nipped out to get something from the supermarket you can come back and eat it.
- **Food/preparation:** Yeah stuff that isn’t particularly good but its easy to just go in a shop and leave it in my drawer and know that if I’ve got five minutes to eat it I can liter; Its in plastic so you take the lid off, I’ve never made one so I will eat it especially so that I can put it in my diary.
- **Plastic packaging:** And I suppose that was my question, we don’t have to answer it now but I thought tetrapacks were plastic and it seems like only the lid is because it says board; And it said on the packaging leave the straw in when you recycle.
- **Disposal/recycling:** Since yesterday, since we started, in the past I would have put that in the bin thinking that’s not recyclable.; And it said on the packaging leave the straw in when you recycle.
- **Reuse:** So I’ve got desk space and I’ve got it in a bag just behind me.; Its changed in supermarkets now but the fruit and veg aisle until very recently your option was to have one of those really flimsy plastic bags to put your toma
- **Routines:** I mean still wouldn’t count on them some times and they’re literally just, I don’t know if I’ve got any to hand but they’re just, you can’t do anything to them.; Since yesterday, since we started, in the past I would have put that in the bin thinking that’s not recyclable.

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

---

#### Diary 1 (Step 1) — 716 words · 3,968 characters

**Themes:**
- There are a few items I have been using recently that seem to me to use plastic unnecessarily, perhaps to add a premium feel to a product, which seems a bit bizarre in light of campaigns in recent yea
- See attached pictures of two examples
- For the last year I have been using a number of apps (Shopmium, Green Jinn and Checkout Smart) that enables users to access free and discounted items, which have resulted in me purchasing items that w

**Behavioral lenses:** Identity, Culture/social, Convenience tradeoff, Recycling diligence, Reuse tendency, Food waste sensitivity.

---

#### Diary 2 (Step 2) — 484 words · 2,646 characters

**Themes:**
- I made my first shopping trip of the week today – to Asda on my way back from work for quite a small and focussed shop. Of the thirteen items purchased (see ‘Pic1’), all but two contained plastic pack
- My father-in-law died yesterday, and as a result our eating habits have changed somewhat – a combination of a lack of appetite and unpredictability about where we would be at any time. We didn’t know 
- On the way to McDonald’s I popped in to Sainsbury’s – of the ten items purchased (see ‘Pic2’), all but two contained plastic packaging – sticky toffee puddings. McDonald’s have made lots of noise in r

**Behavioral lenses:** Occasion, Culture/social, Convenience tradeoff, Recycling diligence, Reuse tendency, Food waste sensitivity.

---

#### Follow-up interview 1 (Step 3) · John — 1,497 words · 8,482 characters

**Themes:**
- 2022-01-27 - First follow up with John
- Reflecting back on John’s video, he mentions that the two salads he purchased via an app on his phone (for free) are not salads that he would ‘ordinarily buy’, as he explained, he wouldn’t normally sp
- He described how the packaging of these salads contained a ‘story’ about how a lady had ‘single-handedly delivered these fresh salad bowls around...and has grown the business’.
- But he explained that the story had no bearing on him – he went on to say that he is probably not their typical customer and that the packaging was not enough to convince him, ‘not with [his] tight pu
- Reflecting back on our discussion during his first interview, John goes on to say how the salads were packaged in a way to create a sense of ‘luxurious[ness]’ and make the salads ‘pop on the shelf’.
- Children’s breakfasts - Yoghurt pots and fruit puree pots
- ‘They’re really picky and I'll be honest, we’re in a rush’
- He explained that ‘this week’s been a little unusual’ [under the circumstances they are facing], but he explained that usually they have a ‘half an hour window’ from the moment the girls are out of be

**Behavioral lenses:** Occasion, Pricing/value, Culture/social, Convenience tradeoff, Recycling diligence, Reuse tendency.

**Questions asked:** See [Follow-up interview 1 (Step 3)](#follow-up-interview-1-step-3-john) below.

---

#### Diary 3 (Step 4) — 496 words · 2,745 characters

**Themes:**
- Thursday: Grilled chicken, pittas and salad
- Friday: Cottage pie (John away)
- Saturday: Buffet (John away)
- Sunday: Beef stew and crusty bread
- Monday: Beans on toast with cheese and lardons
- Tuesday: Omelette
- Wednesday: Eating at funeral wake

**Behavioral lenses:** Occasion, Pricing/value, Convenience tradeoff, Recycling diligence, Reuse tendency, Food waste sensitivity.

---

#### Diary 4 (Step 5) — 471 words · 2,542 characters

**Themes:**
- It occurred to me whilst looking in the fridge today that there is an exception to what I have previously told [researcher] with regards to our recycling – normally I would rinse out harder plastics a
- Today was my father-in-law’s funeral, so most of the day was spent out of the house – and all of the food consumed was eaten out of the house – I did not notice any plastic throughout the afternoon wi

**Behavioral lenses:** Occasion, Culture/social, Convenience tradeoff, Recycling diligence, Reuse tendency, Attitude-behavior gap.

---

#### Follow-up interview 2 (Step 7) · John — 3,540 words · 19,442 characters

**Themes:**
- 2022-02-18 - Second follow up with John
- John’s video diaries – rummages in his kitchen pantry-style cupboard
- Uncertainties about packaging materials
- Video context: References to packets of ‘mug shots’ and ‘Ainsley Harriott's cous cous and he mentioned that he was unsure what materials the packaging was made out of and that the packaging does not r
- Later on in this video, where he moves onto foods on his kitchen table (Packaging which he felt contained plastic in some form compared to the packaged foods still on the shelf in the pantry-cupboard 
- What is the difference between the two ‘types’ of packaging he has identified and separated? [1.18]
- Between the two types of packaging. yeah well i think casting my mind back, so things like the Ainsley Harriet cous cous, so when you rip them open, they’ve kind of got almost a foil like interoir, if
- This, which I’m assuming is plastic, again you know, whether it’s plastic or er- I was watching dragon’s den last night and she was talking about plant-based plastic versus other plastic, so I mean th

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

**Questions asked:** See [Follow-up interview 2 (Step 7)](#follow-up-interview-2-step-7-john) below.

---

#### Interview 2 (held out) · John — 14,322 words · 74,594 characters

**Themes:**
- **Household/home:** And when we buy meat, as much as possible try and get the best, you know people like Jamie Oliver say buy the best quality meat you can buy.; So yeah there’s times I want to be better in the kitchen and you know you can see how bad I am in the kitchen right now, I do the lion’s share of the meal prepa
- **Shopping:** Yeah, did I do a meal plan or did I just do a shopping list?; So yeah no we certainly reduce it and I think we now say we prefer, I’m not saying Quorn mince, we don’t often buy Quorn, but a meatless mince.
- **Food/preparation:** Yeah, did I do a meal plan or did I just do a shopping list?; Oh there’s a meal plan, that was an unusual week.
- **Plastic packaging:** I can’t remember if it was on that video where I had some mini mozzarella balls, something still closed in its packaging.; Probably the more common thing that we do throw away is like a part used tub of salad cream or something which you know we’ll probably have three quarter used i
- **Disposal/recycling:** Probably the more common thing that we do throw away is like a part used tub of salad cream or something which you know we’ll probably have three quarter used i; Yeah waste is waste, I don’t see a difference.
- **Reuse:** So yeah, no our freezer is full of, you’ve seen my freezer or my fridge, but yeah full of these meat substitute burgers, sausages, mince.; Its probably been a theme that I’ve talked about, excessive, I’ve got one of those flapjacks in my bag right now where its harder inner tray which seems complet
- **Routines:** Oh there’s a meal plan, that was an unusual week.; So yeah I’ll say, and my boss always pulls me up, well not me but the fact that they call it chicken and sausages or bacon, which I’ve got no issue with persona

**Behavioral lenses:** Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff, Recycling diligence.

**Questions asked:** See [Interview 2 (held out)](#interview-2-held-out-john) below.

---

### Interview questions

#### Interview 1 (Step 0) · John

**Household / home / neighbourhood**
- You mentioned as well that you at the minute spend three days in the office and two at home. So could you just tell m...
- And just on this one as well, so you showed me the flapjack one that you brought home and you mentioned before that i...
- No it is useful thank you. Just going back to a bit more about you and your family, just thinking about any hobbies t...

**Food / preparation / shopping / routines**
- Yeah. I mean just on what you’ve mentioned there in terms of lunches as well. This is kind of focused on food, this s...
- Do you have cutlery there then as well? You mentioned that you’d eat it there?
- And just moving on a little bit then. Just moving on about food, can you tell me a little bit about you and your fami...
- And when you say treat there what exactly do you mean?

**Disposal / recycling / packaging**
- That is going in the paper recycling now?
- Just out of curiosity then what are the recycling facilities like at work? What is the refuse situation?
- How often have you been doing that then? So anything you think is recyclable how often, how long have you been doing ...
- You mentioned just there that you’ve got more of an awareness now, like in terms of thinking about plastic in the sea...

**Broader context**
- When you check what do you mean by that?
- How do you know that that’s just paper?
- No but that’s interesting so thanks for letting me know about that. So I mean we’ll come back to this if that’s ok. S...
- Ok. So well this interview is all about kind of you and to understand more about you and your life. So to begin with ...
- Yeah, no that’s perfectly fine thank you. And just in terms of the job that you’ve got now then, you mentioned when w...
- Just one more point in terms of work but just in terms of maybe, just thinking about timings then. So when you’re at ...
- That belongs to?
- Right I see. And like the cutlery and everything that’s in there, does that belong to the staff? Like you mentioned t...
- You mentioned as well that you have a particular milk that you have at work as well. Could you tell me a little bit m...
- Oh really, wow. So whereabouts do you store this then? You said you’ve got a storage here and at work as well?
- They sort it? What do they mean by that?
- How did you get into the beach clean ups then?
- Is that the main reason then why you do subscribe then?
- Do you want me to pause?

---

#### Interview 2 (held out) · John

**Diary callbacks (where applicable)**

**Food / preparation / shopping / routines**
- Is there any particular reason why you have reduced your meat consumption and you’re talking there as well, you menti...
- Just how does food waste compare to plastic packaging waste?
- And yeah on the same diary entry, so on this week three diary entry, on the Wednesday there you mentioned that the gi...
- I mean just out of curiosity then so you’ve talked about having this poster or leaflet on your fridge which kind of i...

**Disposal / recycling / packaging**
- Ok. Another question that I wanted to ask you is around kind of awareness of plastic related issues, so in your first...
- Just thinking about milk then and the containers that they come in, often are glass. So how do you think, how does gl...
- How do you think like putting the environmental implications aside, just comparing packaging now, how does it compare...
- You were just talking then for a second about something inside the packaging there. What is that?

**Broader context**
- Just kind of revisiting the first interview initially then. During that interview you did mention that you and your f...
- Oh was it based in a campaign then?
- Ok, but no that’s perfectly fine, you’ve not gone off on a tangent there.  And yeah I guess this may connect up with ...
- And you mentioned as well there that vegan is the end goal but before you get there there’s a lot of learnings that n...
- Ok. Going back to the interview again and I think this is mentioned as well in maybe one of the follow ups we had or ...
- What do you mean by we in that sentence?
- That’s ok. And you mentioned just then as well that this awareness is more passive. Could you tell me what you mean b...
- Ok. Right I just have a couple more questions, how are we doing for time? Just I have a couple more questions and the...
- I mean within all of the diary entries you’ve provided quite a few of the examples there of the different types of pl...
- Can I just ask about. So you mentioned there that there’s videos of people sifting through. Who are these people? Wha...
- You mentioned there as well that you only have 15 minutes from walking into setting off again and like that’s not lon...
- Is that, I guess is that the plan then for tomorrow?
- What will you do with this one then, that you’re not sure about?
- Just moving on to the Friday then. So here this is when you went to Manchester for a couple of nights to see the gig ...
- You mentioned as well that this is a habit that you’ve got into over the past few years. So was there a point then wh...
- And I mean you just mentioned about your bag there. That was going to be one of my questions in terms of where you do...
- Yeah that’s what I wanted to ask you about there. Yeah and on the Saturday, so you mentioned that for this particular...

---

#### Follow-up 1 (Step 3) · John

**Diary callbacks / photo-elicitation**
- Has participation changed how you notice packaging?
- Walk through key diary photos from this period. *(diary callback)*
- Tell me about meals or shopping moments flagged in the diary. *(diary callback)*
- What happened to the packaging from those items? *(diary callback)*
- How does disposal here compare with home or prior habits?

---

#### Follow-up 2 (Step 7) · John

**Diary callbacks (researcher-led probes)**
- What is the difference between the two ‘types’ of packaging he has identified and separated? [1.18] *(diary callback)*
- Between the two types of packaging. yeah well i think casting my mind back, so things like the Ainsley Harriet cous cous, so when you rip them open, they’ve kind of got almost a fo *(diary callback)*
- that’s my understanding of you know...in that, I know with coffee cups, you know, like your Costa takeaway coffee cups that whilst it says that they’re recyclable, I know that they *(diary callback)*
- Packaging that ‘rips like paper’ - how is this disposed of? [4.55] *(diary callback)*
- I know there are different types of tea bags, I know there’s been a move away from having plastic in tea bags. Up until a few years ago, I’d assume that the teabag was just a bit o *(diary callback)*
- Having an awareness that teabags might contain plastic – is this a concern? [20.00] *(diary callback)*

---

### Behavioral lens summary across steps

| Step | Primary lenses |
|------|----------------|
| Interview 1 (Step 0) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |
| Diary 1 (Step 1) | Identity, Culture/social, Convenience tradeoff, Recycling diligence, Reuse tendency |
| Diary 2 (Step 2) | Occasion, Culture/social, Convenience tradeoff, Recycling diligence, Reuse tendency |
| Follow-up interview 1 (Step 3) | Occasion, Pricing/value, Culture/social, Convenience tradeoff, Recycling diligence |
| Diary 3 (Step 4) | Occasion, Pricing/value, Convenience tradeoff, Recycling diligence, Reuse tendency |
| Diary 4 (Step 5) | Occasion, Culture/social, Convenience tradeoff, Recycling diligence, Reuse tendency |
| Follow-up interview 2 (Step 7) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |
| Interview 2 (held out) | Occasion, Pricing/value, Identity, Culture/social, Convenience tradeoff |

---


*Generated from `scripts/classify_p0_files.py` + qualitative synthesis.*
