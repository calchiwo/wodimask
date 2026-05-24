from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class RiskProfile(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass(frozen=True)
class Context:
    app: str
    domain: str
    timestamp: datetime
    network: str
    risk: RiskProfile

    @property
    def hour(self) -> int:
        return self.timestamp.hour