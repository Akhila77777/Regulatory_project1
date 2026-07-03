# Deployment and MLOps Architecture (Google Cloud Platform)

> SIMULATION / TRAINING EXERCISE. DermaScan is a personal portfolio project, NOT a certified
> medical device and NOT a live clinical service. This describes the intended/target cloud
> architecture for learning; no real patient data is processed and nothing is clinically deployed.

| Field | Value |
|---|---|
| Document ID | DEP-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Akhila N Pillai |
| Date | 2026-07-03 |
| Reviewed by | - |
| Approved by | - |

**Standards/regs touched:** IEC 62304 (lifecycle/config mgmt), MDR GSPR 17 (security), EU AI Act
Art. 12 (logging), Art. 15 (robustness/cybersecurity), Art. 72 (post-market monitoring), GDPR
(data residency/protection), ISO 13485 7.4 (supplier/purchasing control). **Related:** ARC-001,
SRS-001, SDP-001, SOUP-001, AIA-001, PMS-001, KPI-001, DG-001, cybersecurity (build phase 11).
**Study reference:** `steps/step-04`, `step-10`, `step-11`.

---

## 1. Purpose and scope

This document defines how DermaScan is intended to be built, deployed, run, and monitored on
**Google Cloud Platform (GCP)**, and how each piece maps to the regulatory requirements already
specified. It covers the runtime inference service (the components in ARC-001), the offline
training/evaluation pipeline (MLOps), and the observability/monitoring that feeds post-market
surveillance.

## 2. Guiding principles

- **EU data residency:** all data and compute in an EU region (e.g. `europe-west3` Frankfurt) for
  GDPR alignment; no health-related data leaves the EU.
- **Least privilege:** IAM roles scoped per service; no broad owner accounts in runtime.
- **Reproducible infrastructure:** infrastructure as code (Terraform) so environments are versioned
  and auditable (config management, IEC 62304 clause 8).
- **Everything logged:** every inference and every deployment is recorded (AI Act Art. 12).
- **Human gate before release:** no model reaches production without passing evaluation gates and an
  explicit approval (design review / predetermined change control plan, PCCP).

## 3. Runtime (serving) architecture

| Concern | GCP service | Maps to |
|---|---|---|
| Inference API (FastAPI service, ARC-001 C1-C9) | **Cloud Run** (containerized, HTTPS, autoscaling) | REQ-014 latency, availability KPI |
| Container images | **Artifact Registry** | SDP-001 config items |
| Trained model artifact (versioned) | **Cloud Storage** bucket (or Vertex AI Model Registry) | REQ-041 model/version binding |
| Secrets (keys, tokens) | **Secret Manager** | REQ-050 auth, security |
| Access control | **Cloud IAM** (least privilege) | REQ-050, RISK-010 |
| Edge protection / rate limiting / WAF | **Cloud Armor** (+ Load Balancer) | REQ-054, RISK-008 |
| Audit and event logs | **Cloud Logging** + **Cloud Audit Logs** (tamper-evident, retained) | REQ-040, REQ-042, AI Act Art. 12 |
| Availability / performance metrics | **Cloud Monitoring** (uptime checks) | KPI-001 service availability |
| Encryption | Default encryption at rest and in transit; optional **CMEK** | REQ-053, GDPR Art. 32 |

Data flow is unchanged from ARC-001 (gate-before-model ordering); GCP provides the hosting, identity,
logging, and network-security layers around it.

## 4. Offline MLOps pipeline (Vertex AI)

Training and evaluation run **outside** the patient-facing runtime, orchestrated as a
**Vertex AI Pipeline**, with regulatory gates built into the pipeline itself:

1. **Data ingestion & validation** - datasets pulled from the governed Cloud Storage bucket
   (DG-001/DSC-001); schema/quality checks; leakage checks.
2. **Training** - Vertex AI training job (PyTorch); run parameters, dataset version, and code commit
   recorded (reproducibility, REQ-041).
3. **Evaluation gate** - compute sensitivity/specificity/AUROC, calibration, and **per-Fitzpatrick
   subgroup** metrics; the pipeline **fails the build** if acceptance criteria (SRS REQ-010..013) or
   subgroup-fairness thresholds are not met. This is automated V&V evidence (TRC-001).
