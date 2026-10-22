# gap_matrix.md

Review analysed: *Context-Window Degradation and Its Impact on Long-Document Research Synthesis*  
Source file: `MNS2026001_ReviewPaper.pdf`  
Prepared: 2026-10-22

**Status:** Five candidate gaps are mapped below. No gap has been selected as the final project, no novelty claim is made, and no experiment has been run.

## How to read the tags

- **VERIFIED:** Directly supported by the review text at the section listed. For claims about a cited publication, this means only that the review makes the claim—not that the original publication has been checked.
- **INFERRED:** Proposed interpretation, research question, or experimental extension.
- **UNKNOWN:** Evidence is missing; the required check is stated.

Section and PDF page references below refer to the 15-page final file `MNS2026001_ReviewPaper.pdf` (PDF page numbers, not printed section numbers).

---

## A. Review inventory

### A1. Scope and themes

| Item | Where in the review | Tag |
|---|---|---|
| The paper synthesizes 20 scholarly papers discovered through ResearchRabbit, Litmaps, Semantic Scholar, and Elicit | Abstract; Section 2 | VERIFIED |
| The review is thematic, not a formal systematic review | Section 2; Section 7 | VERIFIED |
| Four broad themes: context extension/capacity; degradation and positional effects; evaluation/reasoning; mitigation | Abstract; Sections 2–6 | VERIFIED |
| The central distinction is nominal context capacity versus effective context use | Abstract; Sections 1, 4, and 5 | VERIFIED |
| The review reports no new model experiment of its own | Review framing and thematic synthesis; no experimental results are presented | VERIFIED based on the reviewed text |
| Primary papers have all been independently checked | Not established | UNKNOWN |

### A2. Main evaluation dimensions discussed

| Dimension | Why it matters for synthesis | Where |
|---|---|---|
| Context length / effective context size | A model may accept a long input but use it unreliably | Sections 4.2, 5.1, 6.1, 8 |
| Evidence position | Important information may be harder to use in some positions | Sections 4.2, 5.1, 8 |
| Distractor density | Irrelevant material may interfere with evidence use | Sections 1, 6.1, 8 |
| Reasoning depth and distributed evidence | Retrieving facts is not the same as combining them into a supported conclusion | Sections 4.3, 4.6, 6.1 |
| Source attribution / claim–evidence consistency | A correct-sounding answer may be unsupported or attribute evidence to the wrong source | Sections 8.1, 9 |
| Document structure | Headings, tables, references, and file formats may affect evidence use | Sections 8, 8.1 |
| Compute, accuracy, and cost | Mitigation strategies need fair comparison under comparable constraints | Section 8 |

### A3. Limitations stated by the review

| Limitation or caveat | Where | Tag |
|---|---|---|
| The review is thematic and is not exhaustive systematic coverage | Section 2 | VERIFIED |
| Controlled or synthetic tasks help isolate failure modes but do not fully represent real literature reviews | Section 7 | VERIFIED |
| Real research documents contain heterogeneous structure, tables, references, equations, terminology, and conflicting claims | Section 7 | VERIFIED |
| Papers differ in model generations, context sizes, and evaluation protocols, complicating direct numerical comparison | Section 7 | VERIFIED |
| Discovery bias is possible because the literature tools do not expose identical scholarly corpora | Section 7 | VERIFIED |
| The search protocol is sufficiently detailed to reproduce the review | Not established by the reviewed text inspected | UNKNOWN |

---

## B. Five candidate gaps

### G1. Effective-context evaluation for realistic multi-document synthesis

- **Source passages:** Section 4.2 (PDF p. 6), Section 4.3 (PDF p. 7), Section 6.1 (PDF p. 11), Section 8 (PDF pp. 11–12; gaps 1–3), and Section 9 (PDF p. 13). Key wording in Section 8 includes “No single standard yet measures effective context size” and calls for evaluation of distributed evidence and distractors.
- **Reported in the review — VERIFIED:** The review states that maximum token capacity does not guarantee reliable use of information. It calls for realistic research-review benchmarks, distributed evidence, controlled distractors, and effective-context curves.
- **Inference — INFERRED:** A controlled benchmark that jointly varies context length, evidence position, distractor density, and reasoning depth could measure how these factors interact on synthesis tasks.
- **Research question:** For a fixed evidence-grounded synthesis task, how do context length, the location of supporting evidence, and distractor density affect evidence coverage and answer quality?
- **Possible experiment:**
  1. Create a small collection of source documents with a manually checked evidence map and questions requiring evidence from multiple sources.
  2. Keep the underlying evidence and question fixed while varying context length, evidence position, and distractor proportion.
  3. Repeat each condition to estimate run-to-run variation.
  4. Measure answer correctness, evidence coverage, citation/source correctness, and performance relative to a shorter-context baseline.
