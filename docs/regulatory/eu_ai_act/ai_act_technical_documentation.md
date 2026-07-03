# EU AI Act Technical Documentation (Annex IV)

> SIMULATION / TRAINING EXERCISE. DermaScan is a personal portfolio project, NOT a certified
> medical device and NOT a conformity-assessed AI system. No real clinical use. Content is written
> in submission style for learning.

| Field | Value |
|---|---|
| Document ID | AIA-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Akhila N Pillai |
| Date | 2026-06-27 |
| Reviewed by | - |
| Approved by | - |

**Regulation:** EU AI Act (Regulation (EU) 2024/1689), Annex IV; Articles 6, 9-15, 72.
**Related:** CLS-001 (high-risk basis), IU-001, RMF-*, SRS-001, SSC-001, TRC-001,
data_governance.md (DG-001), dataset_card.md (DSC-001). **Study reference:** `steps/step-06-eu-ai-act.html`.

---

## 0. How to read this document

The EU AI Act is designed to integrate with the MDR rather than duplicate it (Art. 8(2)). This file
is therefore an **index and gap-closing layer** over the existing MDR/ISO documentation: where an
Annex IV point is already satisfied by another document, this file points to it and adds only the
AI-specific content. The intent is a single integrated technical file and a single conformity
assessment.

## 1. High-risk status (basis)

DermaScan is a high-risk AI system under **Art. 6(1)**: it is (a safety component of) a product
covered by EU harmonisation law listed in Annex I (the MDR) and that product requires third-party
conformity assessment (Class IIa, Notified Body). Full reasoning: CLS-001 Section 6.

---

## 2. Annex IV Point 1 - General description of the AI system

| Item | Content |
|---|---|
| Intended purpose | See IU-001 (decision-support triage of pigmented skin lesions; output is a malignancy-risk estimate; user is a qualified clinician; not a diagnosis) |
| Provider (simulated) | DermaScan project (portfolio) |
| System version | 0.x (pre-release, simulation) |
| How it works (high level) | A trained image-classification model estimates malignancy likelihood from a dermoscopic/clinical image; served via a FastAPI inference API |
| Interaction with other software/hardware | Standalone software (SaMD); runs on standard compute (CPU/GPU); consumed via API by the deployer's clinical workflow |
| Forms of deployment | Software service/API (no hardware product) |
| Instructions for use to the deployer | See IU-001 Sections 10-12 and REQ-033 (IFU content) |

## 3. Annex IV Point 2 - Detailed description: elements and development process

### 3.1 Development methods and steps
Incremental software lifecycle per IEC 62304 (SDP-001). The trained model and its datasets are
versioned configuration items (SDP-001 Section 5).

### 3.2 System architecture
See architecture.md (pending, build phase 9) and the intended component decomposition in TRC-001
Section 2 (input handler, image-quality/OOD module, model/inference, calibration, response schema
with disclaimer, logging, security).

### 3.3 Data and data governance (Art. 10)
The training, validation, and test data, their provenance, characteristics, labelling, preparation,
and the bias examination are described in **DG-001 (data_governance.md)** and **DSC-001
(dataset_card.md)**. Summary: only public licensed dermoscopic datasets are used; a known
representativeness gap for darker skin phototypes is documented and controlled (RISK-004).

### 3.4 Human oversight (Art. 14)
Oversight is designed in, not added on: the output is decision-support only and cannot trigger
autonomous action (REQ-031); confidence and uncertainty are surfaced (REQ-004, REQ-032); a mandatory
"not a diagnosis" disclaimer appears on every output (REQ-030); and the design counters automation
bias (RISK-005, REQ-032, verified by the usability evaluation TST-009). The deployer must ensure a
qualified clinician reviews and is accountable for every decision (IU-001).

### 3.5 Validation and testing - metrics (Art. 15)
- **Accuracy:** sensitivity overall and per Fitzpatrick subgroup (REQ-010, REQ-013, TST-018),
  specificity and AUROC with confidence intervals (REQ-011, TST-019), calibration/ECE (REQ-012,
  TST-020). No single aggregate accuracy figure is used as a claim.
- **Robustness:** resilience to perturbed/corrupted input and metamorphic invariance (REQ-051,
  REQ-052, TST-022); out-of-distribution handling (REQ-020, TST-012).
- **Cybersecurity:** authentication, input validation, encryption, tamper-evident logging, rate
  limiting (REQ-050 to REQ-054); see also cybersecurity (build phase 11) and AI-specific threats
  (data/model poisoning, adversarial examples, model inversion).
- Targets are defined as acceptance criteria in SRS-001 (some values are placeholders pending the
  clinical evaluation, build phase 8).

