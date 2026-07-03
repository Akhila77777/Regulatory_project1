# Risk Analysis and Risk Control Register

> SIMULATION / TRAINING EXERCISE. DermaScan is a personal portfolio project, NOT a certified
> medical device. No real clinical use. Content is written in submission style for learning.

| Field | Value |
|---|---|
| Document ID | RMF-RA-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Akhila N Pillai |
| Date | 2026-06-27 |
| Reviewed by | - |
| Approved by | - |

**Standard:** ISO 14971:2019. **Scales and acceptability:** see RMF-PLAN-001 Section 3.
**Related:** IU-001, RMF-PLAN-001, RMF-RPT-001, srs.md, traceability_matrix.md.
**Study reference:** `steps/step-03-iso14971-risk.html`.

> Verification links (TST-XXX) and requirement links (REQ-XXX) are forward references to the SRS and
> verification & validation files, which are created in build phase 9. Until those exist, the links
> denote planned verification, not completed evidence.

---

## 1. Characteristics related to safety (ISO 14971 Annex A inputs)

- DermaScan is decision-support SaMD; the intended user is a qualified clinician who independently
  confirms every output (IU-001).
- The model is trained/validated only on public dermoscopic datasets, which under-represent darker
  skin phototypes (dataset_card.md).
- Output is a malignancy-risk estimate; the principal safety concern is an erroneous estimate that
  influences a clinical decision.

## 2. Foreseeable misuse considered

- Using the output as a stand-alone diagnosis without clinician confirmation.
- Submitting unsupported inputs (non-dermoscopic, poor quality, non-pigmented lesions).
- Using the tool for patient self-assessment or for population screening.
- Over-reliance on a confident-looking output (automation bias).

## 3. Hazard list (HAZ)

| ID | Hazard category |
|---|---|
| HAZ-01 | Erroneous output (incorrect malignancy estimate) |
| HAZ-02 | Output outside validated operating range presented as valid |
| HAZ-03 | Biased performance across demographic subgroups |
| HAZ-04 | Loss of human oversight / over-reliance |
| HAZ-05 | Performance degradation over time (dataset shift) |
| HAZ-06 | Compromised input or model (security) |
| HAZ-07 | Use-error from unclear output presentation |
| HAZ-08 | Loss/leak of personal health data |

## 4. Risk register (summary)

S = severity, P = probability (see RMF-PLAN-001 3.1/3.2). Risk level per the matrix in
RMF-PLAN-001 3.3.

| Risk ID | Hazard | Harm | Pre S | Pre P | Pre level | Controls (summary) | Post S | Post P | Post level | Verification |
|---|---|---|---|---|---|---|---|---|---|---|
| RISK-001 | False negative (missed malignancy) | Delayed treatment, disease progression | S4 | P3 | Undesirable | OOD rejection; high-sensitivity threshold; low-confidence warning; mandatory clinician review; IFU limits | S4 | P2 | Undesirable* | TST-018, TST-012 |
| RISK-002 | False positive (benign flagged malignant) | Unnecessary anxiety / biopsy | S3 | P3 | Undesirable | Calibrated probability not binary verdict; clinician review; report specificity | S3 | P2 | Tolerable | TST-019 |
| RISK-003 | OOD / unsupported input scored as valid | Clinician misled by invalid output | S4 | P3 | Undesirable | OOD detector; image-quality gate; explicit unsupported-input notice | S4 | P2 | Undesirable* | TST-012, TST-021 |
| RISK-004 | Reduced sensitivity for under-represented skin tones (bias) | Group-specific delayed diagnosis | S4 | P3 | Undesirable | Subgroup evaluation; stated validated Fitzpatrick range; phototype limitation in IFU; post-market subgroup monitoring | S4 | P2 | Undesirable* | TST-018, PMS |
| RISK-005 | Automation bias / over-reliance | Clinician defers judgement, missed diagnosis | S4 | P3 | Undesirable | Decision-support framing; confidence display; "not a diagnosis" disclaimer; oversight-by-design (AI Act Art.14) | S4 | P2 | Undesirable* | TST-004, usability |
| RISK-006 | Dataset shift / silent degradation | Gradual rise in errors | S4 | P3 | Undesirable | Versioned model+data; post-market drift monitoring with thresholds; predetermined change control plan | S4 | P2 | Undesirable* | PMS |
| RISK-007 | Miscalibrated confidence | Confidence misleads decision | S3 | P3 | Undesirable | Calibration assessment; calibration acceptance criterion; recalibration on retrain | S3 | P2 | Tolerable | TST-020 |
| RISK-008 | Adversarial / corrupted input | Manipulated output | S4 | P2 | Undesirable | Input validation; robustness testing; access control; logging | S4 | P1 | Tolerable | TST-022 |
| RISK-009 | Unclear output presentation (use-error) | Misinterpretation | S3 | P3 | Undesirable | Usability engineering (IEC 62366-1); unambiguous risk-band + disclaimer | S3 | P2 | Tolerable | usability |
| RISK-010 | Personal health data loss/leak | Privacy harm | S3 | P2 | Tolerable | No real patient data (simulation); encryption; minimization; access control (GDPR Art.32) | S2 | P2 | Acceptable | TST-023 |

