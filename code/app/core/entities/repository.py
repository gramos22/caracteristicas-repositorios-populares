from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Repository:
    name: str
    stargazer_count: int
    url: str
    created_at: datetime
    updated_at: datetime
    releases_count: int
    primary_language: Optional[str]
    merged_pull_requests: int
    closed_issues: int
    total_issues: int
    closed_issues_percentage: float

    def __post_init__(self):
        self.__calc_closed_issues_percentage()

    def __calc_closed_issues_percentage(self) -> None:
        if self.total_issues > 0:
            self.closed_issues_percentage = (self.closed_issues / self.total_issues) * 100
        else:
            self.closed_issues_percentage = 0.0