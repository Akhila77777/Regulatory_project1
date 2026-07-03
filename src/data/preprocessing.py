"""Input validation and image-quality gate (ARC-001 C2, C3).

SIMULATION / TRAINING EXERCISE. Scaffolding only. Not for clinical use.

Validates format/resolution (REQ-001), handles single-lesion constraint (REQ-003), and applies the
image-quality gate (REQ-021, RISK-003). Bad inputs must be rejected before reaching the model.
"""

from typing import Any


def validate_input(image_bytes: bytes) -> None:
    """Validate format and minimum resolution; reject unsupported/corrupt input (REQ-001).

    TODO: implement. Scaffolding only.
    """
    raise NotImplementedError("Scaffolding only - not implemented.")


def check_single_lesion(image: Any) -> None:
    """Confirm exactly one lesion; flag multi/no-lesion cases (REQ-003).

    TODO: implement. Scaffolding only.
    """
    raise NotImplementedError("Scaffolding only - not implemented.")


def quality_gate(image: Any) -> bool:
    """Check focus/framing/illumination; return False (reject/flag) on poor quality (REQ-021).

    TODO: implement. Scaffolding only.
    """
    raise NotImplementedError("Scaffolding only - not implemented.")


def preprocess(image: Any) -> Any:
    """Resize/normalize consistently with training (DG-001).

    TODO: implement. Scaffolding only.
    """
    raise NotImplementedError("Scaffolding only - not implemented.")