### 3.6 Logging and record-keeping (Art. 12)
Automatic event logging with timestamp, model version, input reference/hash, and result (REQ-040);
each result bound to the exact model and dataset version for reproducibility (REQ-041); tamper-
evident log storage (REQ-042, TST-040, TST-023).

### 3.7 Predetermined changes / continuous learning
DermaScan is **not** a continuously-learning system in deployment. Retraining is a controlled change
(SDP-001 Section 8) governed by a predetermined change control plan (PCCP) that pre-authorises
bounded model updates with mandatory re-validation and recalibration. Any change outside the PCCP
bounds requires re-assessment.

## 4. Annex IV Point 3 - Monitoring, functioning and control

- **Capabilities and limitations:** stated in IU-001 (Sections 8-10), including the validated
  population, image modality, and phototype range, and the reduced reliability outside it.
- **Expected accuracy and foreseeable unintended outcomes:** the accuracy metrics above; foreseeable
  unintended outcomes (false negative, false positive, biased subgroup performance, automation bias,
  drift) are analysed in RMF-RA-001.
- **Human oversight measures:** Section 3.4.
- **Input data specifications:** REQ-001, REQ-021 (format, resolution, image-quality criteria).

## 5. Annex IV Point 4 - Appropriateness of performance metrics

Sensitivity is prioritised because a false negative (missed malignancy) is the most serious harm
(RMF-RA-001 RISK-001); specificity, AUROC, calibration, and per-subgroup metrics are reported to
characterise false positives, ranking quality, probability reliability, and fairness. Rationale is
detailed in clinical_evaluation.md (build phase 8) and the SRS performance requirements.

## 6. Annex IV Point 5 - Risk management system (Art. 9)

Implemented as the single integrated ISO 14971 risk file (RMF-PLAN-001, RMF-RA-001, RMF-RPT-001),
which explicitly covers AI-specific hazards and is intended to satisfy both ISO 14971/MDR and
AI Act Art. 9. No separate parallel AI risk file is maintained, to avoid divergence.

## 7. Annex IV Point 6 - Changes through the lifecycle

Tracked via configuration management and change control (SDP-001 Sections 4, 8) and the document
change-history tables. Model/data version changes are bound to results (REQ-041) and assessed
against the risk file before release.

## 8. Annex IV Point 7 - Harmonised standards applied

| Area | Standard |
|---|---|
| Risk management | ISO 14971:2019 (with ISO/TR 24971) |
| Software lifecycle | IEC 62304:2006+A1:2015 |
| Quality management | ISO 13485:2016 (discipline; see qms/) |
| AI management | ISO/IEC 42001:2023 (AI management system) |
| Usability | IEC 62366-1 |
| Health software security | IEC 81001-5-1 |

> Note (currency): dedicated **harmonised standards for the AI Act high-risk requirements are still
> under development** by CEN-CENELEC, so a full presumption-of-conformity route for the AI-specific
> obligations is not yet available; the standards above and ISO/IEC 42001 are applied as best
> practice in the interim. This gap is part of the rationale for the Digital Omnibus timeline
> discussion (see step-06, step-13).

## 9. Annex IV Point 8 - EU Declaration of Conformity

Not applicable in this simulation (no conformity assessment performed; no certificate; no CE mark).
In a real submission this would reference the integrated MDR + AI Act Declaration of Conformity. See
technical_documentation/ (build phase 12) for the simulated route.

## 10. Annex IV Point 9 - Post-market monitoring plan (Art. 72)

The post-market monitoring of the AI system is integrated with the MDR PMS/PMCF plan (build phase
10). For the AI system specifically it shall monitor live and per-subgroup performance and model
drift (RISK-004, RISK-006) with predefined thresholds that trigger CAPA or controlled retraining
under the PCCP. Serious incidents are reported per Art. 73 (and MDR vigilance).

## 11. Roles (Art. 3)

- **Provider:** the (simulated) DermaScan manufacturer - holds the obligations documented here.
- **Deployer:** the clinic/clinician using the output - must ensure human oversight, use per the
  instructions, and monitor performance (IU-001).

## 12. Open items

- Confirm architecture.md (Section 3.2).
- Finalise accuracy/robustness targets after the clinical evaluation (Section 3.5).
- Complete DG-001 and DSC-001 (Section 3.3) - addressed in build phase 7.
- Define the PCCP bounds (Section 3.7) and the AI post-market monitoring thresholds (Section 10).

## 13. Change history

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-06-27 | Akhila N Pillai | Initial draft (simulation): Annex IV structure mapped to integrated MDR/ISO file set |
