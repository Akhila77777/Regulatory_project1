# Intended Purpose / Intended Use

> SIMULATION / TRAINING EXERCISE. DermaScan is a personal portfolio project, NOT a certified
> medical device. No real clinical use. Content is written in submission style for learning.

| Field | Value |
|---|---|
| Document ID | IU-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Akhila N Pillai |
| Date | 2026-06-27 |
| Reviewed by | - |
| Approved by | - |

**Related documents:** classification_rationale.md (CLS-001), risk_management_file/ (RMF-*),
eu_ai_act/ (AIA-*), data/dataset_card.md.
**Study reference:** `steps/step-01-intended-purpose-samd.html`.

---

## 1. Purpose of this document

This document defines the intended purpose of DermaScan in accordance with EU MDR 2017/745
(Article 2(12) and Annex I). The intended purpose is the anchor for classification, risk
management, clinical evaluation, software requirements, and post-market surveillance. Any change to
this document must trigger review of the classification rationale (CLS-001), the risk management
file (RMF-*), and the software requirements specification (SRS).

## 2. Device identification

| Item | Value |
|---|---|
| Device (trade) name | DermaScan |
| Device type | Standalone software, Software as a Medical Device (SaMD) |
| Software version (this IU applies to) | 0.x (pre-release, simulation) |
| Manufacturer (simulated) | DermaScan project (portfolio) |
| MDR classification (working assumption) | Class IIa, Rule 11 (see CLS-001) |
| AI Act status (working assumption) | High-risk AI system, Art. 6(1) (see AIA-*) |

## 3. Intended medical purpose

DermaScan is intended to **assist qualified clinicians in the triage of pigmented skin lesions** by
providing a software-generated estimate of the likelihood that an individual lesion is malignant
(for example melanoma), based on analysis of a dermoscopic or standardized clinical image.

DermaScan provides **information used to support a diagnostic decision**. It is a decision-support
tool. It does **not** make a diagnosis, does not recommend treatment, and does not replace
histopathological examination or the independent clinical judgement of the responsible clinician.

## 4. Indication for use

Assessment of a single, visible **pigmented skin lesion** in an adult patient where a clinician has
decided that further evaluation of malignancy risk is warranted, as an adjunct within an existing
clinical examination workflow.

## 5. Target patient population

- Adults (>= 18 years) presenting with a pigmented skin lesion of concern.
- Validated skin phototype range: to be stated explicitly based on the validation dataset
  composition (see dataset_card.md). Where the model has not been validated for a given
  Fitzpatrick phototype, that phototype is listed as a limitation/contraindication in Section 10.

## 6. Intended user

A **qualified healthcare professional** (for example a dermatologist or a general practitioner
trained in skin-lesion assessment). DermaScan is **not** intended for use by patients or laypersons
for self-assessment.

## 7. Intended use environment

A professional clinical setting (clinic or hospital) in which images are acquired with a dermoscope
or a standardized clinical camera under controlled conditions, and in which a qualified clinician
reviews the output as part of the consultation.

## 8. Inputs and outputs

### 8.1 Input
- A single digital dermoscopic or standardized clinical image of one pigmented lesion, meeting the
  stated image-quality criteria (focus, framing, illumination, supported file format and minimum
  resolution; criteria defined in the SRS and IFU).

### 8.2 Output
- A **calibrated malignancy-risk estimate** for the imaged lesion (probability or risk band),
  accompanied by:
  - a confidence indicator and an explicit low-confidence warning where applicable;
  - an out-of-distribution / unsupported-input notice where the image falls outside the validated
    operating range;
  - a mandatory, visible **disclaimer** (see Section 11).

### 8.3 What the output is NOT
- It is **not** a diagnosis, a histopathology result, or a treatment recommendation.
- It does **not** authorize, replace, or override any clinical decision. The responsible clinician
  remains fully accountable for the diagnosis and management.

## 9. Operating principle (summary)

DermaScan applies a trained machine-learning image-classification model to the input image to
estimate malignancy likelihood. The model is trained and validated only on public, properly
licensed dermoscopic datasets (see dataset_card.md). Performance is characterized by sensitivity,
specificity, AUROC and per-subgroup metrics on an independent test set (see clinical_evaluation.md);
no single accuracy figure is used as a performance claim.

## 10. Contraindications and limitations

DermaScan must not be relied upon, and its output is not valid, in the following cases:
- **Non-pigmented lesions** and lesion types outside the validated scope.
- **Poor-quality images** (out of focus, poorly framed, inadequate illumination) or unsupported
  image modalities (for example clinical photographs where only dermoscopy was validated, or vice
  versa).
- **Skin phototypes, anatomical sites, or populations** not represented in the validation data;
  notably, public dermoscopy datasets under-represent darker skin (Fitzpatrick IV-VI), so
  performance for under-represented phototypes is not assured and such use is a limitation.
- Use **without** independent clinician review.
- Use for **screening of asymptomatic general populations** (outside the intended adjunct triage
  use) or for **patient self-assessment**.

## 11. Warnings and mandatory disclaimer

Every DermaScan output, in the user interface and in any API response, displays a visible
disclaimer to the effect:

> "Research/educational decision-support tool. This is not a diagnosis. The output must be
> independently confirmed by a qualified clinician and does not replace clinical judgement or
> histopathological examination."

Additional warnings:
- A **low-confidence** or **out-of-distribution** result must not be interpreted as "low risk".
- Automation bias warning: the output is an adjunct only; clinicians must not defer their judgement
  to the tool.

## 12. Residual risk statement

The overall residual risk associated with the intended use, after risk controls, is evaluated in
the risk management file (RMF-RPT-001) and is required to be acceptable in light of the clinical
benefit demonstrated in the clinical evaluation. The principal residual risks are false-negative
outputs (potential delayed diagnosis), false-positive outputs (potential unnecessary anxiety or
procedures), and reduced performance for under-represented populations; these are controlled by
mandatory clinician review, confidence and out-of-distribution signalling, explicit limitation
statements, and post-market performance monitoring.

## 13. Change history

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-06-27 | Akhila N Pillai | Initial draft (simulation) |
