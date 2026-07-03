# Verification and Validation Plan

> SIMULATION / TRAINING EXERCISE. DermaScan is a personal portfolio project, NOT a certified
> medical device. No real clinical use. Content is written in submission style for learning. Tests
> are specified but not yet executed; results are recorded as they are run.

| Field | Value |
|---|---|
| Document ID | VV-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Akhila N Pillai |
| Date | 2026-07-03 |
| Reviewed by | - |
| Approved by | - |

**Standards:** IEC 62304 (5.5 unit, 5.6 integration, 5.7 system testing); ISO 13485 7.3.6/7.3.7
(design verification/validation); ISO 14971 (verification of risk controls). **Related:** SRS-001
(REQ-XXX), TRC-001 (test index), test_specifications.md (VV-TS-001), ARC-001, CLIN-001, RMF-RA-001.
**Study reference:** `steps/step-09-verification-validation.html`.

---

## 1. Purpose and scope

This plan defines how DermaScan is verified (built to specification) and validated (fit for the
intended use), and the strategy under which the individual test specifications (VV-TS-001) are
executed. It covers software verification, model performance evaluation, safety, security, and
usability/validation, and it is the evidence base that populates the "V&V status" column of TRC-001.

## 2. Verification vs validation

- **Verification** confirms design outputs meet design inputs (REQ-XXX). Covers unit, integration,
  system, performance, safety, and security tests.
- **Validation** confirms the device meets user needs and intended use (IU-001) in the intended
  setting. Covers the usability evaluation and the clinical validation (CLIN-001).

## 3. Test levels

| Level | What | IEC 62304 |
|---|---|---|
| Unit | Individual software units (ARC-001 items) with acceptance criteria | 5.5 |
| Integration | Interactions between units (e.g. gate-before-model ordering) | 5.6 |
| System | End-to-end against system requirements | 5.7 |
| Performance (ML eval) | Model metrics on the independent test set | (evaluation pipeline) |
| Validation | Usability and clinical validation | ISO 13485 7.3.7; CLIN-001 |

## 4. Test categories and datasets

| Category | Purpose | Data |
|---|---|---|
| Functional | Input handling, output schema, single-lesion | Curated valid and invalid inputs |
| Performance | Sensitivity/specificity/AUROC/calibration, subgroup | Independent test set with Fitzpatrick/age/sex labels (DSC-001) |
| Safety | OOD rejection, quality gate, warnings, no autonomous action | OOD probe set; poor-quality set; unsupported-modality set |
| Security | Auth, input robustness, adversarial, rate limiting, logging | Malformed/adversarial/perturbed inputs; access-control cases |
| Usability | Use-error, anti-automation-bias presentation | Representative users, scenario tasks (IEC 62366-1) |
| Document review | IFU/labelling content | IU-001, labelling |

## 5. ML-specific V&V rules

- **No tuning on the test set;** thresholds/calibration set on validation data only.
- **Leakage prevention:** no lesion/patient overlap across splits (DG-001).
- **Reproducibility:** fixed seeds, pinned versions (SOUP-001), recorded model + dataset version and
  code commit for every result (REQ-041).
- **Metamorphic/robustness:** invariance to small, label-preserving perturbations (rotation,
  illumination, compression).
- **Regression suite:** the full test set is re-run on every model version before release; a new
  model must not regress below release criteria (change control, PCCP).

## 6. Entry and exit criteria

- **Entry:** the item under test is under configuration control; test data prepared; environment
  recorded.
- **Exit (per requirement):** the acceptance criterion in the test spec is met and recorded; risk
  controls are verified effective (RMF-RA-001).
- **Release exit:** all safety-related and high-priority tests pass; remaining anomalies are
  evaluated and documented (IEC 62304 5.8), with none of unacceptable residual risk.

## 7. Defect / anomaly handling

Failures are logged as problems (SDP-001 clause 9 / problem resolution); safety-relevant failures
open a CAPA (SOP-CAPA-001) and are assessed against the risk file. Fixes are re-verified and the
affected regression tests re-run.

## 8. Independence

Verification is planned and recorded independently of implementation where practical. (In this solo
project the roles are held by one person; the separation is documented to reflect the real process.)

## 9. Reporting

Results are recorded per test in VV-TS-001 and summarized in a V&V report; the outcomes update the
"V&V status" column in TRC-001 (Planned -> Passed/Failed). The clinical validation outcome updates
CLIN-001 and the benefit-risk determination (RMF-RPT-001).

## 10. Status

All tests are currently **Planned**; execution begins when `src/` and the evaluation pipeline exist
(DEP-001 Section 4). Numeric acceptance criteria marked "(placeholder)" are confirmed against the
clinical evaluation (CLIN-001) before execution.

## 11. Change history

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-07-03 | Akhila N Pillai | Initial draft (simulation): V&V strategy, levels, ML rules, criteria |
