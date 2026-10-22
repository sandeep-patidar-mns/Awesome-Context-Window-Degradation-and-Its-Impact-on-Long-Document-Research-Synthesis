# research_decisions.md

Project: *Context-Window Degradation and Its Impact on Long-Document Research Synthesis*  
Source of truth: `MNS2026001_ReviewPaper.pdf`  
Prepared: 2026-10-22

## Conventions

- **VERIFIED** means the statement is present in the review text. It does not mean the cited primary paper has been independently checked.
- **INFERRED** means the statement is an interpretation or proposed experiment derived from the review.
- **UNKNOWN** means the available material does not establish the claim; the missing evidence is named.
- Do not claim novelty until the relevant primary publications and recent related work have been checked.
- Do not record an experiment, score, model result, or dataset evaluation as completed unless there is an actual execution record.

## Stage tracker

| Stage | Status | Evidence |
|---|---|---|
| 1. Workspace and review-scope summary | Complete | D-001 |
| 2. Evidence-based candidate-gap identification | Complete as candidate analysis only; no gap selected | D-002; `gap_matrix.md` |
| 3. Literature-to-experiment mapping | Not started | Primary-source verification remains open |
| 4. Feasibility and novelty check | Not started | Hardware, model/API access, time, and related-work search are unknown |
| 5. Final research question and success criteria | Not started | Depends on Stages 3–4 |
| 6. Baseline and reproducibility plan | Not started | No model or dataset selected |
| 7. Coding and experiments | Not started | No experiments have been run |
| 8. Manuscript update | Not started | Depends on verified evidence |

## Entry template

### D-XXX | YYYY-MM-DD | Stage | Title
- Decision:
- Reason:
- Evidence / source:
- Status: VERIFIED | INFERRED | UNKNOWN
- Alternatives considered:
- Next action:

## Decision log

### D-000 | 2026-10-22 | Setup | Evidence labels and scope
- **Decision:** Use the final uploaded review as the authoritative source and keep source-supported statements separate from proposed extensions.
- **Reason:** The assignment requires an accountable workspace and a gap analysis, not unsupported novelty claims.
- **Evidence / source:** Assignment Prompt 01 and Prompt 02; `MNS2026001_ReviewPaper.pdf`.
- **Status:** VERIFIED as the chosen workflow.
- **Alternatives considered:** Treating the generated candidate questions as established findings (rejected).
- **Next action:** Preserve these labels in all later work.

### D-001 | 2026-10-22 | Stage 1 | Scope of the existing review
- **Decision:** Treat the paper as a thematic literature review of 20 scholarly papers, not as an experiment or a formal systematic review.
- **Reason:** Section 2 describes a thematic synthesis and names ResearchRabbit, Litmaps, Semantic Scholar, and Elicit as discovery/organization tools. Section 7 notes limitations in coverage and discovery bias.
- **Evidence / source:** `MNS2026001_ReviewPaper.pdf`, Sections 2 and 7; Abstract and Introduction.
- **Status:** VERIFIED as a summary of what the review says; the 20 primary papers have not all been independently audited here.
- **Alternatives considered:** Calling it a formal systematic review (rejected because the review describes its method as thematic).
- **Next action:** If the assignment requires search reproducibility, record any available search queries, screening notes, and inclusion/exclusion decisions. These details are not established by the review text currently inspected.

### D-002 | 2026-10-22 | Stage 2 | Candidate gaps only
- **Decision:** Identify five testable candidate gaps without selecting a final project gap yet.
- **Reason:** The review's Section 8 lists six gaps; Sections 8.1 and 9 elaborate on realistic synthesis, attribution, structure-aware evaluation, adaptive context selection, and effective-context measurement.
- **Evidence / source:** `MNS2026001_ReviewPaper.pdf`, Sections 8, 8.1, and 9; `gap_matrix.md`, Sections B–C.
- **Status:** VERIFIED that the review states these directions; INFERRED for the proposed experimental formulations.
- **Alternatives considered:** Selecting a gap immediately (deferred until resources and primary-source checks are known).
- **Next action:** Verify related primary work before finalizing the research question.

