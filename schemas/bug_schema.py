from pydantic import BaseModel, Field


class Bug(BaseModel):
    bug_type: str = Field(...)
    severity: str = "Medium"
    category: str = "General"
    file: str = "unknown"
    line: int = 0
    explanation: str
    fix: str = ""
    confidence: float = 0.5
