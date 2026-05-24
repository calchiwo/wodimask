from .identity import Identity
from .context import Context, RiskProfile
from .policy import Policy
from .decision import RoutingDecision


class DecisionEngine:
    def __init__(self, policy: Policy):
        self.policy = policy

    def decide(self, identity: Identity, context: Context) -> RoutingDecision:
        rule = self.policy.rule_for_app(context.app)

        if rule:
            rotate = rule.rotate_ip or identity.requires_rotation()
            region = identity.region_intent or self.policy.preferred_region
            risk_flag = context.risk == RiskProfile.HIGH

            return RoutingDecision(
                profile=rule.profile,
                rotate_ip=rotate,
                region=region,
                log_level=rule.log_level,
                risk_flag=risk_flag,
            )

        return RoutingDecision(
            profile="default",
            rotate_ip=identity.requires_rotation(),
            region=self.policy.preferred_region,
            log_level="standard",
            risk_flag=context.risk == RiskProfile.HIGH,
        )