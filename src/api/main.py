"""FastAPI inference service (ARC-001 C1, C7).

SIMULATION / TRAINING EXERCISE. Scaffolding only. Not for clinical use.

Enforces: authentication/authorization before any result (REQ-050), rate limiting (REQ-054),
single-lesion handling (REQ-003), and the mandatory disclaimer on every response (REQ-030).
Runtime ordering is gate-before-model (ARC-001 Section 4): validate -> quality gate -> OOD ->
inference -> calibrate -> format -> log.
"""

from fastapi import FastAPI

from src.api.schemas import InferenceResponse

app = FastAPI(title="DermaScan (SIMULATION - not a medical device)")


@app.get("/health")
def health() -> dict:
    """Liveness probe (supports availability KPI, KPI-001).

    TODO: implement. Scaffolding only.
    """
    raise NotImplementedError("Scaffolding only - not implemented.")


@app.post("/v1/assess", response_model=InferenceResponse)
def assess_lesion() -> InferenceResponse:
    """Assess a single pigmented-lesion image and return a calibrated risk band.

    Pipeline (ARC-001 Section 4):
      1. authenticate/authorize (REQ-050) and rate-limit (REQ-054)
      2. validate input + quality gate (REQ-001, REQ-003, REQ-021) -> preprocessing
      3. OOD check (REQ-020) -> models.ood
      4. inference + calibration + confidence (REQ-002, REQ-004, REQ-012) -> models.inference
      5. format response with disclaimer (REQ-030) -> schemas.InferenceResponse
      6. log event (REQ-040, REQ-041, REQ-042) -> common.logging

    No autonomous downstream action is taken (REQ-031); output is advisory only.
    TODO: implement. Scaffolding only.
    """
    raise NotImplementedError("Scaffolding only - not implemented.")
