from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Repository:
    name: str
    stargazers_count: int
    url: str
    created_at: datetime
    updated_at: datetime
    releases_count: int
    primary_language: Optional[str]
    merged_pull_requests: int
    closed_issues: int
    total_issues: int