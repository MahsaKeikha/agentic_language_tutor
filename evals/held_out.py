"""Held-out governance scenarios for F167."""
from safety.policy import REQUIRED_REVIEWS, authorize


def base():
    return {key: True for key in REQUIRED_REVIEWS}


SCENARIOS = [
    ({}, False),
    (base(), True),
    (base() | {"level_assessment_gap": True}, False),
    (base() | {"lesson_alignment_gap": True}, False),
    (base() | {"practice_quality_gap": True}, False),
    (base() | {"correction_feedback_gap": True}, False),
    (base() | {"progress_evidence_gap": True}, False),
    (base() | {"accessibility_inclusion_gap": True}, False),
    (base() | {"privacy_integrity_risk": True}, False),
    (base() | {"provenance_approval_gap": True}, False),
]


def main():
    for index, (context, expected) in enumerate(SCENARIOS, 1):
        actual = authorize("release_language_tutoring_package", context)["allowed"]
        assert actual is expected, f"scenario {index}: expected {expected}, got {actual}"
    print(f"F167 held-out governance: {len(SCENARIOS)}/{len(SCENARIOS)} passed")


if __name__ == "__main__":
    main()
