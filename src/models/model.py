"""Model definition (ARC-001 C5).

SIMULATION / TRAINING EXERCISE. Scaffolding only. Not for clinical use.

Defines the classification model (PyTorch, SOUP-001). The trained artifact and its dataset version
are configuration items (SDP-001) and are bound to every result (REQ-041). Related risk: RISK-001
(false negative is the priority harm).
"""

from typing import Any


def build_model() -> Any:
    """Construct the (untrained) model architecture.

    TODO: implement. Scaffolding only.
    """
    raise NotImplementedError("Scaffolding only - not implemented.")


def load_model(artifact_path: str) -> Any:
    """Load a versioned trained model artifact (Cloud Storage / Vertex AI per DEP-001).

    TODO: implement. Scaffolding only.
    """
    raise NotImplementedError("Scaffolding only - not implemented.")
