# Post-Market Surveillance Plan (incl. PMCF and Vigilance)

> SIMULATION / TRAINING EXERCISE. DermaScan is a personal portfolio project, NOT a certified
> medical device. No real post-market data, no real incidents, no real vigilance reporting. Content
> is written in submission style for learning.

| Field | Value |
|---|---|
| Document ID | PMS-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Akhila N Pillai |
| Date | 2026-06-27 |
| Reviewed by | - |
| Approved by | - |

**Regulations:** MDR 2017/745 Art. 83-86 and Annex III (PMS), Annex XIV Part B (PMCF), Art. 87-88
(vigilance, trend reporting); EU AI Act Art. 72 (post-market monitoring), Art. 73 (serious incident
reporting). **Related:** RMF-RA-001 (RISK-004, RISK-006), CLIN-001, AIA-001 (Section 10), KPI-001
(dashboard), DSC-001, IU-001, DEP-001 (monitoring data sources), CYB-001 (post-market security).
**Study reference:** `steps/step-10-pms-eudamed-vigilance.html`.

---

## 1. Purpose and scope

This plan defines the proactive and reactive post-market surveillance of DermaScan across its
lifecycle, integrated with the quality and risk systems. Because DermaScan is also a high-risk AI
system, this single plan is intended to satisfy MDR PMS and the EU AI Act post-market monitoring
duty (Art. 72) together. The KPI dashboard (KPI-001) is the operational instrument of this plan.

## 2. PMS system and responsibilities

PMS is a continuous, planned activity, not a one-off. Responsibilities (held by the author in this
solo project, named to reflect the real process): a PMS owner collates and analyses data; the risk
management lead updates the risk file; the (simulated) clinical reviewer assesses clinical impact;
the software lead implements corrective changes.

## 3. Data sources (PMS inputs)

| Type | Source | In DermaScan |
|---|---|---|
| Reactive | Complaints and user feedback | Complaint log; deployer feedback |
| Reactive | Incidents and near-misses | Vigilance intake (Section 7) |
| Proactive | Real-world performance logs | Inference logs (REQ-040), Cloud Logging (DEP-001), KPI-001 |
| Proactive | Model drift / subgroup monitoring | Vertex AI Model Monitoring (DEP-001), KPI-001 (RISK-006, RISK-004) |
| Proactive | Service availability / latency | Cloud Monitoring uptime checks (DEP-001) |
| Proactive | PMCF | Section 6 |
| External | Literature and state of the art | Periodic literature scan (feeds CLIN-001) |
| External | Similar devices / field safety notices | Monitoring of comparable AI dermatology tools |
| Internal | CAPA, audits, change records | QMS (build phase 5) |

## 4. What PMS monitors (indicators)

The KPI catalogue in KPI-001 defines the monitored indicators with targets, spanning service
availability, model performance (overall and per Fitzpatrick subgroup), AUROC, calibration, OOD
rejection, input-quality failures, complaints, serious incidents, reporting timeliness, and CAPA
status. Each indicator has a defined target and an alert threshold.

## 5. AI-specific post-market monitoring (AI Act Art. 72)

DermaScan's performance can degrade silently as real-world data drifts, and bias can emerge in new
populations. The plan therefore explicitly monitors:
- **Performance drift** versus the validated baseline (RISK-006): a drop beyond the defined
  threshold raises a drift flag.
- **Subgroup fairness drift** (RISK-004): per-Fitzpatrick sensitivity is tracked; a subgroup falling
  below threshold triggers investigation even if aggregate metrics look acceptable.
- **Calibration and OOD behaviour** over time.
These are computed from logged real-world outcomes and periodic re-evaluation, surfaced in KPI-001,
and fed back to the risk file and clinical evaluation.

## 6. Post-Market Clinical Follow-up (PMCF) plan (Annex XIV Part B)

- **Objective:** confirm, in real use, the safety and performance claimed in CLIN-001, and detect
  emerging risks and previously unknown subgroup effects.
- **Methods:** analysis of real-world performance against the reference standard where outcomes are
  available; periodic re-evaluation on refreshed/representative data; targeted data collection for
  under-represented subgroups (to close the RISK-004 gap and potentially widen the validated
  Fitzpatrick range in IU-001); literature surveillance.
- **Outputs:** a PMCF evaluation report feeding back into CLIN-001 and the benefit-risk
  determination (RMF-RPT-001).

## 7. Vigilance and serious-incident reporting

| Item | Definition / rule |
|---|---|
| Serious incident | An event that led, might have led, or might lead to death or serious deterioration of health |
| MDR reporting (Art. 87) | Without undue delay and no later than 15 days; 10 days for a serious public-health threat; 2 days for death or serious deterioration |
| FSCA / FSN | Field Safety Corrective Action (e.g. model update, usage restriction, withdrawal) communicated via a Field Safety Notice |
| Trend reporting (Art. 88) | Statistically significant increases in non-serious incidents or expected side effects are reported |
| AI Act (Art. 73) | Serious incidents reported to the relevant market surveillance authority |

A DermaScan-specific worked example of a serious incident would be a confirmed pattern of false
negatives contributing to delayed diagnoses; this would trigger investigation, CAPA, a possible
FSCA, and reporting.

## 8. EUDAMED and UDI

- The device, actors, and (where applicable) certificates are registered in **EUDAMED**; vigilance
  and PMS data are reported through the relevant EUDAMED modules.
- A **UDI** (Device Identifier plus Production Identifier) provides traceability; for software the
  UDI is carried in documentation and an "about" screen and changes with significant software
  versions.
- Currency note: **mandatory EUDAMED use is phasing in around 28 May 2026** (actor, UDI/device, and
  notified-body/certificate modules first, vigilance and market surveillance following), moving from
  voluntary to required. (Simulation: no real registration is performed.)

## 9. PMS outputs and frequency

As a Class IIa device, DermaScan produces a **Periodic Safety Update Report (PSUR)**, not a simple
PMS report. The PSUR summarises PMS data and KPI trends, the conclusions of the benefit-risk
determination, the main findings of PMCF, and any preventive/corrective actions, and is updated
periodically (and on significant findings). It draws directly on KPI-001 and CLIN-001.

## 10. Feedback loop (closing the lifecycle)

PMS findings feed back into:
- the **risk file** (new or changed RISK items; re-estimated probabilities);
- the **clinical evaluation** (CLIN-001) and benefit-risk (RMF-RPT-001);
- **CAPA** and, where a model change is needed, **controlled retraining under the predetermined
  change control plan (PCCP)** with mandatory re-validation and recalibration;
- **design and requirements** (new REQ/RISK, updated traceability).
A drift flag or subgroup breach in KPI-001 is the typical entry point to this loop.

## 11. Open items

- Define numeric alert thresholds aligned with CLIN-001 once real performance is established.
- Connect KPI-001 to real logging/evaluation outputs once `src/` exists.
- Write the QMS CAPA SOP (build phase 5) that this plan invokes.
- Define the PCCP bounds for permissible automated/retraining changes.

## 12. Change history

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-06-27 | Akhila N Pillai | Initial draft (simulation): integrated MDR PMS + PMCF + vigilance + AI Act Art. 72/73 |
