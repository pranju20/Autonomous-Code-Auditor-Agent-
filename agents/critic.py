from services.llm_service import generate_response


def validate_fix(state):
    original = state["code"]
    fixed = state["fixed_code"]

    prompt = f"""
    Compare original and fixed code.
    Is the bug fixed? Answer YES or NO only.
    Original:
    {original}

    Fixed:
    {fixed}
    """

    response = generate_response(prompt)

    if "YES" in response.upper():
        return {**state, "is_fixed": True}
    else:
        return {
            **state,
            "is_fixed": False,
            "retry_count": state.get("retry_count", 0) + 1,
        }
