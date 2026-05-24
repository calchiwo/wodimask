from dataclasses import dataclass


@dataclass(frozen=True)
class RoutingDecision:
    profile: str
    rotate_ip: bool
    region: str
    log_level: str
    risk_flag: bool