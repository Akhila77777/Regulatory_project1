# SOUP List (Software of Unknown Provenance)

> SIMULATION / TRAINING EXERCISE. DermaScan is a personal portfolio project, NOT a certified
> medical device. No real clinical use. Content is written in submission style for learning.

| Field | Value |
|---|---|
| Document ID | SOUP-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Akhila N Pillai |
| Date | 2026-06-27 |
| Reviewed by | - |
| Approved by | - |

**Standard:** IEC 62304:2006+A1:2015 (5.3.3, 5.3.4, 8.1.2). **Related:** SDP-001, SSC-001,
requirements.txt (to be pinned), CYB-001 (cybersecurity, SBOM), DEP-001 (cloud services / supplier).
> Cloud scope note: DermaScan also depends on managed GCP services (Cloud Run, Cloud Storage,
> Vertex AI, IAM, etc.). These managed services are handled as supplier control (ISO 13485 7.4) in
> DEP-001 Section 7, not as SOUP. Any client SDK or library imported into the codebase (for example
> the Google Cloud client libraries) IS SOUP and must be added to the inventory below with a pinned
> version when introduced.
**Study reference:** `steps/step-04-iec62304-software.html` and `step-11-cybersecurity.html`.

---

## 1. Purpose

This list identifies all Software of Unknown Provenance (SOUP) used in DermaScan and records, for
each item, its purpose, the functional and performance requirements it must meet, and the approach
to evaluating its known anomalies. For a Class C system (SSC-001), SOUP control is mandatory. This
list also serves as the basis for the Software Bill of Materials (SBOM) used in cybersecurity.

## 2. SOUP control method

For each SOUP item:
1. Identify it: name and **pinned** version (versions are pinned in requirements.txt).
2. State its purpose and the requirements it must satisfy.
3. State the hardware/software it requires (Python runtime; CPU/GPU as applicable).
4. Evaluate **known anomalies**: review the project's public issue tracker / changelog and known
   vulnerability sources (for example CVE / GitHub advisories) for anomalies relevant to safety or
   security; assess relevance; mitigate or accept with rationale.
5. Re-assess on each version change and periodically (vulnerability monitoring).

> Versions below are placeholders to be fixed when the environment is pinned. The control method is
> binding; the exact version strings are provisional until requirements.txt is finalised.

## 3. SOUP inventory

| SOUP ID | Component | Version (pin) | Purpose | Key requirements | Known-anomaly approach |
|---|---|---|---|---|---|
| SOUP-001 | PyTorch | TBD (pin) | Model definition, training, inference | Correct tensor ops; deterministic inference with fixed seed; supported on target runtime | Track release notes and CVE/advisories; pin version; re-test on upgrade |
| SOUP-002 | torchvision | TBD (pin) | Image transforms, model utilities | Correct, documented image transforms | As above |
| SOUP-003 | NumPy | TBD (pin) | Numerical processing | Correct numerical results | As above |
| SOUP-004 | Pillow (PIL) | TBD (pin) | Image loading/decoding | Correct decode of supported formats; reject malformed images | Image-decoding libraries are a common CVE source; monitor advisories; validate inputs (REQ-051) |
| SOUP-005 | scikit-learn | TBD (pin) | Evaluation metrics, calibration | Correct metric computation (sensitivity, specificity, AUROC, calibration) | Track advisories; pin version |
| SOUP-006 | FastAPI | TBD (pin) | Inference API framework | Correct request handling; schema validation | Track advisories; pin version |
| SOUP-007 | Uvicorn | TBD (pin) | ASGI server | Reliable serving | Track advisories; pin version |
| SOUP-008 | Pydantic | TBD (pin) | Request/response schema validation | Enforce input/output schema incl. mandatory disclaimer field (REQ-030) | Track advisories; pin version |
| SOUP-009 | Python standard library / runtime | TBD (pin) | Base runtime | Stable runtime | Track Python security releases |

(Add rows as dependencies are introduced; every new third-party library must be added here before
use, per SDP-001.)

## 4. Anomaly and vulnerability monitoring

SOUP anomalies and vulnerabilities are monitored on an ongoing basis (changelogs, CVE feeds,
advisories). A vulnerability assessed as safety- or security-relevant is raised as a problem
(SDP-001 clause 9 / problem resolution), assessed against the risk file (notably RISK-008 and
RISK-010), and remediated or accepted with documented rationale. This feeds the cybersecurity
documentation (build phase 11).

## 5. Change history

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-06-27 | Akhila N Pillai | Initial draft (simulation): SOUP method + 9-item inventory (versions to pin) |
