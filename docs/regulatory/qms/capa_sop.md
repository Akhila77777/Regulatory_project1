# SOP: Corrective and Preventive Action (CAPA)

> SIMULATION / TRAINING EXERCISE. DermaScan is a personal portfolio project, NOT a certified
> medical device and NOT a certified QMS. This SOP borrows ISO 13485 discipline for learning.

| Field | Value |
|---|---|
| Document ID | SOP-CAPA-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Akhila N Pillai |
| Date | 2026-06-27 |
| Reviewed by | - |
| Approved by | - |

**Standard:** ISO 13485:2016 clauses 8.5.2 (corrective action) and 8.5.3 (preventive action); links
to MDR PMS/vigilance. **Related:** PMS-001, RMF-RA-001, SOP-DC-001, SOP-DESIGN-001.
**Study reference:** `steps/step-05-iso13485-qms.html`.

---

## 1. Purpose

To define how DermaScan identifies, investigates, and resolves problems (corrective action) and
potential problems (preventive action), including verification that actions are effective.

## 2. Definitions

- **Correction:** an immediate fix of the symptom (containment).
- **Corrective action:** action to eliminate the **root cause** of an existing nonconformity so it
  does not recur.
- **Preventive action:** action to eliminate the cause of a **potential** nonconformity before it
  occurs.

## 3. Triggers (CAPA inputs)

A CAPA may be opened from any of: complaints and user feedback; serious incidents or trends
(vigilance, PMS-001); post-market KPI breaches (KPI-001, e.g. a performance-drift flag or a
Fitzpatrick subgroup falling below threshold); internal audit findings; nonconformities; failed
verification/validation; SOUP vulnerabilities (soup_list.md); risk-control ineffectiveness
(RMF-RA-001).

## 4. CAPA process

1. **Record and describe** the issue; assign a CAPA ID and an owner.
2. **Risk assessment / containment:** assess immediate risk to safety; apply correction/containment
   if needed (e.g. restrict use, roll back a model version).
3. **Root-cause analysis:** investigate using a structured method (e.g. 5 Whys, fishbone). For AI
   issues, consider data (drift, representativeness), model, threshold/calibration, software, and
   use-related causes.
4. **Action plan:** define corrective and/or preventive actions in the risk-control priority order
   (design first, then protective measures, then information for safety).
5. **Impact assessment:** assess effect on the risk file, requirements, traceability, clinical
   evaluation, and other documents; update them under SOP-DC-001 change control.
6. **Implementation:** execute actions; for model changes, follow the predetermined change control
   plan (PCCP) with mandatory re-validation and recalibration.
7. **Effectiveness verification:** confirm, with objective evidence (e.g. re-test, KPI trend over a
   defined period), that the action worked and introduced no new risk.
8. **Closure:** close the CAPA with the verification evidence; if ineffective, reopen or escalate.

## 5. CAPA record (minimum fields)

CAPA ID | source/trigger | description | initial risk | root cause | action(s) (corrective/
preventive) | impacted documents | owner | due date | implementation evidence | effectiveness
verification | status (Open / In progress / Verifying / Closed) | closure date.

## 6. Linkage

- **PMS-001** feeds CAPA (Section 3) and CAPA status is a KPI in KPI-001.
- CAPA outcomes feed back into the **risk file** and, where relevant, **vigilance** reporting and
  **PSUR** content.
- CAPA effectiveness data is a record controlled under SOP-DC-001.

## 7. Change history

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-06-27 | Akhila N Pillai | Initial draft (simulation): CAPA triggers, process, record fields |
