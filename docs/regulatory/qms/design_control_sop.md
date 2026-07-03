# SOP: Design and Development Control

> SIMULATION / TRAINING EXERCISE. DermaScan is a personal portfolio project, NOT a certified
> medical device and NOT a certified QMS. This SOP borrows ISO 13485 discipline for learning.

| Field | Value |
|---|---|
| Document ID | SOP-DESIGN-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Akhila N Pillai |
| Date | 2026-06-27 |
| Reviewed by | - |
| Approved by | - |

**Standard:** ISO 13485:2016 clause 7.3 (design and development); aligned with IEC 62304.
**Related:** IU-001, SRS-001, ARC-001, TRC-001, SDP-001, verification_validation/ (pending),
SOP-DC-001, SOP-CAPA-001. **Study reference:** `steps/step-05-iso13485-qms.html` and
`step-09-verification-validation.html`.

---

## 1. Purpose

To define the controlled design and development process for DermaScan, so the device is developed
against defined inputs, with traceable outputs, reviews, verification, validation, and change
control, forming a design file.

## 2. The design control flow and where each artifact lives

| Stage (ISO 13485 7.3) | Question | DermaScan artifact |
|---|---|---|
| 7.3.2 Planning | What, who, when | SDP-001 (software development plan) |
| 7.3.3 Design inputs | What must it do/be safe against | IU-001 (user needs), RMF-RA-001 (risk controls), SRS-001 (REQ-XXX) |
| 7.3.4 Design outputs | The realized design | ARC-001 (architecture), detailed design, source code |
| 7.3.5 Design review | Is it on track and correct | Documented reviews at defined milestones |
| 7.3.6 Verification | Outputs meet inputs (built it right) | Tests TST-XXX, recorded in verification_validation/ and TRC-001 |
| 7.3.7 Validation | Meets user needs / intended use (right thing) | Usability evaluation, clinical validation (CLIN-001) |
| 7.3.8 Transfer | Ready for production/release | Release record (IEC 62304 5.8) |
| 7.3.9 Design changes | Controlled change | Section 4 below + SOP-DC-001 |
| 7.3.10 Design file | The whole record | The `docs/` tree + repository history |

## 3. Inputs, outputs, and traceability

- **Design inputs** are derived from the intended use (IU-001) and risk controls (RMF-RA-001) and
  written as testable requirements (SRS-001, REQ-XXX).
- **Design outputs** (architecture, detailed design, code) must satisfy the inputs and provide the
  information needed for purchasing, production, and servicing (here: SOUP control, release).
- **Traceability** from need/risk to requirement to design to test is maintained in TRC-001; there
  must be no orphan requirements or risks.

## 4. Design change control

Any design change (including model retraining) is: described and risk-assessed; checked for impact
on inputs, outputs, the risk file, clinical evaluation, and traceability; implemented and
re-verified/validated for affected items; and documented under SOP-DC-001. Model changes follow the
predetermined change control plan (PCCP). Significant changes may affect classification (CLS-001)
and must be re-evaluated.

## 5. Reviews

Design reviews occur at defined milestones (e.g. after requirements, after architecture, before
release). A review confirms the design meets requirements, risks are controlled and verified, and
open issues have owners. Review outcomes are recorded.

## 6. Verification and validation distinction (reinforced)

- **Verification** confirms design outputs meet design inputs (against the specification).
- **Validation** confirms the device meets user needs and intended use in the intended setting.
Both are required; both trace through TRC-001.

## 7. Change history

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-06-27 | Akhila N Pillai | Initial draft (simulation): design control flow mapped to project artifacts |
