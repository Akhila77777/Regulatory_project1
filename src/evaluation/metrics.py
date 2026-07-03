"""Performance metrics (ARC-001 C10; offline).

SIMULATION / TRAINING EXERCISE. Scaffolding only. Not for clinical use.

Computes sensitivity, specificity, AUROC, calibration (ECE), and per-subgroup metrics
(REQ-010, REQ-011, REQ-012, REQ-013). Subgroup metrics operationalize the Fitzpatrick fairness
check (RISK-004). Never report a single aggregate accuracy figure as the claim (SRS-001, CLIN-001).
"""

from typing import Any, Dict


def sensitivity_specificity(y_true: Any, y_pred: Any, threshold: float) -> Dict[str, float]:
    """Return sensitivity and specificity at the operating threshold (REQ-010, REQ-011).

    TODO: implement. Scaffolding only.
    """
    raise NotImplementedError("Scaffolding only - not implemented.")


def auroc(y_true: Any, y_score: Any) -> float:
    """Return AUROC (REQ-011).

    TODO: implement. Scaffolding only.
    """
    raise NotImplementedError("Scaffolding only - not implemented.")


def expected_calibration_error(y_true: Any, y_prob: Any) -> float:
    """Return the expected calibration error (REQ-012, RISK-007).

    TODO: implement. Scaffolding only.
    """
    raise NotImplementedError("Scaffolding only - not implemented.")


def subgroup_metrics(y_true: Any, y_score: Any, subgroup_labels: Any) -> Dict[str, Dict[str, float]]:
    """Return metrics per subgroup (e.g. Fitzpatrick phototype) (REQ-013, RISK-004).

    TODO: implement. Scaffolding only.
    """
    raise NotImplementedError("Scaffolding only - not implemented.")
