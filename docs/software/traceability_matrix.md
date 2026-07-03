# Traceability Matrix

> SIMULATION / TRAINING EXERCISE. DermaScan is a personal portfolio project, NOT a certified
> medical device. No real clinical use. Content is written in submission style for learning.

| Field | Value |
|---|---|
| Document ID | TRC-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Akhila N Pillai |
| Date | 2026-06-27 |
| Reviewed by | - |
| Approved by | - |

**Standards/refs:** ISO 13485 (design controls), IEC 62304, ISO 14971, EU AI Act Annex IV.
**Related:** IU-001, RMF-RA-001, SRS-001, SSC-001, SDP-001, architecture.md (pending),
verification_validation/ (pending). **Study reference:** `steps/step-09-verification-validation.html`.

---

## 1. Purpose

This matrix is the spine that links intended use and risks to requirements, design, and tests, in
both directions, so coverage can be demonstrated and orphans detected. It is the single index that
ISO 13485 design controls and a Notified Body audit rely on.

**Status note:** verification tests (TST-XXX) are defined here and in SRS-001 but are **not yet
executed**; their V&V status is "Planned" until the verification & validation files exist (build
phase 9). Design components reference architecture.md, which is pending; component names below are
the intended decomposition and will be confirmed when architecture.md is written.

Legend: Source types - IU (intended use, IU-001), RISK (RMF-RA-001), AIA (EU AI Act article),
GSPR (MDR Annex I), GDPR. V&V status - Planned / Passed / Failed.

## 2. Forward trace: requirement to design to test

| REQ | Type | Source(s) | Design component (architecture.md, pending) | Test | V&V status |
|---|---|---|---|---|---|
| REQ-001 | Functional | IU 8.1 | Input handler / format-resolution validator | TST-001 | Planned |
| REQ-002 | Functional | IU 8.2; RISK-002 | Inference + risk-band formatter | TST-002 | Planned |
| REQ-003 | Functional | IU 8.1 | Lesion detection / single-lesion guard | TST-003 | Planned |
| REQ-004 | Functional | RISK-001; RISK-007 | Confidence estimator | TST-020 | Planned |
| REQ-010 | Performance | RISK-001; RISK-004 | Model + operating threshold | TST-018 | Planned |
| REQ-011 | Performance | RISK-002 | Evaluation pipeline | TST-019 | Planned |
| REQ-012 | Performance | RISK-007 | Calibration module | TST-020 | Planned |
| REQ-013 | Performance | RISK-004 | Evaluation pipeline (subgroup) | TST-018 | Planned |
| REQ-014 | Performance | IU 7 | Inference service | TST-014 | Planned |
| REQ-020 | Safety | RISK-003; RISK-001 | Out-of-distribution detector | TST-012 | Planned |
| REQ-021 | Safety | RISK-003 | Image-quality gate | TST-021 | Planned |
| REQ-022 | Safety | RISK-001 | Warning/presentation layer | TST-022a | Planned |
| REQ-023 | Safety | RISK-004; IU 10 | Scope/limitation guard | TST-021 | Planned |
| REQ-030 | Human oversight | RISK-005; IU 11; AIA Art.13 | API response schema (disclaimer field) | TST-004 | Planned |
| REQ-031 | Human oversight | RISK-005; AIA Art.14 | System design (no autonomous action) | TST-031 | Planned |
| REQ-032 | Human oversight | RISK-005; RISK-009 | UI/output presentation | TST-009 | Planned |
| REQ-033 | Human oversight | AIA Art.13; IU | IFU / labelling | TST-033 | Planned |
| REQ-040 | Record-keeping | AIA Art.12; RISK-006 | Logging subsystem | TST-040 | Planned |
| REQ-041 | Record-keeping | RISK-006; IEC 62304 cfg mgmt | Model/data version binding | TST-040 | Planned |
| REQ-042 | Record-keeping | AIA Art.12; RISK-010 | Tamper-evident log store | TST-023 | Planned |
| REQ-050 | Security | RISK-010; GSPR 17.4 | Auth/authorization | TST-023 | Planned |
| REQ-051 | Security | RISK-008; AIA Art.15 | Input validation/sanitization | TST-022 | Planned |
| REQ-052 | Security | RISK-008; AIA Art.15 | Robustness controls | TST-022 | Planned |
| REQ-053 | Security | RISK-010; GDPR Art.32 | Encryption / data minimization | TST-023 | Planned |
| REQ-054 | Security | RISK-008 | Rate limiting / output minimization | TST-054 | Planned |
| REQ-060 | Usability | RISK-009 | UI/output presentation | TST-009 | Planned |
| REQ-061 | Usability | IU 6, 10 | UI / IFU | TST-033 | Planned |

## 3. Risk control traceability (RISK to REQ to TST)

Confirms every risk control in RMF-RA-001 is implemented by a requirement and verified by a test.

