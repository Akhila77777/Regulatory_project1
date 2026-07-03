# Software Requirements Specification (SRS)

> SIMULATION / TRAINING EXERCISE. DermaScan is a personal portfolio project, NOT a certified
> medical device. No real clinical use. Content is written in submission style for learning.

| Field | Value |
|---|---|
| Document ID | SRS-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Akhila N Pillai |
| Date | 2026-06-27 |
| Reviewed by | - |
| Approved by | - |

**Standards/refs:** IEC 62304 (5.2 requirements analysis); ISO 14971 (controls -> requirements);
MDR Annex I (GSPR 17); EU AI Act Art. 12, 13, 14, 15. **Related:** IU-001, CLS-001, RMF-RA-001,
traceability_matrix.md (TRC-001), verification_validation/ (VV-001, VV-TS-001), ARC-001, DEP-001.
> Realization note: the non-functional requirements for availability (REQ-014), security
> (REQ-050 to REQ-054), and record-keeping/logging (REQ-040 to REQ-042) are realized and made
> testable by the GCP deployment described in DEP-001 (Cloud Run, IAM, Secret Manager, Cloud Armor,
> Cloud Logging/Audit Logs).
**Study reference:** `steps/step-09-verification-validation.html`.

---

## 1. Introduction

### 1.1 Purpose
This SRS specifies the software requirements for DermaScan. Each requirement is testable, traces to
a source (the intended purpose IU-001, a risk control in RMF-RA-001, or a regulatory article), and
is linked to a verification test (TST-XXX). The verification tests are executed and recorded in the
verification & validation files (build phase 9); until then, TST links denote planned verification.

### 1.2 Scope
DermaScan is decision-support SaMD (MDR Class IIa, AI Act high-risk; see CLS-001) that estimates the
malignancy likelihood of a single pigmented skin lesion from an image, for use by a qualified
clinician who independently confirms every output.

### 1.3 Requirement conventions
- Each requirement uses "**shall**" and is atomic and verifiable.
- Requirement types: Functional (F), Performance (P), Safety (S), Human-oversight/Transparency (H),
  Security (SEC), Usability (U), Regulatory/Record-keeping (R).
- Numeric targets marked "(placeholder)" are to be fixed against the chosen datasets in the clinical
  evaluation; the structure and acceptance method are binding, the exact figure is provisional.

### 1.4 Definitions
OOD = out-of-distribution. AUROC = area under the ROC curve. ECE = expected calibration error.
See IU-001 and the glossary in step-13.

---

## 2. Functional requirements

| ID | Type | Requirement (shall) | Rationale | Source | Test |
|---|---|---|---|---|---|
| REQ-001 | F | The system shall accept a single digital dermoscopic/clinical image of one lesion in the supported formats and shall reject files that do not meet the minimum resolution and format criteria. | Define valid input | IU-001 8.1 | TST-001 |
| REQ-002 | F | The system shall output a calibrated malignancy-risk estimate as a probability and/or risk band, and shall not present a bare binary "benign/malignant" verdict. | Avoid over-definitive output | IU-001 8.2; RISK-002 | TST-002 |
| REQ-003 | F | The system shall process exactly one lesion per request and shall indicate when multiple or no lesions are detected in the image. | Defined operating unit | IU-001 8.1 | TST-003 |
| REQ-004 | F | The system shall return, with every result, a confidence indicator and, where applicable, a low-confidence flag. | Support clinician interpretation | RISK-001; RISK-007 | TST-020 |

---

## 3. Performance requirements

| ID | Type | Requirement (shall) | Rationale | Source | Test |
|---|---|---|---|---|---|
| REQ-010 | P | The system shall achieve melanoma sensitivity >= 0.90 with a 95% CI lower bound >= 0.85 (placeholder) on the independent test set, reported overall and per Fitzpatrick phototype. | Triage prioritises catching malignancy | RISK-001; RISK-004 | TST-018 |
| REQ-011 | P | The system shall report specificity and AUROC with 95% confidence intervals on the independent test set, with specificity not below the pre-defined minimum (placeholder). | Control false positives; honest performance | RISK-002 | TST-019 |
| REQ-012 | P | The predicted probabilities shall be calibrated such that the expected calibration error is below the pre-defined threshold (placeholder), assessed on the independent test set. | A stated probability must be meaningful | RISK-007 | TST-020 |
| REQ-013 | P | The system shall report all performance metrics broken down by Fitzpatrick phototype, age band, and sex where data permit, and shall not report a single aggregate accuracy figure as the performance claim. | Expose hidden subgroup bias | RISK-004 | TST-018 |
| REQ-014 | P | The system shall return a result within the defined latency target (placeholder) under the specified operating conditions. | Usability in workflow | IU-001 7 | TST-014 |

---

## 4. Safety requirements

| ID | Type | Requirement (shall) | Rationale | Source | Test |
|---|---|---|---|---|---|
| REQ-020 | S | The system shall detect out-of-distribution / unsupported inputs and shall not return a malignancy estimate for them; instead it shall return an explicit unsupported-input notice. | Prevent invalid output being trusted | RISK-003; RISK-001 | TST-012 |
| REQ-021 | S | The system shall apply an image-quality gate (focus, framing, illumination) and shall reject or flag images failing the criteria. | Bad input -> unreliable output | RISK-003 | TST-021 |
| REQ-022 | S | The system shall display a clear warning that a low-confidence or out-of-distribution result must not be interpreted as "low malignancy risk". | Counter dangerous misreading | RISK-001 | TST-022a |
| REQ-023 | S | The system shall restrict outputs to the validated population, image modality, and phototype range declared in IU-001, and shall surface the applicable limitation when input falls outside it. | Stay within validated scope | RISK-004; IU-001 10 | TST-021 |