4. **Model registry & approval** - a passing model is registered in **Vertex AI Model Registry**; a
   human approval step (design review / PCCP) is required before deployment.
5. **Deploy** - approved model promoted; new Cloud Run revision rolled out (canary/gradual).
6. **Monitor** - see Section 5; findings can re-trigger the pipeline (retrain) under the PCCP.

## 5. Monitoring and post-market feedback

- **Vertex AI Model Monitoring** watches for **prediction drift and training/serving skew** in
  production, directly operationalizing **RISK-006** (dataset shift) and supporting **RISK-004**
  (subgroup fairness) monitoring.
- **Cloud Monitoring** provides availability/latency; **Cloud Logging** provides the inference audit
  trail.
- These feed **KPI-001** (the dashboard) and **PMS-001**: a drift or subgroup-threshold breach opens
  a CAPA (SOP-CAPA-001) and may trigger controlled retraining via the pipeline under the PCCP.

## 6. Environments and CI/CD

- **Environments:** dev, staging, prod, isolated by GCP project, all EU-region.
- **CI/CD:** source in Git; **Cloud Build** (or GitHub Actions) builds and tests the container, runs
  unit/integration/API tests (TST-XXX), pushes to Artifact Registry, and deploys to Cloud Run.
- **Change control:** infrastructure and deployment changes follow SOP-DESIGN-001 / SOP-DC-001; model
  changes follow the PCCP. Significant changes are re-assessed against CLS-001.

## 7. Supplier / purchasing control (ISO 13485 7.4)

Google Cloud is treated as a **supplier of an outsourced process**. Supplier-control considerations:
Google Cloud's certifications (e.g. ISO/IEC 27001, ISO 27017/27018, SOC 2) are recorded as supplier
evidence; a **Data Processing Agreement (DPA)** and EU-region configuration are required for GDPR;
the division of responsibility (shared-responsibility model) is documented. Cloud SDKs/libraries used
in code remain **SOUP** and are listed in SOUP-001; the managed services themselves are handled as
supplier control rather than SOUP.

## 8. Data protection (GDPR) specifics

- Health-related images are special-category data (GDPR Art. 9). In this simulation only public,
  licensed datasets are used and no real patient data is processed.
- For any real deployment: EU-region storage/compute only, a signed Google Cloud DPA, optional CMEK,
  data minimization, access logging, and a DPIA (DG-001 Section 8). German BDSG and the European
  Health Data Space would also apply.

## 9. Cybersecurity alignment (preview of build phase 11)

IAM least privilege, Secret Manager, Cloud Armor (rate limiting/WAF), private networking, default
encryption, and audit logging implement the security requirements (REQ-050..054) and AI Act Art. 15.
The AI-specific threats (data/model poisoning, adversarial input, model inversion) are mitigated by
governed data buckets, access control, input validation (ARC-001 C2), and output/rate limiting. Full
treatment is in the cybersecurity file (phase 11), which will reference this document.

## 10. Impact on existing documents (change checklist)

Adding GCP affects, and is cross-referenced from: ARC-001 (hosting layer), SRS-001 (availability,
security, logging requirements are now realizable and testable in-cloud), SOUP-001 (cloud SDKs) and
supplier control, PMS-001 / KPI-001 (monitoring data sources), AIA-001 (logging Art. 12, monitoring
Art. 72), and DG-001 (data residency). No intended-purpose or classification change results (CLS-001
unaffected).

## 11. Open items

- Write the Terraform IaC and the Cloud Build/Vertex pipeline definitions (code, `src/` + `infra/`).
- Confirm the EU region and whether CMEK is used.
- Define drift/skew thresholds in Vertex AI Model Monitoring aligned with CLIN-001 and KPI-001.
- Record the Google Cloud DPA and supplier evidence in the QMS supplier file.

## 12. Change history

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-07-03 | Akhila N Pillai | Initial draft (simulation): GCP runtime + Vertex AI MLOps pipeline + regulatory mapping |
