# Risk Management Report (Preliminary)

> SIMULATION / TRAINING EXERCISE. DermaScan is a personal portfolio project, NOT a certified
> medical device. No real clinical use. Content is written in submission style for learning.

| Field | Value |
|---|---|
| Document ID | RMF-RPT-001 |
| Version | 0.1 |
| Status | Draft - PRELIMINARY (pending V&V and clinical evaluation) |
| Author | Akhila N Pillai |
| Date | 2026-06-27 |
| Reviewed by | - |
| Approved by | - |

**Standard:** ISO 14971:2019 clause 9 (risk management report) and clause 8 (overall residual risk).
**Related:** RMF-PLAN-001, RMF-RA-001, IU-001, clinical_evaluation.md (pending),
verification_validation/ (pending). **Study reference:** `steps/step-03-iso14971-risk.html`.

---

## 1. Purpose and status

This report concludes the risk management process for DermaScan per ISO 14971:2019. It is
**preliminary**: the verification evidence (TST-XXX) and the clinical evaluation that substantiate
control effectiveness and clinical benefit are produced in later build phases (9 and 8). The
benefit-risk conclusion below is therefore **provisional** and must be re-confirmed once that
evidence exists.

## 2. Confirmation that the plan was implemented

The risk management activities defined in RMF-PLAN-001 were carried out: characteristics related to
safety and foreseeable misuse were identified (RMF-RA-001 Sections 1-2), hazards and hazardous
situations were identified including AI/ML-specific sources (Section 3), risks were estimated and
evaluated (Section 4), and risk controls were selected following the ISO 14971 priority order.

## 3. Overall residual risk evaluation

- Ten individual risks (RISK-001 to RISK-010) were assessed. After controls, lower-severity risks
  (RISK-002, 007, 008, 009, 010) reach Acceptable or Tolerable.
- Five risks tied to a missed malignancy (RISK-001, 003, 004, 005, 006) retain a residual level of
  Undesirable because the severity S4 is intrinsic and cannot be lowered; their probability is
  reduced and they are accepted only as **Tolerable-AFAP**.
- The decisive control for these is **external to the software**: an independent qualified clinician
  confirms every output (IU-001). The overall residual risk is dominated by these items and is
  therefore conditional on that clinician-review control being credible in real use.

## 4. Benefit-risk determination (provisional)

The intended clinical benefit is earlier and better-informed triage of pigmented lesions as an
adjunct to clinician assessment. **Provisionally**, the residual risks are judged acceptable in
relation to this benefit, **on the conditions that**:
1. the clinical evaluation demonstrates adequate sensitivity/specificity, calibration, and
   per-subgroup performance on an independent (preferably external) test set;
2. the device is used strictly within the validated population, image modality, and phototype range
   declared in IU-001;
3. mandatory independent clinician review is preserved in deployment.

If condition 1 is not met, the benefit-risk conclusion does not hold and the intended use,
classification, or controls must be revised.

## 5. Information disclosed to users

Residual risks and limitations are disclosed to users via the IFU and the mandatory on-output
disclaimer (IU-001 Sections 10-12), satisfying the "information for safety" controls and AI Act
Art. 13 transparency expectations.

## 6. Inputs to production and post-production

The post-market surveillance plan (build phase 10) shall monitor real-world and per-subgroup
performance and model drift (RISK-004, RISK-006), with thresholds that trigger CAPA or controlled
retraining under a predetermined change control plan. Post-market data feeds back into RMF-RA-001.

## 7. Open items before this report can be finalized

- Complete SRS requirements (REQ-XXX) for each control and the traceability matrix.
- Execute and record verification (TST-012, TST-018, TST-019, TST-020, TST-021, TST-022, TST-023).
- Complete the clinical evaluation, including subgroup performance.
- Re-issue this report as Version 1.0 with the benefit-risk conclusion confirmed.

## 8. Change history

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-06-27 | Akhila N Pillai | Initial preliminary draft (simulation) |
