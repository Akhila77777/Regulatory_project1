# CLAUDE.md

This file gives Claude Code (and any other contributor) the context needed to work on **DermaScan**.

## 1. What this project is

DermaScan is a **personal portfolio project**: an AI-based image classifier that screens
dermoscopic/clinical skin lesion images for signs of malignancy (e.g. melanoma vs. benign nevus),
built **as if it were going through the EU regulatory process for a Software as a Medical Device
(SaMD)**.

The project has two intertwined goals:

1. **Engineering**: build a working ML model and inference API for skin lesion classification.
2. **Regulatory simulation**: produce the documentation artifacts that a real EU MDR
   Class IIa/IIb SaMD would require — a risk management file (ISO 14971), QMS-style procedures
   (ISO 13485), a software development lifecycle file (IEC 62304), and EU AI Act high-risk AI
   system documentation.

The regulatory documentation is a **first-class deliverable**, not an afterthought. Code changes
that affect intended use, inputs/outputs, model behaviour, or risk profile should be reflected in
the relevant docs (see §5).

## 2. Hard constraints — read before doing anything

- **This is NOT a certified medical device** and must never be presented as one. No real patient
  data, no real clinical use, no real diagnostic claims.
- Use only **public, properly licensed dermoscopic datasets** (e.g. HAM10000, ISIC Archive,
  BCN20000, PH2). Record provenance, licence, and demographic composition in
  `docs/data/dataset_card.md`.
- Every model output / API response must carry a visible disclaimer that this is a
  research/educational tool and **not a diagnosis**.
- Do **not** fabricate clinical evaluation results, regulatory submissions, certificates, or
  Notified Body approvals. Documents should be written in the style of a real submission but must
  be clearly marked as a **simulation / training exercise** where relevant (e.g. in a header note).
- Do not invent compliance claims ("CE marked", "MDR certified", etc.) anywhere in code, docs, or
  UI text.

## 3. Regulatory framing (simulated)

| Framework | Role in this project |
|---|---|
| **EU MDR 2017/745** | Working assumption: the device is an MDR **Rule 11** software (provides information used to make decisions for diagnosis), tentatively **Class IIa**, pending the documented classification rationale in `docs/regulatory/classification_rationale.md`. |
| **ISO 14971:2019** | Risk management process across the whole lifecycle — hazard identification, risk analysis/evaluation, risk controls, residual risk evaluation. Lives in `docs/regulatory/risk_management_file/`. |
| **ISO 13485:2016** | Used for *document control discipline and process structure* (document IDs, versioning, review/approval fields), not as a literal certified QMS. Lives in `docs/regulatory/qms/`. |
| **IEC 62304:2006+A1:2015** | Software development lifecycle. Software safety classification (A/B/C) is **TBD via risk analysis** — a melanoma-screening tool likely starts from a Class B or C assumption depending on whether it's positioned as decision-support with mandatory clinician review. Document the decision, don't assume it. |
| **EU AI Act (2024/1689)** | DermaScan, as an AI system that is a safety component of a medical device subject to third-party conformity assessment under MDR, is treated as a **high-risk AI system** (Art. 6 / Annex III). Relevant duties to document: risk management system (Art. 9), data & data governance (Art. 10), technical documentation (Art. 11 / Annex IV), record-keeping/logging (Art. 12), transparency to users (Art. 13), human oversight (Art. 14), accuracy/robustness/cybersecurity (Art. 15). |

## 4. Repository structure (target layout)

Not all of this exists yet — build it incrementally as work progresses.

```
Regulatory_project1/
├── CLAUDE.md
├── README.md
├── docs/
│   ├── regulatory/
│   │   ├── intended_use.md            # Intended purpose, target population, indications/contraindications
│   │   ├── classification_rationale.md # MDR Rule 11 classification reasoning
│   │   ├── risk_management_file/       # ISO 14971: plan, hazard analysis, risk controls, RM report
│   │   ├── qms/                        # ISO 13485-style procedures (doc control, CAPA, design controls)
│   │   ├── iec62304/                   # Software development plan, safety classification, SOUP list
│   │   ├── eu_ai_act/                  # High-risk AI system documentation (Annex IV style)
│   │   └── technical_documentation/    # MDR Annex II/III style technical file
│   ├── software/
│   │   ├── srs.md                     # Software Requirements Specification
│   │   ├── architecture.md            # Software architecture & design description
│   │   ├── traceability_matrix.md     # REQ <-> RISK <-> design <-> test
│   │   └── verification_validation/   # V&V plans and reports
│   └── data/
│       ├── data_governance.md         # AI Act Art. 10 — data quality, bias, provenance
│       └── dataset_card.md            # Dataset(s) used, licences, splits, demographics
├── src/
│   ├── data/                          # dataset loading/preprocessing
│   ├── models/                        # model definitions, training scripts
│   ├── api/                           # FastAPI inference service
│   └── evaluation/                    # metrics, validation scripts
├── tests/
├── notebooks/
└── requirements.txt
```

## 5. Working conventions

- **Document IDs**: requirements `REQ-XXX`, risks `RISK-XXX` (hazard / hazardous situation / harm),
  tests `TST-XXX`. The traceability matrix (`docs/software/traceability_matrix.md`) links these
  together — keep it up to date.
- **When changing model behaviour, inputs/outputs, or API contracts**:
  1. Check whether `docs/software/srs.md` needs a new/updated requirement.
  2. Check whether `docs/regulatory/risk_management_file/` needs a new or updated hazard/risk
     entry (new failure modes, new misuse scenarios, etc.).
  3. Update `docs/software/traceability_matrix.md` accordingly.
  4. Keep the code and the related doc updates together (same commit/PR) where practical.
- **Tone in regulatory docs**: precise, falsifiable, and conservative. Prefer "intended to assist
  qualified clinicians in triaging pigmented skin lesions" over "accurately detects skin cancer".
- **Tech stack**:
  - Python for modelling (PyTorch or TensorFlow — pick one and stay consistent once chosen).
  - FastAPI for the inference API. No frontend planned for now.
  - Keep dependencies pinned in `requirements.txt`.
- **Testing**: model evaluation scripts and API tests should map to entries in
  `docs/software/verification_validation/`.

## 6. Glossary

- **SaMD** — Software as a Medical Device
- **MDR** — Medical Device Regulation, EU 2017/745
- **IFU** — Instructions for Use
- **PMS** — Post-Market Surveillance
- **SOUP** — Software of Unknown Provenance (third-party libraries, per IEC 62304)
- **CAPA** — Corrective and Preventive Action
- **GSPR** — General Safety and Performance Requirements (MDR Annex I)
