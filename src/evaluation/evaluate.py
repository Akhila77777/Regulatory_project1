"""Evaluation runner (ARC-001 C10; offline).

SIMULATION / TRAINING EXERCISE. Scaffolding only. Not for clinical use.

Runs the independent-test-set evaluation that produces V&V evidence (VV-001, TST-018/019/020) and
feeds the post-market KPI dashboard (KPI-001). Acts as the evaluation gate in the MLOps pipeline
(DEP-001 Section 4): fails the build if acceptance criteria or subgroup-fairness thresholds are not
met. Must not tune anything on the test set (VV-001).
"""

from typing import Any, Dict


def evaluate_model(model: Any, test_set: Any) -> Dict[str, Any]:
    """Compute the full metric set (overall + subgroup) and return a results record.

    TODO: implement. Scaffolding only.
    """
    raise NotImplementedError("Scaffolding only - not implemented.")


def passes_release_criteria(results: Dict[str, Any]) -> bool:
    """Return True only if all acceptance criteria (SRS-001, CLIN-001) are met, incl. subgroups.

    TODO: implement. Scaffolding only.
    """
    raise NotImplementedError("Scaffolding only - not implemented.")
