# Technical Documentation Index and Conformity Route

> SIMULATION / TRAINING EXERCISE. DermaScan is a personal portfolio project, NOT a certified
> medical device. It is NOT CE marked, has NO Notified Body certificate, and has NO Declaration of
> Conformity. This index is written in submission style for learning only.

| Field | Value |
|---|---|
| Document ID | TF-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Akhila N Pillai |
| Date | 2026-07-03 |
| Reviewed by | - |
| Approved by | - |

**Regulations:** MDR 2017/745 Annex II (technical documentation), Annex III (post-market
surveillance), Annex IX (conformity assessment), Art. 19-20 (DoC, CE), Art. 52; EU AI Act Art. 8(2),
43, 47-49. **Related:** all project documents (this file indexes them).
**Study reference:** `steps/step-12-technical-doc-ce-marking.html`.

---

## 1. Purpose

This document is the master index of the DermaScan technical documentation. It maps the MDR Annex II
and Annex III contents to the actual documents in the repository, states the conformity assessment
route, and describes the (simulated) path to CE marking. It is the entry point a reviewer or Notified
Body would use to navigate the file.

## 2. Device summary

| Item | Value |
|---|---|
| Device | DermaScan (SaMD, standalone software) |
| Intended purpose | Decision-support triage of pigmented skin lesions (IU-001) |
| MDR class | IIa, Rule 11 (CLS-001) |
| AI Act status | High-risk AI system, Art. 6(1) (CLS-001, AIA-001) |
| IEC 62304 software safety class | C (SSC-001) |

## 3. MDR Annex II mapping (technical documentation)

| Annex II section | Content | Document(s) |
|---|---|---|
| 1.1 Device description and specification | What the device is, variants, accessories | IU-001; ARC-001; DEP-001 |
| 1.1 Intended purpose, intended users | Intended use | IU-001 |
| 1.2 Reference to previous/similar generations | Predecessors | (n/a - new; state-of-the-art in CLIN-001) |
| 2 Labelling and instructions for use (IFU) | Labels, IFU, disclaimers | IU-001 (Sections 10-12); REQ-030, REQ-033 |
| 3 Design and manufacturing information | Design stages, software | SDP-001; ARC-001; DEP-001; SRS-001 |
| 4 General Safety and Performance Requirements | GSPR checklist | Section 5 below (GSPR mapping); full checklist is an open item |
| 5 Benefit-risk analysis and risk management | Risk file | RMF-PLAN-001; RMF-RA-001; RMF-RPT-001 |
| 6.1 Pre-clinical and clinical data | Verification, validation, clinical evaluation | SRS-001; TRC-001; verification_validation/ (pending); CLIN-001 |
| 6.2 Additional information (specific cases) | Software, AI | SSC-001; SOUP-001; AIA-001; CYB-001; DG-001; DSC-001 |

## 4. MDR Annex III mapping (post-market)

| Annex III section | Content | Document(s) |
|---|---|---|
| 1.1 PMS plan | Proactive/reactive surveillance | PMS-001 |
| PMCF | Clinical follow-up | PMS-001 (Section 6) |
| PSUR | Periodic safety update report | PMS-001 (Section 9); KPI-001 as data source |

## 5. GSPR mapping (summary; full checklist is an open item)

| GSPR (Annex I) | Evidence |
|---|---|
| Ch. I 1-9 (general safety, benefit-risk, risk management) | RMF-*; CLIN-001 (benefit-risk) |
| 14 (usability, use error) | REQ-032, REQ-060; usability evaluation (TST-009); IEC 62366-1 |
| 17.1 (repeatability, reliability, performance) | SRS performance REQs; SDP-001; TRC-001 |
| 17.2 (development to state of the art incl. security) | SDP-001 (IEC 62304); CYB-001 (IEC 81001-5-1) |
| 17.4 (IT security, unauthorized access) | CYB-001; REQ-050..054 |
| 23 (information supplied / IFU) | IU-001; REQ-033 |

## 6. Conformity assessment route (simulated)

