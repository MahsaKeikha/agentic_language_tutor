"""Fail-closed governance for F167 Agentic Language Tutor."""

PROTECTED_ACTIONS = {
    "complete_assessed_work_for_learner",
    "impersonate_learner_or_contact_third_party",
    "publish_private_learning_data",
    "make_high_stakes_certification_decision",
    "override_learner_consent_or_preferences",
    "generate_deceptive_authorship_or_answer_leakage",
}

REQUIRED_REVIEWS = (
    "learner_level_reviewed",
    "lesson_goal_reviewed",
    "practice_quality_reviewed",
    "correction_quality_reviewed",
    "progress_evidence_reviewed",
    "accessibility_inclusion_reviewed",
    "privacy_integrity_reviewed",
    "learner_approval_reviewed",
)


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in PROTECTED_ACTIONS:
        return {"allowed": False, "reason": "assessed-work completion, impersonation, private-data publication, certification, consent override, or deceptive authorship is outside tutor authority"}
    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required language-tutoring review", "missing": missing}
    checks = {
        "level_assessment_gap": "material learner level, prerequisite, placement, confidence, or diagnostic uncertainty remains unresolved",
        "lesson_alignment_gap": "material lesson objective, sequence, difficulty, modality, cultural context, or learner-goal mismatch remains unresolved",
        "practice_quality_gap": "material exercise validity, answer quality, spacing, transfer, interaction, or difficulty issue remains unresolved",
        "correction_feedback_gap": "material grammar, vocabulary, pronunciation, usage, register, explanation, or feedback-quality issue remains unresolved",
        "progress_evidence_gap": "material mastery, retention, fluency, transfer, assessment validity, or progress-claim evidence remains unresolved",
        "accessibility_inclusion_gap": "material disability access, language variety, accent respect, cultural inclusion, age appropriateness, or usability issue remains unresolved",
        "privacy_integrity_risk": "material learner privacy, sensitive data, plagiarism, academic integrity, answer leakage, authorship, or consent concern remains unresolved",
        "provenance_approval_gap": "material source, lesson, exercise, correction, assessment, progress, revision, or learner-approval provenance is incomplete",
    }
    blockers = [message for key, message in checks.items() if context.get(key)]
    if blockers:
        return {"allowed": False, "reason": "language-tutoring governance blocker", "blockers": blockers}
    return {"allowed": True, "reason": "language-tutoring package approved for learner-controlled use"}


def review_required(action: str) -> bool:
    return action in PROTECTED_ACTIONS
