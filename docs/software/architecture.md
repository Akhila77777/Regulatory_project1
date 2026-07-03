# Software Architecture and Design Description

> SIMULATION / TRAINING EXERCISE. DermaScan is a personal portfolio project, NOT a certified
> medical device. No real clinical use. Content is written in submission style for learning.

| Field | Value |
|---|---|
| Document ID | ARC-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Akhila N Pillai |
| Date | 2026-06-27 |
| Reviewed by | - |
| Approved by | - |

**Standard:** IEC 62304 clause 5.3 (architectural design); detailed design (5.4) required for
Class C (SSC-001). **Related:** SRS-001 (REQ-XXX), TRC-001, SDP-001, SSC-001, SOUP-001, AIA-001,
DEP-001 (deployment/MLOps on GCP), CYB-001 (cybersecurity).
**Study reference:** `steps/step-09-verification-validation.html` and `step-04-iec62304-software.html`.

---

## 1. Purpose and scope

This document describes the software architecture of DermaScan: its decomposition into software
items, their interfaces, the SOUP boundaries, and the data flow, and it maps each item to the
requirements it implements (SRS-001) and the risks it controls (RMF-RA-001). It confirms the
component names referenced as "intended" in TRC-001. As a Class C system, a detailed design (5.4)
will be developed per item; this document is the architectural (5.3) level.

## 2. Architectural overview

DermaScan is a standalone software service (SaMD). A client in the deployer's clinical workflow sends
an image to the inference API; the system validates and screens the input, runs the model, calibrates
and frames the result with the mandatory disclaimer, logs the event, and returns the response. There
is no autonomous downstream action (REQ-031). The runtime hosting, identity, logging, and
network-security layers around these components are provided by the GCP deployment described in
DEP-001; this document specifies the application, DEP-001 specifies where and how it runs.

## 3. Software items (decomposition)

| Item | Responsibility | Implements (REQ) | Controls (RISK) | SOUP |
|---|---|---|---|---|
| C1 API / interface layer | Request handling, authentication/authorization, rate limiting, response schema (incl. disclaimer field) | REQ-030, REQ-050, REQ-054 | RISK-005, RISK-010, RISK-008 | FastAPI, Uvicorn, Pydantic |
| C2 Input handler | Format/resolution validation, decoding, single-lesion handling | REQ-001, REQ-003, REQ-051 | RISK-008 | Pillow |
| C3 Image-quality gate | Focus/framing/illumination checks; reject/flag poor images | REQ-021 | RISK-003 | NumPy, Pillow |
| C4 Out-of-distribution (OOD) detector | Detect unsupported/OOD inputs; block scoring; unsupported-input notice | REQ-020, REQ-023 | RISK-003, RISK-001, RISK-004 | PyTorch, NumPy |
| C5 Inference engine | Run the trained model to produce a raw malignancy score | REQ-002 (raw) | RISK-001 | PyTorch, torchvision |
| C6 Calibration & confidence | Calibrate probability; compute confidence; low-confidence flag | REQ-004, REQ-012 | RISK-007, RISK-001 | scikit-learn, NumPy |
| C7 Output/presentation formatter | Risk band (not bare verdict), warnings, mandatory disclaimer, uncertainty for oversight | REQ-002, REQ-022, REQ-030, REQ-032 | RISK-002, RISK-005, RISK-009 | - |
| C8 Logging subsystem | Tamper-evident event log: timestamp, model+data version, input hash, result | REQ-040, REQ-041, REQ-042 | RISK-006, RISK-010 | std lib |
| C9 Security & data protection | Encryption in transit/at rest, data minimization | REQ-053 | RISK-010 | platform/TLS |
| C10 Evaluation pipeline (offline) | Compute performance, subgroup, calibration metrics for V&V and PMS | REQ-010, REQ-011, REQ-013 | RISK-001, RISK-002, RISK-004 | scikit-learn, NumPy |

(Offline training is part of the development environment, not the runtime service; the trained model
artifact and dataset version are configuration items, SDP-001.)

## 4. Runtime data flow

1. Client -> **C1** (authenticated request with one image).
2. **C1** -> **C2** input validation -> **C3** quality gate -> **C4** OOD check.
   - If C2/C3/C4 reject: return an unsupported-input/low-quality notice (no score), with disclaimer.
3. Valid input -> **C5** inference -> **C6** calibration/confidence.
4. **C7** formats the risk band, confidence, warnings, and mandatory disclaimer.
5. **C8** logs the event (model/data version, input hash, result).
6. **C1** returns the response (always carrying the disclaimer field, REQ-030).

This ordering enforces that an out-of-distribution or low-quality input can never reach the model and
be returned as a confident low-risk score, which is the core control for RISK-001 and RISK-003.

## 5. Interfaces

- **External (deployer-facing):** the inference API contract (request: image + metadata; response:
  risk band, confidence, flags, mandatory disclaimer). Versioned; see SRS for the contract details.
- **Internal:** typed interfaces between C2 to C7; the model artifact interface (C5); the log sink
  (C8). All inter-item interfaces are specified in detailed design (5.4).

## 6. SOUP boundaries

Each SOUP item (SOUP-001) is isolated behind the using component (table in Section 3). Image-decoding
(Pillow) and the API/serialization layer (FastAPI, Pydantic, Uvicorn) are the primary external attack
surface and are paired with input validation (C2) and security controls (C1, C9); SOUP anomalies are
monitored per soup_list.md.

## 7. Segregation note (IEC 62304)

The system is treated as Class C as a whole (SSC-001). No formal segregation claim is made to reduce
the class of any item at this stage. If, in detailed design, items that cannot contribute to serious
harm (for example the offline evaluation pipeline C10, which is not in the patient-facing runtime
path) are demonstrably segregated, they may be documented at a lower class with justification. C10 is
a candidate but is not claimed as segregated here.

## 8. Architectural decisions and rationale

- **Gate-before-model ordering** (C2/C3/C4 before C5): prevents invalid inputs from producing trusted
  outputs (RISK-001, RISK-003).
- **Calibrated risk band, not binary verdict** (C6/C7): supports clinician interpretation and
  oversight, limits over-definitive output (RISK-002, RISK-005).
- **Disclaimer enforced at the schema level** (C1/C7): guarantees it is present on every response
  (REQ-030), rather than relying on UI discipline.
- **Version binding in logs** (C8): enables reproducibility, drift attribution, and change control
  (RISK-006).

## 9. Open items

- Develop the detailed design (5.4) per item, including internal interface specifications.
- Confirm the OOD/quality methods (C3, C4) and the calibration method (C6) when `src/` is built.
- Finalize the API contract schema in coordination with SRS-001.

## 10. Change history

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-06-27 | Akhila N Pillai | Initial draft (simulation): 10-item architecture, data flow, REQ/RISK/SOUP mapping |
