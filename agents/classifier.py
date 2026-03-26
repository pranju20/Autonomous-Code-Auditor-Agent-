import code
import json
from agents.detector import extract_json
from services.llm_service import generate_response


def classify(state):
    bug = state["current_bug"]

    # prompt = f"""

    # Classify the following bug into a proper category and severity.

    # Choose category from:
    # - Runtime Error
    # - Logical Error
    # - Performance Issue
    # - Security Vulnerability
    # - Code Smell
    # - ZeroDivisionError

    # Choose severity from:
    # - Low
    # - Medium
    # - High
    # - Critical

    # Bug Explanation:
    # {bug.explanation}

    # Return output strictly in JSON:
    # {{
    #     "category": "",
    #     "severity": ""
    # }}
    # """

    prompt = f"""
You are a strict JSON generator.

Classify the bug.

Bug:
{bug.explanation}

Return ONLY valid JSON.
No explanation. No extra text.

Format:
{{
  "category": "Runtime Error | Logical Error | Performance Issue | Security Vulnerability | Code Smell | ZeroDivisionError",
  "severity": "Low | Medium | High | Critical"
}}
"""

    response = generate_response(prompt)

    try:
        cleaned = extract_json(response)
        data = json.loads(cleaned)
        bug.category = data.get("category", bug.category)
        bug.severity = data.get("severity", bug.severity)
    except Exception:
        # fallback if parsing fails
        pass

    return {**state, "current_bug": bug}
