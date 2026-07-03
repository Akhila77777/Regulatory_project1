"""Inference, calibration, and confidence (ARC-001 C5, C6).

SIMULATION / TRAINING EXERCISE. Scaffolding only. Not for clinical use.

Produces a calibrated malignancy probability and confidence (REQ-002, REQ-004, REQ-012). Calibration
addresses RISK-007 (miscalibrated confidence). Determinism via fixed seeds / pinned versions (VV-001).
"""

from typing import Any, Tuple


def predict(model: Any, image: Any) -> float:
    """Return the raw malignancy score for a preprocessed image (REQ-002).

    TODO: implement. Scaffolding only.
    """
    raise NotImplementedError("Scaffolding only - not implemented.")


def calibrate(raw_score: float) -> float:
    """Map a raw score to a calibrated probability (REQ-012, RISK-007).

    Calibration parameters are fit on validation data only, never on the test set (VV-001).
    TODO: implement. Scaffolding only.
    """
    raise NotImplementedError("Scaffolding only - not implemented.")


def estimate_confidence(raw_score: float) -> Tuple[float, bool]:
    """Return (confidence, low_confidence_flag) (REQ-004).

    TODO: implement. Scaffolding only.
    """
    raise NotImplementedError("Scaffolding only - not implemented.")
