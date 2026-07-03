"""Configuration and constants for DermaScan.

SIMULATION / TRAINING EXERCISE. Scaffolding only. Not for clinical use.
See ARC-001 (architecture) and IU-001 (intended use).
"""

# Mandatory disclaimer shown on EVERY output / API response.
# Enforced at the schema level so it cannot be omitted (REQ-030, RISK-005; IU-001 Section 11).
DISCLAIMER: str = (
    "Research/educational decision-support tool. This is not a diagnosis. The output must be "
    "independently confirmed by a qualified clinician and does not replace clinical judgement or "
    "histopathological examination."
)

# Supported input constraints (REQ-001; confirm exact values in SRS-001 / DSC-001).
SUPPORTED_IMAGE_FORMATS: tuple = ("JPEG", "PNG")  # TODO confirm against validated modality
MIN_IMAGE_RESOLUTION: tuple = (0, 0)  # TODO (width, height) placeholder

# Operating threshold and targets are placeholders; confirm against CLIN-001 before use.
OPERATING_THRESHOLD: float = 0.0  # TODO set on validation data only (never on the test set)

# Validated scope (IU-001). Empty until fixed from DSC-001 demographics.
VALIDATED_FITZPATRICK_RANGE: tuple = ()  # TODO e.g. ("I", "II", "III")


def load_config() -> dict:
    """Load runtime configuration (env/GCP Secret Manager per DEP-001).

    TODO: implement. Scaffolding only.
    """
    raise NotImplementedError("Scaffolding only - not implemented.")
