from fastapi import FastAPI
from services.audit_service import run_audit
from input_output.output_handler import format_output

app = FastAPI()


@app.post("/audit")
def audit(repo_path: str):
    result = run_audit(repo_path)
    return format_output(result)
