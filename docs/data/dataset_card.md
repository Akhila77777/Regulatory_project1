# Dataset Card

> SIMULATION / TRAINING EXERCISE. DermaScan is a personal portfolio project, NOT a certified
> medical device. No real clinical use. Content is written in submission style for learning.

| Field | Value |
|---|---|
| Document ID | DSC-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Akhila N Pillai |
| Date | 2026-06-27 |
| Reviewed by | - |
| Approved by | - |

**Related:** data_governance.md (DG-001), AIA-001, RMF-RA-001 (RISK-004).
**Study reference:** `steps/step-07-data-governance-bias.html`.

> The values marked "(to confirm)" are to be filled when datasets are finalised and downloaded under
> their licences. Licence terms must be re-verified at the source before use; the notes below are
> indicative and must not be relied upon as legal advice.

---

## 1. Overview

DermaScan uses public, properly licensed dermoscopic datasets. This card records, per dataset, the
provenance, licence, size, class composition, modality, and demographic information relevant to bias
and to the validated intended use. Only datasets listed here are used.

## 2. Candidate datasets

### 2.1 HAM10000
| Field | Value |
|---|---|
| Source / provenance | "Human Against Machine with 10000 training images"; dermatoscopic images, multiple sources (to confirm exact citation) |
| Approx. size | ~10,000 dermoscopic images |
| Classes | 7 diagnostic categories (incl. melanoma, melanocytic nevi, basal cell carcinoma, etc.) |
| Label source | Histopathology, follow-up, expert consensus, or confocal (varies by case) (to confirm) |
| Modality | Dermoscopy |
| Licence | Research-use licence (CC BY-NC style); verify at source (to confirm) |
| Demographics | Age/sex/site partially available; skin-tone labels limited; skews to lighter skin (to confirm) |
| Known limitations | Class imbalance; limited phototype diversity |

### 2.2 ISIC Archive
| Field | Value |
|---|---|
| Source / provenance | International Skin Imaging Collaboration archive; basis of ISIC challenges |
| Approx. size | Large (tens of thousands+); subset to be selected (to confirm) |
| Classes | Multiple; melanoma vs non-melanoma derivable |
| Label source | Varies; biopsy-confirmed subset available (to confirm) |
| Modality | Dermoscopy (and some clinical) |
| Licence | Per-image/collection licences (often CC BY-NC); verify per collection (to confirm) |
| Demographics | Variable; documented per collection where available (to confirm) |
| Known limitations | Heterogeneous acquisition; representativeness varies by collection |

### 2.3 BCN20000
| Field | Value |
|---|---|
| Source / provenance | Hospital Clinic de Barcelona dermoscopic dataset |
| Approx. size | ~19,000 images |
| Classes | Multiple, incl. hard-to-diagnose lesions |
| Label source | Clinical/histopathological (to confirm) |
| Modality | Dermoscopy |
| Licence | Research-use; verify at source (to confirm) |
| Demographics | Single-centre population; limited diversity (to confirm) |
| Known limitations | Single-centre source affects external generalisation |

### 2.4 PH2
| Field | Value |
|---|---|
| Source / provenance | Dermoscopic dataset (Pedro Hispano Hospital, Portugal) |
| Approx. size | ~200 images |
| Classes | Common nevi, atypical nevi, melanoma |
| Label source | Expert annotation incl. segmentation |
| Modality | Dermoscopy |
| Licence | Research/academic use; verify at source (to confirm) |
| Demographics | Small sample; limited diversity |
| Known limitations | Small size; suitable for validation, not primary training |

## 3. Splits (to confirm)

| Split | Source dataset(s) | Size | Notes |
|---|---|---|---|
| Train | (to confirm) | (to confirm) | No lesion/patient overlap with test |
| Validation | (to confirm) | (to confirm) | Threshold/calibration tuning only |
| Test (internal) | (to confirm) | (to confirm) | Used once for final evaluation |
| External validation | (to confirm) | (to confirm) | Different source/site if feasible |

## 4. Demographic composition and representativeness

| Attribute | Coverage | Gap / risk |
|---|---|---|
| Skin phototype (Fitzpatrick) | Skews I-III (to confirm) | IV-VI under-represented -> RISK-004; constrains validated range |
| Age | Partial metadata (to confirm) | Confirm adult coverage per IU-001 |
| Sex | Partial metadata (to confirm) | Report subgroup metrics |
| Anatomical site | Partial metadata (to confirm) | Some sites under-represented |
| Geography | Predominantly European/North American sources (to confirm) | Generalisation to other populations limited |

The validated Fitzpatrick range stated in IU-001 must be set from this table once confirmed; any
phototype not adequately represented is a limitation/contraindication (IU-001 Section 10).

## 5. Intended-use impact

The representativeness gaps above directly bound the validated intended use (IU-001) and are the
basis for RISK-004 and its controls (REQ-013 subgroup reporting, REQ-023 scope guard) and for
post-market subgroup monitoring (build phase 10).

## 6. Ethical and licensing notes

- All datasets are public research datasets; no new patient data is collected.
- Licence terms (including non-commercial restrictions and attribution) must be honoured and
  re-verified at source before use. This portfolio project is non-commercial and educational.

## 7. Change history

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-06-27 | Akhila N Pillai | Initial draft (simulation): candidate datasets, demographics, gaps (values to confirm) |