\* RISK-001, 003, 004, 005, 006 retain residual level Undesirable because the severity of a missed
malignancy (S4) cannot be lowered, only its probability. They are accepted only as Tolerable-AFAP
on the explicit basis that an **independent qualified clinician confirms every output** (a control
external to the software) and that the clinical benefit outweighs the residual risk. This benefit-
risk justification is recorded in RMF-RPT-001. This dependence on clinician review is also the
pivotal argument in the IEC 62304 software-safety-class decision (see iec62304/).

## 5. Detailed risk items (selected)

### RISK-001 - False negative (missed malignancy)
- **Hazard (HAZ-01):** erroneous low-malignancy output.
- **Sequence of events:** a malignant lesion (possibly rare presentation or under-represented
  phototype) is imaged -> model produces a low malignancy estimate with apparent confidence ->
  result displayed.
- **Hazardous situation:** clinician under-triages and defers biopsy/referral.
- **Harm:** delayed diagnosis and treatment of melanoma; disease progression. Severity S4.
- **Pre-control risk:** S4 x P3 = Undesirable.
- **Risk controls (in priority order):**
  1. Inherently safe design: out-of-distribution detector rejects unsupported inputs; operating
     threshold tuned for high sensitivity for the triage purpose.
  2. Protective measure: low-confidence warning; output framed as decision-support requiring
     mandatory independent clinician review; calibrated probability rather than a binary "benign".
  3. Information for safety: IFU states validated population/image type and that a low/OOD result
     is not "low risk".
- **Linked requirements:** REQ (sensitivity target), REQ (OOD rejection), REQ (disclaimer).
- **Verification:** TST-018 (subgroup sensitivity on independent test set), TST-012 (OOD rejection).
- **Post-control risk:** S4 x P2 = Undesirable, accepted as Tolerable-AFAP on the basis of
  mandatory clinician review and demonstrated benefit (RMF-RPT-001).
- **New risks introduced:** a too-aggressive OOD/high-sensitivity setting increases false positives
  (see RISK-002); accepted as the lower-severity trade-off.

### RISK-004 - Demographic / Fitzpatrick bias
- **Hazard (HAZ-03):** systematically lower sensitivity for under-represented skin phototypes.
- **Sequence:** training/validation data dominated by lighter skin (Fitzpatrick I-III) -> model
  generalizes poorly to IV-VI -> elevated false-negative rate for those patients.
- **Hazardous situation:** clinician relies on an output that is less reliable for that patient
  group.
- **Harm:** group-specific delayed diagnosis (S4); also an equity/discrimination concern under AI
  Act Art. 10.
- **Pre-control risk:** S4 x P3 = Undesirable.
- **Controls:** measure and report per-Fitzpatrick performance; state the validated phototype range
  in IU-001; declare unsupported phototypes as a limitation/contraindication; collect and monitor
  subgroup performance in post-market surveillance; address gaps via additional data under change
  control.
- **Verification:** TST-018 (per-subgroup metrics); PMS subgroup monitoring.
- **Post-control risk:** S4 x P2 = Undesirable, Tolerable-AFAP within the declared validated range.

### RISK-005 - Automation bias / loss of human oversight
- **Hazard (HAZ-04):** clinician over-trusts the output.
- **Sequence:** confident-looking output -> clinician reduces independent scrutiny -> error
  propagates.
- **Harm:** missed or wrong decision (up to S4).
- **Controls:** human-oversight-by-design per AI Act Art. 14 (output is adjunct, never autonomous);
  confidence and uncertainty surfaced; mandatory "not a diagnosis" disclaimer on every output;
  user-facing framing that prompts independent assessment.
- **Verification:** TST-004 (disclaimer present on every response), usability evaluation of
  oversight effectiveness.

## 6. Completeness and traceability

Every risk control above is to be expressed as one or more requirements (REQ-XXX) in the SRS and
verified by a test (TST-XXX), with the chain recorded in traceability_matrix.md. No risk control
relies solely on "information for safety" where a higher-priority control is reasonably practicable.

## 7. Change history

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-06-27 | Akhila N Pillai | Initial draft (simulation): scales, 10-item register, detailed items |
