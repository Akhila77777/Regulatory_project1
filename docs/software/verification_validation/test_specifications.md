# Test Specifications

> SIMULATION / TRAINING EXERCISE. DermaScan is a personal portfolio project, NOT a certified
> medical device. No real clinical use. Tests are specified but not yet executed; the Result field
> is "Planned" until run.

| Field | Value |
|---|---|
| Document ID | VV-TS-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Akhila N Pillai |
| Date | 2026-07-03 |
| Reviewed by | - |
| Approved by | - |

**Related:** VV-001 (V&V plan), SRS-001 (REQ-XXX), TRC-001 (test index), RMF-RA-001 (RISK-XXX),
ARC-001. **Study reference:** `steps/step-09-verification-validation.html`.

> Each spec lists: verifies (REQ) / risk link / level / preconditions / data / procedure /
> acceptance criterion / result. "(placeholder)" numeric values are confirmed against CLIN-001
> before execution. Result = Planned for all until executed.

---

## Functional

### TST-001 - Input format and resolution validation
- Verifies: REQ-001 | Level: unit/integration
- Preconditions: input handler (ARC-001 C2) under config control.
- Data: valid images (supported formats, >= min resolution); invalid (wrong format, too small,
  corrupt).
- Procedure: submit each input; observe acceptance/rejection and message.
- Acceptance: all valid accepted; all invalid rejected with a clear reason; no crash on corrupt file.
- Result: Planned.

### TST-002 - Calibrated risk-band output (no bare verdict)
- Verifies: REQ-002 | Risk: RISK-002 | Level: integration
- Data: representative valid images.
- Procedure: inspect response payload.
- Acceptance: output is a probability/risk band with the disclaimer; no bare binary "benign/
  malignant" verdict is returned.
- Result: Planned.

### TST-003 - Single-lesion handling
- Verifies: REQ-003 | Level: integration
- Data: single-lesion, multi-lesion, and no-lesion images.
- Procedure: submit each; observe handling.
- Acceptance: exactly one lesion processed; multi/no-lesion cases flagged, not silently scored.
- Result: Planned.

## Human oversight / transparency

### TST-004 - Disclaimer present on every response
- Verifies: REQ-030 | Risk: RISK-005 | Level: system (API contract)
- Data: a broad set of valid, invalid, OOD, and error requests.
- Procedure: assert the disclaimer field is present and correct in every response, including error
  and rejection responses.
- Acceptance: 100% of responses carry the mandatory disclaimer.
- Result: Planned.

### TST-031 - No autonomous action on output
- Verifies: REQ-031 | Risk: RISK-005 | Level: system/design review
- Procedure: review interfaces and behavior for any automated triage/referral/treatment action.
- Acceptance: no autonomous downstream action exists; output is advisory only.
- Result: Planned.

### TST-009 - Output presentation usability (use-error, anti-automation-bias)
- Verifies: REQ-032, REQ-060 | Risk: RISK-009, RISK-005 | Level: validation (IEC 62366-1)
- Data: representative users; scenario tasks incl. a low-confidence/OOD case.
- Procedure: usability evaluation; observe interpretation and whether users retain independent
  judgement.
- Acceptance: no critical use-errors; users correctly interpret risk band, confidence, and warnings
  and treat output as adjunct.
- Result: Planned.

### TST-033 - IFU / labelling content review
- Verifies: REQ-033, REQ-061 | Level: document review
- Procedure: check IFU against IU-001 for capabilities, limitations, validated performance, intended
  user, oversight, and security information (CYB-001 Section 9).
- Acceptance: all required content present and consistent; clinician-only use stated.
- Result: Planned.

## Performance (model evaluation)

### TST-018 - Sensitivity overall and per Fitzpatrick subgroup
- Verifies: REQ-010, REQ-013 | Risk: RISK-001, RISK-004 | Level: performance
- Data: independent test set with Fitzpatrick labels (DSC-001); no leakage.
- Procedure: compute sensitivity overall and per phototype at the defined operating threshold, with
  95% CIs.
