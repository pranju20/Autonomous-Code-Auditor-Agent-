import json
import re
from services.llm_service import generate_response
from schemas.bug_schema import Bug


def extract_json(text: str):
    try:
        # direct parse
        return json.loads(text)
    except:
        pass

    # extract JSON block
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except:
            pass

    raise ValueError("No valid JSON found")


def detect(state):
    code = state["code"]

    prompt = f"""You are a strict JSON generator. Analyze the following Python code for bugs.

Code:
{code}

Return ONLY valid JSON. No explanation. No extra text. No markdown.

Format:
{{
  "bugs": [
    {{
      "bug_type": "string",
      "severity": "Low | Medium | High | Critical",
      "explanation": "string",
      "fix": "string",
      "line": 0,
      "confidence": 0.0
    }}
  ]
}}"""

    response = generate_response(prompt)

    print("RAW LLM RESPONSE:", response)
    try:
        cleaned = extract_json(response)
        print("CLEANED JSON:", cleaned)
        # Handle if extract_json already returns a dict
        if isinstance(cleaned, dict):
            data = cleaned
        else:
            data = json.loads(cleaned)
        # The LLM returns {"bugs": [...]} so get the first bug
        bugs_list = data.get("bugs", [data])  # fallback to data itself
        bug_dict = bugs_list[0] if bugs_list else data
        bug = Bug(**bug_dict)
    except Exception as e:
        print("JSON ERROR:", e)
        bug = Bug(bug_type="Parsing Error", explanation=str(response))

    return {**state, "bugs": [bug], "current_bug": bug}
    # try:
    #     cleaned = extract_json(response)
    #     print("CLEANED JSON:", cleaned)
    #     bug_dict = json.loads(cleaned)
    #     bug = Bug(**bug_dict)
    # except Exception as e:
    #     print("JSON ERROR:", e)
    #     bug = Bug(bug_type="Parsing Error", explanation=response)

    # return {**state, "bugs": [bug], "current_bug": bug}
