def format_output(result):
    bugs = result.get("bugs", [])

    return {
        "summary": {
            "total_bugs": len(bugs),
            "status": "fixed" if result.get("is_fixed") else "needs_review",
        },
        "bugs": [b.dict() for b in bugs],
        "fixed_code": result.get("fixed_code"),
    }
