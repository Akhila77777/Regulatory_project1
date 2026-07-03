# infra/ - Infrastructure as Code (scaffolding)

> SIMULATION / TRAINING EXERCISE. Terraform stubs only; nothing is deployed. See DEP-001 for the
> full deployment/MLOps architecture. Not for clinical use.

Target: Google Cloud Platform, EU region (e.g. `europe-west3`) for GDPR data residency.

Planned resources (stubs in `main.tf`):
- Cloud Run service (inference API, ARC-001 C1-C9) - REQ-014, availability KPI
- Artifact Registry (container images) - SDP-001 config items
- Cloud Storage buckets (model artifacts, governed datasets) - REQ-041, DG-001
- IAM (least privilege) + Secret Manager - REQ-050, RISK-010
- Cloud Armor + Load Balancer (rate limiting / WAF) - REQ-054, RISK-008
- Cloud Logging / Audit Logs (tamper-evident) - REQ-040/042, AI Act Art. 12
- Cloud Monitoring (uptime) + Vertex AI Model Monitoring (drift/skew) - KPI-001, RISK-004/006

Everything is versioned so environments are reproducible (config management, IEC 62304 clause 8).
TODO: fill in real resource definitions; keep all data and compute in an EU region.
