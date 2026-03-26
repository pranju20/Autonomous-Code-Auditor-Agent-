from pydantic import BaseModel
from typing import List, Optional
from schemas.bug_schema import Bug


class AuditState(BaseModel):
    code: str
    bugs: List[Bug] = []
    current_bug: Optional[Bug] = None
    fixed_code: Optional[str] = None
    is_fixed: bool = False
    retry_count: int = 0
    max_retries: int = 3
