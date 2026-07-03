# Data Governance (EU AI Act Article 10)

> SIMULATION / TRAINING EXERCISE. DermaScan is a personal portfolio project, NOT a certified
> medical device. No real clinical use. Content is written in submission style for learning.

| Field | Value |
|---|---|
| Document ID | DG-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Akhila N Pillai |
| Date | 2026-06-27 |
| Reviewed by | - |
| Approved by | - |

**Regulation:** EU AI Act Art. 10; GDPR (Art. 9, Art. 32). **Related:** dataset_card.md (DSC-001),
AIA-001 (Section 3.3), RMF-RA-001 (RISK-004), SRS-001 (REQ-010, REQ-013, REQ-023).
**Study reference:** `steps/step-07-data-governance-bias.html`.

---

## 1. Purpose and scope

This document defines the data-governance practices for the datasets used to train, validate, and
test DermaScan, as required by EU AI Act Article 10. It records design choices, provenance,
preparation, suitability, and the examination for and mitigation of bias. The per-dataset detail is
in the dataset card (DSC-001).

## 2. Design choices and data requirements

- **Task:** binary/risk-band classification of pigmented skin lesions for malignancy likelihood.
- **Modality:** dermoscopic images (and standardised clinical images where validated).
- **Population fit:** the data must be representative of the intended population and setting declared
  in IU-001; gaps constrain the validated intended use.
- **Splits:** strictly separated train / validation / test sets; the test set is independent and
  used only for final evaluation. External validation (data from a different source/site) is sought
  where feasible.

## 3. Data sources and provenance

Only **public, properly licensed** dermoscopic datasets are used: HAM10000, ISIC Archive,
BCN20000, PH2. Provenance, licence, size, class distribution, modality, and demographic composition
of each are recorded in DSC-001. No real patient data is collected by this project.

## 4. Data preparation

- **Labelling:** prefer histopathology-confirmed ground truth where available; record label source
  and any inter-rater considerations per dataset.
- **Cleaning:** remove duplicates and corrupt files; handle artefacts (rulers, ink markings, hair)
  to reduce spurious correlations.
- **Leakage prevention:** ensure images of the same lesion/patient do not span train and test
  splits.
- **Aggregation:** when combining datasets, harmonise labels and record the mapping; account for
  differing acquisition devices and distributions.
- **Pre-processing:** resizing/normalisation documented and applied consistently at training and
  inference.

## 5. Examination for bias (Art. 10)

| Bias type | Concern for DermaScan | Detection | Mitigation |
|---|---|---|---|
| Selection / representativeness | Public dermoscopy data skews to lighter skin (Fitzpatrick I-III) and certain regions | Demographic composition in DSC-001; per-subgroup metrics (TST-018) | State validated phototype range (IU-001); restrict intended use; seek additional data |
| Label / measurement | Noisy or inconsistent ground truth | Label-source review | Prefer biopsy-confirmed labels |
| Spurious correlation | Model keys on artefacts not pathology | Saliency/feature checks | Artefact handling; augmentation |
| Aggregation | One model underperforms subgroups | Subgroup evaluation | Subgroup-aware thresholds; report per subgroup |
| Automation bias (use-stage) | Over-reliance on output | Usability evaluation (TST-009) | Human-oversight design (REQ-031, REQ-032) |

The principal documented bias is **demographic / Fitzpatrick under-representation**, tracked as
**RISK-004** in the risk file, with controls in SRS (REQ-010, REQ-013, REQ-023) and post-market
subgroup monitoring (build phase 10).

## 6. Suitability assessment (quality, quantity, completeness)

For each dataset the card (DSC-001) records whether quantity and class balance are adequate for the
intended purpose, what is missing, and the resulting limitation on the validated scope. Where data
are insufficient for a subgroup, that subgroup is excluded from the validated intended use until
adequate data and validation exist.

## 7. Data versioning and lineage

- Each dataset version (and any combined/derived set) is identified and recorded.
- Each trained model is bound to the exact dataset version and code used (REQ-041), enabling
  reproducibility and change control.
- Transformations (cleaning, splits, pre-processing) are scripted and version-controlled so the
  pipeline is reproducible.

## 8. Data protection (GDPR)

- Health-related image data is special-category data under **GDPR Art. 9**. This project uses only
  already-public, licensed research datasets and collects no new patient data.
- For any hypothetical real deployment: lawful basis, data minimisation, anonymisation/
  pseudonymisation, security of processing (**Art. 32**), and a **Data Protection Impact Assessment
  (DPIA)** would be required. In Germany the BDSG and the emerging European Health Data Space (EHDS)
  would also apply. (Noted for completeness; not performed in this simulation.)

## 9. Open items

- Finalise the chosen dataset(s) and complete all fields in DSC-001.
- Quantify subgroup composition and fix the validated Fitzpatrick range in IU-001.
- Record final split sizes and any external-validation source.

## 10. Change history

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-06-27 | Akhila N Pillai | Initial draft (simulation): Art. 10 governance, bias examination, GDPR overlap |