### D-003 | 2026-10-22 | Stage 2 | Provisional candidate ranking
- **Decision:** Provisionally rank (1) effective-context evaluation for multi-document synthesis, (2) full-context versus retrieval/compression/hybrid comparisons, and (3) claim-level source attribution and evidence consistency. This matches the provisional ranking in `gap_matrix.md`.
- **Reason:** These candidates connect directly to the review's central distinction between nominal capacity and effective use, and to the gaps on realistic synthesis, attribution, and fair mitigation comparisons.
- **Evidence / source:** `MNS2026001_ReviewPaper.pdf`, Sections 4.2–4.6, 5.1–5.2, 6.1, 8, 8.1, and 9; `gap_matrix.md`, Section C. The ranking is provisional and is not reported by the review.
- **Status:** INFERRED. This ranking is our preliminary assessment, not a ranking reported by the review.
- **Alternatives considered:** Structure-aware evaluation and human-centered evaluation; these remain viable and are included in the matrix.
- **Next action:** Re-rank after checking primary sources and learning the available hardware, model/API access, and time budget.

### D-004 | 2026-10-22 | Stage 2 | No novelty or results claim
- **Decision:** Do not state that any candidate is novel, already validated, or experimentally successful.
- **Reason:** The review is a thematic synthesis; the proposed experiments in the gap matrix have not been run, and the primary-source verification has not been completed.
- **Evidence / source:** Review Section 2 describes the review method; Sections 7–9 discuss limitations and future directions. No execution outputs are attached to this workspace.
- **Status:** VERIFIED as the current project status.
- **Alternatives considered:** Presenting inferred gaps as established gaps (rejected).
- **Next action:** Complete the primary-source checklist in `gap_matrix.md`, Section D.

## Evidence ledger

| ID | Claim | Tag | Source / note |
|---|---|---|---|
| E1 | The review synthesizes 20 scholarly papers. | VERIFIED | Abstract and Section 2 |
| E2 | The review is organized around context capacity, degradation/position, evaluation/reasoning, and mitigation. | VERIFIED | Abstract; Sections 2–6 |
| E3 | The review distinguishes nominal context capacity from effective context use. | VERIFIED | Abstract; Sections 1, 4, and 5 |
| E4 | Section 8 lists six research gaps. | VERIFIED | Section 8 |
| E5 | A benchmark should jointly measure document count, context length, evidence position, distractor density, reasoning depth, and attribution. | VERIFIED as a recommendation in the review | Section 6.1 |
| E6 | A controlled experiment varying length, evidence position, and distractor density could test interactions among these factors. | INFERRED | Proposed design in `gap_matrix.md` |
| E7 | Any candidate gap is novel across the literature. | UNKNOWN | Requires a targeted literature search and primary-source checks |
| E8 | A particular model or mitigation method is best for this task. | UNKNOWN | No comparative experiment has been run |
| E9 | The project has produced experimental results. | UNKNOWN / NOT ESTABLISHED | No experiment outputs are included |

## Open UNKNOWNs

- Which hardware/notebook platform, model/API access, and time budget are available?
- Which of the 20 references will be checked first at the primary-source level?
- Do existing benchmarks already test the exact proposed combination of factors?
- Which dataset and evaluation rubric can be used with a manageable annotation burden?
- What compute and cost constraints should govern a fair comparison of full-context, retrieval, and compression approaches?

## Next actions

1. Verify the primary papers listed in `gap_matrix.md`, Section D.
2. Confirm practical resources before finalizing the ranking.
3. Select one candidate only after the novelty and feasibility check.
4. Do not start implementation until the research question, baseline, metrics, and source evidence are documented.
