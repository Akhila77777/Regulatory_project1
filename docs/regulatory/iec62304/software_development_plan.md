# Software Development Plan (IEC 62304)

> SIMULATION / TRAINING EXERCISE. DermaScan is a personal portfolio project, NOT a certified
> medical device. No real clinical use. Content is written in submission style for learning.

| Field | Value |
|---|---|
| Document ID | SDP-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Akhila N Pillai |
| Date | 2026-06-27 |
| Reviewed by | - |
| Approved by | - |

**Standard:** IEC 62304:2006+A1:2015 (clause 5.1). **Related:** SSC-001 (safety classification),
soup_list.md (SOUP-001), SRS-001, RMF-RA-001, CLS-001, traceability_matrix.md (TRC-001, pending).
**Study reference:** `steps/step-04-iec62304-software.html`.

---

## 1. Purpose and scope

This plan defines how DermaScan software is developed, maintained, and controlled in accordance with
IEC 62304. The rigour of the activities follows the software safety class determined in SSC-001
(**Class C**, see that document). The plan covers the inference application (model and FastAPI
service), its evaluation pipeline, and supporting tooling.

## 2. Lifecycle model

An incremental lifecycle is used: each increment progresses through requirements, design,
implementation, and verification, with risk management and configuration management running
continuously. This suits an iterative ML project where the model and the documentation co-evolve.

## 3. Development activities and deliverables (Class C)

| IEC 62304 clause | Activity | Deliverable |
|---|---|---|
| 5.2 | Software requirements analysis | SRS-001 (REQ-XXX), kept consistent with RMF-RA-001 |
| 5.3 | Software architectural design | architecture.md (components, interfaces, SOUP boundaries) |
| 5.4 | Software detailed design (required for Class C) | detailed design notes per software unit |
| 5.5 | Unit implementation and verification | source code + unit tests, acceptance criteria |
| 5.6 | Software integration and integration testing | integration test records |
| 5.7 | Software system testing | system test records mapped to REQ-XXX (TST-XXX) |
| 5.8 | Software release | release record, list of known anomalies and their evaluation |

## 4. Supporting processes (continuous)

| Process | Clause | Approach in this project |
|---|---|---|
| Risk management | 7 | Single integrated ISO 14971 file (RMF-*) also covers software risk and AI Act Art. 9 |
| Configuration management | 8 | Git version control; pinned dependencies in requirements.txt; the trained model artifact and dataset version are configuration items with recorded identifiers/hashes |
| Problem resolution | 9 | Issue tracker entries; root-cause and change assessment; link to CAPA in the QMS |
| Software maintenance | 6 | Change requests assessed for safety/risk impact before implementation; re-verification of affected items |

## 5. Configuration items

- Application source code (data, models, api, evaluation modules).
- Trained model artifact(s), identified by version and hash.
- Training/validation/test dataset versions (see dataset_card.md).
- SOUP components at pinned versions (soup_list.md).
- Documentation (this plan, SRS, risk file, etc.).

## 6. Tools and environment

- Language: Python. ML framework: **PyTorch** (chosen and used consistently across the project).
- Inference service: FastAPI (served via Uvicorn).
- All third-party components are recorded as SOUP (soup_list.md) with pinned versions in
  requirements.txt.
- Reproducibility: fixed random seeds, recorded environment, pinned dependency versions.

## 7. Verification and traceability strategy

Each REQ-XXX is verified by at least one TST-XXX. Risk controls (RMF-RA-001) trace to requirements
and tests. The bidirectional chain (need/risk to requirement to design to test) is recorded in
traceability_matrix.md (TRC-001). For Class C, detailed design and unit-level verification are
required and recorded.

## 8. ML-specific lifecycle considerations

IEC 62304 predates modern ML, so the following are added (guidance: AAMI CR34971, ISO/IEC 42001):
- The trained model and its training/validation data are treated as versioned configuration items
  with recorded lineage.
- Retraining is treated as a change (clause 6/9): assessed for risk impact, re-verified against the
  regression benchmark suite, and recalibrated. A predetermined change control plan (PCCP) is to be
  defined to pre-authorise bounded model updates.
- Non-determinism is controlled by seed fixing and pinned versions.

## 9. Change history

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-06-27 | Akhila N Pillai | Initial draft (simulation) |
