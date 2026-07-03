"""Test stubs mapped to the V&V test specifications (VV-TS-001).

SIMULATION / TRAINING EXERCISE. Scaffolding only. Tests are skipped until src/ is implemented.
Each stub names the TST it will realize and the REQ/RISK it verifies. See VV-001 and TRC-001.
"""

import pytest

pytestmark = pytest.mark.skip(reason="Scaffolding only - implementation pending (VV-001).")


def test_input_validation():
    """TST-001 -> REQ-001: valid accepted, invalid/corrupt rejected with reason."""
    raise NotImplementedError


def test_risk_band_not_binary():
    """TST-002 -> REQ-002 (RISK-002): output is a risk band, never a bare verdict."""
    raise NotImplementedError


def test_disclaimer_on_every_response():
    """TST-004 -> REQ-030 (RISK-005): disclaimer present on all responses incl. errors/OOD."""
    raise NotImplementedError


def test_ood_rejection():
    """TST-012 -> REQ-020 (RISK-003): OOD inputs not scored; unsupported-input notice returned."""
    raise NotImplementedError


def test_no_autonomous_action():
    """TST-031 -> REQ-031 (RISK-005): output is advisory; no autonomous downstream action."""
    raise NotImplementedError


def test_logging_and_version_binding():
    """TST-040 -> REQ-040/041 (RISK-006): event logged with model/dataset version + input hash."""
    raise NotImplementedError


def test_auth_and_security():
    """TST-023 -> REQ-050/053/042 (RISK-010): auth enforced; data encrypted; logs tamper-evident."""
    raise NotImplementedError
