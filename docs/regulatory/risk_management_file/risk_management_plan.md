# Risk Management Plan

> SIMULATION / TRAINING EXERCISE. DermaScan is a personal portfolio project, NOT a certified
> medical device. No real clinical use. Content is written in submission style for learning.

| Field | Value |
|---|---|
| Document ID | RMF-PLAN-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Akhila N Pillai |
| Date | 2026-06-27 |
| Reviewed by | - |
| Approved by | - |

**Standard:** ISO 14971:2019 (with ISO/TR 24971 guidance); aligned with EU AI Act Art. 9.
**Related:** intended_use.md (IU-001), risk_analysis.md (RMF-RA-001), risk_management_report.md
(RMF-RPT-001). **Study reference:** `steps/step-03-iso14971-risk.html`.

---

## 1. Scope

This plan governs risk management activities for DermaScan across its lifecycle, consistent with
ISO 14971:2019. Because DermaScan is also treated as a high-risk AI system, this single risk
process is intended to satisfy the continuous risk-management-system duty of EU AI Act Article 9; a
separate parallel risk file is deliberately **not** maintained, to avoid divergence.

## 2. Responsibilities

| Role | Responsibility |
|---|---|
| Risk management lead (Akhila N Pillai) | Owns the risk file; performs analysis, evaluation, control selection, residual-risk assessment |
| (Simulated) clinical reviewer | Reviews clinical reasonableness of harms, severities, and the benefit-risk conclusion |
| (Simulated) software lead | Implements and verifies risk controls; provides anomaly data |

(For a solo portfolio project these roles are held by the author; they are named to reflect the
real process.)

## 3. Risk acceptability criteria

### 3.1 Severity of harm (S)

| Level | Label | Description |
|---|---|---|
| S5 | Catastrophic | Death |
| S4 | Critical | Irreversible serious deterioration of health (for example delayed melanoma treatment leading to metastasis) |
| S3 | Serious | Reversible serious injury or intervention (for example unnecessary biopsy/excision) |
| S2 | Minor | Temporary or minor harm (for example short-term anxiety) |
| S1 | Negligible | No or inconsequential harm |

### 3.2 Probability of occurrence of harm (P)

| Level | Label | Qualitative meaning |
|---|---|---|
| P5 | Frequent | Likely to occur often in normal use |
| P4 | Probable | Will occur several times in the lifecycle |
| P3 | Occasional | Likely to occur sometime in the lifecycle |
| P2 | Remote | Unlikely but possible |
| P1 | Improbable | So unlikely it can be assumed not to occur |

### 3.3 Risk evaluation matrix

Risk level = combination of S and P. Acceptability:

| | P1 | P2 | P3 | P4 | P5 |
|---|---|---|---|---|---|
| **S5** | Tolerable | Undesirable | Unacceptable | Unacceptable | Unacceptable |
| **S4** | Tolerable | Undesirable | Undesirable | Unacceptable | Unacceptable |
| **S3** | Acceptable | Tolerable | Undesirable | Undesirable | Unacceptable |
| **S2** | Acceptable | Acceptable | Tolerable | Tolerable | Undesirable |
| **S1** | Acceptable | Acceptable | Acceptable | Acceptable | Tolerable |

Acceptability policy:
- **Acceptable** - no further control required; documented.
- **Tolerable** - acceptable only if reduced as far as possible (AFAP) and justified by benefit;
  apply controls where reasonably practicable.
- **Undesirable / Unacceptable** - risk control measures are **required**; residual risk must be
  reduced at least to Tolerable, and the benefit-risk must be justified.

## 4. Risk control option priority (ISO 14971)

Controls are selected in this order; lower-priority controls may not be used as the primary control
for an Undesirable/Unacceptable risk:
1. Inherently safe design and manufacture.
2. Protective measures in the device itself or in the manufacturing process.
3. Information for safety (IFU, labelling, warnings, training).

## 5. Method

1. Identify intended use and reasonably foreseeable misuse (from IU-001).
2. Identify hazards and hazardous situations, including AI/ML-specific hazards.
3. Estimate risk (S x P) before controls.
4. Evaluate against Section 3 criteria.
5. Select and implement risk controls (Section 4 priority).
6. Verify each control's implementation and effectiveness (link to TST-XXX in the traceability
   matrix).
7. Estimate residual risk; confirm no new risks were introduced.
8. Evaluate individual and overall residual risk; perform benefit-risk determination (RMF-RPT-001).
9. Feed production and post-production information back (link to PMS plan).

## 6. AI/ML-specific hazard sources to be considered

Per the skill guidance and the AI Act, the analysis must explicitly consider: false negative
(missed malignancy), false positive, out-of-distribution input (non-dermoscopic image, unsupported
modality), demographic / Fitzpatrick bias, automation bias / over-reliance, dataset shift over
time, silent model degradation, and adversarial or corrupted input.

## 7. Criteria for overall residual risk acceptability

The overall residual risk is acceptable when all individual residual risks are at most Tolerable
and reduced AFAP, and the documented clinical benefit (clinical_evaluation.md) outweighs the
combined residual risk.

## 8. Risk management activities and review

Risk management is iterative across the lifecycle. The risk file is reviewed when: the intended
purpose changes; model behaviour, inputs/outputs, or API contracts change; new anomalies or
post-market signals arise; or relevant standards/regulations change.

## 9. Change history

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-06-27 | Akhila N Pillai | Initial draft (simulation) |
