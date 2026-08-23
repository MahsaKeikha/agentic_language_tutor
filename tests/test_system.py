from orchestration.orchestrator import run
from safety.policy import PROTECTED_ACTIONS, REQUIRED_REVIEWS, authorize


def approved_context():
    return {key: True for key in REQUIRED_REVIEWS}


def test_orchestrator_runs_five_agents_and_fails_closed():
    result = run({})
    for key in ("assessment", "lesson", "practice", "correction", "progress"):
        assert key in result
    assert result["released"] is False


def test_missing_reviews_fail_closed():
    result = authorize("release_language_tutoring_package", {})
    assert result["allowed"] is False
    assert len(result["missing"]) == 8


def test_reviewed_package_can_release():
    assert authorize("release_language_tutoring_package", approved_context())["allowed"] is True


def test_level_gap_blocks():
    assert authorize("release_language_tutoring_package", approved_context() | {"level_assessment_gap": True})["allowed"] is False


def test_correction_gap_blocks():
    assert authorize("release_language_tutoring_package", approved_context() | {"correction_feedback_gap": True})["allowed"] is False


def test_progress_gap_blocks():
    assert authorize("release_language_tutoring_package", approved_context() | {"progress_evidence_gap": True})["allowed"] is False


def test_privacy_integrity_risk_blocks():
    assert authorize("release_language_tutoring_package", approved_context() | {"privacy_integrity_risk": True})["allowed"] is False


def test_protected_actions_never_autonomously_release():
    for action in PROTECTED_ACTIONS:
        assert authorize(action, approved_context())["allowed"] is False
