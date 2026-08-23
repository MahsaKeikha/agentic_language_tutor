from AGENTS import assessment_agent, correction_agent, lesson_agent, practice_agent, progress_agent
from safety.policy import authorize


def run(case: dict) -> dict:
    result = {
        "assessment": assessment_agent.run(case),
        "lesson": lesson_agent.run(case),
        "practice": practice_agent.run(case),
        "correction": correction_agent.run(case),
        "progress": progress_agent.run(case),
    }
    governance = authorize("release_language_tutoring_package", case.get("governance", {}))
    result["governance"] = governance
    result["released"] = governance["allowed"]
    return result