- **Evidence needed:** Gold evidence sets, controlled document variants, repeat runs, a pre-defined scoring rubric, and an analysis of main effects and interactions.
- **Verify first — UNKNOWN:** Check whether the primary papers and existing benchmarks cited in the review already test this exact combination of factors on synthesis rather than retrieval alone.
- **Risk:** Building and annotating a realistic benchmark can take time. A small pilot may be needed before expanding it.

### G2. Claim-level source attribution and evidence consistency

- **Source passages:** Section 4.6 (PDF p. 8), Section 6.1 (PDF p. 11), Section 8.1 (PDF p. 12), and Section 9 (PDF p. 13). Section 8.1 says the system should identify “which document and passage support each important claim.”
- **Reported in the review — VERIFIED:** The review says source attribution and claim–evidence consistency should be treated as important evaluation dimensions. It notes that a synthesis may ignore a critical limitation or attribute a result to the wrong paper.
- **Inference — INFERRED:** A claim-level evaluation protocol could test whether each important sentence is supported by the cited source, contradicted by the evidence, or unsupported.
- **Research question:** As source documents become longer and evidence is spread across papers, how does claim-level attribution accuracy change?
- **Possible experiment:**
  1. Prepare a small set of synthesis questions and manually identify supporting, contradicting, and contextual passages.
  2. Generate answers with source references attached to individual claims.
  3. Evaluate claim support, citation correctness, omitted caveats, and unsupported-claim rate.
  4. Compare results across context-length and evidence-dispersion conditions.
- **Evidence needed:** Human-checked claim–evidence annotations, model outputs, explicit scoring rules, and agreement between independent annotators on a subset.
- **Verify first — UNKNOWN:** Search for existing long-document citation, factual-consistency, and attribution metrics before proposing a new metric. The review does not prove that such metrics are absent.
- **Risk:** Annotation can be expensive, and automatic judges may make errors. Human checks should be retained.

### G3. Effects of document ordering and scientific-document structure

- **Source passages:** Section 8, gap 4 (PDF pp. 11–12), Section 8.1 (PDF p. 12), and Section 9 (PDF p. 13). Section 8 explicitly names document ordering, section structure, tables, references, and heterogeneous file formats.
- **Reported in the review — VERIFIED:** The review calls for research on ordering, section structure, tables, references, and heterogeneous file formats. It notes that scientific documents differ from generic passages.
- **Inference — INFERRED:** Semantically equivalent versions of the same source set can be used to isolate how ordering and structure affect synthesis.
- **Research question:** With the evidence held constant, do changes in document order or scientific-document structure alter evidence coverage, conclusions, or source attribution?
- **Possible experiment:**
  1. Select a fixed source set and map the evidence required for each question.
  2. Generate controlled variants that change only document order or one structural feature at a time.
  3. Repeat the same task and instructions across variants.
  4. Measure answer stability, evidence coverage, and attribution correctness.
- **Evidence needed:** Matched document variants, verified gold evidence, repeated runs, and a scoring protocol.
- **Verify first — UNKNOWN:** Check related work on position sensitivity, document layout, table understanding, and parsing. File-format effects must be separated from extraction errors.
- **Risk:** Changing layout or extraction can unintentionally change content. Variants need careful validation.

### G4. Fair comparison of full context, retrieval, compression, and hybrid processing

- **Source passages:** Sections 4.5–4.6 (PDF pp. 8–9), Section 5.2 (PDF p. 10), Section 8 gap 6 (PDF p. 12), Section 8.1 (PDF p. 12), and Section 9 (PDF p. 13). Section 8 asks for comparisons under “comparable compute and accuracy constraints.”
- **Reported in the review — VERIFIED:** The review discusses retrieval and compression as ways to reduce irrelevant context, while warning that reduction may remove evidence or cross-document dependencies. It calls for fair comparisons under comparable compute and accuracy constraints and for better rules to choose between approaches.
- **Inference — INFERRED:** The preferred processing strategy may depend on how widely the required evidence is distributed and on the task's complexity.
- **Research question:** Under what evidence-distribution conditions does full-context processing outperform retrieval, compression, or a hybrid approach when quality and resource use are measured together?
- **Possible experiment:** Run the same synthesis tasks using (1) full context, (2) retrieval-augmented input, (3) compressed context, and (4) a simple hybrid strategy. Keep the source corpus, task, output requirements, and model as comparable as possible.
- **Evidence needed:** A shared task set, quality and attribution scores, token usage, latency, cost, and documented differences between systems.
- **Verify first — UNKNOWN:** Check the settings and findings of the primary papers cited for retrieval, long context, and compression. The review's future-direction discussion is not proof that no prior comparison exists.
- **Risk:** This approach requires multiple pipeline components and careful resource accounting.

### G5. Human-centered evaluation of literature-review quality