| RISK | Hazard (short) | Controlling REQ(s) | Verification TST(s) | Residual (RMF-RA-001) |
|---|---|---|---|---|
| RISK-001 | False negative | REQ-004, REQ-010, REQ-020, REQ-022, REQ-030, REQ-031 | TST-018, TST-012, TST-004 | Undesirable -> Tolerable-AFAP |
| RISK-002 | False positive | REQ-002, REQ-011 | TST-019 | Tolerable |
| RISK-003 | OOD input as valid | REQ-020, REQ-021, REQ-023 | TST-012, TST-021 | Undesirable -> Tolerable-AFAP |
| RISK-004 | Subgroup/Fitzpatrick bias | REQ-010, REQ-013, REQ-023 | TST-018; PMS monitoring | Undesirable -> Tolerable-AFAP |
| RISK-005 | Automation bias | REQ-030, REQ-031, REQ-032 | TST-004, TST-031, TST-009 | Undesirable -> Tolerable-AFAP |
| RISK-006 | Dataset shift | REQ-040, REQ-041 | TST-040; PMS monitoring | Undesirable -> Tolerable-AFAP |
| RISK-007 | Miscalibration | REQ-004, REQ-012 | TST-020 | Tolerable |
| RISK-008 | Adversarial/corrupted input | REQ-051, REQ-052, REQ-054 | TST-022, TST-054 | Tolerable |
| RISK-009 | Use-error | REQ-032, REQ-060 | TST-009 | Tolerable |
| RISK-010 | Data loss/leak | REQ-042, REQ-050, REQ-053 | TST-023 | Acceptable |

## 4. EU AI Act Annex IV / article coverage

Confirms each mapped high-risk obligation has a documentary or requirement anchor.

| AI Act article | Obligation | Anchor in this file set |
|---|---|---|
| Art. 9 | Risk management system | RMF-* (integrated ISO 14971 file) |
| Art. 10 | Data and data governance | data_governance.md, dataset_card.md (build phase 7) |
| Art. 11 | Technical documentation (Annex IV) | eu_ai_act/ (build phase 6) |
| Art. 12 | Logging / record-keeping | REQ-040, REQ-041, REQ-042 |
| Art. 13 | Transparency / instructions | REQ-030, REQ-033 |
| Art. 14 | Human oversight | REQ-031, REQ-032; IU-001 |
| Art. 15 | Accuracy, robustness, cybersecurity | REQ-010..013 (accuracy), REQ-051, REQ-052 (robustness/security) |

## 5. Test index

| TST | Verifies (short) | REQ(s) | Method (planned) | Status |
|---|---|---|---|---|
| TST-001 | Input format/resolution validation | REQ-001 | Unit/integration | Planned |
| TST-002 | Calibrated risk-band output, no bare verdict | REQ-002 | Integration | Planned |
| TST-003 | Single-lesion handling | REQ-003 | Integration | Planned |
| TST-004 | Disclaimer present on every response | REQ-030 | API contract test | Planned |
| TST-009 | Output presentation usability (use-error, anti-automation-bias) | REQ-032, REQ-060 | Usability evaluation (IEC 62366-1) | Planned |
| TST-012 | OOD rejection / unsupported-input notice | REQ-020 | System test | Planned |
| TST-014 | Latency target | REQ-014 | Performance test | Planned |
| TST-018 | Sensitivity overall and per Fitzpatrick subgroup | REQ-010, REQ-013 | Evaluation on independent test set | Planned |
| TST-019 | Specificity / AUROC with CIs | REQ-011 | Evaluation on independent test set | Planned |
| TST-020 | Calibration (ECE) and confidence output | REQ-004, REQ-012 | Evaluation | Planned |
| TST-021 | Image-quality gate; scope/limitation guard | REQ-021, REQ-023 | System test | Planned |
| TST-022 | Robustness to perturbed/corrupted input; input validation | REQ-051, REQ-052 | Robustness/metamorphic test | Planned |
| TST-022a | Low-confidence/OOD warning content | REQ-022 | System test | Planned |
| TST-023 | Auth, encryption, tamper-evident logs, data protection | REQ-042, REQ-050, REQ-053 | Security test | Planned |
| TST-031 | No autonomous action on output | REQ-031 | System/design test | Planned |
| TST-033 | IFU/labelling content review | REQ-033, REQ-061 | Document review | Planned |
| TST-040 | Inference logging; model/data version binding | REQ-040, REQ-041 | Integration test | Planned |
| TST-054 | Rate limiting / output minimization | REQ-054 | Security test | Planned |

## 6. Coverage and orphan check

- **Every RISK (001-010)** maps to at least one REQ and one verification (Section 3): no orphan
  risks.
- **Every REQ (Section 2)** has a source and a test: no orphan requirements.
- **Every TST (Section 5)** maps to at least one REQ: no orphan tests.
- **RISK-004 and RISK-006** additionally rely on post-market monitoring (PMS), not on a release test
  alone; this is intentional and flagged for the PMS plan (build phase 10).
- Items needing closure before finalization: architecture.md component confirmation; execution of
  all TST-XXX; replacement of "Planned" with actual V&V results.

## 7. Change history

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-06-27 | Akhila N Pillai | Initial draft (simulation): full REQ/RISK/TST spine + AI Act coverage |
