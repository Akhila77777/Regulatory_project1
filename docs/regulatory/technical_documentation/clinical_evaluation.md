# Clinical Evaluation Plan and Report

> SIMULATION / TRAINING EXERCISE. DermaScan is a personal portfolio project, NOT a certified
> medical device. No real clinical use, no real clinical investigation, and no real clinical
> results. Content is written in submission style for learning.

| Field | Value |
|---|---|
| Document ID | CLIN-001 |
| Version | 0.1 |
| Status | Draft - PLAN complete, REPORT preliminary (pending data) |
| Author | Akhila N Pillai |
| Date | 2026-06-27 |
| Reviewed by | - |
| Approved by | - |

**Regulations/guidance:** MDR 2017/745 Art. 61 and Annex XIV Part A; MDCG 2020-1 (clinical
evaluation of medical device software); IMDRF SaMD clinical evaluation framework; EU AI Act Art. 15.
**Related:** IU-001, RMF-RPT-001, SRS-001 (REQ-010 to REQ-013), DG-001/DSC-001, AIA-001.
**Study reference:** `steps/step-08-clinical-evaluation.html`.

---

## 1. Purpose and status

This document is the clinical evaluation plan and (preliminary) report for DermaScan, prepared per
MDR Annex XIV and MDCG 2020-1. The **plan** (Sections 3-8) is complete; the **report** conclusions
(Section 9) are preliminary because the model performance study has not been executed. No clinical
results are invented; numeric outcomes are shown as acceptance criteria/placeholders to be filled
when the evaluation is run (build of `src/evaluation`).

## 2. Scope and intended purpose under evaluation

The device, intended purpose, intended user, indication, population, and limitations are as defined
in IU-001 (decision-support triage of pigmented skin lesions; output is a malignancy-risk estimate;
qualified-clinician user; not a diagnosis). The clinical evaluation must demonstrate that the device
achieves this intended purpose with acceptable benefit-risk.

## 3. Clinical evaluation method (MDCG 2020-1 / IMDRF three pillars)

For software, clinical evaluation must establish three linked elements:

| Pillar | Question | How addressed for DermaScan |
|---|---|---|
| Valid clinical association | Is the output scientifically linked to the clinical condition? | Dermoscopic image features are an established basis for malignancy assessment; supported by literature (state of the art, Section 4) |
| Technical / analytical validation | Does the software correctly and reliably produce the intended output from the input? | Software verification (SRS/TRC tests: correct, reproducible computation; calibration TST-020) |
| Clinical validation | Does the output achieve the intended clinical purpose in the target population? | Performance study on an independent, representative test set with subgroup analysis (Section 6) |

## 4. State of the art and benchmarking

- Summarise the current standard of care for pigmented-lesion triage (clinical and dermoscopic
  examination, established rule sets, histopathology as reference standard).
- Summarise the published performance range of comparable AI dermatology tools and any CE-marked
  decision-support devices, to set a credible expected performance band and acceptance criteria.
- Identify residual clinical questions the evaluation must answer (generalisation, subgroup fairness,
  real-world robustness).

(References to be compiled in a literature search log; no specific external results are asserted in
this simulation.)

## 5. Clinical evaluation plan

- **Objective:** demonstrate adequate diagnostic performance and acceptable benefit-risk for the
  intended triage-support purpose.
- **Reference standard:** histopathology-confirmed labels where available (DG-001/DSC-001).
- **Data:** independent test set from the governed datasets; external validation (different
  source/site) sought where feasible; no leakage across splits (DG-001).
- **Acceptance criteria:** the performance thresholds in SRS-001 (REQ-010 to REQ-013), confirmed
  against the state of the art (Section 4).
- **Subgroups:** performance reported per Fitzpatrick phototype, age band, and sex where data permit.
- **Analysis plan:** metrics with 95% confidence intervals; calibration assessment; pre-specified
  operating threshold rationale.

## 6. Performance endpoints and acceptance criteria

| Endpoint | Metric | Acceptance criterion (placeholder, confirm vs state of the art) | Source REQ | Test |
|---|---|---|---|---|
| Primary | Melanoma sensitivity (overall and per Fitzpatrick) | >= 0.90, 95% CI lower bound >= 0.85 | REQ-010, REQ-013 | TST-018 |
| Secondary | Specificity | >= defined minimum | REQ-011 | TST-019 |
| Secondary | AUROC | >= defined minimum, with 95% CI | REQ-011 | TST-019 |
| Secondary | Calibration (ECE) | <= defined maximum | REQ-012 | TST-020 |
| Safety-related | Out-of-distribution rejection rate | >= defined minimum on OOD probe set | REQ-020 | TST-012 |

Rationale: sensitivity is the primary endpoint because a false negative (missed malignancy) is the
most serious harm (RMF-RA-001 RISK-001). Operating threshold is set for high sensitivity appropriate
to a triage-support purpose and justified clinically, not by a generic optimisation metric.

## 7. Subgroup / fairness analysis

Per-subgroup performance (especially Fitzpatrick IV-VI) is a required output, not optional. Any
subgroup with materially lower performance, or with insufficient data to evaluate, is excluded from
the validated intended use until adequate data and validation exist (links RISK-004; controls
REQ-013, REQ-023). This is also an EU AI Act Art. 10/15 expectation.

## 8. Link to verification, risk, and AI Act

- Technical/analytical validation evidence is the software verification recorded in TRC-001.
- Clinical validation evidence (this study) feeds the benefit-risk determination in RMF-RPT-001.
- Accuracy and robustness metrics double as the AI Act Art. 15 performance declaration (AIA-001 3.5).

## 9. Clinical evaluation report - preliminary conclusions

**Preliminary and conditional** (no study executed):
- Once the performance study meets the Section 6 acceptance criteria on an independent (preferably
  external) test set, with acceptable subgroup performance, the device is expected to demonstrate a
  valid clinical association, technical validation, and clinical validation for the stated intended
  purpose.
- The clinical benefit (earlier, better-informed triage as an adjunct, under mandatory clinician
  review) is then expected to outweigh the residual risks (RMF-RPT-001), supporting an acceptable
  benefit-risk.
- If the acceptance criteria are not met, the intended purpose, population, classification, or
  controls must be revised, and this report and RMF-RPT-001 updated accordingly.

## 10. Post-Market Clinical Follow-up (PMCF) link

The clinical evaluation is kept current with real-world data via the PMCF plan (build phase 10),
which monitors live and per-subgroup performance and model drift (RISK-004, RISK-006), feeding back
into this report and the risk file.

## 11. Open items

- Execute the performance study (`src/evaluation`) and populate Section 6 with real metrics and CIs.
- Complete the literature search log and state-of-the-art benchmarking (Section 4).
- Fix subgroup composition and the validated Fitzpatrick range (with DSC-001 and IU-001).
- Re-issue the report (Section 9) as Version 1.0 with confirmed conclusions.

## 12. Change history

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-06-27 | Akhila N Pillai | Initial draft (simulation): plan complete, report preliminary |