---

## 5. Human-oversight and transparency requirements (AI Act Art. 13, 14)

| ID | Type | Requirement (shall) | Rationale | Source | Test |
|---|---|---|---|---|---|
| REQ-030 | H | Every output, in the UI and in every API response, shall include the mandatory disclaimer that the result is a research/educational decision-support output, is not a diagnosis, and must be confirmed by a qualified clinician. | Human oversight; transparency | RISK-005; IU-001 11; AI Act Art. 13 | TST-004 |
| REQ-031 | H | The system shall be designed so it cannot act autonomously on its output (no automated triage, referral, or treatment action); the clinician shall remain the decision-maker. | Preserve human oversight | RISK-005; AI Act Art. 14 | TST-031 |
| REQ-032 | H | The system shall present the result and its uncertainty in a form that supports, and does not discourage, independent clinical assessment (anti-automation-bias design). | Mitigate over-reliance | RISK-005; RISK-009 | usability (TST-009) |
| REQ-033 | H | The instructions for use shall state the system's capabilities, limitations, validated performance, intended user, and required oversight. | Deployer transparency | AI Act Art. 13; IU-001 | TST-033 (doc review) |

---

## 6. Record-keeping / regulatory requirements (AI Act Art. 12)

| ID | Type | Requirement (shall) | Rationale | Source | Test |
|---|---|---|---|---|---|
| REQ-040 | R | The system shall automatically log each inference event with timestamp, model version identifier, input image reference/hash, and the returned result. | Traceability; AI Act logging | AI Act Art. 12; RISK-006 | TST-040 |
| REQ-041 | R | Each result shall be associated with the exact model version and dataset version used, recorded so a result can be reproduced. | Change control; reproducibility | RISK-006; IEC 62304 config mgmt | TST-040 |
| REQ-042 | R | Logs shall be protected against unauthorised modification (tamper-evident). | Integrity of records | AI Act Art. 12; RISK-010 | TST-023 |

---

## 7. Security requirements (GSPR 17; AI Act Art. 15)

| ID | Type | Requirement (shall) | Rationale | Source | Test |
|---|---|---|---|---|---|
| REQ-050 | SEC | The API shall require authentication and enforce authorisation before returning any result. | Prevent unauthorised access | RISK-010; GSPR 17.4 | TST-023 |
| REQ-051 | SEC | The system shall validate and sanitise all inputs and shall be robust to malformed or corrupted inputs without producing an unsafe output. | Resist corrupted/adversarial input | RISK-008; AI Act Art. 15 | TST-022 |
| REQ-052 | SEC | The system shall maintain measured robustness to small, label-preserving image perturbations within the defined tolerance (placeholder). | Adversarial/robustness resilience | RISK-008; AI Act Art. 15 | TST-022 |
| REQ-053 | SEC | Personal and health-related data shall be encrypted in transit and at rest, and data collection shall be minimised. | Data protection | RISK-010; GDPR Art. 32 | TST-023 |
| REQ-054 | SEC | The API shall apply rate limiting and shall minimise output detail to reduce model inversion/extraction risk. | Limit model theft/inversion | RISK-008 | TST-054 |

---

## 8. Usability requirements (IEC 62366-1)

| ID | Type | Requirement (shall) | Rationale | Source | Test |
|---|---|---|---|---|---|
| REQ-060 | U | The output (risk estimate, confidence, warnings, disclaimer) shall be presented unambiguously to minimise use-error. | Reduce misinterpretation | RISK-009 | usability (TST-009) |
| REQ-061 | U | The interface and IFU shall state that the system is for qualified clinicians only and shall not be designed for patient self-assessment. | Prevent off-label lay use | IU-001 6, 10 | TST-033 (doc review) |

---

## 9. Requirement-to-source traceability summary

Every risk control in RMF-RA-001 maps to at least one requirement here, and every requirement maps
to a verification test. The full bidirectional matrix (need/risk <-> REQ <-> design <-> TST) is
maintained in traceability_matrix.md (TRC-001).

| Risk | Controlling requirement(s) |
|---|---|
| RISK-001 false negative | REQ-004, REQ-010, REQ-020, REQ-022, REQ-030, REQ-031 |
| RISK-002 false positive | REQ-002, REQ-011 |
| RISK-003 OOD input | REQ-020, REQ-021, REQ-023 |
| RISK-004 subgroup bias | REQ-010, REQ-013, REQ-023 |
| RISK-005 automation bias | REQ-030, REQ-031, REQ-032 |
| RISK-006 dataset shift | REQ-040, REQ-041 (+ PMS monitoring) |
| RISK-007 miscalibration | REQ-004, REQ-012 |
| RISK-008 adversarial/corrupted input | REQ-051, REQ-052, REQ-054 |
| RISK-009 use-error | REQ-032, REQ-060 |
| RISK-010 data loss/leak | REQ-042, REQ-050, REQ-053 |

## 10. Open items

- Fix all "(placeholder)" numeric acceptance criteria against the selected datasets in the clinical
  evaluation (build phase 8).
- Create the verification & validation specifications for each TST-XXX (build phase 9).
- Build and populate traceability_matrix.md.

## 11. Change history

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-06-27 | Akhila N Pillai | Initial draft (simulation): requirements derived from IU-001 and RMF-RA-001 controls |
