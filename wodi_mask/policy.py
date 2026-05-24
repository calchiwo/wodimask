from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class PolicyRule:
    profile: str
    rotate_ip: bool
    log_level: str


class Policy:
    def __init__(self, preferred_region: str, rules: Dict[str, PolicyRule]):
        self.preferred_region = preferred_region
        self._rules = rules

    def rule_for_app(self, app: str) -> PolicyRule | None:
        return self._rules.get(app)

    @staticmethod
    def default() -> "Policy":
        return Policy(
            preferred_region="auto",
            rules={
                "api_testing": PolicyRule(
                    profile="clean-dev",
                    rotate_ip=True,
                    log_level="minimal",
                ),
                "github": PolicyRule(
                    profile="stable-clean",
                    rotate_ip=False,
                    log_level="standard",
                ),
                "browsing": PolicyRule(
                    profile="high-anon",
                    rotate_ip=True,
                    log_level="minimal",
                ),
            },
        )