- **Source passages:** Section 7 (PDF p. 11), Section 8 gap 5 (PDF p. 12), Section 8.1 (PDF p. 12), Section 9 (PDF p. 13), and Section 10 (PDF p. 13). Section 8 calls for human-centered evaluation of whether benchmark gains improve real literature reviews.
- **Reported in the review — VERIFIED:** The review states that benchmark improvements should be evaluated against actual academic or professional literature-review work and that human verification remains important.
- **Inference — INFERRED:** A structured human evaluation could test whether gains on benchmark metrics correspond to better usefulness, faithfulness, and coverage in an actual review task.
- **Research question:** Do improvements in benchmark scores predict improvements in human-rated literature-review quality?
- **Possible experiment:**
  1. Prepare a small set of review tasks with a fixed source collection.
  2. Compare outputs from two or more processing conditions.
  3. Have reviewers assess evidence coverage, correctness, balance, citation fidelity, and preservation of limitations using a shared rubric.
  4. Compare human ratings with automatic benchmark metrics.
- **Evidence needed:** A defined rubric, blinded ratings where practical, multiple raters, agreement analysis, and a documented source set.
- **Verify first — UNKNOWN:** Check prior human evaluations of generated literature reviews and whether the proposed rubric duplicates established measures.
- **Risk:** Human assessment takes time, and ratings may vary. This may be better as a later validation stage.

---

## C. Provisional ranking

The ranking below is an **inference for planning**, not a ranking stated in the review. Feasibility depends on model access, hardware, time, and annotation capacity, which are not yet known.

| Rank | Candidate | Significance | Resource demand | Feasibility with a small pilot |
|---:|---|---|---|---|
| 1 | G1: Effective-context evaluation for multi-document synthesis | High: directly tests the review's central distinction between nominal capacity and effective use | Medium | Medium–High if the initial benchmark is small and controlled |
| 2 | G4: Full context vs retrieval/compression/hybrid | High: addresses the review's call for fair comparison of mitigation strategies | Medium–High | Medium; needs comparable pipelines and cost tracking |
| 3 | G2: Claim-level source attribution | High: directly targets source fidelity in research synthesis | Medium–High due to annotation | Medium; feasible with a small manually checked sample |

G3 (structure-aware evaluation) and G5 (human-centered evaluation) remain viable alternatives. G3 may be combined with G1 as a controlled factor; G5 may be useful after a reliable benchmark and rubric exist.

### Why this ranking is provisional

- G1 is close to the review's central question and can start with a small controlled setup.
- G4 has strong practical relevance but needs multiple comparable processing pipelines.
- G2 is important for academic reliability, but annotation and metric validity need attention.
- No hardware, model/API access, time budget, or dataset has been confirmed; those unknowns may change the ranking.

---

## D. Primary-source checks still required

The review's bibliography includes work on long-context evaluation, context-length effects, positional bias, retrieval, compression, efficient attention, and training/alignment. Before making claims about novelty or reproducing results, check the original sources cited in the review.

| Check | What to verify in the original paper | Status |
|---|---|---|
| Position-sensitive performance (including *Lost in the Middle*) | Task setup, model set, evidence positions, effect size, and whether findings extend from QA to synthesis | UNKNOWN |
| Long-context benchmark coverage (including LongBench) | Task categories, dataset composition, metrics, and whether attribution/coverage are scored | UNKNOWN |
| Reasoning beyond literal matching (including NoLiMa) | How lexical overlap is controlled and how the task differs from research synthesis | UNKNOWN |
| Performance degradation under controlled retrieval (*Context Length Alone Hurts LLM Performance Despite Perfect Retrieval*) | Experimental controls, context sizes, model set, and outcomes | UNKNOWN |
| Positional effects near context limits | Exact evaluation setup and whether effects match the review's summary | UNKNOWN |
| Retrieval versus long-context approaches | Model and resource conditions, retrieval settings, quality comparisons, and cost reporting | UNKNOWN |
| Compression and context reduction | Methods evaluated, evidence-retention measures, and downstream synthesis quality | UNKNOWN |
| Human evaluation of generated literature reviews | Existing rubrics, rating reliability, and whether benchmark scores predict human judgments | UNKNOWN |

**Important:** This checklist is a plan for verification. It does not mean the primary papers have already been checked.

---

## E. Notes on interpreting the review

- The review's six gaps in Section 8 are the source for the candidate directions; the five candidates above consolidate related items into testable study plans.
- The review's statements about the literature are verified here only as statements made by the review. Primary-source confirmation is a separate task.
- The experimental questions, proposed controls, metrics, and ranking are inferred additions intended to operationalize the review's discussion.
- No candidate is claimed to be novel. A separate literature search is required.
- No experiment has been run, so no result or expected effect should be reported as an observed finding.

---

## F. Inputs needed before the next stage

1. Available hardware or notebook environment.
2. Whether API-based models are available and what cost limits apply.
3. Time available for the project.
4. Which primary papers can be accessed in full text.
5. Whether the next stage should prioritize a small feasible experiment or a broader benchmark comparison.

These inputs affect which gap should be selected and whether the study should be a reproduction, an extension, or a new evaluation design.
