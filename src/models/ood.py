"""Out-of-distribution detection (ARC-001 C4).

SIMULATION / TRAINING EXERCISE. Scaffolding only. Not for clinical use.

Detects inputs outside the validated operating range and blocks scoring (REQ-020, REQ-023). Central
control for RISK-003 (OOD input scored as valid) and supports RISK-001/RISK-004. Verified by TST-012.
"""

from typing import Any


def is_out_of_distribution(image: Any) -> bool:
    """Return True if the input is OOD / unsupported and must not be scored (REQ-020).

    TODO: implement. Scaffolding only.
    """
    raise NotImplementedError("Scaffolding only - not implemented.")
