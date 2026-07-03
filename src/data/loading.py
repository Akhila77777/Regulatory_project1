"""Dataset loading and splits (ARC-001 C10; offline).

SIMULATION / TRAINING EXERCISE. Scaffolding only. Not for clinical use.

Loads governed public datasets (HAM10000, ISIC, BCN20000, PH2) per DG-001/DSC-001. Must enforce
no lesion/patient leakage across train/validation/test splits and record dataset version for
reproducibility (REQ-041). Uses only public, licensed data; no real patient data.
"""

from typing import Any


def load_dataset(name: str, version: str) -> Any:
    """Load a governed dataset by name and version (DSC-001).

    TODO: implement. Scaffolding only.
    """
    raise NotImplementedError("Scaffolding only - not implemented.")


def make_splits(dataset: Any) -> Any:
    """Create train/validation/test splits with NO lesion/patient leakage (DG-001).

    TODO: implement. Scaffolding only.
    """
    raise NotImplementedError("Scaffolding only - not implemented.")
