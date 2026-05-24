from dataclasses import dataclass
from enum import Enum


class ExposureLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Stability(str, Enum):
    STABLE = "stable"
    ROTATING = "rotating"


@dataclass(frozen=True)
class Identity:
    mask_id: str
    exposure: ExposureLevel
    stability: Stability
    region_intent: str

    def requires_rotation(self) -> bool:
        return self.stability == Stability.ROTATING