# DermaScan — AI Skin-Lesion Classifier as a Regulated SaMD (Simulation)

![Domain](https://img.shields.io/badge/Domain-MedTech%20Regulatory%20Affairs-0b5394)
![Regulation](https://img.shields.io/badge/EU%20MDR-2017%2F745-1c4587)
![Standard](https://img.shields.io/badge/ISO-14971%20%7C%2013485-2e7d32)
![Software](https://img.shields.io/badge/IEC-62304-2e7d32)
![AI Act](https://img.shields.io/badge/EU%20AI%20Act-2024%2F1689-6a1b9a)
![Status](https://img.shields.io/badge/Status-Portfolio%20%2F%20Simulation-e69138)

**DermaScan** is a personal portfolio project: an AI-based image classifier that screens
dermoscopic / clinical skin-lesion images for signs of malignancy (e.g. melanoma vs. benign
nevus), documented **as if it were going through the full EU regulatory process for Software
as a Medical Device (SaMD)**.

It exists to demonstrate two skill sets side by side:

1. **Engineering** — a skin-lesion image classifier with a FastAPI inference service (Python).
2. **Regulatory simulation** — the documentation artifacts a real EU MDR **Class IIa** SaMD
   would require: a risk management file (ISO 14971), QMS-style procedures (ISO 13485), a
   software lifecycle file (IEC 62304), and EU AI Act high-risk documentation.

The regulatory documentation is treated as a **first-class deliverable**, not an afterthought.

> ### ⚠️ Honesty note (read first)
> This is a **training / simulation exercise**, not a certified device. There is **no real
> patient data, no clinical use, and no diagnostic claim**. Nothing here is CE-marked, MDR-certified,
> or reviewed by a Notified Body. Documents are written in the *style* of a real submission to
> demonstrate competence, and are marked as a simulation where relevant.

---

## Why this project

I am completing a **Master in Medical Systems Engineering** (Otto von Guericke University,
Magdeburg) and targeting a **MedTech Regulatory Affairs / Quality** role in Germany. DermaScan
lets me show, on one AI product, that I can carry a device through the regulatory chain that
matters here: qualification and classification, risk management, software lifecycle, clinical
evaluation, post-market surveillance, and the EU AI Act overlay for high-risk medical AI.

---

## Regulatory framing (simulated)

| Framework | Role in this project |
|---|---|
| **EU MDR 2017/745** | Rule 11 software providing information for diagnostic decisions, classified **Class IIa** per the documented rationale. |
| **ISO 14971:2019** | Full risk management process: plan, hazard analysis, risk register, controls, benefit-risk determination. |
| **ISO 13485:2016** | Document-control discipline and process structure (document IDs, versioning, review/approval), not a literal certified QMS. |
| **IEC 62304:2006+A1:2015** | Software development lifecycle; software safety classification decided as **Class C** via risk analysis. |
| **EU AI Act (2024/1689)** | Treated as a **high-risk AI system** (Art. 6 / Annex III); Annex IV technical documentation, data governance (Art. 10), human oversight (Art. 14). |

---

## What is actually in the repo

### Regulatory & quality documentation — `docs/`
- **Intended purpose / intended use** (MDR Annex I) — `docs/regulatory/intended_use.md`
- **MDR classification rationale** (MDCG 2019-11, Rule 11, Class IIa, AI Act Art. 6) — `docs/regulatory/classification_rationale.md`
- **ISO 14971 risk management file** — plan, risk analysis with a 10-item AI-hazard register
  (false negative/positive, out-of-distribution input, Fitzpatrick/algorithmic bias, automation
  bias, dataset shift, adversarial input), and risk management report — `docs/regulatory/risk_management_file/`
- **IEC 62304 set** — software development plan, Class C safety classification, SOUP/CVE list — `docs/regulatory/iec62304/`
- **EU AI Act Annex IV technical documentation** — `docs/regulatory/eu_ai_act/`
- **QMS SOPs** (document control, CAPA, design control) — `docs/regulatory/qms/`
- **Cybersecurity file** — `docs/regulatory/cybersecurity/`
- **Clinical evaluation** (MDCG 2020-1; plan complete, report preliminary) — `docs/regulatory/technical_documentation/`
- **Post-market surveillance / EUDAMED / vigilance plan** — `docs/regulatory/post_market/`
- **Data governance & dataset card** (AI Act Art. 10; HAM10000, ISIC, BCN20000, PH2) — `docs/data/`
- **Software requirements, architecture, and V&V** with a **REQ / RISK / TST traceability matrix** — `docs/software/`
- **Post-market KPI dashboard** spec (Fitzpatrick fairness drift, vigilance/CAPA metrics) — `docs/quality/`

### Engineering — `src/`
- `src/api/` — FastAPI inference service (schemas + app)
- `src/models/` — model definition, out-of-distribution detection, inference
- `src/data/` — dataset loading & preprocessing
- `src/evaluation/` — metrics & evaluation
- `tests/` — API tests · `infra/` — Terraform deployment scaffold

> Model training and the full inference service are **in progress**. Treat code as a
> work-in-progress demonstrator, not a deployed model.

### Study site — `steps/`
An HTML study site (open `steps/index.html`) walking through each regulatory topic with the
concepts, the actual regulations, 2026 German MedTech RA context, and interview Q&A.

---

## Repository structure

```
Regulatory_project1/
├── docs/
│   ├── regulatory/     # intended use, classification, ISO 14971, IEC 62304, QMS,
│   │                   # EU AI Act, cybersecurity, clinical evaluation, PMS
│   ├── software/       # SRS, architecture, traceability matrix, V&V
│   ├── data/           # data governance, dataset card
│   └── quality/        # post-market KPI dashboard
├── src/                # data, models, FastAPI api, evaluation
├── tests/              # API tests
├── infra/              # Terraform deployment scaffold
└── steps/              # HTML study / interview-prep site
```

## Standards & concepts demonstrated

`EU MDR 2017/745` · `ISO 14971:2019` · `IEC 62304` · `ISO 13485` · `EU AI Act 2024/1689` ·
`MDCG 2019-11` · `MDCG 2020-1` · `GSPR mapping` · `Rule 11 classification` ·
`Risk register & benefit-risk` · `SOUP / CVE assessment` · `REQ/RISK/TST traceability` ·
`Clinical evaluation` · `Post-Market Surveillance & PMCF` · `EUDAMED` · `Data governance & bias`

## Tech stack

Python · FastAPI · PyTorch/TensorFlow (model) · Terraform (infra) · public dermoscopic
datasets (HAM10000, ISIC, BCN20000, PH2)

---

*Author: Akhila N Pillai — M.Sc. Medical Systems Engineering candidate, Magdeburg, Germany.
Built as a self-directed regulatory-affairs portfolio project.*
