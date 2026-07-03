# SOP: Document and Record Control

> SIMULATION / TRAINING EXERCISE. DermaScan is a personal portfolio project, NOT a certified
> medical device and NOT a certified QMS. This SOP borrows ISO 13485 document-control discipline for
> learning; it is not a literal certified procedure.

| Field | Value |
|---|---|
| Document ID | SOP-DC-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Akhila N Pillai |
| Date | 2026-06-27 |
| Reviewed by | - |
| Approved by | - |

**Standard:** ISO 13485:2016 clauses 4.2.4 (control of documents) and 4.2.5 (control of records).
**Related:** all project documents (this SOP defines their control); SOP-CAPA-001, SOP-DESIGN-001.
**Study reference:** `steps/step-05-iso13485-qms.html`.

---

## 1. Purpose

To define how controlled documents and records for DermaScan are identified, reviewed, approved,
versioned, changed, and retained, so that only correct, current documents are in use and changes are
traceable.

## 2. Scope

All regulatory, software, data, and quality documents in the repository (the `docs/` tree) and the
records they generate.

## 3. Document identifier scheme

Every controlled document carries a unique ID. Prefixes in use:

| Prefix | Document type | Example |
|---|---|---|
| IU | Intended use | IU-001 |
| CLS | Classification rationale | CLS-001 |
| RMF-PLAN / RMF-RA / RMF-RPT | Risk management plan / analysis / report | RMF-RA-001 |
| SRS | Software requirements specification | SRS-001 |
| SDP / SSC / SOUP | IEC 62304 dev plan / safety classification / SOUP list | SSC-001 |
| TRC | Traceability matrix | TRC-001 |
| AIA | EU AI Act technical documentation | AIA-001 |
| DG / DSC | Data governance / dataset card | DG-001 |
| CLIN | Clinical evaluation | CLIN-001 |
| PMS | Post-market surveillance plan | PMS-001 |
| KPI | KPI dashboard | KPI-001 |
| SOP-xx | Standard operating procedure | SOP-DC-001 |
| ARC | Architecture | ARC-001 |

Item-level IDs inside documents: requirements `REQ-XXX`, risks `RISK-XXX`, hazards `HAZ-XXX`, tests
`TST-XXX`, SOUP items `SOUP-XXX`.

## 4. Mandatory header block

Every controlled document begins with the simulation note and a header table containing: Document
ID, Version, Status (Draft / In review / Approved / Obsolete), Author, Date, Reviewed by, Approved
by, and a Related-documents line.

## 5. Versioning

- Draft documents use 0.x. The first approved release is 1.0.
- Minor changes increment the decimal (1.0 -> 1.1); significant changes increment the major (1.x ->
  2.0).
- Each document maintains a Change History table (version, date, author, change).

## 6. Review and approval

A document becomes effective only when its Status is Approved and the Approved-by field is filled.
Review confirms technical correctness, consistency with related documents, and compliance with the
applicable standard. (In this solo project the same person may author and review; the fields are
retained to reflect the real segregation of duties.)

## 7. Change control

Changes to an approved document are made by: raising the change (often from a CAPA, a PMS finding, or
a design change), assessing impact on related documents (especially the risk file and the
traceability matrix), making the change, updating the version and Change History, and re-approving.
Code and related document changes are kept together (same commit/PR) where practical.

## 8. Distribution and obsolete documents

Git is the single source of truth and history. Superseded versions remain in version history;
documents no longer valid are marked Status = Obsolete to prevent unintended use.

## 9. Records

Records (evidence that activities occurred, e.g. test results, review notes, CAPA records, PMS/PSUR
reports) are identified, legible, retained, and protected against loss or unauthorized change
(tamper-evidence for logs per REQ-042). Retention period is defined per record type (placeholder:
align with MDR retention expectations in a real submission).

## 10. Change history

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-06-27 | Akhila N Pillai | Initial draft (simulation): ID scheme, header, versioning, change control |