- As a **Class IIa** device, DermaScan requires a **Notified Body**. Intended route: **MDR Annex IX**
  (QMS assessment plus assessment of the technical documentation on a representative basis); Annex XI
  is the alternative.
- Because DermaScan is a **high-risk AI system**, the AI Act high-risk requirements are intended to be
  assessed **through the same conformity assessment** (AI Act Art. 8(2), 43): one integrated file, one
  Notified Body assessment, avoiding duplication.
- **Simulation status:** no Notified Body has been engaged, no audit performed, and no certificate
  issued. All statements here describe the intended route only.

## 7. Path to CE marking (sequence, simulated)

1. Intended purpose and classification (IU-001, CLS-001).
2. QMS and technical documentation in place (this file + SOPs + Annex II/III docs).
3. GSPR conformity demonstrated via standards, risk, clinical evaluation, and V&V.
4. Notified Body conformity assessment (Annex IX), integrated with the AI Act.
5. Notified Body issues the CE certificate. **(Not performed - simulation.)**
6. Manufacturer draws up the **EU Declaration of Conformity**. **(Not issued - simulation.)**
7. Affix the **CE mark** with the Notified Body's number. **(Not affixed - simulation.)**
8. Register device/actors in **EUDAMED**; assign **UDI** (note: EUDAMED mandatory use phasing in
   around 28 May 2026). **(Not registered - simulation.)**
9. Place on market and run PMS/vigilance (PMS-001). **(Not placed on market - simulation.)**

## 8. Economic operators and roles (reference)

Manufacturer (owns conformity, technical file, DoC, PMS); Authorised Representative (EU contact for a
non-EU manufacturer); Importer; Distributor; and the **PRRC** (Person Responsible for Regulatory
Compliance, MDR Art. 15). For the AI Act: provider and deployer (AIA-001 Section 11). These roles are
noted for completeness; DermaScan is a simulation with a single author.

## 9. Document register (current state)

| Doc ID | Title | Phase | Status |
|---|---|---|---|
| IU-001 | Intended use | 1 | Draft |
| CLS-001 | Classification rationale | 2 | Draft |
| RMF-PLAN-001 | Risk management plan | 3 | Draft |
| RMF-RA-001 | Risk analysis and register | 3 | Draft |
| RMF-RPT-001 | Risk management report | 3 | Draft (preliminary) |
| SDP-001 | Software development plan | 4 | Draft |
| SSC-001 | Software safety classification (Class C) | 4 | Draft |
| SOUP-001 | SOUP list | 4 | Draft |
| SOP-DC-001 | Document control SOP | 5 | Draft |
| SOP-CAPA-001 | CAPA SOP | 5 | Draft |
| SOP-DESIGN-001 | Design control SOP | 5 | Draft |
| AIA-001 | EU AI Act technical documentation (Annex IV) | 6 | Draft |
| DG-001 | Data governance | 7 | Draft |
| DSC-001 | Dataset card | 7 | Draft |
| CLIN-001 | Clinical evaluation | 8 | Draft (report preliminary) |
| SRS-001 | Software requirements specification | 9 | Draft |
| ARC-001 | Software architecture | 9 | Draft |
| TRC-001 | Traceability matrix | 9 | Draft |
| DEP-001 | Deployment/MLOps architecture (GCP) | 9 | Draft |
| PMS-001 | Post-market surveillance plan | 10 | Draft |
| KPI-001 | KPI dashboard (spec + data template) | 10 | Draft |
| CYB-001 | Cybersecurity | 11 | Draft |
| TF-001 | Technical documentation index (this) | 12 | Draft |
| (pending) | Verification & validation test specs | 9 | Not started |
| (pending) | GSPR full checklist | 2/12 | Not started |
| (pending) | Source code (src/) and IaC (infra/) | 9 | Not started |

## 10. Open items

- Produce the full GSPR checklist as a standalone controlled document.
- Complete verification & validation and replace "Planned" TST statuses with results.
- Build `src/` and `infra/`; then move documents from Draft toward Approved (SOP-DC-001).

## 11. Change history

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-07-03 | Akhila N Pillai | Initial draft (simulation): Annex II/III index, GSPR summary, conformity route, document register |