- Acceptance: sensitivity >= 0.90, 95% CI lower bound >= 0.85 (placeholder), overall and per
  reported subgroup; subgroups below criterion are excluded from validated use.
- Result: Planned.

### TST-019 - Specificity and AUROC with confidence intervals
- Verifies: REQ-011 | Risk: RISK-002 | Level: performance
- Data: independent test set.
- Procedure: compute specificity and AUROC with 95% CIs.
- Acceptance: specificity and AUROC at or above defined minima (placeholder).
- Result: Planned.

### TST-020 - Calibration (ECE) and confidence output
- Verifies: REQ-004, REQ-012 | Risk: RISK-007 | Level: performance
- Data: independent test set.
- Procedure: compute expected calibration error; verify confidence and low-confidence flag are
  returned.
- Acceptance: ECE <= threshold (placeholder); confidence present; low-confidence flag triggers
  correctly.
- Result: Planned.

### TST-014 - Latency target
- Verifies: REQ-014 | Level: performance
- Procedure: measure end-to-end response time under specified conditions.
- Acceptance: within the latency target (placeholder).
- Result: Planned.

## Safety

### TST-012 - Out-of-distribution rejection / unsupported-input notice
- Verifies: REQ-020 | Risk: RISK-003, RISK-001 | Level: system
- Data: OOD probe set (non-dermoscopic images, unseen categories, noise).
- Procedure: submit OOD inputs.
- Acceptance: OOD inputs are not scored; an explicit unsupported-input notice is returned; rejection
  rate >= defined minimum (placeholder).
- Result: Planned.

### TST-021 - Image-quality gate and scope/limitation guard
- Verifies: REQ-021, REQ-023 | Risk: RISK-003, RISK-004 | Level: system
- Data: poor-quality images; inputs outside validated modality/phototype range.
- Procedure: submit each.
- Acceptance: poor-quality rejected/flagged; out-of-scope inputs surface the applicable limitation.
- Result: Planned.

### TST-022a - Low-confidence / OOD warning content
- Verifies: REQ-022 | Risk: RISK-001 | Level: system
- Procedure: trigger low-confidence and OOD cases; inspect warning text.
- Acceptance: warning clearly states a low-confidence/OOD result must not be read as "low risk".
- Result: Planned.

## Security

### TST-022 - Robustness to perturbed/corrupted input; input validation
- Verifies: REQ-051, REQ-052 | Risk: RISK-008 | Level: security/robustness
- Data: malformed inputs; small label-preserving perturbations; adversarial probes.
- Procedure: submit; observe output stability and failure behavior.
- Acceptance: no unsafe output on malformed input; measured robustness within tolerance
  (placeholder); graceful handling.
- Result: Planned.

### TST-023 - Auth, encryption, tamper-evident logs, data protection
- Verifies: REQ-042, REQ-050, REQ-053 | Risk: RISK-010 | Level: security
- Procedure: attempt unauthenticated/unauthorized access; verify encryption in transit/at rest;
  attempt log modification.
- Acceptance: access denied without valid auth; data encrypted; log tampering detectable.
- Result: Planned.

### TST-054 - Rate limiting / output minimization
- Verifies: REQ-054 | Risk: RISK-008 | Level: security
- Procedure: exceed request-rate limits; inspect output detail.
- Acceptance: rate limiting enforced; output does not expose extraction-enabling internals.
- Result: Planned.

## Record-keeping

### TST-040 - Inference logging and model/data version binding
- Verifies: REQ-040, REQ-041 | Risk: RISK-006 | Level: integration
- Procedure: run inferences; inspect logs.
- Acceptance: each event logs timestamp, model version, dataset version, input hash, and result;
  a result is reproducible from the recorded versions.
- Result: Planned.

## Coverage note

Every TST above maps to at least one REQ and appears in the TRC-001 test index; every RISK with a
release-testable control is covered here. RISK-004 and RISK-006 are additionally covered by
post-market monitoring (PMS-001), not by a release test alone.

## Change history

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-07-03 | Akhila N Pillai | Initial draft (simulation): specs for 18 tests, all Planned |
