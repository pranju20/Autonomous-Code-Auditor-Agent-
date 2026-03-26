from services.llm_service import generate_response
from utils.guardrails import sanitize_output


def fix_bug(state):
    code = state["code"]
    bug = state["current_bug"]

    prompt = f"""
    Fix this bug.

    Bug: {bug.bug_type}
    Explanation: {bug.explanation}

    Code:
    {code}

    Return only fixed code.
    """

    fixed_code = generate_response(prompt)
    fixed_code = sanitize_output(fixed_code)

    return {**state, "fixed_code": fixed_code}
