def validate_input(code: str):
    if not code or len(code.strip()) == 0:
        raise ValueError("Empty code input")

    if len(code) > 20000:
        raise ValueError("Code too large")

    return True


def sanitize_output(text: str):
    # remove unwanted tokens
    return text.strip()
