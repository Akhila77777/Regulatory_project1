# Post-Market Performance & Quality KPI Dashboard (Specification)

> SIMULATION / TRAINING EXERCISE. DermaScan is a personal portfolio project, NOT a certified
> medical device. No real clinical or post-market data. Content is written in submission style for
> learning. All values in the data template are illustrative.

| Field | Value |
|---|---|
| Document ID | KPI-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Akhila N Pillai |
| Date | 2026-06-27 |
| Reviewed by | - |
| Approved by | - |

**Purpose link:** supports MDR Post-Market Surveillance trend analysis (Art. 83-86) and EU AI Act
post-market monitoring (Art. 72). **Related:** pms_plan.md (PMS-001), RMF-RA-001
(RISK-004, RISK-006), CLIN-001, AIA-001 (Section 10), DSC-001. **Skill showcase:** advanced
Microsoft Excel (data model, PivotTables, PivotCharts, slicers, XLOOKUP).
**Study reference:** `steps/step-10-pms-eudamed-vigilance.html`.

---

## 1. Why this exists (and why not "OEE")

For a Software as a Medical Device there is no production equipment, so classical Overall Equipment
Effectiveness (OEE) does not apply. The same monitoring discipline is, however, required for the
software in the post-market phase. This dashboard adapts the OEE idea into a software-service
"effectiveness" view built from three pillars, while remaining a valid PMS instrument:

| OEE pillar (manufacturing) | DermaScan software analog |
|---|---|
| Availability | Service availability (API uptime) |
| Performance | Model performance vs validated baseline (sensitivity, AUROC, drift) |
| Quality | Output quality (calibration, out-of-distribution handling, complaint/incident rate) |

## 2. KPI catalogue

| KPI | Category | Definition | Target (placeholder) | Linked risk/req |
|---|---|---|---|---|
| Service availability | Availability | Uptime % of the inference API in the period | >= 99.5% | RISK-010 |
| Inference volume | Availability | Count of inferences in the period | trend only | - |
| Sensitivity (overall) | Performance | Real-world/periodic re-eval sensitivity | >= 0.90 | REQ-010, RISK-001 |
| Sensitivity by Fitzpatrick | Performance | Sensitivity per phototype I-VI | within 0.05 of overall | REQ-013, RISK-004 |
| AUROC | Performance | Periodic AUROC vs baseline | >= baseline - 0.03 | REQ-011 |
| Performance drift flag | Performance | Drop vs validated baseline beyond threshold | none | RISK-006 |
| Calibration error (ECE) | Quality | Expected calibration error | <= threshold | REQ-012, RISK-007 |
| OOD rejection rate | Quality | Share of inputs correctly rejected as out-of-distribution | within expected band | REQ-020, RISK-003 |
| Input-quality failure rate | Quality | Share of inputs rejected by quality gate | trend only | REQ-021 |
| Complaint rate | Quality | Complaints per 1,000 inferences | downward/stable | PMS |
| Serious incidents | Quality | Count of serious incidents in period | 0 | Vigilance (Art. 87) |
| Incident reporting timeliness | Quality | % reported within MDR deadline | 100% | Vigilance |
| CAPA open / overdue | Quality | Open CAPAs and count past due date | 0 overdue | CAPA |

## 3. Data model (for Excel)

Use a **tidy (long) fact table** loaded into the Excel Data Model so one PivotTable/PivotChart set
can serve every KPI, sliced by period and subgroup.

Fact table `kpi_facts` (see `kpi_dashboard_data_template.csv`):

| Column | Type | Notes |
|---|---|---|
| Period | text (YYYY-MM) | Monthly granularity |
| Category | text | Availability / Performance / Quality |
| KPI | text | KPI name from the catalogue |
| Subgroup | text | "All" or Fitzpatrick I-VI / age / sex |
| Value | number | Measured value |
| Target | number | Threshold for that KPI |
| Unit | text | %, ratio, count, per1000 |
| Direction | text | "higher_better" or "lower_better" |

Optional dimension tables (for a cleaner model and slicers): `dim_period` (Period, Quarter, Year),
`dim_kpi` (KPI, Category, Target, Direction). Relate them to `kpi_facts` on Period and KPI.

## 4. Build steps in Excel (skill showcase)

1. **Get Data** -> import `kpi_dashboard_data_template.csv`; load to the **Data Model** (Power Query).
2. Create `dim_kpi` and `dim_period` and set **relationships** to the fact table.
3. Add a **status measure** with XLOOKUP/IF logic: compare `Value` to `Target` honouring
   `Direction` to output On Target / Watch / Breach (drives conditional formatting / a traffic-light
   column).
4. Build **PivotTables**: KPI by Period; Sensitivity by Fitzpatrick by Period.
5. Build **PivotCharts**: line charts for performance/availability trends; clustered column for
   subgroup sensitivity; a KPI summary card area.
6. Add **slicers/timeline** for Period, Category, and Subgroup so the board is interactive.
7. Apply **conditional formatting** (traffic lights) on the status measure; add a "drift/alert"
   panel listing any KPI in Breach.

## 5. How it drives action (closing the loop)

- A Performance-drift flag or a Fitzpatrick subgroup breach triggers investigation under PMS and,
  if confirmed, a CAPA and/or controlled retraining under the predetermined change control plan
  (RISK-006, RISK-004).
- Serious-incident and timeliness KPIs support MDR vigilance/trend reporting (Art. 87-88).
- The board feeds the PSUR (Class IIa) narrative (build phase 10).

## 6. Open items

- Replace placeholder targets with values aligned to the clinical evaluation (CLIN-001).
- Connect to the real logging/evaluation outputs (REQ-040) once `src/` exists.
- Add EUDAMED/UDI reference fields when the PMS plan is written.

## 7. Change history

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-06-27 | Akhila N Pillai | Initial draft (simulation): KPI catalogue, Excel data model, build steps |
