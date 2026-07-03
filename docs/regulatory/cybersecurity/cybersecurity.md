# Cybersecurity Management and Assessment

> SIMULATION / TRAINING EXERCISE. DermaScan is a personal portfolio project, NOT a certified
> medical device. No real clinical use. Content is written in submission style for learning.

| Field | Value |
|---|---|
| Document ID | CYB-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Akhila N Pillai |
| Date | 2026-07-03 |
| Reviewed by | - |
| Approved by | - |

**Regs/standards/guidance:** MDR Annex I GSPR 17.2 and 17.4; MDCG 2019-16 (medical device
cybersecurity); IEC 81001-5-1 (secure health-software lifecycle); EU AI Act Art. 15; GDPR Art. 32;
context: Cyber Resilience Act (CRA), NIS2. **Related:** RMF-RA-001 (RISK-008, RISK-010), ARC-001,
DEP-001, SOUP-001, SRS-001 (REQ-042, REQ-050..054), AIA-001 (Art. 15), PMS-001.
**Study reference:** `steps/step-11-cybersecurity.html`.

---

## 1. Purpose and scope

This document defines the cybersecurity approach for DermaScan across the lifecycle: secure design,
security risk management, the threat model, the control set, and post-market vulnerability handling.
The governing principle is that **security is part of safety**: a vulnerability that can lead to
patient harm is a safety risk and is managed in the ISO 14971 file, not a separate silo.

## 2. Legal and standards basis

| Instrument | Requirement |
|---|---|
| MDR GSPR 17.2 | Software developed to the state of the art, considering information security |
| MDR GSPR 17.4 | IT security measures, including protection against unauthorized access |
| MDCG 2019-16 | Guidance: secure design, security risk management, IFU security information, post-market |
| IEC 81001-5-1 | Secure development lifecycle for health software (the "security IEC 62304") |
| EU AI Act Art. 15 | Resilience to errors and to attempts to alter use/performance (poisoning, adversarial, evasion) |
| GDPR Art. 32 | Security of processing of (special-category) personal data |
| CRA / NIS2 (context) | Horizontal product-security and operator-security duties; interplay noted |

## 3. Security risk management (parallel to ISO 14971)

A security risk assessment is run alongside the safety risk analysis. Threats are identified using
**STRIDE**; security risks that can result in patient harm are escalated into RMF-RA-001 (notably
RISK-008 adversarial/corrupted input and RISK-010 data loss/leak). Security risk = likelihood of
exploitation x impact; residual risk must be acceptable and is reduced in the ISO 14971 control
priority order (design first).

## 4. Threat model (STRIDE over the ARC-001 components)

| STRIDE threat | Where (ARC-001) | Control | Req / Risk |
|---|---|---|---|
| **S**poofing (identity) | C1 API layer | Authentication of callers; token management (Secret Manager) | REQ-050; RISK-010 |
| **T**ampering (data/model) | C5 model, C2 input, C8 logs | Input validation; governed model/data buckets; tamper-evident logs | REQ-051, REQ-042; RISK-008 |
| **R**epudiation | C8 logging | Audit logs with timestamp, model version, input hash | REQ-040, REQ-042 |
| **I**nformation disclosure | C1/C9 | Encryption in transit/at rest; data minimization; least-privilege IAM | REQ-053; RISK-010 |
| **D**enial of service | C1 edge | Rate limiting / WAF (Cloud Armor); autoscaling | REQ-054; RISK-008 |
| **E**levation of privilege | Platform | Least-privilege IAM; no broad roles in runtime; secret isolation | REQ-050 |

## 5. Secure-by-design and defence in depth

- **Authentication and authorization** on the API before any result is returned (REQ-050).
- **Input validation and sanitization** at the boundary; robustness to malformed input (REQ-051, C2).
- **Encryption** in transit and at rest; data minimization (REQ-053).
- **Least privilege** identities per service (DEP-001 IAM).
- **Rate limiting / edge protection** to blunt DoS and model-extraction (REQ-054, Cloud Armor).
- **Tamper-evident logging** for audit and forensics (REQ-042, AI Act Art. 12).
- **Secret management** (no secrets in code; Secret Manager).

## 6. AI-specific security threats (AI Act Art. 15)

| Threat | Description | Control |
|---|---|---|
| Adversarial examples | Crafted perturbations flip the output | Robustness/metamorphic testing (REQ-052, TST-022); input quality/OOD gates (C3, C4) |
| Data poisoning | Corrupted training data biases the model | Governed, versioned datasets with provenance (DG-001); access control on data buckets |
| Model poisoning / supply chain | Tampered model artifact or dependency | Signed/versioned model registry; SOUP integrity (SOUP-001); pinned dependencies |
| Model inversion / extraction | Reconstructing model or training data via the API | Rate limiting; output minimization (REQ-054); authentication |
| Evasion | Inputs engineered to bypass detection | OOD detection; monitoring; anomaly logging |

## 7. Software Bill of Materials (SBOM) and vulnerability management

- The **SOUP list (SOUP-001) serves as the SBOM**: every component with a pinned version.
- **Monitoring:** track CVE feeds and vendor/GitHub advisories for listed components and GCP SDKs.
- **Triage:** score with CVSS; assess safety/security relevance against the risk file.
- **Remediation:** patch/upgrade under change control (SOP-DC-001, SOP-DESIGN-001); re-verify; if a
  vulnerability is safety-relevant, open a CAPA (SOP-CAPA-001) and consider vigilance.
- **Coordinated vulnerability disclosure:** a defined intake channel and response process (MDCG
  2019-16 expectation).

## 8. Cloud security (links DEP-001)

The GCP deployment implements the technical controls: Cloud IAM (least privilege), Secret Manager,
Cloud Armor (rate limiting/WAF), default encryption plus optional CMEK, private networking, and Cloud
Audit Logs. Google Cloud is a supplier (ISO 13485 7.4): its certifications (ISO/IEC 27001, 27017,
27018, SOC 2) and the Data Processing Agreement are recorded as supplier evidence (DEP-001 Section 7).
The shared-responsibility split is documented (provider secures the platform; DermaScan secures its
configuration, code, identities, and data).

## 9. Security information for the deployer (IFU)

The IFU states the security assumptions and the deployer's responsibilities: use over secure
channels, manage credentials, apply updates, and report suspected incidents. (MDCG 2019-16 expects
security information to users; links REQ-033.)

## 10. Post-market cybersecurity (links PMS-001)

Security is monitored in the post-market phase: continuous vulnerability monitoring, periodic
re-assessment, incident response, and coordinated disclosure. A security incident that meets the
serious-incident definition is handled under vigilance (PMS-001 Section 7); security KPIs and
patch status can be tracked alongside KPI-001.

## 11. Open items

- Execute the security tests (TST-022 robustness, TST-023 security, TST-054 rate limiting) in V&V.
- Produce a formal SBOM export from pinned dependencies once `src/` exists.
- Define the CVSS triage thresholds and the coordinated-disclosure contact.
- Confirm CMEK and network topology in DEP-001.

## 12. Change history

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-07-03 | Akhila N Pillai | Initial draft (simulation): standards basis, STRIDE threat model, AI threats, SBOM, post-market |
