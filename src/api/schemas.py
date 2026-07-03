"""API request/response schemas (ARC-001 C1, C7).

SIMULATION / TRAINING EXERCISE. Scaffolding only. Not for clinical use.

The response schema enforces the mandatory disclaimer field (REQ-030) and a calibrated risk band
rather than a bare binary verdict (REQ-002, RISK-002). Confidence and warnings support human
oversight (REQ-004, REQ-022, REQ-032).
"""

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field

from src.common.config import DISCLAIMER


class RiskBand(str, Enum):
    """Calibrated risk band (not a binary diagnosis). REQ-002."""

    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    UNSUPPORTED = "unsupported_input"  # OOD / quality-gate rejection (REQ-020, REQ-021)


class InferenceResponse(BaseModel):
    """Response returned for every request. The disclaimer is required (REQ-030)."""

    risk_band: RiskBand
    malignancy_probability: Optional[float] = Field(
        default=None, description="Calibrated probability; None for unsupported input."
    )
    confidence: Optional[float] = Field(default=None, description="Model confidence (REQ-004).")
    low_confidence: bool = Field(default=False, description="Low-confidence flag (REQ-004).")
    warning: Optional[str] = Field(
        default=None, description="Low-confidence/OOD warning (REQ-022); not to be read as low risk."
    )
    disclaimer: str = Field(default=DISCLAIMER, description="Mandatory; must never be empty (REQ-030).")
    model_version: Optional[str] = None
    dataset_version: Optional[str] = None
