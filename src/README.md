# DermaScan source (scaffolding)

> SIMULATION / TRAINING EXERCISE. Scaffolding only: package structure, signatures, and docstrings
> that reference the regulatory IDs. No working logic and no trained model yet. Not for clinical use.

## Layout (maps to ARC-001 components)

| Path | ARC-001 | Responsibility | Key REQ / RISK |
|---|---|---|---|
| `src/common/config.py` | - | Config, constants, mandatory disclaimer text | REQ-030 |
| `src/common/logging.py` | C8 | Tamper-evident inference/audit logging | REQ-040, REQ-041, REQ-042 / RISK-006, RISK-010 |
| `src/api/schemas.py` | C1, C7 | Request/response schema (disclaimer field) | REQ-002, REQ-030 |
| `src/api/main.py` | C1, C7 | FastAPI service, auth, rate limiting, response | REQ-001, REQ-030, REQ-050, REQ-054 / RISK-005, RISK-010 |
| `src/data/preprocessing.py` | C2, C3 | Input validation and image-quality gate | REQ-001, REQ-003, REQ-021 / RISK-003 |
| `src/data/loading.py` | C10 | Dataset loading/splits (governed data) | DG-001, DSC-001 |
| `src/models/model.py` | C5 | Model definition | RISK-001 |
| `src/models/ood.py` | C4 | Out-of-distribution detection | REQ-020, REQ-023 / RISK-003, RISK-004 |
| `src/models/inference.py` | C5, C6 | Inference + calibration + confidence | REQ-002, REQ-004, REQ-012 / RISK-007 |
| `src/evaluation/metrics.py` | C10 | Sensitivity/specificity/AUROC/ECE, subgroup | REQ-010, REQ-011, REQ-013 / RISK-004 |
| `src/evaluation/evaluate.py` | C10 | Evaluation runner (feeds V&V and PMS) | VV-001, KPI-001 |

## Notes
- Every third-party import is SOUP (SOUP-001); versions pinned in `requirements.txt`.
- Design decisions (gate-before-model ordering, calibrated risk band not binary verdict, disclaimer
  enforced at schema level) are specified in ARC-001 Section 8.
- Deployment/MLOps (GCP, Vertex AI) is described in DEP-001; infrastructure lives in `infra/`.
